# Code and Editorial Style

These conventions apply to Markdown, explanations, examples, and project code. The goal is consistent, maintainable content that works well for screen-reader users and other learners.

## Markdown and structure

- Use one top-level `#` heading per page. Nest headings in logical order; do not choose heading levels for visual appearance.
- Use descriptive headings that communicate the topic.
- Prefer short paragraphs and explicit ordered steps for procedures.
- Use descriptive link text. Avoid "click here", unexplained raw URLs, and links whose purpose is conveyed only by color.
- Use tables only when they clarify relationships. Keep them simple, with header rows; do not use tables for layout.
- Provide meaningful alt text for informative images. Never put essential instructions only in an image.
- Use fenced code blocks with language identifiers such as ```python, ```javascript, ```java, or ```sh.
- Use inline code for identifiers, commands, filenames, shortcuts, and literal values.
- Keep internal links relative to the source Markdown file and verify their targets.

## Accessible instructional writing

- Write explicit instructions that can be followed without visual interpretation.
- Describe keyboard actions by key name and sequence. Avoid "click the green icon" or "look at the panel on the right" unless an equivalent accessible route is also provided.
- Do not rely on color, position, shape, or typography alone to convey meaning.
- Explain relevant editor, terminal, and screen-reader context. Identify operating-system- or application-specific commands.
- Spell out unfamiliar abbreviations on first use.
- Explain punctuation, indentation, braces, and other syntax when important to understanding or screen-reader navigation.
- Include expected text output when it helps learners verify behavior.
- Keep core learning activities possible using keyboard-accessible, text-based workflows.
- If a task genuinely requires a graphical tool, state that requirement and provide an accessible alternative where feasible.

## Code examples

- Prefer small, complete, runnable examples over fragments with unexplained dependencies.
- Use conventional idioms and consistent formatting for each language.
- Include imports, setup, and execution commands when necessary.
- Use descriptive variable and function names.
- Explain non-obvious behavior and important edge cases.
- Show representative output in a separate text block when useful.
- Never include credentials, tokens, private data, or unsafe commands.
- Identify language and runtime assumptions, especially when syntax or APIs vary by version.

## Language conventions

- **Python:** follow standard Python conventions (PEP 8) unless a lesson explicitly teaches a contrast. Use four spaces for indentation.
- **JavaScript:** use modern, broadly supported syntax compatible with the curriculum's stated Node.js baseline. Use consistent braces and indentation; explain asynchronous behavior when introduced.
- **Java:** use conventional naming (UpperCamelCase for classes, lowerCamelCase for methods and variables), explicit types, and consistent indentation. Identify the required JDK version.
- **Shell:** identify the intended shell or operating system if commands are not portable.

## Editorial consistency

- Use consistent terminology within a curriculum and define terms before relying on them.
- Distinguish language features from editor, runtime, operating-system, or screen-reader features.
- Mark optional extensions and advanced topics as such.
- Keep learning objectives, explanations, examples, and exercises aligned.
- Use inclusive language; do not assume a learner's vision, assistive technology, prior knowledge, or hardware.
- Cite external sources and attribute adapted material. Do not copy substantial third-party text without permission.
- For version-sensitive installation guides, verify official documentation and state when instructions were last checked where appropriate.

## mdBook and repository files

- Edit Markdown source, `SUMMARY.md`, `book.toml`, and relevant workflow/documentation files.
- Do not commit generated mdBook output from `book/`.
- Keep `SUMMARY.md` in teaching order and ensure every listed page exists.
- Test with `mdbook build` when possible.
- Record changes in `CHANGES.md`.
- Never modify files under `cs_curriculum_final/`; that directory is reference-only.
