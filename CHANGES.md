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

## 2026-10-30 — Step 6: Expanded curriculum overviews and teacher guides

- Rewrote `OVERALL_README.md` as a comprehensive book entry point covering purpose, audience, learning outcomes, language selection, course pathways, study routine, accessibility approach, assessment, AI use, contribution routes, and references.
- Expanded `PYTHON/PYTHON_README.md`, `JAVASCRIPT/JAVASCRIPT_README.md`, and `JAVA/JAVA_README.md` with course outcomes, prerequisites, sequenced topic maps, evidence of progress, environment guidance, accessibility practices, study methods, assessment, AI guidance, and further learning.
- Reviewed all three active `teachers-guide.md` files. Added guidance for using the guides, expanded the Python AI section, and added AI teaching sections to JavaScript and Java. All three now address both instructor preparation and student use, language-specific risks, accessibility, privacy, security, equity, verification, and assessment boundaries.
- Added a comprehensive instructional-planning section to each teacher guide covering course alignment, learner readiness, lesson architecture, accessible navigation, language-specific emphasis, misconceptions, differentiation, assessment and feedback, debugging, pair programming, projects, collaboration, instructor preparation, and continuous improvement.
- Verified local links in the four overview/landing pages; teacher-guide links resolve through the existing book navigation. Checked that teacher-guide fenced-code markers are balanced. The only apparent relative-link match in the Python teacher guide occurs inside a fenced example and is not a real Markdown link.
- No files under `cs_curriculum_final/` were modified.
- Implementation commits: `eef517751d763025ae183e2d7c0561e2b1a44dd2`, `53a94aa9e415f5bec788ab8648f21461a9088a0d`, and `615fcf5b5472a22663366d4b720e96b89a98817c`.
- mdBook CI and live-site smoke testing are pending; do not mark publication verification complete until the current workflow succeeds and the rendered site is checked.

## 2026-10-30 — Step 7: mdBook build and Pages deployment after curriculum expansion

- GitHub Actions run [41080845202](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41080845202) completed successfully for commit `ec51d5b99f998493979ae3c5a9f03b38efd16376`.
- mdBook installation and `mdbook build` succeeded; GitHub Pages configuration, artifact upload, and deployment also succeeded.
- Published target: [Accessible Introduction to Computer Science](https://mrhunsaker.github.io/VI_Focused_Coding_Curricula/).
- The available web viewer could not independently retrieve the published URL. This is a limitation of that viewer, not evidence that the website is unavailable. A normal-browser smoke test of the overview, three language pages, 15 unit pages, three teacher guides, and representative internal links remains outstanding.
- Updated `convert_to_mdbook.json` to mark the content expansion and build/deployment validation complete while keeping live-site browser verification explicitly pending.


## 2026-10-30 — Step 8: Runtime modernization and TypeScript/Kotlin expansion

- **Python:** Set the minimum supported version to Python 3.12+. Recorded Python 3.15.2 as the current stable release on the review date while keeping every course example compatible with Python 3.12. Updated setup and package commands, including virtual-environment and `python -m pip` usage. Added modern PEP 8, built-in generic type-hint, pathlib, context-manager, exception-handling, and type-annotation guidance across the learner and teacher materials.
- **JavaScript:** Updated the curriculum and instructor guide to Node.js 26.13.0 LTS. Added the current LTS baseline across lesson pages, made CommonJS/ES module choices explicit, modernized Node built-in imports to `node:` specifiers, documented ESLint flat configuration, and reinforced `const`/`let`, strict equality, explicit conversion, and asynchronous error handling.
- **Java:** Updated the learner and teacher materials to JDK 25 LTS and standard Java SE 25 without preview features. Added current naming, import, generics, equality, and resource-management guidance. Corrected file API usage and replaced wildcard imports with explicit imports in affected examples.
- **TypeScript:** Added a fourth complete curriculum in `TYPESCRIPT/`: a comprehensive introduction, four unit documents mirroring the JavaScript curriculum sequence, and a teacher guide. The introduction explains TypeScript's growing adoption and compile-time type safety while clearly distinguishing static checks from JavaScript runtime behavior. Setup targets Node.js 26 LTS and TypeScript 7.0.2, uses strict compiler options, and examples include type annotations, type guards, and runtime validation of external data.
- **Kotlin:** Added `JAVA/kotlin.md` as an optional post-capstone supplement for Java learners. It covers the JVM relationship, syntax differences, null safety, functions, classes, collections, Java interoperability, environment setup, testing, and an optional learning sequence. It is not a fifth core curriculum.
- Updated `SUMMARY.md`, `OVERALL_README.md`, root `README.md`, `CODE_STYLE.md`, and `JAVA/JAVA_README.md` for the four core curricula and optional Kotlin supplement.
- Version references checked against current official release information on 2026-10-30: Python 3.15.2 stable / Python 3.12 minimum; Node.js 26.13.0 LTS; TypeScript 7.0.2 stable; JDK 25 LTS; Kotlin 2.4.21 stable.
- Validation: 32 active Markdown documents were audited; all fenced-code markers were balanced and local links reviewed. GitHub compare from the previous checkpoint to this implementation head shows no changed paths under `cs_curriculum_final/`.
- GitHub Actions run [41084997810](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41084997810) for implementation head `5f39ff02411ca20e889c70b3aa74b2478c35b673` completed successfully. mdBook installation, build, Pages configuration, artifact upload, and deployment all succeeded.
- The web viewer could not retrieve the published home page or TypeScript page. This is not evidence that the site is down; a normal-browser rendered-page smoke test remains pending.
- Implementation commits (chronological work grouped into the following checkpoints): `483713539b52fc6ce548a7744f2640d06ea78da6`, `b9713e33e49e7acd073494040857aa69b2afe044`, `008fce857632adcdedc7e0b8745b2e1856c4ffbd`, `34f692eef10b5d9704a06bd288bd3476975ea5ad`, `49f54096e8d0127ea6d8fc40c807e55d2d392545`, `0a6be9f3aff2195e463a0ea7ed41b78a9ab690fb`, `40e94b515e036731223f7623e0d05684ede56e09`, `f4b4825a422e9a13575977e73590a9801f502b00`, `202989dc5eaed8562215741bde6ccb692acf8483`, `f7245a7820672761ad4c76709974685faeb30c64`, `5212592e523fb9f72f57639dbbda0ade72f88fd7`, `cc698f86774e807c94880045f10df9ee307b667d`, `f6ea6613da152ce999ddf77ba0484aaa07f36fd5`, `3ca4e6745fa9ee9ec83147a2b81944952eb585db`, `27749ed6f249b6227678eaced8871bf04eec0974`, `14077ea7ff465a84d791a329d20ca734e33921ef`, `fc83a263cdaf482ef6095af488fcf0a5bff6d818`, `2026a6b2206985441807dc8a2826d6cf1cae83c4`, `7e0b55872609e4f4105cf06af4ab5f352d4f17b5`, `b764a8772ed5b8eeb4faef9177e023f2f233d7fc`, `98106a48e2a9ae11055b14a8dcd52dc0ec1b83d7`, `2ce9e0452c1a6fb56643aa14c26b9559091ea19d`, `10c2988c3d729b72f56ab184ced06cd6e6aad220`, `8cdd4fe0a23044012b31a4848d25999dc138f203`, `51982b396627bd2626f476c158a3466a7d2f35ef`, `7871f5618d08f6fa5e60ceceb8fbba2ce1e50210`, and `5f39ff02411ca20e889c70b3aa74b2478c35b673`.
- Pre-checkpoint implementation head: `5f39ff02411ca20e889c70b3aa74b2478c35b673`.
