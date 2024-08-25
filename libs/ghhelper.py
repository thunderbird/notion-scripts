import requests
import settings
import time
import os

from datetime import datetime, timedelta
from typing import Dict, Any

from .notion_data import NotionDatabase
from github import Auth
from github import Github
import pdb


PROJECT_PHASE_PREFIX = "phase:"

def issue_status_to_notion(issue):
    """Convert a GH state to values suitable for Notion."""
    # TODO
    return issue.state

def map_issue_to_page(issue):
    """Mapping for issue fields to Notion properties. """
    notion_data = {
        'Bug Status': issue.state,
        'Assignee': issue.assignee if issue.assignee else '',
        'Bug Number': issue.number,
        'Link': issue.url,
        'Summary': issue.title
        #'Labels': 
    }
    for label in issue.get_labels():
        label_name = label.name
        if label_name.startswith(PROJECT_PHASE_PREFIX):
            print("got phase: ", label_name);
            notion_data['Phase']: label_name[len(PROJECT_PHASE_PREFIX):].strip()
    return notion_data

def page_data(issue, notion_db):
    """Converts `issue` into a dict that matches the formatting for a Notion db page."""
    issue_data = map_issue_to_page(issue)
    props = notion_db.properties

    page = {
        "Status": {"status": {"name": issue_data.pop('Bug Status')}},
        "Summary": {"type": "title", "title": [{"text": {"content": issue_data.pop('Summary')}}]}
    }

    for key, value in issue_data.items():
        if key in props:
            page.update(props[key].update_content(value))

    return page

def get_all_issues(repo: str, gh_api_key: str, status: str = 'open') -> Dict[str, Any]:
    """Get all issues from repo """
    token = os.environ['GITHUB_TOKEN']
    auth = Auth.Token(token)
    g = Github(auth=auth)
    repo = g.get_repo('thunderbird/appointment')
    issues = repo.get_issues(state=status)
    g.close()
    return issues


def issue_page_diff(issue: Dict[str, Any], page: Dict[str, Any], notion_db: NotionDatabase) -> bool:
    """Return true or false based on whether the Notion `page` matches the issue data or not."""
    props = notion_db.properties

    for prop_name, isue_value in map_issue_to_page(issue).items():
        if prop_name in props and props[prop_name].is_prop_diff(page["properties"].get(prop_name, {}), issue_value):
            return True

    return False


def update_page(issue, page, notion_db):
    """Helper to update a page in Notion based on issue data."""
    # Only update if data is different.
    if issue_page_diff(issue, page, notion_db):
        data = page_data(issue, notion_db)
        if notion_db.update_page(page["id"], data):
            return True
    return False


def create_page(issue, notion_db):
    """Helper to create a new page in Notion based on issue data."""
    new_page = page_data(issue, notion_db)
    pdb.set_trace();
    if notion_db.create_page(new_page):
        return True
    else:
        return False


def sync_gh_to_notion(repo, gh_api_key, notion_db):
    issues = get_all_issues(repo, gh_api_key)
    print('retrieved: ', issues);
    pages = notion_db.get_all_pages()
    issue_count = issues.totalCount
    # dict of issues numbers: pages for issues in the notion db
    pages_issues = {p["properties"]["Bug Number"]["number"]:p for p in pages}
    issue_ids = [issue.number for issue in issues]

    added = 0
    updated = 0
    deleted = 0

    # delete pages that no longer match the criteria to be included
    for inum in pages_issues.keys():
        if inum and inum not in issue_ids:
            notion_db.delete_page(pages_issues[inum]["id"])
            print('deleting: ', inum)
            deleted += 1

    # Add or update pages corresponding to issue.
    for issue in issues:
        # Sleep for a bit if we're hammering the Notion API.
        total_changes = added + updated
        if total_changes > 0 and total_changes % 20 == 0:
            print(f"Added {added} issues, updated {updated}, and deleted {deleted}")
            print("Sleeping for 10 seconds...")
            time.sleep(10)

        elif "id" in pages_issues.keys():
            if update_page(issue, pages_issues[issue["id"]], notion_db):
                updated += 1
        else:
            if create_page(issue, notion_db):
                added += 1
    print(len(pages))
    print(f"Sync Complete. {issue_count} issues in query, {pagecount} in Notion: Added {added}, updated {updated}, and deleted {deleted}")
