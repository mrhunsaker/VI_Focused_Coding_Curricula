[Header 2 ("unit-11-capstone", [], []) [Str "Unit 11: Capstone"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops capstone through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly."], Header 3 ("lesson-111-requirements-and-design", ["unnumbered", "unlisted"], []) [Str "Lesson 11.1: Requirements and design"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Structs"] ("https://doc.rust-lang.org/book/ch05-01-defining-structs.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Result"] ("https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 11.1: Introduction to NiceGUI"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write requirements for a personal data manager."]], [Plain [Str "Define the shared record schema as a struct."]], [Plain [Str "Check records against the validation rules before building features."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The capstone is a ", Emph [Str "personal data manager"], Str ": a program that keeps a list of records, lets the user add, view, search, change, complete, and delete them, and saves them to a file. In the Rust track it is a text program, so it runs from the terminal and is fully usable with a screen reader or braille display."], Para [Strong [Str "Shared record schema (all general-purpose language tracks)."], Str " Every record has ", Code ("", [], []) "id", Str " (unique whole number), ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "category", Str ", ", Code ("", [], []) "created_at", Str ", and ", Code ("", [], []) "updated_at", Str " (ISO 8601 text). A project may add fields, such as an optional ", Code ("", [], []) "done", Str " flag, but must not remove these. Rust field names use ", Code ("", [], []) "snake_case", Str ", the same as the stored JSON."], Para [Strong [Str "Validation rules."], Str " A record must have a non-empty title and a non-empty category. Timestamps are ISO 8601 text such as ", Code ("", [], []) "2026-01-15T09:00:00", Str ". A ", Code ("", [], []) "Result<(), String>", Str " return type states in the signature that validation can fail with a message."], Para [Str "Design before coding: list the operations, then the data, then the messages. The example checks the three shared sample records against the rules and prints them as a plain-text list."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "struct Entry {
    id: i32,
    title: String,
    description: String,
    category: String,
    created_at: String,
    updated_at: String,
}

fn validate(title: &str, category: &str) -> Result<(), String> {
    if title.trim().is_empty() {
        return Err(\"A title is required.\".to_string());
    }
    if category.trim().is_empty() {
        return Err(\"A category is required.\".to_string());
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
        entry(1, \"Notebook\", \"Course notes\", \"supplies\", \"2026-01-15T09:00:00\"),
        entry(2, \"Pencil\", \"Box of 10\", \"supplies\", \"2026-01-15T09:05:00\"),
        entry(3, \"Study plan\", \"Weekly schedule\", \"planning\", \"2026-01-15T09:10:00\"),
    ];

    for record in &sample {
        let outcome = match validate(&record.title, &record.category) {
            Ok(()) => \"valid\".to_string(),
            Err(message) => message,
        };
        println!(\"{}. {} [{}] - {}\", record.id, record.title, record.category, outcome);
    }
    println!(\"{} | {} | {}\", sample[0].description, sample[0].created_at, sample[0].updated_at);

    println!(\"{:?}\", validate(\"  \", \"supplies\"));
    println!(\"{:?}\", validate(\"Ruler\", \"\"));
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "1. Notebook [supplies] - valid
2. Pencil [supplies] - valid
3. Study plan [planning] - valid
Course notes | 2026-01-15T09:00:00 | 2026-01-15T09:00:00
Err(\"A title is required.\")
Err(\"A category is required.\")
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Starting to build features before agreeing on the record fields."]], [Plain [Str "Allowing a record with an empty title because the check was left for later."]], [Plain [Str "Storing timestamps in different formats in different places."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write the seven operations as a numbered list of requirements."]], [Plain [Str "Add one project-specific field and say how it is validated."]], [Plain [Str "Write three sample records for your own project."]], [Plain [Str "Describe in plain sentences what each shared field means."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Design the screen output as lines of plain text: one record per line, with the same field order each time. Decide the wording of every message now so that it can be tested."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write requirements."]], [Plain [Str "\9744", Space, Str "I know the shared record fields."]], [Plain [Str "\9744", Space, Str "I can write validation rules."]], [Plain [Str "\9744", Space, Str "I can describe sample data."]], [Plain [Str "\9744", Space, Str "I can plan messages before coding."]]], HorizontalRule, Header 3 ("lesson-112-data-model-and-storage", ["unnumbered", "unlisted"], []) [Str "Lesson 11.2: Data model and storage"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Result"] ("https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Reading a File"] ("https://doc.rust-lang.org/book/ch12-02-reading-a-file.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 11.2: Data Model and Storage"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Store records as structs."]], [Plain [Str "Save and load them as JSON."]], [Plain [Str "Confirm that every field survives a round trip."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Records are stored as a ", Code ("", [], []) "Vec<Entry>", Str " in memory and as a JSON array on disk. The storage layer has two functions: ", Code ("", [], []) "save_entries(path, entries)", Str " and ", Code ("", [], []) "load_entries(path)", Str ", which returns ", Code ("", [], []) "Result<Vec<Entry>, String>", Str " so the caller decides what to do when the file is missing or damaged."], Para [Str "An ", Code ("", [], []) "Entry", Str " is converted to a ", Code ("", [], []) "Json::Object", Str " for saving (", Code ("", [], []) "to_json", Str ") and rebuilt from one when loading (", Code ("", [], []) "from_json", Str "), which checks that each field is present and has the right type. The optional ", Code ("", [], []) "done", Str " field defaults to ", Code ("", [], []) "false", Str "."], Para [Str "The example uses the teaching JSON helper from Lesson 8.5 (included so the program runs on its own). After saving and reloading it compares the lists; deriving ", Code ("", [], []) "PartialEq", Str " lets Rust compare structs field by field, so this ", Emph [Str "round-trip test"], Str " checks every field of every entry. It is the first acceptance test for storage."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "#![allow(dead_code)]
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
    let mut out = String::from(\"\\\"\");
    for c in text.chars() {
        match c {
            '\"' => out.push_str(\"\\\\\\\"\"),
            '\\\\' => out.push_str(\"\\\\\\\\\"),
            '\\n' => out.push_str(\"\\\\n\"),
            '\\r' => out.push_str(\"\\\\r\"),
            '\\t' => out.push_str(\"\\\\t\"),
            c if (c as u32) < 0x20 => out.push_str(&format!(\"\\\\u{:04x}\", c as u32)),
            c => out.push(c),
        }
    }
    out.push('\"');
    out
}

fn encode(value: &Json) -> String {
    match value {
        Json::Null => \"null\".to_string(),
        Json::Bool(flag) => flag.to_string(),
        Json::Int(number) => number.to_string(),
        Json::Float(number) => number.to_string(),
        Json::Str(text) => quote(text),
        Json::List(items) => {
            let parts: Vec<String> = items.iter().map(encode).collect();
            format!(\"[{}]\", parts.join(\",\"))
        }
        Json::Object(map) => {
            let parts: Vec<String> = map.iter().map(|(key, item)| format!(\"{}:{}\", quote(key), encode(item))).collect();
            format!(\"{{{}}}\", parts.join(\",\"))
        }
    }
}

struct Parser {
    chars: Vec<char>,
    pos: usize,
}

impl Parser {
    fn fail<T>(&self, message: &str) -> Result<T, String> {
        Err(format!(\"{message} at position {}\", self.pos))
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
            None => self.fail(\"unexpected end of text\"),
            Some('{') => self.object(),
            Some('[') => self.list(),
            Some('\"') => Ok(Json::Str(self.string()?)),
            Some(c) if c == '-' || c.is_ascii_digit() => self.number(),
            Some(_) if self.starts_with(\"true\") => {
                self.pos += 4;
                Ok(Json::Bool(true))
            }
            Some(_) if self.starts_with(\"false\") => {
                self.pos += 5;
                Ok(Json::Bool(false))
            }
            Some(_) if self.starts_with(\"null\") => {
                self.pos += 4;
                Ok(Json::Null)
            }
            Some(_) => self.fail(\"unexpected character\"),
        }
    }

    fn number(&mut self) -> Result<Json, String> {
        let start = self.pos;
        if self.peek() == Some('-') {
            self.pos += 1;
        }
        while let Some(c) = self.peek() {
            if c.is_ascii_digit() || \".eE+-\".contains(c) {
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
            Err(_) => self.fail(\"bad number\"),
        }
    }

    fn string(&mut self) -> Result<String, String> {
        self.pos += 1;
        let mut out = String::new();
        loop {
            let Some(c) = self.peek() else {
                return self.fail(\"unterminated string\");
            };
            self.pos += 1;
            match c {
                '\"' => return Ok(out),
                '\\\\' => {
                    let Some(escape) = self.peek() else {
                        return self.fail(\"bad escape\");
                    };
                    self.pos += 1;
                    match escape {
                        'n' => out.push('\\n'),
                        't' => out.push('\\t'),
                        'r' => out.push('\\r'),
                        '\"' => out.push('\"'),
                        '\\\\' => out.push('\\\\'),
                        '/' => out.push('/'),
                        'u' => {
                            if self.pos + 4 > self.chars.len() {
                                return self.fail(\"bad escape\");
                            }
                            let hex: String = self.chars[self.pos..self.pos + 4].iter().collect();
                            let code = u32::from_str_radix(&hex, 16).map_err(|_| \"bad escape\".to_string())?;
                            out.push(char::from_u32(code).unwrap_or('?'));
                            self.pos += 4;
                        }
                        _ => return self.fail(\"bad escape\"),
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
            if self.peek() != Some('\"') {
                return self.fail(\"expected a key\");
            }
            let key = self.string()?;
            self.skip();
            if self.peek() != Some(':') {
                return self.fail(\"expected ':'\");
            }
            self.pos += 1;
            let item = self.value()?;
            map.insert(key, item);
            self.skip();
            match self.peek() {
                None => return self.fail(\"unterminated object\"),
                Some('}') => {
                    self.pos += 1;
                    return Ok(Json::Object(map));
                }
                Some(',') => self.pos += 1,
                Some(_) => return self.fail(\"expected ',' or '}'\"),
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
                None => return self.fail(\"unterminated list\"),
                Some(']') => {
                    self.pos += 1;
                    return Ok(Json::List(items));
                }
                Some(',') => self.pos += 1,
                Some(_) => return self.fail(\"expected ',' or ']'\"),
            }
        }
    }
}

fn decode(text: &str) -> Result<Json, String> {
    let mut parser = Parser { chars: text.chars().collect(), pos: 0 };
    let value = parser.value()?;
    parser.skip();
    if parser.pos < parser.chars.len() {
        return parser.fail(\"unexpected extra text\");
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
    map.insert(\"id\".to_string(), Json::Int(entry.id));
    map.insert(\"title\".to_string(), Json::Str(entry.title.clone()));
    map.insert(\"description\".to_string(), Json::Str(entry.description.clone()));
    map.insert(\"category\".to_string(), Json::Str(entry.category.clone()));
    map.insert(\"created_at\".to_string(), Json::Str(entry.created_at.clone()));
    map.insert(\"updated_at\".to_string(), Json::Str(entry.updated_at.clone()));
    map.insert(\"done\".to_string(), Json::Bool(entry.done));
    Json::Object(map)
}

fn text_field(map: &BTreeMap<String, Json>, key: &str) -> Result<String, String> {
    match map.get(key) {
        Some(Json::Str(text)) => Ok(text.clone()),
        _ => Err(format!(\"missing field {key}\")),
    }
}

fn from_json(value: &Json) -> Result<Entry, String> {
    let Json::Object(map) = value else {
        return Err(\"a record must be an object\".to_string());
    };
    let id = match map.get(\"id\") {
        Some(Json::Int(number)) => *number,
        _ => return Err(\"missing field id\".to_string()),
    };
    Ok(Entry {
        id,
        title: text_field(map, \"title\")?,
        description: text_field(map, \"description\")?,
        category: text_field(map, \"category\")?,
        created_at: text_field(map, \"created_at\")?,
        updated_at: text_field(map, \"updated_at\")?,
        done: map.get(\"done\") == Some(&Json::Bool(true)),
    })
}

fn save_entries(path: &str, entries: &[Entry]) -> Result<(), String> {
    let list = Json::List(entries.iter().map(to_json).collect());
    fs::write(path, encode(&list)).map_err(|_| format!(\"Could not write {path}.\"))
}

fn load_entries(path: &str) -> Result<Vec<Entry>, String> {
    let text = fs::read_to_string(path).map_err(|_| format!(\"Could not open {path}: file not found.\"))?;
    match decode(&text) {
        Ok(Json::List(items)) => items.iter().map(from_json).collect::<Result<Vec<Entry>, String>>().map_err(|e| format!(\"The data file is not valid: {e}\")),
        Ok(_) => Err(\"The data file is not valid: expected a list\".to_string()),
        Err(message) => Err(format!(\"The data file is not valid: {message}\")),
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
        entry(1, \"Notebook\", \"Course notes\", \"supplies\", \"2026-01-15T09:00:00\"),
        entry(2, \"Pencil\", \"Box of 10\", \"supplies\", \"2026-01-15T09:05:00\"),
        entry(3, \"Study plan\", \"Weekly schedule\", \"planning\", \"2026-01-15T09:10:00\"),
    ];

    println!(\"{:?}\", save_entries(\"records.json\", &sample));
    match load_entries(\"records.json\") {
        Ok(loaded) => {
            println!(\"Round trip preserved all fields: {}\", loaded == sample);
            println!(\"Records loaded: {}\", loaded.len());
        }
        Err(message) => println!(\"{message}\"),
    }

    if let Err(message) = load_entries(\"missing.json\") {
        println!(\"{message}\");
    }

    fs::write(\"broken.json\", \"[{\\\"id\\\": 1,\").expect(\"could not write the broken file\");
    if let Err(message) = load_entries(\"broken.json\") {
        println!(\"{message}\");
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Ok(())
Round trip preserved all fields: true
Records loaded: 3
Could not open missing.json: file not found.
The data file is not valid: expected a key at position 10
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Overwriting the data file with an empty list after a failed load."]], [Plain [Str "Saving only some of the fields."]], [Plain [Str "Assuming a loaded record has every field without checking."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program and open ", Code ("", [], []) "records.json", Str " to read the saved text."]], [Plain [Str "Add a field to ", Code ("", [], []) "Entry", Str ", save it, and confirm that it survives the round trip."]], [Plain [Str "Make ", Code ("", [], []) "from_json", Str " reject a record whose title is blank."]], [Plain [Str "Explain why ", Code ("", [], []) "load_entries", Str " returns a ", Code ("", [], []) "Result", Str " and does not panic."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Messages that name the file and the problem read clearly in speech. After saving, read the file in the terminal to confirm it contains what you expect."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can store records in structs."]], [Plain [Str "\9744", Space, Str "I can save and load JSON."]], [Plain [Str "\9744", Space, Str "I can run a round-trip test."]], [Plain [Str "\9744", Space, Str "I handle missing and damaged files."]], [Plain [Str "\9744", Space, Str "I do not overwrite good data after a failed load."]]], HorizontalRule, Header 3 ("lesson-113-create-read-update-delete", ["unnumbered", "unlisted"], []) [Str "Lesson 11.3: Create, read, update, delete"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Method Syntax"] ("https://doc.rust-lang.org/book/ch05-03-method-syntax.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Result"] ("https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 11.3: Displaying and Managing Items"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Add, list, search, change, complete, and delete records."]], [Plain [Str "Assign new ids and update timestamps correctly."]], [Plain [Str "Return a ", Code ("", [], []) "Result", Str " with a message when an operation cannot be done."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Code ("", [], []) "Manager", Str " struct owns the entries and offers one method per operation. Each method that can fail returns a ", Code ("", [], []) "Result<_, String>", Str " whose ", Code ("", [], []) "Err", Str " holds the message to show. New ids are one more than the highest id, so ids are never reused while higher ids exist. Updating an entry sets ", Code ("", [], []) "updated_at", Str " but never changes ", Code ("", [], []) "created_at", Str ". A ", Code ("", [], []) "Changes", Str " struct with ", Code ("", [], []) "Option", Str " fields says which fields to change, so ", Code ("", [], []) "Changes { done: Some(true), ..Default::default() }", Str " changes only ", Code ("", [], []) "done", Str ". Completing an entry counts as an update."], Para [Str "For repeatable output the example passes in a ", Emph [Str "fake clock"], Str ": a boxed closure that returns a new fixed time on each call. A real program passes a closure that reads the real time."], Para [Str "The example adds the three shared sample records, lists them, searches for \"note\", changes one description, completes one entry, deletes one, and tries to delete an entry that does not exist."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "#![allow(dead_code)]
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
        format!(\"{}. {} [{}] ({})\", self.id, self.title, self.category, if self.done { \"done\" } else { \"not done\" })
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
        return Err(\"A title is required.\".to_string());
    }
    if category.trim().is_empty() {
        return Err(\"A category is required.\".to_string());
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
            None => return Err(\"No record has that id.\".to_string()),
        };
        validate(&title, &category)?;
        let stamp = (self.clock)();
        let entry = self.entries.iter_mut().find(|entry| entry.id == id).ok_or(\"No record has that id.\")?;
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
        let position = self.entries.iter().position(|entry| entry.id == id).ok_or(\"No record has that id.\")?;
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
        format!(\"2026-01-15T10:00:{ticks:02}\")
    })
}

fn show(manager: &Manager) {
    for entry in &manager.entries {
        println!(\"{}\", entry.describe());
    }
}

fn main() {
    let mut manager = Manager::new(fake_clock());
    manager.add(\"Notebook\", \"Course notes\", \"supplies\").unwrap();
    manager.add(\"Pencil\", \"Box of 10\", \"supplies\").unwrap();
    manager.add(\"Study plan\", \"Weekly schedule\", \"planning\").unwrap();
    show(&manager);

    println!(\"Search for 'note':\");
    for entry in manager.search(\"note\") {
        println!(\"{}\", entry.title);
    }

    manager.update(2, Changes { description: Some(\"Box of 12\".to_string()), ..Default::default() }).unwrap();
    manager.complete(3).unwrap();
    if let Some(entry) = manager.find(2) {
        println!(\"{} {} {}\", entry.description, entry.created_at, entry.updated_at);
    }

    println!(\"{:?}\", manager.delete(1));
    println!(\"{:?}\", manager.delete(99));
    show(&manager);
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "1. Notebook [supplies] (not done)
2. Pencil [supplies] (not done)
3. Study plan [planning] (not done)
Search for 'note':
Notebook
Box of 12 2026-01-15T10:00:02 2026-01-15T10:00:04
Ok(())
Err(\"No record has that id.\")
2. Pencil [supplies] (not done)
3. Study plan [planning] (done)
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Reusing a deleted entry's id by counting the vector length instead of using the highest id."]], [Plain [Str "Changing ", Code ("", [], []) "created_at", Str " when updating a record."]], [Plain [Str "Calling ", Code ("", [], []) "unwrap()", Str " on every ", Code ("", [], []) "Result", Str " in a real program instead of showing the message to the user."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output before running."]], [Plain [Str "Add ", Code ("", [], []) "list_by_category(category)", Str " to ", Code ("", [], []) "Manager", Str "."]], [Plain [Str "Add a rule that blocks completing an entry that is already complete, with a message."]], [Plain [Str "Explain how the fake clock makes the output repeatable."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "List output uses the same fixed format for every record and the words ", Code ("", [], []) "done", Str " and ", Code ("", [], []) "not done", Str ". Search results print only titles, so each line is short."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can implement add, list, search, change, complete, and delete."]], [Plain [Str "\9744", Space, Str "I assign unique ids."]], [Plain [Str "\9744", Space, Str "I update timestamps correctly."]], [Plain [Str "\9744", Space, Str "I return clear messages for failures."]], [Plain [Str "\9744", Space, Str "I can make output repeatable with a fake clock."]]], HorizontalRule, Header 3 ("lesson-114-validation-and-tests", ["unnumbered", "unlisted"], []) [Str "Lesson 11.4: Validation and tests"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: How to Write Tests"] ("https://doc.rust-lang.org/book/ch11-01-writing-tests.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Test Organization"] ("https://doc.rust-lang.org/book/ch11-03-test-organization.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 11.4: Testing and Refinement"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Run the shared acceptance tests."]], [Plain [Str "Verify that validation rejects bad data."]], [Plain [Str "Read and interpret test results."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The shared acceptance tests describe behavior that every language track's capstone must show:"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Adding a record with an empty title is rejected with a clear message."]], [Plain [Str "A new record receives an unused ", Code ("", [], []) "id", Str "."]], [Plain [Str "Updating a record changes ", Code ("", [], []) "updated_at", Str " but not ", Code ("", [], []) "created_at", Str "."]], [Plain [Str "Deleting a record removes only that record."]], [Plain [Str "Saving and reloading preserves all fields and values (shown in Lesson 11.2)."]], [Plain [Str "Every message and control can be used without color or a mouse (checked by hand in Lesson 11.5)."]]], Para [Str "This lesson automates tests 1 to 4 and also tests completion and the rejection of a blank title in an update. Each test builds a new ", Code ("", [], []) "Manager", Str ", so tests cannot affect each other. The fake clock keeps timestamps predictable so a test can check that ", Code ("", [], []) "updated_at", Str " changed while ", Code ("", [], []) "created_at", Str " did not. Each test is a function returning ", Code ("", [], []) "Result<(), String>", Str ", run by a small loop that prints PASS or FAIL."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "#![allow(dead_code)]
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
        format!(\"{}. {} [{}] ({})\", self.id, self.title, self.category, if self.done { \"done\" } else { \"not done\" })
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
        return Err(\"A title is required.\".to_string());
    }
    if category.trim().is_empty() {
        return Err(\"A category is required.\".to_string());
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
            None => return Err(\"No record has that id.\".to_string()),
        };
        validate(&title, &category)?;
        let stamp = (self.clock)();
        let entry = self.entries.iter_mut().find(|entry| entry.id == id).ok_or(\"No record has that id.\")?;
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
        let position = self.entries.iter().position(|entry| entry.id == id).ok_or(\"No record has that id.\")?;
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
        format!(\"2026-01-15T10:00:{ticks:02}\")
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
    manager.add(\"Notebook\", \"Course notes\", \"supplies\").unwrap();
    manager.add(\"Pencil\", \"Box of 10\", \"supplies\").unwrap();
    manager.add(\"Study plan\", \"Weekly schedule\", \"planning\").unwrap();
    manager
}

fn empty_title_is_rejected() -> Result<(), String> {
    let mut manager = fresh();
    expect(manager.add(\"   \", \"x\", \"supplies\") == Err(\"A title is required.\".to_string()), \"expected the title message\")?;
    expect(manager.entries.len() == 3, \"the list should be unchanged\")
}

fn new_record_gets_an_unused_id() -> Result<(), String> {
    let mut manager = fresh();
    manager.delete(2)?;
    let id = manager.add(\"Ruler\", \"30 cm\", \"supplies\")?;
    expect(id == 4, \"expected id 4\")
}

fn update_changes_updated_at_but_not_created_at() -> Result<(), String> {
    let mut manager = fresh();
    let (created, updated) = {
        let entry = manager.find(1).ok_or(\"record 1 missing\")?;
        (entry.created_at.clone(), entry.updated_at.clone())
    };
    manager.update(1, Changes { description: Some(\"Lecture notes\".to_string()), ..Default::default() })?;
    let entry = manager.find(1).ok_or(\"record 1 missing\")?;
    expect(entry.created_at == created, \"created_at changed\")?;
    expect(entry.updated_at != updated, \"updated_at did not change\")
}

fn delete_removes_only_that_record() -> Result<(), String> {
    let mut manager = fresh();
    manager.delete(2)?;
    let ids: Vec<i32> = manager.entries.iter().map(|entry| entry.id).collect();
    expect(ids == vec![1, 3], \"wrong records remain\")
}

fn complete_marks_done_and_updates_the_record() -> Result<(), String> {
    let mut manager = fresh();
    manager.complete(3)?;
    let entry = manager.find(3).ok_or(\"record 3 missing\")?;
    expect(entry.done && entry.updated_at != entry.created_at, \"completion not recorded\")
}

fn blank_title_cannot_be_saved_by_update() -> Result<(), String> {
    let mut manager = fresh();
    let result = manager.update(1, Changes { title: Some(String::new()), ..Default::default() });
    expect(result == Err(\"A title is required.\".to_string()), \"update accepted a blank title\")
}

fn main() {
    let tests: [(&str, fn() -> Result<(), String>); 6] = [
        (\"1. an empty title is rejected\", empty_title_is_rejected),
        (\"2. a new record gets an unused id\", new_record_gets_an_unused_id),
        (\"3. update changes updated_at but not created_at\", update_changes_updated_at_but_not_created_at),
        (\"4. delete removes only that record\", delete_removes_only_that_record),
        (\"5. complete marks done and updates the record\", complete_marks_done_and_updates_the_record),
        (\"6. a blank title cannot be saved by update\", blank_title_cannot_be_saved_by_update),
    ];

    let mut failures = 0;
    for (name, test) in tests {
        match test() {
            Ok(()) => println!(\"PASS {name}\"),
            Err(message) => {
                failures += 1;
                println!(\"FAIL {name}: {message}\");
            }
        }
    }
    if failures == 0 {
        println!(\"All acceptance tests passed.\");
    } else {
        println!(\"{failures} test(s) failed.\");
    }
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "PASS 1. an empty title is rejected
PASS 2. a new record gets an unused id
PASS 3. update changes updated_at but not created_at
PASS 4. delete removes only that record
PASS 5. complete marks done and updates the record
PASS 6. a blank title cannot be saved by update
All acceptance tests passed.
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Sharing one manager between tests, so one test's deletions change the next test."]], [Plain [Str "Checking only that no error occurred, and not checking the result."]], [Plain [Str "Writing the expected message differently from the program, so a correct program fails the test."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Break ", Code ("", [], []) "Manager::update", Str " so it also changes ", Code ("", [], []) "created_at", Str " and watch test 3 fail. Restore it."]], [Plain [Str "Add a test that searching ignores case."]], [Plain [Str "Add a test that deleting an unknown id returns a message."]], [Plain [Str "Explain why test 2 deletes record 2 before adding the new one."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "The test names begin with the acceptance-test number, so PASS and FAIL lines can be matched to the specification. Read only the first word of each line to hear the overall result quickly."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can run the shared acceptance tests."]], [Plain [Str "\9744", Space, Str "I can test validation failures."]], [Plain [Str "\9744", Space, Str "I can test timestamps with a fake clock."]], [Plain [Str "\9744", Space, Str "I can read PASS and FAIL lines."]], [Plain [Str "\9744", Space, Str "I use a fresh manager for every test."]]], HorizontalRule, Header 3 ("lesson-115-documentation-and-presentation", ["unnumbered", "unlisted"], []) [Str "Lesson 11.5: Documentation and presentation"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Link ("", [], []) [Str "Unit P, Lesson P.6"] ("docs/pandoc/pdf/src/FOUNDATIONS/unit-p-computing-foundations.md#unit-p-computing-foundations-primer-complete-before-any-language-track", ""), Str ": files, data formats, and the shared accessible workflow"]], [Plain [Str "Matching Python lesson: Lesson 11.5: Final Submission"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write a plain-text project summary."]], [Plain [Str "Report a count of records by category."]], [Plain [Str "Complete a manual accessibility check."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Documentation tells a future reader what the program does and how to run it. Write it as plain text or Markdown with short headings, numbered steps, and complete sentences. Include: the purpose of the program, the ", Code ("", [], []) "cargo", Str " commands to build and run it, the shared record fields, the commands a user can give, the accessibility checks you carried out, and what you would improve next."], Para [Str "The example generates a summary from the shared sample data. It counts records by category in a ", Code ("", [], []) "BTreeMap", Str ", which keeps its keys sorted, so the output is stable. It then prints the manual accessibility checklist. The unchecked boxes ", Code ("", [], []) "[ ]", Str " are for ", Emph [Str "you"], Str " to complete by hand with your own access technology; the program cannot verify them."], Para [Str "Acceptance test 6 is a manual check: every message and control can be used without color or a mouse. Test it with the keyboard only, and with the screen reader or braille display you actually use. Record what you tested and its version; do not claim compatibility with software you did not test."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::collections::BTreeMap;

struct Entry {
    id: i32,
    title: String,
    category: String,
}

fn main() {
    let sample = vec![
        Entry { id: 1, title: \"Notebook\".to_string(), category: \"supplies\".to_string() },
        Entry { id: 2, title: \"Pencil\".to_string(), category: \"supplies\".to_string() },
        Entry { id: 3, title: \"Study plan\".to_string(), category: \"planning\".to_string() },
    ];

    let mut counts: BTreeMap<&str, u32> = BTreeMap::new();
    for entry in &sample {
        *counts.entry(entry.category.as_str()).or_insert(0) += 1;
    }

    println!(\"Personal Data Manager - Summary\");
    println!(\"Records: {}\", sample.len());
    println!(\"Categories:\");
    for (category, count) in &counts {
        println!(\"- {category}: {count}\");
    }
    let titles: Vec<String> = sample.iter().map(|entry| format!(\"{} ({})\", entry.title, entry.id)).collect();
    println!(\"Titles: {}\", titles.join(\", \"));

    println!();
    println!(\"Manual accessibility checklist (complete this by hand):\");
    let checks = [
        \"[ ] Every command can be used with the keyboard only.\",
        \"[ ] Every message is a complete sentence that says what to do next.\",
        \"[ ] No meaning depends on color, position, or symbols alone.\",
        \"[ ] The output was read with my own screen reader or braille display.\",
        \"[ ] I recorded the operating system, program, and version I tested.\",
    ];
    for check in checks {
        println!(\"{check}\");
    }
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Personal Data Manager - Summary
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
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing documentation that only the author can follow."]], [Plain [Str "Claiming that a program is accessible without recording what was tested and how."]], [Plain [Str "Letting the documentation drift from the program after later changes."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write the project summary for your own capstone using the headings above."]], [Plain [Str "Run the keyboard-only check and record each problem you find."]], [Plain [Str "Ask a classmate to follow your run instructions from a fresh folder and note where they get stuck."]], [Plain [Str "Write three improvements for the next version, ordered by user benefit."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "This is the final accessibility lesson. Read your own documentation aloud from start to finish. Anything you have to look at the screen to understand needs rewriting."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a plain-text project summary."]], [Plain [Str "\9744", Space, Str "I can report counts by category."]], [Plain [Str "\9744", Space, Str "I can run a manual accessibility check."]], [Plain [Str "\9744", Space, Str "I record what I tested."]], [Plain [Str "\9744", Space, Str "I do not claim untested compatibility."]]], HorizontalRule, Header 3 ("course-wide-assessment-and-portfolio", ["unnumbered", "unlisted"], []) [Str "Course-Wide Assessment and Portfolio"], Para [Str "Submit a Cargo project that compiles with the Rust 2024 edition, passes cargo fmt --check, cargo check, and cargo test, and documents its data model, input validation, error handling, persistence format, and keyboard/screen-reader workflow. Include a README with exact build, test, and run commands."], Header 3 ("ai-policy", ["unnumbered", "unlisted"], []) [Str "AI Policy"], Para [Str "AI tools may explain compiler diagnostics, compare ownership strategies, and suggest tests. Learners must explain every ownership transfer, borrow, trait bound, error path, and dependency. Compile and test generated code, review dependency provenance, and do not expose private data or credentials. AI output is a draft, not evidence of correctness."], Header 3 ("rust-specific-verification-notes", ["unnumbered", "unlisted"], []) [Str "Rust-Specific Verification Notes"], Para [Str "The JSON example demonstrates the serialized record shape only; production code should use serde_json. The deterministic pseudo-random example is not cryptographically secure and is not a substitute for a maintained random-number generator."]]