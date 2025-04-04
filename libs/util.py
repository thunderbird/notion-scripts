# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import time
import httpx

logger = logging.getLogger("notion_sync")


class RetryingClient(httpx.Client):
    """A replacement httpx.Client for Notion.

    Handles Notion's rate limiting and request timeouts.
    """

    def send(self, request, *args, recur=10, **kwargs):
        """httpx.Client send that retries."""
        try:
            response = super().send(request, *args, **kwargs)
        except (httpx.TimeoutException, httpx.ConnectError) as e:
            if recur <= 0:
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
    except (LookupError, AttributeError):
        return default
