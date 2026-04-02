import datetime
import unittest

from mzla_notion.notion_data import date, dates


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


if __name__ == "__main__":
    unittest.main()
