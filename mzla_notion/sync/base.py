# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Synchronizer for a project-based sync between Notion and Bugzilla."""

import logging
import asyncio
import re
import notion_client
import datetime

from collections import defaultdict
from functools import cached_property

from notion_client.helpers import async_iterate_paginated_api

from .. import notion_data as p
from ..notion_data import NotionDatabase
from ..util import getnestedattr, AsyncRetryingClient, ensure_datetime

logger = logging.getLogger("project_sync")


class BaseSync:
    """Base class for project and label sync."""

    TASK_BODY_WARNING = "ℹ️ _This task synchronizes with {0}. Any changes you make here will be overwritten._"
    LAST_SYNC_MESSAGE = "Last Issue Tracker Sync ({0}): {1}"

    def __init__(
        self,
        project_key,
        notion_token,
        tracker,
        milestones_id,
        tasks_id,
        sprint_id=None,
        milestones_body_sync=False,
        milestones_body_sync_if_empty=False,
        tasks_body_sync=False,
        milestones_tracker_prefix="",
        milestones_extra_label="",
        milestones_issue_type=None,
        tasks_notion_prefix="",
        team_id=None,
        team_association=None,
        dry=False,
        synchronous=False,
    ):
        """Set up the project sync.

        Args:
            project_key (str): The identifying project key
            notion_token (str): The Notion client token
            tracker (IssueTracker): The issue tracker
            milestones_id (str): The Notion database id for the "Milestones" database
            tasks_id (str): The Notion database id for the "Tasks" database
            sprint_id (str): The Notion database id for the "Sprints" database. Leave out to disable
                sprint syncing.
            milestones_body_sync (bool): If true, the Notion page body will always be synchronized
                to the issue tracker. Note this takes a lot of requests, so recommend avoiding
            milestones_body_sync_if_empty (bool): If true, the Notion page body will be synchronized
                to the tracker, but only if the tracker issue is empty. This works great for a one
                time import.
            tasks_body_sync (bool): If true, the issue body will be synced to Notion tasks.
                Note this takes a lot of requests, so recommend avoiding.
            milestones_tracker_prefix (str): Optional prefix on the issue tracker when synchronized
                from milestones.
            milestones_extra_label (str): Optional label for GitHub issues synchronized from
                milestones.
            milestones_issue_type (str): Optional issue type for GitHub issues synchronized from
                milestones.
            tasks_notion_prefix (str): Optional prefix for Notion tasks synchronized from the issue
                tracker.
            team_id (str): The Notion database id for the "Teams" database. Optional, used with the team property.
            team_association (str): The id of the team for this sync. Optional, used with notion_tasks_team property.
            dry (bool): If true, only query operations are done. Mutations are disabled for both
                the issue tracker and Notion.
            synchronous (bool): If true, run any async tasks sequentially.
        """
        self.notion = notion_client.AsyncClient(auth=notion_token, client=AsyncRetryingClient(http2=True))
        self.tracker = tracker

        # Milestones Database
        milestones_properties = [
            # There are more, but this is the only one we change
            p.link(self.propnames["notion_issue_field"]),
        ]
        self.milestones_db = NotionDatabase(milestones_id, self.notion, milestones_properties, dry=dry)
        self.milestones_body_sync = milestones_body_sync
        self.milestones_body_sync_if_empty = milestones_body_sync_if_empty
        self.milestones_tracker_prefix = milestones_tracker_prefix
        self.milestones_extra_label = milestones_extra_label
        self.milestones_issue_type = milestones_issue_type

        # Tasks Properties
        tasks_properties = [
            p.relation(self.propnames["notion_tasks_milestone_relation"], milestones_id, True),
            p.title(self.propnames["notion_tasks_title"]),
            p.files(self.propnames["notion_issue_field"]),
        ]

        if team_id:
            self._setup_prop(tasks_properties, "notion_tasks_team", "relation", team_id, False)
            self._setup_prop(milestones_properties, "notion_milestones_team", "relation", team_id, False)

        self._setup_prop(tasks_properties, "notion_tasks_priority", "select")
        self._setup_prop(tasks_properties, "notion_tasks_assignee", "people")
        self._setup_prop(tasks_properties, "notion_tasks_review_url", "files")
        self._setup_prop(tasks_properties, "notion_tasks_text_assignee", "rich_text_space_set")
        self._setup_prop(tasks_properties, "notion_tasks_repository", "select", unknown="skip")
        self._setup_prop(tasks_properties, "notion_tasks_labels", "multi_select", unknown="skip")

        self._setup_prop(tasks_properties, "notion_tasks_whiteboard", "rich_text")
        self._setup_date_prop(tasks_properties, "notion_tasks_dates")
        self._setup_date_prop(tasks_properties, "notion_tasks_openclose")

        # Sprint Database
        if sprint_id:
            tasks_properties.append(p.relation(self.propnames["notion_tasks_sprint_relation"], sprint_id, True))

            sprint_properties = [
                p.title(self.propnames["notion_sprint_title"]),
                p.status(self.propnames["notion_sprint_status"]),
                p.dates(self.propnames["notion_sprint_dates"]),
            ]

            self.sprint_db = NotionDatabase(sprint_id, self.notion, sprint_properties, dry=dry)
        else:
            self.sprint_db = None

        # Tasks Database
        self.tasks_db = NotionDatabase(tasks_id, self.notion, tasks_properties, dry=dry)
        self.tasks_body_sync = tasks_body_sync
        self.tasks_notion_prefix = tasks_notion_prefix

        # Other settings
        self.team = team_association
        self.dry = dry
        self.synchronous = synchronous
        self.project_key = project_key

    @property
    def propnames(self):
        """Get the property names from the tracker."""
        return self.tracker.property_names

    def _get_prop(self, block_or_page, key_name, default=None, safe=True):
        if safe:
            prop = getnestedattr(lambda: block_or_page["properties"][self.propnames[key_name]], default)
            return getnestedattr(lambda: prop[prop["type"]], default) if prop else default
        else:
            prop = block_or_page["properties"][self.propnames[key_name]]
            return prop[prop["type"]]

    def _setup_date_prop(self, properties, key_name):
        if prop := self.propnames[key_name]:
            if isinstance(prop, list):
                properties.append(p.date(prop[0]))
                properties.append(p.date(prop[1]))
            else:
                properties.append(p.dates(prop))

    def _setup_prop(self, properties, key_name, type_name, *extra_args, **extra_kwargs):
        if prop := self.propnames[key_name]:
            typefunc = getattr(p, type_name)
            properties.append(typefunc(prop, *extra_args, **extra_kwargs))

    def _get_date_prop(self, block_or_page, key_name, default=None):
        propinfo = self.propnames[key_name]
        if isinstance(propinfo, list):
            start_prop_name, end_prop_name = propinfo
            start_prop_key = end_prop_key = "start"
        else:
            start_prop_name = end_prop_name = propinfo
            start_prop_key = "start"
            end_prop_key = "end"

        start_prop = getnestedattr(lambda: block_or_page["properties"][start_prop_name], default)
        end_prop = getnestedattr(lambda: block_or_page["properties"][end_prop_name], default)

        return (
            getnestedattr(lambda: start_prop[start_prop["type"]][start_prop_key], default),
            getnestedattr(lambda: end_prop[end_prop["type"]][end_prop_key], default),
        )

    def _get_richtext_prop(self, block_or_page, key_name, default=None):
        prop = self._get_prop(block_or_page, key_name, default)

        if prop:
            return "".join(map(lambda rich_text: rich_text["plain_text"], prop))
        else:
            return default

    def _set_if_prop(self, obj, key_name, value):
        if propname := self.propnames[key_name]:
            obj[propname] = value

    def _set_if_date_prop(self, obj, key_name, start=None, end=None):
        if propname := self.propnames[key_name]:
            if isinstance(propname, list):
                obj[propname[0]] = start if start else None
                obj[propname[1]] = end if end else None
            else:
                obj[propname] = {"start": start, "end": end} if start or end else None

    async def _discover_notion_issues(self, notion_db_id, filter_team=None, filter_issue_type="url"):
        repos = defaultdict(dict)

        query_filter = {
            "property": self.propnames["notion_issue_field"],
            filter_issue_type: {"is_not_empty": True},
        }

        if filter_team and self.team:
            query_filter = {
                "and": [
                    {"property": filter_team, "relation": {"contains": self.team}},
                    query_filter,
                ]
            }

        async for block in async_iterate_paginated_api(
            self.notion.databases.query,
            database_id=notion_db_id,
            filter=query_filter,
        ):
            url = self._get_prop(block, "notion_issue_field")

            # Issue field is either a URL or files field
            if isinstance(url, list):
                url = url[0]["external"]["url"]

            ref = self.tracker.parse_issueref(url)

            if ref and self.tracker.is_repo_allowed(ref.repo):
                repos[ref.repo][ref.id] = block

        return repos

    @cached_property
    def _sprint_pages_by_title(self):
        return {
            content: page
            for page in self._all_sprint_pages
            if (content := self._get_richtext_prop(page, "notion_sprint_title"))
        }

    async def _get_task_notion_data(self, tracker_issue, parent_milestone_ids=[], old_page=None):
        # Base data
        title = self.tracker.notion_tasks_title(self.tasks_notion_prefix, tracker_issue)
        notion_data = {
            self.propnames["notion_tasks_title"]: title,
            self.propnames["notion_issue_field"]: [
                {"url": tracker_issue.url, "name": self.tracker.format_issueref_short(tracker_issue)}
            ],
        }

        # Assignees
        assignees = [user.notion_user for user in tracker_issue.assignees if user.notion_user is not None]
        text_assignees = [user.tracker_user for user in tracker_issue.assignees]

        self._set_if_prop(notion_data, "notion_tasks_assignee", assignees or None)
        self._set_if_prop(notion_data, "notion_tasks_text_assignee", " ".join(text_assignees))

        if self.team and self.propnames.get("notion_tasks_team"):
            teams = getnestedattr(lambda: self._get_prop(old_page, "notion_tasks_team"), None)
            teams = {team["id"].replace("-", "") for team in (teams or [])}
            teams.add(self.team)
            self._set_if_prop(notion_data, "notion_tasks_team", list(teams))

        # Status and Priority
        self._set_if_prop(notion_data, "notion_tasks_priority", tracker_issue.priority)

        final_status = tracker_issue.state
        if not tracker_issue.state:
            # If we don't have a state, we just have opened/closed. Change if there is a transition.
            if old_page:
                old_status = getnestedattr(lambda: self._get_prop(old_page, "notion_tasks_status")["name"], None)
                if old_status in self.propnames["notion_closed_states"] and not tracker_issue.closed_date:
                    # If the existing page is closed and we have no closed date, open it
                    final_status = self.propnames["notion_default_open_state"]
                elif old_status not in self.propnames["notion_closed_states"] and tracker_issue.closed_date:
                    # If the existing page is open and we have a closed date, close it
                    final_status = self.propnames["notion_closed_states"][0]
                else:
                    # Otherwise keep whatever status we had
                    final_status = old_status
            else:
                # Adjust the open/closed state based on if we have a closed date
                if tracker_issue.closed_date:
                    final_status = self.propnames["notion_closed_states"][0]
                else:
                    final_status = self.propnames["notion_default_open_state"]

        self._set_if_prop(notion_data, "notion_tasks_status", final_status)

        # Review URL
        review_url = None
        if tracker_issue.review_url:
            review_url = [
                {"name": self.tracker.format_patchref_short(tracker_issue.review_url), "url": tracker_issue.review_url}
            ]
        self._set_if_prop(notion_data, "notion_tasks_review_url", review_url)

        # Labels and Whiteboard
        self._set_if_prop(notion_data, "notion_tasks_labels", tracker_issue.labels or [])
        self._set_if_prop(notion_data, "notion_tasks_whiteboard", tracker_issue.whiteboard)

        # Repository
        repomap = self.propnames.get("notion_tasks_repository_map") or {}
        repo = repomap.get(tracker_issue.repo) or tracker_issue.repo
        self._set_if_prop(notion_data, "notion_tasks_repository", repo)

        # Start/end dates
        old_planned_start, old_planned_target = getnestedattr(
            lambda: self._get_date_prop(old_page, "notion_tasks_planned_dates"), (None, None)
        )
        utc_min = datetime.datetime.min.replace(tzinfo=datetime.timezone.utc)
        if tracker_issue.sprint:
            final_start = tracker_issue.sprint.start_date
            final_end = tracker_issue.sprint.end_date
        elif tracker_issue.start_date or tracker_issue.end_date:
            # TODO we should probably only use datetime for comparison, and then a normal date.
            # Some get added as "2025-04-01T00:00:00+00:00"
            final_start = max(
                ensure_datetime(tracker_issue.start_date) or utc_min,
                ensure_datetime(tracker_issue.created_date),
                ensure_datetime(old_planned_start) or utc_min,
            )
            final_end = tracker_issue.end_date or tracker_issue.closed_date
        elif final_status in self.propnames["notion_closed_states"]:
            # No dates set otherwise, and the issue is closed
            final_start = max(tracker_issue.created_date, old_planned_start or utc_min)
            final_end = tracker_issue.closed_date
        else:
            final_start = None
            final_end = None

        if final_start and final_end and ensure_datetime(final_start) > ensure_datetime(final_end):
            logger.warn(f"Issue {tracker_issue.url} ends before it starts ({final_start} – {final_end})")
            final_end = final_start

        self._set_if_date_prop(notion_data, "notion_tasks_dates", final_start, final_end)

        # Open/close dates
        self._set_if_date_prop(
            notion_data, "notion_tasks_openclose", tracker_issue.created_date, tracker_issue.closed_date
        )

        # Sprints
        if self.sprint_db:
            sprint_name = getnestedattr(lambda: tracker_issue.sprint.name, None)
            notion_sprint = self._sprint_pages_by_title.get(sprint_name)

            if notion_sprint:
                notion_data[self.propnames["notion_tasks_sprint_relation"]] = [notion_sprint["id"]]
            else:
                notion_data[self.propnames["notion_tasks_sprint_relation"]] = []

        # Milestone relation
        notion_data[self.propnames["notion_tasks_milestone_relation"]] = parent_milestone_ids

        return notion_data

    async def _update_timestamp(self, database, timestamp):
        if self.dry:
            return

        timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
        pattern = re.escape(self.LAST_SYNC_MESSAGE.format(self.project_key, "REGEX_PLACEHOLDER"))
        pattern = pattern.replace("REGEX_PLACEHOLDER", r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")

        description, count = re.subn(
            pattern, self.LAST_SYNC_MESSAGE.format(self.project_key, timestamp), await database.get_description()
        )

        if count < 1:
            description = self.LAST_SYNC_MESSAGE.format(self.project_key, timestamp) + "\n\n" + description

        await database.set_description(description)

    async def synchronize_single_task(self, tracker_issue, page=None):
        """Synchronize a single tracker issue to Notion.

        Args:
            tracker_issue (Issue): tracker issue
            page (dict): The Notion page object of the existing task in notion. Leave out to add
                instead of update.
        """
        parents = self._find_task_parents(tracker_issue)
        notion_data = await self._get_task_notion_data(
            tracker_issue=tracker_issue, parent_milestone_ids=parents, old_page=page
        )

        if page:
            changed = await self.tasks_db.update_page(page, notion_data)
            if changed:
                logger.info(f"Updating task {tracker_issue.repo}#{tracker_issue.id} - {tracker_issue.title}")
                logger.info("\t" + str(notion_data))
            else:
                logger.info(f"Unchanged task {tracker_issue.repo}#{tracker_issue.id} - {tracker_issue.title}")
        else:
            logger.info(f"Adding new task {tracker_issue.id} - {tracker_issue.title}")
            logger.debug("\t" + str(notion_data))
            page = await self.tasks_db.create_page(notion_data)

            if not self.tasks_body_sync and self.TASK_BODY_WARNING:
                # At least show the warning if not the full body
                await self.tasks_db.replace_page_contents(page["id"], self.TASK_BODY_WARNING.format(self.tracker.name))

        if self.tasks_body_sync:
            body = tracker_issue.description
            if self.TASK_BODY_WARNING:
                body = self.TASK_BODY_WARNING.format(self.tracker.name) + "\n\n" + body

            await self.tasks_db.replace_page_contents(page["id"], body)

    async def _async_init(self):
        async with asyncio.TaskGroup() as tg:
            valid_milestones = tg.create_task(self.milestones_db.validate_props())
            valid_tasks = tg.create_task(self.tasks_db.validate_props())

            tasks_issues = tg.create_task(
                self._discover_notion_issues(
                    self.tasks_db.database_id, self.propnames["notion_tasks_team"], filter_issue_type="files"
                )
            )

            if self.sprint_db:
                sprint_pages = tg.create_task(self.sprint_db.get_all_pages())

        if not valid_milestones.result():
            raise Exception("Milestone schema failed to validate")
        if not valid_tasks.result():
            raise Exception("Tasks schema failed to validate")

        self._notion_tasks_issues = tasks_issues.result()

        if self.sprint_db:
            self._all_sprint_pages = sprint_pages.result()
