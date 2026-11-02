# Python Validation

## Current source alignment

- Student dictionary and profile examples use the canonical Avery record: name, age 16, height 1.72 m, and Computer Science.
- Numeric examples use the $24.50 bill and 15% tip with decimal half-up cent rounding; expected tip $3.68 and total $28.18.
- Grade examples use thresholds A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, otherwise F, and scores 82, 91, 76, 88.
- List, dictionary, and function examples use the Notebook/Pencil/Folder inventory and its $17.50 total.
- Text and CSV examples use the canonical text sample and five-column student CSV contract. CSV is parsed with `csv.DictReader`, not manual comma splitting.
- JSON examples use the five-field to-do record. Unit 10 project instructions use the shared five-room adventure and five-field to-do contract. Unit 11 uses the six-field capstone record.
- The conflicting AI-generated-code advice was removed from the capstone material. Git is presented independently of AI code generation.
- Unit 0's mapping now reflects all five live Python setup lessons.

## Automated validation

- Checker: `scripts/check_python_curriculum.py`.
- Cross-language contract checker: `scripts/check_curriculum_contracts.py`; workflow: `.github/workflows/curriculum-contracts.yml`. [Run 41538051208](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41538051208) passed the static shared-dataset, project-contract, Unit 0 mapping, and Lua fixture audit.
- Workflow: `.github/workflows/python-curriculum.yml`.
- Scope: canonical profile, calculator, coordinates, grades, inventory, text analysis, CSV parsing, task schema, and capstone record examples; compile, execute, and exact stdout checks.
- Previous passing run [41529629787](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41529629787) predates the latest legacy-example and project-contract edits. The latest revision, including the scripted adventure win-path test, passed [run 41538051184](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41538051184). Canonical examples compiled, executed, and matched exact stdout; the adventure test completed the shiny-key, locked-door, and treasure-room path.

- Repository documentation validation: [run 41538243813](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41538243813) passed the complete mdBook build and repository-wide local Markdown link-target check.

## Remaining work

- Run the updated canonical checker in GitHub Actions and resolve failures.
- Run syntax checks over runnable Python examples across the full track.
- Complete to-do manager and capstone acceptance tests without publishing full assessment solutions.
- Run a fresh mdBook build and complete Markdown/local-link crawl.
- Perform hands-on keyboard-only, screen-reader, and braille testing with named operating systems, editors, and access technologies.
