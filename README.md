# notion-scripts

## How to set up a syncing database:

1. Create a database in notion, and set the Status property. The API doesn't support modifying the Status property.
2. Attach the Bugzilla Sync integration under "Connections" in the ... menu, otherwise the script won't be able to access the database.
3. Get the database id from the URL. It's the string after `/mzthunderbird/` not including the query params.
4. Create a new file similar to the existing `bz_notion_sync.py`.

## Overview

`libs/notion_data.py` contains classes and utilities for adding and updating Notion database pages and properties.
`libs/bzhelper.py` contains helper functions and utilities for connecting to Bugzilla and syncing Bugzilla -> Notion.
`settings.py` contains Notion database properties and bugzilla fields that are used by sync process.

A Bugzilla API key and the Notion integration secret for Bugzilla Sync are required to run this script.

## notion_data

This contains two main classes:

`NotionDatabase`: Defines a Notion database, along wih its properties and a remotely tied Notion client used for CRUD operations.
`NotionProperty`: Defines a generic Notion property, including functions to return the right data for updating content and the property itself.
