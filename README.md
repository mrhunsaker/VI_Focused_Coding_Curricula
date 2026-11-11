# Accessible Introduction to Computer Science

[![License](https://img.shields.io/badge/LICENSE-CC0%201.0-blue.svg?)](LICENSE)
![GitHub top language](https://img.shields.io/github/languages/top/mrhunsaker/VI_Focused_Coding_Curricula)
[![Documentation](https://img.shields.io/badge/docs-mdBook-blue)](https://mrhunsaker.github.io/VI_Focused_Coding_Curricula/)
[![Last commit](https://img.shields.io/github/last-commit/mrhunsaker/VI_Focused_Coding_Curricula)](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/commits/main)
![GitHub Release](https://img.shields.io/github/v/release/mrhunsaker/VI_Focused_Coding_Curricula)
[![Contributors](https://img.shields.io/github/contributors/mrhunsaker/VI_Focused_Coding_Curricula/graphs/contributors)](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/graphs/contributors)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Build and deploy mdBook](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/workflows/mdbook.yml/badge.svg)](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/workflows/mdbook.yml)

An accessibility-first, open educational resource for learning computer science and software development. The repository brings together **13 language curricula**, focused modules in **Git, HTML/CSS, Markdown, R, regular expressions, SQL, structured data formats, and web accessibility**, and prerequisite **Bash and PowerShell** terminal tracks. It is designed especially for learners who are blind or visually impaired and use screen readers, while remaining useful to anyone who prefers keyboard-first, text-based instruction.

**Read the living textbook:** [https://mrhunsaker.github.io/VI_Focused_Coding_Curricula/](https://mrhunsaker.github.io/VI_Focused_Coding_Curricula/)

## What this project is

This repository is a **living textbook published with mdBook**. It is intentionally an **mdBook project, not a GitBook project**. mdBook turns the repository's Markdown lessons into a structured, navigable book and static website. GitHub Actions builds the book and publishes it to GitHub Pages.

The Markdown files and configuration in this repository are the maintained source of truth. The textbook is intended to evolve continuously as explanations, examples, exercises, accessibility guidance, references, and learning pathways are reviewed and improved. Contributions should improve the source materials and their accessibility, not edit generated website output.

## Purpose and principles

- **Accessible by design:** prioritize screen-reader compatibility, semantic structure, descriptive links, keyboard operation, and text-based workflows.
- **Teach transferable computer science:** explain programming, data, algorithms, software design, development tools, testing, and debugging through languages used in different technical domains.
- **Practice-first learning:** support concepts with runnable examples, guided exercises, projects, and capstone work.
- **Keep it living:** welcome corrections, clearer explanations, new examples, improved exercises, and updates as tools and language ecosystems change.
- **Build in the open:** invite learners, educators, developers, and accessibility practitioners to participate.
- **Support independence:** do not make visual inspection, mouse-only interaction, or graphical output a requirement for core learning activities.

## Intended audience

The primary audience includes learners who are blind or visually impaired and use screen readers such as NVDA, JAWS, VoiceOver, or Narrator. Educators adapting computer science instruction and self-directed learners may also use the material. The curriculum assumes no previous programming experience for its introductory learning paths, while its broader language coverage also supports learners pursuing particular technical interests.

The lessons emphasize keyboard-first development, accessible editor and terminal workflows, text output, explicit instructions, and interpreting error messages. Visual Studio Code is the primary editor in many examples; [Theia IDE](https://theia-ide.org/#theiaide) is another option. Project-defined development containers are emphasized where a consistent compiler, runtime, linter, formatter, and test toolchain is required. The IDE guide also discusses JetBrains products, Databricks, and other specialist environments by their professional roles; it does not provide setup instructions for those products.

Accessibility support varies across operating systems, editor versions, screen readers, and language tooling. Consult the relevant tool documentation and validate workflows in the learner's actual environment.

## Curriculum scope

The textbook is organized into three complementary kinds of learning material:

1. **Full language curricula:** structured courses with language-specific lesson sequences, examples, indexes, and supporting materials.
2. **Focused technology modules:** targeted introductions to version control, web structure and styling, technical documentation, statistical computing, pattern-based text processing, relational databases, structured data formats, and web accessibility.
3. **Shared prerequisites and development practices:** computing foundations, terminal skills, editors, project environments, containers, and cross-language workflow.

### Full language curricula

| Language | Primary usage and domain | Representative software, platforms, or projects associated with it |
| --- | --- | --- |
| [Python](PYTHON/PYTHON_README.md) | Automation, scripting, web services, scientific computing, data analysis, and machine learning | Django and Flask services; scientific and data ecosystems such as NumPy, pandas, and PyTorch; automation tools |
| [JavaScript](JAVASCRIPT/JAVASCRIPT_README.md) | Browser-based interaction, web applications, server-side JavaScript, and developer tooling | Node.js, React-based applications, browser applications, and tools such as ESLint |
| [TypeScript](TYPESCRIPT/TYPESCRIPT_README.md) | Statically checked application development across large JavaScript codebases, web front ends, and server applications | Visual Studio Code, Angular applications, and TypeScript-based Node.js services |
| [Java](JAVA/JAVA_README.md) | Enterprise services, large application systems, backend platforms, and Android ecosystem development | Minecraft: Java Edition, Elasticsearch, and many Spring-based enterprise services |
| [Kotlin](KOTLIN/KOTLIN_README.md) | Android application development, JVM services, and multiplatform application development | Android applications, Gradle build tooling, and Kotlin-based server services |
| [C](C/c_README.md) | Operating systems, embedded systems, systems interfaces, and performance-sensitive libraries | Linux kernel components, CPython implementation components, and embedded firmware |
| [C++](CPP/cpp_README.md) | Game engines, graphics, browsers, desktop software, and performance-intensive systems | Unreal Engine, Chromium components, and major desktop or graphics applications |
| [C#](CSHARP/csharp_README.md) | .NET business applications, cloud services, desktop software, and game development | Unity projects, ASP.NET Core services, and .NET desktop applications |
| [Julia](JULIA/julia_README.md) | Numerical computing, scientific simulation, optimization, and technical research | Julia scientific-computing packages and SciML ecosystem projects |
| [Swift](SWIFT/swift_README.md) | Apple-platform applications and systems programming | iOS, iPadOS, macOS, watchOS, and tvOS applications |
| [Rust](RUST/rust_README.md) | Systems software, command-line tools, infrastructure, and performance-sensitive services | ripgrep, parts of Firefox, and infrastructure tooling |
| [Go](GO/GO_README.md) | Cloud infrastructure, network services, command-line tools, and concurrent backend systems | Docker, Kubernetes, and Prometheus |
| [Lua](LUA/LUA_README.md) | Embedded scripting, game logic, configuration, and extensible applications | Roblox experiences, Neovim configuration, and applications embedding Lua |

These examples illustrate common uses and notable projects; they do not imply that an entire product is written in one language. Production systems routinely combine languages and technologies.

### Focused technology modules

| Technology | Primary usage and role | Representative software or platforms |
| --- | --- | --- |
| [Git](MODULES/GIT.md) | Distributed version control: commits, branches, merges, remotes, and pull-request collaboration | Git, GitHub, GitLab, and the GitHub CLI (`gh`) |
| [HTML and CSS](MODULES/HTML_CSS.md) | HTML structures web content; CSS controls presentation, layout, and responsive styling. They are foundational web technologies rather than general-purpose programming languages. | Websites, web applications, browser interfaces, and design systems |
| [Markdown](MODULES/MARKDOWN.md) | Lightweight plain-text markup for documentation, README files, and technical notes | GitHub documentation, static site generators, and Pandoc |
| [R](MODULES/R.md) | Statistical analysis, data visualization, research computing, and reproducible reports | RStudio/Posit, the tidyverse, and Bioconductor |
| [Regular expressions](MODULES/REGEX.md) | Pattern-based finding, extracting, validating, and replacing of text | `grep`, `sed`, ripgrep, and regex support in every mainstream language |
| [SQL](MODULES/SQL.md) | Declarative querying, defining, and managing relational data | PostgreSQL, SQLite, MySQL, SQL Server, and applications backed by relational databases |
| [Structured data formats](MODULES/STRUCTURED_DATA.md) | JSON for data interchange, YAML for configuration, and TOML for application settings | APIs, GitHub Actions, Kubernetes, `pyproject.toml`, and `Cargo.toml` |
| [Web accessibility](MODULES/WEB_ACCESSIBILITY.md) | Building websites and applications usable with screen readers, keyboard-only interaction, and other access technologies | WCAG, ARIA, NVDA, VoiceOver, JAWS, and axe DevTools |

### Terminal and shared development foundations

| Material | Role |
| --- | --- |
| [Computing foundations](FOUNDATIONS/FOUNDATIONS_README.md) | Concepts and vocabulary that apply across languages and tools |
| [Bash track](TERMINAL/bash.md) | Shell commands and scripting workflows commonly used on macOS and Linux |
| [PowerShell track](TERMINAL/powershell.md) | Cross-platform and Windows administration and development workflows |
| [IDE and editor guide](DEVELOPMENT/IDE_SETUP.md) | VS Code and Theia workflows, plus professional IDE and data-platform context |
| [Environment isolation guide](DEVELOPMENT/ENVIRONMENT_ISOLATION.md) | Project dependencies, reproducibility, development containers, Docker, and Podman |

Bash and PowerShell are shell languages used to operate systems and automate workflows. They are taught as shared prerequisites because learners need to navigate projects, run tools, inspect files, and interpret command output across the language curricula.

## How to use the curriculum

Start with the [curriculum overview](OVERALL_README.md), complete the [terminal prerequisite](TERMINAL/TERMINAL_README.md), and review the computing foundations. Then select a language or focused module according to the work you want to understand. The curricula are not a ranking and are not intended to be completed all at once. A learner should select a relevant path, build a solid working understanding, and then compare concepts across other languages as useful.

Examples of choosing by intended use:

- **Automation, data work, or machine learning:** Python; add R for statistical analysis or Julia for numerical and scientific computing.
- **Web application development:** JavaScript and TypeScript, alongside the HTML/CSS and web accessibility modules, and SQL when persistent relational data is needed.
- **Enterprise and JVM applications:** Java or Kotlin.
- **Android and Apple platforms:** Kotlin for Android-focused development; Swift for Apple-platform development.
- **Operating systems, embedded devices, and systems software:** C, C++, or Rust, depending on ecosystem, constraints, and safety requirements.
- **Cloud services and infrastructure tooling:** Go, Java, Python, Rust, or C# depending on the platform and system requirements.
- **Game development and embedded application scripting:** C++, C#, and Lua have distinct roles across engines, application code, and scripting.
- **Relational data:** SQL is a focused companion to application languages rather than a replacement for them.
- **Professional workflow skills:** the Git, Markdown, regular expressions, and structured data formats modules support every other path in the textbook.

These are orientation points, not exclusive boundaries. Language selection should reflect the problem domain, deployment target, existing codebase, team expertise, performance and safety requirements, and available libraries.

## Student reference tools

Each language curriculum includes a topic index mapping terms, APIs, setup tasks, and concepts to the lessons where they are taught. Each language and focused-module introduction also provides a curated bibliography of introductory books, with notes on edition, prerequisites, and version differences where relevant. The Foundations introduction and Bash/PowerShell tracks include their own reading recommendations. The shared [Programming Code Glossary](backmatter/GLOSSARY.md) defines common and language-specific terminology. The [mdBook table of contents](SUMMARY.md) is the authoritative navigation for the published textbook.

## Accessibility approach

The curricula share these practical principles:

1. Use editor accessibility features such as Visual Studio Code's Screen Reader Optimized Mode or corresponding accessibility settings in Theia IDE where available.
2. Prefer keyboard navigation and document relevant commands where they are part of a lesson.
3. Explain indentation, braces, punctuation, and other code structure that assistive technologies may announce differently.
4. Keep core exercises runnable in a terminal and make program output text-based wherever practical.
5. Use descriptive headings, ordered steps, meaningful link labels, and properly fenced code blocks.
6. Treat debugging and reading error messages as teachable skills; do not rely on screenshots or color alone to convey essential information.

Accessibility is an ongoing quality goal, not a claim that every page or third-party tool is fully accessible. Report barriers, confusing instructions, or screen-reader-specific issues through [GitHub Issues](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/issues).

## Technology and local development

- **Book engine:** [mdBook](https://rust-lang.github.io/mdBook/)
- **Content:** Markdown files in this repository
- **Hosting:** GitHub Pages
- **Automation:** GitHub Actions
- **Curriculum:** 13 full language curricula, focused Git, HTML/CSS, Markdown, R, regular expressions, SQL, structured data, and web accessibility modules, and Bash/PowerShell terminal tracks

To build locally:

1. Install mdBook using the [official installation instructions](https://rust-lang.github.io/mdBook/guide/installation.html).
2. Clone this repository.
3. From the repository root, run:

```sh
mdbook build
```

On Windows PowerShell, the command is the same:

```powershell
mdbook build
```

4. Open `book/index.html` in a browser, or run `mdbook serve` and open the local address printed by mdBook.

The generated `book/` directory is build output and is intentionally ignored by Git. Edit the Markdown source, `SUMMARY.md`, or `book.toml`, then rebuild. Pushes to `main` trigger the workflow that builds and deploys the site.

## Contribute to the living textbook

Contributions are welcome. You do not need to work across every language or technology. A focused correction to one explanation, a reproducible example, a screen-reader usability report, or a better exercise can make the book more useful.

- **Discussions:** ask questions, propose ideas, compare learning approaches, and discuss the textbook's direction in [GitHub Discussions](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/discussions).
- **Issues:** report errors, broken links, outdated setup instructions, unclear explanations, missing topics, or accessibility barriers in [GitHub Issues](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/issues).
- **Pull requests:** submit focused improvements to Markdown, navigation, documentation, or the build workflow through [Pull Requests](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/pulls).

Read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_STYLE.md](CODE_STYLE.md), and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing. Report security concerns using the private process in [SECURITY.md](SECURITY.md).

## Project structure

```text
.
├── OVERALL_README.md       # Curriculum overview included in the mdBook
├── SUMMARY.md              # Complete mdBook table of contents
├── book.toml               # mdBook configuration
├── FOUNDATIONS/            # Shared computing foundations
├── TERMINAL/               # Bash and PowerShell prerequisite tracks
├── DEVELOPMENT/            # IDE, project environments, containers, and audits
├── PYTHON/                 # Python curriculum
├── JAVASCRIPT/             # JavaScript curriculum
├── TYPESCRIPT/             # TypeScript curriculum
├── JAVA/                   # Java curriculum
├── KOTLIN/                 # Kotlin curriculum
├── C/                      # C curriculum
├── CPP/                    # C++ curriculum
├── CSHARP/                 # C# curriculum
├── JULIA/                  # Julia curriculum
├── SWIFT/                  # Swift curriculum
├── RUST/                   # Rust curriculum
├── GO/                     # Go curriculum
├── LUA/                    # Lua curriculum
├── MODULES/                # Git, HTML/CSS, Markdown, R, regex, SQL, structured data, and web accessibility modules
├── backmatter/             # Glossary, indexes, and teacher resources
├── .github/workflows/      # mdBook build and GitHub Pages deployment
├── CHANGES.md              # Project change log
├── CONTRIBUTING.md         # Contribution process
├── CODE_STYLE.md           # Editorial and code-example conventions
├── CODE_OF_CONDUCT.md      # Community standards
├── SECURITY.md             # Security reporting policy
└── LICENSE                 # Project license
```

`cs_curriculum_final/` is a reference-only directory from the original conversion work. It is not part of the published book and must not be modified during routine curriculum contributions.

## Project policies

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contribution Guide](CONTRIBUTING.md)
- [Code and Editorial Style](CODE_STYLE.md)
- [Security Policy](SECURITY.md)
- [Project License](LICENSE)

## Acknowledgments and learning references

The curriculum overview and individual language pages identify source texts and official documentation that inform the materials. Preserve appropriate attribution when improving or extending material.

---

This is an open, evolving textbook. Contributions can improve any language path, focused module, shared prerequisite, or accessibility practice.
