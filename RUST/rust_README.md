# Rust Curriculum

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.Rust is used for systems software, command-line tools, networking, embedded development, WebAssembly, and performance-sensitive services.

A complete introductory course aligned to Python Units 0–11. Familiar problem contexts recur so learners focus on Rust's ownership, borrowing, types, collections, error handling, traits, and idioms.

## Environment

Install Rust using rustup. Verify `rustc --version` and `cargo --version`. Create a project with `cargo new course_app`, then run `cargo run`.

Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md) and [terminal prerequisite](../TERMINAL/TERMINAL_README.md).

- [Complete lessons](lessons.md)
- [Topic index](INDEX.md)


## Lesson-quality refinement

The Unit 0–11 manuscript now has four complete setup lessons and 53 numbered lessons, including the missing Unit 2 Lesson 2.5 math counterpart. Each numbered lesson includes Rust-specific concepts, a distinct standard-library worked example, three common mistakes, four activities, accessibility practice, and five measurable checklist criteria. The course targets stable Rust with the Rust 2024 edition.

### Validation

scripts/check_rust_examples.py compiles and smoke-runs every fenced Rust example with rustc --edition=2024 -D warnings. The GitHub Actions workflow .github/workflows/rust-examples.yml runs this check on relevant changes. Passing establishes compilation and successful process exit, not expected-output correctness, complete capstone behavior, or assistive-technology certification. See VALIDATION.md for current status.

## GUI, visualization, and workbench accessibility

See the shared [GUI, visualization, and workbench accessibility reference](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) for screen-reader support by toolkit, platform-specific activation settings, recommended alternatives, and interfaces that must not be required without an equivalent accessible route.
## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
## Recommended introductory books

- Klabnik, Steve, Carol Nichols, and Chris Krycho, with contributions from the Rust community. *The Rust Programming Language*. No Starch Press; continuously maintained online edition. The official Rust book introduces ownership, borrowing, types, structs, enums, pattern matching, error handling, generics, and Cargo through sequential explanations and projects. [Free official online edition](https://doc.rust-lang.org/book/).

**Prerequisite note:** the official Rust book explicitly recommends that readers who are entirely new to programming first study a general programming introduction. Complete the shared computing foundations and an introductory language pathway if concepts such as variables, functions, collections, and control flow are unfamiliar. Then use this book alongside the course's Rust lessons. Check its stated Rust version against the course toolchain.
