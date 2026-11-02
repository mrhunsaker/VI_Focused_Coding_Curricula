# Lua Validation

## Current source alignment

- Runtime target: Lua 5.4.
- Unit 0 setup lessons: 4 (maintained in the Lua setup material).
- Numbered lessons: 53 across Units 1–11.
- The previous generic worked-example pattern has been replaced with 53 lesson-specific examples covering the mapped topics and canonical shared data.
- Common-mistake lists and activities have been revised by lesson topic rather than repeating one universal set of prompts.
- Lua-specific adaptations are explicit: one-based sequences, tables as maps/records, truthiness, metatables, no built-in class/tuple/continue construct, no standard JSON module, and no general CSV parser.
- The shared student, calculator, grade, score, inventory, coordinate, text, CSV, task, and capstone data contracts are documented in the course.

## Automated validation history

- Checker: `scripts/check_lua_examples.py`.
- Workflow: `.github/workflows/lua-examples.yml`.
- Scope: `luac5.4 -p` syntax validation and independent smoke execution of each fenced Lua example.
- Earlier CI run [41336626558](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41336626558) passed against the prior lesson content. **That run does not validate the rewritten examples in this branch.**
- The rewritten course passed [run 41529629790](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41529629790) on the current audit branch using Lua 5.4.6. All 53 fenced examples parsed and smoke-executed independently. This verifies syntax and clean process exit only; the checker does not compare stdout with the documented expected output.

## Not yet verified

- Run the Lua 5.4 workflow against the rewritten 53 examples and fix every parse/runtime failure.
- Add exact expected-output assertions for every deterministic example; keep nondeterministic or environment-dependent examples isolated and explicitly qualified.
- Test the adventure game and CLI to-do manager end to end, including all movement, inventory, puzzle, CRUD, and persistence cases.
- Select, pin, and test a JSON dependency; test malformed JSON and missing-file behavior.
- Select a standards-aware CSV parser and test quoted commas, escaped quotes, and embedded newlines.
- Run a fresh mdBook build and complete Markdown/local-link crawl.
- Perform hands-on keyboard-only, screen-reader, and braille testing with named operating systems, editors, and access technologies.
