# Canvas LMS Curriculum Export and API Sync

This guide documents two workflows in canvas_api_full_curriculum_sync.py: an offline IMS Common Cartridge export for LMS import without API credentials, and a direct Canvas API sync for users with authorized Canvas API access.

> **Important: this script is currently a create-only importer, not a safe repeatable synchronizer.** Every successful run creates new Canvas Modules, Pages, and qualifying Assignments. It does not search for previously created objects, update them, or remove stale objects. Do not rerun it against the same course unless you intend to create another copy of the content.


## Offline export: create an LMS-importable Common Cartridge (no API token)

Use this mode when an instructor or institution cannot provide a Canvas API token. It builds an **IMS Common Cartridge 1.2** package (.imscc) from the mdBook source. Common Cartridge is an LMS interchange format; it is not a Canvas API export and does not require a Canvas account to generate.

### Requirements

- Python 3.9 or later.
- The Markdown Python package. The export mode uses Python's standard library for ZIP and XML packaging.
- The repository source tree, including SUMMARY.md and every Markdown file linked from it.

Install the Markdown dependency:

~~~bash
python -m pip install markdown
~~~

If you already installed all dependencies for API sync, no additional package installation is required.

### Generate the package

Run from the repository root:

~~~bash
python canvas_api_full_curriculum_sync.py --export-imscc dist/VI_Focused_Coding_Curricula.imscc
~~~

Optional arguments:

~~~bash
python canvas_api_full_curriculum_sync.py \
  --source-dir . \
  --summary SUMMARY.md \
  --title "VI Focused Coding Curricula" \
  --export-imscc dist/VI_Focused_Coding_Curricula.imscc
~~~

The command:

1. Reads the mdBook SUMMARY.md file.
2. Creates a Common Cartridge organization with one organization section for each curriculum heading/module.
3. Converts each linked Markdown file into an HTML web-content resource.
4. Rewrites links between Markdown pages when both pages are included in SUMMARY.md.
5. Copies local files referenced by rendered HTML links and images into the package and rewrites those references.
6. Writes imsmanifest.xml and the web resources into a ZIP-based .imscc file.
7. Reopens the finished archive and checks ZIP integrity, XML well-formedness, and that manifest file references exist.

The command prints the output path, package size, module count, page count, and packaged file count. It does not connect to Canvas or modify any LMS course.

### Import the package into Canvas

1. Sign in to Canvas and open the destination course.
2. Open **Settings**.
3. Select **Import Course Content**.
4. For **Content Type**, choose **Common Cartridge 1.x Package**.
5. Choose the generated .imscc file.
6. Select **All Content** (or select specific content if offered).
7. Start the import and wait for the import job to finish.
8. Review the imported Modules and Pages, open several pages, and verify images, downloads, and internal links.

Canvas's import interface and labels may vary by institution. Other LMS products may support Common Cartridge 1.x import under a similarly named course-import or content-import workflow.

### What the package includes—and does not include

Included:
- Module/section organization from the headings in SUMMARY.md.
- HTML pages converted from the linked Markdown files.
- Local images and other local files referenced by links or image elements in the rendered pages, when those files exist inside the source directory.
- Rewritten internal links when the target Markdown file is also listed in SUMMARY.md.

Not represented as native LMS objects by this Common Cartridge export:
- Graded Canvas Assignments, online file-submission settings, points, due dates, rubrics, quizzes, question banks, discussions, announcements, gradebook configuration, student submissions, or enrollments.
- Canvas-specific API settings, course permissions, LTI integrations, or user data.
- Markdown files not linked from SUMMARY.md as standalone course pages.
- CSS url(...) assets, JavaScript behavior, or external resources requiring authentication.

The current export creates standard Common Cartridge **web-content pages and module organization**. It does not claim to reproduce every feature of a Canvas course or guarantee identical behavior in every LMS. In particular, nested indentation in SUMMARY.md is flattened within each module; the module and page order are retained.

### Export validation and troubleshooting

- If export stops because a linked Markdown file is missing, fix the path in SUMMARY.md or restore the file. The exporter fails before writing a completed package rather than silently creating a placeholder page.
- If a local image or linked file is absent, inspect the original Markdown path and the generated page; missing non-Markdown assets are not silently fabricated.
- If an internal Markdown link points to a page not listed in SUMMARY.md, the exporter cannot map it to a generated page. Add that page to the summary or update the link.
- If the LMS rejects the package, confirm that the import type is **Common Cartridge 1.x Package** and not a Canvas API export or an arbitrary ZIP import. LMS support and interpretation can vary.
- The script checks ZIP integrity and manifest references locally. A successful local package check is not the same as a successful import into Canvas or another LMS; verify with a test course before distributing the package.


## 1. API sync: what the script creates

The script reads `SUMMARY.md` from the current working directory and uses its Markdown links as the curriculum manifest.

| Source in `SUMMARY.md` | Canvas result |
| --- | --- |
| Heading line beginning with `#` | Starts a new Canvas Module for subsequent links |
| Markdown link to a local file | Creates a published Canvas Page from that file |
| Indented Markdown link | Adds the Page module item with Canvas indent level 1 |
| Link whose path begins with `http` or `#` | Skipped |
| Link path containing `unit`, `lesson`, `bash`, or `powershell` (case-insensitive) | Also creates a published online-upload Assignment |

Links before the first heading are grouped under a module named **General**. Each linked local file is converted from Markdown to HTML using the `fenced_code`, `tables`, and `nl2br` extensions. The Page is then added to the current Module.

Assignments are configured with `POINTS_PER_ASSIGNMENT` points, `online_upload` submissions, and this extension allowlist: `zip`, `tar`, `py`, `c`, `cpp`, `rs`, `js`, `go`, `java`, `cs`, `txt`, and `pdf`.

### Important interpretation details

- The parser treats every line whose trimmed text begins with `#` as a module boundary. It is intended for the heading structure in mdBook's `SUMMARY.md`, not arbitrary Markdown documents.
- Indentation is simplified to two levels: no leading spaces becomes Canvas indent 0; any leading spaces becomes Canvas indent 1. Deeper nesting is not preserved.
- A missing local Markdown file does not stop the run. The script creates a Page containing a “Content missing” placeholder.
- Assignment creation is based on keywords in the *path*, not on the content or an explicit assignment marker in the curriculum.
- The script creates Modules, Pages, and Assignments as it proceeds. If an API request fails partway through, earlier objects remain in Canvas; there is no transaction or automatic rollback.
- The script does not upload the source curriculum files as Canvas Files. It converts Markdown into Page HTML and creates upload Assignments for learners.

## 2. API sync requirements

- Python 3.9 or later is recommended.
- A Canvas instance and a course in which the API user can create Modules, Pages, and Assignments.
- A Canvas API access token authorized for that course.
- The Python packages:
  - `canvasapi`
  - `Markdown`
  - `python-dotenv`

Install the dependencies from the repository root:

```bash
uv pip install canvasapi markdown python-dotenv
```

Alternatively, create and activate a virtual environment, then install the same packages with `python -m pip install canvasapi markdown python-dotenv`.

## 3. Configure Canvas API credentials

Create a local `.env` file in the repository root:

```dotenv
CANVAS_API_URL=https://your-institution.instructure.com
CANVAS_API_KEY=your_canvas_bearer_token
CANVAS_COURSE_ID=123456
POINTS_PER_ASSIGNMENT=10
```

Configuration:

| Variable | Required | Meaning |
| --- | --- | --- |
| `CANVAS_API_URL` | Yes | Institution Canvas base URL, for example `https://school.instructure.com`. Do not append a course URL. |
| `CANVAS_API_KEY` | Yes | Canvas API access token. Treat this as a password. |
| `CANVAS_COURSE_ID` | Yes | Numeric Canvas course ID, not the course name or SIS ID. |
| `POINTS_PER_ASSIGNMENT` | No | Points possible for each generated Assignment; defaults to `10`. Must be an integer accepted by Canvas. |

### Protect the token

- Do not commit `.env`, paste the token into source code, or include it in screenshots or logs.
- Confirm that `.env` is covered by `.gitignore`. If it is not, add it before proceeding.
- If a token is exposed, revoke it in Canvas and create a replacement.
- Use a token belonging to an account with only the permissions needed to manage content in the target course.

## 4. Run the API sync

Run from the repository root so that both SUMMARY.md and its linked files resolve correctly. This mode creates content in the configured live Canvas course:

~~~bash
uv run python canvas_api_full_curriculum_sync.py
~~~

For an offline .imscc file instead, use the --export-imscc command above. Export mode does not require .env, canvasapi, python-dotenv, or an API token.

The script connects to the configured course, then processes each parsed module in order. Console output reports the course connection, module names, Page creation, and Assignment creation.

The script uses paths relative to the current working directory, not relative to the Python script's own location. Running it from another directory can therefore cause it to miss `SUMMARY.md` or source files.

## 5. Recommended first API-sync procedure

1. **Use a Canvas test course first.** Do not experiment in a live production course.
2. Confirm the course ID and institution URL independently in Canvas.
3. Confirm `.env` is local and ignored by Git.
4. Review `SUMMARY.md` and verify that its links point to the intended curriculum files.
5. Check that all linked local files exist. In particular, do not rely on the script's placeholder behavior as a substitute for checking missing content.
6. Review the assignment keyword rule. Paths containing `unit`, `lesson`, `bash`, or `powershell` will produce upload Assignments.
7. Run the script once against the test course.
8. Inspect the resulting Modules, Pages, module item order/indentation, Page formatting, publication state, Assignment points, submission type, and allowed file extensions.
9. Only after the test course is correct should you plan a production run. Because the script is create-only, verify that the production course does not already contain a prior import.

## 6. API-sync limitations and safety considerations

These limitations are present in the current Python implementation; the README does not imply that the script already handles them.

- **No dry-run mode:** running the script makes live Canvas API changes.
- **No idempotency:** a second run creates another set of Modules, Pages, and Assignments. There is no duplicate detection or update-in-place behavior.
- **No cleanup:** content removed from `SUMMARY.md` is not removed from Canvas.
- **No full nesting support:** any nonzero indentation is represented as indent 1.
- **Missing files are not fatal:** the script creates a placeholder Page and continues.
- **Partial completion is possible:** an API error during processing can leave a partially imported course.
- **Configuration validation is limited:** missing required environment variables are reported, but malformed numeric values (including a non-integer course ID or points value) can raise a Python exception.
- **No explicit preflight of all paths:** the script does not validate every linked file before making the first Canvas write.
- **No detailed run manifest:** it does not save a mapping of source paths to Canvas object IDs for later updates or cleanup.

For these reasons, treat each execution as a one-time content creation operation. If repeatable updates are required, the script should first be enhanced with a dry-run/preflight phase and a persistent source-path-to-Canvas-ID manifest, then tested against a non-production course.

## 7. API-sync troubleshooting

| Symptom | Checks |
| --- | --- |
| Missing configuration message | Confirm the `.env` file is in the repository root and the three required variable names are spelled exactly as shown. |
| Connection or authorization failure | Verify the Canvas base URL, token validity, course ID, and the account's course-level permissions. |
| `SUMMARY.md` not found | Run the command from the repository root. |
| Placeholder Page appears | Check the corresponding link path in `SUMMARY.md`; confirm the file exists relative to the repository root. |
| Duplicate Modules or Pages | The current script does not deduplicate. Stop rerunning it; manually review and clean up the test-course content as appropriate. |
| Run stops after creating some content | Inspect the course for partial results before attempting anything else. A retry can create duplicates. Review the complete exception and API response. |
| Assignment is missing | Confirm that the linked file path contains one of the assignment trigger keywords: `unit`, `lesson`, `bash`, or `powershell`. |

## 8. Verification status

The script now supports an offline Common Cartridge export and a separate API-sync mode. The exporter uses the Python standard library for ZIP/XML packaging plus the Markdown package for conversion. Local validation is performed by the automated export tests and by reopening the generated archive to check ZIP integrity, XML well-formedness, and manifest references. These checks do not prove that Canvas or another LMS will import and render the package identically. The API-sync mode uses CanvasAPI request payloads aligned with the library method signatures for creating Pages, Assignments, and module items. These checks do **not** prove that Canvas permissions, API responses, course configuration, or a live end-to-end sync have been validated.

For the offline export, run python -m unittest tests.test_canvas_common_cartridge_export and then import the resulting .imscc into a non-production Canvas course to verify LMS behavior. For API sync, a configured test course and token are required, followed by inspection of the created Canvas objects. Record the test date, course/test environment, script revision, outcome, and any exceptions separately. Do not record the API token.

## 9. Source code

The implementation is maintained separately in:

- [`canvas_api_full_curriculum_sync.py`](canvas_api_full_curriculum_sync.py)

Run that file using the command in [Section 4](#4-run-the-script). This README documents the behavior of the current implementation; if the script changes, update this guide and repeat the test-course verification.
