import dateutil.parser
import requests
import bzsettings
import time

from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, Any

from .notion_data import NotionDatabase

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
    """Mapping for bug fields to Notion properties. """
    # This is a datadict.
    notion_data = {
        'Status': bug_status_to_notion(bug),
        'Assignee': bug["assigned_to"],
        'Bug Number': bug["id"],
        'Component': bug["component"],
        'Keywords': " ".join(bug["keywords"]),
        'Link': "https://bugzil.la/" + str(bug["id"]),
        'Product': bug["product"],
        'Version': bug["version"],
        'Whiteboard': bug["whiteboard"],
        'Summary': f'{bug["id"]} - {bug["summary"]}'
    }

    return notion_data


def get_all_bugs(bzquery: str, bugzilla_api_key: str) -> Dict[str, Any]:
    """Get all bugs from `bzquery` which is the query params from a bz advanced search."""
    base_url = f"{bzsettings.bugzilla_base_url}/rest/bug"
    included_fields = ','.join(bzsettings.bugzilla_fields)
    all_bugs = {}
    offset = 0
    limit = bzsettings.bz_limit

    while True:
        url = f"{base_url}{bzquery}&api_key={bugzilla_api_key}&include_fields={included_fields}&limit={limit}&offset={offset}"

        response = requests.get(url)
        response_json = response.json()

        if 'bugs' in response_json:
            bugs = response_json['bugs']
            if not bugs:
                break
            all_bugs.update({b['id']: b for b in bugs})
            offset += limit
        else:
            break

    return all_bugs


def is_old(bug, days=90):
    """Determine if a bug was last resolved more than `days` ago."""
    timestamp = dateutil.parser.parse(bug["cf_last_resolved"]).replace(tzinfo=None)
    return timestamp < (datetime.utcnow() - timedelta(days=days))


def skip_status(bug):
    """Determine if a bug should be skipped or not. If it's skippable, it will be deleted from the db
    if it already exists in the db."""
    skip_status = ["UNCONFIRMED"]

    if bug["status"] in skip_status:
        return True
    elif bug["resolution"] == "DUPLICATE":
        return True
    elif (bug["status"] == "RESOLVED" or bug["status"] == "VERIFIED") and is_old(bug):
        return True
    else:
        return False


def remove_duplicates(pages, notion_db):
    """Removes duplicate pages based on bug numbers, keeping only
       one page per bug number."""
    bug_to_pages = defaultdict(list)
    total_deleted = 0   # Total number of duplicates deleted

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
                notion_db.delete_page(page["id"])
                pages.remove(page)
                total_deleted += 1

                if total_deleted % 20 == 0:
                    print(f"Total duplicates deleted: {total_deleted}")
                    print("Pausing for 10 seconds...")
                    time.sleep(10)

    # Print final total of duplicates deleted
    print(f"Total duplicates deleted: {total_deleted}")


def sync_bugzilla_to_notion(bugs, pages, notion_db):
    bugcount = len(bugs)

    # dict of bug numbers: pages for bugs in the notion db
    pages_bugs = {p["properties"]["Bug Number"]["number"]:p for p in pages}

    added = 0
    updated = 0
    skipped = 0
    deleted = 0
    last_skip = False

    # delete pages that no longer match the criteria to be included
    for bnum in pages_bugs.keys():
        if bnum not in bugs.keys() or skip_status(bugs[bnum]) or list(bugs.keys()).count(bnum) > 1:
            notion_db.delete_page(pages_bugs[bnum]["id"])
            deleted += 1

    # If we somehow have duplicates in Notion, remove them.
    remove_duplicates(pages, notion_db)

    # Add or update pages corresponding to bugs.
    for bug in bugs.values():
        # Sleep for a bit if we're hammering the Notion API.
        total_changes = added + updated
        if not last_skip and total_changes > 0 and total_changes % 20 == 0:
            print(f"Added {added} bugs, updated {updated}, deleted {deleted} and skipped {skipped}")
            print("Sleeping for 10 seconds...")
            time.sleep(10)
        # We only skip pausing for one iteration after a skip, so this resets.
        last_skip = False

        if skip_status(bug):
                skipped += 1
                last_skip = True
        elif bug["id"] in pages_bugs.keys():
            if notion_db.update_page(pages_bugs[bug["id"]], map_bug_to_page(bug)):
                updated += 1
        else:
            if notion_db.create_page(map_bug_to_page(bug)):
                added += 1

    # Finish up and summarize results.
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    pagecount = len(pages)
    print(f"{timestamp} synced {bugcount} bugs in query, {pagecount} in Notion: Added {added}, updated {updated}, deleted {deleted} and skipped {skipped}")
