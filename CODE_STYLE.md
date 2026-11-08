# Code and Editorial Style

These conventions apply to Markdown, explanations, examples, and project code. The goal is consistent, maintainable content that works well for screen-reader users and other learners.

## Markdown and structure

- Use one top-level `#` heading per page. Nest headings in logical order; do not choose heading levels for visual appearance.
- Use descriptive headings that communicate the topic.
- Prefer short paragraphs and explicit ordered steps for procedures.
- Use descriptive link text. Avoid "click here", unexplained raw URLs, and links whose purpose is conveyed only by color.
- Use tables only when they clarify relationships. Keep them simple, with header rows; do not use tables for layout.
- Provide meaningful alt text for informative images. Never put essential instructions only in an image.
- Use fenced code blocks with language identifiers such as ```python, ```javascript, ```typescript, ```java, or ```sh.
- Use inline code for identifiers, commands, filenames, shortcuts, and literal values.
- Keep internal links relative to the source Markdown file and verify their targets.

## Cross-platform command examples

- Every executable fenced `bash`, `sh`, or `shell` command block must be followed immediately by a matching fenced `powershell` block for Windows 11.
- Keep the Bash-family block first for macOS and Linux. Place the PowerShell block directly after it, with a clear Windows Powershell label.

- **Shell-specific prerequisite tracks:** files dedicated to teaching one shell (for example, `TERMINAL/bash.md` and `TERMINAL/powershell.md`) intentionally contain executable examples only for that shell. Their paired track pages must teach equivalent outcomes. The immediate Bash/PowerShell pairing rule applies to cross-platform lesson documents, not to these intentionally separate shell tracks.
- The two blocks must perform the same task, use the same project paths and filenames, and preserve the same learning objective. Do not translate Linux-only commands literally: provide a Windows-native alternative such as `winget`, `Set-Location`, or the Gradle `.bat` wrapper as appropriate.
- Do not install Python course dependencies with bare/global `pip` or `python -m pip`. Prefer `uv` project environments and dependency declarations (`uv init`, `uv add`, `uv run`, `uv sync`). For Node.js/TypeScript, use project-local npm dependencies and `npx`/npm scripts; avoid global package installs. For Java, prefer the project Maven/Gradle wrapper so build tools and dependencies are project-scoped.
- Do not recommend Volta for Node.js version management. Use the Node.js LTS installer or another actively maintained, documented version manager.
- Use PowerShell syntax in the Windows block, not Command Prompt syntax. Prefer commands compatible with the Windows PowerShell shipped with Windows 11.
- For Python virtual environments, use `.venv\\Scripts\\Activate.ps1` in PowerShell. If script execution is blocked, explain how to set a temporary process-scoped execution policy rather than changing the machine-wide policy.
- For interactive REPL examples, make clear which commands are entered in the shell and which are entered after the REPL starts.
- Keep output-only examples, source-code examples, configuration files, and syntax demonstrations unpaired unless they actually instruct the learner to execute shell commands.

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

- **Python:** target Python 3.12 or newer; keep examples compatible with 3.12. Follow PEP 8, use four spaces for indentation, prefer built-in collection type annotations, pathlib, context managers, and `uv` for project environments and dependencies. Avoid global pip installs.
- **JavaScript:** target Node.js 26 LTS. Use const by default, let when reassignment is required, strict equality, explicit input conversion, node: built-in module specifiers, and an explicitly declared CommonJS or ES module format. Use consistent braces and indentation; explain asynchronous behavior when introduced.
- **TypeScript:** compile with the current stable TypeScript compiler and target Node.js 26 LTS. Enable strict checking, annotate function parameters and public contracts, prefer inference for obvious local values, use unknown and type guards for untrusted data, and avoid routine any or unsafe type assertions. Remember that TypeScript types are erased and do not validate runtime input.
- **Kotlin (supplement only):** Kotlin material is optional post-capstone extension for Java learners. Follow current Kotlin conventions and clearly distinguish Kotlin syntax from Java interoperability details.
- **Java:** target JDK 25 LTS and avoid preview features. Use conventional naming (UpperCamelCase for classes, lowerCamelCase for methods and variables), explicit imports and types, generics, try-with-resources, and consistent indentation.
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
