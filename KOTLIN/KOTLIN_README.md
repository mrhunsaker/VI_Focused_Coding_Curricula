# Introduction to Kotlin

<<<<<<< HEAD
=======
**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

>>>>>>> 2067a20 (curriculum clearning and updates)
## Standardized beginner curriculum

This course is a Kotlin/JVM parallel track aligned to the shared 12-unit, 57-lesson sequence. It assumes no prior Java experience. Kotlin is statically typed, supports nullable and non-nullable types, and interoperates with Java libraries on the JVM.

## Toolchain

- Use a supported JDK; the course Java pathway baseline is JDK 25 LTS.
- Use Kotlin compiler and Gradle plugin 1.9.24 (the version used by the example-validation workflow) for the documented course baseline; check the [Kotlin release process](https://kotlinlang.org/docs/releases.html) before changing versions.
- Verify the compiler with `kotlinc -version` and the runtime with `java -version`.
- For a single file: `kotlinc Hello.kt -include-runtime -d hello.jar`, then `java -jar hello.jar`.
- For multi-file work, use the Gradle wrapper and Kotlin/JVM plugin. Commit the wrapper so the build version is reproducible.

## Course files

- [Unit 0–1: setup and foundations](unit00-01-setup-foundations.md)
- [Unit 2–4: expressions, control flow, and collections](unit02-04-io-control-data.md)
- [Unit 5–8: input, functions, OOP, and files](unit05-08-strings-functions-oop-files.md)
- [Unit 9–11: testing, analysis, and projects](unit09-11-collections-projects.md)
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
<<<<<<< HEAD
=======

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.

## Verification status

Every lesson has one Kotlin example that uses the shared datasets. All 57 examples compile together with `kotlinc` 1.9.24, run independently with empty standard input, and match the exact output in `examples_expected.json` (`scripts/check_kotlin_examples.py`; checked on JDK 21). The "Expected Behavior or Output" blocks in the lessons are captured from runs of the same examples, with the standard input shown where a program reads input. This has not been tested with screen readers or braille displays.
>>>>>>> 2067a20 (curriculum clearning and updates)
