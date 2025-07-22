import sys
import json
import urllib
import datetime

from pathlib import Path

sys.path.insert(0, Path(__file__).parent.parent)
from libs.project_sync.common import IssueRef, Issue, IssueTracker, Sprint
from libs.project_sync.sync import ProjectSync

from freezegun import freeze_time
from unittest.mock import MagicMock

from .handlers import BaseTestCase

USER_MAP = {"user1@example.com": "a5fba708-e170-4a68-8392-ba6894272c70"}

TEST_PROPERTY_NAMES = {
    "notion_milestones_title": "Title",
    "notion_tasks_title": "Title",
    "notion_tasks_text_assignee": "Text Assignee",
    "notion_tasks_review_url": "Review URL",
    "notion_sprint_tracker_id": "TestTracker ID",
}


class TestTracker(IssueTracker):
    name = "TestTracker"

    def __init__(self, user_map={}, issues=[], property_names={}, **kwargs):
        all_props = {**TEST_PROPERTY_NAMES, **property_names}
        super().__init__(property_names=all_props, **kwargs)
        self.user_map = user_map
        self.issues = {str(issue.id): issue for issue in issues}
        self.additional_tasks = []

        self.update_milestone_issue = MagicMock(wraps=self.update_milestone_issue)
        self.get_issues_by_number = MagicMock(wraps=self.get_issues_by_number)

    def parse_issueref(self, ref):
        res = urllib.parse.urlparse(ref)

        if res.netloc == "example.com":
            parts = res.path.split("/")
            return IssueRef(repo=parts[1], id=parts[2])
        else:
            return None

    def get_issues_by_number(self, issues, sub_issues=False):
        return {issue.id: self.issues[issue.id] for issue in issues if issue.id in self.issues}

    def update_milestone_issue(self, old_issue, new_issue):
        pass

    def notion_tasks_title(self, prefix, issue):
        return f"{prefix}- test - {issue.title}"

    def collect_additional_tasks(self, collected_tasks):
        for task in self.additional_tasks:
            collected_tasks[task.repo][task.id] = None

    def get_sprints(self):
        return [
            Sprint(
                id="1",
                name="Sprint 1",
                status="Past",
                start_date=datetime.date(2025, 1, 1),
                end_date=datetime.date(2025, 1, 7),
            ),
            Sprint(
                id="2",
                name="Sprint 2",
                status="Current",
                start_date=datetime.date(2025, 1, 8),
                end_date=datetime.date(2025, 1, 15),
            ),
            Sprint(
                id="3",
                name="Sprint 3",
                status="Future",
                start_date=datetime.date(2025, 1, 16),
                end_date=datetime.date(2025, 1, 23),
            ),
        ]


class ProjectSyncTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self._total_expected_count = 0

        self.issues = [
            Issue(
                repo="repo",
                id="123",
                title="Rebuild the calendar Read Event dialog",
                description="description",
                state="NEW",
                priority=None,
                url="https://example.com/repo/123",
                notion_url="https://notion.so/example/rebuild-event-read-dialog-726fac286b6348ca90ec0066be1a2755",
            ),
            Issue(
                parents=[IssueRef(repo="repo", id="123")],
                repo="repo",
                id="234",
                title="Subissue 1",
                description="description",
                state="NEW",
                priority=None,
                url="https://example.com/repo/234",
            ),
            Issue(
                parents=[IssueRef(repo="repo", id="123")],
                repo="repo",
                id="345",
                title="Subissue 2",
                description="description",
                state="NEW",
                priority=None,
                url="https://example.com/repo/345",
            ),
        ]
        self.issues[0].sub_issues = [
            IssueRef(repo="repo", id="234", parents=[self.issues[0]]),
            IssueRef(repo="repo", id="345", parents=[self.issues[0]]),
        ]

    def expect_call(self, route, amount):
        self._total_expected_count += amount
        self.assertEqual(self.respx.routes[route].calls.call_count, amount)

    def expect_total_calls(self):
        if self.respx.calls.call_count != self._total_expected_count:
            from pprint import pprint

            pprint(self.respx.calls)

        self.assertEqual(self.respx.calls.call_count, self._total_expected_count)

    def expect_reset(self):
        self._total_expected_count = 0
        self.respx.reset()

    def expect_typical_db_update(self):
        db_count = 3 if self.project_sync.sprint_db else 2

        self.expect_call("db_info", 0 if self.project_sync.dry else db_count)
        self.expect_call("db_update", 0 if self.project_sync.dry else db_count)
        self.expect_call("db_query", db_count)

    def synchronize_project(self, tracker, **kwargs):
        sync_kwargs_defaults = {
            "project_key": "test",
            "tracker": tracker,
            "notion_token": "NOTION_TOKEN",
            "milestones_id": "milestones_id",
            "tasks_id": "tasks_id",
            "sprint_id": None,
            "milestones_body_sync": False,
            "milestones_body_sync_if_empty": False,
            "tasks_body_sync": False,
            "milestones_tracker_prefix": "",
            "milestones_extra_label": None,
            "tasks_notion_prefix": "[tasks_notion_prefix] ",
            "sprints_merge_by_name": False,
            "dry": False,
        }
        self.project_sync = ProjectSync(**{**sync_kwargs_defaults, **kwargs})
        self.project_sync.synchronize()

    @freeze_time("2023-01-01 12:13:14")
    def test_update_sync_stamp(self):
        self.notion_handler.milestones_handler.pages = []
        tracker = TestTracker(dry=True)

        # Dry run, no updates
        self.synchronize_project(tracker, dry=True)
        self.expect_typical_db_update()
        self.expect_total_calls()

        # Not a dry run
        self.expect_reset()
        self.synchronize_project(tracker, dry=False)
        self.expect_typical_db_update()

        last_update = {
            "description": [
                {
                    "type": "text",
                    "text": {"content": "Last Issue Tracker Sync (test): 2023-01-01T12:13:14Z\n\nPrevious Content"},
                }
            ]
        }
        self.assertEqual(json.loads(self.respx.routes["db_update"].calls[0].request.content), last_update)

        last_update["description"][0]["text"]["content"] = "Last Issue Tracker Sync (test): 2023-01-01T12:13:14Z\n\n"
        self.assertEqual(json.loads(self.respx.routes["db_update"].calls[1].request.content), last_update)

        self.expect_total_calls()

    def test_milestone_sync_single_no_children_no_updates(self):
        # Only milestone issue
        issue = self.issues[0]
        issue.sub_issues = []
        tracker = TestTracker(issues=[issue], dry=False)

        with self.assertLogs("project_sync", level="INFO") as logs:
            self.synchronize_project(tracker)

        # There is a second milestone with an invalid url, it should not sync
        self.assertIn("INFO:project_sync:Synchronizing 1 milestones for repo", logs.output)

        # Query database tasks and milestones
        self.expect_typical_db_update()
        self.assertEqual(self.respx.routes["db_query"].calls[0].request.url.path, "/v1/databases/milestones_id/query")
        self.assertEqual(self.respx.routes["db_query"].calls[1].request.url.path, "/v1/databases/tasks_id/query")

        # There should be one issue retrieved as a milestone
        self.assertEqual(tracker.get_issues_by_number.call_count, 2)
        self.assertEqual(len(tracker.get_issues_by_number.call_args_list[0].args[0]), 1)
        self.assertEqual(tracker.get_issues_by_number.call_args_list[0].args[0][0].id, "123")

        # No updates
        self.assertEqual(tracker.update_milestone_issue.call_count, 0)

        self.expect_total_calls()

    def test_milestone_sync_single_no_children_with_update(self):
        self.issues[0].title = "Title will be changed"
        tracker = TestTracker(issues=self.issues, dry=False)

        self.synchronize_project(tracker)
        self.assertEqual(tracker.update_milestone_issue.call_count, 1)
        self.assertEqual(tracker.update_milestone_issue.call_args[0][0].title, "Title will be changed")
        self.assertEqual(tracker.update_milestone_issue.call_args[0][1].title, "Rebuild the calendar Read Event dialog")

        # Description should not change, body sync is off
        self.assertEqual(tracker.update_milestone_issue.call_args[0][1].description, "description")

    def test_milestone_sync_single_no_children_dry(self):
        tracker = TestTracker(issues=self.issues, dry=True)

        self.synchronize_project(tracker, dry=True)
        self.assertEqual(tracker.update_milestone_issue.call_count, 0)

    def test_milestone_sync_apply_extra_label(self):
        # Only milestone issue
        issue = self.issues[0]
        issue.sub_issues = []

        tracker = TestTracker(issues=[issue])

        self.synchronize_project(tracker, milestones_extra_label="extra-label")
        self.assertEqual(tracker.update_milestone_issue.call_count, 1)
        self.assertEqual(tracker.update_milestone_issue.call_args[0][0].labels, set())
        self.assertEqual(tracker.update_milestone_issue.call_args[0][1].labels, {"extra-label"})

    def test_milestone_sync_with_task(self):
        tracker = TestTracker(issues=self.issues)
        self.synchronize_project(tracker)

        self.expect_typical_db_update()

        # Create the task to synchronize
        self.expect_call("pages_create", 1)
        self.assertEqual(
            json.loads(self.respx.routes["pages_create"].calls.last.request.content),
            {
                "parent": {"database_id": "tasks_id"},
                "properties": {
                    "Dates": {"date": None},
                    "Issue Link": {"url": "https://example.com/repo/234"},
                    "Owner": {"type": "people", "people": []},
                    "Priority": {"select": None},
                    "Project": {"relation": [{"id": "726fac28-6b63-48ca-90ec-0066be1a2755"}]},
                    "Status": {"status": {"name": "NEW"}},
                    "Title": {
                        "title": [{"text": {"content": "[tasks_notion_prefix] - test - Subissue 1"}}],
                        "type": "title",
                    },
                    "Text Assignee": {"rich_text": [{"text": {"content": ""}}]},
                    "Review URL": {"url": None},
                },
            },
        )

        self.expect_call("pages_update", 1)
        self.assertEqual(
            json.loads(self.respx.routes["pages_update"].calls.last.request.content)["properties"]["Issue Link"]["url"],
            "https://example.com/repo/345",
        )

        # Get existing children
        self.expect_call("pages_child_get", 1)

        # Update to task body warning
        self.expect_call("pages_child_update", 1)
        update_content = json.loads(self.respx.routes["pages_child_update"].calls.last.request.content)

        self.assertEqual(update_content["children"][0]["paragraph"]["rich_text"][0]["text"]["content"], "ℹ️ ")
        self.assertEqual(
            update_content["children"][0]["paragraph"]["rich_text"][1]["text"]["content"],
            "This task synchronizes with TestTracker. Any changes you make here will be overwritten.",
        )

        # Update database info
        self.expect_total_calls()

    def test_milestone_sync_with_task_sync_body(self):
        # Remove 234
        del self.issues[1]
        del self.issues[0].sub_issues[0]

        tracker = TestTracker(issues=self.issues)
        self.synchronize_project(tracker, tasks_body_sync=True)

        self.expect_call("pages_update", 1)
        self.expect_call("pages_child_get", 1)

        # Update to task body warning
        self.expect_call("pages_child_update", 1)
        update_content = json.loads(self.respx.routes["pages_child_update"].calls.last.request.content)

        self.assertEqual(update_content["children"][0]["paragraph"]["rich_text"][0]["text"]["content"], "ℹ️ ")
        self.assertEqual(
            update_content["children"][0]["paragraph"]["rich_text"][1]["text"]["content"],
            "This task synchronizes with TestTracker. Any changes you make here will be overwritten.",
        )

        # Update database info
        self.expect_typical_db_update()
        self.expect_total_calls()

    def test_milestone_sync_single_with_body(self):
        """Tests the milestones_body_sync setting."""
        issue = self.issues[0]
        issue.sub_issues = []
        tracker = TestTracker(issues=[issue], dry=False)

        self.synchronize_project(tracker, milestones_body_sync=True)
        self.expect_call("pages_child_get", 1)

        self.assertEqual(tracker.update_milestone_issue.call_count, 1)
        self.assertEqual(
            tracker.update_milestone_issue.call_args[0][1].description, "\n_This is some page content._\n\n"
        )

        self.expect_typical_db_update()
        self.expect_total_calls()

    def test_milestone_sync_single_with_body_if_empty(self):
        """Tests the milestones_body_sync_if_empty setting."""
        self.issues[0].sub_issues = []
        issues = [self.issues[0]]

        tracker = TestTracker(issues=issues, dry=False)

        with self.subTest(msg="not empty"):
            self.synchronize_project(tracker, milestones_body_sync_if_empty=True)
            self.expect_call("pages_child_get", 0)

            self.assertEqual(tracker.update_milestone_issue.call_count, 0)

            self.expect_typical_db_update()
            self.expect_total_calls()

        self.expect_reset()

        with self.subTest(msg="empty"):
            issues[0].description = ""

            self.synchronize_project(tracker, milestones_body_sync_if_empty=True)
            self.expect_call("pages_child_get", 1)

            self.assertEqual(tracker.update_milestone_issue.call_count, 1)
            self.assertEqual(
                tracker.update_milestone_issue.call_args[0][1].description, "\n_This is some page content._\n\n"
            )

            self.expect_typical_db_update()
            self.expect_total_calls()

    def test_milestone_sync_with_sprint(self):
        tracker = TestTracker(issues=self.issues)

        self.issues[1].sprint = tracker.get_sprints()[1]
        self.issues[2].sprint = tracker.get_sprints()[2]

        self.synchronize_project(tracker, sprint_id="sprints_id")

        self.expect_typical_db_update()

        # Create the task to synchronize
        self.expect_call("pages_create", 3)
        self.assertEqual(
            json.loads(self.respx.routes["pages_create"].calls[0].request.content),
            {
                "parent": {"database_id": "sprints_id"},
                "properties": {
                    "Sprint name": {"type": "title", "title": [{"text": {"content": "Sprint 1"}}]},
                    "Dates": {"date": {"start": "2025-01-01", "end": "2025-01-07"}},
                    "Sprint status": {"status": {"name": "Past"}},
                    "TestTracker ID": {"rich_text": [{"text": {"content": "1"}}]},
                },
            },
        )
        self.assertEqual(
            json.loads(self.respx.routes["pages_create"].calls[1].request.content),
            {
                "parent": {"database_id": "sprints_id"},
                "properties": {
                    "Sprint name": {"type": "title", "title": [{"text": {"content": "Sprint 3"}}]},
                    "Dates": {"date": {"start": "2025-01-16", "end": "2025-01-23"}},
                    "Sprint status": {"status": {"name": "Future"}},
                    "TestTracker ID": {"rich_text": [{"text": {"content": "3"}}]},
                },
            },
        )

        self.expect_call("pages_update", 2)
        self.assertEqual(
            json.loads(self.respx.routes["pages_update"].calls[0].request.content),
            {
                "properties": {
                    "Sprint name": {"type": "title", "title": [{"text": {"content": "Sprint 2"}}]},
                    "Dates": {"date": {"start": "2025-01-08", "end": "2025-01-15"}},
                    "Sprint status": {"status": {"name": "Current"}},
                },
            },
        )

        sprint_3_id = json.loads(self.respx.routes["pages_create"].calls[1].response.content)["id"]

        self.assertEqual(
            json.loads(self.respx.routes["pages_update"].calls[1].request.content),
            {
                "properties": {
                    "Status": {"status": {"name": "NEW"}},
                    "Title": {
                        "type": "title",
                        "title": [{"text": {"content": "[tasks_notion_prefix] - test - Subissue 2"}}],
                    },
                    "Issue Link": {"url": "https://example.com/repo/345"},
                    "Owner": {"type": "people", "people": []},
                    "Text Assignee": {"rich_text": [{"text": {"content": ""}}]},
                    "Priority": {"select": None},
                    "Review URL": {"url": None},
                    "Dates": {"date": {"start": "2025-01-16", "end": "2025-01-23"}},
                    "Sprint": {"relation": [{"id": sprint_3_id}]},
                    "Project": {"relation": [{"id": "726fac28-6b63-48ca-90ec-0066be1a2755"}]},
                }
            },
        )

        self.assertEqual(
            json.loads(self.respx.routes["pages_create"].calls[2].request.content),
            {
                "parent": {"database_id": "tasks_id"},
                "properties": {
                    "Dates": {"date": {"end": "2025-01-15", "start": "2025-01-08"}},
                    "Issue Link": {"url": "https://example.com/repo/234"},
                    "Owner": {"type": "people", "people": []},
                    "Priority": {"select": None},
                    "Project": {"relation": [{"id": "726fac28-6b63-48ca-90ec-0066be1a2755"}]},
                    "Status": {"status": {"name": "NEW"}},
                    "Sprint": {"relation": [{"id": "1c5dea4a-dcdf-8159-948b-f193a527ef1a"}]},
                    "Title": {
                        "title": [{"text": {"content": "[tasks_notion_prefix] - test - Subissue 1"}}],
                        "type": "title",
                    },
                    "Text Assignee": {"rich_text": [{"text": {"content": ""}}]},
                    "Review URL": {"url": None},
                },
            },
        )

        # Remaining calls tested in other tests
        self.expect_call("pages_child_get", 1)
        self.expect_call("pages_child_update", 1)
        self.expect_total_calls()

    def test_milestone_sync_with_sprint_merge_by_title(self):
        tracker = TestTracker(issues=self.issues)

        self.issues[1].sprint = tracker.get_sprints()[1]
        self.issues[2].sprint = tracker.get_sprints()[2]

        self.synchronize_project(tracker, sprint_id="sprints_id", sprints_merge_by_name=True)

        self.expect_typical_db_update()

        # Create the task to synchronize
        self.expect_call("pages_create", 2)
        self.assertEqual(
            json.loads(self.respx.routes["pages_create"].calls[0].request.content),
            {
                "parent": {"database_id": "sprints_id"},
                "properties": {
                    "Sprint name": {"type": "title", "title": [{"text": {"content": "Sprint 1"}}]},
                    "Dates": {"date": {"start": "2025-01-01", "end": "2025-01-07"}},
                    "Sprint status": {"status": {"name": "Past"}},
                    "TestTracker ID": {"rich_text": [{"text": {"content": "1"}}]},
                },
            },
        )

        self.expect_call("pages_update", 3)
        self.assertEqual(
            json.loads(self.respx.routes["pages_update"].calls[0].request.content),
            {
                "properties": {
                    "Sprint name": {"type": "title", "title": [{"text": {"content": "Sprint 2"}}]},
                    "Dates": {"date": {"start": "2025-01-08", "end": "2025-01-15"}},
                    "Sprint status": {"status": {"name": "Current"}},
                },
            },
        )
        self.assertEqual(
            json.loads(self.respx.routes["pages_update"].calls[1].request.content),
            {
                "properties": {
                    "TestTracker ID": {"rich_text": [{"text": {"content": "three\n3"}}]},
                },
            },
        )

        self.assertEqual(
            json.loads(self.respx.routes["pages_create"].calls[1].request.content),
            {
                "parent": {"database_id": "tasks_id"},
                "properties": {
                    "Dates": {"date": {"end": "2025-01-15", "start": "2025-01-08"}},
                    "Issue Link": {"url": "https://example.com/repo/234"},
                    "Owner": {"type": "people", "people": []},
                    "Priority": {"select": None},
                    "Project": {"relation": [{"id": "726fac28-6b63-48ca-90ec-0066be1a2755"}]},
                    "Status": {"status": {"name": "NEW"}},
                    "Sprint": {"relation": [{"id": "1c5dea4a-dcdf-8159-948b-f193a527ef1a"}]},
                    "Title": {
                        "title": [{"text": {"content": "[tasks_notion_prefix] - test - Subissue 1"}}],
                        "type": "title",
                    },
                    "Text Assignee": {"rich_text": [{"text": {"content": ""}}]},
                    "Review URL": {"url": None},
                },
            },
        )
        self.assertEqual(
            json.loads(self.respx.routes["pages_update"].calls[2].request.content),
            {
                "properties": {
                    "Dates": {"date": {"end": "2025-01-23", "start": "2025-01-16"}},
                    "Issue Link": {"url": "https://example.com/repo/345"},
                    "Owner": {"type": "people", "people": []},
                    "Priority": {"select": None},
                    "Project": {"relation": [{"id": "726fac28-6b63-48ca-90ec-0066be1a2755"}]},
                    "Status": {"status": {"name": "NEW"}},
                    "Sprint": {"relation": [{"id": "89cc4fa2-f788-430d-a337-64a9aa6cb0ab"}]},
                    "Title": {
                        "title": [{"text": {"content": "[tasks_notion_prefix] - test - Subissue 2"}}],
                        "type": "title",
                    },
                    "Text Assignee": {"rich_text": [{"text": {"content": ""}}]},
                    "Review URL": {"url": None},
                },
            },
        )

        self.expect_call("pages_child_get", 1)
        self.expect_call("pages_child_update", 1)
        self.expect_total_calls()

    def test_milestone_sync_with_sprint_merge_by_title_date_mismatch(self):
        tracker = TestTracker(issues=self.issues)
        self.issues[1].sprint = tracker.get_sprints()[1]
        self.issues[2].sprint = tracker.get_sprints()[2]

        with self.subTest(msg="end date"):
            self.notion_handler.sprints_handler.pages[1]["properties"]["Dates"]["date"]["end"] = "2025-01-24"
            with self.assertRaisesRegex(
                Exception, r"Could not merge sprint Sprint 3, end dates mismatch! 2025-01-24 != 2025-01-23"
            ):
                self.synchronize_project(tracker, sprint_id="sprints_id", sprints_merge_by_name=True)

            self.notion_handler.sprints_handler.pages[1]["properties"]["Dates"]["date"]["end"] = "2025-01-23"

        with self.subTest(msg="start date"):
            self.notion_handler.sprints_handler.pages[1]["properties"]["Dates"]["date"]["start"] = "2025-01-15"

            with self.assertRaisesRegex(
                Exception, r"Could not merge sprint Sprint 3, start dates mismatch! 2025-01-15 != 2025-01-16"
            ):
                self.synchronize_project(tracker, sprint_id="sprints_id", sprints_merge_by_name=True)

    def test_task_with_dates(self):
        self.issues[2].start_date = datetime.date(2025, 4, 1)
        self.issues[2].end_date = datetime.date(2025, 4, 7)

        tracker = TestTracker(issues=self.issues)
        self.issues[2].sprint = tracker.get_sprints()[1]

        self.synchronize_project(tracker, sprint_id="sprints_id")

        # Uses augmented dates, but still associated with the original sprint
        self.assertEqual(
            json.loads(self.respx.routes["pages_update"].calls[1].request.content),
            {
                "properties": {
                    "Dates": {"date": {"end": "2025-04-07", "start": "2025-04-01"}},
                    "Issue Link": {"url": "https://example.com/repo/345"},
                    "Owner": {"type": "people", "people": []},
                    "Priority": {"select": None},
                    "Project": {"relation": [{"id": "726fac28-6b63-48ca-90ec-0066be1a2755"}]},
                    "Status": {"status": {"name": "NEW"}},
                    "Sprint": {"relation": [{"id": "1c5dea4a-dcdf-8159-948b-f193a527ef1a"}]},
                    "Title": {
                        "title": [{"text": {"content": "[tasks_notion_prefix] - test - Subissue 2"}}],
                        "type": "title",
                    },
                    "Text Assignee": {"rich_text": [{"text": {"content": ""}}]},
                    "Review URL": {"url": None},
                },
            },
        )

    def test_task_no_parent(self):
        self.issues[1].parents = []

        tracker = TestTracker(issues=self.issues)
        tracker.additional_tasks = [IssueRef(id="234", repo="repo")]

        self.synchronize_project(tracker)

        self.expect_call("pages_create", 1)
        self.assertEqual(
            json.loads(self.respx.routes["pages_create"].calls.last.request.content),
            {
                "parent": {"database_id": "tasks_id"},
                "properties": {
                    "Dates": {"date": None},
                    "Issue Link": {"url": "https://example.com/repo/234"},
                    "Owner": {"type": "people", "people": []},
                    "Priority": {"select": None},
                    "Project": {"relation": []},
                    "Status": {"status": {"name": "NEW"}},
                    "Title": {
                        "title": [{"text": {"content": "[tasks_notion_prefix] - test - Subissue 1"}}],
                        "type": "title",
                    },
                    "Text Assignee": {"rich_text": [{"text": {"content": ""}}]},
                    "Review URL": {"url": None},
                },
            },
        )

    def test_task_wrong_title(self):
        tracker = TestTracker(
            issues=self.issues,
            property_names={
                "notion_milestones_title": "Headline",
            },
        )
        self.synchronize_project(tracker)

        self.assertEqual(tracker.update_milestone_issue.call_count, 1)
        self.assertEqual(tracker.update_milestone_issue.call_args[0][0].title, "Rebuild the calendar Read Event dialog")
        self.assertEqual(tracker.update_milestone_issue.call_args[0][1].title, "")
