import datetime

from dataclasses import dataclass, field


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


@dataclass(kw_only=True)
class Issue(IssueRef):
    """Represents an issue."""

    title: str
    description: str
    state: str
    priority: str
    assignees: list = field(default_factory=list)
    labels: list = field(default_factory=list)
    url: str
    review_url: str = ""
    notion_url: str = ""
    start_date: datetime.date = None
    end_date: datetime.date = None
    sprint: Sprint = None
    sub_issues: list = field(default_factory=list)


class User:
    """A user representation that can be converted into different representations."""

    def __init__(self, user_map, notion_user=None, tracker_user=None):
        """Initialize a user by passing either notion or tracker user."""
        self.user_map = user_map
        self._notion_user = notion_user
        self._tracker_user = tracker_user

    @property
    def tracker_user(self):
        """The issue tracker id/name for this user."""
        return self._tracker_user or self.user_map.notion_to_tracker(self._notion_user)

    @property
    def notion_user(self):
        """The notion user id for this user."""
        return self._notion_user or self.user_map.tracker_to_notion(self._tracker_user)

    @property
    def tracker_mention(self):
        """The way the user is mentioned in the issue tracker."""
        return self.user_map.tracker_mention(self.tracker_user)

    def __eq__(self, other):
        """Check if two users are equal."""
        if type(other) is type(self):
            return self.tracker_user == other.tracker_user
        return False

    def __repr__(self):
        """Representation of a user."""
        return f"{self.__class__.__name__}(tracker={self._tracker_user},notion={self._notion_user})"


class IssueTracker:
    """Base class for issue trackers."""

    # In order to make Notion field names configurable we have a mapping from a static key to the
    # Notion field name. These defaults will be overwritten by the field config
    DEFAULT_PROPERTY_NAMES = {
        "notion_tasks_title": "Task name",
        "notion_tasks_assignee": "Owner",
        "notion_tasks_dates": "Dates",
        "notion_tasks_priority": "Priority",
        "notion_tasks_milestone_relation": "Project",
        "notion_tasks_sprint_relation": "Sprint",
        "notion_tasks_text_assignee": "",  # Default is disabled
        "notion_tasks_review_url": "",  # Default is disabled
        "notion_milestones_title": "Project",
        "notion_milestones_assignee": "Owner",
        "notion_milestones_priority": "Priority",
        "notion_milestones_status": "Status",
        "notion_milestones_dates": "Dates",
        "notion_issue_field": "Issue Link",
        "notion_sprint_tracker_id": "Bug Tracker External ID",
        "notion_sprint_title": "Sprint name",
        "notion_sprint_status": "Sprint status",
        "notion_sprint_dates": "Dates",
        # Some default states and values
        "notion_tasks_priority_values": ["P1", "P2", "P3"],
        "notion_default_open_state": "Backlog",
        "notion_closed_states": ["Done", "Canceled"],
    }

    def __init__(self, property_names={}, dry=False):
        """Initialize the issue tracker."""
        self.dry = dry
        self.property_names = {**self.DEFAULT_PROPERTY_NAMES, **property_names}

    def new_user(self, notion_user=None, tracker_user=None):
        """Create a new user instance based on notion user or tracker user."""
        return User(self.user_map, notion_user=notion_user, tracker_user=tracker_user)

    def notion_tasks_title(self, tasks_notion_prefix, issue):
        """Determine the title for notion tasks."""
        return tasks_notion_prefix + issue.title

    def collect_additional_tasks(self, collected_tasks):
        """Add additional tasks to the collected tasks for sync."""
        pass

    def is_repo_allowed(self, repo):
        """If the repository is allowed as per repository setup."""
        return True

    def get_sprints(self):
        """Get the sprints associated with this tracker."""
        return []

    def get_issue(self, issueref):
        """Get a single issue by issue ref."""
        issues = self.get_issues_by_number([issueref])
        return issues[issueref.id]


class UserMap:
    """A map between different types of user names."""

    def __init__(self, trk_to_notion):
        """Initialize.

        Args:
            trk_to_notion (dict[str, str]): Map from tracker username to notion guid
        """
        self._trk_to_notion = trk_to_notion
        self._notion_to_trk = {notion: trk for trk, notion in trk_to_notion.items()}

    def map(self, func, inputs):
        """Map helper to apply one of the other functions if there is a value."""
        return [result for value in inputs if (result := func(value))]

    def tracker_to_notion(self, login):
        """Convert a tracker username to a notion id."""
        return self._trk_to_notion.get(login)

    def notion_to_tracker(self, notion_id):
        """Convert a notion id to a tracker username."""
        return self._notion_to_trk.get(notion_id)

    def tracker_mention(self, tracker_user):
        """Convert a tracker username to a mention in issue text."""
        raise NotImplementedError
