# Unit 11 Capstone Acceptance Matrix

**Audit baseline:** `main` at `65a6cbc17f2b408d3f8821da6fef33c97e1524aa` (2026-11-12).

This matrix separates three different claims:

1. **Lesson coverage** — the Unit 11 curriculum explains the shared project and its requirements.
2. **Executable reference core** — the repository contains a runnable implementation of the data and persistence behavior.
3. **Runtime acceptance** — an automated workflow executes the implementation and verifies the required behavior.

A lesson with code fragments is not automatically a complete application. A passing record-core test is not proof of a complete learner-facing interface or verified assistive-technology compatibility.

## Cross-track contract

The required record fields are `id` (unique positive integer), `title`, `description`, `category`, `created_at`, and `updated_at` (ISO 8601 text). An optional `done` field is permitted. Stored JSON uses the canonical snake_case field names.

The shared runtime acceptance surface should cover:

- Create records; reject blank required fields; allocate IDs without reusing a deleted maximum ID.
- Read/list and search records; search behavior should be case-insensitive and cover the documented fields.
- Update records; preserve `created_at`, refresh `updated_at`, and reject invalid updates.
- Delete only the requested record; complete records where the track supports the optional `done` extension.
- Save and reload JSON without losing fields; handle missing files and malformed or invalid records predictably.
- Produce deterministic, plain-text feedback suitable for keyboard and screen-reader use.

## Track-by-track status

| Track | Lesson source | Reference implementation in repository | Runtime evidence at audit baseline | Next acceptance work |
|---|---|---|---|---|
| Python | `PYTHON/unit11-capstone-project-accessible-personal-data-manager.md` | Yes — NiceGUI application and record module under `PYTHON/capstone/` | Dedicated record and UI test files exist; the common Unit 11 runtime workflow does not yet include this suite. | Run and integrate the Python record/UI tests into the common acceptance workflow; retain manual assistive-technology verification. |
| Java | `JAVA/unit11-capstone-accessible-personal-data-manager.md` | Complete runnable Lesson 11.2/11.4 examples in Markdown | **Pass** — `unit11-capstone-runtime.yml` compiles/exercises the actual lesson examples for storage/error and CRUD acceptance. | Keep the extracted lesson examples under CI; consider a separately assembled end-to-end app only if needed for parity. |
| JavaScript | `JAVASCRIPT/unit11-capstone-project-accessible-personal-data-manager.md` | Yes — `JAVASCRIPT/capstone/` | **Pass** — 7 Node test cases passed on the audit-baseline run. | Link each lesson's worked examples to the tested core and add a command-loop integration test if the interface is assembled. |
| TypeScript | `TYPESCRIPT/unit11-capstone-accessible-personal-data-manager.md` | Yes — `TYPESCRIPT/capstone/` | **Pass** — strict TypeScript build and 7 Node test cases passed on the audit-baseline run. | Link lesson examples to the tested core; preserve runtime validation of parsed JSON (static types do not validate input files). |
| Kotlin | `KOTLIN/unit11-capstone-accessible-personal-data-manager.md` | Complete runnable Lesson 11.2/11.4 examples in Markdown | **Pass** — actual lesson examples pass storage/error and CRUD acceptance in the common workflow. | Keep lesson extraction and runtime assertions under CI. |
| C | `C/unit11-capstone-personal-data-manager.md` | No standalone capstone project directory/test runner; lesson specifies a terminal-first implementation and an external JSON library | Not runtime-accepted. | Build a runnable core, pin/document the JSON dependency, and test bounded input, ownership, CRUD, persistence, and malformed data. |
| C++ | `CPP/unit11-capstone.md` | Worked examples and implementation activities; no standalone capstone project directory/test runner | Not runtime-accepted. | Assemble a C++20 core and test ownership/lifetime, validation, CRUD, JSON round-trip, and file errors. |
| C# | `CSHARP/unit11-capstone.md` | Yes — `CSHARP/capstone/` | **Blocked by a test-fixture defect** — the latest additional-capstones run passed JavaScript and TypeScript, then failed the timestamp-update assertion in C#; Go was skipped. The fixture's update clock restarted at second 01 even though `Fresh()` had already assigned second 01 to the record. | Make the injected test clock advance beyond the fixture timestamps, then rerun the full additional-capstones workflow. |
| Julia | `JULIA/unit11-capstone.md` | Lesson fragments and package guidance (including JSON3.jl); no standalone capstone project directory/test runner | Not runtime-accepted. | Assemble a project with a committed `Project.toml`, deterministic core tests, JSON round-trip, and file-error coverage. |
| Swift | `SWIFT/unit11-capstone.md` | Lesson examples include the shared JSON field encoding; no standalone capstone project directory/test runner | Not runtime-accepted. | Assemble a Swift package and test Codable mapping, CRUD, validation, timestamps, and persistence failures. |
| Rust | `RUST/unit11-capstone.md` | Complete runnable Lesson 11.2/11.4 examples in Markdown | **Pass** — actual lesson examples pass storage/error and CRUD acceptance in the common workflow. | Keep lesson extraction and runtime assertions under CI. |
| Go | `GO/unit11-capstone-accessible-personal-data-manager.md` | Yes — `GO/capstone/` package and tests | **Not yet verified on baseline** — its workflow step was skipped because the preceding C# step failed. | Run `go test -v ./...` independently or after the C# fix; then record the result in CI. |
| Lua | `LUA/unit11-capstone-accessible-personal-data-manager.md` | Worked examples and dependency-selection guidance; no standalone capstone project directory/test runner | Not runtime-accepted. | Select and pin JSON dependency; assemble a terminal-first core and test CRUD, validation, persistence, and malformed/quoted input. |

## Evidence and interpretation

- **Java/Kotlin/Rust:** the merged Unit 11 runtime workflow extracts the actual Lesson 11.2 and Lesson 11.4 code blocks from the curriculum Markdown and checks JSON round-trip, missing/malformed files, and six CRUD/validation cases. This is stronger than checking for the presence of code fences, but it does not prove a complete integrated command-line application.
- **JavaScript/TypeScript/C#/Go:** the additional-capstones workflow tests repository reference cores. At the audit baseline, JavaScript and TypeScript passed all seven tests each. C# failed its timestamp assertion because its deterministic test clock was reset to a timestamp already present in the fixture data; Go did not run in that failed job. The C# failure is a test-fixture sequencing issue, not evidence that production timestamps are incorrect.
- **Python:** the repository contains an existing capstone application and record/UI test files. Those tests need to be run and represented in the shared acceptance workflow before the matrix can call Python runtime-accepted on the same CI basis.
- **C/C++/Julia/Swift/Lua:** the curriculum contains project requirements and worked examples, but there is no corresponding standalone `capstone/` implementation/test harness in the repository tree at this audit baseline.

## Recommended implementation order

1. Stabilize the C# fixture clock and rerun the JavaScript/TypeScript/C#/Go workflow; confirm Go is actually executed.
2. Run the Python record and UI tests, then add them to CI with the required dependencies.
3. Create standalone reference cores and deterministic acceptance tests for Swift and C++ next, then Julia, Lua, and C. Choose dependencies and toolchain versions explicitly.
4. Add integration-level command-loop tests for each terminal application, and keep them distinct from record-core unit tests.
5. Maintain a separate manual accessibility checklist for keyboard-only operation, screen-reader announcements, focus order, and error/status feedback. Automated core tests cannot establish assistive-technology compatibility.

## Acceptance status vocabulary

- **Runtime accepted:** the declared automated acceptance suite passes on the current main branch.
- **Core present; CI blocked:** a runnable core exists, but the current CI acceptance job fails.
- **Core present; CI unverified:** a runnable core exists, but the relevant test step did not execute or no passing run is available.
- **Implementation present; CI integration pending:** an application/test suite exists but is not yet included in the common acceptance workflow.
- **Lesson-only:** requirements and examples exist, but no standalone runnable capstone core/test harness is present.
