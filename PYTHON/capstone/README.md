# Python Capstone: Accessible Personal Data Manager

These files are the verified code for Unit 11 of the Python track.

- `records.py`: the rules and JSON storage (no user-interface code)
- `app.py`: the finished NiceGUI page (Lessons 11.3 and 11.4)
- `app_v1.py`: the add, list, and search version (Lesson 11.3)
- `hello_app.py`: the first NiceGUI page (Lesson 11.1)
- `test_records.py`: the shared acceptance tests for the logic (Lesson 11.5)
- `test_app_ui.py`, `test_app_v1_ui.py`, `test_hello_ui.py`: user-level page tests

## Run

    uv add nicegui
    uv run python app.py

## Test

    uv add --dev pytest pytest-asyncio
    uv run python -m unittest -v test_records
    uv run python -m pytest -q test_app_ui.py

`pytest.ini` points the page tests at `app.py`. The other two page tests need their own `main_file` setting (`app_v1.py` or `hello_app.py`).

## Verification status

Run with Python 3.12 and NiceGUI 3.19.0: 9 unit tests pass, and the three page tests pass. The page tests simulate the page in Python. They do not test a real browser, a screen reader, or a braille display.
