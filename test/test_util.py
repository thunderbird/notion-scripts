import unittest
from unittest.mock import AsyncMock, patch

import httpx

from mzla_notion.util import AsyncRetryingClient, GitHubHTTPXEndpoint


class AsyncRetryingClientRateLimitTest(unittest.IsolatedAsyncioTestCase):
    async def test_github_graphql_rate_limit_retries_until_reset_header(self):
        calls = 0

        async def handler(request):
            nonlocal calls
            calls += 1
            if calls == 1:
                return httpx.Response(
                    200,
                    headers={
                        "content-type": "application/json",
                        "x-ratelimit-limit": "5000",
                        "x-ratelimit-remaining": "0",
                        "x-ratelimit-reset": "1700000060",
                        "x-ratelimit-resource": "graphql",
                        "x-ratelimit-used": "5000",
                    },
                    json={"errors": [{"message": "API rate limit already exceeded for installation ID #123123"}]},
                )

            return httpx.Response(200, json={"data": {"ok": True}})

        transport = httpx.MockTransport(handler)
        async with AsyncRetryingClient(transport=transport) as client:
            with (
                patch("mzla_notion.util.time.time", return_value=1700000000.2),
                patch("mzla_notion.util.rate_limit_gate.engage", new=AsyncMock()) as engage,
                self.assertLogs("notion_sync", level="INFO") as logs,
            ):
                response = await client.post("https://api.github.com/graphql", json={"query": "{ viewer { login } }"})

        self.assertEqual(response.json(), {"data": {"ok": True}})
        self.assertEqual(calls, 2)
        engage.assert_awaited_once_with(60)
        self.assertIn("retry_source=x-ratelimit-reset", "\n".join(logs.output))
        self.assertIn("reset_at=2023-11-14T22:14:20+00:00", "\n".join(logs.output))

    async def test_http_429_backoff(self):
        for autoraise in (False, True):
            with self.subTest(autoraise=autoraise):
                headers = {}

                async def handler(request):
                    return httpx.Response(429, headers=headers)

                async with AsyncRetryingClient(transport=httpx.MockTransport(handler), autoraise=autoraise) as client:
                    with patch("mzla_notion.util.rate_limit_gate.engage", new=AsyncMock()) as engage:
                        if autoraise:
                            with self.assertRaises(httpx.HTTPStatusError):
                                await client.post("https://phabricator.test/api/user.search")
                        else:
                            response = await client.post("https://phabricator.test/api/user.search")
                            self.assertEqual(response.status_code, 429)
                        self.assertEqual(
                            [call.args[0] for call in engage.await_args_list],
                            [10, 20, 40, 80, 160, 300, 300, 300, 300, 300],
                        )

                        # A new request resets the backoff, even with a smaller retry budget.
                        engage.reset_mock()
                        if autoraise:
                            with self.assertRaises(httpx.HTTPStatusError):
                                await client.send(client.build_request("POST", "https://phabricator.test"), recur=2)
                        else:
                            await client.send(client.build_request("POST", "https://phabricator.test"), recur=2)
                        self.assertEqual([call.args[0] for call in engage.await_args_list], [10, 20])

                        # Server delays longer than the fallback cap must still be honored.
                        headers["Retry-After"] = "600"
                        engage.reset_mock()
                        if autoraise:
                            with self.assertRaises(httpx.HTTPStatusError):
                                await client.send(client.build_request("POST", "https://phabricator.test"), recur=2)
                        else:
                            await client.send(client.build_request("POST", "https://phabricator.test"), recur=2)
                        self.assertEqual([call.args[0] for call in engage.await_args_list], [600, 600])

    async def test_github_403_includes_response_details(self):
        async def handler(request):
            return httpx.Response(
                403,
                headers={"content-type": "text/plain", "x-github-request-id": "ABC123"},
                text="GitHub is temporarily unavailable",
            )

        transport = httpx.MockTransport(handler)
        async with AsyncRetryingClient(transport=transport) as client:
            endpoint = GitHubHTTPXEndpoint("https://api.github.com/graphql", client=client)
            response = await endpoint("query { viewer { login } }")

        self.assertIn("GitHub is temporarily unavailable", response["errors"][0]["message"])
        self.assertIn("x-github-request-id", response["errors"][0]["message"])

    async def test_github_secondary_rate_limit_retries_after_retry_header(self):
        calls = 0

        async def handler(request):
            nonlocal calls
            calls += 1
            if calls == 1:
                return httpx.Response(
                    403,
                    headers={"content-type": "application/json", "retry-after": "60"},
                    json={"message": "You have exceeded a secondary rate limit."},
                )

            return httpx.Response(200, json={"data": {"ok": True}})

        transport = httpx.MockTransport(handler)
        async with AsyncRetryingClient(transport=transport) as client:
            with patch("mzla_notion.util.rate_limit_gate.engage", new=AsyncMock()) as engage:
                response = await client.post("https://api.github.com/graphql", json={"query": "{ viewer { login } }"})

        self.assertEqual(response.json(), {"data": {"ok": True}})
        self.assertEqual(calls, 2)
        engage.assert_awaited_once_with(60)


if __name__ == "__main__":
    unittest.main()
