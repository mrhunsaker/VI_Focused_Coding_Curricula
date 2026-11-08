# Unit 11: Capstone

## Overview
This unit develops capstone through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 11.1: Requirements and design

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Requirements and design using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is a record manager. Model records, define validation rules, implement create/read/update/delete, persist data safely, and verify behavior with tests. Document build, test, and run workflows and accessibility decisions. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main(){let fields=["id","title","description","category","created_at","updated_at"];println!("Capstone fields: {}",fields.join(", "));}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Updating a record without checking whether its identifier exists.
2. Persisting before validation or overwriting the only copy without recovery.
3. Treating compilation as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical to-do and capstone record fields and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (requirements and design); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain requirements and design using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 11.2: Data model and storage

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Data model and storage using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is a record manager. Model records, define validation rules, implement create/read/update/delete, persist data safely, and verify behavior with tests. Document build, test, and run workflows and accessibility decisions. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
struct Record{id:u32,title:String,description:String,category:String,created_at:String,updated_at:String}fn main(){let r=Record{id:1,title:"Study Rust".into(),description:"Review ownership".into(),category:"learning".into(),created_at:"2026-11-01".into(),updated_at:"2026-11-01".into()};println!("id={}, title={}, description={}, category={}, created_at={}, updated_at={}",r.id,r.title,r.description,r.category,r.created_at,r.updated_at);}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Updating a record without checking whether its identifier exists.
2. Persisting before validation or overwriting the only copy without recovery.
3. Treating compilation as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical to-do and capstone record fields and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (data model and storage); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain data model and storage using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 11.3: Create, read, update, delete

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Create, read, update, delete using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is a record manager. Model records, define validation rules, implement create/read/update/delete, persist data safely, and verify behavior with tests. Document build, test, and run workflows and accessibility decisions. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
#[derive(Debug)]struct Record{id:u32,title:String,done:bool}fn main(){let mut v=vec![Record{id:1,title:"Draft".into(),done:false}];v.push(Record{id:2,title:"Review".into(),done:false});if let Some(r)=v.iter_mut().find(|r|r.id==1){r.done=true;}v.retain(|r|r.id!=99);for r in &v{println!("{} {} done={}",r.id,r.title,r.done);}}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Updating a record without checking whether its identifier exists.
2. Persisting before validation or overwriting the only copy without recovery.
3. Treating compilation as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical to-do and capstone record fields and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (create, read, update, delete); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain create, read, update, delete using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 11.4: Validation and tests

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Validation and tests using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is a record manager. Model records, define validation rules, implement create/read/update/delete, persist data safely, and verify behavior with tests. Document build, test, and run workflows and accessibility decisions. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn valid(s:&str)->bool{!s.trim().is_empty()&&s.len()<=80}fn main(){for s in ["Plan","","A title that is intentionally longer than the allowed boundary because it has more than eighty characters and should be rejected"]{println!("{s:?}: {}",valid(s));}}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Updating a record without checking whether its identifier exists.
2. Persisting before validation or overwriting the only copy without recovery.
3. Treating compilation as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical to-do and capstone record fields and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (validation and tests); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain validation and tests using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 11.5: Documentation and presentation

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Documentation and presentation using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is a record manager. Model records, define validation rules, implement create/read/update/delete, persist data safely, and verify behavior with tests. Document build, test, and run workflows and accessibility decisions. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main(){println!("Project: accessible record manager");println!("Build: cargo build --release");println!("Test: cargo test");println!("Run: cargo run");println!("Document validation, storage, errors, and keyboard workflow.");}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Updating a record without checking whether its identifier exists.
2. Persisting before validation or overwriting the only copy without recovery.
3. Treating compilation as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical to-do and capstone record fields and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (documentation and presentation); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain documentation and presentation using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

## Course-Wide Assessment and Portfolio

Submit a Cargo project that compiles with the Rust 2024 edition, passes cargo fmt --check, cargo check, and cargo test, and documents its data model, input validation, error handling, persistence format, and keyboard/screen-reader workflow. Include a README with exact build, test, and run commands.

## AI Policy

<<<<<<< HEAD
AI tools may explain compiler diagnostics, compare ownership strategies, and suggest tests. Learners must explain every ownership transfer, borrow, trait bound, error path, and dependency. Compile and test generated code, review dependency provenance, and do not expose private data or credentials. AI output is a draft, not evidence of correctness.
=======
AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)

## Rust-Specific Verification Notes

The JSON example demonstrates the serialized record shape only; production code should use serde_json. The deterministic pseudo-random example is not cryptographically secure and is not a substitute for a maintained random-number generator.
