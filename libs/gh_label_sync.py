# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import logging

from datetime import datetime
from typing import Any, Dict

from notion_client import Client
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from . import notion_data as p
from .notion_data import NotionDatabase
from .util import getnestedattr, RetryingClient
from .github_schema import schema

logger = logging.getLogger("gh_label_sync")


def synchronize(
    notion_token,
    milestones_id,
    tasks_id,
    repositories,
    milestone_prefix="M:",
    sync_status="all",
    strip_orgname=False,
    dry=False,
):
    """Synchronize all issues into Notion.

    Args:
        notion_token (str): The notion integration auth token.
        milestones_id (str): The ID of the milestones database in notion.
        tasks_id (str): The ID of the "All GitHub Issues" database in notion.
        repositories (list[str]): A list of orgname/repo with the repositories to sync.
        milestone_prefix (str): The prefix for milestone labels. See README
        sync_status (str): Set to "all" to sync all issues.
        strip_orgname (bool): If true, the organization name will be stripped from the repo field.
        dry (bool): If true, no mutating operations will occur.
    """
    # Initialize Notion client.
    notion = Client(auth=notion_token, client=RetryingClient())

    # Gather issues first so that we can populate select properties accordingly.
    logger.info("Getting GitHub issues...")
    issues = get_all_issues(repositories, sync_status)
    logger.info("Issues retrieved successfully")

    if strip_orgname:
        repo_field_values = list(map(lambda repo: repo.split("/")[1], repositories))
    else:
        repo_field_values = repositories

    labels = extract_labels(issues)
    properties = [
        p.select("Repository", repo_field_values),
        p.rich_text("Assignee"),
        p.title("Title"),
        p.link("Link"),
        p.rich_text("Unique ID"),
        p.date("Opened"),
        p.date("Closed"),
        p.relation("Milestones", milestones_id, True),
        p.multi_select("Labels", labels),
    ]

    # Extract the milestones for relational purposes.
    milestones_db = NotionDatabase(milestones_id, notion, dry=dry)
    milestones = extract_milestones(milestones_db.get_all_pages())
    logger.info(f"Found {len(milestones.keys())} milestones ")

    # Create database object.
    notion_db = NotionDatabase(tasks_id, notion, properties, dry=dry)

    # Set properties on database.
    logger.info("Update tasks database properties")
    notion_db.update_props(delete=True)

    # Gather pages.
    logger.info("Get pages")
    pages = notion_db.get_all_pages()

    # Start sync.
    logger.info("Starting sync")
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    # Create dict of {issue_id: notion_page} for issues in the notion db.
    pages_issues = {}
    for page in pages:
        key = getnestedattr(lambda: page["properties"]["Unique ID"]["rich_text"][0]["plain_text"], None)
        if key:
            pages_issues[key] = page
        else:
            logger.error(f"Page {page['id']} has no Unique ID! Deleting it...")
            notion_db.delete_page(p["id"])

    added = 0
    updated = 0
    issue_count = 0
    for repo in issues.values():
        issue_count += len(repo)
        for issue in repo:
            if issue.id in pages_issues.keys():
                page = pages_issues[issue.id]
                page_status = getnestedattr(lambda: page["properties"]["Status"]["status"]["name"], None)
                if dry:
                    logger.info(f"Updating page for {issue.id}")

                if notion_db.update_page(
                    page,
                    map_issue_to_page(issue, milestones, page_status, milestone_prefix),
                ):
                    updated += 1
            else:
                if dry:
                    logger.info(f"Creating page for {issue.id}")

                if notion_db.create_page(map_issue_to_page(issue, milestones, milestone_prefix=milestone_prefix)):
                    added += 1

    page_count = len(pages)
    notion_db.description = f"Last Sync: {timestamp} UTC"
    logger.info(
        f"Synced {issue_count} issues in query, {page_count} were in Notion: Added {added} and updated {updated}."
    )


def map_issue_to_page(issue, milestones, page_status=None, milestone_prefix="M:"):
    """Map a single issue's data into the datadict format for the NotionDatabase class."""
    notion_data = {
        "Assignee": " ".join(a.login for a in issue.assignees.nodes) if issue.assignees.nodes else "",
        "Link": issue.url,
        "Title": issue.title,
        "Repository": issue.repository.name,
        "Unique ID": issue.id,
        "Opened": issue.created_at,
        "Closed": issue.closed_at,
        "Labels": [label.name for label in issue.labels.nodes],
    }

    # Assign 'Done' to closed tickets
    if issue.state == "CLOSED":
        notion_data["Status"] = "Done"

    # Assign 'Not started' to re-opened tickets
    if page_status == "Done" and issue.state == "OPEN":
        notion_data["Status"] = "Not started"

    mlen = len(milestone_prefix)
    filtered_labels = [
        label[mlen:].strip()
        for label in notion_data["Labels"]
        if label.startswith(milestone_prefix) and label[mlen:].strip() in milestones
    ]
    notion_data["Milestones"] = [milestones[label] for label in filtered_labels]

    # for label in issue.get_labels():
    return notion_data


def extract_labels(issues):
    """Extract labels into a list with no duplicates."""
    labels = set()

    for repo in issues.values():
        for issue in repo:
            for label in issue.labels.nodes:
                labels.add(label.name)
    return labels


def extract_milestones(pages):
    """Convert pages from the Notion Milestones database into a dict of milestone_title:page_id."""
    milestones = {}
    for page in pages:
        for prop in page["properties"].values():
            if prop["id"] == "title":
                title = prop["title"][0]["plain_text"].strip()
                if title:
                    milestones[title] = page["id"]
    return milestones


def get_issues_from_repo(orgname, reponame):
    """Get all issues from the orgname/reponame repository."""
    endpoint = HTTPEndpoint(
        "https://api.github.com/graphql",
        {"Authorization": f'Bearer {os.getenv("GITHUB_TOKEN")}'},
    )
    has_next_page = True
    cursor = None

    all_issues = []
    while has_next_page:
        op = Operation(schema.query_type)
        issues = op.repository(owner=orgname, name=reponame).issues(
            first=100,
            after=cursor,
            order_by={"field": "UPDATED_AT", "direction": "DESC"},
        )
        issues.nodes.updated_at()
        issues.nodes.created_at()
        issues.nodes.closed_at()
        issues.nodes.title()
        issues.nodes.state()
        issues.nodes.url()
        issues.nodes.id()
        issues.nodes.repository().name()
        issues.nodes.labels(first=100).nodes.name()
        issues.nodes.assignees(first=10).nodes.login()

        sprint_field = (
            issues.nodes.project_items(first=100, include_archived=False)
            .nodes.field_value_by_name(name="Sprint")
            .__as__(schema.ProjectV2ItemFieldIterationValue)
        )
        sprint_field.title()
        sprint_field.iteration_id()

        issues.page_info.__fields__(has_next_page=True)
        issues.page_info.__fields__(end_cursor=True)
        data = endpoint(op)

        # sgqlc magic to turn the response into an object rather than a dict
        repo = (op + data).repository
        all_issues.extend(repo.issues.nodes)

        has_next_page = repo.issues.page_info.has_next_page
        cursor = repo.issues.page_info.end_cursor

    return all_issues


def get_all_issues(repos: list[str], status: str = "all") -> Dict[str, Any]:
    """Get all issues from repo."""
    all_issues = {}
    for orgrepo in repos:
        orgname, repo = orgrepo.split("/")
        all_issues[orgrepo] = get_issues_from_repo(orgname, repo)
    return all_issues
