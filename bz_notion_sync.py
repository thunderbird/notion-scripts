import bzsettings
import libs.bzhelper as bzhelper
import os

from libs.notion_data import NotionDatabase
from notion_client import Client

# Token for the Bugzilla Sync integration that's registered with Notion.
notion = Client(auth=os.environ['NOTION_TOKEN'])

# API key for Bugzilla account.
bugzilla_api_key = os.environ['BZ_KEY']

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
notion_db = NotionDatabase(bzsettings.bugs_db, notion, bzsettings.properties)

# Ensure the database has the properties we expect.
# This should probably happen on init, but we'll do it explicitly for now.
notion_db.update_props()

# Get all the bugs we want to sync from the Bugzilla API.
bugs = bzhelper.get_all_bugs(bzquery, bugzilla_api_key)
num_bugs = len(bugs)
print(f"Bugzilla API get completed, found {num_bugs} bugs.")

# Get all the pages currently in the Notion db.
pages = notion_db.get_all_pages()
num_pages = len(pages)
print(f"Notion API get completed, found {num_pages} pages.")

bzhelper.sync_bugzilla_to_notion(bugs, pages, notion_db)
