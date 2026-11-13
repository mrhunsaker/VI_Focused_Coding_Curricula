import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import records


def make_clock():
    state = {"n": 0}

    def clock():
        state["n"] += 1
        return f"2026-01-15T10:00:{state['n']:02d}"
    return clock


class TestRecords(unittest.TestCase):
    def setUp(self):
        self.clock = make_clock()
        self.items = []
        records.add_record(self.items, "Notebook", "Course notes", "supplies", self.clock)
        records.add_record(self.items, "Pencil", "Box of 10", "supplies", self.clock)
        records.add_record(self.items, "Study plan", "Weekly schedule", "planning", self.clock)

    def test_empty_title_and_category_are_rejected(self):
        record, message = records.add_record(self.items, "   ", "x", "supplies", self.clock)
        self.assertIsNone(record)
        self.assertEqual(message, "A title is required.")
        record, message = records.add_record(self.items, "Valid", "x", " ", self.clock)
        self.assertIsNone(record)
        self.assertEqual(message, "A category is required.")
        self.assertEqual(len(self.items), 3)

    def test_new_record_gets_an_unused_id(self):
        records.delete_record(self.items, 2)
        record, _ = records.add_record(self.items, "Ruler", "30 cm", "supplies", self.clock)
        self.assertEqual(record["id"], 4)

    def test_update_changes_updated_at_but_not_created_at(self):
        before = dict(records.find(self.items, 1))
        updated, problem = records.update_record(self.items, 1, {"description": "Lecture notes"}, self.clock)
        self.assertIsNone(problem)
        self.assertEqual(updated["created_at"], before["created_at"])
        self.assertNotEqual(updated["updated_at"], before["updated_at"])

    def test_update_rejects_identity_and_timestamp_fields_without_mutation(self):
        before = dict(self.items[0])
        for field in ("id", "created_at", "updated_at", "unknown"):
            updated, problem = records.update_record(self.items, 1, {field: "tampered"}, self.clock)
            self.assertIsNone(updated)
            self.assertIn("cannot be updated", problem)
            self.assertEqual(self.items[0], before)

    def test_update_validates_types_before_mutating(self):
        before = dict(self.items[0])
        updated, problem = records.update_record(self.items, 1, {"done": "yes"}, self.clock)
        self.assertIsNone(updated)
        self.assertIn("true or false", problem)
        self.assertEqual(self.items[0], before)

    def test_delete_removes_only_that_record(self):
        ok, _ = records.delete_record(self.items, 2)
        self.assertTrue(ok)
        self.assertEqual([r["id"] for r in self.items], [1, 3])

    def test_save_and_reload_preserves_all_fields(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            records.save_records(path, self.items)
            loaded, message = records.load_records(path)
        self.assertIsNone(message)
        self.assertEqual(loaded, self.items)

    def test_save_rejects_invalid_data_before_writing(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            with self.assertRaises(ValueError):
                records.save_records(path, [{"id": 0}])
            self.assertFalse(path.exists())

    def test_damaged_json_gives_an_empty_list_and_a_message(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            path.write_text('[{"id": 1,', encoding="utf-8")
            loaded, message = records.load_records(path)
        self.assertEqual(loaded, [])
        self.assertIn("not valid UTF-8 JSON", message)

    def test_invalid_utf8_is_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            path.write_bytes(b"\xff")
            loaded, message = records.load_records(path)
        self.assertEqual(loaded, [])
        self.assertIn("not valid UTF-8 JSON", message)

    def test_missing_file_is_a_normal_first_run(self):
        with tempfile.TemporaryDirectory() as folder:
            loaded, message = records.load_records(Path(folder) / "missing.json")
        self.assertEqual(loaded, [])
        self.assertIsNone(message)

    def test_unreadable_file_returns_a_message(self):
        with patch("builtins.open", side_effect=PermissionError("denied")):
            loaded, message = records.load_records("restricted.json")
        self.assertEqual(loaded, [])
        self.assertIn("Could not read", message)

    def test_schema_rejects_duplicate_ids_and_invalid_types(self):
        duplicate = [dict(self.items[0]), dict(self.items[0])]
        self.assertIn("duplicated", records.validate_records(duplicate))
        invalid = dict(self.items[0], id=True)
        self.assertIn("positive integer", records.validate_record(invalid))
        invalid = dict(self.items[0], done="false")
        self.assertIn("true or false", records.validate_record(invalid))
        invalid = dict(self.items[0], extra="field")
        self.assertIn("unsupported fields", records.validate_record(invalid))

    def test_schema_rejects_invalid_timestamps(self):
        invalid = dict(self.items[0], created_at="yesterday")
        self.assertIn("ISO 8601", records.validate_record(invalid))

    def test_complete_marks_done_and_updates(self):
        record, _ = records.complete_record(self.items, 3, self.clock)
        self.assertTrue(record["done"])
        self.assertNotEqual(record["updated_at"], record["created_at"])

    def test_search_is_case_insensitive_across_all_documented_fields(self):
        self.assertEqual([r["title"] for r in records.search(self.items, "NOTE")], ["Notebook"])
        self.assertEqual([r["title"] for r in records.search(self.items, "box")], ["Pencil"])
        self.assertEqual([r["title"] for r in records.search(self.items, "PLANNING")], ["Study plan"])

    def test_blank_title_cannot_be_saved_by_update(self):
        record, message = records.update_record(self.items, 1, {"title": ""}, self.clock)
        self.assertIsNone(record)
        self.assertEqual(message, "A title is required.")


if __name__ == "__main__":
    unittest.main()
