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
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Continue and filtering using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Read input into String, trim it, then parse. loop, while, and iterator loops express different repetition patterns. Every loop needs a clear termination condition; break and continue should make control flow easier to reason about. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let values=[-2,3,0,7,-1,9]; let mut positives=Vec::new(); for v in values {if v<=0 {continue;} positives.push(v);} println!("{positives:?}"); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Failing to trim the newline before parsing input.
2. Choosing a sentinel that is also valid data without documenting it.
3. Creating a loop whose state is not updated on every path.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical scores [82, 91, 76, 88] and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (continue and filtering); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain continue and filtering using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

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
