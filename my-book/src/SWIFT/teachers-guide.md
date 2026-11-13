# Swift Teacher's Guide

## Purpose and course context

This guide supports the [Swift curriculum](swift_README.md) for beginning programmers, including blind and visually impaired learners using VoiceOver, other screen readers, braille displays, magnification, and keyboard navigation. It supplements the [complete lessons](lessons.md), [topic index](INDEX.md), and [validation instructions](VALIDATION.md).

The course baseline is **Swift 6 language mode** with a current Swift 6 toolchain. Swift is used for Apple-platform applications, server software, and systems components. Teach Swift's value semantics, optionals, protocols, structured error handling, Codable, and concurrency as language concepts. Do not conflate learning Swift with building a graphical iOS interface; the core course should remain accessible through command-line projects.

## Outcomes and sequence

Complete the shared [Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md) and [Terminal Skills prerequisite](../TERMINAL/TERMINAL_README.md), then follow Units 0–11. Learners should compile and run Swift programs, use types and control flow, work with arrays and dictionaries, write functions, define structs and classes, use protocols, handle optional and throwing operations, process files and Codable data, test behavior, and complete the capstone. They should understand the distinction between a command-line Swift package and an Apple-platform application requiring Xcode and platform SDKs.

Use a consistent lesson cycle: objective and vocabulary; code walkthrough; prediction; swift execution or package build; output/diagnostic review; modification; learner explanation. Encourage learners to predict both values and types, especially when optionals and inferred types are involved.

## Toolchain and packages

Verify with `swift --version` and `swiftc --version`. Run a source file with `swift main.swift`; create an executable package with `swift package init --type executable`, then use `swift build`, `swift run`, and `swift test`. Xcode and Apple SDKs are needed for simulator and native application work, but not for the core command-line sequence. Use Foundation for file operations and Codable JSON encoding. The curriculum uses a standards-aware external CSV library where quoted fields and embedded newlines require full CSV parsing.

## Teaching Swift concepts

### Types, value semantics, and collections

Swift is statically typed with type inference. Explain that inference does not make the language dynamically typed. Distinguish let from var and explain value semantics for structs and enums. Arrays and dictionaries are value types with copy-on-write implementation behavior; teach observable value behavior without overpromising a particular copy timing. Explain dictionary lookup as optional because a key may be absent.

### Optionals and error handling

An optional explicitly represents a value that may be absent. Teach optional binding, if let/guard let, nil coalescing, and optional chaining as separate tools. Do not normalize force unwraps as the default response to compiler errors. Distinguish optional absence from thrown errors: they represent different forms of control flow. Teach do/try/catch and throwing function contracts with explicit failure cases.

### Protocols, generics, and concurrency

Introduce protocols as behavior contracts and generics as reusable abstractions with type constraints. Use concrete examples before protocol-heavy designs. Swift 6 concurrency checking can surface data-isolation and Sendable diagnostics. Teach async/await and task structure only after sequential control flow and function contracts are secure. Explain actor isolation and shared mutable state conceptually; do not dismiss concurrency diagnostics as compiler noise.

### Files and Codable

Use explicit paths and deterministic fixtures. Explain process working directories and Foundation file APIs. Teach Codable as a structured serialization mechanism, not as a guarantee that arbitrary external data is valid. Handle decoding failures explicitly and test missing, malformed, and unexpected fields. Use a CSV parser that supports quoted fields and embedded newlines rather than splitting every row on commas.

## Accessibility and delivery

- Keep the introductory workflow command-line and text-first; do not require Xcode's visual interface for core outcomes.
- Teach VoiceOver and editor navigation appropriate to the learner's platform; provide keyboard paths for build, run, and test.
- Explicitly describe optionals, question marks, exclamation marks, arrows, generics, and closure syntax.
- Make compiler diagnostics, test output, and program output navigable as text.
- Describe collection contents, protocol conformance, and asynchronous event order in text.
- Treat simulator and GUI testing as an extension with a documented accessible alternative, not the only way to demonstrate programming knowledge.
- Allow time for punctuation review and verbose Swift 6 concurrency diagnostics.

Validate the actual macOS or Linux toolchain, editor, terminal, and assistive technology. VoiceOver and other screen readers differ by platform; do not assume a workflow transfers unchanged.

## Assessment and differentiation

Assess type reasoning, value semantics, optional handling, collection selection, protocol use, error propagation, Codable validation, and tests. Include absent dictionary keys, empty collections, malformed JSON, file errors, and throwing operations. Require learners to explain why a force unwrap is or is not justified. Separate compilation, expected-output behavior, package tests, platform UI behavior, and accessibility evidence.

Scaffold with structs, simple functions, and sequential code before protocols and concurrency. Extend advanced learners with generic constraints, actors, or platform APIs only after the core language outcomes are secure.

## AI-use policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, refactor, or generate course code or assessment solutions.

## Instructor preparation

Verify Swift 6 language mode, run the repository's example validation instructions, and separately exercise expected behavior and accessibility. Record OS, compiler version, package commands, and any platform-specific prerequisites. See the [shared GUI and workbench accessibility guidance](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) before requiring Xcode or graphical application tooling.
