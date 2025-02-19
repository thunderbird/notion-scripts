# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Synchronizer for a project-based sync between Notion and GitHub."""

import logging
import re
from collections import defaultdict
from datetime import datetime, date, timedelta
from functools import cached_property

from copy import deepcopy
from notion_client import Client
from notion_client.helpers import iterate_paginated_api

from libs.notion_data import NotionDatabase

from . import ghhelper
from . import notion_data as p
from .util import getnestedattr
from .notion_data import CustomNotionToMarkdown

logger = logging.getLogger("gh_project_sync")


class ProjectSync:
    """This is a project-based sync between Notion and GitHub.

    The authoritative source for milestones is in Notion, while the source for Tasks is in GitHub.
    This enables engineers to work in GitHub, while allowing managers to look at the high level in
    Notion. See README.md for more info.
    """

    TASK_BODY_WARNING = "ℹ️ _This issue synchronizes from GitHub. Any changes you make here will be overwritten._"
    LAST_SYNC_MESSAGE = "Last GitHub Sync: {0}"

    # In order to make Notion field names configurable we have a mapping from a static key to the
    # Notion field name. These defaults will be overwritten by the field config
    DEFAULT_PROPERTY_NAMES = {
        "notion_tasks_title": "Task name",
        "notion_tasks_assignee": "Owner",
        "notion_tasks_text_assignee": "GitHub Assignee",
        "notion_tasks_dates": "Dates",
        "notion_tasks_priority": "Priority",
        "notion_tasks_milestone_relation": "Project",
        "notion_tasks_sprint_relation": "Sprint",
        "notion_milestones_title": "Project",
        "notion_milestones_assignee": "Owner",
        "notion_milestones_priority": "Priority",
        "notion_milestones_status": "Status",
        "notion_milestones_dates": "Dates",
        "notion_github_issue": "GitHub Issue",
        "notion_sprint_github_id": "GitHub ID",
        "notion_sprint_title": "Sprint name",
        "notion_sprint_status": "Sprint status",
        "notion_sprint_dates": "Dates",
        # Some default states and values
        "notion_tasks_priority_values": ["P1", "P2", "P3"],
        "notion_tasks_open_state": "Backlog",
        "notion_tasks_closed_state": "Done",
    }

    GITHUB_PROJECT_TASKS_FIELDS = ["Status", "Priority", "Sprint"]
    GITHUB_PROJECT_MILESTONE_FIELDS = [
        "Status",
        "Priority",
        "Start Date",
        "Target Date",
    ]

    def __init__(
        self,
        notion_token,
        milestones_id,
        tasks_id,
        milestones_project_id,
        tasks_project_id,
        sprint_id=None,
        milestones_body_sync=False,
        milestones_body_sync_if_empty=True,
        tasks_body_sync=True,
        allowed_repositories=None,
        milestones_github_prefix="",
        tasks_notion_prefix="",
        user_map={},
        property_names={},
        dry=False,
    ):
        """Set up the project sync.

        Args:
            notion_token (str): The Notion client token
            milestones_id (str): The Notion database id for the "Milestones" database
            tasks_id (str): The Notion database id for the "Tasks" database
            milestones_project_id (str): The id of the GitHub Project to sync with milestones
                database
            tasks_project_id (str): The id of the GitHub project to sync with the tasks database
            sprint_id (str): The Notion database id for the "Sprints" database. Leave out to disable
                sprint syncing.
            milestones_body_sync (bool): If true, the Notion page body will always be synchronized
                to GitHub. Note this takes a lot of requests, so recommend avoiding
            milestones_body_sync_if_empty (bool): If true, the Notion page body will be synchronized
                to GitHub, but only if the GitHub issue is empty. This works great for a one time import.
            tasks_body_sync (bool): If true, the github issue body will be synced to Notion tasks.
                Note this takes a lot of requests, so recommend avoiding.
            allowed_repositories (list[str]): List of orgname/repo with those repostories for which
                GitHub links should be followed. Avoids mistakes when linking external issues.
            milestones_github_prefix (str): Optional prefix for GitHub issues synchronized from
                milestones.
            tasks_notion_prefix (str): Optional prefix for Notion tasks synchronized from GitHub
                issues.
            user_map (dict[str,str]): Mapping from a GitHub username to a Notion user id, to allow
                translating mentions between the two platforms.
            property_names (dict[str,str]): Allows adjusting the Notion property names. See
                DEFAULT_PROPERTY_NAMES for the defaults.
            dry (bool): If true, only query operations are done. Mutations are disabled for both
                GitHub and Notion.
        """
        self.notion = Client(auth=notion_token)
        self.propnames = {**self.DEFAULT_PROPERTY_NAMES, **property_names}

        # Milestones Database
        self.milestones_db = NotionDatabase(milestones_id, self.notion, dry=dry)
        self.milestones_project_id = milestones_project_id
        self.milestones_body_sync = milestones_body_sync
        self.milestones_body_sync_if_empty = milestones_body_sync_if_empty
        self.milestones_github_prefix = milestones_github_prefix

        # Tasks Properties
        tasks_properties = [
            p.relation(self.propnames["notion_tasks_milestone_relation"], milestones_id, True),
            p.title(self.propnames["notion_tasks_title"]),
            p.people(self.propnames["notion_tasks_assignee"]),
            p.dates(self.propnames["notion_tasks_dates"]),
            p.link(self.propnames["notion_github_issue"]),
            p.rich_text(self.propnames["notion_tasks_text_assignee"]),
            p.select(self.propnames["notion_tasks_priority"], self.propnames["notion_tasks_priority_values"]),
        ]

        # Sprint Database
        if sprint_id:
            tasks_properties.append(p.relation(self.propnames["notion_tasks_sprint_relation"], sprint_id, True))

            sprint_properties = [
                p.rich_text(self.propnames["notion_sprint_github_id"]),
                p.title(self.propnames["notion_sprint_title"]),
                p.status(self.propnames["notion_sprint_status"]),
                p.dates(self.propnames["notion_sprint_dates"]),
            ]

            self.sprint_db = NotionDatabase(sprint_id, self.notion, sprint_properties, dry=dry)
        else:
            self.sprint_db = None

        # Tasks Database
        self.tasks_db = NotionDatabase(tasks_id, self.notion, tasks_properties, dry=dry)
        self.tasks_project_id = tasks_project_id
        self.tasks_body_sync = tasks_body_sync
        self.tasks_notion_prefix = tasks_notion_prefix

        # Other settings
        self.allowed_repositories = allowed_repositories
        self.user_map = ghhelper.UserMap(user_map)
        self.dry = dry

    def _is_repo_allowed(self, org=None, repo=None, orgrepo=None):
        """Checks if the repository is permitted for synchronization."""
        if orgrepo:
            return not self.allowed_repositories or orgrepo in self.allowed_repositories
        elif org and repo:
            return not self.allowed_repositories or f"{org}/{repo}" in self.allowed_repositories
        else:
            raise Exception("Must specify either org/repo or orgrepo")

    def _get_prop(self, block_or_page, key_name, default=None, safe=True):
        if safe:
            prop = getnestedattr(lambda: block_or_page["properties"][self.propnames[key_name]], default)
            return getnestedattr(lambda: prop[prop["type"]], default) if prop else default
        else:
            prop = block_or_page["properties"][self.propnames[key_name]]
            return prop[prop["type"]]

    def _get_richtext_prop(self, block_or_page, key_name, default=None):
        prop = self._get_prop(block_or_page, key_name)

        if prop:
            return "".join(map(lambda rich_text: rich_text["plain_text"], prop))
        else:
            return default

    def _discover_notion_issues(self, notion_db_id, org=None, repos=None):
        repos = defaultdict(dict)

        for block in iterate_paginated_api(
            self.notion.databases.query,
            database_id=notion_db_id,
            filter={
                "property": self.propnames["notion_github_issue"],
                "rich_text": {"is_not_empty": True},
            },
        ):
            url = self._get_prop(block, "notion_github_issue")

            parts = url.split("/")
            if parts[2] == "github.com" and parts[5] == "issues" and self._is_repo_allowed(parts[3], parts[4]):
                repo = parts[3] + "/" + parts[4]
                issue = int(parts[6])
                repos[repo][issue] = block

        return repos

    @cached_property
    def _sprint_pages(self):
        return {
            content: page
            for page in self.sprint_db.get_all_pages()
            if (content := self._get_richtext_prop(page, "notion_sprint_github_id"))
        }

    @cached_property
    def _notion_milestone_issues(self):
        return self._discover_notion_issues(self.milestones_db.database_id)

    @cached_property
    def _notion_tasks_issues(self):
        return self._discover_notion_issues(self.tasks_db.database_id)

    @cached_property
    def _github_tasks_project(self):
        return ghhelper.GitHubProjectV2(self.tasks_project_id, self.GITHUB_PROJECT_TASKS_FIELDS)

    @cached_property
    def _github_milestones_project(self):
        return ghhelper.GitHubProjectV2(self.milestones_project_id, self.GITHUB_PROJECT_MILESTONE_FIELDS)

    def _get_task_notion_data(self, github_issue, milestone_id):
        # Base data
        gh_assignee = " ".join(a.login for a in github_issue.assignees.nodes) if github_issue.assignees.nodes else ""

        notion_data = {
            "GitHub Assignee": gh_assignee,
            self.propnames["notion_tasks_title"]: self.tasks_notion_prefix + github_issue.title,
            self.propnames["notion_github_issue"]: github_issue.url,
        }

        # Assignees
        assignees = self.user_map.map(
            lambda assignee: self.user_map.gh_to_notion(assignee.login), github_issue.assignees.nodes
        )
        if len(assignees) and self.propnames["notion_tasks_assignee"]:
            notion_data[self.propnames["notion_tasks_assignee"]] = assignees

        # Project item
        gh_project_item = self._github_tasks_project.find_project_item(
            github_issue, self._github_tasks_project.database_id
        )
        if gh_project_item:
            # Dates
            start_date = getnestedattr(lambda: gh_project_item.start_date, None)
            end_date = getnestedattr(lambda: gh_project_item.end_date, None)
            if start_date or end_date:
                notion_data[self.propnames["notion_tasks_dates"]] = {"start": start_date, "end": end_date}
            elif getattr(gh_project_item, "sprint", None):
                end_date = gh_project_item.sprint.start_date + timedelta(days=gh_project_item.sprint.duration - 1)
                notion_data[self.propnames["notion_tasks_dates"]] = {
                    "start": gh_project_item.sprint.start_date,
                    "end": end_date,
                }
            else:
                notion_data[self.propnames["notion_tasks_dates"]] = None

            # Priority and Status
            notion_data["Priority"] = getnestedattr(lambda: gh_project_item.priority.name, None)
            status = getnestedattr(lambda: gh_project_item.status.name, self.propnames["notion_tasks_open_state"])
            notion_data["Status"] = status

            # Sprint Relation
            if self.sprint_db:
                iteration_id = getnestedattr(lambda: gh_project_item.sprint.iteration_id, None)
                notion_sprint = self._sprint_pages.get(iteration_id, None)
                if notion_sprint:
                    notion_data[self.propnames["notion_tasks_sprint_relation"]] = [notion_sprint["id"]]
                else:
                    notion_data[self.propnames["notion_tasks_sprint_relation"]] = []
        else:
            notion_data["Status"] = (
                self.propnames["notion_tasks_closed_state"]
                if github_issue.state == "CLOSED"
                else self.propnames["notion_tasks_open_state"]
            )

        # Milestone relation
        if milestone_id:
            notion_data[self.propnames["notion_tasks_milestone_relation"]] = [milestone_id]
        else:
            notion_data[self.propnames["notion_tasks_milestone_relation"]] = []

        return notion_data

    def _update_timestamp(self, database, timestamp=None):
        if self.dry:
            return

        if not timestamp:
            timestamp = datetime.utcnow()

        timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
        pattern = re.escape(self.LAST_SYNC_MESSAGE.format("REGEX_PLACEHOLDER"))
        pattern = pattern.replace("REGEX_PLACEHOLDER", r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")

        description, count = re.subn(pattern, self.LAST_SYNC_MESSAGE.format(timestamp), database.description)

        if count < 1:
            description = self.LAST_SYNC_MESSAGE.format(timestamp) + "\n\n" + description

        database.description = description

    def synchronize_sprints(self, sprint_field):
        """Synchronize sprints from GitHub to Notion.

        Args:
            sprint_field (ProjectV2IterationField): The GitHub GraphQL response with the sprint field.
        """

        def process_iteration(sprint, status):
            end_date = sprint.start_date + timedelta(days=sprint.duration - 1)

            notion_data = {
                self.propnames["notion_sprint_github_id"]: sprint.id,
                self.propnames["notion_sprint_title"]: sprint.title,
                self.propnames["notion_sprint_dates"]: {"start": sprint.start_date, "end": end_date},
                self.propnames["notion_sprint_status"]: status,
            }

            if sprint.id in self._sprint_pages:
                page = self._sprint_pages[sprint.id]
                logger.info(f"Updating Sprint {sprint.title} - {sprint.start_date} to {end_date}")
                self.sprint_db.update_page(page, notion_data)
            else:
                logger.info(f"Creating Sprint {sprint.title} - {sprint.start_date} to {end_date}")
                self.sprint_db.create_page(notion_data)

        if not self.sprint_db:
            return

        today = date.today()

        for sprint in sprint_field.configuration.iterations:
            process_iteration(sprint, "Future" if sprint.start_date > today else "Current")

        for sprint in sprint_field.configuration.completed_iterations:
            process_iteration(sprint, "Past")

    def synchronize_single_task(self, github_issue, page=None):
        """Synchronize a single GitHub issue to Notion.

        Args:
            github_issue (Issue): GraphQL Issue from GitHub
            page (dict): The Notion page object of the existing task in notion. Leave out to add
                instead of update.
        """
        orgrepo = getnestedattr(lambda: github_issue.parent.repository.name_with_owner, None)
        parent = getnestedattr(
            lambda: self._notion_milestone_issues[orgrepo][github_issue.parent.number]["id"],
            None,
        )

        notion_data = self._get_task_notion_data(github_issue=github_issue, milestone_id=parent)

        if page:
            logger.info(f"Updating task {github_issue.number} - {github_issue.title}")
            self.tasks_db.update_page(page, notion_data)
        else:
            logger.info(f"Adding new task {github_issue.number} - {github_issue.title}")
            page = self.tasks_db.create_page(notion_data)

            if not self.tasks_body_sync and self.TASK_BODY_WARNING:
                # At least show the warning if not the full body
                self.tasks_db.replace_page_contents(page["id"], self.TASK_BODY_WARNING)

        if self.tasks_body_sync:
            if self.TASK_BODY_WARNING:
                body = self.TASK_BODY_WARNING + "\n\n" + github_issue.body
            else:
                body = github_issue.body
            self.tasks_db.replace_page_contents(page["id"], body)

    def synchronize_single_milestone(self, github_issue, page):
        """Synchronize a single Notion milestone to GitHub.

        Args:
            github_issue (Issue): GraphQL Issue from GitHub to synchronize with.
            page (dict): The Notion page object of the milestone in notion.
        """
        logger.info(f"Updating milestone {github_issue.number} - {github_issue.title}")
        if self.dry:
            return

        # Update the issue itself
        body = None
        if self.milestones_body_sync or (self.milestones_body_sync_if_empty and not len(github_issue.body)):
            blocks = self.milestones_db.get_page_contents(page["id"])
            converter = CustomNotionToMarkdown(self.notion, strip_images=True, user_map=self.user_map)
            body = converter.convert(blocks)

        title = self._get_richtext_prop(page, "notion_milestones_title", "")
        ghhelper.update_issue(
            github_issue,
            {
                "title": self.milestones_github_prefix + title,
                "status": self._get_prop(page, "notion_milestones_status", {}).get("name"),
                "body": body,
            },
        )

        # Assignees use a different endpoint, do them next
        assignees = self.user_map.map(
            lambda person: self.user_map.notion_to_dbid(person["id"]), self._get_prop(page, "notion_tasks_assignee", [])
        )
        ghhelper.update_assignees(github_issue, assignees)

        # Finally the GitHub ProjectV2 with the planning properties
        self._github_milestones_project.update_project_for_issue(
            github_issue,
            {
                "start_date": self._get_prop(page, "notion_milestones_dates", {}).get("start"),
                "target_date": self._get_prop(page, "notion_milestones_dates", {}).get("end"),
                "priority": self._get_prop(page, "notion_milestones_priority", {}).get("name"),
                "status": self._get_prop(page, "notion_milestones_status", {}).get("name"),
            },
            add=True,
        )

    def synchronize(self):
        """Synchronize all the things!"""
        timestamp = datetime.utcnow()
        collected_tasks = deepcopy(self._notion_tasks_issues)

        # Synchronize sprints (if enabled)
        self.synchronize_sprints(self._github_tasks_project.field("sprint"))

        # Synchronize issues found in milestones
        for orgrepo, issues in self._notion_milestone_issues.items():
            org, repo = orgrepo.split("/")

            if not self._is_repo_allowed(org, repo):
                continue

            github_issues = ghhelper.get_issues_by_number(org, repo, issues.keys(), True)
            logger.info(f"Synchronizing {len(github_issues)} milestones for {orgrepo}")

            # Update the GitHub issue from milestone data
            for issue in issues.keys():
                github_issue = github_issues[issue]
                notion_page = issues[issue]

                self.synchronize_single_milestone(github_issue, notion_page)

                # For each sub-issue in the epic, make sure we have a notion task
                for subissue in github_issue.sub_issues.nodes:
                    if subissue.number not in collected_tasks[orgrepo]:
                        collected_tasks[orgrepo][subissue.number] = None

        # Collect issues from sprint board, there may be a few not associated with a milestone
        # We'll sync them in the next loop
        project_item_count = 0
        for issue_info in self._github_tasks_project.get_issue_numbers():
            orgrepo = issue_info.repository.name_with_owner
            if self._is_repo_allowed(orgrepo=orgrepo) and issue_info.number not in collected_tasks[orgrepo]:
                collected_tasks[orgrepo][issue_info.number] = None
                project_item_count += 1

        logger.info(f"Will sync {project_item_count} new sprint board tasks not associated with a milestone")

        # Synchronize individual and above collected tasks
        for orgrepo, issue_pages in collected_tasks.items():
            org, repo = orgrepo.split("/")

            if not self._is_repo_allowed(org, repo):
                continue

            github_issues = ghhelper.get_issues_by_number(org, repo, issue_pages.keys())
            logger.info(f"Synchronizing {len(github_issues)} tasks for {orgrepo}")

            for number, issue in github_issues.items():
                self.synchronize_single_task(github_issues[number], issue_pages[number])

        # Update the description with the last updated timestamp
        self._update_timestamp(self.milestones_db, timestamp)
        self._update_timestamp(self.tasks_db, timestamp)

    def setup(self):
        """Verify the Notion/GitHub setup. Note this is not yet implemented."""
        # TODO This is incomplete, but a setup validation is a lot of work
        self.milestones_db.update_props()
        self.tasks_db.update_props()

        if self.sprint_db:
            self.sprint_db.update_props()


def synchronize(**kwargs):
    """Exported method to begin synchronization."""
    ProjectSync(**kwargs).synchronize()
