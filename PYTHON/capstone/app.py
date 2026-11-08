"""Personal Data Manager: a NiceGUI front end for records.py."""
import os
from pathlib import Path

from nicegui import ui

import records as store

DATA_FILE = Path(os.environ.get("PDM_DATA_FILE", "data.json"))
items, load_problem = store.load_records(DATA_FILE)


@ui.page("/")
def main_page():
    ui.page_title("Personal Data Manager")
    ui.label("Personal Data Manager").classes("text-2xl")

    # A plain-text status line. aria-live asks assistive technology to announce changes.
    status = ui.label(load_problem or "Ready.").props('role="status" aria-live="polite"')

    def say(message, ok=True):
        status.set_text(message)
        ui.notify(message, type="positive" if ok else "negative")

    ui.label("Add a record")
    title = ui.input(label="Record title")
    description = ui.input(label="Record description")
    category = ui.input(label="Record category")

    ui.label("Find records")
    search_text = ui.input(label="Search title or description")

    ui.label("Records")
    list_column = ui.column()

    ui.label("Change one record")
    chooser = ui.select(options={}, label="Choose a record")
    new_title = ui.input(label="New title (leave blank to keep)")
    new_category = ui.input(label="New category (leave blank to keep)")

    def refresh():
        shown = store.search(items, search_text.value) if search_text.value else items
        list_column.clear()
        with list_column:
            if not shown:
                ui.label("No records to show.")
            for record in shown:
                ui.label(store.describe(record))
                if record["description"]:
                    ui.label("Details: " + record["description"])
        chooser.set_options({r["id"]: store.describe(r) for r in items})

    def add_clicked():
        record, problem = store.add_record(items, title.value, description.value, category.value)
        if problem:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        title.set_value("")
        description.set_value("")
        category.set_value("")
        refresh()
        say(f"Added record {record['id']}: {record['title']}.")

    def change_clicked():
        if chooser.value is None:
            say("Choose a record first.", ok=False)
            return
        changes = {}
        if new_title.value.strip():
            changes["title"] = new_title.value
        if new_category.value.strip():
            changes["category"] = new_category.value
        if not changes:
            say("Enter a new title or a new category.", ok=False)
            return
        record, problem = store.update_record(items, chooser.value, changes)
        if problem:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        new_title.set_value("")
        new_category.set_value("")
        refresh()
        say(f"Updated record {record['id']}.")

    def complete_clicked():
        if chooser.value is None:
            say("Choose a record first.", ok=False)
            return
        record, problem = store.complete_record(items, chooser.value)
        if problem:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        refresh()
        say(f"Marked record {record['id']} as done.")

    def delete_clicked():
        if chooser.value is None:
            say("Choose a record first.", ok=False)
            return
        record_id = chooser.value
        ok, problem = store.delete_record(items, record_id)
        if not ok:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        chooser.set_value(None)
        refresh()
        say(f"Deleted record {record_id}.")

    ui.button("Add record", on_click=add_clicked)
    search_text.on_value_change(lambda _: refresh())
    ui.button("Change selected record", on_click=change_clicked)
    ui.button("Mark selected record done", on_click=complete_clicked)
    ui.button("Delete selected record", on_click=delete_clicked)
    refresh()


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Personal Data Manager", reload=False, show=False)
