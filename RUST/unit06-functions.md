# Unit 6: Functions

## Overview
This unit develops functions through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 6.1: Defining and calling functions

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Defining and calling functions using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Functions declare parameter and return types. Borrow &T for read-only access and &mut T for exclusive mutation; accept owned values when retaining or transforming ownership. Generics express behavior over multiple types while preserving static checking. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn greet(name:&str) {println!("Hello, {name}!");} fn main() {greet("Avery");}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Returning a reference that outlives its owner.
2. Taking ownership when a shared borrow is sufficient.
3. Adding a semicolon to the final expression that should be returned.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical scores [82, 91, 76, 88] and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (defining and calling functions); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain defining and calling functions using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 6.2: Parameters, ownership, and borrowing

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Parameters, ownership, and borrowing using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Functions declare parameter and return types. Borrow &T for read-only access and &mut T for exclusive mutation; accept owned values when retaining or transforming ownership. Generics express behavior over multiple types while preserving static checking. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn describe(name:&str,score:i32) {println!("{name} scored {score}.");} fn main() {let name=String::from("Avery");describe(&name,82);println!("still owned: {name}");}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Returning a reference that outlives its owner.
2. Taking ownership when a shared borrow is sufficient.
3. Adding a semicolon to the final expression that should be returned.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical scores [82, 91, 76, 88] and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (parameters, ownership, and borrowing); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain parameters, ownership, and borrowing using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 6.3: Return values and expressions

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Return values and expressions using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Functions declare parameter and return types. Borrow &T for read-only access and &mut T for exclusive mutation; accept owned values when retaining or transforming ownership. Generics express behavior over multiple types while preserving static checking. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn grade(s:i32)->&'static str {if s>=60 {"pass"} else {"retry"}} fn main() {println!("{}",grade(82));}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Returning a reference that outlives its owner.
2. Taking ownership when a shared borrow is sufficient.
3. Adding a semicolon to the final expression that should be returned.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical scores [82, 91, 76, 88] and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (return values and expressions); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain return values and expressions using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 6.4: Functions over collections

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Functions over collections using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Functions declare parameter and return types. Borrow &T for read-only access and &mut T for exclusive mutation; accept owned values when retaining or transforming ownership. Generics express behavior over multiple types while preserving static checking. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn average(v:&[i32])->f64 {v.iter().sum::<i32>() as f64/v.len() as f64} fn main() {let s=[82,91,76,88];println!("{:.1}",average(&s));}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Returning a reference that outlives its owner.
2. Taking ownership when a shared borrow is sufficient.
3. Adding a semicolon to the final expression that should be returned.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical scores [82, 91, 76, 88] and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (functions over collections); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain functions over collections using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 6.5: Scope, generics, and variadic alternatives

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Scope, generics, and variadic alternatives using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Functions declare parameter and return types. Borrow &T for read-only access and &mut T for exclusive mutation; accept owned values when retaining or transforming ownership. Generics express behavior over multiple types while preserving static checking. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn first<T>(v:&[T])->Option<&T> {v.first()} fn main() {let names=["Avery","Jordan"];println!("{}",first(&names).unwrap());}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Returning a reference that outlives its owner.
2. Taking ownership when a shared borrow is sufficient.
3. Adding a semicolon to the final expression that should be returned.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical scores [82, 91, 76, 88] and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (scope, generics, and variadic alternatives); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain scope, generics, and variadic alternatives using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)
