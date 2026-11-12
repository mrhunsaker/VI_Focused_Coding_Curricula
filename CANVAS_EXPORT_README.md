# Canvas LMS Curriculum Sync

This guide documents the current behavior of `canvas_api_full_curriculum_sync.py`, the configuration it expects, how it translates the mdBook curriculum into Canvas course content, and the checks to perform before running it against a live course.

> **Important: this script is currently a create-only importer, not a safe repeatable synchronizer.** Every successful run creates new Canvas Modules, Pages, and qualifying Assignments. It does not search for previously created objects, update them, or remove stale objects. Do not rerun it against the same course unless you intend to create another copy of the content.

## 1. What the script creates

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

## 2. Requirements

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

## 3. Configure Canvas credentials

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

## 4. Run the script

Run from the repository root so that both `SUMMARY.md` and its linked files resolve correctly:

```bash
uv run python canvas_api_full_curriculum_sync.py
```

The script connects to the configured course, then processes each parsed module in order. Console output reports the course connection, module names, Page creation, and Assignment creation.

The script uses paths relative to the current working directory, not relative to the Python script's own location. Running it from another directory can therefore cause it to miss `SUMMARY.md` or source files.

## 5. Recommended first-run procedure

1. **Use a Canvas test course first.** Do not experiment in a live production course.
2. Confirm the course ID and institution URL independently in Canvas.
3. Confirm `.env` is local and ignored by Git.
4. Review `SUMMARY.md` and verify that its links point to the intended curriculum files.
5. Check that all linked local files exist. In particular, do not rely on the script's placeholder behavior as a substitute for checking missing content.
6. Review the assignment keyword rule. Paths containing `unit`, `lesson`, `bash`, or `powershell` will produce upload Assignments.
7. Run the script once against the test course.
8. Inspect the resulting Modules, Pages, module item order/indentation, Page formatting, publication state, Assignment points, submission type, and allowed file extensions.
9. Only after the test course is correct should you plan a production run. Because the script is create-only, verify that the production course does not already contain a prior import.

## 6. Current limitations and safety considerations

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

## 7. Troubleshooting

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

The Python file has been checked for Python syntax compilation. That check establishes that the file parses; it does **not** prove that the installed dependency versions, Canvas permissions, Canvas API responses, course configuration, or end-to-end import have been validated.

A successful live verification requires a configured test course and token, followed by inspection of the created Canvas objects. Record the test date, course/test environment, script revision, outcome, and any exceptions separately. Do not record the API token.

## 9. Source code

The implementation is maintained separately in:

- `canvas_api_full_curriculum_sync.py`

Run that file using the command in [Section 4](#4-run-the-script). This README documents the behavior of the current implementation; if the script changes, update this guide and repeat the test-course verification.
