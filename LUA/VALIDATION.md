# Lua Validation

## Current source alignment

- Runtime target: Lua 5.4.
- Unit 0 setup lessons: 4.
- Numbered lessons: 53 across Units 1–11, each with one worked example and one documented output fixture.
- Canonical calculator rounding is half-up to the nearest cent; the $24.50 bill at 15% produces a $3.68 tip and $28.18 total.
- Grade scores, inventory, text, CSV, to-do records, and capstone records use the shared canonical values and fields.
- The adventure lessons use the same five-room graph, key inventory, locked door, commands, and win condition as Python.
- To-do examples use all five fields: `id`, `title`, `description`, `done`, and `created_at`.
- Capstone examples use all six fields: `id`, `title`, `description`, `category`, `created_at`, and `updated_at`.
- Lua-specific adaptations are explicit: one-based sequences, tables as maps/records, truthiness, metatables, no built-in class/tuple/continue construct, no standard JSON module, and no general CSV parser.

## Automated validation

- Checker: `scripts/check_lua_examples.py`.
- Workflow: `.github/workflows/lua-examples.yml`.
- The checker now requires exactly 53 lesson sections, one Lua example and one expected-output fixture per lesson, parses each example, runs it in an isolated directory, supplies deterministic input/file fixtures where required, and compares stdout byte-for-byte with the documented output.
- Earlier passing smoke run [41529629790](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41529629790) predates the exact-output checker and latest content fixes. A new workflow run is required to verify the current revision.

## Remaining work

- Run the exact-output workflow and correct every source/fixture mismatch.
- Add project-level tests for complete adventure and to-do workflows, including save/load and malformed data.
- Select, pin, and test a JSON dependency; select a standards-aware CSV parser and test quoted commas, escaped quotes, and embedded newlines.
- Run a fresh mdBook build and complete Markdown/local-link crawl.
- Perform hands-on keyboard-only, screen-reader, and braille testing with named operating systems, editors, and access technologies.
