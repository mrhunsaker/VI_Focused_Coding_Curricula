# Python Capstone: Accessible Personal Data Manager

These files are the reference implementation for Unit 11 of the Python track.

- records.py: validated record rules and atomic JSON persistence (no user-interface code)
- app.py: NiceGUI page for adding, searching, changing, completing, and deleting records
- app_v1.py: the add, list, and search version (Lesson 11.3)
- hello_app.py: the first NiceGUI page (Lesson 11.1)
- test_records.py: deterministic domain and storage acceptance tests (Lesson 11.5)
- test_app_ui.py, test_app_v1_ui.py, test_hello_ui.py: simulated user-level page tests

## Run

    uv add nicegui
    uv run python app.py

## Test

    uv add --dev pytest pytest-asyncio
    uv run python -m unittest -v test_records
    uv run python -m pytest -q test_app_ui.py

pytest.ini points the page tests at app.py. The other two page tests need their own main_file setting (app_v1.py or hello_app.py).

## Verification status

The domain suite now covers required-field and type validation, the allowed record schema, unique positive IDs, restricted update fields, timestamps, CRUD/completion, case-insensitive search across title/description/category, JSON round-trip, malformed and invalid-UTF-8 input, missing files, and read errors. JSON writes validate first and replace the destination atomically.

The three NiceGUI page suites run in repository PR validation. They simulate page interactions in Python; they do not test a real browser, keyboard focus, a screen reader, or a Braille display. See ACCESSIBILITY_VERIFICATION.md for the manual test protocol and evidence register.