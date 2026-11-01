# Accessible Introduction to Computer Science

## A living, accessibility-first textbook in Python, JavaScript, TypeScript, Java, Kotlin, C, C++, C#, Julia, Swift, and Rust

This book is a structured introduction to programming and core computer science concepts. It is designed with blind and visually impaired learners who use screen readers, braille displays, magnification, keyboard navigation, or combinations of access technologies in mind. It is also intended for sighted beginners, educators, and anyone who benefits from explicit, text-first instruction.

Command-line instructions are cross-platform: macOS and Linux learners use the Bash-family examples (also suitable for typical zsh workflows), and each executable Bash-family block is immediately followed by a Windows 11 PowerShell equivalent. Windows alternatives use native PowerShell commands and tools such as `winget` where Linux package managers are not available.

The textbook is published with **mdBook**. It is not a GitBook project. Markdown files in this repository are the maintained source; mdBook builds them into the navigable online textbook hosted on GitHub Pages. The book is intended to remain a living resource: lessons, examples, exercises, accessibility notes, and teaching materials can be reviewed and improved as learners and educators use them.

Project environments and dependency isolation are introduced in the [development environment guide](DEVELOPMENT/ENVIRONMENT_ISOLATION.md). It covers project-local package management across Python, JavaScript/TypeScript, Rust, and other ecosystems; Conda; Docker and Podman; optional VS Code/Theia container workflows; and the distinction between project tooling and accessibility settings.

**Start learning:** choose a curriculum below, or read this overview to understand the sequence and how to use the materials. Each language curriculum includes its own topic index. The shared [Programming Code Glossary](backmatter/GLOSSARY.md) defines common and language-specific terminology explicitly.

## Purpose and learning philosophy

The goal is not simply to teach programming syntax. Learners should develop the habits used to solve problems with computers: clarify requirements, decompose a task, represent information, design an algorithm, implement it, test it, interpret errors, revise the solution, and explain their decisions.

The curricula share these commitments:

- **Accessibility is part of the design.** Core activities use text-based input and output and can be completed through keyboard-accessible tools. Lessons explain code structure and navigation rather than depending on visual scanning.
- **Concepts precede tools.** Editors, terminals, runtimes, and libraries are taught as instruments for learning computer science, not as ends in themselves.
- **Practice is central.** Short experiments, guided exercises, debugging, and projects provide repeated opportunities to apply concepts.
- **Understanding matters more than typing speed.** Learners reason about programs, predict behavior, test assumptions, and explain their decisions.
- **Errors are part of learning.** Reading diagnostics and correcting a program are core skills.
- **The resource evolves.** Corrections, new examples, and accessibility improvements are welcome through GitHub Discussions, Issues, and Pull Requests.

## Who should use this book?

The primary audience is beginning computer science learners, including students who are blind or visually impaired. It may be used in secondary or postsecondary courses, accessible technology programs, tutoring, independent study, or educator professional development.

No previous programming experience is required. Learners should have, or be developing, basic keyboard and screen-reader or braille-display navigation skills. A teacher can introduce programming and assistive-technology workflows together; lack of advanced screen-reader fluency should not be mistaken for lack of programming ability.

The material is also useful to sighted learners because it emphasizes precise language, semantic structure, explicit feedback, and reproducible text-based workflows.

## What learners will develop

By working through one curriculum, learners should build the ability to:

1. Describe what a computer program is and explain a basic software-development cycle.
2. Set up and use a language runtime, editor, and terminal.
3. Read code structurally, including identifiers, operators, delimiters, indentation, braces, and nested blocks.
4. Store, convert, compare, and process values using appropriate data types.
5. Use expressions, input, output, decisions, and repetition to solve small problems.
6. Organize related values in collections and select suitable data structures.
7. Decompose programs into functions or methods with clear inputs, outputs, and responsibilities.
8. Work with strings, files, exceptions, and structured data at an introductory level.
9. Design and use classes and objects where the language curriculum introduces object-oriented programming.
10. Test behavior, diagnose errors, refine a solution, and communicate how it works.
11. Build text-based applications and complete a capstone that combines course concepts.
12. Evaluate whether program interaction, prompts, messages, and output are understandable through assistive technology.

These are introductory outcomes, not a claim of professional mastery.

## Additional language courses and modules

### Full programming-language courses

Go and Lua are now included as complete introductory courses aligned to the Python Units 0–11 sequence. The C, C++, C#, Julia, Swift, and Rust tracks have also been expanded from short outlines into unit-by-unit lesson manuscripts using the same instructional progression and recurring problem contexts.

- [Go](GO/GO_README.md)
- [Lua](LUA/LUA_README.md)
- [C](C/c_README.md)
- [C++](CPP/cpp_README.md)
- [C#](CSHARP/csharp_README.md)
- [Julia](JULIA/julia_README.md)
- [Swift](SWIFT/swift_README.md)
- [Rust](RUST/rust_README.md)

### Specialized introductory modules

These subjects have different learning objectives, so they are taught as domain-specific modules rather than being forced into the Python lesson sequence.

- [HTML and CSS](MODULES/HTML_CSS.md): semantic, accessible web documents and styling.
- [R](MODULES/R.md): statistical computing, data analysis, and reproducible research.
- [SQL](MODULES/SQL.md): relational data, querying, joins, integrity, and transactions.

### Parallel-course standardization

The [lesson_standardization.json](lesson_standardization.json) file specifies the Python curriculum unit by unit, defines shared datasets and example problems, and contains a reusable prompt for refining each general-purpose language course. Its objective is functional equivalence: students encounter the same concepts and problems while learning the syntax and semantics of a different language. HTML/CSS, R, and SQL remain specialized modules.

## Development environment and lesson structure

Before beginning a language pathway, complete the [terminal skills prerequisite](TERMINAL/TERMINAL_README.md) and review the standalone [IDE setup lesson](DEVELOPMENT/IDE_SETUP.md). The IDE lesson provides installation steps for Visual Studio Code, VSCodium, and Eclipse Theia on Windows, macOS, and Linux; compares IDEs with lightweight text editors; and sets the course policy that AI features may be used only for personal conceptual understanding and reinforcement, not to write or complete course code.

The [lesson structure audit](DEVELOPMENT/LESSON_STRUCTURE_AUDIT.md) compares the current lesson files with the original Python course. The audit finds that the repository is not yet fully standardized: some language tracks are concise lesson maps, and some existing JavaScript, TypeScript, Java, Kotlin, and terminal lessons use different section patterns. It defines a common lesson structure for future normalization rather than claiming that every lesson already matches Python.

## Choose a language

### Python

[Open the Python curriculum](PYTHON/PYTHON_README.md)

Python is a strong starting point for many beginners because its syntax is comparatively compact and it supports interactive experimentation. The course moves from environment setup and computing foundations through numeric programs, decisions, loops, lists, dictionaries, tuples, functions, classes, files, exceptions, testing, data analysis, and projects.

### JavaScript

[Open the JavaScript curriculum](JAVASCRIPT/JAVASCRIPT_README.md)

JavaScript introduces a widely used language with applications in web and server development. This curriculum uses Node.js so the core learning sequence can be completed in a terminal without requiring browser-based visual work. Learners encounter variables, types and coercion, input, control flow, arrays, objects, strings, functions, asynchronous input patterns, classes, files, modules, collections, tests, and projects.

### TypeScript

[Open the TypeScript curriculum](TYPESCRIPT/TYPESCRIPT_README.md)

TypeScript complements JavaScript with a static type system and a compiler-driven workflow. Its growing use in large JavaScript codebases makes it valuable for learning how explicit types, object contracts, strict null checks, and editor diagnostics can prevent many errors before runtime. TypeScript still compiles to JavaScript and requires runtime validation for untrusted data.

### Java

[Open the Java curriculum](JAVA/JAVA_README.md)

Java offers an explicit, statically typed introduction to programming and object-oriented design. Learners work with the JDK and a terminal-based workflow, then study primitive types, expressions, input, control flow, arrays, ArrayLists, strings, methods, classes, inheritance, files, exceptions, collections, testing, and projects.

## Comparing the language paths

| Dimension | Python | JavaScript | TypeScript | Java |
| --------- | ------ | ---------- | ---------- | ---- |
| Typing model | Dynamic | Dynamic, with coercion rules | Static, structural, erased at runtime | Static, explicit types |
| Block structure | Indentation | Braces | Braces |
| Typical execution | Python interpreter | Node.js | TypeScript compiler, then Node.js/JavaScript runtime | JDK compiler and JVM |
| Interactive experimentation | Python REPL | Node.js REPL | TypeScript playground/editor plus Node.js REPL for runtime JavaScript | JShell |
| Beginner emphasis | Concise syntax and problem solving | Data, control flow, and runtime behavior | Explicit contracts, static analysis, and JavaScript interoperability | Types, program structure, and object-oriented design |
| Common next steps | Automation, data work, scripting, APIs | Browser programming, web services, tooling | Typed web applications, large JavaScript codebases, shared libraries | Larger applications, APIs, typed software design |

This is a practical orientation, not a ranking. No language is universally easiest or best. The suitable starting point depends on learner goals, course context, available tools, and instructor expertise. Core concepts transfer across languages; syntax and runtime behavior do not always transfer directly.

## Suggested learning pathways

- **First programming course:** choose one language and complete its units in order. Python is often a comfortable starting point, but goals or course requirements may make JavaScript or Java the better choice.
- **Web and interactive application pathway:** start with JavaScript and Node.js, then continue to browser technologies and accessible web development.
- **Type safety and JavaScript ecosystem:** TypeScript adds static checking to JavaScript and supports incremental adoption in existing projects.
- **Types and object-oriented design:** Java makes types, classes, compilation, and program structure explicit.
- **Cross-language comparison:** complete one introductory course first, then study a second language by comparing equivalent concepts rather than learning several syntaxes simultaneously.
- **Educator-led course:** use the matching teacher's guide alongside the learner units.

Kotlin is a standalone curriculum and does not require completion of Java. C, C++, C#, Julia, Swift, and Rust are also independent learning paths.

Avoid requiring students to learn multiple curricula at once. Complete one language path before comparing syntax and design trade-offs across languages. Depth in one language provides a stronger foundation for transfer.

## Additional standalone language curricula

All language tracks share the [preliminary Bash and PowerShell terminal course](TERMINAL/TERMINAL_README.md). Complete it first so learners can navigate projects, run tools, and interpret command output independently.

| Language | Primary uses | Typical information and workloads | Curriculum |
| --- | --- | --- | --- |
| Kotlin | Android, JVM services, command-line tools, multiplatform software | Typed application models, API payloads, structured records, nullable data, asynchronous state | [Kotlin](KOTLIN/KOTLIN_README.md) |
| C | Operating systems, embedded firmware, drivers, networking, runtimes | Bytes, fixed-width values, memory buffers, binary records, low-level structures | [C](C/c_README.md) |
| C++ | Game engines, simulation, real-time and high-performance software | Numerical arrays, large objects, resource-owning structures, performance-sensitive streams | [C++](CPP/cpp_README.md) |
| C# | Business software, web APIs, cloud services, desktop apps, Unity | Business entities, typed models, JSON/API payloads, database records | [C#](CSHARP/csharp_README.md) |
| Julia | Scientific computing, numerical analysis, optimization, statistics, machine learning | Vectors, matrices, tensors, measurements, simulation outputs, statistical datasets | [Julia](JULIA/julia_README.md) |
| Swift | Apple-platform apps, server-side Swift, cross-platform libraries | Strongly typed app models, settings, structured records, JSON, asynchronous results | [Swift](SWIFT/swift_README.md) |
| Rust | Systems software, CLI tools, network services, WebAssembly, embedded software | Owned values, borrowed views, byte buffers, structured records, concurrent data | [Rust](RUST/rust_README.md) |

These are common application patterns, not hard limits. Choose a language by considering target platform, ecosystem, performance, safety, interoperability, available libraries, and maintainability. Data suitability depends on the data model and validation practices, not simply the language. Treat external input as untrusted and protect sensitive information.

## How the curriculum is organized

Each language has an opening page, a sequence of unit documents, and a teacher's guide. The [mdBook table of contents](SUMMARY.md) is the authoritative navigation for the published book. Unit files may group multiple numbered units; follow the headings and lesson numbers inside each document.

| Language | Learner materials | Teacher support |
| --- | --- | --- |
| Python | [Python overview and units](PYTHON/PYTHON_README.md) | [Python teacher's guide](PYTHON/teachers-guide.md) |
| JavaScript | [JavaScript overview and units](JAVASCRIPT/JAVASCRIPT_README.md) | [JavaScript teacher's guide](JAVASCRIPT/teachers-guide.md) |
| TypeScript | [TypeScript overview and units](TYPESCRIPT/TYPESCRIPT_README.md) | [TypeScript teacher's guide](TYPESCRIPT/teachers-guide.md) |
| Java | [Java overview and units](JAVA/JAVA_README.md) | [Java teacher's guide](JAVA/teachers-guide.md) |

## A practical study routine

1. **Preview:** read the lesson title, objectives or overview, vocabulary, and prerequisites.
2. **Understand:** read the explanation and trace each example. Identify what each statement contributes.
3. **Predict:** state what you expect the program to do before running it.
4. **Run:** execute the example and inspect its text output.
5. **Experiment:** change one input, value, or statement at a time.
6. **Practice:** complete the activities without copying a finished solution.
7. **Debug:** read the diagnostic, locate the relevant code, form a hypothesis, and test a correction.
8. **Explain:** describe the algorithm and the role of important variables, conditions, loops, functions, methods, or objects.
9. **Review:** revisit the skills checklist and record concepts that need more practice.

Keep a learning journal or portfolio. Include the problem statement, approach, sample input and output, errors encountered, and what changed.

## Accessibility and technology

### Recommended working approach

The curricula use a keyboard-first editor and a text-based terminal. Visual Studio Code is the primary editor in the setup material. [Theia IDE](https://theia-ide.org/#theiaide) is another supported option; it provides the keyboard- and screen-reader-oriented accessibility workflows expected in this course and supports many VS Code extensions through Open VSX. Extension availability and individual screen-reader behavior can differ, so verify the required language tools with the learner's setup. JetBrains IDEs are intentionally excluded from the recommended beginner setup: although capable, their breadth and complexity are unnecessary overhead for introductory learners.

Access configurations vary by operating system, screen reader, braille display, editor version, and individual preference. Treat shortcuts and settings in the lessons as starting points; verify them in the learner's environment.

### Dependency and environment management

For Python, use [uv](https://docs.astral.sh/uv/) to manage Python versions, project environments, and dependencies. Install project packages with `uv add package` and run commands with `uv run`; do not use global `pip install` or `python -m pip install` for course dependencies. For JavaScript and TypeScript, install dependencies into the project with `npm install`/`npm install --save-dev` and run project tools through `npx` or npm scripts; do not use global npm installs for course tools. For Java, use the project's Maven Wrapper (`mvnw`/`mvnw.cmd`) or Gradle Wrapper (`gradlew`/`gradlew.bat`) so build tooling and dependencies are reproducible.

### Shared accessibility practices

- Use semantic headings, descriptive link text, ordered procedures, and code fences with language identifiers.
- Enable editor screen-reader support where available and learn navigation by line, word, symbol, file, and diagnostic.
- Configure speech or braille output for punctuation, indentation, line numbers, and code symbols according to learner preference.
- Use a terminal or REPL to run examples and inspect text output.
- Keep examples and output understandable when read sequentially. Label collections, menu options, and results.
- Avoid relying on syntax highlighting, color, spatial placement, diagrams, or screenshots to communicate essential meaning.
- Provide a text description or equivalent activity when a visual resource is included.
- Allow time for navigation and tool interaction; assess programming reasoning separately from assistive-technology speed.
- Ask learners which tools and interaction patterns work for them. Do not infer needs from a diagnosis.

A text-only interface is not automatically accessible. Output order, verbosity, prompts, error handling, keyboard operation, and documentation structure all affect usability. Test activities with the actual access technology where possible and revise barriers as they are identified.

## Assessment and evidence of learning

Use varied evidence rather than relying only on timed code production:

- Explain a program or algorithm in the learner's own words.
- Predict output before execution and explain any difference.
- Complete a short program from a clear specification.
- Find and fix a deliberately introduced bug.
- Write tests or identify useful test cases.
- Refactor a program into clearer functions, methods, or data structures.
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

The curriculum draws on established introductory programming texts and official language documentation, including *Python Crash Course* by Eric Matthes, *Python Programming: An Introduction to Computer Science* by John Zelle, *Introduction to Programming Using Java* by David J. Eck, MDN Web Docs, and official Python, Node.js, TypeScript, and Java documentation. Language-specific pages and lessons provide further references.

Use official documentation to confirm version-sensitive installation and API details. External resources may change or have different accessibility characteristics over time; evaluate them in the learner's actual environment.

---

Select one language, open its curriculum page, and work through the units in sequence. The goal is to become an independent problem solver who can read, write, test, explain, and improve programs using accessible tools.

## GUI, visualization, and workbench accessibility

See the shared [GUI, visualization, and workbench accessibility reference](DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) for screen-reader support by toolkit, platform-specific activation settings, recommended alternatives, and interfaces that must not be required without an equivalent accessible route.
