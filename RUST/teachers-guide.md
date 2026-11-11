# Rust Teacher's Guide

## Purpose and course context

This guide supports the [Rust curriculum](rust_README.md) for beginning programmers, including blind and visually impaired learners using screen readers, braille displays, magnification, or keyboard-first workflows. It supplements the [complete lessons](lessons.md), [topic index](INDEX.md), and [validation instructions](VALIDATION.md).

The course uses stable Rust with the **Rust 2024 edition** and Cargo. Rust's ownership and borrowing rules are not incidental syntax; they are a central part of how learners reason about memory safety, data access, and program design. The official Rust book recommends that learners with no programming background first study general programming concepts. Complete shared foundations and ensure learners understand variables, functions, collections, and control flow before expecting them to work independently with ownership.

## Outcomes and sequence

Complete the shared [Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md) and [Terminal Skills prerequisite](../TERMINAL/TERMINAL_README.md), plus introductory programming preparation where needed. Then follow Units 0–11. Learners should use Cargo, compile and run programs, interpret compiler diagnostics, work with ownership and borrowing, model data with structs and enums, use pattern matching and collections, handle errors with Result and Option, define traits and functions, test behavior, and complete the capstone.

Use a predictable cycle: objective and vocabulary; trace a small code example; predict ownership and output; compile; inspect diagnostics; make one change; explain why the borrow checker accepts or rejects the program. Treat compiler feedback as a source of information, not an adversary.

## Toolchain and Cargo

Install Rust with rustup. Verify `rustc --version` and `cargo --version`. Create a project with:

```sh
cargo new course_app
cd course_app
cargo run
cargo test
```

Explain Cargo.toml, Cargo.lock, crates, modules, build profiles, and the distinction between rustc and Cargo. Use the Rust 2024 edition consistently. Keep dependencies explicit and project-scoped. Teach learners to read the first relevant compiler diagnostic and follow the borrow checker explanation back to the expression or binding that created the constraint.

## Teaching Rust concepts

### Ownership, borrowing, and lifetimes

Teach ownership through concrete values and moves before introducing references. Distinguish Copy types from moved values. Explain shared references and exclusive mutable references, and connect borrowing rules to aliasing and mutation. Do not reduce lifetimes to punctuation or tell learners to add annotations until the code compiles; first ask what data must remain valid and for how long. Avoid presenting clone as a universal repair for ownership errors.

### Structs, enums, and pattern matching

Use structs for records and enums for alternatives that must be represented explicitly. Teach exhaustive match expressions as a way to account for every variant. Explain Option<T> for possible absence and Result<T, E> for operations that may fail. Encourage explicit handling rather than unwrap or expect in ordinary application paths; explain panic as a deliberate failure mechanism, not normal validation.

### Collections, traits, and errors

Teach Vec, String, HashMap, and iterators with attention to ownership and borrowing of elements. Introduce traits as shared behavior contracts and generics only after learners understand concrete functions. Explain iterator adapters as transformations and distinguish lazy adapters from terminal operations. Use the standard error propagation operator only after learners understand Result and the caller's responsibility.

### Files and tests

Use explicit paths and deterministic fixtures. Explain that relative paths resolve from the process working directory. Check I/O errors and avoid panics for expected file failures. Teach unit tests, integration tests, and test assertions through Cargo after learners can explain function inputs and outputs.

## Accessibility and delivery

- Keep code, rustc/cargo output, and test failures available as selectable text.
- Explicitly name angle brackets, ampersands, asterisks, colons, double colons, lifetimes, and pattern syntax when introduced.
- Teach keyboard navigation by diagnostic, line, symbol, and file; avoid mouse-only IDE features.
- Describe ownership changes as ordered events: binding, move, borrow, mutation, and scope end.
- Do not rely on graphical ownership diagrams; provide text traces with named variables and lifetimes.
- Ensure compiler diagnostics and test names are navigable with the learner's assistive technology.
- Allow time for dense compiler messages and repeated code navigation.

Test the actual rustup, editor, terminal, and screen-reader combination. Accessibility validation is separate from successful compilation.

## Assessment and differentiation

Ask learners to predict whether a value is moved, copied, borrowed, or dropped; justify data-model choices; handle every enum variant; and explain how errors propagate. Include empty collections, missing map keys, invalid input, and file failures. Evaluate the quality of reasoning, not simply whether the learner found a way to silence the compiler.

Start with owned values and short scopes. Add nested borrowing, traits, iterators, and more advanced lifetimes only when prerequisite concepts are stable. Advanced extensions should deepen understanding without turning the course into a contest to satisfy the borrow checker.

## AI-use policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, refactor, or generate course code or assessment solutions.

## Instructor preparation

Verify stable Rust and the Rust 2024 edition, run the repository's rustc example checker, and separately test expected behavior and accessibility. The documented smoke checks establish compilation and process exit only; they do not prove capstone correctness or assistive-technology certification. Record toolchain versions and validation scope. See the [shared accessibility guidance](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md).
