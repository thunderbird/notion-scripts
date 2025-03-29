# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse
import logging
import os
import sys
import tomllib

from libs.bugzilla_sync import synchronize as synchronize_bugzilla
from libs.gh_label_sync import synchronize as synchronize_gh_label
from libs.gh_project_sync import synchronize as synchronize_gh_project

logger = logging.getLogger("notion_sync")


def list_synchronizers(config):
    """Just list synchronizers."""
    with open(config, "rb") as fp:
        settings = tomllib.load(fp)

    enabled = [key for key, project in settings["sync"].items() if project.get("enabled", True)]
    print("\n".join(enabled))


def main(projects, config, verbose=0, dry_run=False):
    """This is the main cli. Please use --help on how to use it."""
    logging.basicConfig(
        format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    with open(config, "rb") as fp:
        settings = tomllib.load(fp)

    httpx_log_level = [logging.WARNING, logging.INFO, logging.DEBUG][verbose] if verbose <= 3 else logging.DEBUG
    sync_log_level = [logging.INFO, logging.INFO, logging.DEBUG][verbose] if verbose <= 3 else logging.DEBUG

    logging.getLogger("httpx").setLevel(httpx_log_level)
    logging.getLogger("httpcore").setLevel(httpx_log_level)
    logging.getLogger("sgqlc.endpoint.http").setLevel(httpx_log_level)

    logging.getLogger("gh_project_sync").setLevel(sync_log_level)
    logging.getLogger("gh_label_sync").setLevel(sync_log_level)
    logging.getLogger("bugzilla_sync").setLevel(sync_log_level)
    logging.getLogger("notion_sync").setLevel(sync_log_level)

    # This will list the GitHub project ids for you
    # import libs.ghhelper
    # libs.ghhelper.GitHubProjectV2.list("thunderbird", "thunderbird-android")

    # This will give you a list of users and their ids
    # from notion_client import Client
    # from pprint import pprint
    # notion = Client(auth=os.environ["NOTION_TOKEN"])
    # pprint(notion.users.list())

    # This will give you the properties
    # from pprint import pprint
    # notion = Client(auth=os.environ["NOTION_TOKEN"])
    # pprint(notion.databases.retrieve(database_id="DB_ID_HERE"))

    if dry_run:
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

        logger.info(f"Synchronizing project {key}...")

        if project["method"] == "github_project":
            synchronize_gh_project(
                notion_token=os.environ["NOTION_TOKEN"],
                repository_settings=project["repositories"],
                milestones_id=project["notion_milestones_id"],
                tasks_id=project["notion_tasks_id"],
                sprint_id=project.get("notion_sprints_id", None),
                milestones_body_sync=project.get("milestones_body_sync", False),
                milestones_body_sync_if_empty=project.get("milestones_body_sync_if_empty", False),
                tasks_body_sync=project.get("tasks_body_sync", False),
                milestones_github_prefix=project.get("milestones_github_prefix", ""),
                tasks_notion_prefix=project.get("tasks_notion_prefix", ""),
                user_map=settings.get("usermap", {}).get("github", {}),
                property_names=project.get("properties", {}),
                dry=dry_run,
            )
        elif project["method"] == "github_labels":
            synchronize_gh_label(
                notion_token=os.environ["NOTION_TOKEN"],
                repositories=project["repositories"],
                milestones_id=project["notion_milestones_id"],
                tasks_id=project["notion_tasks_id"],
                sync_status=project.get("sync_status", "all"),
                milestone_prefix=project.get("milestone_prefix", "M:"),
                strip_orgname=project.get("strip_orgname", False),
                dry=dry_run,
            )
        elif project["method"] == "bugzilla":
            synchronize_bugzilla(
                notion_token=os.environ["NOTION_TOKEN"],
                bugzilla_api_key=os.environ["BZ_KEY"],
                bugs_id=project["notion_bugs_id"],
                products=project["products"],
                list_id=project.get("list_id", None),
                bugzilla_base_url=project.get("bugzilla_base_url", "https://bugzilla.mozilla.org"),
                bugzilla_limit=project.get("bugzilla_limit", 100),
                dry=dry_run,
            )
        else:
            raise Exception(f"Unknown synchronization {project['type']}")

        logger.info(f"Synchronizing project {key} completed")

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Notion Synchronization for MZLA")
    parser.add_argument(
        "-c",
        "--config",
        default="sync_settings.toml",
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
        "-n",
        "--dry-run",
        action="store_true",
        help="Run the script without making changes",
    )
    parser.add_argument("-l", "--list", action="store_true", help="List synchronizers and exit")
    parser.add_argument(
        "projects",
        nargs="*",
        default=None,
        help="The keys of the projects to synchronize. Defaults to all projects.",
    )

    args = parser.parse_args()

    if args.list:
        list_synchronizers(args.config)
    else:
        sys.exit(main(args.projects, config=args.config, verbose=args.verbose, dry_run=args.dry_run))
