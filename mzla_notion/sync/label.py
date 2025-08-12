# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import datetime
import asyncio

from functools import cached_property

from .base import BaseSync

logger = logging.getLogger("gh_label_sync")


class LabelSync(BaseSync):
    """This is a label-based sync between Notion and an GitHub.

    All tasks in the associated repositories are synchronized to notion. The relation to the
    milestones is done using GitHub labels and a prefix. The label `M: milestone name` will link the
    task to the milestone `milestone name`.
    """

    def __init__(self, milestone_label_prefix="", **kwargs):
        """Initialize label sync."""
        super().__init__(**kwargs)
        self.milestone_label_prefix = milestone_label_prefix

    async def _async_init(self):
        async with asyncio.TaskGroup() as tg:
            tg.create_task(super()._async_init())
            milestone_pages = tg.create_task(self.milestones_db.get_all_pages())

        self._all_milestone_pages = milestone_pages.result()

    @cached_property
    def _milestone_pages_by_title(self):
        return {
            content: page
            for page in self._all_milestone_pages
            if (content := self._get_richtext_prop(page, "notion_milestones_title"))
        }

    def _find_task_parents(self, issue):
        parent_ids = []

        for label in issue.labels:
            if label.startswith(self.milestone_label_prefix):
                clean_label = label[len(self.milestone_label_prefix) :].strip()
                if page := self._milestone_pages_by_title.get(clean_label):
                    parent_ids.append(page["id"])

        return parent_ids

    async def synchronize(self):
        """Synchronize all the issues!"""
        await self._async_init()

        timestamp = datetime.datetime.now(datetime.UTC)

        tracker_issues = self.tracker.get_all_issues()
        tasks_issues = self._notion_tasks_issues

        # Synchronize all issues into the tasks db
        async with asyncio.TaskGroup() as tg:
            async for issue in tracker_issues:
                tg.create_task(self.synchronize_single_task(issue, tasks_issues.get(issue.repo, {}).get(issue.id)))

        # Update the description with the last updated timestamp
        await self._update_timestamp(self.tasks_db, timestamp)
        await self.notion.aclose()


async def synchronize(**kwargs):  # pragma: no cover
    """Exported method to begin synchronization."""
    await LabelSync(**kwargs).synchronize()
