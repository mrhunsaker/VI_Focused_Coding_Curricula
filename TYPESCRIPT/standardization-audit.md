# TypeScript Curriculum Standardization Audit

**Branch:** `2026-11-01-curriculum-expansion`  
**Specification:** `lesson_standardization.json`  
**Runtime baseline:** Node.js 26 LTS; TypeScript 7.0.2; strict checking  
**Status:** Content alignment complete; strict example type-check automated; runtime, full-project, book-build, and assistive-technology verification pending.

## Scope completed

- All 57 mapped lesson sections across Units 0–11 are present exactly once.
- Every lesson contains all nine required sections: references, objectives, concept explanation, worked example, expected behavior, common mistakes, activities, accessibility practice, and skills checklist.
- The sequence preserves the shared Python learning objectives, problem contexts, datasets, and assessment requirements.
- TypeScript-specific material includes strict typing, interfaces, readonly tuples, generics, discriminated unions, type guards, runtime validation, and explicit module configuration.
- The text adventure preserves the cave, tunnel, clearing, torch, magic key, inventory, and gate puzzle.
- The to-do project preserves the shared task fields and persistence requirement.
- The capstone uses a text-based terminal interface instead of NiceGUI while preserving the record schema, validation, persistence, CRUD operations, testing, and accessibility criteria.
- The README, topic index, teacher guide, checker, and GitHub Actions workflow are updated.
- AI use is restricted to conceptual understanding and reinforcement; AI must not write, autocomplete, repair, complete, refactor, or generate course code or assessment solutions.

## Canonical data

| Context | Shared values |
|---|---|
| Student | Avery, age 16, height 1.72 m, Computer Science |
| Tip calculator | $24.50 bill; 15% tip; formatted tip $3.67 and total $28.18 |
| Grades | A 90+, B 80+, C 70+, D 60+, F below 60 |
| Scores | 82, 91, 76, 88; total 337; average 84.25 |
| Inventory | Notebook, Pencil, Folder; total value $17.50 |
| Coordinates | (3, 4); distance 5 |
| Text | “A student studies programming. Programming develops problem-solving skills.” |
| CSV | student_id, first_name, last_name, score, active |
| To-do fields | id, title, description, done, created_at |
| Capstone fields | id, title, description, category, created_at, updated_at |

## Automated validation

The repository includes `scripts/check_typescript_curriculum.mjs` and `.github/workflows/typescript-curriculum.yml`.

GitHub Actions run [41345416186](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41345416186) passed on Node.js 26.13.0. It validated all 57 lesson sections and strictly type-checked all 58 fenced TypeScript examples using TypeScript 7.0.2, `@types/node` 26, and `csv-parse` 6.

Run the checker after installing those dependencies:

```bash
node scripts/check_typescript_curriculum.mjs
```

The checker type-checks isolated examples. It does not execute them or assert expected output.

## Verification still required

- Execute examples under Node.js 26 and assert documented outputs.
- Test invalid input, boundaries, missing files, malformed JSON, and CSV fixtures.
- Run the text adventure and to-do manager end to end.
- Run the capstone end to end, including CRUD, JSON persistence, and at least five tests.
- Run a fresh mdBook build and a complete repository Markdown/local-link crawl.
- Perform hands-on keyboard-only, screen-reader, and braille verification. Written accessibility practices do not prove assistive-technology testing occurred.
