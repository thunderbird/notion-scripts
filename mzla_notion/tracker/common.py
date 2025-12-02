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
    assignees: set = field(default_factory=set)
    labels: set = field(default_factory=set)
    issue_type: str = None
    url: str
    review_url: str = ""
    notion_url: str = ""
    created_date: datetime.datetime = None
    closed_date: datetime.datetime = None
    start_date: datetime.date = None
    end_date: datetime.date = None
    sprint: Sprint = None
    sub_issues: list = field(default_factory=list)
    whiteboard: str = ""


class User:
    """A user representation that can be converted into different representations."""

    def __init__(self, user_map, notion_user=None, tracker_user=None):
        """Initialize a user by passing either notion or tracker user."""
        self.user_map = user_map
        self.notion_user = notion_user or self.user_map.tracker_to_notion(tracker_user)
        self.tracker_user = tracker_user or self.user_map.notion_to_tracker(notion_user)

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
        "notion_tasks_status": "Status",
        "notion_tasks_milestone_relation": "Project",
        "notion_tasks_sprint_relation": "Sprint",
        "notion_tasks_text_assignee": "",  # Default is disabled
        "notion_tasks_review_url": "",  # Default is disabled
        "notion_tasks_labels": "",  # Default is disabled
        "notion_tasks_whiteboard": "",  # Default is disabled
        "notion_tasks_repository": "",  # Default is disabled
        "notion_tasks_openclose": "",  # Default is disabled
        "notion_milestones_team": "",  # Default is disabled
        "notion_milestones_title": "Project",
        "notion_milestones_assignee": "Owner",
        "notion_milestones_priority": "Priority",
        "notion_milestones_status": "Status",
        "notion_milestones_dates": "Dates",
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

    def new_user(self, notion_user=None, tracker_user=None):
        """Create a new user instance based on notion user or tracker user."""
        return User(self.user_map, notion_user=notion_user, tracker_user=tracker_user)

    def notion_tasks_title(self, tasks_notion_prefix, issue):
        """Determine the title for notion tasks."""
        return tasks_notion_prefix + issue.title

    async def collect_additional_tasks(self, collected_tasks):
        """Add additional tasks to the collected tasks for sync."""
        pass

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
