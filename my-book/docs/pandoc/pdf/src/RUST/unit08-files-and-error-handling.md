[Header 2 ("unit-8-files-and-error-handling", [], []) [Str "Unit 8: Files and Error Handling"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops files and error handling through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly."], Header 3 ("lesson-81-reading-text-files", ["unnumbered", "unlisted"], []) [Str "Lesson 8.1: Reading text files"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language"] ("https://doc.rust-lang.org/book/", "")]], [Plain [Link ("", [], []) [Str "Rust standard library"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Link ("", [], []) [Str "Cargo Book"] ("https://doc.rust-lang.org/cargo/", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain Reading text files using Rust's types, ownership model, and standard-library conventions."]], [Plain [Str "Select an idiomatic Rust construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the example's behavior."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "File APIs return Result. The ? operator propagates compatible failures. RAII releases resources when owners leave scope. Use a maintained parser/serializer such as serde_json for production JSON; the standard-library-only example illustrates the serialized record shape. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::fs; fn main(){let p=std::env::temp_dir().join(\"rust_read_demo.txt\");fs::write(&p,\"Avery,82\\\\n\").unwrap();let s=fs::read_to_string(&p).unwrap();print!(\"{s}\");let _=fs::remove_file(p);}
", Para [Strong [Str "Expected behavior:"], Str " Demonstrates a scoped file operation in the system temporary directory and removes its demonstration file."], Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using unwrap on production I/O paths instead of handling or propagating errors."]], [Plain [Str "Assuming file handles require manual close; RAII drops them at scope exit."]], [Plain [Str "Hand-building JSON without correct escaping; use serde_json in real projects."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line."]], [Plain [Str "Change the canonical inventory and CSV records and predict the result before running it."]], [Plain [Str "Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change."]], [Plain [Str "Refactor one part using the Rust feature named in this lesson (reading text files); run cargo check and explain the diagnostic output."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain reading text files using Rust terminology."]], [Plain [Str "\9744", Space, Str "I can compile and run the example with cargo run."]], [Plain [Str "\9744", Space, Str "I can explain the ownership, borrowing, and type decisions used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-82-writing-and-appending-files", ["unnumbered", "unlisted"], []) [Str "Lesson 8.2: Writing and appending files"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language"] ("https://doc.rust-lang.org/book/", "")]], [Plain [Link ("", [], []) [Str "Rust standard library"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Link ("", [], []) [Str "Cargo Book"] ("https://doc.rust-lang.org/cargo/", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain Writing and appending files using Rust's types, ownership model, and standard-library conventions."]], [Plain [Str "Select an idiomatic Rust construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the example's behavior."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "File APIs return Result. The ? operator propagates compatible failures. RAII releases resources when owners leave scope. Use a maintained parser/serializer such as serde_json for production JSON; the standard-library-only example illustrates the serialized record shape. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::fs::OpenOptions;use std::io::Write;fn main(){let p=std::env::temp_dir().join(\"rust_append_demo.txt\");{let mut f=OpenOptions::new().create(true).append(true).open(&p).unwrap();writeln!(f,\"Notebook,3\").unwrap();}println!(\"appended inventory record\");let _=std::fs::remove_file(p);}
", Para [Strong [Str "Expected behavior:"], Str " Demonstrates a scoped file operation in the system temporary directory and removes its demonstration file."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using unwrap on production I/O paths instead of handling or propagating errors."]], [Plain [Str "Assuming file handles require manual close; RAII drops them at scope exit."]], [Plain [Str "Hand-building JSON without correct escaping; use serde_json in real projects."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line."]], [Plain [Str "Change the canonical inventory and CSV records and predict the result before running it."]], [Plain [Str "Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change."]], [Plain [Str "Refactor one part using the Rust feature named in this lesson (writing and appending files); run cargo check and explain the diagnostic output."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain writing and appending files using Rust terminology."]], [Plain [Str "\9744", Space, Str "I can compile and run the example with cargo run."]], [Plain [Str "\9744", Space, Str "I can explain the ownership, borrowing, and type decisions used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-83-result-and-error-propagation", ["unnumbered", "unlisted"], []) [Str "Lesson 8.3: Result and error propagation"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Recoverable Errors with Result"] ("https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: To panic! or Not to panic!"] ("https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 8.3: Exceptions - Handling Errors"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Handle a ", Code ("", [], []) "Result", Str " with ", Code ("", [], []) "match", Str " and propagate it with ", Code ("", [], []) "?", Str "."]], [Plain [Str "Tell recoverable errors (", Code ("", [], []) "Result", Str ") from panics."]], [Plain [Str "Use ", Code ("", [], []) "Box<dyn Error>", Str " to combine different error types."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Rust has no exceptions. A function that can fail returns ", Code ("", [], []) "Result<T, E>", Str ", and the caller must handle it: ", Code ("", [], []) "match", Str " on ", Code ("", [], []) "Ok", Str " and ", Code ("", [], []) "Err", Str ", ", Code ("", [], []) "unwrap_or", Str " to supply a default, or ", Code ("", [], []) "?", Str " to return the error to ", Emph [Str "its"], Str " caller. The ", Code ("", [], []) "?", Str " operator also converts the error: with a return type of ", Code ("", [], []) "Result<T, Box<dyn Error>>", Str ", ", Code ("", [], []) "?", Str " accepts both an ", Code ("", [], []) "io::Error", Str " and a ", Code ("", [], []) "ParseIntError", Str "."], Para [Str "A ", Strong [Str "panic"], Str " (", Code ("", [], []) "unwrap()", Str " on an ", Code ("", [], []) "Err", Str ", an index out of range, integer division by zero) stops the program and is for bugs, not for expected problems like a missing file. ", Code ("", [], []) "checked_div", Str " returns an ", Code ("", [], []) "Option", Str " instead of panicking. The error kind of an I/O failure can be matched, for example ", Code ("", [], []) "ErrorKind::NotFound", Str ". Library error messages can depend on the operating system, so the example prints only messages that are the same everywhere."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::error::Error;
use std::fs;
use std::io::ErrorKind;
use std::num::ParseIntError;

fn parse_score(text: &str) -> Result<i32, ParseIntError> {
    let number = text.trim().parse::<i32>()?;
    Ok(number)
}

fn read_first_number(path: &str) -> Result<i32, Box<dyn Error>> {
    let text = fs::read_to_string(path)?;
    let first = text.lines().next().unwrap_or(\"\");
    Ok(first.trim().parse::<i32>()?)
}

fn main() {
    match fs::read_to_string(\"missing_notes.txt\") {
        Ok(_) => println!(\"The file was read.\"),
        Err(error) if error.kind() == ErrorKind::NotFound => println!(\"Error: missing_notes.txt was not found.\"),
        Err(_) => println!(\"Error: the file could not be read.\"),
    }

    match parse_score(\"abc\") {
        Ok(number) => println!(\"Score {number}\"),
        Err(error) => println!(\"Error: 'abc' is not a valid score ({error})\"),
    }
    println!(\"{:?}\", parse_score(\" 88 \"));

    println!(\"{:?}\", 10_i32.checked_div(0));
    println!(\"{}\", 10_i32.checked_div(0).unwrap_or(0));

    match read_first_number(\"missing_notes.txt\") {
        Ok(number) => println!(\"First number: {number}\"),
        Err(_) => println!(\"Could not read a number from the file.\"),
    }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score (invalid digit found in string)
Ok(88)
None
0
Could not read a number from the file.
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Calling ", Code ("", [], []) "unwrap()", Str " on a ", Code ("", [], []) "Result", Str " for expected failures, which turns them into panics."]], [Plain [Str "Using ", Code ("", [], []) "?", Str " in a function whose return type is not a ", Code ("", [], []) "Result", Str " or ", Code ("", [], []) "Option", Str ", which is a compile error."]], [Plain [Str "Printing an operating-system error message in an expected output, which differs between systems."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict each printed line before running."]], [Plain [Str "Write a function that reads a file and returns the number of lines as a ", Code ("", [], []) "Result", Str "."]], [Plain [Str "Use ", Code ("", [], []) "?", Str " in a function that parses two numbers and adds them."]], [Plain [Str "Explain when to return a ", Code ("", [], []) "Result", Str " and when a panic is acceptable."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.' When a panic message appears, read the line that names your own file first."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can handle a ", Code ("", [], []) "Result", Str " with ", Code ("", [], []) "match", Str "."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "?", Str " to pass errors up."]], [Plain [Str "\9744", Space, Str "I can tell a ", Code ("", [], []) "Result", Str " from a panic."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "Box<dyn Error>", Str "."]], [Plain [Str "\9744", Space, Str "I can write clear error messages."]]], HorizontalRule, Header 3 ("lesson-84-resource-cleanup-and-raii", ["unnumbered", "unlisted"], []) [Str "Lesson 8.4: Resource cleanup and RAII"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Running Code on Cleanup with the Drop Trait"] ("https://doc.rust-lang.org/book/ch15-03-drop.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 8.4: The else and finally Blocks"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain that Rust releases resources when a value goes out of scope."]], [Plain [Str "Implement ", Code ("", [], []) "Drop", Str " to see when cleanup runs."]], [Plain [Str "Close a file by letting it go out of scope."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Rust has no ", Code ("", [], []) "finally", Str ". Instead, every value is ", Emph [Str "dropped"], Str " (cleaned up) automatically when its owner goes out of scope, and values are dropped in ", Strong [Str "reverse order of creation"], Str ". This idea is called ", Strong [Str "RAII"], Str " (resource acquisition is initialization). A file handle closes itself when it is dropped, so a file cannot be left open by a forgotten call, even if the code returns early or a panic unwinds."], Para [Str "A type can run its own cleanup by implementing the ", Code ("", [], []) "Drop", Str " trait, whose ", Code ("", [], []) "drop", Str " method is called automatically. ", Code ("", [], []) "drop(value)", Str " ends a value's life early. A binding named ", Code ("", [], []) "_name", Str " stays alive until the end of its scope, but the bare pattern ", Code ("", [], []) "_", Str " drops the value immediately, which surprises many learners."], Para [Str "The example shows the order of cleanup and writes a file inside a block so that it is closed before it is read back."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::fs::{self, File};
use std::io::Write;

struct Guard(&'static str);

impl Drop for Guard {
    fn drop(&mut self) {
        println!(\"Releasing {}\", self.0);
    }
}

fn main() {
    let _outer = Guard(\"outer resource\");
    {
        let _inner = Guard(\"inner resource\");
        println!(\"Using the inner resource\");
    }
    println!(\"After the inner block\");

    let early = Guard(\"early resource\");
    drop(early);
    println!(\"After the explicit drop\");

    {
        let mut file = File::create(\"cleanup_demo.txt\").expect(\"could not create the file\");
        file.write_all(b\"Some data.\\n\").expect(\"could not write the file\");
    }
    let text = fs::read_to_string(\"cleanup_demo.txt\").expect(\"could not read the file\");
    println!(\"{}\", text.trim());
    println!(\"End of main\");
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Using the inner resource
Releasing inner resource
After the inner block
Releasing early resource
After the explicit drop
Some data.
End of main
Releasing outer resource
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing ", Code ("", [], []) "let _ = Guard(...)", Str " and expecting it to live until the end of the scope. It is dropped at once."]], [Plain [Str "Expecting values to be dropped in the order they were created. The order is reversed."]], [Plain [Str "Reading a file before the handle that wrote it has gone out of scope, which can miss buffered data."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the eight printed lines, especially the order of the ", Code ("", [], []) "Releasing", Str " lines."]], [Plain [Str "Change ", Code ("", [], []) "_outer", Str " to ", Code ("", [], []) "_", Str " and describe what changes."]], [Plain [Str "Add a third guard and predict where its message appears."]], [Plain [Str "Explain why Rust does not need a ", Code ("", [], []) "finally", Str " block."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print a short labelled line when each resource is released, so the screen reader announces the order of cleanup. Labelled lines make a rule that is normally invisible audible."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain scope-based cleanup."]], [Plain [Str "\9744", Space, Str "I can implement ", Code ("", [], []) "Drop", Str "."]], [Plain [Str "\9744", Space, Str "I know values drop in reverse order."]], [Plain [Str "\9744", Space, Str "I know a file closes when it is dropped."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "_", Str " and ", Code ("", [], []) "_name", Str " differ."]]], HorizontalRule, Header 3 ("lesson-85-json-serialization-and-persistence", ["unnumbered", "unlisted"], []) [Str "Lesson 8.5: JSON serialization and persistence"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Packages and Crates"] ("https://doc.rust-lang.org/book/ch07-01-packages-and-crates.html", "")]], [Plain [Link ("", [], []) [Str "serde_json documentation"] ("https://docs.rs/serde_json/", "")]], [Plain [Str "JSON specification: https://www.json.org"]], [Plain [Str "Matching Python lesson: Lesson 8.5: Storing Data with JSON"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain why this lesson includes a JSON helper."]], [Plain [Str "Encode and decode the shared task records."]], [Plain [Str "Handle a missing or malformed file."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The Rust standard library has no JSON support. Real projects add the ", Code ("", [], []) "serde", Str " and ", Code ("", [], []) "serde_json", Str " crates through Cargo. To keep this course free of dependencies, the example includes a ", Emph [Str "teaching implementation"], Str ": an ", Code ("", [], []) "enum Json", Str " with an ", Code ("", [], []) "encode", Str " function and a ", Code ("", [], []) "decode", Str " function built from a small parser. It handles strings, numbers, booleans, ", Code ("", [], []) "null", Str ", lists, and objects, writes object keys in sorted order (a ", Code ("", [], []) "BTreeMap", Str "), and reports malformed text with a message that includes the position. It is not a replacement for a production library, and a decimal such as ", Code ("", [], []) "2.0", Str " is written as ", Code ("", [], []) "2", Str ", so it reads back as an integer."], Para [Str "JSON text stores data in a standard format: ", Code ("", [], []) "{ ... }", Str " holds key-value pairs, ", Code ("", [], []) "[ ... ]", Str " holds ordered items, and text is in double quotation marks. Decoded data is a ", Code ("", [], []) "Json", Str " enum, so ", Code ("", [], []) "match", Str " forces you to handle every kind of value."], Para [Str "The shared to-do record has the fields ", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "done", Str ", and ", Code ("", [], []) "created_at", Str ". The example saves two tasks, loads them back, and shows the message for a malformed file."], Para [Str "The teaching helper decodes JSON ", Code ("", [], []) "null", Str " as ", Code ("", [], []) "Json::Null", Str " and whole numbers as ", Code ("", [], []) "Json::Int", Str ". It does not handle every number edge case that a full parser must."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::collections::BTreeMap;

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
use std::io;

fn task(id: i64, title: &str, description: &str, done: bool, created_at: &str) -> Json {
    let mut map = BTreeMap::new();
    map.insert(\"id\".to_string(), Json::Int(id));
    map.insert(\"title\".to_string(), Json::Str(title.to_string()));
    map.insert(\"description\".to_string(), Json::Str(description.to_string()));
    map.insert(\"done\".to_string(), Json::Bool(done));
    map.insert(\"created_at\".to_string(), Json::Str(created_at.to_string()));
    Json::Object(map)
}

fn main() -> io::Result<()> {
    let tasks = Json::List(vec![
        task(1, \"Study programming\", \"Finish Unit 8\", false, \"2026-01-15T09:00:00\"),
        task(2, \"Review scores\", \"Check the four scores\", true, \"2026-01-15T09:30:00\"),
    ]);
    fs::write(\"tasks.json\", encode(&tasks))?;

    let text = match fs::read_to_string(\"tasks.json\") {
        Ok(text) => text,
        Err(_) => {
            println!(\"Tasks file not found.\");
            return Ok(());
        }
    };

    match decode(&text) {
        Ok(Json::List(items)) => {
            for item in &items {
                if let Json::Object(map) = item {
                    let id = match map.get(\"id\") {
                        Some(Json::Int(number)) => *number,
                        _ => 0,
                    };
                    let title = match map.get(\"title\") {
                        Some(Json::Str(text)) => text.as_str(),
                        _ => \"?\",
                    };
                    let status = if map.get(\"done\") == Some(&Json::Bool(true)) { \"done\" } else { \"not done\" };
                    println!(\"{id}: {title} ({status})\");
                }
            }
        }
        Ok(_) => println!(\"Error: the tasks file must contain a list.\"),
        Err(message) => println!(\"Error: could not decode tasks file: {message}\"),
    }

    println!(\"{:?}\", decode(\"[{\\\"id\\\": 1,\"));
    Ok(())
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "1: Study programming (not done)
2: Review scores (done)
Err(\"expected a key at position 10\")
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming Rust has built-in JSON support."]], [Plain [Str "Trusting decoded data without matching on the kind of each value."]], [Plain [Str "Overwriting a good data file with an empty list after a failed load."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program and read the saved JSON text from ", Code ("", [], []) "tasks.json", Str "."]], [Plain [Str "Edit ", Code ("", [], []) "tasks.json", Str " by hand to remove a closing bracket and run the loading part again. Read the message."]], [Plain [Str "Add a third task and confirm that it is saved and loaded."]], [Plain [Str "Explain why a production project should use ", Code ("", [], []) "serde_json", Str "."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Open ", Code ("", [], []) "tasks.json", Str " in the terminal and read it as text. JSON in a single line is difficult to navigate, so practise stepping through it by word or character."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I know Rust has no built-in JSON."]], [Plain [Str "\9744", Space, Str "I can encode and decode records."]], [Plain [Str "\9744", Space, Str "I handle missing and malformed files."]], [Plain [Str "\9744", Space, Str "I match on decoded values."]], [Plain [Str "\9744", Space, Str "I know when to use a crate."]]], HorizontalRule]