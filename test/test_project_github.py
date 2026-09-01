import datetime
import dataclasses
import types
import sgqlc.operation
import json
import httpx
from unittest.mock import AsyncMock, MagicMock

from freezegun import freeze_time

from mzla_notion.tracker.github import (
    GitHub,
    GitHubProjectV2,
    GitHubUserMap,
    LabelCache,
    GitHubIssue,
    GitHubUser,
)
from mzla_notion.tracker.github_utils import build_scalar_field_update, field_value_changed
from mzla_notion.tracker.common import Issue, IssueRef, Sprint

from .handlers import BaseTestCase

REPO_SETTINGS = {
    "reposetA": {
        "repositories": ["kewisch/test"],
        "github_tasks_project_id": "PVT_kwHOAAlD3s4AxVFW",
        "github_milestones_project_id": "PVT_kwHOAAlD3s4AxVDI",
    }
}


class GitHubProjectTest(BaseTestCase):
    async def asyncSetUp(self):
        await super().asyncSetUp()

        self.github = await GitHub.create(token="GITHUB_TOKEN", repositories=REPO_SETTINGS, user_map={}, dry=False)

    async def test_init_flat_repo(self):
        flat_repo_settings = REPO_SETTINGS["reposetA"]

        github = await GitHub.create(token="GITHUB_TOKEN", repositories=flat_repo_settings, user_map={}, dry=False)
        self.assertTrue(github.is_repo_allowed("kewisch/test"))
        self.assertEqual(github.get_all_repositories(), ["kewisch/test"])

    async def test_disabled_fixups_skip_issue_and_pull_request_handlers(self):
        github = await GitHub.create(
            token="GITHUB_TOKEN",
            repositories=REPO_SETTINGS,
            user_map={},
            dry=False,
            fixups_enabled=False,
        )
        github._fixup_issue_both_projects = AsyncMock()
        github._fixup_issue_milestone_with_parent = AsyncMock()
        github._fixup_pull_request_assign_author = AsyncMock()
        github._fixup_add_to_tasks_project = AsyncMock()

        await github._fixup_issue(types.SimpleNamespace(), sub_issues=True)
        await github._fixup_pull_requests([types.SimpleNamespace()])

        github._fixup_issue_both_projects.assert_not_awaited()
        github._fixup_issue_milestone_with_parent.assert_not_awaited()
        github._fixup_pull_request_assign_author.assert_not_awaited()
        github._fixup_add_to_tasks_project.assert_not_awaited()

    def test_is_task_issue_uses_github_task_criteria(self):
        def classifier_issue(issue_type=None, parent_type=None, on_tasks_project=False, review_url=None):
            project_items = []
            if on_tasks_project:
                project_items.append(types.SimpleNamespace(project=types.SimpleNamespace(id="PVT_kwHOAAlD3s4AxVFW")))

            parent = None
            parents = []
            if parent_type:
                parent = types.SimpleNamespace(issue_type=types.SimpleNamespace(name=parent_type))
                parents = [IssueRef(repo="kewisch/test", id="2")]

            return GitHubIssue(
                repo="kewisch/test",
                id="10",
                parents=parents,
                title="Classifier issue",
                description="",
                state="Backlog",
                priority="P2",
                issue_type=issue_type,
                labels=set(),
                url="https://github.com/kewisch/test/issues/10",
                review_url=review_url,
                gql=types.SimpleNamespace(
                    parent=parent,
                    project_items=types.SimpleNamespace(nodes=project_items),
                ),
            )

        self.github.milestones_issue_type = "Milestone"
        self.github.epics_issue_type = "Epic"

        cases = [
            ("milestone_with_epic_parent", classifier_issue("Milestone", parent_type="Epic"), False),
            ("epic_on_tasks_project", classifier_issue("Epic", on_tasks_project=True), False),
            ("milestone_parent", classifier_issue(parent_type="Milestone"), True),
            ("tasks_project", classifier_issue(on_tasks_project=True), True),
            ("pull_request", classifier_issue(review_url="https://github.com/kewisch/test/pull/10"), True),
            ("standalone", classifier_issue(), False),
        ]

        for name, issue, expected in cases:
            with self.subTest(name):
                self.assertEqual(self.github.is_task_issue(issue), expected)

    async def test_recent_issues_includes_project_item_updates(self):
        async def no_recent_repo_issues(*args, **kwargs):
            if False:
                yield None

        class ProjectWithRecentItem:
            database_id = "project"

            async def get_issues_updated_since(self, since, allowed_repositories):
                yield types.SimpleNamespace()

        async def parse_issue(ghissue, sub_issues=False):
            return Issue(
                repo="kewisch/test",
                id="9",
                title="Project item update",
                description="",
                state="Backlog",
                priority="P2",
                url="https://github.com/kewisch/test/issues/9",
            )

        self.github._get_repo_issues = no_recent_repo_issues
        self.github._parse_issue = parse_issue
        self.github.all_tasks_projects = [ProjectWithRecentItem()]
        self.github.all_milestones_projects = []

        issues = await self.github.get_recent_issues_by_repo(
            datetime.datetime(2026, 8, 20, tzinfo=datetime.timezone.utc)
        )

        self.assertIn("9", issues["kewisch/test"])

    async def test_project_item_recent_query_filters_by_updated_date_and_repo(self):
        project = GitHubProjectV2(self.github.endpoint, "project-filter-test")

        issues = [
            issue
            async for issue in project.get_issues_updated_since(
                datetime.datetime(2025, 7, 1, 12, tzinfo=datetime.timezone.utc),
                {"kewisch/test"},
            )
        ]

        self.assertEqual([issue.number for issue in issues], [3])
        self.assertEqual(len(self.github_handler.calls["get_recent_project_filtered_items"]), 1)

    async def test_github_get_issues_basics(self):
        issues = [issue async for issue in self.github.get_issues_by_number([], True)]
        self.assertEqual(issues, [])

        with self.assertRaisesRegex(Exception, r"Can't yet query from different repositories"):
            iterator = self.github.get_issues_by_number(
                [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test2", id="1")], True
            )
            issues = [issue async for issue in iterator]

    async def test_github_get_inaccessible_issue_logs_notion_page(self):
        self.github_handler.responses["get_issues_3"]["data"]["repository"]["issue3"] = None
        self.respx.get("https://github.com/kewisch/test/issues/3").mock(return_value=httpx.Response(404))

        ref = IssueRef(
            repo="kewisch/test",
            id="3",
            notion_url="https://www.notion.so/example/inaccessible-page-123",
        )

        with self.assertLogs("project_sync", level="WARNING") as logs:
            issues = [issue async for issue in self.github.get_issues_by_number([ref])]

        self.assertEqual(issues, [])
        self.assertIn(
            "Issue https://github.com/kewisch/test/issues/3 "
            "from Notion page https://www.notion.so/example/inaccessible-page-123 "
            "is no longer accessible",
            "\n".join(logs.output),
        )

    async def test_github_get_issue_reviewers(self):
        self.github.user_map = GitHubUserMap({"kewisch": "3df71ec3-17c7-4eb4-80bc-a321af157be6"})
        self.github.user_map._trk_to_dbid = {"kewisch": "MDQ6VXNlcjYwNzE5OA=="}
        self.github.user_map._dbid_to_trk = {"MDQ6VXNlcjYwNzE5OA==": "kewisch"}

        iterator = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="1")], True)
        issues = {issue.id: issue async for issue in iterator}
        issue = issues["1"]

        self.assertEqual(issue.review_url, "https://github.com/kewisch/test/pull/10")
        self.assertTrue(self.github.is_task_issue(issue))
        self.assertEqual({user.tracker_user for user in issue.reviewers}, {"kewisch"})
        self.assertEqual({user.notion_user for user in issue.reviewers}, {"3df71ec3-17c7-4eb4-80bc-a321af157be6"})

    async def test_github_get_issues_epics(self):
        iterator = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )
        issues = {issue.id: issue async for issue in iterator}

        self.assertEqual(len(issues), 2)
        issue = issues["1"]

        self.assertEqual(issue.repo, "kewisch/test")
        self.assertEqual(issue.id, "1")
        self.assertEqual(issue.gql.id, "I_kwDOMwGgpM6WLTqc")
        self.assertEqual(issue.parents, [])
        self.assertEqual(issue.title, "Account Drawer Improvements")
        self.assertEqual(issue.description, "I am the body")
        self.assertEqual(issue.state, "Not started")
        self.assertEqual(issue.priority, "P2")
        self.assertEqual(issue.estimate, "5")
        self.assertEqual(len(issue.assignees), 1)
        self.assertEqual(next(iter(issue.assignees)).tracker_user, "kewisch")
        self.assertEqual(issue.creator.tracker_user, "kewisch")
        self.assertEqual(issue.labels, {"type: epic"})
        self.assertEqual(issue.url, "https://github.com/kewisch/test/issues/1")
        self.assertEqual(issue.review_url, None)
        self.assertEqual(
            issue.notion_url, "https://notion.so/example/rebuild-event-read-dialog-726fac286b6348ca90ec0066be1a2755"
        )
        self.assertEqual(issue.start_date, datetime.date.fromisoformat("2025-01-24"))
        self.assertEqual(issue.end_date, datetime.date.fromisoformat("2025-01-28"))
        self.assertEqual(issue.sprint, None)
        self.assertEqual(issue.sub_issues, [])

        issue = issues["2"]

        self.assertEqual(issue.repo, "kewisch/test")
        self.assertEqual(issue.id, "2")
        self.assertEqual(issue.gql.id, "I_kwDOMwGgpM6oTotN")
        self.assertEqual(issue.parents, [])
        self.assertEqual(issue.title, "test2")
        self.assertEqual(
            issue.description, "\nThis is a page with content\n\n\n@kewisch \n\n\n# hi\n\n\ndings\n\n\n---\n\n"
        )
        self.assertEqual(issue.state, "In progress")
        self.assertEqual(issue.priority, "P3")
        self.assertEqual(issue.estimate, None)
        self.assertEqual(len(issue.assignees), 0)
        self.assertEqual(issue.labels, {"type: epic"})
        self.assertEqual(issue.url, "https://github.com/kewisch/test/issues/2")
        self.assertEqual(issue.review_url, None)
        self.assertEqual(
            issue.notion_url, "https://notion.so/example/test-ref-failure-a2b009b4b63447599b138cf059a7f885"
        )
        self.assertEqual(issue.start_date, datetime.date.fromisoformat("2025-02-19"))
        self.assertEqual(issue.end_date, datetime.date.fromisoformat("2025-02-23"))
        self.assertEqual(issue.sprint, None)
        self.assertEqual(
            issue.sub_issues,
            [
                IssueRef(repo="kewisch/test", id="4", parents=[issue]),
                IssueRef(repo="kewisch/test", id="3", parents=[issue]),
            ],
        )

        self.assertEqual(len(self.github_handler.calls), 2)
        self.assertEqual(len(self.github_handler.calls["get_issues_1_and_2"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issue_field_priority"]), 1)

    async def test_github_get_issue_tasks(self):
        iterator = self.github.get_issues_by_number([], True)
        issues = [issue async for issue in iterator]
        self.assertEqual(issues, [])

        issue3 = GitHubIssue(
            repo="kewisch/test",
            id="3",
            parents=[IssueRef(repo="kewisch/test", id="2", parents=[])],
            title="test2-sub1",
            description="sup",
            state="In review",
            priority="P2",
            assignees={
                GitHubUser(user_map=self.github.user_map, tracker_user="kewisch", dbid_user="MDQ6VXNlcjYwNzE5OA==")
            },
            labels=set(),
            url="https://github.com/kewisch/test/issues/3",
            review_url=None,
            notion_url=None,
            created_date=datetime.datetime(2025, 1, 31, 20, 38, 43, tzinfo=datetime.timezone.utc),
            updated_date=datetime.datetime(2025, 1, 31, 20, 38, 43, tzinfo=datetime.timezone.utc),
            start_date=None,
            end_date=None,
            sprint=Sprint(
                id="08dfe996",
                name="Sprint 1",
                status="Past",
                start_date=datetime.date(2025, 2, 2),
                end_date=datetime.date(2025, 2, 8),
            ),
            sub_issues=[],
        )

        with freeze_time("2025-02-09"):
            iterator = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="3")])
            issues = {issue.id: issue async for issue in iterator}
            self.assertEqual(issues["3"].gql.id, "I_kwDOMwGgpM6oWELp")
            issue3.updated_date = issues["3"].updated_date

            issues["3"].gql = None
            self.assertEqual(issues, {"3": issue3})

        with freeze_time("2025-02-05"):
            iterator = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="3")])
            issues = {issue.id: issue async for issue in iterator}
            self.assertEqual(issues["3"].gql.id, "I_kwDOMwGgpM6oWELp")
            issue3.updated_date = issues["3"].updated_date

            issue3.sprint.status = "Current"

            issues["3"].gql = None
            self.assertEqual(issues, {"3": issue3})

        with freeze_time("2025-02-01"):
            iterator = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="3")])
            issues = {issue.id: issue async for issue in iterator}
            self.assertEqual(issues["3"].gql.id, "I_kwDOMwGgpM6oWELp")
            issue3.updated_date = issues["3"].updated_date

            issue3.sprint.status = "Future"

            issues["3"].gql = None
            self.assertEqual(issues, {"3": issue3})

    async def test_github_get_issue_both_projects(self):
        iterator = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="4")])
        issues = [issue async for issue in iterator]

        # This issue was in both roadmaps. The test is also validated by the commenting request
        # being made, and a delete item from project request
        self.assertEqual(len(issues[0].gql.project_items), 1)

    async def test_github_update_no_change(self):
        self.github.user_map = await GitHubUserMap.create(
            self.github.endpoint,
            {"kewisch": "3df71ec3-17c7-4eb4-80bc-a321af157be6", "notkewisch": "b5a819b4-e2b3-432c-8e5a-256dace1176f"},
        )

        iterator = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )
        issues = {issue.id: issue async for issue in iterator}

        old_issue = issues["1"]

        # A call without change shouldn't trigger anything
        await self.github.update_milestone_issue(old_issue, old_issue)
        self.assertEqual(len(self.github_handler.calls), 3)
        self.assertEqual(len(self.github_handler.calls["get_users"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issues_1_and_2"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issue_field_priority"]), 1)

    async def test_github_update_milestone_issue(self):
        self.github.user_map = await GitHubUserMap.create(
            self.github.endpoint,
            {"kewisch": "3df71ec3-17c7-4eb4-80bc-a321af157be6", "notkewisch": "b5a819b4-e2b3-432c-8e5a-256dace1176f"},
        )

        iterator = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )
        issues = {issue.id: issue async for issue in iterator}

        old_issue = issues["1"]

        notkewisch = self.github.new_user(tracker_user="notkewisch")

        self.github.property_names["notion_closed_states"] = ("Banana", "Done")

        new_issue = dataclasses.replace(
            old_issue,
            title="title2",
            labels={"bug"},
            description="description2",
            state="Banana",
            priority="P3",
            assignees={notkewisch},
            notion_url="https://www.notion.so/mzthunderbird/123123123",
            start_date=datetime.date.fromisoformat("2025-07-04"),
            end_date=datetime.date.fromisoformat("2025-07-04"),
            sprint=None,
            sub_issues=[],
        )

        await self.github.update_milestone_issue(old_issue, new_issue)

        self.assertEqual(len(self.github_handler.calls), 10)

        self.assertEqual(len(self.github_handler.calls["get_users"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issues_1_and_2"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_basic_closed"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_assignees"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_labels"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_project"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_label_bug"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_project_info"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issue_field_priority"]), 1)
        self.assertEqual(len(self.github_handler.calls["set_issue_field_value"]), 1)
        request_query = json.loads(self.github_handler.calls["set_issue_field_value"][0].content)["query"]
        self.assertIn('textValue: "https://www.notion.so/mzthunderbird/123123123"', request_query)

    async def test_github_update_issue_add_roadmap(self):
        self.github.user_map = await GitHubUserMap.create(
            self.github.endpoint,
            {"kewisch": "3df71ec3-17c7-4eb4-80bc-a321af157be6", "notkewisch": "b5a819b4-e2b3-432c-8e5a-256dace1176f"},
        )

        iterator = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )
        issues = {issue.id: issue async for issue in iterator}

        old_issue = issues["1"]
        old_issue.gql.project_items.nodes = []
        notkewisch = self.github.new_user(tracker_user="notkewisch")

        new_issue = dataclasses.replace(
            old_issue,
            title="title2",
            labels={"bug"},
            description="description2",
            state="In Progress",
            priority="P3",
            assignees={notkewisch},
            notion_url="https://www.notion.so/mzthunderbird/123123123",
            start_date=datetime.date.fromisoformat("2025-07-04"),
            end_date=datetime.date.fromisoformat("2025-07-04"),
            sprint=None,
            sub_issues=[],
        )

        await self.github.update_milestone_issue(old_issue, new_issue)

        self.assertEqual(len(self.github_handler.calls), 11)

        self.assertEqual(len(self.github_handler.calls["get_users"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issues_1_and_2"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_label_bug"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_project_info"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_basic"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_assignees"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_labels"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_project"]), 1)
        self.assertEqual(len(self.github_handler.calls["add_issue_to_project"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issue_field_priority"]), 1)
        self.assertEqual(len(self.github_handler.calls["set_issue_field_value"]), 1)

    async def test_github_update_issue_dry(self):
        self.github.dry = True

        self.github.user_map = await GitHubUserMap.create(
            self.github.endpoint,
            {"kewisch": "3df71ec3-17c7-4eb4-80bc-a321af157be6", "notkewisch": "b5a819b4-e2b3-432c-8e5a-256dace1176f"},
        )

        iterator = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )
        issues = {issue.id: issue async for issue in iterator}

        old_issue = issues["1"]

        notkewisch = self.github.new_user(tracker_user="notkewisch")

        new_issue = dataclasses.replace(
            old_issue,
            title="title2",
            labels={"bug"},
            description="description2",
            state="In Progress",
            priority="P3",
            assignees={notkewisch},
            notion_url="https://www.notion.so/mzthunderbird/123123123",
            start_date=datetime.date.fromisoformat("2025-07-04"),
            end_date=datetime.date.fromisoformat("2025-07-04"),
            sprint=None,
            sub_issues=[],
        )

        await self.github.update_milestone_issue(old_issue, new_issue)

        self.assertEqual(len(self.github_handler.calls), 4)

        self.assertEqual(len(self.github_handler.calls["get_users"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issues_1_and_2"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_label_bug"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issue_field_priority"]), 1)

    async def test_github_update_issue_fields_fail_fast_missing_priority(self):
        iterator = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )
        old_issue = {issue.id: issue async for issue in iterator}["1"]

        self.github.issue_planning_cache._issue_field_cache["kewisch"] = {}
        self.github.issue_planning_cache._issue_type_cache["kewisch"] = {}
        new_issue = dataclasses.replace(old_issue, priority="P3")

        with self.assertRaisesRegex(
            Exception,
            r"GitHub issue field 'Priority' in kewisch/test must be SINGLE_SELECT, got '\(missing\)'",
        ):
            await self.github._update_issue_fields(old_issue, new_issue)

    async def test_github_update_issue_fields_clear_notion_link(self):
        iterator = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="1")], True)
        old_issue = {issue.id: issue async for issue in iterator}["1"]
        new_issue = dataclasses.replace(old_issue, notion_url=None)

        await self.github._update_issue_fields(old_issue, new_issue)

        self.assertEqual(len(self.github_handler.calls["set_issue_field_value_clear_notion_link"]), 1)

    async def test_github_update_issue_fields_estimate(self):
        iterator = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="1")], True)
        old_issue = {issue.id: issue async for issue in iterator}["1"]
        new_issue = dataclasses.replace(old_issue, estimate="3")

        await self.github._update_issue_fields(old_issue, new_issue)

        self.assertEqual(len(self.github_handler.calls["set_issue_field_value_estimate"]), 1)

    async def test_github_update_task_issue_updates_priority(self):
        iterator = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="1")], True)
        old_issue = {issue.id: issue async for issue in iterator}["1"]
        new_issue = dataclasses.replace(old_issue, priority="P3")

        await self.github.update_task_issue(old_issue, new_issue)

        self.assertEqual(len(self.github_handler.calls["set_issue_field_value_priority"]), 1)

    async def test_github_update_issue_fields_fail_fast_missing_notion_link(self):
        iterator = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="1")], True)
        old_issue = {issue.id: issue async for issue in iterator}["1"]

        self.github.issue_planning_cache._issue_field_cache["kewisch"] = {
            "Priority": types.SimpleNamespace(id="IF_priority", data_type="SINGLE_SELECT", options=[])
        }
        self.github.issue_planning_cache._issue_type_cache["kewisch"] = {}
        new_issue = dataclasses.replace(old_issue, notion_url="https://www.notion.so/mzthunderbird/123123123")

        with self.assertRaisesRegex(
            Exception,
            r"GitHub issue field 'Notion Link' in kewisch/test must be TEXT, got '\(missing\)'",
        ):
            await self.github._update_issue_fields(old_issue, new_issue)

    async def test_github_update_issue_fields_fail_fast_wrong_notion_link_type(self):
        iterator = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="1")], True)
        old_issue = {issue.id: issue async for issue in iterator}["1"]

        self.github.issue_planning_cache._issue_field_cache["kewisch"]["Notion Link"] = types.SimpleNamespace(
            id="IF_notion_link", data_type="NUMBER"
        )
        self.github.issue_planning_cache._issue_type_cache["kewisch"] = {}
        new_issue = dataclasses.replace(old_issue, notion_url="https://www.notion.so/mzthunderbird/123123123")

        with self.assertRaisesRegex(
            Exception,
            r"GitHub issue field 'Notion Link' in kewisch/test must be TEXT, got 'NUMBER'",
        ):
            await self.github._update_issue_fields(old_issue, new_issue)

    def test_field_value_changed_normalized_date(self):
        self.assertFalse(field_value_changed(datetime.date(2025, 7, 4), "2025-07-04"))
        self.assertTrue(field_value_changed(datetime.date(2025, 7, 4), "2025-07-05"))

    def test_field_value_changed_normalized_notion_url(self):
        self.assertFalse(field_value_changed("https://app.notion.com/p/xxx", "https://www.notion.so/xxx"))
        self.assertFalse(field_value_changed("https://app.notion.com/p/xxx", "https://notion.so/xxx"))
        self.assertFalse(
            field_value_changed(
                "https://app.notion.com/p/Kubernetes-Migration-33c2df5d45ae80989ba4d7e9e694ad0f",
                "https://app.notion.com/p/Epic-Kubernetes-Migration-FY26-Q3-33c2df5d45ae80989ba4d7e9e694ad0f",
            )
        )
        self.assertFalse(
            field_value_changed(
                "https://app.notion.com/p/Kubernetes-Migration-33c2df5d45ae80989ba4d7e9e694ad0f?source=copy_link",
                "https://app.notion.com/p/Epic-Kubernetes-Migration-FY26-Q3-33c2df5d45ae80989ba4d7e9e694ad0f",
            )
        )
        self.assertTrue(field_value_changed("https://app.notion.com/p/xxx", "https://www.notion.so/yyy"))

    def test_build_scalar_field_update_number(self):
        self.assertEqual(build_scalar_field_update("NUMBER", "5"), {"number_value": 5.0})
        self.assertEqual(build_scalar_field_update("NUMBER", 8), {"number_value": 8.0})
        self.assertEqual(build_scalar_field_update("NUMBER", None), {"delete": True})

    async def test_get_sprints(self):
        with freeze_time("2025-02-24 12:13:14"):
            res = await self.github.get_sprints()
            self.assertCountEqual(
                res,
                [
                    Sprint(
                        id="08c4a1b9",
                        name="Sprint 5",
                        status="Future",
                        start_date=datetime.date(2025, 3, 2),
                        end_date=datetime.date(2025, 3, 8),
                    ),
                    Sprint(
                        id="8260fc57",
                        name="Sprint 4",
                        status="Current",
                        start_date=datetime.date(2025, 2, 23),
                        end_date=datetime.date(2025, 3, 1),
                    ),
                    Sprint(
                        id="ff6e72b7",
                        name="Sprint 3",
                        status="Past",
                        start_date=datetime.date(2025, 2, 16),
                        end_date=datetime.date(2025, 2, 22),
                    ),
                    Sprint(
                        id="adaae9c2",
                        name="Sprint 2",
                        status="Past",
                        start_date=datetime.date(2025, 2, 9),
                        end_date=datetime.date(2025, 2, 15),
                    ),
                    Sprint(
                        id="08dfe996",
                        name="Sprint 1",
                        status="Past",
                        start_date=datetime.date(2025, 2, 2),
                        end_date=datetime.date(2025, 2, 8),
                    ),
                ],
            )

    async def test_collect_additional_tasks(self):
        collected_tasks = {"kewisch/test": {"4": None, "6": {"id": "mock_block"}}}

        await self.github.collect_additional_tasks(collected_tasks)

        self.assertIn("3", collected_tasks["kewisch/test"])
        self.assertIn("4", collected_tasks["kewisch/test"])
        self.assertIn("6", collected_tasks["kewisch/test"])
        self.assertIsNone(collected_tasks["kewisch/test"]["3"])
        self.assertIsNone(collected_tasks["kewisch/test"]["4"])
        self.assertEqual(collected_tasks["kewisch/test"]["6"], {"id": "mock_block"})

        self.assertEqual(len(self.github_handler.calls["get_sprint_tasks"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_pull_requests"]), 1)

    def test_parse_issueref_allowed(self):
        res = self.github.parse_issueref("https://github.com/kewisch/test/issues/1")
        self.assertEqual(res, IssueRef(repo="kewisch/test", id="1"))

        res = self.github.parse_issueref("https://BANANAS")
        self.assertIsNone(res)

        self.assertTrue(self.github.is_repo_allowed("kewisch/test"))
        self.assertFalse(self.github.is_repo_allowed("kewisch/test2"))

        self.assertEqual(len(self.github_handler.calls), 0)

    async def test_get_all_issues(self):
        issues = [issue async for issue in self.github.get_all_issues()]
        self.assertEqual(len(issues), 7)
        self.assertIsNotNone(issues[0].updated_date)

    async def test_get_recent_issues_by_repo(self):
        since = datetime.datetime(2025, 7, 1, tzinfo=datetime.timezone.utc)
        repos = await self.github.get_recent_issues_by_repo(since, sub_issues=False)
        self.assertIn("kewisch/test", repos)
        self.assertGreaterEqual(len(repos["kewisch/test"]), 1)
        self.assertIn("1", repos["kewisch/test"])

    async def test_label_cache(self):
        cache = LabelCache(self.github.endpoint)

        ab = await cache.get_labels("org", "repo", ["a", "b"])
        bc = await cache.get_labels("org", "repo", ["b", "c"])

        self.assertEqual(ab, {"a": "LA_kwDOMwGgpM8AAAABvAun4g", "b": "LA_kwDOMwGgpM8AAAABvAun6Q"})
        self.assertEqual(bc, {"b": "LA_kwDOMwGgpM8AAAABvAun6Q", "c": "LA_kwDOMwGgpM8AAAABvAun9Q"})

        self.assertEqual(len(self.github_handler.calls), 2)
        self.assertEqual(len(self.github_handler.calls["get_labels_ab"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_labels_c"]), 1)

    async def test_usermap(self):
        user_map = self.github.user_map = await GitHubUserMap.create(
            self.github.endpoint,
            {"kewisch": "3df71ec3-17c7-4eb4-80bc-a321af157be6", "notkewisch": "b5a819b4-e2b3-432c-8e5a-256dace1176f"},
            notion_to_teams={"3df71ec3-17c7-4eb4-80bc-a321af157be6": ["team-a"]},
        )

        self.assertEqual(user_map.tracker_mention("kewisch"), "@kewisch")
        self.assertEqual(user_map.trk_to_dbid("kewisch"), "MDQ6VXNlcjYwNzE5OA==")
        self.assertEqual(user_map.dbid_to_trk("MDQ6VXNlcjYwNzE5OA=="), "kewisch")
        self.assertEqual(user_map.notion_to_dbid("3df71ec3-17c7-4eb4-80bc-a321af157be6"), "MDQ6VXNlcjYwNzE5OA==")
        self.assertEqual(user_map.dbid_to_notion("MDQ6VXNlcjYwNzE5OA=="), "3df71ec3-17c7-4eb4-80bc-a321af157be6")
        self.assertEqual(user_map.tracker_to_notion("kewisch"), "3df71ec3-17c7-4eb4-80bc-a321af157be6")
        self.assertEqual(user_map.notion_to_tracker("3df71ec3-17c7-4eb4-80bc-a321af157be6"), "kewisch")
        self.assertEqual(user_map.notion_to_teams("3df71ec3-17c7-4eb4-80bc-a321af157be6"), ["teama"])

        user = GitHubUser(user_map=self.github.user_map, tracker_user="kewisch", dbid_user="MDQ6VXNlcjYwNzE5OA==")
        self.assertEqual(user.team_ids, ["teama"])
        self.assertEqual(
            repr(user),
            "GitHubUser(tracker=kewisch,notion=3df71ec3-17c7-4eb4-80bc-a321af157be6,dbid=MDQ6VXNlcjYwNzE5OA==)",
        )

    async def test_validate_timeout(self):
        issue_count_queried = []

        count = 0
        max_count = 5

        def handler(request):
            nonlocal count
            reqdata = json.loads(request.content)
            issue_count_queried.append(reqdata["query"].count("issue(number:"))

            if count < max_count:
                count += 1
                return httpx.Response(200, json={"errors": [{"message": "Timeout on validation of query"}]})
            else:
                return self.github_handler.handle(request)

        self.respx.route(name="github_graphql", method="POST", url="https://api.github.com/graphql").mock(
            side_effect=handler
        )

        with self.subTest(msg="eventual success"):
            iterator = self.github.get_issues_by_number(
                [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
            )
            issues = [issue async for issue in iterator]

            self.assertEqual(issue_count_queried, [2, 2, 2, 2, 2, 1, 0, 1])
            self.assertEqual(len(issues), 2)

        count = 0
        max_count = 9

        with self.subTest(msg="eventual failure"):
            with self.assertRaisesRegex(sgqlc.operation.GraphQLErrors, r"Timeout on validation of query"):
                iterator = self.github.get_issues_by_number(
                    [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
                )
                issues = [issue async for issue in iterator]

    async def test_resource_limit_reduces_issue_chunk(self):
        issue_count_queried = []
        count = 0
        max_count = 5

        def handler(request):
            nonlocal count
            reqdata = json.loads(request.content)
            issue_count_queried.append(reqdata["query"].count("issue(number:"))

            if count < max_count:
                count += 1
                return httpx.Response(200, json={"errors": [{"message": "Resource limits for this query exceeded."}]})

            return self.github_handler.handle(request)

        self.respx.route(name="github_graphql", method="POST", url="https://api.github.com/graphql").mock(
            side_effect=handler
        )

        iterator = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )
        issues = [issue async for issue in iterator]

        self.assertEqual(issue_count_queried, [2, 2, 2, 2, 2, 1, 0, 1])
        self.assertEqual(len(issues), 2)

    async def test_issue_state(self):
        issues = [issue async for issue in self.github.get_all_issues()]

        # Open issue, takes from project state
        with self.subTest(msg="open issue"):
            self.assertEqual(issues[0].state, "Not started")

        # Completed issue, takes closed state
        with self.subTest(msg="completed issue"):
            self.assertEqual(issues[4].state, "Done")

        # Not planned issue, takes canceled state
        with self.subTest(msg="not planned issue"):
            self.assertEqual(issues[5].state, "Canceled")

    async def test_fixup_milestone_parent_epic_allowed(self):
        self.github._get_project_items = MagicMock(return_value=(None, None))
        self.github.milestones_issue_type = "Milestone"

        parent = types.SimpleNamespace(
            id="PARENT",
            number=1,
            issue_type=types.SimpleNamespace(name="Epic"),
            repository=types.SimpleNamespace(name_with_owner="kewisch/test"),
        )
        issue = types.SimpleNamespace(
            id="ISSUE",
            number=2,
            url="https://github.com/kewisch/test/issues/2",
            issue_type=types.SimpleNamespace(name=self.github.milestones_issue_type),
            parent=parent,
            repository=types.SimpleNamespace(name_with_owner="kewisch/test"),
            sub_issues=types.SimpleNamespace(nodes=[]),
        )

        await self.github._fixup_issue_milestone_with_parent(issue)
        self.assertIsNotNone(issue.parent)

    async def test_fixup_milestone_parent_non_epic_removed(self):
        self.github._get_project_items = MagicMock(return_value=(None, None))
        self.github.dry = True
        self.github.milestones_issue_type = "Milestone"

        parent = types.SimpleNamespace(
            id="PARENT",
            number=1,
            issue_type=types.SimpleNamespace(name="Task"),
            repository=types.SimpleNamespace(name_with_owner="kewisch/test"),
        )
        issue = types.SimpleNamespace(
            id="ISSUE",
            number=2,
            url="https://github.com/kewisch/test/issues/2",
            issue_type=types.SimpleNamespace(name=self.github.milestones_issue_type),
            parent=parent,
            repository=types.SimpleNamespace(name_with_owner="kewisch/test"),
            sub_issues=types.SimpleNamespace(nodes=[]),
        )

        await self.github._fixup_issue_milestone_with_parent(issue)
        self.assertIsNone(issue.parent)

    def _make_parent(self, type_name):
        return types.SimpleNamespace(
            id="PARENT",
            number=1,
            issue_type=types.SimpleNamespace(name=type_name) if type_name else None,
            repository=types.SimpleNamespace(name_with_owner="kewisch/test"),
        )

    def _make_typed_issue(self, type_name, parent=None):
        return types.SimpleNamespace(
            id="ISSUE",
            number=2,
            url="https://github.com/kewisch/test/issues/2",
            issue_type=types.SimpleNamespace(name=type_name),
            parent=parent,
            repository=types.SimpleNamespace(name_with_owner="kewisch/test"),
            sub_issues=types.SimpleNamespace(nodes=[]),
        )

    async def test_fixup_epic_parent_untyped_removed_by_default(self):
        self.github._get_project_items = MagicMock(return_value=(None, None))
        self.github.dry = True
        self.github.epics_issue_type = "Epic"

        issue = self._make_typed_issue("Epic", self._make_parent(None))

        await self.github._fixup_issue_milestone_with_parent(issue)
        self.assertIsNone(issue.parent)

    async def test_fixup_epic_parent_untyped_allowed_when_configured(self):
        self.github._get_project_items = MagicMock(return_value=(None, None))
        self.github.dry = True
        self.github.epics_issue_type = "Epic"
        self.github.epics_allow_parents = True

        issue = self._make_typed_issue("Epic", self._make_parent(None))

        await self.github._fixup_issue_milestone_with_parent(issue)
        self.assertIsNotNone(issue.parent)

    async def test_fixup_epic_parent_typed_removed_when_parents_allowed(self):
        self.github._get_project_items = MagicMock(return_value=(None, None))
        self.github.dry = True
        self.github.epics_issue_type = "Epic"
        self.github.epics_allow_parents = True

        issue = self._make_typed_issue("Epic", self._make_parent("Program"))

        await self.github._fixup_issue_milestone_with_parent(issue)
        self.assertIsNone(issue.parent)

    async def test_fixup_epic_allowed_parent_stays_on_milestones_project(self):
        milestones_project = types.SimpleNamespace(remove_project_from_issue=AsyncMock())
        self.github._get_project_items = MagicMock(return_value=(None, object()))
        self.github._comment_on_issue = AsyncMock()
        self.github.github_milestones_projects = {"kewisch/test": milestones_project}
        self.github.dry = False
        self.github.epics_issue_type = "Epic"
        self.github.epics_allow_parents = True

        issue = self._make_typed_issue("Epic", self._make_parent(None))

        await self.github._fixup_issue_milestone_with_parent(issue)
        self.assertIsNotNone(issue.parent)
        milestones_project.remove_project_from_issue.assert_not_called()
        self.github._comment_on_issue.assert_not_called()

    def test_is_deeply_nested_subissue(self):
        self.github.milestones_issue_type = "Milestone"
        self.github.epics_issue_type = "Epic"

        with self.subTest(msg="no parent"):
            issue = types.SimpleNamespace(parent=None)
            self.assertFalse(self.github._is_deeply_nested_subissue(issue))

        with self.subTest(msg="parent is a milestone"):
            issue = types.SimpleNamespace(parent=self._make_parent("Milestone"))
            self.assertFalse(self.github._is_deeply_nested_subissue(issue))

        with self.subTest(msg="parent is an epic"):
            issue = types.SimpleNamespace(parent=self._make_parent("Epic"))
            self.assertFalse(self.github._is_deeply_nested_subissue(issue))

        with self.subTest(msg="untyped parent is treated as valid"):
            issue = types.SimpleNamespace(parent=self._make_parent(None))
            self.assertFalse(self.github._is_deeply_nested_subissue(issue))

        with self.subTest(msg="parent is a regular task"):
            issue = types.SimpleNamespace(parent=self._make_parent("Task"))
            self.assertTrue(self.github._is_deeply_nested_subissue(issue))
