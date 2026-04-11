import logging
import urllib.parse
import notion_client

from notion_client.helpers import async_iterate_paginated_api

from .util import AsyncRetryingClient
from .util import getnestedattr

logger = logging.getLogger("notion_sync")


def _get_notion_property(page, field_name):
    if not field_name:
        return None
    return getnestedattr(lambda: page["properties"][field_name], None)


def _get_notion_property_value(page, field_name):
    prop = _get_notion_property(page, field_name)
    if not prop:
        return None

    prop_type = prop.get("type")
    if prop_type == "email":
        value = prop.get("email")
    elif prop_type == "url":
        value = prop.get("url")
    elif prop_type in ("rich_text", "title"):
        value = "".join(item.get("plain_text", "") for item in prop.get(prop_type, []))
    else:
        value = prop.get(prop_type)

    if isinstance(value, str):
        value = value.strip()
    return value or None


def _get_notion_people_id(page, field_name):
    prop = _get_notion_property(page, field_name)
    if not prop or prop.get("type") != "people":
        return None

    people = prop.get("people") or []
    if not people:
        return None
    return people[0].get("id")


def _normalize_github_login(profile):
    if not profile:
        return None

    profile = profile.strip()
    if not profile:
        return None
    if profile.startswith("@"):
        profile = profile[1:]

    if profile.startswith("github.com"):
        profile = "https://" + profile

    if profile.startswith("http://") or profile.startswith("https://"):
        parsed = urllib.parse.urlparse(profile)
        if parsed.netloc.casefold() in ("github.com", "www.github.com"):
            path = parsed.path.strip("/")
            if not path:
                return None
            return path.split("/")[0]
        return None

    return profile.split("/")[0]


async def load_notion_usermap(settings, notion_token):
    """Load github/bugzilla/phabricator user maps from the configured `[people]` Notion database."""
    directory_cfg = settings.get("people") or {}
    required_fields = [
        "notion_people_id",
        "notion_people_github",
        "notion_people_email",
        "notion_people_bugzilla",
        "notion_people_phabricator",
        "notion_people_uuid",
    ]
    if not directory_cfg:
        return {}
    if not notion_token:
        logger.warning("NOTION_TOKEN is not set, cannot load [people] user map")
        return {}
    if any(not directory_cfg.get(field) for field in required_fields):
        missing = [field for field in required_fields if not directory_cfg.get(field)]
        logger.warning(f"People directory configuration incomplete, missing {', '.join(missing)}")
        return {}

    notion = notion_client.AsyncClient(auth=notion_token, client=AsyncRetryingClient(http2=True))
    pages = [
        page
        async for page in async_iterate_paginated_api(
            notion.databases.query,
            database_id=directory_cfg["notion_people_id"],
            page_size=100,
        )
    ]
    logger.info(f"Loaded {len(pages)} entries from Notion people directory")

    result = {"github": {}, "bugzilla": {}, "phabricator": {}}

    field_github_profile = directory_cfg["notion_people_github"]
    field_email = directory_cfg["notion_people_email"]
    field_bugzilla_email = directory_cfg["notion_people_bugzilla"]
    field_phabricator = directory_cfg["notion_people_phabricator"]
    field_user_id = directory_cfg["notion_people_uuid"]

    for page in pages:
        notion_user = _get_notion_people_id(page, field_user_id)
        if not notion_user:
            continue

        github_profile = _get_notion_property_value(page, field_github_profile)
        if github_login := _normalize_github_login(github_profile):
            result["github"][github_login] = notion_user

        account_email = _get_notion_property_value(page, field_email)
        bugzilla_email = _get_notion_property_value(page, field_bugzilla_email) or account_email
        if bugzilla_email:
            result["bugzilla"][bugzilla_email] = notion_user

        phabricator_username = _get_notion_property_value(page, field_phabricator)
        if phabricator_username:
            result["phabricator"][phabricator_username] = notion_user

    logger.debug(
        f"GitHub Profiles: {len(result['github'])} "
        f"Bugzilla Profiles: {len(result['bugzilla'])} "
        f"Phabricator Profiles: {len(result['phabricator'])}"
    )

    return result
