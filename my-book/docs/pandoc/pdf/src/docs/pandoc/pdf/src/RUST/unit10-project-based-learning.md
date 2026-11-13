[Header 2 ("unit-10-project-based-learning", [], []) [Str "Unit 10: Project-Based Learning"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops project-based learning through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly."], Header 3 ("lesson-101-requirements-and-top-down-design", ["unnumbered", "unlisted"], []) [Str "Lesson 10.1: Requirements and top-down design"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Hash Maps"] ("https://doc.rust-lang.org/book/ch08-03-hash-maps.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Functions"] ("https://doc.rust-lang.org/book/ch03-03-how-functions-work.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 10.1: Project Planning and Design"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write a short requirements list."]], [Plain [Str "Design a command loop with a map of function pointers."]], [Plain [Str "Plan in small steps and test each one."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A project is easier to finish when it is planned in small steps. Write down what the program must do (", Emph [Str "requirements"], Str "), what information it keeps (", Emph [Str "data"], Str "), and the commands a person can give (", Emph [Str "interface"], Str "). Build one small piece, test it, then add the next."], Para [Str "Text-based projects share a ", Emph [Str "command loop"], Str ": show a prompt, read a line, find the matching action, and repeat until the user quits. In Rust, a ", Code ("", [], []) "HashMap<&str, fn()>", Str " holds actions: the keys are command names and the values are ", Emph [Str "function pointers"], Str ". A new command is one new entry, and an unknown command is a failed lookup (", Code ("", [], []) "None", Str ") that prints a helpful message."], Para [Str "The loop stops on ", Code ("", [], []) "quit", Str " and also when input ends. The example is a skeleton with two commands; typing ", Code ("", [], []) "help", Str ", ", Code ("", [], []) "look", Str ", an unknown word, and ", Code ("", [], []) "quit", Str " shows each path."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::collections::HashMap;
use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn help() {
    println!(\"Commands: help, look, quit\");
}

fn look() {
    println!(\"You are in a dark cave.\");
}

fn main() {
    let mut commands: HashMap<&str, fn()> = HashMap::new();
    commands.insert(\"help\", help);
    commands.insert(\"look\", look);

    println!(\"Type a command:\");
    let mut line = next_line();
    while let Some(text) = &line {
        if text == \"quit\" {
            break;
        }
        match commands.get(text.as_str()) {
            Some(handler) => handler(),
            None => println!(\"I don't understand that command. Type help for a list.\"),
        }
        println!(\"Type a command:\");
        line = next_line();
    }
    println!(\"Goodbye!\");
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "help
look
dance
quit
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "Type a command:
Commands: help, look, quit
Type a command:
You are in a dark cave.
Type a command:
I don't understand that command. Type help for a list.
Type a command:
Goodbye!
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "Type a command:
Goodbye!
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Starting to code before listing the requirements."]], [Plain [Str "Using a long chain of ", Code ("", [], []) "if", Str " statements instead of a map of handlers."]], [Plain [Str "Forgetting that an unknown command should say what to do next."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write five requirements for the text adventure and the to-do list."]], [Plain [Str "Add a ", Code ("", [], []) "score", Str " command that prints the shared scores."]], [Plain [Str "Add the aliases ", Code ("", [], []) "h", Str " and ", Code ("", [], []) "l", Str " without copying the functions."]], [Plain [Str "Describe the data for the capstone in three sentences."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Prompts and responses are on separate lines and every response is a complete sentence. Test the prompts by listening to them before you add features."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can list requirements."]], [Plain [Str "\9744", Space, Str "I can design a command loop."]], [Plain [Str "\9744", Space, Str "I can use a map of function pointers."]], [Plain [Str "\9744", Space, Str "I handle unknown commands."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]]], HorizontalRule, Header 3 ("lesson-102-text-adventure-part-1-five-rooms-and-movement", ["unnumbered", "unlisted"], []) [Str "Lesson 10.2: Text Adventure, Part 1: Five Rooms and Movement"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Hash Maps"] ("https://doc.rust-lang.org/book/ch08-03-hash-maps.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Structs"] ("https://doc.rust-lang.org/book/ch05-01-defining-structs.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Represent the five canonical rooms and their exits with Rust structs and hash maps."]], [Plain [Str "Move through valid exits without changing location after an invalid command."]], [Plain [Str "Explain why the north exit from the locked-door room is not available yet."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The shared adventure has five rooms: start_room, tunnel, clearing, locked_door_room, and treasure_room. The unconditional connections are start north to tunnel; tunnel south to start and east to clearing; clearing west to tunnel and north to the locked-door room; and locked-door room south to clearing. The north exit to the treasure room is conditional and is added in Part 2 only after the shiny-key puzzle is solved."], Para [Str "A Room struct stores a description and a HashMap of exits. HashMap::get returns an Option; a missing direction must not change the current room."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::collections::HashMap;
use std::io;

struct Room {
    description: &'static str,
    exits: HashMap<&'static str, &'static str>,
}

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_lowercase()),
    }
}

fn main() {
    let rooms = HashMap::from([
        (\"start_room\", Room {
            description: \"A dimly lit cave. A narrow passage leads north.\",
            exits: HashMap::from([(\"north\", \"tunnel\")]),
        }),
        (\"tunnel\", Room {
            description: \"A damp tunnel. Passages lead south and east.\",
            exits: HashMap::from([(\"south\", \"start_room\"), (\"east\", \"clearing\")]),
        }),
        (\"clearing\", Room {
            description: \"A quiet clearing. An antechamber lies to the north.\",
            exits: HashMap::from([(\"west\", \"tunnel\"), (\"north\", \"locked_door_room\")]),
        }),
        (\"locked_door_room\", Room {
            description: \"A chamber with a heavy door to the north.\",
            exits: HashMap::from([(\"south\", \"clearing\")]),
        }),
        (\"treasure_room\", Room {
            description: \"You found the treasure. You win!\",
            exits: HashMap::new(),
        }),
    ]);

    let mut current_room = \"start_room\";
    loop {
        let room = rooms.get(current_room).expect(\"current room must exist\");
        println!(\"---\");
        println!(\"{}\", room.description);
        println!(\"What do you want to do?\");
        let command = next_line().unwrap_or_else(|| \"quit\".to_string());
        if command == \"quit\" {
            println!(\"Exiting game. Goodbye!\");
            break;
        }
        match room.exits.get(command.as_str()) {
            Some(destination) => current_room = destination,
            None => println!(\"You cannot go that way. Enter a listed direction or quit.\"),
        }
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With north, east, north, north, quit entered as separate input lines, the player visits tunnel, clearing, and locked_door_room. The second north from locked_door_room is rejected and the current room does not change. The treasure room exists in the model but cannot be reached in Part 1."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Adding the treasure-room north exit before implementing the key puzzle."]], [Plain [Str "Updating current_room before confirming that the requested exit exists."]], [Plain [Str "Assuming a direction is present instead of handling None from HashMap::get."]], [Plain [Str "Defining an exit whose destination is not one of the five room identifiers."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace north, east, north, north and record the room after each command."]], [Plain [Str "Try west from start_room; confirm that the location does not change."]], [Plain [Str "Check that every destination in every unconditional exit exists in rooms."]], [Plain [Str "Explain why treasure_room has no incoming exit in Part 1."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the separator, room description, and prompt in order. The invalid-movement response explains what happened and how to continue. Test the sequence by listening to terminal output; do not rely on a visual map."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model all five canonical rooms."]], [Plain [Str "\9744", Space, Str "I can represent exits with a hash map."]], [Plain [Str "\9744", Space, Str "I can move only when an exit exists."]], [Plain [Str "\9744", Space, Str "I can reject an invalid direction without changing state."]], [Plain [Str "\9744", Space, Str "I can explain why the treasure room is not yet reachable."]]], HorizontalRule, Header 3 ("lesson-103-text-adventure-part-2-shiny-key-and-locked-door", ["unnumbered", "unlisted"], []) [Str "Lesson 10.3: Text Adventure, Part 2: Shiny Key and Locked Door"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Vectors"] ("https://doc.rust-lang.org/book/ch08-01-vectors.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: References and Borrowing"] ("https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Place the shiny key in start_room and transfer it to inventory exactly once."]], [Plain [Str "Require the player to use the key while in locked_door_room."]], [Plain [Str "Unlock the north exit to treasure_room only after the puzzle succeeds."]], [Plain [Str "End the game when the player reaches the treasure room."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Part 2 keeps the same five-room graph. The shiny key begins in start_room. The take shiny key command removes it from that room and adds it to inventory. The use shiny key command works only in locked_door_room and only when the key is in inventory. Attempting north from the locked-door room before that action prints a locked-door message and leaves the player in place. After the key is used, north leads to treasure_room."], Para [Str "Room descriptions do not claim that an item is still present. Room items and inventory are announced on separate lines."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::collections::HashMap;
use std::io;

struct Room {
    description: &'static str,
    exits: HashMap<&'static str, &'static str>,
    items: Vec<&'static str>,
}

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_lowercase()),
    }
}

fn main() {
    let mut rooms = HashMap::from([
        (\"start_room\", Room {
            description: \"A dimly lit cave.\",
            exits: HashMap::from([(\"north\", \"tunnel\")]),
            items: vec![\"shiny key\"],
        }),
        (\"tunnel\", Room {
            description: \"A damp tunnel. Passages lead south and east.\",
            exits: HashMap::from([(\"south\", \"start_room\"), (\"east\", \"clearing\")]),
            items: Vec::new(),
        }),
        (\"clearing\", Room {
            description: \"A quiet clearing. An antechamber lies to the north.\",
            exits: HashMap::from([(\"west\", \"tunnel\"), (\"north\", \"locked_door_room\")]),
            items: Vec::new(),
        }),
        (\"locked_door_room\", Room {
            description: \"A chamber with a heavy door to the north.\",
            exits: HashMap::from([(\"south\", \"clearing\"), (\"north\", \"treasure_room\")]),
            items: Vec::new(),
        }),
        (\"treasure_room\", Room {
            description: \"You found the treasure. You win!\",
            exits: HashMap::new(),
            items: Vec::new(),
        }),
    ]);

    let mut current_room = \"start_room\";
    let mut inventory: Vec<&'static str> = Vec::new();
    let mut door_locked = true;

    loop {
        let room = rooms.get(current_room).expect(\"current room must exist\");
        println!();
        println!(\"{}\", room.description);
        if current_room == \"treasure_room\" {
            break;
        }
        if !room.items.is_empty() {
            println!(\"You see: {}\", room.items.join(\", \"));
        }
        println!(
            \"Your inventory: {}\",
            if inventory.is_empty() { \"empty\" } else { \"shiny key\" }
        );
        println!(\"What do you want to do?\");

        let command = next_line().unwrap_or_else(|| \"quit\".to_string());
        match command.as_str() {
            \"quit\" => {
                println!(\"You quit the adventure.\");
                break;
            }
            \"take shiny key\" => {
                let taken = {
                    let room = rooms.get_mut(current_room).expect(\"current room must exist\");
                    if let Some(index) = room.items.iter().position(|item| *item == \"shiny key\") {
                        room.items.remove(index);
                        true
                    } else {
                        false
                    }
                };
                if taken {
                    inventory.push(\"shiny key\");
                    println!(\"You picked up the shiny key.\");
                } else {
                    println!(\"There is no shiny key here to take.\");
                }
            }
            \"use shiny key\" => {
                if current_room != \"locked_door_room\" {
                    println!(\"You must be at the locked door to use the key.\");
                } else if !inventory.contains(&\"shiny key\") {
                    println!(\"You do not have the shiny key.\");
                } else {
                    door_locked = false;
                    println!(\"You unlocked the door!\");
                }
            }
            \"north\" if current_room == \"locked_door_room\" && door_locked => {
                println!(\"The door is locked! You need to use the shiny key here.\");
            }
            direction => {
                let destination = rooms
                    .get(current_room)
                    .and_then(|room| room.exits.get(direction))
                    .copied();
                match destination {
                    Some(next_room) => current_room = next_room,
                    None => println!(
                        \"Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.\"
                    ),
                }
            }
        }
    }
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Use this sequence to verify the puzzle: north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north."], Para [Str "The first north attempt from locked_door_room must be rejected. Taking the key removes it from start_room and adds it to inventory. Using it outside locked_door_room must be rejected. Using it there prints You unlocked the door!; the next north reaches treasure_room and prints You found the treasure. You win!. End-of-file is treated as quit."], Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Leaving the shiny key in the room after adding it to inventory."]], [Plain [Str "Unlocking the door outside locked_door_room."]], [Plain [Str "Unlocking the door without checking inventory."]], [Plain [Str "Allowing north movement before door_locked becomes false."]], [Plain [Str "Describing the key as still on the floor after it has been collected."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the full sequence and record room, room items, inventory, and door state after every command."]], [Plain [Str "Try take shiny key twice; the second attempt must not duplicate the item."]], [Plain [Str "Try use shiny key in start_room and clearing; both attempts must be rejected."]], [Plain [Str "Try north from locked_door_room before and after unlocking."]], [Plain [Str "Add a look command that announces room, visible items, inventory, and exits in a consistent order."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Announce room description, visible items, inventory, and prompt as separate text lines. Every failed action explains why it failed. Listen to the full puzzle sequence and verify that key location and door state are unambiguous."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model the five canonical rooms."]], [Plain [Str "\9744", Space, Str "I can transfer the shiny key from a room to inventory."]], [Plain [Str "\9744", Space, Str "I can prevent duplicate pickup."]], [Plain [Str "\9744", Space, Str "I can require key use in the locked-door room."]], [Plain [Str "\9744", Space, Str "I can block and unlock the north exit."]], [Plain [Str "\9744", Space, Str "I can end the game when the treasure room is reached."]]], HorizontalRule, Header 3 ("lesson-104-command-line-to-do-manager", ["unnumbered", "unlisted"], []) [Str "Lesson 10.4: Command-line to-do manager"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Recoverable Errors with Result"] ("https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Reading a File"] ("https://doc.rust-lang.org/book/ch12-02-reading-a-file.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 10.4: Building a Command-Line To-Do List"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Keep records with the shared fields."]], [Plain [Str "Save and load them as JSON."]], [Plain [Str "Offer add, view, mark-done, save, load, and quit commands."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A to-do list ties together records, loops, functions, and files. Each task is a struct with the shared fields ", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "done", Str ", and ", Code ("", [], []) "created_at", Str ". The program keeps a ", Code ("", [], []) "Vec<Task>", Str " in memory, shows a numbered menu, and saves the list to ", Code ("", [], []) "todos.json", Str " when asked and on exit."], Para [Str "Saving uses the teaching JSON helper from Lesson 8.5, included here so the example runs on its own. Each task is converted to a ", Code ("", [], []) "Json::Object", Str " for saving and rebuilt from one when loading, and the conversion refuses a record with a missing field. At start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program. The timestamp is computed from the system clock in UTC with a short date algorithm, because the standard library has no date formatting."], Para [Str "In the sample session the user adds two tasks, views the list, marks task 2 done, views it again, tries an invalid menu choice, views the list, and quits."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "#![allow(dead_code)]
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
use std::io;
use std::time::{SystemTime, UNIX_EPOCH};

struct Task {
    id: i64,
    title: String,
    description: String,
    done: bool,
    created_at: String,
}

fn civil_from_days(days: i64) -> (i64, i64, i64) {
    let z = days + 719468;
    let era = z.div_euclid(146097);
    let doe = z.rem_euclid(146097);
    let yoe = (doe - doe / 1460 + doe / 36524 - doe / 146096) / 365;
    let year = yoe + era * 400;
    let doy = doe - (365 * yoe + yoe / 4 - yoe / 100);
    let mp = (5 * doy + 2) / 153;
    let day = doy - (153 * mp + 2) / 5 + 1;
    let month = if mp < 10 { mp + 3 } else { mp - 9 };
    (if month <= 2 { year + 1 } else { year }, month, day)
}

fn now_iso() -> String {
    let seconds = SystemTime::now().duration_since(UNIX_EPOCH).map(|d| d.as_secs() as i64).unwrap_or(0);
    let (year, month, day) = civil_from_days(seconds.div_euclid(86400));
    let rest = seconds.rem_euclid(86400);
    format!(\"{year:04}-{month:02}-{day:02}T{:02}:{:02}:{:02}\", rest / 3600, rest % 3600 / 60, rest % 60)
}

fn to_json(task: &Task) -> Json {
    let mut map = BTreeMap::new();
    map.insert(\"id\".to_string(), Json::Int(task.id));
    map.insert(\"title\".to_string(), Json::Str(task.title.clone()));
    map.insert(\"description\".to_string(), Json::Str(task.description.clone()));
    map.insert(\"done\".to_string(), Json::Bool(task.done));
    map.insert(\"created_at\".to_string(), Json::Str(task.created_at.clone()));
    Json::Object(map)
}

fn text_field(map: &BTreeMap<String, Json>, key: &str) -> Result<String, String> {
    match map.get(key) {
        Some(Json::Str(text)) => Ok(text.clone()),
        _ => Err(format!(\"missing field {key}\")),
    }
}

fn from_json(value: &Json) -> Result<Task, String> {
    let Json::Object(map) = value else {
        return Err(\"a task must be an object\".to_string());
    };
    let id = match map.get(\"id\") {
        Some(Json::Int(number)) => *number,
        _ => return Err(\"missing field id\".to_string()),
    };
    Ok(Task {
        id,
        title: text_field(map, \"title\")?,
        description: text_field(map, \"description\")?,
        done: map.get(\"done\") == Some(&Json::Bool(true)),
        created_at: text_field(map, \"created_at\")?,
    })
}

fn load_todos() -> Vec<Task> {
    let text = match fs::read_to_string(\"todos.json\") {
        Ok(text) => text,
        Err(_) => {
            println!(\"No existing tasks found.\");
            return Vec::new();
        }
    };
    let loaded = match decode(&text) {
        Ok(Json::List(items)) => items.iter().map(from_json).collect::<Result<Vec<Task>, String>>(),
        Ok(_) => Err(\"expected a list\".to_string()),
        Err(message) => Err(message),
    };
    match loaded {
        Ok(tasks) => {
            println!(\"Tasks loaded.\");
            tasks
        }
        Err(_) => {
            println!(\"Error: todos.json is not valid JSON. Starting with an empty list.\");
            Vec::new()
        }
    }
}

fn save_todos(todos: &[Task]) -> io::Result<()> {
    let list = Json::List(todos.iter().map(to_json).collect());
    fs::write(\"todos.json\", encode(&list))?;
    println!(\"Tasks saved.\");
    Ok(())
}

fn add_task(todos: &mut Vec<Task>, title: &str, description: &str) {
    if title.trim().is_empty() {
        println!(\"A title is required.\");
        return;
    }
    let id = todos.iter().map(|task| task.id).max().unwrap_or(0) + 1;
    todos.push(Task {
        id,
        title: title.trim().to_string(),
        description: description.trim().to_string(),
        done: false,
        created_at: now_iso(),
    });
    println!(\"Task '{}' added.\", title.trim());
}

fn view_tasks(todos: &[Task]) {
    if todos.is_empty() {
        println!(\"No tasks in your list.\");
        return;
    }
    println!(\"--- Your To-Do List ---\");
    for task in todos {
        let status = if task.done { \"done\" } else { \"not done\" };
        println!(\"{}. {} ({})\", task.id, task.title, status);
    }
    println!(\"-----------------------\");
}

fn mark_done(todos: &mut [Task], text: &str) {
    let Ok(id) = text.trim().parse::<i64>() else {
        println!(\"Please enter a whole number.\");
        return;
    };
    match todos.iter_mut().find(|task| task.id == id) {
        Some(task) => {
            task.done = true;
            println!(\"Task '{}' marked as done.\", task.title);
        }
        None => println!(\"No task has that number.\"),
    }
}

fn show_menu() {
    println!();
    println!(\"--- To-Do List Menu ---\");
    println!(\"1. Add Task\");
    println!(\"2. View Tasks\");
    println!(\"3. Mark Task Done\");
    println!(\"4. Save Tasks\");
    println!(\"5. Load Tasks\");
    println!(\"6. Quit\");
    println!(\"-----------------------\");
}

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() -> io::Result<()> {
    let mut todos = load_todos();
    loop {
        show_menu();
        println!(\"Enter your choice (1-6):\");
        let choice = next_line().unwrap_or_else(|| \"6\".to_string());
        match choice.as_str() {
            \"1\" => {
                println!(\"Enter task title:\");
                let title = next_line().unwrap_or_default();
                println!(\"Enter task description:\");
                let description = next_line().unwrap_or_default();
                add_task(&mut todos, &title, &description);
            }
            \"2\" => view_tasks(&todos),
            \"3\" => {
                view_tasks(&todos);
                println!(\"Enter task number to mark done:\");
                let text = next_line().unwrap_or_default();
                mark_done(&mut todos, &text);
            }
            \"4\" => save_todos(&todos)?,
            \"5\" => todos = load_todos(),
            \"6\" => {
                save_todos(&todos)?;
                println!(\"Goodbye!\");
                return Ok(());
            }
            _ => println!(\"Invalid choice. Please try again.\"),
        }
    }
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "1
Study programming
Finish Unit 10
1
Review scores
Check the four scores
2
3
2
3
7
2
6
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "No existing tasks found.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Study programming' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Review scores' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------
Enter task number to mark done:
Task 'Review scores' marked as done.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------
Enter task number to mark done:
No task has that number.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Tasks saved.
Goodbye!
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "No existing tasks found.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Tasks saved.
Goodbye!
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Saving the file but never loading it, so tasks disappear between runs."]], [Plain [Str "Reusing a deleted task's id, which can confuse saved references."]], [Plain [Str "Letting a damaged ", Code ("", [], []) "todos.json", Str " crash the program instead of printing a message."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the sample session, then run the program again typing ", Code ("", [], []) "2", Str " and ", Code ("", [], []) "6", Str " to see the saved tasks."]], [Plain [Str "Add a command to delete a task by number."]], [Plain [Str "Open ", Code ("", [], []) "todos.json", Str " and read the saved text. Edit it to remove a bracket and run the program again."]], [Plain [Str "Show each task's description in the view command."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Every menu is printed as numbered lines and every prompt is on its own line. The status words are ", Code ("", [], []) "done", Str " and ", Code ("", [], []) "not done", Str ", not symbols, so the list reads clearly in speech and braille."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can keep records with the shared fields."]], [Plain [Str "\9744", Space, Str "I can save and load JSON."]], [Plain [Str "\9744", Space, Str "I handle a missing or damaged file."]], [Plain [Str "\9744", Space, Str "I keep ids unique."]], [Plain [Str "\9744", Space, Str "I show status in words."]]], HorizontalRule, Header 3 ("lesson-105-accessible-interaction-and-validation", ["unnumbered", "unlisted"], []) [Str "Lesson 10.5: Accessible interaction and validation"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Recoverable Errors with Result"] ("https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Option"] ("https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 10.5: Refining User Experience and Validation"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write reusable validation functions."]], [Plain [Str "Limit retries and handle the end of input."]], [Plain [Str "Write clear, accessible messages."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Reusable validation functions make every menu and form consistent. ", Code ("", [], []) "ask_number(prompt, low, high, attempts)", Str " prints a prompt, reads a line, converts it, checks the range, and either returns ", Code ("", [], []) "Some(number)", Str " or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns ", Code ("", [], []) "None", Str ". ", Code ("", [], []) "ask_yes_no(prompt)", Str " returns ", Code ("", [], []) "Option<bool>", Str " and accepts ", Code ("", [], []) "y", Str ", ", Code ("", [], []) "yes", Str ", ", Code ("", [], []) "n", Str ", and ", Code ("", [], []) "no", Str " in any letter case. The ", Code ("", [], []) "Option", Str " return type makes the caller deal with the failure case."], Para [Str "Good messages say ", Emph [Str "what was wrong"], Str " and ", Emph [Str "what to do"], Str ": \"Enter a whole number from 0 to 100,\" not \"Invalid.\" They never depend on color, position, or symbols alone, and they use the same wording every time."], Para [Str "The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn ask_number(prompt: &str, low: i32, high: i32, attempts: u32) -> Option<i32> {
    for attempt in 1..=attempts {
        println!(\"{prompt}\");
        let text = next_line()?;
        if let Ok(number) = text.parse::<i32>() {
            if (low..=high).contains(&number) {
                return Some(number);
            }
        }
        println!(\"Enter a whole number from {low} to {high}. You have {} attempt(s) left.\", attempts - attempt);
    }
    None
}

fn ask_yes_no(prompt: &str) -> Option<bool> {
    loop {
        println!(\"{prompt} (yes or no)\");
        let text = next_line()?.to_lowercase();
        match text.as_str() {
            \"y\" | \"yes\" => return Some(true),
            \"n\" | \"no\" => return Some(false),
            _ => println!(\"Please answer yes or no.\"),
        }
    }
}

fn main() {
    match ask_number(\"Enter a score from 0 to 100:\", 0, 100, 3) {
        Some(score) => println!(\"Accepted score: {score}\"),
        None => println!(\"No valid score was entered.\"),
    }

    let keep = ask_yes_no(\"Save this score?\");
    println!(\"Save answer: {:?}\", keep);
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "abc
105
88
maybe
y
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 2 attempt(s) left.
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 1 attempt(s) left.
Enter a score from 0 to 100:
Accepted score: 88
Save this score? (yes or no)
Please answer yes or no.
Save this score? (yes or no)
Save answer: Some(true)
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "Enter a score from 0 to 100:
No valid score was entered.
Save this score? (yes or no)
Save answer: None
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing the message \"Invalid\" without saying what is valid."]], [Plain [Str "Accepting a decimal such as 88.5 for a field that requires a whole number."]], [Plain [Str "Looping forever on bad input instead of limiting attempts."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the sample input and read each message aloud."]], [Plain [Str "Run with three invalid numbers and read the final message."]], [Plain [Str "Add ", Code ("", [], []) "ask_text(prompt) -> Option<String>", Str " that rejects empty answers."]], [Plain [Str "Rewrite two messages from earlier lessons so they say what to do next."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Check that every error message ends with an action the user can take, and that the same situation always produces the same words."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write reusable validation functions."]], [Plain [Str "\9744", Space, Str "I limit retries."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]], [Plain [Str "\9744", Space, Str "I write messages that say what to do."]], [Plain [Str "\9744", Space, Str "I keep wording consistent."]]], HorizontalRule]