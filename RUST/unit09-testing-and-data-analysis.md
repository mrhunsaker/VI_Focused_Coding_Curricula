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
