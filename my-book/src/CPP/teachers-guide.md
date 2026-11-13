# C++ Teacher's Guide

## Purpose and course context

This guide supports instruction in the [C++ curriculum](cpp_README.md) for beginning programmers, including blind and visually impaired learners using screen readers, braille displays, magnification, or keyboard-first workflows. It supplements the [complete lessons](lessons.md) and [topic index](INDEX.md).

The course targets **C++20** and GCC, Clang, or MSVC. C++ combines procedural, object-oriented, and generic programming with a large standard library. Instruction should make abstraction useful without hiding object lifetime, value semantics, resource ownership, or the behavior of the compiled program.

## Outcomes and instructional sequence

Complete the shared [Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md) and [Terminal Skills prerequisite](../TERMINAL/TERMINAL_README.md), then teach Units 0–11 in order. Learners should be able to build and run a project, interpret compiler diagnostics, use types and expressions, control flow, standard containers, functions, classes, files, exceptions, tests, and an integrated capstone. They should also explain the difference between copying a value, borrowing through a reference, and transferring or sharing ownership.

Use a consistent cycle: objective and vocabulary; code-structure preview; learner prediction; compilation and execution; diagnostic/output review; one deliberate modification; learner explanation. Keep examples small enough that a screen-reader user can navigate the complete construct without losing context.

## Toolchain and project workflow

Use a C++20-capable GCC, Clang, or MSVC toolchain. The representative GCC/Clang command is:

```sh
c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror main.cpp -o main
./main
```

Explain compiler, linker, source file, executable, standard-library headers, and build configuration. Teach project builds consistently and explain when a lesson uses a fragment that is wrapped by a validation harness. Treat warnings as feedback. The course's published example check compiles and links fenced examples; compilation is not equivalent to full behavioral testing or accessibility certification.

## Teaching C++ concepts deliberately

### Values, references, and object lifetime

Start with values and ordinary function calls, then introduce references and pointers as different forms of access to objects. Teach const references for read-only access where appropriate. Explain scope, lifetime, temporary objects, and the consequences of returning a reference to an object that no longer exists. Learners should be able to state which function or object owns a resource and how long it remains valid.

### Standard containers and algorithms

Prefer standard containers such as std::vector, std::array, std::string, and std::map over raw arrays for ordinary application-level tasks. Explain container size, indexing, iteration, and invalidation rules at the level needed by each lesson. Teach iterators as positions in a sequence and algorithms as operations over ranges. Do not imply that every container has constant-time indexing or that modifying a container can never invalidate an iterator or reference.

### Classes, RAII, and resource management

Teach classes as contracts around state and behavior, not as a requirement to model every noun. Introduce constructors, access control, invariants, and member functions. RAII is a core C++ design principle: resource acquisition and release should be tied to object lifetime. Use standard library resource-managing types before introducing manual new/delete. Explain copying and moving as distinct operations, and introduce smart pointers only when ownership relationships justify them. Avoid teaching raw owning pointers as the default.

### Exceptions, files, and generic code

Explain exceptions as a control-flow mechanism for exceptional failure, not as a substitute for validating ordinary user input. Teach file streams and check their state. Introduce templates and generic algorithms through concrete use cases, emphasizing type requirements and compiler diagnostics. When diagnostics are long, teach learners to locate the first meaningful error rather than reading every cascading message as an independent failure.

## Accessibility and delivery

- Use selectable text for source, build output, test results, and diagnostics.
- Explicitly name punctuation and delimiters, including angle brackets, scope resolution, ampersands, asterisks, braces, and template syntax.
- Teach keyboard navigation by symbol, line, file, and diagnostic; provide non-mouse build and run commands.
- Avoid relying on syntax colors, indentation guides, object inspectors, or graphical debugger panes to communicate program structure.
- Describe container contents, iterator positions, object lifetimes, and ownership in ordered text.
- Provide a text alternative for diagrams and ensure any GUI or game-engine work has an accessible nonvisual route.
- Allow additional time for verbose compiler diagnostics and template errors without reducing the conceptual objective.

Validate the actual compiler/editor/screen-reader combination in the classroom. Accessibility support varies by platform and version.

## Assessment

Assess both code behavior and explanation. Ask learners to justify a container choice, trace a function call, identify an object's lifetime, explain a resource's owner, and distinguish an exception from an ordinary validation result. Include tests for empty and non-empty collections, boundary indexes, failed file operations, and invalid input. A compile-only example check is useful but does not establish correct output, resource safety, or complete project behavior.

## Differentiation

For learners who need more structure, use short programs, explicit build commands, and one new abstraction at a time. For learners ready to extend the material, compare vector and map tradeoffs, exception guarantees, move semantics, interfaces, and algorithmic complexity. Keep visual memory models optional; use text traces and named states as the shared representation.

## AI-use policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, refactor, or generate course code or assessment solutions. Apply this consistently to instructor and learner work.

## Instructor preparation

Verify a C++20 compiler, run the current repository validation script, and separately execute representative examples with expected input and output. Check that build commands and diagnostics are accessible through the learner's tools. Record compiler versions and distinguish compilation/linking evidence from behavioral and assistive-technology testing. See the [shared GUI and workbench accessibility guidance](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) before requiring a graphical environment.
