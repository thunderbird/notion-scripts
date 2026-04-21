import datetime
import unittest

from mzla_notion.notion_data import date, dates
from mzla_notion.util import NotionQueryIncompleteError, check_notion_request_status, guard_notion_query_response


class NotionDateDiffTest(unittest.TestCase):
    def test_dates_compares_only_down_to_minute(self):
        prop = dates("Dates")
        property_data = {
            "date": {
                "start": "2026-03-23T17:51:00.000+00:00",
                "end": "2026-04-27T00:00:00.000+00:00",
            }
        }
        content = {
            "start": datetime.datetime(2026, 3, 23, 17, 51, 6, tzinfo=datetime.timezone.utc),
            "end": datetime.datetime(2026, 4, 27, 0, 0, 45, tzinfo=datetime.timezone.utc),
        }
        self.assertFalse(prop.is_prop_diff(property_data, content))

    def test_dates_treats_date_and_midnight_utc_datetime_as_equal(self):
        prop = dates("Dates")
        property_data = {
            "date": {
                "start": "2026-03-23T17:51:00.000+00:00",
                "end": "2026-04-27T00:00:00.000+00:00",
            }
        }
        content = {
            "start": datetime.datetime(2026, 3, 23, 17, 51, 0, tzinfo=datetime.timezone.utc),
            "end": datetime.date(2026, 4, 27),
        }
        self.assertFalse(prop.is_prop_diff(property_data, content))

    def test_dates_keeps_non_midnight_datetime_different_from_date(self):
        prop = dates("Dates")
        property_data = {
            "date": {
                "start": "2026-03-23T17:51:00.000+00:00",
                "end": "2026-04-27",
            }
        }
        content = {
            "start": datetime.datetime(2026, 3, 23, 17, 51, 0, tzinfo=datetime.timezone.utc),
            "end": datetime.datetime(2026, 4, 27, 0, 1, 0, tzinfo=datetime.timezone.utc),
        }
        self.assertTrue(prop.is_prop_diff(property_data, content))

    def test_date_treats_date_and_midnight_utc_datetime_as_equal(self):
        prop = date("Date")
        property_data = {"date": {"start": "2026-04-27T00:00:00.000+00:00"}}
        content = datetime.date(2026, 4, 27)
        self.assertFalse(prop.is_prop_diff(property_data, content))

    def test_dates_treats_date_only_notion_strings_as_equal_to_dates(self):
        prop = dates("Dates")
        property_data = {"date": {"start": "2025-03-10", "end": "2025-03-16"}}
        content = {"start": datetime.date(2025, 3, 10), "end": datetime.date(2025, 3, 16)}
        self.assertFalse(prop.is_prop_diff(property_data, content))

    def test_dates_update_preserves_date_without_time(self):
        prop = dates("Dates")
        updated = prop.update_content({"start": datetime.date(2026, 4, 27), "end": datetime.date(2026, 4, 28)})
        self.assertEqual(updated["Dates"]["date"]["start"], "2026-04-27")
        self.assertEqual(updated["Dates"]["date"]["end"], "2026-04-28")

    def test_dates_update_preserves_datetime(self):
        prop = dates("Dates")
        updated = prop.update_content(
            {
                "start": datetime.datetime(2026, 4, 27, 13, 45, 6, tzinfo=datetime.timezone.utc),
                "end": datetime.datetime(2026, 4, 28, 8, 1, 2, tzinfo=datetime.timezone.utc),
            }
        )
        self.assertEqual(updated["Dates"]["date"]["start"], "2026-04-27T13:45:06+00:00")
        self.assertEqual(updated["Dates"]["date"]["end"], "2026-04-28T08:01:02+00:00")

    def test_date_update_preserves_date_without_time(self):
        prop = date("Date")
        updated = prop.update_content(datetime.date(2026, 4, 27))
        self.assertEqual(updated["Date"]["date"]["start"], "2026-04-27")


class NotionRequestStatusTest(unittest.IsolatedAsyncioTestCase):
    async def test_check_notion_request_status_raises_on_query_limit(self):
        response = {
            "results": [],
            "request_status": {
                "type": "incomplete",
                "incomplete_reason": "query_result_limit_reached",
            },
        }
        with self.assertRaises(NotionQueryIncompleteError):
            check_notion_request_status(response, context="Notion database query (db-id)")

    async def test_guard_notion_query_response_raises_on_query_limit(self):
        async def fake_query(**kwargs):
            return {
                "results": [],
                "request_status": {
                    "type": "incomplete",
                    "incomplete_reason": "query_result_limit_reached",
                },
            }

        guarded = guard_notion_query_response(fake_query, context="Notion database query (db-id)")
        with self.assertRaisesRegex(NotionQueryIncompleteError, r"filter=.*Status"):
            await guarded(database_id="db-id", filter={"property": "Status", "status": {"equals": "In progress"}})

    async def test_guard_notion_query_response_passes_when_complete(self):
        async def fake_query(**kwargs):
            return {"results": [], "has_more": False}

        guarded = guard_notion_query_response(fake_query, context="Notion database query (db-id)")
        response = await guarded(database_id="db-id")
        self.assertEqual(response["results"], [])


if __name__ == "__main__":
    unittest.main()
