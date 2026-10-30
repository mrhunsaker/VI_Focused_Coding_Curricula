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
- Step 2 review completed and committed: `2be38ddc08fa67563840b45bddc2fb88c5de32dc`.

## 2026-10-30 — Step 3: GitHub Pages deployment automation

- Added `.github/workflows/mdbook.yml`.
- Workflow runs on pushes to `main` and manual dispatch, installs mdBook, builds the book, uploads the Pages artifact, and deploys it.
- Uses `actions/configure-pages@v5` with `enablement: true` because repository metadata reported that Pages was not enabled before this workflow was added.
- Uses least-privilege workflow permissions: `contents: read`, `pages: write`, and `id-token: write`.
- Uses project-site base URL `/VI_Focused_Coding_Curricula/` from `book.toml`.
- Workflow run and live URL verification are pending step 4.
- Step 3 workflow commit: `e1972d6355011a3c6ee7039d6fb3cfe21343a766`.

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
- Step 4 verification/checkpoint record committed in `5d1f81b61ff3172f6ed814dfaa59bde46c29b507`.
- Workflow run [41072475503](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41072475503) installed mdBook v0.5.4 successfully and completed `mdbook build` successfully.
- The same run then failed at `Configure GitHub Pages` with `Resource not accessible by integration`; the Actions token cannot create a Pages site for this repository. Artifact upload and deployment were skipped.
- Repository metadata still reports `has_pages=false`. The site is not yet published, and its URL has not been verified.
- **Required owner action:** open [Repository Settings → Pages](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/settings/pages), set **Build and deployment → Source** to **GitHub Actions**, and save. Then open Actions and rerun **Build and deploy mdBook**.
- Step 4 is blocked pending that repository-owner setting. The mdBook build itself is verified successful.


## 2026-10-30 — Step 4: Successful GitHub Pages deployment

- Reran failed jobs for workflow run [41072733650](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41072733650); GitHub accepted retry attempt 2.
- Attempt 2 completed with overall conclusion **success**. The deploy job (ID `124123160228`) succeeded.
- Confirmed successful steps: checkout, mdBook v0.5.4 installation, `mdbook build`, GitHub Pages configuration, Pages artifact upload, and deployment to GitHub Pages.
- The previous `Resource not accessible by integration` Pages-creation blocker is resolved; the retry configured Pages and deployed successfully.
- Intended site URL: https://mrhunsaker.github.io/VI_Focused_Coding_Curricula/.
- Live-site HTTP/rendered-page verification is not yet independently confirmed in this environment. Final smoke test remains: load the home page, traverse Python/JavaScript/Java navigation, inspect all 15 unit pages, and test internal links.
- Project status: deployment succeeded; final browser verification pending.

## 2026-10-30 — Step 5: Project README and community governance

- Added a comprehensive root `README.md` defining the project as an accessibility-first, evolving introductory computer science textbook for Python, JavaScript, and Java.
- Explicitly documented that the published textbook is built with **mdBook, not GitBook**; repository Markdown is the source of truth and GitHub Pages hosts the generated book.
- Documented the audience, accessibility principles, curriculum coverage, local mdBook build, repository structure, and contribution pathways through GitHub Discussions, Issues, and Pull Requests.
- Added repository-specific shields.io badges for Apache 2.0 licensing, top language, documentation, last commit, releases, contributors, welcome PRs, and GitHub Actions build status.
- Added `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `CODE_STYLE.md`, `SECURITY.md`, and the Apache 2.0 license notice in `LICENSE`.
- Updated `convert_to_mdbook.json` with step 5 scope and validation. The outstanding live-site browser smoke test from step 4 remains pending and is not represented as complete.
- Validation: reviewed badge targets and internal links; confirmed README is separate from mdBook navigation in `SUMMARY.md`; no curriculum source files or paths under `cs_curriculum_final/` were changed.
- Added the complete Apache License 2.0 text to `LICENSE` in a follow-up commit.
- Documentation commit: `2bffb36b30e499fee17d4feb3086ef4bd838e668`; full-license follow-up: `fd1c4f1510a5b1e4c8992acd9e96e2bd0ef9e477`.
- The repository's prior license file was CC0 1.0; it was changed to Apache 2.0 as explicitly requested. Confirm that the project maintainer has authority to apply the new license to all included material before relying on the relicense.
