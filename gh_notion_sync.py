import ghsettings
import os
import libs.ghhelper as ghhelper

from libs.notion_data import NotionDatabase
from notion_client import Client

# Initialize Notion client.
notion = Client(auth=os.environ['NOTION_TOKEN'])
notion_db = NotionDatabase(ghsettings.database_id, notion, ghsettings.properties)

# Set properties on database.
notion_db.update_props()

# Gather data.
issues = ghhelper.get_all_issues()
pages = notion_db.get_all_pages()

# Start sync.
ghhelper.sync_github_to_notion(issues, pages, notion_db)
