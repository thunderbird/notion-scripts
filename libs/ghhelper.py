# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""GitHub related helper functions."""

import os
from typing import Any, Dict
from collections import defaultdict

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from .github_schema import schema


class LabelCache:
    """A cache to get the label id for a repo label."""

    def __init__(self):
        """Initialize the project container.

        Args:
            database_id (str): The node id of the GiHub project
            field_names (list[str]): The names of the project fields to retrieve
        """
        self.endpoint = HTTPEndpoint(
            "https://api.github.com/graphql",
            {"Authorization": f'Bearer {os.getenv("GITHUB_TOKEN")}'},
        )
        self.cache = defaultdict(dict)

    def get_id(self, orgrepo, label):
        """Get the id for the label in orgrepo."""
        orgcache = self.cache[orgrepo]
        if label not in orgcache:
            org, repo = orgrepo.split("/")
            orgcache[label] = get_label_id(org, repo, label)

        return orgcache[label]


class GitHubProjectV2:
    """A container for GitHub's ProjectV2."""

    @staticmethod
    def list(org, repo):
        """List all projects with theirs ids.

        Helpful to find out the node id from the number.

        Args:
            org (str): The organization/team name
            repo (str): The repository name this project is on
        """
        endpoint = HTTPEndpoint(
            "https://api.github.com/graphql",
            {"Authorization": f'Bearer {os.getenv("GITHUB_TOKEN")}'},
        )

        op = Operation(schema.query_type)

        repo = op.repository(owner=org, name=repo)
        projects = repo.projects_v2(first=100)

        projects.nodes.id()
        projects.nodes.url()
        projects.nodes.number()
        projects.nodes.title()

        data = endpoint(op)
        res_projects = (op + data).repository.projects_v2

        for project in res_projects.nodes:
            print(f"Project {project.url} ({project.title}) has id {project.id}")

    def __init__(self, database_id: str, field_names=[]):
        """Initialize the project container.

        Args:
            database_id (str): The node id of the GiHub project
            field_names (list[str]): The names of the project fields to retrieve
        """
        self.database_id = database_id
        self.endpoint = HTTPEndpoint(
            "https://api.github.com/graphql",
            {"Authorization": f'Bearer {os.getenv("GITHUB_TOKEN")}'},
        )
        self.field_names = field_names
        self.project = None

    def get(self, force=False):
        """Retrieve the cached project and its fields.

        Args:
            force (bool): If true, the project will be reloaded from GitHub
        """
        if force or not self.project:
            op = Operation(schema.query_type)
            project = op.node(id=self.database_id).__as__(schema.ProjectV2)
            project.number()
            project.title()
            project.id()

            for field in self.field_names:
                field_alias = field.lower().replace(" ", "_")
                gqlfield = project.field(name=field, __alias__=field_alias)
                gqlfield.__typename__()

                commonField = gqlfield.__as__(schema.ProjectV2Field)
                commonField.id()
                commonField.data_type()
                commonField.name()

                iterationField = gqlfield.__as__(schema.ProjectV2IterationField)
                iterationField.id()
                iterationField.name()
                iterationField.data_type()

                iterationFieldConfig = iterationField.configuration
                for iteration in [
                    iterationFieldConfig.completed_iterations,
                    iterationFieldConfig.iterations,
                ]:
                    iteration.id()
                    iteration.start_date()
                    iteration.title()
                    iteration.duration()

                optionField = gqlfield.__as__(schema.ProjectV2SingleSelectField)
                optionField.id()
                optionField.name()
                optionField.data_type()

                optionField.options.id()
                optionField.options.name()

            data = self.endpoint(op)
            self.project = (op + data).node

        return self.project

    def get_issue_numbers(self):
        """Return a GraphQL Issue with minimal info about the issue (number, repo name and owner)."""
        has_next_page = True
        cursor = None

        all_issue_numbers = []
        while has_next_page:
            op = Operation(schema.query_type)
            project = op.node(id=self.database_id).__as__(schema.ProjectV2)

            project_items = project.items(first=100, after=cursor)

            issue = project_items.nodes.content.__as__(schema.Issue)
            issue.number()
            issue.repository.name_with_owner()
            issue_field_ops(issue)

            project_items.page_info.__fields__(has_next_page=True)
            project_items.page_info.__fields__(end_cursor=True)
            data = self.endpoint(op)

            project_items = (op + data).node.items
            for item in project_items.nodes:
                if isinstance(item.content, schema.Issue):
                    all_issue_numbers.append(item.content)

            has_next_page = project_items.page_info.has_next_page
            cursor = project_items.page_info.end_cursor

        return all_issue_numbers

    def field(self, name, default=None):
        """Get a specific field from the project."""
        return getattr(self.get(), name, default)

    def update_project_for_issue(self, issue, properties, add=False):
        """Update ProjectV2 properties for the given issue.

        Args:
            issue (Issue): The GitHub Issue from GraphQL
            properties (dict): A dict with project fields to update
            add (bool): If true, the issue will be added to the project if not the case.
        """
        project = self.get()
        item = self.find_project_item(issue, self.database_id)

        # Check if the issue needs to be added to the project
        if not item and add:
            op = Operation(schema.mutation_type)
            op.add_project_v2_item_by_id(input={"project_id": project.id, "content_id": issue.id})
            self.endpoint(op)

            org, repo = issue.repository.name_with_owner.split("/")
            issue = get_issues_by_number(org, repo, [issue.number])[issue.number]

            item = self.find_project_item(issue, self.database_id)

        matches = True

        # Adjust each of the passed project fields. There are only a few different types
        op = Operation(schema.mutation_type)
        for key, value in properties.items():
            field = self.field(key)

            input_item = {
                "project_id": project.id,
                "item_id": item.id,
                "field_id": field.id,
            }

            old_value = getattr(item, key, None)

            if field.data_type == "DATE":
                old_value = old_value.date.isoformat() if old_value else None
                input_item["value"] = {"date": value}
            elif field.data_type == "SINGLE_SELECT":
                old_value = old_value.name if old_value else None
                input_item["value"] = {"single_select_option_id": self.find_option_id(field, value)}
            elif field.data_tupe == "ITERATION":
                old_value = old_value.iteration_id if old_value else None
                input_item["value"] = {"iteration_id": "TODO"}
                raise Exception("TODO")

            if old_value != value:
                matches = False

            op.update_project_v2_item_field_value(__alias__=f"update{key}", input=input_item)

        # Only actually update if there were changes
        if not matches:
            self.endpoint(op)

    def find_project_item(self, gh_issue, project_id):
        """Find the correct project item.

        An issue might be connected to multiple projects, find the project item associated with this
        project instance.

        Args:
            gh_issue (Issue): The GraphQL GitHub Issue to look on
            project_id (str): The node id of the project to look for

        Returns:
            ProjectV2Item: The project item associated with the Issue
        """
        for project_item in gh_issue.project_items.nodes:
            if project_item.project.id == project_id:
                return project_item

    def find_option_id(self, field, option_name):
        """Find the option id assoicated with the name for use in updates."""
        for option in field.options:
            if option.name == option_name:
                return option.id

        return None


class UserMap:
    """This is a map between different types of user ids to avoid mental gymnastics."""

    def __init__(self, gh_to_notion):
        """Initialize.

        Args:
            gh_to_notion (dict[str, str]): Map from github username to notion guid
        """
        self._gh_to_notion = gh_to_notion
        self._notion_to_gh = {notion: gh for gh, notion in gh_to_notion.items()}
        self._gh_to_dbid = self._get_userid_for_user_logins(gh_to_notion.keys())
        self._dbid_to_gh = {dbid: gh for gh, dbid in self._gh_to_dbid.items()}

    def map(self, func, inputs):
        """Map helper to apply one of the other functions if there is a value."""
        return [result for value in inputs if (result := func(value))]

    def gh_to_dbid(self, login):
        """Convert a GitHub username to its database id."""
        return self._gh_to_dbid.get(login)

    def dbid_to_gh(self, dbid):
        """Convert a database id to a github login."""
        return self._dbid_to_gh.get(dbid)

    def notion_to_dbid(self, notion_id):
        """Convert a notion id directly to a GitHub database id."""
        return self._gh_to_dbid.get(self._notion_to_gh.get(notion_id))

    def dbid_to_notion(self, dbid):
        """Convert a GitHub database id directly to a notion id."""
        return self._gh_to_notion.get(self._dbid.to_gh.get(dbid))

    def gh_to_notion(self, login):
        """Convert a GitHub username to a notion id."""
        return self._gh_to_notion.get(login)

    def notion_to_gh(self, notion_id):
        """Convert a notion id to a GitHub username."""
        return self._notion_to_gh.get(notion_id)

    def _get_userid_for_user_logins(self, user_logins):
        if not len(user_logins):
            return {}

        endpoint = HTTPEndpoint(
            "https://api.github.com/graphql",
            {"Authorization": f'Bearer {os.getenv("GITHUB_TOKEN")}'},
        )
        op = Operation(schema.query_type)

        user_nodes = {}

        for login in user_logins:
            user_nodes[login] = op.user(__alias__=f"user_{login}", login=login)
            user_nodes[login].id()
            user_nodes[login].database_id()

        data = endpoint(op)
        return {
            login: dbid for login in user_logins if (dbid := data.get("data", {}).get(f"user_{login}", {}).get("id"))
        }


def update_assignees(gh_issue, assignees):
    """Update the assignees on the GitHub issue by adding/removing the right ones.

    Use the UserMap to convert to GitHub user node ids.

    Args:
        gh_issue (Issue): The GitHub issue to update
        assignees (list[str]): List of assignee node ids (not usernames)
    """
    endpoint = HTTPEndpoint(
        "https://api.github.com/graphql",
        {"Authorization": f'Bearer {os.getenv("GITHUB_TOKEN")}'},
    )
    old_assignees = {assignee.id for assignee in gh_issue.assignees.nodes}
    new_assignees = set(assignees)
    if old_assignees == new_assignees:
        return

    remove = old_assignees.difference(new_assignees)
    add = new_assignees.difference(old_assignees)

    op = Operation(schema.mutation_type)

    if len(add):
        op.add_assignees_to_assignable(input={"assignable_id": gh_issue["id"], "assignee_ids": list(add)})

    if len(remove):
        op.remove_assignees_from_assignable(input={"assignable_id": gh_issue["id"], "assignee_ids": list(remove)})

    endpoint(op)


def update_issue(gh_issue, properties):
    """Update a GitHub issue with title, status and body."""
    endpoint = HTTPEndpoint(
        "https://api.github.com/graphql",
        {"Authorization": f'Bearer {os.getenv("GITHUB_TOKEN")}'},
    )
    op = Operation(schema.mutation_type)

    issue_data = {
        "id": gh_issue.id,
        "title": properties["title"],
        "state": "CLOSED" if properties["status"] == "Done" else "OPEN",
    }

    if properties.get("body", None) is not None:
        issue_data["body"] = properties["body"]

    matches = True
    for prop in ["title", "state", "body"]:
        if prop in issue_data and issue_data[prop] != getattr(gh_issue, prop):
            matches = False
            break

    if not matches:
        op.update_issue(input=issue_data)
        endpoint(op)


def get_label_id(org, repo, label):
    """Get the label id for the given label in org/repo."""
    endpoint = HTTPEndpoint(
        "https://api.github.com/graphql",
        {"Authorization": f'Bearer {os.getenv("GITHUB_TOKEN")}'},
    )

    op = Operation(schema.query_type)

    repo = op.repository(owner=org, name=repo)
    repo.label(name=label).id()

    data = endpoint(op)
    repo = (op + data).repository

    return getattr(repo.label, "id", None)


def add_label(gh_issue, label_id):
    """Add a label to a GitHub issue."""
    if not label_id:
        return

    endpoint = HTTPEndpoint(
        "https://api.github.com/graphql",
        {"Authorization": f'Bearer {os.getenv("GITHUB_TOKEN")}'},
    )
    op = Operation(schema.mutation_type)

    op.add_labels_to_labelable(input={"labelable_id": gh_issue.id, "label_ids": [label_id]})
    endpoint(op)


def issue_field_ops(issue):
    """Set the fields we need for project sync on the GraphQL operation."""
    issue.title()
    issue.number()
    issue.updated_at()
    issue.created_at()
    issue.closed_at()
    issue.title()
    issue.state()
    issue.url()
    issue.id()
    issue.body()
    issue.parent.number()
    issue.parent.repository.name_with_owner()
    issue.repository.name_with_owner()
    issue.repository.name()
    issue.labels(first=100).nodes.name()

    assignees = issue.assignees(first=10)
    assignees.nodes.id()
    assignees.nodes.login()

    project_items = issue.project_items(first=10, include_archived=False).nodes
    project_items.id()
    project_items.project.id()
    project_items.project.number()
    project_items.project.title()
    fieldvalue = project_items.field_value_by_name(name="Priority", __alias__="priority").__as__(
        schema.ProjectV2ItemFieldSingleSelectValue
    )
    fieldvalue.__as__(schema.ProjectV2ItemFieldValueCommon).field.__as__(schema.ProjectV2FieldCommon).id()
    fieldvalue.name()
    fieldvalue.option_id()

    fieldvalue = project_items.field_value_by_name(name="Start Date", __alias__="start_date").__as__(
        schema.ProjectV2ItemFieldDateValue
    )
    fieldvalue.__as__(schema.ProjectV2ItemFieldValueCommon).field.__as__(schema.ProjectV2FieldCommon).id()
    fieldvalue.date()

    fieldvalue = project_items.field_value_by_name(name="Target Date", __alias__="target_date").__as__(
        schema.ProjectV2ItemFieldDateValue
    )
    fieldvalue.__as__(schema.ProjectV2ItemFieldValueCommon).field.__as__(schema.ProjectV2FieldCommon).id()
    fieldvalue.date()

    fieldvalue = project_items.field_value_by_name(name="Status", __alias__="status").__as__(
        schema.ProjectV2ItemFieldSingleSelectValue
    )
    fieldvalue.field.__as__(schema.ProjectV2FieldCommon).id()
    fieldvalue.name()
    fieldvalue.option_id()

    fieldvalue = project_items.field_value_by_name(name="Sprint", __alias__="sprint").__as__(
        schema.ProjectV2ItemFieldIterationValue
    )
    fieldvalue.field.__as__(schema.ProjectV2FieldCommon).id()
    fieldvalue.iteration_id()
    fieldvalue.start_date()
    fieldvalue.title()
    fieldvalue.duration()


def get_issues_by_number(org, repo, issues, sub_issues=False):
    """Get the indicated numbered issues."""
    endpoint = HTTPEndpoint(
        "https://api.github.com/graphql",
        {"Authorization": f'Bearer {os.getenv("GITHUB_TOKEN")}'},
    )
    res = {}

    op = Operation(schema.query_type)
    repo = op.repository(owner=org, name=repo)

    for number in issues:
        issue = repo.issue(__alias__=f"issue{number}", number=number)
        issue_field_ops(issue)

        if sub_issues:
            # TODO run through this with a cursor
            subissues = issue.sub_issues(first=100)
            subissues.nodes.number()

    data = endpoint(op)
    repo = (op + data).repository

    for number in issues:
        ghissue = getattr(repo, f"issue{number}", None)
        res[number] = ghissue

    return res


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
