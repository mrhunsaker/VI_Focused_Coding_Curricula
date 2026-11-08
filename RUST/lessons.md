# Rust: Complete Curriculum — Units 0–11

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

## Course Overview

Rust is a systems programming language designed for memory safety, concurrency, and performance without a garbage collector. It is used for command-line tools, operating-system components, networking, embedded software, WebAssembly, and performance-sensitive services. This course uses the Python curriculum's canonical examples and datasets while teaching Rust idioms: ownership, borrowing, lifetimes, enums, pattern matching, Option, Result, traits, iterators, and RAII.

**Toolchain baseline:** stable Rust with the Rust 2024 edition. Install through rustup; use Cargo for project creation, dependency management, formatting, checking, testing, and builds. The worked examples use the standard library unless a lesson explicitly discusses an ecosystem crate.

**Verification status:** every lesson has one complete Rust program that uses the shared datasets. All 57 programs compile with `rustc` (edition 2021, `-D warnings`) and run independently, and the "Expected Behavior or Output" blocks are the captured output of those programs, with the standard input shown where a program reads input. The two lessons that contain a `#[cfg(test)]` module also had that module compiled with `--test` and run. This has not been tested with screen readers or braille displays. Rust prints the shared tip as 3.67 with `{:.2}`; Java and Kotlin print 3.68 for the same stored value.

# Unit 0: Accessible Environment and Toolchain

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

# Unit 1: Foundations of Computing

## Overview
This unit develops foundations of computing through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 1.1: Computer science and problem solving

### Reading References
- [The Rust Programming Language: Control Flow](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 1.1: Welcome to Computer Science

### Learning Objectives
- Explain hardware, software, and algorithm in your own words.
- Turn a written algorithm into a short Rust program.
- Predict a program's output by hand before running it.

### Concept Explanation

Computers follow instructions exactly. *Hardware* is the machine, *software* is the set of instructions it follows, and an *algorithm* is an ordered, finite list of clear steps that solves a problem. Unit P of this repository covers these ideas in detail.

A reliable way to solve a problem is to understand it, break it into steps, write the steps in plain language, translate them into code, and test the result.

The plan here is: set a total to zero; for each score, add it to the total; divide the total by the number of scores; report both. In Rust, `let mut total = 0` creates a binding that can change, `for score in scores` visits each item, and `scores.len()` is the number of items. Rust does not convert between number types for you, so the average needs `total as f64 / scores.len() as f64`.

The shared scores are 82, 91, 76, and 88. Their total is 337 and their average is 84.25. A hand trace should reach the same numbers: 82, 173, 249, then 337.

### Worked Example

```rust
fn main() {
    let scores = [82, 91, 76, 88];
    let mut total = 0;
    for score in scores {
        total += score;
    }
    let average = total as f64 / scores.len() as f64;
    println!("Total: {total}");
    println!("Average: {average}");
}
```

### Expected Behavior or Output

The program prints:
```text
Total: 337
Average: 84.25
```

### Common Mistakes
1. Writing code before writing the steps, then forgetting to divide by the number of scores.
2. Dividing two integers and expecting a decimal. `337 / 4` is `84`; convert with `as f64`.
3. Forgetting `mut` and then trying to add to `total`, which is a compile error.

### Activities
1. Trace the loop by hand and write the running total after each score.
2. Change the array to 90 and 80 and predict the total and average before running.
3. Add a loop that finds the highest score and prints it.
4. Explain the difference between the algorithm and the program in two sentences.

### Accessibility Practice

Write the hand trace as numbered sentences, one for each loop pass, and read it back with your screen reader. Compare it with the two printed lines in order.

### Skills Checklist
- [ ] I can define hardware, software, and algorithm.
- [ ] I can describe an algorithm as ordered steps.
- [ ] I can trace a loop by hand.
- [ ] I can explain `mut` and `as f64`.
- [ ] I can run the program and compare it with my trace.

---

## Lesson 1.2: Your first program and sequential execution

### Reading References
- [The Rust Programming Language: Hello, World!](https://doc.rust-lang.org/book/ch01-02-hello-world.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 1.2: Your First Python Program - Hello World

### Learning Objectives
- Write and run a program that prints text.
- Use `println!`, `print!`, and format placeholders.
- Explain that statements run in order.

### Concept Explanation

A Rust program is a list of statements that run in order inside `main`. `println!` writes text and ends the line; `print!` writes without ending the line. Both are *macros* that take a **format string**: `{}` inserts a value, `{name}` inserts a variable by name, `{:?}` inserts a debugging form, and `{:.2}` inserts a decimal with two places. `{{` and `}}` print literal braces.

Text in double quotation marks is a string literal. A line comment starts with `//`, and `///` starts a documentation comment. Because Rust is compiled, a mistake such as a missing quotation mark is reported at compile time and no program is produced.

### Worked Example

```rust
fn main() {
    // This program greets the shared student.
    let name = "Avery";
    println!("Hello, {}!", name);
    print!("No new line here, ");
    println!("then one here.");
    println!("Name has {} letters.", name.len());
    println!("Braces look like {{this}}.");
    println!("Debug form: {:?}", name);
}
```

### Expected Behavior or Output

The program prints:
```text
Hello, Avery!
No new line here, then one here.
Name has 5 letters.
Braces look like {this}.
Debug form: "Avery"
```

### Common Mistakes
1. Forgetting the `!` and writing `println("...")`, which is not a macro call.
2. Writing `{}` without a matching value, which is a compile error.
3. Using a curly quotation mark pasted from a document instead of a straight one.

### Activities
1. Run the program and describe how the second and third lines differ from the others.
2. Change the greeting to use your own name and predict the output.
3. Print three lines: your name, the course name, and today's task.
4. Add a comment above every line and read the file aloud with the comments.

### Accessibility Practice

Run from the terminal and read the output line by line. Check that your screen reader announces the braces in a format string, since they decide what the program prints.

### Skills Checklist
- [ ] I can write and run a program that prints text.
- [ ] I can use format placeholders.
- [ ] I can write comments.
- [ ] I know how `print!` and `println!` differ.
- [ ] I can read a first compile error.

---

## Lesson 1.3: Variables, bindings, mutability, and primitive types

### Reading References
- [The Rust Programming Language: Variables and Mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)
- [The Rust Programming Language: Data Types](https://doc.rust-lang.org/book/ch03-02-data-types.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 1.3: Variables and Simple Data Types

### Learning Objectives
- Declare immutable and mutable bindings and use shadowing.
- Name Rust's basic types and check a value's type.
- Use `const` for fixed values.

### Concept Explanation

`let` creates a *binding*. Bindings are **immutable by default**: `let age = 16;` cannot be reassigned. `let mut visits = 1;` can. *Shadowing* declares a new binding with the same name, `let visits = visits * 10;`, which may even change the type; it is not the same as mutation.

Rust is statically typed with inference. A whole-number literal is an `i32` and a decimal literal is an `f64` unless the context says otherwise; you can write the type (`let big: i64 = 3_000_000_000;`). The basic types are the integers `i8`..`i128` and `u8`..`u128` (`i` signed, `u` unsigned), `f32` and `f64`, `bool`, `char`, and `&str` (a string slice). `const NAME: Type = value;` declares a fixed value that must have a type.

`std::any::type_name::<T>()` reports a type's name. The shared student profile is Avery, 16, 1.72 meters, and Computer Science. Three notebooks at 2.50 cost 7.5.

### Worked Example

```rust
fn type_of<T>(_value: &T) -> &'static str {
    std::any::type_name::<T>()
}

fn main() {
    let name = "Avery";
    let age = 16;
    let height = 1.72;
    let favorite_subject = "Computer Science";
    let likes_cs = true;
    println!("{name}, {age}, {height}, {favorite_subject}, {likes_cs}");
    println!("{} {} {} {}", type_of(&name), type_of(&age), type_of(&height), type_of(&likes_cs));

    let mut visits = 1;
    visits += 1;
    println!("Visits: {visits}");
    let visits = visits * 10;
    println!("Shadowed visits: {visits}");

    const NOTEBOOK_PRICE: f64 = 2.50;
    let notebook_quantity = 3;
    println!("Notebook total: {}", NOTEBOOK_PRICE * notebook_quantity as f64);

    let big: i64 = 3_000_000_000;
    println!("{big}");
}
```

### Expected Behavior or Output

The program prints:
```text
Avery, 16, 1.72, Computer Science, true
&str i32 f64 bool
Visits: 2
Shadowed visits: 20
Notebook total: 7.5
3000000000
```

### Common Mistakes
1. Reassigning a binding declared without `mut`, which is a compile error.
2. Confusing shadowing with mutation. Shadowing makes a new binding.
3. Writing `let big = 3000000000;` and getting an out-of-range error for `i32`.

### Activities
1. Run the example and write each type name in the order printed.
2. Change `age` to `16u8` and predict the type name.
3. Add a `char` initial for the student and print its type.
4. Explain the difference between `let mut x` and shadowing with `let x`.

### Accessibility Practice

Say names with their underscores aloud (`favorite_subject`) and print each value inside a labelled sentence so the screen reader announces the name and the value together.

### Skills Checklist
- [ ] I can declare immutable and mutable bindings.
- [ ] I can use shadowing.
- [ ] I can name Rust's basic types.
- [ ] I can use `const`.
- [ ] I can explain why bindings are immutable by default.

---

# Unit 2: Numeric Computations

## Overview
This unit develops numeric computations through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 2.1: Software design and tracing

### Reading References
- [The Rust Programming Language: Data Types](https://doc.rust-lang.org/book/ch03-02-data-types.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 2.1: The Software Development Process

### Learning Objectives
- Describe the design, implement, and test cycle.
- Write pseudocode for the tip calculator and implement it.
- Explain why money is formatted to two decimals.

### Concept Explanation

Software is built in a cycle: understand the problem, design a solution, implement it, test it, and refine it. For the tip calculator the plan is: get the bill, calculate 15 percent of it as the tip, add the tip to the bill for the total, and print the tip and the total.

With the shared values (bill 24.50, tip rate 0.15) the exact tip is 3.675 and the total is 28.175. `{:.2}` formats an `f64` with two decimals, rounding the exact binary value. The stored tip is 3.67499999999999982, so Rust prints **3.67** and the total **28.18**. Java and Kotlin print 3.68 for the same number because their formatters round half up on the decimal digits. Both displays are correct for the same stored value. `{}` prints the shortest text that reads back as the same number, which is `3.675`.

### Worked Example

```rust
fn main() {
    let bill = 24.5_f64;
    let tip_rate = 0.15;

    let tip = bill * tip_rate;
    let total = bill + tip;

    println!("Bill: {bill:.2}");
    println!("Tip: {tip:.2}");
    println!("Total: {total:.2}");
    println!("Unformatted tip: {tip}");
}
```

### Expected Behavior or Output

The program prints:
```text
Bill: 24.50
Tip: 3.67
Total: 28.18
Unformatted tip: 3.675
```

### Common Mistakes
1. Writing the rate as 15 instead of 0.15, which makes the tip fifteen times too large.
2. Rounding the tip first and then adding it, which can change the total by a cent.
3. Assuming every language prints the same two-decimal text for 3.675.

### Activities
1. Trace the plan with the shared values and write each result as a sentence.
2. Change the rate to 0.20 and predict the tip and total (4.90 and 29.40).
3. Add a test for a bill of 100 with a written expected result before running.
4. Explain in two sentences why Rust prints 3.67 even though the shortest form of the tip is 3.675.

### Accessibility Practice

Print each result on its own labelled line (`Tip: 3.67`) so a screen reader announces one clear unit per line. Never use alignment or spacing to carry meaning.

### Skills Checklist
- [ ] I can name the stages of the development cycle.
- [ ] I can write pseudocode for a calculation.
- [ ] I can format a number with `{:.2}`.
- [ ] I know `{}` and `{:.2}` print differently.
- [ ] I can explain why displays can differ between languages.

---

## Lesson 2.2: Expressions, operators, and assignment

### Reading References
- [The Rust Programming Language: Data Types](https://doc.rust-lang.org/book/ch03-02-data-types.html)
- [The Rust Programming Language: Statements and Expressions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 2.2: Elements of Programs - Expressions and Assignment

### Learning Objectives
- Evaluate expressions using operator precedence.
- Predict integer division, remainder, and overflow behavior.
- Use compound assignment and `as` casts.

### Concept Explanation

An *expression* produces a value. The arithmetic operators are `+`, `-`, `*`, `/`, and `%`. Multiplication, division, and remainder happen before addition and subtraction, and parentheses change the order, so `8 + 4 * 2` is 16 and `(8 + 4) * 2` is 24.

**Division depends on the types.** Two integers give an integer with the fraction dropped toward zero, so `7 / 2` is `3` and `-7 / 2` is `-3`. Rust never mixes number types: `7 / 2.0` does not compile, so convert with `as`: `7 as f64 / 2.0` is `3.5`. The remainder keeps the sign of the left side, so `-7 % 2` is `-1`; `rem_euclid(2)` always gives 0 or 1.

Integers have a fixed size. In a *debug* build an addition that overflows stops the program with a panic, and in a *release* build it wraps around silently. Use `checked_add` (returns `None` on overflow) or `wrapping_add` when overflow matters. Assignment is `score = score + 9`, shortened to `score += 9`, and needs `mut`.

### Worked Example

```rust
fn main() {
    println!("{}", 8 + 4 * 2);
    println!("{}", (8 + 4) * 2);

    let mut score = 82;
    score += 9;
    println!("New score: {score}");

    println!("{}", 7 / 2);
    println!("{}", 7 as f64 / 2.0);
    println!("{}", 7 % 2);
    println!("{}", -7 / 2);
    println!("{}", -7 % 2);
    println!("{}", (-7_i32).rem_euclid(2));
    println!("{}", 5 != 6);
    println!("{:?}", i32::MAX.checked_add(1));
    println!("{}", format!("{} {}", "Avery", "Student"));
}
```

### Expected Behavior or Output

The program prints:
```text
16
24
New score: 91
3
3.5
1
-3
-1
1
true
None
Avery Student
```

### Common Mistakes
1. Expecting `7 / 2` to be `3.5`. With two integers the fraction is dropped.
2. Writing `7 / 2.0`, which does not compile because the types differ.
3. Relying on silent wrap-around on overflow. Use `checked_add` and handle `None`.

### Activities
1. Predict the eleven output lines before running, then compare.
2. Write an expression for the area and the perimeter of a 12 by 8 rectangle.
3. Explain why `-7 / 2` prints `-3` rather than `-4`.
4. Use `wrapping_add` to show what `i32::MAX + 1` would wrap to.

### Accessibility Practice

Say operators by name when reading code aloud ('slash', 'percent', 'plus equals'). Raise your punctuation level while checking expressions so that parentheses and operators are all announced.

### Skills Checklist
- [ ] I can apply operator precedence.
- [ ] I can predict integer division.
- [ ] I can use `as` to convert for division.
- [ ] I can use `checked_add`.
- [ ] I can use `+=`.

---

## Lesson 2.3: Input and output

### Reading References
- [The Rust Programming Language: Programming a Guessing Game](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 2.3: Input and Output Revisited

### Learning Objectives
- Read a line from standard input.
- Convert text with `parse` and handle failure.
- Handle missing and invalid input.

### Concept Explanation

`std::io::stdin().read_line(&mut line)` appends the next line to a `String` you own and returns a `Result` holding the number of bytes read. A result of `Ok(0)` means the input has ended. The line keeps its line ending, so call `trim()`.

Typed text is always text. `text.parse::<i32>()` returns a `Result`: `Ok(number)` or `Err(error)`. `.ok()` turns a `Result` into an `Option`, discarding the error, and the `?` operator in a function that returns `Option` stops early with `None`. Rust has no null; a value that may be missing is an `Option`.

The example reads a name and two numbers and prints a greeting and their sum. With Avery, 12, and 8 the sum is 20. Prompts are printed on their own lines so the screen reader reads each cleanly.

### Worked Example

```rust
use std::io;

fn read_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn read_number() -> Option<i32> {
    read_line()?.parse().ok()
}

fn main() {
    println!("Enter your name:");
    let name = read_line();
    println!("Enter the first number:");
    let first = read_number();
    println!("Enter the second number:");
    let second = read_number();

    match (name, first, second) {
        (Some(name), Some(first), Some(second)) => {
            println!("Hello, {name}!");
            println!("The sum of {first} and {second} is {}.", first + second);
        }
        _ => println!("Input was missing or not a number."),
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
Avery
12
8
```

the program prints:
```text
Enter your name:
Enter the first number:
Enter the second number:
Hello, Avery!
The sum of 12 and 8 is 20.
```

With no standard input at all, the program ends cleanly and prints:
```text
Enter your name:
Enter the first number:
Enter the second number:
Input was missing or not a number.
```

### Common Mistakes
1. Forgetting `trim()`, so the line ending makes `parse` fail.
2. Calling `unwrap()` on a `parse` result and crashing on `abc`.
3. Forgetting that `read_line` returns `Ok(0)` at the end of input and looping forever.

### Activities
1. Run with Avery, 12, and 8 and confirm the output.
2. Type `twelve` for the first number and explain the result.
3. Run with no input and describe the output.
4. Change the program to subtract the second number from the first.

### Accessibility Practice

Every prompt is a complete sentence on its own line and every result is a complete sentence. When you test, listen for whether the prompt is read in full before you begin to type.

### Skills Checklist
- [ ] I can read a line with `read_line`.
- [ ] I can convert text with `parse`.
- [ ] I handle `Ok(0)` at the end of input.
- [ ] I can write clear prompts.
- [ ] I handle missing and invalid input.

---

## Lesson 2.4: Numeric types, conversions, and math

### Reading References
- [The Rust Programming Language: Data Types](https://doc.rust-lang.org/book/ch03-02-data-types.html)
- [Rust by Example: Casting](https://doc.rust-lang.org/rust-by-example/types/cast.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 2.4: Computing with Numbers and Type Conversions

### Learning Objectives
- Convert between text and numbers with `parse`.
- Explain what `as` does and when `try_from` is safer.
- Explain why decimal arithmetic is approximate.

### Concept Explanation

`"16".parse::<i32>()` converts text and returns a `Result`; invalid text gives an `Err` whose message is readable, for example `invalid digit found in string`. `to_string()` converts a number to text.

`as` converts between number types and **never fails**: `3.9_f64 as i32` is `3` (the fraction is truncated), and `300_i32 as u8` is `44` (the value wraps). When a lossy conversion would be a bug, use `i32::try_from(value)` or `u8::try_from(value)`, which return a `Result`. `f64::round()` rounds halves away from zero.

A float is a binary approximation. `0.1 + 0.2` prints `0.30000000000000004`, not `0.3`; this is correct behavior. Compare decimals with a tolerance and format them for display.

The shared student has age 16 and height 1.72 meters; the example converts text to those values and computes the height in centimeters.

### Worked Example

```rust
fn main() {
    let age: i32 = "16".parse().unwrap_or(0);
    let height: f64 = "1.72".parse().unwrap_or(0.0);
    println!("{age} {height}");

    match "abc".parse::<i32>() {
        Ok(number) => println!("number {number}"),
        Err(error) => println!("abc is not a whole number: {error}"),
    }
    println!("{} is now text", 42.to_string());

    println!("{}", 3.9_f64 as i32);
    println!("{}", 3.5_f64.round());
    println!("{}", 300_i32 as u8);
    println!("{:?}", u8::try_from(300_i32).is_err());
    println!("{}", 0.1 + 0.2);

    let height_cm = height * 100.0;
    println!("Height in centimeters: {height_cm:.1}");
}
```

### Expected Behavior or Output

The program prints:
```text
16 1.72
abc is not a whole number: invalid digit found in string
42 is now text
3
4
44
true
0.30000000000000004
Height in centimeters: 172.0
```

### Common Mistakes
1. Using `as` for a lossy conversion and not noticing that the value was truncated or wrapped.
2. Calling `unwrap()` on untrusted text and crashing on `abc`.
3. Comparing decimals with `==` after arithmetic.

### Activities
1. Predict each output line before running, then compare.
2. Check what `" 16 ".parse::<i32>()` does and explain the result.
3. Write a function that returns `Option<i32>` for text that may not be a number.
4. Explain the difference between `3.5 as i32` and `3.5_f64.round()`.

### Accessibility Practice

Format floating-point results so the screen reader reads short numbers. Read the error text aloud when a parse fails; it is written to be understood in words.

### Skills Checklist
- [ ] I can convert between text and numbers.
- [ ] I know `as` never fails.
- [ ] I can use `try_from` for safe conversion.
- [ ] I can handle a parse error.
- [ ] I can explain why decimals are approximate.

---

## Lesson 2.5: Mathematical functions, circle geometry, and distance

### Reading References
- [f64 documentation](https://doc.rust-lang.org/std/primitive.f64.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 2.5: Using the Math Library

### Learning Objectives
- Use `PI`, `powi`, `sqrt`, and `hypot`.
- Compute circle area and circumference.
- Compute the distance from the origin.

### Concept Explanation

Rust has no separate math library to import for common work: numeric types have methods. `f64` provides `sqrt()`, `powi(n)` (an integer power), `powf(x)`, `abs()`, `floor()`, `ceil()`, `round()`, `hypot(other)`, `max(other)`, and `min(other)`. Constants such as `PI` live in `std::f64::consts`. Integers have `abs()`, `max`, `min`, and `pow`.

For a circle of radius 5 the area is `PI * radius.powi(2)` (about 78.54) and the circumference is `2.0 * PI * radius` (about 31.42). `x.hypot(y)` computes the distance from the origin, so the shared point (3, 4) is exactly 5.0 away. `81.0_f64.sqrt()` is `9`, which prints as `9` with `{}`.

Literals need the right type: `2.0 * PI` is valid but `2 * PI` is not, because an integer cannot be multiplied by a float.

### Worked Example

```rust
use std::f64::consts::PI;

fn main() {
    let radius = 5.0_f64;
    let area = PI * radius.powi(2);
    let circumference = 2.0 * PI * radius;
    println!("Area: {area:.2}");
    println!("Circumference: {circumference:.2}");

    println!("{}", 81.0_f64.sqrt());
    println!("Distance from origin: {:.2}", 3.0_f64.hypot(4.0));
    println!("{} {} {}", 82.max(91), 76.min(88), (-5_i32).abs());
}
```

### Expected Behavior or Output

The program prints:
```text
Area: 78.54
Circumference: 31.42
9
Distance from origin: 5.00
91 76 5
```

### Common Mistakes
1. Writing `2 * PI`, which does not compile because an integer cannot multiply a float.
2. Writing the area as `PI * radius * 2`; the radius must be squared.
3. Forgetting `use std::f64::consts::PI;` so `PI` is not found.

### Activities
1. Predict each printed line and then run the program.
2. Compute the area for radius 2.5 by hand and with the program.
3. Change the point to (6, 8) and predict the distance before running.
4. Print the larger of two shared scores using `max`.

### Accessibility Practice

Round results with `{:.2}` so the screen reader announces `78.54` rather than fifteen digits. Say 'colon colon' aloud in `std::f64::consts::PI` and check that your screen reader announces both colons.

### Skills Checklist
- [ ] I can use `f64` methods.
- [ ] I can compute circle area and circumference.
- [ ] I can compute distance with `hypot`.
- [ ] I can format results to two decimals.
- [ ] I know literals need matching types.

---

# Unit 3: Control Flow

## Overview
This unit develops control flow through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 3.1: Boolean expressions and if expressions

### Reading References
- [The Rust Programming Language: Control Flow](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 3.1: Boolean Expressions and if Statements

### Learning Objectives
- Write comparisons and combine them with `&&`, `||`, and `!`.
- Use `if` as an expression.
- Explain that a condition must be a `bool`.

### Concept Explanation

A *Boolean expression* is `true` or `false`. Comparisons use `==`, `!=`, `<`, `<=`, `>`, `>=`, and conditions combine with `&&`, `||`, and `!`. Rust never treats 0, an empty string, or an `Option` as a condition: it must be a real `bool`. `&&` and `||` short-circuit.

In Rust, **`if` is an expression**: `let label = if score >= 90 { "high" } else { "not high" };` produces a value, so both branches must have the same type and `else` is required. `(80..=89).contains(&score)` tests a range, both ends included. `Option::is_some_and(|t| ...)` checks a possibly missing value safely.

The shared score is 82. It passes (at least 60), it is in the 80 to 89 range, and it is not at least 90.

### Worked Example

```rust
fn main() {
    let score = 82;

    if score >= 60 {
        println!("Avery passed.");
    } else {
        println!("Avery did not pass.");
    }

    println!("{}", score >= 80 && score < 90);
    println!("{}", score < 60 || score > 100);
    println!("{}", !(score >= 90));
    println!("{}", (80..=89).contains(&score));

    let label = if score >= 90 { "high" } else { "not high" };
    println!("{label}");

    let text: Option<&str> = None;
    println!("{}", text.is_some_and(|t| !t.is_empty()));
}
```

### Expected Behavior or Output

The program prints:
```text
Avery passed.
true
false
true
true
not high
false
```

### Common Mistakes
1. Writing `if score {`, which does not compile because `score` is not a `bool`.
2. Giving the two branches of an `if` expression different types, which is a compile error.
3. Forgetting `else` when `if` is used for its value.

### Activities
1. Change the score to 59 and predict which lines change.
2. Write a condition that is true only for scores from 70 to 79 inclusive, in two ways.
3. Rewrite the `label` line as an `if` statement.
4. Explain why `if score` is not allowed in Rust.

### Accessibility Practice

Read each condition aloud with 'greater than or equal to', 'and', 'or', and 'not'. Check that your screen reader announces `&&` and `||` so you do not confuse them with single symbols.

### Skills Checklist
- [ ] I can write comparisons and combine them.
- [ ] I can write `if` and `else`.
- [ ] I can use `if` as an expression.
- [ ] I can test a range with `contains`.
- [ ] I know conditions must be `bool`.

---

## Lesson 3.2: Chained conditionals and grade classification

### Reading References
- [The Rust Programming Language: The match Control Flow Construct](https://doc.rust-lang.org/book/ch06-02-match.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 3.2: Chained Conditionals (elif, else)

### Learning Objectives
- Use `else if` to test conditions in order.
- Use `match` with ranges for the same decision.
- Classify the shared grade thresholds and test the boundaries.

### Concept Explanation

Rust has no `elif`; write `else if`. Conditions are tested from top to bottom and only the first true branch runs. The shared grade thresholds are 90 or more for A, 80 or more for B, 70 or more for C, 60 or more for D, and anything lower for F.

`match` compares a value against *patterns* and the compiler checks that every case is covered. A pattern can be a range: `90..=100 => "A"`. The final `_` arm catches everything else, which here is any score outside 0 to 100 (so invalid scores are reported instead of silently graded).

*Boundary scores* sit exactly on or just below a threshold. The scores 90, 89, 80, 79, 70, 69, 60, and 59 check every boundary.

### Worked Example

```rust
fn classify(score: i32) -> &'static str {
    if score >= 90 {
        "A"
    } else if score >= 80 {
        "B"
    } else if score >= 70 {
        "C"
    } else if score >= 60 {
        "D"
    } else {
        "F"
    }
}

fn classify_with_match(score: i32) -> &'static str {
    match score {
        90..=100 => "A",
        80..=89 => "B",
        70..=79 => "C",
        60..=69 => "D",
        0..=59 => "F",
        _ => "invalid",
    }
}

fn main() {
    for score in [90, 89, 80, 79, 70, 69, 60, 59, 101] {
        println!("{} {} {}", score, classify(score), classify_with_match(score));
    }
}
```

### Expected Behavior or Output

The program prints:
```text
90 A A
89 B B
80 B B
79 C C
70 C C
69 D D
60 D D
59 F F
101 A invalid
```

### Common Mistakes
1. Putting the branches in the wrong order, such as testing `score >= 60` first so every passing score is a D.
2. Using `>` instead of `>=`, so exactly 90 receives a B.
3. Leaving gaps in a `match` on integers, which the compiler rejects until you add `_`.

### Activities
1. Trace the score 82 through each branch and say which one runs.
2. Add the scores 100, 0, and -5 and predict the results of both functions.
3. Reorder the `if` branches so `score >= 60` is first, run it, and explain the wrong output.
4. Write `is_passing(score: i32) -> bool` using `match`.

### Accessibility Practice

Read the nine output lines in order. Each is a number and two words, so they are easy to follow by ear and in braille; the last line shows how the two functions treat an invalid score.

### Skills Checklist
- [ ] I can write an `else if` chain.
- [ ] I know branch order matters.
- [ ] I can write a `match` with ranges.
- [ ] I can choose boundary tests.
- [ ] I can classify with the shared thresholds.

---

## Lesson 3.3: Arrays, vectors, and indexing

### Reading References
- [The Rust Programming Language: Storing Lists of Values with Vectors](https://doc.rust-lang.org/book/ch08-01-vectors.html)
- [The Rust Programming Language: The Array Type](https://doc.rust-lang.org/book/ch03-02-data-types.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 3.3: Introduction to Lists

### Learning Objectives
- Create an array and a vector.
- Index from 0 and use `get` for checked access.
- Explain the difference between an array and a vector.

### Concept Explanation

An *array* has a fixed length that is part of its type: `[i32; 4]`. A *vector*, `Vec<i32>`, can grow and is created with `vec![82, 91, 76, 88]`. Indexes start at 0, `scores[0]` is the first item, and `len()` is the length. Indexing outside the collection with `[]` stops the program with a *panic*. `scores.get(index)` returns an `Option`: `Some(&value)` or `None`, so a missing item is handled instead of crashing. `last()` and `first()` return `Option` too.

`{:?}` prints a collection in a readable one-line form. To change an element, the collection must be declared `mut`. The shared list is 82, 91, 76, 88; Python uses the same 0-based indexes.

### Worked Example

```rust
fn main() {
    let mut array = [82, 91, 76, 88];
    println!("{} {} {}", array[0], array[array.len() - 1], array.len());
    array[2] = 80;
    println!("{:?}", array);

    let scores = vec![82, 91, 76, 88];
    println!("{:?}", scores.get(1));
    println!("{:?}", scores.get(10));
    println!("{:?}", scores.last());
    println!("{}", scores.len());

    match scores.get(10) {
        Some(value) => println!("Found {value}"),
        None => println!("Index 10 is outside the list"),
    }
}
```

### Expected Behavior or Output

The program prints:
```text
82 88 4
[82, 91, 80, 88]
Some(91)
None
Some(88)
4
Index 10 is outside the list
```

### Common Mistakes
1. Using `scores[10]` on a short vector and crashing with a panic instead of using `get`.
2. Using index 1 for the first item. The first item is at index 0.
3. Trying to change an element of a collection that was not declared `mut`.

### Activities
1. Predict each output line before running.
2. Replace the second score with 95 in both the array and the vector and print them.
3. Make a copy of the vector with `clone()` and show that changing the original does not change the copy.
4. Explain when an array is better than a vector.

### Accessibility Practice

Print a whole collection on one line and its length on another, so the screen reader announces a complete state in one pass. When reading `scores[0]` aloud, say 'scores, open bracket, zero, close bracket'.

### Skills Checklist
- [ ] I can create arrays and vectors.
- [ ] I can index from 0.
- [ ] I can use `get` for checked access.
- [ ] I know `Option` means a value may be missing.
- [ ] I can copy a vector.

---

## Lesson 3.4: For loops and iteration

### Reading References
- [The Rust Programming Language: Repetition with Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
- [The Rust Programming Language: Processing a Series of Items with Iterators](https://doc.rust-lang.org/book/ch13-02-iterators.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 3.4: Iterating with for Loops

### Learning Objectives
- Use `for`, ranges, and `enumerate`.
- Compute the total and average of the shared scores.
- Use `while` and `loop` with `break`.

### Concept Explanation

`for item in collection` visits every element. A range `1..=3` includes both ends and `1..3` excludes the end; `(1..=10).rev().step_by(3)` counts down by 3. `iter().enumerate()` gives each item with its position. Looping over `&scores` borrows the vector, so it can still be used afterward; looping over `scores` itself would *move* it.

Iterators can summarize without an explicit loop: `scores.iter().sum::<i32>()` adds a vector's items. A loop is still the way to learn what such a call does. `while condition { ... }` repeats while a condition is true, and `loop { ... }` repeats until a `break`, which can give back a value.

The shared scores 82, 91, 76, 88 total 337 and average 84.25. Convert the integers with `as f64` before dividing.

### Worked Example

```rust
fn main() {
    let scores = vec![82, 91, 76, 88];
    let mut total = 0;
    for (index, score) in scores.iter().enumerate() {
        println!("Adding score {}: {}", index + 1, score);
        total += score;
    }
    println!("Total: {total}");
    println!("Average: {}", total as f64 / scores.len() as f64);
    println!("Same total with an iterator: {}", scores.iter().sum::<i32>());

    for i in 1..=3 {
        println!("Count: {i}");
    }
    for i in (1..=10).rev().step_by(3) {
        println!("Step: {i}");
    }

    let mut count = 3;
    while count > 0 {
        println!("Countdown: {count}");
        count -= 1;
    }

    let mut tries = 0;
    let found = loop {
        tries += 1;
        if tries == 4 {
            break tries * 10;
        }
    };
    println!("Found {found}");
}
```

### Expected Behavior or Output

The program prints:
```text
Adding score 1: 82
Adding score 2: 91
Adding score 3: 76
Adding score 4: 88
Total: 337
Average: 84.25
Same total with an iterator: 337
Count: 1
Count: 2
Count: 3
Step: 10
Step: 7
Step: 4
Step: 1
Countdown: 3
Countdown: 2
Countdown: 1
Found 40
```

### Common Mistakes
1. Looping over `scores` (not `&scores`) and then using `scores` again, which is a compile error because the vector was moved.
2. Writing `1..3` and expecting it to include 3.
3. Dividing the integer total by the length and getting a truncated result.

### Activities
1. Predict the last nine output lines before running.
2. Change the loop to print only the scores above 80.
3. Write a loop that counts from 20 down to 0 by 5.
4. Explain why the average prints `84.25` and not `84`.

### Accessibility Practice

Each output line starts with a label and a number, so the running total is read step by step. Count the lines to confirm that the loop ran four times.

### Skills Checklist
- [ ] I can write `for` loops with ranges.
- [ ] I can use `enumerate`.
- [ ] I can total and average a vector.
- [ ] I know `&scores` borrows and `scores` moves.
- [ ] I can use `while` and `loop`.

---

## Lesson 3.5: Strings and string slices

### Reading References
- [The Rust Programming Language: Storing UTF-8 Encoded Text with Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 3.5: Basic String Operations

### Learning Objectives
- Use `len`, `to_lowercase`, `contains`, `find`, and `trim`.
- Explain `String` versus `&str` and byte length versus characters.
- Normalize a name and search the shared text sample.

### Concept Explanation

Rust has two main string types. `&str` is a borrowed *string slice* (a string literal is one). `String` is an owned, growable string. Both hold **UTF-8** text, so `len()` counts **bytes**, not characters: `"héllo".len()` is 6 but `"héllo".chars().count()` is 5. For ASCII text, the two agree.

Useful methods: `trim()`, `to_lowercase()`, `to_uppercase()`, `contains(text)`, `find(text)` (returns `Option<usize>`, a byte position), `matches(text).count()` (non-overlapping matches), `replace(from, to)`, and slicing `&text[..9]`. Slicing at a position that is not a character boundary panics.

Strings are not changed by these methods; each returns a new `String`. The shared text sample is "A student studies programming. Programming develops problem-solving skills." It has 75 characters and contains `programming` twice (once in each case), first found at index 18 after lowercasing.

### Worked Example

```rust
fn main() {
    let raw_name = "  avery  ";
    let stripped = raw_name.trim();
    let mut chars = stripped.chars();
    let clean_name = match chars.next() {
        Some(first) => first.to_uppercase().collect::<String>() + chars.as_str(),
        None => String::new(),
    };
    println!("Name: '{clean_name}'");

    let text = "A student studies programming. Programming develops problem-solving skills.";
    let lowered = text.to_lowercase();
    println!("Characters: {}", text.len());
    println!("Contains 'programming': {}", lowered.contains("programming"));
    println!("First index of 'programming': {:?}", lowered.find("programming"));
    println!("Times 'programming' appears: {}", lowered.matches("programming").count());
    println!("Missing word index: {:?}", lowered.find("rust"));

    let upper = text.to_uppercase();
    println!("{}", &upper[..9]);
    println!("{} bytes, {} characters", "héllo".len(), "héllo".chars().count());
}
```

### Expected Behavior or Output

The program prints:
```text
Name: 'Avery'
Characters: 75
Contains 'programming': true
First index of 'programming': Some(18)
Times 'programming' appears: 2
Missing word index: None
A STUDENT
6 bytes, 5 characters
```

### Common Mistakes
1. Treating `len()` as the number of characters for text that is not ASCII.
2. Slicing with `&text[..n]` at a position inside a multi-byte character, which panics.
3. Expecting `find` to return `-1` when the text is missing. It returns `None`.

### Activities
1. Predict the printed values, then run and compare.
2. Find the index of the word `student` in the sample text.
3. Replace every `programming` with `coding` and print the result.
4. Write code that trims and capitalizes `"  riley  "`.

### Accessibility Practice

Strings with many quotation marks are hard to read by ear. Say 'single quote' and 'double quote' aloud when checking a line, and print results inside labelled sentences so values are not run together.

### Skills Checklist
- [ ] I can use common string methods.
- [ ] I know `String` versus `&str`.
- [ ] I know `len()` counts bytes.
- [ ] I can search text and find positions.
- [ ] I can trim and capitalize a name.

---

# Unit 4: Data Structures

## Overview
This unit develops data structures through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 4.1: Vectors and collection mutation

### Reading References
- [The Rust Programming Language: Vectors](https://doc.rust-lang.org/book/ch08-01-vectors.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 4.1: More on Lists

### Learning Objectives
- Push, insert, replace, and remove vector items.
- Remove by value using `position` and by condition using `retain`.
- Handle an empty `pop` with `Option`.

### Concept Explanation

A `Vec` changes with `push(value)` (append), `insert(index, value)` (insert and shift), `scores[i] = value` (replace), `remove(index)` (remove by **position** and return the item), `pop()` (remove and return the last item as an `Option`, because the vector might be empty), and `retain(|item| condition)` (keep only matching items). Rust has no "remove by value"; find the position first with `iter().position(|&s| s == value)`, which returns an `Option<usize>`.

`contains(&value)` tests membership. All of these methods need the vector to be declared `mut`, and Rust checks at compile time that nothing else holds a borrow of the vector while it changes.

The example applies the same operations as the Python course to the shared scores, from [82, 91, 76, 88] to [82, 85, 93, 88].

### Worked Example

```rust
fn main() {
    let mut scores = vec![82, 91, 76, 88];

    scores.push(95);
    scores.insert(1, 85);
    scores[2] = 93;
    if let Some(position) = scores.iter().position(|&s| s == 76) {
        scores.remove(position);
    }
    let last = scores.pop();

    println!("{:?}", scores);
    println!("{} items; removed {:?}", scores.len(), last);
    println!("{}", scores.contains(&88));
    println!("{:?}", scores.iter().position(|&s| s == 88));
    println!("{:?}", scores.iter().position(|&s| s == 100));

    scores.retain(|&s| s >= 90);
    println!("{:?}", scores);
}
```

### Expected Behavior or Output

The program prints:
```text
[82, 85, 93, 88]
4 items; removed Some(95)
true
Some(3)
None
[93]
```

### Common Mistakes
1. Looking for a `remove_value` method. Find the position first, then remove by index.
2. Calling `remove(index)` with an index that is too large, which panics.
3. Holding a reference into the vector (`let first = &scores[0];`) and then calling `push`, which the borrow checker rejects.

### Activities
1. Trace the vector after every operation and write each version as a sentence.
2. Remove the first score with `remove(0)` and describe what happens to the others.
3. Remove every score below 80 with `retain`.
4. Print the position of the first score above 90.

### Accessibility Practice

After every change, print the whole vector on one line so the screen reader reads a complete state in one pass. Say the method names aloud and notice how `remove` and `retain` differ in what they take.

### Skills Checklist
- [ ] I can push, insert, replace, and remove items.
- [ ] I can find a position with `position`.
- [ ] I can filter with `retain`.
- [ ] I know `pop` returns an `Option`.
- [ ] I can show a vector in one line.

---

## Lesson 4.2: Sorting and organizing data

### Reading References
- [The Rust Programming Language: Vectors](https://doc.rust-lang.org/book/ch08-01-vectors.html)
- [Vec sorting methods](https://doc.rust-lang.org/std/vec/struct.Vec.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 4.2: Organizing Lists

### Learning Objectives
- Sort a vector ascending and descending.
- Sort a clone so the original is unchanged.
- Sort by a computed key and sort decimals.

### Concept Explanation

`sort()` sorts a `mut` vector **in place**, smallest first. `sort_by(|a, b| b.cmp(a))` takes a comparison closure, here reversing the order to get descending. `sort_by_key(|w| w.len())` sorts by a computed key and keeps equal keys in their original order (the sort is *stable*). `reverse()` flips the current order. To keep the original, sort a `clone()`.

Decimals (`f64`) cannot use `sort()` because `NaN` has no order. Use `sort_by(|a, b| a.partial_cmp(b).unwrap())`, which is safe when the data contains no `NaN`.

The shared scores sort to 76, 82, 88, 91 in ascending order and 91, 88, 82, 76 in descending order.

### Worked Example

```rust
fn main() {
    let scores = vec![82, 91, 76, 88];

    let mut ascending = scores.clone();
    ascending.sort();
    let mut descending = scores.clone();
    descending.sort_by(|a, b| b.cmp(a));
    println!("Original: {:?}", scores);
    println!("Ascending: {:?}", ascending);
    println!("Descending: {:?}", descending);

    let mut in_place = scores.clone();
    in_place.sort();
    in_place.reverse();
    println!("Sorted then reversed in place: {:?}", in_place);

    let mut words = vec!["pencil", "folder", "notebook"];
    words.sort();
    println!("{:?}", words);
    words.sort_by_key(|w| w.len());
    println!("{:?}", words);

    let mut prices = vec![2.5, 0.5, 1.25];
    prices.sort_by(|a, b| a.partial_cmp(b).unwrap());
    println!("{:?}", prices);
}
```

### Expected Behavior or Output

The program prints:
```text
Original: [82, 91, 76, 88]
Ascending: [76, 82, 88, 91]
Descending: [91, 88, 82, 76]
Sorted then reversed in place: [91, 88, 82, 76]
["folder", "notebook", "pencil"]
["folder", "pencil", "notebook"]
[0.5, 1.25, 2.5]
```

### Common Mistakes
1. Calling `sort()` on a vector of `f64`, which does not compile because decimals are only partially ordered.
2. Forgetting `mut` on the vector, so `sort` is rejected.
3. Expecting `sort` to return the sorted vector. It sorts in place and returns nothing.

### Activities
1. Predict each printed line before running.
2. Print the scores in descending order without changing the original.
3. Sort the words by their last letter with `sort_by_key`.
4. Explain why decimals need `partial_cmp`.

### Accessibility Practice

Print each result on its own labelled line (`Ascending:`, `Descending:`). The first and last numbers are the quickest to check by ear.

### Skills Checklist
- [ ] I can sort ascending and descending.
- [ ] I can sort a clone.
- [ ] I can sort by a key.
- [ ] I can sort decimals.
- [ ] I can reverse a vector.

---

## Lesson 4.3: Tuples and immutable values

### Reading References
- [The Rust Programming Language: The Tuple Type](https://doc.rust-lang.org/book/ch03-02-data-types.html)
- [The Rust Programming Language: Using Tuple Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 4.3: Tuples - Immutable Lists

### Learning Objectives
- Create tuples and unpack them by destructuring.
- Declare a tuple struct for a named fixed group.
- Return several values from a function.

### Concept Explanation

A *tuple* groups a fixed number of values that may have different types: `(3, 4)` or `("Avery", 16, 1.72)`. Read a part with `point.0`, or **destructure** the whole tuple: `let (x, y) = point;`. A tuple is immutable unless its binding is `mut`, and its length and types cannot change.

A *tuple struct* gives a tuple a name: `struct Point(i32, i32);` so that two values of different meaning cannot be mixed up. For anything with more than two or three parts, a struct with named fields (Unit 7) reads better.

Functions return several values as a tuple: `fn min_max(values: &[i32]) -> (i32, i32)`. The shared coordinates are x = 3 and y = 4.

### Worked Example

```rust
struct Point(i32, i32);

fn min_max(values: &[i32]) -> (i32, i32) {
    let mut low = values[0];
    let mut high = values[0];
    for &value in values {
        if value < low {
            low = value;
        }
        if value > high {
            high = value;
        }
    }
    (low, high)
}

fn main() {
    let (x, y) = (3, 4);
    println!("x={x} y={y}");

    let point = (3, 4);
    println!("{:?} {} {}", point, point.0, point.1);

    let named = Point(3, 4);
    println!("{} {}", named.0, named.1);

    let moved = (point.0, 10);
    println!("{:?} -> {:?}", point, moved);
    println!("{}", point == (3, 4));

    let (low, high) = min_max(&[82, 91, 76, 88]);
    println!("low={low} high={high}");

    let profile = ("Avery", 16, 1.72);
    println!("{} {} {}", profile.0, profile.1, profile.2);
}
```

### Expected Behavior or Output

The program prints:
```text
x=3 y=4
(3, 4) 3 4
3 4
(3, 4) -> (3, 10)
true
low=76 high=91
Avery 16 1.72
```

### Common Mistakes
1. Trying to assign `point.0 = 5` on a binding that is not `mut`, which is a compile error.
2. Forgetting that `min_max` panics on an empty slice because it reads `values[0]`.
3. Using a tuple where named fields would make the code readable.

### Activities
1. Predict the output, then run.
2. Create a tuple for the shared profile and destructure it into three bindings.
3. Write a function that returns the lowest and highest scores as a tuple and test it with one score.
4. Explain when a tuple is a better choice than a struct.

### Accessibility Practice

Printing a tuple with `{:?}` shows the parentheses and commas, so the screen reader announces `(3, 4)` as a complete phrase. Named fields read better aloud than `.0` and `.1`.

### Skills Checklist
- [ ] I can create and destructure tuples.
- [ ] I can use a tuple struct.
- [ ] I can return several values.
- [ ] I know tuples cannot change length.
- [ ] I can choose between a tuple and a struct.

---

## Lesson 4.4: Hash maps and key-value data

### Reading References
- [The Rust Programming Language: Storing Keys with Associated Values in Hash Maps](https://doc.rust-lang.org/book/ch08-03-hash-maps.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 4.4: Introducing Dictionaries

### Learning Objectives
- Create a `HashMap` and insert, read, and remove entries.
- Handle a missing key with `Option`.
- Model the shared inventory item with a struct.

### Concept Explanation

A `HashMap<K, V>` from `std::collections` pairs keys with values. `insert(key, value)` adds or replaces an entry, `get(&key)` returns an `Option<&V>` (`None` when the key is missing, never a crash), `remove(&key)` deletes one, `contains_key(&key)` tests for a key, and `len()` counts the entries. `entry(key).or_insert(0)` gives a mutable reference to a value, inserting a starting value if the key is new: `*counts.entry("pencil").or_insert(0) += 1;`.

Every value in a map has the **same type**. For a record whose fields have different types, use a struct, as with the shared Notebook item. A `HashMap` has no useful order, so the example prints only counts and single lookups.

### Worked Example

```rust
use std::collections::HashMap;

struct Item {
    name: String,
    quantity: u32,
    unit_price: f64,
}

fn main() {
    let mut profile: HashMap<String, String> = HashMap::new();
    profile.insert("name".to_string(), "Avery".to_string());
    profile.insert("age".to_string(), "16".to_string());
    profile.insert("height_m".to_string(), "1.72".to_string());
    profile.insert("favorite_subject".to_string(), "Computer Science".to_string());

    println!("{:?}", profile.get("name"));
    profile.insert("age".to_string(), "17".to_string());
    profile.insert("grade_level".to_string(), "11".to_string());
    profile.remove("height_m");
    println!("{}", profile.len());
    println!("{:?}", profile.get("height_m"));
    println!("{}", profile.get("height_m").map(String::as_str).unwrap_or("unknown"));
    println!("{}", profile.contains_key("grade_level"));

    let mut counts: HashMap<&str, u32> = HashMap::new();
    *counts.entry("pencil").or_insert(0) += 1;
    *counts.entry("pencil").or_insert(0) += 1;
    println!("{:?}", counts.get("pencil"));

    let mut item = Item { name: "Notebook".to_string(), quantity: 3, unit_price: 2.50 };
    item.quantity += 2;
    println!("{}: {} at {} = {}", item.name, item.quantity, item.unit_price, item.quantity as f64 * item.unit_price);
}
```

### Expected Behavior or Output

The program prints:
```text
Some("Avery")
4
None
unknown
true
Some(2)
Notebook: 5 at 2.5 = 12.5
```

### Common Mistakes
1. Using `profile["height_m"]` on a missing key, which panics. Use `get`.
2. Printing a whole `HashMap` and expecting the same order every run.
3. Trying to store values of different types in one `HashMap`.

### Activities
1. Predict the printed lines before running.
2. Add a `discount` field to `Item` and print the discounted value.
3. Remove `favorite_subject` and show what `get` returns.
4. Explain why a struct is safer than a map of text for a known set of fields.

### Accessibility Practice

Print one lookup per line, because a one-line `{key: value, ...}` form is hard to navigate and has no stable order. Choose key names that read well aloud, such as `favorite_subject`.

### Skills Checklist
- [ ] I can create and change a `HashMap`.
- [ ] I know `get` returns an `Option`.
- [ ] I can use `entry` to count.
- [ ] I know map values share one type.
- [ ] I can model an item with a struct.

---

## Lesson 4.5: Collection traversal and iterators

### Reading References
- [The Rust Programming Language: Iterators](https://doc.rust-lang.org/book/ch13-02-iterators.html)
- [The Rust Programming Language: Hash Maps](https://doc.rust-lang.org/book/ch08-03-hash-maps.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 4.5: Looping Through Dictionaries

### Learning Objectives
- Visit pairs in a stable order.
- Explain why `HashMap` order is unspecified.
- Sort keys with `BTreeMap` and total the shared inventory.

### Concept Explanation

Iterating a `HashMap` visits entries in an **unspecified order that can change between runs**; Rust randomizes it on purpose. For readable, testable output choose a collection with a defined order: a `Vec` of pairs keeps insertion order, and a `BTreeMap` keeps its keys sorted.

`for (name, stock) in &inventory` visits a `Vec` of pairs and borrows it. Iterator methods can summarize: `.iter().map(|(_, s)| ...).sum::<f64>()` totals a computed value, and `.collect()` can build a `BTreeMap` from pairs.

The shared inventory is Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25), worth 7.50 + 5.00 + 5.00 = 17.50.

### Worked Example

```rust
use std::collections::BTreeMap;

struct Stock {
    quantity: u32,
    unit_price: f64,
}

fn main() {
    let inventory = vec![
        ("Notebook", Stock { quantity: 3, unit_price: 2.50 }),
        ("Pencil", Stock { quantity: 10, unit_price: 0.50 }),
        ("Folder", Stock { quantity: 4, unit_price: 1.25 }),
    ];

    println!("Keys:");
    for (name, _) in &inventory {
        println!("{name}");
    }

    println!("Quantities:");
    for (_, stock) in &inventory {
        println!("{}", stock.quantity);
    }

    let mut total_value = 0.0;
    for (name, stock) in &inventory {
        let line_value = stock.quantity as f64 * stock.unit_price;
        println!("{name}: {} in stock, value {line_value:.2}", stock.quantity);
        total_value += line_value;
    }
    println!("Total inventory value: {total_value:.2}");

    let sorted: BTreeMap<&str, u32> = inventory.iter().map(|(name, stock)| (*name, stock.quantity)).collect();
    println!("{:?}", sorted);
    println!("{}", inventory.iter().map(|(_, s)| s.quantity as f64 * s.unit_price).sum::<f64>());
}
```

### Expected Behavior or Output

The program prints:
```text
Keys:
Notebook
Pencil
Folder
Quantities:
3
10
4
Notebook: 3 in stock, value 7.50
Pencil: 10 in stock, value 5.00
Folder: 4 in stock, value 5.00
Total inventory value: 17.50
{"Folder": 4, "Notebook": 3, "Pencil": 10}
17.5
```

### Common Mistakes
1. Using a `HashMap` and expecting the same order every run.
2. Looping over `inventory` instead of `&inventory`, which moves the vector so that it cannot be used again.
3. Forgetting `*name` when building a map from borrowed pairs, which gives a type error.

### Activities
1. Run the example and write the three key-value lines in order.
2. Print only the items with a quantity below 5.
3. Print the items from the highest line value to the lowest.
4. Explain how `BTreeMap` differs from `HashMap`.

### Accessibility Practice

Printing each inventory line as one sentence lets the screen reader announce the name, quantity, and value together. Because the order is stable, you can learn it and compare runs by ear.

### Skills Checklist
- [ ] I can visit pairs in a stable order.
- [ ] I know `HashMap` order is unspecified.
- [ ] I can sort keys with `BTreeMap`.
- [ ] I can total with an iterator.
- [ ] I can total the shared inventory.

---

# Unit 5: Input and Iteration

## Overview
This unit develops input and iteration through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 5.1: Input and validation

### Reading References
- [The Rust Programming Language: Programming a Guessing Game](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 5.1: How the input() Function Works

### Learning Objectives
- Read a line and recognize it as text.
- Convert it safely and handle failure.
- Handle the end of input.

### Concept Explanation

`read_line` appends the next line to a `String` and returns a `Result`; `Ok(0)` means the input has ended. The text keeps its line ending, so `trim()` it. Typed digits are text until you convert them: `text.parse::<i32>()` returns `Ok(number)` or `Err(error)`.

`.ok()` turns a `Result` into an `Option` and `and_then` chains steps that may each fail: `text.as_deref().and_then(|t| t.parse::<i32>().ok())` means "if there is text, and it parses, give the number". A program that reads input must plan for three cases: a valid value, an invalid value, and no value at all. With the typed value 16 the age five years later is 21; the second value, `abc`, is rejected.

### Worked Example

```rust
use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    println!("How old are you?");
    let text = next_line();
    match &text {
        Some(t) => println!("Read: {} characters of text", t.len()),
        None => println!("Read: nothing"),
    }

    let age = text.as_deref().and_then(|t| t.parse::<i32>().ok());
    match age {
        Some(age) => println!("In 5 years: {}", age + 5),
        None => println!("That was not a whole number."),
    }

    println!("Enter another value:");
    let second = next_line().and_then(|t| t.parse::<i32>().ok());
    match second {
        Some(number) => println!("Number: {number}"),
        None => println!("Not a number; the parse returned None."),
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
16
abc
```

the program prints:
```text
How old are you?
Read: 2 characters of text
In 5 years: 21
Enter another value:
Not a number; the parse returned None.
```

With no standard input at all, the program ends cleanly and prints:
```text
How old are you?
Read: nothing
That was not a whole number.
Enter another value:
Not a number; the parse returned None.
```

### Common Mistakes
1. Adding to the text without converting it, which does not compile.
2. Forgetting `trim()`, so the line ending makes `parse` fail.
3. Using `unwrap()` on user input and crashing on `abc`.

### Activities
1. Run with 16 and then `abc` and compare with the shown output.
2. Run with no input and explain every line printed.
3. Accept an age only from 0 to 120.
4. Rewrite the second input with a `match` on the `Result` and print the parse error.

### Accessibility Practice

Each prompt is a complete sentence on its own line. Run the program twice, once typing and once with piped input, and compare what your screen reader announces.

### Skills Checklist
- [ ] I can read a line of input.
- [ ] I can convert and validate it.
- [ ] I handle the end of input.
- [ ] I know typed input is text.
- [ ] I can chain `Option` steps.

---

## Lesson 5.2: While loops and sentinel repetition

### Reading References
- [The Rust Programming Language: Repetition with Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 5.2: The while Loop in Action

### Learning Objectives
- Write a counting `while` loop.
- Write a sentinel loop that ends on a command.
- Stop at the end of input.

### Concept Explanation

`while condition { ... }` repeats while the condition is true, testing **before** each pass. A loop needs a way to make its condition false, normally by changing a variable inside the body: `count += 1` adds one. `while let Some(x) = value { ... }` repeats while a pattern matches.

A *sentinel* is a special input that tells the loop to stop, here the word `quit`. The standard pattern reads once before the loop and again at the end of each pass, and ends when there is no more input (`None`) as well as on `quit`, so the loop stops when input runs out even without `quit`.

The example counts from 1 to 5, then repeats a message prompt until the user types `quit`.

### Worked Example

```rust
use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    let mut count = 1;
    while count <= 5 {
        println!("{count}");
        count += 1;
    }
    println!("Counting finished!");

    println!("Enter a message, or type quit to exit:");
    let mut message = next_line();
    while let Some(text) = &message {
        if text == "quit" {
            break;
        }
        println!("You said: {text}");
        println!("Enter a message, or type quit to exit:");
        message = next_line();
    }
    println!("Goodbye!");
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
hello
scores
quit
```

the program prints:
```text
1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit:
You said: hello
Enter a message, or type quit to exit:
You said: scores
Enter a message, or type quit to exit:
Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit:
Goodbye!
```

### Common Mistakes
1. Forgetting to change the loop variable, which creates an endless loop.
2. Testing for `quit` but not for `None`, so the loop reads forever after input ends.
3. Comparing a `String` with `"quit"` after forgetting that the text still contains its line ending.

### Activities
1. Predict the output for the typed lines hello, scores, and quit.
2. Change the sentinel to `exit` and update the prompt.
3. Count the messages entered and print the count at the end.
4. Rewrite the counting loop as `for count in 1..=5` and compare.

### Accessibility Practice

Each prompt is on its own line and each response begins with `You said:`, so the conversation can be followed in order by ear. If a loop floods the screen reader, stop it with Ctrl+C.

### Skills Checklist
- [ ] I can write a counting `while` loop.
- [ ] I can write a sentinel loop.
- [ ] I test for `None` as well as the sentinel.
- [ ] I update the loop variable.
- [ ] I can use `while let`.

---

## Lesson 5.3: Flags and loop exits

### Reading References
- [The Rust Programming Language: Loop Labels to Disambiguate Between Multiple Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 5.3: Using Flags and break to Exit Loops

### Learning Objectives
- Control a loop with a Boolean flag.
- Leave a loop with `break` and an outer loop with a label.
- Search a collection and remember the position.

### Concept Explanation

A *flag* is a `bool` variable that controls a loop: the loop runs while `running` is true, and the body sets it to `false` to stop. `break` leaves the nearest enclosing loop at once.

A search keeps its answer in an `Option<usize>` (`None` means "not found"), sets it when the item is found, and uses `break`. After the loop, the `Option` says whether a match was found. Positions start at 0. The iterator method `position` does the same search in one line.

A *label* lets `break` leave an outer loop from inside an inner one: write `'outer:` before the outer loop and `break 'outer;` inside.

The shared scores 82, 91, 76, 88 have their first score of 90 or higher at index 1, with the value 91.

### Worked Example

```rust
use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    let mut running = true;
    let mut handled = 0;
    while running {
        println!("Say something, or type quit to stop:");
        match next_line() {
            Some(message) if message != "quit" => {
                handled += 1;
                println!("You said: {message}");
            }
            _ => running = false,
        }
    }
    println!("Messages handled: {handled}");

    let scores = [82, 91, 76, 88];
    let mut found_index = None;
    for (index, &score) in scores.iter().enumerate() {
        if score >= 90 {
            found_index = Some(index);
            break;
        }
    }
    match found_index {
        Some(index) => println!("First score of 90 or higher: {} at index {}", scores[index], index),
        None => println!("No score of 90 or higher."),
    }
    println!("{:?}", scores.iter().position(|&s| s >= 90));

    'outer: for row in 1..=3 {
        for col in 1..=3 {
            if row * col == 4 {
                println!("Stopped at row {row}, column {col}");
                break 'outer;
            }
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
hello
quit
ignored
```

the program prints:
```text
Say something, or type quit to stop:
You said: hello
Say something, or type quit to stop:
Messages handled: 1
First score of 90 or higher: 91 at index 1
Some(1)
Stopped at row 2, column 2
```

With no standard input at all, the program ends cleanly and prints:
```text
Say something, or type quit to stop:
Messages handled: 0
First score of 90 or higher: 91 at index 1
Some(1)
Stopped at row 2, column 2
```

### Common Mistakes
1. Setting the flag but running more code in the same pass that should be skipped.
2. Forgetting to give the result variable a starting value (`None`), then misreading it after the loop.
3. Using `break` in an inner loop and expecting it to leave the outer loop.

### Activities
1. Run with hello and quit and confirm the count is 1.
2. Change the search to the first score below 80 and predict the index.
3. Rewrite the first loop without a flag, using `break`.
4. Explain in two sentences when a flag is clearer than `break`.

### Accessibility Practice

Report search results as complete sentences that include both the value and its position. Remember that Rust indexes start at 0, and say 'index 1' aloud to avoid confusing it with 'the first'.

### Skills Checklist
- [ ] I can control a loop with a flag.
- [ ] I can use `break`.
- [ ] I can use a label to leave an outer loop.
- [ ] I can search with an `Option`.
- [ ] I can explain flag versus `break`.

---

## Lesson 5.4: Continue and filtering

### Reading References
- [The Rust Programming Language: Repetition with Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
- [The Rust Programming Language: Iterators](https://doc.rust-lang.org/book/ch13-02-iterators.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 5.4: Using continue in Loops

### Learning Objectives
- Skip one pass of a loop with `continue`.
- Skip invalid scores in a list.
- Compare `continue` with `filter`.

### Concept Explanation

`continue` skips the rest of the current pass and goes straight to the next one. It is useful for ignoring invalid entries while still reporting them. In a `while` loop, make sure that the loop variable is updated *before* `continue`, or the loop never ends.

An iterator can filter first: `raw.iter().filter(|&&s| (0..=100).contains(&s))` keeps only the valid scores, which is shorter when you do not need to report each skipped entry.

The example skips the invalid scores -5 and 105 in the list 82, -5, 91, 105, 76, 88. The four valid scores total 337.

### Worked Example

```rust
fn main() {
    let raw_scores = [82, -5, 91, 105, 76, 88];
    let mut valid_total = 0;
    let mut valid_count = 0;

    for raw in raw_scores {
        if !(0..=100).contains(&raw) {
            println!("Skipping invalid score: {raw}");
            continue;
        }
        valid_total += raw;
        valid_count += 1;
    }
    println!("Valid scores: {valid_count}, total: {valid_total}");

    for number in 1..=9 {
        if number % 2 == 0 {
            continue;
        }
        println!("{number}");
    }

    let filtered: i32 = raw_scores.iter().filter(|&&s| (0..=100).contains(&s)).sum();
    println!("{filtered}");
}
```

### Expected Behavior or Output

The program prints:
```text
Skipping invalid score: -5
Skipping invalid score: 105
Valid scores: 4, total: 337
1
3
5
7
9
337
```

### Common Mistakes
1. Putting statements that must always run after `continue`, so they are skipped.
2. Using `continue` in a `while` loop before updating the counter, which creates an endless loop.
3. Confusing `continue` (skip this pass) with `break` (leave the loop).

### Activities
1. Predict the printed lines and the final total.
2. Skip scores below 80 instead.
3. Rewrite the first loop with an `if`/`else` and no `continue`.
4. Rewrite it with `filter` and explain what you no longer report.

### Accessibility Practice

Print a line for each skipped entry, so the screen reader announces what was ignored. Never skip silently when a user needs to know what happened to their data.

### Skills Checklist
- [ ] I can use `continue`.
- [ ] I can skip invalid entries.
- [ ] I know where the counter must be updated.
- [ ] I can use `filter` as an alternative.
- [ ] I can tell `continue` from `break`.

---

## Lesson 5.5: Preventing infinite loops

### Reading References
- [The Rust Programming Language: Repetition with Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 5.5: Avoiding Infinite Loops

### Learning Objectives
- Identify what makes a loop stop.
- Add an attempt limit and handle the end of input.
- Write a loop that runs at least once.

### Concept Explanation

An *infinite loop* never ends because its condition never becomes false. Common causes are forgetting to change the loop variable, testing the wrong variable, and waiting for input that never arrives. In a terminal, stop a running program with Ctrl+C. Rust's `loop { ... }` is an *intentional* endless loop and must contain a `break` or `return`.

Protect every loop with a *progress rule* and a *limit*: count attempts, and stop when the limit is reached or the input ends. Rust has no `do ... while`; to run a body at least once, use `loop` and put the exit test at the end.

The example allows three attempts to enter a score from 0 to 100. With the typed lines abc, 105, and 88, the first two are rejected and the third is accepted.

### Worked Example

```rust
use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    let max_attempts = 3;
    let mut attempts = 0;
    let mut score: Option<i32> = None;

    while attempts < max_attempts && score.is_none() {
        attempts += 1;
        println!("Enter a score from 0 to 100 (attempt {attempts} of {max_attempts}):");
        let Some(text) = next_line() else {
            println!("No more input.");
            break;
        };
        match text.parse::<i32>() {
            Ok(number) if (0..=100).contains(&number) => score = Some(number),
            _ => println!("Invalid score: {text}"),
        }
    }

    match score {
        Some(score) => println!("Accepted score: {score}"),
        None => println!("No valid score was entered."),
    }

    let mut count = 1;
    loop {
        println!("{count}");
        count += 1;
        if count > 3 {
            break;
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
abc
105
88
```

the program prints:
```text
Enter a score from 0 to 100 (attempt 1 of 3):
Invalid score: abc
Enter a score from 0 to 100 (attempt 2 of 3):
Invalid score: 105
Enter a score from 0 to 100 (attempt 3 of 3):
Accepted score: 88
1
2
3
```

With no standard input at all, the program ends cleanly and prints:
```text
Enter a score from 0 to 100 (attempt 1 of 3):
No more input.
No valid score was entered.
1
2
3
```

### Common Mistakes
1. Forgetting to increase `attempts`, so the limit is never reached.
2. Writing `loop { ... }` with no `break` or `return`, which never ends.
3. Looking for a `do ... while` loop. Use `loop` with the test at the end.

### Activities
1. Run with abc, 105, and 88 and confirm the accepted score.
2. Run with three invalid lines and read the final message.
3. Change the limit to 5 and test it.
4. For each loop in the example, write down what makes it stop.

### Accessibility Practice

A loop that cannot be stopped is an accessibility problem, because it can flood a screen reader with output. Learn Ctrl+C before running loops, give every input loop a limit, and write error messages that say what is valid.

### Skills Checklist
- [ ] I can name what ends each loop.
- [ ] I can add an attempt limit.
- [ ] I handle the end of input.
- [ ] I can write a loop that runs at least once.
- [ ] I know how to interrupt a program.

---

# Unit 6: Functions

## Overview
This unit develops functions through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 6.1: Defining and calling functions

### Reading References
- [The Rust Programming Language: Functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 6.1: Defining Functions

### Learning Objectives
- Define and call functions.
- Pass parameters and return nothing or a value.
- Store a function in a variable.

### Concept Explanation

A function is declared with `fn name(parameter: Type) -> ReturnType { ... }`. Every parameter names its type, and a function that returns nothing omits the arrow (it returns the empty tuple `()`). Naming follows `snake_case`. The *parameters* are the names in the definition and the *arguments* are the values you pass; they are matched by position.

Functions are values. A *function pointer* type such as `fn(f64, f64)` can hold a function, so `let reference: fn(f64, f64) = show_tip;` stores one and `reference(100.0, 0.2)` calls it. The `main` function is just a function the runtime calls first.

The example defines greetings and a reusable tip calculator using the shared values: a bill of 24.50 and a tip rate of 0.15.

### Worked Example

```rust
fn greet_user() {
    println!("Hello, Rust programmer!");
}

fn greet_name(name: &str) {
    println!("Hello, {name}!");
}

fn show_tip(bill: f64, tip_rate: f64) {
    let tip = bill * tip_rate;
    println!("Tip: {tip:.2}");
    println!("Total: {:.2}", bill + tip);
}

fn main() {
    greet_user();
    greet_user();
    greet_name("Avery");
    greet_name("Riley");
    show_tip(24.5, 0.15);

    let reference: fn(f64, f64) = show_tip;
    reference(100.0, 0.2);
}
```

### Expected Behavior or Output

The program prints:
```text
Hello, Rust programmer!
Hello, Rust programmer!
Hello, Avery!
Hello, Riley!
Tip: 3.67
Total: 28.18
Tip: 20.00
Total: 120.00
```

### Common Mistakes
1. Writing `greet_user;` without parentheses, which is not a call.
2. Passing arguments in the wrong order, such as `show_tip(0.15, 24.5)`.
3. Omitting a parameter's type, which is a compile error.

### Activities
1. Call `show_tip(100.0, 0.2)` yourself and predict both lines.
2. Write `describe_student(name: &str, age: u32)` that prints one sentence.
3. Call `greet_name()` with no argument and read the compiler message.
4. Explain the difference between a parameter and an argument.

### Accessibility Practice

Choose function names that read as actions when spoken, such as `show_tip`. Print complete sentences from a function so the screen reader announces each call's result separately.

### Skills Checklist
- [ ] I can define and call a function.
- [ ] I can distinguish parameters from arguments.
- [ ] I know every parameter needs a type.
- [ ] I can store a function in a variable.
- [ ] I can read a function signature aloud.

---

## Lesson 6.2: Parameters, ownership, and borrowing

### Reading References
- [The Rust Programming Language: What Is Ownership?](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)
- [The Rust Programming Language: References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 6.2: Passing Arguments

### Learning Objectives
- Explain moving versus borrowing a value.
- Use a struct with `Default` in place of default and named arguments.
- Pass a reference to read data without taking it.

### Concept Explanation

Rust has no default arguments and no named arguments. A struct with `Default` gives both: `TipOptions { bill: 24.5, ..Default::default() }` names each field and fills the rest from the default, here a tip rate of 0.15.

Passing a value to a function normally **moves** it: the function owns it, and the caller can no longer use it. Passing a **reference**, `&name`, lets the function *borrow* the value to read it, and the caller keeps ownership. `&mut` borrows it for changing, and Rust allows either many readers or one writer at a time.

With the shared bill of 24.50, the total at the default rate 0.15 is 28.18, at 0.20 it is 29.40, and at 0.10 it is 26.95.

### Worked Example

```rust
struct TipOptions {
    bill: f64,
    tip_rate: f64,
}

impl Default for TipOptions {
    fn default() -> Self {
        TipOptions { bill: 0.0, tip_rate: 0.15 }
    }
}

fn calculate_total(options: &TipOptions) -> f64 {
    options.bill + options.bill * options.tip_rate
}

fn borrow_length(text: &String) -> usize {
    text.len()
}

fn take_ownership(text: String) {
    println!("The function now owns {text}");
}

fn main() {
    let default_rate = TipOptions { bill: 24.5, ..Default::default() };
    let high = TipOptions { bill: 24.5, tip_rate: 0.20 };
    let low = TipOptions { tip_rate: 0.10, bill: 24.5 };
    println!("{:.2}", calculate_total(&default_rate));
    println!("{:.2}", calculate_total(&high));
    println!("{:.2}", calculate_total(&low));

    let name = String::from("Avery");
    let length = borrow_length(&name);
    println!("{name} has {length} letters");
    take_ownership(name);
    // println!("{name}");   // would not compile: name was moved
}
```

### Expected Behavior or Output

The program prints:
```text
28.18
29.40
26.95
Avery has 5 letters
The function now owns Avery
```

### Common Mistakes
1. Using a value after passing it by value to a function, which is a compile error ("borrow of moved value").
2. Taking `&String` when `&str` would accept more kinds of text.
3. Expecting default or named arguments. Use a struct with `Default`.

### Activities
1. Predict the output before running.
2. Uncomment the last line, read the compiler message, and restore the comment.
3. Change `borrow_length` to take `&str` and call it with a literal and with a `String`.
4. Explain in two sentences the difference between moving and borrowing.

### Accessibility Practice

The compiler message for a moved value names the line where the move happened and the line where the value was used again, so read both. Say 'ampersand' aloud for a borrow and check that your screen reader announces it.

### Skills Checklist
- [ ] I can explain move versus borrow.
- [ ] I can pass a reference.
- [ ] I can use a struct with `Default`.
- [ ] I can read a borrow-checker message.
- [ ] I know Rust has no default arguments.

---

## Lesson 6.3: Return values and expressions

### Reading References
- [The Rust Programming Language: Functions with Return Values](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 6.3: Return Values

### Learning Objectives
- Return a computed value as the final expression.
- Return an `Option` when a value may be missing.
- Return several values with a tuple or a struct.

### Concept Explanation

A function's body ends with an *expression* **without a semicolon**, and that is its return value: `fn classify(score: f64) -> &'static str { if score >= 90.0 { "A" } else { "F" } }`. `return value;` leaves early. Adding a semicolon to the last line turns it into a statement and the function returns `()`, which the compiler rejects when a value is expected.

When a result may not exist, such as the average of an empty slice, return an `Option<f64>`: `Some(x)` or `None`. Rust has no null, so the caller must handle both cases. To return several values, return a tuple or a small struct.

The example returns the average of the shared scores, classifies the average, returns a minimum and maximum together, and shows the empty case.

### Worked Example

```rust
struct ScoreRange {
    low: i32,
    high: i32,
}

fn average(scores: &[i32]) -> Option<f64> {
    if scores.is_empty() {
        return None;
    }
    let total: i32 = scores.iter().sum();
    Some(total as f64 / scores.len() as f64)
}

fn classify(score: f64) -> &'static str {
    if score >= 90.0 {
        "A"
    } else if score >= 80.0 {
        "B"
    } else if score >= 70.0 {
        "C"
    } else if score >= 60.0 {
        "D"
    } else {
        "F"
    }
}

fn min_max(scores: &[i32]) -> ScoreRange {
    let low = *scores.iter().min().unwrap_or(&0);
    let high = *scores.iter().max().unwrap_or(&0);
    ScoreRange { low, high }
}

fn main() {
    let scores = [82, 91, 76, 88];
    let avg = average(&scores);
    println!("Average: {:?}", avg);
    if let Some(value) = avg {
        println!("Grade for the average: {}", classify(value));
    }
    let range = min_max(&scores);
    println!("Lowest and highest: {} and {}", range.low, range.high);
    println!("{:?}", average(&[]));
}
```

### Expected Behavior or Output

The program prints:
```text
Average: Some(84.25)
Grade for the average: B
Lowest and highest: 76 and 91
None
```

### Common Mistakes
1. Adding a semicolon to the last expression, so the function returns `()` instead of the value.
2. Calling `unwrap()` on an empty `Option` and crashing.
3. Printing inside the function and then trying to use the result in a calculation.

### Activities
1. Predict the four printed lines before running.
2. Write `total(scores: &[i32]) -> i32` that returns the sum.
3. Write `is_passing(score: i32) -> bool`.
4. Explain how a caller should use a function that returns `Option<f64>`.

### Accessibility Practice

Return values instead of printing inside logic functions, so the caller prints once and the screen reader announces each result a single time.

### Skills Checklist
- [ ] I can return the final expression.
- [ ] I can return an `Option`.
- [ ] I can return several values.
- [ ] I know a trailing semicolon changes the meaning.
- [ ] I can classify an average with the shared thresholds.

---

## Lesson 6.4: Functions over collections

### Reading References
- [The Rust Programming Language: References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)
- [The Rust Programming Language: The Slice Type](https://doc.rust-lang.org/book/ch04-03-slices.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 6.4: Functions with Lists and Dictionaries

### Learning Objectives
- Pass a slice to read and `&mut Vec` to change.
- Return a new vector and leave the original unchanged.
- Process the shared inventory with a function.

### Concept Explanation

A function that only **reads** a list takes a *slice*, `&[i32]`, which accepts a vector, an array, or part of either without copying. A function that **changes** a vector takes `&mut Vec<i32>`, and the caller passes `&mut scores`; the call site shows that a change will happen. A function can also take ownership and return a new vector.

Rust enforces the rules at compile time: while a function holds a `&mut`, nothing else may read the vector. That removes a whole class of bugs that other languages find at run time.

The shared inventory is Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25), worth 17.50 in total.

### Worked Example

```rust
struct Item {
    name: String,
    quantity: u32,
    unit_price: f64,
}

fn add_score(score_list: &mut Vec<i32>, new_score: i32) {
    score_list.push(new_score);
}

fn with_score(score_list: &[i32], new_score: i32) -> Vec<i32> {
    let mut copy = score_list.to_vec();
    copy.push(new_score);
    copy
}

fn inventory_value(inventory: &[Item]) -> f64 {
    inventory.iter().map(|item| item.quantity as f64 * item.unit_price).sum()
}

fn main() {
    let mut scores = vec![82, 91, 76, 88];
    add_score(&mut scores, 95);
    println!("{:?}", scores);

    let longer = with_score(&scores, 100);
    println!("{} {}", scores.len(), longer.len());

    let inventory = vec![
        Item { name: "Notebook".to_string(), quantity: 3, unit_price: 2.50 },
        Item { name: "Pencil".to_string(), quantity: 10, unit_price: 0.50 },
        Item { name: "Folder".to_string(), quantity: 4, unit_price: 1.25 },
    ];
    println!("Total inventory value: {:.2}", inventory_value(&inventory));
    println!("{}", inventory.iter().map(|item| item.name.as_str()).collect::<Vec<_>>().join(", "));
}
```

### Expected Behavior or Output

The program prints:
```text
[82, 91, 76, 88, 95]
5 6
Total inventory value: 17.50
Notebook, Pencil, Folder
```

### Common Mistakes
1. Passing `&scores` to a function that needs `&mut Vec<i32>`, which is a compile error.
2. Taking `&Vec<i32>` in a function that only reads, instead of the more flexible `&[i32]`.
3. Holding a reference to an element while calling a function that pushes to the vector.

### Activities
1. Predict the four printed lines before running.
2. Write `scale_prices(inventory: &mut [Item], factor: f64)` that changes prices in place.
3. Write a version that returns a new vector and leaves the original unchanged.
4. Explain why `&mut` appears at the call site.

### Accessibility Practice

State aloud before each call whether the function changes its argument: `&mut` at the call site and a name such as `add_score` both say so. Print the list before and after so the effect is heard.

### Skills Checklist
- [ ] I can pass a slice to read.
- [ ] I can pass `&mut Vec` to change.
- [ ] I can return a new vector.
- [ ] I can explain why `&mut` is written at the call.
- [ ] I can total the shared inventory.

---

## Lesson 6.5: Scope, generics, and variadic alternatives

### Reading References
- [The Rust Programming Language: Generic Data Types](https://doc.rust-lang.org/book/ch10-01-syntax.html)
- [Rust by Example: macro_rules!](https://doc.rust-lang.org/rust-by-example/macros.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 6.5: Arbitrary Number of Arguments

### Learning Objectives
- Take any number of values with a slice.
- Write a generic function over a type parameter.
- Explain scope and a variadic macro.

### Concept Explanation

Rust functions have a fixed number of parameters; there are no variadic functions. The usual replacement is a **slice**: `average_of(&[82, 91, 76, 88])` takes any number of values. A *macro* defined with `macro_rules!` can accept a repeated pattern, which is how `println!` and `vec!` take any number of arguments.

A *generic* function works for many types: `fn largest<T: PartialOrd + Copy>(items: &[T]) -> T` accepts any type that can be compared and copied. *Scope* is the region where a name is visible: a `{ ... }` block creates a scope, and a name declared inside ends at the closing brace. An inner binding with the same name *shadows* the outer one.

The shared scores average 84.25, and the average of 90 and 80 is 85.

### Worked Example

```rust
macro_rules! average {
    ($($x:expr),+ $(,)?) => {{
        let values = [$($x as f64),+];
        values.iter().sum::<f64>() / values.len() as f64
    }};
}

fn average_of(scores: &[i32]) -> Option<f64> {
    if scores.is_empty() {
        None
    } else {
        Some(scores.iter().sum::<i32>() as f64 / scores.len() as f64)
    }
}

fn largest<T: PartialOrd + Copy>(items: &[T]) -> T {
    let mut best = items[0];
    for &item in items {
        if item > best {
            best = item;
        }
    }
    best
}

fn main() {
    println!("{}", average!(82, 91, 76, 88));
    println!("{}", average!(90, 80));
    println!("{:?}", average_of(&[82, 91, 76, 88]));
    println!("{:?}", average_of(&[]));

    println!("{} {} {}", largest(&[82, 91, 76]), largest(&[2.5, 0.5]), largest(&['a', 'z', 'm']));

    let value = 1;
    {
        let value = value + 41;
        println!("inner {value}");
    }
    println!("outer {value}");
}
```

### Expected Behavior or Output

The program prints:
```text
84.25
85
Some(84.25)
None
91 2.5 z
inner 42
outer 1
```

### Common Mistakes
1. Looking for a variadic function. Use a slice or a macro.
2. Calling `largest(&[])` on an empty slice, which panics because it reads `items[0]`.
3. Forgetting the trait bounds on `T`, so the comparison does not compile.

### Activities
1. Predict each printed line.
2. Write `maximum_of(scores: &[i32]) -> Option<i32>` that handles an empty slice.
3. Call `largest` with a slice of words (`&str`) and explain why it works.
4. Explain scope and shadowing using the last lines of the example.

### Accessibility Practice

Read macro and generic syntax aloud one piece at a time: 'fn largest, angle bracket T colon PartialOrd plus Copy, close angle bracket'. Check that your screen reader announces the angle brackets and the plus sign.

### Skills Checklist
- [ ] I can take many values with a slice.
- [ ] I can write a generic function.
- [ ] I understand scope and shadowing.
- [ ] I can read a macro call.
- [ ] I handle the empty case.

---

# Unit 7: Data Modeling and Traits

## Overview
This unit develops data modeling and traits through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 7.1: Structs, enums, and data modeling

### Reading References
- [The Rust Programming Language: Defining and Instantiating Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [The Rust Programming Language: Defining an Enum](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [The Rust Programming Language: Modules and Privacy](https://doc.rust-lang.org/book/ch07-02-defining-modules-to-control-scope-and-privacy.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 7.1: Why Learn About Classes?

### Learning Objectives
- Model data with a struct and with an enum.
- Hide a field with module privacy and change it only through methods.
- Explain that Rust has no classes and no inheritance.

### Concept Explanation

Rust has no classes. Data is modeled with a **struct** (named fields) or an **enum** (a value that is exactly one of several variants), and behavior is added in `impl` blocks (Lesson 7.3) and *traits* (Lesson 7.4). Bundling data with the functions that work on it, and hiding the details, is still called **encapsulation**.

Privacy in Rust is controlled by *modules*. Fields and functions are private to the module they are written in unless marked `pub`. In the example, `mod inventory` holds an `Item` whose `quantity` field is private: code outside the module can read it only through the `quantity()` method and change it only through `restock`.

`match` on an enum must cover every variant, so adding a new variant later makes the compiler point at every place that needs a decision. The shared Notebook has quantity 3; restocking 2 gives 5.

### Worked Example

```rust
mod inventory {
    pub struct Item {
        pub name: String,
        quantity: u32,
        pub unit_price: f64,
    }

    impl Item {
        pub fn new(name: &str, quantity: u32, unit_price: f64) -> Item {
            Item { name: name.to_string(), quantity, unit_price }
        }

        pub fn quantity(&self) -> u32 {
            self.quantity
        }

        pub fn restock(&mut self, amount: u32) {
            self.quantity += amount;
        }
    }
}

#[derive(Debug)]
enum Stock {
    Out,
    Low,
    Enough,
}

fn status(quantity: u32) -> Stock {
    match quantity {
        0 => Stock::Out,
        1..=4 => Stock::Low,
        _ => Stock::Enough,
    }
}

fn main() {
    let mut notebook = inventory::Item::new("Notebook", 3, 2.50);
    println!("{}: {} at {} is {:?}", notebook.name, notebook.quantity(), notebook.unit_price, status(notebook.quantity()));
    notebook.restock(2);
    println!("{}: {} is now {:?}", notebook.name, notebook.quantity(), status(notebook.quantity()));
    println!("{:?}", status(0));
    // notebook.quantity = 99;   // would not compile: the field is private
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.5 is Low
Notebook: 5 is now Enough
Out
```

### Common Mistakes
1. Looking for a `class` keyword. Rust uses structs, enums, impl blocks, and traits.
2. Making every field `pub`, so outside code can put the value into an invalid state.
3. Forgetting a variant in a `match` on an enum, which the compiler rejects.

### Activities
1. Predict the three printed lines before running.
2. Add a variant `Overstocked` for quantities above 100 and fix every `match` the compiler points to.
3. Uncomment the assignment, read the compiler message, and restore the comment.
4. Explain what encapsulation means and how modules provide it.

### Accessibility Practice

Describe a data type as a list read in order: the name, then each field, then each variant. Reading a struct aloud works best by saying 'pub struct Item, open brace, pub name colon String comma...' and listening for the braces that show structure.

### Skills Checklist
- [ ] I can model data with a struct and an enum.
- [ ] I can hide a field with a module.
- [ ] I know Rust has no classes.
- [ ] I can read a struct definition aloud.
- [ ] I can match every enum variant.

---

## Lesson 7.2: Creating instances and methods

### Reading References
- [The Rust Programming Language: Method Syntax](https://doc.rust-lang.org/book/ch05-03-method-syntax.html)
- [The Rust Programming Language: Recoverable Errors with Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 7.2: Creating and Using a Class

### Learning Objectives
- Write a constructor function that validates and returns a `Result`.
- Create several instances with the same fields.
- Handle the error when a value is invalid.

### Concept Explanation

Rust has no constructors in the language; by convention an *associated function* named `new` builds a value: `Item::new("Notebook", 3, 2.50)`. Because Rust has no exceptions, a constructor that can fail returns a `Result<Item, String>`: `Ok(item)` for success or `Err(message)` for a clear failure. The caller must handle both cases, usually with `match` or `?`.

An `impl Item { ... }` block holds the functions. A method takes `&self` to read the value or `&mut self` to change it. The example creates the three shared inventory items and then tries to create an invalid one.

### Worked Example

```rust
struct Item {
    name: String,
    quantity: i32,
    unit_price: f64,
}

impl Item {
    fn new(name: &str, quantity: i32, unit_price: f64) -> Result<Item, String> {
        if quantity < 0 {
            return Err("quantity must not be negative".to_string());
        }
        if unit_price < 0.0 {
            return Err("unit price must not be negative".to_string());
        }
        Ok(Item { name: name.to_string(), quantity, unit_price })
    }

    fn total_value(&self) -> f64 {
        self.quantity as f64 * self.unit_price
    }
}

fn main() {
    let notebook = Item::new("Notebook", 3, 2.50).unwrap();
    let pencil = Item::new("Pencil", 10, 0.50).unwrap();
    let folder = Item::new("Folder", 4, 1.25).unwrap();

    for item in [&notebook, &pencil, &folder] {
        println!("{}: {} at {:.2}, value {:.2}", item.name, item.quantity, item.unit_price, item.total_value());
    }

    match Item::new("Broken", -1, 1.0) {
        Ok(item) => println!("Created {}", item.name),
        Err(message) => println!("Could not create the item: {message}"),
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50, value 7.50
Pencil: 10 at 0.50, value 5.00
Folder: 4 at 1.25, value 5.00
Could not create the item: quantity must not be negative
```

### Common Mistakes
1. Calling `unwrap()` on a `Result` from untrusted data, which panics on `Err`.
2. Forgetting `&self`, so the function is associated and cannot be called with the dot syntax.
3. Ignoring the `Err` case. The compiler warns about an unused `Result`.

### Activities
1. Create a fourth item with your own values and print it.
2. Add a rule that the name must not be blank.
3. Create two items with the same name and different quantities and show that they are separate values.
4. Explain the difference between `Item::new` and `item.total_value()`.

### Accessibility Practice

Say the signature aloud in order: 'fn new, open parenthesis, name colon ampersand str...' and check that your screen reader announces the arrow and the `Result` type. Print each item on its own line so output can be matched to values by ear.

### Skills Checklist
- [ ] I can write a `new` function.
- [ ] I can return a `Result` from a constructor.
- [ ] I can create several instances.
- [ ] I can handle the `Err` case.
- [ ] I can tell `&self` from `&mut self`.

---

## Lesson 7.3: Associated functions and impl blocks

### Reading References
- [The Rust Programming Language: Method Syntax](https://doc.rust-lang.org/book/ch05-03-method-syntax.html)
- [The Rust Programming Language: Implementing a Trait on a Type](https://doc.rust-lang.org/book/ch10-02-traits.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 7.3: Working with Attributes and Methods

### Learning Objectives
- Write methods that read, change, and consume a value.
- Define an associated constant.
- Implement `Display` so a value prints as a sentence.

### Concept Explanation

An `impl` block can hold three kinds of function. A method with **`&self`** reads the value, a method with **`&mut self`** changes it, and a method with **`self`** *consumes* it, so the value cannot be used afterward. A function without a `self` parameter, such as `new`, is an *associated function* called with `Item::new`. An *associated constant* such as `const LOW_STOCK: u32 = 5;` belongs to the type and is read as `Item::LOW_STOCK`.

`impl fmt::Display for Item` teaches `println!("{}", item)` how to print the value, so it prints as a useful sentence. The example adds a computed value, a low-stock check, a restock method with validation, a consuming summary, and `Display` to the shared Notebook.

### Worked Example

```rust
use std::fmt;

struct Item {
    name: String,
    quantity: u32,
    unit_price: f64,
}

impl Item {
    const LOW_STOCK: u32 = 5;

    fn new(name: &str, quantity: u32, unit_price: f64) -> Item {
        Item { name: name.to_string(), quantity, unit_price }
    }

    fn total_value(&self) -> f64 {
        self.quantity as f64 * self.unit_price
    }

    fn is_low_stock(&self) -> bool {
        self.quantity < Item::LOW_STOCK
    }

    fn restock(&mut self, amount: i32) {
        if amount < 0 {
            println!("Cannot restock a negative amount.");
            return;
        }
        self.quantity += amount as u32;
    }

    fn into_summary(self) -> String {
        format!("{} x{}", self.name, self.quantity)
    }
}

impl fmt::Display for Item {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}: {} at {:.2} each, value {:.2}", self.name, self.quantity, self.unit_price, self.total_value())
    }
}

fn main() {
    let mut notebook = Item::new("Notebook", 3, 2.50);
    println!("{notebook}");
    println!("Low stock: {}", notebook.is_low_stock());
    notebook.restock(2);
    println!("{notebook}");
    println!("Low stock: {}", notebook.is_low_stock());
    notebook.restock(-1);
    println!("{}", notebook.into_summary());
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
Low stock: true
Notebook: 5 at 2.50 each, value 12.50
Low stock: false
Cannot restock a negative amount.
Notebook x5
```

### Common Mistakes
1. Using a value after calling a method that takes `self`, which is a compile error because the value was consumed.
2. Calling a `&mut self` method on a binding that is not `mut`.
3. Forgetting `use std::fmt;` or the `fmt::Result` return type when implementing `Display`.

### Activities
1. Predict the six printed lines before running.
2. Add a method `discounted(&self, rate: f64) -> f64` that returns the value after a discount without changing the item.
3. Try to print `notebook` after `into_summary` and read the compiler message.
4. Explain the difference between `&self`, `&mut self`, and `self`.

### Accessibility Practice

Name methods after actions (`restock`) so a call reads as a sentence. A good `Display` gives the screen reader one complete line per value; say 'ampersand self' and 'self' aloud to hear the difference between a borrow and a move.

### Skills Checklist
- [ ] I can write read, change, and consume methods.
- [ ] I can define an associated constant.
- [ ] I can implement `Display`.
- [ ] I know a `self` method consumes the value.
- [ ] I can validate in a method.

---

## Lesson 7.4: Traits and polymorphic behavior

### Reading References
- [The Rust Programming Language: Traits: Defining Shared Behavior](https://doc.rust-lang.org/book/ch10-02-traits.html)
- [The Rust Programming Language: Using Trait Objects](https://doc.rust-lang.org/book/ch17-02-trait-objects.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 7.4: Inheritance

### Learning Objectives
- Define a trait with a default method.
- Implement the trait for two types.
- Explain polymorphism with generics and trait objects.

### Concept Explanation

Rust has no inheritance. Shared behavior is described by a **trait**: a set of methods that a type promises to provide. A trait may supply a *default method*, here `describe`, which calls the trait's other methods. Each type writes `impl Priced for Item { ... }` to implement the trait, and may override a default.

*Polymorphism* comes in two forms. A *generic* function, `fn print_total<T: Priced>(item: &T)`, is compiled for each type it is used with. A *trait object*, `Box<dyn Priced>`, lets one vector hold values of different types and picks the method at run time. A struct can hold another struct as a field (composition) instead of inheriting from it.

The example discounts the shared Folder (4 at 1.25) by 20 percent, so its value is 4.00 instead of 5.00.

### Worked Example

```rust
trait Priced {
    fn name(&self) -> &str;
    fn total_value(&self) -> f64;

    fn describe(&self) -> String {
        format!("{}: value {:.2}", self.name(), self.total_value())
    }
}

struct Item {
    name: String,
    quantity: u32,
    unit_price: f64,
}

struct DiscountedItem {
    item: Item,
    discount_rate: f64,
}

impl Priced for Item {
    fn name(&self) -> &str {
        &self.name
    }

    fn total_value(&self) -> f64 {
        self.quantity as f64 * self.unit_price
    }
}

impl Priced for DiscountedItem {
    fn name(&self) -> &str {
        self.item.name()
    }

    fn total_value(&self) -> f64 {
        self.item.total_value() * (1.0 - self.discount_rate)
    }
}

fn print_total<T: Priced>(item: &T) {
    println!("Generic: {}", item.describe());
}

fn main() {
    let notebook = Item { name: "Notebook".to_string(), quantity: 3, unit_price: 2.50 };
    let folder = DiscountedItem {
        item: Item { name: "Folder".to_string(), quantity: 4, unit_price: 1.25 },
        discount_rate: 0.20,
    };

    print_total(&folder);

    let items: Vec<Box<dyn Priced>> = vec![Box::new(notebook), Box::new(folder)];
    for item in &items {
        println!("{}", item.describe());
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Generic: Folder: value 4.00
Notebook: value 7.50
Folder: value 4.00
```

### Common Mistakes
1. Looking for `extends`. Rust has no inheritance; use a trait or a field.
2. Forgetting to implement a required method, which the compiler reports by name.
3. Putting values of different types in a plain `Vec<T>`, which allows only one type; use `Vec<Box<dyn Trait>>`.

### Activities
1. Predict the output before running.
2. Add a third type, `PerishableItem`, that implements `Priced` and override `describe`.
3. Explain why `describe` prints the discounted value without being rewritten.
4. Explain the difference between a generic function and a trait object.

### Accessibility Practice

Describe a trait as a list of promised methods. Speaking `impl Priced for DiscountedItem` aloud ('implement Priced for DiscountedItem') is clearer than a diagram. Print one line per value so the screen reader announces each result in order.

### Skills Checklist
- [ ] I can define a trait with a default method.
- [ ] I can implement a trait for two types.
- [ ] I can explain polymorphism.
- [ ] I know Rust has no inheritance.
- [ ] I can store trait objects in a vector.

---

## Lesson 7.5: Composition and ownership

### Reading References
- [The Rust Programming Language: Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [The Rust Programming Language: Ownership](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 7.5: Instances as Attributes (Composition)

### Learning Objectives
- Explain composition ("has a") and ownership of parts.
- Hold a vector of values inside a struct.
- Build an inventory from the shared items.

### Concept Explanation

*Composition* means one value contains other values. An inventory *has* items; it is not a kind of item. In Rust a struct **owns** its fields: `Inventory { items: Vec<Item> }` owns the vector and every item in it. `add(&mut self, item: Item)` takes the item by value, so ownership **moves** into the inventory and the caller can no longer use it.

Methods that look at the parts borrow: `find(&self, name)` returns `Option<&Item>`, a borrowed reference that lives no longer than the inventory. `remove` returns the owned item back as `Option<Item>`.

The example builds an `Inventory` with the three shared items and reports each quantity and the total value, 17.50.

### Worked Example

```rust
struct Item {
    name: String,
    quantity: u32,
    unit_price: f64,
}

impl Item {
    fn total_value(&self) -> f64 {
        self.quantity as f64 * self.unit_price
    }
}

struct Inventory {
    items: Vec<Item>,
}

impl Inventory {
    fn new() -> Inventory {
        Inventory { items: Vec::new() }
    }

    fn add(&mut self, item: Item) {
        self.items.push(item);
    }

    fn find(&self, name: &str) -> Option<&Item> {
        self.items.iter().find(|item| item.name == name)
    }

    fn remove(&mut self, name: &str) -> Option<Item> {
        let position = self.items.iter().position(|item| item.name == name)?;
        Some(self.items.remove(position))
    }

    fn total_value(&self) -> f64 {
        self.items.iter().map(|item| item.total_value()).sum()
    }

    fn report(&self) {
        for item in &self.items {
            println!("{}: {}", item.name, item.quantity);
        }
        println!("Total value: {:.2}", self.total_value());
    }
}

fn main() {
    let mut inventory = Inventory::new();
    inventory.add(Item { name: "Notebook".to_string(), quantity: 3, unit_price: 2.50 });
    inventory.add(Item { name: "Pencil".to_string(), quantity: 10, unit_price: 0.50 });
    inventory.add(Item { name: "Folder".to_string(), quantity: 4, unit_price: 1.25 });
    inventory.report();

    println!("{:?}", inventory.find("Pencil").map(|item| item.quantity));
    println!("{}", inventory.find("Eraser").is_none());
    let removed = inventory.remove("Pencil");
    println!("{}", removed.map(|item| item.name).unwrap_or_default());
    println!("{}", inventory.items.len());
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3
Pencil: 10
Folder: 4
Total value: 17.50
Some(10)
true
Pencil
2
```

### Common Mistakes
1. Using an item after passing it to `add`, which is a compile error because it was moved.
2. Returning a reference from `find` and then changing the inventory while still holding it.
3. Using inheritance thinking: an inventory is not a kind of item.

### Activities
1. Predict the output.
2. Add a method that returns the names of items with a quantity below 5.
3. Try to use `notebook` after `inventory.add(notebook)` and read the compiler message.
4. Explain "is a" versus "has a" with two examples.

### Accessibility Practice

Report the inventory as one labelled line per item and a final total line, so the screen reader reads a complete summary in order. Say 'ampersand' and 'ampersand mut' aloud so that borrows are heard.

### Skills Checklist
- [ ] I can explain composition.
- [ ] I can hold a vector in a struct.
- [ ] I understand ownership moving into a container.
- [ ] I can return a borrowed `Option<&Item>`.
- [ ] I can build the shared inventory.

---

# Unit 8: Files and Error Handling

## Overview
This unit develops files and error handling through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 8.1: Reading text files

### Reading References
- [The Rust Programming Language: Reading a File](https://doc.rust-lang.org/book/ch12-02-reading-a-file.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 8.1: Reading from a File

### Learning Objectives
- Read a whole file and read it line by line.
- Check that a file exists before reading.
- Report a missing file clearly.

### Concept Explanation

`std::fs::read_to_string(path)` returns the whole file as a `Result<String, io::Error>`, and `.lines()` splits a string into lines. `std::fs::write(path, text)` writes a file. `Path::new("notes.txt").exists()` tests whether a file is there. A relative path starts from the program's working directory.

The `?` operator passes an error up to the caller: in a function returning `io::Result<()>`, `let text = fs::read_to_string(path)?;` stops and returns the error if reading fails. `main` itself can return `io::Result<()>`.

To keep the lesson self-contained, the example first writes the two-line `notes.txt` that every language track uses, then reads it three ways and checks a file that does not exist.

### Worked Example

```rust
use std::fs;
use std::io;
use std::path::Path;

fn main() -> io::Result<()> {
    let path = Path::new("notes.txt");
    fs::write(path, "Practice Rust.\nReview vectors and functions.\n")?;

    let contents = fs::read_to_string(path)?;
    println!("{contents}");

    for line in contents.lines() {
        println!("{line}");
    }
    println!("{}", contents.lines().count());

    for line in contents.lines() {
        println!("{}", line.to_uppercase());
    }

    let missing = Path::new("missing_notes.txt");
    if !missing.exists() {
        println!("missing_notes.txt was not found.");
    }
    Ok(())
}
```

### Expected Behavior or Output

The program prints:
```text
Practice Rust.
Review vectors and functions.

Practice Rust.
Review vectors and functions.
2
PRACTICE RUST.
REVIEW VECTORS AND FUNCTIONS.
missing_notes.txt was not found.
```

### Common Mistakes
1. Reading a file that does not exist without checking or handling the error.
2. Using `unwrap()` on a file result, which crashes with a long message.
3. Forgetting that `read_to_string` keeps the final line ending, so `println!` adds a blank line.

### Activities
1. Run the program and describe each block of output.
2. Add a third line to the file text and predict the new count.
3. Print each line with its line number using `enumerate`.
4. Print a friendly message that includes the missing file's name.

### Accessibility Practice

Read the output aloud in order. Make an error message a complete sentence that includes the file name so it is clear without seeing the screen.

### Skills Checklist
- [ ] I can read a file whole and by line.
- [ ] I can check that a file exists.
- [ ] I can use `?` to pass an error up.
- [ ] I can report a missing file.
- [ ] I know `main` can return a `Result`.

---

## Lesson 8.2: Writing and appending files

### Reading References
- [std::fs::OpenOptions](https://doc.rust-lang.org/std/fs/struct.OpenOptions.html)
- [The Rust Programming Language: Reading a File](https://doc.rust-lang.org/book/ch12-02-reading-a-file.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 8.2: Writing to a File

### Learning Objectives
- Write with `fs::write` and append with `OpenOptions`.
- Include line endings correctly.
- Read the file back to verify it.

### Concept Explanation

`fs::write(path, text)` creates the file or **replaces** its contents. To add to the end, open the file with `OpenOptions::new().append(true).open(path)?` and call `write_all` from the `Write` trait on the byte form of the text, `b"..."` or `text.as_bytes()`. Neither adds a line ending for you, so end each line with `\n`.

When the file handle goes out of scope Rust closes it automatically (Lesson 8.4). Reading the file back is the simplest way to confirm what was saved. The example writes the first notes line, appends the second, and reads the file back.

### Worked Example

```rust
use std::fs::{self, OpenOptions};
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let path = "notes.txt";
    fs::write(path, "Practice Rust.\n")?;

    let mut file = OpenOptions::new().append(true).open(path)?;
    file.write_all(b"Review vectors and functions.\n")?;

    print!("{}", fs::read_to_string(path)?);
    println!("Lines: {}", fs::read_to_string(path)?.lines().count());
    Ok(())
}
```

### Expected Behavior or Output

The program prints:
```text
Practice Rust.
Review vectors and functions.
Lines: 2
```

### Common Mistakes
1. Using `fs::write` when appending was intended, which erases earlier content.
2. Forgetting `use std::io::Write`, so `write_all` is not found.
3. Forgetting `\n`, so all written lines run together.

### Activities
1. Predict the output, then run.
2. Replace the append with `fs::write` and explain the difference.
3. Append a third line with the current count of lines.
4. Write the shared scores, one per line, then read them back and total them.

### Accessibility Practice

Always read a written file back in the terminal to confirm it, using line navigation, so you do not depend on assumptions about what was saved.

### Skills Checklist
- [ ] I can write and append.
- [ ] I know `fs::write` replaces.
- [ ] I can include line endings.
- [ ] I can verify by reading back.
- [ ] I can count lines in a file.

---

## Lesson 8.3: Result and error propagation

### Reading References
- [The Rust Programming Language: Recoverable Errors with Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [The Rust Programming Language: To panic! or Not to panic!](https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 8.3: Exceptions - Handling Errors

### Learning Objectives
- Handle a `Result` with `match` and propagate it with `?`.
- Tell recoverable errors (`Result`) from panics.
- Use `Box<dyn Error>` to combine different error types.

### Concept Explanation

Rust has no exceptions. A function that can fail returns `Result<T, E>`, and the caller must handle it: `match` on `Ok` and `Err`, `unwrap_or` to supply a default, or `?` to return the error to *its* caller. The `?` operator also converts the error: with a return type of `Result<T, Box<dyn Error>>`, `?` accepts both an `io::Error` and a `ParseIntError`.

A **panic** (`unwrap()` on an `Err`, an index out of range, integer division by zero) stops the program and is for bugs, not for expected problems like a missing file. `checked_div` returns an `Option` instead of panicking. The error kind of an I/O failure can be matched, for example `ErrorKind::NotFound`. Library error messages can depend on the operating system, so the example prints only messages that are the same everywhere.

### Worked Example

```rust
use std::error::Error;
use std::fs;
use std::io::ErrorKind;
use std::num::ParseIntError;

fn parse_score(text: &str) -> Result<i32, ParseIntError> {
    let number = text.trim().parse::<i32>()?;
    Ok(number)
}

fn read_first_number(path: &str) -> Result<i32, Box<dyn Error>> {
    let text = fs::read_to_string(path)?;
    let first = text.lines().next().unwrap_or("");
    Ok(first.trim().parse::<i32>()?)
}

fn main() {
    match fs::read_to_string("missing_notes.txt") {
        Ok(_) => println!("The file was read."),
        Err(error) if error.kind() == ErrorKind::NotFound => println!("Error: missing_notes.txt was not found."),
        Err(_) => println!("Error: the file could not be read."),
    }

    match parse_score("abc") {
        Ok(number) => println!("Score {number}"),
        Err(error) => println!("Error: 'abc' is not a valid score ({error})"),
    }
    println!("{:?}", parse_score(" 88 "));

    println!("{:?}", 10_i32.checked_div(0));
    println!("{}", 10_i32.checked_div(0).unwrap_or(0));

    match read_first_number("missing_notes.txt") {
        Ok(number) => println!("First number: {number}"),
        Err(_) => println!("Could not read a number from the file."),
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score (invalid digit found in string)
Ok(88)
None
0
Could not read a number from the file.
```

### Common Mistakes
1. Calling `unwrap()` on a `Result` for expected failures, which turns them into panics.
2. Using `?` in a function whose return type is not a `Result` or `Option`, which is a compile error.
3. Printing an operating-system error message in an expected output, which differs between systems.

### Activities
1. Predict each printed line before running.
2. Write a function that reads a file and returns the number of lines as a `Result`.
3. Use `?` in a function that parses two numbers and adds them.
4. Explain when to return a `Result` and when a panic is acceptable.

### Accessibility Practice

Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.' When a panic message appears, read the line that names your own file first.

### Skills Checklist
- [ ] I can handle a `Result` with `match`.
- [ ] I can use `?` to pass errors up.
- [ ] I can tell a `Result` from a panic.
- [ ] I can use `Box<dyn Error>`.
- [ ] I can write clear error messages.

---

## Lesson 8.4: Resource cleanup and RAII

### Reading References
- [The Rust Programming Language: Running Code on Cleanup with the Drop Trait](https://doc.rust-lang.org/book/ch15-03-drop.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 8.4: The else and finally Blocks

### Learning Objectives
- Explain that Rust releases resources when a value goes out of scope.
- Implement `Drop` to see when cleanup runs.
- Close a file by letting it go out of scope.

### Concept Explanation

Rust has no `finally`. Instead, every value is *dropped* (cleaned up) automatically when its owner goes out of scope, and values are dropped in **reverse order of creation**. This idea is called **RAII** (resource acquisition is initialization). A file handle closes itself when it is dropped, so a file cannot be left open by a forgotten call, even if the code returns early or a panic unwinds.

A type can run its own cleanup by implementing the `Drop` trait, whose `drop` method is called automatically. `drop(value)` ends a value's life early. A binding named `_name` stays alive until the end of its scope, but the bare pattern `_` drops the value immediately, which surprises many learners.

The example shows the order of cleanup and writes a file inside a block so that it is closed before it is read back.

### Worked Example

```rust
use std::fs::{self, File};
use std::io::Write;

struct Guard(&'static str);

impl Drop for Guard {
    fn drop(&mut self) {
        println!("Releasing {}", self.0);
    }
}

fn main() {
    let _outer = Guard("outer resource");
    {
        let _inner = Guard("inner resource");
        println!("Using the inner resource");
    }
    println!("After the inner block");

    let early = Guard("early resource");
    drop(early);
    println!("After the explicit drop");

    {
        let mut file = File::create("cleanup_demo.txt").expect("could not create the file");
        file.write_all(b"Some data.\n").expect("could not write the file");
    }
    let text = fs::read_to_string("cleanup_demo.txt").expect("could not read the file");
    println!("{}", text.trim());
    println!("End of main");
}
```

### Expected Behavior or Output

The program prints:
```text
Using the inner resource
Releasing inner resource
After the inner block
Releasing early resource
After the explicit drop
Some data.
End of main
Releasing outer resource
```

### Common Mistakes
1. Writing `let _ = Guard(...)` and expecting it to live until the end of the scope. It is dropped at once.
2. Expecting values to be dropped in the order they were created. The order is reversed.
3. Reading a file before the handle that wrote it has gone out of scope, which can miss buffered data.

### Activities
1. Predict the eight printed lines, especially the order of the `Releasing` lines.
2. Change `_outer` to `_` and describe what changes.
3. Add a third guard and predict where its message appears.
4. Explain why Rust does not need a `finally` block.

### Accessibility Practice

Print a short labelled line when each resource is released, so the screen reader announces the order of cleanup. Labelled lines make a rule that is normally invisible audible.

### Skills Checklist
- [ ] I can explain scope-based cleanup.
- [ ] I can implement `Drop`.
- [ ] I know values drop in reverse order.
- [ ] I know a file closes when it is dropped.
- [ ] I know `_` and `_name` differ.

---

## Lesson 8.5: JSON serialization and persistence

### Reading References
- [The Rust Programming Language: Packages and Crates](https://doc.rust-lang.org/book/ch07-01-packages-and-crates.html)
- [serde_json documentation](https://docs.rs/serde_json/)
- JSON specification: https://www.json.org
- Matching Python lesson: Lesson 8.5: Storing Data with JSON

### Learning Objectives
- Explain why this lesson includes a JSON helper.
- Encode and decode the shared task records.
- Handle a missing or malformed file.

### Concept Explanation

The Rust standard library has no JSON support. Real projects add the `serde` and `serde_json` crates through Cargo. To keep this course free of dependencies, the example includes a *teaching implementation*: an `enum Json` with an `encode` function and a `decode` function built from a small parser. It handles strings, numbers, booleans, `null`, lists, and objects, writes object keys in sorted order (a `BTreeMap`), and reports malformed text with a message that includes the position. It is not a replacement for a production library, and a decimal such as `2.0` is written as `2`, so it reads back as an integer.

JSON text stores data in a standard format: `{ ... }` holds key-value pairs, `[ ... ]` holds ordered items, and text is in double quotation marks. Decoded data is a `Json` enum, so `match` forces you to handle every kind of value.

The shared to-do record has the fields `id`, `title`, `description`, `done`, and `created_at`. The example saves two tasks, loads them back, and shows the message for a malformed file.

The teaching helper decodes JSON `null` as `Json::Null` and whole numbers as `Json::Int`. It does not handle every number edge case that a full parser must.

### Worked Example

```rust
use std::collections::BTreeMap;

#[derive(Debug, Clone, PartialEq)]
enum Json {
    Null,
    Bool(bool),
    Int(i64),
    Float(f64),
    Str(String),
    List(Vec<Json>),
    Object(BTreeMap<String, Json>),
}

fn quote(text: &str) -> String {
    let mut out = String::from("\"");
    for c in text.chars() {
        match c {
            '"' => out.push_str("\\\""),
            '\\' => out.push_str("\\\\"),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            c if (c as u32) < 0x20 => out.push_str(&format!("\\u{:04x}", c as u32)),
            c => out.push(c),
        }
    }
    out.push('"');
    out
}

fn encode(value: &Json) -> String {
    match value {
        Json::Null => "null".to_string(),
        Json::Bool(flag) => flag.to_string(),
        Json::Int(number) => number.to_string(),
        Json::Float(number) => number.to_string(),
        Json::Str(text) => quote(text),
        Json::List(items) => {
            let parts: Vec<String> = items.iter().map(encode).collect();
            format!("[{}]", parts.join(","))
        }
        Json::Object(map) => {
            let parts: Vec<String> = map.iter().map(|(key, item)| format!("{}:{}", quote(key), encode(item))).collect();
            format!("{{{}}}", parts.join(","))
        }
    }
}

struct Parser {
    chars: Vec<char>,
    pos: usize,
}

impl Parser {
    fn fail<T>(&self, message: &str) -> Result<T, String> {
        Err(format!("{message} at position {}", self.pos))
    }

    fn skip(&mut self) {
        while self.pos < self.chars.len() && self.chars[self.pos].is_whitespace() {
            self.pos += 1;
        }
    }

    fn peek(&self) -> Option<char> {
        self.chars.get(self.pos).copied()
    }

    fn starts_with(&self, word: &str) -> bool {
        word.chars().enumerate().all(|(i, c)| self.chars.get(self.pos + i) == Some(&c))
    }

    fn value(&mut self) -> Result<Json, String> {
        self.skip();
        match self.peek() {
            None => self.fail("unexpected end of text"),
            Some('{') => self.object(),
            Some('[') => self.list(),
            Some('"') => Ok(Json::Str(self.string()?)),
            Some(c) if c == '-' || c.is_ascii_digit() => self.number(),
            Some(_) if self.starts_with("true") => {
                self.pos += 4;
                Ok(Json::Bool(true))
            }
            Some(_) if self.starts_with("false") => {
                self.pos += 5;
                Ok(Json::Bool(false))
            }
            Some(_) if self.starts_with("null") => {
                self.pos += 4;
                Ok(Json::Null)
            }
            Some(_) => self.fail("unexpected character"),
        }
    }

    fn number(&mut self) -> Result<Json, String> {
        let start = self.pos;
        if self.peek() == Some('-') {
            self.pos += 1;
        }
        while let Some(c) = self.peek() {
            if c.is_ascii_digit() || ".eE+-".contains(c) {
                self.pos += 1;
            } else {
                break;
            }
        }
        let token: String = self.chars[start..self.pos].iter().collect();
        if let Ok(number) = token.parse::<i64>() {
            return Ok(Json::Int(number));
        }
        match token.parse::<f64>() {
            Ok(number) => Ok(Json::Float(number)),
            Err(_) => self.fail("bad number"),
        }
    }

    fn string(&mut self) -> Result<String, String> {
        self.pos += 1;
        let mut out = String::new();
        loop {
            let Some(c) = self.peek() else {
                return self.fail("unterminated string");
            };
            self.pos += 1;
            match c {
                '"' => return Ok(out),
                '\\' => {
                    let Some(escape) = self.peek() else {
                        return self.fail("bad escape");
                    };
                    self.pos += 1;
                    match escape {
                        'n' => out.push('\n'),
                        't' => out.push('\t'),
                        'r' => out.push('\r'),
                        '"' => out.push('"'),
                        '\\' => out.push('\\'),
                        '/' => out.push('/'),
                        'u' => {
                            if self.pos + 4 > self.chars.len() {
                                return self.fail("bad escape");
                            }
                            let hex: String = self.chars[self.pos..self.pos + 4].iter().collect();
                            let code = u32::from_str_radix(&hex, 16).map_err(|_| "bad escape".to_string())?;
                            out.push(char::from_u32(code).unwrap_or('?'));
                            self.pos += 4;
                        }
                        _ => return self.fail("bad escape"),
                    }
                }
                other => out.push(other),
            }
        }
    }

    fn object(&mut self) -> Result<Json, String> {
        self.pos += 1;
        let mut map = BTreeMap::new();
        self.skip();
        if self.peek() == Some('}') {
            self.pos += 1;
            return Ok(Json::Object(map));
        }
        loop {
            self.skip();
            if self.peek() != Some('"') {
                return self.fail("expected a key");
            }
            let key = self.string()?;
            self.skip();
            if self.peek() != Some(':') {
                return self.fail("expected ':'");
            }
            self.pos += 1;
            let item = self.value()?;
            map.insert(key, item);
            self.skip();
            match self.peek() {
                None => return self.fail("unterminated object"),
                Some('}') => {
                    self.pos += 1;
                    return Ok(Json::Object(map));
                }
                Some(',') => self.pos += 1,
                Some(_) => return self.fail("expected ',' or '}'"),
            }
        }
    }

    fn list(&mut self) -> Result<Json, String> {
        self.pos += 1;
        let mut items = Vec::new();
        self.skip();
        if self.peek() == Some(']') {
            self.pos += 1;
            return Ok(Json::List(items));
        }
        loop {
            items.push(self.value()?);
            self.skip();
            match self.peek() {
                None => return self.fail("unterminated list"),
                Some(']') => {
                    self.pos += 1;
                    return Ok(Json::List(items));
                }
                Some(',') => self.pos += 1,
                Some(_) => return self.fail("expected ',' or ']'"),
            }
        }
    }
}

fn decode(text: &str) -> Result<Json, String> {
    let mut parser = Parser { chars: text.chars().collect(), pos: 0 };
    let value = parser.value()?;
    parser.skip();
    if parser.pos < parser.chars.len() {
        return parser.fail("unexpected extra text");
    }
    Ok(value)
}

use std::fs;
use std::io;

fn task(id: i64, title: &str, description: &str, done: bool, created_at: &str) -> Json {
    let mut map = BTreeMap::new();
    map.insert("id".to_string(), Json::Int(id));
    map.insert("title".to_string(), Json::Str(title.to_string()));
    map.insert("description".to_string(), Json::Str(description.to_string()));
    map.insert("done".to_string(), Json::Bool(done));
    map.insert("created_at".to_string(), Json::Str(created_at.to_string()));
    Json::Object(map)
}

fn main() -> io::Result<()> {
    let tasks = Json::List(vec![
        task(1, "Study programming", "Finish Unit 8", false, "2026-01-15T09:00:00"),
        task(2, "Review scores", "Check the four scores", true, "2026-01-15T09:30:00"),
    ]);
    fs::write("tasks.json", encode(&tasks))?;

    let text = match fs::read_to_string("tasks.json") {
        Ok(text) => text,
        Err(_) => {
            println!("Tasks file not found.");
            return Ok(());
        }
    };

    match decode(&text) {
        Ok(Json::List(items)) => {
            for item in &items {
                if let Json::Object(map) = item {
                    let id = match map.get("id") {
                        Some(Json::Int(number)) => *number,
                        _ => 0,
                    };
                    let title = match map.get("title") {
                        Some(Json::Str(text)) => text.as_str(),
                        _ => "?",
                    };
                    let status = if map.get("done") == Some(&Json::Bool(true)) { "done" } else { "not done" };
                    println!("{id}: {title} ({status})");
                }
            }
        }
        Ok(_) => println!("Error: the tasks file must contain a list."),
        Err(message) => println!("Error: could not decode tasks file: {message}"),
    }

    println!("{:?}", decode("[{\"id\": 1,"));
    Ok(())
}
```

### Expected Behavior or Output

The program prints:
```text
1: Study programming (not done)
2: Review scores (done)
Err("expected a key at position 10")
```

### Common Mistakes
1. Assuming Rust has built-in JSON support.
2. Trusting decoded data without matching on the kind of each value.
3. Overwriting a good data file with an empty list after a failed load.

### Activities
1. Run the program and read the saved JSON text from `tasks.json`.
2. Edit `tasks.json` by hand to remove a closing bracket and run the loading part again. Read the message.
3. Add a third task and confirm that it is saved and loaded.
4. Explain why a production project should use `serde_json`.

### Accessibility Practice

Open `tasks.json` in the terminal and read it as text. JSON in a single line is difficult to navigate, so practise stepping through it by word or character.

### Skills Checklist
- [ ] I know Rust has no built-in JSON.
- [ ] I can encode and decode records.
- [ ] I handle missing and malformed files.
- [ ] I match on decoded values.
- [ ] I know when to use a crate.

---

# Unit 9: Testing and Data Analysis

## Overview
This unit develops testing and data analysis through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 9.1: Unit tests

### Reading References
- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Rust Programming Language: Test Organization](https://doc.rust-lang.org/book/ch11-03-test-organization.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 9.1: Testing Your Code

### Learning Objectives
- Write checks with chosen inputs and expected results.
- Write a `#[cfg(test)]` module with `#[test]` functions.
- Compare decimals with a tolerance and test boundary values.

### Concept Explanation

Rust has testing built in. A function marked `#[test]` inside a module marked `#[cfg(test)]` is compiled and run only by the test harness (`cargo test`, or `rustc --test`), and `assert_eq!(actual, expected)` stops that test with a clear message when the values differ. A normal build ignores the module, so tests cost nothing at run time.

The example shows both styles: a small hand-written `Tally` that prints PASS and FAIL lines when the program runs, and the idiomatic `#[test]` module, which is verified separately in the Expected section. Decimal results are compared with a *tolerance*, not `==`, because the tip for 24.50 at 0.15 is stored as 3.6749999999999998.

The same tests appear in every language track: `add(5, 3)` is 8, `add(-5, -3)` is -8, `add(10, -4)` is 6, the tip is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F. `std::process::exit(1)` ends the program with a failure status.

### Worked Example

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn calculate_tip(bill: f64, rate: f64) -> f64 {
    bill * rate
}

fn classify(score: i32) -> &'static str {
    if score >= 90 {
        "A"
    } else if score >= 80 {
        "B"
    } else if score >= 70 {
        "C"
    } else if score >= 60 {
        "D"
    } else {
        "F"
    }
}

struct Tally {
    passed: u32,
    failed: u32,
}

impl Tally {
    fn check<T: PartialEq + std::fmt::Debug>(&mut self, name: &str, actual: T, expected: T) {
        if actual == expected {
            self.passed += 1;
            println!("PASS {name}");
        } else {
            self.failed += 1;
            println!("FAIL {name}: expected {:?} but got {:?}", expected, actual);
        }
    }

    fn check_close(&mut self, name: &str, actual: f64, expected: f64, tolerance: f64) {
        self.check(name, (actual - expected).abs() <= tolerance, true);
    }
}

fn main() {
    let mut tally = Tally { passed: 0, failed: 0 };
    tally.check("add 5 and 3", add(5, 3), 8);
    tally.check("add -5 and -3", add(-5, -3), -8);
    tally.check("add 10 and -4", add(10, -4), 6);
    tally.check_close("tip on 24.50 at 0.15", calculate_tip(24.5, 0.15), 3.675, 1e-9);
    tally.check("tip on a zero bill", calculate_tip(0.0, 0.15), 0.0);
    tally.check("classify 90", classify(90), "A");
    tally.check("classify 89", classify(89), "B");
    tally.check("classify 60", classify(60), "D");
    tally.check("classify 59", classify(59), "F");

    println!("{} passed, {} failed", tally.passed, tally.failed);
    if tally.failed > 0 {
        std::process::exit(1);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn adds_numbers() {
        assert_eq!(add(5, 3), 8);
        assert_eq!(add(-5, -3), -8);
        assert_eq!(add(10, -4), 6);
    }

    #[test]
    fn tip_is_close_to_expected() {
        assert!((calculate_tip(24.5, 0.15) - 3.675).abs() < 1e-9);
    }

    #[test]
    fn grade_boundaries() {
        assert_eq!(classify(90), "A");
        assert_eq!(classify(89), "B");
        assert_eq!(classify(60), "D");
        assert_eq!(classify(59), "F");
    }
}
```

### Expected Behavior or Output

The program prints:
```text
PASS add 5 and 3
PASS add -5 and -3
PASS add 10 and -4
PASS tip on 24.50 at 0.15
PASS tip on a zero bill
PASS classify 90
PASS classify 89
PASS classify 60
PASS classify 59
9 passed, 0 failed
```

The `#[cfg(test)]` module is not compiled in a normal build. Running it with the test harness (`rustc --test main.rs -o tests` then `./tests --test-threads=1`, or `cargo test`) prints:
```text
running 3 tests
test tests::adds_numbers ... ok
test tests::grade_boundaries ... ok
test tests::tip_is_close_to_expected ... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
```

### Common Mistakes
1. Comparing decimal results with `assert_eq!` and `==`.
2. Testing only typical values and skipping the boundaries 90, 89, 60, and 59.
3. Putting `#[test]` functions outside a `#[cfg(test)]` module, which compiles them into the normal build.

### Activities
1. Change one expected value so a check fails, read the message, and restore it.
2. Add checks for the grades at 80, 79, 70, and 69.
3. Write the tests for `is_passing(score)` before writing the function.
4. Explain why the tip test uses a tolerance.

### Accessibility Practice

Each check prints one complete line that starts with PASS or FAIL, and the last line gives the counts, so the result can be understood from the first word of each line and the final summary. The test harness prints one line per test and a final result line in the same style.

### Skills Checklist
- [ ] I can write a check with an expected value.
- [ ] I can write a `#[test]` module.
- [ ] I can compare decimals with a tolerance.
- [ ] I can choose boundary tests.
- [ ] I know how to signal failure with an exit status.

---

## Lesson 9.2: Testing stateful types

### Reading References
- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Rust Programming Language: Checking for Panics with should_panic](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 9.2: Testing a Class

### Learning Objectives
- Create a fresh value for every test.
- Test a return value, a change of state, and an error result.
- Write the same tests in a `#[cfg(test)]` module.

### Concept Explanation

Each test should start from a known state, so build a new value for every test with a *setup* function. Tests that share a value can affect each other and fail in confusing ways.

Test three kinds of behavior: that a method returns the right value (`total_value` for 3 at 2.50 is 7.5), that a method changes the value correctly (restocking 2 makes the quantity 5), and that invalid use is reported (restocking a negative amount returns an `Err`). Because Rust reports expected failures with `Result`, a test can simply check `is_err()`. A function that is expected to panic can be tested with `#[should_panic]`.

The example runs each test as a function returning `Result<(), String>`, so a failed check carries a message, and the same tests also appear in a `#[cfg(test)]` module.

### Worked Example

```rust
struct Item {
    name: String,
    quantity: i32,
    unit_price: f64,
}

impl Item {
    fn total_value(&self) -> f64 {
        self.quantity as f64 * self.unit_price
    }

    fn restock(&mut self, amount: i32) -> Result<(), String> {
        if amount < 0 {
            return Err("amount must not be negative".to_string());
        }
        self.quantity += amount;
        Ok(())
    }
}

fn setup() -> Item {
    Item { name: "Notebook".to_string(), quantity: 3, unit_price: 2.50 }
}

fn expect(condition: bool, message: &str) -> Result<(), String> {
    if condition {
        Ok(())
    } else {
        Err(message.to_string())
    }
}

fn total_value_is_7_5() -> Result<(), String> {
    expect((setup().total_value() - 7.5).abs() < 1e-9, "wrong total")
}

fn restock_adds_to_the_quantity() -> Result<(), String> {
    let mut item = setup();
    item.restock(2)?;
    expect(item.quantity == 5, "quantity should be 5")
}

fn restock_rejects_a_negative_amount() -> Result<(), String> {
    let mut item = setup();
    expect(item.restock(-1).is_err(), "an error should have been returned")?;
    expect(item.quantity == 3, "the quantity should be unchanged")?;
    expect(!item.name.is_empty(), "the name should be kept")
}

fn main() {
    let tests: [(&str, fn() -> Result<(), String>); 3] = [
        ("total value is 7.5", total_value_is_7_5),
        ("restock adds to the quantity", restock_adds_to_the_quantity),
        ("restock rejects a negative amount", restock_rejects_a_negative_amount),
    ];

    let mut failures = 0;
    for (name, test) in tests {
        match test() {
            Ok(()) => println!("PASS {name}"),
            Err(message) => {
                failures += 1;
                println!("FAIL {name}: {message}");
            }
        }
    }
    println!("{}", if failures == 0 { "All tests passed.".to_string() } else { format!("{failures} test(s) failed.") });
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn total_value() {
        assert!(total_value_is_7_5().is_ok());
    }

    #[test]
    fn restock_adds() {
        assert_eq!(restock_adds_to_the_quantity(), Ok(()));
    }

    #[test]
    fn restock_rejects_negative() {
        assert_eq!(restock_rejects_a_negative_amount(), Ok(()));
    }
}
```

### Expected Behavior or Output

The program prints:
```text
PASS total value is 7.5
PASS restock adds to the quantity
PASS restock rejects a negative amount
All tests passed.
```

The `#[cfg(test)]` module is not compiled in a normal build. Running it with the test harness (`rustc --test main.rs -o tests` then `./tests --test-threads=1`, or `cargo test`) prints:
```text
running 3 tests
test tests::restock_adds ... ok
test tests::restock_rejects_negative ... ok
test tests::total_value ... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
```

### Common Mistakes
1. Sharing one value between tests, so an earlier test changes the later ones.
2. Testing only the successful path and never the error path.
3. Using `unwrap()` inside a test helper so that a failure panics with no message about which check failed.

### Activities
1. Add a test that `restock(0)` leaves the quantity unchanged.
2. Add a test for an `is_valid` method.
3. Break `restock` on purpose and read the failure line.
4. Explain why `setup` creates a new item each time.

### Accessibility Practice

Name each test as a short sentence that says what it checks, so the PASS and FAIL lines read as clear statements. Read the final summary line first.

### Skills Checklist
- [ ] I can create a fresh value per test.
- [ ] I can test a return value.
- [ ] I can test a change of state.
- [ ] I can test an error result.
- [ ] I can write a clear test name.

---

## Lesson 9.3: Random values

### Reading References
- [The rand crate](https://docs.rs/rand/)
- [The Rust Programming Language: Method Syntax](https://doc.rust-lang.org/book/ch05-03-method-syntax.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 9.3: Random Numbers and Simulation

### Learning Objectives
- Explain why the standard library has no random numbers.
- Use a small seeded generator and test it by its properties.
- Pick a random list item.

### Concept Explanation

The Rust standard library has **no random-number generator**. Real programs add the `rand` crate through Cargo. To keep this course free of dependencies, the example uses a tiny *xorshift* generator written in a few lines. It is predictable and **not secure**, so it must never be used for passwords or tokens, but it is enough to learn the ideas.

A generator started from the same *seed* produces the same sequence, so a test can check *repeatability*. A seed must not be zero for this algorithm. Because the exact numbers depend on the algorithm, tests should check *properties* (every roll is between 1 and 6, a decimal is in 0 up to but not including 1) and not particular values.

### Worked Example

```rust
struct Rng {
    state: u64,
}

impl Rng {
    fn new(seed: u64) -> Rng {
        Rng { state: if seed == 0 { 1 } else { seed } }
    }

    fn next_u64(&mut self) -> u64 {
        let mut x = self.state;
        x ^= x << 13;
        x ^= x >> 7;
        x ^= x << 17;
        self.state = x;
        x
    }

    fn range(&mut self, low: u64, high: u64) -> u64 {
        low + self.next_u64() % (high - low)
    }

    fn next_f64(&mut self) -> f64 {
        (self.next_u64() >> 11) as f64 / (1u64 << 53) as f64
    }
}

fn main() {
    let mut first = Rng::new(42);
    let mut second = Rng::new(42);
    let first_rolls: Vec<u64> = (0..5).map(|_| first.range(1, 7)).collect();
    let second_rolls: Vec<u64> = (0..5).map(|_| second.range(1, 7)).collect();
    println!("Same seed gives the same rolls: {}", first_rolls == second_rolls);

    let mut random = Rng::new(7);
    let in_range = (0..1000).all(|_| (1..=6).contains(&random.range(1, 7)));
    println!("All rolls between 1 and 6: {in_range}");

    let decimal = random.next_f64();
    println!("Decimal in [0, 1): {}", (0.0..1.0).contains(&decimal));

    let scores = [82, 91, 76, 88];
    let chosen = scores[random.range(0, scores.len() as u64) as usize];
    println!("Chosen score is from the list: {}", scores.contains(&chosen));
}
```

### Expected Behavior or Output

The program prints:
```text
Same seed gives the same rolls: true
All rolls between 1 and 6: true
Decimal in [0, 1): true
Chosen score is from the list: true
```

### Common Mistakes
1. Looking for `std::random`. It does not exist; use the `rand` crate in real programs.
2. Using a simple generator for passwords or tokens, which it is not designed for.
3. Seeding with zero, which makes this algorithm produce only zeros.

### Activities
1. Run the program three times and compare.
2. Change the seeds and check that the property lines still print `true`.
3. Simulate 600 rolls and count how many of each face appeared (the counts depend on the seed).
4. Explain why a test should check a property rather than a specific random number.

### Accessibility Practice

Print yes or no style results for random behavior, so the announced output is the same on every run and the screen reader does not read unpredictable values.

### Skills Checklist
- [ ] I know the standard library has no random numbers.
- [ ] I can use a seeded generator.
- [ ] I can test properties of random code.
- [ ] I know this generator is not secure.
- [ ] I can pick a random list item.

---

## Lesson 9.4: Text analysis

### Reading References
- [The Rust Programming Language: Hash Maps](https://doc.rust-lang.org/book/ch08-03-hash-maps.html)
- [The Rust Programming Language: Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 9.4: Data Analysis - Text Analysis

### Learning Objectives
- Split text into words and count them.
- Count word and letter frequencies in a stable order.
- Sort with a tie-break.

### Concept Explanation

`text.split_whitespace()` iterates over the words of a string. Counting uses a map; because a `HashMap` has no stable order, the example keeps first-seen order in a `Vec<(String, u32)>` for words and uses a `BTreeMap` for letters, then sorts the letter pairs with `sort_by`: count descending first, then letter ascending, so ties print in a fixed order.

`to_lowercase()` and `replace(".", "")` normalize the text first. The shared text sample is "A student studies programming. Programming develops problem-solving skills." After lower-casing and removing the periods it has 8 words, and `programming` appears twice.

### Worked Example

```rust
use std::collections::BTreeMap;

fn main() {
    let text = "A student studies programming. Programming develops problem-solving skills.";
    let cleaned = text.to_lowercase().replace('.', "");
    let words: Vec<&str> = cleaned.split_whitespace().collect();

    let mut frequencies: Vec<(String, u32)> = Vec::new();
    for word in &words {
        match frequencies.iter_mut().find(|(known, _)| known == word) {
            Some((_, count)) => *count += 1,
            None => frequencies.push((word.to_string(), 1)),
        }
    }

    println!("Word count: {}", words.len());
    println!("Word frequencies:");
    for (word, count) in &frequencies {
        println!("'{word}': {count}");
    }

    let mut letters: BTreeMap<char, u32> = BTreeMap::new();
    for c in text.to_lowercase().chars().filter(|c| c.is_alphabetic()) {
        *letters.entry(c).or_insert(0) += 1;
    }
    let mut pairs: Vec<(char, u32)> = letters.into_iter().collect();
    pairs.sort_by(|a, b| b.1.cmp(&a.1).then(a.0.cmp(&b.0)));
    println!("Most common letters:");
    for (letter, count) in pairs.iter().take(3) {
        println!("{letter}: {count}");
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Word count: 8
Word frequencies:
'a': 1
'student': 1
'studies': 1
'programming': 2
'develops': 1
'problem-solving': 1
'skills': 1
Most common letters:
s: 7
e: 5
g: 5
```

### Common Mistakes
1. Counting punctuation as part of a word, so `programming.` and `programming` are different words.
2. Forgetting to lower-case first, so `Programming` and `programming` are counted separately.
3. Printing a `HashMap` and expecting a stable order.

### Activities
1. Predict the word count and the count for `programming` before running.
2. Count the words longer than 8 letters.
3. Print the longest word.
4. Change the sort so ties are listed in reverse alphabetical order.

### Accessibility Practice

Read the frequency list in its fixed order. Because the order is stable, you can learn it and compare runs by ear. Print each pair as a short sentence with the same wording every time.

### Skills Checklist
- [ ] I can split text into words.
- [ ] I can count frequencies in a stable order.
- [ ] I can sort with a tie-break.
- [ ] I can remove punctuation first.
- [ ] I can read a stable report.

---

## Lesson 9.5: CSV records

### Reading References
- [The Rust Programming Language: Reading a File](https://doc.rust-lang.org/book/ch12-02-reading-a-file.html)
- [The csv crate](https://docs.rs/csv/)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 9.5: Data Analysis - CSV Files

### Learning Objectives
- Create and read a CSV file.
- Split lines into fields and convert numbers.
- Compute an average and a count.

### Concept Explanation

A CSV (comma-separated values) file stores a table as text. The first line names the columns and each later line is a record. The shared student file has the columns `student_id`, `first_name`, `last_name`, `score`, and `active`, and three records.

The standard library has no CSV reader. `line.split(',')` works only for **simple** files: a value that contains a comma inside quotation marks, such as `"Smith, Jr."`, would be split wrongly. For such files use the `csv` crate or write a real parser.

Every field is text. Convert the score with `parse::<i32>()` and compare `active` with the text `"true"`. With scores 91, 82, and 76 the average is 83.00, and two students are active.

### Worked Example

```rust
use std::fs;
use std::io;

fn main() -> io::Result<()> {
    let content = [
        "student_id,first_name,last_name,score,active",
        "1,Avery,Student,91,true",
        "2,Jordan,Lee,82,true",
        "3,Casey,Smith,76,false",
    ]
    .join("\n")
        + "\n";
    fs::write("students.csv", content)?;

    let text = match fs::read_to_string("students.csv") {
        Ok(text) => text,
        Err(_) => {
            println!("Error: students.csv was not found.");
            return Ok(());
        }
    };
    let mut lines = text.lines();
    let header = lines.next().unwrap_or("");
    println!("Columns: {}", header.split(',').collect::<Vec<_>>().join(", "));

    let mut total = 0;
    let mut active = 0;
    let mut count = 0;
    for line in lines {
        let row: Vec<&str> = line.split(',').collect();
        let score: i32 = row[3].parse().unwrap_or(0);
        total += score;
        count += 1;
        if row[4] == "true" {
            active += 1;
        }
        println!("{}: {} {} scored {}", row[0], row[1], row[2], score);
    }

    println!("Students: {count}");
    println!("Average score: {:.2}", total as f64 / count as f64);
    println!("Active students: {active}");
    Ok(())
}
```

### Expected Behavior or Output

The program prints:
```text
Columns: student_id, first_name, last_name, score, active
1: Avery Student scored 91
2: Jordan Lee scored 82
3: Casey Smith scored 76
Students: 3
Average score: 83.00
Active students: 2
```

### Common Mistakes
1. Splitting a CSV line at every comma when a value contains a quoted comma.
2. Forgetting to convert the text in the score column to a number.
3. Not skipping the header line, so `parse` fails on the text `score`.

### Activities
1. Predict the printed lines before running.
2. Add a fourth student and check the new average.
3. Print only the active students.
4. Explain, with an example, why `"Smith, Jr."` breaks `split(',')`.

### Accessibility Practice

Print one student per line with the same wording each time, so the screen reader announces a repeating pattern that is easy to compare. Read the column names aloud once at the start.

### Skills Checklist
- [ ] I can write and read a CSV file.
- [ ] I can split a line into fields.
- [ ] I convert text fields to numbers.
- [ ] I can compute an average and a count.
- [ ] I know when `split` is not enough.

---

# Unit 10: Project-Based Learning

## Overview
This unit develops project-based learning through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 10.1: Requirements and top-down design

### Reading References
- [The Rust Programming Language: Hash Maps](https://doc.rust-lang.org/book/ch08-03-hash-maps.html)
- [The Rust Programming Language: Functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 10.1: Project Planning and Design

### Learning Objectives
- Write a short requirements list.
- Design a command loop with a map of function pointers.
- Plan in small steps and test each one.

### Concept Explanation

A project is easier to finish when it is planned in small steps. Write down what the program must do (*requirements*), what information it keeps (*data*), and the commands a person can give (*interface*). Build one small piece, test it, then add the next.

Text-based projects share a *command loop*: show a prompt, read a line, find the matching action, and repeat until the user quits. In Rust, a `HashMap<&str, fn()>` holds actions: the keys are command names and the values are *function pointers*. A new command is one new entry, and an unknown command is a failed lookup (`None`) that prints a helpful message.

The loop stops on `quit` and also when input ends. The example is a skeleton with two commands; typing `help`, `look`, an unknown word, and `quit` shows each path.

### Worked Example

```rust
use std::collections::HashMap;
use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn help() {
    println!("Commands: help, look, quit");
}

fn look() {
    println!("You are in a dark cave.");
}

fn main() {
    let mut commands: HashMap<&str, fn()> = HashMap::new();
    commands.insert("help", help);
    commands.insert("look", look);

    println!("Type a command:");
    let mut line = next_line();
    while let Some(text) = &line {
        if text == "quit" {
            break;
        }
        match commands.get(text.as_str()) {
            Some(handler) => handler(),
            None => println!("I don't understand that command. Type help for a list."),
        }
        println!("Type a command:");
        line = next_line();
    }
    println!("Goodbye!");
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
help
look
dance
quit
```

the program prints:
```text
Type a command:
Commands: help, look, quit
Type a command:
You are in a dark cave.
Type a command:
I don't understand that command. Type help for a list.
Type a command:
Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
Type a command:
Goodbye!
```

### Common Mistakes
1. Starting to code before listing the requirements.
2. Using a long chain of `if` statements instead of a map of handlers.
3. Forgetting that an unknown command should say what to do next.

### Activities
1. Write five requirements for the text adventure and the to-do list.
2. Add a `score` command that prints the shared scores.
3. Add the aliases `h` and `l` without copying the functions.
4. Describe the data for the capstone in three sentences.

### Accessibility Practice

Prompts and responses are on separate lines and every response is a complete sentence. Test the prompts by listening to them before you add features.

### Skills Checklist
- [ ] I can list requirements.
- [ ] I can design a command loop.
- [ ] I can use a map of function pointers.
- [ ] I handle unknown commands.
- [ ] I handle the end of input.

---

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- [The Rust Programming Language: Hash Maps](https://doc.rust-lang.org/book/ch08-03-hash-maps.html)
- [The Rust Programming Language: Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 10.2: Building a Text-Based Adventure Game (Part 1)

### Learning Objectives
- Represent rooms and exits with a struct and a map.
- Move the player by command.
- Handle impossible moves and the end of input.

### Concept Explanation

A room is a struct with a `description` and an `exits` map from a direction to the *name* of another room. The program remembers the player's location in one variable. A move looks up the command in the current room's exits; `get` returns an `Option`, so a missing direction is `None` and the program explains that the move is impossible.

This is the same three-room layout as the Python course: a cave, a tunnel, and a clearing. Part 2 adds items and a locked door.

The example is played with north, east, west, up, south, and quit. The command `up` is not an exit anywhere, so it prints the help message.

### Worked Example

```rust
use std::collections::HashMap;
use std::io;

struct Room {
    description: &'static str,
    exits: HashMap<&'static str, &'static str>,
}

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    let mut rooms: HashMap<&str, Room> = HashMap::new();
    rooms.insert("start_room", Room {
        description: "You are in a dimly lit cave. There's a narrow passage to the NORTH.",
        exits: HashMap::from([("north", "tunnel")]),
    });
    rooms.insert("tunnel", Room {
        description: "The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.",
        exits: HashMap::from([("south", "start_room"), ("east", "clearing")]),
    });
    rooms.insert("clearing", Room {
        description: "You've reached a small, sunny clearing. A faint path leads WEST.",
        exits: HashMap::from([("west", "tunnel")]),
    });

    let mut current = "start_room";
    loop {
        println!("---");
        println!("{}", rooms[current].description);
        println!("What do you want to do?");
        let command = next_line().unwrap_or_else(|| "quit".to_string()).to_lowercase();
        if let Some(next) = rooms[current].exits.get(command.as_str()) {
            current = next;
        } else if command == "quit" {
            println!("Exiting game. Goodbye!");
            break;
        } else {
            println!("I don't understand that command or you can't go that way.");
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
north
east
west
up
south
quit
```

the program prints:
```text
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You've reached a small, sunny clearing. A faint path leads WEST.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
I don't understand that command or you can't go that way.
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Indexing `exits[command]` with a direction that is missing, which panics. Use `get`.
2. Forgetting to treat the end of input as `quit`, so the program loops forever when input is piped in.
3. Misspelling a room name in `exits`, so a move leads to a room that does not exist and `rooms[current]` panics.

### Activities
1. Trace the six commands by hand and write the room after each one.
2. Add a fourth room reached from the clearing and test it.
3. Add the aliases `n`, `s`, `e`, and `w`.
4. Write a loop that checks that every exit names a real room.

### Accessibility Practice

Each turn prints a separator line, the description, and the prompt, so a whole turn can be read in order. Listen to one turn from start to finish to confirm that a player could follow it without seeing the screen.

### Skills Checklist
- [ ] I can represent rooms with a struct.
- [ ] I can move the player by command.
- [ ] I can handle an impossible move.
- [ ] I treat end of input as quit.
- [ ] I can trace a game by hand.

---

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- [The Rust Programming Language: Vectors](https://doc.rust-lang.org/book/ch08-01-vectors.html)
- [The Rust Programming Language: References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 10.3: Building a Text-Based Adventure Game (Part 2)

### Learning Objectives
- Keep items in rooms and in an inventory.
- Implement take and use commands.
- Block and then allow a move through a locked door.

### Concept Explanation

Part 2 adds *state*: items in rooms, an inventory, and a door that is locked until the player uses the key. This is the shared specification used by every language track: three rooms (`start`, `locked_door_room`, `treasure_room`); the commands `north`, `south`, `east`, `west`, `take shiny key`, `use shiny key`, and `quit`; the door between the chamber and the treasure room stays locked until the key is used there; reaching the treasure room ends the game.

Items are a `Vec` of names inside each room. Taking an item removes it from the room's list with `get_mut` (a mutable borrow) and adds it to the inventory. The borrow checker needs the immutable borrow of the room to end before the mutable one begins, which is why each command reads what it needs first. The locked door is a `bool` variable.

The example is played with: north (into the chamber), north (the locked door refuses), south, take shiny key, north, use shiny key, north (the treasure room).

### Worked Example

```rust
use std::collections::HashMap;
use std::io;

struct Room {
    description: &'static str,
    exits: HashMap<&'static str, &'static str>,
    items: Vec<&'static str>,
}

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    let mut rooms: HashMap<&str, Room> = HashMap::new();
    rooms.insert("start", Room {
        description: "A dark cave.",
        exits: HashMap::from([("north", "locked_door_room")]),
        items: vec!["shiny key"],
    });
    rooms.insert("locked_door_room", Room {
        description: "A small chamber with a heavy door to the NORTH.",
        exits: HashMap::from([("south", "start"), ("north", "treasure_room")]),
        items: Vec::new(),
    });
    rooms.insert("treasure_room", Room {
        description: "A glittering room full of treasure. You win!",
        exits: HashMap::from([("south", "locked_door_room")]),
        items: Vec::new(),
    });

    let mut current = "start";
    let mut inventory: Vec<&str> = Vec::new();
    let mut door_locked = true;

    loop {
        println!();
        println!("{}", rooms[current].description);
        if current == "treasure_room" {
            break;
        }
        if !rooms[current].items.is_empty() {
            println!("You see: {}", rooms[current].items.join(", "));
        }
        let held = if inventory.is_empty() { "empty".to_string() } else { inventory.join(", ") };
        println!("Your inventory: {held}");
        println!("What do you want to do?");

        let command = next_line().unwrap_or_else(|| "quit".to_string()).to_lowercase();
        let has_key_here = rooms[current].items.contains(&"shiny key");
        let next_room = rooms[current].exits.get(command.as_str()).copied();

        if command == "take shiny key" && has_key_here {
            if let Some(room) = rooms.get_mut(current) {
                room.items.retain(|&item| item != "shiny key");
            }
            inventory.push("shiny key");
            println!("You picked up the shiny key.");
        } else if command == "use shiny key" && current == "locked_door_room" && inventory.contains(&"shiny key") {
            door_locked = false;
            println!("You unlocked the door!");
        } else if let Some(next) = next_room {
            if current == "locked_door_room" && command == "north" && door_locked {
                println!("The door is locked! You need a key.");
            } else {
                current = next;
            }
        } else if command == "quit" {
            println!("Exiting game. Goodbye!");
            break;
        } else {
            println!("I don't understand that command.");
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
north
north
south
take shiny key
north
use shiny key
north
```

the program prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?
The door is locked! You need a key.

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?
You picked up the shiny key.

A dark cave.
Your inventory: shiny key
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?
You unlocked the door!

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?

A glittering room full of treasure. You win!
```

With no standard input at all, the program ends cleanly and prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Making the door's locked state part of the exits so that the "locked" message can never be reached.
2. Holding a reference to a room while calling `get_mut`, which the borrow checker rejects; read what you need first.
3. Printing a fixed room description that still mentions an item after the player has taken it.

### Activities
1. Play the program with the shown commands and follow each turn on paper.
2. Try `use shiny key` in the cave and describe what happens.
3. Add a second item and require both to open the door.
4. List the game's state (location, inventory, door) and say which command changes each part.

### Accessibility Practice

The room description never mentions the key. A separate 'You see:' line lists items, so the description stays true after the key is taken and the screen reader announces the current state.

### Skills Checklist
- [ ] I can store items in rooms and an inventory.
- [ ] I can implement take and use commands.
- [ ] I can block and allow a move.
- [ ] I can explain the borrow-checker constraint.
- [ ] I can keep descriptions true after state changes.

---

## Lesson 10.4: Command-line to-do manager

### Reading References
- [The Rust Programming Language: Recoverable Errors with Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [The Rust Programming Language: Reading a File](https://doc.rust-lang.org/book/ch12-02-reading-a-file.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 10.4: Building a Command-Line To-Do List

### Learning Objectives
- Keep records with the shared fields.
- Save and load them as JSON.
- Offer add, view, mark-done, save, load, and quit commands.

### Concept Explanation

A to-do list ties together records, loops, functions, and files. Each task is a struct with the shared fields `id`, `title`, `description`, `done`, and `created_at`. The program keeps a `Vec<Task>` in memory, shows a numbered menu, and saves the list to `todos.json` when asked and on exit.

Saving uses the teaching JSON helper from Lesson 8.5, included here so the example runs on its own. Each task is converted to a `Json::Object` for saving and rebuilt from one when loading, and the conversion refuses a record with a missing field. At start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program. The timestamp is computed from the system clock in UTC with a short date algorithm, because the standard library has no date formatting.

In the sample session the user adds two tasks, views the list, marks task 2 done, views it again, tries an invalid menu choice, views the list, and quits.

### Worked Example

```rust
#![allow(dead_code)]
use std::collections::BTreeMap;

#[derive(Debug, Clone, PartialEq)]
enum Json {
    Null,
    Bool(bool),
    Int(i64),
    Float(f64),
    Str(String),
    List(Vec<Json>),
    Object(BTreeMap<String, Json>),
}

fn quote(text: &str) -> String {
    let mut out = String::from("\"");
    for c in text.chars() {
        match c {
            '"' => out.push_str("\\\""),
            '\\' => out.push_str("\\\\"),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            c if (c as u32) < 0x20 => out.push_str(&format!("\\u{:04x}", c as u32)),
            c => out.push(c),
        }
    }
    out.push('"');
    out
}

fn encode(value: &Json) -> String {
    match value {
        Json::Null => "null".to_string(),
        Json::Bool(flag) => flag.to_string(),
        Json::Int(number) => number.to_string(),
        Json::Float(number) => number.to_string(),
        Json::Str(text) => quote(text),
        Json::List(items) => {
            let parts: Vec<String> = items.iter().map(encode).collect();
            format!("[{}]", parts.join(","))
        }
        Json::Object(map) => {
            let parts: Vec<String> = map.iter().map(|(key, item)| format!("{}:{}", quote(key), encode(item))).collect();
            format!("{{{}}}", parts.join(","))
        }
    }
}

struct Parser {
    chars: Vec<char>,
    pos: usize,
}

impl Parser {
    fn fail<T>(&self, message: &str) -> Result<T, String> {
        Err(format!("{message} at position {}", self.pos))
    }

    fn skip(&mut self) {
        while self.pos < self.chars.len() && self.chars[self.pos].is_whitespace() {
            self.pos += 1;
        }
    }

    fn peek(&self) -> Option<char> {
        self.chars.get(self.pos).copied()
    }

    fn starts_with(&self, word: &str) -> bool {
        word.chars().enumerate().all(|(i, c)| self.chars.get(self.pos + i) == Some(&c))
    }

    fn value(&mut self) -> Result<Json, String> {
        self.skip();
        match self.peek() {
            None => self.fail("unexpected end of text"),
            Some('{') => self.object(),
            Some('[') => self.list(),
            Some('"') => Ok(Json::Str(self.string()?)),
            Some(c) if c == '-' || c.is_ascii_digit() => self.number(),
            Some(_) if self.starts_with("true") => {
                self.pos += 4;
                Ok(Json::Bool(true))
            }
            Some(_) if self.starts_with("false") => {
                self.pos += 5;
                Ok(Json::Bool(false))
            }
            Some(_) if self.starts_with("null") => {
                self.pos += 4;
                Ok(Json::Null)
            }
            Some(_) => self.fail("unexpected character"),
        }
    }

    fn number(&mut self) -> Result<Json, String> {
        let start = self.pos;
        if self.peek() == Some('-') {
            self.pos += 1;
        }
        while let Some(c) = self.peek() {
            if c.is_ascii_digit() || ".eE+-".contains(c) {
                self.pos += 1;
            } else {
                break;
            }
        }
        let token: String = self.chars[start..self.pos].iter().collect();
        if let Ok(number) = token.parse::<i64>() {
            return Ok(Json::Int(number));
        }
        match token.parse::<f64>() {
            Ok(number) => Ok(Json::Float(number)),
            Err(_) => self.fail("bad number"),
        }
    }

    fn string(&mut self) -> Result<String, String> {
        self.pos += 1;
        let mut out = String::new();
        loop {
            let Some(c) = self.peek() else {
                return self.fail("unterminated string");
            };
            self.pos += 1;
            match c {
                '"' => return Ok(out),
                '\\' => {
                    let Some(escape) = self.peek() else {
                        return self.fail("bad escape");
                    };
                    self.pos += 1;
                    match escape {
                        'n' => out.push('\n'),
                        't' => out.push('\t'),
                        'r' => out.push('\r'),
                        '"' => out.push('"'),
                        '\\' => out.push('\\'),
                        '/' => out.push('/'),
                        'u' => {
                            if self.pos + 4 > self.chars.len() {
                                return self.fail("bad escape");
                            }
                            let hex: String = self.chars[self.pos..self.pos + 4].iter().collect();
                            let code = u32::from_str_radix(&hex, 16).map_err(|_| "bad escape".to_string())?;
                            out.push(char::from_u32(code).unwrap_or('?'));
                            self.pos += 4;
                        }
                        _ => return self.fail("bad escape"),
                    }
                }
                other => out.push(other),
            }
        }
    }

    fn object(&mut self) -> Result<Json, String> {
        self.pos += 1;
        let mut map = BTreeMap::new();
        self.skip();
        if self.peek() == Some('}') {
            self.pos += 1;
            return Ok(Json::Object(map));
        }
        loop {
            self.skip();
            if self.peek() != Some('"') {
                return self.fail("expected a key");
            }
            let key = self.string()?;
            self.skip();
            if self.peek() != Some(':') {
                return self.fail("expected ':'");
            }
            self.pos += 1;
            let item = self.value()?;
            map.insert(key, item);
            self.skip();
            match self.peek() {
                None => return self.fail("unterminated object"),
                Some('}') => {
                    self.pos += 1;
                    return Ok(Json::Object(map));
                }
                Some(',') => self.pos += 1,
                Some(_) => return self.fail("expected ',' or '}'"),
            }
        }
    }

    fn list(&mut self) -> Result<Json, String> {
        self.pos += 1;
        let mut items = Vec::new();
        self.skip();
        if self.peek() == Some(']') {
            self.pos += 1;
            return Ok(Json::List(items));
        }
        loop {
            items.push(self.value()?);
            self.skip();
            match self.peek() {
                None => return self.fail("unterminated list"),
                Some(']') => {
                    self.pos += 1;
                    return Ok(Json::List(items));
                }
                Some(',') => self.pos += 1,
                Some(_) => return self.fail("expected ',' or ']'"),
            }
        }
    }
}

fn decode(text: &str) -> Result<Json, String> {
    let mut parser = Parser { chars: text.chars().collect(), pos: 0 };
    let value = parser.value()?;
    parser.skip();
    if parser.pos < parser.chars.len() {
        return parser.fail("unexpected extra text");
    }
    Ok(value)
}

use std::fs;
use std::io;
use std::time::{SystemTime, UNIX_EPOCH};

struct Task {
    id: i64,
    title: String,
    description: String,
    done: bool,
    created_at: String,
}

fn civil_from_days(days: i64) -> (i64, i64, i64) {
    let z = days + 719468;
    let era = z.div_euclid(146097);
    let doe = z.rem_euclid(146097);
    let yoe = (doe - doe / 1460 + doe / 36524 - doe / 146096) / 365;
    let year = yoe + era * 400;
    let doy = doe - (365 * yoe + yoe / 4 - yoe / 100);
    let mp = (5 * doy + 2) / 153;
    let day = doy - (153 * mp + 2) / 5 + 1;
    let month = if mp < 10 { mp + 3 } else { mp - 9 };
    (if month <= 2 { year + 1 } else { year }, month, day)
}

fn now_iso() -> String {
    let seconds = SystemTime::now().duration_since(UNIX_EPOCH).map(|d| d.as_secs() as i64).unwrap_or(0);
    let (year, month, day) = civil_from_days(seconds.div_euclid(86400));
    let rest = seconds.rem_euclid(86400);
    format!("{year:04}-{month:02}-{day:02}T{:02}:{:02}:{:02}", rest / 3600, rest % 3600 / 60, rest % 60)
}

fn to_json(task: &Task) -> Json {
    let mut map = BTreeMap::new();
    map.insert("id".to_string(), Json::Int(task.id));
    map.insert("title".to_string(), Json::Str(task.title.clone()));
    map.insert("description".to_string(), Json::Str(task.description.clone()));
    map.insert("done".to_string(), Json::Bool(task.done));
    map.insert("created_at".to_string(), Json::Str(task.created_at.clone()));
    Json::Object(map)
}

fn text_field(map: &BTreeMap<String, Json>, key: &str) -> Result<String, String> {
    match map.get(key) {
        Some(Json::Str(text)) => Ok(text.clone()),
        _ => Err(format!("missing field {key}")),
    }
}

fn from_json(value: &Json) -> Result<Task, String> {
    let Json::Object(map) = value else {
        return Err("a task must be an object".to_string());
    };
    let id = match map.get("id") {
        Some(Json::Int(number)) => *number,
        _ => return Err("missing field id".to_string()),
    };
    Ok(Task {
        id,
        title: text_field(map, "title")?,
        description: text_field(map, "description")?,
        done: map.get("done") == Some(&Json::Bool(true)),
        created_at: text_field(map, "created_at")?,
    })
}

fn load_todos() -> Vec<Task> {
    let text = match fs::read_to_string("todos.json") {
        Ok(text) => text,
        Err(_) => {
            println!("No existing tasks found.");
            return Vec::new();
        }
    };
    let loaded = match decode(&text) {
        Ok(Json::List(items)) => items.iter().map(from_json).collect::<Result<Vec<Task>, String>>(),
        Ok(_) => Err("expected a list".to_string()),
        Err(message) => Err(message),
    };
    match loaded {
        Ok(tasks) => {
            println!("Tasks loaded.");
            tasks
        }
        Err(_) => {
            println!("Error: todos.json is not valid JSON. Starting with an empty list.");
            Vec::new()
        }
    }
}

fn save_todos(todos: &[Task]) -> io::Result<()> {
    let list = Json::List(todos.iter().map(to_json).collect());
    fs::write("todos.json", encode(&list))?;
    println!("Tasks saved.");
    Ok(())
}

fn add_task(todos: &mut Vec<Task>, title: &str, description: &str) {
    if title.trim().is_empty() {
        println!("A title is required.");
        return;
    }
    let id = todos.iter().map(|task| task.id).max().unwrap_or(0) + 1;
    todos.push(Task {
        id,
        title: title.trim().to_string(),
        description: description.trim().to_string(),
        done: false,
        created_at: now_iso(),
    });
    println!("Task '{}' added.", title.trim());
}

fn view_tasks(todos: &[Task]) {
    if todos.is_empty() {
        println!("No tasks in your list.");
        return;
    }
    println!("--- Your To-Do List ---");
    for task in todos {
        let status = if task.done { "done" } else { "not done" };
        println!("{}. {} ({})", task.id, task.title, status);
    }
    println!("-----------------------");
}

fn mark_done(todos: &mut [Task], text: &str) {
    let Ok(id) = text.trim().parse::<i64>() else {
        println!("Please enter a whole number.");
        return;
    };
    match todos.iter_mut().find(|task| task.id == id) {
        Some(task) => {
            task.done = true;
            println!("Task '{}' marked as done.", task.title);
        }
        None => println!("No task has that number."),
    }
}

fn show_menu() {
    println!();
    println!("--- To-Do List Menu ---");
    println!("1. Add Task");
    println!("2. View Tasks");
    println!("3. Mark Task Done");
    println!("4. Save Tasks");
    println!("5. Load Tasks");
    println!("6. Quit");
    println!("-----------------------");
}

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() -> io::Result<()> {
    let mut todos = load_todos();
    loop {
        show_menu();
        println!("Enter your choice (1-6):");
        let choice = next_line().unwrap_or_else(|| "6".to_string());
        match choice.as_str() {
            "1" => {
                println!("Enter task title:");
                let title = next_line().unwrap_or_default();
                println!("Enter task description:");
                let description = next_line().unwrap_or_default();
                add_task(&mut todos, &title, &description);
            }
            "2" => view_tasks(&todos),
            "3" => {
                view_tasks(&todos);
                println!("Enter task number to mark done:");
                let text = next_line().unwrap_or_default();
                mark_done(&mut todos, &text);
            }
            "4" => save_todos(&todos)?,
            "5" => todos = load_todos(),
            "6" => {
                save_todos(&todos)?;
                println!("Goodbye!");
                return Ok(());
            }
            _ => println!("Invalid choice. Please try again."),
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
1
Study programming
Finish Unit 10
1
Review scores
Check the four scores
2
3
2
3
7
2
6
```

the program prints:
```text
No existing tasks found.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Study programming' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Review scores' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------
Enter task number to mark done:
Task 'Review scores' marked as done.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------
Enter task number to mark done:
No task has that number.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Tasks saved.
Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
No existing tasks found.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Tasks saved.
Goodbye!
```

### Common Mistakes
1. Saving the file but never loading it, so tasks disappear between runs.
2. Reusing a deleted task's id, which can confuse saved references.
3. Letting a damaged `todos.json` crash the program instead of printing a message.

### Activities
1. Run the sample session, then run the program again typing `2` and `6` to see the saved tasks.
2. Add a command to delete a task by number.
3. Open `todos.json` and read the saved text. Edit it to remove a bracket and run the program again.
4. Show each task's description in the view command.

### Accessibility Practice

Every menu is printed as numbered lines and every prompt is on its own line. The status words are `done` and `not done`, not symbols, so the list reads clearly in speech and braille.

### Skills Checklist
- [ ] I can keep records with the shared fields.
- [ ] I can save and load JSON.
- [ ] I handle a missing or damaged file.
- [ ] I keep ids unique.
- [ ] I show status in words.

---

## Lesson 10.5: Accessible interaction and validation

### Reading References
- [The Rust Programming Language: Recoverable Errors with Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [The Rust Programming Language: Option](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 10.5: Refining User Experience and Validation

### Learning Objectives
- Write reusable validation functions.
- Limit retries and handle the end of input.
- Write clear, accessible messages.

### Concept Explanation

Reusable validation functions make every menu and form consistent. `ask_number(prompt, low, high, attempts)` prints a prompt, reads a line, converts it, checks the range, and either returns `Some(number)` or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns `None`. `ask_yes_no(prompt)` returns `Option<bool>` and accepts `y`, `yes`, `n`, and `no` in any letter case. The `Option` return type makes the caller deal with the failure case.

Good messages say *what was wrong* and *what to do*: "Enter a whole number from 0 to 100," not "Invalid." They never depend on color, position, or symbols alone, and they use the same wording every time.

The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y.

### Worked Example

```rust
use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn ask_number(prompt: &str, low: i32, high: i32, attempts: u32) -> Option<i32> {
    for attempt in 1..=attempts {
        println!("{prompt}");
        let text = next_line()?;
        if let Ok(number) = text.parse::<i32>() {
            if (low..=high).contains(&number) {
                return Some(number);
            }
        }
        println!("Enter a whole number from {low} to {high}. You have {} attempt(s) left.", attempts - attempt);
    }
    None
}

fn ask_yes_no(prompt: &str) -> Option<bool> {
    loop {
        println!("{prompt} (yes or no)");
        let text = next_line()?.to_lowercase();
        match text.as_str() {
            "y" | "yes" => return Some(true),
            "n" | "no" => return Some(false),
            _ => println!("Please answer yes or no."),
        }
    }
}

fn main() {
    match ask_number("Enter a score from 0 to 100:", 0, 100, 3) {
        Some(score) => println!("Accepted score: {score}"),
        None => println!("No valid score was entered."),
    }

    let keep = ask_yes_no("Save this score?");
    println!("Save answer: {:?}", keep);
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
abc
105
88
maybe
y
```

the program prints:
```text
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 2 attempt(s) left.
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 1 attempt(s) left.
Enter a score from 0 to 100:
Accepted score: 88
Save this score? (yes or no)
Please answer yes or no.
Save this score? (yes or no)
Save answer: Some(true)
```

With no standard input at all, the program ends cleanly and prints:
```text
Enter a score from 0 to 100:
No valid score was entered.
Save this score? (yes or no)
Save answer: None
```

### Common Mistakes
1. Writing the message "Invalid" without saying what is valid.
2. Accepting a decimal such as 88.5 for a field that requires a whole number.
3. Looping forever on bad input instead of limiting attempts.

### Activities
1. Run the sample input and read each message aloud.
2. Run with three invalid numbers and read the final message.
3. Add `ask_text(prompt) -> Option<String>` that rejects empty answers.
4. Rewrite two messages from earlier lessons so they say what to do next.

### Accessibility Practice

Check that every error message ends with an action the user can take, and that the same situation always produces the same words.

### Skills Checklist
- [ ] I can write reusable validation functions.
- [ ] I limit retries.
- [ ] I handle the end of input.
- [ ] I write messages that say what to do.
- [ ] I keep wording consistent.

---

# Unit 11: Capstone

## Overview
This unit develops capstone through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 11.1: Requirements and design

### Reading References
- [The Rust Programming Language: Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [The Rust Programming Language: Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 11.1: Introduction to NiceGUI

### Learning Objectives
- Write requirements for a personal data manager.
- Define the shared record schema as a struct.
- Check records against the validation rules before building features.

### Concept Explanation

The capstone is a *personal data manager*: a program that keeps a list of records, lets the user add, view, search, change, complete, and delete them, and saves them to a file. In the Rust track it is a text program, so it runs from the terminal and is fully usable with a screen reader or braille display.

**Shared record schema (all general-purpose language tracks).** Every record has `id` (unique whole number), `title`, `description`, `category`, `created_at`, and `updated_at` (ISO 8601 text). A project may add fields, such as an optional `done` flag, but must not remove these. Rust field names use `snake_case`, the same as the stored JSON.

**Validation rules.** A record must have a non-empty title and a non-empty category. Timestamps are ISO 8601 text such as `2026-01-15T09:00:00`. A `Result<(), String>` return type states in the signature that validation can fail with a message.

Design before coding: list the operations, then the data, then the messages. The example checks the three shared sample records against the rules and prints them as a plain-text list.

### Worked Example

```rust
struct Entry {
    id: i32,
    title: String,
    description: String,
    category: String,
    created_at: String,
    updated_at: String,
}

fn validate(title: &str, category: &str) -> Result<(), String> {
    if title.trim().is_empty() {
        return Err("A title is required.".to_string());
    }
    if category.trim().is_empty() {
        return Err("A category is required.".to_string());
    }
    Ok(())
}

fn entry(id: i32, title: &str, description: &str, category: &str, created_at: &str) -> Entry {
    Entry {
        id,
        title: title.to_string(),
        description: description.to_string(),
        category: category.to_string(),
        created_at: created_at.to_string(),
        updated_at: created_at.to_string(),
    }
}

fn main() {
    let sample = vec![
        entry(1, "Notebook", "Course notes", "supplies", "2026-01-15T09:00:00"),
        entry(2, "Pencil", "Box of 10", "supplies", "2026-01-15T09:05:00"),
        entry(3, "Study plan", "Weekly schedule", "planning", "2026-01-15T09:10:00"),
    ];

    for record in &sample {
        let outcome = match validate(&record.title, &record.category) {
            Ok(()) => "valid".to_string(),
            Err(message) => message,
        };
        println!("{}. {} [{}] - {}", record.id, record.title, record.category, outcome);
    }
    println!("{} | {} | {}", sample[0].description, sample[0].created_at, sample[0].updated_at);

    println!("{:?}", validate("  ", "supplies"));
    println!("{:?}", validate("Ruler", ""));
}
```

### Expected Behavior or Output

The program prints:
```text
1. Notebook [supplies] - valid
2. Pencil [supplies] - valid
3. Study plan [planning] - valid
Course notes | 2026-01-15T09:00:00 | 2026-01-15T09:00:00
Err("A title is required.")
Err("A category is required.")
```

### Common Mistakes
1. Starting to build features before agreeing on the record fields.
2. Allowing a record with an empty title because the check was left for later.
3. Storing timestamps in different formats in different places.

### Activities
1. Write the seven operations as a numbered list of requirements.
2. Add one project-specific field and say how it is validated.
3. Write three sample records for your own project.
4. Describe in plain sentences what each shared field means.

### Accessibility Practice

Design the screen output as lines of plain text: one record per line, with the same field order each time. Decide the wording of every message now so that it can be tested.

### Skills Checklist
- [ ] I can write requirements.
- [ ] I know the shared record fields.
- [ ] I can write validation rules.
- [ ] I can describe sample data.
- [ ] I can plan messages before coding.

---

## Lesson 11.2: Data model and storage

### Reading References
- [The Rust Programming Language: Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [The Rust Programming Language: Reading a File](https://doc.rust-lang.org/book/ch12-02-reading-a-file.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 11.2: Data Model and Storage

### Learning Objectives
- Store records as structs.
- Save and load them as JSON.
- Confirm that every field survives a round trip.

### Concept Explanation

Records are stored as a `Vec<Entry>` in memory and as a JSON array on disk. The storage layer has two functions: `save_entries(path, entries)` and `load_entries(path)`, which returns `Result<Vec<Entry>, String>` so the caller decides what to do when the file is missing or damaged.

An `Entry` is converted to a `Json::Object` for saving (`to_json`) and rebuilt from one when loading (`from_json`), which checks that each field is present and has the right type. The optional `done` field defaults to `false`.

The example uses the teaching JSON helper from Lesson 8.5 (included so the program runs on its own). After saving and reloading it compares the lists; deriving `PartialEq` lets Rust compare structs field by field, so this *round-trip test* checks every field of every entry. It is the first acceptance test for storage.

### Worked Example

```rust
#![allow(dead_code)]
use std::collections::BTreeMap;

#[derive(Debug, Clone, PartialEq)]
enum Json {
    Null,
    Bool(bool),
    Int(i64),
    Float(f64),
    Str(String),
    List(Vec<Json>),
    Object(BTreeMap<String, Json>),
}

fn quote(text: &str) -> String {
    let mut out = String::from("\"");
    for c in text.chars() {
        match c {
            '"' => out.push_str("\\\""),
            '\\' => out.push_str("\\\\"),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            c if (c as u32) < 0x20 => out.push_str(&format!("\\u{:04x}", c as u32)),
            c => out.push(c),
        }
    }
    out.push('"');
    out
}

fn encode(value: &Json) -> String {
    match value {
        Json::Null => "null".to_string(),
        Json::Bool(flag) => flag.to_string(),
        Json::Int(number) => number.to_string(),
        Json::Float(number) => number.to_string(),
        Json::Str(text) => quote(text),
        Json::List(items) => {
            let parts: Vec<String> = items.iter().map(encode).collect();
            format!("[{}]", parts.join(","))
        }
        Json::Object(map) => {
            let parts: Vec<String> = map.iter().map(|(key, item)| format!("{}:{}", quote(key), encode(item))).collect();
            format!("{{{}}}", parts.join(","))
        }
    }
}

struct Parser {
    chars: Vec<char>,
    pos: usize,
}

impl Parser {
    fn fail<T>(&self, message: &str) -> Result<T, String> {
        Err(format!("{message} at position {}", self.pos))
    }

    fn skip(&mut self) {
        while self.pos < self.chars.len() && self.chars[self.pos].is_whitespace() {
            self.pos += 1;
        }
    }

    fn peek(&self) -> Option<char> {
        self.chars.get(self.pos).copied()
    }

    fn starts_with(&self, word: &str) -> bool {
        word.chars().enumerate().all(|(i, c)| self.chars.get(self.pos + i) == Some(&c))
    }

    fn value(&mut self) -> Result<Json, String> {
        self.skip();
        match self.peek() {
            None => self.fail("unexpected end of text"),
            Some('{') => self.object(),
            Some('[') => self.list(),
            Some('"') => Ok(Json::Str(self.string()?)),
            Some(c) if c == '-' || c.is_ascii_digit() => self.number(),
            Some(_) if self.starts_with("true") => {
                self.pos += 4;
                Ok(Json::Bool(true))
            }
            Some(_) if self.starts_with("false") => {
                self.pos += 5;
                Ok(Json::Bool(false))
            }
            Some(_) if self.starts_with("null") => {
                self.pos += 4;
                Ok(Json::Null)
            }
            Some(_) => self.fail("unexpected character"),
        }
    }

    fn number(&mut self) -> Result<Json, String> {
        let start = self.pos;
        if self.peek() == Some('-') {
            self.pos += 1;
        }
        while let Some(c) = self.peek() {
            if c.is_ascii_digit() || ".eE+-".contains(c) {
                self.pos += 1;
            } else {
                break;
            }
        }
        let token: String = self.chars[start..self.pos].iter().collect();
        if let Ok(number) = token.parse::<i64>() {
            return Ok(Json::Int(number));
        }
        match token.parse::<f64>() {
            Ok(number) => Ok(Json::Float(number)),
            Err(_) => self.fail("bad number"),
        }
    }

    fn string(&mut self) -> Result<String, String> {
        self.pos += 1;
        let mut out = String::new();
        loop {
            let Some(c) = self.peek() else {
                return self.fail("unterminated string");
            };
            self.pos += 1;
            match c {
                '"' => return Ok(out),
                '\\' => {
                    let Some(escape) = self.peek() else {
                        return self.fail("bad escape");
                    };
                    self.pos += 1;
                    match escape {
                        'n' => out.push('\n'),
                        't' => out.push('\t'),
                        'r' => out.push('\r'),
                        '"' => out.push('"'),
                        '\\' => out.push('\\'),
                        '/' => out.push('/'),
                        'u' => {
                            if self.pos + 4 > self.chars.len() {
                                return self.fail("bad escape");
                            }
                            let hex: String = self.chars[self.pos..self.pos + 4].iter().collect();
                            let code = u32::from_str_radix(&hex, 16).map_err(|_| "bad escape".to_string())?;
                            out.push(char::from_u32(code).unwrap_or('?'));
                            self.pos += 4;
                        }
                        _ => return self.fail("bad escape"),
                    }
                }
                other => out.push(other),
            }
        }
    }

    fn object(&mut self) -> Result<Json, String> {
        self.pos += 1;
        let mut map = BTreeMap::new();
        self.skip();
        if self.peek() == Some('}') {
            self.pos += 1;
            return Ok(Json::Object(map));
        }
        loop {
            self.skip();
            if self.peek() != Some('"') {
                return self.fail("expected a key");
            }
            let key = self.string()?;
            self.skip();
            if self.peek() != Some(':') {
                return self.fail("expected ':'");
            }
            self.pos += 1;
            let item = self.value()?;
            map.insert(key, item);
            self.skip();
            match self.peek() {
                None => return self.fail("unterminated object"),
                Some('}') => {
                    self.pos += 1;
                    return Ok(Json::Object(map));
                }
                Some(',') => self.pos += 1,
                Some(_) => return self.fail("expected ',' or '}'"),
            }
        }
    }

    fn list(&mut self) -> Result<Json, String> {
        self.pos += 1;
        let mut items = Vec::new();
        self.skip();
        if self.peek() == Some(']') {
            self.pos += 1;
            return Ok(Json::List(items));
        }
        loop {
            items.push(self.value()?);
            self.skip();
            match self.peek() {
                None => return self.fail("unterminated list"),
                Some(']') => {
                    self.pos += 1;
                    return Ok(Json::List(items));
                }
                Some(',') => self.pos += 1,
                Some(_) => return self.fail("expected ',' or ']'"),
            }
        }
    }
}

fn decode(text: &str) -> Result<Json, String> {
    let mut parser = Parser { chars: text.chars().collect(), pos: 0 };
    let value = parser.value()?;
    parser.skip();
    if parser.pos < parser.chars.len() {
        return parser.fail("unexpected extra text");
    }
    Ok(value)
}

use std::fs;

#[derive(Debug, Clone, PartialEq)]
struct Entry {
    id: i64,
    title: String,
    description: String,
    category: String,
    created_at: String,
    updated_at: String,
    done: bool,
}

fn to_json(entry: &Entry) -> Json {
    let mut map = BTreeMap::new();
    map.insert("id".to_string(), Json::Int(entry.id));
    map.insert("title".to_string(), Json::Str(entry.title.clone()));
    map.insert("description".to_string(), Json::Str(entry.description.clone()));
    map.insert("category".to_string(), Json::Str(entry.category.clone()));
    map.insert("created_at".to_string(), Json::Str(entry.created_at.clone()));
    map.insert("updated_at".to_string(), Json::Str(entry.updated_at.clone()));
    map.insert("done".to_string(), Json::Bool(entry.done));
    Json::Object(map)
}

fn text_field(map: &BTreeMap<String, Json>, key: &str) -> Result<String, String> {
    match map.get(key) {
        Some(Json::Str(text)) => Ok(text.clone()),
        _ => Err(format!("missing field {key}")),
    }
}

fn from_json(value: &Json) -> Result<Entry, String> {
    let Json::Object(map) = value else {
        return Err("a record must be an object".to_string());
    };
    let id = match map.get("id") {
        Some(Json::Int(number)) => *number,
        _ => return Err("missing field id".to_string()),
    };
    Ok(Entry {
        id,
        title: text_field(map, "title")?,
        description: text_field(map, "description")?,
        category: text_field(map, "category")?,
        created_at: text_field(map, "created_at")?,
        updated_at: text_field(map, "updated_at")?,
        done: map.get("done") == Some(&Json::Bool(true)),
    })
}

fn save_entries(path: &str, entries: &[Entry]) -> Result<(), String> {
    let list = Json::List(entries.iter().map(to_json).collect());
    fs::write(path, encode(&list)).map_err(|_| format!("Could not write {path}."))
}

fn load_entries(path: &str) -> Result<Vec<Entry>, String> {
    let text = fs::read_to_string(path).map_err(|_| format!("Could not open {path}: file not found."))?;
    match decode(&text) {
        Ok(Json::List(items)) => items.iter().map(from_json).collect::<Result<Vec<Entry>, String>>().map_err(|e| format!("The data file is not valid: {e}")),
        Ok(_) => Err("The data file is not valid: expected a list".to_string()),
        Err(message) => Err(format!("The data file is not valid: {message}")),
    }
}

fn entry(id: i64, title: &str, description: &str, category: &str, stamp: &str) -> Entry {
    Entry {
        id,
        title: title.to_string(),
        description: description.to_string(),
        category: category.to_string(),
        created_at: stamp.to_string(),
        updated_at: stamp.to_string(),
        done: false,
    }
}

fn main() {
    let sample = vec![
        entry(1, "Notebook", "Course notes", "supplies", "2026-01-15T09:00:00"),
        entry(2, "Pencil", "Box of 10", "supplies", "2026-01-15T09:05:00"),
        entry(3, "Study plan", "Weekly schedule", "planning", "2026-01-15T09:10:00"),
    ];

    println!("{:?}", save_entries("records.json", &sample));
    match load_entries("records.json") {
        Ok(loaded) => {
            println!("Round trip preserved all fields: {}", loaded == sample);
            println!("Records loaded: {}", loaded.len());
        }
        Err(message) => println!("{message}"),
    }

    if let Err(message) = load_entries("missing.json") {
        println!("{message}");
    }

    fs::write("broken.json", "[{\"id\": 1,").expect("could not write the broken file");
    if let Err(message) = load_entries("broken.json") {
        println!("{message}");
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Ok(())
Round trip preserved all fields: true
Records loaded: 3
Could not open missing.json: file not found.
The data file is not valid: expected a key at position 10
```

### Common Mistakes
1. Overwriting the data file with an empty list after a failed load.
2. Saving only some of the fields.
3. Assuming a loaded record has every field without checking.

### Activities
1. Run the program and open `records.json` to read the saved text.
2. Add a field to `Entry`, save it, and confirm that it survives the round trip.
3. Make `from_json` reject a record whose title is blank.
4. Explain why `load_entries` returns a `Result` and does not panic.

### Accessibility Practice

Messages that name the file and the problem read clearly in speech. After saving, read the file in the terminal to confirm it contains what you expect.

### Skills Checklist
- [ ] I can store records in structs.
- [ ] I can save and load JSON.
- [ ] I can run a round-trip test.
- [ ] I handle missing and damaged files.
- [ ] I do not overwrite good data after a failed load.

---

## Lesson 11.3: Create, read, update, delete

### Reading References
- [The Rust Programming Language: Method Syntax](https://doc.rust-lang.org/book/ch05-03-method-syntax.html)
- [The Rust Programming Language: Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 11.3: Displaying and Managing Items

### Learning Objectives
- Add, list, search, change, complete, and delete records.
- Assign new ids and update timestamps correctly.
- Return a `Result` with a message when an operation cannot be done.

### Concept Explanation

A `Manager` struct owns the entries and offers one method per operation. Each method that can fail returns a `Result<_, String>` whose `Err` holds the message to show. New ids are one more than the highest id, so ids are never reused while higher ids exist. Updating an entry sets `updated_at` but never changes `created_at`. A `Changes` struct with `Option` fields says which fields to change, so `Changes { done: Some(true), ..Default::default() }` changes only `done`. Completing an entry counts as an update.

For repeatable output the example passes in a *fake clock*: a boxed closure that returns a new fixed time on each call. A real program passes a closure that reads the real time.

The example adds the three shared sample records, lists them, searches for "note", changes one description, completes one entry, deletes one, and tries to delete an entry that does not exist.

### Worked Example

```rust
#![allow(dead_code)]
struct Entry {
    id: i32,
    title: String,
    description: String,
    category: String,
    created_at: String,
    updated_at: String,
    done: bool,
}

impl Entry {
    fn describe(&self) -> String {
        format!("{}. {} [{}] ({})", self.id, self.title, self.category, if self.done { "done" } else { "not done" })
    }
}

#[derive(Default)]
struct Changes {
    title: Option<String>,
    description: Option<String>,
    category: Option<String>,
    done: Option<bool>,
}

fn validate(title: &str, category: &str) -> Result<(), String> {
    if title.trim().is_empty() {
        return Err("A title is required.".to_string());
    }
    if category.trim().is_empty() {
        return Err("A category is required.".to_string());
    }
    Ok(())
}

struct Manager {
    entries: Vec<Entry>,
    clock: Box<dyn FnMut() -> String>,
}

impl Manager {
    fn new(clock: Box<dyn FnMut() -> String>) -> Manager {
        Manager { entries: Vec::new(), clock }
    }

    fn next_id(&self) -> i32 {
        self.entries.iter().map(|entry| entry.id).max().unwrap_or(0) + 1
    }

    fn find(&self, id: i32) -> Option<&Entry> {
        self.entries.iter().find(|entry| entry.id == id)
    }

    fn add(&mut self, title: &str, description: &str, category: &str) -> Result<i32, String> {
        validate(title, category)?;
        let stamp = (self.clock)();
        let id = self.next_id();
        self.entries.push(Entry {
            id,
            title: title.trim().to_string(),
            description: description.trim().to_string(),
            category: category.trim().to_string(),
            created_at: stamp.clone(),
            updated_at: stamp,
            done: false,
        });
        Ok(id)
    }

    fn update(&mut self, id: i32, changes: Changes) -> Result<(), String> {
        let (title, category) = match self.find(id) {
            Some(entry) => (
                changes.title.clone().unwrap_or_else(|| entry.title.clone()),
                changes.category.clone().unwrap_or_else(|| entry.category.clone()),
            ),
            None => return Err("No record has that id.".to_string()),
        };
        validate(&title, &category)?;
        let stamp = (self.clock)();
        let entry = self.entries.iter_mut().find(|entry| entry.id == id).ok_or("No record has that id.")?;
        if let Some(value) = changes.title {
            entry.title = value.trim().to_string();
        }
        if let Some(value) = changes.description {
            entry.description = value.trim().to_string();
        }
        if let Some(value) = changes.category {
            entry.category = value.trim().to_string();
        }
        if let Some(value) = changes.done {
            entry.done = value;
        }
        entry.updated_at = stamp;
        Ok(())
    }

    fn complete(&mut self, id: i32) -> Result<(), String> {
        self.update(id, Changes { done: Some(true), ..Default::default() })
    }

    fn delete(&mut self, id: i32) -> Result<(), String> {
        let position = self.entries.iter().position(|entry| entry.id == id).ok_or("No record has that id.")?;
        self.entries.remove(position);
        Ok(())
    }

    fn search(&self, text: &str) -> Vec<&Entry> {
        let needle = text.trim().to_lowercase();
        self.entries
            .iter()
            .filter(|entry| entry.title.to_lowercase().contains(&needle) || entry.description.to_lowercase().contains(&needle))
            .collect()
    }
}

fn fake_clock() -> Box<dyn FnMut() -> String> {
    let mut ticks = 0;
    Box::new(move || {
        ticks += 1;
        format!("2026-01-15T10:00:{ticks:02}")
    })
}

fn show(manager: &Manager) {
    for entry in &manager.entries {
        println!("{}", entry.describe());
    }
}

fn main() {
    let mut manager = Manager::new(fake_clock());
    manager.add("Notebook", "Course notes", "supplies").unwrap();
    manager.add("Pencil", "Box of 10", "supplies").unwrap();
    manager.add("Study plan", "Weekly schedule", "planning").unwrap();
    show(&manager);

    println!("Search for 'note':");
    for entry in manager.search("note") {
        println!("{}", entry.title);
    }

    manager.update(2, Changes { description: Some("Box of 12".to_string()), ..Default::default() }).unwrap();
    manager.complete(3).unwrap();
    if let Some(entry) = manager.find(2) {
        println!("{} {} {}", entry.description, entry.created_at, entry.updated_at);
    }

    println!("{:?}", manager.delete(1));
    println!("{:?}", manager.delete(99));
    show(&manager);
}
```

### Expected Behavior or Output

The program prints:
```text
1. Notebook [supplies] (not done)
2. Pencil [supplies] (not done)
3. Study plan [planning] (not done)
Search for 'note':
Notebook
Box of 12 2026-01-15T10:00:02 2026-01-15T10:00:04
Ok(())
Err("No record has that id.")
2. Pencil [supplies] (not done)
3. Study plan [planning] (done)
```

### Common Mistakes
1. Reusing a deleted entry's id by counting the vector length instead of using the highest id.
2. Changing `created_at` when updating a record.
3. Calling `unwrap()` on every `Result` in a real program instead of showing the message to the user.

### Activities
1. Predict the output before running.
2. Add `list_by_category(category)` to `Manager`.
3. Add a rule that blocks completing an entry that is already complete, with a message.
4. Explain how the fake clock makes the output repeatable.

### Accessibility Practice

List output uses the same fixed format for every record and the words `done` and `not done`. Search results print only titles, so each line is short.

### Skills Checklist
- [ ] I can implement add, list, search, change, complete, and delete.
- [ ] I assign unique ids.
- [ ] I update timestamps correctly.
- [ ] I return clear messages for failures.
- [ ] I can make output repeatable with a fake clock.

---

## Lesson 11.4: Validation and tests

### Reading References
- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Rust Programming Language: Test Organization](https://doc.rust-lang.org/book/ch11-03-test-organization.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 11.4: Testing and Refinement

### Learning Objectives
- Run the shared acceptance tests.
- Verify that validation rejects bad data.
- Read and interpret test results.

### Concept Explanation

The shared acceptance tests describe behavior that every language track's capstone must show:

1. Adding a record with an empty title is rejected with a clear message.
2. A new record receives an unused `id`.
3. Updating a record changes `updated_at` but not `created_at`.
4. Deleting a record removes only that record.
5. Saving and reloading preserves all fields and values (shown in Lesson 11.2).
6. Every message and control can be used without color or a mouse (checked by hand in Lesson 11.5).

This lesson automates tests 1 to 4 and also tests completion and the rejection of a blank title in an update. Each test builds a new `Manager`, so tests cannot affect each other. The fake clock keeps timestamps predictable so a test can check that `updated_at` changed while `created_at` did not. Each test is a function returning `Result<(), String>`, run by a small loop that prints PASS or FAIL.

### Worked Example

```rust
#![allow(dead_code)]
struct Entry {
    id: i32,
    title: String,
    description: String,
    category: String,
    created_at: String,
    updated_at: String,
    done: bool,
}

impl Entry {
    fn describe(&self) -> String {
        format!("{}. {} [{}] ({})", self.id, self.title, self.category, if self.done { "done" } else { "not done" })
    }
}

#[derive(Default)]
struct Changes {
    title: Option<String>,
    description: Option<String>,
    category: Option<String>,
    done: Option<bool>,
}

fn validate(title: &str, category: &str) -> Result<(), String> {
    if title.trim().is_empty() {
        return Err("A title is required.".to_string());
    }
    if category.trim().is_empty() {
        return Err("A category is required.".to_string());
    }
    Ok(())
}

struct Manager {
    entries: Vec<Entry>,
    clock: Box<dyn FnMut() -> String>,
}

impl Manager {
    fn new(clock: Box<dyn FnMut() -> String>) -> Manager {
        Manager { entries: Vec::new(), clock }
    }

    fn next_id(&self) -> i32 {
        self.entries.iter().map(|entry| entry.id).max().unwrap_or(0) + 1
    }

    fn find(&self, id: i32) -> Option<&Entry> {
        self.entries.iter().find(|entry| entry.id == id)
    }

    fn add(&mut self, title: &str, description: &str, category: &str) -> Result<i32, String> {
        validate(title, category)?;
        let stamp = (self.clock)();
        let id = self.next_id();
        self.entries.push(Entry {
            id,
            title: title.trim().to_string(),
            description: description.trim().to_string(),
            category: category.trim().to_string(),
            created_at: stamp.clone(),
            updated_at: stamp,
            done: false,
        });
        Ok(id)
    }

    fn update(&mut self, id: i32, changes: Changes) -> Result<(), String> {
        let (title, category) = match self.find(id) {
            Some(entry) => (
                changes.title.clone().unwrap_or_else(|| entry.title.clone()),
                changes.category.clone().unwrap_or_else(|| entry.category.clone()),
            ),
            None => return Err("No record has that id.".to_string()),
        };
        validate(&title, &category)?;
        let stamp = (self.clock)();
        let entry = self.entries.iter_mut().find(|entry| entry.id == id).ok_or("No record has that id.")?;
        if let Some(value) = changes.title {
            entry.title = value.trim().to_string();
        }
        if let Some(value) = changes.description {
            entry.description = value.trim().to_string();
        }
        if let Some(value) = changes.category {
            entry.category = value.trim().to_string();
        }
        if let Some(value) = changes.done {
            entry.done = value;
        }
        entry.updated_at = stamp;
        Ok(())
    }

    fn complete(&mut self, id: i32) -> Result<(), String> {
        self.update(id, Changes { done: Some(true), ..Default::default() })
    }

    fn delete(&mut self, id: i32) -> Result<(), String> {
        let position = self.entries.iter().position(|entry| entry.id == id).ok_or("No record has that id.")?;
        self.entries.remove(position);
        Ok(())
    }

    fn search(&self, text: &str) -> Vec<&Entry> {
        let needle = text.trim().to_lowercase();
        self.entries
            .iter()
            .filter(|entry| entry.title.to_lowercase().contains(&needle) || entry.description.to_lowercase().contains(&needle))
            .collect()
    }
}

fn fake_clock() -> Box<dyn FnMut() -> String> {
    let mut ticks = 0;
    Box::new(move || {
        ticks += 1;
        format!("2026-01-15T10:00:{ticks:02}")
    })
}

fn expect(condition: bool, message: &str) -> Result<(), String> {
    if condition {
        Ok(())
    } else {
        Err(message.to_string())
    }
}

fn fresh() -> Manager {
    let mut manager = Manager::new(fake_clock());
    manager.add("Notebook", "Course notes", "supplies").unwrap();
    manager.add("Pencil", "Box of 10", "supplies").unwrap();
    manager.add("Study plan", "Weekly schedule", "planning").unwrap();
    manager
}

fn empty_title_is_rejected() -> Result<(), String> {
    let mut manager = fresh();
    expect(manager.add("   ", "x", "supplies") == Err("A title is required.".to_string()), "expected the title message")?;
    expect(manager.entries.len() == 3, "the list should be unchanged")
}

fn new_record_gets_an_unused_id() -> Result<(), String> {
    let mut manager = fresh();
    manager.delete(2)?;
    let id = manager.add("Ruler", "30 cm", "supplies")?;
    expect(id == 4, "expected id 4")
}

fn update_changes_updated_at_but_not_created_at() -> Result<(), String> {
    let mut manager = fresh();
    let (created, updated) = {
        let entry = manager.find(1).ok_or("record 1 missing")?;
        (entry.created_at.clone(), entry.updated_at.clone())
    };
    manager.update(1, Changes { description: Some("Lecture notes".to_string()), ..Default::default() })?;
    let entry = manager.find(1).ok_or("record 1 missing")?;
    expect(entry.created_at == created, "created_at changed")?;
    expect(entry.updated_at != updated, "updated_at did not change")
}

fn delete_removes_only_that_record() -> Result<(), String> {
    let mut manager = fresh();
    manager.delete(2)?;
    let ids: Vec<i32> = manager.entries.iter().map(|entry| entry.id).collect();
    expect(ids == vec![1, 3], "wrong records remain")
}

fn complete_marks_done_and_updates_the_record() -> Result<(), String> {
    let mut manager = fresh();
    manager.complete(3)?;
    let entry = manager.find(3).ok_or("record 3 missing")?;
    expect(entry.done && entry.updated_at != entry.created_at, "completion not recorded")
}

fn blank_title_cannot_be_saved_by_update() -> Result<(), String> {
    let mut manager = fresh();
    let result = manager.update(1, Changes { title: Some(String::new()), ..Default::default() });
    expect(result == Err("A title is required.".to_string()), "update accepted a blank title")
}

fn main() {
    let tests: [(&str, fn() -> Result<(), String>); 6] = [
        ("1. an empty title is rejected", empty_title_is_rejected),
        ("2. a new record gets an unused id", new_record_gets_an_unused_id),
        ("3. update changes updated_at but not created_at", update_changes_updated_at_but_not_created_at),
        ("4. delete removes only that record", delete_removes_only_that_record),
        ("5. complete marks done and updates the record", complete_marks_done_and_updates_the_record),
        ("6. a blank title cannot be saved by update", blank_title_cannot_be_saved_by_update),
    ];

    let mut failures = 0;
    for (name, test) in tests {
        match test() {
            Ok(()) => println!("PASS {name}"),
            Err(message) => {
                failures += 1;
                println!("FAIL {name}: {message}");
            }
        }
    }
    if failures == 0 {
        println!("All acceptance tests passed.");
    } else {
        println!("{failures} test(s) failed.");
    }
}
```

### Expected Behavior or Output

The program prints:
```text
PASS 1. an empty title is rejected
PASS 2. a new record gets an unused id
PASS 3. update changes updated_at but not created_at
PASS 4. delete removes only that record
PASS 5. complete marks done and updates the record
PASS 6. a blank title cannot be saved by update
All acceptance tests passed.
```

### Common Mistakes
1. Sharing one manager between tests, so one test's deletions change the next test.
2. Checking only that no error occurred, and not checking the result.
3. Writing the expected message differently from the program, so a correct program fails the test.

### Activities
1. Break `Manager::update` so it also changes `created_at` and watch test 3 fail. Restore it.
2. Add a test that searching ignores case.
3. Add a test that deleting an unknown id returns a message.
4. Explain why test 2 deletes record 2 before adding the new one.

### Accessibility Practice

The test names begin with the acceptance-test number, so PASS and FAIL lines can be matched to the specification. Read only the first word of each line to hear the overall result quickly.

### Skills Checklist
- [ ] I can run the shared acceptance tests.
- [ ] I can test validation failures.
- [ ] I can test timestamps with a fake clock.
- [ ] I can read PASS and FAIL lines.
- [ ] I use a fresh manager for every test.

---

## Lesson 11.5: Documentation and presentation

### Reading References
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- [Unit P, Lesson P.6](../FOUNDATIONS/unit-p-computing-foundations.md): files, data formats, and the shared accessible workflow
- Matching Python lesson: Lesson 11.5: Final Submission

### Learning Objectives
- Write a plain-text project summary.
- Report a count of records by category.
- Complete a manual accessibility check.

### Concept Explanation

Documentation tells a future reader what the program does and how to run it. Write it as plain text or Markdown with short headings, numbered steps, and complete sentences. Include: the purpose of the program, the `cargo` commands to build and run it, the shared record fields, the commands a user can give, the accessibility checks you carried out, and what you would improve next.

The example generates a summary from the shared sample data. It counts records by category in a `BTreeMap`, which keeps its keys sorted, so the output is stable. It then prints the manual accessibility checklist. The unchecked boxes `[ ]` are for *you* to complete by hand with your own access technology; the program cannot verify them.

Acceptance test 6 is a manual check: every message and control can be used without color or a mouse. Test it with the keyboard only, and with the screen reader or braille display you actually use. Record what you tested and its version; do not claim compatibility with software you did not test.

### Worked Example

```rust
use std::collections::BTreeMap;

struct Entry {
    id: i32,
    title: String,
    category: String,
}

fn main() {
    let sample = vec![
        Entry { id: 1, title: "Notebook".to_string(), category: "supplies".to_string() },
        Entry { id: 2, title: "Pencil".to_string(), category: "supplies".to_string() },
        Entry { id: 3, title: "Study plan".to_string(), category: "planning".to_string() },
    ];

    let mut counts: BTreeMap<&str, u32> = BTreeMap::new();
    for entry in &sample {
        *counts.entry(entry.category.as_str()).or_insert(0) += 1;
    }

    println!("Personal Data Manager - Summary");
    println!("Records: {}", sample.len());
    println!("Categories:");
    for (category, count) in &counts {
        println!("- {category}: {count}");
    }
    let titles: Vec<String> = sample.iter().map(|entry| format!("{} ({})", entry.title, entry.id)).collect();
    println!("Titles: {}", titles.join(", "));

    println!();
    println!("Manual accessibility checklist (complete this by hand):");
    let checks = [
        "[ ] Every command can be used with the keyboard only.",
        "[ ] Every message is a complete sentence that says what to do next.",
        "[ ] No meaning depends on color, position, or symbols alone.",
        "[ ] The output was read with my own screen reader or braille display.",
        "[ ] I recorded the operating system, program, and version I tested.",
    ];
    for check in checks {
        println!("{check}");
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Personal Data Manager - Summary
Records: 3
Categories:
- planning: 1
- supplies: 2
Titles: Notebook (1), Pencil (2), Study plan (3)

Manual accessibility checklist (complete this by hand):
[ ] Every command can be used with the keyboard only.
[ ] Every message is a complete sentence that says what to do next.
[ ] No meaning depends on color, position, or symbols alone.
[ ] The output was read with my own screen reader or braille display.
[ ] I recorded the operating system, program, and version I tested.
```

### Common Mistakes
1. Writing documentation that only the author can follow.
2. Claiming that a program is accessible without recording what was tested and how.
3. Letting the documentation drift from the program after later changes.

### Activities
1. Write the project summary for your own capstone using the headings above.
2. Run the keyboard-only check and record each problem you find.
3. Ask a classmate to follow your run instructions from a fresh folder and note where they get stuck.
4. Write three improvements for the next version, ordered by user benefit.

### Accessibility Practice

This is the final accessibility lesson. Read your own documentation aloud from start to finish. Anything you have to look at the screen to understand needs rewriting.

### Skills Checklist
- [ ] I can write a plain-text project summary.
- [ ] I can report counts by category.
- [ ] I can run a manual accessibility check.
- [ ] I record what I tested.
- [ ] I do not claim untested compatibility.

---

## Course-Wide Assessment and Portfolio

Submit a Cargo project that compiles with the Rust 2024 edition, passes cargo fmt --check, cargo check, and cargo test, and documents its data model, input validation, error handling, persistence format, and keyboard/screen-reader workflow. Include a README with exact build, test, and run commands.

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.

## Rust-Specific Verification Notes

The JSON example demonstrates the serialized record shape only; production code should use serde_json. The deterministic pseudo-random example is not cryptographically secure and is not a substitute for a maintained random-number generator.