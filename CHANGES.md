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

## 2026-10-30 — Step 2: Curriculum navigation and compatibility review

- Reviewed all 15 existing unit Markdown files: Python 7, JavaScript 4, and Java 4.
- Confirmed all 15 unit pages are included in `SUMMARY.md`; all 19 navigation targets resolve to tracked Markdown files.
- Checked fenced code blocks: 262 code blocks across the 15 unit files, with balanced opening and closing fence markers in every file.
- Reviewed Markdown links. Existing unit-page links are external references; no broken relative links were found. The Python landing page's relative links resolve.
- Retained grouped multi-unit files in their original form. No lesson-content edits or wording changes were necessary.
- Confirmed no changed path is under `cs_curriculum_final/`.
- mdBook executable build is deferred to CI/final verification because mdBook is not installed in the available execution environment.
- Validation correction: the repository contains 15 unit files (Python 7, JavaScript 4, Java 4), not 17. The plan's validation counts have been corrected.
- Step 2 review completed; checkpoint commit SHA will be recorded after the commit succeeds.

## 2026-10-30 — Step 3: GitHub Pages deployment automation

- Added `.github/workflows/mdbook.yml`.
- Workflow runs on pushes to `main` and manual dispatch, installs mdBook, builds the book, uploads the Pages artifact, and deploys it.
- Uses `actions/configure-pages@v5` with `enablement: true` because repository metadata reported that Pages was not enabled before this workflow was added.
- Uses least-privilege workflow permissions: `contents: read`, `pages: write`, and `id-token: write`.
- Uses project-site base URL `/VI_Focused_Coding_Curricula/` from `book.toml`.
- Workflow run and live URL verification are pending step 4.
- Step 3 workflow commit SHA will be recorded after the commit succeeds.

## 2026-10-30 — Step 4: Build and deployment verification

- Inspected workflow run [41072285741](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41072285741).
- Checkout succeeded. The `Configure GitHub Pages` step failed before mdBook installation/build.
- Runner log evidence: `Create Pages site failed. Error: Resource not accessible by integration`. The repository currently reports `has_pages=false`; the workflow's `GITHUB_TOKEN` cannot create the Pages site.
- Required owner action: open repository **Settings → Pages**, set **Build and deployment → Source** to **GitHub Actions**, and save. Then rerun the workflow.
- Reordered the workflow so mdBook installation and `mdbook build` execute before Pages configuration. This allows build validation to complete even while the Pages setting is awaiting owner action.
- Step 4 remains in progress until a successful build and Pages deployment are verified.

## 2026-10-30 — Step 4: Build verification and Pages deployment blocker

- Workflow run [41072285741](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41072285741) initially failed at Pages configuration before the mdBook build.
- Reordered the workflow in commit `80af75ec1c4aa33c6b55b8518de80e4170ec162b` so installation and build run before Pages configuration.
- Workflow run [41072475503](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41072475503) installed mdBook v0.5.4 successfully and completed `mdbook build` successfully.
- The same run then failed at `Configure GitHub Pages` with `Resource not accessible by integration`; the Actions token cannot create a Pages site for this repository. Artifact upload and deployment were skipped.
- Repository metadata still reports `has_pages=false`. The site is not yet published, and its URL has not been verified.
- **Required owner action:** open [Repository Settings → Pages](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/settings/pages), set **Build and deployment → Source** to **GitHub Actions**, and save. Then open Actions and rerun **Build and deploy mdBook**.
- Step 4 is blocked pending that repository-owner setting. The mdBook build itself is verified successful.
