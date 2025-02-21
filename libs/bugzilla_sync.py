# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
from collections import defaultdict
from datetime import datetime, timedelta
from typing import Any, Dict, List

import dateutil.parser
import requests
from notion_client import Client

from . import notion_data as p
from .notion_data import NotionDatabase

logger = logging.getLogger("bugzilla_sync")

# List of bugzilla fields to include in queries using included_fields.
# These do not always have a 1:1 relationship with Notion fields.
# There is a map_bug_to_page function to map bug data to Notion fields.
bugzilla_fields = [
    "id",  # Bug Number
    "assigned_to",  # Email of assignee
    "cf_last_resolved",
    "component",
    "keywords",
    "last_change_time",
    "product",
    "resolution",  # Needed as part of status
    "summary",
    "status",
    "version",
    "whiteboard",
]


def synchronize(
    notion_token,
    bugzilla_base_url,
    bugzilla_api_key,
    bugs_id,
    products,
    bugzilla_limit=100,
    list_id=None,
    dry=False,
):
    """Synchronize Bugzilla with Notion.

    Args:
        notion_token (str): The notion integration auth token.
        bugzilla_base_url (str): The base url where the bugzilla instance is.
        bugzilla_api_key (str): The api key for bugzilla.
        bugs_id (str): The id of the notion database where all bugs should be placed.
        products (list[str]): A list of bugzilla products to sync.
        bugzilla_limit (int): The number of items to sync at once.
        list_id (int): The saved search list id, to speed up queries.
        dry (bool): If true, no mutating operations will occur.
    """
    notion = Client(auth=notion_token)

    properties = [
        p.rich_text("Assignee"),
        p.number("Bug Number"),
        p.rich_text("Component"),
        p.rich_text("Keywords"),
        p.link("Link"),
        p.select("Product", products),
        p.title("Summary"),
        p.rich_text("Version"),
        p.rich_text("Whiteboard"),
    ]

    bzquery = (
        "?bug_status=NEW"
        "&bug_status=ASSIGNED"
        "&bug_status=REOPENED"
        "&bug_status=RESOLVED"
        "&bug_status=VERIFIED"
        "&bug_status=CLOSED"
        "&f1=OP"
        "&f2=days_elapsed"
        "&f3=CP"
        "&o2=lessthaneq"
        "&query_format=advanced"
        "&v2=90"
        "&order=changeddate DESC"
    )

    if list_id:
        bzquery += "&list_id=" + list_id

    for product in products:
        bzquery += "&product=" + product

    # Initialize python representation of the Notion DB.
    notion_db = NotionDatabase(bugs_id, notion, properties, dry=dry)

    # Ensure the database has the properties we expect.
    # This should probably happen on init, but we'll do it explicitly for now.
    notion_db.update_props(dry=dry)

    # Get all the bugs we want to sync from the Bugzilla API.
    bugs = get_all_bugs(bugzilla_base_url, bzquery, bugzilla_api_key, bugzilla_fields)
    num_bugs = len(bugs)
    logger.info(f"Bugzilla API get completed, found {num_bugs} bugs.")

    # Get all the pages currently in the Notion db.
    pages = notion_db.get_all_pages()
    num_pages = len(pages)
    logger.info(f"Notion API get completed, found {num_pages} pages.")

    # dict of bug numbers: pages for bugs in the notion db
    pages_bugs = {p["properties"]["Bug Number"]["number"]: p for p in pages}
    bugcount = len(bugs)

    added = 0
    updated = 0
    skipped = 0
    deleted = 0

    # delete pages that no longer match the criteria to be included
    for bnum in pages_bugs.keys():
        if bnum not in bugs.keys() or skip_status(bugs[bnum]) or list(bugs.keys()).count(bnum) > 1:
            if dry:
                logger.info(f"Deleting page for bug {bnum}")
            else:
                notion_db.delete_page(pages_bugs[bnum]["id"])
            deleted += 1

    # If we somehow have duplicates in Notion, remove them.
    total_deleted = remove_duplicates(pages, notion_db, dry=dry)
    logger.info(f"Total duplicates deleted: {total_deleted}")

    # Add or update pages corresponding to bugs.
    for bug in bugs.values():
        if skip_status(bug):
            skipped += 1

        elif bug["id"] in pages_bugs.keys():
            if dry:
                logger.info(f"Updating page for bug {bug['id']}")
            else:
                if notion_db.update_page(pages_bugs[bug["id"]], map_bug_to_page(bug)):
                    updated += 1
        else:
            if dry:
                logger.info(f"Creating page for bug {bug['id']}")
            else:
                if notion_db.create_page(map_bug_to_page(bug)):
                    added += 1

    # Finish up and summarize results.
    pagecount = len(pages)
    logger.info(
        f"Synced {bugcount} bugs in query, {pagecount} in Notion: "
        f"Added {added}, updated {updated}, deleted {deleted} and skipped {skipped}"
    )


def bug_status_to_notion(bug: Dict[str, Any]) -> str:
    """Convert a Bugzilla status to values suitable for Notion."""
    done = ["VERIFIED", "RESOLVED"]
    status = "Not started"
    if bug["status"] in done:
        status = "Done"
    elif bug["assigned_to"] != "nobody@mozilla.org":
        status = "In progress"
    return status


def map_bug_to_page(bug):
    """Mapping for bug fields to Notion properties."""
    # This is a datadict.
    notion_data = {
        "Status": bug_status_to_notion(bug),
        "Assignee": bug["assigned_to"],
        "Bug Number": bug["id"],
        "Component": bug["component"],
        "Keywords": " ".join(bug["keywords"]),
        "Link": "https://bugzil.la/" + str(bug["id"]),
        "Product": bug["product"],
        "Version": bug["version"],
        "Whiteboard": bug["whiteboard"],
        "Summary": f'{bug["id"]} - {bug["summary"]}',
    }

    return notion_data


def get_all_bugs(
    bugzilla_base_url: str,
    bzquery: str,
    bugzilla_api_key: str,
    bugzilla_fields: List[str],
    bugzilla_limit: int,
) -> Dict[str, Any]:
    """Get all bugs from `bzquery` which is the query params from a bz advanced search."""
    base_url = f"{bugzilla_base_url}/rest/bug"
    included_fields = ",".join(bugzilla_fields)
    all_bugs = {}
    offset = 0

    while True:
        url = (
            f"{base_url}{bzquery}&api_key={bugzilla_api_key}&include_fields={included_fields}&"
            f"limit={bugzilla_limit}&offset={offset}"
        )

        response = requests.get(url)
        response_json = response.json()

        if "bugs" in response_json:
            bugs = response_json["bugs"]
            if not bugs:
                break
            all_bugs.update({b["id"]: b for b in bugs})
            offset += bugzilla_limit
        else:
            break

    return all_bugs


def is_old(bug, days=90):
    """Determine if a bug was last resolved more than `days` ago."""
    timestamp = dateutil.parser.parse(bug["cf_last_resolved"]).replace(tzinfo=None)
    return timestamp < (datetime.utcnow() - timedelta(days=days))


def skip_status(bug):
    """Determine if a bug should be skipped or not.

    If it's skippable, it will be deleted from the db if it already exists in the db.
    """
    skip_status = ["UNCONFIRMED"]

    if bug["status"] in skip_status:
        return True
    elif bug["resolution"] == "DUPLICATE":
        return True
    elif (bug["status"] == "RESOLVED" or bug["status"] == "VERIFIED") and is_old(bug):
        return True
    else:
        return False


def remove_duplicates(pages, notion_db, dry=False):
    """Removes duplicate pages based on bug numbers, keeping only one page per bug number."""
    bug_to_pages = defaultdict(list)
    total_deleted = 0  # Total number of duplicates deleted

    # Map each bug number to its corresponding pages
    for page in pages:
        bug_number = page["properties"]["Bug Number"]["number"]
        bug_to_pages[bug_number].append(page)

    # Iterate over the bug numbers and delete duplicate pages
    for bug_number, page_list in bug_to_pages.items():
        if len(page_list) > 1:
            # Keep the first page and delete the rest
            pages_to_delete = page_list[1:]
            for page in pages_to_delete:
                if not dry:
                    notion_db.delete_page(page["id"])

                pages.remove(page)
                total_deleted += 1

    return total_deleted
