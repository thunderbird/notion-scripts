#!/usr/bin/env python3
"""Debug helpers for Notion data and user mappings."""

import argparse
import asyncio
import logging
import os
import tomllib

from pprint import pprint

import notion_client

from mzla_notion.people import load_notion_usermap
from mzla_notion.tracker.bugzilla import PhabClient

EMAIL_PROPERTY = "Email"
PERSON_PROPERTY = "Person"


def cmd_users():
    """Show Notion users with email, id, and display name."""
    notion = notion_client.Client(auth=os.environ["NOTION_TOKEN"])
    users = notion.users.list()

    for user in users["results"]:
        email = (user.get("person") or {}).get("email", "")
        print(f'{email} = "{user["id"]}" # {user["name"]}')


def cmd_db(dbid):
    """Show a debug view of a database, page, or block."""
    notion = notion_client.Client(auth=os.environ["NOTION_TOKEN"])

    try:
        database_info = notion.databases.retrieve(database_id=dbid)
        print("Database Information:")
        pprint(database_info)
    except notion_client.errors.APIResponseError:
        try:
            page_info = notion.pages.retrieve(dbid)
            child_info = notion.blocks.children.list(block_id=dbid)
            print("Page Information:")
            pprint(page_info)
            print("\nChild blocks:")
            pprint(child_info)
        except notion_client.errors.APIResponseError:
            block_info = notion.blocks.retrieve(block_id=dbid)
            child_info = notion.blocks.children.list(block_id=dbid)
            print("Block Information:")
            pprint(block_info)
            print("\nChild blocks:")
            pprint(child_info)


def _print_table(headers, rows):
    widths = [len(header) for header in headers]
    for row in rows:
        for idx, cell in enumerate(row):
            widths[idx] = max(widths[idx], len(cell))

    def _format_row(row):
        return " | ".join(cell.ljust(widths[idx]) for idx, cell in enumerate(row))

    print(_format_row(headers))
    print(" | ".join("-" * width for width in widths))
    for row in rows:
        print(_format_row(row))


def build_usermap_table_rows(user_map, phabricator_phids=None):
    """Create aggregate user map data for later display."""

    def _reverse_user_map(mapping):
        result = {}
        for tracker_user, notion_user in (mapping or {}).items():
            result.setdefault(notion_user, []).append(tracker_user)
        return {key: sorted(values, key=str.casefold) for key, values in result.items()}

    phabricator_phids = phabricator_phids or {}
    github_map = _reverse_user_map(user_map.get("github"))
    bugzilla_map = _reverse_user_map(user_map.get("bugzilla"))
    phabricator_map = _reverse_user_map(user_map.get("phabricator"))
    notion_ids = sorted(set(github_map.keys()) | set(bugzilla_map.keys()) | set(phabricator_map.keys()))

    rows = []
    for notion_user_id in notion_ids:
        phabricator_usernames = phabricator_map.get(notion_user_id, [])
        rows.append(
            [
                notion_user_id,
                ", ".join(github_map.get(notion_user_id, [])),
                ", ".join(bugzilla_map.get(notion_user_id, [])),
                ", ".join(
                    phabricator_phids[username] for username in phabricator_usernames if phabricator_phids.get(username)
                ),
                ", ".join(phabricator_usernames),
            ]
        )

    return rows


def configure_logging(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def normalize_email(value):
    if not value:
        return None
    normalized = value.strip().lower()
    return normalized or None


def extract_title_value(page, prop_name):
    prop = page.get("properties", {}).get(prop_name, {})
    if prop.get("type") != "title":
        return None
    chunks = prop.get("title", [])
    return "".join(chunk.get("plain_text", "") for chunk in chunks) or None


def list_all_users(notion):
    users = []
    start_cursor = None

    while True:
        kwargs = {"page_size": 100}
        if start_cursor:
            kwargs["start_cursor"] = start_cursor

        response = notion.users.list(**kwargs)
        users.extend(response.get("results", []))

        if not response.get("has_more"):
            break
        start_cursor = response.get("next_cursor")

    return users


def list_existing_user_emails(notion, database_id):
    existing = set()
    start_cursor = None

    while True:
        kwargs = {"database_id": database_id, "page_size": 100}
        if start_cursor:
            kwargs["start_cursor"] = start_cursor

        response = notion.databases.query(**kwargs)
        for page in response.get("results", []):
            email = normalize_email(extract_title_value(page, EMAIL_PROPERTY))
            if email:
                existing.add(email)

        if not response.get("has_more"):
            break
        start_cursor = response.get("next_cursor")

    return existing


def create_target_page(notion, database_id, properties):
    return notion.pages.create(parent={"database_id": database_id}, properties=properties)


def cmd_usersync(config, dry_run=False, verbose=False):
    """Fill a user directory database from the Notion workspace users list."""
    configure_logging(verbose)

    with open(config, "rb") as fp:
        settings = tomllib.load(fp)
    people_cfg = settings.get("people") or {}
    database_id = people_cfg.get("notion_people_id")
    if not database_id:
        raise RuntimeError(f"No people.notion_people_id configured in {config}")

    notion_token = os.environ.get("NOTION_TOKEN")
    if not notion_token:
        raise RuntimeError("NOTION_TOKEN environment variable is required")

    notion = notion_client.Client(auth=notion_token)

    users = list_all_users(notion)
    logging.info("Found %d Notion users", len(users))

    existing_emails = list_existing_user_emails(notion, database_id)
    logging.info("Found %d existing rows in target database", len(existing_emails))

    created = 0
    skipped_existing = 0
    skipped_non_person_or_no_email = 0

    for user in users:
        user_id = user.get("id", "")
        user_name = user.get("name") or "(no name)"
        user_type = user.get("type")
        email = normalize_email((user.get("person") or {}).get("email"))

        logging.info("User: %s type=%s <%s> (%s)", user_name, user_type, email or "no-email", user_id)

        if user_type != "person" or not email:
            skipped_non_person_or_no_email += 1
            continue

        if email in existing_emails:
            skipped_existing += 1
            continue

        props = {
            EMAIL_PROPERTY: {
                "type": "title",
                "title": [{"type": "text", "text": {"content": email}}],
            },
            PERSON_PROPERTY: {
                "type": "people",
                "people": [{"object": "user", "id": user_id}],
            },
        }

        if dry_run:
            logging.info("[dry-run] Would create row for %s (%s)", email, user_name)
        else:
            create_target_page(notion, database_id, props)
            logging.info("Created row for %s (%s)", email, user_name)

        existing_emails.add(email)
        created += 1

    logging.info(
        "Done. Created=%d SkippedExisting=%d SkippedNonPersonOrNoEmail=%d",
        created,
        skipped_existing,
        skipped_non_person_or_no_email,
    )


async def cmd_usermap(config):
    """Show a table with notion-to-tracker user mappings."""
    with open(config, "rb") as fp:
        settings = tomllib.load(fp)

    user_map = await load_notion_usermap(settings, notion_token=os.environ.get("NOTION_TOKEN"))

    phabricator_map = user_map.get("phabricator") or {}
    phabricator_phids = {}
    if phabricator_map and os.environ.get("PHAB_TOKEN"):
        phab_client = PhabClient(
            base_url="https://phabricator.services.mozilla.com/api/",
            phab_token=os.environ["PHAB_TOKEN"],
            http2=True,
            autoraise=True,
        )
        phabricator_phids = await phab_client.get_user_phids_by_username(phabricator_map.keys())

    headers = [
        "notion user id",
        "github tracker user id",
        "bugzilla tracker user id",
        "phabricator PHID",
        "phabricator userName",
    ]
    rows = build_usermap_table_rows(user_map, phabricator_phids=phabricator_phids)
    _print_table(headers, rows)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("users", help="Show users with their id")

    parser_db = subparsers.add_parser("db", help="Show debug database/page/block view")
    parser_db.add_argument("dbid", help="Notion database/page/block id")

    parser_usermap = subparsers.add_parser("usermap", help="Show user mapping table")
    parser_usermap.add_argument(
        "-c",
        "--config",
        default="config/sync_settings.toml",
        help="Use a different config file, defaults to sync_settings.toml.",
    )

    parser_usersync = subparsers.add_parser("usersync", help="Populate a Notion users directory database")
    parser_usersync.add_argument(
        "-c",
        "--config",
        default="config/sync_settings.toml",
        help="Use a different config file, defaults to sync_settings.toml.",
    )
    parser_usersync.add_argument(
        "--dry-run",
        action="store_true",
        help="Print intended page creations without writing.",
    )
    parser_usersync.add_argument("--verbose", action="store_true")

    return parser.parse_args()


async def async_main():
    args = parse_args()

    if args.command == "users":
        cmd_users()
    elif args.command == "db":
        cmd_db(args.dbid)
    elif args.command == "usermap":
        await cmd_usermap(args.config)
    elif args.command == "usersync":
        cmd_usersync(args.config, dry_run=args.dry_run, verbose=args.verbose)

    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(async_main()))
