# Curriculum Standardization Report, Round 2 (5 November 2026)

This report covers the second pass: converting Python to the standard template, fixing rounding errors, making the sample students canonical, and standardizing the other tracks as far as could be verified. The first report is `AUDIT_REPORT.md`.

## What was run, and with what

Run here: Python 3.12 (plus NiceGUI 3.19.0, pytest), gcc 13.3 (C17, C++20), Go 1.22.2, Lua 5.4.6, JDK 21 (javac), .NET 8, rustc 1.75 (edition 2021), Node 22, TypeScript 7.0.2 with tsx. Not available here: Julia, Swift, and a working Kotlin compiler. Several toolchains are older than the course baselines (JDK 21 vs 25, .NET 8 vs 10, rustc 1.75 vs 1.99, Go 1.22 vs 1.27), so the captured outputs should be re-run on the baseline versions. Nothing was tested with a screen reader or braille display.

## 1. Python conversion (done)

- All 57 Python lessons have the nine standard sections in the standard order, with a Worked Example and an Expected Behavior or Output section in every lesson. Learning Objectives come from each lesson's Skills Checklist.
- Lesson 0.5 was merged into 0.4. Unit 11 was split into 11.1–11.5. The Git and version-control section and the Assessment Criteria and Deliverables were kept.
- Existing concept text was kept. Missing parts (mistakes, activities, accessibility practice, some worked examples) were written for each lesson. Expected output was produced by running the code, using scripted input for interactive programs.
- The old capstone was a skeleton that referred to functions that did not exist. It was replaced with real code in `PYTHON/capstone/`: `records.py` (logic), `app.py`, `app_v1.py`, `hello_app.py`, and tests. Results: 9 unit tests pass; 3 NiceGUI user-simulation page tests pass (one was also checked with a failing negative control); the finished app was started and answered HTTP 200. The page tests simulate the page in Python and do not replace a real browser and screen reader.

## 2. Rounding errors (done)

C, JavaScript, and TypeScript said the tip displays as 3.68. Corrected to 3.67 (checked by running each). Java really prints 3.68, and the Java lesson now says why. C#'s `F2` format prints 3.67 but its `0.00` format and `Math.Round` give 3.68; this is recorded in `lesson_standardization.json` under `calculator_display_rounding`. Swift, Julia, and Kotlin were not run, so no value is claimed for them.

## 3. Canonical sample students (done)

`students.csv` rows added to the JSON as canonical: 1, Avery, Student, 91, true; 2, Jordan, Lee, 82, true; 3, Casey, Smith, 76, false. The `notes.txt` pattern and the optional capstone field `done` are also recorded.

## 4. Standardization across tracks

Verified by script for all 13 tracks: 57 lessons each, the nine sections in order in every lesson, one H1 per unit and an Overview for each of the 12 units, no broken relative links, balanced code fences.

Fixes made:
- Unit P prerequisite pointer and one identical AI policy sentence in every track's README and lesson file.
- Unit 0 layout normalized in C, C++, C#, Julia, Swift, Rust, and Go.
- Unit headings and overviews added to Go (Units 8–11), Java (Unit 0), and Kotlin (all units). Kotlin lessons moved to the standard heading levels, and both Kotlin check scripts were updated to match.
- Duplicate unit headings removed from TypeScript; 11 JavaScript lessons reordered. A bug in my first reordering damaged JavaScript Lesson 11.5; it was caught by the check and restored from the original.
- Go: 29 lessons had program listings where the Concept Explanation belonged. The listings were moved into Worked Example (all compile and run; the Go checker now passes 158 examples), and short Go-specific concept text was written. Five listings that did not compile were removed.
- Java: tip example, scores, and one grade example changed to the shared data.
- Real captured output now sits in Expected Behavior or Output for Java (57), C (45, plus written statements for the 8 lessons with no runnable code), C++ (53), Go (53), Rust (53), and C# (53).

Repository checkers after the changes: C 49, C++ 54, Go 158, Lua 56, and Java 57 (compiled with `--release 21`) pass. The JavaScript and Kotlin structure checks pass. The Rust checker cannot run here (needs edition 2024) and the TypeScript checker needs `node_modules`.

## 5. Still not standardized (the real remaining work)

Distinct text per lesson, counted over the 57 lessons (concept / mistakes / activities / accessibility):
- Python 57/57/57/57, JavaScript 57/57/57/57, TypeScript 57/57/57/57, Lua 57/57/57/57: fine.
- C 57/57/57/**6**, C++ 57/57/57/**6**: accessibility text is repeated.
- Go 38/13/54/3, Rust 15/12/54/2, Swift 57/15/15/5, Julia 57/15/15/5, C# 16/16/16/6, Java 57/12/12/**1**: mostly templated.
- **Kotlin 2/2/2/2 and about 2 lines of code per example: effectively one template repeated 57 times.** This is the worst track.

Other open items:
1. Kotlin, Swift, Julia, JavaScript, and TypeScript expected-output text was not regenerated by running the code.
2. Java worked examples still include non-canonical data in topic examples (milestone lists and similar).
3. The 29 repaired Go concept sections are short and generic.
4. TypeScript's adventure uses a torch and magic key; Python and Lua use a shiny key. Python Lessons 10.2 and 10.3 use different room names.
5. `cs_curriculum_final/` and the zip files duplicate live content. The Java record in the JSON sits outside `completed_tracks`.
6. Python lesson concept sections are still short in places (kept from the original).

## Recommended order for the next pass

Kotlin first, then Java, Rust, C#, Swift, Julia, and Go concept text. The Lua rewrite is a workable pattern: write each lesson's code against the shared data, run it, and capture the output.
