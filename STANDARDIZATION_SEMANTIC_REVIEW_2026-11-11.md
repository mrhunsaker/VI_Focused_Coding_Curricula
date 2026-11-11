# Standardization Tracker Semantic Review — 2026-11-11

## Scope and method

Reviewed the 16 conflict blocks from the original `lesson_standardization.json` at commit `62d2f3914315f97b02953849320157e042d0e934`. Compared each recovered choice with the current Python source map, shared project contracts, language-specific lesson files, and recorded validation evidence. Also searched and fetched the current source files for unresolved conflict markers.

The original recovery used a content-length heuristic (10 HEAD selections, 6 incoming selections). This review confirms that several choices were sound, but it also identifies choices that required correction or qualification. A longer side is not automatically the semantically correct side.

## Review of the 16 tracker conflicts

| Block | Review outcome | Finding |
|---:|---|---|
| 1 | Confirm incoming | Unit P is required; the Foundations primer exists and contains seven lessons. |
| 2 | Corrected | The current Python Unit 0 has four lessons, not five. Lesson 0.5 was merged into 0.4. |
| 3 | Corrected | Preserve all four setup outcomes: runtime, accessible editor, workspace/first file, and terminal Hello World. Accessibility and terminal workflow are combined in 0.4. |
| 4 | Confirm incoming | The five capstone lessons are split into 11.1–11.5, with distinct 11.3, 11.4, and 11.5 responsibilities. |
| 5 | Confirm incoming | The Python capstone implementation files exist. This does not establish that all lesson-source instructions are conflict-free. |
| 6 | Confirm HEAD, qualify | The decimal half-up reference tip is 3.68 and total 28.18. Python's current f-string example prints 3.67; the tracker separately documents language-specific display behavior. |
| 7 | Confirm incoming | The canonical CSV rows and notes-file metadata extend the shared dataset. |
| 8 | Confirm incoming | The Unit P prerequisite reference is consistent with the Foundations primer. |
| 9 | Supersede | The competing date/current-language values were historical branch snapshots; current metadata has been refreshed. |
| 10 | Confirm HEAD, qualify | C++ Unit 10.2 uses the canonical `start_room → tunnel` transition. The related checker/CI rerun is still a verification task. |
| 11 | Confirm HEAD | The C++ CI rerun remains pending until a current run verifies the edited example. |
| 12 | Supersede | The old next-track list and PR #4 instruction were stale; current priorities are now recorded. |
| 13 | Confirm HEAD | Go's capstone lesson declares the six canonical record fields; end-to-end persistence testing remains pending. |
| 14 | Confirm HEAD | Lua has four Unit 0 lessons and 53 numbered Unit 1–11 lessons; the incoming 57-numbered-lesson snapshot is stale. |
| 15 | Downgrade to blocked | Java Unit 10 and Unit 11 still contain unresolved conflict blocks, in addition to pending capstone and accessibility testing. |
| 16 | Keep richer record, downgrade status | The fuller Python progress record is more useful, but Units 1, 2, 3, 4, 8, 10, and 11 still contain conflict blocks. |

## Tracker corrections applied

- Replaced all 12 stale Python unit source paths with the exact paths linked by `PYTHON/lessons.md`; the Unit P source path was also checked. All 13 targets exist.
- Corrected Unit 0 from five lesson titles to the four current headings. Removed the obsolete standalone 0.5 entry.
- Updated Unit 0's parallel examples to include runtime installation, accessible editor configuration, workspace/first file, and terminal Hello World.
- Downgraded Python and Java status fields so unresolved lesson-source conflicts are not hidden by historical CI results.
- Recorded this review and the remaining conflict inventory in `lesson_standardization.json`.

## Current source conflict inventory

A current-branch search and direct file fetch found **41 unresolved conflict blocks in 20 curriculum files**:

| Track | Files | Conflict blocks |
|---|---:|---:|
| Python | 7 | 15 |
| TypeScript | 4 | 6 |
| Lua | 5 | 5 |
| Java | 2 | 12 |
| Rust | 1 | 2 |
| Kotlin | 1 | 1 |
| **Total** | **20** | **41** |

Affected files:

- `PYTHON/unit01-foundations-of-computing-and-getting-started-with-pytho.md` (1)
- `PYTHON/unit02-writing-simple-programs-and-numeric-computations.md` (1)
- `PYTHON/unit03-control-flow-decisions-and-loops.md` (1)
- `PYTHON/unit04-data-structures-lists-and-dictionaries.md` (2)
- `PYTHON/unit08-files-and-exceptions.md` (1)
- `PYTHON/unit10-project-based-learning-building-text-based-applications.md` (3)
- `PYTHON/unit11-capstone-project-accessible-personal-data-manager.md` (6)
- `TYPESCRIPT/unit00-accessible-development-environment.md` (1)
- `TYPESCRIPT/unit01-foundations-of-computing.md` (2)
- `TYPESCRIPT/unit04-data-structures-arrays-tuples-and-objects.md` (2)
- `TYPESCRIPT/unit09-testing-and-data-analysis.md` (1)
- `LUA/unit01-foundations-of-computing.md` (1)
- `LUA/unit03-control-flow-decisions-and-loops.md` (1)
- `LUA/unit04-data-structures-lists-and-dictionaries.md` (1)
- `LUA/unit05-user-input-and-while-loops.md` (1)
- `LUA/unit08-files-and-exceptions.md` (1)
- `JAVA/unit10-project-based-learning-text-applications.md` (6)
- `JAVA/unit11-capstone-accessible-personal-data-manager.md` (6)
- `RUST/unit00-accessible-environment-and-toolchain.md` (2)
- `KOTLIN/examples_expected.json` (1)

The Kotlin fixture is not valid JSON while its conflict block remains. The Python and Java Unit 10/11 conflicts affect project contracts, expected behavior, and capstone instructions and should be resolved before those tracks are treated as publishable.

## Additional project-contract divergence

- JavaScript Unit 10 begins with an obsolete three-room cave/torch/magic-key description, while later content describes the five-room shiny-key graph.
- TypeScript Unit 10 contains both the obsolete torch/magic-key implementation and newer five-room shiny-key requirements.
- Python Unit 10 has a conflict between a five-room canonical graph and an older three-room graph, plus competing to-do project content.
- Python Unit 11 has six conflicts affecting the record schema, project setup, AI policy, and canonical project contracts.
- Java Unit 10/11 conflicts include generic placeholder lessons on one side and detailed Java 25 examples with expected output on the other.

## Next work

1. Resolve the 41 source conflict blocks semantically; do not apply a longest-side rule.
2. Replace JavaScript and TypeScript's obsolete three-room torch/magic-key content with the canonical five-room shiny-key contract.
3. Regenerate and validate Kotlin expected-output fixtures against the current Kotlin lessons.
4. Run JSON validation, language-specific checkers, mdBook build, and repository-wide local-link validation after repairs.
5. Keep hands-on keyboard, screen-reader, and braille verification pending until it has been performed and recorded.

This review does not claim that the source conflicts have been repaired. It establishes the correct repair priorities and prevents historical tracker status from being mistaken for current verification.
