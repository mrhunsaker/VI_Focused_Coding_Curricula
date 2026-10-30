# Change Log

All implementation changes are recorded here. Each numbered step is committed separately before the next step begins.

## 2026-10-30 — Step 0: Conversion plan
- Added `convert_to_mdbook.json` before implementation edits.
- Recorded source inventory, reference-only boundary, mdBook design, deployment plan, validation, and per-step checkpoint protocol.
- Commit: `6240f1fdd052f4f3b9f41d80e9f83df686a71f4b`.
- Validation: fetched the committed file and parsed it as JSON.
- Confirmed no paths under `cs_curriculum_final/` were changed.

## 2026-10-30 — Step 1: mdBook foundation
- Added root mdBook configuration and navigation.
- Added a Python landing page to complement existing Java and JavaScript landing pages.
- Added this change log and ignored generated mdBook output.
- Validation: parsed convert_to_mdbook.json; confirmed all 19 Markdown targets in SUMMARY.md resolve to tracked files; reviewed the commit diff and confirmed no changes under cs_curriculum_final/. mdBook executable build is deferred to CI/final verification.
- Implementation commit: `7bfa28d7043bd94ac1fc1101c7832b2a90f27107`.
