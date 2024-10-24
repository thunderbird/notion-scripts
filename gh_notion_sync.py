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


# To add more repos, duplicate an existing notion page that uses this script, ex: https://www.notion.so/mzthunderbird/11b2df5d45ae80dcb716c22f068ce667?v=11b2df5d45ae81fda446000c779bfb51
# Then add the MZLA Integration connection so we can access it through the API. Then add the repo name database id below:
repos = [
    ["thunderbird/pulumi", "11b2df5d45ae80dcb716c22f068ce667"],
    ["thunderbird/assist-daily-digest", "11b2df5d45ae80e0b3a9d275b8e58f30"],
    ["thunderbird/send-suite", "11b2df5d45ae80c5a078e5f041dfe06d"],
    ["thunderbird/appointment", "3030fbc779254c6bbbb76d391e2f7923"],
]

for repo in repos:
    repo_name = repo[0]
    database_id = repo[1]
    print('connecting to notion for ', repo_name);
    # Initialize the Notion client with your integration token
    notion = Client(auth=os.environ['NOTION_TOKEN'])

    notion_db = NotionDatabase(database_id, notion, settings.gh_properties)
    ghhelper.sync_gh_to_notion([repo_name], os.environ['GITHUB_TOKEN'], notion_db, database_id)
