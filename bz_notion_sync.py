import libs.bzhelper as bzhelper
import os
import settings
from libs.notion_data import NotionDatabase
from notion_client import Client

# Token for the Bugzilla Sync integration that's registered with Notion.
notion = Client(auth=os.environ['NOTION_TOKEN'])
# API key for Bugzilla account.
bugzilla_api_key = os.environ['BZ_KEY']

# This is the ID for the Global Bug database in Notion.
global_bugs_db = "5f30c08339c04f1b97a50f23c2391a30"

# This is the ID for the desktop Tasks database in Notion.
# TODO: change to production, this is currently a test db.
desktop_task_db = "b45b29583a554d048792af51ce061ee4"

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
    "&v2=90"
    "&order=changeddate DESC"
)

# Initialize python representation of the Notion DB.
notion_db = NotionDatabase(global_bugs_db, notion, settings.properties)

# Ensure the database has the properties we expect.
# This should probably happen on init, but we'll do it explicitly for now.
notion_db.update_props()

bugs = bzhelper.get_all_bugs(bzquery, bugzilla_api_key)
num_bugs = len(bugs)
print(f"Bugzilla API get completed, found {num_bugs} bugs.")

pages = notion_db.get_all_pages()
num_pages = len(pages)
print(f"Notion API get completed, found {num_pages} pages.")

bzhelper.sync_bugzilla_to_notion(bugs, pages, notion_db)
