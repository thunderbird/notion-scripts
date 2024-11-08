import ghsettings
import os
import libs.ghhelper as ghhelper
import libs.notion_data as p

from libs.notion_data import NotionDatabase
from notion_client import Client

# Initialize Notion client.
notion = Client(auth=os.environ['NOTION_TOKEN'])

# Gather issues first so that we can populate select properties accordingly.
issues = ghhelper.get_all_issues()
labels = ghhelper.extract_labels(issues)

# Add labels property limited to all known labels
properties = ghsettings.properties + [p.multi_select('Labels', labels)]

# Create database object.
notion_db = NotionDatabase(ghsettings.database_id, notion, properties)

# Set properties on database.
notion_db.update_props()

# Gather pages.
pages = notion_db.get_all_pages()

# Start sync.
ghhelper.sync_github_to_notion(issues, pages, notion_db)
