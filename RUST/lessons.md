# Rust: Lessons and Guided Practice

## Toolchain and first run

Install stable Rust with rustup. Create a project using Cargo, then run it with cargo run and execute tests with cargo test. Learn the roles of Cargo.toml, src/main.rs, and the generated lockfile.

## Lesson 1: Cargo and project structure

Study rustup, rustc, Cargo, packages, crates, modules, and build profiles. Exercise: create a project and run its starter program.

## Lesson 2: Bindings and types

Use let, mut, scalar types, tuples, arrays, expressions, and explicit conversions. Exercise: calculate a summary and explain integer overflow behavior.

## Lesson 3: Ownership and borrowing

Understand moves, Copy, references, mutable borrowing, and the borrow checker. Explain why multiple mutable aliases are restricted. Exercise: pass data by reference without transferring ownership unnecessarily.

## Lesson 4: Control flow and functions

Use if expressions, loops, match, functions, parameters, return values, and modules. Exercise: split parsing, validation, and reporting into functions.

## Lesson 5: Structs, enums, and pattern matching

Model records with structs and finite states with enums. Use match and exhaustive handling. Exercise: represent parsing outcomes with Result or a custom enum.

## Lesson 6: Collections, strings, and errors

Use Vec, HashMap, String, slices, Option, Result, and the question-mark operator. Exercise: parse records and report malformed entries without panicking.

## Lesson 7: Traits, generics, and lifetimes

Study trait bounds, generic functions, lifetime annotations, and borrowing relationships. Exercise: define a generic reporting trait and explain its constraints.

## Lesson 8: Files, iterators, and tests

Read and write files, use iterator adapters, and write unit and integration tests. Exercise: process a file and test empty, malformed, and valid records.

## Lesson 9: Safe concurrency

Introduce threads, message passing, shared state, Send, Sync, and synchronization primitives. Exercise: split independent work and communicate results safely.

## Lesson 10: Capstone

Build a command-line file-processing utility with structured errors, ownership-aware data flow, tests, and clear documentation. Explain how ownership shapes the design.
