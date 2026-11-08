# Unit 0: Accessible Environment and Toolchain

## Course overview

<<<<<<< HEAD
=======
**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

>>>>>>> 2067a20 (curriculum clearning and updates)
## Course Overview

Rust is a systems programming language designed for memory safety, concurrency, and performance without a garbage collector. It is used for command-line tools, operating-system components, networking, embedded software, WebAssembly, and performance-sensitive services. This course uses the Python curriculum's canonical examples and datasets while teaching Rust idioms: ownership, borrowing, lifetimes, enums, pattern matching, Option, Result, traits, iterators, and RAII.

**Toolchain baseline:** stable Rust with the Rust 2024 edition. Install through rustup; use Cargo for project creation, dependency management, formatting, checking, testing, and builds. The worked examples use the standard library unless a lesson explicitly discusses an ecosystem crate.

<<<<<<< HEAD
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

=======
**Verification status:** every lesson has one complete Rust program that uses the shared datasets. All 57 programs compile with `rustc` (edition 2021, `-D warnings`) and run independently, and the "Expected Behavior or Output" blocks are the captured output of those programs, with the standard input shown where a program reads input. The two lessons that contain a `#[cfg(test)]` module also had that module compiled with `--test` and run. This has not been tested with screen readers or braille displays. Rust prints the shared tip as 3.67 with `{:.2}`; Java and Kotlin print 3.68 for the same stored value.

## Overview
Install Rust, understand Cargo projects, configure an editor with rust-analyzer, and establish an accessible keyboard/screen-reader workflow.

## Lesson 0.1: Install and Verify Rust

### Reading References
- [The Rust Programming Language: Installation](https://doc.rust-lang.org/book/ch01-01-installation.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 0.1: Installing Python and uv

### Learning Objectives
- Install Rust with `rustup` from the official source.
- Verify `rustc` and `cargo` from the terminal.
- Compile and run a first program.

### Concept Explanation

Rust is a compiled language. The compiler is `rustc`, and **Cargo** is Rust's build tool and package manager. Both are installed by **rustup**, the official installer and version manager. This course targets stable Rust with the 2024 edition (Rust 1.85 or later); check `rustc --version` rather than assuming.

Install from the official Rust site, and write down which route you used. Then verify:
```text
rustc --version
cargo --version
```
Each prints a version line. If a command is not found, open a new terminal so that the updated PATH is read.

To compile and run the example below without Cargo, save it as `main.rs`, then:
```text
rustc main.rs
./main
```
(on Windows the program is `main.exe`). `rustc` prints nothing when the compile succeeds and there are no warnings.

### Worked Example

```rust
fn main() {
    println!("Rust toolchain ready.");
}
```

### Expected Behavior or Output

The program prints:
```text
Rust toolchain ready.
```

### Common Mistakes
1. Installing from an unofficial source or running an installer command without reading what it does.
2. Not opening a new terminal after installing, so the tools are reported as not found.
3. Assuming an old `rustc` supports the 2024 edition. Check the version.

### Activities
1. Install Rust and record the exact output of both version commands.
2. Compile and run the example from the keyboard and list the files `rustc` created.
3. Remove the semicolon after the `println!` call, compile, and write down the message (it is still valid Rust, so explain why).
4. Explain in two sentences what rustup does that rustc alone does not.

### Accessibility Practice

Run each command from the keyboard and read the output line by line with your screen reader. Confirm that the version numbers are announced digit by digit. Compiler messages are long, so jump to the first line, which names the problem and the file.

### Skills Checklist
- [ ] I can install Rust with rustup.
- [ ] I can verify `rustc` and `cargo`.
- [ ] I can compile and run a first program.
- [ ] I know what Cargo is for.
- [ ] I can say which route I used.

---

## Lesson 0.2: Cargo Workspace and First Run

### Reading References
- [The Rust Programming Language: Hello, Cargo!](https://doc.rust-lang.org/book/ch01-03-hello-cargo.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 0.2: Configuring Your Screen Reader for VS Code or Theia IDE

### Learning Objectives
- Create a Cargo project and run it.
- Name the files Cargo creates.
- Read a compiler error and find the file, line, and message.

### Concept Explanation

A **Cargo project** keeps one program's files together. `cargo new rust-course` creates a folder with `Cargo.toml` (the project's name, version, and dependencies) and `src/main.rs` (the source). From inside that folder, `cargo run` compiles and runs the program, `cargo check` checks it without producing a program (fast), `cargo build` compiles it, `cargo fmt` formats the source, and `cargo clippy` suggests improvements.

Every Rust program starts at `fn main()`. Statements end with semicolons and blocks are enclosed in braces. `println!` is a *macro*, which is why its name ends with an exclamation mark.

Rust's compiler messages are detailed: each starts with `error[E0425]: ...` or `warning: ...`, then an arrow line `--> src/main.rs:3:5` giving the file, line, and column, then the code with a caret under the problem and often a `help:` suggestion. Read the first message first, because later ones are often consequences of it.

### Worked Example

```rust
fn main() {
    println!("Hello, Avery!");
    println!("Welcome to Rust programming!");
}
```

### Expected Behavior or Output

The program prints:
```text
Hello, Avery!
Welcome to Rust programming!
```

### Common Mistakes
1. Running `cargo` commands outside the project folder, so no `Cargo.toml` is found.
2. Fixing the last error message first. Start with the first one.
3. Ignoring `help:` lines, which often contain the exact fix.

### Activities
1. Create a Cargo project from the keyboard, run it, and record the files it created.
2. Misspell `println` as `printn`, run `cargo check`, and write down the code, file, line, and help text. Then restore it.
3. Add a third `println!` with your own name and predict the output before running.
4. Explain the difference between `cargo check` and `cargo run`.

### Accessibility Practice

Create the project with terminal commands. When the compiler reports an error, read the `-->` line first (it holds the file, line, and column), then jump to that line in the editor. Ask your screen reader to read the caret line by character, because the caret marks the exact position.

### Skills Checklist
- [ ] I can create and run a Cargo project.
- [ ] I know what `Cargo.toml` is.
- [ ] I can use `cargo check`.
- [ ] I can read the location line of an error.
- [ ] I know why `println!` ends with `!`.

---

## Lesson 0.3: Editor and Accessibility Workflow

### Reading References
- [rust-analyzer manual](https://rust-analyzer.github.io/manual.html)
- [The Rust Programming Language: The match Control Flow Construct](https://doc.rust-lang.org/book/ch06-02-match.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 0.3: Setting Up Your VS Code or Theia IDE Workspace

### Learning Objectives
- Configure an editor so Rust source is readable by speech or braille.
- Choose a punctuation level that announces the symbols Rust depends on.
- Read `Option`, references, closures, and macros aloud.

### Concept Explanation

Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md) first. Then adapt the editor for Rust. **rust-analyzer** is the usual language server; it is optional, and the course works with a plain editor and the terminal. Install extensions only from a source you trust and read the permissions they request.

Rust depends on punctuation that a screen reader may skip at low settings. Learn to say these: `&` is a *reference* (a borrow), `&mut` is a *mutable reference*, `::` separates a path (`std::env::args`), `->` introduces a return type, `?` passes an error up, `!` after a name marks a *macro*, `'a` is a *lifetime*, `|x| x * 2` is a *closure* (the bars hold its parameters), `{}` inside a format string is a placeholder, and `<T>` holds a type parameter.

Rust structure comes from braces, not indentation, so count the closing braces when you read a nested block.

Read the example aloud: "let name colon Option open angle bracket ampersand str close angle bracket equals None semicolon." Then say what it prints.

### Worked Example

```rust
fn main() {
    let name: Option<&str> = None;
    println!("{}", name.unwrap_or("no value"));

    let title: Option<&str> = Some("Rust");
    if let Some(t) = title {
        println!("title has {} characters", t.len());
    }

    let numbers = vec![1, 2, 3];
    let doubled: Vec<i32> = numbers.iter().map(|n| n * 2).collect();
    println!("{:?}", doubled);
}
```

### Expected Behavior or Output

The program prints:
```text
no value
title has 4 characters
[2, 4, 6]
```

### Common Mistakes
1. Setting punctuation so low that `&`, `::`, and `|` are never spoken, then misreading references or closures.
2. Relying on indentation alone to see where a block ends. Count the closing braces.
3. Installing several overlapping extensions and getting duplicate diagnostics.

### Activities
1. Test your editor with the example and record the punctuation level at which every symbol is announced.
2. Navigate the file by line, word, and character and note the commands you used.
3. Remove a closing brace, save, and find how your editor reports it. Then restore it.
4. Write a half-page note of your edit, check, and run steps using only the keyboard.

### Accessibility Practice

This whole lesson is accessibility practice. Verify that you can open the file, move to a given line, read a line character by character, run `cargo check` in the terminal, and read the output. Record the operating system, editor, and access technology you actually tested; do not describe the setup as verified for other combinations.

### Skills Checklist
- [ ] I can configure my editor for keyboard-only use.
- [ ] I can hear `&`, `::`, and `|` announced.
- [ ] I can read `Option` and a closure aloud.
- [ ] I know Rust structure comes from braces.
- [ ] I can check and read the output from the keyboard.

---

## Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

### Reading References
- [The Rust Programming Language: Accepting Command Line Arguments](https://doc.rust-lang.org/book/ch12-01-accepting-command-line-arguments.html)
- [The Cargo Book](https://doc.rust-lang.org/cargo/)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 0.4: Python Environments, Terminal Usage, and Accessibility Tools

### Learning Objectives
- Run a program with command-line arguments.
- Describe the project root and what Cargo adds.
- Explain when a dependency is needed.

### Concept Explanation

A *command-line argument* is an extra word typed after the program name. `std::env::args()` returns an iterator over them; the first item is the program's own name, so `.skip(1)` leaves only the arguments you typed. This is the simplest way to pass input without a prompt, and it is easy to test.

Keep each project in its own folder and run commands from the *project root*, the folder that contains `Cargo.toml`. With Cargo, pass arguments after `--`: `cargo run -- red blue`. **Dependencies** (called *crates*) are listed in `Cargo.toml` and downloaded from crates.io; `Cargo.lock` records the exact versions so that every machine builds the same way. The standard library is enough for this course, so do not add a crate to a small exercise.

### Worked Example

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    println!("Argument count: {}", args.len());
    for (index, arg) in args.iter().enumerate() {
        println!("Argument {}: {}", index + 1, arg);
    }
    if args.is_empty() {
        println!("No arguments were given.");
    }
}
```

### Expected Behavior or Output

Run with the command-line arguments `red blue`.

The program prints:
```text
Argument count: 2
Argument 1: red
Argument 2: blue
```

With no arguments it prints:
```text
Argument count: 0
No arguments were given.
```

### Common Mistakes
1. Forgetting `--`, so Cargo treats `red` as its own option.
2. Forgetting that the first item of `args()` is the program name.
3. Adding a crate for something the standard library already does.

### Activities
1. Run the program with `red blue` and then with no arguments. Compare the output.
2. Pass three words and a number and print the number plus one (use `parse`).
3. Print the arguments in reverse order.
4. Explain what `Cargo.lock` is for.

### Accessibility Practice

Arguments let you test a program without answering prompts, so every run produces plain text read in order. Read the output of the two runs aloud and compare them line by line.

### Skills Checklist
- [ ] I can run a program with arguments.
- [ ] I know the first item is the program name.
- [ ] I can pass arguments through Cargo.
- [ ] I know what a crate is.
- [ ] I can say where the project root is.

---
>>>>>>> 2067a20 (curriculum clearning and updates)
