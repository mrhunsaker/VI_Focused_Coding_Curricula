# Project acceptance test plan — Python and Lua

This file defines student-project acceptance behavior without publishing completed project solutions. The cases are deterministic specifications for instructor-authored tests and manual assessment. The Python and Lua projects must pass the same behavioral cases; syntax and interface details may differ.

## Unit 10A: Text adventure

Use the canonical graph in `lesson_standardization.json`.

| ID | Scenario | Required result |
|---|---|---|
| ADV-01 | Start a new game | Current room is `start_room`; shiny key is visible; inventory is empty. |
| ADV-02 | Take the shiny key in `start_room` | Key is removed from room items and appears exactly once in inventory. |
| ADV-03 | Take the key a second time | Clear error; inventory and room contents do not change. |
| ADV-04 | Move north, east, north without unlocking | Player reaches `locked_door_room`; no transition to treasure room. |
| ADV-05 | Attempt north at the locked door without key | Door-locked message; player remains in `locked_door_room`. |
| ADV-06 | Attempt to use the key before entering the locked-door room | Clear error; door remains locked. |
| ADV-07 | Use the key in `locked_door_room` while carrying it | Door unlocks once and the north exit becomes available. |
| ADV-08 | Move north after unlocking | Player enters `treasure_room` and receives the win message. |
| ADV-09 | Attempt an unknown direction or command | Clear textual error; current room and inventory remain unchanged. |
| ADV-10 | Quit from a nonterminal room | Game exits cleanly without a traceback. |

The canonical successful command sequence is: `take shiny key`, `north`, `east`, `north`, `use shiny key`, `north`.

## Unit 10B: Command-line to-do manager

Every task has exactly five fields: `id`, `title`, `description`, `done`, and `created_at`.

| ID | Scenario | Required result |
|---|---|---|
| TODO-01 | Add a task with a valid title, description, and fixed timestamp | New task has a unique positive integer ID and all five fields; `done` is false. |
| TODO-02 | Add a blank or whitespace-only title | Reject with a useful message; task collection is unchanged. |
| TODO-03 | List an empty collection | Report that there are no tasks; do not crash. |
| TODO-04 | List multiple tasks | Stable ID order; display title and completion state. |
| TODO-05 | Complete an existing task by ID | Only the matching task's `done` value changes. |
| TODO-06 | Update title/description of an existing task | Preserve ID, done state, and created_at; validate title. |
| TODO-07 | Complete or update a missing ID | Clear not-found result; no record changes. |
| TODO-08 | Delete an existing task | Only that task is removed; remaining IDs remain unchanged. |
| TODO-09 | Delete a missing or malformed ID | Clear error; collection remains unchanged. |
| TODO-10 | Delete a task, then add another | New ID does not collide with any surviving ID. |
| TODO-11 | Save and reload multiple tasks | All five fields and values round-trip exactly. |
| TODO-12 | Load a missing file | Clear first-run/absent-file behavior; no traceback. |
| TODO-13 | Load malformed JSON or a non-list top level | Reject with a textual error; do not silently replace valid in-memory data. |
| TODO-14 | Load a record with a missing or extra field | Reject the file and identify the schema problem. |
| TODO-15 | Load records with incorrect field types or duplicate/non-positive IDs | Reject invalid data; do not partially load it. |

Use fixed timestamps in tests. Do not compare wall-clock values in exact-output fixtures.

## Unit 11: Personal data manager

Every record has exactly six fields: `id`, `title`, `description`, `category`, `created_at`, and `updated_at`.

| ID | Scenario | Required result |
|---|---|---|
| CAP-01 | Add a valid record | Assign a unique positive integer ID and preserve all six fields. |
| CAP-02 | Add blank title or category | Reject with textual feedback; no record is added. |
| CAP-03 | List records | Present every record in stable ID order with all relevant fields available as text. |
| CAP-04 | Search by exact title, partial title, description, or category | Case-insensitive matching returns all matching records. |
| CAP-05 | Search with no matches | Report no matches explicitly. |
| CAP-06 | Update an existing record | Preserve ID and created_at; update updated_at from a deterministic supplied timestamp. |
| CAP-07 | Update a missing ID | Clear not-found result; no record changes. |
| CAP-08 | Delete an existing record | Remove only the selected record and confirm the action. |
| CAP-09 | Delete a missing ID | Clear not-found result; no record changes. |
| CAP-10 | Save and reload records | All six fields round-trip exactly. |
| CAP-11 | Load missing or malformed JSON | Provide a clear recoverable error; do not crash or partially overwrite records. |
| CAP-12 | Load missing/extra fields, invalid types, duplicate IDs, or non-positive IDs | Reject invalid records and explain the validation failure. |
| CAP-13 | Keyboard-only operation | Every operation is reachable and usable without a mouse. |
| CAP-14 | Screen-reader/braille review | Labels, prompts, status, errors, and record content are available in a meaningful reading order; record the actual platform and assistive technology tested. |

## Execution and sign-off policy

- These are acceptance requirements, not claims that the projects have been implemented or passed.
- The public curriculum repository must not contain complete assessment solutions.
- Add instructor-only executable tests only after private solution storage is available and access-controlled.
- Record a test as passed only when a runnable implementation or a controlled manual test has actually been exercised.
- Accessibility sign-off requires hands-on testing; static source review is insufficient.
