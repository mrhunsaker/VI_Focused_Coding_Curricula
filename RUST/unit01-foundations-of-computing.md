# Unit 1: Foundations of Computing

## Overview
This unit develops foundations of computing through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 1.1: Computer science and problem solving

### Reading References
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

## Lesson 1.2: Your first program and sequential execution

### Reading References
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
