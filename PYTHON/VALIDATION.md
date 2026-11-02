# Python Validation

## Current source alignment work

- The canonical student profile, calculator, grade thresholds and scores, inventory, coordinates, text sample, CSV header, to-do schema, and capstone schema are now explicitly used in the Python lesson files.
- Currency calculations use `Decimal` with half-up cent rounding; expected results are a $3.68 tip and $28.18 total for the $24.50 bill.
- The AI-generated-code advice in the capstone was replaced with the course-wide assessment-integrity restriction.
- The complete legacy lesson set has not yet been exhaustively reconciled against the canonical examples; the canonical dataset sections are the authoritative comparison examples pending that pass.

## Canonical example validation

- Checker: `scripts/check_python_curriculum.py`.
- Workflow: `.github/workflows/python-curriculum.yml`.
- Scope: compile and execute the canonical Python code blocks and compare stdout against exact fixtures.
- Manual execution in the current audit verified the student profile, Decimal tip calculation, coordinate distance, grade classification and average, inventory total, and canonical text counts.
- CI: [run 41529629787](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41529629787) passed on the current audit branch. The checker compiled, executed, and matched stdout for all canonical Python examples in its fixture set.

## Not yet verified

- Execute the new checker in GitHub Actions and resolve any discrepancies.
- Run syntax checks over all Python code fences, not only the canonical dataset sections.
- Audit every legacy Python lesson example and replace unrelated or conflicting values where standardization requires the canonical dataset.
- Run project-level tests for the adventure game, CLI to-do persistence, and capstone CRUD/JSON behavior.
- Run a fresh mdBook build and complete Markdown/local-link crawl.
- Perform hands-on keyboard-only, screen-reader, and braille testing with named operating systems, editors, and access technologies.
