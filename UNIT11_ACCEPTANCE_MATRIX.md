# Unit 11 Capstone Acceptance Matrix

Current audit baseline: main at 08dda9a715a368bf549c8938db43311124d7286b (2026-11-12).

This matrix distinguishes lesson coverage, executable domain/storage code, automated runtime acceptance, integrated UI tests, and human assistive-technology verification. A passing domain test is not proof of a finished learner-facing application or screen-reader compatibility.

## Cross-track contract

The required record fields are id (unique positive integer), title, description, category, created_at, and updated_at (ISO 8601 timestamp). The optional done field is boolean. Stored JSON uses canonical snake_case field names.

The shared acceptance surface covers creation and required-field validation; unique IDs; list/search; restricted updates and timestamp preservation; deletion/completion; JSON round-trip; missing, malformed, invalid, and inaccessible files; and plain-text feedback.

## Current evidence

| Track(s) | Implementation and evidence | Current interpretation |
|---|---|---|
| Python | PYTHON/capstone/ includes NiceGUI app, record module, record tests, and three UI test suites. Record tests run in unit11-capstone-runtime.yml; all three page suites run in pull-request-validation.yml. Main PR validation run 43208932201 passed at the baseline commit. | Automated domain and simulated-page tests integrated. Real browser/assistive-technology evidence remains pending. |
| Java, Kotlin, Rust | Shared runtime workflow extracts, compiles, and runs the actual Lesson 11.2 storage and Lesson 11.4 acceptance examples. Run 43208932339 passed at the baseline commit. | Lesson-example domain/storage acceptance passed. Does not establish complete integrated applications. |
| C, C++ | Standalone reference cores and tests are exercised by the C/C++ runtime workflow. Run 43208932295 passed at the baseline commit. | Domain/storage acceptance passed. UI and broader project acceptance remain separate. |
| JavaScript, TypeScript, C#, Go, Swift, Julia, Lua | Standalone domain/storage cores and acceptance tests are exercised by the additional-capstones workflow. Run 43135992714 passed on the PR #57 head; the baseline-main rerun 43208932072 was in progress when this matrix was refreshed. | PR-head domain/storage acceptance passed; latest baseline-main rerun pending. These cores are not finished accessible UIs. |

## Python-specific coverage

- Record tests cover blank required fields, ID allocation, update timestamps, immutable identity/creation time, CRUD, completion, case-insensitive title/description/category search, JSON round-trip, invalid schema, duplicate IDs, malformed JSON, invalid UTF-8, missing files, and filesystem read errors.
- Page tests cover the initial page, add/search, blank-title feedback, completion, and deletion using NiceGUI's simulated user harness.
- The current workflow pins NiceGUI to 3.19.0 and Python to 3.12. The Python UI test job is part of repository PR validation.
- The page test harness does not drive a real browser or screen reader. Use ACCESSIBILITY_VERIFICATION.md for hands-on evidence.

## Remaining acceptance work

1. Complete manual keyboard-only, browser, screen-reader, and (where applicable) Braille verification. Record exact environment versions, outcomes, and defects in ACCESSIBILITY_VERIFICATION.md.
2. Extend capstone acceptance to CSV import/export and additional boundary cases wherever those are part of the track's project specification.
3. Keep domain/storage acceptance distinct from integrated command-line or graphical application acceptance for each track.
4. Refresh this matrix after the pending baseline-main additional-capstones workflow completes; do not infer a pass from a queued or in-progress run.

## Acceptance vocabulary

- Domain/storage accepted: declared deterministic tests pass for schema, CRUD, validation, timestamps, persistence, and documented error cases.
- Simulated-page tests integrated: UI test harness executes page interactions; this is not a real browser/AT test.
- Human accessibility verified: a completed evidence record identifies OS, browser, assistive technology, versions, and observed results.
- Pending: required evidence has not yet completed on the stated baseline.
