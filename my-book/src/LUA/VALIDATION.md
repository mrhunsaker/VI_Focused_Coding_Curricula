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
- Cross-language contract checker: `scripts/check_curriculum_contracts.py`; workflow: `.github/workflows/curriculum-contracts.yml`. [Run 41538051208](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41538051208) passed the static shared-dataset, project-contract, Unit 0 mapping, and Lua fixture audit.
- Workflow: `.github/workflows/lua-examples.yml`.
- The checker now requires exactly 53 lesson sections, one Lua example and one expected-output fixture per lesson, parses each example, runs it in an isolated directory, supplies deterministic input/file fixtures where required, and compares stdout byte-for-byte with the documented output.
- The exact-output checker passed [run 41537622785](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41537622785): all 53 Lua 5.4.6 examples parsed, executed in isolated directories, and matched their documented stdout fixtures.

- Repository documentation validation: [run 41538243813](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41538243813) passed the complete mdBook build and repository-wide local Markdown link-target check.

## Remaining work

- Add project-level tests for complete adventure and to-do workflows, including save/load and malformed data.
- Select, pin, and test a JSON dependency; select a standards-aware CSV parser and test quoted commas, escaped quotes, and embedded newlines.
- Run a fresh mdBook build and complete Markdown/local-link crawl.
- Perform hands-on keyboard-only, screen-reader, and braille testing with named operating systems, editors, and access technologies.

## Pinned dependency decision and integration checks

- Dependency pins: [DEPENDENCIES.md](DEPENDENCIES.md) — dkjson 2.11-1 and ftcsv 1.5.0-1 for Lua 5.4.
- Integration checker: [../scripts/check_lua_dependencies.lua](../scripts/check_lua_dependencies.lua).
- CI workflow: [../.github/workflows/lua-dependencies.yml](../.github/workflows/lua-dependencies.yml).
- The checker exercises JSON round-trip and malformed JSON, plus CSV quoted commas, escaped quotes, embedded newlines, CRLF records, and the canonical five-column header. These checks are pending their first CI run; dependency selection is complete, validation is not yet claimed.
- Shared project acceptance matrix: [../PROJECT_ACCEPTANCE.md](../PROJECT_ACCEPTANCE.md). It specifies the adventure, five-field to-do manager, and six-field capstone behavioral cases without publishing assessment solutions.
- No complete Lua adventure or CRUD application is claimed as implemented or passed. The acceptance matrix is a test specification pending executable project implementations.
