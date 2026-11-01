# TypeScript Curriculum Standardization Audit

**Branch:** `2026-11-01-curriculum-expansion`  
**Specification:** `lesson_standardization.json`  
**Runtime baseline:** Node.js 26 LTS; TypeScript 7.0.2; strict checking  
**Status:** Lesson alignment and structural coverage complete; strict example type-check is automated; runtime, full-project, book-build, and assistive-technology verification remain separate tasks.

## Scope completed

- All 57 mapped lesson sections across Units 0–11 are present exactly once.
- Every lesson includes Reading References, Learning Objectives, Concept Explanation, Worked Example, Expected Behavior or Output, Common Mistakes, Activities, Accessibility Practice, and Skills Checklist.
- Unit 0 includes runtime/compiler installation, editor setup, workspace configuration, strict project configuration, and compile/run workflow.
- Units 2–4 preserve the shared software-design, expression, input/output, numeric conversion, Math, grade thresholds, score list, array, string, tuple, inventory, and iteration sequence.
- Units 5–8 cover asynchronous terminal input, sentinel-controlled loops, typed functions, classes, inheritance, composition, files, exceptions, and JSON.
- Unit 9 covers built-in Node.js testing, random values, text frequency, and CSV parsing with a standards-aware parser.
- Units 10–11 preserve the text adventure, torch and magic-key puzzle, command-line to-do manager, and personal-data-manager capstone requirements.
- The TypeScript adaptation of the Python NiceGUI capstone is a terminal interface. It preserves the record schema, validation, persistence, CRUD operations, tests, and text-first accessibility criteria.
- TypeScript-specific topics include strict typing, interfaces, readonly tuples, generic types, discriminated unions, type guards, runtime validation, and explicit module configuration.
- The README, 57-entry topic index, teacher guide, and standardization progress tracker were updated.
- Student and instructor AI use is restricted to conceptual understanding and reinforcement; AI must not write, autocomplete, repair, complete, refactor, or generate course code or assessment solutions.

## Canonical shared data

| Context | Shared values |
|---|---|
| Student | Avery, age 16, height 1.72 m, Computer Science |
| Tip calculator | Bill $24.50; tip rate 15%; formatted tip $3.67 and total $28.18 |
| Grade thresholds | A 90+, B 80+, C 70+, D 60+, F below 60 |
| Scores | 82, 91, 76, 88; total 337; average 84.25 |
| Inventory | Notebook, Pencil, Folder; total value $17.50 |
| Coordinates | (3, 4); distance 5 |
| Text | “A student studies programming. Programming develops problem-solving skills.” |
| CSV | student_id, first_name, last_name, score, active |
| To-do record | id, title, description, done, created_at |
| Capstone record | id, title, description, category, created_at, updated_at |

## Language-specific decisions

- TypeScript source is checked and compiled to JavaScript; Node.js executes the emitted JavaScript in the documented workflow.
- Terminal input uses `node:readline/promises` and `async/await`; input still arrives as strings and requires runtime conversion and validation.
- Native TypeScript tuple and readonly tuple types are used for fixed coordinate sequences.
- Interfaces describe object records; `Map<K, V>` represents dynamic key-value collections.
- Union types and type guards model and narrow values. A type assertion does not validate external data.
- Node's built-in `node:test` and `node:assert/strict` are the core test framework; Jest is optional.
- CSV uses `csv-parse` rather than splitting on commas, which fails on quoted fields.
- The capstone uses a terminal interface rather than NiceGUI to preserve the accessible text-first course design.

## Automated validation

The repository includes:

- `scripts/check_typescript_curriculum.mjs`
- `.github/workflows/typescript-curriculum.yml`

Run the checker from the repository root after installing TypeScript 7.0.2, `@types/node` 26, and `csv-parse` 6:

```bash
node scripts/check_typescript_curriculum.mjs
```

The checker verifies the 57 lesson structures and type-checks each fenced TypeScript example independently with strict mode. It does not execute examples or assert their expected output.

## Verification still required

- Execute examples under Node.js 26 and assert the documented outputs, not only successful compilation.
- Run invalid-input, boundary, missing-file, malformed-JSON, and CSV fixture tests.
- Run the complete text adventure and to-do manager end to end.
- Run the personal-data-manager capstone end to end, including CRUD operations, JSON persistence, and at least five tests.
- Run a fresh mdBook build and a full repository Markdown/local-link crawl.
- Perform hands-on keyboard-only, screen-reader, and braille verification with named operating systems, editors, and access technologies. Written accessibility practices are not evidence that assistive-technology testing has occurred.
