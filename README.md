# notion-scripts

This tool synchronizes Notion with GitHub and Bugzilla, for use with MZLA's Notion setup.

## Configuration

#### Repository sets
A single project synchronization is meant to be used for a Notion Milestone/Tasks database
combination. If you use more than one Notion Milestones/Tasks database, you'll want one Project
Synchronization for each of them.

Within each Notion Milestones/Tasks database, you might be catering to more than one GitHub
repository. For this we use the repository sets, to be configured in the
`sync_settings.<name>.repositories` section.

* If you have one GitHub Project set (Roadmap/Sprints) that spans all of your GitHub repositories,
  configure one repository set that has multiple repositories listed in the `repositories` array of
  the `sync_settings.<name>.repositories.<id>` section.
* If you have one GitHub Project set (Roadmap/Sprints) per repository, configure multiple repository
  sets that each have that one repository listed. Repository sets can certainly have more than one
  repository as well if you want to group them.

### Notion Setup

To configure, you need to create/edit the sync_settings.toml file, set a few environment variables,
and create a few databases in Notion. When creating databases, make sure you share them with the
`MZLA Integrations` integration in the `Connections` menu within the three-dots menu on the
respective database. You can also do so for the parent item all databases are in.

The database ids are found within the URL when you visit the database page in your browser.

### Environment
The following variables need to be set, depending on which integrations are enabled.

```shell
NOTION_TOKEN=<your notion integration token>
GITHUB_TOKEN=<your github integration token>
BZ_KEY=<your bugzilla API key>
```

The following variable can optionally be set instead of the `usermap.github` configuration option.

```shell
NOTION_SYNC_GITHUB_USERMAP=`cat users.toml`
```

Your `users.toml` from the above example cab look like this. The UUID is the id from the notion API.
There are instructions on how to get this id in notion_sync.py

```toml
kewisch = "8e664893-abc5-4700-b805-8e0facecce99"
wmontwe = "0259eb9f-353f-4b1b-af8f-e25f5bf06a59"
```

### sync_settings.toml

This is the main configuration file. Here is a verbose example:

```toml
# This is the configuration file. It is more verbose than it needs to be so you can see all options
[usermap]

[usermap.github]
# This section maps github username to the id of the notion user.
# Use it to ensure that mentions are correctly translated.
kewisch = "8e664893-abc5-4700-b805-8e0facecce99"

[sync]
# There are three supported synchronization engines: github_labels, github_project and bugzilla They
# each behave very different, as described further below. The options for each engine are different
# as well, even if there is some overlap

[sync.services]
# Services uses a labels-based github sync (required)
method = "github_labels"

# All issues are synced into a separate "All GitHub Issues" database with this id (required)
notion_tasks_id = "19ddea4adcdf8052906aeeb2f3d5acc9"

# The Milestones are connected via labels, and this is the id of the milestones Notion db (required)
notion_milestones_id = "19ddea4adcdf8018b060cda446ff2835"

# All repos are within the thunderbird/ space, so strip the org name from the repos (default false)
strip_orgname = true

# The list of repositories to synchronize (required)
repositories = [
    "thunderbird/addons-server",
    "thunderbird/appointment"
    # ...
]


[sync.mobile]
# Mobile uses a GitHub projects based sync, as also described below
method = "github_project"

# The Tasks and Milestones are required. Tasks is the normal tasks database, it is not a separate
# database and tasks are intermingled with other items. This is fine because not all issues sync to
# tasks.
notion_tasks_id = "18adea4adcdf807c8fabcc9c11b61777"
notion_milestones_id = "18adea4adcdf80b9a9e0f3c1a18ede53"

# The sprints database is optional, if not specified then sprints will not synchronize.
# Please note that sprints will be synchronized by name, if you use multiple repository sets then
# you have to make sure the sprint names and dates stay in sync.
notion_sprints_id = "18adea4adcdf8073af16f1d07eb1661e"

# If true, the github issue body will be synced for each task
# This is time consuming because Notion requires multiple requests per page
body_sync = false


# You can synchronize the body of the Milestone items from Notion as Markdown to GitHub so they are
# constantly updated. This is time consuming though because a lot of requests are required due to
# notion's API. You likely want to keep this disabled (the default)
milestones_body_sync = false

# What you might want however is a one-time sync when the GitHub issue is empty. Your workflow is to
# create an empty GitHub issue, connect it to the milestone, wait for sync. Then the GitHub issue
# will be updated with the markdown.
milestones_body_sync_if_empty = true

# If you want all GitHub issues connected to milestones to have a prefix in their title, set this
# property. Don't forget the trailing space.
milestones_github_prefix = "[EPIC] "

# If you want all GitHub issues connected to milestones to have a label applied, set this property.
milestones_github_label = "type: epic"

# Likewise, you might want to prefix all synced Notion tasks so you can easier identify them between
# other high level tasks.
tasks_notion_prefix = "[GitHub] "

# If you have multiple GitHub projects synchronizing into one Sprints database, you can choose to
# merge sprints by name. The requirement is that the dates align.
sprints_merge_by_name = false

# Now we begin repositories. We need a mapping between the repositories and the connected GitHub
# Projects. You might just have one if everything is in a single GitHub Project, or you might have
# multiple if you want to separate them.
[sync.mobile.repositories]

[sync.mobile.repositories.android]
# The list of repositories that are allowed to be synced. This doesn't mean all issues from these
# will be copied over however, as sync is much more selective.
repositories = [
  "thunderbird/thunderbird-android",
]

# There needs to be a GitHub project for the roadmap that is connected to the milestones, and one
# for the sprint tasks which is connected to the tasks. Find them via the commented out code in the
# main script.
github_tasks_project_id = "PVT_kwHOAAlD3s4AxVFW"
github_milestones_project_id = "PVT_kwHOAAlD3s4AxVDI"

# Here is an example of a second set of repositories, connected to different GitHub Projects.
[sync.mobile.repositories.ios]
repositories = [
  "thunderbird/thunderbird-ios",
]
github_tasks_project_id = "PVT_kwDOAOe9Jc4A1aav"
github_milestones_project_id = "PVT_kwDOAOe9Jc4A1aX6"

# Here you can change the property names for certain Notion properties. They tend to be different
# depending on how the database was created and how you maybe renamed them. See
# libs/gh_project_sync.py for the default settings, they will also help you in the initial setup.
[sync.mobile.properties]
notion_tasks_title = "Title"
notion_tasks_assignee = "Assignee"
notion_tasks_dates = "Date"
notion_tasks_milestone_relation = "Project"
notion_milestones_title = "Name"
notion_milestones_assignee = "Assignee"
notion_tasks_open_state = "Not started"


[sync.bugzilla]
# Desktop uses a bugzilla sync. 
method = "bugzilla"

# There is a database with All Thunderbird Bugs in Notion, specify the ID here.
notion_bugs_id = "5f30c08339c04f1b97a50f23c2391a30"

# This is the bugzilla instance. You don't need to specify as the default is BMO.
bugzilla_base_url = "https://bugzilla.mozilla.org"

# This allows adjusting the products to synchronize, though you might also need to adjust the query.
products = ["Thunderbird", "MailNews Core", "Calendar"]

# The list id of a bugzilla query that matches, speeds up search. Leave out if unknown.
list_id = 17103050

# Max bugs in each API query.
# https://www.bugzilla.org/docs/4.4/en/html/api/Bugzilla/WebService/Bug.html#limit
bugzilla_limit = 100
```

## Synchronization Mechanisms
There are three sync mechanisms. Two for GitHub, one for Bugzilla.


### GitHub Labels Synchronization (method = "github_labels")

This is a  simple integration without complexities:
* All GitHub issues will be synchronized into the configured tasks database in Notion
* Issues are connected to a milestone using a label "M: Milestone Name". 
* The Milestone name will be matched with a Milestone on Notion.

This way you keep the issues separate, but can still connect them to the Milestone. Setup required:
* Create an empty "All GitHub Issues" database and make sure you have a `Status` property. 
* The code will set/overwrite all remaining properties as needed. 

### GitHub Project Synchronization (method = "github_projects")

If you'd like more elaborate synchronization between GitHub Projects and Notion, this section is for
you. The setup is opinionated, though attempts to work generally for Thunderbird's projects.
 
* Notion is the authoritative source for "Milestones", here is where you plan your high level
  projects. Notion info is synced to the connected issue.
  
* GitHub is the authoritative source for "Tasks", here is where engineers will work in the day to
  day. Sub-issues of milestones on GitHub, Issues that are connected to a Notion task manually, and
  other issues that are on the GitHub sprint project will all be synchronized to Notion.
  
#### Workflow

Here is your workflow as a manager/project manager:
  * For each Milestone in Notion, create an issue on GitHub and link it via the `GitHub Issue`
    property on your Notion milestone. When the sync happens, all info will be copied over to the
    new GitHub issue.
  * Any Milestone changes you make in Notion will be synchronized, one-way, to the GitHub issue.
    Depending on settings this will also include the body text of the Notion milestone.
  * Make the GitHub Project for the roadmap public, but consider this a readonly view where you do
    not make changes.
  * If you have the "Sprints" feature enabled in Notion or would like to, consider sprints in Notion
    to be a read-only view. The actual work should happen in GitHub. It may be tempting to add
    additional items, but then engineers have two places to look.

Here is your workflow as an engineer:
* Use the Epic issue on GitHub as the parent item for any work you do. All child issues one level
  deep will be synchronized to Notion. 
* Plan these issues into sprints using the Sprints GitHub Project. You can do all the work on
  GitHub.
* If you have additional high level tasks or are still breaking things down, you can also use Tasks
  on Notion connected to the Milestone. These won't sync from Notion to GitHub unless you connect
  them with a GitHub issue after the fact.
* Consider any Tasks connected to a GitHub issue read-only on the Notion side. Comments and work
  should happen on the GitHub issue.

#### Notion Setup

Make use of the pre-existing "Milestones" and "Tasks" databases in Notion. If wanted, enable the
"Sprints" feature in your Tasks database. Remember, not all issues are synchronized, so you don't
have to worry about your Tasks being cluttered.

On Notion, make sure the Databases have the expected properties:

* Milestones Database
  * `Status`: Make sure you have a status property and take note of the exact Status values.
  * `Dates`: The start and target date for your milestones
  * `Priority`: The priority for your milestone, with values P1, P2, P3
  * `GitHub Issue`: A link field which will be used to save the link to the GitHub issue.
* Tasks Database:
  * `GitHub Assignee`: A rich text field, not an owner field. The real owner will still be used, but
    this helps for people not on Notion.
  * `GitHub Issue`: An URL field which will be used to save the link to the GitHub issue.
  * `Dates`: The start/end date for the task. This will be mapped to sprint dates.
  * `Priority`: The priority for the task, with values P1, P2, P3

You can change the property names in the sync_settings config if needed. 

#### GitHub Setup
On GitHub, you'll need to create two projects for each set of repositories you want to synchronize:

**Sprint Project**: This is the project that will retain the individual tasks, as noted above, with
  the following fields:
 * `Status`: Dropdown field, which uses the exact names of the `Status` property on Notion, with
   matching case.
 * `Priority`: Dropdown field, with the exact names of the `Priority` property on Notion, with
   matching case.
 * `Sprint`: Iteration field, with the respective sprint names you are using
 * Usually there is also a "Sub-issues progress" field, though it isn't relevant for the sync
 * Create a Kanban board:
   * Layout: Board
   * Fields: Title, Assignees, Status, Priority, Sprint
   * Column by: Sprint
 * Create a Timeline view:
   * Layout: Roadmap
   * Group by: Parent issue
   * Sort by: Sprint
   * Zoom level: Quarter


**Roadmap Project**: This project shows a public view of your roadmap, including all issues you've
  linked in Notion. It should have the following fields:
  
 * `Status`: Dropdown field, which uses the exact names of the `Status` property on Notion, with
    matching case.
 * `Priority`: Dropdown field, with the exact names of the `Priority` property on Notion, with
   matching case.
 * `Start Date`: Date field, with the start date. On Notion you'll have a single field `Dates` with
   a start and end date
 * `Target Date`: Date field, with the end date. On Notion you'll have a single field `Dates` with
   a start and end date
 * `Link`: Text field, which will be filled with a backlink to Notion.
 * Usually there is also a "Sub-issues progress" field, though it isn't relevant for the sync
 * When you describe the roadmap project, make sure to indicate that this view is read-only and any
   changes made on GitHub will be overwritten
 * Create a view with:
   * Layout: Roadmap
   * Group by: none
   * Sort by: Target Date
   * Dates: Start Date and Target Date
   * Zoom level: Year
 * Workflows
   * Disable "Auto-add sub-issues to project" and "When a pull request is merged"

Once you have the two projects, use this code to determine the GitHub database ID from the
repository and then set `github_tasks_project_id` and `github_milestones_project_id` in the
repository settings:

```python
ghhelper.GitHubProjectV2.list("thunderbird", "thunderbird-android")
```

### Bugzilla
TODO The bugzilla integration does things. Check the config and code for more details.
