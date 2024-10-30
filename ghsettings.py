from libs.notion_data import NotionDatabase, link, select, number, rich_text, title

# This is the ID of the All GitHub Issues database.
database_id = "3ca7ed3fe75b4a6d805953156a603540"

# Name of the org to prefix repos for API calls, with trailing slash.
orgname = 'thunderbird'

# Repositories to import issues from.
repos = [
    "addons-server",
    "appointment",
    "assist",
    "cloudops",
    "code-coverage",
    "mailstrom",
    "pulumi",
    "send-suite",
    "services-ui",
    "services-utils",
    "stats",
    "thunderbird-notifications",
    "thunderbird-website",
    "thunderblog",
    "thundernest-ansible"
]

# Properties of the "All GitHub Issues" database in Notion.
# There must also be a status property named 'Status'.
properties = [
    select('Repository', repos),
    rich_text('Assignee'),
    title('Title'),
    link('Link'),
    rich_text('Unique ID')
]
