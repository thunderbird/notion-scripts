# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Dict, List

from md2notionpage.core import parse_md
from notion_client.helpers import collect_paginated_api
from notion_to_md import NotionToMarkdown

from .util import retry_call

logger = logging.getLogger("notion_database")


@dataclass
class NotionProperty:
    """Defines a generic Notion database property.

    It must contain functions to let you check whether a property's content differs from input
    content, and a function to return the correct structure to update the property's contents in a
    Notion database page.
    """

    name: str
    type: str
    additional: Dict[str, Any] = field(default_factory=dict)
    _update: Callable[[Any], Dict[str, Any]] = None
    _diff: Callable[[Dict[str, Any], Any], bool] = None

    def to_dict(self):
        """Returns a dict that defines this property in the Notion API format."""
        return {"name": self.name, "type": self.type, **self.additional}

    def update_content(self, content: Any):
        """Returns `content` formatted in the right way for the Notion API to accept."""
        if self._update:
            return self._update(content)
        else:
            raise ValueError("No update function defined.")

    def is_prop_diff(self, property_data: Dict[str, Any], content: Any) -> bool:
        """Logic to return whether `property_data` is different from `content` for this property type."""
        if self._diff:
            return self._diff(property_data, content)
        else:
            raise ValueError(f"No diff function defined for {self.name} property.")


class NotionDatabase:
    """Defines the structure of a Notion database and its properties.

    Additionally contains methods to add, delete, and update pages inside the database.
    The Status property is special and can't be modified by the Notion API. Similarly, the Title
    property can't be deleted or modified, though the name can be changed.
    """

    def __init__(
        self, database_id: str, notion_client: Any, properties: List[NotionProperty] = None, dry: bool = False
    ):
        """Initialize! Pass `dry` to nerf all mutating properties."""
        self.properties: Dict[str, NotionProperty] = {}
        if properties:
            for prop in properties:
                self.add_property(prop)
        self.notion = notion_client
        self.database_id = database_id
        self.dry = dry

    @property
    def description(self):
        """Get the database description, what is shown at the top of the page."""
        database_info = self.notion.databases.retrieve(self.database_id)
        # Extract and return the description as plain text.
        return "".join([item["text"]["content"] for item in database_info.get("description", [])])

    @description.setter
    def description(self, new_desc):
        if self.dry:
            return

        self.notion.databases.update(
            database_id=self.database_id,
            description=[{"type": "text", "text": {"content": new_desc}}],
        )

    def get_all_pages(self):
        """Gets all pages currently in the Notion database."""
        pages = []
        cursor = None

        while True:
            response = retry_call(
                lambda: self.notion.databases.query(self.database_id, start_cursor=cursor, page_size=100)
            )
            pages.extend(response["results"])
            cursor = response.get("next_cursor")

            if cursor is None:
                break

        return pages

    def dict_to_page(self, datadict: Dict[str, Any]):
        """Takes a `datadict` and returns a Notion database page formatted for the Notion API.

        A datadict is a dictionary containing {<property_name>: <data>}.
        """
        props = self.properties
        page = {}

        if datadict.get("Status"):
            page = {"Status": {"status": {"name": datadict.pop("Status")}}}

        for key, value in datadict.items():
            if key in props:
                page.update(props[key].update_content(value))

        return page

    def create_page(self, datadict: Dict[str, Any]) -> bool:
        """Create a new page in the Notion database.

        `datadict` must be a dictionary containing {<property_name>: <data>}.
        """
        page_data = self.dict_to_page(datadict)
        if page_data:
            if self.dry:
                return {"id": "dry"}  # Fake page
            else:
                return retry_call(
                    lambda: self.notion.pages.create(parent={"database_id": self.database_id}, properties=page_data)
                )
        return None

    def delete_page(self, page_id):
        """Delete a page in the remote Notion database by `page_id`."""
        if not self.dry:
            retry_call(lambda: self.notion.pages.update(page_id, archived=True))

    def update_page(self, page: Dict[str, Any], datadict: Dict[str, Any]) -> bool:
        """Update `page` with the data in `datadict`. Updates only occur if `page` and `datadict` are different."""
        if self.page_diff(datadict, page):
            data = self.dict_to_page(datadict)
            if not self.dry:
                retry_call(lambda: self.notion.pages.update(page["id"], properties=data))
            return True
        return False

    def page_diff(self, datadict: Dict[str, Any], page: Dict[str, Any]) -> bool:
        """Return true or false based on whether the Notion `datadict` matches `page` or not."""
        cur_props = self.properties

        # The status property needs special handling if it exists since it isn't a registered property.
        if datadict.get("Status") and datadict["Status"] != page["properties"]["Status"]["status"]["name"]:
            return True
        # Loop over all properties and see if any are different.
        for prop_name, prop_value in datadict.items():
            if prop_name in cur_props and cur_props[prop_name].is_prop_diff(
                page["properties"].get(prop_name, {}), prop_value
            ):
                return True
        return False

    def get_page_contents(self, page_id):
        """Retrieves the blocks in a Notion page in this database."""
        return collect_paginated_api(self.notion.blocks.children.list, block_id=page_id)

    def replace_page_contents(self, page_id, markdown):
        """Replace the contents of the notion page with the supplied markdown."""
        if self.dry:
            return

        blocks = parse_md(markdown)
        blocks = list(filter(lambda block: block["type"] != "image", blocks))

        server_blocks = collect_paginated_api(self.notion.blocks.children.list, block_id=page_id)

        for block in server_blocks:
            retry_call(lambda: self.notion.blocks.delete(block_id=block["id"]))

        retry_call(lambda: self.notion.blocks.children.append(block_id=page_id, children=blocks))

    def add_property(self, prop: NotionProperty):
        """Adds a property to the local instance of the Notion database."""
        self.properties[prop.name] = prop

    def to_dict(self):
        """Returns the property definition in the right format to modify a Notion database."""
        return {name: prop.to_dict() for name, prop in self.properties.items()}

    def get_props(self):
        """Returns the database information (e.g. properties)."""
        return retry_call(lambda: self.notion.databases.retrieve(database_id=self.database_id))

    def update_props(self, delete=False):
        """Updates the properties of the remote Notion database tied to the local instance."""
        # TODO: This method could use some error checking and verifying that it worked properly.
        desired_props = self.to_dict()

        # Fetch the current properties of the database.
        current_db = retry_call(lambda: self.notion.databases.retrieve(database_id=self.database_id))
        current_props = current_db["properties"]

        # Process current properties: delete properties not in desired list, and add/update missing ones
        # The status and title properties cannot be deleted via the API.
        if delete:
            for prop_name, prop_info in current_props.items():
                if prop_name not in desired_props and prop_info["type"] not in [
                    "status",
                    "title",
                ]:
                    if self.dry:
                        logger.info(f"Extra property {prop_name} on database {self.database_id} will be deleted")
                    else:
                        retry_call(
                            lambda: self.notion.databases.update(
                                database_id=self.database_id,
                                properties={prop_name: None},
                            )
                        )

        # Add or update missing properties
        changes = False
        for prop_name, prop_schema in desired_props.items():
            if prop_name not in current_props or current_props[prop_name]["type"] != prop_schema["type"]:
                if prop_schema["type"] == "title":
                    # The title property always has the id "title" so can be renamed that way.
                    properties = {"title": {"name": prop_name}}
                else:
                    properties = {prop_name: prop_schema}

                changes = True
                if self.dry:
                    logger.info(f"Updating property {prop_name} to schema {prop_schema} on {self.database_id}")
                else:
                    retry_call(
                        lambda: self.notion.databases.update(database_id=self.database_id, properties=properties)
                    )

        if not changes and self.dry:
            logger.info(f"All properties on {self.database_id} are up to date")


class CustomNotionToMarkdown(NotionToMarkdown):
    """NotionToMarkdown converter that strips images and converts mentions from notion to GitHub."""

    def __init__(self, notion_client, strip_images=False, user_map=None, config={}):
        """Initialize. Pass in a user map to convert mentions."""
        super().__init__(notion_client, config)
        self.strip_images = strip_images
        self.user_map = user_map

    def convert(self, blocks) -> str:
        """Convenience function to convert blocks directly to string."""
        md_blocks = self.block_list_to_markdown(blocks)
        return self.to_markdown_string(md_blocks).get("parent")

    def block_to_markdown(self, block: Dict) -> str:
        """Super class class this for processing each block."""
        if block["type"] == "image" and self.strip_images:
            return ""

        if block["type"] == "paragraph":
            for rich_text in block["paragraph"]["rich_text"]:
                if rich_text["type"] == "mention":
                    new_user = None
                    if rich_text["mention"]["type"] == "user" and self.user_map:
                        gh_user = self.user_map.notion_to_gh(rich_text["mention"]["user"]["id"])
                        new_user = "@" + gh_user if gh_user else None

                    if new_user:
                        rich_text["plain_text"] = new_user
                    else:
                        # Strip the @ to avoid mentioning random people on github
                        rich_text["plain_text"] = rich_text["plain_text"].replace("@", "")

        return super().block_to_markdown(block)


# Property creation functions
# Each must have an _update function and _diff function.
# _update is used to return content formatted to be a Notion page.
# _diff returns whether or not a Notion page contains the same data as the input content.


def dates(name: str) -> NotionProperty:
    """A multi-date property.

    TODO this is likely the same as the singular date property, just with the extra end date field
    """

    def _update(content: dict) -> Dict[str, Any]:
        if content:
            return {
                name: {
                    "date": {
                        "start": content["start"].isoformat(),
                        "end": content["end"].isoformat(),
                    }
                }
            }
        else:
            return {name: {"date": None}}

    def _diff(property_data: Dict[str, Any], content: datetime) -> bool:
        start_data = property_data.get("date").get("start") if property_data.get("date") else None
        end_data = property_data.get("date").get("end") if property_data.get("date") else None

        content_start = content["start"].isoformat() if content else None
        content_end = content["end"].isoformat() if content else None

        if content_start != start_data or content_end != end_data:
            return True
        return False

    return NotionProperty(name=name, type="date", additional={"date": {}}, _update=_update, _diff=_diff)


def date(name: str) -> NotionProperty:
    """A singular date property."""

    def _update(content: datetime) -> Dict[str, Any]:
        if content:
            return {name: {"date": {"start": content.date().isoformat()}}}
        else:
            return {name: {"date": None}}

    def _diff(property_data: Dict[str, Any], content: datetime) -> bool:
        property_data = property_data.get("date").get("start") if property_data.get("date") else None
        if content:
            content = content.date().isoformat()
        if property_data != content:
            return True
        return False

    return NotionProperty(name=name, type="date", additional={"date": {}}, _update=_update, _diff=_diff)


def status(name: str) -> NotionProperty:
    """The status dropdown.

    This is a special property since in many cases it cannot be changed/added from the API. It just
    exists on certain databases.
    """

    def _update(content: str) -> Dict[str, Any]:
        return {name: {"status": {"name": content}}}

    def _diff(property_data: Dict[str, Any], content: str) -> bool:
        if "status" not in property_data:
            return True
        if property_data.get("status", {}).get("name") != content:
            return True
        return False

    return NotionProperty(
        name=name,
        type="status",
        additional={"status": {}},
        _update=_update,
        _diff=_diff,
    )


def link(name: str) -> NotionProperty:
    """An URL link."""

    def _update(content: str) -> Dict[str, Any]:
        return {name: {"url": content}}

    def _diff(property_data: Dict[str, Any], content: str) -> bool:
        if "url" not in property_data:
            return True
        if property_data.get("url") != content:
            return True
        return False

    return NotionProperty(name=name, type="url", additional={"url": {}}, _update=_update, _diff=_diff)


def rich_text(name: str) -> NotionProperty:
    """A rich text propertay."""

    def _update(content: str) -> Dict[str, Any]:
        return {name: {"rich_text": [{"text": {"content": content}}]}}

    def _diff(property_data: Dict[str, Any], content: str) -> bool:
        if "rich_text" not in property_data:
            return True
        if len(property_data["rich_text"]) == 0:
            return True
        if property_data["rich_text"][0]["plain_text"] != content:
            return True
        return False

    return NotionProperty(
        name=name,
        type="rich_text",
        additional={"rich_text": {}},
        _update=_update,
        _diff=_diff,
    )


def number(name: str) -> NotionProperty:
    """A number property."""

    def _update(content: int) -> Dict[str, Any]:
        return {name: {"number": content}}

    def _diff(property_data: Dict[str, Any], content: int) -> bool:
        if "number" not in property_data:
            return True
        if property_data.get("number") != content:
            return True
        return False

    return NotionProperty(
        name=name,
        type="number",
        additional={"number": {}},
        _update=_update,
        _diff=_diff,
    )


def select(name: str, options: List[str]) -> NotionProperty:
    """A single-select with a list of options."""

    def _update(content: str) -> Dict[str, Any]:
        if content and content not in options:
            raise ValueError(f"Invalid option: {content}. Must be one of {options}.")

        if content:
            return {name: {"select": {"name": content}}}
        else:
            return {name: {"select": None}}

    def _diff(property_data: Dict[str, Any], content: str) -> bool:
        if "select" not in property_data:
            return True
        if (property_data.get("select", {}) or {}).get("name", None) != content:
            return True
        return False

    return NotionProperty(
        name=name,
        type="select",
        additional={"select": {"options": [{"name": opt} for opt in options]}},
        _update=_update,
        _diff=_diff,
    )


def multi_select(name: str, options: List[str]) -> NotionProperty:
    """A multi-select with a list of options."""

    def _update(content: List[str]) -> Dict[str, Any]:
        vals = []
        for val in content:
            if val not in options:
                raise ValueError(f"Invalid option: {val}. Must be one of {options}.")
            vals.append({"name": val})
        return {name: {"multi_select": vals}}

    def _diff(property_data: Dict[str, Any], content: List[str]) -> bool:
        if "multi_select" not in property_data:
            return True
        vals = [v["name"] for v in property_data["multi_select"]]
        if set(vals) == set(content):
            return False
        if {s.lower() for s in vals} == {s.lower() for s in content}:
            logger.warn(f"Case Warning!\n{vals} | {content}\n")
        return True

    return NotionProperty(
        name=name,
        type="multi_select",
        additional={"multi_select": {"options": [{"name": opt} for opt in options]}},
        _update=_update,
        _diff=_diff,
    )


def relation(name: str, related_db: str, dual: bool = False) -> NotionProperty:
    """A relation between two databases. dual indicates a bi-directional relation."""
    relation_type = "dual_property" if dual else "single_property"

    def _update(page_ids: List[str]) -> Dict[str, Any]:
        return {name: {"relation": [{"id": page_id} for page_id in page_ids]}}

    def _diff(property_data: Dict[str, Any], related_page_ids: List[str]) -> bool:
        existing_ids = {relation["id"] for relation in property_data.get("relation", [])}
        return existing_ids != set(related_page_ids)

    return NotionProperty(
        name=name,
        type="relation",
        additional={
            "relation": {
                "database_id": related_db,
                "type": relation_type,
                relation_type: {},
            }
        },
        _update=_update,
        _diff=_diff,
    )


def title(name: str) -> NotionProperty:
    """The title property is special as it is the title of a page.

    All Notion databases have this property auotmatically, and it seems to have a different field
    name each time.
    """

    def _update(content: str) -> Dict[str, Any]:
        return {name: {"type": "title", "title": [{"text": {"content": content}}]}}

    def _diff(property_data: Dict[str, Any], content: str) -> bool:
        if "title" not in property_data:
            return True
        if len(property_data["title"]) == 0:
            return True
        if property_data["title"][0]["plain_text"] != content:
            return True
        return False

    return NotionProperty(name=name, type="title", additional={}, _update=_update, _diff=_diff)


def people(name: str) -> NotionProperty:
    """The Person/People property in Notion. Assign people to this Property."""

    def _update(content: str) -> Dict[str, Any]:
        vals = []
        for val in content:
            vals.append({"object": "user", "id": val})

        return {name: {"type": "people", "people": vals}}

    def _diff(property_data: Dict[str, Any], content: str) -> bool:
        if "people" not in property_data:
            return True
        vals = [v["id"] for v in property_data["people"]]
        return set(vals) != set(content)

    return NotionProperty(name=name, type="people", additional={}, _update=_update, _diff=_diff)
