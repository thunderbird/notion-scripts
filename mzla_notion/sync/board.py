# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import datetime
import notion_client
import re
import asyncio

from functools import cached_property

from .. import notion_data as p
from ..util import getnestedattr, RetryingClient, AsyncRetryingClient
from ..notion_data import NotionDatabase

logger = logging.getLogger("board_sync")


DONE_STATES = ("Done", "Cancelled", "Canceled")
INPROGRESS_STATES = ("In progress", "In Progress")


class BoardSync:
    """This is a cross-functional board sync within notion.

    With our current setup there is no great way to show milestones for one initiative across teams.
    This is a hack to keep the dates and status in sync.
    """

    LAST_SYNC_MESSAGE = "Last Sync ({0}): {1}"

    def __init__(self, project_key, notion_token, board_id, properties={}, dry=False, synchronous=False):
        """Initialize board sync."""
        # TODO async everything
        self.notion = notion_client.Client(auth=notion_token, client=RetryingClient(http2=True))
        self.anotion = notion_client.AsyncClient(auth=notion_token, client=AsyncRetryingClient(http2=True))
        self.project_key = project_key
        self.dry = dry
        self.synchronous = synchronous

        self.database_props = {}
        for propkey, props in properties.items():
            dbid = props["database"]
            del props["database"]
            props["area"] = propkey[0].upper() + propkey[1:]
            self.database_props[dbid] = props

        team_options = [props["area"] for props in self.database_props.values()]
        team_options.append("Needs Milestone")

        board_properties = [p.title("Name"), p.dates("Dates"), p.status("Status"), p.select("Team", team_options)]
        self.board_db = NotionDatabase(board_id, self.notion, board_properties, dry=dry)
        if not self.board_db.validate_props():
            raise Exception("Milestone schema failed to validate")

    def _get_date_prop(self, block_or_page, propinfo, default=None):
        if isinstance(propinfo, list):
            start_prop_name, end_prop_name = propinfo
            start_prop_key = end_prop_key = "start"
        else:
            start_prop_name = end_prop_name = propinfo
            start_prop_key = "start"
            end_prop_key = "end"

        start_prop = getnestedattr(lambda: block_or_page["properties"][start_prop_name], default)
        end_prop = getnestedattr(lambda: block_or_page["properties"][end_prop_name], default)

        return (
            getnestedattr(lambda: start_prop[start_prop["type"]][start_prop_key], default),
            getnestedattr(lambda: end_prop[end_prop["type"]][end_prop_key], default),
        )

    def _get_prop(self, block_or_page, prop_name, default=None, safe=True):
        if safe:
            prop = getnestedattr(lambda: block_or_page["properties"][prop_name], default)
            return getnestedattr(lambda: prop[prop["type"]], default) if prop else default
        else:
            prop = block_or_page["properties"][prop_name]
            return prop[prop["type"]]

    def _get_richtext_prop(self, block_or_page, key_name, default=None, safe=True):
        prop = self._get_prop(block_or_page, key_name, default, safe)

        if prop:
            return "".join(map(lambda rich_text: rich_text["plain_text"], prop))
        else:
            return default

    def _update_timestamp(self, database, timestamp):
        if self.dry:
            return

        timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
        pattern = re.escape(self.LAST_SYNC_MESSAGE.format(self.project_key, "REGEX_PLACEHOLDER"))
        pattern = pattern.replace("REGEX_PLACEHOLDER", r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")

        description, count = re.subn(
            pattern, self.LAST_SYNC_MESSAGE.format(self.project_key, timestamp), database.description
        )

        if count < 1:
            description = self.LAST_SYNC_MESSAGE.format(self.project_key, timestamp) + "\n\n" + description

        database.description = description

    @cached_property
    def _all_board_pages(self):
        return self.board_db.get_all_pages()

    async def _get_page_notion_data(self, page):
        earliest_start = unchanged_start = datetime.datetime.max.replace(tzinfo=datetime.timezone.utc)
        latest_end = unchanged_end = datetime.datetime.min.replace(tzinfo=datetime.timezone.utc)
        status = "Done"
        title = ""
        area = None

        for name, data in page["properties"].items():
            firstrel = next(iter(data.get("relation", [])), None)
            if not firstrel:
                continue

            relpage = await self.anotion.pages.retrieve(firstrel["id"])
            relprops = relpage["properties"]

            parent_db = relpage["parent"]["database_id"]
            reldbprops = self.database_props.get(parent_db.replace("-", ""), {})
            area = reldbprops.get("area")

            # Dates
            date_props = reldbprops.get("dates")
            if not date_props:
                from pprint import pprint

                pprint(await self.anotion.databases.retrieve(parent_db))
                raise Exception(f"Could not find date props for {parent_db}")

            start_date, end_date = self._get_date_prop(relpage, date_props)

            if start_date:
                start_date = datetime.datetime.fromisoformat(start_date).replace(tzinfo=datetime.timezone.utc)
                earliest_start = min(start_date, earliest_start)

            if end_date:
                end_date = datetime.datetime.fromisoformat(end_date).replace(tzinfo=datetime.timezone.utc)
                latest_end = max(end_date, latest_end)

            # Status
            relstatus = relprops["Status"]["status"]["name"]

            if relstatus not in DONE_STATES:
                status = "In progress"

                if relstatus not in INPROGRESS_STATES:
                    status = "Not started"

            # Titles
            title = self._get_richtext_prop(relpage, reldbprops.get("title"), default="")

        # If there are no set relations change nothing
        if not area:
            return None

        dates = {
            "start": earliest_start if earliest_start != unchanged_start else None,
            "end": latest_end if latest_end != unchanged_end else None,
        }

        notion_data = {
            "Dates": dates if dates["start"] or dates["end"] else None,
            "Status": status,
            "Team": area,
            "Name": title,
        }

        return notion_data

    async def synchronize_single_page(self, page):
        """Synchronize a single notion page."""
        notion_data = await self._get_page_notion_data(page)

        if notion_data and await self.board_db.update_page_async(self.anotion, page, notion_data):
            logger.info(f"Updated {page['url']} with {notion_data}")
        else:
            logger.info(f"Unchanged {page['url']}")

    async def synchronize(self):
        """Synchronize the milestones."""
        timestamp = datetime.datetime.now(datetime.UTC)

        if self.synchronous:
            for page in self._all_board_pages:
                await self.synchronize_single_page(page)
        else:
            async with asyncio.TaskGroup() as tg:
                for page in self._all_board_pages:
                    tg.create_task(self.synchronize_single_page(page))

        self._update_timestamp(self.board_db, timestamp)


def synchronize(**kwargs):
    """Exported method to begin synchronization."""
    asyncio.run(BoardSync(**kwargs).synchronize())
