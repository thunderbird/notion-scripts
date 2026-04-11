#!/usr/bin/env python3
"""Debug helpers for GitHub integrations."""

import argparse
import asyncio

from mzla_notion.tracker.github import GitHubProjectV2


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_project = subparsers.add_parser("project", help="Show GitHub project properties")
    parser_project.add_argument("orgrepo", help="Repository in the format <org>/<repo>")

    return parser.parse_args()


async def async_main():
    args = parse_args()

    if args.command == "project":
        org, repo = args.orgrepo.split("/", 1)
        await GitHubProjectV2.list(org, repo)

    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(async_main()))
