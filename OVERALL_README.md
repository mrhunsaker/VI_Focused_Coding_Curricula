# Accessible Introduction to Computer Science

## A living, accessibility-first textbook across programming languages and software domains

This book is a structured introduction to computer science and software development. It is designed with blind and visually impaired learners who use screen readers, braille displays, magnification, keyboard navigation, or combinations of access technologies in mind. It is also intended for sighted learners, educators, and anyone who benefits from explicit, text-first instruction.

The repository contains 13 full language curricula, focused modules in HTML/CSS, R, and SQL, and shared Bash and PowerShell terminal tracks. The languages are presented by their common technical uses and ecosystems, not as a hierarchy. No single language is the best choice for every problem.

The textbook is published with **mdBook**. Markdown files in this repository are the maintained source; mdBook builds them into the navigable online textbook hosted on GitHub Pages. The book is intended to remain a living resource: lessons, examples, exercises, accessibility notes, and teaching materials can be reviewed and improved as learners and educators use them.

**Start learning:** complete the shared prerequisites, then choose a language curriculum or focused module that aligns with your goals. Each language curriculum includes its own topic index. The shared [Programming Code Glossary](backmatter/GLOSSARY.md) defines common and language-specific terminology.

## Complete the shared prerequisites

### Terminal skills

Before beginning a language curriculum, complete the [Terminal Skills prerequisite](TERMINAL/TERMINAL_README.md). Choose the [Bash track for macOS and Linux](TERMINAL/bash.md) or the [PowerShell track for Windows](TERMINAL/powershell.md). Both tracks teach equivalent foundational workflows using native commands: navigating directories, managing files, reading and searching text, running programs, interpreting errors, and working safely from a project folder. These skills support every language and toolchain in the book.

### Computing foundations

Read the [Foundations overview](FOUNDATIONS/FOUNDATIONS_README.md) and [Computing Foundations Primer](FOUNDATIONS/unit-p-computing-foundations.md). These materials introduce concepts and vocabulary that apply across programming languages, operating systems, and development tools.

### Development environments

Review the [IDE and editor guide](DEVELOPMENT/IDE_SETUP.md) and [Environment Isolation guide](DEVELOPMENT/ENVIRONMENT_ISOLATION.md). Visual Studio Code and Theia IDE are the primary editor options discussed for the course. The materials also describe professional IDEs and data platforms—including JetBrains products and Databricks—by their typical roles and use cases, without providing setup procedures for those products.

Project-defined **development containers** receive particular emphasis when a course requires a consistent compiler, runtime, linter, formatter, test runner, or supporting service. The guides explain the relationship between development containers, Docker, and Podman and how project-level environments support reproducible learning and assessment.

## Purpose and learning philosophy

The goal is not simply to teach syntax. Learners should develop the habits used to solve problems with computers: clarify requirements, decompose a task, represent information, design an algorithm, implement it, test it, interpret errors, revise the solution, and explain their decisions.

The curricula share these commitments:

- **Accessibility is part of the design.** Core activities use text-based input and output and can be completed through keyboard-accessible tools. Lessons explain code structure and navigation rather than depending on visual scanning.
- **Concepts precede tools.** Editors, terminals, runtimes, compilers, interpreters, and libraries are instruments for learning computer science.
- **Practice is central.** Short experiments, guided exercises, debugging, and projects provide repeated opportunities to apply concepts.
- **Understanding matters more than typing speed.** Learners reason about programs, predict behavior, test assumptions, and explain their decisions.
- **Errors are part of learning.** Reading diagnostics and correcting a program are core skills.
- **The resource evolves.** Corrections, new examples, and accessibility improvements are welcome through GitHub Discussions, Issues, and Pull Requests.

## Who should use this book?

The primary audience includes learners who are blind or visually impaired. It may be used in secondary or postsecondary courses, accessible technology programs, tutoring, independent study, or educator professional development.

No previous programming experience is required for the introductory learning paths. Learners should have, or be developing, basic keyboard and screen-reader or braille-display navigation skills. A teacher can introduce programming and assistive-technology workflows together; lack of advanced screen-reader fluency should not be mistaken for lack of programming ability.

The material is also useful to sighted learners because it emphasizes precise language, semantic structure, explicit feedback, and reproducible text-based workflows.

## What learners will develop

By working through a selected curriculum, learners should build the ability to:

1. Describe what a computer program is and explain a basic software-development cycle.
2. Use a language runtime, compiler, editor, terminal, and project environment appropriate to the selected technology.
3. Read code structurally, including identifiers, operators, delimiters, indentation, braces, and nested blocks.
4. Store, convert, compare, and process values using appropriate data types.
5. Use expressions, input, output, decisions, and repetition to solve problems.
6. Organize related values in collections and select suitable data structures.
7. Decompose programs into functions, methods, modules, or components with clear responsibilities.
8. Work with files, exceptions, structured data, and external libraries where relevant.
9. Understand classes, objects, interfaces, memory, concurrency, or other paradigms where the selected language requires them.
10. Test behavior, diagnose errors, refine a solution, and communicate how it works.
11. Build text-based applications or domain-appropriate projects and complete the projects specified by the selected path.
12. Evaluate whether program interaction, prompts, messages, and output are understandable through assistive technology.

Outcomes vary by curriculum and module. These are learning goals, not a claim of professional mastery.

## Choose a curriculum by primary use

The following descriptions identify common domains and representative software or projects associated with each language. Examples illustrate ecosystem usage; they do not mean that a complete product is written exclusively in that language.

### Full language curricula

| Language and curriculum | Primary usage | Representative software, platforms, or projects |
| --- | --- | --- |
| [Python](PYTHON/PYTHON_README.md) | Automation, scripting, web services, scientific computing, data analysis, and machine learning | Django and Flask services; NumPy, pandas, and PyTorch ecosystems |
| [JavaScript](JAVASCRIPT/JAVASCRIPT_README.md) | Browser interaction, web applications, server-side JavaScript, and developer tooling | Node.js, React-based applications, browser applications, ESLint |
| [TypeScript](TYPESCRIPT/TYPESCRIPT_README.md) | Statically checked web and server applications, especially large JavaScript codebases | Visual Studio Code, Angular applications, TypeScript-based Node.js services |
| [Java](JAVA/JAVA_README.md) | Enterprise services, large application systems, backend platforms, and JVM software | Minecraft: Java Edition, Elasticsearch, Spring-based services |
| [Kotlin](KOTLIN/KOTLIN_README.md) | Android applications, JVM services, and multiplatform development | Android applications, Gradle build tooling, Kotlin server services |
| [C](C/c_README.md) | Operating systems, embedded systems, low-level interfaces, and performance-sensitive libraries | Linux kernel components, CPython implementation components, embedded firmware |
| [C++](CPP/cpp_README.md) | Game engines, graphics, browsers, desktop software, and performance-intensive systems | Unreal Engine, Chromium components, graphics and desktop applications |
| [C#](CSHARP/csharp_README.md) | .NET business applications, cloud services, desktop software, and game development | Unity projects, ASP.NET Core services, .NET desktop applications |
| [Julia](JULIA/julia_README.md) | Numerical computing, scientific simulation, optimization, and technical research | Julia scientific-computing packages and SciML ecosystem projects |
| [Swift](SWIFT/swift_README.md) | Apple-platform application development and systems programming | iOS, iPadOS, macOS, watchOS, and tvOS applications |
| [Rust](RUST/rust_README.md) | Systems software, command-line tools, infrastructure, and performance-sensitive services | ripgrep, parts of Firefox, infrastructure tooling |
| [Go](GO/GO_README.md) | Cloud infrastructure, network services, command-line tools, and concurrent backend systems | Docker, Kubernetes, Prometheus |
| [Lua](LUA/LUA_README.md) | Embedded scripting, game logic, configuration, and extensible applications | Roblox experiences, Neovim configuration, applications embedding Lua |

### Focused technology modules

Some important technologies are not general-purpose programming languages. They have distinct roles and are included as focused modules:

| Module | Primary usage and role | Representative software or platforms |
| --- | --- | --- |
| [HTML and CSS](MODULES/HTML_CSS.md) | HTML structures web content; CSS controls presentation, layout, and responsive styling | Websites, browser interfaces, web applications, design systems |
| [R](MODULES/R.md) | Statistical analysis, data visualization, research computing, and reproducible reports | RStudio/Posit, tidyverse, Bioconductor |
| [SQL](MODULES/SQL.md) | Declarative querying, defining, and managing relational data | PostgreSQL, SQLite, MySQL, SQL Server |

HTML is a markup language and CSS is a style-sheet language; together they form the structure and presentation layer of the web. SQL is a declarative query language for relational data. R is a programming language used extensively in statistics and data analysis.

### Shared terminal tracks

[Bash](TERMINAL/bash.md) and [PowerShell](TERMINAL/powershell.md) are shell languages. They support command execution, file and process management, automation, and development workflows. Bash is common on macOS and Linux; PowerShell is central to Windows administration and is also available cross-platform. Both are shared prerequisites rather than alternatives to the application languages above.

## Selecting a pathway

Choose a path according to the problem domain, deployment target, ecosystem, and learning objectives:

- **Automation, data analysis, and machine learning:** Python; consider R for statistical analysis and Julia for numerical or scientific computing.
- **Web application development:** JavaScript and TypeScript, alongside HTML/CSS; add SQL when the application stores relational data.
- **Enterprise and JVM applications:** Java or Kotlin.
- **Android and Apple platforms:** Kotlin is widely used for Android development; Swift is the primary language for modern native Apple-platform development.
- **Operating systems, embedded devices, and systems software:** C, C++, or Rust, depending on hardware, ecosystem, performance, and safety requirements.
- **Cloud services and infrastructure tooling:** Go, Java, Python, Rust, or C# depending on platform and system requirements.
- **Game development and application scripting:** C++, C#, and Lua have distinct roles across engines, application logic, and embedded scripting.
- **Relational data systems:** SQL is a companion to application languages, not a replacement for them.

These categories overlap. A real product may use several languages, and a language may serve multiple domains. Selection should reflect the problem being solved, the existing codebase, team expertise, operational constraints, and available libraries.

## How the curriculum is organized

The [mdBook table of contents](SUMMARY.md) is the authoritative navigation for the published book. The repository is grouped by shared foundations, language curricula, focused modules, development guidance, and backmatter.

| Area | Contents |
| --- | --- |
| Shared foundations | Computing foundations and terminal skills in Bash and PowerShell |
| Development guidance | IDE and editor roles, project dependency management, environment isolation, development containers, Docker, and Podman |
| Full language curricula | Python, JavaScript, TypeScript, Java, Kotlin, C, C++, C#, Julia, Swift, Rust, Go, and Lua |
| Focused modules | HTML/CSS, R, and SQL |
| Backmatter | Teacher resources, programming glossary, topic indexes, validation records, and other references |

Each full language curriculum has its own landing page and supporting lesson materials. Depending on the language, it may also include a topic index, teacher's guide, standardization audit, or validation record. The focused modules provide a narrower introduction to a particular technology. Follow the sequence and scope documented on the corresponding landing page and in the [table of contents](SUMMARY.md).

## A practical study routine

1. **Preview:** read the lesson title, objectives or overview, vocabulary, and prerequisites.
2. **Understand:** read the explanation and trace each example. Identify what each statement contributes.
3. **Predict:** state what you expect the program to do before running it.
4. **Run:** execute the example and inspect its text output.
5. **Experiment:** change one input, value, or statement at a time.
6. **Practice:** complete the activities without copying a finished solution.
7. **Debug:** read the diagnostic, locate the relevant code, form a hypothesis, and test a correction.
8. **Explain:** describe the algorithm and the role of important variables, conditions, loops, functions, methods, modules, or objects.
9. **Review:** revisit the skills checklist and record concepts that need more practice.

Keep a learning journal or portfolio. Include the problem statement, approach, sample input and output, errors encountered, and what changed.

## Accessibility and technology

### Recommended editor and development workflow

Visual Studio Code is the primary editor in the setup material. [Theia IDE](https://theia-ide.org/#theiaide) is another option for keyboard-first development. The [IDE guide](DEVELOPMENT/IDE_SETUP.md) also describes the roles of JetBrains IDEs, Databricks, and other professional tools without giving setup instructions for them.

For projects that require compilers, linters, formatters, test runners, and supporting services, the course emphasizes repository-defined **development containers**. A containerized project environment can make the toolchain more consistent across learner computers and CI. The [environment guide](DEVELOPMENT/ENVIRONMENT_ISOLATION.md) explains the Dev Container model and the roles of Docker and Podman.

Access configurations vary by operating system, screen reader, braille display, editor version, and individual preference. Treat shortcuts and settings in the lessons as starting points; verify them in the learner's environment.

### Dependency and environment management

Use the project-native dependency and build tools documented by each language curriculum. Examples include uv and Python project environments, npm for JavaScript and TypeScript, Maven or Gradle wrappers for JVM projects, and the relevant package and build tools for C, C++, C#, Julia, Swift, Rust, Go, and Lua. Keep dependencies project-scoped where possible, commit lockfiles when the ecosystem supports them, and use the repository's documented commands rather than relying on undocumented global tools.

A development container can complement these tools; it does not replace language package managers, lockfiles, or build systems. The project should document both the container environment and the commands used to build, lint, test, and run its code.

### Shared accessibility practices

- Use semantic headings, descriptive link text, ordered procedures, and code fences with language identifiers.
- Enable editor screen-reader support where available and learn navigation by line, word, symbol, file, and diagnostic.
- Configure speech or braille output for punctuation, indentation, line numbers, and code symbols according to learner preference.
- Use a terminal or REPL to run examples and inspect text output.
- Keep examples and output understandable when read sequentially. Label collections, menu options, and results.
- Avoid relying on syntax highlighting, color, spatial placement, diagrams, or screenshots to communicate essential information.
- Provide a text description or equivalent activity when a visual resource is included.
- Allow time for navigation and tool interaction; assess programming reasoning separately from assistive-technology speed.
- Ask learners which tools and interaction patterns work for them. Do not infer needs from a diagnosis.

A text-only interface is not automatically accessible. Output order, verbosity, prompts, error handling, keyboard operation, and documentation structure all affect usability. Test activities with the actual access technology where possible and revise barriers as they are identified.

## Assessment and evidence of learning

Use varied evidence rather than relying only on timed code production:

- Explain a program or algorithm in the learner's own words.
- Predict output before execution and explain any difference.
- Complete a program or technical task from a clear specification.
- Find and fix a deliberately introduced bug.
- Write tests or identify useful test cases.
- Refactor a program into clearer functions, methods, modules, or data structures.
- Demonstrate keyboard and assistive-technology workflows used to create, run, and debug the work.
- Maintain a portfolio with incremental versions and reflections.

Assess correctness, reasoning, testing, clarity, independence, and progress. Provide reasonable accommodations without lowering the underlying learning objective.

## Using AI tools thoughtfully

AI-assisted coding tools may help explain unfamiliar concepts, interpret diagnostics, propose test cases, or provide alternative explanations. They can also produce incorrect, insecure, inaccessible, outdated, or overly complicated code. AI output is not evidence that a learner understands a topic.

Follow the instructor's policy for each activity and assessment. Disclose assistance when required; never submit generated code that the learner cannot explain, test, and modify. Do not share personal, educational-record, credential, or confidential information with public AI systems. Review generated code for correctness, dependencies, security, licensing, and screen-reader usability. Keep a non-AI path available so paid tools or accounts are not prerequisites.

## Contributing to this living textbook

Learners, teachers, developers, and accessibility specialists are invited to contribute:

- Use [GitHub Discussions](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/discussions) for questions, proposals, and teaching ideas.
- Use [GitHub Issues](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/issues) to report errors, broken links, unclear explanations, outdated setup instructions, or accessibility barriers.
- Use [Pull Requests](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/pulls) to propose corrections and additions.

Read [CONTRIBUTING.md](CONTRIBUTING.md), follow [CODE_STYLE.md](CODE_STYLE.md), and respect the [Code of Conduct](CODE_OF_CONDUCT.md). Record textbook-source changes in [CHANGES.md](CHANGES.md).

## References and acknowledgments

The [Foundations introduction](FOUNDATIONS/FOUNDATIONS_README.md) includes a bibliography of introductory computer science texts. Each language landing page and focused technology module includes curated introductory book recommendations, with authors, editions or publication dates where verified, notes on intended use, and links to publisher, author, or free online editions. The Bash and PowerShell tracks also include shell-specific reading recommendations. These bibliographies complement—not replace—the course lessons and official language documentation. Use official documentation to confirm version-sensitive language, API, and tool details.

External resources may change or have different accessibility characteristics over time; evaluate them in the learner's actual environment. Preserve appropriate attribution when improving or extending material.

---

Select a curriculum that matches a technical domain or learning objective, complete its prerequisites, and work through its materials in sequence. The goal is to become an independent problem solver who can read, write, test, explain, and improve software using accessible tools.
