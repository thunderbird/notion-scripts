from dataclasses import dataclass, field
from libs.notion_data import link, select, number, rich_text
from typing import Dict, Any

bugzilla_base_url = "https://bugzilla.mozilla.org"

# Max bugs in each API query.
# https://www.bugzilla.org/docs/4.4/en/html/api/Bugzilla/WebService/Bug.html#limit
bz_limit = 100

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

# Define the properties and their types
# Excludes Status and Summary due to API restrictions.
# To add a new property:
# 1. Add it below and the corresponding bugzilla field above.
# 2. Correct the map_bug_to_page function in bzhelper.
# TODO: Add Summary here, it's a special title property and needs unique logic.
properties = [
    rich_text('Assignee'),
    number('Bug Number'),
    rich_text('Component'),
    rich_text('Keywords'),
    link('Link'),
    select('Product', ['Thunderbird', 'MailNews Core', 'Calendar']),
    rich_text('Version'),
    rich_text('Whiteboard')
]
