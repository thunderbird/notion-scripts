import datetime
import json
import sqlite3
import tempfile
import unittest

from pathlib import Path
from unittest.mock import AsyncMock

from freezegun import freeze_time

from mzla_notion.sync.twoway import TrackerTwoWaySync
from mzla_notion.tracker.common import Issue, IssueRef, IssueTracker, User, UserMap
from mzla_notion.util import NotionQueryIncompleteError

from .handlers import BaseTestCase


class StaticUserMap(UserMap):
    def tracker_mention(self, tracker_user):
        return tracker_user


class TwoWayTestTracker(IssueTracker):
    name = "TwoWayTestTracker"

    def __init__(self, issues, recent_ids=None, **kwargs):
        defaults = {
            "notion_milestones_title": "Title",
            "notion_milestones_assignee": "Owner",
            "notion_milestones_priority": "Priority",
            "notion_milestones_dates": "Dates",
            "notion_milestones_epic_relation": "Epic",
            "notion_epics_title": "Title",
            "notion_epics_assignee": "Owner",
            "notion_epics_priority": "Priority",
            "notion_epics_dates": "Dates",
            "notion_tasks_title": "Title",
            "notion_tasks_assignee": "Owner",
            "notion_tasks_dates": "Dates",
            "notion_tasks_milestone_relation": "Project",
            "notion_tasks_text_assignee": "Text Assignee",
            "notion_tasks_priority": "Priority",
            "notion_tasks_review_url": "Review URL",
            "notion_tasks_reviewers": "Peer Reviewer",
            "notion_tasks_repository": "Repository",
            "notion_tasks_labels": "Labels",
            "notion_tasks_sprint_relation": "Sprint",
            "notion_issue_field": "Issue Link",
        }
        filter_recent_by_since = kwargs.pop("filter_recent_by_since", False)
        property_names = {**defaults, **kwargs.pop("property_names", {})}
        super().__init__(property_names=property_names, **kwargs)
        self.user_map = StaticUserMap({})
        self.issues = {(issue.repo, issue.id): issue for issue in issues}
        self.recent_ids = set(recent_ids or [])
        self.filter_recent_by_since = filter_recent_by_since
        self.updated_milestones = []
        self.updated_tasks = []
        self.created_tasks = []
        self.recent_since_calls = []

    def parse_issueref(self, ref):
        parts = ref.split("/")
        if len(parts) == 5 and parts[2] == "example.com":
            return IssueRef(repo=parts[3], id=parts[4])
        return None

    async def get_issues_by_number(self, refs, sub_issues=False):
        for ref in refs:
            issue = self.issues.get((ref.repo, ref.id))
            if issue:
                yield issue

    async def get_recent_issues_by_repo(self, since, sub_issues=False):
        self.recent_since_calls.append(since)
        repos = {}
        for repo, issue_id in self.recent_ids:
            issue = self.issues.get((repo, issue_id))
            if issue:
                if self.filter_recent_by_since and issue.updated_date and issue.updated_date < since:
                    continue
                repos.setdefault(repo, {})[issue_id] = issue
        return repos

    async def update_milestone_issue(self, old_issue, new_issue):
        self.updated_milestones.append((old_issue, new_issue))

    async def update_task_issue(self, old_issue, new_issue):
        self.updated_tasks.append((old_issue, new_issue))

    async def create_task_issue_from_notion(
        self, parent_issue, title, description="", assignees=None, labels=None, estimate=None
    ):
        self.created_tasks.append((parent_issue, title, estimate))
        return Issue(
            repo=parent_issue.repo,
            id=f"c{len(self.created_tasks)}",
            parents=[IssueRef(repo=parent_issue.repo, id=parent_issue.id)],
            title=title,
            description=description,
            state="Backlog",
            priority="P2",
            estimate=estimate,
            assignees=set(),
            labels=set(),
            url=f"https://example.com/{parent_issue.repo}/c{len(self.created_tasks)}",
            created_date=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
            updated_date=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
            sub_issues=[],
        )


class TwoWaySyncTest(BaseTestCase):
    async def _run_sync(self, tracker, **kwargs):
        dry = kwargs.pop("dry", False)
        kwargs.setdefault("incremental_lookback_seconds", 604800)
        sync = TrackerTwoWaySync(
            project_key="twoway",
            tracker=tracker,
            notion_token="NOTION_TOKEN",
            milestones_id="milestones_id",
            tasks_id="tasks_id",
            tasks_notion_prefix="[prefix] ",
            dry=dry,
            **kwargs,
        )
        await sync.synchronize()

    def _issue(
        self, issue_id, *, updated, parents=None, title=None, state="Backlog", issue_type=None, deeply_nested=False
    ):
        return Issue(
            repo="repo",
            id=issue_id,
            parents=parents or [],
            title=title or f"Issue {issue_id}",
            description="desc",
            state=state,
            priority="P2",
            assignees=set(),
            labels=set(),
            url=f"https://example.com/repo/{issue_id}",
            created_date=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
            updated_date=updated,
            issue_type=issue_type,
            sub_issues=[],
            deeply_nested=deeply_nested,
        )

    def _assert_stats_row(self, logs, label, task_count, milestone_count):
        output = "\n".join(logs.output)
        self.assertRegex(output, rf"Two-way sync stats\s+{label}\s+{task_count}\s+{milestone_count}")

    def _set_epic_page_issue(self, issue_id):
        page = self.notion_handler.epics_handler.pages[0]
        page["properties"]["Issue Link"]["url"] = f"https://example.com/repo/{issue_id}"
        return page

    def _set_milestone_page_issue(self, issue_id):
        page = self.notion_handler.milestones_handler.pages[0]
        page["properties"]["Issue Link"]["url"] = f"https://example.com/repo/{issue_id}"
        return page

    def _add_unlinked_task_page(self, page_id="bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", url=None):
        page = {
            "object": "page",
            "id": page_id,
            "created_time": "2025-01-01T00:00:00.000Z",
            "last_edited_time": "2025-01-01T00:00:00.000Z",
            "url": url or f"https://notion.so/example/{page_id}",
            "properties": {
                "Title": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {"content": "Create me"},
                            "plain_text": "Create me",
                        }
                    ],
                },
                "Status": {
                    "id": "st",
                    "type": "status",
                    "status": {"name": "Backlog"},
                },
                "Issue Link": {"type": "files", "files": []},
                "Project": {
                    "type": "relation",
                    "relation": [{"id": "726fac28-6b63-48ca-90ec-0066be1a2755"}],
                },
            },
        }
        self.notion_handler.tasks_handler.pages.append(page)
        return page

    async def test_incremental_skips_when_not_recent(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue("123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc)),
                self._issue(
                    "234",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    parents=[IssueRef(repo="repo", id="123")],
                ),
            ],
            recent_ids=[],
        )

        await self._run_sync(tracker, incremental_lookback_seconds=604800)
        self.assertEqual(len(tracker.updated_milestones), 0)
        self.assertEqual(len(tracker.updated_tasks), 0)
        self.assertEqual(self.respx.routes["pages_update"].calls.call_count, 0)

    @freeze_time("2025-01-01T01:00:00Z", real_asyncio=True)
    async def test_incremental_lookback_controls_tracker_updates(self):
        async def run_sync(lookback):
            tracker = TwoWayTestTracker(
                issues=[
                    self._issue(
                        "345",
                        updated=datetime.datetime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
                        parents=[IssueRef(repo="repo", id="123")],
                        title="Subissue 2 from tracker",
                    ),
                ],
                recent_ids=[("repo", "345")],
                filter_recent_by_since=True,
            )
            await self._run_sync(
                tracker,
                incremental_lookback_seconds=lookback,
                tasks_tracker_to_notion=True,
                tasks_notion_to_tracker=False,
                milestones_tracker_to_notion=False,
                milestones_notion_to_tracker=False,
            )
            return tracker

        tracker = await run_sync(30 * 60)
        self.assertEqual(len(tracker.updated_tasks), 0)
        self.assertEqual(self.respx.routes["pages_update"].calls.call_count, 0)

        self.reset_handlers()

        tracker = await run_sync(2 * 60 * 60)
        task_updates = [
            call
            for call in self.respx.routes["pages_update"].calls
            if call.request.url.path == "/v1/pages/a4e70f0b-b5b1-43ca-ac0e-7723ae7dc359"
        ]
        self.assertEqual(len(tracker.updated_tasks), 0)
        self.assertEqual(len(task_updates), 1)
        title = json.loads(task_updates[0].request.content)["properties"]["Title"]["title"][0]["text"]["content"]
        self.assertEqual(title, "[prefix] Subissue 2 from tracker")

    @freeze_time("2022-07-06T21:25:30Z", real_asyncio=True)
    async def test_incremental_notion_window_includes_boundary_minute(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "345",
                    updated=datetime.datetime(2022, 7, 6, 20, 0, tzinfo=datetime.timezone.utc),
                    parents=[IssueRef(repo="repo", id="123")],
                    title="Old tracker title",
                ),
            ],
            recent_ids=[],
        )

        await self._run_sync(
            tracker,
            incremental_lookback_seconds=60 * 60,
            tasks_tracker_to_notion=False,
            tasks_notion_to_tracker=True,
            milestones_tracker_to_notion=False,
            milestones_notion_to_tracker=False,
        )

        self.assertEqual(len(tracker.updated_tasks), 1)
        self.assertEqual(tracker.updated_tasks[0][1].title, "Subissue 2")
        self.assertEqual(tracker.recent_since_calls[0], datetime.datetime(2022, 7, 6, 20, 25, tzinfo=datetime.UTC))

    async def test_warm_cache_retrieves_cached_recent_tracker_page(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            cache_path = Path(tmpdir) / "twoway.sqlite3"
            tracker = TwoWayTestTracker(
                issues=[
                    self._issue("123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc)),
                    self._issue(
                        "345",
                        updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                        parents=[IssueRef(repo="repo", id="123")],
                    ),
                ],
                recent_ids=[("repo", "123"), ("repo", "345")],
            )
            await self._run_sync(
                tracker,
                incremental_lookback_seconds=None,
                twoway_cache_enabled=True,
                twoway_cache_path=cache_path,
            )

            self.reset_handlers()

            tracker = TwoWayTestTracker(
                issues=[
                    self._issue("123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc)),
                    self._issue(
                        "345",
                        updated=datetime.datetime(2025, 1, 2, tzinfo=datetime.timezone.utc),
                        parents=[IssueRef(repo="repo", id="123")],
                    ),
                ],
                recent_ids=[("repo", "345")],
            )
            await self._run_sync(
                tracker,
                incremental_lookback_seconds=604800,
                twoway_cache_enabled=True,
                twoway_cache_path=cache_path,
                tasks_tracker_to_notion=True,
                tasks_notion_to_tracker=False,
                milestones_tracker_to_notion=False,
                milestones_notion_to_tracker=False,
            )

        retrieved_pages = [
            call
            for call in self.respx.routes["pages_retrieve"].calls
            if call.request.url.path == "/v1/pages/a4e70f0b-b5b1-43ca-ac0e-7723ae7dc359"
        ]
        task_query_bodies = [
            call.request.content.decode("utf-8")
            for call in self.respx.routes["db_query"].calls
            if call.request.url.path == "/v1/databases/tasks_id/query"
        ]
        self.assertEqual(len(retrieved_pages), 1)
        self.assertTrue(task_query_bodies)
        self.assertTrue(all("last_edited_time" in body for body in task_query_bodies))

    async def test_warm_cache_stores_updated_task_page_snapshot(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            cache_path = Path(tmpdir) / "twoway.sqlite3"
            tracker = TwoWayTestTracker(
                issues=[
                    self._issue("123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc)),
                    self._issue(
                        "345",
                        updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                        parents=[IssueRef(repo="repo", id="123")],
                    ),
                ],
                recent_ids=[("repo", "123"), ("repo", "345")],
            )
            await self._run_sync(
                tracker,
                incremental_lookback_seconds=None,
                twoway_cache_enabled=True,
                twoway_cache_path=cache_path,
            )

            self.reset_handlers()

            tracker = TwoWayTestTracker(
                issues=[
                    self._issue("123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc)),
                    self._issue(
                        "345",
                        updated=datetime.datetime(2025, 1, 2, tzinfo=datetime.timezone.utc),
                        parents=[IssueRef(repo="repo", id="123")],
                        title="Updated cached title",
                    ),
                ],
                recent_ids=[("repo", "345")],
            )
            await self._run_sync(
                tracker,
                incremental_lookback_seconds=604800,
                twoway_cache_enabled=True,
                twoway_cache_path=cache_path,
                tasks_tracker_to_notion=True,
                tasks_notion_to_tracker=False,
                milestones_tracker_to_notion=False,
                milestones_notion_to_tracker=False,
            )

            with sqlite3.connect(cache_path) as conn:
                page_json = conn.execute(
                    """
                    SELECT page_json
                      FROM notion_page_links
                     WHERE entity_kind = 'task'
                       AND issue_repo = 'repo'
                       AND issue_id = '345'
                    """
                ).fetchone()[0]

        cached_page = json.loads(page_json)
        title = cached_page["properties"]["Title"]["title"][0]["text"]["content"]
        self.assertEqual(title, "[prefix] Updated cached title")

    async def test_dry_run_primes_and_reuses_twoway_cache(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            cache_path = Path(tmpdir) / "twoway.sqlite3"
            tracker = TwoWayTestTracker(
                issues=[
                    self._issue("123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc)),
                    self._issue(
                        "345",
                        updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                        parents=[IssueRef(repo="repo", id="123")],
                    ),
                ],
                recent_ids=[("repo", "123"), ("repo", "345")],
            )
            await self._run_sync(
                tracker,
                incremental_lookback_seconds=None,
                dry=True,
                twoway_cache_enabled=True,
                twoway_cache_path=cache_path,
            )

            with sqlite3.connect(cache_path) as conn:
                rows = conn.execute(
                    """
                    SELECT entity_kind, issue_repo, issue_id
                      FROM notion_page_links
                     ORDER BY entity_kind, issue_id
                    """
                ).fetchall()

            self.assertEqual(rows, [("milestone", "repo", "123"), ("task", "repo", "345")])

            self.reset_handlers()

            tracker = TwoWayTestTracker(
                issues=[
                    self._issue("123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc)),
                    self._issue(
                        "345",
                        updated=datetime.datetime(2025, 1, 2, tzinfo=datetime.timezone.utc),
                        parents=[IssueRef(repo="repo", id="123")],
                    ),
                ],
                recent_ids=[("repo", "345")],
            )
            await self._run_sync(
                tracker,
                incremental_lookback_seconds=604800,
                dry=True,
                twoway_cache_enabled=True,
                twoway_cache_path=cache_path,
                tasks_tracker_to_notion=True,
                tasks_notion_to_tracker=False,
                milestones_tracker_to_notion=False,
                milestones_notion_to_tracker=False,
            )

        query_bodies = [call.request.content.decode("utf-8") for call in self.respx.routes["db_query"].calls]
        self.assertTrue(query_bodies)
        self.assertTrue(all("last_edited_time" in body for body in query_bodies))

    async def test_linked_epic_updates_tracker_from_notion(self):
        page = self._set_epic_page_issue("900")
        page["properties"]["Dates"] = {
            "type": "date",
            "date": {"start": "2026-06-24", "end": None},
        }
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "900",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    title="Old epic title",
                    issue_type="Epic",
                ),
            ],
            recent_ids=[],
        )

        await self._run_sync(
            tracker,
            epics_id="epics_id",
            epics_notion_to_tracker=True,
            epics_tracker_to_notion=False,
            tasks_tracker_to_notion=False,
            milestones_notion_to_tracker=False,
            incremental_lookback_seconds=None,
        )

        self.assertEqual(len(tracker.updated_milestones), 1)
        _, new_issue = tracker.updated_milestones[0]
        self.assertEqual(new_issue.title, "Account Drawer Improvements")
        self.assertEqual(new_issue.issue_type, "Epic")
        self.assertIsNone(new_issue.start_date)
        self.assertEqual(new_issue.end_date, datetime.date(2026, 6, 24))

    async def test_linked_epic_updates_notion_from_tracker(self):
        self._set_epic_page_issue("900")
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "900",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    title="Updated epic title",
                    issue_type="Epic",
                ),
            ],
            recent_ids=[("repo", "900")],
        )

        await self._run_sync(
            tracker,
            epics_id="epics_id",
            epics_tracker_to_notion=True,
            epics_notion_to_tracker=False,
            tasks_tracker_to_notion=False,
            milestones_notion_to_tracker=False,
            incremental_lookback_seconds=604800,
        )

        epic_updates = [
            call
            for call in self.respx.routes["pages_update"].calls
            if call.request.url.path == "/v1/pages/6f6fac28-6b63-48ca-90ec-0066be1a2755"
        ]
        self.assertEqual(len(epic_updates), 1)
        title = json.loads(epic_updates[0].request.content)["properties"]["Title"]["title"][0]["text"]["content"]
        self.assertEqual(title, "Updated epic title")

    async def test_closed_epic_tracker_to_notion_uses_target_date(self):
        tracker_issue = self._issue(
            "900",
            updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
            title="Closed epic",
            state="Done",
            issue_type="Epic",
        )
        tracker_issue.start_date = None
        tracker_issue.end_date = datetime.date(2025, 3, 4)
        tracker_issue.closed_date = datetime.datetime(2025, 3, 4, 12, 0, tzinfo=datetime.timezone.utc)
        tracker = TwoWayTestTracker(issues=[tracker_issue])
        sync = TrackerTwoWaySync(
            project_key="twoway",
            tracker=tracker,
            notion_token="NOTION_TOKEN",
            epics_id="epics_id",
            milestones_id="milestones_id",
            tasks_id="tasks_id",
            dry=False,
        )

        notion_data = sync._get_epic_notion_data_from_tracker(tracker_issue)

        self.assertEqual(notion_data["Dates"], {"start": datetime.date(2025, 3, 4), "end": None})

    async def test_tracker_to_notion_epic_create(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "901",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    title="New epic",
                    issue_type="Epic",
                ),
            ],
            recent_ids=[("repo", "901")],
        )

        with self.assertLogs("twoway_sync", level="INFO") as logs:
            await self._run_sync(
                tracker,
                epics_id="epics_id",
                epics_tracker_to_notion=True,
                epics_tracker_to_notion_create=True,
                epics_notion_to_tracker=False,
                tasks_tracker_to_notion=False,
                milestones_notion_to_tracker=False,
                incremental_lookback_seconds=None,
            )

        epic_creates = [
            call
            for call in self.respx.routes["pages_create"].calls
            if json.loads(call.request.content)["parent"]["database_id"] == "epics_id"
        ]
        self.assertEqual(len(epic_creates), 1)
        self._assert_stats_row(logs, "created from tracker", 0, 0)
        self.assertRegex("\n".join(logs.output), r"created from tracker\s+0\s+0\s+1")

    async def test_milestone_epic_relation_updates_in_twoway_sync(self):
        self._set_epic_page_issue("900")
        self._set_milestone_page_issue("901")
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "901",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    parents=[IssueRef(repo="repo", id="900")],
                    title="Milestone with epic parent",
                    issue_type="Milestone",
                ),
            ],
            recent_ids=[("repo", "901")],
        )

        await self._run_sync(
            tracker,
            epics_id="epics_id",
            milestones_issue_type="Milestone",
            milestones_tracker_to_notion=True,
            milestones_notion_to_tracker=False,
            tasks_tracker_to_notion=False,
            epics_tracker_to_notion=False,
            epics_notion_to_tracker=False,
            incremental_lookback_seconds=604800,
        )

        milestone_updates = [
            call
            for call in self.respx.routes["pages_update"].calls
            if call.request.url.path == "/v1/pages/726fac28-6b63-48ca-90ec-0066be1a2755"
        ]
        self.assertEqual(len(milestone_updates), 1)
        body = json.loads(milestone_updates[0].request.content)
        self.assertEqual(
            body["properties"]["Epic"]["relation"],
            [{"id": "6f6fac286b6348ca90ec0066be1a2755"}],
        )

    async def test_dry_run_epic_create_does_not_feed_milestone_relation_update(self):
        self._set_milestone_page_issue("902")
        tie_ts = datetime.datetime(2022, 7, 6, 20, 25, tzinfo=datetime.timezone.utc)
        tracker = TwoWayTestTracker(
            issues=[
                self._issue("901", updated=tie_ts, title="New epic", issue_type="Epic"),
                self._issue(
                    "902",
                    updated=tie_ts,
                    parents=[IssueRef(repo="repo", id="901")],
                    title="Rebuild the calendar Read Event dialog",
                    issue_type="Milestone",
                ),
            ],
            recent_ids=[("repo", "901"), ("repo", "902")],
        )

        with self.assertLogs("twoway_sync", level="INFO") as logs:
            await self._run_sync(
                tracker,
                epics_id="epics_id",
                epics_tracker_to_notion=True,
                epics_tracker_to_notion_create=True,
                epics_notion_to_tracker=False,
                milestones_issue_type="Milestone",
                milestones_tracker_to_notion=True,
                milestones_notion_to_tracker=True,
                tasks_tracker_to_notion=False,
                incremental_lookback_seconds=604800,
                dry=True,
            )

        output = "\n".join(logs.output)
        self.assertRegex(output, r"created from tracker\s+0\s+0\s+1")
        self.assertNotIn("Updating milestone epic relation (Tracker->Notion)", output)
        self.assertNotIn("to ['dry']", output)

    async def test_warm_cache_retrieves_cached_recent_epic_page(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            cache_path = Path(tmpdir) / "twoway.sqlite3"
            self._set_epic_page_issue("900")
            tracker = TwoWayTestTracker(
                issues=[
                    self._issue(
                        "900",
                        updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                        issue_type="Epic",
                    ),
                ],
                recent_ids=[("repo", "900")],
            )
            await self._run_sync(
                tracker,
                epics_id="epics_id",
                incremental_lookback_seconds=None,
                twoway_cache_enabled=True,
                twoway_cache_path=cache_path,
            )

            self.reset_handlers()
            self._set_epic_page_issue("900")

            tracker = TwoWayTestTracker(
                issues=[
                    self._issue(
                        "900",
                        updated=datetime.datetime(2025, 1, 2, tzinfo=datetime.timezone.utc),
                        issue_type="Epic",
                    ),
                ],
                recent_ids=[("repo", "900")],
            )
            await self._run_sync(
                tracker,
                epics_id="epics_id",
                incremental_lookback_seconds=604800,
                twoway_cache_enabled=True,
                twoway_cache_path=cache_path,
                epics_tracker_to_notion=True,
                epics_notion_to_tracker=False,
                tasks_tracker_to_notion=False,
                milestones_notion_to_tracker=False,
            )

        retrieved_pages = [
            call
            for call in self.respx.routes["pages_retrieve"].calls
            if call.request.url.path == "/v1/pages/6f6fac28-6b63-48ca-90ec-0066be1a2755"
        ]
        self.assertEqual(len(retrieved_pages), 1)

    async def test_epic_notion_to_tracker_create_is_unsupported(self):
        tracker = TwoWayTestTracker(issues=[], recent_ids=[])

        with self.assertLogs("twoway_sync", level="WARNING") as logs:
            await self._run_sync(
                tracker,
                epics_id="epics_id",
                epics_notion_to_tracker=False,
                epics_notion_to_tracker_create=True,
                epics_tracker_to_notion=False,
                tasks_tracker_to_notion=False,
                milestones_notion_to_tracker=False,
                incremental_lookback_seconds=604800,
            )

        self.assertEqual(tracker.updated_milestones, [])
        self.assertIn("epics_notion_to_tracker_create is not supported", "\n".join(logs.output))

    async def test_full_sync_processes_linked_refs(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue("123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc), title="M!"),
                self._issue(
                    "234",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    parents=[IssueRef(repo="repo", id="123")],
                    title="Task Updated",
                ),
            ],
            recent_ids=[],
        )

        await self._run_sync(tracker, incremental_lookback_seconds=None)
        self.assertGreaterEqual(len(tracker.updated_milestones), 1)
        self.assertEqual(len(tracker.updated_tasks), 0)

    async def test_partitioned_task_discovery_fails_on_incomplete_notion_query(self):
        def incomplete_query(req):
            return {
                "results": [],
                "has_more": False,
                "next_cursor": None,
                "request_status": {
                    "type": "incomplete",
                    "incomplete_reason": "query_result_limit_reached",
                },
            }

        self.notion_handler.tasks_handler.query_handler = incomplete_query
        tracker = TwoWayTestTracker(
            issues=[self._issue("123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc))],
            recent_ids=[("repo", "123")],
        )

        with self.assertRaisesInGroup(NotionQueryIncompleteError, "incomplete results"):
            await self._run_sync(
                tracker,
                tasks_notion_to_tracker=True,
                tasks_notion_to_tracker_create=True,
                incremental_lookback_seconds=None,
            )

    async def test_lww_tie_break_defaults(self):
        tie_ts = datetime.datetime(2022, 7, 6, 20, 25, tzinfo=datetime.timezone.utc)
        page = self._set_milestone_page_issue("123")
        page["properties"]["Dates"] = {
            "type": "date",
            "date": {"start": "2026-06-24", "end": None},
        }
        tracker = TwoWayTestTracker(
            issues=[
                self._issue("123", updated=tie_ts, title="[meta] Milestone"),
                self._issue("234", updated=tie_ts, parents=[IssueRef(repo="repo", id="123")]),
            ],
            recent_ids=[("repo", "123"), ("repo", "234")],
        )

        await self._run_sync(
            tracker,
            tasks_tracker_to_notion=True,
            tasks_notion_to_tracker=True,
            milestones_tracker_to_notion=True,
            milestones_notion_to_tracker=True,
            incremental_lookback_seconds=604800,
        )

        # Tie fallback: tracker for tasks, notion for milestones
        self.assertEqual(len(tracker.updated_tasks), 0)
        self.assertGreaterEqual(len(tracker.updated_milestones), 1)
        milestone_updates = [new_issue for old_issue, new_issue in tracker.updated_milestones if old_issue.id == "123"]
        self.assertTrue(milestone_updates)
        self.assertIsNone(milestone_updates[0].start_date)
        self.assertEqual(milestone_updates[0].end_date, datetime.date(2026, 6, 24))

    async def test_exact_task_tie_uses_configured_conflict_preference(self):
        tracker_issue = self._issue(
            "345",
            updated=datetime.datetime(2022, 7, 6, 20, 25, tzinfo=datetime.timezone.utc),
            parents=[IssueRef(repo="repo", id="123")],
        )
        tracker = TwoWayTestTracker(issues=[tracker_issue])
        sync = TrackerTwoWaySync(
            project_key="twoway",
            tracker=tracker,
            notion_token="NOTION_TOKEN",
            milestones_id="milestones_id",
            tasks_id="tasks_id",
            tasks_conflict_preference="notion",
            dry=True,
        )

        notion_page = {
            "last_edited_time": "2022-07-06T20:25:00.000Z",
        }

        self.assertEqual(
            sync._pick_direction("task", tracker_issue, notion_page, True, True),
            "notion_to_tracker",
        )

        tracker_issue.updated_date = datetime.datetime(2022, 7, 6, 20, 26, tzinfo=datetime.timezone.utc)
        self.assertEqual(
            sync._pick_direction("task", tracker_issue, notion_page, True, True),
            "tracker_to_notion",
        )
        await sync.notion.aclose()

    async def test_exact_milestone_tie_uses_configured_conflict_preference(self):
        tracker_issue = self._issue(
            "123",
            updated=datetime.datetime(2022, 7, 6, 20, 25, tzinfo=datetime.timezone.utc),
        )
        tracker = TwoWayTestTracker(issues=[tracker_issue])
        sync = TrackerTwoWaySync(
            project_key="twoway",
            tracker=tracker,
            notion_token="NOTION_TOKEN",
            milestones_id="milestones_id",
            tasks_id="tasks_id",
            milestones_conflict_preference="tracker",
            dry=True,
        )

        notion_page = {
            "last_edited_time": "2022-07-06T20:25:00.000Z",
        }

        self.assertEqual(
            sync._pick_direction("milestone", tracker_issue, notion_page, True, True),
            "tracker_to_notion",
        )
        await sync.notion.aclose()

    async def test_notion_link_domain_change_does_not_update_tracker(self):
        tracker_issue = self._issue(
            "234",
            updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
            parents=[IssueRef(repo="repo", id="123")],
        )
        tracker_issue.notion_url = "https://www.notion.so/xxx"
        tracker = TwoWayTestTracker(issues=[tracker_issue])
        sync = TrackerTwoWaySync(
            project_key="twoway",
            tracker=tracker,
            notion_token="NOTION_TOKEN",
            milestones_id="milestones_id",
            tasks_id="tasks_id",
            dry=True,
        )

        page = {
            "url": "https://app.notion.com/p/xxx",
            "properties": {"Title": {"type": "title", "title": []}},
        }

        new_issue = sync._get_task_tracker_issue_from_notion(tracker_issue, page)
        self.assertEqual(new_issue.notion_url, "https://app.notion.com/p/xxx")
        self.assertFalse(sync._task_needs_tracker_update(tracker_issue, page))
        await sync.notion.aclose()

    async def test_task_estimate_maps_in_both_directions(self):
        tracker_issue = self._issue(
            "234",
            updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
            parents=[IssueRef(repo="repo", id="123")],
        )
        tracker_issue.estimate = "3"
        tracker = TwoWayTestTracker(
            issues=[tracker_issue],
            property_names={
                "notion_tasks_estimate": "Estimate",
            },
        )
        sync = TrackerTwoWaySync(
            project_key="twoway",
            tracker=tracker,
            notion_token="NOTION_TOKEN",
            milestones_id="milestones_id",
            tasks_id="tasks_id",
            dry=True,
        )

        notion_page = {
            "id": "task-234",
            "url": "https://notion.so/example/task-234",
            "properties": {
                "Title": {"type": "title", "title": [{"plain_text": "Issue 234"}]},
                "Estimate": {"type": "select", "select": {"name": "5"}},
            },
        }

        from_notion = sync._get_task_tracker_issue_from_notion(tracker_issue, notion_page)
        self.assertEqual(from_notion.estimate, "5")

        notion_page["properties"]["Estimate"]["select"] = None
        from_notion = sync._get_task_tracker_issue_from_notion(tracker_issue, notion_page)
        self.assertIsNone(from_notion.estimate)

        to_notion = await sync._get_task_notion_data(
            tracker_issue=tracker_issue,
            parent_milestone_pages=[],
            old_page=None,
        )
        self.assertEqual(to_notion["Estimate"], "3")
        await sync.notion.aclose()

    async def test_linked_task_repository_updates_with_normal_tracker_to_notion_sync(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "123",
                    updated=datetime.datetime(2022, 7, 6, 20, 25, tzinfo=datetime.timezone.utc),
                    title="Milestone",
                ),
                self._issue(
                    "345",
                    updated=datetime.datetime(2022, 7, 6, 20, 26, tzinfo=datetime.timezone.utc),
                    parents=[IssueRef(repo="repo", id="123")],
                    title="Subissue 2",
                ),
            ],
            recent_ids=[("repo", "345")],
            property_names={
                "notion_tasks_repository_map": {"repo": "test"},
            },
        )

        await self._run_sync(
            tracker,
            tasks_tracker_to_notion=True,
            tasks_notion_to_tracker=True,
            tasks_conflict_preference="notion",
            incremental_lookback_seconds=604800,
        )

        task_updates = [
            call
            for call in self.respx.routes["pages_update"].calls
            if call.request.url.path == "/v1/pages/a4e70f0b-b5b1-43ca-ac0e-7723ae7dc359"
        ]
        self.assertEqual(len(task_updates), 1)
        self.assertEqual(
            json.loads(task_updates[0].request.content)["properties"]["Repository"],
            {"select": {"name": "test"}},
        )

    async def test_tracker_to_notion_task_create_requires_parent(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc), title="Milestone"
                ),
                self._issue(
                    "500",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    parents=[IssueRef(repo="repo", id="123")],
                    title="New Child",
                ),
                self._issue("501", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc), title="Orphan"),
            ],
            recent_ids=[("repo", "500"), ("repo", "501")],
        )

        await self._run_sync(
            tracker,
            tasks_tracker_to_notion=True,
            tasks_tracker_to_notion_create=True,
            tasks_notion_to_tracker=False,
            incremental_lookback_seconds=604800,
        )

        self.assertEqual(self.respx.routes["pages_create"].calls.call_count, 1)

    async def test_deeply_nested_task_create_candidate_is_not_counted_as_created(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "502",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    parents=[IssueRef(repo="repo", id="123")],
                    title="Nested Child",
                    deeply_nested=True,
                ),
            ],
            recent_ids=[("repo", "502")],
        )

        with self.assertLogs("twoway_sync", level="INFO") as logs:
            await self._run_sync(
                tracker,
                tasks_tracker_to_notion=True,
                tasks_tracker_to_notion_create=True,
                tasks_notion_to_tracker=False,
                incremental_lookback_seconds=604800,
            )

        self.assertEqual(self.respx.routes["pages_create"].calls.call_count, 0)
        self._assert_stats_row(logs, "created from tracker", 0, 0)

    async def test_milestone_issue_with_parent_is_not_task_create_candidate(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "1253",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    parents=[IssueRef(repo="repo", id="1000")],
                    issue_type="Milestone",
                    title="Milestone with epic parent",
                ),
            ],
            recent_ids=[("repo", "1253")],
        )

        await self._run_sync(
            tracker,
            tasks_tracker_to_notion=True,
            tasks_tracker_to_notion_create=True,
            milestones_issue_type="Milestone",
            milestones_tracker_to_notion=True,
            milestones_tracker_to_notion_create=False,
            incremental_lookback_seconds=604800,
        )

        self.assertEqual(self.respx.routes["pages_create"].calls.call_count, 0)

    async def test_recent_milestone_issue_is_not_counted_as_task(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "1253",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    parents=[IssueRef(repo="repo", id="1000")],
                    issue_type="Milestone",
                    title="Milestone with epic parent",
                ),
            ],
            recent_ids=[("repo", "1253")],
        )

        with self.assertLogs("twoway_sync", level="INFO") as logs:
            await self._run_sync(
                tracker,
                tasks_tracker_to_notion=True,
                tasks_tracker_to_notion_create=True,
                milestones_issue_type="Milestone",
                milestones_tracker_to_notion=True,
                milestones_tracker_to_notion_create=False,
                incremental_lookback_seconds=604800,
            )

        self.assertEqual(self.respx.routes["pages_create"].calls.call_count, 0)
        output = "\n".join(logs.output)
        self.assertRegex(output, r"recent_tracker_refs=0 recent_tracker_tasks=0")
        self._assert_stats_row(logs, "created from tracker", 0, 0)

    async def test_recent_epic_issue_is_not_counted_as_task(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "1254",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    parents=[IssueRef(repo="repo", id="1000")],
                    issue_type="Epic",
                    title="Epic with parent",
                ),
            ],
            recent_ids=[("repo", "1254")],
        )

        with self.assertLogs("twoway_sync", level="INFO") as logs:
            await self._run_sync(
                tracker,
                tasks_tracker_to_notion=True,
                tasks_tracker_to_notion_create=True,
                milestones_issue_type="Milestone",
                epics_issue_type="Epic",
                incremental_lookback_seconds=604800,
            )

        self.assertEqual(self.respx.routes["pages_create"].calls.call_count, 0)
        output = "\n".join(logs.output)
        self.assertRegex(output, r"recent_tracker_refs=0 recent_tracker_tasks=0")
        self._assert_stats_row(logs, "created from tracker", 0, 0)

    async def test_recent_child_task_under_milestone_parent_is_still_task_candidate(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "1255",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    parents=[IssueRef(repo="repo", id="1000")],
                    issue_type="Task",
                    title="Task under milestone",
                ),
            ],
            recent_ids=[("repo", "1255")],
        )

        with self.assertLogs("twoway_sync", level="INFO") as logs:
            await self._run_sync(
                tracker,
                tasks_tracker_to_notion=True,
                tasks_tracker_to_notion_create=True,
                milestones_issue_type="Milestone",
                epics_issue_type="Epic",
                incremental_lookback_seconds=604800,
            )

        self.assertEqual(self.respx.routes["pages_create"].calls.call_count, 1)
        output = "\n".join(logs.output)
        self.assertRegex(output, r"recent_tracker_refs=1 recent_tracker_tasks=1")
        self._assert_stats_row(logs, "created from tracker", 1, 0)

    async def test_tracker_to_notion_milestone_create(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "999",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    title="[meta] New Milestone",
                ),
            ],
            recent_ids=[("repo", "999")],
        )

        await self._run_sync(
            tracker,
            milestones_tracker_to_notion=True,
            milestones_tracker_to_notion_create=True,
            milestones_notion_to_tracker=False,
            tasks_tracker_to_notion=False,
            incremental_lookback_seconds=604800,
        )

        self.assertEqual(self.respx.routes["pages_create"].calls.call_count, 1)

    async def test_tracker_to_notion_milestone_create_uses_creator_team_without_assignees(self):
        user_map = StaticUserMap(
            {"creator@example.com": "notion-creator"},
            notion_to_teams={"notion-creator": ["team-a"]},
        )
        tracker_issue = self._issue(
            "999",
            updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
            title="[meta] New Milestone",
        )
        tracker_issue.creator = User(user_map, tracker_user="creator@example.com")
        tracker = TwoWayTestTracker(
            issues=[tracker_issue],
            property_names={"notion_milestones_team": "Team"},
        )
        tracker.user_map = user_map
        sync = TrackerTwoWaySync(
            project_key="twoway",
            tracker=tracker,
            notion_token="NOTION_TOKEN",
            milestones_id="milestones_id",
            tasks_id="tasks_id",
            team_id="team_db_id",
            team_association=["fallback-team"],
            dry=True,
        )
        sync.milestones_db.create_page = AsyncMock(return_value={"id": "dry", "url": "https://notion.so/dry"})

        await sync._create_milestone_in_notion_from_tracker(tracker_issue)

        created_data = sync.milestones_db.create_page.await_args.args[0]
        self.assertEqual(created_data["Team"], ["teama"])

    async def test_tracker_to_notion_milestone_create_logs_payload(self):
        tracker_issue = self._issue(
            "999",
            updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
            title="[meta] New Milestone",
        )
        tracker = TwoWayTestTracker([tracker_issue])
        sync = TrackerTwoWaySync(
            project_key="twoway",
            tracker=tracker,
            notion_token="NOTION_TOKEN",
            milestones_id="milestones_id",
            tasks_id="tasks_id",
            dry=True,
        )
        sync.milestones_db.create_page = AsyncMock(return_value={"id": "dry", "url": "https://notion.so/dry"})

        with self.assertLogs("twoway_sync", level="DEBUG") as logs:
            await sync._create_milestone_in_notion_from_tracker(tracker_issue)

        output = "\n".join(logs.output)
        self.assertIn(
            "Creating milestone (Tracker->Notion) https://example.com/repo/999 - [meta] New Milestone", output
        )
        self.assertIn("'Issue Link': 'https://example.com/repo/999'", output)

    @freeze_time("2026-08-24T00:01:00Z", real_asyncio=True)
    async def test_tracker_to_notion_typed_milestone_create(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "997",
                    updated=datetime.datetime(2026, 8, 24, 0, 0, tzinfo=datetime.timezone.utc),
                    title="Typed Milestone",
                    issue_type="Milestone",
                ),
            ],
            recent_ids=[("repo", "997")],
        )

        with self.assertLogs("twoway_sync", level="INFO") as logs:
            await self._run_sync(
                tracker,
                milestones_issue_type="Milestone",
                milestones_tracker_to_notion=True,
                milestones_tracker_to_notion_create=True,
                milestones_notion_to_tracker=False,
                tasks_tracker_to_notion=True,
                tasks_tracker_to_notion_create=True,
                incremental_lookback_seconds=604800,
            )

        self.assertEqual(self.respx.routes["pages_create"].calls.call_count, 1)
        self._assert_stats_row(logs, "created from tracker", 0, 1)

    async def test_tracker_to_notion_milestone_create_dry_run(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            cache_path = Path(tmpdir) / "twoway.sqlite3"
            tracker = TwoWayTestTracker(
                issues=[
                    self._issue(
                        "998",
                        updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                        title="[meta] Dry Run Milestone",
                    ),
                ],
                recent_ids=[("repo", "998")],
            )

            await self._run_sync(
                tracker,
                milestones_tracker_to_notion=True,
                milestones_tracker_to_notion_create=True,
                milestones_notion_to_tracker=False,
                tasks_tracker_to_notion=False,
                incremental_lookback_seconds=604800,
                dry=True,
                twoway_cache_enabled=True,
                twoway_cache_path=cache_path,
            )

            with sqlite3.connect(cache_path) as conn:
                dry_rows = conn.execute(
                    """
                    SELECT page_id, issue_id
                      FROM notion_page_links
                     WHERE page_id = 'dry'
                        OR issue_id = '998'
                    """
                ).fetchall()

        # NotionDatabase.create_page() returns a fake dry page; no remote create call is made.
        self.assertEqual(self.respx.routes["pages_create"].calls.call_count, 0)
        self.assertEqual(dry_rows, [])

    async def test_notion_to_tracker_task_create_dry_run_does_not_cache_simulated_link_back(self):
        self.notion_handler.tasks_handler.pages.append(
            {
                "object": "page",
                "id": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
                "created_time": "2025-01-01T00:00:00.000Z",
                "last_edited_time": "2025-01-01T00:00:00.000Z",
                "url": "https://notion.so/example/new-task",
                "properties": {
                    "Title": {
                        "id": "title",
                        "type": "title",
                        "title": [
                            {
                                "type": "text",
                                "text": {"content": "Create me"},
                                "plain_text": "Create me",
                            }
                        ],
                    },
                    "Status": {
                        "id": "st",
                        "type": "status",
                        "status": {"name": "Backlog"},
                    },
                    "Issue Link": {"type": "files", "files": []},
                    "Project": {
                        "type": "relation",
                        "relation": [{"id": "726fac28-6b63-48ca-90ec-0066be1a2755"}],
                    },
                },
            }
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            cache_path = Path(tmpdir) / "twoway.sqlite3"
            tracker = TwoWayTestTracker(
                issues=[
                    self._issue(
                        "123",
                        updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                        title="Milestone",
                    ),
                ],
                recent_ids=[("repo", "123")],
            )

            await self._run_sync(
                tracker,
                tasks_tracker_to_notion=False,
                tasks_notion_to_tracker=True,
                tasks_notion_to_tracker_create=True,
                incremental_lookback_seconds=None,
                dry=True,
                twoway_cache_enabled=True,
                twoway_cache_path=cache_path,
            )

            with sqlite3.connect(cache_path) as conn:
                simulated_rows = conn.execute(
                    """
                    SELECT page_id, issue_id
                      FROM notion_page_links
                     WHERE page_id = 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb'
                        OR issue_id LIKE 'c%'
                    """
                ).fetchall()

        self.assertEqual(len(tracker.created_tasks), 1)
        self.assertEqual(simulated_rows, [])

    async def test_tracker_to_notion_milestone_create_dry_run_legacy(self):
        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "998",
                    updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
                    title="[meta] Dry Run Milestone",
                ),
            ],
            recent_ids=[("repo", "998")],
        )

        await self._run_sync(
            tracker,
            milestones_tracker_to_notion=True,
            milestones_tracker_to_notion_create=True,
            milestones_notion_to_tracker=False,
            tasks_tracker_to_notion=False,
            incremental_lookback_seconds=604800,
            dry=True,
        )

        # NotionDatabase.create_page() returns a fake dry page; no remote create call is made.
        self.assertEqual(self.respx.routes["pages_create"].calls.call_count, 0)

    async def test_notion_to_tracker_task_create(self):
        # Add an unlinked active Notion task linked to milestone page 123.
        page = self._add_unlinked_task_page(url="https://notion.so/example/new-task")
        page["properties"]["Estimate"] = {"type": "select", "select": {"name": "5"}}

        tracker = TwoWayTestTracker(
            issues=[
                self._issue(
                    "123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc), title="Milestone"
                ),
            ],
            recent_ids=[("repo", "123")],
            property_names={
                "notion_tasks_estimate": "Estimate",
            },
        )

        await self._run_sync(
            tracker,
            tasks_tracker_to_notion=False,
            tasks_notion_to_tracker=True,
            tasks_notion_to_tracker_create=True,
            incremental_lookback_seconds=None,
        )

        self.assertEqual(len(tracker.created_tasks), 1)
        self.assertEqual(tracker.created_tasks[0][2], "5")
        self.assertGreaterEqual(self.respx.routes["pages_update"].calls.call_count, 1)
        tasks_query_calls = [
            call
            for call in self.respx.routes["db_query"].calls
            if call.request.url.path == "/v1/databases/tasks_id/query"
        ]
        self.assertEqual(len(tasks_query_calls), 1)

    async def test_unsupported_milestone_notion_to_tracker_create_is_ignored(self):
        tracker = TwoWayTestTracker(
            issues=[self._issue("123", updated=datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc))],
            recent_ids=[("repo", "123")],
        )

        await self._run_sync(
            tracker,
            milestones_notion_to_tracker=True,
            milestones_notion_to_tracker_create=True,
            incremental_lookback_seconds=None,
        )

        # still only the normal milestone update behavior, no create attempts
        self.assertGreaterEqual(len(tracker.updated_milestones), 1)


if __name__ == "__main__":
    unittest.main()
