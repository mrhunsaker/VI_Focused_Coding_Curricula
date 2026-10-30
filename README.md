# Accessible Introduction to Computer Science

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
![GitHub top language](https://img.shields.io/github/languages/top/mrhunsaker/VI_Focused_Coding_Curricula)
[![Documentation](https://img.shields.io/badge/docs-mdBook-blue)](https://mrhunsaker.github.io/VI_Focused_Coding_Curricula/)
[![Last commit](https://img.shields.io/github/last-commit/mrhunsaker/VI_Focused_Coding_Curricula)](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/commits/main)
![GitHub Release](https://img.shields.io/github/v/release/mrhunsaker/VI_Focused_Coding_Curricula)
[![Contributors](https://img.shields.io/github/contributors/mrhunsaker/VI_Focused_Coding_Curricula)](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/graphs/contributors)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Build and deploy mdBook](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/workflows/mdbook.yml/badge.svg)](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/workflows/mdbook.yml)

An accessibility-first, open educational resource for learning introductory computer science through **Python, JavaScript, TypeScript, and Java**. It is designed especially for learners who are blind or visually impaired and use screen readers, while remaining useful to anyone who prefers keyboard-first, text-based instruction.

**Read the living textbook:** [https://mrhunsaker.github.io/VI_Focused_Coding_Curricula/](https://mrhunsaker.github.io/VI_Focused_Coding_Curricula/)

## What this project is

This repository is a **living textbook published with mdBook**. It is intentionally an **mdBook project, not a GitBook project**. mdBook turns the repository's Markdown lessons into a structured, navigable book and static website. GitHub Actions builds the book and publishes it to GitHub Pages.

The textbook is intended to evolve continuously. Explanations, examples, exercises, accessibility guidance, references, and learning paths can be corrected and extended over time. The Markdown files and configuration in this repository are the source of truth; the published site is the rendered reading experience. Contributions should improve the source materials and their accessibility, not edit generated website output.

## Student reference tools

Each language curriculum has a topic index mapping terms, APIs, setup tasks, and concepts to the lessons where they are taught. The shared [Programming Code Glossary](backmatter/GLOSSARY.md) provides explicit definitions organized by language, with cross-language distinctions. These references are intended for use throughout the course.

## Purpose and principles

- **Accessible by design:** prioritize screen-reader compatibility, semantic structure, descriptive links, keyboard operation, and text-based workflows.
- **Teach transferable computer science:** introduce core programming concepts through four widely used languages.
- **Practice-first learning:** support concepts with runnable examples, guided exercises, projects, and capstone work.
- **Keep it living:** welcome corrections, clearer explanations, new examples, improved exercises, and updates as tools and language ecosystems change.
- **Build in the open:** invite learners, educators, developers, and accessibility practitioners to participate.
- **Support independence:** do not make visual inspection, mouse-only interaction, or graphical output a requirement for core learning activities.

## Intended audience

The primary audience is beginning programmers, including students who are blind or visually impaired and use screen readers such as NVDA, JAWS, VoiceOver, or Narrator. Educators adapting introductory computer science instruction and self-directed learners may also use the material.

The lessons emphasize keyboard-first development, accessible editor and terminal workflows, text output, explicit instructions, and interpreting error messages. Accessibility support varies across operating systems, editor versions, screen readers, and language tooling; consult the relevant tool documentation when your environment differs from the examples.

## What's in the textbook

The current book includes an overview and four language curricula, organized into 19 unit documents, plus an optional post-capstone Kotlin supplement for Java learners.

| Curriculum | Coverage |
| --- | --- |
| [Python](PYTHON/PYTHON_README.md) | Accessible setup; computing foundations; numeric programs; control flow; data structures; input and functions; object-oriented programming; files, exceptions, and testing; projects and capstone |
| [JavaScript](JAVASCRIPT/JAVASCRIPT_README.md) | Setup and foundations; numbers and input; control flow; arrays and objects; functions; classes; files and errors; modules, collections, testing, projects, and capstone |
| [TypeScript](TYPESCRIPT/TYPESCRIPT_README.md) | Node.js and TypeScript setup; type annotations and inference; input; control flow; data structures; functions; classes; files; modules; collections; testing; projects and capstone |
| [Java](JAVA/JAVA_README.md) | Setup and foundations; numeric programs; control flow; arrays and collections; input and strings; methods; object-oriented programming; files and exceptions; projects and capstone |

Start with the [curriculum overview](OVERALL_README.md), then choose a language:

- [Python curriculum and units](PYTHON/PYTHON_README.md)
- [JavaScript curriculum and units](JAVASCRIPT/JAVASCRIPT_README.md)
- [TypeScript curriculum and units](TYPESCRIPT/TYPESCRIPT_README.md)
- [Java curriculum and units](JAVA/JAVA_README.md)
- [Optional Kotlin post-capstone supplement](JAVA/kotlin.md)

The [mdBook table of contents](SUMMARY.md) defines the published book's navigation.

## Accessibility approach

The curricula share these practical principles:

1. Use editor accessibility features such as Visual Studio Code's Screen Reader Optimized Mode where available.
2. Prefer keyboard navigation and document relevant commands where they are part of a lesson.
3. Explain indentation, braces, punctuation, and other code structure that assistive technologies may announce differently.
4. Keep core exercises runnable in a terminal and make program output text-based.
5. Use descriptive headings, ordered steps, meaningful link labels, and properly fenced code blocks.
6. Treat debugging and reading error messages as teachable skills; do not rely on screenshots or color alone to convey essential information.

Accessibility is an ongoing quality goal, not a claim that every page or third-party tool is fully accessible. Report barriers, confusing instructions, or screen-reader-specific issues through [GitHub Issues](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/issues).

## Technology and local development

- **Book engine:** [mdBook](https://rust-lang.github.io/mdBook/)
- **Content:** Markdown files in this repository
- **Hosting:** GitHub Pages
- **Automation:** GitHub Actions
- **Curriculum languages:** Python, JavaScript (Node.js), TypeScript (compiled to JavaScript and run with Node.js), and Java

To build locally:

1. Install mdBook using the [official installation instructions](https://rust-lang.github.io/mdBook/guide/installation.html).
2. Clone this repository.
3. From the repository root, run:

```sh
mdbook build
```

**Windows PowerShell (Windows 11):**

```powershell
mdbook build
```

4. Open `book/index.html` in a browser, or run `mdbook serve` and open the local address printed by mdBook.

The generated `book/` directory is build output and is intentionally ignored by Git. Edit the Markdown source, `SUMMARY.md`, or `book.toml`, then rebuild. Pushes to `main` trigger the workflow that builds and deploys the site.

## Contribute to the living textbook

Contributions are welcome. You do not need to be an expert in all four curricula. A focused correction to one explanation, a reproducible example, a screen-reader usability report, or a better exercise can make the book more useful.

- **Discussions:** ask questions, propose ideas, compare learning approaches, and discuss the textbook's direction in [GitHub Discussions](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/discussions).
- **Issues:** report errors, broken links, outdated setup instructions, unclear explanations, missing topics, or accessibility barriers in [GitHub Issues](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/issues).
- **Pull requests:** submit focused improvements to Markdown, navigation, documentation, or the build workflow through [Pull Requests](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/pulls).

Read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_STYLE.md](CODE_STYLE.md), and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing. Report security concerns using the private process in [SECURITY.md](SECURITY.md).

## Project structure

```text
.
├── OVERALL_README.md       # Curriculum overview included in the mdBook
├── SUMMARY.md              # mdBook table of contents
├── book.toml               # mdBook configuration
├── PYTHON/                 # Python curriculum and units
├── JAVASCRIPT/             # JavaScript curriculum and units
├── JAVA/                   # Java curriculum, units, and Kotlin supplement
├── TYPESCRIPT/             # TypeScript curriculum and units
├── .github/workflows/      # mdBook build and GitHub Pages deployment
├── CHANGES.md              # Project change log
├── CONTRIBUTING.md         # Contribution process
├── CODE_STYLE.md           # Editorial and code-example conventions
├── CODE_OF_CONDUCT.md      # Community standards
├── SECURITY.md             # Security reporting policy
└── LICENSE                 # Apache License 2.0
```

`cs_curriculum_final/` is a reference-only directory from the original conversion work. It is not part of the published book and must not be modified during routine curriculum contributions.

## Project policies

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contribution Guide](CONTRIBUTING.md)
- [Code and Editorial Style](CODE_STYLE.md)
- [Security Policy](SECURITY.md)
- [Apache License 2.0](LICENSE)

## Acknowledgments and learning references

The curriculum overview identifies source texts and documentation that informed the materials, including Python programming texts, *Introduction to Programming Using Java*, and MDN Web Docs. See [OVERALL_README.md](OVERALL_README.md) and each language landing page for curriculum-specific references. Preserve appropriate attribution when improving or extending material.

---

This is an open, evolving textbook. If you find it useful, help make the next version clearer, more accessible, and more complete.
