# Canvas LMS Export and Synchronization Guide

This repository uses a single publishing tool:

```text
canvas_api_full_curriculum_sync.py
```

The script supports two workflows:

| Workflow | Recommended | Requires Canvas API Credentials | Modifies Live Canvas Course |
|-----------|-----------|-----------|-----------|
| IMS Common Cartridge Export (`--export-imscc`) | Yes | No | No |
| Canvas API Synchronization | Advanced | Yes | Yes |

For most users, the recommended workflow is:

```text
mdBook → IMSCC Export → Canvas Import
```

This produces a portable standards-based package that can be reviewed, tested, archived, and imported into one or more Canvas courses.

---

# Which Workflow Should I Use?

## Use IMSCC Export If

- You want a portable package.
- You want to validate content before publishing.
- You need a backup archive.
- You are importing into multiple Canvas courses.
- You do not have Canvas API access.
- You want the safest and most reproducible workflow.

## Use Canvas API Synchronization If

- You have Canvas API credentials.
- You want direct publishing into Canvas.
- You are working with development or test courses.
- You want automated curriculum publication.
- You do not want to manually import IMSCC files.

For most users, IMSCC export is the recommended workflow.

---

# Project Layout

The exporter no longer requires all content to live in the repository root.

Example:

```text
project-root/
├── .env
├── pyproject.toml
├── uv.lock
├── canvas_api_full_curriculum_sync.py
└── my-book/
    └── src/
        ├── SUMMARY.md
        ├── introduction.md
        ├── lesson-01.md
        ├── lesson-02.md
        ├── images/
        └── downloads/
```

The exporter reads:

```env
SUMMARY_PATH=./my-book/src/SUMMARY.md
```

from `.env`.

The directory containing `SUMMARY.md` automatically becomes the mdBook source directory unless overridden by `--source-dir`.

---

# Installing Dependencies

This project uses **uv**.

## Export-Only Dependencies

Required for IMSCC package generation:

```bash
uv add markdown python-dotenv
```

## Full Functionality

Required for IMSCC export, validation, and Canvas API synchronization:

```bash
uv add markdown python-dotenv canvasapi
```

## Existing Repository

If dependencies are already defined in `pyproject.toml`:

```bash
uv sync
```

---

# Configuration

Create a `.env` file in the repository root.

## Export-Only Configuration

```env
SUMMARY_PATH=./my-book/src/SUMMARY.md
```

## Full Configuration

```env
SUMMARY_PATH=./my-book/src/SUMMARY.md

CANVAS_API_URL=https://yourinstitution.instructure.com
CANVAS_API_KEY=your_canvas_token
CANVAS_COURSE_ID=123456

POINTS_PER_ASSIGNMENT=10
```

---

# Configuration Variables

| Variable | Required | Description |
|-----------|-----------|-----------|
| `SUMMARY_PATH` | Yes | Path to mdBook `SUMMARY.md` |
| `CANVAS_API_URL` | API Mode | Canvas base URL |
| `CANVAS_API_KEY` | API Mode | Canvas API token |
| `CANVAS_COURSE_ID` | API Mode | Canvas course ID |
| `POINTS_PER_ASSIGNMENT` | Optional | Default assignment point value used during API synchronization |

---

# Command and Flag Reference

## Commands

| Command | Effect |
|----------|----------|
| `uv run python canvas_api_full_curriculum_sync.py --dry-run` | Validate curriculum structure without creating an IMSCC package or contacting Canvas. |
| `uv run python canvas_api_full_curriculum_sync.py --export-imscc curriculum.imscc` | Create an IMS Common Cartridge package. Does not connect to Canvas. |
| `uv run python canvas_api_full_curriculum_sync.py --title "Course Name" --export-imscc curriculum.imscc` | Create an IMSCC package with a custom title stored in cartridge metadata. |
| `uv run python canvas_api_full_curriculum_sync.py --summary ./other/SUMMARY.md --export-imscc curriculum.imscc` | Use an alternate summary file instead of `SUMMARY_PATH`. |
| `uv run python canvas_api_full_curriculum_sync.py --source-dir ./other/src --summary ./other/src/SUMMARY.md --export-imscc curriculum.imscc` | Override the source directory used to resolve curriculum files and assets. |
| `uv run python canvas_api_full_curriculum_sync.py` | Publish directly to Canvas using the configured API credentials. |

## Flags

| Flag | Description |
|--------|--------|
| `--dry-run` | Validate curriculum structure and report curriculum statistics without exporting or contacting Canvas. |
| `--export-imscc OUTPUT.imscc` | Enable IMS Common Cartridge export mode. |
| `--title "Course Title"` | Set the course title stored in cartridge metadata. |
| `--summary PATH` | Override the `SUMMARY_PATH` value from `.env`. |
| `--source-dir PATH` | Override the source directory used when resolving Markdown files and local assets. |

---

# Validation Workflow

Before publishing curriculum content, validate it.

## Step 1: Validate

```bash
uv run python canvas_api_full_curriculum_sync.py --dry-run
```

The validator:

- Loads `SUMMARY.md`
- Parses curriculum modules
- Counts curriculum pages
- Counts assignment candidates
- Verifies referenced Markdown files exist

The validator does **not**:

- Create an IMSCC package
- Connect to Canvas
- Modify any Canvas course

Example output:

```text
Curriculum Validation Summary
================================

SUMMARY.md: /path/to/SUMMARY.md
Source Root: /path/to/src

Modules: 8
Pages: 54
Assignment Candidates: 21

Validation: PASS
```

## Step 2: Export

```bash
uv run python canvas_api_full_curriculum_sync.py \
    --export-imscc dist/curriculum.imscc
```

## Step 3: Test Import

Import the generated cartridge into a Canvas sandbox or test course.

Verify:

- Module organization
- Page order
- Images
- Downloads
- Internal links

## Step 4: Publish

Import into production or use Canvas API synchronization if appropriate.

---

# Recommended Workflow: IMSCC Export

## Generate a Common Cartridge Package

```bash
uv run python canvas_api_full_curriculum_sync.py \
    --export-imscc dist/curriculum.imscc
```

Result:

```text
dist/curriculum.imscc
```

The exporter does not:

- Connect to Canvas
- Require Canvas API credentials
- Modify any live course

## Generate a Package With a Custom Course Title

```bash
uv run python canvas_api_full_curriculum_sync.py \
    --title "VI Focused Coding Curricula" \
    --export-imscc dist/curriculum.imscc
```

The supplied title is stored in cartridge metadata.

---

# What Happens During IMSCC Export

The exporter performs the following operations.

## 1. Loads SUMMARY.md

The script loads:

```env
SUMMARY_PATH
```

or the path supplied through:

```bash
--summary
```

## 2. Creates Module Structure

Each heading in `SUMMARY.md` becomes a logical LMS module section.

Example:

```markdown
# Module 1

- [Introduction](intro.md)
- [Lesson 1](lesson1.md)

# Module 2

- [Lesson 2](lesson2.md)
```

## 3. Converts Markdown to HTML

Each referenced Markdown file is converted into standalone HTML.

Supported Markdown extensions:

```text
fenced_code
tables
nl2br
```

## 4. Rewrites Internal Links

Links between Markdown files included in the curriculum are rewritten to point to generated HTML pages inside the cartridge.

This preserves course navigation after import.

## 5. Packages Local Assets

Referenced assets are automatically included.

Examples:

```markdown
images/network.png
downloads/lab.pdf
```

Asset references are rewritten to packaged resources.

## 6. Creates an IMS Common Cartridge Manifest

The exporter generates:

```text
imsmanifest.xml
```

conforming to the IMS Common Cartridge 1.2 specification.

## 7. Validates the Package

Before writing the final archive, the exporter validates:

- XML well-formedness
- ZIP integrity
- Manifest presence
- Manifest file references

The exporter verifies that every file referenced by the generated manifest exists within the package.

---

# What the Exporter Places Into the IMSCC Package

The generated package contains:

- Module hierarchy metadata
- Page metadata
- HTML page content
- Internal curriculum links
- Images
- Downloadable resources
- IMS Common Cartridge metadata
- Navigation relationships

> Canvas ultimately controls how imported content is represented after import. The exporter provides module and navigation metadata, but final presentation depends upon Canvas's Common Cartridge importer.

---

# What the IMSCC Package Does Not Contain

> [!IMPORTANT]
> IMSCC export creates web-content resources and module organization only.

The exporter does **not** create:

- Canvas Assignments
- Gradebook items
- Rubrics
- Discussions
- Quizzes
- Question banks
- Announcements
- Student submissions
- Enrollment information
- LTI tools
- Canvas-specific settings

These are Canvas objects and are not generated during IMSCC export.

---

# Importing Into Canvas

1. Open the destination Canvas course.
2. Select **Settings**.
3. Select **Import Course Content**.
4. Choose:

```text
Common Cartridge 1.x Package
```

5. Upload the generated `.imscc` file.
6. Select **All Content**.
7. Start the import.
8. Verify:

   - Modules
   - Pages
   - Images
   - Downloads
   - Internal navigation links

before importing into production.

---

# Canvas API Synchronization

Canvas API mode directly modifies an existing Canvas course.

Run:

```bash
uv run python canvas_api_full_curriculum_sync.py
```

The script will:

- Connect to the configured Canvas course
- Create Canvas modules
- Create Canvas pages
- Publish pages
- Add pages to modules
- Create file-upload assignments for qualifying lesson content

Canvas API credentials must be configured in `.env`.

---

# Assignment Generation (API Mode Only)

Assignments are **only** created during Canvas API synchronization.

Assignments are **never** created during IMSCC export.

During API synchronization, the script automatically creates a file-upload assignment whenever the source path contains one of the following keywords:

```text
unit
lesson
bash
powershell
```

(case-insensitive)

Generated assignments:

- Published
- File-upload based
- Created using the value of `POINTS_PER_ASSIGNMENT`

Allowed file extensions:

```text
zip
tar
py
c
cpp
rs
js
go
java
cs
txt
pdf
```

---

# Important API Limitations

> [!WARNING]
> Canvas API synchronization is currently create-only.

Each execution may create additional modules, pages, and assignments.

The script currently does not:

- Update existing content
- Delete existing content
- Detect duplicates
- Merge changes
- Roll back failed operations

The IMSCC workflow is not affected by these limitations.

Always test API synchronization against a non-production course first.

---

# Troubleshooting

## SUMMARY.md Not Found

Verify:

```env
SUMMARY_PATH=./my-book/src/SUMMARY.md
```

and confirm the file exists.

## Linked Markdown File Missing

Every file referenced by `SUMMARY.md` must exist.

Example:

```markdown
- [Lesson 1](lesson-01.md)
```

must point to a valid file.

## Missing Images or Downloads

Verify asset paths exist beneath the mdBook source directory.

Example:

```markdown
images/network.png
```

## Canvas Rejects the Package

Verify:

```text
Common Cartridge 1.x Package
```

was selected as the import type.

Also verify that the IMSCC package was created successfully and was not modified after export.

---

# Quick Start

## Validate Curriculum

```bash
uv run python canvas_api_full_curriculum_sync.py --dry-run
```

## Generate an IMSCC Package

```bash
uv run python canvas_api_full_curriculum_sync.py \
    --export-imscc dist/curriculum.imscc
```

## Import Into Canvas

```text
Settings
→ Import Course Content
→ Common Cartridge 1.x Package
→ Upload curriculum.imscc
```

## Publish Directly Through the API

```bash
uv run python canvas_api_full_curriculum_sync.py
```

Use API synchronization only when you intend to directly modify a Canvas course.

---

# Source File

```text
canvas_api_full_curriculum_sync.py
```

This README documents the current behavior of the exporter and synchronization tool. Update the README whenever exporter behavior changes.