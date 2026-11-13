[Header 2 ("unit-11-capstone-project--accessible-personal-data-manager", [], []) [Str "Unit 11: Capstone Project — Accessible Personal Data Manager"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Students develop a fully functional personal data manager that is built to work with a screen reader and keyboard. The program keeps a list of structured records, lets the user add, view, search, change, complete, and delete them, and saves them to a JSON file. The Python track builds it as a small local web application with NiceGUI. The other language tracks build a text-based version with the same records, rules, and tests."], Para [Strong [Str "Project Goal:"], Str " Build an application to manage structured records with list, add, search, update, delete, and JSON persistence operations. The interface may be GUI-based in Python; the same data contract and operation semantics apply to the Lua terminal implementation."], Para [Strong [Str "Project Options:"]], BulletList [[Plain [Str "Contact Manager"]], [Plain [Str "Book/Movie Tracker"]], [Plain [Str "Study Notes Manager"]], [Plain [Str "Personal Inventory"]]], Para [Str "Every option uses the same six-field record schema (", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "category", Str ", ", Code ("", [], []) "created_at", Str ", ", Code ("", [], []) "updated_at", Str "). The selected project domain changes the meaning of the field values, not the record shape or required operations."], HorizontalRule, Header 3 ("lesson-111-introduction-to-nicegui", ["unnumbered", "unlisted"], []) [Str "Lesson 11.1: Introduction to NiceGUI"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Strong [Str "Add New Item"], Str " — A form to input details for a new item."]], [Plain [Strong [Str "View All Items"], Str " — Display items in a clear, accessible list format."]], [Plain [Strong [Str "Edit Item"], Str " — Select an existing item and modify its details."]], [Plain [Strong [Str "Search Items"], Str " — Find records by ID and case-insensitive text in title, description, or category; report no matches explicitly."]], [Plain [Strong [Str "Delete Item"], Str " — Remove an item from the collection and confirm the result."]], [Plain [Strong [Str "Save/Load Data"], Str " — Persist the data to a JSON file and validate the complete six-field schema on load."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Install NiceGUI with ", Code ("", [], []) "uv", Str " and start a page from the terminal."]], [Plain [Str "Explain that each ", Code ("", [], []) "ui.", Str " call creates an element and that an event handler runs when the user acts."]], [Plain [Str "Give every input a label and report results in a plain text status line."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "NiceGUI lets you build a web page in Python. When the program runs it starts a small web server on your own computer and prints an address, normally ", Code ("", [], []) "http://localhost:8080", Str ". You open that address in a browser. Nothing is sent to other people; the page is served only from your computer unless you choose otherwise."], Para [Strong [Str "Setup."], Str " Install the package into the project environment:"], CodeBlock ("", ["bash"], []) "uv add nicegui
", Para [Str "Windows PowerShell uses the same command:"], CodeBlock ("", ["powershell"], []) "uv add nicegui
", Para [Strong [Str "Elements and handlers."], Str " Each call such as ", Code ("", [], []) "ui.label(...)", Str ", ", Code ("", [], []) "ui.input(...)", Str ", or ", Code ("", [], []) "ui.button(...)", Str " creates an element on the page. A button takes an ", Code ("", [], []) "on_click", Str " function, called a ", Emph [Str "handler"], Str ", that runs when the user presses it. The code inside ", Code ("", [], []) "@ui.page(\"/\")", Str " builds the page each time someone opens it."], Para [Strong [Str "Starting the server."], Str " ", Code ("", [], []) "ui.run(...)", Str " starts the server. Guard it with ", Code ("", [], []) "if __name__ in {\"__main__\", \"__mp_main__\"}:", Str " as NiceGUI requires. Pass ", Code ("", [], []) "show=False", Str " so that no browser is opened automatically, and ", Code ("", [], []) "reload=False", Str " while learning."], Para [Strong [Str "Accessibility."], Str " NiceGUI pages are ordinary web pages, so a screen reader reads them as any other page. Three habits make them usable: give every input a clear ", Code ("", [], []) "label", Str ", because the label text is what a screen reader announces for the field; report every result in a plain text label as well as in a pop-up, because a pop-up message disappears; and never use color as the only signal. The status label below uses the standard attributes ", Code ("", [], []) "role=\"status\"", Str " and ", Code ("", [], []) "aria-live=\"polite\"", Str ", which ask assistive technology to announce changes. Whether your screen reader announces them as intended must be tested with your own setup."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "Save this as ", Code ("", [], []) "hello_app.py", Str ":"], CodeBlock ("", ["python"], []) "from nicegui import ui


@ui.page(\"/\")
def main_page():
    ui.page_title(\"Personal Data Manager\")
    ui.label(\"Personal Data Manager\")
    name = ui.input(label=\"Your name\")
    greeting = ui.label(\"Type a name and press the button.\").props('role=\"status\" aria-live=\"polite\"')

    def greet():
        if name.value.strip():
            greeting.set_text(f\"Hello, {name.value.strip()}!\")
        else:
            greeting.set_text(\"Please enter a name.\")

    ui.button(\"Greet\", on_click=greet)


if __name__ in {\"__main__\", \"__mp_main__\"}:
    ui.run(title=\"Personal Data Manager\", reload=False, show=False)
", Para [Str "Start it from the terminal and open the address that it prints:"], CodeBlock ("", ["bash"], []) "uv run python hello_app.py
", Para [Str "The repository also includes a user-level test, ", Code ("", [], []) "test_hello_ui.py", Str ", which needs ", Code ("", [], []) "uv add --dev pytest pytest-asyncio", Str ":"], CodeBlock ("", ["python"], []) "from nicegui.testing import User

pytest_plugins = [\"nicegui.testing.user_plugin\"]


async def test_greeting(user: User) -> None:
    await user.open(\"/\")
    await user.should_see(\"Personal Data Manager\")
    user.find(\"Greet\").click()
    await user.should_see(\"Please enter a name.\")
    user.find(\"Your name\").type(\"Avery\")
    user.find(\"Greet\").click()
    await user.should_see(\"Hello, Avery!\")
", CodeBlock ("", ["ini"], []) "# pytest.ini
[pytest]
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
main_file = hello_app.py
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "When the program starts, the terminal prints a line like this one (the address and port depend on your computer; the default port is 8080):"], CodeBlock ("", ["text"], []) "NiceGUI ready to go on http://localhost:8080, and http://192.0.2.2:8080
", Para [Str "The page title is Personal Data Manager. Pressing ", Strong [Str "Greet"], Str " with an empty field sets the status line to ", Code ("", [], []) "Please enter a name.", Str "; after typing ", Code ("", [], []) "Avery", Str " it says ", Code ("", [], []) "Hello, Avery!", Str ". Running the test with ", Code ("", [], []) "python -m pytest -q test_hello_ui.py", Str " prints:"], CodeBlock ("", ["text"], []) "1 passed
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Calling ", Code ("", [], []) "ui.run()", Str " without the ", Code ("", [], []) "__name__", Str " guard, which can start the server twice."]], [Plain [Str "Relying only on ", Code ("", [], []) "ui.notify", Str ", whose message disappears, instead of also updating a text status line."]], [Plain [Str "Leaving an input without a label, so the screen reader announces only \"edit text\"."]], [Plain [Str "Starting a second copy of the program while the first still holds the port."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Start ", Code ("", [], []) "hello_app.py", Str " and read the page title and the status line with your screen reader."]], [Plain [Str "Change the greeting to include the time of day using a second input."]], [Plain [Str "Run the test file and then break the greeting text on purpose to watch the test fail."]], [Plain [Str "Add a second button that clears the name and sets the status line to ", Code ("", [], []) "Name cleared."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Open the page with the keyboard only: press Tab to move between the input and the button and read each stop. Check that the input's label is announced and that the status line is read after you press the button. Record the browser, screen reader, and version you tested, and do not claim the page is accessible to other setups."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can install NiceGUI and start a page from the terminal."]], [Plain [Str "\9744", Space, Str "I can explain elements and event handlers."]], [Plain [Str "\9744", Space, Str "I can give every input a label."]], [Plain [Str "\9744", Space, Str "I can report results in a plain text status line."]], [Plain [Str "\9744", Space, Str "I can run a user-level test."]]], HorizontalRule, Header 3 ("lesson-112-data-model-and-storage", ["unnumbered", "unlisted"], []) [Str "Lesson 11.2: Data Model and Storage"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 6 (Dictionaries) and Chapter 10 (Files and Exceptions)"]], [Plain [Str "Python documentation: the ", Code ("", [], []) "json", Str " and ", Code ("", [], []) "datetime", Str " modules"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Represent each record as a dictionary with the shared fields."]], [Plain [Str "Validate input and return a clear message when it is invalid."]], [Plain [Str "Save to and load from a JSON file, and handle a missing or damaged file."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The data and the rules live in one module, ", Code ("", [], []) "records.py", Str ", that contains no user-interface code. Keeping logic separate from the page has two benefits: the rules can be tested without a browser, and the same logic can serve a different front end later."], Para [Str "Each record is a dictionary with the shared fields (", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "category", Str ", ", Code ("", [], []) "created_at", Str ", ", Code ("", [], []) "updated_at", Str ") and the optional ", Code ("", [], []) "done", Str " field. Dictionaries convert directly to JSON."], Para [Strong [Str "Rules."], Str " A title and a category are required. A new record gets an ", Code ("", [], []) "id", Str " one higher than the highest in use. ", Code ("", [], []) "created_at", Str " is set once and never changes. ", Code ("", [], []) "updated_at", Str " changes whenever a record is updated, completed, or edited. Every function that can fail returns a clear message instead of raising an error that the user must interpret; functions return a pair ", Code ("", [], []) "(result, message)", Str "."], Para [Strong [Str "Storage."], Str " ", Code ("", [], []) "save_records", Str " writes the list as JSON. ", Code ("", [], []) "load_records", Str " treats a missing file as an empty list (this is normal on first use), and returns a message when the file is damaged or does not contain valid records, so the program never overwrites good data with an empty list without telling the user."], Para [Strong [Str "Testable time."], Str " Functions that stamp a record take a ", Code ("", [], []) "clock", Str " argument that defaults to the real time. Tests pass a fake clock so that timestamps are predictable."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "Save this as ", Code ("", [], []) "records.py", Str ":"], CodeBlock ("", ["python"], []) "\"\"\"Logic for the Personal Data Manager. No user-interface code lives here.\"\"\"
import json
from datetime import datetime

REQUIRED_FIELDS = (\"id\", \"title\", \"description\", \"category\", \"created_at\", \"updated_at\")


def now():
    \"\"\"Return the current time as ISO 8601 text, for example 2026-01-15T09:00:00.\"\"\"
    return datetime.now().isoformat(timespec=\"seconds\")


def validate(title, category):
    \"\"\"Return an error message for invalid input, or None when it is valid.\"\"\"
    if not title or not title.strip():
        return \"A title is required.\"
    if not category or not category.strip():
        return \"A category is required.\"
    return None


def next_id(records):
    \"\"\"Return one more than the highest id in use (1 for an empty list).\"\"\"
    return max((record[\"id\"] for record in records), default=0) + 1


def find(records, record_id):
    \"\"\"Return the record with this id, or None.\"\"\"
    for record in records:
        if record[\"id\"] == record_id:
            return record
    return None


def add_record(records, title, description, category, clock=now):
    \"\"\"Add a record. Return (record, None) on success or (None, message) on failure.\"\"\"
    problem = validate(title, category)
    if problem:
        return None, problem
    stamp = clock()
    record = {
        \"id\": next_id(records),
        \"title\": title.strip(),
        \"description\": (description or \"\").strip(),
        \"category\": category.strip(),
        \"created_at\": stamp,
        \"updated_at\": stamp,
        \"done\": False,
    }
    records.append(record)
    return record, None


def update_record(records, record_id, changes, clock=now):
    \"\"\"Change fields of a record. created_at and id never change.\"\"\"
    record = find(records, record_id)
    if record is None:
        return None, \"No record has that id.\"
    problem = validate(changes.get(\"title\", record[\"title\"]), changes.get(\"category\", record[\"category\"]))
    if problem:
        return None, problem
    for key, value in changes.items():
        if key not in (\"id\", \"created_at\"):
            record[key] = value.strip() if isinstance(value, str) else value
    record[\"updated_at\"] = clock()
    return record, None


def complete_record(records, record_id, clock=now):
    \"\"\"Mark a record done; this counts as an update.\"\"\"
    return update_record(records, record_id, {\"done\": True}, clock)


def delete_record(records, record_id):
    \"\"\"Remove one record. Return (True, None) or (False, message).\"\"\"
    record = find(records, record_id)
    if record is None:
        return False, \"No record has that id.\"
    records.remove(record)
    return True, None


def search(records, text):
    \"\"\"Return records whose title or description contains the text (ignoring case).\"\"\"
    needle = text.strip().lower()
    return [r for r in records if needle in r[\"title\"].lower() or needle in r[\"description\"].lower()]


def describe(record):
    \"\"\"One line of plain text for a record; status is shown in words, never by color.\"\"\"
    status = \"done\" if record.get(\"done\") else \"not done\"
    return f\"{record['id']}. {record['title']} [{record['category']}] ({status})\"


def save_records(path, records):
    \"\"\"Write records to a JSON file.\"\"\"
    with open(path, \"w\", encoding=\"utf-8\") as file:
        json.dump(records, file, indent=4)


def load_records(path):
    \"\"\"Return (records, None) or ([], message). A missing file is not an error.\"\"\"
    try:
        with open(path, \"r\", encoding=\"utf-8\") as file:
            data = json.load(file)
    except FileNotFoundError:
        return [], None
    except json.JSONDecodeError:
        return [], f\"{path} is not valid JSON, so the list starts empty.\"
    if not isinstance(data, list) or not all(isinstance(r, dict) and all(f in r for f in REQUIRED_FIELDS) for r in data):
        return [], f\"{path} does not contain valid records, so the list starts empty.\"
    return data, None
", Para [Str "Try it with this short script, ", Code ("", [], []) "demo.py", Str ", in the same folder:"], CodeBlock ("", ["python"], []) "import records

ticks = iter(range(1, 100))


def clock():
    return f\"2026-01-15T10:00:{next(ticks):02d}\"


items = []
records.add_record(items, \"Notebook\", \"Course notes\", \"supplies\", clock)
records.add_record(items, \"Pencil\", \"Box of 10\", \"supplies\", clock)
print(records.add_record(items, \"  \", \"x\", \"supplies\", clock))
for item in items:
    print(records.describe(item))

records.save_records(\"data.json\", items)
loaded, problem = records.load_records(\"data.json\")
print(loaded == items, problem)
print(records.load_records(\"missing.json\"))
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Running ", Code ("", [], []) "python demo.py", Str " prints:"], CodeBlock ("", ["text"], []) "(None, 'A title is required.')
1. Notebook [supplies] (not done)
2. Pencil [supplies] (not done)
True None
([], None)
", Para [Str "The invalid record is rejected with ", Code ("", [], []) "(None, 'A title is required.')", Str ". The saved and reloaded list equals the original (", Code ("", [], []) "True None", Str "), and a missing file gives an empty list with no message."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Letting the user interface and the rules share the same code, so neither can be tested alone."]], [Plain [Str "Overwriting ", Code ("", [], []) "data.json", Str " with an empty list after a failed load."]], [Plain [Str "Changing ", Code ("", [], []) "created_at", Str " when a record is edited."]], [Plain [Str "Reusing an old ", Code ("", [], []) "id", Str " by counting the list length instead of using the highest ", Code ("", [], []) "id", Str "."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run ", Code ("", [], []) "demo.py", Str " and open the saved ", Code ("", [], []) "data.json", Str ". Read the text aloud."]], [Plain [Str "Add a rule that a title may not be longer than 60 characters, with a clear message."]], [Plain [Str "Add an ", Code ("", [], []) "is_done", Str " filter function that returns only completed records."]], [Plain [Str "Damage ", Code ("", [], []) "data.json", Str " by deleting a bracket and run ", Code ("", [], []) "load_records", Str " again; read the message it returns."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Messages are complete sentences that say what is wrong (", Code ("", [], []) "A title is required.", Str ") so they read clearly in speech and braille. After saving, read ", Code ("", [], []) "data.json", Str " in the terminal; ", Code ("", [], []) "indent=4", Str " puts one field per line, which reads well line by line."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can represent records as dictionaries."]], [Plain [Str "\9744", Space, Str "I can validate input and return clear messages."]], [Plain [Str "\9744", Space, Str "I can save and load JSON."]], [Plain [Str "\9744", Space, Str "I can handle a missing or damaged file."]], [Plain [Str "\9744", Space, Str "I can keep logic separate from the user interface."]]], HorizontalRule, Header 3 ("lesson-113-displaying-and-searching-items", ["unnumbered", "unlisted"], []) [Str "Lesson 11.3: Displaying and Searching Items"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "NiceGUI documentation (official site, nicegui.io); check the documentation for the version you installed"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Build a page that adds a record and lists all records."]], [Plain [Str "Filter the list as the user types in a search box."]], [Plain [Str "Show errors in a status line that is also announced."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The page uses the functions from ", Code ("", [], []) "records.py", Str ". It builds a form for a new record, a search box, and a list. The list is rebuilt by one function, ", Code ("", [], []) "refresh()", Str ", that clears the list column and then creates one label per record. Calling ", Code ("", [], []) "refresh()", Str " after every change keeps the page and the data in step."], Para [Str "Each record is shown as one plain sentence produced by ", Code ("", [], []) "describe()", Str ", for example ", Code ("", [], []) "1. Notebook [supplies] (not done)", Str ". The status is the words ", Emph [Str "done"], Str " and ", Emph [Str "not done"], Str ", never a color or an icon alone. The description appears on its own line prefixed ", Code ("", [], []) "Details:", Str "."], Para [Str "The search box filters as the user types: ", Code ("", [], []) "search_text.on_value_change(...)", Str " calls ", Code ("", [], []) "refresh()", Str ", which uses ", Code ("", [], []) "search()", Str " when the box is not empty."], Para [Str "Every input has a unique label (", Code ("", [], []) "Record title", Str ", ", Code ("", [], []) "Record description", Str ", ", Code ("", [], []) "Record category", Str ", ", Code ("", [], []) "Search title or description", Str "). Unique labels let a screen reader user tell the fields apart and let the tests find them."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "Save this as ", Code ("", [], []) "app_v1.py", Str " (it uses ", Code ("", [], []) "records.py", Str " from Lesson 11.2):"], CodeBlock ("", ["python"], []) "\"\"\"Personal Data Manager, version for Lesson 11.3: add, list, and search.\"\"\"
import os
from pathlib import Path

from nicegui import ui

import records as store

DATA_FILE = Path(os.environ.get(\"PDM_DATA_FILE\", \"data.json\"))
items, load_problem = store.load_records(DATA_FILE)


@ui.page(\"/\")
def main_page():
    ui.page_title(\"Personal Data Manager\")
    ui.label(\"Personal Data Manager\").classes(\"text-2xl\")

    # A plain-text status line. aria-live asks assistive technology to announce changes.
    status = ui.label(load_problem or \"Ready.\").props('role=\"status\" aria-live=\"polite\"')

    def say(message, ok=True):
        status.set_text(message)
        ui.notify(message, type=\"positive\" if ok else \"negative\")

    ui.label(\"Add a record\")
    title = ui.input(label=\"Record title\")
    description = ui.input(label=\"Record description\")
    category = ui.input(label=\"Record category\")

    ui.label(\"Find records\")
    search_text = ui.input(label=\"Search title or description\")

    ui.label(\"Records\")
    list_column = ui.column()

    def refresh():
        shown = store.search(items, search_text.value) if search_text.value else items
        list_column.clear()
        with list_column:
            if not shown:
                ui.label(\"No records to show.\")
            for record in shown:
                ui.label(store.describe(record))
                if record[\"description\"]:
                    ui.label(\"Details: \" + record[\"description\"])

    def add_clicked():
        record, problem = store.add_record(items, title.value, description.value, category.value)
        if problem:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        title.set_value(\"\")
        description.set_value(\"\")
        category.set_value(\"\")
        refresh()
        say(f\"Added record {record['id']}: {record['title']}.\")

    ui.button(\"Add record\", on_click=add_clicked)
    search_text.on_value_change(lambda _: refresh())
    refresh()


if __name__ in {\"__main__\", \"__mp_main__\"}:
    ui.run(title=\"Personal Data Manager\", reload=False, show=False)
", Para [Str "The user-level test ", Code ("", [], []) "test_app_v1_ui.py", Str ":"], CodeBlock ("", ["python"], []) "import os
import tempfile

from nicegui.testing import User

pytest_plugins = [\"nicegui.testing.user_plugin\"]
os.environ[\"PDM_DATA_FILE\"] = os.path.join(tempfile.mkdtemp(), \"data.json\")


async def test_add_and_search(user: User) -> None:
    await user.open(\"/\")
    await user.should_see(\"No records to show.\")
    for title, description, category in [(\"Notebook\", \"Course notes\", \"supplies\"), (\"Pencil\", \"Box of 10\", \"supplies\")]:
        user.find(\"Record title\").type(title)
        user.find(\"Record description\").type(description)
        user.find(\"Record category\").type(category)
        user.find(\"Add record\").click()
    await user.should_see(\"2. Pencil [supplies] (not done)\")
    user.find(\"Search title or description\").type(\"note\")
    await user.should_see(\"1. Notebook [supplies] (not done)\")
    await user.should_not_see(\"2. Pencil [supplies] (not done)\")
    user.find(\"Add record\").click()
    await user.should_see(\"A title is required.\")
", CodeBlock ("", ["ini"], []) "# pytest.ini
[pytest]
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
main_file = app_v1.py
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Start the app with ", Code ("", [], []) "uv run python app_v1.py", Str " and open the printed address. With no records the list says ", Code ("", [], []) "No records to show.", Str " After adding Notebook and Pencil, the list shows ", Code ("", [], []) "1. Notebook [supplies] (not done)", Str " and ", Code ("", [], []) "2. Pencil [supplies] (not done)", Str ". Typing ", Code ("", [], []) "note", Str " in the search box leaves only the Notebook line. Pressing ", Strong [Str "Add record"], Str " with an empty title sets the status line to ", Code ("", [], []) "A title is required.", Str " Running the test prints:"], CodeBlock ("", ["text"], []) "1 passed
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Building the list outside ", Code ("", [], []) "refresh()", Str ", so it is not updated when the data changes."]], [Plain [Str "Using the same label text for two inputs, so the screen reader cannot tell them apart."]], [Plain [Str "Showing a record's status only by color."]], [Plain [Str "Forgetting to clear the form after a successful add, so the next record starts with old text."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Add the three shared sample records through the page and compare the list with the sample data."]], [Plain [Str "Add a category filter next to the search box."]], [Plain [Str "Show the number of records after the list, for example ", Code ("", [], []) "3 records."]], [Plain [Str "Break the ", Code ("", [], []) "describe()", Str " text on purpose and see which test fails."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Tab through the form and confirm that each field is announced with its label. After pressing ", Strong [Str "Add record"], Str ", listen for the status line. If your screen reader does not announce it, note the browser and screen reader you used, then add a visible sentence under the button as a fallback."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can build a form and a list in NiceGUI."]], [Plain [Str "\9744", Space, Str "I can refresh the list after every change."]], [Plain [Str "\9744", Space, Str "I can filter the list with a search box."]], [Plain [Str "\9744", Space, Str "I can show status in words."]], [Plain [Str "\9744", Space, Str "I can give each input a unique label."]]], HorizontalRule, Header 3 ("lesson-114-changing-completing-and-deleting-items", ["unnumbered", "unlisted"], []) [Str "Lesson 11.4: Changing, Completing, and Deleting Items"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "NiceGUI documentation (official site, nicegui.io); check the documentation for the version you installed"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Select a record from a list and change its title or category."]], [Plain [Str "Mark a record done and delete a record."]], [Plain [Str "Save after every successful change and report each result."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The finished page adds a ", Emph [Str "chooser"], Str " (", Code ("", [], []) "ui.select", Str ") that lists every record by its descriptive sentence, plus buttons to change, complete, or delete the chosen record. All three handlers follow the same pattern: check that a record is chosen, call the matching function in ", Code ("", [], []) "records.py", Str ", show the message if it failed, and otherwise save the file, refresh the list, and report what happened."], Para [Code ("", [], []) "update_record", Str " changes only the fields that are supplied and always updates ", Code ("", [], []) "updated_at", Str ". ", Code ("", [], []) "complete_record", Str " is an update that sets ", Code ("", [], []) "done", Str " to ", Code ("", [], []) "True", Str ". ", Code ("", [], []) "delete_record", Str " removes exactly one record. After a delete the chooser is cleared so a stale choice cannot be used."], Para [Str "Notice that the handlers contain no rules. A rule such as \"a title is required\" exists once, in ", Code ("", [], []) "records.py", Str ", and applies the same way no matter which control triggers it."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "The finished ", Code ("", [], []) "app.py", Str " (it uses ", Code ("", [], []) "records.py", Str " from Lesson 11.2):"], CodeBlock ("", ["python"], []) "\"\"\"Personal Data Manager: a NiceGUI front end for records.py.\"\"\"
import os
from pathlib import Path

from nicegui import ui

import records as store

DATA_FILE = Path(os.environ.get(\"PDM_DATA_FILE\", \"data.json\"))
items, load_problem = store.load_records(DATA_FILE)


@ui.page(\"/\")
def main_page():
    ui.page_title(\"Personal Data Manager\")
    ui.label(\"Personal Data Manager\").classes(\"text-2xl\")

    # A plain-text status line. aria-live asks assistive technology to announce changes.
    status = ui.label(load_problem or \"Ready.\").props('role=\"status\" aria-live=\"polite\"')

    def say(message, ok=True):
        status.set_text(message)
        ui.notify(message, type=\"positive\" if ok else \"negative\")

    ui.label(\"Add a record\")
    title = ui.input(label=\"Record title\")
    description = ui.input(label=\"Record description\")
    category = ui.input(label=\"Record category\")

    ui.label(\"Find records\")
    search_text = ui.input(label=\"Search title or description\")

    ui.label(\"Records\")
    list_column = ui.column()

    ui.label(\"Change one record\")
    chooser = ui.select(options={}, label=\"Choose a record\")
    new_title = ui.input(label=\"New title (leave blank to keep)\")
    new_category = ui.input(label=\"New category (leave blank to keep)\")

    def refresh():
        shown = store.search(items, search_text.value) if search_text.value else items
        list_column.clear()
        with list_column:
            if not shown:
                ui.label(\"No records to show.\")
            for record in shown:
                ui.label(store.describe(record))
                if record[\"description\"]:
                    ui.label(\"Details: \" + record[\"description\"])
        chooser.set_options({r[\"id\"]: store.describe(r) for r in items})

    def add_clicked():
        record, problem = store.add_record(items, title.value, description.value, category.value)
        if problem:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        title.set_value(\"\")
        description.set_value(\"\")
        category.set_value(\"\")
        refresh()
        say(f\"Added record {record['id']}: {record['title']}.\")

    def change_clicked():
        if chooser.value is None:
            say(\"Choose a record first.\", ok=False)
            return
        changes = {}
        if new_title.value.strip():
            changes[\"title\"] = new_title.value
        if new_category.value.strip():
            changes[\"category\"] = new_category.value
        if not changes:
            say(\"Enter a new title or a new category.\", ok=False)
            return
        record, problem = store.update_record(items, chooser.value, changes)
        if problem:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        new_title.set_value(\"\")
        new_category.set_value(\"\")
        refresh()
        say(f\"Updated record {record['id']}.\")

    def complete_clicked():
        if chooser.value is None:
            say(\"Choose a record first.\", ok=False)
            return
        record, problem = store.complete_record(items, chooser.value)
        if problem:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        refresh()
        say(f\"Marked record {record['id']} as done.\")

    def delete_clicked():
        if chooser.value is None:
            say(\"Choose a record first.\", ok=False)
            return
        record_id = chooser.value
        ok, problem = store.delete_record(items, record_id)
        if not ok:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        chooser.set_value(None)
        refresh()
        say(f\"Deleted record {record_id}.\")

    ui.button(\"Add record\", on_click=add_clicked)
    search_text.on_value_change(lambda _: refresh())
    ui.button(\"Change selected record\", on_click=change_clicked)
    ui.button(\"Mark selected record done\", on_click=complete_clicked)
    ui.button(\"Delete selected record\", on_click=delete_clicked)
    refresh()


if __name__ in {\"__main__\", \"__mp_main__\"}:
    ui.run(title=\"Personal Data Manager\", reload=False, show=False)
", Para [Str "The user-level test ", Code ("", [], []) "test_app_ui.py", Str ":"], CodeBlock ("", ["python"], []) "\"\"\"User-level tests for app.py. They need: pip install nicegui pytest pytest-asyncio\"\"\"
import os
import tempfile

from nicegui.testing import User

pytest_plugins = [\"nicegui.testing.user_plugin\"]
os.environ[\"PDM_DATA_FILE\"] = os.path.join(tempfile.mkdtemp(), \"data.json\")


async def test_add_search_complete_delete(user: User) -> None:
    await user.open(\"/\")
    await user.should_see(\"Personal Data Manager\")
    await user.should_see(\"No records to show.\")

    user.find(\"Record title\").type(\"Notebook\")
    user.find(\"Record description\").type(\"Course notes\")
    user.find(\"Record category\").type(\"supplies\")
    user.find(\"Add record\").click()
    await user.should_see(\"1. Notebook [supplies] (not done)\")
    await user.should_see(\"Added record 1: Notebook.\")

    user.find(\"Add record\").click()
    await user.should_see(\"A title is required.\")

    user.find(\"Choose a record\").click()
    user.find(\"1. Notebook [supplies] (not done)\").click()
    user.find(\"Mark selected record done\").click()
    await user.should_see(\"1. Notebook [supplies] (done)\")

    user.find(\"Delete selected record\").click()
    await user.should_see(\"Deleted record 1.\")
    await user.should_see(\"No records to show.\")
", CodeBlock ("", ["ini"], []) "# pytest.ini
[pytest]
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
main_file = app.py
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "In the page: choose ", Code ("", [], []) "1. Notebook [supplies] (not done)", Str " and press ", Strong [Str "Mark selected record done"], Str "; the list shows ", Code ("", [], []) "1. Notebook [supplies] (done)", Str " and the status line says ", Code ("", [], []) "Marked record 1 as done.", Str " Pressing ", Strong [Str "Delete selected record"], Str " says ", Code ("", [], []) "Deleted record 1.", Str " Pressing a change button with nothing chosen says ", Code ("", [], []) "Choose a record first.", Str " The test prints:"], CodeBlock ("", ["text"], []) "1 passed
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using a stale choice after deleting, so a later action targets a record that no longer exists."]], [Plain [Str "Putting rules in the handlers, so two buttons enforce the same rule differently."]], [Plain [Str "Forgetting to save after a change, so the change is lost when the program stops."]], [Plain [Str "Deleting without telling the user, which gives no way to confirm that the action happened."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Change the title and category of record 2 through the page and read ", Code ("", [], []) "data.json", Str " to confirm."]], [Plain [Str "Add a confirmation step before a delete (for example a second button that must be pressed)."]], [Plain [Str "Add a button that deletes all completed records and reports how many were removed."]], [Plain [Str "Write a user-level test for the change handler."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use the keyboard to choose a record in the chooser and press each button. Confirm that the result of every action is spoken or readable in the status line without using a mouse. Check that buttons have text labels that say what they do; avoid icon-only buttons."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can select a record and change its fields."]], [Plain [Str "\9744", Space, Str "I can mark a record done."]], [Plain [Str "\9744", Space, Str "I can delete one record."]], [Plain [Str "\9744", Space, Str "I save and refresh after each change."]], [Plain [Str "\9744", Space, Str "I keep rules in one place."]]], HorizontalRule, Header 3 ("lesson-115-testing-documentation-and-final-submission", ["unnumbered", "unlisted"], []) [Str "Lesson 11.5: Testing, Documentation, and Final Submission"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 11 (Testing Your Code)"]], [Plain [Str "Python documentation: the ", Code ("", [], []) "unittest", Str " module"]], [Plain [Str "NiceGUI documentation (official site, nicegui.io); check the documentation for the version you installed"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Run the shared acceptance tests for the logic module."]], [Plain [Str "Check the page by hand with the keyboard and your own screen reader."]], [Plain [Str "Write the README and submit the deliverables."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The shared acceptance tests (listed in the unit overview) are written once for the logic in ", Code ("", [], []) "records.py", Str ". Tests 1 to 5 are automated below; test 6, using every control without color or a mouse, must be checked by hand. The user-level page test from Lesson 11.4 adds a simulated walk through the page, but it runs in Python, so it cannot tell you how a real browser and screen reader behave."], Para [Str "A ", Strong [Str "README"], Str " tells the next reader what the program does and how to run it. Write it in plain text or Markdown with short headings and complete sentences. Include the project title and your name, a description, the run command (", Code ("", [], []) "uv run python app.py", Str "), the keyboard and screen reader instructions that you actually tested, the shared record fields, and a reflection on what was hard."], Para [Strong [Str "Version control."], Str " Keep your project in Git and commit after each working step so you can return to a working version (see the supplemental section at the end of this unit)."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "The test file ", Code ("", [], []) "test_records.py", Str " (put it next to ", Code ("", [], []) "records.py", Str "):"], CodeBlock ("", ["python"], []) "import json
import tempfile
import unittest
from pathlib import Path

import records


def make_clock():
    state = {\"n\": 0}

    def clock():
        state[\"n\"] += 1
        return f\"2026-01-15T10:00:{state['n']:02d}\"
    return clock


class TestRecords(unittest.TestCase):
    def setUp(self):
        self.clock = make_clock()
        self.items = []
        records.add_record(self.items, \"Notebook\", \"Course notes\", \"supplies\", self.clock)
        records.add_record(self.items, \"Pencil\", \"Box of 10\", \"supplies\", self.clock)
        records.add_record(self.items, \"Study plan\", \"Weekly schedule\", \"planning\", self.clock)

    def test_1_empty_title_is_rejected(self):
        record, message = records.add_record(self.items, \"   \", \"x\", \"supplies\", self.clock)
        self.assertIsNone(record)
        self.assertEqual(message, \"A title is required.\")
        self.assertEqual(len(self.items), 3)

    def test_2_new_record_gets_an_unused_id(self):
        records.delete_record(self.items, 2)
        record, _ = records.add_record(self.items, \"Ruler\", \"30 cm\", \"supplies\", self.clock)
        self.assertEqual(record[\"id\"], 4)

    def test_3_update_changes_updated_at_but_not_created_at(self):
        before = dict(records.find(self.items, 1))
        records.update_record(self.items, 1, {\"description\": \"Lecture notes\"}, self.clock)
        after = records.find(self.items, 1)
        self.assertEqual(after[\"created_at\"], before[\"created_at\"])
        self.assertNotEqual(after[\"updated_at\"], before[\"updated_at\"])

    def test_4_delete_removes_only_that_record(self):
        ok, _ = records.delete_record(self.items, 2)
        self.assertTrue(ok)
        self.assertEqual([r[\"id\"] for r in self.items], [1, 3])

    def test_5_save_and_reload_preserves_all_fields(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / \"data.json\"
            records.save_records(path, self.items)
            loaded, message = records.load_records(path)
        self.assertIsNone(message)
        self.assertEqual(loaded, self.items)

    def test_damaged_file_gives_an_empty_list_and_a_message(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / \"data.json\"
            path.write_text('[{\"id\": 1,', encoding=\"utf-8\")
            loaded, message = records.load_records(path)
        self.assertEqual(loaded, [])
        self.assertIn(\"not valid JSON\", message)

    def test_complete_marks_done_and_updates(self):
        record, _ = records.complete_record(self.items, 3, self.clock)
        self.assertTrue(record[\"done\"])
        self.assertNotEqual(record[\"updated_at\"], record[\"created_at\"])

    def test_search_ignores_case_and_checks_description(self):
        self.assertEqual([r[\"title\"] for r in records.search(self.items, \"NOTE\")], [\"Notebook\"])
        self.assertEqual([r[\"title\"] for r in records.search(self.items, \"box\")], [\"Pencil\"])

    def test_blank_title_cannot_be_saved_by_update(self):
        record, message = records.update_record(self.items, 1, {\"title\": \"\"}, self.clock)
        self.assertIsNone(record)
        self.assertEqual(message, \"A title is required.\")


if __name__ == \"__main__\":
    unittest.main()
", Para [Str "Run it from the terminal:"], CodeBlock ("", ["bash"], []) "uv run python -m unittest -v test_records
", Para [Str "A starting point for ", Code ("", [], []) "README.md", Str ":"], CodeBlock ("", ["markdown"], []) "# Personal Data Manager

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
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The command prints one line per test and a summary (the timing differs from run to run):"], CodeBlock ("", ["text"], []) "test_1_empty_title_is_rejected (test_records.TestRecords.test_1_empty_title_is_rejected) ... ok
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
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Testing only that nothing crashed, and not checking the values returned."]], [Plain [Str "Sharing one list of records between tests, so one test's changes affect the next."]], [Plain [Str "Writing a README that only the author can follow, or claiming accessibility that was never tested."]], [Plain [Str "Skipping test 6 because it cannot be automated."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the tests, then break ", Code ("", [], []) "update_record", Str " so it also changes ", Code ("", [], []) "created_at", Str " and watch test 3 fail. Restore it."]], [Plain [Str "Add a test that deleting an unknown id returns ", Code ("", [], []) "False", Str " and a message."]], [Plain [Str "Ask a classmate to follow your README from an empty folder and note where they get stuck."]], [Plain [Str "Complete test 6 by hand: use every control with the keyboard only and record what you found."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Run the tests from the terminal and read the summary line first. For the hand check, use the keyboard only, then repeat with your screen reader or braille display. Record the operating system, browser, screen reader, and versions that you tested, and describe only what you actually tried."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can run the acceptance tests and read the results."]], [Plain [Str "\9744", Space, Str "I can complete a hand check of keyboard and screen reader use."]], [Plain [Str "\9744", Space, Str "I can write a README another person can follow."]], [Plain [Str "\9744", Space, Str "I know what the page test does and does not show."]], [Plain [Str "\9744", Space, Str "I can submit the listed deliverables."]]], HorizontalRule, Header 3 ("assessment-criteria", ["unnumbered", "unlisted"], []) [Str "Assessment Criteria"], Header 4 ("functionality-60", ["unnumbered", "unlisted"], []) [Str "Functionality (60%)"], BulletList [[Plain [Str "\9744", Space, Str "Ability to add new items with all specified attributes."]], [Plain [Str "\9744", Space, Str "Correct display of all current items."]], [Plain [Str "\9744", Space, Str "Correct editing of existing items."]], [Plain [Str "\9744", Space, Str "Correct deletion of items."]], [Plain [Str "\9744", Space, Str "Accurate saving and loading to and from ", Code ("", [], []) "data.json", Str "."]], [Plain [Str "\9744", Space, Str "Search and completion work as described."]], [Plain [Str "\9744", Space, Str "No major bugs or crashes during typical usage."]]], Header 4 ("code-quality-and-structure-20", ["unnumbered", "unlisted"], []) [Str "Code Quality and Structure (20%)"], BulletList [[Plain [Str "\9744", Space, Str "Clear and concise Python code."]], [Plain [Str "\9744", Space, Str "Appropriate use of functions, with rules kept in ", Code ("", [], []) "records.py", Str "."]], [Plain [Str "\9744", Space, Str "Meaningful variable and function names."]], [Plain [Str "\9744", Space, Str "Adequate comments where logic is complex."]], [Plain [Str "\9744", Space, Str "Proper indentation."]]], Header 4 ("accessibility-and-user-experience-15", ["unnumbered", "unlisted"], []) [Str "Accessibility and User Experience (15%)"], BulletList [[Plain [Str "\9744", Space, Str "All interactive elements are correctly labeled for screen readers."]], [Plain [Str "\9744", Space, Str "Clear and consistent feedback in a text status line."]], [Plain [Str "\9744", Space, Str "Logical flow and presentation of information."]], [Plain [Str "\9744", Space, Str "No visual-only cues for critical information."]]], Header 4 ("readme-and-reflection-5", ["unnumbered", "unlisted"], []) [Str "README and Reflection (5%)"], BulletList [[Plain [Str "\9744", Space, Str "Complete and clear README."]], [Plain [Str "\9744", Space, Str "Thoughtful reflection on development and accessibility challenges."]]], HorizontalRule, Header 3 ("deliverables", ["unnumbered", "unlisted"], []) [Str "Deliverables"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Code ("", [], []) "app.py", Str " and ", Code ("", [], []) "records.py", Str ": the complete application code."]], [Plain [Code ("", [], []) "test_records.py", Str ": the acceptance tests."]], [Plain [Code ("", [], []) "data.json", Str ": an example file that shows saved data."]], [Plain [Code ("", [], []) "README.md", Str ", including: the project title and student name; a description of the application; instructions on how to run it (", Code ("", [], []) "uv run python app.py", Str "); instructions for interacting with a screen reader; and a reflection on challenges faced."]]], HorizontalRule, Header 3 ("supplemental-ai-tools-and-version-control", ["unnumbered", "unlisted"], []) [Str "Supplemental: AI Tools and Version Control"], Header 4 ("academic-integrity-ai-and-assessment", ["unnumbered", "unlisted"], []) [Str "Academic Integrity: AI and Assessment"], Para [Str "AI tools must not write, complete, autocomplete, repair, or generate course code or assessment solutions. Students may use only instructor-authorized conceptual explanations that do not produce deliverable code. Git and version control are taught separately and are not a workaround for the assessment-integrity rule."], Header 4 ("git-and-version-control", ["unnumbered", "unlisted"], []) [Str "Git and Version Control"], Para [Strong [Str "Git"], Str " is the most widely used distributed version control system, invented in 2005 by Linus Torvalds for the Linux kernel project."], Para [Strong [Str "Core workflow:"]], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Strong [Str "Working directory"], Str " — Make changes to files."]], [Plain [Strong [Str "Staging area"], Str " — ", Code ("", [], []) "git add", Str " — Stage changes."]], [Plain [Strong [Str "Repository"], Str " — ", Code ("", [], []) "git commit", Str " — Save a permanent snapshot."]], [Plain [Strong [Str "Remote"], Str " — ", Code ("", [], []) "git push", Str " / ", Code ("", [], []) "git pull", Str " — Sync with GitHub."]]], Para [Strong [Str "Why Git is valuable:"]], BulletList [[Plain [Strong [Str "Rollback"], Str " — If a change breaks your app, revert instantly."]], [Plain [Strong [Code ("", [], []) "git blame"], Str " — See exactly which commit introduced a bug."]], [Plain [Strong [Str "Branches"], Str " — Try experiments in isolation without affecting main code."]], [Plain [Strong [Str "Pull requests"], Str " — Review changes with others before merging."]]], Para [Strong [Str "Basic commands:"]], CodeBlock ("", ["bash"], []) "git init                    # Initialize a repository
git add .                   # Stage all changes
git commit -m \"Add feature\" # Save a snapshot
git log                     # View history
git diff                    # See what changed
git checkout -- file.py     # Discard changes to a file
", Para [Str "Windows Powershell"], CodeBlock ("", ["powershell"], []) "git init                    # Initialize a repository
git add .                   # Stage all changes
git commit -m \"Add feature\" # Save a snapshot
git log                     # View history
git diff                    # See what changed
git restore -- file.py     # Discard changes to a file
", Header 3 ("canonical-shared-project-contracts", ["unnumbered", "unlisted"], []) [Str "Canonical Shared Project Contracts"], Header 4 ("unit-10-adventure-and-command-line-to-do-projects", ["unnumbered", "unlisted"], []) [Str "Unit 10: Adventure and command-line to-do projects"], Para [Str "All parallel-language versions must use this exact adventure graph and command set."], Table ("", [], []) (Caption Nothing []) [(AlignDefault, (ColWidth 0.3333333333333333)), (AlignDefault, (ColWidth 0.3333333333333333)), (AlignDefault, (ColWidth 0.3333333333333333))] (TableHead ("", [], []) [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Room"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Exits"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Items / state"]]]]) [(TableBody ("", [], []) (RowHeadColumns 0) [] [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "start_room"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "north → ", Code ("", [], []) "tunnel"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "shiny key"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "tunnel"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "south → ", Code ("", [], []) "start_room", Str "; east → ", Code ("", [], []) "clearing"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "none"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "clearing"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "west → ", Code ("", [], []) "tunnel", Str "; north → ", Code ("", [], []) "locked_door_room"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "north exit is blocked until unlocked"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "locked_door_room"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "south → ", Code ("", [], []) "clearing", Str "; north → ", Code ("", [], []) "treasure_room", Str " after unlocking"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "locked door"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "treasure_room"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "none"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "terminal winning room"]]]])] (TableFoot ("", [], []) []), Para [Str "Commands are ", Code ("", [], []) "north", Str ", ", Code ("", [], []) "south", Str ", ", Code ("", [], []) "east", Str ", ", Code ("", [], []) "west", Str ", ", Code ("", [], []) "take shiny key", Str ", ", Code ("", [], []) "use shiny key", Str ", and ", Code ("", [], []) "quit", Str ". The key begins in ", Code ("", [], []) "start_room", Str "; the player must take it, travel to ", Code ("", [], []) "locked_door_room", Str ", use it there, and then enter ", Code ("", [], []) "treasure_room", Str " to win. Invalid movement must not change the current room."], Para [Str "The CLI to-do manager must store these five fields on every task: ", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "done", Str ", and ", Code ("", [], []) "created_at", Str ". It must support create, list, complete/update, delete, save, and load. Invalid identifiers, empty titles, and malformed persistence data require explicit textual errors."], Header 4 ("unit-11-accessible-personal-data-manager", ["unnumbered", "unlisted"], []) [Str "Unit 11: Accessible Personal Data Manager"], Para [Str "The shared capstone record has exactly these fields:"], CodeBlock ("", ["python"], []) "record = {
    \"id\": 1,
    \"title\": \"Programming notes\",
    \"description\": \"Review lists and dictionaries\",
    \"category\": \"Study\",
    \"created_at\": \"2025-01-15T09:00:00Z\",
    \"updated_at\": \"2025-01-15T09:00:00Z\",
}
", Para [Str "Required operations are list/display, add, search, update, delete, and JSON save/load. Search is case-insensitive across title, description, and category and must report an empty result set clearly. Updating any field other than the ID must preserve the ID and refresh updated_at using the supplied timestamp. Reject blank titles, duplicate/non-positive IDs, incorrect field types, missing fields, and extra fields. A GUI framework is a Python-specific implementation choice; the data model, operations, textual status/error messages, keyboard access, and acceptance tests are not optional or language-specific."], Header 4 ("academic-integrity-and-ai-policy", ["unnumbered", "unlisted"], []) [Str "Academic integrity and AI policy"], Para [Str "AI tools must not write, complete, autocomplete, repair, or generate course code or assessment solutions. Students may use only instructor-authorized conceptual explanations that do not produce deliverable code. Git and version control remain appropriate topics when taught independently of AI code generation."]]