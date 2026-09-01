import datetime

from dataclasses import dataclass, field, replace

from ..util import notion_url_equal


@dataclass
class Sprint:
    """Represents a sprint."""

    id: str
    name: str
    status: str
    start_date: datetime.date
    end_date: datetime.date


@dataclass
class IssueRef:
    """An issue reference."""

    repo: str
    id: str
    parents: list["IssueRef"] = field(default_factory=list)
    notion_url: str = ""


@dataclass(kw_only=True)
class Issue(IssueRef):
    """Represents an issue."""

    title: str
    description: str
    state: str
    priority: str
    estimate: str = None
    assignees: set = field(default_factory=set)
    labels: set = field(default_factory=set)
    issue_type: str = None
    url: str
    review_url: str = ""
    reviewers: set = field(default_factory=set)
    creator: "User" = None
    notion_url: str = ""
    created_date: datetime.datetime = None
    updated_date: datetime.datetime = None
    closed_date: datetime.datetime = None
    start_date: datetime.date = None
    end_date: datetime.date = None
    sprint: Sprint = None
    sub_issues: list = field(default_factory=list)
    whiteboard: str = ""
    target_milestone: str = ""
    requested_ref: IssueRef = None
    # True when the issue is nested deeper than a single sub-issue layer (a sub-issue of a task).
    # The sync only supports a Milestone -> Task hierarchy, so these are ignored.
    deeply_nested: bool = False


class User:
    """A user representation that can be converted into different representations."""

    def __init__(self, user_map, notion_user=None, tracker_user=None):
        """Initialize a user by passing either notion or tracker user."""
        self.user_map = user_map
        self.notion_user = notion_user or self.user_map.tracker_to_notion(tracker_user)
        self.tracker_user = tracker_user or self.user_map.notion_to_tracker(notion_user)
        self.team_ids = self.user_map.notion_to_teams(self.notion_user)

    @property
    def tracker_mention(self):
        """The way the user is mentioned in the issue tracker."""
        return self.user_map.tracker_mention(self.tracker_user)

    def __eq__(self, other):
        """Check if two users are equal."""
        if type(other) is type(self):
            if self.tracker_user is None or other.tracker_user is None:
                return self.tracker_user == other.tracker_user
            else:
                return self.tracker_user.casefold() == other.tracker_user.casefold()

        return False

    def __repr__(self):
        """Representation of a user."""
        return f"{self.__class__.__name__}(tracker={self.tracker_user},notion={self.notion_user})"

    def __hash__(self):
        """Hash of the user, which is just the tracker_user."""
        return hash(self.tracker_user.casefold() if self.tracker_user is not None else None)


class IssueTracker:
    """Base class for issue trackers."""

    # In order to make Notion field names configurable we have a mapping from a static key to the
    # Notion field name. These defaults will be overwritten by the field config
    DEFAULT_PROPERTY_NAMES = {
        "notion_tasks_title": "Task name",
        "notion_tasks_assignee": "Owner",
        "notion_tasks_dates": "Dates",
        "notion_tasks_planned_dates": "",  # Default is disabled
        "notion_tasks_team": "",  # Default is disabled
        "notion_tasks_priority": "Priority",
        "notion_tasks_estimate": "",  # Default is disabled
        "notion_tasks_status": "Status",
        "notion_tasks_milestone_relation": "Project",
        "notion_tasks_sprint_relation": "Sprint",
        "notion_tasks_text_assignee": "",  # Default is disabled
        "notion_tasks_review_url": "",  # Default is disabled
        "notion_tasks_reviewers": "",  # Default is disabled
        "notion_tasks_labels": "",  # Default is disabled
        "notion_tasks_whiteboard": "",  # Default is disabled
        "notion_tasks_target_milestone": "",  # Default is disabled
        "notion_tasks_repository": "",  # Default is disabled
        "notion_tasks_openclose": "",  # Default is disabled
        "notion_milestones_team": "",  # Default is disabled
        "notion_milestones_epic_relation": "",  # Default is disabled
        "notion_milestones_title": "Project",
        "notion_milestones_assignee": "Owner",
        "notion_milestones_priority": "Priority",
        "notion_milestones_status": "Status",
        "notion_milestones_dates": "Dates",
        "notion_epics_team": "",  # Default is disabled
        "notion_epics_title": "Project",
        "notion_epics_assignee": "Owner",
        "notion_epics_priority": "Priority",
        "notion_epics_status": "Status",
        "notion_epics_dates": "Dates",
        "notion_issue_field": "Issue Link",
        "notion_sprint_title": "Sprint name",
        "notion_sprint_status": "Sprint status",
        "notion_sprint_dates": "Dates",
        # Some default states and values
        "notion_tasks_priority_values": ["P1", "P2", "P3", "P4", "P5"],
        "notion_default_open_state": "Backlog",
        "notion_closed_states": ["Done", "Canceled"],
        "notion_canceled_state": "Canceled",
        "notion_inprogress_state": "In progress",
    }

    @classmethod
    async def create(cls, **kwargs):
        """Instanciate the tracker and run async init."""
        self = cls(**kwargs)
        await self._async_init()
        return self

    def __init__(self, property_names={}, dry=False):
        """Initialize the issue tracker."""
        self.dry = dry
        self.property_names = {**self.DEFAULT_PROPERTY_NAMES, **property_names}

    async def _async_init(self):
        pass

    def format_issueref_short(self, ref):
        """Formats an issue ref to a very short string, suitable for Files & Media properties."""
        return f"{ref.repo}/{ref.id}"

    def format_patchref_short(self, ref):
        """Formats an patch URL to a very short string, suitable for Files & Media properties."""
        return ref

    def new_user(self, notion_user=None, tracker_user=None):
        """Create a new user instance based on notion user or tracker user."""
        return User(self.user_map, notion_user=notion_user, tracker_user=tracker_user)

    def notion_tasks_title(self, tasks_notion_prefix, issue):
        """Determine the title for notion tasks."""
        return tasks_notion_prefix + issue.title

    def is_task_issue(self, issue, *, milestones_issue_type=None, epics_issue_type=None):
        """Return whether an issue should be synchronized as a task."""
        if milestones_issue_type and issue.issue_type == milestones_issue_type:
            return False
        if epics_issue_type and issue.issue_type == epics_issue_type:
            return False

        # Generic trackers do not expose parent issue type in the common model. Preserve the
        # historical fallback for trackers that only model task-ness as "has a parent".
        return bool(issue.parents)

    async def collect_tracker_milestones(self, milestones_issue_type, sub_issues=False):
        """Collect all milestone issues on the tracker."""
        if False:
            yield "hack"

    async def collect_tracker_epics(self, epics_issue_type, sub_issues=False):
        """Collect all epic issues on the tracker."""
        if False:
            yield "hack"

    async def collect_additional_tasks(self, collected_tasks):
        """Add additional tasks to the collected tasks for sync."""
        pass

    async def update_milestone_issue(self, old_issue, new_issue):
        """Update a milestone issue on the tracker."""
        raise NotImplementedError

    async def update_task_issue(self, old_issue, new_issue):
        """Update a task issue on the tracker.

        By default this reuses milestone update behavior. Trackers may override this to avoid
        milestone-specific side effects.
        """
        await self.update_milestone_issue(old_issue, new_issue)

    async def create_task_issue_from_notion(
        self, parent_issue, title, description="", assignees=None, labels=None, estimate=None
    ):
        """Create a task issue on the tracker from Notion data."""
        raise NotImplementedError

    def should_update_task_issue(self, old_issue, new_issue):
        """Return whether task update should be sent to tracker."""
        if notion_url_equal(old_issue.notion_url, new_issue.notion_url):
            old_issue = replace(old_issue, notion_url=new_issue.notion_url)
        return old_issue != new_issue

    def should_update_milestone_issue(self, old_issue, new_issue):
        """Return whether milestone update should be sent to tracker."""
        if notion_url_equal(old_issue.notion_url, new_issue.notion_url):
            old_issue = replace(old_issue, notion_url=new_issue.notion_url)
        return old_issue != new_issue

    def is_repo_allowed(self, repo):
        """If the repository is allowed as per repository setup."""
        return True

    def get_all_repositories(self):
        """Get a list of all associated repositories."""
        return []

    async def get_sprints(self):
        """Get the sprints associated with this tracker."""
        return []

    async def get_issue(self, issueref):
        """Get a single issue by issue ref."""
        retissue = None
        async for issue in self.get_issues_by_number([issueref]):
            retissue = issue

        return retissue

    async def get_all_issues(self):
        """Get all issues in all asscoiated repositories."""
        if False:
            yield "hack"

    async def get_recent_issues_by_repo(self, since, sub_issues=False):
        """Get recently updated issues grouped by repository.

        The return value is a mapping:
            { "<org>/<repo>" or "<bugzilla-host>": { "<id>": Issue } }
        """
        repos = {}
        try:
            iterator = self.get_all_issues(sub_issues=sub_issues)
        except TypeError:
            iterator = self.get_all_issues()

        async for issue in iterator:
            if issue.updated_date and since and issue.updated_date < since:
                continue
            repos.setdefault(issue.repo, {})[issue.id] = issue

        return repos

    async def get_recent_issues_by_parent_refs(self, since, parent_refs, sub_issues=False):
        """Get recently updated issues that have one of the given parents."""
        child_refs_by_repo = {}
        parent_refs_by_repo = {}
        for ref in parent_refs:
            parent_refs_by_repo.setdefault(ref.repo, []).append(ref)

        for refs in parent_refs_by_repo.values():
            async for issue in self.get_issues_by_number(refs, sub_issues=True):
                for child in issue.sub_issues:
                    child_refs_by_repo.setdefault(child.repo, {})[child.id] = child

        repos = {}
        for repo, child_refs in child_refs_by_repo.items():
            async for issue in self.get_issues_by_number(list(child_refs.values()), sub_issues=sub_issues):
                if issue.updated_date and since and issue.updated_date < since:
                    continue
                repos.setdefault(repo, {})[issue.id] = issue

        return repos


class UserMap:
    """A map between different types of user names."""

    def __init__(self, trk_to_notion, notion_to_teams=None):
        """Initialize.

        Args:
            trk_to_notion (dict[str, str]): Map from tracker username to notion guid
            notion_to_teams (dict[str, list[str]]): Map from Notion user id to Notion team page ids.
        """
        self._trk_to_notion = trk_to_notion
        self._notion_to_trk = {notion: trk for trk, notion in trk_to_notion.items()}
        self._notion_to_teams = {}
        for notion_id, team_ids in (notion_to_teams or {}).items():
            if not notion_id:
                continue
            normalized_notion_id = notion_id.replace("-", "")
            self._notion_to_teams[normalized_notion_id] = [team_id.replace("-", "") for team_id in team_ids if team_id]

    def map(self, func, inputs):
        """Map helper to apply one of the other functions if there is a value."""
        return [result for value in inputs if (result := func(value))]

    def tracker_to_notion(self, login):
        """Convert a tracker username to a notion id."""
        return self._trk_to_notion.get(login)

    def notion_to_tracker(self, notion_id):
        """Convert a notion id to a tracker username."""
        return self._notion_to_trk.get(notion_id)

    def notion_to_teams(self, notion_id):
        """Get Notion team ids associated with a Notion user id."""
        if not notion_id:
            return []
        return self._notion_to_teams.get(notion_id.replace("-", ""), [])

    def tracker_mention(self, tracker_user):
        """Convert a tracker username to a mention in issue text."""
        raise NotImplementedError
