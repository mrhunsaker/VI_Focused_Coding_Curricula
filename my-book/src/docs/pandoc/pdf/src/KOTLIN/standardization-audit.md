# Kotlin Curriculum Standardization Audit

## Scope

This audit records the intended alignment of the Kotlin track with the repository's shared introductory sequence. It is an editorial and structural reference, not a substitute for a fresh compiler run, behavioral test, or assistive-technology evaluation.

## Curriculum alignment

The Kotlin track follows the shared beginner progression: accessible environment and toolchain concepts; computing foundations and first programs; numeric values, expressions, and input; decisions and repetition; collections and structured data; functions and decomposition; object-oriented programming; files and error handling; testing, analysis, projects, and capstone integration.

Course files:

- [Kotlin overview](KOTLIN_README.md)
- [Unit 0–1](unit00-01-setup-foundations.md)
- [Unit 2–4](unit02-04-io-control-data.md)
- [Unit 5–8](unit05-08-strings-functions-oop-files.md)
- [Unit 9–11](unit09-11-collections-projects.md)
- [Complete lessons](lessons.md)
- [Topic index](INDEX.md)

## Language-specific accuracy requirements

Reviewers should confirm that instruction consistently reflects Kotlin rather than mechanically translating Python or Java:

- val declares a read-only reference; var permits reassignment.
- Kotlin distinguishes nullable and non-nullable types.
- Safe calls (?.), the Elvis operator (?:), and not-null assertions (!!) have distinct semantics and risk profiles.
- Numeric conversions are explicit; arithmetic should not assume implicit widening.
- Classes are final by default unless declared open.
- Collection interfaces distinguish read-only access from mutable operations; read-only does not imply deep immutability.
- Pair and Triple are available, but named data classes are often clearer for domain records.
- Resource cleanup should use appropriate resource-safe constructs such as use.
- Java interoperability and JVM build behavior should be explained without implying identical syntax or type semantics.

## Accessibility criteria

Examples should remain understandable through linear reading and screen-reader output. Punctuation, braces, parentheses, generic types, and nested expressions should be explained when they affect comprehension. Compiler diagnostics should be treated as text to interpret, not visual markers alone. Core exercises should be completable through keyboard-driven editor and terminal workflows. GUI demonstrations must not be the only route to demonstrate a learning outcome.

## Verification evidence

The repository includes examples_expected.json and the Kotlin example-checking script referenced by the curriculum. A reviewer should run the current validation script using the documented Kotlin compiler and JDK baseline before recording a new pass. The existence of expected-output fixtures does not itself prove that examples still compile or match those fixtures.

Record the exact compiler, JDK, operating system, command, commit, and result for each validation run. Separate compilation, process execution, output comparison, and accessibility testing in the report.

## Known limitations and maintenance

This audit is a checklist for continued review. It does not claim a new runtime validation or screen-reader certification. Before publishing a release, verify all 57 lesson/example references, fixture parity, supported Kotlin and JDK versions, scripts from a clean checkout, internal links and mdBook navigation, and screen-reader/braille workflows on target platforms.

Update this file when the lesson sequence, validation scripts, compiler baseline, or expected-output fixtures change.
