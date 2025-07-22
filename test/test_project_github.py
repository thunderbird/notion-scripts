import sys
import datetime
import dataclasses

from pathlib import Path
from freezegun import freeze_time

sys.path.insert(0, Path(__file__).parent.parent)
from libs.project_sync import GitHub
from libs.project_sync.common import IssueRef, Sprint
from libs.project_sync.github import GitHubUserMap, LabelCache, GitHubIssue, GitHubUser

from .handlers import BaseTestCase

REPO_SETTINGS = {
    "reposetA": {
        "repositories": ["kewisch/test"],
        "github_tasks_project_id": "PVT_kwHOAAlD3s4AxVFW",
        "github_milestones_project_id": "PVT_kwHOAAlD3s4AxVDI",
    }
}


class GitHubProjectTest(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.github = GitHub(token="GITHUB_TOKEN", repositories=REPO_SETTINGS, user_map={}, dry=False)

    def test_github_get_issues_basics(self):
        issues = self.github.get_issues_by_number([], True)
        self.assertEqual(issues, {})

        with self.assertRaisesRegex(Exception, r"Can't yet query from different repositories"):
            self.github.get_issues_by_number(
                [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test2", id="1")], True
            )

    def test_github_get_issues_epics(self):
        issues = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )

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
        self.assertEqual(len(issue.assignees), 1)
        self.assertEqual(next(iter(issue.assignees)).tracker_user, "kewisch")
        self.assertEqual(issue.labels, {"type: epic"})
        self.assertEqual(issue.url, "https://github.com/kewisch/test/issues/1")
        self.assertEqual(issue.review_url, "")
        self.assertEqual(issue.notion_url, "")
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
        self.assertEqual(len(issue.assignees), 0)
        self.assertEqual(issue.labels, ["type: epic"])
        self.assertEqual(issue.url, "https://github.com/kewisch/test/issues/2")
        self.assertEqual(issue.review_url, "")
        self.assertEqual(issue.notion_url, "")
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

        self.assertEqual(len(self.github_handler.calls), 1)
        self.assertEqual(len(self.github_handler.calls["get_issues_1_and_2"]), 1)

    def test_github_get_issue_tasks(self):
        issues = self.github.get_issues_by_number([], True)
        self.assertEqual(issues, {})

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
            review_url="",
            notion_url="",
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
            issues = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="3")])
            self.assertEqual(issues["3"].gql.id, "I_kwDOMwGgpM6oWELp")

            issues["3"].gql = None
            self.assertEqual(issues, {"3": issue3})

        with freeze_time("2025-02-05"):
            issues = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="3")])
            self.assertEqual(issues["3"].gql.id, "I_kwDOMwGgpM6oWELp")

            issue3.sprint.status = "Current"

            issues["3"].gql = None
            self.assertEqual(issues, {"3": issue3})

        with freeze_time("2025-02-01"):
            issues = self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="3")])
            self.assertEqual(issues["3"].gql.id, "I_kwDOMwGgpM6oWELp")

            issue3.sprint.status = "Future"

            issues["3"].gql = None
            self.assertEqual(issues, {"3": issue3})

    def test_github_get_issue_both_projects(self):
        with self.assertRaisesRegex(
            Exception, r"Issue https://github.com/kewisch/test/issues/4 has both tasks and milestones project"
        ):
            self.github.get_issues_by_number([IssueRef(repo="kewisch/test", id="4")])

    def test_github_update_no_change(self):
        self.github.user_map = GitHubUserMap(
            self.github.endpoint,
            {"kewisch": "3df71ec3-17c7-4eb4-80bc-a321af157be6", "notkewisch": "b5a819b4-e2b3-432c-8e5a-256dace1176f"},
        )

        issues = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )

        old_issue = issues["1"]

        # A call without change shouldn't trigger anything
        self.github.update_milestone_issue(old_issue, old_issue)
        self.assertEqual(len(self.github_handler.calls), 2)
        self.assertEqual(len(self.github_handler.calls["get_users"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issues_1_and_2"]), 1)

    def test_github_update_milestone_issue(self):
        self.github.user_map = GitHubUserMap(
            self.github.endpoint,
            {"kewisch": "3df71ec3-17c7-4eb4-80bc-a321af157be6", "notkewisch": "b5a819b4-e2b3-432c-8e5a-256dace1176f"},
        )

        issues = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )

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

        self.github.update_milestone_issue(old_issue, new_issue)

        self.assertEqual(len(self.github_handler.calls), 8)

        self.assertEqual(len(self.github_handler.calls["get_users"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issues_1_and_2"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_basic_closed"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_assignees"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_labels"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_project"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_label_bug"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_project_info"]), 1)

    def test_github_update_issue_add_roadmap(self):
        self.github.user_map = GitHubUserMap(
            self.github.endpoint,
            {"kewisch": "3df71ec3-17c7-4eb4-80bc-a321af157be6", "notkewisch": "b5a819b4-e2b3-432c-8e5a-256dace1176f"},
        )

        issues = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )

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

        self.github.update_milestone_issue(old_issue, new_issue)

        self.assertEqual(len(self.github_handler.calls), 9)

        self.assertEqual(len(self.github_handler.calls["get_users"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issues_1_and_2"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_label_bug"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_project_info"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_basic"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_assignees"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_labels"]), 1)
        self.assertEqual(len(self.github_handler.calls["update_issue_1_project"]), 1)
        self.assertEqual(len(self.github_handler.calls["add_issue_to_project"]), 1)

    def test_github_update_issue_dry(self):
        self.github.dry = True

        self.github.user_map = GitHubUserMap(
            self.github.endpoint,
            {"kewisch": "3df71ec3-17c7-4eb4-80bc-a321af157be6", "notkewisch": "b5a819b4-e2b3-432c-8e5a-256dace1176f"},
        )

        issues = self.github.get_issues_by_number(
            [IssueRef(repo="kewisch/test", id="1"), IssueRef(repo="kewisch/test", id="2")], True
        )

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

        self.github.update_milestone_issue(old_issue, new_issue)

        self.assertEqual(len(self.github_handler.calls), 3)

        self.assertEqual(len(self.github_handler.calls["get_users"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_issues_1_and_2"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_label_bug"]), 1)

    @freeze_time("2025-02-24 12:13:14")
    def test_get_sprints(self):
        res = self.github.get_sprints()

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

    def test_collect_additional_tasks(self):
        collected_tasks = {"kewisch/test": {"4": None, "6": {"id": "mock_block"}}}

        self.github.collect_additional_tasks(collected_tasks)

        self.assertIn("3", collected_tasks["kewisch/test"])
        self.assertIn("4", collected_tasks["kewisch/test"])
        self.assertIn("6", collected_tasks["kewisch/test"])
        self.assertIsNone(collected_tasks["kewisch/test"]["3"])
        self.assertIsNone(collected_tasks["kewisch/test"]["4"])
        self.assertEqual(collected_tasks["kewisch/test"]["6"], {"id": "mock_block"})

        self.assertEqual(len(self.github_handler.calls), 1)
        self.assertEqual(len(self.github_handler.calls["get_sprint_tasks"]), 1)

    def test_parse_issueref_allowed(self):
        res = self.github.parse_issueref("https://github.com/kewisch/test/issues/1")
        self.assertEqual(res, IssueRef(repo="kewisch/test", id="1"))

        res = self.github.parse_issueref("https://BANANAS")
        self.assertIsNone(res)

        self.assertTrue(self.github.is_repo_allowed("kewisch/test"))
        self.assertFalse(self.github.is_repo_allowed("kewisch/test2"))

        self.assertEqual(len(self.github_handler.calls), 0)

    def test_label_cache(self):
        cache = LabelCache(self.github.endpoint)

        ab = cache.get_labels("org", "repo", ["a", "b"])
        bc = cache.get_labels("org", "repo", ["b", "c"])

        self.assertEqual(ab, {"a": "LA_kwDOMwGgpM8AAAABvAun4g", "b": "LA_kwDOMwGgpM8AAAABvAun6Q"})
        self.assertEqual(bc, {"b": "LA_kwDOMwGgpM8AAAABvAun6Q", "c": "LA_kwDOMwGgpM8AAAABvAun9Q"})

        self.assertEqual(len(self.github_handler.calls), 2)
        self.assertEqual(len(self.github_handler.calls["get_labels_ab"]), 1)
        self.assertEqual(len(self.github_handler.calls["get_labels_c"]), 1)

    def test_usermap(self):
        user_map = self.github.user_map = GitHubUserMap(
            self.github.endpoint,
            {"kewisch": "3df71ec3-17c7-4eb4-80bc-a321af157be6", "notkewisch": "b5a819b4-e2b3-432c-8e5a-256dace1176f"},
        )

        self.assertEqual(user_map.tracker_mention("kewisch"), "@kewisch")
        self.assertEqual(user_map.trk_to_dbid("kewisch"), "MDQ6VXNlcjYwNzE5OA==")
        self.assertEqual(user_map.dbid_to_trk("MDQ6VXNlcjYwNzE5OA=="), "kewisch")
        self.assertEqual(user_map.notion_to_dbid("3df71ec3-17c7-4eb4-80bc-a321af157be6"), "MDQ6VXNlcjYwNzE5OA==")
        self.assertEqual(user_map.dbid_to_notion("MDQ6VXNlcjYwNzE5OA=="), "3df71ec3-17c7-4eb4-80bc-a321af157be6")
        self.assertEqual(user_map.tracker_to_notion("kewisch"), "3df71ec3-17c7-4eb4-80bc-a321af157be6")
        self.assertEqual(user_map.notion_to_tracker("3df71ec3-17c7-4eb4-80bc-a321af157be6"), "kewisch")
