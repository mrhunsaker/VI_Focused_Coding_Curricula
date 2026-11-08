# Unit 1: Foundations of Computing

## Overview
This unit develops foundations of computing through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 1.1: Computer science and problem solving

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Computer science and problem solving using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Rust is compiled and statically typed. Bindings are immutable by default. Ownership determines which binding is responsible for a value; borrowing provides temporary access without transferring ownership. Compiler diagnostics are part of the design feedback loop. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { println!("A program is a precise set of instructions."); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Changing a binding declared with let instead of declaring it mutable.
2. Assuming every value is copied; String moves unless borrowed or cloned.
3. Treating a type annotation as a runtime conversion.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical Avery profile, calculator bill, or grade thresholds and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (computer science and problem solving); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain computer science and problem solving using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 1.2: Your first program and sequential execution

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Your first program and sequential execution using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Rust is compiled and statically typed. Bindings are immutable by default. Ownership determines which binding is responsible for a value; borrowing provides temporary access without transferring ownership. Compiler diagnostics are part of the design feedback loop. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let name = "Avery"; println!("Hello, {name}!"); println!("This line runs second."); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Changing a binding declared with let instead of declaring it mutable.
2. Assuming every value is copied; String moves unless borrowed or cloned.
3. Treating a type annotation as a runtime conversion.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical Avery profile, calculator bill, or grade thresholds and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (your first program and sequential execution); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain your first program and sequential execution using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 1.3: Variables, bindings, mutability, and primitive types

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Variables, bindings, mutability, and primitive types using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Rust is compiled and statically typed. Bindings are immutable by default. Ownership determines which binding is responsible for a value; borrowing provides temporary access without transferring ownership. Compiler diagnostics are part of the design feedback loop. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let age: u8 = 16; let height_m = 1.72_f64; let active = true; println!("age={age}, height={height_m:.2}, active={active}"); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Changing a binding declared with let instead of declaring it mutable.
2. Assuming every value is copied; String moves unless borrowed or cloned.
3. Treating a type annotation as a runtime conversion.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical Avery profile, calculator bill, or grade thresholds and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (variables, bindings, mutability, and primitive types); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain variables, bindings, mutability, and primitive types using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)
