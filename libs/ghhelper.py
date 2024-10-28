import ghsettings
import os
import requests
import time

from github import Auth
from github import Github
from typing import Dict, Any

def issue_status_to_notion(issue) -> str:
    """Convert a GH issue state to a Notion database status."""
    if issue.state == "closed":
        status = "Done"
    elif issue.state == "open":
        if issue.assignee:
            status = "In progress"
        else:
            status = "Not started"

    return status

def map_issue_to_page(issue):
    """Map a single issue's data into the datadict format for the NotionDatabase class. """
    notion_data = {
        'Status': issue_status_to_notion(issue),
        'Assignee': issue.assignee.login if issue.assignee else '',
        'Issue Number': issue.number,
        'Link': issue.html_url,
        'Title': issue.title,
        'Repository': issue.repository.name,
        'Node ID': issue.id
        #'Labels':
    }

    # for label in issue.get_labels():
    return notion_data


def get_all_issues(status: str = 'all') -> Dict[str, Any]:
    """Get all issues from repo """
    token = os.environ['GITHUB_TOKEN']
    auth = Auth.Token(token)
    g = Github(auth=auth)
    all_issues = {}
    for r in ghsettings.repos:
        repo = g.get_repo(ghsettings.orgname + r)
        all_issues[r] = repo.get_issues(state=status)
    g.close()
    return all_issues


def sync_github_to_notion(issues, pages, notion_db):
    # dict of issues numbers: pages for issues in the notion db
    # ["properties"]["Node ID"]["rich_text"][0]["plain_text"]
    pages_issues = {p["properties"]["Node ID"]["number"]:p for p in pages}

    added = 0
    updated = 0
    deleted = 0
    issue_count = 0
    for repo in issues.values():
        issue_count += repo.totalCount
        for issue in repo:
            # Sleep for a bit if we're hammering the Notion API.
            total_changes = added + updated
            if total_changes > 0 and total_changes % 20 == 0:
                print(f"Added {added} issues, updated {updated}, deleted {deleted}")
                print("Sleeping for 10 seconds...")
                time.sleep(10)

            if issue.number in pages_issues.keys():
                if notion_db.update_page(pages_issues[issue.id], map_issue_to_page(issue)):
                    updated += 1
            else:
                if notion_db.create_page(map_issue_to_page(issue)):
                    added += 1

    print(f"Sync Complete. {issue_count} issues in query, Added {added}, updated {updated}, and deleted {deleted}")
