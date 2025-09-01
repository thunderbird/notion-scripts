# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import time
import httpx
import dataclasses
import asyncio
import http.client
import random

logger = logging.getLogger("notion_sync")


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
            except (httpx.TransportError, httpx.HTTPStatusError, ConnectionError, http.client.HTTPException) as e:
                # Bail if our retry limit has been reached
                if recur <= 0:
                    raise

                if await self._engage_retry(response, e):
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

    async def _engage_retry(self, response, exception=None):
        if response.status_code == 409:
            seconds = random.randint(10, 20)
            logger.info(f"Sleeping {seconds} seconds due to 409 conflict")
            await rate_limit_gate.engage(seconds)
            return True

        if response.status_code == 429:
            seconds = int(response.headers.get("Retry-After", 10))
            logger.info(f"Sleeping {seconds} seconds due to rate limiting")
            await rate_limit_gate.engage(seconds)
            return True

        if response.status_code // 100 == 5:
            logger.info(f"Sleeping {self.RETRY_TIMEOUT} due to {response.status_code} response")
            await rate_limit_gate.engage(self.RETRY_TIMEOUT)
            return True

        if exception and not isinstance(exception, httpx.HTTPStatusError):
            logger.info(f"Sleeping {self.RETRY_TIMEOUT} due to {type(exception).__name__} ")
            await rate_limit_gate.engage(self.RETRY_TIMEOUT)
            return True

        return False


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
