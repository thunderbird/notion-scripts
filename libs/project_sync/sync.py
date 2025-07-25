# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Synchronizer for a project-based sync between Notion and Bugzilla."""

import logging
import re
import notion_client
import datetime
import dataclasses

from collections import defaultdict
from functools import cached_property

from copy import deepcopy
from notion_client.helpers import iterate_paginated_api

from .. import notion_data as p
from ..notion_data import CustomNotionToMarkdown, NotionDatabase
from ..util import getnestedattr, RetryingClient, diff_dataclasses, strip_orgname

from .common import IssueRef

logger = logging.getLogger("project_sync")


class ProjectSync:
    """This is a project-based sync between Notion and an external issue tracker like GitHub or Bugzilla.

    The authoritative source for milestones is in Notion, while the source for Tasks is in the
    tracker. This enables engineers to work in the tracker, while allowing managers to look at the
    high level in Notion. See README.md for more info.
    """

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
        tasks_notion_prefix="",
        sprints_merge_by_name=False,
        dry=False,
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
            tasks_notion_prefix (str): Optional prefix for Notion tasks synchronized from the issue
                tracker.
            sprints_merge_by_name (bool): If a sprint does not exist, find an existing one by name
                and merge it
            dry (bool): If true, only query operations are done. Mutations are disabled for both
                the issue tracker and Notion.
        """
        self.notion = notion_client.Client(auth=notion_token, client=RetryingClient())
        self.tracker = tracker

        # Milestones Database
        milestones_properties = [
            # There are more, but this is the only one we change
            p.link(self.propnames["notion_issue_field"]),
        ]
        self.milestones_db = NotionDatabase(milestones_id, self.notion, milestones_properties, dry=dry)
        if not self.milestones_db.validate_props():
            raise Exception("Milestone schema failed to validate")
        self.milestones_body_sync = milestones_body_sync
        self.milestones_body_sync_if_empty = milestones_body_sync_if_empty
        self.milestones_tracker_prefix = milestones_tracker_prefix
        self.milestones_extra_label = milestones_extra_label

        # Tasks Properties
        tasks_properties = [
            p.relation(self.propnames["notion_tasks_milestone_relation"], milestones_id, True),
            p.title(self.propnames["notion_tasks_title"]),
            p.link(self.propnames["notion_issue_field"]),
        ]

        self._setup_prop(
            tasks_properties, "notion_tasks_priority", "select", self.propnames["notion_tasks_priority_values"]
        )
        self._setup_prop(tasks_properties, "notion_tasks_assignee", "people")
        self._setup_prop(tasks_properties, "notion_tasks_review_url", "link")
        self._setup_prop(tasks_properties, "notion_tasks_text_assignee", "rich_text_space_set")
        self._setup_prop(tasks_properties, "notion_tasks_labels", "multi_select", self.tracker.get_all_labels())
        self._setup_prop(
            tasks_properties, "notion_tasks_repository", "select", strip_orgname(self.tracker.get_all_repositories())
        )
        self._setup_date_prop(tasks_properties, "notion_tasks_dates")
        self._setup_date_prop(tasks_properties, "notion_tasks_openclose")

        # Sprint Database
        if sprint_id:
            tasks_properties.append(p.relation(self.propnames["notion_tasks_sprint_relation"], sprint_id, True))

            sprint_properties = [
                p.rich_text(self.propnames["notion_sprint_tracker_id"]),
                p.title(self.propnames["notion_sprint_title"]),
                p.status(self.propnames["notion_sprint_status"]),
                p.dates(self.propnames["notion_sprint_dates"]),
            ]

            self.sprint_db = NotionDatabase(sprint_id, self.notion, sprint_properties, dry=dry)
        else:
            self.sprint_db = None

        # Tasks Database
        self.tasks_db = NotionDatabase(tasks_id, self.notion, tasks_properties, dry=dry)
        if not self.tasks_db.validate_props():
            raise Exception("Tasks schema failed to validate")
        self.tasks_body_sync = tasks_body_sync
        self.tasks_notion_prefix = tasks_notion_prefix

        # Other settings
        self.dry = dry
        self.sprints_merge_by_name = sprints_merge_by_name
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

    def _setup_prop(self, properties, key_name, type_name, *extra_args):
        if prop := self.propnames[key_name]:
            typefunc = getattr(p, type_name)
            properties.append(typefunc(prop, *extra_args))

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

    def _discover_notion_issues(self, notion_db_id):
        repos = defaultdict(dict)

        for block in iterate_paginated_api(
            self.notion.databases.query,
            database_id=notion_db_id,
            filter={
                "property": self.propnames["notion_issue_field"],
                "rich_text": {"is_not_empty": True},
            },
        ):
            url = self._get_prop(block, "notion_issue_field")

            ref = self.tracker.parse_issueref(url)

            if ref and self.tracker.is_repo_allowed(ref.repo):
                repos[ref.repo][ref.id] = block

        return repos

    @cached_property
    def _all_sprint_pages(self):
        return self.sprint_db.get_all_pages()

    @cached_property
    def _sprint_pages_by_id(self):
        sprintmap = {}

        for page in self._all_sprint_pages:
            sprint_ids = self._get_richtext_prop(page, "notion_sprint_tracker_id", "").split("\n")
            for sprint_id in sprint_ids:
                sprintmap[sprint_id] = page

        return sprintmap

    @cached_property
    def _sprint_pages_by_title(self):
        return {
            content: page
            for page in self._all_sprint_pages
            if (content := self._get_richtext_prop(page, "notion_sprint_title"))
        }

    @cached_property
    def _notion_milestone_issues(self):
        return self._discover_notion_issues(self.milestones_db.database_id)

    @cached_property
    def _notion_tasks_issues(self):
        return self._discover_notion_issues(self.tasks_db.database_id)

    def _get_task_notion_data(self, tracker_issue, parent_milestone_ids=[], old_page=None):
        # Base data
        title = self.tracker.notion_tasks_title(self.tasks_notion_prefix, tracker_issue)
        notion_data = {
            self.propnames["notion_tasks_title"]: title,
            self.propnames["notion_issue_field"]: tracker_issue.url,
        }

        # Assignees
        assignees = [user.notion_user for user in tracker_issue.assignees if user.notion_user is not None]
        text_assignees = [user.tracker_user for user in tracker_issue.assignees]

        self._set_if_prop(notion_data, "notion_tasks_assignee", assignees or None)
        self._set_if_prop(notion_data, "notion_tasks_text_assignee", " ".join(text_assignees))

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
        self._set_if_prop(notion_data, "notion_tasks_review_url", tracker_issue.review_url or None)

        # Start/end dates
        if tracker_issue.sprint:
            self._set_if_date_prop(
                notion_data, "notion_tasks_dates", tracker_issue.sprint.start_date, tracker_issue.sprint.end_date
            )
        elif tracker_issue.start_date or tracker_issue.end_date:
            self._set_if_date_prop(notion_data, "notion_tasks_dates", tracker_issue.start_date, tracker_issue.end_date)
        else:
            self._set_if_date_prop(notion_data, "notion_tasks_dates", None)

        # Open/close dates
        self._set_if_date_prop(
            notion_data, "notion_tasks_openclose", tracker_issue.created_date, tracker_issue.closed_date
        )

        # Sprints
        if self.sprint_db:
            sprint_id = getnestedattr(lambda: tracker_issue.sprint.id, None)
            notion_sprint = self._sprint_pages_by_id.get(sprint_id, None)
            if notion_sprint:
                notion_data[self.propnames["notion_tasks_sprint_relation"]] = [notion_sprint["id"]]
            else:
                notion_data[self.propnames["notion_tasks_sprint_relation"]] = []

        # Milestone relation
        notion_data[self.propnames["notion_tasks_milestone_relation"]] = parent_milestone_ids

        return notion_data

    def _update_timestamp(self, database, timestamp):
        if self.dry:
            return

        timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
        pattern = re.escape(self.LAST_SYNC_MESSAGE.format(self.project_key, "REGEX_PLACEHOLDER"))
        pattern = pattern.replace("REGEX_PLACEHOLDER", r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")

        description, count = re.subn(
            pattern, self.LAST_SYNC_MESSAGE.format(self.project_key, timestamp), database.description
        )

        if count < 1:
            description = self.LAST_SYNC_MESSAGE.format(self.project_key, timestamp) + "\n\n" + description

        database.description = description

    def synchronize_sprints(self):
        """Synchronize sprints from the tracker to Notion."""
        for sprint in self.tracker.get_sprints():
            idprop = self.propnames["notion_sprint_tracker_id"]

            notion_data = {
                self.propnames["notion_sprint_title"]: sprint.name,
                self.propnames["notion_sprint_dates"]: {"start": sprint.start_date, "end": sprint.end_date},
                self.propnames["notion_sprint_status"]: sprint.status,
            }

            if sprint.id in self._sprint_pages_by_id:
                page = self._sprint_pages_by_id[sprint.id]
                changed = self.sprint_db.update_page(page, notion_data)
                if changed:
                    logger.info(
                        f"Updating Sprint {sprint.id} ({sprint.name}) - {sprint.start_date} to {sprint.end_date}"
                    )
                else:
                    logger.info(
                        f"Unchanged Sprint {sprint.id} ({sprint.name}) - {sprint.start_date} to {sprint.end_date}"
                    )
            elif self.sprints_merge_by_name and sprint.name in self._sprint_pages_by_title:
                page = self._sprint_pages_by_title[sprint.name]
                page_tracker_ids = self._get_richtext_prop(page, "notion_sprint_tracker_id", "").split("\n")
                page_dates = self._get_prop(page, "notion_sprint_dates", safe=False)
                logger.info(
                    f"Merging Sprint {sprint.id} with {','.join(page_tracker_ids)} {sprint.name} - {sprint.start_date} to {sprint.end_date}"
                )
                if page_dates["start"] != sprint.start_date.isoformat():
                    raise Exception(
                        f"Could not merge sprint {sprint.name}, start dates mismatch! {page_dates['start']} != {sprint.start_date.isoformat()}"
                    )
                if page_dates["end"] != sprint.end_date.isoformat():
                    raise Exception(
                        f"Could not merge sprint {sprint.name}, end dates mismatch! {page_dates['end']} != {sprint.end_date.isoformat()}"
                    )

                page_tracker_ids.append(sprint.id)
                self.sprint_db.update_page(page, {idprop: "\n".join(page_tracker_ids)})
                self._sprint_pages_by_id[sprint.id] = page
            else:
                logger.info(f"Creating Sprint {sprint.name} - {sprint.start_date} to {sprint.end_date}")
                notion_data[idprop] = sprint.id
                page = self.sprint_db.create_page(notion_data)
                self._sprint_pages_by_id[sprint.id] = page

    def _find_task_parents(self, tracker_issue):
        found_milestone_parents = [
            milestone_parent["id"]
            for parent in tracker_issue.parents
            if (
                milestone_parent := getnestedattr(
                    lambda: self._notion_milestone_issues[parent.repo][parent.id],
                    None,
                )
            )
            is not None
        ]

        return found_milestone_parents

    def synchronize_single_task(self, tracker_issue, page=None):
        """Synchronize a single tracker issue to Notion.

        Args:
            tracker_issue (Issue): tracker issue
            page (dict): The Notion page object of the existing task in notion. Leave out to add
                instead of update.
        """
        notion_data = self._get_task_notion_data(
            tracker_issue=tracker_issue, parent_milestone_ids=self._find_task_parents(tracker_issue), old_page=page
        )

        if page:
            changed = self.tasks_db.update_page(page, notion_data)
            if changed:
                logger.info(f"Updating task {tracker_issue.repo}#{tracker_issue.id} - {tracker_issue.title}")
                logger.info("\t" + str(notion_data))
            else:
                logger.info(f"Unchanged task {tracker_issue.repo}#{tracker_issue.id} - {tracker_issue.title}")
        else:
            logger.info(f"Adding new task {tracker_issue.id} - {tracker_issue.title}")
            logger.debug("\t" + str(notion_data))
            page = self.tasks_db.create_page(notion_data)

            if not self.tasks_body_sync and self.TASK_BODY_WARNING:
                # At least show the warning if not the full body
                self.tasks_db.replace_page_contents(page["id"], self.TASK_BODY_WARNING.format(self.tracker.name))

        if self.tasks_body_sync:
            body = tracker_issue.description
            if self.TASK_BODY_WARNING:
                body = self.TASK_BODY_WARNING.format(self.tracker.name) + "\n\n" + body

            self.tasks_db.replace_page_contents(page["id"], body)

    def synchronize_single_milestone(self, tracker_issue, page):
        """Synchronize a single Notion milestone to the issue tracker.

        Args:
            tracker_issue (Issue): Issue that is being updated
            page (dict): The Notion page object of the milestone in notion.
        """
        # Body
        body = tracker_issue.description
        if self.milestones_body_sync or (self.milestones_body_sync_if_empty and not len(tracker_issue.description)):
            blocks = self.milestones_db.get_page_contents(page["id"])
            converter = CustomNotionToMarkdown(self.notion, strip_images=True, tracker=self.tracker)
            body = converter.convert(blocks)

        # Assignees. Community assignees should be kept on the issue so a sync doesn't remove them.
        community_assignees = {assignee for assignee in tracker_issue.assignees if assignee.notion_user is None}
        milestone_assignees = {
            self.tracker.new_user(notion_user=assignee["id"])
            for assignee in self._get_prop(page, "notion_milestones_assignee", [])
        }

        title = self._get_richtext_prop(page, "notion_milestones_title", "")
        labels = set(tracker_issue.labels)
        if self.milestones_extra_label:
            labels.add(self.milestones_extra_label)

        start_date_str, end_date_str = self._get_date_prop(page, "notion_milestones_dates")

        new_issue = dataclasses.replace(
            tracker_issue,
            title=self.milestones_tracker_prefix + title,
            labels=labels,
            description=body,
            state=(self._get_prop(page, "notion_milestones_status") or {}).get("name"),
            priority=(self._get_prop(page, "notion_milestones_priority") or {}).get("name"),
            assignees=community_assignees.union(milestone_assignees),
            notion_url=page.get("url", ""),
            start_date=datetime.date.fromisoformat(start_date_str) if start_date_str else None,
            end_date=datetime.date.fromisoformat(end_date_str) if end_date_str else None,
        )

        if tracker_issue != new_issue:
            logger.info(
                f"Updating milestone {tracker_issue.id} - {tracker_issue.title} ({tracker_issue.url} / {new_issue.notion_url})"
            )
            diff_dataclasses(tracker_issue, new_issue, log=logger.debug)

            if not self.dry:
                self.tracker.update_milestone_issue(tracker_issue, new_issue)
        else:
            logger.info(
                f"Unchanged milestone {tracker_issue.id} - {tracker_issue.title} ({tracker_issue.url} / {new_issue.notion_url})"
            )

    def synchronize(self):
        """Synchronize all the things!"""
        timestamp = datetime.datetime.now(datetime.UTC)

        milestone_issues = self._notion_milestone_issues
        tasks_issues = self._notion_tasks_issues
        collected_tasks = deepcopy(tasks_issues)

        # Synchronize sprints (if enabled)
        if self.sprint_db:
            logger.info(f"Synchronizing sprints to {self.sprint_db}")
            self.synchronize_sprints()

        # Synchronize issues found in milestones
        for reporef, issues in milestone_issues.items():
            refs = [IssueRef(id=issue, repo=reporef) for issue in issues.keys()]

            tracker_issues = self.tracker.get_issues_by_number(refs, True)
            logger.info(f"Synchronizing {len(issues)} milestones for {reporef}")

            # Update the tracker issue from milestone data
            for issue in issues.keys():
                tracker_issue = tracker_issues[issue]
                notion_page = issues[issue]

                self.synchronize_single_milestone(tracker_issue, notion_page)

                # For each sub-issue in the tracker milestone, make sure we have a notion task
                for subissue in tracker_issue.sub_issues:
                    if subissue.id not in collected_tasks[subissue.repo]:
                        collected_tasks[subissue.repo][subissue.id] = None

        # Any additional tasks the tracker might be interested in (e.g. sprint boards)
        self.tracker.collect_additional_tasks(collected_tasks)

        # Synchronize individual and above collected tasks
        for reporef, issue_pages in collected_tasks.items():
            refs = [IssueRef(id=issue, repo=reporef) for issue in issue_pages.keys()]

            tracker_issues = self.tracker.get_issues_by_number(refs)
            logger.info(f"Synchronizing {len(tracker_issues)} tasks for {reporef}")

            for issue_id, issue in tracker_issues.items():
                self.synchronize_single_task(issue, issue_pages[issue_id])

        # Update the description with the last updated timestamp
        self._update_timestamp(self.milestones_db, timestamp)
        self._update_timestamp(self.tasks_db, timestamp)
        if self.sprint_db:
            self._update_timestamp(self.sprint_db, timestamp)


def synchronize(**kwargs):  # pragma: no cover
    """Exported method to begin synchronization."""
    ProjectSync(**kwargs).synchronize()
