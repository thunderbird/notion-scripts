import unittest
import json
import datetime
import dataclasses

from mzla_notion.tracker.bugzilla import Bugzilla, BugzillaUserMap
from mzla_notion.tracker.common import IssueRef, Issue, User

from .handlers import BaseTestCase


class BugzillaProjectTest(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.bugzilla = Bugzilla(base_url="https://bugzilla.dev", token="BUGZILLA_TOKEN", dry=False, user_map={})

        day1 = datetime.date.fromisoformat("2025-07-05")
        self.issue = Issue(
            id="1944850",
            repo="bugzilla.dev",
            title="title",
            description="description",
            state="NEW",
            priority="priority",
            assignees=[],
            labels=[],
            url="https://bugzilla.dev/show_bug.cgi?id=123",
            notion_url="https://www.notion.so/mzthunderbird/b183c949289f4282864cd373cb8b2cb7",
            start_date=day1,
            end_date=day1,
            sprint=None,
            sub_issues=[],
        )

    async def test_bugzilla_update_milestone_issue(self):
        day2 = datetime.date.fromisoformat("2025-07-04")

        old_issue = self.issue
        new_issue = dataclasses.replace(
            old_issue,
            title="title2",
            labels=[],
            description="description2",
            state="ASSIGNED",
            priority="priority2",
            assignees=[],
            url="https://bugzilla.dev/show_bug.cgi?id=234",
            notion_url="https://www.notion.so/mzthunderbird/123123123",
            start_date=day2,
            end_date=day2,
            sprint=None,
            sub_issues=[],
        )

        await self.bugzilla.update_milestone_issue(old_issue, new_issue)

        self.assertEqual(self.respx.routes["bugs_update"].calls.call_count, 1)
        issue = json.loads(self.respx.routes["bugs_update"].calls.last.request.content)

        self.assertEqual(issue["summary"], "title2")
        self.assertEqual(issue["priority"], "priority2")
        self.assertEqual(issue["cf_user_story"], "description2")
        self.assertEqual(issue["status"], "ASSIGNED")
        self.assertEqual(
            issue["see_also"],
            {
                "add": ["https://www.notion.so/mzthunderbird/123123123"],
                "remove": ["https://www.notion.so/mzthunderbird/b183c949289f4282864cd373cb8b2cb7"],
            },
        )

        # Move from open to resolved
        self.respx.reset()
        new_issue.state = "RESOLVED"
        await self.bugzilla.update_milestone_issue(old_issue, new_issue)

        self.assertEqual(self.respx.routes["bugs_update"].calls.call_count, 1)
        issue = json.loads(self.respx.routes["bugs_update"].calls.last.request.content)

        self.assertEqual(issue["status"], "RESOLVED")
        self.assertEqual(issue["resolution"], "FIXED")

        # Move from resolved to open
        self.respx.reset()
        old_issue.state = "RESOLVED"
        new_issue.state = "REOPENED"
        await self.bugzilla.update_milestone_issue(old_issue, new_issue)

        self.assertEqual(self.respx.routes["bugs_update"].calls.call_count, 1)
        issue = json.loads(self.respx.routes["bugs_update"].calls.last.request.content)

        self.assertEqual(issue["status"], "REOPENED")
        self.assertEqual(issue["resolution"], "")

        # Community assignee
        user_map = BugzillaUserMap({}, {"staff@example.com": "3f92ed7d-9ca8-4266-98d7-4604ea623c46"})

        self.respx.reset()
        old_issue.assignees = [User(user_map, tracker_user="community@example.com")]
        await self.bugzilla.update_milestone_issue(old_issue, new_issue)
        old_issue.assignees = []
        new_issue.assignees = [User(user_map, tracker_user="community@example.com")]
        await self.bugzilla.update_milestone_issue(old_issue, new_issue)
        old_issue.assignees = [User(user_map, tracker_user="staff@example.com")]
        new_issue.assignees = [User(user_map, tracker_user="staff2@example.com")]
        await self.bugzilla.update_milestone_issue(old_issue, new_issue)

        self.assertEqual(self.respx.routes["bugs_update"].calls.call_count, 3)

        issue = json.loads(self.respx.routes["bugs_update"].calls[0].request.content)
        self.assertNotIn("assigned_to", issue)

        issue = json.loads(self.respx.routes["bugs_update"].calls[1].request.content)
        self.assertEqual(issue["assigned_to"], "community@example.com")

        issue = json.loads(self.respx.routes["bugs_update"].calls[2].request.content)
        self.assertEqual(issue["assigned_to"], "staff2@example.com")

    async def test_bugzilla_get_issues_by_number(self):
        issues = await self.bugzilla.get_issues_by_number(
            [IssueRef(repo="bugzilla.dev", id="1944850"), IssueRef(repo="bugzilla.dev", id="1944885")], True
        )

        self.assertEqual(self.respx.routes["bugs_get"].calls.call_count, 1)
        self.assertEqual(self.respx.routes["bugs_get"].calls.last.request.url.params["id"], "1944850,1944885")

        issue = issues["1944850"]

        self.assertEqual(issue.id, "1944850")
        self.assertEqual(issue.repo, "bugzilla.dev")
        self.assertEqual(issue.url, "https://bugzilla.dev/show_bug.cgi?id=1944850")
        self.assertEqual(issue.title, "[meta] Rebuild the calendar Read Event dialog")
        self.assertEqual(issue.state, "NEW")
        self.assertEqual(issue.labels, set())
        self.assertEqual(issue.description, "Rebuild the Read Event dialog based on designs in blabla")
        self.assertEqual(issue.assignees, set())
        self.assertEqual(issue.priority, None)
        self.assertEqual(issue.parents, [IssueRef(repo="bugzilla.dev", id="1944847")])
        self.assertEqual(len(issue.sub_issues), 1)
        self.assertEqual(issue.sub_issues[0].id, "1944885")

        issue = issues["1944885"]

        self.assertEqual(issue.state, "IN REVIEW")
        self.assertEqual(issue.review_url, "https://phabricator.services.mozilla.com/D248065")
        self.assertEqual(issue.notion_url, "https://www.notion.so/mzthunderbird/b183c949289f4282864cd373cb8b2cb7")

    async def test_bugzilla_resolved_state(self):
        issues = await self.bugzilla.get_issues_by_number(
            [IssueRef(repo="bugzilla.dev", id="1849476"), IssueRef(repo="bugzilla.dev", id="1944885")], True
        )

        issue = issues["1944885"]

        self.assertEqual(issue.state, "IN REVIEW")
        self.assertEqual(issue.closed_date, None)

        issue = issues["1849476"]

        self.assertEqual(issue.state, "RESOLVED")
        self.assertEqual(issue.closed_date, datetime.datetime(2025, 2, 6, 10, 18, 39, tzinfo=datetime.timezone.utc))

    def test_parse_issueref_allowed(self):
        res = self.bugzilla.parse_issueref("https://bugzilla.dev/show_bug.cgi?garbage=1&id=2")
        self.assertEqual(res, IssueRef(repo="bugzilla.dev", id="2"))

        res = self.bugzilla.parse_issueref("https://BANANAS")
        self.assertIsNone(res)

        self.assertTrue(self.bugzilla.is_repo_allowed("bugzilla.dev"))

    def test_notion_tasks_prefix(self):
        res = self.bugzilla.notion_tasks_title("[PREFIX] ", self.issue)
        self.assertEqual(res, "[PREFIX] title - bug 1944850")

    def test_usermap(self):
        user_map = BugzillaUserMap(
            self.bugzilla.sync_client, {"staff@example.com": "3f92ed7d-9ca8-4266-98d7-4604ea623c46"}
        )

        self.assertEqual(user_map.tracker_mention("staff@example.com"), "Staff user")
        self.assertEqual(user_map.tracker_to_notion("staff@example.com"), "3f92ed7d-9ca8-4266-98d7-4604ea623c46")
        self.assertEqual(user_map.notion_to_tracker("3f92ed7d-9ca8-4266-98d7-4604ea623c46"), "staff@example.com")


if __name__ == "__main__":
    unittest.main()
