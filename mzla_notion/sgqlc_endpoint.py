import json
import httpx

from sgqlc.endpoint.base import add_query_to_url
from sgqlc.endpoint.http import HTTPEndpoint
from typing import Optional, Union, Dict


class HTTPXEndpoint(HTTPEndpoint):
    """GraphQL endpoint access via httpx."""

    def __init__(
        self,
        client: Optional[httpx.Client] = None,
        **kwargs,
    ):
        """Initialize the httpx endpoint, optionally with an existing httpx client."""
        super().__init__(**kwargs)
        self.client = client or httpx.AsyncClient()

    def __call__(
        self,
        query: Union[bytes, str],
        variables: Optional[Dict] = None,
        operation_name: Optional[str] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
    ):
        """Calls the GraphQL endpoint."""
        query, req = self._prepare(
            query=query,
            variables=variables,
            operation_name=operation_name,
            extra_headers=extra_headers,
        )

        req.extensions["timeout"] = httpx.Timeout(timeout or self.timeout).as_dict()

        # TODO log http error

        if isinstance(self.client, httpx.AsyncClient):

            async def runner():
                try:
                    response = await self.client.send(req)
                    return self._parse_httpx_response(query, response)
                except httpx.HTTPError as exc:
                    return self._log_http_error(query, req, exc)

            return runner()
        elif isinstance(self.client, httpx.Client):
            try:
                response = self.client.send(req)
                return self._parse_httpx_response(query, response)
            except httpx.HTTPError as exc:
                return self._log_httpx_error(query, req, exc)

    def _parse_httpx_response(self, query, response):
        try:
            data = response.json()
            if data and data.get("errors"):
                return self._log_graphql_error(query, data)
            return data
        except json.JSONDecodeError as exc:
            return self._log_json_error(response.text, exc)

    def _log_httpx_error(self, query, request, exc):
        self.logger.error("%s: %s", request.url, exc)

        return {
            "data": None,
            "errors": [
                {
                    "message": str(exc),
                    "exception": exc,
                }
            ],
        }

    def get_http_post_request(self, query, variables, operation_name, headers):
        """Createa a http POST request for the query."""
        return self.client.build_request(
            method="POST",
            url=self.url,
            headers=headers,
            json={
                "query": query,
                "variables": variables,
                "operationName": operation_name,
            },
        )

    def get_http_get_request(self, query, variables, operation_name, headers):
        """Createa a http GET request for the query."""
        params = {"query": query}
        if operation_name:
            params["operationName"] = operation_name

        if variables:
            params["variables"] = json.dumps(variables)

        url = add_query_to_url(self.url, params)

        return self.client.build_request(method="GET", url=url, headers=headers)
