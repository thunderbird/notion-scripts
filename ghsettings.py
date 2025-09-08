import libs.notion_data as p

# This is the ID of the All GitHub Issues database.
database_id = "3ca7ed3fe75b4a6d805953156a603540"

# This is the ID of the Milestones database.
milestones_id = "1352df5d45ae8068a42dc799f13ea87a"

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
    "notion-scripts",
    "pulumi",
    "send-suite",
    "services-ui",
    "services-utils",
    "stats",
    "thunderbird-accounts",
    "thunderbird-notifications",
    "thunderbird-website",
    "thunderblog",
    "thundernest-ansible",
    "knowledgebase-issues",
    "android-knowledgebase-issues",
    "tbpro-knowledgebase-issues",
    "zendesk-config",
    "private-issue-tracking",
    "tbpro-add-on",
    "observability-strategy"
]

# Properties of the "All GitHub Issues" database in Notion.
# There must also be a status property named 'Status', which is not listed here.
# There is also a Labels property defined in gh_notion_sync.py
properties = [
    p.select('Repository', repos),
    p.rich_text('Assignee'),
    p.title('Title'),
    p.link('Link'),
    p.rich_text('Unique ID'),
    p.date('Opened'),
    p.date('Closed'),
    p.relation('Milestones', milestones_id, True)
]
