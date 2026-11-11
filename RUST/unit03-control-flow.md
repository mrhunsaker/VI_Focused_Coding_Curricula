# Unit 3: Control Flow

## Overview
This unit develops control flow through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 3.1: Boolean expressions and if expressions

### Reading References
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Boolean expressions and if expressions using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Conditions are expressions and branches must have compatible types. Arrays have fixed length; vectors grow dynamically. Prefer iteration or checked get access over unchecked indexing. String owns UTF-8 bytes and &str borrows a slice; use chars when counting Unicode scalar values. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let score=82; println!("score={score}; passing={}",score>=60); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Using an out-of-range index instead of checked access with get.
2. Returning incompatible types from if branches.
3. Confusing UTF-8 byte length with Unicode character count.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical Avery profile, calculator bill, or grade thresholds and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (boolean expressions and if expressions); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain boolean expressions and if expressions using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 3.2: Chained conditionals and grade classification

### Reading References
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Chained conditionals and grade classification using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Conditions are expressions and branches must have compatible types. Arrays have fixed length; vectors grow dynamically. Prefer iteration or checked get access over unchecked indexing. String owns UTF-8 bytes and &str borrows a slice; use chars when counting Unicode scalar values. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { for s in [82,91,76,88,59] { let g=if s>=90 {"A"} else if s>=80 {"B"} else if s>=70 {"C"} else if s>=60 {"D"} else {"F"}; println!("{s}: {g}"); } }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Using an out-of-range index instead of checked access with get.
2. Returning incompatible types from if branches.
3. Confusing UTF-8 byte length with Unicode character count.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical Avery profile, calculator bill, or grade thresholds and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (chained conditionals and grade classification); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain chained conditionals and grade classification using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 3.3: Arrays, vectors, and indexing

### Reading References
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Arrays, vectors, and indexing using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Conditions are expressions and branches must have compatible types. Arrays have fixed length; vectors grow dynamically. Prefer iteration or checked get access over unchecked indexing. String owns UTF-8 bytes and &str borrows a slice; use chars when counting Unicode scalar values. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let scores=[82,91,76,88]; println!("first={}, last={}, count={}",scores[0],scores[3],scores.len()); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Using an out-of-range index instead of checked access with get.
2. Returning incompatible types from if branches.
3. Confusing UTF-8 byte length with Unicode character count.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical Avery profile, calculator bill, or grade thresholds and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (arrays, vectors, and indexing); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain arrays, vectors, and indexing using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

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
