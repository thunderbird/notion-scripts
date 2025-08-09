import logging
import datetime
import dataclasses
import asyncio

from copy import deepcopy

from .base import BaseSync

from ..tracker.common import IssueRef
from ..util import diff_dataclasses

from ..notion_data import CustomNotionToMarkdown

logger = logging.getLogger("project_sync")


class ProjectSync(BaseSync):
    """This is a project-based sync between Notion and an external issue tracker like GitHub or Bugzilla.

    The authoritative source for milestones is in Notion, while the source for Tasks is in the
    tracker. This enables engineers to work in the tracker, while allowing managers to look at the
    high level in Notion. See README.md for more info.
    """

    async def _async_init(self):
        async with asyncio.TaskGroup() as tg:
            tg.create_task(super()._async_init())
            milestones_issues = tg.create_task(self._discover_notion_issues(self.milestones_db.database_id))

        self._notion_milestone_issues = milestones_issues.result()

    def _find_task_parents(self, tracker_issue):
        milestone_issues = self._notion_milestone_issues

        found_milestone_parents = [
            milestone_parent["id"]
            for parent in tracker_issue.parents
            if (milestone_parent := milestone_issues.get(parent.repo, {}).get(parent.id, None)) is not None
        ]

        return found_milestone_parents

    async def synchronize_single_milestone(self, tracker_issue, page):
        """Synchronize a single Notion milestone to the issue tracker.

        Args:
            tracker_issue (Issue): Issue that is being updated
            page (dict): The Notion page object of the milestone in notion.
        """
        # Body
        body = tracker_issue.description
        if self.milestones_body_sync or (self.milestones_body_sync_if_empty and not len(tracker_issue.description)):
            blocks = await self.milestones_db.get_page_contents(page["id"])
            converter = CustomNotionToMarkdown(self.notion, strip_images=True, tracker=self.tracker)
            body = await converter.convert(blocks)

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
                await self.tracker.update_milestone_issue(tracker_issue, new_issue)
        else:
            logger.info(
                f"Unchanged milestone {tracker_issue.id} - {tracker_issue.title} ({tracker_issue.url} / {new_issue.notion_url})"
            )

    async def synchronize(self):
        """Synchronize all the things!"""
        await self._async_init()

        timestamp = datetime.datetime.now(datetime.UTC)
        collected_tasks = deepcopy(self._notion_tasks_issues)

        async with asyncio.TaskGroup() as tg:
            # Synchronize sprints (if enabled)
            if self.sprint_db:
                logger.info(f"Synchronizing sprints to {self.sprint_db}")
                tg.create_task(self.synchronize_sprints())

            # Synchronize issues found in milestones
            for reporef, issues in self._notion_milestone_issues.items():
                refs = [IssueRef(id=issue, repo=reporef) for issue in issues.keys()]

                tracker_issues = await self.tracker.get_issues_by_number(refs, True)
                logger.info(f"Synchronizing {len(issues)} milestones for {reporef}")

                # Update the tracker issue from milestone data
                for issue in issues.keys():
                    tracker_issue = tracker_issues[issue]
                    notion_page = issues[issue]

                    tg.create_task(self.synchronize_single_milestone(tracker_issue, notion_page))

                    # For each sub-issue in the tracker milestone, make sure we have a notion task
                    for subissue in tracker_issue.sub_issues:
                        if subissue.id not in collected_tasks[subissue.repo]:
                            collected_tasks[subissue.repo][subissue.id] = None

            # Any additional tasks the tracker might be interested in (e.g. sprint boards)
            self.tracker.collect_additional_tasks(collected_tasks)

            # Synchronize individual and above collected tasks
            for reporef, issue_pages in collected_tasks.items():
                refs = [IssueRef(id=issue, repo=reporef) for issue in issue_pages.keys()]

                tracker_issues = await self.tracker.get_issues_by_number(refs)
                logger.info(f"Synchronizing {len(tracker_issues)} tasks for {reporef}")

                for issue_id, issue in tracker_issues.items():
                    tg.create_task(self.synchronize_single_task(issue, issue_pages[issue_id]))

        async with asyncio.TaskGroup() as tg:
            # Update the description with the last updated timestamp
            tg.create_task(self._update_timestamp(self.milestones_db, timestamp))
            tg.create_task(self._update_timestamp(self.tasks_db, timestamp))
            if self.sprint_db:
                tg.create_task(self._update_timestamp(self.sprint_db, timestamp))

        await self.notion.aclose()


async def synchronize(**kwargs):  # pragma: no cover
    """Exported method to begin synchronization."""
    await ProjectSync(**kwargs).synchronize()
