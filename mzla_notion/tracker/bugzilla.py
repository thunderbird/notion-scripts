import re
import urllib.parse
import httpx
import base64
import logging
import datetime
import asyncio
import json

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
        "bugzilla_map_state": {},
    }

    name = "Bugzilla"

    def __init__(self, base_url, token=None, user_map=None, **kwargs):
        """Initialize the Bugzilla issue tracker."""
        super().__init__(**kwargs)

        res = urllib.parse.urlparse(base_url)

        self.base_url = base_url
        self.repo_name = res.netloc
        self._hack_parent_cache = {}

        self.client = BugzillaAsyncRetryingClient(
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

        if old_issue.state != new_issue.state:
            statemap = self.property_names.get("bugzilla_map_state")
            data["status"] = statemap.get(new_issue.state) or new_issue.state

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

    async def _get_bugzilla_bugs(self, bugids, sub_issues=False):
        issues = []
        fields = "id,summary,status,product,cf_user_story,assigned_to,priority,depends_on,blocks,attachments,comments,see_also,creation_time,cf_last_resolved,keywords,whiteboard,attachments"

        response = await self.client.get("/bug", params={"id": ",".join(bugids), "include_fields": fields})
        response_json = response.json()

        unhandled = set(bugids)

        for bug in response_json["bugs"]:
            assignee = bug["assigned_to"] if bug["assigned_to"] != "nobody@mozilla.org" else None
            parents = [IssueRef(repo=self.repo_name, id=str(parent_id)) for parent_id in bug["blocks"]]

            closed_date = None
            if bug["cf_last_resolved"] and bug["status"] == "RESOLVED":
                closed_date = datetime.datetime.fromisoformat(bug["cf_last_resolved"])

            statemap = self.property_names.get("bugzilla_map_state")
            status = statemap.get(bug["status"]) or bug["status"]

            labels = set(bug["keywords"])
            for attachment in bug["attachments"]:
                for flag in attachment["flags"]:
                    labels.add("attach:" + flag["name"] + flag["status"])

            review_url = None
            notion_url = None
            phab = next(
                filter(
                    lambda att: att["is_obsolete"] == 0 and att.get("content_type") == "text/x-phabricator-request",
                    bug["attachments"],
                ),
                None,
            )
            if phab:
                if bug["status"] in ("ASSIGNED", "REOPENED"):
                    status = statemap.get("IN REVIEW") or "IN REVIEW"  # TODO hack

                review_url = base64.b64decode(phab["data"]).decode("utf-8")

            for url in bug["see_also"]:
                if url.startswith("https://www.notion.so/"):
                    notion_url = url
                    break

            issue = Issue(
                id=str(bug["id"]),
                repo=self.repo_name,
                url=f"{self.base_url}/show_bug.cgi?id={bug['id']}",
                notion_url=notion_url,
                review_url=review_url,
                title=bug["summary"],
                state=status,
                labels=labels,
                whiteboard=bug["whiteboard"] or "",
                description=bug["cf_user_story"] or getnestedattr(lambda: bug["comments"][0]["text"], ""),
                assignees={User(self.user_map, tracker_user=assignee)} if assignee else set(),
                priority=bug["priority"] if bug["priority"] != "--" else None,
                parents=parents,
                sub_issues=sub_issues,
                created_date=datetime.datetime.fromisoformat(bug["creation_time"]),
                closed_date=closed_date,
            )

            issue.sub_issues = []
            for sub_issue_id in bug["depends_on"]:
                if not self._is_allowed_product(bug):
                    continue

                str_sub_id = str(sub_issue_id)
                self._hack_parent_cache[str_sub_id] = issue.id
                issue.sub_issues.append(IssueRef(repo=self.repo_name, id=str_sub_id, parents=[issue]))

            unhandled.remove(issue.id)
            issues.append(issue)

        for bugid in unhandled:
            parents = []
            if bugid in self._hack_parent_cache:
                parents = [IssueRef(id=self._hack_parent_cache[bugid], repo=self.repo_name)]

            issue = Issue(
                id=bugid,
                repo=self.repo_name,
                url=f"{self.base_url}/show_bug.cgi?id={bugid}",
                title="Secure Bug",
                description="",
                priority=None,
                state=None,
                parents=parents,
            )

            issues.append(issue)

        return issues

    async def get_issues_by_number(self, bugrefs, sub_issues=False):
        """Retrieve issues by their id number."""
        bugids = [urllib.parse.quote(str(bug.id), safe="") for bug in bugrefs]

        chunk_size = 100

        tasks = [
            asyncio.create_task(self._get_bugzilla_bugs(bugids[i : i + chunk_size], sub_issues))
            for i in range(0, len(bugids), chunk_size)
        ]

        for got_bugs in asyncio.as_completed(tasks):
            for issue in await got_bugs:
                yield issue


class BugzillaAsyncRetryingClient(AsyncRetryingClient):
    """A retrying client that will additionally retry on bugzilla errors."""

    async def send(self, request, *args, recur=None, **kwargs):
        """AsyncRetryingClient send that retries."""
        response = await super().send(request, *args, recur=recur, **kwargs)

        if recur is None:
            recur = self.MAX_RETRY

        try:
            response_json = response.json()
        except json.JSONDecodeError as e:
            if recur <= 0:
                raise

            logger.info(f"Sleeping {self.RETRY_TIMEOUT} seconds due to {type(e).__name__}")
            await asyncio.sleep(self.RETRY_TIMEOUT)
            return await self.send(request, *args, recur=recur - 1, **kwargs)

        if response_json.get("error", False):
            if recur <= 0:
                raise Exception("Bugzilla Error: " + str(response_json))

            logger.info(f"Sleeping {self.RETRY_TIMEOUT} seconds due to {response_json}")
            await asyncio.sleep(self.RETRY_TIMEOUT)
            return await self.send(request, *args, recur=recur - 1, **kwargs)

        return response
