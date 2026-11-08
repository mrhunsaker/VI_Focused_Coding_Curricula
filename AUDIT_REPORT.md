# Curriculum Audit and Change Report (3 November 2026)

## Scope and method

The repository was cloned and audited. Code was executed only where a toolchain was available: Python 3 (all tracks' canonical source), C and C++ (gcc 13.3), Go 1.22.2, Lua 5.4.6. Java (runtime only, no compiler), JavaScript (Node 22), TypeScript, Kotlin, C#, Julia, Swift, and Rust were checked for structure and cross-track consistency, not for whether the code runs. Version claims in the JSON (for example Go 1.27, Rust 1.99, Node 26, TypeScript 7) were not checked. Nothing was tested with a screen reader or braille display.

## Changes made

### Python (canonical source)
- Replaced Alice, Charlie, Jamie, Emily, Dog, Car, Employee, and ad hoc values with the shared datasets in Units 1–11.
- Added the tip calculator (24.50 at 0.15), the full A/B/C/D/F thresholds with boundary scores 90, 89, 80, 79, 70, 69, 60, 59, the scores 82/91/76/88, the Notebook/Pencil/Folder inventory, the text sample, `students.csv`, the five-field to-do record, and the six-field capstone record.
- Every new expected-output block was produced by running the code. Interactive examples show a transcript with typed input.
- Fixed Lesson 10.3: the adventure crashed with `KeyError: 'treasure_room'` after unlocking the door, the "door is locked" message was unreachable, and the room description still mentioned the key after it was taken.
- Replaced the "AI-Powered Coding Tools" section with the course AI policy, and aligned the Python teachers guide (it had allowed AI hints and "if an assignment permits AI").
- Added search and completion to the Python capstone requirements to match the JSON specification.

### Lua
- Rewrote `LUA/lessons.md`: 57 lessons (Unit 0 has 4; Units 1–11 have 53), all nine template sections, lesson-specific content, shared datasets, and Lua-specific semantics (1-based indexes, truthiness, `goto continue`, `pcall`, `<close>`, no JSON in the standard library).
- 56 of 56 Lua examples pass the repository's checker. A separate re-run of every example against its documented output matched exactly (0 mismatches). Concept, mistakes, activities, and accessibility sections are distinct in 57 of 57 lessons.
- Included a small teaching JSON encoder/decoder in Lessons 8.5, 10.4, and 11.2. It was tested with a round trip and six malformed inputs only.
- Updated `LUA/README.md` and `LUA/VALIDATION.md` to state what was and was not verified.

### Foundations
- Added `FOUNDATIONS/unit-p-computing-foundations.md` (six lessons) and `FOUNDATIONS/FOUNDATIONS_README.md`.
- Added a Unit P entry at the start of `unit_map` in `lesson_standardization.json`, an equivalence rule requiring Unit P as a prerequisite, updated Lua and Python progress records, and an `audit_2026_11_03` record of open findings. The JSON still parses and keeps its original formatting.
- Added a Foundations section to `SUMMARY.md`.

## Structural comparison of the other tracks

Counts of numbered lessons: Java, JavaScript, TypeScript, Kotlin, C, C++, C#, Julia, Swift, Rust, Go, Lua have 57. Python has 56: it has five Unit 0 lessons (0.1–0.5) and Unit 11 ends at 11.3.

- **Python does not follow `lesson_template`.** Its lessons use topical headings (for example "The Three-Phase Development Process") and lack Learning Objectives, Concept Explanation, Expected Behavior or Output, and Common Mistakes headings. The JSON calls Python canonical, so the template and the canonical source disagree. A decision is needed on whether to convert Python to the template.
- Java, JavaScript, TypeScript, Kotlin, Julia, Swift, Rust, Go, and Lua have all nine section headings in every lesson.
- C, C++, and C# lack a separate Expected Behavior or Output section in many lessons: C 38 of 57, C++ 56 of 57, C# 57 of 57. They give the expected result as an inline sentence.
- Unit-level Overview sections: Go has them for 8 of 12 units, Java and JavaScript for 11 of 12; the Kotlin layout differs.

## Open findings (not changed)

1. Tip rounding errors: the C lesson says `$3.68` but `printf("%.2f", 24.50 * 0.15)` prints 3.67 (verified by compiling). TypeScript says 3.68 but `toFixed(2)` gives 3.67. JavaScript states both values for the same calculation. Java's `String.format` really does print 3.68, so tracks should explain the difference instead of showing one value everywhere.
2. Java uses scores 76/88/91/84 and a 0.18 tip rate.
3. Go, Rust, C#, Julia, Swift, and C++ are largely templated, with few distinct Common Mistakes or Activities sections and about one to three lines of code per worked example. Go Lesson 1.1's expected text promises shared example data that its code does not use.
4. The AI policy statement is missing from the C, C#, Swift, and Julia lesson files.
5. TypeScript describes a torch-and-magic-key adventure; Python and now Lua use a shiny key. Python Lesson 10.2 uses cave/tunnel/clearing and Lesson 10.3 uses start/locked_door_room/treasure_room.
6. `cs_curriculum_final/` and the two zip files duplicate live content and can drift.
7. In the JSON, the Rust, Go, Lua, and Java progress records sit outside `completed_tracks`, and several `not_yet_verified` lists contain duplicates.
8. The Python NiceGUI snippet in Unit 11 has not been executed.

## Needs your manual review

- Reading-reference chapter numbers in the Lua lessons follow the fourth edition of *Programming in Lua*. Check them against your copy.
- The shared students.csv rows (Avery Student 91, Jordan Lee 82, Casey Smith 76) were taken from the JavaScript track because the JSON lists only the column names; confirm they should be canonical.
- All accessibility claims. They are design intentions only.
