# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import os
import time
import datetime
import email.utils
import httpx
import dataclasses
import asyncio
import http.client
import json
import math
import random
import re
import sgqlc.operation
from urllib.parse import urlsplit

logger = logging.getLogger("notion_sync")

NOTION_PAGE_ID_RE = re.compile(r"(?i)([0-9a-f]{32}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$")


class NotionQueryIncompleteError(RuntimeError):
    """Raised when Notion reports incomplete query results."""


def notion_url_page_key(value, *, preserve_slug=False):
    """Return a stable comparison key for Notion URLs."""
    if value in (None, ""):
        return None
    if not isinstance(value, str):
        return value

    parts = urlsplit(value)
    hostname = (parts.hostname or "").lower()
    if hostname not in {"app.notion.com", "www.notion.so", "notion.so"}:
        return value

    path = (parts.path or "").strip("/")
    if hostname == "app.notion.com" and path.startswith("p/"):
        path = path[2:]

    if preserve_slug:
        return path

    path_end = path.rsplit("/", 1)[-1]
    if match := NOTION_PAGE_ID_RE.search(path_end):
        return match.group(1).replace("-", "").lower()

    return path


def normalize_notion_url(value):
    """Normalize Notion URLs to canonical https://www.notion.so/... form."""
    path = notion_url_page_key(value, preserve_slug=True)
    if path in (None, ""):
        return None
    if path == value and not isinstance(value, str):
        return value

    parts = urlsplit(value)
    hostname = (parts.hostname or "").lower()
    if hostname not in {"app.notion.com", "www.notion.so", "notion.so"}:
        return value

    return f"https://www.notion.so/{path}"


def canonical_notion_url(value):
    """Normalize Notion URLs to canonical https://app.notion.com/p/... form."""
    path = notion_url_page_key(value, preserve_slug=True)
    if path in (None, ""):
        return None
    if path == value and not isinstance(value, str):
        return value

    parts = urlsplit(value)
    hostname = (parts.hostname or "").lower()
    if hostname not in {"app.notion.com", "www.notion.so", "notion.so"}:
        return value

    return f"https://app.notion.com/p/{path}"


def notion_url_equal(left, right):
    """Return whether two values refer to the same Notion URL."""
    left_key = notion_url_page_key(left)
    right_key = notion_url_page_key(right)
    return left_key == right_key


def check_notion_request_status(response, context="Notion query", query_kwargs=None):
    """Raise when Notion reports incomplete query results."""
    request_status = response.get("request_status") if isinstance(response, dict) else None
    if not request_status:
        return

    if request_status.get("type") != "incomplete":
        return

    incomplete_reason = request_status.get("incomplete_reason", "unknown")
    query_kwargs = query_kwargs if isinstance(query_kwargs, dict) else {}
    query_filter = query_kwargs.get("filter")
    query_debug_context = {
        "database_id": query_kwargs.get("database_id"),
        "page_size": query_kwargs.get("page_size"),
        "start_cursor": query_kwargs.get("start_cursor"),
        "filter": query_filter,
    }

    logger.debug("%s returned incomplete request_status. Query context: %s", context, query_debug_context)

    if incomplete_reason == "query_result_limit_reached":
        details = f" filter={query_filter!r}" if query_filter is not None else ""
        raise NotionQueryIncompleteError(
            f"{context} returned incomplete results (query_result_limit_reached). "
            f"Narrow the query or switch to incremental sync.{details}"
        )

    raise NotionQueryIncompleteError(f"{context} returned incomplete results ({incomplete_reason}).")


def guard_notion_query_response(query_func, context="Notion query"):
    """Wrap a Notion query function and validate request_status on responses."""

    async def wrapped_query(*args, **kwargs):
        response = await query_func(*args, **kwargs)
        check_notion_request_status(response, context=context, query_kwargs=kwargs)
        return response

    return wrapped_query


class RetryingClient(httpx.Client):
    """A replacement httpx.Client for Notion.

    Handles Notion's rate limiting and request timeouts.
    """

    def __init__(self, autoraise=False, **kwargs):
        """Initialize client. autoraise is useful if not used for NotionClient."""
        self.autoraise = autoraise
        super().__init__(**kwargs)

    def send(self, request, *args, recur=10, **kwargs):
        """httpx.Client send that retries."""
        try:
            response = super().send(request, *args, **kwargs)
            if self.autoraise:
                response.raise_for_status()
        except (httpx.TransportError, httpx.HTTPStatusError, ConnectionError, http.client.HTTPException) as e:
            # Bail if our retry limit has been reached
            if recur <= 0:
                raise

            # 5xx errors we can retry on, 4xx errors we should throw, 409 we can retry on
            if (
                isinstance(e, httpx.HTTPStatusError)
                and e.response.status_code // 100 != 5
                and e.response.status_code != 409
            ):
                raise

            logger.info("Sleeping 10 seconds due to " + type(e).__name__)
            time.sleep(10)
            return self.send(request, *args, recur=recur - 1, **kwargs)

        if response.status_code == 429 and recur > 0:
            seconds = int(response.headers.get("Retry-After", 10))
            logger.info(f"Sleeping {seconds} seconds due to rate limiting")
            time.sleep(seconds)
            return self.send(request, *args, recur=recur - 1, **kwargs)

        return response


class RateLimitGate:
    """Cooperative async gate that can be closed."""

    def __init__(self):
        """Create the gate."""
        self._event = asyncio.Event()
        self._event.set()
        self._until = 0.0
        self._lock = asyncio.Lock()

    def is_limited(self) -> bool:
        """Check if the gate is closed."""
        return not self._event.is_set()

    async def wait_open(self) -> None:
        """Wait until the gate opens."""
        waited = False
        while True:
            if self._event.is_set():
                await asyncio.sleep(0)
                if self._event.is_set():
                    break
            await self._event.wait()
            waited = True

        if waited:
            # Make sure not all requests are released at once
            await asyncio.sleep(random.randint(1, 10))

    async def engage(self, seconds):
        """Close the gate once and schedule reopen."""
        now = time.monotonic()
        async with self._lock:
            if now >= self._until:
                self._until = now + max(0.0, seconds)
                self._event.clear()
                logger.info(f"Rate limit engaged for {seconds} seconds")

                async def _unlock():
                    await asyncio.sleep(max(0.0, self._until - time.monotonic()))
                    self._event.set()
                    logger.info("Rate limit released")

                asyncio.create_task(_unlock())


# Shared instance. Theoretically this should be per-host
rate_limit_gate = RateLimitGate()


class AsyncRetryingClient(httpx.AsyncClient):
    """A replacement httpx.Client for Notion.

    Handles Notion's rate limiting and request timeouts.
    """

    MAX_RETRY = 10
    RETRY_TIMEOUT = 10

    def __init__(self, autoraise=False, **kwargs):
        """Initialize client. autoraise is useful if not used for NotionClient."""
        self.autoraise = autoraise
        super().__init__(**kwargs)

    async def send(self, request, *args, recur=None, **kwargs):
        """httpx.AsyncClient send that retries."""
        if recur is None:
            recur = self.MAX_RETRY

        while True:
            await rate_limit_gate.wait_open()

            try:
                response = await super().send(request, *args, **kwargs)
                if self.autoraise:
                    response.raise_for_status()
            except (
                httpx.TransportError,
                httpx.HTTPStatusError,
                ConnectionError,
                http.client.HTTPException,
                sgqlc.operation.GraphQLErrors,
            ) as e:
                # Bail if our retry limit has been reached
                if recur <= 0:
                    raise

                if await self._engage_retry(exception=e):
                    # We've engaged the rate limit and need to retry
                    recur -= 1
                    continue
                else:
                    # Some other error we should throw
                    raise

            # If we're not autoraising, then 4xx/5xx responses won't cause an exception. Handle just
            # the responses here.
            if not self.autoraise and recur > 0 and await self._engage_retry(response):
                recur -= 1
                continue

            return response

    async def _engage_retry(self, response=None, exception=None):
        if not response and exception:
            response = getattr(exception, "response", None)

        if response and response.status_code == 409:
            seconds = random.randint(10, 20)
            logger.info(f"Sleeping {seconds} seconds due to 409 conflict")
            await rate_limit_gate.engage(seconds)
            return True

        if response and response.status_code == 429:
            seconds, retry_source = self._rate_limit_sleep_seconds(response.headers, default=10)
            self._log_rate_limit_sleep(seconds, "HTTP 429 rate limit", retry_source, response.headers)
            await rate_limit_gate.engage(seconds)
            return True

        if response and (error := self._response_graphql_rate_limit_error(response)):
            seconds, retry_source = self._rate_limit_sleep_seconds(response.headers, default=60)
            self._log_rate_limit_sleep(seconds, "GitHub GraphQL rate limit", retry_source, response.headers, error)
            await rate_limit_gate.engage(seconds)
            return True

        if response and response.status_code // 100 == 5:
            logger.info(f"Sleeping {self.RETRY_TIMEOUT} seconds due to {response.status_code} response")
            await rate_limit_gate.engage(self.RETRY_TIMEOUT)
            return True

        if exception and isinstance(exception, sgqlc.operation.GraphQLErrors):
            for error in exception.errors:
                if (error.get("status") or 0) // 100 == 5:
                    logger.info(f"Sleeping {self.RETRY_TIMEOUT} seconds due to {error.get('status')} response")
                    await rate_limit_gate.engage(self.RETRY_TIMEOUT)
                    return True
                if "API rate limit already exceeded" in error.get("message", ""):
                    headers = error.get("headers") or (response.headers if response else {})
                    seconds, retry_source = self._rate_limit_sleep_seconds(headers, default=60)
                    self._log_rate_limit_sleep(seconds, "GraphQL rate limit", retry_source, headers, error)
                    await rate_limit_gate.engage(seconds)
                    return True

        if exception and not isinstance(exception, httpx.HTTPStatusError):
            logger.info(f"Sleeping {self.RETRY_TIMEOUT} due to {type(exception).__name__} ")
            await rate_limit_gate.engage(self.RETRY_TIMEOUT)
            return True

        return False

    @staticmethod
    def _header_value(headers, name):
        """Return a header value from either httpx.Headers or a plain dict."""
        if not headers:
            return None

        try:
            value = headers.get(name)
            if value is not None:
                return value
        except AttributeError:
            pass

        lower_name = name.lower()
        for key, value in headers.items():
            if key.lower() == lower_name:
                return value

        return None

    @classmethod
    def _parse_retry_after(cls, headers, now):
        retry_after = cls._header_value(headers, "retry-after")
        if retry_after is None:
            return None

        try:
            return max(0, int(retry_after))
        except ValueError:
            try:
                retry_at = email.utils.parsedate_to_datetime(retry_after)
            except (TypeError, ValueError):
                logger.debug("Ignoring invalid retry-after header: %s", retry_after)
                return None
            if retry_at.tzinfo is None:
                retry_at = retry_at.replace(tzinfo=datetime.timezone.utc)
            return max(0, math.ceil(retry_at.timestamp() - now))

    @classmethod
    def _rate_limit_sleep_seconds(cls, headers, default=60, now=None):
        """Calculate how long to sleep from rate-limit headers."""
        now = time.time() if now is None else now
        if (seconds := cls._parse_retry_after(headers, now)) is not None:
            return seconds, "retry-after"

        reset = cls._header_value(headers, "x-ratelimit-reset")
        if reset:
            try:
                return max(0, math.ceil(int(reset) - now)), "x-ratelimit-reset"
            except ValueError:
                logger.debug("Ignoring invalid x-ratelimit-reset header: %s", reset)

        return default, "default"

    @classmethod
    def _response_graphql_rate_limit_error(cls, response):
        content_type = response.headers.get("content-type", "")
        if "json" not in content_type:
            return None

        try:
            data = response.json()
        except json.JSONDecodeError:
            return None

        for error in data.get("errors", []) if isinstance(data, dict) else []:
            message = error.get("message", "")
            if "API rate limit already exceeded" in message:
                return error

        return None

    @classmethod
    def _log_rate_limit_sleep(cls, seconds, reason, retry_source, headers, error=None):
        reset = cls._header_value(headers, "x-ratelimit-reset")
        reset_at = None
        if reset:
            try:
                reset_at = datetime.datetime.fromtimestamp(int(reset), datetime.UTC).isoformat()
            except ValueError:
                reset_at = f"invalid:{reset}"

        logger.info(
            "Sleeping %s seconds due to %s (retry_source=%s, reset_at=%s, limit=%s, remaining=%s, used=%s, resource=%s, retry_after=%s)",
            seconds,
            reason,
            retry_source,
            reset_at,
            cls._header_value(headers, "x-ratelimit-limit"),
            cls._header_value(headers, "x-ratelimit-remaining"),
            cls._header_value(headers, "x-ratelimit-used"),
            cls._header_value(headers, "x-ratelimit-resource"),
            cls._header_value(headers, "retry-after"),
        )
        if error:
            logger.debug("Rate-limit GraphQL error: %s", error.get("message"))


class GitHubActionsFormatter(logging.Formatter):
    """logging formatter to bubble up warnings and errors to github actions."""

    def format(self, record):
        """Format the record for GitHub actions."""
        file_name = os.path.basename(record.pathname)
        message = super().format(record)

        if record.levelno == logging.WARNING:
            return f"::warning file={file_name},line={record.lineno},title={record.name}::{message}"
        elif record.levelno == logging.ERROR:
            return f"::error file={file_name},line={record.lineno},title={record.name}::{message}"

        return message


def getnestedattr(func, default):
    """Oh I wish python supported optional chaining!"""
    try:
        return func()
    except (LookupError, AttributeError, TypeError):
        return default


def diff_dataclasses(a, b, log=None):
    """Compare two dataclasses."""
    if type(a) is not type(b):
        raise TypeError("Both objects must be of the same dataclass type")

    differences = {}
    for field in dataclasses.fields(a):
        value_a = getattr(a, field.name)
        value_b = getattr(b, field.name)
        if value_a != value_b:
            if log:
                log(f"\t{field.name}: {value_a} != {value_b}")
            differences[field.name] = (value_a, value_b)
    return differences


def strip_orgname(repos):
    """Strip the org prefix if it is the same across all items."""
    firstprefix, _ = repos[0].split("/", 1) if repos else (None, None)
    stripped = [parts[1] for repo in repos if (parts := repo.split("/", 1)) and parts[0] == firstprefix]
    return stripped if len(stripped) == len(repos) else repos


def from_isoformat(value):
    """Reads the string from iso format, either as a date or datetime."""
    try:
        return datetime.date.fromisoformat(value)
    except ValueError:
        return datetime.datetime.fromisoformat(value)


def ensure_datetime(value):
    """Return a datetime by filling utc midnight for dates."""
    if value is None:
        return None
    if isinstance(value, datetime.datetime):
        return value
    if isinstance(value, datetime.date):
        return datetime.datetime(value.year, value.month, value.day, tzinfo=datetime.timezone.utc)
    raise TypeError(f"Expected date or datetime, got {type(value)}")


def ensure_date(value):
    """Ensure the passed value is a date."""
    if value is None:
        return None
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    raise TypeError(f"Expected date or datetime, got {type(value)}")
