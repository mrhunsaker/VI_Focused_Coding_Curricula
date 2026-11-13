"""Personal Data Manager, version for Lesson 11.3: add, list, and search."""
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

    ui.button("Add record", on_click=add_clicked)
    search_text.on_value_change(lambda _: refresh())
    refresh()


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Personal Data Manager", reload=False, show=False)
