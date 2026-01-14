import asyncio
import logging
from ..util import getnestedattr
from sgqlc.operation import Operation
from ..github_schema import schema


logger = logging.getLogger("gh_fixups")


class GitHubFixups:
    """Mixin class to separate the fixups.

    There is likely a better way to do this, but these fixups exist to resolve inconsistencies in
    the tracker. We do them centrally here since the script runs anyway, and we have the project
    permissions that GitHub Actions tokens don't have. We avoid needing to save secrets across all
    repositories.
    """

    async def _fixup_pull_requests(self, pull_requests):
        for pull_request in pull_requests:
            ghissues = pull_request.closing_issues_references.nodes

            if not ghissues or pull_request.state != "OPEN":
                continue

            # We could do this one level up, but that might mean a lot of parallel requests
            async with asyncio.TaskGroup() as tg:
                tg.create_task(self._fixup_pull_request_assign_author(pull_request, ghissues))
                tg.create_task(self._fixup_add_to_tasks_project(pull_request, ghissues))

    async def _fixup_pull_request_assign_author(self, pull_request, ghissues):
        """Sets the author of the pull request as an assignee of the linked issue."""
        author = getnestedattr(lambda: pull_request.author.login, None)
        author_id = self.user_map.trk_to_dbid(author)

        if not author_id:
            return

        added = 0
        op = Operation(schema.mutation_type)
        for idx, ghissue in enumerate(ghissues):
            if any(assignee.id == author_id for assignee in ghissue.assignees.nodes):
                continue

            op.add_assignees_to_assignable(
                __alias__=f"add_{idx}",
                input={"assignable_id": ghissue.id, "assignee_ids": [author_id]},
            )
            added += 1

        if added:
            logger.info(f"Adding author {author} to {added} issues for pull request {pull_request.url}")
            if not self.dry:
                await self.endpoint(op)

    async def _fixup_add_to_tasks_project(self, pull_request, ghissues):
        """Adds issues liked to the pull request to the Tasks project and sets it to In Review."""

        async def update_and_log(project, ghissue, status):
            item = project.find_project_item(ghissue, project.database_id)
            if not item:
                logger.info(f"Adding {ghissue.url} to tasks project due to pull request {pull_request.url}")
                await project.add_issue_to_project(ghissue)

            if not pull_request.is_draft:
                changed = await project.update_project_for_issue(ghissue, {"status": status})
                if changed:
                    logger.info(
                        f"Setting {ghissue.url} task project status to {status} due to pull request {pull_request.url}"
                    )

        async with asyncio.TaskGroup() as tg:
            for ghissue in ghissues:
                orgrepo = ghissue.repository.name_with_owner
                tasks_project = self.github_tasks_projects[orgrepo]

                tg.create_task(update_and_log(tasks_project, ghissue, "In Review"))

    async def _fixup_issue(self, ghissue, sub_issues=False):
        orgrepo = ghissue.repository.name_with_owner

        tasks_project_item = (
            self.github_tasks_projects[orgrepo].find_project_item(
                ghissue, self.github_tasks_projects[orgrepo].database_id
            )
            if orgrepo in self.github_tasks_projects
            else None
        )

        milestones_project_item = (
            self.github_milestones_projects[orgrepo].find_project_item(
                ghissue, self.github_milestones_projects[orgrepo].database_id
            )
            if orgrepo in self.github_milestones_projects
            else None
        )

        await self._fixup_issue_both_projects(tasks_project_item, milestones_project_item, ghissue, sub_issues)
        await self._fixup_issue_milestone_with_parent(milestones_project_item, ghissue)

    async def _fixup_issue_both_projects(self, tasks_project_item, milestones_project_item, ghissue, sub_issues):
        """Issues should not be on both boards. Use some indicators to make a best effort call where it belongs."""
        issue_type = getnestedattr(lambda: ghissue.issue_type.name, None)
        orgrepo = ghissue.repository.name_with_owner

        # Issues cannot be on both tasks and milestone projects
        if tasks_project_item and milestones_project_item:
            if not ghissue.parent and (
                issue_type == self.milestones_issue_type or (sub_issues and ghissue.sub_issues.nodes)
            ):
                # This is a milestone, or it at least has sub-issues. Remove it from the task
                # project
                logger.warn(
                    f"Issue https://github.com/{orgrepo}/issues/{ghissue.number} is on both "
                    "milestone and task project. Removing from task project."
                )

                async with asyncio.TaskGroup() as tg:
                    tg.create_task(
                        self._comment_on_issue(
                            ghissue,
                            "Issues cannot be both on the Milestones and Tasks boards. This "
                            "appears to be a Milestone issue, removing from Tasks board",
                        )
                    )
                    tg.create_task(self.github_tasks_projects[orgrepo].remove_project_from_issue(ghissue))

                tasks_project_item = None
            elif ghissue.parent and ghissue.parent.number:
                # this has a parent issue, which might be a milestone. Remove it from the milestone
                # project
                logger.warn(
                    f"Issue https://github.com/{orgrepo}/issues/{ghissue.number} is on both the "
                    "Milestone and Tasks project. Removing from Milestones project."
                )

                async with asyncio.TaskGroup() as tg:
                    tg.create_task(
                        self._comment_on_issue(
                            ghissue,
                            "Issues cannot be both on the Milestones and Tasks boards. This "
                            "appears to be a Task, removing from Milestones board",
                        )
                    )
                    tg.create_task(self.github_milestones_projects[orgrepo].remove_project_from_issue(ghissue))

                milestones_project_item = None
            else:
                raise Exception(f"Issue {ghissue.url} has both tasks and milestones project")

    async def _fixup_issue_milestone_with_parent(self, milestones_project_item, ghissue):
        """Issues on the Milestone project shouldn't have parents. Avoids sub-issues landing on the roadmap."""
        orgrepo = ghissue.repository.name_with_owner

        if milestones_project_item and ghissue.parent and ghissue.parent.number:
            # This is an issue with a parent, but it is also on the milestones board. This can
            # happen when you create sub-issues of items on the milestone board, github defaults to
            # adding it to the project.
            logger.warn(
                f"Issue https://github.com/{orgrepo}/issues/{ghissue.number} has a parent and is "
                "on the Milestones board. Removing from milestones project."
            )

            async with asyncio.TaskGroup() as tg:
                tg.create_task(
                    self._comment_on_issue(
                        ghissue,
                        "Issues with a parent cannot be on the Milestones board, removing. "
                        "Either move your sub-issues up to the parent issue, or turn this into "
                        "an independent Milestone issue that has sub-issues.",
                    )
                )
                tg.create_task(self.github_milestones_projects[orgrepo].remove_project_from_issue(ghissue))
