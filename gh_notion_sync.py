"""
import dateutil.parser
import requests
import time
from datetime import datetime, timedelta
"""
import libs.ghhelper as ghhelper 
from notion_client import Client
from libs.notion_data import NotionDatabase
import settings
import os
import pdb

# Initialize the Notion client with your integration token
#database_id = "c008270018c444fcb377170185c059ed"
print('connecting to notion');
database_id = "3030fbc779254c6bbbb76d391e2f7923"
notion = Client(auth=os.environ['NOTION_TOKEN'])
notion_db = NotionDatabase(database_id, notion, settings.properties)

# Ensure the database has the properties we expect.
# This should probably happen on init, but we'll do it explicitly for now.
notion_db.update_props()
#notion_db.get_all_pages();

ghhelper.sync_gh_to_notion('thunderbird/appointment', os.environ['GITHUB_TOKEN'], notion_db)
