## 2026-11-08 — Foundations lesson on self-documenting code

- Added Lesson P.7, **Self-Documenting Code, Naming, Types, and Comments**, to the Computing Foundations Primer.
- Covers meaningful names for variables, functions, classes, and constants; focused function responsibilities; side effects; type systems and annotations across statically and dynamically typed languages; useful API documentation; and comments that explain intent, assumptions, and constraints rather than restating code.
- Includes a before-and-after Python example, practical review questions for code revisited months later, activities, screen-reader-oriented naming guidance, and a skills checklist.
- Updated the Foundations overview to list the new lesson. Existing Summary links remain unchanged; no new file or navigation entry was required.

## 2026-11-08 — Standalone topics section introduction and summary audit

- Created `MODULES/README.md` as the introduction to the standalone topics section, describing HTML/CSS, R, and SQL; explaining how these focused modules relate to the full language curricula; and providing prerequisites, suggested study order, accessibility expectations, and navigation to the section index.
- Audited every relative Markdown link in the reorganized `SUMMARY.md` against the repository's current file tree. The only missing target was `MODULES/README.md`; it has now been created. All Summary links now resolve to existing files.
- Checked the new section introduction's relative links against the repository tree; all resolve. No other Summary targets required creation.

## 2026-11-08 — Screen-reader-accessible GUI libraries and implementation guidance

- Created `DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md`, covering accessible GUI frameworks and platform accessibility APIs for all 13 full language curricula, HTML/CSS, R, SQL, and the Bash and PowerShell terminal tracks.
- Documented recommended libraries, implementation practices, higher-risk approaches to avoid or restrict, platform-specific screen-reader testing, automated checks, and a release checklist.
- Clarified that no toolkit guarantees accessibility on its own; accessibility must be verified in the shipped application with the target operating systems and assistive technologies.
- Added the guide to `SUMMARY.md`, resolving the previously identified missing target referenced by the Swift, Rust, and Go introductions.
- Research references include W3C WCAG and ARIA guidance, platform documentation from Apple, Microsoft, Android, Qt, GTK, and toolkit-specific accessibility documentation. A complete mdBook build has not been run in this turn.

## 2026-11-08 — Introductory computer science and language bibliographies

- Added a general computer science bibliography to the shared Foundations introduction, covering broad CS survey, digital-computing concepts, and introductory problem-solving texts.
- Added curated introductory book recommendations to all 13 language curriculum introductions: Python, JavaScript, TypeScript, Java, Kotlin, C, C++, C#, Julia, Swift, Rust, Go, and Lua.
- Added relevant reading recommendations to the HTML/CSS, R, and SQL focused modules.
- Added Bash and PowerShell book recommendations to their respective terminal-track introductions.
- Each entry identifies author(s), title, edition or publication year when verified, publisher or free online source, and a short note explaining fit, prerequisite assumptions, or version limitations.
- Updated the curriculum overview to point readers to the new bibliographies.
- Validation: book details and bibliographic links were researched against publisher, author, official language, and maintained book-site sources. Confirmed that each of the 13 language introductions, three focused modules, the shared Foundations introduction, and both terminal tracks contains a bibliography. The added bibliography links are external references; a complete mdBook build has not been run in this turn. A relative-link audit also surfaced three links to `DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md` in the Swift, Rust, and Go introductions; the target was subsequently created as the screen-reader-accessible GUI guide.

## 2026-11-08 — Curriculum scope and language-use overview

- Rewrote the main README and curriculum overview to describe the complete repository structure: 13 full language curricula, focused HTML/CSS, R, and SQL modules, shared computing foundations, and Bash and PowerShell terminal tracks.
- Replaced the original four-language framing with domain-oriented descriptions of each language's primary uses and representative software, platforms, and projects.
- Clarified the distinction between general-purpose programming languages, markup and style-sheet technologies, declarative SQL, and shell languages.
- Removed language-tier framing such as beginner and advanced languages. Language selection is now described in terms of technical domain, ecosystem, deployment target, and project requirements.
- Updated project structure, learning pathways, accessibility, and development-environment descriptions to reflect the expanded curriculum, including development containers and specialist IDE/data platforms.
- Validation: checked both updated documents for stale four-language and beginner/advanced-language framing; repository link and mdBook build validation pending.

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


## 2026-10-30 — Step 9: Cross-platform Bash and Windows PowerShell command examples

- Audited **all 63 Markdown files** in the repository, including active curricula, instructor guides, project documentation, and archived/reference Markdown.
- Identified **127 executable Bash-family fenced command blocks** across **29 Markdown files**. Added a labeled `powershell` block immediately after each corresponding `bash`, `sh`, `shell`, or `zsh` block. Bash-family examples remain first for macOS and Linux; Windows 11 learners receive native PowerShell equivalents.
- Windows alternatives cover Python installation, `py -3`, pip, virtual environments and activation, Node.js installation and REPL use, npm, JDK installation, JShell, Java/Kotlin compilation, Maven, the Gradle `.bat` wrapper, VS Code, mdBook, and Git. Linux-only apt/dpkg/NodeSource installation commands are translated to Windows `winget` or an appropriate Windows installer rather than copied literally.
- Historical Node 18 lessons in the archived material use the pinned Node.js 18.20.8 Windows MSI installer so the Windows command matches the legacy Node 18 runtime target. Current Node.js lessons use the Node.js LTS winget package.
- Removed duplicate Windows install commands introduced when multi-line apt installation sequences were translated. Python virtual-environment instructions include process-scoped PowerShell execution-policy guidance for activation when needed.
- Added the permanent paired-command rule to `CODE_STYLE.md` and `CONTRIBUTING.md`, and documented the platform convention in `OVERALL_README.md`.
- Automated validation: all 127 Bash-family fences have an immediately following Windows PowerShell label and `powershell` fence. All 29 changed Markdown files passed a balanced-fence audit.
- The user explicitly requested that every Markdown file be covered. Accordingly, `cs_curriculum_final/` received only the PowerShell counterparts for existing shell examples; its archived curriculum text was otherwise left unchanged.
- GitHub Actions run [41088527780](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41088527780) for commit `6f421e4b1d5c0b5b8a8251b1751c78082c8ec741` completed successfully. mdBook build, Pages configuration, artifact upload, and deployment all passed.
- The normal-browser published-site smoke test remains pending from the prior deployment-validation step.
- Implementation commits: `84040c66eb196231f365375d529bfe7dadc6dcaf`, `49707f3725b0841d63706dfd530e43e14b4f89bf`, `e2df42fb7df0348779751cae75ffdcb7bcfc8501`, `1b45d6df5509409cd601fbb88b6998ba05fec905`, `883c71b60c4ef6497cd1ad35079b535d92308791`, `7a159a360bf1c7a683a591cd6e8966da0ec842de`, `a50665ff803e4507468683a625fba250f8958637`, `f1bf41ebca8592e1fd5ad459c66826853324756c`, `b6feb659fac70e4612fd3abc0c0d8d52181ee142`, `ad5ef4fd931cb969c3985fd8df73c5d78600b15b`, `23191bd243a8a47cac377683d40e02b62728321d`, `f7eb9a362d29b3877d2afb8a6acb2e6bb139067a`, `50a4584af92f691b75991c518b173975a1daa61a`, `36681803f5036ea2f094cdacd1d83593d11322c2`, `8944436bc778d0a9f10e44cf20037599eef4132b`, and `6f421e4b1d5c0b5b8a8251b1751c78082c8ec741`.
- Implementation head validated by Actions: `6f421e4b1d5c0b5b8a8251b1751c78082c8ec741`.


## 2026-10-30 — Student glossary and language indexes

- Added backmatter/GLOSSARY.md, an explicit glossary of shared concepts and language-specific terminology for Python, JavaScript, TypeScript, Java, and Kotlin.
- Added topic-to-lesson indexes in PYTHON/INDEX.md, JAVASCRIPT/INDEX.md, TYPESCRIPT/INDEX.md, and JAVA/INDEX.md. The Java index includes the optional Kotlin supplement.
- Added backmatter/indexing_setup.json, a reusable maintenance prompt and schema for future index creation and updates.
- Updated SUMMARY.md, README.md, and OVERALL_README.md. mdBook full-text search remains enabled; curated indexes supplement it with organized topic navigation.

- Validation: glossary has 148 term headings; four language indexes contain 135 relative links, all resolving to existing files. The JSON indexing prompt parsed successfully.
- GitHub Actions run [41091043060](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41091043060) for commit `b50ed5ea4e53ef72cc2fc3be80d29361c7c4ea75` succeeded, including mdBook build and GitHub Pages deployment.
- Normal-browser visual smoke test remains pending; successful build/deployment is not a substitute for that check.


## 2026-10-30 — Project-scoped environment management and Theia IDE option

- Standardized Python package installation guidance on Astral uv: `uv init --python 3.12`, `uv add`, `uv run`, `uv sync`, and `uv tree`. The Python setup now documents installing uv with the official standalone installers and using uv to manage the interpreter and project-local `.venv`. Removed global pip installation instructions from active Python setup and capstone materials.
- Confirmed JavaScript and TypeScript setup uses project-local npm dependencies and `npx`/npm scripts; updated teacher guidance to explicitly avoid global npm installs for course tools. No Volta recommendations were introduced.
- Added [Theia IDE](https://theia-ide.org/#theiaide) as an alternative to Visual Studio Code in the overview, README, Python/JavaScript/TypeScript/Java landing pages, setup lessons, and teacher guidance. Instructions advise checking Open VSX extension availability and testing screen-reader workflows in the learner's environment.
- Explicitly excluded JetBrains IDEs from the recommended introductory setup because their breadth and complexity create unnecessary overhead for beginners. Removed IntelliJ IDEA recommendations from Java and Kotlin setup guidance.
- Updated CODE_STYLE.md, CONTRIBUTING.md, and backmatter/indexing_setup.json so future contributors and indexing passes preserve these environment-management and editor-choice conventions.

- The Python, JavaScript, TypeScript, and Java setup lessons now give Theia-specific extension-view and screen-reader configuration guidance instead of assuming every VS Code command or shortcut is identical.

- Final setup review aligned the Python completion checklist with the uv-managed interpreter (`uv run python --version`) rather than assuming a system-wide Python executable.

- Java build/test examples now use Maven and Gradle project wrappers (`./mvnw` / `mvnw.cmd`, `./gradlew` / `gradlew.bat`) rather than requiring globally installed build tools.

- Expanded the student glossary with explicit entries for `uv`, `npx`, project-local npm dependencies, and Maven/Gradle wrappers so the new setup conventions are defined in the student reference.

- Static validation passed for the updated environment-management and editor guidance. JSON validation passed for the indexing setup prompt and project plan. GitHub Actions run [41101871104](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41101871104) remains queued for the implementation commit; mdBook build and deployment confirmation are pending.


## 2026-10-30 — Step 12: Strengthen language-specific IDE and environment setup

- Updated all four language setup units: Python, JavaScript, TypeScript, and Java.
- Made VS Code and Theia IDE explicit parallel editor options in each setup, with separate extension guidance and a reminder that Visual Studio Marketplace extensions are not automatically available through Open VSX.
- Added verification expectations for language services, diagnostics, completion, navigation, terminal access, debugging/testing where relevant, and screen-reader announcements.
- Strengthened environment alignment habits:
  - Python: select the project-local `.venv` interpreter and use `uv add` / `uv run`; avoid global package installs and editor run actions that bypass the environment.
  - JavaScript: open the npm project root, use local `node_modules` tools, and verify that the IDE terminal and system terminal resolve the same Node.js runtime.
  - TypeScript: use the workspace TypeScript compiler, run `npx tsc`, compile to JavaScript, and execute the emitted JavaScript with Node.js.
  - Java: configure the IDE and terminal to use the same full JDK 25, verify both `java` and `javac`, and introduce Maven/Gradle wrappers only when the curriculum reaches build tools.
- Added JetBrains IDEs as advanced options for experienced coders in each setup, without download or usage instructions. They remain outside the recommended beginner workflow.
- Clarified the Theia-specific workspace-opening workflow in the Python setup so the project root containing `pyproject.toml` is opened and `.venv` discovery works.
- Standardized the Python advanced-editor wording to explicitly name JetBrains IDEs (PyCharm) as an experienced-coder option.
- No lesson topics or language baselines were changed. No files under `cs_curriculum_final/` were modified.
- Static validation passed: all four setup documents have balanced Markdown fences; all 20 Bash-family blocks are immediately paired with Windows PowerShell blocks; each setup contains VS Code, Theia, and JetBrains advanced-option guidance; `convert_to_mdbook.json` parses successfully. mdBook build/CI verification is pending.
- Implementation commits: `19a091e7b15683e4446307c9d8ecf72e85b8cb79`, `3018ffc98ec455de06ab106cd00b303c225a1930`, `249ec412cf2e20a2ec96b2adb3916a4e4ca92808`, `c8b35f54fbc7b38d364eef40fe15bf379aa7d9b5`.
- Pre-checkpoint HEAD: `c8b35f54fbc7b38d364eef40fe15bf379aa7d9b5`.

## 2026-11-08 — Terminal prerequisite curriculum

- Added the missing `TERMINAL/` curriculum referenced by the book navigation: a prerequisite overview plus independent Bash (macOS/Linux) and PowerShell (Windows 11) tracks.
- Both tracks teach equivalent outcomes through eight lessons: shell orientation; paths and navigation; file and directory operations; command syntax and efficient entry; text inspection and search; running programs and interpreting exit status; processes and help; and an integrated practice project.
- Added explicit learning objectives, worked command sequences, expected behavior, activities, safety guidance, accessibility practices, skills checklists, and official documentation references.
- Kept shell-specific examples native to each track and clarified this intentional exception in `CODE_STYLE.md`; cross-platform curriculum documents continue to pair Bash and PowerShell command blocks.
- Cleaned pre-existing merge-conflict marker text from `SUMMARY.md` while retaining the Foundations navigation section and the existing terminal navigation entries.
- No files under `cs_curriculum_final/` were modified.
- Implementation commits: `701a6f1fbfdf669b141d1cc2fea4cac645530097` (overview), `d0aba3a2f65b9596377dc3e7135d1429a2d6049c` (Bash), `d6c548c3bbdea02f48c81dfd43b6a0091989a53a` (PowerShell), `0e5a534c9b37953c7e13ca7c59a806ebd127e862` (navigation), and `46314e57ae9dd0e179b2704c86289777460522d8` (style clarification).
- mdBook build and GitHub Actions verification are pending.
