# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse
import datetime
import logging
import os
import sys
import tomllib

from .sync.label import synchronize as synchronize_gh_label
from .sync.project import synchronize as synchronize_project
from .sync.twoway import synchronize as synchronize_twoway
from .sync.board import synchronize as synchronize_board
from .sync.deployments import synchronize as synchronize_deployments
from .tracker.github import GitHub
from .tracker.bugzilla import Bugzilla
from .people import load_notion_usermap
from .util import GitHubActionsFormatter

logger = logging.getLogger("notion_sync")


def parse_lookback(value, now=None):
    """Parse lookback seconds or an ISO timestamp."""
    try:
        return int(value)
    except ValueError:
        pass

    normalized = value.removesuffix("Z") + "+00:00" if value.endswith("Z") else value
    try:
        timestamp = datetime.datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("lookback must be seconds or an ISO date/time") from exc

    if now is None:
        now = datetime.datetime.now(timestamp.tzinfo)

    lookback_seconds = int((now - timestamp).total_seconds())
    if lookback_seconds < 0:
        raise argparse.ArgumentTypeError("lookback date/time must not be in the future")

    return lookback_seconds


def cmd_list_synchronizers(config):
    """Just list synchronizers."""
    with open(config, "rb") as fp:
        settings = tomllib.load(fp)

    enabled = [key for key, project in settings["sync"].items() if project.get("enabled", True)]
    print("\n".join(enabled))


def cmd_list_repositories(projects, config):
    """Just list repositories."""
    with open(config, "rb") as fp:
        settings = tomllib.load(fp)

    if not projects:
        projects = settings["sync"].keys()

    repos = set()

    for key in projects:
        project = settings["sync"][key]

        if not project.get("enabled", True):
            continue

        repository_settings = project.get("repositories")
        if not repository_settings:
            continue

        if "repositories" in repository_settings:
            repository_settings = {"default": repository_settings}

        for settings in repository_settings.values():
            repos.update(settings["repositories"])

    print("\n".join(repos))


def setup_logging(verbose):
    """Set up debugging based on verbosity level."""
    SYNC_LOGGERS = [
        "project_sync",
        "twoway_sync",
        "base_sync",
        "board_sync",
        "gh_fixups",
        "gh_label_sync",
        "gh_deployments",
        "bugzilla_sync",
        "notion_sync",
        "notion_database",
    ]
    DEFAULT_FORMAT = f"%(levelname)-5s [%(asctime)s] %(name)-{max(len(name) for name in SYNC_LOGGERS)}s - %(message)s"
    HTTPX_LOGGERS = ["httpx", "httpcore", "sgqlc.endpoint.http"]
    logging.basicConfig(
        format=DEFAULT_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    httpx_log_level = (
        [logging.WARNING, logging.INFO, logging.INFO, logging.DEBUG][verbose] if verbose <= 3 else logging.DEBUG
    )
    sync_log_level = [logging.INFO, logging.INFO, logging.DEBUG][verbose] if verbose <= 2 else logging.DEBUG

    actionsHandler = logging.StreamHandler()
    actionsHandler.setFormatter(
        GitHubActionsFormatter(
            fmt=DEFAULT_FORMAT,
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )

    for logger_name in HTTPX_LOGGERS:
        logging.getLogger(logger_name).setLevel(httpx_log_level)

    for logger_name in SYNC_LOGGERS:
        logger = logging.getLogger(logger_name)
        logger.setLevel(sync_log_level)

        if os.environ.get("GITHUB_ACTIONS") == "true":
            logger.addHandler(actionsHandler)
            logger.propagate = False


async def cmd_synchronize(
    projects,
    config,
    verbose=0,
    dry_run=None,
    synchronous=False,
    lookback=None,
    twoway_cache=None,
    twoway_cache_path=None,
    hide_unchanged=False,
):
    """This is the main cli. Please use --help on how to use it."""
    with open(config, "rb") as fp:
        settings = tomllib.load(fp)

    notion_token = os.environ.get("NOTION_TOKEN")
    user_map = await load_notion_usermap(settings, notion_token=notion_token)

    if settings.get("dry", False):
        if dry_run is None or dry_run is True:
            logger.info("Forcing a dry run via configuration, no changes will be made")
            dry_run = True
        elif dry_run is False:
            logger.info("Ignoring dry run from configuration due to --no-dry-run")
            dry_run = False
    elif dry_run:
        logger.info("Doing a dry run, no changes will be made")

    if not projects:
        projects = settings["sync"].keys()

    for key in projects:
        if key not in settings["sync"]:
            logger.error(f"Error: Could not find project {key}")
            return 1

        project = settings["sync"][key]

        if not project.get("enabled", True):
            if verbose > 0:
                logger.warning(f"Skipping project {key} because it is disabled")
            continue

        effective_dry_run = bool(dry_run)
        if project.get("dry", False):
            if not effective_dry_run:
                logger.info(f"Forcing a dry run for project {key} via configuration, no changes will be made")
            effective_dry_run = True

        logger.info(f"Synchronizing project {key}...")

        if project["method"].endswith("_project"):
            if project["method"] == "bugzilla_project":
                tracker = await Bugzilla.create(
                    base_url=project["bugzilla_base"],
                    token=os.environ["BUGZILLA_TOKEN"],
                    phab_token=os.environ["PHAB_TOKEN"],
                    dry=effective_dry_run or project.get("tracker_dry_run", False),
                    user_map=user_map.get("bugzilla") or {},
                    user_teams=user_map.get("teams") or {},
                    phabricator_user_map=user_map.get("phabricator") or {},
                    property_names=project.get("properties", {}),
                )
            elif project["method"] == "github_project":
                tracker = await GitHub.create(
                    token=os.environ["GITHUB_TOKEN"],
                    repositories=project["repositories"],
                    dry=effective_dry_run or project.get("tracker_dry_run", False),
                    user_map=user_map.get("github") or {},
                    user_teams=user_map.get("teams") or {},
                    milestones_issue_type=project.get("milestones_issue_type", None),
                    epics_issue_type=project.get("epics_issue_type", "Epic"),
                    epics_allow_parents=project.get("epics_allow_parents", False),
                    property_names=project.get("properties", {}),
                )

            else:
                raise Exception(f"Unknown synchronization {project['method']}")

            await synchronize_project(
                project_key=key,
                tracker=tracker,
                notion_token=notion_token,
                epics_id=project.get("notion_epics_id"),
                milestones_id=project["notion_milestones_id"],
                tasks_id=project["notion_tasks_id"],
                sprint_id=project.get("notion_sprints_id", None),
                epics_create_from_tracker=project.get("epics_create_from_tracker", False),
                milestones_body_sync=project.get("milestones_body_sync", False),
                milestones_body_sync_if_empty=project.get("milestones_body_sync_if_empty", False),
                milestones_create_from_tracker=project.get("milestones_create_from_tracker", False),
                tasks_body_sync=project.get("tasks_body_sync", False),
                epics_tracker_prefix=project.get("epics_tracker_prefix", ""),
                epics_extra_label=project.get("epics_extra_label", ""),
                epics_issue_type=project.get("epics_issue_type", "Epic"),
                milestones_tracker_prefix=project.get("milestones_tracker_prefix", ""),
                milestones_extra_label=project.get("milestones_extra_label", ""),
                milestones_issue_type=project.get("milestones_issue_type", None),
                tasks_notion_prefix=project.get("tasks_notion_prefix", ""),
                team_id=project.get("notion_team_id"),
                team_association=project.get("notion_associated_team"),
                dry=effective_dry_run,
                synchronous=synchronous,
                hide_unchanged=hide_unchanged,
            )
        elif project["method"] == "tracker_twoway":
            tracker_kind = project.get("tracker")
            if not tracker_kind:
                tracker_kind = "bugzilla" if project.get("bugzilla_base") else "github"

            if tracker_kind == "bugzilla":
                tracker = await Bugzilla.create(
                    base_url=project["bugzilla_base"],
                    token=os.environ["BUGZILLA_TOKEN"],
                    phab_token=os.environ["PHAB_TOKEN"],
                    dry=effective_dry_run or project.get("tracker_dry_run", False),
                    user_map=user_map.get("bugzilla") or {},
                    user_teams=user_map.get("teams") or {},
                    property_names=project.get("properties", {}),
                )
            elif tracker_kind == "github":
                tracker = await GitHub.create(
                    token=os.environ["GITHUB_TOKEN"],
                    repositories=project["repositories"],
                    dry=effective_dry_run or project.get("tracker_dry_run", False),
                    user_map=user_map.get("github") or {},
                    user_teams=user_map.get("teams") or {},
                    milestones_issue_type=project.get("milestones_issue_type", None),
                    epics_issue_type=project.get("epics_issue_type", "Epic"),
                    epics_allow_parents=project.get("epics_allow_parents", False),
                    property_names=project.get("properties", {}),
                )
            else:
                raise Exception(f"Unknown tracker type {tracker_kind}")

            await synchronize_twoway(
                project_key=key,
                tracker=tracker,
                notion_token=os.environ["NOTION_TOKEN"],
                epics_id=project.get("notion_epics_id", None),
                milestones_id=project["notion_milestones_id"],
                tasks_id=project["notion_tasks_id"],
                sprint_id=project.get("notion_sprints_id", None),
                milestones_body_sync=project.get("milestones_body_sync", False),
                milestones_body_sync_if_empty=project.get("milestones_body_sync_if_empty", False),
                tasks_body_sync=project.get("tasks_body_sync", False),
                epics_tracker_prefix=project.get("epics_tracker_prefix", ""),
                epics_extra_label=project.get("epics_extra_label", ""),
                epics_issue_type=project.get("epics_issue_type", "Epic"),
                milestones_tracker_prefix=project.get("milestones_tracker_prefix", ""),
                milestones_extra_label=project.get("milestones_extra_label", ""),
                milestones_issue_type=project.get("milestones_issue_type", None),
                tasks_notion_prefix=project.get("tasks_notion_prefix", ""),
                team_id=project.get("notion_team_id"),
                team_association=project.get("notion_associated_team"),
                dry=effective_dry_run,
                synchronous=synchronous,
                incremental_lookback_seconds=lookback,
                tasks_tracker_to_notion=project.get("tasks_tracker_to_notion", True),
                tasks_notion_to_tracker=project.get("tasks_notion_to_tracker", False),
                milestones_tracker_to_notion=project.get("milestones_tracker_to_notion", False),
                milestones_notion_to_tracker=project.get("milestones_notion_to_tracker", True),
                epics_tracker_to_notion=project.get("epics_tracker_to_notion", False),
                epics_notion_to_tracker=project.get("epics_notion_to_tracker", True),
                tasks_tracker_to_notion_create=project.get("tasks_tracker_to_notion_create", True),
                tasks_notion_to_tracker_create=project.get("tasks_notion_to_tracker_create", False),
                milestones_tracker_to_notion_create=project.get("milestones_tracker_to_notion_create", False),
                milestones_notion_to_tracker_create=project.get("milestones_notion_to_tracker_create", False),
                epics_tracker_to_notion_create=project.get("epics_tracker_to_notion_create", False),
                epics_notion_to_tracker_create=project.get("epics_notion_to_tracker_create", False),
                tasks_conflict_preference=project.get("tasks_conflict_preference", "tracker"),
                milestones_conflict_preference=project.get("milestones_conflict_preference", "notion"),
                epics_conflict_preference=project.get("epics_conflict_preference", "notion"),
                tracker_kind=tracker_kind,
                twoway_cache_enabled=(
                    twoway_cache if twoway_cache is not None else project.get("twoway_cache_enabled", False)
                ),
                twoway_cache_path=twoway_cache_path
                or project.get("twoway_cache_path", ".cache/mzla-notion/twoway.sqlite3"),
                hide_unchanged=hide_unchanged,
            )
        elif project["method"] == "github_labels":
            tracker = await GitHub.create(
                token=os.environ["GITHUB_TOKEN"],
                repositories=project["repositories"],
                dry=effective_dry_run or project.get("tracker_dry_run", False),
                user_map=user_map.get("github") or {},
                user_teams=user_map.get("teams") or {},
                property_names=project.get("properties", {}),
            )
            await synchronize_gh_label(
                project_key=key,
                tracker=tracker,
                notion_token=notion_token,
                milestones_id=project["notion_milestones_id"],
                tasks_id=project["notion_tasks_id"],
                sprint_id=project.get("notion_sprints_id", None),
                milestones_body_sync=project.get("milestones_body_sync", False),
                milestones_body_sync_if_empty=project.get("milestones_body_sync_if_empty", False),
                tasks_body_sync=project.get("tasks_body_sync", False),
                milestones_tracker_prefix=project.get("milestones_tracker_prefix", ""),
                milestones_extra_label=project.get("milestones_extra_label", ""),
                tasks_notion_prefix=project.get("tasks_notion_prefix", ""),
                milestone_label_prefix=project.get("milestone_label_prefix", "M: "),
                team_id=project.get("notion_team_id"),
                team_association=project.get("notion_associated_team"),
                dry=effective_dry_run,
                synchronous=synchronous,
            )
        elif project["method"] == "project_board":
            await synchronize_board(
                project_key=key,
                notion_token=notion_token,
                board_id=project["notion_board_id"],
                properties=project.get("properties", {}),
                dry=effective_dry_run,
                synchronous=synchronous,
            )
        elif project["method"] == "github_deployments":
            await synchronize_deployments(
                project_key=key,
                blocks=project.get("blocks", {}),
                notion_token=notion_token,
                github_token=os.environ["GITHUB_TOKEN"],
                expected_columns=project["expected_columns"],
                stage_column=project["stage_column"],
                prod_column=project["prod_column"],
                dry=effective_dry_run,
            )
        else:
            raise Exception(f"Unknown synchronization {project['method']}")

        logger.info(f"Synchronizing project {key} completed")

    return 0


async def async_main():
    """Main mzla-notion program."""
    parser = argparse.ArgumentParser(description="Notion Synchronization for MZLA")
    parser.add_argument(
        "-c",
        "--config",
        default="config/sync_settings.toml",
        help="Use a different config file, defaults to sync_settings.toml.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Enable verbose logging. Use multiple times for more.",
    )
    parser.add_argument(
        "--synchronous",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Run requests in order, for debugging",
    )
    parser.add_argument(
        "--lookback",
        dest="lookback",
        type=parse_lookback,
        default=None,
        help="Run supported engines incrementally using seconds or an ISO date/time as the lookback window.",
    )
    parser.add_argument(
        "--twoway-cache",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="Enable or disable the SQLite Notion link cache for two-way sync.",
    )
    parser.add_argument(
        "--twoway-cache-path",
        default=None,
        help="Path to the SQLite Notion link cache for two-way sync.",
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="Run the script without making changes",
    )
    parser.add_argument(
        "--hide-unchanged",
        action="store_true",
        help="Suppress unchanged item logs for project and two-way sync.",
    )
    parser.add_argument("-l", "--list", action="store_true", help="List synchronizers and exit")
    parser.add_argument("--repositories", action="store_true", help="List repositories and exit")
    parser.add_argument(
        "projects",
        nargs="*",
        default=None,
        help="The keys of the projects to synchronize. Defaults to all projects.",
    )

    args = parser.parse_args()
    setup_logging(args.verbose)

    if args.repositories:
        cmd_list_repositories(args.projects, args.config)
    elif args.list:
        cmd_list_synchronizers(args.config)
    else:
        sys.exit(
            await cmd_synchronize(
                args.projects,
                config=args.config,
                verbose=args.verbose,
                dry_run=args.dry_run,
                synchronous=args.synchronous,
                lookback=args.lookback,
                twoway_cache=args.twoway_cache,
                twoway_cache_path=args.twoway_cache_path,
                hide_unchanged=args.hide_unchanged,
            )
        )
