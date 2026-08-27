import asyncio
import dataclasses
import datetime
import hashlib
import json
import logging
import sqlite3

from collections import defaultdict

from notion_client.errors import APIResponseError
from notion_client.helpers import async_iterate_paginated_api

from .base import BaseSync
from .twoway_cache import TwoWayNotionCache

from ..util import canonical_notion_url, ensure_date, getnestedattr, guard_notion_query_response
from ..tracker.common import IssueRef
from ..util import diff_dataclasses
from ..notion_data import CustomNotionToMarkdown

logger = logging.getLogger("twoway_sync")


class TrackerTwoWaySync(BaseSync):
    """Two-way tracker sync with incremental/LWW semantics."""

    def __init__(
        self,
        incremental_lookback_seconds=None,
        tasks_tracker_to_notion=True,
        tasks_notion_to_tracker=False,
        milestones_tracker_to_notion=False,
        milestones_notion_to_tracker=True,
        tasks_tracker_to_notion_create=True,
        tasks_notion_to_tracker_create=False,
        milestones_tracker_to_notion_create=False,
        milestones_notion_to_tracker_create=False,
        epics_tracker_to_notion=False,
        epics_notion_to_tracker=True,
        epics_tracker_to_notion_create=False,
        epics_notion_to_tracker_create=False,
        tasks_conflict_preference="tracker",
        milestones_conflict_preference="notion",
        epics_conflict_preference="notion",
        tracker_kind=None,
        twoway_cache_enabled=False,
        twoway_cache_path=".cache/mzla-notion/twoway.sqlite3",
        **kwargs,
    ):
        """Initialize two-way sync configuration and directional behavior."""
        super().__init__(**kwargs, logger=logging.getLogger("twoway_sync"))
        self.incremental_lookback_seconds = incremental_lookback_seconds
        self.tasks_tracker_to_notion = tasks_tracker_to_notion
        self.tasks_notion_to_tracker = tasks_notion_to_tracker
        self.milestones_tracker_to_notion = milestones_tracker_to_notion
        self.milestones_notion_to_tracker = milestones_notion_to_tracker
        self.epics_tracker_to_notion = epics_tracker_to_notion
        self.epics_notion_to_tracker = epics_notion_to_tracker
        self.tasks_tracker_to_notion_create = tasks_tracker_to_notion_create
        self.tasks_notion_to_tracker_create = tasks_notion_to_tracker_create
        self.milestones_tracker_to_notion_create = milestones_tracker_to_notion_create
        self.milestones_notion_to_tracker_create = milestones_notion_to_tracker_create
        self.epics_tracker_to_notion_create = epics_tracker_to_notion_create
        self.epics_notion_to_tracker_create = epics_notion_to_tracker_create
        self.conflict_preference = {
            "task": "notion_to_tracker" if tasks_conflict_preference == "notion" else "tracker_to_notion",
            "milestone": "notion_to_tracker" if milestones_conflict_preference == "notion" else "tracker_to_notion",
            "epic": "notion_to_tracker" if epics_conflict_preference == "notion" else "tracker_to_notion",
        }
        self.tracker_kind = tracker_kind or type(self.tracker).__name__
        self.twoway_cache_enabled = twoway_cache_enabled
        self.twoway_cache_path = twoway_cache_path
        self._notion_cache = None
        self._using_notion_cache = False
        self.full_sync = incremental_lookback_seconds is None
        self._task_create_cache = {}
        self._unlinked_notion_tasks = []
        self._task_discovery_since = None

        if self.milestones_notion_to_tracker_create:
            self.logger.warning("milestones_notion_to_tracker_create is not supported in v2; skipping")
            self.milestones_notion_to_tracker_create = False
        if self.epics_notion_to_tracker_create:
            self.logger.warning("epics_notion_to_tracker_create is not supported in v2; skipping")
            self.epics_notion_to_tracker_create = False

    async def _async_init(self):
        if self.twoway_cache_enabled:
            self._notion_cache = self._open_notion_cache()

        if self._notion_cache and not self.full_sync and self._notion_cache.is_valid(self._cache_fingerprint()):
            self._using_notion_cache = True
            await self._async_init_from_cache()
            return

        if self._notion_cache and not self.full_sync:
            self.logger.info("Two-way Notion cache missing or stale, doing full Notion discovery")

        await self._async_init_full()
        self._rebuild_notion_cache()

    async def _async_init_full(self):
        use_single_task_query = self.tasks_notion_to_tracker and self.tasks_notion_to_tracker_create
        if not use_single_task_query:
            async with asyncio.TaskGroup() as tg:
                tg.create_task(super()._async_init())
                if self.epics_db:
                    epics_issues = tg.create_task(
                        self._discover_notion_issues(self.epics_db.database_id, self.propnames["notion_epics_team"])
                    )
                milestones_issues = tg.create_task(
                    self._discover_notion_issues(
                        self.milestones_db.database_id, self.propnames["notion_milestones_team"]
                    )
                )

            self._notion_epic_issues = epics_issues.result() if self.epics_db else {}
            self._notion_milestone_issues = milestones_issues.result()
            self._unlinked_notion_tasks = []
            return

        async with asyncio.TaskGroup() as tg:
            if self.epics_db:
                valid_epics = tg.create_task(self.epics_db.validate_props())
            valid_milestones = tg.create_task(self.milestones_db.validate_props())
            valid_tasks = tg.create_task(self.tasks_db.validate_props())
            tasks_partitioned = tg.create_task(self._discover_notion_tasks_partitioned(self._task_discovery_since))
            if self.epics_db:
                epics_issues = tg.create_task(
                    self._discover_notion_issues(self.epics_db.database_id, self.propnames["notion_epics_team"])
                )
            milestones_issues = tg.create_task(
                self._discover_notion_issues(self.milestones_db.database_id, self.propnames["notion_milestones_team"])
            )

            if self.sprint_db:
                sprint_pages = tg.create_task(self.sprint_db.get_all_pages())

        if self.epics_db and not valid_epics.result():
            raise Exception("Epic schema failed to validate")
        if not valid_milestones.result():
            raise Exception("Milestone schema failed to validate")
        if not valid_tasks.result():
            raise Exception("Tasks schema failed to validate")

        linked, unlinked = tasks_partitioned.result()
        self._notion_tasks_issues = linked
        self._unlinked_notion_tasks = unlinked
        self._notion_epic_issues = epics_issues.result() if self.epics_db else {}
        self._notion_milestone_issues = milestones_issues.result()

        if self.sprint_db:
            self._all_sprint_pages = sprint_pages.result()

    async def _async_init_from_cache(self):
        self.logger.info("Using two-way Notion cache at %s", self.twoway_cache_path)
        self._notion_tasks_issues, duplicate_tasks = self._notion_cache.load_linked_pages(
            "task", self.tasks_db.database_id
        )
        self._notion_milestone_issues, duplicate_milestones = self._notion_cache.load_linked_pages(
            "milestone", self.milestones_db.database_id
        )
        if self.epics_db:
            self._notion_epic_issues, duplicate_epics = self._notion_cache.load_linked_pages(
                "epic", self.epics_db.database_id
            )
        else:
            self._notion_epic_issues, duplicate_epics = {}, set()
        self._log_duplicate_cache_refs("task", duplicate_tasks)
        self._log_duplicate_cache_refs("milestone", duplicate_milestones)
        self._log_duplicate_cache_refs("epic", duplicate_epics)

        async with asyncio.TaskGroup() as tg:
            if self.epics_db:
                valid_epics = tg.create_task(self.epics_db.validate_props())
            valid_milestones = tg.create_task(self.milestones_db.validate_props())
            valid_tasks = tg.create_task(self.tasks_db.validate_props())
            changed_tasks = tg.create_task(
                self._discover_recent_notion_pages(
                    "task",
                    self.tasks_db.database_id,
                    self.propnames.get("notion_tasks_team"),
                    self._task_discovery_since,
                )
            )
            changed_milestones = tg.create_task(
                self._discover_recent_notion_pages(
                    "milestone",
                    self.milestones_db.database_id,
                    self.propnames.get("notion_milestones_team"),
                    self._task_discovery_since,
                )
            )
            if self.epics_db:
                changed_epics = tg.create_task(
                    self._discover_recent_notion_pages(
                        "epic",
                        self.epics_db.database_id,
                        self.propnames.get("notion_epics_team"),
                        self._task_discovery_since,
                    )
                )

            if self.sprint_db:
                sprint_pages = tg.create_task(self.sprint_db.get_all_pages())

        if self.epics_db and not valid_epics.result():
            raise Exception("Epic schema failed to validate")
        if not valid_milestones.result():
            raise Exception("Milestone schema failed to validate")
        if not valid_tasks.result():
            raise Exception("Tasks schema failed to validate")

        self._unlinked_notion_tasks = []
        self._merge_recent_notion_pages("task", self.tasks_db.database_id, changed_tasks.result())
        self._merge_recent_notion_pages("milestone", self.milestones_db.database_id, changed_milestones.result())
        if self.epics_db:
            self._merge_recent_notion_pages("epic", self.epics_db.database_id, changed_epics.result())
        self._remove_duplicate_cache_refs("task", self.tasks_db.database_id, self._notion_tasks_issues)
        self._remove_duplicate_cache_refs("milestone", self.milestones_db.database_id, self._notion_milestone_issues)
        if self.epics_db:
            self._remove_duplicate_cache_refs("epic", self.epics_db.database_id, self._notion_epic_issues)

        if self.sprint_db:
            self._all_sprint_pages = sprint_pages.result()

    def _open_notion_cache(self):
        try:
            return TwoWayNotionCache(self.twoway_cache_path, self.project_key)
        except sqlite3.DatabaseError:
            self.logger.warning("Two-way Notion cache is corrupt, rebuilding %s", self.twoway_cache_path)
            try:
                TwoWayNotionCache(self.twoway_cache_path, self.project_key).close()
            except sqlite3.DatabaseError:
                from pathlib import Path

                Path(self.twoway_cache_path).unlink(missing_ok=True)
            return TwoWayNotionCache(self.twoway_cache_path, self.project_key)

    def _cache_fingerprint(self):
        data = {
            "tracker_kind": self.tracker_kind,
            "tasks_database_id": self.tasks_db.database_id,
            "milestones_database_id": self.milestones_db.database_id,
            "epics_database_id": self.epics_db.database_id if self.epics_db else None,
            "sprint_database_id": self.sprint_db.database_id if self.sprint_db else None,
            "milestones_issue_type": self.milestones_issue_type,
            "epics_issue_type": self.epics_issue_type,
            "team_ids": sorted(self.configured_team_ids),
            "repositories": sorted(self.tracker.get_all_repositories()),
            "properties": self.propnames,
        }
        raw = json.dumps(data, sort_keys=True, default=str)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def _rebuild_notion_cache(self):
        if not self._notion_cache:
            return

        self._notion_cache.reset(self._cache_fingerprint())
        cache_sources = [
            ("task", self.tasks_db.database_id, self._notion_tasks_issues),
            ("milestone", self.milestones_db.database_id, self._notion_milestone_issues),
        ]
        if self.epics_db:
            cache_sources.append(("epic", self.epics_db.database_id, self._notion_epic_issues))

        for entity_kind, database_id, refs in cache_sources:
            for repo, pages_by_issue in refs.items():
                for issue_id, page in pages_by_issue.items():
                    issue_url = self._page_issue_url(page)
                    self._notion_cache.upsert_page(
                        entity_kind,
                        database_id,
                        page,
                        issue_ref=IssueRef(repo=repo, id=issue_id),
                        issue_url=issue_url,
                    )

    def _log_duplicate_cache_refs(self, entity_kind, duplicate_refs):
        for repo, issue_id in sorted(duplicate_refs):
            self.logger.warning(
                "Skipping cached %s %s#%s because multiple Notion pages use the same issue URL",
                entity_kind,
                repo,
                issue_id,
            )

    def _remove_duplicate_cache_refs(self, entity_kind, database_id, refs):
        duplicates = self._notion_cache.duplicate_issue_keys(entity_kind, database_id)
        self._log_duplicate_cache_refs(entity_kind, duplicates)
        for repo, issue_id in duplicates:
            refs.get(repo, {}).pop(issue_id, None)

    def _page_issue_url(self, page):
        value = self._get_prop(page, "notion_issue_field")
        if isinstance(value, list):
            return getnestedattr(lambda: value[0]["external"]["url"], "") if value else ""
        return value or ""

    def _page_issue_ref(self, page):
        issue_url = self._page_issue_url(page)
        ref = self.tracker.parse_issueref(issue_url) if issue_url else None
        if ref and self.tracker.is_repo_allowed(ref.repo):
            return ref, issue_url
        return None, issue_url

    def _drop_page_from_refs(self, refs, page_id):
        for repo in list(refs):
            for issue_id, page in list(refs[repo].items()):
                if page.get("id") == page_id:
                    del refs[repo][issue_id]
            if not refs[repo]:
                del refs[repo]

    def _cache_upsert_page(self, entity_kind, database_id, page, ref, issue_url, observed=False):
        if self._notion_cache and (observed or not self.dry):
            self._notion_cache.upsert_page(entity_kind, database_id, page, issue_ref=ref, issue_url=issue_url)

    def _cache_delete_page(self, entity_kind, database_id, page_id, observed=False):
        if self._notion_cache and (observed or not self.dry):
            self._notion_cache.delete_page(entity_kind, database_id, page_id)

    async def _record_task_cache_update(self, page, tracker_issue):
        self._cache_upsert_page(
            "task",
            self.tasks_db.database_id,
            page,
            IssueRef(repo=tracker_issue.repo, id=tracker_issue.id),
            tracker_issue.url,
        )

    def _record_milestone_cache_update(self, page, tracker_issue):
        self._cache_upsert_page(
            "milestone",
            self.milestones_db.database_id,
            page,
            IssueRef(repo=tracker_issue.repo, id=tracker_issue.id),
            tracker_issue.url,
        )

    def _record_epic_cache_update(self, page, tracker_issue):
        if not self.epics_db:
            return
        self._cache_upsert_page(
            "epic",
            self.epics_db.database_id,
            page,
            IssueRef(repo=tracker_issue.repo, id=tracker_issue.id),
            tracker_issue.url,
        )

    def _refs_for_entity(self, entity_kind):
        if entity_kind == "task":
            return self._notion_tasks_issues
        if entity_kind == "milestone":
            return self._notion_milestone_issues
        if entity_kind == "epic":
            return self._notion_epic_issues
        raise ValueError(f"Unknown entity kind {entity_kind}")

    def _team_prop_key_for_entity(self, entity_kind):
        if entity_kind == "task":
            return "notion_tasks_team"
        if entity_kind == "milestone":
            return "notion_milestones_team"
        if entity_kind == "epic":
            return "notion_epics_team"
        raise ValueError(f"Unknown entity kind {entity_kind}")

    def _merge_linked_page(self, entity_kind, database_id, refs, page):
        page_id = page["id"]
        self._drop_page_from_refs(refs, page_id)
        ref, issue_url = self._page_issue_ref(page)
        if ref:
            refs[ref.repo][ref.id] = page
            self._cache_upsert_page(entity_kind, database_id, page, ref, issue_url, observed=True)
            return ref

        self._cache_delete_page(entity_kind, database_id, page_id, observed=True)
        return None

    def _is_task_unlinked_create_candidate(self, page):
        if self._get_prop(page, "notion_issue_field", []):
            return False

        status = getnestedattr(
            lambda: self._get_prop(page, "notion_tasks_status")["name"],
            None,
        )
        if self._is_closed_status(status):
            return False

        task_team_prop = self.propnames.get("notion_tasks_team")
        if task_team_prop and self.configured_team_ids:
            page_teams = set(self._get_relation_ids(page, "notion_tasks_team"))
            if not page_teams.intersection(self.configured_team_ids):
                return False

        return True

    def _merge_recent_notion_pages(self, entity_kind, database_id, pages):
        refs = self._refs_for_entity(entity_kind)
        for page in pages:
            ref = self._merge_linked_page(entity_kind, database_id, refs, page)
            if entity_kind == "task" and ref is None and self._is_task_unlinked_create_candidate(page):
                self._unlinked_notion_tasks.append(page)

    def _recent_filter(self, since):
        return {
            "timestamp": "last_edited_time",
            "last_edited_time": {
                "on_or_after": since.strftime("%Y-%m-%dT%H:%M:%SZ"),
            },
        }

    def _team_filter(self, team_prop):
        if not team_prop or not self.configured_team_ids:
            return None
        return {"or": [{"property": team_prop, "relation": {"contains": team}} for team in self.configured_team_ids]}

    def _combined_filter(self, *filters):
        filters = [item for item in filters if item]
        if len(filters) == 1:
            return filters[0]
        return {"and": filters}

    async def _discover_recent_notion_pages(self, entity_kind, database_id, team_prop, since):
        pages = []
        query_filter = self._combined_filter(self._team_filter(team_prop), self._recent_filter(since))
        query_func = guard_notion_query_response(
            self.notion.databases.query,
            context=f"Notion database query ({database_id})",
        )

        async for page in async_iterate_paginated_api(
            query_func,
            database_id=database_id,
            filter=query_filter,
        ):
            edited = self._page_timestamp(page)
            if edited is None or edited < since:
                continue

            if team_prop and self.configured_team_ids:
                prop_key = self._team_prop_key_for_entity(entity_kind)
                page_teams = set(self._get_relation_ids(page, prop_key))
                if not page_teams.intersection(self.configured_team_ids):
                    continue

            pages.append(page)

        return pages

    def _find_task_parents(self, tracker_issue):
        milestone_issues = self._notion_milestone_issues

        found_milestone_parents = [
            milestone_parent
            for parent in tracker_issue.parents
            if (milestone_parent := milestone_issues.get(parent.repo, {}).get(parent.id, None)) is not None
        ]

        return found_milestone_parents

    def _find_milestone_epic_parent(self, tracker_issue):
        if not self.epics_db:
            return None
        for parent in tracker_issue.parents:
            if epic_parent := self._notion_epic_issues.get(parent.repo, {}).get(parent.id, None):
                return epic_parent
        return None

    def _page_timestamp(self, page):
        value = page.get("last_edited_time")
        if not value:
            return None
        return datetime.datetime.fromisoformat(value.replace("Z", "+00:00")).replace(second=0, microsecond=0)

    def _format_timestamp(self, value):
        if not value:
            return "None"
        return value.isoformat()

    def _is_closed_status(self, status_name):
        return bool(status_name and status_name in self.propnames["notion_closed_states"])

    def _is_task_issue(self, tracker_issue):
        return self.tracker.is_task_issue(
            tracker_issue,
            milestones_issue_type=self.milestones_issue_type,
            epics_issue_type=self.epics_issue_type,
        )

    def _is_milestone_issue(self, tracker_issue):
        milestone_issue_type = self.milestones_issue_type or getattr(self.tracker, "milestones_issue_type", None)
        if milestone_issue_type:
            return tracker_issue.issue_type == milestone_issue_type

        # Generic parent issues fallback
        if tracker_issue.parents:
            return False
        return bool(tracker_issue.sub_issues) or tracker_issue.title.startswith("[meta]")

    def _is_epic_issue(self, tracker_issue):
        epic_issue_type = self.epics_issue_type or getattr(self.tracker, "epics_issue_type", None)
        return bool(epic_issue_type and tracker_issue.issue_type == epic_issue_type)

    def _get_epic_notion_data_from_tracker(self, tracker_issue):
        notion_data = {
            self.propnames["notion_epics_title"]: tracker_issue.title,
            self.propnames["notion_issue_field"]: tracker_issue.url,
        }

        assignees = [user.notion_user for user in tracker_issue.assignees if user.notion_user is not None]
        self._set_if_prop(notion_data, "notion_epics_assignee", assignees or None)
        self._set_if_prop(notion_data, "notion_epics_priority", tracker_issue.priority)

        state = tracker_issue.state
        if not state:
            state = (
                self.propnames["notion_closed_states"][0]
                if tracker_issue.closed_date
                else self.propnames["notion_default_open_state"]
            )
        self._set_if_prop(notion_data, "notion_epics_status", state)
        self._set_if_date_prop(
            notion_data,
            "notion_epics_dates",
            ensure_date(tracker_issue.start_date),
            ensure_date(tracker_issue.end_date),
        )

        return notion_data

    async def synchronize_single_epic_from_tracker(self, tracker_issue, page, candidate_debug=None):
        """Apply tracker epic fields onto the linked Notion epic page."""
        notion_data = self._get_epic_notion_data_from_tracker(tracker_issue)
        changed = self.epics_db.page_diff(notion_data, page, log=False)
        if changed:
            self.logger.info(f"Updating epic (Tracker->Notion) {page.get('url')} - {tracker_issue.title}")
            if candidate_debug:
                self.logger.debug(f"  candidate: {candidate_debug}")
            self.logger.debug("  notion changes:")
            self.epics_db.page_diff(notion_data, page, log=self.logger.isEnabledFor(logging.DEBUG))
            self.logger.debug("\t" + str(notion_data))
            updated_page = await self.epics_db.update_page(page, notion_data, diff_log=False, return_page=True)
            if updated_page:
                page = updated_page
            self._record_epic_cache_update(page, tracker_issue)
        elif not self.hide_unchanged:
            self.logger.info(f"Unchanged epic {tracker_issue.repo}#{tracker_issue.id} - {tracker_issue.title}")
        return changed

    def _get_epic_tracker_issue_from_notion(self, tracker_issue, page):
        community_assignees = {assignee for assignee in tracker_issue.assignees if assignee.notion_user is None}
        epic_assignees = {
            self.tracker.new_user(notion_user=assignee["id"])
            for assignee in self._get_prop(page, "notion_epics_assignee", [])
        }

        title = self._get_richtext_prop(page, "notion_epics_title", "")
        labels = set(tracker_issue.labels)
        if self.epics_extra_label:
            labels.add(self.epics_extra_label)

        start_date, end_date = self._get_date_prop(page, "notion_epics_dates")

        return dataclasses.replace(
            tracker_issue,
            title=self.epics_tracker_prefix + title,
            labels=labels,
            state=(self._get_prop(page, "notion_epics_status") or {}).get("name"),
            priority=(self._get_prop(page, "notion_epics_priority") or {}).get("name"),
            assignees=community_assignees.union(epic_assignees),
            notion_url=canonical_notion_url(page.get("url", "")),
            start_date=ensure_date(start_date) if start_date else None,
            end_date=ensure_date(end_date) if end_date else None,
            issue_type=self.epics_issue_type or tracker_issue.issue_type,
        )

    async def synchronize_single_epic(self, tracker_issue, page, skip_unchanged_msg=False, candidate_debug=None):
        """Apply Notion epic fields onto the linked tracker epic issue."""
        old_issue_url = self._get_prop(page, "notion_issue_field")
        if old_issue_url and old_issue_url != tracker_issue.url:
            self.logger.warning(
                f"Epic URL changed for {tracker_issue.repo}#{tracker_issue.id}: {old_issue_url} -> {tracker_issue.url}"
            )

        new_issue = self._get_epic_tracker_issue_from_notion(tracker_issue, page)
        needs_update = self.tracker.should_update_milestone_issue(tracker_issue, new_issue)

        if needs_update:
            self.logger.info(f"Updating epic (Notion->Tracker) {tracker_issue.url} - {new_issue.title}")
            if candidate_debug:
                self.logger.debug(f"  candidate: {candidate_debug}")
            diff_dataclasses(tracker_issue, new_issue, log=self.logger.debug)

            if not self.dry:
                await self.tracker.update_milestone_issue(tracker_issue, new_issue)
            return True
        elif not skip_unchanged_msg and not self.hide_unchanged:
            self.logger.info(
                f"Unchanged epic {tracker_issue.id} - {tracker_issue.title} ({tracker_issue.url} / {new_issue.notion_url})"
            )
        return False

    def _pick_direction(self, entity_kind, tracker_issue, notion_page, tracker_to_notion, notion_to_tracker):
        if tracker_to_notion and not notion_to_tracker:
            return "tracker_to_notion"
        if notion_to_tracker and not tracker_to_notion:
            return "notion_to_tracker"
        if not tracker_to_notion and not notion_to_tracker:
            return None

        tracker_ts = tracker_issue.updated_date or tracker_issue.created_date
        if tracker_ts:
            tracker_ts = tracker_ts.replace(second=0, microsecond=0)
        notion_ts = self._page_timestamp(notion_page)
        fallback = self.conflict_preference[entity_kind]

        if tracker_ts and notion_ts:
            if tracker_ts > notion_ts:
                return "tracker_to_notion"
            if notion_ts > tracker_ts:
                return "notion_to_tracker"
            return fallback

        if tracker_ts and not notion_ts:
            return "tracker_to_notion"
        if notion_ts and not tracker_ts:
            return "notion_to_tracker"
        return fallback

    def _get_milestone_notion_data_from_tracker(self, tracker_issue):
        notion_data = {
            self.propnames["notion_milestones_title"]: tracker_issue.title,
            self.propnames["notion_issue_field"]: tracker_issue.url,
        }

        assignees = [user.notion_user for user in tracker_issue.assignees if user.notion_user is not None]
        self._set_if_prop(notion_data, "notion_milestones_assignee", assignees or None)
        self._set_if_prop(notion_data, "notion_milestones_priority", tracker_issue.priority)

        state = tracker_issue.state
        if not state:
            state = (
                self.propnames["notion_closed_states"][0]
                if tracker_issue.closed_date
                else self.propnames["notion_default_open_state"]
            )
        self._set_if_prop(notion_data, "notion_milestones_status", state)

        self._set_if_date_prop(
            notion_data,
            "notion_milestones_dates",
            ensure_date(tracker_issue.start_date),
            ensure_date(tracker_issue.end_date),
        )
        if self.epics_db and self.propnames.get("notion_milestones_epic_relation"):
            epic_parent = self._find_milestone_epic_parent(tracker_issue)
            self._set_if_prop(
                notion_data,
                "notion_milestones_epic_relation",
                [epic_parent["id"]] if epic_parent else [],
            )

        return notion_data

    async def _sync_milestone_epic_relation_from_tracker(self, tracker_issue, page, candidate_debug=None):
        if not self.epics_db or not self.propnames.get("notion_milestones_epic_relation"):
            return False

        epic_parent = self._find_milestone_epic_parent(tracker_issue)
        relation_data = {self.propnames["notion_milestones_epic_relation"]: [epic_parent["id"]] if epic_parent else []}
        changed = self.milestones_db.page_diff(relation_data, page, log=False)
        if changed:
            self.logger.info(
                f"Updating milestone epic relation (Tracker->Notion) {page.get('url')} - {tracker_issue.title}"
            )
            if candidate_debug:
                self.logger.debug(f"  timestamps: {candidate_debug}")
            self.milestones_db.page_diff(relation_data, page, log=True, log_level=logging.INFO)
            self.logger.debug(relation_data)
            updated_page = await self.milestones_db.update_page(page, relation_data, diff_log=False, return_page=True)
            if updated_page:
                page = updated_page
            self._record_milestone_cache_update(page, tracker_issue)
        return changed

    async def synchronize_single_milestone_from_tracker(self, tracker_issue, page, candidate_debug=None):
        """Apply tracker milestone fields onto the linked Notion milestone page."""
        notion_data = self._get_milestone_notion_data_from_tracker(tracker_issue)
        changed = self.milestones_db.page_diff(notion_data, page, log=False)
        if changed:
            self.logger.info(f"Updating milestone (Tracker->Notion) {page.get('url')} - {tracker_issue.title}")
            if candidate_debug:
                self.logger.debug(f"  timestamps: {candidate_debug}")
            self.milestones_db.page_diff(notion_data, page, log=True, log_level=logging.INFO)
            self.logger.debug("\t" + str(notion_data))
            updated_page = await self.milestones_db.update_page(page, notion_data, diff_log=False, return_page=True)
            if updated_page:
                page = updated_page
            self._record_milestone_cache_update(page, tracker_issue)
        elif not self.hide_unchanged:
            self.logger.info(f"Unchanged milestone {tracker_issue.repo}#{tracker_issue.id} - {tracker_issue.title}")
            if candidate_debug:
                self.logger.debug(f"  timestamps: {candidate_debug}")
        return changed

    async def synchronize_single_milestone(self, tracker_issue, page, skip_unchanged_msg=False, candidate_debug=None):
        """Synchronize a single Notion milestone to the issue tracker."""
        old_issue_url = self._get_prop(page, "notion_issue_field")
        if old_issue_url and old_issue_url != tracker_issue.url:
            self.logger.warning(
                f"Milestone URL changed for {tracker_issue.repo}#{tracker_issue.id}: {old_issue_url} -> {tracker_issue.url}"
            )

        body = tracker_issue.description
        if self.milestones_body_sync or (self.milestones_body_sync_if_empty and not len(tracker_issue.description)):
            blocks = await self.milestones_db.get_page_contents(page["id"])
            converter = CustomNotionToMarkdown(self.notion, strip_images=True, tracker=self.tracker)
            body = await converter.convert(blocks) or ""

        community_assignees = {assignee for assignee in tracker_issue.assignees if assignee.notion_user is None}
        milestone_assignees = {
            self.tracker.new_user(notion_user=assignee["id"])
            for assignee in self._get_prop(page, "notion_milestones_assignee", [])
        }

        title = self._get_richtext_prop(page, "notion_milestones_title", "")
        labels = set(tracker_issue.labels)
        if self.milestones_extra_label:
            labels.add(self.milestones_extra_label)

        start_date, end_date = self._get_date_prop(page, "notion_milestones_dates")

        new_issue = dataclasses.replace(
            tracker_issue,
            title=self.milestones_tracker_prefix + title,
            labels=labels,
            description=body,
            state=(self._get_prop(page, "notion_milestones_status") or {}).get("name"),
            priority=(self._get_prop(page, "notion_milestones_priority") or {}).get("name"),
            assignees=community_assignees.union(milestone_assignees),
            notion_url=canonical_notion_url(page.get("url", "")),
            start_date=ensure_date(start_date) if start_date else None,
            end_date=ensure_date(end_date) if end_date else None,
        )

        if self.milestones_issue_type:
            new_issue.issue_type = self.milestones_issue_type

        await self._sync_milestone_epic_relation_from_tracker(tracker_issue, page, candidate_debug)
        needs_update = self.tracker.should_update_milestone_issue(tracker_issue, new_issue)

        if needs_update:
            self.logger.info(f"Updating milestone (Notion->Tracker) {tracker_issue.url} - {new_issue.title}")
            if candidate_debug:
                self.logger.debug(f"  timestamps: {candidate_debug}")
            diff_dataclasses(tracker_issue, new_issue, log=self.logger.debug)

            if not self.dry:
                await self.tracker.update_milestone_issue(tracker_issue, new_issue)
            return True
        elif not skip_unchanged_msg and not self.hide_unchanged:
            self.logger.info(
                f"Unchanged milestone {tracker_issue.id} - {tracker_issue.title} ({tracker_issue.url} / {new_issue.notion_url})"
            )
            if candidate_debug:
                self.logger.debug(f"  timestamps: {candidate_debug}")
        return False

    def _get_task_tracker_issue_from_notion(self, tracker_issue, page):
        title = self._get_richtext_prop(page, "notion_tasks_title", tracker_issue.title)
        status = (self._get_prop(page, "notion_tasks_status") or {}).get("name")
        priority = (self._get_prop(page, "notion_tasks_priority") or {}).get("name")
        estimate = tracker_issue.estimate
        if self.propnames.get("notion_tasks_estimate"):
            estimate = (self._get_prop(page, "notion_tasks_estimate") or {}).get("name")

        assignees = {
            self.tracker.new_user(notion_user=assignee["id"])
            for assignee in self._get_prop(page, "notion_tasks_assignee", [])
        }

        return dataclasses.replace(
            tracker_issue,
            title=title or tracker_issue.title,
            state=status or tracker_issue.state,
            priority=priority or tracker_issue.priority,
            estimate=estimate,
            assignees=assignees if assignees else tracker_issue.assignees,
            notion_url=canonical_notion_url(page.get("url", tracker_issue.notion_url)),
        )

    async def _task_needs_notion_update(self, tracker_issue, page):
        parent_pages = self._find_task_parents(tracker_issue) or []
        notion_data = await self._get_task_notion_data(
            tracker_issue=tracker_issue,
            parent_milestone_pages=parent_pages,
            old_page=page,
        )
        return self.tasks_db.page_diff(notion_data, page, log=False)

    def _task_needs_tracker_update(self, tracker_issue, page):
        new_issue = self._get_task_tracker_issue_from_notion(tracker_issue, page)
        return self.tracker.should_update_task_issue(tracker_issue, new_issue)

    async def synchronize_single_task_to_tracker(self, tracker_issue, page, candidate_debug=None):
        """Apply Notion task fields onto the linked tracker task issue."""
        new_issue = self._get_task_tracker_issue_from_notion(tracker_issue, page)
        if self._task_needs_tracker_update(tracker_issue, page):
            self.logger.info(f"Updating task (Notion->Tracker) {tracker_issue.url} - {new_issue.title}")
            if candidate_debug:
                self.logger.debug(f"  timestamps: {candidate_debug}")
            if not self.dry:
                await self.tracker.update_task_issue(tracker_issue, new_issue)
            return True
        elif not self.hide_unchanged:
            self.logger.info(f"Unchanged task {tracker_issue.repo}#{tracker_issue.id}")
            if candidate_debug:
                self.logger.debug(f"  timestamps: {candidate_debug}")
        return False

    def _collect_candidates(self, notion_refs, recent_refs, since, tracker_to_notion, notion_to_tracker):
        linked = set(notion_refs.keys())
        if not tracker_to_notion and not notion_to_tracker:
            return set(), len(linked), len(linked)

        if self.full_sync:
            return linked, len(linked), 0

        candidates = set()
        if notion_to_tracker:
            candidates.update(
                key
                for key, page in notion_refs.items()
                if (ts := self._page_timestamp(page)) is not None and ts >= since
            )
        if tracker_to_notion:
            candidates.update(linked.intersection(recent_refs))

        return candidates, len(linked), len(linked - candidates)

    async def _load_tracker_candidates(self, candidates, recent_by_repo):
        tracker_issues = {}
        missing = defaultdict(list)

        for repo, issue_id in candidates:
            issue = recent_by_repo.get(repo, {}).get(issue_id)
            if issue:
                tracker_issues[(repo, issue_id)] = issue
            else:
                missing[repo].append(IssueRef(repo=repo, id=issue_id))

        for repo, refs in missing.items():
            async for issue in self.tracker.get_issues_by_number(refs):
                tracker_issues[(repo, issue.id)] = issue

        return tracker_issues

    async def _retrieve_cached_page(self, entity_kind, database_id, refs, key, page):
        try:
            current_page = await self.notion.pages.retrieve(page["id"])
        except APIResponseError as exc:
            if getattr(exc, "status", None) == 404 or getattr(exc, "code", None) == "object_not_found":
                self.logger.warning("Evicting stale cached Notion %s page %s", entity_kind, page["id"])
                self._cache_delete_page(entity_kind, database_id, page["id"], observed=True)
                refs.pop(key, None)
                return None, None
            raise

        if current_page.get("archived"):
            self.logger.warning("Evicting archived cached Notion %s page %s", entity_kind, page["id"])
            self._cache_delete_page(entity_kind, database_id, page["id"], observed=True)
            refs.pop(key, None)
            return None, None

        ref, issue_url = self._page_issue_ref(current_page)
        for existing_key, existing_page in list(refs.items()):
            if existing_page.get("id") == current_page["id"]:
                refs.pop(existing_key, None)

        if not ref:
            self._cache_delete_page(entity_kind, database_id, current_page["id"], observed=True)
            return None, None

        refs[(ref.repo, ref.id)] = current_page
        self._cache_upsert_page(entity_kind, database_id, current_page, ref, issue_url, observed=True)
        return current_page, (ref.repo, ref.id)

    async def _refresh_cached_candidate_pages(self, entity_kind, database_id, refs, candidates):
        if not self._using_notion_cache:
            return candidates

        refreshed_candidates = set(candidates)
        for key in list(candidates):
            page = refs.get(key)
            if not page or not page.get("_twoway_cache_snapshot"):
                continue

            current_page, current_key = await self._retrieve_cached_page(entity_kind, database_id, refs, key, page)
            if current_page is None:
                refreshed_candidates.discard(key)
            elif current_key != key:
                refreshed_candidates.discard(key)
                refreshed_candidates.add(current_key)

        return refreshed_candidates

    def _filter_task_issues_by_repo(self, issues_by_repo):
        task_issues = defaultdict(dict)
        skipped = 0

        for repo, issues in issues_by_repo.items():
            for issue_id, issue in issues.items():
                if self._is_task_issue(issue):
                    task_issues[repo][issue_id] = issue
                else:
                    skipped += 1

        return task_issues

    def _filter_milestone_issues_by_repo(self, issues_by_repo):
        milestone_issues = defaultdict(dict)

        for repo, issues in issues_by_repo.items():
            for issue_id, issue in issues.items():
                if self._is_milestone_issue(issue):
                    milestone_issues[repo][issue_id] = issue

        return milestone_issues

    def _filter_epic_issues_by_repo(self, issues_by_repo):
        epic_issues = defaultdict(dict)

        if not self.epics_db:
            return epic_issues

        for repo, issues in issues_by_repo.items():
            for issue_id, issue in issues.items():
                if self._is_epic_issue(issue):
                    epic_issues[repo][issue_id] = issue

        return epic_issues

    def _filter_task_issues(self, issues):
        return {key: issue for key, issue in issues.items() if self._is_task_issue(issue)}

    async def _discover_unlinked_notion_tasks(self, since):
        pages = []
        issue_filter = {
            "property": self.propnames["notion_issue_field"],
            "files": {"is_empty": True},
        }
        query_filter = issue_filter

        task_team_prop = self.propnames.get("notion_tasks_team")
        if task_team_prop and self.configured_team_ids:
            team_filter = {
                "or": [
                    {"property": task_team_prop, "relation": {"contains": team}} for team in self.configured_team_ids
                ]
            }
            query_filter = {"and": [team_filter, issue_filter]}

        query_func = guard_notion_query_response(
            self.notion.databases.query,
            context=f"Notion database query ({self.tasks_db.database_id})",
        )
        async for page in async_iterate_paginated_api(
            query_func,
            database_id=self.tasks_db.database_id,
            filter=query_filter,
        ):
            if self._get_prop(page, "notion_issue_field", []):
                continue

            if not self.full_sync:
                edited = self._page_timestamp(page)
                if edited is None or edited < since:
                    continue

            status = getnestedattr(
                lambda: self._get_prop(page, "notion_tasks_status")["name"],
                None,
            )
            if self._is_closed_status(status):
                continue

            if task_team_prop and self.configured_team_ids:
                page_teams = set(self._get_relation_ids(page, "notion_tasks_team"))
                if not page_teams.intersection(self.configured_team_ids):
                    continue

            pages.append(page)

        return pages

    async def _discover_notion_tasks_partitioned(self, since):
        linked_repos = defaultdict(dict)
        unlinked_pages = []

        query_filter = None
        task_team_prop = self.propnames.get("notion_tasks_team")
        if task_team_prop and self.configured_team_ids:
            query_filter = {
                "or": [
                    {"property": task_team_prop, "relation": {"contains": team}} for team in self.configured_team_ids
                ]
            }

        query_func = guard_notion_query_response(
            self.notion.databases.query,
            context=f"Notion database query ({self.tasks_db.database_id})",
        )
        async for page in async_iterate_paginated_api(
            query_func,
            database_id=self.tasks_db.database_id,
            filter=query_filter,
        ):
            if task_team_prop and self.configured_team_ids:
                page_teams = set(self._get_relation_ids(page, "notion_tasks_team"))
                if not page_teams.intersection(self.configured_team_ids):
                    continue

            issue_files = self._get_prop(page, "notion_issue_field", []) or []
            if issue_files:
                issue_url = getnestedattr(lambda: issue_files[0]["external"]["url"], None)
                if issue_url:
                    ref = self.tracker.parse_issueref(issue_url)
                    if ref and self.tracker.is_repo_allowed(ref.repo):
                        linked_repos[ref.repo][ref.id] = page
                continue

            if not self.full_sync:
                edited = self._page_timestamp(page)
                if edited is None or edited < since:
                    continue

            status = getnestedattr(
                lambda: self._get_prop(page, "notion_tasks_status")["name"],
                None,
            )
            if self._is_closed_status(status):
                continue

            unlinked_pages.append(page)

        return linked_repos, unlinked_pages

    async def _create_milestone_in_notion_from_tracker(self, tracker_issue):
        notion_data = self._get_milestone_notion_data_from_tracker(tracker_issue)
        self._set_if_prop(
            notion_data,
            "notion_milestones_team",
            self._resolve_tracker_created_milestone_teams(tracker_issue),
        )
        self.logger.info(f"Creating milestone (Tracker->Notion) {tracker_issue.url} - {tracker_issue.title}")
        self.logger.debug("\t" + str(notion_data))
        page = await self.milestones_db.create_page(notion_data)
        if page:
            self._record_milestone_cache_update(page, tracker_issue)
        return page

    async def _create_epic_in_notion_from_tracker(self, tracker_issue):
        notion_data = self._get_epic_notion_data_from_tracker(tracker_issue)
        self._set_if_prop(notion_data, "notion_epics_team", self.configured_team_ids or None)
        page = await self.epics_db.create_page(notion_data)
        if page:
            self._record_epic_cache_update(page, tracker_issue)
        return page

    async def _link_task_page_to_issue(self, page, tracker_issue):
        notion_data = {
            self.propnames["notion_issue_field"]: [
                {"url": tracker_issue.url, "name": self.tracker.format_issueref_short(tracker_issue)}
            ]
        }
        updated_page = await self.tasks_db.update_page(page, notion_data, return_page=True)
        if updated_page:
            page = updated_page
            await self._record_task_cache_update(page, tracker_issue)
        return page

    def _new_stats(self):
        return {
            "tasks_updated_from_tracker": 0,
            "tasks_updated_from_notion": 0,
            "milestones_updated_from_tracker": 0,
            "milestones_updated_from_notion": 0,
            "epics_updated_from_tracker": 0,
            "epics_updated_from_notion": 0,
            "tasks_created_from_tracker": 0,
            "tasks_created_from_notion": 0,
            "milestones_created_from_tracker": 0,
            "epics_created_from_tracker": 0,
            "tasks_create_skipped_no_parent": 0,
            "tasks_create_skipped_closed": 0,
            "tasks_create_skipped_unsupported_path": 0,
            "tasks_create_link_back_retry": 0,
            "milestones_create_skipped_closed": 0,
            "milestones_create_skipped_wrong_type": 0,
            "epics_create_skipped_closed": 0,
            "epics_create_skipped_wrong_type": 0,
        }

    async def _add_tracker_create_candidates(
        self,
        recent_tasks_by_repo,
        recent_milestones_by_repo,
        recent_epics_by_repo,
        notion_task_refs,
        notion_milestone_refs,
        notion_epic_refs,
        task_issues,
        milestone_issues,
        epic_issues,
    ):
        if self.tasks_tracker_to_notion and self.tasks_tracker_to_notion_create:
            for repo, issues in recent_tasks_by_repo.items():
                for issue_id, issue in issues.items():
                    key = (repo, issue_id)
                    if key in notion_task_refs:
                        continue
                    if self._is_task_issue(issue):
                        task_issues[key] = issue

        if self.milestones_tracker_to_notion and self.milestones_tracker_to_notion_create:
            for repo, issues in recent_milestones_by_repo.items():
                for issue_id, issue in issues.items():
                    key = (repo, issue_id)
                    if key in notion_milestone_refs:
                        continue
                    milestone_issues[key] = issue
        elif self.milestones_tracker_to_notion:
            skipped_milestones = [
                (repo, issue_id)
                for repo, issues in recent_milestones_by_repo.items()
                for issue_id in issues
                if (repo, issue_id) not in notion_milestone_refs
            ]
            if skipped_milestones:
                self.logger.info(
                    "Skipping %d tracker->Notion milestone create candidates because milestones_tracker_to_notion_create is disabled",
                    len(skipped_milestones),
                )

        if self.epics_db and self.epics_tracker_to_notion and self.epics_tracker_to_notion_create:
            for repo, issues in recent_epics_by_repo.items():
                for issue_id, issue in issues.items():
                    key = (repo, issue_id)
                    if key in notion_epic_refs:
                        continue
                    epic_issues[key] = issue
        elif self.epics_db and self.epics_tracker_to_notion:
            skipped_epics = [
                (repo, issue_id)
                for repo, issues in recent_epics_by_repo.items()
                for issue_id in issues
                if (repo, issue_id) not in notion_epic_refs
            ]
            if skipped_epics:
                self.logger.info(
                    "Skipping %d tracker->Notion epic create candidates because epics_tracker_to_notion_create is disabled",
                    len(skipped_epics),
                )

    def _candidate_debug(self, entity_kind, issue, page, tracker_to_notion, notion_to_tracker):
        tracker_ts = issue.updated_date or issue.created_date
        if tracker_ts:
            tracker_ts = tracker_ts.replace(second=0, microsecond=0)
        notion_ts = self._page_timestamp(page)
        direction = self._pick_direction(
            entity_kind,
            issue,
            page,
            tracker_to_notion,
            notion_to_tracker,
        )

        if not tracker_to_notion and not notion_to_tracker:
            reason = "No sync direction configured"
        elif not (tracker_to_notion and notion_to_tracker):
            reason = "One-way sync configured"
        elif tracker_ts and notion_ts:
            if tracker_ts > notion_ts:
                reason = "Tracker is more recent"
            elif notion_ts > tracker_ts:
                reason = "Notion is more recent"
            else:
                reason = "Tie break configured"
        elif tracker_ts:
            reason = "Only tracker timestamp available"
        elif notion_ts:
            reason = "Only Notion timestamp available"
        else:
            reason = "No timestamps available"

        action = {
            "tracker_to_notion": "Tracker->Notion",
            "notion_to_tracker": "Notion->Tracker",
        }.get(direction, "No sync direction")

        debug = (
            f"tracker_ts={self._format_timestamp(tracker_ts)} "
            f"notion_ts={self._format_timestamp(notion_ts)} "
            f"- {action} - {reason}"
        )
        return direction, debug

    async def _run_epic_phase(self, epic_issues, notion_epic_refs, stats):
        if not self.epics_db:
            return

        stat_tasks = []
        async with asyncio.TaskGroup() as tg:
            for key, issue in epic_issues.items():
                page = notion_epic_refs.get(key)
                if page is None:
                    if self.epics_tracker_to_notion and self.epics_tracker_to_notion_create:
                        if self._is_epic_issue(issue):
                            if issue.closed_date or self._is_closed_status(issue.state):
                                stats["epics_create_skipped_closed"] += 1
                                continue
                            page = await self._create_epic_in_notion_from_tracker(issue)
                            if not page:
                                continue
                            notion_epic_refs[key] = page
                            self._notion_epic_issues.setdefault(issue.repo, {})[issue.id] = page
                            stats["epics_created_from_tracker"] += 1
                            if "properties" in page:
                                await self.synchronize_single_epic_from_tracker(issue, page)
                        else:
                            stats["epics_create_skipped_wrong_type"] += 1
                    continue

                direction, candidate_debug = self._candidate_debug(
                    "epic",
                    issue,
                    page,
                    self.epics_tracker_to_notion,
                    self.epics_notion_to_tracker,
                )

                if direction == "tracker_to_notion":
                    stat_tasks.append(
                        (
                            "epics_updated_from_tracker",
                            tg.create_task(self.synchronize_single_epic_from_tracker(issue, page, candidate_debug)),
                        )
                    )
                elif direction == "notion_to_tracker":
                    stat_tasks.append(
                        (
                            "epics_updated_from_notion",
                            tg.create_task(self.synchronize_single_epic(issue, page, candidate_debug=candidate_debug)),
                        )
                    )

        for stat_key, task in stat_tasks:
            if task.result():
                stats[stat_key] += 1

    async def _run_milestone_phase(self, milestone_issues, notion_milestone_refs, milestone_page_by_id, stats):
        stat_tasks = []
        async with asyncio.TaskGroup() as tg:
            for key, issue in milestone_issues.items():
                page = notion_milestone_refs.get(key)
                if page is None:
                    if self.milestones_tracker_to_notion and self.milestones_tracker_to_notion_create:
                        if self._is_milestone_issue(issue):
                            if issue.closed_date or self._is_closed_status(issue.state):
                                stats["milestones_create_skipped_closed"] += 1
                                continue
                            page = await self._create_milestone_in_notion_from_tracker(issue)
                            if not page:
                                continue
                            notion_milestone_refs[key] = page
                            self._notion_milestone_issues.setdefault(issue.repo, {})[issue.id] = page
                            milestone_page_by_id[page["id"].replace("-", "")] = (issue.repo, issue.id, page)
                            stats["milestones_created_from_tracker"] += 1
                            if "properties" in page:
                                await self.synchronize_single_milestone_from_tracker(issue, page)
                        else:
                            stats["milestones_create_skipped_wrong_type"] += 1
                    continue

                direction, candidate_debug = self._candidate_debug(
                    "milestone",
                    issue,
                    page,
                    self.milestones_tracker_to_notion,
                    self.milestones_notion_to_tracker,
                )

                if direction == "tracker_to_notion":
                    stat_tasks.append(
                        (
                            "milestones_updated_from_tracker",
                            tg.create_task(
                                self.synchronize_single_milestone_from_tracker(issue, page, candidate_debug)
                            ),
                        )
                    )
                elif direction == "notion_to_tracker":
                    stat_tasks.append(
                        (
                            "milestones_updated_from_notion",
                            tg.create_task(
                                self.synchronize_single_milestone(issue, page, candidate_debug=candidate_debug)
                            ),
                        )
                    )

        for stat_key, task in stat_tasks:
            if task.result():
                stats[stat_key] += 1

    async def _create_tracker_task_from_notion(self, page, milestone_page_by_id, milestone_issues, stats):
        status = getnestedattr(lambda: self._get_prop(page, "notion_tasks_status")["name"], None)
        if self._is_closed_status(status):
            stats["tasks_create_skipped_closed"] += 1
            return

        page_id = page["id"]
        relation = self._get_prop(page, "notion_tasks_milestone_relation", [])
        parent_rel_id = relation[0]["id"].replace("-", "") if relation else None
        parent_info = milestone_page_by_id.get(parent_rel_id)
        if not parent_info:
            stats["tasks_create_skipped_no_parent"] += 1
            return

        milestone_repo, milestone_issue_id, milestone_page = parent_info
        parent_issue = milestone_issues.get((milestone_repo, milestone_issue_id))
        if not parent_issue:
            parent_ref = self.tracker.parse_issueref(self._get_prop(milestone_page, "notion_issue_field", ""))
            if not parent_ref:
                stats["tasks_create_skipped_no_parent"] += 1
                return
            async for fetched_parent in self.tracker.get_issues_by_number([parent_ref], sub_issues=False):
                parent_issue = fetched_parent
                break

        if not parent_issue:
            stats["tasks_create_skipped_no_parent"] += 1
            return

        title = self._get_richtext_prop(page, "notion_tasks_title", "Untitled Task")
        estimate = None
        if self.propnames.get("notion_tasks_estimate"):
            estimate = (self._get_prop(page, "notion_tasks_estimate") or {}).get("name")
        assignees = {
            self.tracker.new_user(notion_user=user["id"]) for user in self._get_prop(page, "notion_tasks_assignee", [])
        }

        created_issue = self._task_create_cache.get(page_id)
        if not created_issue:
            try:
                created_issue = await self.tracker.create_task_issue_from_notion(
                    parent_issue=parent_issue,
                    title=title,
                    description="",
                    assignees=assignees,
                    labels=None,
                    estimate=estimate,
                )
                if created_issue:
                    self._task_create_cache[page_id] = created_issue
                    stats["tasks_created_from_notion"] += 1
                else:
                    self.logger.info(
                        "Skipping dependent Notion link/update for %s because tracker create produced no issue",
                        page.get("url"),
                    )
                    return
            except NotImplementedError as exc:
                stats["tasks_create_skipped_unsupported_path"] += 1
                self.logger.warning(f"Skipping notion->tracker task create for {page.get('url')}: {exc}")
                return

        try:
            page = await self._link_task_page_to_issue(page, created_issue)
        except Exception:
            stats["tasks_create_link_back_retry"] += 1
            self.logger.warning(
                "Created tracker task %s but could not link it back to %s; a later run may create a duplicate",
                created_issue.url,
                page.get("url"),
                exc_info=True,
            )
            return

        direction = self._pick_direction(
            "task",
            created_issue,
            page,
            self.tasks_tracker_to_notion,
            self.tasks_notion_to_tracker,
        )
        if direction == "tracker_to_notion":
            if await self._task_needs_notion_update(created_issue, page):
                await self.synchronize_single_task(created_issue, page)
        elif direction == "notion_to_tracker":
            if self._task_needs_tracker_update(created_issue, page):
                await self.synchronize_single_task_to_tracker(created_issue, page)

    async def _run_task_phase(
        self, since, task_issues, notion_task_refs, milestone_page_by_id, milestone_issues, stats
    ):
        stat_tasks = []
        async with asyncio.TaskGroup() as tg:
            for key, issue in task_issues.items():
                if not self._is_task_issue(issue):
                    self.logger.debug(
                        "Skipping task sync %s#%s because it is not a relevant task",
                        issue.repo,
                        issue.id,
                    )
                    continue

                page = notion_task_refs.get(key)
                if page is None:
                    if self.tasks_tracker_to_notion and self.tasks_tracker_to_notion_create:
                        stat_tasks.append(
                            ("tasks_created_from_tracker", tg.create_task(self.synchronize_single_task(issue, None)))
                        )
                    continue

                direction, candidate_debug = self._candidate_debug(
                    "task",
                    issue,
                    page,
                    self.tasks_tracker_to_notion,
                    self.tasks_notion_to_tracker,
                )
                if direction == "tracker_to_notion":
                    stat_tasks.append(
                        (
                            "tasks_updated_from_tracker",
                            tg.create_task(self.synchronize_single_task(issue, page, candidate_debug=candidate_debug)),
                        )
                    )
                elif direction == "notion_to_tracker":
                    stat_tasks.append(
                        (
                            "tasks_updated_from_notion",
                            tg.create_task(
                                self.synchronize_single_task_to_tracker(issue, page, candidate_debug=candidate_debug)
                            ),
                        )
                    )

            if self.tasks_notion_to_tracker and self.tasks_notion_to_tracker_create:
                unlinked_notion_tasks = self._unlinked_notion_tasks
                for page in unlinked_notion_tasks:
                    tg.create_task(
                        self._create_tracker_task_from_notion(page, milestone_page_by_id, milestone_issues, stats)
                    )

        for stat_key, task in stat_tasks:
            if task.result():
                stats[stat_key] += 1

    def _log_sync_stats(
        self,
        task_linked_count,
        milestone_linked_count,
        epic_linked_count,
        task_skipped,
        milestone_skipped,
        epic_skipped,
        stats,
    ):
        self.logger.info("Two-way sync stats %-22s %8s %10s %10s", "", "tasks", "milestones", "epics")
        self.logger.info(
            "Two-way sync stats %-22s %8d %10d %10d",
            "linked",
            task_linked_count,
            milestone_linked_count,
            epic_linked_count,
        )
        self.logger.info(
            "Two-way sync stats %-22s %8d %10d %10d",
            "skipped",
            task_skipped,
            milestone_skipped,
            epic_skipped,
        )
        self.logger.info(
            "Two-way sync stats %-22s %8d %10d %10d",
            "updated from tracker",
            stats["tasks_updated_from_tracker"],
            stats["milestones_updated_from_tracker"],
            stats["epics_updated_from_tracker"],
        )
        self.logger.info(
            "Two-way sync stats %-22s %8d %10d %10d",
            "updated from notion",
            stats["tasks_updated_from_notion"],
            stats["milestones_updated_from_notion"],
            stats["epics_updated_from_notion"],
        )
        self.logger.info(
            "Two-way sync stats %-22s %8d %10d %10d",
            "created from tracker",
            stats["tasks_created_from_tracker"],
            stats["milestones_created_from_tracker"],
            stats["epics_created_from_tracker"],
        )
        self.logger.info(
            "Two-way sync stats %-22s %8d %10s %10s",
            "created from notion",
            stats["tasks_created_from_notion"],
            "-",
            "-",
        )
        self.logger.info(
            "Two-way sync stats task create skipped no_parent=%5d unsupported=%5d link_back_retry=%5d",
            stats["tasks_create_skipped_no_parent"],
            stats["tasks_create_skipped_unsupported_path"],
            stats["tasks_create_link_back_retry"],
        )
        self.logger.info(
            "Two-way sync stats milestone create skipped closed=%5d wrong_type=%5d",
            stats["milestones_create_skipped_closed"],
            stats["milestones_create_skipped_wrong_type"],
        )
        self.logger.info(
            "Two-way sync stats epic create skipped closed=%5d wrong_type=%5d",
            stats["epics_create_skipped_closed"],
            stats["epics_create_skipped_wrong_type"],
        )

    async def synchronize(self):
        """Run a complete two-way synchronization cycle."""
        timestamp = datetime.datetime.now(datetime.UTC)
        if self.full_sync:
            since = None
            self.logger.info("Two-way sync window full_sync=True")
        else:
            since = (timestamp - datetime.timedelta(seconds=self.incremental_lookback_seconds)).replace(
                second=0,
                microsecond=0,
            )
            self.logger.info(
                "Two-way sync window full_sync=False lookback_seconds=%d since=%s",
                self.incremental_lookback_seconds,
                self._format_timestamp(since),
            )
        self._task_discovery_since = since
        self.logger.debug(
            "Two-way sync directions tasks tracker->notion=%s notion->tracker=%s create tracker->notion=%s notion->tracker=%s",
            self.tasks_tracker_to_notion,
            self.tasks_notion_to_tracker,
            self.tasks_tracker_to_notion_create,
            self.tasks_notion_to_tracker_create,
        )
        self.logger.debug(
            "Two-way sync directions milestones tracker->notion=%s notion->tracker=%s create tracker->notion=%s notion->tracker=%s",
            self.milestones_tracker_to_notion,
            self.milestones_notion_to_tracker,
            self.milestones_tracker_to_notion_create,
            self.milestones_notion_to_tracker_create,
        )
        self.logger.debug(
            "Two-way sync directions epics tracker->notion=%s notion->tracker=%s create tracker->notion=%s notion->tracker=%s",
            self.epics_tracker_to_notion,
            self.epics_notion_to_tracker,
            self.epics_tracker_to_notion_create,
            self.epics_notion_to_tracker_create,
        )

        await self._async_init()

        recent_tasks_by_repo = {}
        recent_milestones_by_repo = {}
        recent_epics_by_repo = {}
        fetch_recent = (
            self.tasks_tracker_to_notion
            or self.tasks_notion_to_tracker
            or self.milestones_tracker_to_notion
            or self.milestones_notion_to_tracker
            or (self.epics_db and self.epics_tracker_to_notion)
            or (self.epics_db and self.epics_notion_to_tracker)
            or self.tasks_tracker_to_notion_create
            or self.milestones_tracker_to_notion_create
            or (self.epics_db and self.epics_tracker_to_notion_create)
        )
        if fetch_recent:
            fetch_since = since if not self.full_sync else datetime.datetime(1970, 1, 1, tzinfo=datetime.UTC)
            recent_issues_by_repo = await self.tracker.get_recent_issues_by_repo(fetch_since, sub_issues=False)
            recent_tasks_by_repo = self._filter_task_issues_by_repo(recent_issues_by_repo)
            recent_milestones_by_repo = self._filter_milestone_issues_by_repo(recent_issues_by_repo)
            recent_epics_by_repo = self._filter_epic_issues_by_repo(recent_issues_by_repo)
        else:
            self.logger.info(
                "Two-way sync not fetching recent tracker issues because all tracker directions are disabled"
            )

        notion_task_refs = {
            (repo, issue_id): page
            for repo, issues in self._notion_tasks_issues.items()
            for issue_id, page in issues.items()
        }
        notion_milestone_refs = {
            (repo, issue_id): page
            for repo, issues in self._notion_milestone_issues.items()
            for issue_id, page in issues.items()
        }
        notion_epic_refs = {
            (repo, issue_id): page
            for repo, issues in self._notion_epic_issues.items()
            for issue_id, page in issues.items()
        }

        recent_task_keys = {(repo, issue_id) for repo, issues in recent_tasks_by_repo.items() for issue_id in issues}
        recent_milestone_keys = {
            (repo, issue_id) for repo, issues in recent_milestones_by_repo.items() for issue_id in issues
        }
        recent_epic_keys = {(repo, issue_id) for repo, issues in recent_epics_by_repo.items() for issue_id in issues}
        recent_tracker_task_count = sum(
            1 for issues in recent_tasks_by_repo.values() for issue in issues.values() if self._is_task_issue(issue)
        )
        recent_tracker_epic_count = sum(
            1 for issues in recent_epics_by_repo.values() for issue in issues.values() if self._is_epic_issue(issue)
        )
        self.logger.info(
            "Two-way sync discovered linked Notion refs tasks=%d milestones=%d epics=%d recent_tracker_refs=%d recent_tracker_tasks=%d recent_tracker_epics=%d",
            len(notion_task_refs),
            len(notion_milestone_refs),
            len(notion_epic_refs),
            len(recent_task_keys),
            recent_tracker_task_count,
            recent_tracker_epic_count,
        )

        task_candidates, task_linked_count, task_skipped = self._collect_candidates(
            notion_task_refs,
            recent_task_keys,
            since,
            self.tasks_tracker_to_notion,
            self.tasks_notion_to_tracker,
        )
        milestone_candidates, milestone_linked_count, milestone_skipped = self._collect_candidates(
            notion_milestone_refs,
            recent_milestone_keys,
            since,
            self.milestones_tracker_to_notion,
            self.milestones_notion_to_tracker,
        )
        epic_candidates, epic_linked_count, epic_skipped = self._collect_candidates(
            notion_epic_refs,
            recent_epic_keys,
            since,
            self.epics_tracker_to_notion,
            self.epics_notion_to_tracker,
        )
        task_candidates = await self._refresh_cached_candidate_pages(
            "task", self.tasks_db.database_id, notion_task_refs, task_candidates
        )
        milestone_candidates = await self._refresh_cached_candidate_pages(
            "milestone", self.milestones_db.database_id, notion_milestone_refs, milestone_candidates
        )
        if self.epics_db:
            epic_candidates = await self._refresh_cached_candidate_pages(
                "epic", self.epics_db.database_id, notion_epic_refs, epic_candidates
            )

        task_issues = await self._load_tracker_candidates(task_candidates, recent_tasks_by_repo)
        task_issues = self._filter_task_issues(task_issues)
        milestone_issues = await self._load_tracker_candidates(milestone_candidates, recent_milestones_by_repo)
        epic_issues = await self._load_tracker_candidates(epic_candidates, recent_epics_by_repo)
        epic_issues = {key: issue for key, issue in epic_issues.items() if self._is_epic_issue(issue)}
        self.logger.info(
            "Two-way sync loaded tracker candidates tasks=%d milestones=%d epics=%d",
            len(task_issues),
            len(milestone_issues),
            len(epic_issues),
        )

        stats = self._new_stats()

        milestone_page_by_id = {
            page["id"].replace("-", ""): (repo, issue_id, page)
            for (repo, issue_id), page in notion_milestone_refs.items()
        }

        await self._add_tracker_create_candidates(
            recent_tasks_by_repo,
            recent_milestones_by_repo,
            recent_epics_by_repo,
            notion_task_refs,
            notion_milestone_refs,
            notion_epic_refs,
            task_issues,
            milestone_issues,
            epic_issues,
        )
        await self._run_epic_phase(epic_issues, notion_epic_refs, stats)
        await self._run_milestone_phase(milestone_issues, notion_milestone_refs, milestone_page_by_id, stats)
        await self._run_task_phase(since, task_issues, notion_task_refs, milestone_page_by_id, milestone_issues, stats)
        self._log_sync_stats(
            task_linked_count,
            milestone_linked_count,
            epic_linked_count,
            task_skipped,
            milestone_skipped,
            epic_skipped,
            stats,
        )
        async with asyncio.TaskGroup() as tg:
            if self.epics_db:
                tg.create_task(self._update_timestamp(self.epics_db, timestamp))
            tg.create_task(self._update_timestamp(self.milestones_db, timestamp))
            tg.create_task(self._update_timestamp(self.tasks_db, timestamp))

        if self._notion_cache:
            self._notion_cache.close()

        await self.notion.aclose()


async def synchronize(**kwargs):  # pragma: no cover
    """Exported method to begin synchronization."""
    await TrackerTwoWaySync(**kwargs).synchronize()
