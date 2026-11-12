# Canvas LMS Curriculum Sync Tool

This tool programmatically syncs your `mdBook` project structure directly into **Canvas LMS** as structured Modules, Markdown Pages, and file-upload Assignments. It reads your `SUMMARY.md` file to map hierarchy and supports nested parallel tracks (such as OS-specific paths).

## Prerequisites

- Python 3.x
- [`uv`](https://github.com/astral-sh/uv) package manager installed.

## Setup Instructions

1. **Configure Environment Variables:**
   Create a `.env` file in the root directory of your project with the following configuration:
   ```env
   CANVAS_API_URL=[https://your-institution.instructure.com](https://your-institution.instructure.com)
   CANVAS_API_KEY=your_canvas_bearer_token_here
   CANVAS_COURSE_ID=your_numeric_course_id
   POINTS_PER_ASSIGNMENT=10