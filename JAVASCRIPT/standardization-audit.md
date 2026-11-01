# JavaScript Curriculum Standardization Audit

**Branch:** `2026-11-01-curriculum-expansion`  
**Specification:** `lesson_standardization.json`  
**Status:** Content and structural alignment complete; runtime and full accessibility verification pending.

## Scope completed

- Units 0–11 mapped to the Python curriculum's 57 lesson sections.
- Unit 0 now includes four setup lessons, including project initialization, terminal execution, npm scripts, and explicit module-mode configuration.
- Unit 2 follows the shared sequence: software development process, expressions and assignment, input/output, numeric conversion, and Math.
- Units 3–4 use the canonical grade thresholds, score list, student profile, inventory, and coordinates.
- Units 5–8 cover asynchronous terminal input, while loops, functions, OOP, files, exceptions, and JSON.
- Unit 9 covers function/class testing, random values, text-frequency analysis, and CSV parsing.
- Unit 10 preserves the three-room text adventure, torch, magic key, inventory behavior, and command-line to-do requirements.
- Unit 11 implements the accessible terminal-based personal-data-manager capstone with the shared record fields and CRUD requirements.
- The README, index, teacher guide, and `lesson_standardization.json` progress record were updated.

## Language-specific adaptations

| Python concept or workflow | JavaScript / Node.js adaptation |
|---|---|
| `input()` | Asynchronous `node:readline/promises` with `await` |
| Integer and float types | JavaScript `Number`, with explicit conversion and validation |
| `math` module | Built-in `Math` object |
| Lists | Arrays |
| Tuples | No direct JavaScript equivalent; frozen arrays illustrate fixed-sequence intent |
| Dictionaries | Plain objects for records; `Map` for dynamic key-value collections |
| `*args` / `**kwargs` | Rest parameters and options objects; no direct keyword-argument equivalent |
| Python classes | JavaScript classes, private fields, inheritance, and composition |
| `with open()` | Promise-based Node.js file APIs and explicit error handling |
| `unittest` | Built-in `node:test` and `node:assert/strict` |
| Python CSV module | Standards-aware `csv-parse` package |
| NiceGUI capstone | Accessible terminal interface preserving core data model, CRUD, persistence, and acceptance criteria |

## Validation performed

- 57 lesson sections checked for all nine required template sections.
- 63 fenced JavaScript examples syntax-parsed successfully using the available V8 JavaScript parser.
- Relative Markdown links in the README, index, teacher guide, and four core lesson files resolved against the branch tree.
- Canonical score total (337), score average (84.25), tip display behavior, and inventory total ($17.50) checked; expected outputs were corrected where needed.

## Not yet verified

- The 63 examples have **not** all been executed under Node.js 26. Syntax parsing is not runtime validation.
- Exact expected-output assertions and broader invalid-input, missing-file, malformed-JSON, and CSV fixture tests remain to be run.
- The complete text adventure, to-do manager, and personal-data-manager capstone have not been run end to end.
- A fresh mdBook build and full repository link crawl remain pending.
- Hands-on keyboard-only, screen-reader, and braille testing remains pending. Do not interpret the written accessibility practices as evidence of completed assistive-technology testing.

## Repeatable structural check

Run:

```bash
node scripts/check_javascript_curriculum.mjs
```

The checker verifies lesson-template coverage and parses JavaScript code fences. It deliberately does not execute examples or assert their output. A GitHub Actions workflow runs this check on changes to the JavaScript curriculum.
