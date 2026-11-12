# Standardization Tracker Semantic Review — refreshed 2026-11-12

## Scope and method

This document preserves the semantic decisions from the 2026-11-11 review and refreshes its claims against main at commit 08dda9a715a368bf549c8938db43311124d7286b. The prior 41-block inventory was a historical snapshot, not a current count.

The refresh used:
- The current-main PR validation workflow, including repository-wide merge-marker scanning, JSON validation, Python record/UI tests, and mdBook build.
- Direct re-fetch of the 20 files previously listed as affected.
- Current Unit 11 acceptance workflow results and the current Unit 11 acceptance matrix.

## Historical semantic decisions retained

The 16 tracker conflict decisions from the original review remain useful as historical rationale: several selections were corrected or downgraded based on live lesson content, rather than choosing the longer side. The original corrections to Python Unit 0 lesson count/source paths, Unit P prerequisites, Unit 10 adventure graph, and Unit 11 schema remain part of the review history. They are not a claim that every lesson is now semantically complete.

## Refreshed merge-marker status

The 20 paths in the earlier inventory were re-fetched from current main and scanned for standard line-leading merge-marker forms. Zero marker lines were found in those 20 files.

The current-main repository validation workflow also completed successfully at the refreshed baseline:
- Pull request curriculum validation, run 43208932201 — success.
- Commit: 08dda9a715a368bf549c8938db43311124d7286b.
- The workflow's repository scan checks supported text extensions and excludes generated/build/vendor directories. It is a marker scan, not a semantic review. Marker-like strings used as instructional examples or inside the scanner's own regular expression are not unresolved conflict blocks.

| Previously flagged area | Files rechecked | Current marker lines |
|---|---:|---:|
| Python | 7 | 0 |
| TypeScript | 4 | 0 |
| Lua | 5 | 0 |
| Java | 2 | 0 |
| Rust | 1 | 0 |
| Kotlin | 1 | 0 |
| Total | 20 | 0 |

Interpretation: the earlier 41-block inventory is superseded as a current-branch marker count. Do not carry forward the 41 figure as an open defect count. Semantic correctness, stale examples, and cross-track contract parity still require content review.

## Current validation and implementation observations

- The current-main PR validation run passed JSON validation, merge-marker scanning, Python record tests, Python NiceGUI simulated-page tests, repository checks, and mdBook build.
- Python page test suites are now part of .github/workflows/pull-request-validation.yml; the previous statement that Python UI tests were not in CI is stale.
- Unit 11 domain/storage acceptance has been added across all 13 general-purpose tracks. Python, Java/Kotlin/Rust, and C/C++ baseline-main workflows passed on commit 08dda9a...; the additional-capstones baseline-main rerun also completed successfully (run 43208932072). The earlier PR #57 head run for JavaScript, TypeScript, C#, Go, Swift, Julia, and Lua passed.
- Domain/storage acceptance does not establish complete learner-facing UIs, CSV import/export parity, or assistive-technology usability.
- Python's NiceGUI page tests simulate interactions; they do not establish real browser focus behavior or screen-reader/Braille output.

## Accessibility evidence status

Manual keyboard-only, screen-reader, and Braille verification remains not yet verified. The protocol and evidence template are maintained in ACCESSIBILITY_VERIFICATION.md. Do not convert automated test success into a human accessibility pass.

## Remaining work

1. Complete and commit hands-on accessibility evidence for named OS/browser/screen-reader combinations; include Braille where available.
2. Keep the additional-capstones main-branch run (43208932072) recorded as passed; refresh after subsequent baseline changes.
3. Continue semantic review of lesson content and contract parity even though the previously flagged merge markers are gone.
4. Extend project acceptance to CSV workflows and integrated CLI/GUI behavior where required by each track.
5. Keep audit statements tied to commit SHAs and completed workflow runs; mark queued/in-progress runs as pending.
