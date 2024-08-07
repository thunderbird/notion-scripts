import libs.bzhelper as bzhelper
import settings
from libs.notion_data import NotionDatabase
from notion_client import Client

# Token for the Bugzilla Sync integration that's registered with Notion.
notion = Client(auth="")

# This is the ID that's in the notion URL.
database_id = "5f30c08339c04f1b97a50f23c2391a30"

bugzilla_api_key = ""

bzquery = (
    "?bug_status=NEW"
    "&bug_status=ASSIGNED"
    "&bug_status=REOPENED"
    "&bug_status=RESOLVED"
    "&bug_status=VERIFIED"
    "&bug_status=CLOSED"
    "&f1=OP"
    "&f2=days_elapsed"
    "&f3=CP"
    "&list_id=17103050"
    "&o2=lessthaneq"
    "&product=MailNews Core"
    "&product=Thunderbird"
    "&query_format=advanced"
    "&v2=60"
    "&order=changeddate DESC"
)

# Initialize python representation of the Notion DB.
notion_db = NotionDatabase(database_id, notion, settings.properties)

# Ensure the database has the properties we expect.
# This should probably happen on init, but we'll do it explicitly for now.
notion_db.update_props()

bzhelper.sync_bugzilla_to_notion(bzquery, bugzilla_api_key, notion_db)
