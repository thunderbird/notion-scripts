import dateutil.parser
import requests
import settings
import time

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


def page_data(bug, notion_db):
    """Converts `bug` into a dict that matches the formatting for a Notion db page."""
    bug_data = map_bug_to_page(bug)
    props = notion_db.properties

    page = {
        "Status": {"status": {"name": bug_data.pop('Status')}},
        "Summary": {"type": "title", "title": [{"text": {"content": bug_data.pop('Summary')}}]}
    }

    for key, value in bug_data.items():
        if key in props:
            page.update(props[key].update_content(value))

    return page


def get_all_bugs(bzquery: str, bugzilla_api_key: str) -> Dict[str, Any]:
    """Get all bugs from `bzquery` which is the query params from a bz advanced search."""
    base_url = f"{settings.bugzilla_base_url}/rest/bug"
    included_fields = ','.join(settings.bugzilla_fields)
    all_bugs = {}
    offset = 0
    limit = settings.bz_limit  # Changed the settings parameter to bz_limit

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


def bug_page_diff(bug: Dict[str, Any], page: Dict[str, Any], notion_db: NotionDatabase) -> bool:
    """Return true or false based on whether the Notion `page` matches the bug data or not."""
    props = notion_db.properties

    for prop_name, bug_value in map_bug_to_page(bug).items():
        if prop_name in props and props[prop_name].is_prop_diff(page["properties"].get(prop_name, {}), bug_value):
            return True

    return False


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


def update_page(bug, page, notion_db):
    """Helper to update a page in Notion based on bug data."""
    # Only update if data is different.
    if bug_page_diff(bug, page, notion_db):
        data = page_data(bug, notion_db)
        if notion_db.update_page(page["id"], data):
            return True
    return False


def create_page(bug, notion_db):
    """Helper to create a new page in Notion based on bug data."""
    new_page = page_data(bug, notion_db)
    if notion_db.create_page(new_page):
        return True
    else:
        return False


def sync_bugzilla_to_notion(bzquery, bugzilla_api_key, notion_db):
    bugs = get_all_bugs(bzquery, bugzilla_api_key)
    pages = notion_db.get_all_pages()
    bugcount = len(bugs)

    # list of bug numbers to use for deduplication
    pagelist = [page["properties"]["Bug Number"]["number"] for p in pages]

    # dict of bug numbers: pages for bugs in the notion db
    pages_bugs = {p["properties"]["Bug Number"]["number"]:p for p in pages}

    added = 0
    updated = 0
    skipped = 0
    deleted = 0

    # delete pages that no longer match the criteria to be included
    for bnum in pages_bugs.keys():
        if bnum not in bugs.keys() or skip_status(bugs[bnum]) or list(bugs.keys()).count(bnum) > 1:
            notion_db.delete_page(pages_bugs[bnum]["id"])
            deleted += 1

    # Add or update pages corresponding to bugs.
    for bug in bugs.values():
        # Sleep for a bit if we're hammering the Notion API.
        total_changes = added + updated
        if total_changes > 0 and total_changes % 20 == 0:
            print(f"Added {added} bugs, updated {updated}, deleted {deleted} and skipped {skipped}")
            print("Sleeping for 10 seconds...")
            time.sleep(10)

        if skip_status(bug):
                skipped += 1
        elif bug["id"] in pages_bugs.keys():
            if update_page(bug, pages_bugs[bug["id"]], notion_db):
                updated += 1
        else:
            if create_page(bug, notion_db):
                added += 1

    # Finish up and summarize results.
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    pagecount = len(pages)
    print(f"{timestamp} synced {bugcount} bugs in query, {pagecount} in Notion: Added {added}, updated {updated}, deleted {deleted} and skipped {skipped}")
