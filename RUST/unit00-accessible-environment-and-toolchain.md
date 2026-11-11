# Unit 0: Accessible Environment and Toolchain

## Course overview

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.
## Course Overview

Rust is a systems programming language designed for memory safety, concurrency, and performance without a garbage collector. It is used for command-line tools, operating-system components, networking, embedded software, WebAssembly, and performance-sensitive services. This course uses the Python curriculum's canonical examples and datasets while teaching Rust idioms: ownership, borrowing, lifetimes, enums, pattern matching, Option, Result, traits, iterators, and RAII.

**Toolchain baseline:** stable Rust with the Rust 2024 edition. Install through rustup; use Cargo for project creation, dependency management, formatting, checking, testing, and builds. The worked examples use the standard library unless a lesson explicitly discusses an ecosystem crate.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install Rust, understand Cargo projects, configure an editor with rust-analyzer, and establish an accessible keyboard/screen-reader workflow.

### Lesson 0.1: Install and Verify Rust

### Reading References
- [Install Rust](https://www.rust-lang.org/tools/install)
- [The Cargo Book](https://doc.rust-lang.org/cargo/)

### Learning Objectives
- Install rustup, the stable toolchain, rustc, and Cargo.
- Verify the setup with terminal commands and interpret their output.
- Complete the workflow using keyboard navigation and accessible diagnostics.

### Concept Explanation
rustup manages Rust toolchains. rustc compiles source files; Cargo manages packages, dependencies, builds, and tests. Prefer the stable channel.

### Worked Example
```sh
rustc --version\ncargo --version\nrustup show active-toolchain
```

**Expected behavior:** The terminal prints compiler and Cargo versions and identifies the active toolchain.

### Common Mistakes
- Installing Rust from an untrusted binary or unofficial mirror.
- Confusing the editor integration with the compiler or Cargo.
- Running commands from the wrong working directory or package root.

### Activities
1. Follow the commands from a new project directory and record the result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional error and locate the diagnostic text.
4. Explain which files belong to the project and which are generated artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostics navigation, and sequential output reading. Keep keyboard workflows documented.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the project root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.
### Lesson 0.2: Cargo Workspace and First Run

### Reading References
- [Install Rust](https://www.rust-lang.org/tools/install)
- [The Cargo Book](https://doc.rust-lang.org/cargo/)

### Learning Objectives
- Create a Cargo binary project and identify its source and manifest.
- Verify the setup with terminal commands and interpret their output.
- Complete the workflow using keyboard navigation and accessible diagnostics.

### Concept Explanation
A Cargo package is described by Cargo.toml; executable source conventionally starts at src/main.rs. Generated build artifacts live under target/.

### Worked Example
```sh
cargo new course_app\ncd course_app\ncargo run
```

**Expected behavior:** Cargo creates the project and runs a program that prints Hello, world!.

### Common Mistakes
- Installing Rust from an untrusted binary or unofficial mirror.
- Confusing the editor integration with the compiler or Cargo.
- Running commands from the wrong working directory or package root.

### Activities
1. Follow the commands from a new project directory and record the result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional error and locate the diagnostic text.
4. Explain which files belong to the project and which are generated artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostics navigation, and sequential output reading. Keep keyboard workflows documented.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the project root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.
### Lesson 0.3: Editor and Accessibility Workflow

### Reading References
- [Install Rust](https://www.rust-lang.org/tools/install)
- [The Cargo Book](https://doc.rust-lang.org/cargo/)

### Learning Objectives
- Configure an editor with rust-analyzer and verify accessible navigation.
- Verify the setup with terminal commands and interpret their output.
- Complete the workflow using keyboard navigation and accessible diagnostics.

### Concept Explanation
rust-analyzer provides language-aware completion, navigation, and diagnostics. It is an editor integration, not the compiler. Complete the shared IDE setup and test the exact editor/screen-reader combination used in class.

### Worked Example
```sh
cargo check\ncargo fmt --check
```

**Expected behavior:** Cargo checks the project and reports formatting differences without changing source files.

### Common Mistakes
- Installing Rust from an untrusted binary or unofficial mirror.
- Confusing the editor integration with the compiler or Cargo.
- Running commands from the wrong working directory or package root.

### Activities
1. Follow the commands from a new project directory and record the result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional error and locate the diagnostic text.
4. Explain which files belong to the project and which are generated artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostics navigation, and sequential output reading. Keep keyboard workflows documented.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the project root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.
### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

### Reading References
- [Install Rust](https://www.rust-lang.org/tools/install)
- [The Cargo Book](https://doc.rust-lang.org/cargo/)

### Learning Objectives
- Manage project-local crates and run Cargo commands from the package root.
- Verify the setup with terminal commands and interpret their output.
- Complete the workflow using keyboard navigation and accessible diagnostics.

### Concept Explanation
Cargo records direct dependencies in Cargo.toml and the resolved graph in Cargo.lock for applications. cargo check type-checks; cargo test runs tests; cargo run builds and launches the application. Review third-party crate provenance before adding it.

### Worked Example
```sh
cargo add serde\ncargo check\ncargo test\ncargo run
```

**Expected behavior:** Cargo adds a dependency, resolves it, checks the project, runs tests, and launches the application; initial resolution requires network access.

### Common Mistakes
- Installing Rust from an untrusted binary or unofficial mirror.
- Confusing the editor integration with the compiler or Cargo.
- Running commands from the wrong working directory or package root.

### Activities
1. Follow the commands from a new project directory and record the result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional error and locate the diagnostic text.
4. Explain which files belong to the project and which are generated artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostics navigation, and sequential output reading. Keep keyboard workflows documented.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the project root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.
