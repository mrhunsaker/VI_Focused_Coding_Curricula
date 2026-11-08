# Kotlin Teacher's Guide

## Purpose and audience

This guide supports instructors teaching the Kotlin pathway to beginning programmers, including blind and visually impaired learners who use screen readers, braille displays, keyboard navigation, magnification, or other access technology. It supplements the [Kotlin curriculum overview](KOTLIN_README.md), [unit lessons](unit00-01-setup-foundations.md), and [complete lesson reference](lessons.md).

Kotlin is a statically typed language that runs primarily on the Java Virtual Machine in this course. It interoperates with Java libraries but has distinct syntax, null-safety rules, collection interfaces, and language conventions. Do not assume Java knowledge is a prerequisite.

## Course outcomes

Learners should be able to explain the role of source code, compiler, runtime, project, and dependency; write, compile, and run small Kotlin programs; declare values and variables; use numeric types and explicit conversions; read input and produce output; construct decisions and loops; select and manipulate collections; design functions; explain classes and objects; work with files and errors; test behavior; and complete and communicate an integrated project.

## Recommended instructional sequence

Follow the unit order in the curriculum. Do not skip computing foundations or the terminal prerequisite simply because a learner can use an IDE. The terminal provides a transferable route to running tools, interpreting diagnostics, and understanding project structure.

Use a predictable lesson rhythm:

1. State the learning objective and prerequisite concepts.
2. Define new vocabulary before using it in a code example.
3. Explain the structure of the example before asking learners to execute it.
4. Ask learners to predict the result.
5. Run the example and compare actual behavior with the prediction.
6. Discuss diagnostics and common mistakes as evidence about program structure.
7. Assign a modification that requires reasoning rather than copying.
8. Ask the learner to explain the result in their own words.

## Teaching Kotlin's type system

Explicitly distinguish a variable's declared type from its current value. Kotlin's type inference reduces annotation where the type is clear, but inference does not make Kotlin dynamically typed. Use examples that contrast val and var, and explain that val prevents reassignment of the reference rather than guaranteeing deep immutability of every referenced object.

Teach numeric conversions as explicit operations. Do not imply that an Int can be used wherever a Double is expected without conversion. Explain integer division, floating-point representation, and overflow at a level appropriate to the learner's stage.

## Teaching null safety

Null safety is a central Kotlin concept. Introduce nullable types deliberately and contrast a non-nullable declaration with a nullable one. Teach the following as distinct tools:

- Safe call ?. performs an access only when the receiver is non-null.
- Elvis operator ?: provides an alternate expression when the left side is null.
- Not-null assertion !! asserts that a value is not null and accepts the possibility of a runtime exception.

Do not teach !! as the routine solution to a compiler error. Ask learners to explain why a value may be absent and choose a design that handles that possibility.

## Collections and data modeling

Distinguish arrays, lists, sets, and maps by their behavior and intended use. Kotlin's read-only collection interfaces do not necessarily guarantee that the underlying collection cannot be changed through another reference. Avoid teaching read-only as synonymous with deeply immutable.

Use named data classes when records have domain meaning. Pair and Triple are useful for small temporary groupings, but opaque positional fields can make a program harder to read and explain through a screen reader.

## Object-oriented instruction

Kotlin classes are final by default. Explain that inheritance requires an explicit design decision and the appropriate open declarations. Teach composition and interfaces alongside inheritance rather than presenting subclassing as the default reuse strategy. Distinguish properties from Java-style field access and explain constructors, visibility, and member functions.

## Files, resources, and errors

Teach file operations with explicit paths and predictable test data. Discuss working directories because relative paths are interpreted relative to the process's current directory, not necessarily the source file's location. Use resource-safe constructs such as use when appropriate. Learners should inspect returned values and exceptions rather than suppressing failures.

## Accessibility and instructional delivery

- Provide all essential content as selectable text.
- Use semantic headings and descriptive links.
- State code punctuation and nesting explicitly when introducing unfamiliar syntax.
- Avoid instructions such as “click the green triangle” without a keyboard equivalent.
- Ensure the learner can inspect compiler messages and program output as text.
- Provide keyboard-first navigation paths for editing, saving, running, and debugging.
- Allow additional time for screen-reader verbosity and braille review; do not interpret slower navigation as weaker conceptual understanding.
- Test the actual toolchain with the learner's assistive technology. Do not infer accessibility from a vendor statement or another learner's configuration.
- Do not make a visual debugger, diagram, or GUI-only tool the sole assessment route.

See [Development editors and IDEs](../DEVELOPMENT/IDE_SETUP.md) for the role of VS Code, Theia, and other professional environments. That reference discusses product purposes and accessibility evaluation but does not provide third-party IDE setup procedures.

## Assessment

Assess both the program and the learner's reasoning. Suitable evidence includes a prediction of output before execution; a clear explanation of variables, types, and control flow; a test that distinguishes normal from boundary or invalid input; a diagnosis of a compiler or runtime error; a justified choice of collection or data model; a function or class explanation in terms of responsibility and inputs/outputs; a demonstration of file handling and error reporting; and a reflection describing what was tested and what remains uncertain.

Do not equate a program that compiles with a program that is correct. Require expected-output checks or explicit behavioral tests where the lesson calls for them.

## AI-use policy

Follow the repository's course policy. AI may be used only for personal conceptual understanding and reinforcement; it must not write, complete, autocomplete, repair, refactor, or generate course code or assessment solutions for students or instructors. Instructors should provide the same policy consistently across language tracks.

## Validation and maintenance

The course includes expected-output fixtures and an example-checking workflow. Before a teaching term, instructors should review the current compiler and JDK baseline, run the validation script from a clean checkout, verify relevant mdBook links, and record exact versions and results. Runtime validation and assistive-technology validation are separate activities.

Report corrections through the repository's contribution process. When changing examples, update expected output and validation evidence together. Do not claim that the course has been fully accessibility-tested unless the exact supported workflows have been exercised and documented.
