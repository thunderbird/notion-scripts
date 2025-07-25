# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import time
import httpx
import dataclasses

logger = logging.getLogger("notion_sync")


class RetryingClient(httpx.Client):
    """A replacement httpx.Client for Notion.

    Handles Notion's rate limiting and request timeouts.
    """

    def send(self, request, *args, recur=10, **kwargs):
        """httpx.Client send that retries."""
        try:
            response = super().send(request, *args, **kwargs)
        except (httpx.TimeoutException, httpx.NetworkError, httpx.HTTPStatusError, ConnectionError) as e:
            # Bail if our retry limit has been reached
            if recur <= 0:
                raise

            # 5xx errors we can retry on, 4xx errors we should throw
            if isinstance(e, httpx.HTTPStatusError) and e.response.status_code // 100 != 5:
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
