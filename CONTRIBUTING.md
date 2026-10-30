# Contributing

Thank you for helping improve this accessible, living computer science textbook. Contributions of all sizes are welcome: corrections, accessibility reports, clearer explanations, new exercises, and improvements to the build and documentation.

## Ways to contribute

- Start a conversation or propose an idea in [GitHub Discussions](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/discussions).
- Report an error, accessibility barrier, outdated instruction, or missing topic in [GitHub Issues](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/issues).
- Submit a focused change as a [Pull Request](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/pulls).

For substantial changes, open an issue or discussion first so the scope and learning objective can be agreed before a large rewrite.

## Contribution workflow

1. Check existing issues and discussions to avoid duplicate work.
2. Describe the problem and learner impact. For accessibility reports, include the operating system, screen reader, editor, language/runtime version, and reproduction steps when possible. Do not include private or sensitive information.
3. Fork the repository and create a branch for your change.
4. Edit Markdown source or project configuration. Do not edit generated files in `book/`.
5. Follow [CODE_STYLE.md](CODE_STYLE.md), including accessibility and code-example requirements. Every executable Bash-family command block must be immediately followed by a functionally equivalent Windows 11 PowerShell block.
6. Validate links and navigation. If mdBook is installed, run `mdbook build` from the repository root.
7. Review the rendered result where possible, including headings, code blocks, link text, and keyboard/screen-reader usability.
8. Submit a pull request describing the change, why it helps learners, affected files, and checks performed. Link a related issue or discussion when applicable.

Keep pull requests focused. If a change affects more than one language, explain why it applies to each curriculum.

## Content principles

- Preserve the educational intent and progression unless the change explicitly proposes an improvement.
- Prefer clear, direct explanations and define technical terms when first introduced.
- Use examples learners can run and inspect through text-based tools.
- Include expected output and explain meaningful errors where useful.
- Do not make visual inspection, color distinction, mouse-only actions, or screenshots a requirement for core activities.
- Do not introduce uncredited third-party content. Respect copyright and cite sources.
- Identify operating-system, language/runtime, and tool-version assumptions.
- Manage Python dependencies with `uv` rather than global pip. Keep npm dependencies project-local and use `npx` or npm scripts for local tools. Prefer Maven/Gradle wrappers for Java projects.
- Offer Theia IDE as an alternative to VS Code, and do not recommend JetBrains IDEs as the default for introductory learners. Verify screen-reader and extension behavior for the learner's setup.

## Review

Pull requests may be reviewed for correctness, clarity, accessibility, consistency with the learning sequence, licensing, and maintainability. A passing build does not by itself establish that content is accessible or pedagogically sound.

By participating, you agree to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Report vulnerabilities using the private process in [SECURITY.md](SECURITY.md), not through a public issue.
