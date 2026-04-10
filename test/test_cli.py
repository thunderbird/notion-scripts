import unittest

from unittest.mock import patch

from mzla_notion.people import load_notion_usermap, build_usermap_table_rows


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
                }
            },
            {
                "properties": {
                    "GitHub Profile": {"type": "rich_text", "rich_text": [{"plain_text": "@other-user"}]},
                    "Email": {"type": "email", "email": "other@example.com"},
                    "Bugzilla Email": {"type": "email", "email": "bz-other@example.com"},
                    "Phabricator": {"type": "rich_text", "rich_text": [{"plain_text": "other-phab"}]},
                    "User": {"type": "people", "people": [{"id": "22222222-2222-2222-2222-222222222222"}]},
                }
            },
            {
                "properties": {
                    "GitHub Profile": {"type": "url", "url": "https://github.com/ignored"},
                    "Email": {"type": "email", "email": "ignored@example.com"},
                    "Bugzilla Email": {"type": "email", "email": ""},
                    "Phabricator": {"type": "rich_text", "rich_text": [{"plain_text": "ignored-phab"}]},
                    "User": {"type": "people", "people": []},
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

    async def test_load_notion_usermap_missing_config(self):
        user_map = await load_notion_usermap({"people": {"notion_people_id": "db"}}, "NOTION_TOKEN")
        self.assertEqual(user_map, {})


class TestCliHelpers(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
