# Go Teacher's Guide

## Purpose and course context

This guide supports instructors using the [Go curriculum](GO_README.md) with beginning programmers, including blind and visually impaired learners using screen readers, braille displays, magnification, or keyboard navigation. It supplements the [complete lessons](lessons.md) and [topic index](INDEX.md).

Go is a compiled, statically typed language used for command-line tools, network services, infrastructure, and concurrent systems. Its package model, slices, maps, structs, interfaces, explicit error returns, and goroutines shape the course. The curriculum uses a current stable Go toolchain; check the repository's stated baseline before each term.

## Outcomes and sequence

Complete the shared [Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md) and [Terminal Skills prerequisite](../TERMINAL/TERMINAL_README.md), then follow Units 0–11. Learners should create a module, build and run programs, interpret compiler diagnostics, use static types and control flow, work with slices and maps, define functions and structs, use interfaces, handle errors, process files and data, test code, and complete the capstone. They should understand Go's concurrency model conceptually even when concurrency is not required for every task.

Use a consistent cycle: objective and vocabulary; code walkthrough; prediction; gofmt/build/run; output and diagnostic review; modification; learner explanation. Keep examples small and avoid introducing concurrency, interfaces, and error handling all at once.

## Toolchain and modules

Verify the installed version with `go version`. Create a project with:

```sh
mkdir courseapp
cd courseapp
go mod init example.com/courseapp
go run .
go test ./...
```

Explain package declarations, imports, module paths, the go.mod file, and the difference between go run and go build. Use gofmt consistently; formatting is part of the standard Go workflow, not a cosmetic optional step. Teach learners to run commands from the module root and interpret package-qualified diagnostics.

## Teaching Go's language model

### Types, zero values, and conversions

Go is statically typed and uses explicit conversions between many numeric types. Explain zero values and initialization, and contrast a declared variable with an inferred short declaration. Teach that short declarations have scope rules and are not interchangeable with assignment. Do not imply that Go performs arbitrary implicit numeric conversion.

### Slices, maps, structs, and interfaces

A slice is a descriptor over an underlying array; its length and capacity are different. Appending may allocate a new backing array, so explain when two slices may share storage. Maps provide key/value lookup but do not promise iteration order. Use structs for named records and interfaces to describe behavior at the point where abstraction is useful. Explain that Go interfaces are satisfied implicitly; avoid teaching interfaces as mandatory ceremony for every type.

### Errors and concurrency

Errors are values returned by functions. Teach the pattern of checking an error before using the accompanying result. Do not normalize ignored errors or use panic/recover for ordinary input validation. Introduce goroutines and channels with a clear model of independent execution and communication; discuss cancellation, blocking, and synchronization before assigning multi-goroutine projects. Race freedom cannot be inferred from a successful build or test run without an appropriate race check.

### Files and tests

Use explicit paths and deterministic fixtures. Explain the process working directory, os package operations, and error checks. Teach table-driven tests after learners understand functions and assertions. Include normal, boundary, and invalid cases; use temporary directories for file exercises where appropriate.

## Accessibility and instructional delivery

- Present source, gofmt output, compiler messages, test output, and command results as text.
- Explicitly describe braces, short declarations, pointers, channel operators, and interface method sets.
- Teach keyboard-first editor navigation and terminal commands; no mouse-only run controls.
- Explain goroutine and channel traces as ordered text events rather than relying on animation or diagrams.
- Ensure learners can navigate test failures by package, file, line, and test name.
- Avoid color-only status indicators and graphical workbenches without an equivalent text workflow.
- Allow additional time for punctuation verbosity and diagnostic navigation.

Verify accessibility with the actual OS, editor, terminal, screen reader, and braille display used in class.

## Assessment and differentiation

Assess whether the learner can explain types, slice length versus capacity, map ordering, interface satisfaction, explicit error handling, and concurrency risks. Require tests for empty collections, missing keys, file errors, and malformed input. For concurrency, ask learners to identify possible blocking and shared-state access before execution. Distinguish compilation, smoke execution, expected-output validation, race testing, and accessibility testing; they are different forms of evidence.

Scaffold with single-package programs and sequential code first. Extend learners with additional packages, interfaces, context cancellation, or concurrent workers only after the core data and error models are stable.

## AI-use policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, refactor, or generate course code or assessment solutions.

## Instructor preparation

Verify the Go toolchain, run the repository's gofmt/build/smoke-check workflow, and separately inspect expected behavior and accessibility. The current example check does not establish exact output, capstone correctness, race freedom, or assistive-technology certification. Record toolchain versions and validation scope. See the [shared accessibility guidance](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md).
