# notion-scripts

## How to set up a syncing database:

1. Create a new database in Notion, and set the Status property. This is manual because the API doesn't support adding or modifying the Status property on a database.
2. Attach the `MZLA Integrations` app under `Connections` in the ... menu, otherwise the script won't be able to access the database.
3. Get the database id from the URL. It's the string after `/mzthunderbird/` not including the query params.
4. Create a new file similar to the existing `bz_notion_sync.py` and write the API integration logic.

Currently, a Bugzilla API key, GitHub API key, and the Notion integration secret for MZLA Integrations are required to run this script.

## Overview

`libs/notion_data.py` contains classes and utilities for adding and updating Notion database pages and properties.

This contains two main classes:

`NotionDatabase`: Defines a Notion database, along wih its properties and a remotely tied Notion client used for CRUD operations.
`NotionProperty`: Defines a generic Notion property, including functions to return the right data for updating content and the property itself.

### Bugzilla Sync
`libs/bzhelper.py` contains helper functions and utilities for connecting to Bugzilla and syncing Bugzilla -> Notion.
`bzsettings.py` contains Notion database properties and bugzilla fields that are used by sync process.
`bz_notion_sync.py` is used to run the sync code.

### GitHub Issues Sync
`libs/ghhelper.py` contains helper functions and utilities for connecting to GitHub and syncing to Notion.
`ghsettings.py` contains the repo list, db properties and other basic settings.
`gh_notion_sync.py` is used to run the sync code.
