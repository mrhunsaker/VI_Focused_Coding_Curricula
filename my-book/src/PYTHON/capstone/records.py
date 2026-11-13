"""Validated domain and JSON persistence logic for the Personal Data Manager."""

import json
import os
import tempfile
from datetime import datetime
from pathlib import Path

REQUIRED_FIELDS = ("id", "title", "description", "category", "created_at", "updated_at")
ALLOWED_FIELDS = frozenset((*REQUIRED_FIELDS, "done"))
EDITABLE_FIELDS = frozenset(("title", "description", "category", "done"))


def now():
    """Return the current time as ISO 8601 text."""
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _is_timestamp(value):
    if not isinstance(value, str) or "T" not in value:
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def validate(title, category):
    """Return an error message for invalid required text fields."""
    if not isinstance(title, str) or not title.strip():
        return "A title is required."
    if not isinstance(category, str) or not category.strip():
        return "A category is required."
    return None


def validate_record(record):
    """Return an error message when a record violates the stored schema."""
    if not isinstance(record, dict):
        return "Each record must be a JSON object."
    missing = [field for field in REQUIRED_FIELDS if field not in record]
    if missing:
        return "Record is missing required fields: " + ", ".join(missing) + "."
    unknown = sorted(set(record) - ALLOWED_FIELDS)
    if unknown:
        return "Record contains unsupported fields: " + ", ".join(unknown) + "."
    record_id = record["id"]
    if isinstance(record_id, bool) or not isinstance(record_id, int) or record_id <= 0:
        return "Record id must be a positive integer."
    problem = validate(record["title"], record["category"])
    if problem:
        return problem
    if not isinstance(record["description"], str):
        return "Record description must be text."
    for field in ("created_at", "updated_at"):
        if not _is_timestamp(record[field]):
            return f"Record {field} must be an ISO 8601 timestamp."
    if "done" in record and not isinstance(record["done"], bool):
        return "Record done must be true or false."
    return None


def validate_records(records):
    """Validate a complete list, including uniqueness of positive IDs."""
    if not isinstance(records, list):
        return "The data file must contain a JSON list of records."
    seen = set()
    for record in records:
        problem = validate_record(record)
        if problem:
            return problem
        if record["id"] in seen:
            return f"Record id {record['id']} is duplicated."
        seen.add(record["id"])
    return None


def next_id(records):
    """Return one more than the highest id currently in use."""
    return max((record["id"] for record in records), default=0) + 1


def find(records, record_id):
    """Return the record with this id, or None."""
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def add_record(records, title, description, category, clock=now):
    """Add a record. Return (record, None) or (None, error message)."""
    problem = validate(title, category)
    if problem:
        return None, problem
    if description is not None and not isinstance(description, str):
        return None, "A description must be text."
    stamp = clock()
    record = {
        "id": next_id(records),
        "title": title.strip(),
        "description": (description or "").strip(),
        "category": category.strip(),
        "created_at": stamp,
        "updated_at": stamp,
        "done": False,
    }
    records.append(record)
    return record, None


def update_record(records, record_id, changes, clock=now):
    """Apply only supported edits; never permit callers to alter identity/timestamps."""
    record = find(records, record_id)
    if record is None:
        return None, "No record has that id."
    if not isinstance(changes, dict):
        return None, "Changes must be supplied as a field dictionary."
    unsupported = sorted(set(changes) - EDITABLE_FIELDS)
    if unsupported:
        return None, "These fields cannot be updated: " + ", ".join(unsupported) + "."
    candidate = dict(record)
    candidate.update(changes)
    problem = validate_record(candidate)
    if problem:
        return None, problem
    record.update({
        key: value.strip() if isinstance(value, str) else value
        for key, value in changes.items()
    })
    record["updated_at"] = clock()
    return record, None


def complete_record(records, record_id, clock=now):
    """Mark a record done; this counts as an update."""
    return update_record(records, record_id, {"done": True}, clock)


def delete_record(records, record_id):
    """Remove one record. Return (True, None) or (False, message)."""
    record = find(records, record_id)
    if record is None:
        return False, "No record has that id."
    records.remove(record)
    return True, None


def search(records, text):
    """Case-insensitive search across title, description, and category."""
    needle = text.strip().casefold()
    return [
        record for record in records
        if needle in record["title"].casefold()
        or needle in record["description"].casefold()
        or needle in record["category"].casefold()
    ]


def describe(record):
    """Return one line of plain text; status is never conveyed by color alone."""
    status = "done" if record.get("done") else "not done"
    return f"{record['id']}. {record['title']} [{record['category']}] ({status})"


def save_records(path, records):
    """Validate and atomically replace a UTF-8 JSON data file.

    OSError is intentionally propagated so the UI/caller can report a storage failure.
    """
    problem = validate_records(records)
    if problem:
        raise ValueError(problem)
    destination = Path(path)
    temporary_name = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=destination.parent,
            prefix=f".{destination.name}.",
            suffix=".tmp",
            delete=False,
        ) as file:
            temporary_name = file.name
            json.dump(records, file, indent=4, ensure_ascii=False)
            file.write("\n")
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary_name, destination)
    finally:
        if temporary_name and os.path.exists(temporary_name):
            os.unlink(temporary_name)


def load_records(path):
    """Return (records, None) or ([], explanatory message).

    A missing file is a normal first-run state. Other filesystem, encoding, JSON,
    schema, and duplicate-ID failures are returned to the caller as messages.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return [], None
    except (json.JSONDecodeError, UnicodeDecodeError):
        return [], f"{path} is not valid UTF-8 JSON, so the list starts empty."
    except OSError as error:
        return [], f"Could not read {path}: {error.strerror or error}."
    problem = validate_records(data)
    if problem:
        return [], f"{path} contains invalid records ({problem}), so the list starts empty."
    return data, None
