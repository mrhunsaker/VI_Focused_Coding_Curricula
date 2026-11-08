# Unit 4: Data Structures

## Overview
This unit develops data structures through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 4.1: Vectors and collection mutation

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Vectors and collection mutation using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Choose Vec for ordered sequences, tuples for small fixed groupings, and HashMap for keyed lookup. Iterators compose transformations without manual index bookkeeping. Borrow collections when ownership transfer or mutation is unnecessary. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let mut scores=vec![82,91,76]; scores.push(88); println!("{scores:?}"); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Mutating a collection while an incompatible borrow remains active.
2. Assuming HashMap iteration order is sorted or stable.
3. Moving a collection into an iterator and then reusing it.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical scores [82, 91, 76, 88] and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (vectors and collection mutation); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain vectors and collection mutation using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 4.2: Sorting and organizing data

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Sorting and organizing data using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Choose Vec for ordered sequences, tuples for small fixed groupings, and HashMap for keyed lookup. Iterators compose transformations without manual index bookkeeping. Borrow collections when ownership transfer or mutation is unnecessary. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let mut v=vec![82,91,76,88]; v.sort(); println!("ascending={v:?}"); v.reverse(); println!("descending={v:?}"); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Mutating a collection while an incompatible borrow remains active.
2. Assuming HashMap iteration order is sorted or stable.
3. Moving a collection into an iterator and then reusing it.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical scores [82, 91, 76, 88] and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (sorting and organizing data); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain sorting and organizing data using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 4.3: Tuples and immutable values

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Tuples and immutable values using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Choose Vec for ordered sequences, tuples for small fixed groupings, and HashMap for keyed lookup. Iterators compose transformations without manual index bookkeeping. Borrow collections when ownership transfer or mutation is unnecessary. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let student=("Avery",16,82); println!("name={}, age={}, score={}",student.0,student.1,student.2); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Mutating a collection while an incompatible borrow remains active.
2. Assuming HashMap iteration order is sorted or stable.
3. Moving a collection into an iterator and then reusing it.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical scores [82, 91, 76, 88] and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (tuples and immutable values); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain tuples and immutable values using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 4.4: Hash maps and key-value data

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Hash maps and key-value data using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Choose Vec for ordered sequences, tuples for small fixed groupings, and HashMap for keyed lookup. Iterators compose transformations without manual index bookkeeping. Borrow collections when ownership transfer or mutation is unnecessary. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
use std::collections::HashMap; fn main() { let mut stock=HashMap::new(); stock.insert("Notebook",3); stock.insert("Pencil",10); println!("Notebook stock={}",stock.get("Notebook").copied().unwrap_or(0)); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Mutating a collection while an incompatible borrow remains active.
2. Assuming HashMap iteration order is sorted or stable.
3. Moving a collection into an iterator and then reusing it.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical scores [82, 91, 76, 88] and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (hash maps and key-value data); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain hash maps and key-value data using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 4.5: Collection traversal and iterators

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Collection traversal and iterators using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Choose Vec for ordered sequences, tuples for small fixed groupings, and HashMap for keyed lookup. Iterators compose transformations without manual index bookkeeping. Borrow collections when ownership transfer or mutation is unnecessary. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main() { let scores=[82,91,76,88]; let passing:Vec<i32>=scores.into_iter().filter(|s|*s>=80).collect(); println!("{passing:?}"); }
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Mutating a collection while an incompatible borrow remains active.
2. Assuming HashMap iteration order is sorted or stable.
3. Moving a collection into an iterator and then reusing it.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical scores [82, 91, 76, 88] and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (collection traversal and iterators); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain collection traversal and iterators using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)
