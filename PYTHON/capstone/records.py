"""Logic for the Personal Data Manager. No user-interface code lives here."""
import json
from datetime import datetime

REQUIRED_FIELDS = ("id", "title", "description", "category", "created_at", "updated_at")


def now():
    """Return the current time as ISO 8601 text, for example 2026-01-15T09:00:00."""
    return datetime.now().isoformat(timespec="seconds")


def validate(title, category):
    """Return an error message for invalid input, or None when it is valid."""
    if not title or not title.strip():
        return "A title is required."
    if not category or not category.strip():
        return "A category is required."
    return None


def next_id(records):
    """Return one more than the highest id in use (1 for an empty list)."""
    return max((record["id"] for record in records), default=0) + 1


def find(records, record_id):
    """Return the record with this id, or None."""
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def add_record(records, title, description, category, clock=now):
    """Add a record. Return (record, None) on success or (None, message) on failure."""
    problem = validate(title, category)
    if problem:
        return None, problem
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
    """Change fields of a record. created_at and id never change."""
    record = find(records, record_id)
    if record is None:
        return None, "No record has that id."
    problem = validate(changes.get("title", record["title"]), changes.get("category", record["category"]))
    if problem:
        return None, problem
    for key, value in changes.items():
        if key not in ("id", "created_at"):
            record[key] = value.strip() if isinstance(value, str) else value
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
    """Return records whose title or description contains the text (ignoring case)."""
    needle = text.strip().lower()
    return [r for r in records if needle in r["title"].lower() or needle in r["description"].lower()]


def describe(record):
    """One line of plain text for a record; status is shown in words, never by color."""
    status = "done" if record.get("done") else "not done"
    return f"{record['id']}. {record['title']} [{record['category']}] ({status})"


def save_records(path, records):
    """Write records to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


def load_records(path):
    """Return (records, None) or ([], message). A missing file is not an error."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return [], None
    except json.JSONDecodeError:
        return [], f"{path} is not valid JSON, so the list starts empty."
    if not isinstance(data, list) or not all(isinstance(r, dict) and all(f in r for f in REQUIRED_FIELDS) for r in data):
        return [], f"{path} does not contain valid records, so the list starts empty."
    return data, None
