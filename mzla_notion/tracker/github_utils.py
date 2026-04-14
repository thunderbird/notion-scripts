import datetime

from ..github_schema import schema


# Normalization and comparison helpers
def normalize_outbound_field_value(value):
    """Normalize values before outbound comparison/mutation payload construction."""
    if value in (None, ""):
        return None
    if isinstance(value, datetime.datetime):
        return value.date().isoformat()
    if isinstance(value, datetime.date):
        return value.isoformat()
    return value


def build_scalar_field_update(data_type, value):
    """Build a normalized scalar field update payload."""
    normalized = normalize_outbound_field_value(value)
    if normalized is None:
        return {"delete": True}
    if data_type == "TEXT":
        return {"text_value": str(normalized)}
    if data_type == "NUMBER":
        return {"number_value": float(normalized)}
    if data_type == "DATE":
        return {"date_value": str(normalized)}
    raise Exception(f"Unsupported scalar field data type '{data_type}'")


def extract_project_item_old_value(project_item_value, data_type):
    """Extract and normalize old values from a project item field."""
    if data_type == "TEXT":
        return normalize_outbound_field_value(project_item_value.text if project_item_value else None)
    if data_type == "DATE":
        return normalize_outbound_field_value(project_item_value.date if project_item_value else None)
    if data_type == "SINGLE_SELECT":
        return normalize_outbound_field_value(project_item_value.name if project_item_value else None)
    if data_type == "ITERATION":  # pragma: no cover
        return normalize_outbound_field_value(project_item_value.iteration_id if project_item_value else None)
    raise Exception("Unknown type " + data_type)


def field_value_changed(old_value, new_value):
    """Compare field values with normalization applied to both sides."""
    return normalize_outbound_field_value(old_value) != normalize_outbound_field_value(new_value)


# Option helpers
def find_option_id(options, option_name):
    """Find a single-select option id by its name."""
    for option in options:
        if option.name == option_name:
            return option.id

    return None


# Mutation payload helpers
def project_field_value_from_update(data_type, update):
    """Map normalized update payload to project mutation value shape."""
    if "single_select_option_id" in update:
        return {"single_select_option_id": update["single_select_option_id"]}
    if "text_value" in update:
        return {"text": update["text_value"]}
    if "number_value" in update:
        return {"number": update["number_value"]}
    if "date_value" in update:
        return {"date": update["date_value"]}
    if "delete" in update:
        if data_type == "SINGLE_SELECT":
            return {"single_select_option_id": None}
        if data_type == "TEXT":
            return {"text": None}
        if data_type == "NUMBER":
            return {"number": None}
        if data_type == "DATE":
            return {"date": None}
    raise Exception(f"Unsupported project field update for '{data_type}'")


# GraphQL query-shape helper
def issue_field_ops(issue):
    """Set the fields we need for project sync on the GraphQL operation."""
    issue.title()
    issue.number()
    issue.updated_at()
    issue.created_at()
    issue.closed_at()
    issue.title()
    issue.state()
    issue.state_reason()
    issue.url()
    issue.id()
    issue.body()
    issue.parent.id()
    issue.parent.number()
    issue.parent.repository.name_with_owner()
    issue.repository.id()
    issue.repository.name_with_owner()
    issue.repository.name()
    issue.repository.is_private()
    issue.labels(first=100).nodes.name()
    issue.issue_type.id()
    issue.issue_type.name()

    assignees = issue.assignees(first=10)
    assignees.nodes.id()
    assignees.nodes.login()

    issue_field_values = issue.issue_field_values(first=20)
    issue_field_single_select = issue_field_values.nodes.__as__(schema.IssueFieldSingleSelectValue)
    issue_field_single_select.name()
    issue_field_single_select.value()
    issue_field_single_select.option_id()
    issue_field_single_select.field.__as__(schema.IssueFieldSingleSelect).id()

    issue_field_number = issue_field_values.nodes.__as__(schema.IssueFieldNumberValue)
    issue_field_number.value()
    issue_field_number.field.__as__(schema.IssueFieldNumber).id()

    issue_field_text = issue_field_values.nodes.__as__(schema.IssueFieldTextValue)
    issue_field_text.value()
    issue_field_text.field.__as__(schema.IssueFieldText).id()

    issue_field_date = issue_field_values.nodes.__as__(schema.IssueFieldDateValue)
    issue_field_date.value()
    issue_field_date.field.__as__(schema.IssueFieldDate).id()

    timeline_items = issue.timeline_items(last=50, item_types=["CROSS_REFERENCED_EVENT"])
    crossref_events = timeline_items.nodes.__as__(schema.CrossReferencedEvent)
    crossref_events.will_close_target()
    pull_request = crossref_events.source.__as__(schema.PullRequest)
    pull_request.url()
    pull_request_reviewer = pull_request.review_requests(first=10).nodes.requested_reviewer.__as__(schema.User)
    pull_request_reviewer.id()
    pull_request_reviewer.login()

    project_items = issue.project_items(first=10, include_archived=True).nodes
    project_items.id()

    project = project_items.project.__as__(schema.ProjectV2)
    project.id()
    project.number()
    project.title()
    project.__fields__("id", "title", "number")

    project_items.project.__as__(schema.Node).id()

    fieldvalue = project_items.field_value_by_name(name="Start Date", __alias__="start_date").__as__(
        schema.ProjectV2ItemFieldDateValue
    )
    fieldvalue.__as__(schema.ProjectV2ItemFieldValueCommon).field.__as__(schema.ProjectV2FieldCommon).id()
    fieldvalue.date()

    fieldvalue = project_items.field_value_by_name(name="Target Date", __alias__="target_date").__as__(
        schema.ProjectV2ItemFieldDateValue
    )
    fieldvalue.__as__(schema.ProjectV2ItemFieldValueCommon).field.__as__(schema.ProjectV2FieldCommon).id()
    fieldvalue.date()

    fieldvalue = project_items.field_value_by_name(name="Status", __alias__="status").__as__(
        schema.ProjectV2ItemFieldSingleSelectValue
    )
    fieldvalue.field.__as__(schema.ProjectV2FieldCommon).id()
    fieldvalue.name()
    fieldvalue.option_id()

    fieldvalue = project_items.field_value_by_name(name="Sprint", __alias__="sprint").__as__(
        schema.ProjectV2ItemFieldIterationValue
    )
    fieldvalue.field.__as__(schema.ProjectV2FieldCommon).id()
    fieldvalue.iteration_id()
    fieldvalue.start_date()
    fieldvalue.title()
    fieldvalue.duration()
