# Unit 2: Numeric Computations

## Overview
This unit develops numeric computations through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 2.1: Software design and tracing

### Reading References
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Software design and tracing using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Rust distinguishes integer and floating-point types and does not silently coerce between them. Expressions have values; mutable assignment updates a place. Input is read as text and parsed into a requested type through Result. For real financial systems, use integer minor units or a decimal type rather than binary floating point. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let bill=24.50_f64; let rate=0.15_f64; let tip=bill*rate; println!("Tip: {tip:.2}; total: {:.2}",bill+tip); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Using integer division when a fractional result is required.
2. Ignoring the Result returned by parsing user input.
3. Mixing numeric types without explicit conversions.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical Avery profile, calculator bill, or grade thresholds and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (software design and tracing); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain software design and tracing using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 2.5: Mathematical functions, circle geometry, and distance

### Reading References
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Mathematical functions, circle geometry, and distance using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Rust distinguishes integer and floating-point types and does not silently coerce between them. Expressions have values; mutable assignment updates a place. Input is read as text and parsed into a requested type through Result. For real financial systems, use integer minor units or a decimal type rather than binary floating point. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let d=3.0_f64.hypot(4.0); println!("Distance from origin: {d}"); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Using integer division when a fractional result is required.
2. Ignoring the Result returned by parsing user input.
3. Mixing numeric types without explicit conversions.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical Avery profile, calculator bill, or grade thresholds and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (mathematical functions, circle geometry, and distance); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain mathematical functions, circle geometry, and distance using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 2.2: Expressions, operators, and assignment

### Reading References
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Expressions, operators, and assignment using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Rust distinguishes integer and floating-point types and does not silently coerce between them. Expressions have values; mutable assignment updates a place. Input is read as text and parsed into a requested type through Result. For real financial systems, use integer minor units or a decimal type rather than binary floating point. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let subtotal=24.50_f64; let tax=subtotal*0.075; println!("Subtotal {subtotal:.2}, tax {tax:.2}, total {:.2}",subtotal+tax); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Using integer division when a fractional result is required.
2. Ignoring the Result returned by parsing user input.
3. Mixing numeric types without explicit conversions.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical Avery profile, calculator bill, or grade thresholds and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (expressions, operators, and assignment); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain expressions, operators, and assignment using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

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
