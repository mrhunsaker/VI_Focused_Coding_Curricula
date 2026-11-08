import json
import tempfile
import unittest
from pathlib import Path

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

    def test_1_empty_title_is_rejected(self):
        record, message = records.add_record(self.items, "   ", "x", "supplies", self.clock)
        self.assertIsNone(record)
        self.assertEqual(message, "A title is required.")
        self.assertEqual(len(self.items), 3)

    def test_2_new_record_gets_an_unused_id(self):
        records.delete_record(self.items, 2)
        record, _ = records.add_record(self.items, "Ruler", "30 cm", "supplies", self.clock)
        self.assertEqual(record["id"], 4)

    def test_3_update_changes_updated_at_but_not_created_at(self):
        before = dict(records.find(self.items, 1))
        records.update_record(self.items, 1, {"description": "Lecture notes"}, self.clock)
        after = records.find(self.items, 1)
        self.assertEqual(after["created_at"], before["created_at"])
        self.assertNotEqual(after["updated_at"], before["updated_at"])

    def test_4_delete_removes_only_that_record(self):
        ok, _ = records.delete_record(self.items, 2)
        self.assertTrue(ok)
        self.assertEqual([r["id"] for r in self.items], [1, 3])

    def test_5_save_and_reload_preserves_all_fields(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            records.save_records(path, self.items)
            loaded, message = records.load_records(path)
        self.assertIsNone(message)
        self.assertEqual(loaded, self.items)

    def test_damaged_file_gives_an_empty_list_and_a_message(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            path.write_text('[{"id": 1,', encoding="utf-8")
            loaded, message = records.load_records(path)
        self.assertEqual(loaded, [])
        self.assertIn("not valid JSON", message)

    def test_complete_marks_done_and_updates(self):
        record, _ = records.complete_record(self.items, 3, self.clock)
        self.assertTrue(record["done"])
        self.assertNotEqual(record["updated_at"], record["created_at"])

    def test_search_ignores_case_and_checks_description(self):
        self.assertEqual([r["title"] for r in records.search(self.items, "NOTE")], ["Notebook"])
        self.assertEqual([r["title"] for r in records.search(self.items, "box")], ["Pencil"])

    def test_blank_title_cannot_be_saved_by_update(self):
        record, message = records.update_record(self.items, 1, {"title": ""}, self.clock)
        self.assertIsNone(record)
        self.assertEqual(message, "A title is required.")


if __name__ == "__main__":
    unittest.main()
