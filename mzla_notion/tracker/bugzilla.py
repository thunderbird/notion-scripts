import re
import urllib.parse
import httpx
import base64
import logging
import datetime

from functools import cache

from ..util import getnestedattr, AsyncRetryingClient, RetryingClient

from .common import UserMap, IssueRef, Issue, User, IssueTracker

logger = logging.getLogger("project_sync")


class BugzillaUserMap(UserMap):
    """This is a map between different types of user ids to avoid mental gymnastics."""

    def __init__(self, client, trk_to_notion):
        """Initialize."""
        super().__init__(trk_to_notion)
        self._client = client

    @cache
    def tracker_mention(self, username):
        """Convert a tracker username to a mention in issue text."""
        response = self._client.get("/user", params={"names": username})
        user = response.json()
        return user["real_name"] or user["name"]


class Bugzilla(IssueTracker):
    """Bugzilla issue tracker connector."""

    BUGZILLA_SHOW_RE = re.compile(r"https://([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)/show_bug\.cgi\?id=[0-9]+")

    DEFAULT_PROPERTY_NAMES = {
        **IssueTracker.DEFAULT_PROPERTY_NAMES,
        "notion_tasks_priority_values": ["P1", "P2", "P3", "P4", "P5"],
        "notion_tasks_review_url": "Review URL",
        "notion_default_open_state": "NEW",
        "notion_tasks_dates": None,  # We don't support dates
        "notion_default_closed_states": ["RESOLVED"],
        "bugzilla_allowed_products": None,  # Default to all is allowed
    }

    name = "Bugzilla"

    def __init__(self, base_url, token=None, user_map=None, **kwargs):
        """Initialize the Bugzilla issue tracker."""
        super().__init__(**kwargs)

        res = urllib.parse.urlparse(base_url)

        self.base_url = base_url
        self.repo_name = res.netloc

        self.client = AsyncRetryingClient(
            base_url=f"{base_url}/rest",
            limits=httpx.Limits(keepalive_expiry=30.0),
            http2=True,
            params={"api_key": token},
            timeout=60.0,
            autoraise=True,
        )

        self.sync_client = RetryingClient(
            base_url=f"{base_url}/rest",
            limits=httpx.Limits(keepalive_expiry=30.0),
            http2=True,
            params={"api_key": token},
            timeout=60.0,
            autoraise=True,
        )

        self.user_map = BugzillaUserMap(self.sync_client, user_map)

    def parse_issueref(self, ref):
        """Parse an issue identifier (e.g. bugzilla url) to an IssueRef."""
        res = urllib.parse.urlparse(ref)
        res_qs = urllib.parse.parse_qs(res.query)

        if res.scheme + "://" + res.netloc == self.base_url and res.path == "/show_bug.cgi" and "id" in res_qs:
            return IssueRef(repo=res.netloc, id=res_qs["id"][0])
        else:
            return None

    def is_repo_allowed(self, reporef):
        """If the repository is allowed as per repository setup."""
        return reporef == self.repo_name

    def _is_allowed_product(self, bug):
        return (
            self.property_names["bugzilla_allowed_products"] is None
            or bug["product"] in self.property_names["bugzilla_allowed_products"]
        )

    def notion_tasks_title(self, tasks_notion_prefix, issue):
        """The augmented notion tasks title (includes bug reference)."""
        return f"{tasks_notion_prefix}{issue.title} - bug {issue.id}"

    async def update_milestone_issue(self, old_issue, new_issue):
        """Update an issue on the tracker."""

        def _set_if(data, prop, bzname):
            if getattr(old_issue, prop) != getattr(new_issue, prop):
                data[bzname] = getattr(new_issue, prop)

        data = {}

        _set_if(data, "title", "summary")
        _set_if(data, "priority", "priority")

        if new_issue.description is not None:
            _set_if(data, "description", "cf_user_story")

        # Status
        _set_if(data, "state", "status")
        if old_issue.state != "RESOLVED" and new_issue.state == "RESOLVED":
            data["resolution"] = "FIXED"
        elif old_issue.state == "RESOLVED" and new_issue.state != "RESOLVED":
            data["resolution"] = ""

        # Assignee
        old_assignee = next(iter(old_issue.assignees or []), None)
        new_assignee = next(iter(new_issue.assignees or []), None)
        old_assignee_is_notion_user = old_assignee and old_assignee.notion_user is not None

        if old_assignee != new_assignee:
            # This condition ensures that if a community user is assigned to an issue, they are not
            # removed from it.
            if not old_assignee or old_assignee_is_notion_user:
                data["assigned_to"] = new_assignee.tracker_user if new_assignee else None

        # Notion URL
        if old_issue.notion_url != new_issue.notion_url and new_issue.notion_url:
            data["see_also"] = {}
            if old_issue.notion_url:
                data["see_also"]["remove"] = [old_issue.notion_url]
            if new_issue.notion_url:
                data["see_also"]["add"] = [new_issue.notion_url]

        # Fields we won't handle here:
        # - start_date / end_date: We don't have an equivalent
        # - sub_issues: These will be managed on bugzilla

        if data and not self.dry:
            await self.client.put(f"/bug/{new_issue.id}", json=data)

    async def get_issues_by_number(self, bugrefs, sub_issues=False):
        """Retrieve issues by their id number."""
        res = {}
        bugids = map(lambda bug: urllib.parse.quote(str(bug.id), safe=""), bugrefs)
        fields = "id,summary,status,product,cf_user_story,assigned_to,priority,depends_on,blocks,attachments,comments,see_also,creation_time,cf_last_resolved"

        response = await self.client.get("/bug", params={"id": ",".join(bugids), "include_fields": fields})
        response_json = response.json()

        for bug in response_json["bugs"]:
            assignee = bug["assigned_to"] if bug["assigned_to"] != "nobody@mozilla.org" else None
            parents = [IssueRef(repo=self.repo_name, id=str(parent_id)) for parent_id in bug["blocks"]]

            closed_date = None
            if bug["cf_last_resolved"] and bug["status"] == "RESOLVED":
                closed_date = datetime.datetime.fromisoformat(bug["cf_last_resolved"])

            issue = Issue(
                id=str(bug["id"]),
                repo=self.repo_name,
                url=f"{self.base_url}/show_bug.cgi?id={bug['id']}",
                title=bug["summary"],
                state=bug["status"],
                labels=set(),
                description=bug["cf_user_story"] or getnestedattr(lambda: bug["comments"][0]["text"], ""),
                assignees={User(self.user_map, tracker_user=assignee)} if assignee else set(),
                priority=bug["priority"] if bug["priority"] != "--" else None,
                parents=parents,
                created_date=datetime.datetime.fromisoformat(bug["creation_time"]),
                closed_date=closed_date,
            )

            phab = next(
                filter(
                    lambda att: att["is_obsolete"] == 0 and att.get("content_type") == "text/x-phabricator-request",
                    bug["attachments"],
                ),
                None,
            )
            if phab:
                if issue.state in ("ASSIGNED", "REOPENED"):
                    issue.state = "IN REVIEW"  # TODO hack
                issue.review_url = base64.b64decode(phab["data"]).decode("utf-8")

            for url in bug["see_also"]:
                if url.startswith("https://www.notion.so/"):
                    issue.notion_url = url
                    break

            issue.sub_issues = [
                IssueRef(repo=self.repo_name, id=str(sub_issue_id), parents=[issue])
                for sub_issue_id in bug["depends_on"]
                if self._is_allowed_product(bug)
            ]

            res[issue.id] = issue

        return res
