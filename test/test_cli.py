import argparse
import datetime
import tempfile
import unittest

from pathlib import Path
from unittest.mock import AsyncMock, patch

from mzla_notion.cli import cmd_synchronize, parse_lookback
from mzla_notion.people import load_notion_usermap
from scripts.notion_debug import build_usermap_table_rows


class DummyNotion:
    class Databases:
        async def query(self, **kwargs):
            return kwargs

    def __init__(self, *args, **kwargs):
        self.databases = self.Databases()


class TestPeopleLoader(unittest.IsolatedAsyncioTestCase):
    async def test_load_notion_usermap(self):
        settings = {
            "people": {
                "notion_people_id": "people-db-id",
                "notion_people_github": "GitHub Profile",
                "notion_people_email": "Email",
                "notion_people_bugzilla": "Bugzilla Email",
                "notion_people_phabricator": "Phabricator",
                "notion_people_uuid": "User",
                "notion_people_team": "Team",
            }
        }
        pages = [
            {
                "properties": {
                    "GitHub Profile": {"type": "url", "url": "https://github.com/example-user"},
                    "Email": {"type": "email", "email": "user@example.com"},
                    "Bugzilla Email": {"type": "email", "email": ""},
                    "Phabricator": {"type": "rich_text", "rich_text": [{"plain_text": "example-phab"}]},
                    "User": {"type": "people", "people": [{"id": "11111111-1111-1111-1111-111111111111"}]},
                    "Team": {"type": "relation", "relation": [{"id": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"}]},
                }
            },
            {
                "properties": {
                    "GitHub Profile": {"type": "rich_text", "rich_text": [{"plain_text": "@other-user"}]},
                    "Email": {"type": "email", "email": "other@example.com"},
                    "Bugzilla Email": {"type": "email", "email": "bz-other@example.com"},
                    "Phabricator": {"type": "rich_text", "rich_text": [{"plain_text": "other-phab"}]},
                    "User": {"type": "people", "people": [{"id": "22222222-2222-2222-2222-222222222222"}]},
                    "Team": {
                        "type": "relation",
                        "relation": [
                            {"id": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb"},
                            {"id": "cccccccc-cccc-cccc-cccc-cccccccccccc"},
                        ],
                    },
                }
            },
            {
                "properties": {
                    "GitHub Profile": {"type": "url", "url": "https://github.com/ignored"},
                    "Email": {"type": "email", "email": "ignored@example.com"},
                    "Bugzilla Email": {"type": "email", "email": ""},
                    "Phabricator": {"type": "rich_text", "rich_text": [{"plain_text": "ignored-phab"}]},
                    "User": {"type": "people", "people": []},
                    "Team": {"type": "relation", "relation": [{"id": "dddddddd-dddd-dddd-dddd-dddddddddddd"}]},
                }
            },
        ]

        async def fake_iterate(*args, **kwargs):
            for page in pages:
                yield page

        with patch("mzla_notion.people.notion_client.AsyncClient", DummyNotion):
            with patch("mzla_notion.people.async_iterate_paginated_api", fake_iterate):
                user_map = await load_notion_usermap(settings, "NOTION_TOKEN")

        self.assertEqual(
            user_map["github"],
            {
                "example-user": "11111111-1111-1111-1111-111111111111",
                "other-user": "22222222-2222-2222-2222-222222222222",
            },
        )
        self.assertEqual(
            user_map["bugzilla"],
            {
                "user@example.com": "11111111-1111-1111-1111-111111111111",
                "bz-other@example.com": "22222222-2222-2222-2222-222222222222",
            },
        )
        self.assertEqual(
            user_map["phabricator"],
            {
                "example-phab": "11111111-1111-1111-1111-111111111111",
                "other-phab": "22222222-2222-2222-2222-222222222222",
            },
        )
        self.assertEqual(
            user_map["teams"],
            {
                "11111111-1111-1111-1111-111111111111": ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"],
                "22222222-2222-2222-2222-222222222222": [
                    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                    "cccccccccccccccccccccccccccccccc",
                ],
            },
        )

    async def test_load_notion_usermap_missing_config(self):
        user_map = await load_notion_usermap({"people": {"notion_people_id": "db"}}, "NOTION_TOKEN")
        self.assertEqual(user_map, {})


class TestCliHelpers(unittest.TestCase):
    def test_parse_lookback_accepts_seconds(self):
        self.assertEqual(parse_lookback("3600"), 3600)

    def test_parse_lookback_calculates_seconds_from_iso_datetime(self):
        now = datetime.datetime(2026, 8, 24, 12, 0, tzinfo=datetime.UTC)

        self.assertEqual(parse_lookback("2026-08-24T10:30:00Z", now=now), 5400)
        self.assertEqual(parse_lookback("2026-08-24T10:30:00+00:00", now=now), 5400)

    def test_parse_lookback_rejects_future_iso_datetime(self):
        now = datetime.datetime(2026, 8, 24, 12, 0, tzinfo=datetime.UTC)

        with self.assertRaises(argparse.ArgumentTypeError):
            parse_lookback("2026-08-24T12:00:01Z", now=now)

    def test_build_usermap_table_rows(self):
        user_map = {
            "github": {
                "gh1": "notion-a",
                "gh2": "notion-a",
            },
            "bugzilla": {
                "bz1@example.com": "notion-a",
                "bz2@example.com": "notion-b",
            },
            "phabricator": {
                "phab-user-a": "notion-a",
                "phab-user-b": "notion-b",
            },
        }
        phabricator_phids = {
            "phab-user-a": "PHID-USER-aaa",
            "phab-user-b": "PHID-USER-bbb",
        }

        rows = build_usermap_table_rows(user_map, phabricator_phids=phabricator_phids)

        self.assertEqual(
            rows,
            [
                [
                    "notion-a",
                    "gh1, gh2",
                    "bz1@example.com",
                    "PHID-USER-aaa",
                    "phab-user-a",
                ],
                [
                    "notion-b",
                    "",
                    "bz2@example.com",
                    "PHID-USER-bbb",
                    "phab-user-b",
                ],
            ],
        )


class TestSynchronizeCli(unittest.IsolatedAsyncioTestCase):
    async def _run_twoway_cli(self, config_body, **kwargs):
        with tempfile.TemporaryDirectory() as tmpdir:
            config = Path(tmpdir) / "sync.toml"
            config.write_text(config_body, encoding="utf-8")

            tracker = object()
            load_users = AsyncMock(return_value={"github": {}})
            create_github = AsyncMock(return_value=tracker)
            synchronize = AsyncMock()

            with patch.dict(
                "os.environ",
                {"GITHUB_TOKEN": "GITHUB_TOKEN", "NOTION_TOKEN": "NOTION_TOKEN"},
            ):
                with (
                    patch("mzla_notion.cli.load_notion_usermap", load_users),
                    patch("mzla_notion.cli.GitHub.create", create_github),
                    patch("mzla_notion.cli.synchronize_twoway", synchronize),
                ):
                    result = await cmd_synchronize(["services"], str(config), **kwargs)

        return result, tracker, create_github, synchronize

    async def test_project_dry_forces_tracker_and_twoway_sync_dry(self):
        result, tracker, create_github, synchronize = await self._run_twoway_cli(
            """
[sync.services]
method = "tracker_twoway"
tracker = "github"
dry = true
repositories = ["example/repo"]
notion_milestones_id = "milestones-id"
notion_tasks_id = "tasks-id"
""",
            dry_run=False,
        )

        self.assertEqual(result, 0)
        self.assertIs(create_github.await_args.kwargs["dry"], True)
        self.assertIs(synchronize.await_args.kwargs["dry"], True)
        self.assertIs(synchronize.await_args.kwargs["tracker"], tracker)

    async def test_twoway_without_lookback_requests_full_sync(self):
        result, _, _, synchronize = await self._run_twoway_cli(
            """
[sync.services]
method = "tracker_twoway"
tracker = "github"
repositories = ["example/repo"]
notion_milestones_id = "milestones-id"
notion_tasks_id = "tasks-id"
incremental_lookback_seconds = 60
""",
        )

        self.assertEqual(result, 0)
        self.assertIsNone(synchronize.await_args.kwargs["incremental_lookback_seconds"])

    async def test_lookback_cli_is_forwarded_to_twoway_sync(self):
        result, _, _, synchronize = await self._run_twoway_cli(
            """
[sync.services]
method = "tracker_twoway"
tracker = "github"
repositories = ["example/repo"]
notion_milestones_id = "milestones-id"
notion_tasks_id = "tasks-id"
incremental_lookback_seconds = 60
""",
            lookback=3600,
        )

        self.assertEqual(result, 0)
        self.assertEqual(synchronize.await_args.kwargs["incremental_lookback_seconds"], 3600)

    async def test_twoway_cache_config_is_forwarded(self):
        result, _, _, synchronize = await self._run_twoway_cli(
            """
[sync.services]
method = "tracker_twoway"
tracker = "github"
repositories = ["example/repo"]
notion_milestones_id = "milestones-id"
notion_tasks_id = "tasks-id"
twoway_cache_enabled = true
twoway_cache_path = ".cache/custom.sqlite3"
""",
        )

        self.assertEqual(result, 0)
        self.assertTrue(synchronize.await_args.kwargs["twoway_cache_enabled"])
        self.assertEqual(synchronize.await_args.kwargs["twoway_cache_path"], ".cache/custom.sqlite3")

    async def test_twoway_cache_cli_overrides_config(self):
        result, _, _, synchronize = await self._run_twoway_cli(
            """
[sync.services]
method = "tracker_twoway"
tracker = "github"
repositories = ["example/repo"]
notion_milestones_id = "milestones-id"
notion_tasks_id = "tasks-id"
twoway_cache_enabled = false
twoway_cache_path = ".cache/config.sqlite3"
""",
            twoway_cache=True,
            twoway_cache_path=".cache/cli.sqlite3",
        )

        self.assertEqual(result, 0)
        self.assertTrue(synchronize.await_args.kwargs["twoway_cache_enabled"])
        self.assertEqual(synchronize.await_args.kwargs["twoway_cache_path"], ".cache/cli.sqlite3")


if __name__ == "__main__":
    unittest.main()
