import logging
import datetime
import dataclasses
import asyncio

from copy import deepcopy

from .base import BaseSync

from ..tracker.common import IssueRef
from ..util import diff_dataclasses, ensure_datetime, ensure_date, from_isoformat

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
            milestones_issues = tg.create_task(
                self._discover_notion_issues(self.milestones_db.database_id, self.propnames["notion_milestones_team"])
            )

        self._notion_milestone_issues = milestones_issues.result()

    def _find_task_parents(self, tracker_issue):
        milestone_issues = self._notion_milestone_issues

        found_milestone_parents = [
            milestone_parent["id"]
            for parent in tracker_issue.parents
            if (milestone_parent := milestone_issues.get(parent.repo, {}).get(parent.id, None)) is not None
        ]

        return found_milestone_parents

    async def create_single_milestone(self, tracker_issue):
        """Create a milestone in Notion from the issue tracker.

        Args:
            tracker_issue (Issue): Issue to create from
        """
        # Base data
        notion_data = {
            self.propnames["notion_milestones_title"]: tracker_issue.title,
            self.propnames["notion_issue_field"]: tracker_issue.url,
        }

        # Assignees
        assignees = [user.notion_user for user in tracker_issue.assignees if user.notion_user is not None]
        self._set_if_prop(notion_data, "notion_milestones_assignee", assignees or None)

        if not assignees:
            # No assignees we know of in Notion, which probably means this one isn't relevant for
            # project management.
            # TODO decide how this feels
            # return
            pass

        # Team
        self._set_if_prop(notion_data, "notion_milestones_team", [self.team] if self.team else None)

        # Priority
        self._set_if_prop(notion_data, "notion_milestones_priority", tracker_issue.priority)

        # Status
        final_status = tracker_issue.state
        if tracker_issue.closed_date:
            logger.info(
                f"Skip creating milestone {tracker_issue.id} - {tracker_issue.title} ({tracker_issue.url}) because it is already closed"
            )
            return
        else:
            final_status = self.propnames["notion_default_open_state"]
        self._set_if_prop(notion_data, "notion_milestones_status", final_status)

        # Dates
        utc_min = datetime.datetime.min.replace(tzinfo=datetime.timezone.utc)
        if tracker_issue.start_date or tracker_issue.end_date:
            final_start = max(
                ensure_datetime(tracker_issue.start_date) or utc_min, ensure_datetime(tracker_issue.created_date)
            )
            final_end = tracker_issue.end_date or tracker_issue.closed_date
        else:
            final_start = None
            final_end = None

        self._set_if_date_prop(notion_data, "notion_milestones_dates", ensure_date(final_start), ensure_date(final_end))

        # TODO labels
        # TODO body

        logger.debug(notion_data)
        page = await self.milestones_db.create_page(notion_data)
        logger.info(
            f"Creating milestone {tracker_issue.id} - {tracker_issue.title} ({tracker_issue.url} / {page.get('url')})"
        )

        if not self.dry:
            await self.synchronize_single_milestone(tracker_issue, page, skip_unchanged_msg=True)

    async def synchronize_single_milestone(self, tracker_issue, page, skip_unchanged_msg=False):
        """Synchronize a single Notion milestone to the issue tracker.

        Args:
            tracker_issue (Issue): Issue that is being updated
            page (dict): The Notion page object of the milestone in notion.
            skip_unchanged_msg (bool): Skip the "Unchanged milestone" log message (for creating).
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
            start_date=ensure_date(from_isoformat(start_date_str)) if start_date_str else None,
            end_date=ensure_date(from_isoformat(end_date_str)) if end_date_str else None,
        )

        if self.milestones_issue_type:
            new_issue.issue_type = self.milestones_issue_type

        if tracker_issue != new_issue:
            logger.info(
                f"Updating milestone {tracker_issue.id} - {tracker_issue.title} ({tracker_issue.url} / {new_issue.notion_url})"
            )
            diff_dataclasses(tracker_issue, new_issue, log=logger.debug)

            if not self.dry:
                await self.tracker.update_milestone_issue(tracker_issue, new_issue)
        elif not skip_unchanged_msg:
            logger.info(
                f"Unchanged milestone {tracker_issue.id} - {tracker_issue.title} ({tracker_issue.url} / {new_issue.notion_url})"
            )

    def _schedule_milestone_sync(self, tg, tracker_issue, notion_page, collected_tasks):
        if notion_page:
            tg.create_task(self.synchronize_single_milestone(tracker_issue, notion_page))
        elif self.milestones_create_from_tracker:
            tg.create_task(self.create_single_milestone(tracker_issue))

        # For each sub-issue in the tracker milestone, make sure we have a notion task
        for subissue in tracker_issue.sub_issues:
            collected_tasks.setdefault(subissue.repo, {}).setdefault(subissue.id, None)

    async def synchronize(self):
        """Synchronize all the things!"""
        await self._async_init()

        timestamp = datetime.datetime.now(datetime.UTC)
        collected_tasks = deepcopy(self._notion_tasks_issues)

        collected_tracker_milestones = {}
        if self.milestones_create_from_tracker:
            async for milestone in self.tracker.collect_tracker_milestones(self.milestones_issue_type, sub_issues=True):
                collected_tracker_milestones.setdefault(milestone.repo, {})[milestone.id] = milestone

        async with asyncio.TaskGroup() as tg:
            # Synchronize issues found in milestones
            for reporef, notion_pages in self._notion_milestone_issues.items():
                repo_milestones = collected_tracker_milestones.get(reporef, {})
                missing_refs = []

                # First pass. Schedule sync for milestones we already have
                for issue_id, notion_page in notion_pages.items():
                    milestone = repo_milestones.pop(issue_id, None)

                    if milestone is not None:
                        self._schedule_milestone_sync(
                            tg,
                            milestone,
                            notion_page,
                            collected_tasks,
                        )
                    else:
                        missing_refs.append(IssueRef(id=issue_id, repo=reporef))

                # Remaining milestones are new in the tracker

                # Fetch and schedule missing milestones
                async for issue in self.tracker.get_issues_by_number(missing_refs, True):
                    self._schedule_milestone_sync(
                        tg,
                        issue,
                        notion_pages.get(issue.id),
                        collected_tasks,
                    )

                logger.info(f"Synchronizing {len(notion_pages)} milestones for {reporef}")

            if self.milestones_create_from_tracker:
                for reporef, milestones in collected_tracker_milestones.items():
                    if not len(milestones):
                        continue

                    logger.info(f"Creating {len(milestones)} new milestones for {reporef}")
                    for milestone in milestones.values():
                        self._schedule_milestone_sync(
                            tg,
                            milestone,
                            None,
                            collected_tasks,
                        )

            # Any additional tasks the tracker might be interested in (e.g. sprint boards)
            await self.tracker.collect_additional_tasks(collected_tasks)

            # Synchronize individual and above collected tasks
            for reporef, issue_pages in collected_tasks.items():
                refs = [IssueRef(id=issue, repo=reporef) for issue in issue_pages.keys()]

                tracker_issues = self.tracker.get_issues_by_number(refs)
                logger.info(f"Synchronizing tasks for {reporef}")

                async for issue in tracker_issues:
                    tg.create_task(self.synchronize_single_task(issue, issue_pages[issue.id]))

        async with asyncio.TaskGroup() as tg:
            # Update the description with the last updated timestamp
            tg.create_task(self._update_timestamp(self.milestones_db, timestamp))
            tg.create_task(self._update_timestamp(self.tasks_db, timestamp))

        await self.notion.aclose()


async def synchronize(**kwargs):  # pragma: no cover
    """Exported method to begin synchronization."""
    await ProjectSync(**kwargs).synchronize()
