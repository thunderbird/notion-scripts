import sys
import os
import logging
import unittest
import respx
import httpx
import json
import urllib.parse
import uuid


from pathlib import Path
from unittest.mock import MagicMock, patch
from collections import defaultdict
from contextlib import contextmanager


def load_fixture(name):
    with open(Path(__file__).parent / "fixtures" / name, "r") as fp:
        return json.load(fp)


def load_directory(path):
    basepath = Path(__file__).parent / "fixtures" / path
    for filename in os.listdir(basepath):
        if filename.endswith(".json"):
            with open(basepath / filename, "r") as fp:
                yield filename, json.load(fp)


class BaseTestCase(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        if "-v" in sys.argv:
            sync_log_level = logging.DEBUG
            handler = logging.StreamHandler(sys.stderr)

            for logName in ("project_sync", "gh_label_sync", "bugzilla_sync", "notion_sync", "notion_database"):
                logger = logging.getLogger(logName)
                logger.setLevel(sync_log_level)
                logger.addHandler(handler)
                logger.propagate = False
        else:
            logging.getLogger("sgqlc.endpoint.http").setLevel(logging.CRITICAL)

        self._configure_mock_urlopen()

        self.respx = respx.mock(assert_all_called=False)
        self.maxDiff = None
        self.respx.start()

        self.reset_handlers()

    def reset_handlers(self):
        self.respx.reset()
        self.bugzilla_handler = BugzillaHandler(self.respx)
        self.notion_handler = NotionHandler(self.respx)
        self.github_handler = GitHubHandler()

    def tearDown(self):
        not_called = [route for route in self.respx.routes if not route.called]
        if not_called and self.respx._assert_all_called:
            print("NOT CALLED", not_called)
        self.respx.stop()

    @contextmanager
    def assertRaisesInGroup(self, expected_type, msg_part):
        with self.assertRaises(ExceptionGroup) as cm:
            yield

        subgroup = cm.exception.subgroup(expected_type)
        self.assertIsNotNone(subgroup, f"{expected_type} not found in exception group")
        matches = [e for e in subgroup.exceptions if msg_part in str(e)]
        self.assertTrue(matches, f"No {expected_type.__name__} contained message '{msg_part}'")

    def _configure_mock_urlopen(self):
        def side_effect(request, *args, **kwargs):
            url = request.full_url if hasattr(request, "full_url") else request

            urldata = urllib.parse.urlparse(url)
            if urldata.netloc == "api.github.com" and urldata.path == "/graphql":
                result = self.github_handler.handle(request)

            if isinstance(result, Exception):
                raise result
            elif result:
                mock_response = MagicMock()
                mock_response.__enter__.return_value = mock_response
                mock_response.read.return_value = result
                mock_response.headers = {}
                return mock_response
            else:
                raise RuntimeError(f"Unhandled endpoint {url}")

        patcher = patch("urllib.request.urlopen")
        self.addCleanup(patcher.stop)
        mock_urlopen = patcher.start()
        mock_urlopen.side_effect = side_effect


class BugzillaHandler:
    bugs = {}

    def __init__(self, respx_mock):
        self.bugs = {str(bug["id"]): bug for _, bug in load_directory("bugzilla")}
        self.users = {"staff@example.com": {"real_name": "Staff user", "name": "staff@example.com"}}

        BUGID_PATTERN = r"^/rest/bug/(?P<bugid>\d+)$"

        respx_mock.route(name="bugs_get", method="GET", url="https://bugzilla.dev/rest/bug").mock(
            side_effect=self.query_handler
        )
        respx_mock.route(
            name="bugs_update", method="PUT", scheme="https", host="bugzilla.dev", path__regex=BUGID_PATTERN
        ).mock(side_effect=self.update_handler)

        respx_mock.route(name="users", method="GET", scheme="https", host="bugzilla.dev", path="/rest/user").mock(
            side_effect=self.user_handler
        )

    def user_handler(self, req):
        name = req.url.params["names"]
        if name in self.users:
            return httpx.Response(200, json=self.users[name])
        else:
            return httpx.Response(404)

    def update_handler(self, req, bugid=None):
        self.bugs[bugid] = self.bugs.get(bugid) | json.loads(req.content)
        return httpx.Response(200, json=self.bugs[bugid])

    def query_handler(self, req):
        qs = urllib.parse.parse_qs(req.url.query)
        bugs = {
            "bugs": [
                bugdata
                for bugid in qs[b"id"][0].split(b",")
                if (bugdata := self.bugs.get(bugid.decode("utf-8"))) is not None
            ]
        }
        return httpx.Response(200, json=bugs)


class NotionDatabaseHandler:
    pages = []

    def __init__(self, database):
        data = load_fixture(f"notion_{database}.json")
        self.database_info = data["dbinfo"]
        self.pages = data["pages"]

    def get_page(self, pageid):
        return next((page for page in self.pages if page["id"] == pageid), None)

    def query_handler(self, req):
        return {"results": self.pages, "has_more": False, "next_cursor": None}

    def update_handler(self, req):
        data = json.loads(req.content)

        if "description" in data:
            self.database_info["description"] = data["description"]

        return self.database_info

    def create_handler(self, reqjson):
        self.pages.append(reqjson)
        reqjson["id"] = str(uuid.uuid4())
        reqjson["url"] = "https://notion.so/example/" + reqjson["id"]

        for prop in reqjson["properties"].values():
            if len(prop) == 1:
                prop["type"] = next(iter(prop))

            if prop["type"] in ("rich_text", "text", "title"):
                for text_prop in prop[prop["type"]]:
                    if "plain_text" not in text_prop:
                        text_prop["plain_text"] = text_prop["text"]["content"]

        return reqjson


class NotionHandler:
    def __init__(self, respx_mock):
        self.milestones_handler = NotionDatabaseHandler("milestones_id")
        self.tasks_handler = NotionDatabaseHandler("tasks_id")
        self.sprints_handler = NotionDatabaseHandler("sprints_id")

        self.blocks = load_fixture("notion_blocks.json")

        DBID_PATTERN = r"^/v1/databases/(?P<dbid>[^/]+)$"
        QUERY_PATTERN = r"^/v1/databases/(?P<dbid>[^/]+)/query$"
        CHILD_PATTERN = r"^/v1/blocks/(?P<block>[^/]+)/children$"
        PAGE_PATTERN = r"^/v1/pages/(?P<page>[^/]+)$"

        respx_mock.route(name="pages_create", method="POST", url="https://api.notion.com/v1/pages").mock(
            side_effect=self.pages_create_handler
        )
        respx_mock.route(
            name="pages_update", method="PATCH", scheme="https", host="api.notion.com", path__regex=PAGE_PATTERN
        ).mock(side_effect=self.pages_update_handler)

        respx_mock.route(
            name="db_info", method="GET", scheme="https", host="api.notion.com", path__regex=DBID_PATTERN
        ).mock(side_effect=self.database_info_handler)
        respx_mock.route(
            name="db_query", method="POST", scheme="https", host="api.notion.com", path__regex=QUERY_PATTERN
        ).mock(side_effect=self.database_query_handler)
        respx_mock.route(
            name="db_update", method="PATCH", scheme="https", host="api.notion.com", path__regex=DBID_PATTERN
        ).mock(side_effect=self.database_update_handler)

        respx_mock.route(
            name="pages_child_get", method="GET", scheme="https", host="api.notion.com", path__regex=CHILD_PATTERN
        ).mock(side_effect=self.blocks_child_handler)
        respx_mock.route(
            name="pages_child_update", method="PATCH", scheme="https", host="api.notion.com", path__regex=CHILD_PATTERN
        ).mock(side_effect=self.blocks_child_handler)

    def _get_handler(self, dbid):
        if dbid == "milestones_id":
            return self.milestones_handler
        elif dbid == "tasks_id":
            return self.tasks_handler
        elif dbid == "sprints_id":
            return self.sprints_handler

    def blocks_child_handler(self, req, block=None):
        res = {
            "object": "list",
            "next_cursor": None,
            "has_more": False,
            "type": "block",
            "block": {},
            "request_id": str(uuid.uuid4()),
            "results": self.blocks[block] if block in self.blocks else [],
        }

        return httpx.Response(200, json=res)

    def database_info_handler(self, req, dbid):
        handler = self._get_handler(dbid)
        if handler:
            return httpx.Response(200, json=handler.database_info)

        return httpx.Response(404)

    def database_update_handler(self, req, dbid=None):
        handler = self._get_handler(dbid)
        if handler:
            return httpx.Response(200, json=handler.update_handler(req))

        return httpx.Response(404)

    def database_query_handler(self, req, dbid=None):
        handler = self._get_handler(dbid)
        if handler:
            return httpx.Response(200, json=handler.query_handler(req))

        return httpx.Response(404)

    def pages_create_handler(self, req):
        reqjson = json.loads(req.content.decode("utf-8"))
        db_id = reqjson["parent"]["database_id"]
        if handler := self._get_handler(db_id):
            return httpx.Response(200, json=handler.create_handler(reqjson))

        return httpx.Response(404)

    def pages_update_handler(self, req, page):
        page = (
            self.tasks_handler.get_page(page)
            or self.milestones_handler.get_page(page)
            or self.sprints_handler.get_page(page)
        )

        if page:
            # TODO do we need to update this?
            return httpx.Response(200, json=page)

        return httpx.Response(404)


class GitHubHandler:
    def __init__(self):
        self.reset()

        requests = {}
        responses = {}

        basepath = Path(__file__).parent / "fixtures" / "github"
        for filename in os.listdir(basepath):
            if filename.endswith("_response.json"):
                with open(basepath / filename, "r") as fp:
                    responses[filename[:-14]] = json.load(fp)
            elif filename.endswith("_request.gql"):
                with open(basepath / filename, "r") as fp:
                    requests[filename[:-12]] = fp.read()

        self.pages = {request: filename for filename, request in requests.items()}
        self.responses = responses

    def reset(self):
        self.calls = defaultdict(list)

    def handle(self, request):
        reqdata = json.loads(request.data)["query"]

        if reqdata in self.pages:
            request_name = self.pages[reqdata]
            self.calls[request_name].append(request)
            return json.dumps(self.responses[request_name]).encode()
        else:
            print(reqdata)
            with open("lastreq.gql", "w") as fp:
                fp.write(reqdata)
            raise Exception("Unhandled request, find it in lastreq.gql")
