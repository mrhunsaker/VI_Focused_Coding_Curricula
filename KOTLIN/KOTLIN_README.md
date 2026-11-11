# Introduction to Kotlin

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

## Standardized beginner curriculum

This course is a Kotlin/JVM parallel track aligned to the shared 12-unit, 57-lesson sequence. It assumes no prior Java experience. Kotlin is statically typed, supports nullable and non-nullable types, and interoperates with Java libraries on the JVM.

## Toolchain

- Use a supported JDK; the course Java pathway baseline is JDK 25 LTS.
- Use Kotlin compiler and Gradle plugin 1.9.24 (the version used by the example-validation workflow) for the documented course baseline; check the [Kotlin release process](https://kotlinlang.org/docs/releases.html) before changing versions.
- Verify the compiler with `kotlinc -version` and the runtime with `java -version`.
- For a single file: `kotlinc Hello.kt -include-runtime -d hello.jar`, then `java -jar hello.jar`.
- For multi-file work, use the Gradle wrapper and Kotlin/JVM plugin. Commit the wrapper so the build version is reproducible.

## Course files

- [Unit 0: accessible development environment](unit00-accessible-development-environment.md)
- [Unit 1: foundations of computing](unit01-foundations-of-computing.md)
- [Unit 2: numeric computations](unit02-numeric-computations.md)
- [Unit 3: control flow, decisions, and loops](unit03-control-flow-decisions-and-loops.md)
- [Unit 4: data structures, lists, and dictionaries](unit04-data-structures-lists-and-dictionaries.md)
- [Unit 5: user input and while loops](unit05-user-input-and-while-loops.md)
- [Unit 6: functions](unit06-functions.md)
- [Unit 7: classes and object-oriented programming](unit07-classes-and-object-oriented-programming.md)
- [Unit 8: files and exceptions](unit08-files-and-exceptions.md)
- [Unit 9: testing and data analysis](unit09-testing-and-data-analysis.md)
- [Unit 10: project-based text applications](unit10-project-based-learning-text-based-applications.md)
- [Unit 11: accessible personal data manager capstone](unit11-capstone-accessible-personal-data-manager.md)
- [Complete standalone Kotlin reference lessons](lessons.md)
- [57-topic index](INDEX.md)
- [Teacher guide](teachers-guide.md)
- [Expected output fixtures for all 57 examples](examples_expected.json)
- [Standardization audit](standardization-audit.md)

## Kotlin semantics emphasized

Teach `val` versus `var`, static typing and inference, explicit numeric conversions, nullable types, safe calls (`?.`), Elvis expressions (`?:`), and the risk of not-null assertions (`!!`). Kotlin has no general tuple syntax; use named data classes, Pair, or Triple as appropriate. Distinguish read-only collection interfaces from mutable collections. Kotlin classes are final by default; inheritance requires deliberate `open` declarations. Use `use` for resource-safe operations and maintained libraries for JSON and CSV.

## Accessibility baseline

Use keyboard-first editor and terminal workflows. Verify the selected Kotlin language server, diagnostics, Gradle tasks, and screen-reader announcements with the learner's actual access technology. Explain punctuation and indentation explicitly. Prefer named intermediate values and short functions over deeply nested expressions. The default capstone interface is text-first; a GUI is not required to demonstrate the shared data operations.

## Assessment and AI-use policy

Assess conceptual understanding, independent tracing, testing, explanation, and accessible tool use. AI may support conceptual understanding and reinforcement only; it must not generate, complete, repair, refactor, or write course code or assessment solutions for students or instructors.

The lesson files provide the aligned instructional structure. The audit records what has and has not been verified; structural completeness is not a claim that every example or full application has passed runtime tests.

## GUI, visualization, and workbench accessibility

See the shared [GUI, visualization, and workbench accessibility reference](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) for screen-reader support by toolkit, platform-specific activation settings, recommended alternatives, and interfaces that must not be required without an equivalent accessible route.
## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.

## Verification status

Every lesson has one Kotlin example that uses the shared datasets. All 57 examples compile together with `kotlinc` 1.9.24, run independently with empty standard input, and match the exact output in `examples_expected.json` (`scripts/check_kotlin_examples.py`; checked on JDK 21). The "Expected Behavior or Output" blocks in the lessons are captured from runs of the same examples, with the standard input shown where a program reads input. This has not been tested with screen readers or braille displays.

## Recommended introductory books

- Griffiths, Dawn, and David Griffiths. *Head First Kotlin: A Brain-Friendly Guide*. O'Reilly Media, 2019. A hands-on introduction to Kotlin syntax and programming concepts. [Publisher catalog](https://www.oreilly.com/search/?q=Head%20First%20Kotlin).
- Eckel, Bruce, and Svetlana Isakova. *Atomic Kotlin*. Mindview, 2021. Presents Kotlin concepts in small, focused lessons with exercises; intended for both beginning and experienced programmers. [Author-maintained learning resources](https://www.atomickotlin.com/atomickotlin/).
- Aigner, Sebastian, Roman Elizarov, Svetlana Isakova, and Dmitry Jemerov. *Kotlin in Action*, 2nd edition. Manning, 2024. A comprehensive treatment aimed primarily at readers familiar with Java or another object-oriented language. [Kotlin documentation's book recommendations](https://kotlinlang.org/docs/books.html).

**Suggested use:** *Head First Kotlin* or *Atomic Kotlin* is the more suitable first companion. Treat *Kotlin in Action* as a follow-on reference, not a prerequisite. Check current Kotlin documentation when book examples differ from the course baseline.
