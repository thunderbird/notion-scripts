import ghsettings
import os
import requests
import time

from datetime import datetime
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from sgqlc_schemas import github_schema as schema
from typing import Dict, Any

def map_issue_to_page(issue, milestones):
    """Map a single issue's data into the datadict format for the NotionDatabase class. """
    notion_data = {
        'Assignee': ' '.join(a.login for a in issue.assignees.nodes) if issue.assignees.nodes else '',
        'Link': issue.url,
        'Title': issue.title,
        'Repository': issue.repository.name,
        'Unique ID': issue.id,
        'Opened': issue.created_at,
        'Closed': issue.closed_at,
        'Labels': [l.name for l in issue.labels.nodes],
    }

    if issue.state == "CLOSED":
        notion_data['Status'] = "Done"

    filtered_labels = [label[2:].strip() for label in notion_data['Labels'] if label.startswith("M:") and label[2:].strip() in milestones]
    notion_data['Milestones'] = [milestones[label] for label in filtered_labels]

    # for label in issue.get_labels():
    return notion_data


def get_issues_from_repo(reponame):
    endpoint = HTTPEndpoint('https://api.github.com/graphql', {'Authorization': f'Bearer {os.getenv("GITHUB_TOKEN")}'})
    has_next_page = True
    cursor = None

    all_issues = []
    while has_next_page:
        op = Operation(schema.query_type)
        issues = op.repository(owner=ghsettings.orgname, name=reponame).issues(first=100, after=cursor)
        issues.nodes.created_at()
        issues.nodes.closed_at()
        issues.nodes.title()
        issues.nodes.state()
        issues.nodes.url()
        issues.nodes.id()
        issues.nodes.repository().name()
        issues.nodes.labels(first=100).nodes.name()
        issues.nodes.assignees(first=10).nodes.login()
        issues.page_info.__fields__(has_next_page=True)
        issues.page_info.__fields__(end_cursor=True)
        data = endpoint(op)

        # sgqlc magic to turn the response into an object rather than a dict
        repo = (op + data).repository
        all_issues.extend(repo.issues.nodes)

        # pagination
        has_next_page = repo.issues.page_info.has_next_page
        cursor = repo.issues.page_info.end_cursor
    return all_issues


def get_all_issues(status: str = 'all') -> Dict[str, Any]:
    """Get all issues from repo """
    all_issues = {}
    for r in ghsettings.repos:
        all_issues[r] = get_issues_from_repo(r)
    return all_issues


def extract_labels(issues):
    """Extract labels into a list with no duplicates."""
    labels = set()

    for repo in issues.values():
        for issue in repo:
            for label in issue.labels.nodes:
                labels.add(label.name)
    return labels


def extract_milestones(pages):
    """ Convert pages from the Notion Milestones database into a dict of milestone_title:page_id. """
    milestones = {}
    for page in pages:
        for prop in page["properties"].values():
            if prop["id"] == "title":
                title = prop["title"][0]["plain_text"]
                if title:
                    milestones[title] = page["id"]
    return milestones


def sync_github_to_notion(issues, pages, milestones, notion_db):
    # dict of issues numbers: pages for issues in the notion db
    pages_issues = {p["properties"]["Unique ID"]["rich_text"][0]["plain_text"]:p for p in pages}

    added = 0
    updated = 0
    issue_count = 0
    for repo in issues.values():
        issue_count += len(repo)
        for issue in repo:
            # Sleep for a bit if we're hammering the Notion API.
            total_changes = added + updated
            if total_changes > 0 and total_changes % 20 == 0:
                print(f"Added {added} issues, updated {updated}")
                print("Sleeping for 10 seconds...")
                time.sleep(10)

            if issue.id in pages_issues.keys():
                if notion_db.update_page(pages_issues[issue.id], map_issue_to_page(issue, milestones)):
                    updated += 1
            else:
                if notion_db.create_page(map_issue_to_page(issue, milestones)):
                    added += 1
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    page_count = len(pages)
    notion_db.description = f"Last Sync: {timestamp} UTC"
    print(f"{timestamp} synced {issue_count} issues in query, {page_count} were in Notion: Added {added} and updated {updated}.")
