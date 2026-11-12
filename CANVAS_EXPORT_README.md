# Canvas LMS Curriculum Sync Tool

This tool programmatically syncs your `mdBook` project structure directly into **Canvas LMS** as structured Modules, Markdown Pages, and file-upload Assignments. It reads your `SUMMARY.md` file to map hierarchy and supports nested parallel tracks (such as OS-specific paths).

## Prerequisites

- Python 3.x
- [`uv`](https://github.com/astral-sh/uv) package manager installed.

## Setup Instructions

1. **Configure Environment Variables:**
   Create a `.env` file in the root directory of your project with the following configuration:

   ```env
   CANVAS_API_URL=https://your-institution.instructure.com
   CANVAS_API_KEY=your_canvas_bearer_token_here
   CANVAS_COURSE_ID=your_numeric_course_id
   POINTS_PER_ASSIGNMENT=10
   ```

2. **Install Dependencies via `uv`:**
   Run the following command in your terminal to initialize dependencies inside your `uv` environment:

   ```bash
   uv pip install canvasapi markdown python-dotenv
   ```

## Running the Sync Script

Execute the script from your project root using `uv run`:

```bash
uv run python canvas_api_full_curriculum_sync.py
```

## How It Works

- **Modules:** Top-level section headers (`# C`, `# PYTHON`, etc.) in your `SUMMARY.md` are created as unique Canvas Modules.
- **Pages & Context:** Markdown files (including overview READMEs and index files) are automatically converted into published Canvas Pages.
- **Parallel Tracks:** Indented sub-bullets in `SUMMARY.md` (e.g., Bash vs. PowerShell options) are mapped with proper indentation levels (`indent: 1`) inside Canvas modules.
- **Assignments:** Core units and lesson files automatically generate a companion online-upload Assignment requesting code files or workspace archives (`.zip`, `.py`, `.rs`, `.c`, etc.).
