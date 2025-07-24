import datetime
import os
import sgqlc.types
import itertools
import logging

from collections import defaultdict
from dataclasses import dataclass
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation, GraphQLErrors

from ..github_schema import schema
from ..util import getnestedattr

from .common import UserMap, Sprint, IssueRef, Issue, User, IssueTracker

logger = logging.getLogger("project_sync")

GITHUB_PROJECT_TASKS_FIELDS = ["Status", "Priority", "Sprint"]
GITHUB_PROJECT_MILESTONE_FIELDS = [
    "Status",
    "Priority",
    "Start Date",
    "Target Date",
    "Link",
]


class GitHubUserMap(UserMap):
    """User map for GitHub repositories."""

    def __init__(self, endpoint, trk_to_notion):
        """Initialize."""
        super().__init__(trk_to_notion)
        self._endpoint = endpoint
        self._trk_to_dbid = self._get_userid_for_user_logins(trk_to_notion.keys())
        self._dbid_to_trk = {dbid: trk for trk, dbid in self._trk_to_dbid.items()}

    def tracker_mention(self, tracker_username):
        """Convert a tracker username to a mention in issue text."""
        return "@" + tracker_username

    def trk_to_dbid(self, login):
        """Convert a GitHub username to its database id."""
        return self._trk_to_dbid.get(login)

    def dbid_to_trk(self, dbid):
        """Convert a database id to a github login."""
        return self._dbid_to_trk.get(dbid)

    def notion_to_dbid(self, notion_id):
        """Convert a notion id directly to a GitHub database id."""
        return self._trk_to_dbid.get(self._notion_to_trk.get(notion_id))

    def dbid_to_notion(self, dbid):
        """Convert a GitHub database id directly to a notion id."""
        return self._trk_to_notion.get(self._dbid_to_trk.get(dbid))

    def _get_userid_for_user_logins(self, user_logins):
        if not len(user_logins):
            return {}

        op = Operation(schema.query_type)

        for login in user_logins:
            usernode = op.user(__alias__=f"user_{login}", login=login)
            usernode.id()
            usernode.database_id()

        data = self._endpoint(op)
        return {
            login: dbid for login in user_logins if (dbid := data.get("data", {}).get(f"user_{login}", {}).get("id"))
        }


class GitHubUser(User):
    """GitHub User, with additional database id member."""

    def __init__(self, dbid_user=None, **kwargs):
        """Initialize a GitHubUser."""
        super().__init__(**kwargs)
        self.dbid_user = dbid_user or self.user_map.trk_to_dbid(self.tracker_user)

    def __repr__(self):
        """Representation of a user."""
        return f"{self.__class__.__name__}(tracker={self.tracker_user},notion={self.notion_user},dbid={self.dbid_user})"


@dataclass
class GitHubIssue(Issue):
    """GitHub Issue, with additional GraphQL member."""

    gql: sgqlc.types.Type = None


class GitHub(IssueTracker):
    """GitHub issue tracker connection."""

    name = "GitHub"

    def __init__(self, token=None, repositories={}, user_map=None, **kwargs):
        """Initialize issue tracker."""
        super().__init__(**kwargs)

        self.endpoint = HTTPEndpoint(
            url="https://api.github.com/graphql", base_headers={"Authorization": f"Bearer {token}"}, timeout=120.0
        )

        self.user_map = GitHubUserMap(self.endpoint, user_map)
        self.label_cache = LabelCache(self.endpoint)

        self._init_repository_settings(repositories)

    def _init_repository_settings(self, repository_settings):
        self.allowed_repositories = set()
        self.github_tasks_projects = {}
        self.github_milestones_projects = {}
        self.all_tasks_projects = []
        self.all_milestones_projects = []

        if "repositories" in repository_settings:
            repository_settings = {"default": repository_settings}

        for settings in repository_settings.values():
            self.allowed_repositories.update(settings["repositories"])

            if tasks_project_id := settings.get("github_tasks_project_id"):
                tasks_project = GitHubProjectV2(self.endpoint, tasks_project_id, GITHUB_PROJECT_TASKS_FIELDS)
                self.all_tasks_projects.append(tasks_project)
                for repo in settings["repositories"]:
                    self.github_tasks_projects[repo] = tasks_project

            if milestones_project_id := settings.get("github_milestones_project_id"):
                milestones_project = GitHubProjectV2(
                    self.endpoint, milestones_project_id, GITHUB_PROJECT_MILESTONE_FIELDS
                )
                self.all_milestones_projects.append(milestones_project)
                for repo in settings["repositories"]:
                    self.github_milestones_projects[repo] = milestones_project

    def parse_issueref(self, ref):
        """Parse an issue identifier (e.g. github url) to an IssueRef."""
        parts = ref.split("/")
        if parts[2] == "github.com" and parts[5] == "issues":
            return IssueRef(repo=parts[3] + "/" + parts[4], id=parts[6])
        else:
            return None

    def new_user(self, notion_user=None, tracker_user=None):
        """Create a new user instance based on notion user or tracker user."""
        return GitHubUser(user_map=self.user_map, notion_user=notion_user, tracker_user=tracker_user)

    def is_repo_allowed(self, reporef):
        """If the repository is allowed as per repository setup."""
        return reporef in self.allowed_repositories

    def get_all_repositories(self):
        """Get a list of all associated repositories."""
        return list(self.allowed_repositories)

    def collect_additional_tasks(self, collected_tasks):
        """Add additional tasks to the collected tasks for sync."""
        # Collect issues from sprint board, there may be a few not associated with a milestone
        project_item_count = 0
        for project in self.all_tasks_projects:
            for issue_ref in project.get_issue_numbers():
                if self.is_repo_allowed(issue_ref.repo) and issue_ref.id not in collected_tasks[issue_ref.repo]:
                    collected_tasks[issue_ref.repo][issue_ref.id] = None
                    project_item_count += 1

        logger.info(f"Will sync {project_item_count} new sprint board tasks not associated with a milestone")

    def update_milestone_issue(self, old_issue, new_issue):
        """Update an issue on GitHub."""
        self._update_issue_basic(old_issue, new_issue)
        self._update_issue_assignees(old_issue, new_issue)
        self._update_issue_labels(old_issue, new_issue)
        self._update_issue_project(old_issue, new_issue)

    def _update_issue_basic(self, old_issue, new_issue):
        matches = True
        for prop in ["title", "state", "description"]:
            if getattr(new_issue, prop) != getattr(old_issue, prop):
                matches = False
                break

        if matches:
            return

        op = Operation(schema.mutation_type)
        closed_states = self.property_names["notion_closed_states"]
        issue_data = {
            "id": new_issue.gql.id,
            "state": "CLOSED" if new_issue.state in closed_states else "OPEN",
        }

        if new_issue.title != old_issue.title:
            issue_data["title"] = new_issue.title

        if new_issue.description != old_issue.description:
            issue_data["body"] = new_issue.description

        if not self.dry:
            op.update_issue(input=issue_data)
            self.endpoint(op)

    def _update_issue_assignees(self, old_issue, new_issue):
        db_assignees = self.user_map.map(lambda user: user.dbid_user, new_issue.assignees)

        # If we've assigned a community member to this milestone, keep them on the issue
        community_assignees = {assignee.dbid_user for assignee in old_issue.assignees if assignee.notion_user is None}

        # Check if assignees have not changed
        old_assignees = {assignee.dbid_user for assignee in old_issue.assignees}
        new_assignees = community_assignees.union(db_assignees)

        # Check who to add or remove
        remove = old_assignees - new_assignees
        add = new_assignees - old_assignees

        # Bail early if no operations needed
        if not remove and not add:
            return

        # Adjust attendees
        op = Operation(schema.mutation_type)

        if len(remove):
            op.remove_assignees_from_assignable(input={"assignable_id": old_issue.gql.id, "assignee_ids": list(remove)})

        if len(add):
            op.add_assignees_to_assignable(input={"assignable_id": old_issue.gql.id, "assignee_ids": list(add)})

        if not self.dry:
            self.endpoint(op)

    def _update_issue_labels(self, old_issue, new_issue):
        new_labels = new_issue.labels - old_issue.labels
        if not len(new_labels):
            return

        org, repo = old_issue.repo.split("/")
        labels = self.label_cache.get_labels(org, repo, new_labels)
        label_ids = [labelid for labelid in labels.values()]

        if not self.dry:
            op = Operation(schema.mutation_type)
            op.add_labels_to_labelable(input={"labelable_id": old_issue.gql.id, "label_ids": label_ids})
            self.endpoint(op)

    def _update_issue_project(self, old_issue, new_issue):
        if self.dry:
            return

        gh_project_item = self.github_milestones_projects[old_issue.repo].find_project_item(
            old_issue.gql, self.github_milestones_projects[old_issue.repo].database_id
        )

        default_open_state = self.property_names["notion_default_open_state"]

        old_state = getnestedattr(lambda: gh_project_item.status.name, default_open_state)
        old_start_date = getnestedattr(lambda: gh_project_item.start_date.date, None)
        old_end_date = getnestedattr(lambda: gh_project_item.target_date.date, None)
        old_priority = getnestedattr(lambda: gh_project_item.priority.name, None)

        if (
            not gh_project_item
            or old_state != new_issue.state
            or old_start_date != new_issue.start_date
            or old_end_date != new_issue.end_date
            or old_priority != new_issue.priority
        ):
            self.github_milestones_projects[new_issue.repo].update_project_for_issue(
                new_issue,
                {
                    "start_date": new_issue.start_date,
                    "target_date": new_issue.end_date,
                    "priority": new_issue.priority,
                    "status": new_issue.state,
                    "link": new_issue.notion_url,
                },
                add=True,
            )

    def _parse_issue(self, ref, ghissue, sub_issues=False):
        tasks_project_item = self.github_tasks_projects[ref.repo].find_project_item(
            ghissue, self.github_tasks_projects[ref.repo].database_id
        )

        milestones_project_item = self.github_milestones_projects[ref.repo].find_project_item(
            ghissue, self.github_milestones_projects[ref.repo].database_id
        )

        if tasks_project_item and milestones_project_item:
            raise Exception(f"Issue {ghissue.url} has both tasks and milestones project")

        gh_project_item = tasks_project_item or milestones_project_item
        default_open_state = self.property_names["notion_default_open_state"]
        closed_states = self.property_names["notion_closed_states"]

        project_state = getnestedattr(lambda: gh_project_item.status.name, default_open_state)
        issue_state = default_open_state if ghissue.state == "OPEN" else closed_states[0]

        issue = GitHubIssue(
            repo=ref.repo,
            id=ref.id,
            url=f"https://github.com/{ref.repo}/issues/{ref.id}",
            title=ghissue.title,
            description=ghissue.body,
            assignees={
                GitHubUser(user_map=self.user_map, tracker_user=a.login, dbid_user=a.id)
                for a in ghissue.assignees.nodes
            },
            state=project_state if gh_project_item else issue_state,
            start_date=getnestedattr(lambda: gh_project_item.start_date.date, None),
            end_date=getnestedattr(lambda: gh_project_item.target_date.date, None),
            priority=getnestedattr(lambda: gh_project_item.priority.name, None),
            notion_url=getnestedattr(lambda: gh_project_item.link.text, None),
            labels={label.name for label in ghissue.labels.nodes},
            gql=ghissue,
        )

        if ghissue.parent:
            issue.parents = [IssueRef(repo=ghissue.parent.repository.name_with_owner, id=str(ghissue.parent.number))]

        if sub_issues:
            issue.sub_issues = [
                IssueRef(id=str(subissue.number), repo=ref.repo, parents=[issue])
                for subissue in ghissue.sub_issues.nodes
            ]

        if gh_project_item and getattr(gh_project_item, "sprint", None):
            ghsprint = gh_project_item.sprint
            today = datetime.date.today()
            end_date = ghsprint.start_date + datetime.timedelta(days=ghsprint.duration - 1)
            if ghsprint.start_date > today:
                status = "Future"
            elif end_date < today:
                status = "Past"
            else:
                status = "Current"

            issue.sprint = Sprint(
                id=ghsprint.iteration_id,
                name=ghsprint.title,
                status=status,
                start_date=ghsprint.start_date,
                end_date=end_date,
            )
        return issue

    def get_issues_by_number(self, issues, sub_issues=False, chunk_size=50):
        """Get the indicated numbered issues."""
        res = {}

        if not len(issues):
            return res

        i = 0
        chunk_size = 100

        while i < len(issues):
            op = Operation(schema.query_type)
            org, repo = issues[0].repo.split("/")
            oprepo = op.repository(owner=org, name=repo)
            logger.debug(f"Get issues {i} through {i+chunk_size}")

            for ref in itertools.islice(issues, i, i + chunk_size):
                if ref.repo != issues[0].repo:
                    raise Exception("Can't yet query from different repositories")

                issue = oprepo.issue(__alias__=f"issue{ref.id}", number=int(ref.id))
                issue_field_ops(issue)

                if sub_issues:
                    # TODO run through this with a cursor
                    subissues = issue.sub_issues(first=100)
                    subissues.nodes.number()

            try:
                data = self.endpoint(op)
                datarepo = (op + data).repository

                for ref in itertools.islice(issues, i, i + chunk_size):
                    ghissue = getattr(datarepo, f"issue{ref.id}", None)
                    res[ref.id] = self._parse_issue(ref, ghissue, sub_issues)

                i += chunk_size
            except GraphQLErrors as e:
                if str(e) == "Timeout on validation of query" and chunk_size > 1:
                    chunk_size = chunk_size // 2
                    logger.info(f"Decreasing chunk size to {chunk_size} due to validation timeout")
                    continue
                raise e

        return res

    def get_sprints(self):
        """Retrieve the sprints from the issue tracker."""

        def process_iteration(ghsprint, status):
            end_date = ghsprint.start_date + datetime.timedelta(days=ghsprint.duration - 1)
            return Sprint(
                id=ghsprint.id,
                name=ghsprint.title,
                status=status,
                start_date=ghsprint.start_date,
                end_date=end_date,
            )

        sprints = []
        today = datetime.date.today()

        for project in self.all_tasks_projects:
            sprint_field = project.field("sprint")

            for sprint in sprint_field.configuration.iterations:
                sprints.append(process_iteration(sprint, "Future" if sprint.start_date > today else "Current"))

            for sprint in sprint_field.configuration.completed_iterations:
                sprints.append(process_iteration(sprint, "Past"))
        return sprints

    def get_all_labels(self):
        """Get the names of all labels in all associated repositories."""
        all_labels = set()

        for orgrepo in self.allowed_repositories:
            orgname, repo = orgrepo.split("/")
            all_labels.update(self.label_cache.get_all(orgname, repo).keys())

        return all_labels


class LabelCache:
    """A cache for retrieving the label ids from GitHub."""

    def __init__(self, endpoint):
        """Initialize the label cache with an endpoint."""
        self._cache = defaultdict(dict)
        self.endpoint = endpoint

    def get_all(self, org, repo):
        """Get all labels in the repository."""
        orgrepocache = self._cache[org + "/" + repo]

        has_next_page = True
        cursor = None

        while has_next_page:
            op = Operation(schema.query_type)
            repo = op.repository(owner=org, name=repo)
            labels = repo.labels(first=100, after=cursor)
            labels.nodes.name()
            labels.nodes.id()

            labels.page_info.__fields__(has_next_page=True)
            labels.page_info.__fields__(end_cursor=True)

            data = self.endpoint(op)
            datarepo = (op + data).repository

            for label in datarepo.labels.nodes:
                orgrepocache[label.name] = label

            has_next_page = datarepo.labels.page_info.has_next_page
            cursor = datarepo.labels.page_info.end_cursor

        return orgrepocache

    def get_labels(self, org, repo, labels):
        """Get the list of labels from the org/repo."""
        res = {}
        remaining = []

        orgrepocache = self._cache[org + "/" + repo]

        for label in labels:
            if label in orgrepocache:
                res[label] = orgrepocache[label]
            else:
                remaining.append(label)

        op = Operation(schema.query_type)
        repo = op.repository(owner=org, name=repo)

        for index, label in enumerate(remaining):
            labelnode = repo.label(__alias__=f"label_{index}", name=label)
            labelnode.id()

        data = self.endpoint(op)
        repo = (op + data).repository

        for index, label in enumerate(remaining):
            orgrepocache[label] = res[label] = getattr(repo, f"label_{index}").id

        return res


class GitHubProjectV2:
    """A container for GitHub's ProjectV2."""

    @staticmethod
    def list(org, repo):  # pragma: no cover
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

    def __init__(self, endpoint, database_id: str, field_names=[]):
        """Initialize the project container.

        Args:
            endpoint (HTTPEndpoint): The GraphQL endpoint to use
            database_id (str): The node id of the GiHub project
            field_names (list[str]): The names of the project fields to retrieve
        """
        self.database_id = database_id
        self.endpoint = endpoint
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
        """Return a list of IssueRefs for each issue in the project."""
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
                    all_issue_numbers.append(
                        IssueRef(repo=item.content.repository.name_with_owner, id=str(item.content.number))
                    )

            has_next_page = project_items.page_info.has_next_page
            cursor = project_items.page_info.end_cursor

        return all_issue_numbers

    def field(self, name, default=None):
        """Get a specific field from the project."""
        return getattr(self.get(), name, default)

    def update_project_for_issue(self, issue, properties, add=False):
        """Update ProjectV2 properties for the given issue.

        Args:
            issue (GitHubIssue): The GitHub Issue
            properties (dict): A dict with project fields to update
            add (bool): If true, the issue will be added to the project if not the case.
        """
        project = self.get()
        item = self.find_project_item(issue.gql, self.database_id)

        # Check if the issue needs to be added to the project
        if not item and add:
            op = Operation(schema.mutation_type)
            op.add_project_v2_item_by_id(input={"project_id": project.id, "content_id": issue.gql.id})
            data = self.endpoint(op)
            item = (op + data).add_project_v2_item_by_id.item

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

            if field.data_type == "TEXT":
                old_value = old_value.text if old_value else None
                input_item["value"] = {"text": value}
            elif field.data_type == "DATE":
                old_value = old_value.date.isoformat() if old_value else None
                input_item["value"] = {"date": value}
            elif field.data_type == "SINGLE_SELECT":
                old_value = old_value.name if old_value else None
                input_item["value"] = {"single_select_option_id": self.find_option_id(field, value)}
            elif field.data_type == "ITERATION":  # pragma: no cover
                old_value = old_value.iteration_id if old_value else None
                input_item["value"] = {"iteration_id": "TODO"}
                raise Exception("TODO")
            else:  # pragma: no cover
                raise Exception("Unknown type " + field.data_type)

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
    issue.repository.id()
    issue.repository.name_with_owner()
    issue.repository.name()
    issue.repository.is_private()
    issue.labels(first=100).nodes.name()

    assignees = issue.assignees(first=10)
    assignees.nodes.id()
    assignees.nodes.login()

    project_items = issue.project_items(first=10, include_archived=True).nodes
    project_items.id()

    project = project_items.project.__as__(schema.ProjectV2)
    project.id()
    project.number()
    project.title()
    project.__fields__("id", "title", "number")

    project_items.project.__as__(schema.Node).id()

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

    fieldvalue = project_items.field_value_by_name(name="Link", __alias__="link").__as__(
        schema.ProjectV2ItemFieldTextValue
    )
    fieldvalue.field.__as__(schema.ProjectV2FieldCommon).id()
    fieldvalue.text()

    fieldvalue = project_items.field_value_by_name(name="Sprint", __alias__="sprint").__as__(
        schema.ProjectV2ItemFieldIterationValue
    )
    fieldvalue.field.__as__(schema.ProjectV2FieldCommon).id()
    fieldvalue.iteration_id()
    fieldvalue.start_date()
    fieldvalue.title()
    fieldvalue.duration()
