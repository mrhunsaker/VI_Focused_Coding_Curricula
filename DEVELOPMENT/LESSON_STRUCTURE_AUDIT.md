# Lesson Structure Audit

## Purpose

This audit compares the curriculum lesson files with the instructional pattern established by the original Python course. It checks organization and teaching components, not whether every lesson teaches the same subject matter or has the same length.

## Python course reference pattern

The Python units establish a recognizable sequence:

1. Unit title and **Overview** with scope, compatibility notes where relevant, and learning objectives.
2. Individual numbered lessons with a clear lesson title.
3. **Reading References** where appropriate.
4. Concept explanations, definitions, and structured examples.
5. Examples with expected output or an explanation of the result.
6. **Common Mistakes/Common Errors** where relevant.
7. **Activities** or guided practice.
8. **Skills Checklist** describing observable learning outcomes.
9. Accessibility guidance where it materially affects the workflow.

The Python source is not mechanically identical in every lesson: some later Python lessons omit one or more subsections such as Reading References or Activities. The useful standard is therefore a consistent instructional sequence and predictable signposts, not identical word counts or forcing irrelevant sections into every topic.

## Audit result

<blockquote>
**Result: the repository does not yet have one consistent lesson structure across every language and prerequisite.** The original Python course is the strongest existing model, but several other tracks use shorter outlines or different heading patterns. This audit does not certify all lessons as structurally identical.
</blockquote>

### File groups reviewed

| Curriculum group | Files reviewed | Finding |
|---|---:|---|
| Python | 7 unit files | Reference model. Most lessons use explicit references, explanations, examples, activities, and checklists, but some later lessons omit individual components. |
| JavaScript | 4 unit files | Detailed lesson content exists, but several lessons omit Overview, Reading References, Activities, or consistent lesson-level checklists. |
| TypeScript | 4 unit files | Closely follows the JavaScript grouping and inherits its inconsistent lesson-level signposts; some units add TypeScript-specific notes. |
| Java | 4 unit files | Detailed content exists and often includes Overview, examples, and checklists, but Reading References and Activities are not consistently present. |
| Kotlin | 1 standalone lessons file | Uses numbered topic sections and a learning sequence rather than the Python unit/lesson structure. It is standalone and has substantial instructional content, but its headings are not normalized to the Python pattern. |
| C, C++, C#, Julia, Swift, Rust | 6 lessons files | Each contains a ten-lesson sequence, but the files are compact guided outlines. Lesson entries generally have a short topic description and exercise rather than the full Python-style set of instructional subsections. |
| Bash and PowerShell | 2 terminal lesson files | Organized as command-skill lessons and practice, not as language-course units with the complete Python lesson architecture. |
| IDE setup | 1 standalone lesson | Uses Overview, objectives, prerequisites, sequenced lessons, explanations, activities, and a skills checklist. It is aligned to the Python teaching approach, while retaining tool-specific sections. |

### Specific structural differences

- The newer C-family, Julia, Swift, and Rust lesson files are lesson maps, not full lesson manuscripts. They need expanded explanations, examples with expected output, common errors, activities, and skills checklists for each lesson.
- Kotlin is a substantial standalone course, but its numbered sections do not consistently use the same repeated lesson-level headings as Python.
- JavaScript and TypeScript have grouped unit files with uneven use of the Python signposts. Some lessons have examples and checklists but no explicit reading references or activities.
- Java is closer to the Python format than the shorter tracks, but its lesson-level sections are not fully uniform.
- Bash and PowerShell are prerequisite skill modules. Their command-oriented organization is appropriate to the subject, but they should use a documented adapted template rather than be described as identical to a programming-language lesson.
- The Python reference itself is not perfectly uniform; its later units sometimes omit Reading References or Activities. A course-wide standard should preserve useful variation while making the key teaching sequence predictable.

## Recommended standard for future and revised lessons

Each unit file should begin with:

- Unit title.
- Overview explaining scope and prerequisites.
- Compatibility/toolchain note where applicable.
- Unit learning objectives.
- A numbered lesson sequence.

Each substantive lesson should normally include:

1. **Reading References** — official documentation and/or course text, when a useful source exists.
2. **Learning Objectives** — observable outcomes for that lesson.
3. **Concept Explanation** — definitions, syntax, semantics, and a worked explanation.
4. **Examples** — complete, runnable examples with expected text output or an explicit description of behavior.
5. **Common Mistakes** — likely errors, their symptoms, and a correction or diagnostic approach.
6. **Activities** — independent practice that changes or extends the example; include expected behavior, not a copied solution.
7. **Accessibility Practice** — keyboard/screen-reader/braille workflow when relevant to the task.
8. **Skills Checklist** — first-person statements that a learner can verify.

A section may be omitted when it genuinely does not apply, but the reason should be clear. Project and capstone lessons may use requirements, milestones, test criteria, and deliverables in place of a conventional worked example.

## Validation status

- Heading-level review completed for the Python, JavaScript, TypeScript, Java, Kotlin, C, C++, C#, Julia, Swift, Rust, Bash, and PowerShell lesson files.
- The new standalone IDE lesson follows the recommended sequence and includes learning objectives, explanations, platform-specific steps, activities, and a checklist.
- This is a structural audit, not a complete content rewrite of all lesson files.
- A full normalization pass remains necessary before the repository can accurately claim that every lesson follows one common template.
- No claim is made here that every code example, external link, screen-reader workflow, or lesson objective has been independently tested.

---

The goal of standardization is predictable navigation and teaching structure, not identical prose. Keep each language's compiler, runtime, syntax, and accessibility requirements specific to that language.


## Follow-up: expanded language tracks and machine-readable alignment plan

The first expansion pass is now committed on the working branch.

- C, C++, C#, Julia, Swift, Rust, Go, and Lua each have a Unit 0–11 lesson manuscript with 52 numbered lesson headings, overview pages, and topic indexes.
- Go and Lua are now full courses rather than proposed tracks.
- HTML/CSS, R, and SQL are separate specialist modules with their own domain-appropriate outcomes.
- The root `lesson_standardization.json` contains the explicit Python unit map, mapped lesson names, common example datasets, functional-equivalence rules, accessibility and quality gates, and a reusable course-refinement prompt.

**Important qualification:** the eight expanded lesson manuscripts are a substantive first-pass expansion, not yet a verified line-by-line translation of every Python lesson. Some lessons currently reuse a representative worked example within a unit. The JSON prompt is intended to guide a later refinement pass that assigns each Python example and activity to its exact language counterpart, verifies each expected result, and removes any repeated or insufficiently specific examples. Kotlin, Java, JavaScript, and TypeScript also require a full comparison against the JSON map before they can be declared completely aligned.

The current course set should therefore be described as **expanded and mapped for standardization**, not fully validated as functionally identical. Compiler/runtime execution, complete link validation, mdBook rendering, and screen-reader testing remain outstanding.


## 2026-11-01 follow-up: C lesson-quality refinement

The C curriculum received a lesson-level quality pass on the working branch.

- All four Unit 0 setup lessons now use a complete instructional sequence: references, objectives, concept explanation, worked instructions, common mistakes, activities, accessibility practice, and skills checklist.
- All 53 numbered lessons in Units 1–11 now have lesson-specific common mistakes, four independent activities tied to the lesson's C concepts and shared datasets, and an observable mastery checklist.
- Activities use the canonical calculator, grade thresholds, score collection, inventory records, coordinate example, text sample, CSV schema, to-do tasks, and capstone record fields where appropriate.
- C-specific risks are stated explicitly: array bounds, null termination, conversion validation, integer division, pointer ownership, struct semantics, resource cleanup, file errors, JSON-library limitations, and fixed-capacity project data.
- The standardization JSON now records this C quality pass and its remaining verification requirements.

**Verification boundary:** structural checks were run against the committed Markdown and JSON. Every C snippet has not yet been compiled or executed with GCC/Clang. The available GitHub connector does not provide a local compiler, and a repository clone attempt failed because the execution environment could not resolve github.com. Screen-reader/braille testing and a fresh mdBook build also remain outstanding. Do not describe the C course as runtime-verified or accessibility-certified.


## 2026-11-01 follow-up: C compiler verification

A repeatable compiler check is now committed:

- `scripts/check_c_examples.py` extracts every fenced C example from `C/lessons.md`.
- `.github/workflows/c-examples.yml` runs the check with both GCC and Clang in C17 mode.
- GitHub Actions run [41316160464](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41316160464) completed successfully.
- GCC 13.3.0 and Clang 18.1.3 both passed all 49 C examples with `-Wall -Wextra -Wpedantic -Werror`: 46 complete programs compiled and linked; 3 declaration/function fragments passed syntax-only checks.

This is compiler and linker verification. The examples have not all been executed with representative input or file fixtures. A fresh mdBook build, complete link crawl, and hands-on screen-reader/braille testing remain outstanding.


## 2026-11-01 follow-up: C++ lesson-quality and compiler-verification pass

- Expanded all four Unit 0 lessons into structured compiler, workspace, editor/accessibility, and dependency/build instruction.
- Added the missing C++ equivalent of Python Lesson 2.5 for standard mathematical functions and the shared circle/distance problems.
- Replaced repeated worked examples with distinct lesson-specific C++20 examples across the 53 numbered Unit 1–11 lessons.
- Rewrote all 53 numbered lessons with three C++-specific common mistakes, four targeted activities, and five observable skills-checklist criteria.
- Added `scripts/check_cpp_examples.py` and `.github/workflows/cpp-examples.yml`.
- GitHub Actions run [41318426947](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41318426947) passed with GCC 13.3.0 and Clang 18.1.3. All 54 fenced C++ examples compiled and linked as C++20 with strict warning flags.
- Remaining: runtime execution with representative inputs/files, fresh mdBook build, complete local-link crawl, and hands-on screen-reader/braille testing. Compiler success is not runtime or accessibility validation.


## 2026-11-01 follow-up: C# lesson-quality pass

- Expanded all four Unit 0 lessons into complete .NET 10 SDK, project workspace, editor/accessibility, NuGet, restore, build, test, and run workflows.
- Added the missing C# counterpart of Python Unit 2 Lesson 2.5 using `System.Math`, circle area/circumference, and distance from the origin.
- Replaced repeated examples with 53 distinct C# examples using the canonical shared profile, calculator, grade thresholds, scores, inventory, coordinates, text sample, CSV columns, task fields, and capstone record fields.
- Rewrote all 53 numbered lessons with three C#-specific common mistakes, four practice activities, and five observable mastery criteria per lesson.
- Standardized the examples on .NET 10 / C# 14 and added `scripts/check_csharp_examples.py` plus `.github/workflows/csharp-examples.yml`.
- Structural validation confirms four fully structured setup lessons, 53 numbered lessons, 53 distinct C# examples, and the required three/four/five mistake/activity/checklist counts.
- GitHub Actions run [41320247156](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41320247156) passed with .NET SDK 10.0.403; all 53 C# examples compiled, linked, and exited successfully as independent .NET 10 / C# 14 console programs with nullable analysis and warnings-as-errors. This is a smoke-execution check rather than full expected-output or application testing. A fresh mdBook build/link crawl and hands-on screen-reader/braille testing remain outstanding.


## 2026-11-01 — Julia lesson-quality pass

- Expanded all four Julia Unit 0 lessons with toolchain installation, REPL and script execution, workspace and working-directory semantics, editor/accessibility workflow, and project-local package management.
- Added the missing Python Unit 2 Lesson 2.5 counterpart for Julia's mathematical library, including circle calculations and distance from the origin.
- Replaced repeated within-unit worked examples with 53 distinct Julia lesson examples aligned to canonical shared datasets and project contexts.
- Rewrote all 53 numbered lessons with Julia-specific concept explanations, three common mistakes, four targeted activities, accessibility practice, and five observable checklist criteria.
- Added a Julia 1.12 example runner and GitHub Actions workflow. CI execution is pending; no compiler/runtime success is claimed until the workflow completes.
- Outstanding: expected-output and broader behavior tests, mdBook build and local-link crawl, and hands-on screen-reader/braille testing.

- GitHub Actions run [41322088371](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41322088371) passed with Julia 1.12.7; all 57 fenced Julia examples executed successfully in isolated temporary directories. This is a smoke-execution check, not expected-output assertion or full application testing.

- A final setup pass brought each of the four Unit 0 Julia lessons to the complete nine-section structure: references, objectives, concept explanation, worked example, expected behavior, mistakes, activities, accessibility practice, and checklist.


## 2026-11-01 — Swift lesson-quality pass

- Expanded all four Swift Unit 0 lessons with installation, compiler/interpreter verification, workspace and path semantics, accessible editor and SourceKit-LSP workflow, and Swift Package Manager.
- Added the missing Python Unit 2 Lesson 2.5 counterpart for Foundation math functions, circle area/circumference, and distance from the origin.
- Replaced repeated worked examples with 53 distinct Swift examples aligned to canonical shared datasets and project contexts.
- Rewrote all 53 numbered lessons with Swift-specific concept explanations, three common mistakes, four targeted activities, accessibility practice, and five observable checklist criteria.
- Added a Swift 6 example runner and GitHub Actions workflow. CI execution is pending; no successful compile/runtime result is claimed until the workflow completes.
- Outstanding: expected-output and broader behavior tests, mdBook build and local-link crawl, and hands-on screen-reader/braille testing.

- GitHub Actions run [41324186133](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41324186133) passed on Swift 6.0; all 57 fenced Swift examples executed successfully as independent scripts. This is a smoke-execution check, not exact-output assertion or full package/capstone testing.

- A second finalized-checker run [41324246202](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41324246202) also passed using Swift 6.0.3; all 57 examples executed successfully.


## 2026-11-01 follow-up: Rust lesson-quality and execution verification

- Expanded all four Unit 0 lessons with rustup/stable toolchain installation, Cargo project structure, rust-analyzer and assistive-technology workflow, project-local dependencies, and build/test commands.
- Added the missing Unit 2 Lesson 2.5 counterpart for mathematical functions, circle area/circumference, and distance using PI, powi, and hypot.
- Replaced repeated generic examples with 53 lesson-specific standard-library Rust programs aligned to shared course contexts.
- Rewrote all 53 numbered lessons with Rust-specific concept explanations, three topic-relevant common mistakes, four targeted activities, accessibility practice, and five observable checklist criteria.
- Standardized on stable Rust / Rust 2024 edition and documented production JSON and randomness boundaries.
- Added scripts/check_rust_examples.py and .github/workflows/rust-examples.yml. GitHub Actions run [41324948920](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41324948920) passed on Rust 1.99.1; all 53 examples compiled with warnings denied and smoke-executed successfully.
- Remaining: expected-output assertions and broader file/error/capstone tests, fresh mdBook build and local-link crawl, and hands-on screen-reader/braille testing.


## 2026-11-01 follow-up: Go lesson-quality and execution verification

- Expanded Unit 0 with four complete setup lessons covering installation, modules and first run, editor and accessibility workflow, and dependency/terminal practice.
- Added the missing Unit 2 Lesson 2.5 counterpart for mathematical functions, circle geometry, and distance from origin.
- Replaced generic/repeated snippets with 53 distinct standalone Go examples using canonical student, calculator, grades, scores, inventory, text, file, CSV, to-do, and capstone contexts.
- Rewrote all 53 numbered lessons with Go-specific explanations, three relevant mistakes, four targeted activities, accessibility practice, and five measurable checklist criteria.
- Added scripts/check_go_examples.py and .github/workflows/go-examples.yml. GitHub Actions run [41326670760](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41326670760) passed on Go 1.27.3; all 53 fenced examples were formatted with gofmt, built independently, and smoke-executed successfully.
- Remaining: expected-output assertions, broader file/input tests, capstone persistence tests, mdBook/link validation, and hands-on screen-reader/braille testing.


## Lua lesson pass — 2026-11-01

- Expanded the Lua sequence to 53 numbered lessons, adding Unit 2 Lesson 2.5 for math-library operations, circle geometry, and distance from the origin.
- Replaced the repeated fenced Lua snippets with 53 distinct standard-library examples and added a Lua 5.4 syntax/smoke-execution checker and GitHub Actions workflow.
- Added Lua README and validation-scope documentation.
- This pass verifies distinct examples and structural counts; lesson-level concept explanations, mistakes, and activities still require deeper topic-specific editorial refinement. GitHub Actions run [41336406502](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41336406502) passed on Lua 5.4.6, parsing and smoke-executing all 53 examples. Expected-output assertions, capstone persistence, mdBook/link validation, and hands-on accessibility tests remain pending.

- Follow-up editorial refinement added topic-aligned Lua concept explanations, three mistake prompts, and four activities to each of the 53 numbered lessons. Each lesson retains accessibility practice and a five-item checklist. A final CI run after this prose-only refinement is pending.


## Java standardization pass — 2026-11-01

- Added `JAVA/lessons.md` as the consolidated lesson-by-lesson Java sequence: four Unit 0 setup lessons and 53 numbered lessons across Units 1–11.
- Each of the 57 lessons has references, objectives, a concept explanation, a complete worked example with expected behavior, three Java-specific mistakes, four activities, accessibility practice, and a five-item skills checklist.
- Retained the original grouped Java unit documents as supplementary reference material and linked the consolidated course from the Java landing page, index, and mdBook navigation.
- Added a JDK 25 checker and GitHub Actions workflow. Run [41337711452](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41337711452) passed on Temurin 25.0.5, compiling and smoke-executing all 57 examples independently. The final prose-refinement workflow run [41337829888](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41337829888) passed on Temurin JDK 25.0.5; all 57 examples compiled and smoke-executed independently.
- Remaining work: exact output assertions, invalid-input and file fixtures, capstone persistence/JUnit integration, fresh mdBook/link crawl, and hands-on screen-reader/braille testing.
