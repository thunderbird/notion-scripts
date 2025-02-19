# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import time

from notion_client.errors import APIErrorCode, APIResponseError

logger = logging.getLogger("notion_sync")


def retry_call(func, recur=3):
    """Retry the Notion API call in case it was rate limited after the indicated back-off time."""
    try:
        return func()
    except APIResponseError as error:
        if error.code == APIErrorCode.RateLimited:
            if recur < 0:
                raise error
            else:
                seconds = int(error.response.headers["Retry-After"])
                logger.info(f"Sleeping {seconds} due to rate limiting")
                time.sleep(seconds)
                return retry_call(func, recur - 1)
        else:
            raise error


def getnestedattr(func, default):
    """Oh I wish python supported optional chaining!"""
    try:
        return func()
    except (LookupError, AttributeError):
        return default
