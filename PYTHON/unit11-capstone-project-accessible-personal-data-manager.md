# Unit 11: Capstone Project — Accessible Personal Data Manager

## Overview

Students develop a fully functional personal data manager that is built to work with a screen reader and keyboard. The program keeps a list of structured records, lets the user add, view, search, change, complete, and delete them, and saves them to a JSON file. The Python track builds it as a small local web application with NiceGUI. The other language tracks build a text-based version with the same records, rules, and tests.

<<<<<<< HEAD
**Project Goal:** Build an application to manage structured records with list, add, search, update, delete, and JSON persistence operations. The interface may be GUI-based in Python; the same data contract and operation semantics apply to the Lua terminal implementation.

**Project Options:**
- Contact Manager
- Book/Movie Tracker
- Study Notes Manager
- Personal Inventory

Every option uses the same six-field record schema (`id`, `title`, `description`, `category`, `created_at`, `updated_at`). The selected project domain changes the meaning of the field values, not the record shape or required operations.
=======
**Project goal.** Build a simple application that manages a list of structured items.

**Shared record schema (all general-purpose language tracks).** Every record has these fields: `id` (unique whole number), `title`, `description`, `category`, `created_at`, and `updated_at` (ISO 8601 text). A project may add fields but must not remove these. This course adds the optional field `done` (true or false).

**Project options (each builds on the shared schema):**
- Contact Manager: add phone and email fields
- Book/Movie Tracker: add author/director and status fields
- Simple To-Do List: add a done field and due date
- Simple Inventory: add quantity and location fields

**Shared sample data.** Use these three records for demonstrations and tests:
```json
[
  {"id": 1, "title": "Notebook", "description": "Course notes", "category": "supplies", "created_at": "2026-01-15T09:00:00", "updated_at": "2026-01-15T09:00:00"},
  {"id": 2, "title": "Pencil", "description": "Box of 10", "category": "supplies", "created_at": "2026-01-15T09:05:00", "updated_at": "2026-01-15T09:05:00"},
  {"id": 3, "title": "Study plan", "description": "Weekly schedule", "category": "planning", "created_at": "2026-01-15T09:10:00", "updated_at": "2026-01-15T09:10:00"}
]
```

**Shared acceptance tests.**
1. Adding a record with an empty title is rejected with a clear message.
2. A new record receives an unused `id`.
3. Updating a record changes `updated_at` but not `created_at`.
4. Deleting a record removes only that record.
5. Saving and reloading preserves all fields and values.
6. Every message and control can be used without color or a mouse (checked by hand, Lesson 11.5).

**Core functionality requirements.**
1. **Add New Item** — a form to enter the details of a new item.
2. **View All Items** — display items in a clear, accessible list.
3. **Edit Item** — select an existing item and change its details.
4. **Delete Item** — remove an item from the collection.
5. **Save/Load Data** — keep the data in a JSON file.
6. **Search Items** — find items whose title or description contains the entered text.
7. **Mark an Item Complete** — set the optional `done` field; this updates `updated_at`.

**Verified code.** The code in this unit is available as files in the `PYTHON/capstone/` folder of this repository. It was run with Python 3.12 and NiceGUI 3.19.0. The NiceGUI tests simulate the page in Python; they do not replace testing with a real browser and your own screen reader.

**Lessons in this unit.** 11.1 Introduction to NiceGUI; 11.2 Data Model and Storage; 11.3 Displaying and Searching Items; 11.4 Changing, Completing, and Deleting Items; 11.5 Testing, Documentation, and Final Submission.
>>>>>>> 2067a20 (curriculum clearning and updates)

---

## Lesson 11.1: Introduction to NiceGUI

<<<<<<< HEAD
1. **Add New Item** — A form to input details for a new item.
2. **View All Items** — Display items in a clear, accessible list format.
3. **Edit Item** — Select an existing item and modify its details.
4. **Search Items** — Find records by ID and case-insensitive text in title, description, or category; report no matches explicitly.
5. **Delete Item** — Remove an item from the collection and confirm the result.
6. **Save/Load Data** — Persist the data to a JSON file and validate the complete six-field schema on load.
=======
### Reading References
- NiceGUI documentation (official site, nicegui.io); check the documentation for the version you installed
- Matthes: Chapter 8 (Functions) and Chapter 9 (Classes) for the Python used in this capstone
>>>>>>> 2067a20 (curriculum clearning and updates)

### Learning Objectives
- Install NiceGUI with `uv` and start a page from the terminal.
- Explain that each `ui.` call creates an element and that an event handler runs when the user acts.
- Give every input a label and report results in a plain text status line.

### Concept Explanation

NiceGUI lets you build a web page in Python. When the program runs it starts a small web server on your own computer and prints an address, normally `http://localhost:8080`. You open that address in a browser. Nothing is sent to other people; the page is served only from your computer unless you choose otherwise.

**Setup.** Install the package into the project environment:
```bash
uv add nicegui
```
Windows PowerShell uses the same command:
```powershell
uv add nicegui
```

**Elements and handlers.** Each call such as `ui.label(...)`, `ui.input(...)`, or `ui.button(...)` creates an element on the page. A button takes an `on_click` function, called a *handler*, that runs when the user presses it. The code inside `@ui.page("/")` builds the page each time someone opens it.

**Starting the server.** `ui.run(...)` starts the server. Guard it with `if __name__ in {"__main__", "__mp_main__"}:` as NiceGUI requires. Pass `show=False` so that no browser is opened automatically, and `reload=False` while learning.

**Accessibility.** NiceGUI pages are ordinary web pages, so a screen reader reads them as any other page. Three habits make them usable: give every input a clear `label`, because the label text is what a screen reader announces for the field; report every result in a plain text label as well as in a pop-up, because a pop-up message disappears; and never use color as the only signal. The status label below uses the standard attributes `role="status"` and `aria-live="polite"`, which ask assistive technology to announce changes. Whether your screen reader announces them as intended must be tested with your own setup.

### Worked Example

<<<<<<< HEAD
**Task 2:** Define a data model class with all six canonical record fields:
```python
class PersonalRecord:
    def __init__(self, record_id, title, description, category,
                 created_at, updated_at):
        self.id = record_id
        self.title = title
        self.description = description
        self.category = category
        self.created_at = created_at
        self.updated_at = updated_at
=======
Save this as `hello_app.py`:
```python
from nicegui import ui


@ui.page("/")
def main_page():
    ui.page_title("Personal Data Manager")
    ui.label("Personal Data Manager")
    name = ui.input(label="Your name")
    greeting = ui.label("Type a name and press the button.").props('role="status" aria-live="polite"')

    def greet():
        if name.value.strip():
            greeting.set_text(f"Hello, {name.value.strip()}!")
        else:
            greeting.set_text("Please enter a name.")

    ui.button("Greet", on_click=greet)


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Personal Data Manager", reload=False, show=False)
>>>>>>> 2067a20 (curriculum clearning and updates)
```

Start it from the terminal and open the address that it prints:
```bash
uv run python hello_app.py
```

The repository also includes a user-level test, `test_hello_ui.py`, which needs `uv add --dev pytest pytest-asyncio`:
```python
from nicegui.testing import User

pytest_plugins = ["nicegui.testing.user_plugin"]


async def test_greeting(user: User) -> None:
    await user.open("/")
    await user.should_see("Personal Data Manager")
    user.find("Greet").click()
    await user.should_see("Please enter a name.")
    user.find("Your name").type("Avery")
    user.find("Greet").click()
    await user.should_see("Hello, Avery!")
```
```ini
# pytest.ini
[pytest]
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
main_file = hello_app.py
```

### Expected Behavior or Output

When the program starts, the terminal prints a line like this one (the address and port depend on your computer; the default port is 8080):
```text
NiceGUI ready to go on http://localhost:8080, and http://192.0.2.2:8080
```
The page title is Personal Data Manager. Pressing **Greet** with an empty field sets the status line to `Please enter a name.`; after typing `Avery` it says `Hello, Avery!`. Running the test with `python -m pytest -q test_hello_ui.py` prints:
```text
1 passed
```

### Common Mistakes

1. Calling `ui.run()` without the `__name__` guard, which can start the server twice.
2. Relying only on `ui.notify`, whose message disappears, instead of also updating a text status line.
3. Leaving an input without a label, so the screen reader announces only "edit text".
4. Starting a second copy of the program while the first still holds the port.

### Activities

1. Start `hello_app.py` and read the page title and the status line with your screen reader.
2. Change the greeting to include the time of day using a second input.
3. Run the test file and then break the greeting text on purpose to watch the test fail.
4. Add a second button that clears the name and sets the status line to `Name cleared.`

### Accessibility Practice

Open the page with the keyboard only: press Tab to move between the input and the button and read each stop. Check that the input's label is announced and that the status line is read after you press the button. Record the browser, screen reader, and version you tested, and do not claim the page is accessible to other setups.

### Skills Checklist

- [ ] I can install NiceGUI and start a page from the terminal.
- [ ] I can explain elements and event handlers.
- [ ] I can give every input a label.
- [ ] I can report results in a plain text status line.
- [ ] I can run a user-level test.

---

## Lesson 11.2: Data Model and Storage

### Reading References
- Matthes: Chapter 6 (Dictionaries) and Chapter 10 (Files and Exceptions)
- Python documentation: the `json` and `datetime` modules

### Learning Objectives
- Represent each record as a dictionary with the shared fields.
- Validate input and return a clear message when it is invalid.
- Save to and load from a JSON file, and handle a missing or damaged file.

### Concept Explanation

The data and the rules live in one module, `records.py`, that contains no user-interface code. Keeping logic separate from the page has two benefits: the rules can be tested without a browser, and the same logic can serve a different front end later.

Each record is a dictionary with the shared fields (`id`, `title`, `description`, `category`, `created_at`, `updated_at`) and the optional `done` field. Dictionaries convert directly to JSON.

**Rules.** A title and a category are required. A new record gets an `id` one higher than the highest in use. `created_at` is set once and never changes. `updated_at` changes whenever a record is updated, completed, or edited. Every function that can fail returns a clear message instead of raising an error that the user must interpret; functions return a pair `(result, message)`.

**Storage.** `save_records` writes the list as JSON. `load_records` treats a missing file as an empty list (this is normal on first use), and returns a message when the file is damaged or does not contain valid records, so the program never overwrites good data with an empty list without telling the user.

**Testable time.** Functions that stamp a record take a `clock` argument that defaults to the real time. Tests pass a fake clock so that timestamps are predictable.

### Worked Example

Save this as `records.py`:
```python
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
```

Try it with this short script, `demo.py`, in the same folder:
```python
import records

ticks = iter(range(1, 100))


def clock():
    return f"2026-01-15T10:00:{next(ticks):02d}"


items = []
records.add_record(items, "Notebook", "Course notes", "supplies", clock)
records.add_record(items, "Pencil", "Box of 10", "supplies", clock)
print(records.add_record(items, "  ", "x", "supplies", clock))
for item in items:
    print(records.describe(item))

records.save_records("data.json", items)
loaded, problem = records.load_records("data.json")
print(loaded == items, problem)
print(records.load_records("missing.json"))
```

### Expected Behavior or Output

Running `python demo.py` prints:
```text
(None, 'A title is required.')
1. Notebook [supplies] (not done)
2. Pencil [supplies] (not done)
True None
([], None)
```
The invalid record is rejected with `(None, 'A title is required.')`. The saved and reloaded list equals the original (`True None`), and a missing file gives an empty list with no message.

### Common Mistakes

1. Letting the user interface and the rules share the same code, so neither can be tested alone.
2. Overwriting `data.json` with an empty list after a failed load.
3. Changing `created_at` when a record is edited.
4. Reusing an old `id` by counting the list length instead of using the highest `id`.

### Activities

1. Run `demo.py` and open the saved `data.json`. Read the text aloud.
2. Add a rule that a title may not be longer than 60 characters, with a clear message.
3. Add an `is_done` filter function that returns only completed records.
4. Damage `data.json` by deleting a bracket and run `load_records` again; read the message it returns.

### Accessibility Practice

Messages are complete sentences that say what is wrong (`A title is required.`) so they read clearly in speech and braille. After saving, read `data.json` in the terminal; `indent=4` puts one field per line, which reads well line by line.

### Skills Checklist

- [ ] I can represent records as dictionaries.
- [ ] I can validate input and return clear messages.
- [ ] I can save and load JSON.
- [ ] I can handle a missing or damaged file.
- [ ] I can keep logic separate from the user interface.

---

## Lesson 11.3: Displaying and Searching Items

### Reading References
- NiceGUI documentation (official site, nicegui.io); check the documentation for the version you installed

### Learning Objectives
- Build a page that adds a record and lists all records.
- Filter the list as the user types in a search box.
- Show errors in a status line that is also announced.

### Concept Explanation

The page uses the functions from `records.py`. It builds a form for a new record, a search box, and a list. The list is rebuilt by one function, `refresh()`, that clears the list column and then creates one label per record. Calling `refresh()` after every change keeps the page and the data in step.

Each record is shown as one plain sentence produced by `describe()`, for example `1. Notebook [supplies] (not done)`. The status is the words *done* and *not done*, never a color or an icon alone. The description appears on its own line prefixed `Details:`.

The search box filters as the user types: `search_text.on_value_change(...)` calls `refresh()`, which uses `search()` when the box is not empty.

Every input has a unique label (`Record title`, `Record description`, `Record category`, `Search title or description`). Unique labels let a screen reader user tell the fields apart and let the tests find them.

### Worked Example

Save this as `app_v1.py` (it uses `records.py` from Lesson 11.2):
```python
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
```

The user-level test `test_app_v1_ui.py`:
```python
import os
import tempfile

from nicegui.testing import User

pytest_plugins = ["nicegui.testing.user_plugin"]
os.environ["PDM_DATA_FILE"] = os.path.join(tempfile.mkdtemp(), "data.json")


async def test_add_and_search(user: User) -> None:
    await user.open("/")
    await user.should_see("No records to show.")
    for title, description, category in [("Notebook", "Course notes", "supplies"), ("Pencil", "Box of 10", "supplies")]:
        user.find("Record title").type(title)
        user.find("Record description").type(description)
        user.find("Record category").type(category)
        user.find("Add record").click()
    await user.should_see("2. Pencil [supplies] (not done)")
    user.find("Search title or description").type("note")
    await user.should_see("1. Notebook [supplies] (not done)")
    await user.should_not_see("2. Pencil [supplies] (not done)")
    user.find("Add record").click()
    await user.should_see("A title is required.")
```
```ini
# pytest.ini
[pytest]
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
main_file = app_v1.py
```

### Expected Behavior or Output

Start the app with `uv run python app_v1.py` and open the printed address. With no records the list says `No records to show.` After adding Notebook and Pencil, the list shows `1. Notebook [supplies] (not done)` and `2. Pencil [supplies] (not done)`. Typing `note` in the search box leaves only the Notebook line. Pressing **Add record** with an empty title sets the status line to `A title is required.` Running the test prints:
```text
1 passed
```

### Common Mistakes

1. Building the list outside `refresh()`, so it is not updated when the data changes.
2. Using the same label text for two inputs, so the screen reader cannot tell them apart.
3. Showing a record's status only by color.
4. Forgetting to clear the form after a successful add, so the next record starts with old text.

### Activities

1. Add the three shared sample records through the page and compare the list with the sample data.
2. Add a category filter next to the search box.
3. Show the number of records after the list, for example `3 records.`
4. Break the `describe()` text on purpose and see which test fails.

### Accessibility Practice

Tab through the form and confirm that each field is announced with its label. After pressing **Add record**, listen for the status line. If your screen reader does not announce it, note the browser and screen reader you used, then add a visible sentence under the button as a fallback.

### Skills Checklist

- [ ] I can build a form and a list in NiceGUI.
- [ ] I can refresh the list after every change.
- [ ] I can filter the list with a search box.
- [ ] I can show status in words.
- [ ] I can give each input a unique label.

---

## Lesson 11.4: Changing, Completing, and Deleting Items

### Reading References
- NiceGUI documentation (official site, nicegui.io); check the documentation for the version you installed

### Learning Objectives
- Select a record from a list and change its title or category.
- Mark a record done and delete a record.
- Save after every successful change and report each result.

### Concept Explanation

The finished page adds a *chooser* (`ui.select`) that lists every record by its descriptive sentence, plus buttons to change, complete, or delete the chosen record. All three handlers follow the same pattern: check that a record is chosen, call the matching function in `records.py`, show the message if it failed, and otherwise save the file, refresh the list, and report what happened.

`update_record` changes only the fields that are supplied and always updates `updated_at`. `complete_record` is an update that sets `done` to `True`. `delete_record` removes exactly one record. After a delete the chooser is cleared so a stale choice cannot be used.

Notice that the handlers contain no rules. A rule such as "a title is required" exists once, in `records.py`, and applies the same way no matter which control triggers it.

### Worked Example

The finished `app.py` (it uses `records.py` from Lesson 11.2):
```python
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
```

The user-level test `test_app_ui.py`:
```python
"""User-level tests for app.py. They need: pip install nicegui pytest pytest-asyncio"""
import os
import tempfile

from nicegui.testing import User

pytest_plugins = ["nicegui.testing.user_plugin"]
os.environ["PDM_DATA_FILE"] = os.path.join(tempfile.mkdtemp(), "data.json")


async def test_add_search_complete_delete(user: User) -> None:
    await user.open("/")
    await user.should_see("Personal Data Manager")
    await user.should_see("No records to show.")

    user.find("Record title").type("Notebook")
    user.find("Record description").type("Course notes")
    user.find("Record category").type("supplies")
    user.find("Add record").click()
    await user.should_see("1. Notebook [supplies] (not done)")
    await user.should_see("Added record 1: Notebook.")

    user.find("Add record").click()
    await user.should_see("A title is required.")

    user.find("Choose a record").click()
    user.find("1. Notebook [supplies] (not done)").click()
    user.find("Mark selected record done").click()
    await user.should_see("1. Notebook [supplies] (done)")

    user.find("Delete selected record").click()
    await user.should_see("Deleted record 1.")
    await user.should_see("No records to show.")
```
```ini
# pytest.ini
[pytest]
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
main_file = app.py
```

### Expected Behavior or Output

In the page: choose `1. Notebook [supplies] (not done)` and press **Mark selected record done**; the list shows `1. Notebook [supplies] (done)` and the status line says `Marked record 1 as done.` Pressing **Delete selected record** says `Deleted record 1.` Pressing a change button with nothing chosen says `Choose a record first.` The test prints:
```text
1 passed
```

### Common Mistakes

1. Using a stale choice after deleting, so a later action targets a record that no longer exists.
2. Putting rules in the handlers, so two buttons enforce the same rule differently.
3. Forgetting to save after a change, so the change is lost when the program stops.
4. Deleting without telling the user, which gives no way to confirm that the action happened.

### Activities

1. Change the title and category of record 2 through the page and read `data.json` to confirm.
2. Add a confirmation step before a delete (for example a second button that must be pressed).
3. Add a button that deletes all completed records and reports how many were removed.
4. Write a user-level test for the change handler.

### Accessibility Practice

Use the keyboard to choose a record in the chooser and press each button. Confirm that the result of every action is spoken or readable in the status line without using a mouse. Check that buttons have text labels that say what they do; avoid icon-only buttons.

### Skills Checklist

- [ ] I can select a record and change its fields.
- [ ] I can mark a record done.
- [ ] I can delete one record.
- [ ] I save and refresh after each change.
- [ ] I keep rules in one place.

---

## Lesson 11.5: Testing, Documentation, and Final Submission

### Reading References
- Matthes: Chapter 11 (Testing Your Code)
- Python documentation: the `unittest` module
- NiceGUI documentation (official site, nicegui.io); check the documentation for the version you installed

### Learning Objectives
- Run the shared acceptance tests for the logic module.
- Check the page by hand with the keyboard and your own screen reader.
- Write the README and submit the deliverables.

### Concept Explanation

The shared acceptance tests (listed in the unit overview) are written once for the logic in `records.py`. Tests 1 to 5 are automated below; test 6, using every control without color or a mouse, must be checked by hand. The user-level page test from Lesson 11.4 adds a simulated walk through the page, but it runs in Python, so it cannot tell you how a real browser and screen reader behave.

A **README** tells the next reader what the program does and how to run it. Write it in plain text or Markdown with short headings and complete sentences. Include the project title and your name, a description, the run command (`uv run python app.py`), the keyboard and screen reader instructions that you actually tested, the shared record fields, and a reflection on what was hard.

**Version control.** Keep your project in Git and commit after each working step so you can return to a working version (see the supplemental section at the end of this unit).

### Worked Example

The test file `test_records.py` (put it next to `records.py`):
```python
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
```

Run it from the terminal:
```bash
uv run python -m unittest -v test_records
```

A starting point for `README.md`:
```markdown
# Personal Data Manager

By: (your name)

## What it does
A small web application that keeps a list of records and saves them to data.json.

## How to run
    uv run python app.py
Then open the address that the terminal prints.

## Keyboard and screen reader notes
(Describe what you tested: operating system, browser, screen reader, and versions.)

## Record fields
id, title, description, category, created_at, updated_at, done

## Reflection
(What was hard, and what would you improve?)
```

### Expected Behavior or Output

The command prints one line per test and a summary (the timing differs from run to run):
```text
test_1_empty_title_is_rejected (test_records.TestRecords.test_1_empty_title_is_rejected) ... ok
test_2_new_record_gets_an_unused_id (test_records.TestRecords.test_2_new_record_gets_an_unused_id) ... ok
test_3_update_changes_updated_at_but_not_created_at (test_records.TestRecords.test_3_update_changes_updated_at_but_not_created_at) ... ok
test_4_delete_removes_only_that_record (test_records.TestRecords.test_4_delete_removes_only_that_record) ... ok
test_5_save_and_reload_preserves_all_fields (test_records.TestRecords.test_5_save_and_reload_preserves_all_fields) ... ok
test_blank_title_cannot_be_saved_by_update (test_records.TestRecords.test_blank_title_cannot_be_saved_by_update) ... ok
test_complete_marks_done_and_updates (test_records.TestRecords.test_complete_marks_done_and_updates) ... ok
test_damaged_file_gives_an_empty_list_and_a_message (test_records.TestRecords.test_damaged_file_gives_an_empty_list_and_a_message) ... ok
test_search_ignores_case_and_checks_description (test_records.TestRecords.test_search_ignores_case_and_checks_description) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

### Common Mistakes

1. Testing only that nothing crashed, and not checking the values returned.
2. Sharing one list of records between tests, so one test's changes affect the next.
3. Writing a README that only the author can follow, or claiming accessibility that was never tested.
4. Skipping test 6 because it cannot be automated.

### Activities

1. Run the tests, then break `update_record` so it also changes `created_at` and watch test 3 fail. Restore it.
2. Add a test that deleting an unknown id returns `False` and a message.
3. Ask a classmate to follow your README from an empty folder and note where they get stuck.
4. Complete test 6 by hand: use every control with the keyboard only and record what you found.

### Accessibility Practice

Run the tests from the terminal and read the summary line first. For the hand check, use the keyboard only, then repeat with your screen reader or braille display. Record the operating system, browser, screen reader, and versions that you tested, and describe only what you actually tried.

### Skills Checklist

- [ ] I can run the acceptance tests and read the results.
- [ ] I can complete a hand check of keyboard and screen reader use.
- [ ] I can write a README another person can follow.
- [ ] I know what the page test does and does not show.
- [ ] I can submit the listed deliverables.

---

## Assessment Criteria

### Functionality (60%)
- [ ] Ability to add new items with all specified attributes.
- [ ] Correct display of all current items.
- [ ] Correct editing of existing items.
- [ ] Correct deletion of items.
- [ ] Accurate saving and loading to and from `data.json`.
- [ ] Search and completion work as described.
- [ ] No major bugs or crashes during typical usage.

### Code Quality and Structure (20%)
- [ ] Clear and concise Python code.
- [ ] Appropriate use of functions, with rules kept in `records.py`.
- [ ] Meaningful variable and function names.
- [ ] Adequate comments where logic is complex.
- [ ] Proper indentation.

### Accessibility and User Experience (15%)
- [ ] All interactive elements are correctly labeled for screen readers.
- [ ] Clear and consistent feedback in a text status line.
- [ ] Logical flow and presentation of information.
- [ ] No visual-only cues for critical information.

### README and Reflection (5%)
- [ ] Complete and clear README.
- [ ] Thoughtful reflection on development and accessibility challenges.

---

## Deliverables

1. `app.py` and `records.py`: the complete application code.
2. `test_records.py`: the acceptance tests.
3. `data.json`: an example file that shows saved data.
4. `README.md`, including: the project title and student name; a description of the application; instructions on how to run it (`uv run python app.py`); instructions for interacting with a screen reader; and a reflection on challenges faced.

---

<<<<<<< HEAD
## Supplemental: AI Tools and Version Control

### Academic Integrity: AI and Assessment

AI tools must not write, complete, autocomplete, repair, or generate course code or assessment solutions. Students may use only instructor-authorized conceptual explanations that do not produce deliverable code. Git and version control are taught separately and are not a workaround for the assessment-integrity rule.
=======
## Supplemental: Version Control
>>>>>>> 2067a20 (curriculum clearning and updates)

### Git and Version Control

**Git** is the most widely used distributed version control system, invented in 2005 by Linus Torvalds for the Linux kernel project.

**Core workflow:**
1. **Working directory** — Make changes to files.
2. **Staging area** — `git add` — Stage changes.
3. **Repository** — `git commit` — Save a permanent snapshot.
4. **Remote** — `git push` / `git pull` — Sync with GitHub.

<<<<<<< HEAD
**Why Git is useful in collaborative development:**
- **Rollback** — Revert a change when a regression is introduced.
- **`git blame`** — Identify the commit that introduced a change.
- **Branches** — Develop and test changes in isolation.
- **Pull requests** — Review changes before merging.
=======
**Why Git is valuable:**
- **Rollback** — If a change breaks your app, revert instantly.
- **`git blame`** — See exactly which commit introduced a bug.
- **Branches** — Try experiments in isolation without affecting main code.
- **Pull requests** — Review changes with others before merging.
>>>>>>> 2067a20 (curriculum clearning and updates)

**Basic commands:**
```bash
git init                    # Initialize a repository
git add .                   # Stage all changes
git commit -m "Add feature" # Save a snapshot
git log                     # View history
git diff                    # See what changed
git checkout -- file.py     # Discard changes to a file
```

Windows Powershell

```powershell
git init                    # Initialize a repository
git add .                   # Stage all changes
git commit -m "Add feature" # Save a snapshot
git log                     # View history
git diff                    # See what changed
git restore -- file.py     # Discard changes to a file
```

<<<<<<< HEAD
## Canonical Shared Project Contracts

### Unit 10: Adventure and command-line to-do projects

All parallel-language versions must use this exact adventure graph and command set.

| Room | Exits | Items / state |
|---|---|---|
| `start_room` | north → `tunnel` | shiny key |
| `tunnel` | south → `start_room`; east → `clearing` | none |
| `clearing` | west → `tunnel`; north → `locked_door_room` | north exit is blocked until unlocked |
| `locked_door_room` | south → `clearing`; north → `treasure_room` after unlocking | locked door |
| `treasure_room` | none | terminal winning room |

Commands are `north`, `south`, `east`, `west`, `take shiny key`, `use shiny key`, and `quit`. The key begins in `start_room`; the player must take it, travel to `locked_door_room`, use it there, and then enter `treasure_room` to win. Invalid movement must not change the current room.

The CLI to-do manager must store these five fields on every task: `id`, `title`, `description`, `done`, and `created_at`. It must support create, list, complete/update, delete, save, and load. Invalid identifiers, empty titles, and malformed persistence data require explicit textual errors.

### Unit 11: Accessible Personal Data Manager

The shared capstone record has exactly these fields:

```python
record = {
    "id": 1,
    "title": "Programming notes",
    "description": "Review lists and dictionaries",
    "category": "Study",
    "created_at": "2025-01-15T09:00:00Z",
    "updated_at": "2025-01-15T09:00:00Z",
}
```

Required operations are list/display, add, search, update, delete, and JSON save/load. Search is case-insensitive across title, description, and category and must report an empty result set clearly. Updating any field other than the ID must preserve the ID and refresh updated_at using the supplied timestamp. Reject blank titles, duplicate/non-positive IDs, incorrect field types, missing fields, and extra fields. A GUI framework is a Python-specific implementation choice; the data model, operations, textual status/error messages, keyboard access, and acceptance tests are not optional or language-specific.

### Academic integrity and AI policy

AI tools must not write, complete, autocomplete, repair, or generate course code or assessment solutions. Students may use only instructor-authorized conceptual explanations that do not produce deliverable code. Git and version control remain appropriate topics when taught independently of AI code generation.
=======
## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)
