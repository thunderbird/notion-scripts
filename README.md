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

## Github Issues -> Notion Pages

There is a [shared GH database](https://www.notion.so/mzthunderbird/3030fbc779254c6bbbb76d391e2f7923?v=c81686996f5d4b0f8ff6a5ae3e5af309) across our repos. Each repository will have a page associated with it, whose parent page is the shared GH database. Each issue in a repostiory will be a notion task (a page), and these tasks' parent pages are their respective repository pages.

actually, i'll just shove them on this page and add a column for the repo. It's less coding and we can just filter on it?

Regarding the code:

`gh_notion_sync.py` contains the list of repositories we will be combing, and triggers the import.
`libs/ghhelper.py` contains helper functions for pulling in issues from Github and turning them into pages. 

