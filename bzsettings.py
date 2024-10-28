from dataclasses import dataclass, field
from libs.notion_data import link, number, rich_text, select, title
from typing import Dict, Any

bugzilla_base_url = "https://bugzilla.mozilla.org"

# Max bugs in each API query.
# https://www.bugzilla.org/docs/4.4/en/html/api/Bugzilla/WebService/Bug.html#limit
bz_limit = 100

# ID of the All Thunderbird Bugs Database in Notion.
bugs_db = "5f30c08339c04f1b97a50f23c2391a30"

# This is the ID for the desktop Tasks database in Notion.
# TODO: change to production, this is currently a test db.
desktop_task_db = "b45b29583a554d048792af51ce061ee4"

# List of bugzilla fields to include in queries using included_fields.
# These do not always have a 1:1 relationship with Notion fields.
# There is a map_bug_to_page function in bzhelper to map bug data to Notion fields.
bugzilla_fields = [
    'id', # Bug Number
    'assigned_to', # Email of assignee
    'cf_last_resolved',
    'component',
    'keywords',
    'last_change_time',
    'product',
    'resolution', # Needed as part of status
    'summary',
    'status',
    'version',
    'whiteboard'
]

# Define the properties and their types.
# This list MUST contain a title property.
# The database MUST contain a status property named 'Status'.
# To add a new property:
# 1. Add it below and the corresponding bugzilla field above.
# 2. Correct the map_bug_to_page function in bzhelper.

properties = [
    rich_text('Assignee'),
    number('Bug Number'),
    rich_text('Component'),
    rich_text('Keywords'),
    link('Link'),
    select('Product', ['Thunderbird', 'MailNews Core', 'Calendar']),
    title('Summary'),
    rich_text('Version'),
    rich_text('Whiteboard')
]
