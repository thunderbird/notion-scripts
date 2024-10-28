from dataclasses import dataclass, field
from typing import Any, Dict, List, Callable

@dataclass
class NotionProperty:
    """
    Defines a generic Notion database property. It must contain functions to let you check whether
    a property's content differs from input content, and a function to return the correct structure
    to update the property's contents in a Notion database page.
    """
    name: str
    type: str
    additional: Dict[str, Any] = field(default_factory=dict)
    _update: Callable[[Any], Dict[str, Any]] = None
    _diff: Callable[[Dict[str, Any], Any], bool] = None

    def to_dict(self):
        """ Returns a dict that defines this property in the Notion API format. """
        return {
            'name': self.name,
            'type': self.type,
            **self.additional
        }

    def update_content(self, content: Any):
        """ Returns `content` formatted in the right way for the Notion API to accept. """
        if self._update:
            return self._update(content)
        else:
            raise ValueError("No update function defined.")

    def is_prop_diff(self, property_data: Dict[str, Any], content: Any) -> bool:
        """ Logic to return whether `property_data` is different from `content` for this property type. """
        if self._diff:
            return self._diff(property_data, content)
        else:
            raise ValueError(f"No diff function defined for {self.name} property.")

class NotionDatabase:
    """
    Defines the structure of a Notion database and its properties, and additionally contains methods to
    add, delete, and update pages inside the database.
    The Status property is special and can't be modified by the Notion API.
    Similarly, the Title property can't be deleted or modified, though the name can be changed.
    """
    def __init__(self, database_id: str, notion_client: Any, properties: List[NotionProperty] = None):
        self.properties: Dict[str, NotionProperty] = {}
        if properties:
            for prop in properties:
                self.add_property(prop)
        self.notion = notion_client
        self.database_id = database_id

    def get_all_pages(self):
        """ Gets all pages currently in the Notion database. """
        pages = []
        cursor = None

        while True:
            response = self.notion.databases.query(
                self.database_id,
                start_cursor=cursor,
                page_size=100
            )
            pages.extend(response["results"])
            cursor = response.get("next_cursor")

            if cursor is None:
                break

        return pages

    def dict_to_page(self, datadict):
        """
        Takes a `datadict` and returns a Notion database page formatted for the Notion API.
        A datadict is a dictionary containing {<property_name>: <data>}.
        """
        props = self.properties

        page = {
            "Status": {"status": {"name": datadict.pop('Status')}}
        }

        for key, value in datadict.items():
            if key in props:
                page.update(props[key].update_content(value))

        return page

    def create_page(self, datadict):
        """
        Create a new page in the Notion database.
        `datadict` must be a dictionary containing {<property_name>: <data>}.
        """
        page_data = self.dict_to_page(datadict)
        if page_data:
            self.notion.pages.create(parent={"database_id": self.database_id}, properties=page_data)
            return True
        return False

    def delete_page(self, page_id):
        """Delete a page in the remote Notion database by `page_id`."""
        self.notion.pages.update(page_id, archived=True)

    def update_page(self, page, datadict):
        """Update `page` with the data in `datadict`. Updates only occur if `page` and `datadict` are different."""
        if self.page_diff(datadict, page):
            data = self.dict_to_page(datadict)
            self.notion.pages.update(page_id, properties=data)
            return True
        return False

    def page_diff(self, datadict: Dict[str, Any], page: Dict[str, Any]) -> bool:
        """Return true or false based on whether the Notion `datadict` matches page2 or not."""
        cur_props = self.properties
        for prop_name, prop_value in datadict.items():
            if prop_name in cur_props and cur_props[prop_name].is_prop_diff(page["properties"].get(prop_name, {}), prop_value):
                return True
        return False

    def add_property(self, prop: NotionProperty):
        """Adds a property to the local instance of the Notion database."""
        self.properties[prop.name] = prop

    def to_dict(self):
        """Returns the property definition in the right format to modify a Notion database."""
        return {name: prop.to_dict() for name, prop in self.properties.items()}

    def update_props(self):
        """Updates the properties of the remote Notion database tied to the local instance."""
        # TODO: This method could use some error checking and verifying that it worked properly.
        desired_props = self.to_dict()

        # Fetch the current properties of the database.
        current_db = self.notion.databases.retrieve(database_id=self.database_id)
        current_props = current_db["properties"]

        # Process current properties: delete properties not in desired list, and add/update missing ones
        # The status and title properties cannot be deleted via the API.
        for prop_name, prop_info in current_props.items():
            if prop_name not in desired_props and prop_info["type"] not in ["status", "title"]:
                self.notion.databases.update(
                    database_id=self.database_id,
                    properties={prop_name: None}
                )

        # Add or update missing properties
        for prop_name, prop_schema in desired_props.items():
            if prop_name not in current_props or current_props[prop_name]["type"] != prop_schema["type"]:
                if prop_schema["type"] == 'title':
                    # The title property always has the id "title" so can be renamed that way.
                    properties = {"title": {"name": prop_name}}
                else:
                    properties = {prop_name: prop_schema}
                self.notion.databases.update(
                    database_id=self.database_id,
                    properties=properties
                )

# Property creation functions
# Each must have an _update function and _diff function.
# _update is used to return content formatted to be a Notion page.
# _diff returns whether or not a Notion page contains the same data as the input content.

def link(name: str) -> NotionProperty:
    def _update(content: str) -> Dict[str, Any]:
        return {name: {"url": content}}

    def _diff(property_data: Dict[str, Any], content: str) -> bool:
        if "url" not in property_data:
            return True
        if property_data.get("url") != content:
            return True
        return False

    return NotionProperty(name=name, type='url', additional={'url': {}}, _update=_update, _diff=_diff)


def rich_text(name: str) -> NotionProperty:
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

    return NotionProperty(name=name, type='rich_text', additional={'rich_text': {}}, _update=_update, _diff=_diff)


def number(name: str) -> NotionProperty:
    def _update(content: int) -> Dict[str, Any]:
        return {name: {"number": content}}

    def _diff(property_data: Dict[str, Any], content: int) -> bool:
        if "number" not in property_data:
            return True
        if property_data.get("number") != content:
            return True
        return False

    return NotionProperty(name=name, type='number', additional={'number': {}}, _update=_update, _diff=_diff)


def select(name: str, options: List[str]) -> NotionProperty:
    def _update(content: str) -> Dict[str, Any]:
        if content not in options:
            raise ValueError(f"Invalid option: {content}. Must be one of {options}.")
        return {name: {"select": {"name": content}}}

    def _diff(property_data: Dict[str, Any], content: str) -> bool:
        if "select" not in property_data:
            return True
        if property_data.get("select", {}).get("name") != content:
            return True
        return False

    return NotionProperty(name=name, type='select', additional={'select': {'options': [{'name': option} for option in options]}}, _update=_update, _diff=_diff)


# This is a special text field that cannot have its type changed. All Notion databases automatically have a title property.
def title(name: str) -> NotionProperty:
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

    return NotionProperty(name=name, type='title', additional={}, _update=_update, _diff=_diff)
