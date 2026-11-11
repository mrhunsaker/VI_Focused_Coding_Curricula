# Unit 8: Files and Error Handling

## Overview
This unit develops files and error handling through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 8.1: Reading text files

### Reading References
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Reading text files using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
File APIs return Result. The ? operator propagates compatible failures. RAII releases resources when owners leave scope. Use a maintained parser/serializer such as serde_json for production JSON; the standard-library-only example illustrates the serialized record shape. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
use std::fs; fn main(){let p=std::env::temp_dir().join("rust_read_demo.txt");fs::write(&p,"Avery,82\\n").unwrap();let s=fs::read_to_string(&p).unwrap();print!("{s}");let _=fs::remove_file(p);}
```

**Expected behavior:** Demonstrates a scoped file operation in the system temporary directory and removes its demonstration file.

### Common Mistakes
1. Using unwrap on production I/O paths instead of handling or propagating errors.
2. Assuming file handles require manual close; RAII drops them at scope exit.
3. Hand-building JSON without correct escaping; use serde_json in real projects.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical inventory and CSV records and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (reading text files); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain reading text files using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 8.2: Writing and appending files

### Reading References
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Writing and appending files using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
File APIs return Result. The ? operator propagates compatible failures. RAII releases resources when owners leave scope. Use a maintained parser/serializer such as serde_json for production JSON; the standard-library-only example illustrates the serialized record shape. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
use std::fs::OpenOptions;use std::io::Write;fn main(){let p=std::env::temp_dir().join("rust_append_demo.txt");{let mut f=OpenOptions::new().create(true).append(true).open(&p).unwrap();writeln!(f,"Notebook,3").unwrap();}println!("appended inventory record");let _=std::fs::remove_file(p);}
```

**Expected behavior:** Demonstrates a scoped file operation in the system temporary directory and removes its demonstration file.

### Common Mistakes
1. Using unwrap on production I/O paths instead of handling or propagating errors.
2. Assuming file handles require manual close; RAII drops them at scope exit.
3. Hand-building JSON without correct escaping; use serde_json in real projects.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical inventory and CSV records and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (writing and appending files); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain writing and appending files using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

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
