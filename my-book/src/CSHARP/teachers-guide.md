# C# Teacher's Guide

## Purpose and course context

This guide supports the [C# curriculum](csharp_README.md), designed for beginning programmers including blind and visually impaired learners who use screen readers, braille displays, magnification, or keyboard navigation. It supplements the [complete lessons](lessons.md) and [topic index](INDEX.md).

The course uses the **.NET 10 SDK and C# 14 toolchain**. C# is a statically typed, managed language with a broad .NET library ecosystem. Teach the language and the .NET runtime as related but distinct ideas: C# is the source language; the SDK builds projects; the runtime executes applications; and libraries provide APIs.

## Outcomes and course sequence

Complete the shared [Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md) and [Terminal Skills prerequisite](../TERMINAL/TERMINAL_README.md), then follow Units 0–11. Learners should be able to create and run a console project, read compiler diagnostics, use types and expressions, implement control flow, work with collections, write methods and classes, handle files and exceptions, test programs, and complete the capstone. They should understand nullable reference types and the role of the .NET project system.

Use a repeatable lesson structure: objective and vocabulary; explicit code walkthrough; prediction; build/run; output and diagnostic review; independent modification; explanation. Require learners to explain what the program does, not merely repeat the compiler's response.

## Toolchain and build workflow

Use the .NET 10 SDK and create a console project with:

```sh
dotnet new console
dotnet run
dotnet build
dotnet test
```

Explain the project file, target framework, SDK, compiler, runtime, NuGet dependency, and build artifacts. Run commands from the project directory and teach learners to identify the current working directory. Use repository-defined commands and dependencies; avoid global, undocumented tooling. The curriculum's automated checker builds and smoke-executes each fenced C# example with nullable analysis and warnings treated as errors. This is a useful baseline check, not proof of expected-output correctness or complete capstone behavior.

## Teaching C# concepts

### Types, conversions, and nullability

C# is statically typed. Explain type inference with var without implying dynamic typing. Teach numeric conversions, integer division, overflow behavior, and the difference between value types and reference types at an introductory level. Nullable reference types provide compiler analysis; they do not make runtime null values impossible. Use nullable annotations and flow analysis to reason about possible absence. Avoid suppressing warnings with the null-forgiving operator as a routine fix.

### Collections and data modeling

Compare arrays, List<T>, Dictionary<TKey,TValue>, and other collections by ordering, key lookup, mutability, and intended use. Teach generic type parameters as constraints on the values a collection accepts. Use named record or class models when they make domain data easier to inspect and explain. Avoid opaque tuples for long-lived records.

### Methods, classes, and object-oriented design

Teach method signatures as contracts: name, parameters, return type, and observable behavior. Explain constructors, properties, access modifiers, static members, interfaces, and composition. Inheritance should solve a clear substitutability problem rather than serve as the default reuse technique. Distinguish reference identity from value equality and teach equality deliberately when learners use records or custom types.

### Exceptions, files, and tests

Teach exceptions for exceptional failures and validation for expected invalid input. Use explicit paths, predictable fixtures, and deterministic output. Explain working directories and dispose resources reliably, using using declarations or statements where appropriate. Tests should cover normal, boundary, and invalid cases. Learners should read assertion failures and compiler diagnostics as structured text.

## Accessibility and delivery

- Keep essential instruction, code, diagnostics, and output in selectable text.
- State braces, angle brackets, nullable markers, question marks, lambda arrows, and generic type syntax explicitly when introduced.
- Teach keyboard-first editor, terminal, build, and test workflows.
- Ensure diagnostics can be navigated by file, line, and severity; explain the difference between build warnings and errors.
- Do not make a visual debugger, GUI designer, or IDE-only feature the sole route to completing an objective.
- Use text descriptions for object relationships and collection contents; do not rely on diagrams or syntax color.
- Allow time for screen-reader verbosity and braille review. Assess reasoning independently of navigation speed.

Test the actual .NET SDK, editor, and assistive technology used by the learner. A successful build does not establish that the workflow is accessible.

## Assessment and differentiation

Ask learners to explain type choices, nullable-flow assumptions, collection selection, method contracts, object responsibilities, and exception paths. Require tests for empty collections, missing keys, null values, malformed input, and unavailable files. Evaluate correctness, reasoning, test quality, and communication separately.

Provide scaffolded starter projects and short diagnostics for learners who need additional practice. Extend advanced learners with LINQ, asynchronous methods, interfaces, or dependency design only when these topics reinforce the stated outcomes; do not overload the beginner sequence.

## AI-use policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, refactor, or generate course code or assessment solutions. Keep this rule consistent across demonstrations, homework, and assessment.

## Instructor preparation and maintenance

Before the course, verify the .NET 10 SDK and C# 14 compiler baseline, run the repository's C# example checker, and separately test expected behavior and accessibility. The published smoke check is not a substitute for complete behavioral testing. Record exact SDK versions and validation scope. Consult the [shared GUI and workbench accessibility guidance](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) before requiring graphical tools.
