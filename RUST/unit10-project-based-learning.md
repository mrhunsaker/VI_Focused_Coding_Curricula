# Unit 10: Project-Based Learning

## Overview
This unit develops project-based learning through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 10.1: Requirements and top-down design

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Requirements and top-down design using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Build an application in vertical slices: requirements, state model, command handling, validation, and accessible output. Separate domain logic from terminal interaction so it can be tested without simulating a user. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main(){let req=["list tasks","add task","mark task complete","save tasks"];for(i,r)in req.iter().enumerate(){println!("{}. {r}",i+1);}}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Combining input, validation, state changes, and output in one oversized function.
2. Using numeric indexes without checking bounds.
3. Making prompts depend on color, animation, or cursor position.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical to-do and capstone record fields and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (requirements and top-down design); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain requirements and top-down design using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
- [The Rust Programming Language: Hash Maps](https://doc.rust-lang.org/book/ch08-03-hash-maps.html)
- [The Rust Programming Language: Functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 10.1: Project Planning and Design

### Learning Objectives
- Write a short requirements list.
- Design a command loop with a map of function pointers.
- Plan in small steps and test each one.

### Concept Explanation

A project is easier to finish when it is planned in small steps. Write down what the program must do (*requirements*), what information it keeps (*data*), and the commands a person can give (*interface*). Build one small piece, test it, then add the next.

Text-based projects share a *command loop*: show a prompt, read a line, find the matching action, and repeat until the user quits. In Rust, a `HashMap<&str, fn()>` holds actions: the keys are command names and the values are *function pointers*. A new command is one new entry, and an unknown command is a failed lookup (`None`) that prints a helpful message.

The loop stops on `quit` and also when input ends. The example is a skeleton with two commands; typing `help`, `look`, an unknown word, and `quit` shows each path.

### Worked Example

```rust
use std::collections::HashMap;
use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn help() {
    println!("Commands: help, look, quit");
}

fn look() {
    println!("You are in a dark cave.");
}

fn main() {
    let mut commands: HashMap<&str, fn()> = HashMap::new();
    commands.insert("help", help);
    commands.insert("look", look);

    println!("Type a command:");
    let mut line = next_line();
    while let Some(text) = &line {
        if text == "quit" {
            break;
        }
        match commands.get(text.as_str()) {
            Some(handler) => handler(),
            None => println!("I don't understand that command. Type help for a list."),
        }
        println!("Type a command:");
        line = next_line();
    }
    println!("Goodbye!");
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
help
look
dance
quit
```

the program prints:
```text
Type a command:
Commands: help, look, quit
Type a command:
You are in a dark cave.
Type a command:
I don't understand that command. Type help for a list.
Type a command:
Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
Type a command:
Goodbye!
```

### Common Mistakes
1. Starting to code before listing the requirements.
2. Using a long chain of `if` statements instead of a map of handlers.
3. Forgetting that an unknown command should say what to do next.

### Activities
1. Write five requirements for the text adventure and the to-do list.
2. Add a `score` command that prints the shared scores.
3. Add the aliases `h` and `l` without copying the functions.
4. Describe the data for the capstone in three sentences.

### Accessibility Practice

Prompts and responses are on separate lines and every response is a complete sentence. Test the prompts by listening to them before you add features.

### Skills Checklist
- [ ] I can list requirements.
- [ ] I can design a command loop.
- [ ] I can use a map of function pointers.
- [ ] I handle unknown commands.
- [ ] I handle the end of input.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Text adventure: rooms and movement using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Build an application in vertical slices: requirements, state model, command handling, validation, and accessible output. Separate domain logic from terminal interaction so it can be tested without simulating a user. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
#[derive(Clone,Copy)]enum Room{StartRoom,Tunnel,Clearing,LockedDoorRoom,TreasureRoom}fn main(){let rooms=[Room::StartRoom,Room::Tunnel,Room::Clearing,Room::LockedDoorRoom,Room::TreasureRoom];let room=rooms[0];let direction="north";let next=match (room,direction){(Room::StartRoom,"north")=>Some(Room::Tunnel),_=>None};println!("entered tunnel={} room_count={}",matches!(next,Some(Room::Tunnel)),rooms.len());}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Combining input, validation, state changes, and output in one oversized function.
2. Using numeric indexes without checking bounds.
3. Making prompts depend on color, animation, or cursor position.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical to-do and capstone record fields and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (text adventure: rooms and movement); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain text adventure: rooms and movement using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
- [The Rust Programming Language: Hash Maps](https://doc.rust-lang.org/book/ch08-03-hash-maps.html)
- [The Rust Programming Language: Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 10.2: Building a Text-Based Adventure Game (Part 1)

### Learning Objectives
- Represent rooms and exits with a struct and a map.
- Move the player by command.
- Handle impossible moves and the end of input.

### Concept Explanation

A room is a struct with a `description` and an `exits` map from a direction to the *name* of another room. The program remembers the player's location in one variable. A move looks up the command in the current room's exits; `get` returns an `Option`, so a missing direction is `None` and the program explains that the move is impossible.

This is the same three-room layout as the Python course: a cave, a tunnel, and a clearing. Part 2 adds items and a locked door.

The example is played with north, east, west, up, south, and quit. The command `up` is not an exit anywhere, so it prints the help message.

### Worked Example

```rust
use std::collections::HashMap;
use std::io;

struct Room {
    description: &'static str,
    exits: HashMap<&'static str, &'static str>,
}

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    let mut rooms: HashMap<&str, Room> = HashMap::new();
    rooms.insert("start_room", Room {
        description: "You are in a dimly lit cave. There's a narrow passage to the NORTH.",
        exits: HashMap::from([("north", "tunnel")]),
    });
    rooms.insert("tunnel", Room {
        description: "The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.",
        exits: HashMap::from([("south", "start_room"), ("east", "clearing")]),
    });
    rooms.insert("clearing", Room {
        description: "You've reached a small, sunny clearing. A faint path leads WEST.",
        exits: HashMap::from([("west", "tunnel")]),
    });

    let mut current = "start_room";
    loop {
        println!("---");
        println!("{}", rooms[current].description);
        println!("What do you want to do?");
        let command = next_line().unwrap_or_else(|| "quit".to_string()).to_lowercase();
        if let Some(next) = rooms[current].exits.get(command.as_str()) {
            current = next;
        } else if command == "quit" {
            println!("Exiting game. Goodbye!");
            break;
        } else {
            println!("I don't understand that command or you can't go that way.");
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
north
east
west
up
south
quit
```

the program prints:
```text
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You've reached a small, sunny clearing. A faint path leads WEST.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
I don't understand that command or you can't go that way.
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Indexing `exits[command]` with a direction that is missing, which panics. Use `get`.
2. Forgetting to treat the end of input as `quit`, so the program loops forever when input is piped in.
3. Misspelling a room name in `exits`, so a move leads to a room that does not exist and `rooms[current]` panics.

### Activities
1. Trace the six commands by hand and write the room after each one.
2. Add a fourth room reached from the clearing and test it.
3. Add the aliases `n`, `s`, `e`, and `w`.
4. Write a loop that checks that every exit names a real room.

### Accessibility Practice

Each turn prints a separator line, the description, and the prompt, so a whole turn can be read in order. Listen to one turn from start to finish to confirm that a player could follow it without seeing the screen.

### Skills Checklist
- [ ] I can represent rooms with a struct.
- [ ] I can move the player by command.
- [ ] I can handle an impossible move.
- [ ] I treat end of input as quit.
- [ ] I can trace a game by hand.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Text adventure: inventory and puzzles using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Build an application in vertical slices: requirements, state model, command handling, validation, and accessible output. Separate domain logic from terminal interaction so it can be tested without simulating a user. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
fn main(){let mut inventory=vec!["key"];let unlocked=inventory.contains(&"key");if unlocked{inventory.push("map");}println!("puzzle unlocked={unlocked}; inventory={inventory:?}");}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Combining input, validation, state changes, and output in one oversized function.
2. Using numeric indexes without checking bounds.
3. Making prompts depend on color, animation, or cursor position.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical to-do and capstone record fields and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (text adventure: inventory and puzzles); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain text adventure: inventory and puzzles using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
- [The Rust Programming Language: Vectors](https://doc.rust-lang.org/book/ch08-01-vectors.html)
- [The Rust Programming Language: References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 10.3: Building a Text-Based Adventure Game (Part 2)

### Learning Objectives
- Keep items in rooms and in an inventory.
- Implement take and use commands.
- Block and then allow a move through a locked door.

### Concept Explanation

Part 2 adds *state*: items in rooms, an inventory, and a door that is locked until the player uses the key. This is the shared specification used by every language track: three rooms (`start`, `locked_door_room`, `treasure_room`); the commands `north`, `south`, `east`, `west`, `take shiny key`, `use shiny key`, and `quit`; the door between the chamber and the treasure room stays locked until the key is used there; reaching the treasure room ends the game.

Items are a `Vec` of names inside each room. Taking an item removes it from the room's list with `get_mut` (a mutable borrow) and adds it to the inventory. The borrow checker needs the immutable borrow of the room to end before the mutable one begins, which is why each command reads what it needs first. The locked door is a `bool` variable.

The example is played with: north (into the chamber), north (the locked door refuses), south, take shiny key, north, use shiny key, north (the treasure room).

### Worked Example

```rust
use std::collections::HashMap;
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
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    let mut rooms: HashMap<&str, Room> = HashMap::new();
    rooms.insert("start", Room {
        description: "A dark cave.",
        exits: HashMap::from([("north", "locked_door_room")]),
        items: vec!["shiny key"],
    });
    rooms.insert("locked_door_room", Room {
        description: "A small chamber with a heavy door to the NORTH.",
        exits: HashMap::from([("south", "start"), ("north", "treasure_room")]),
        items: Vec::new(),
    });
    rooms.insert("treasure_room", Room {
        description: "A glittering room full of treasure. You win!",
        exits: HashMap::from([("south", "locked_door_room")]),
        items: Vec::new(),
    });

    let mut current = "start";
    let mut inventory: Vec<&str> = Vec::new();
    let mut door_locked = true;

    loop {
        println!();
        println!("{}", rooms[current].description);
        if current == "treasure_room" {
            break;
        }
        if !rooms[current].items.is_empty() {
            println!("You see: {}", rooms[current].items.join(", "));
        }
        let held = if inventory.is_empty() { "empty".to_string() } else { inventory.join(", ") };
        println!("Your inventory: {held}");
        println!("What do you want to do?");

        let command = next_line().unwrap_or_else(|| "quit".to_string()).to_lowercase();
        let has_key_here = rooms[current].items.contains(&"shiny key");
        let next_room = rooms[current].exits.get(command.as_str()).copied();

        if command == "take shiny key" && has_key_here {
            if let Some(room) = rooms.get_mut(current) {
                room.items.retain(|&item| item != "shiny key");
            }
            inventory.push("shiny key");
            println!("You picked up the shiny key.");
        } else if command == "use shiny key" && current == "locked_door_room" && inventory.contains(&"shiny key") {
            door_locked = false;
            println!("You unlocked the door!");
        } else if let Some(next) = next_room {
            if current == "locked_door_room" && command == "north" && door_locked {
                println!("The door is locked! You need a key.");
            } else {
                current = next;
            }
        } else if command == "quit" {
            println!("Exiting game. Goodbye!");
            break;
        } else {
            println!("I don't understand that command.");
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
north
north
south
take shiny key
north
use shiny key
north
```

the program prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?
The door is locked! You need a key.

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?
You picked up the shiny key.

A dark cave.
Your inventory: shiny key
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?
You unlocked the door!

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?

A glittering room full of treasure. You win!
```

With no standard input at all, the program ends cleanly and prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Making the door's locked state part of the exits so that the "locked" message can never be reached.
2. Holding a reference to a room while calling `get_mut`, which the borrow checker rejects; read what you need first.
3. Printing a fixed room description that still mentions an item after the player has taken it.

### Activities
1. Play the program with the shown commands and follow each turn on paper.
2. Try `use shiny key` in the cave and describe what happens.
3. Add a second item and require both to open the door.
4. List the game's state (location, inventory, door) and say which command changes each part.

### Accessibility Practice

The room description never mentions the key. A separate 'You see:' line lists items, so the description stays true after the key is taken and the screen reader announces the current state.

### Skills Checklist
- [ ] I can store items in rooms and an inventory.
- [ ] I can implement take and use commands.
- [ ] I can block and allow a move.
- [ ] I can explain the borrow-checker constraint.
- [ ] I can keep descriptions true after state changes.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 10.4: Command-line to-do manager

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Command-line to-do manager using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Build an application in vertical slices: requirements, state model, command handling, validation, and accessible output. Separate domain logic from terminal interaction so it can be tested without simulating a user. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
struct Task{id:u32,title:String,done:bool}fn main(){let mut tasks=vec![Task{id:1,title:"Read lesson".into(),done:false}];tasks.push(Task{id:2,title:"Run example".into(),done:false});tasks[0].done=true;for t in &tasks{println!("{}: {} [{}]",t.id,t.title,if t.done{"done"}else{"open"});}}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Combining input, validation, state changes, and output in one oversized function.
2. Using numeric indexes without checking bounds.
3. Making prompts depend on color, animation, or cursor position.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical to-do and capstone record fields and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (command-line to-do manager); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain command-line to-do manager using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
- [The Rust Programming Language: Recoverable Errors with Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [The Rust Programming Language: Reading a File](https://doc.rust-lang.org/book/ch12-02-reading-a-file.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 10.4: Building a Command-Line To-Do List

### Learning Objectives
- Keep records with the shared fields.
- Save and load them as JSON.
- Offer add, view, mark-done, save, load, and quit commands.

### Concept Explanation

A to-do list ties together records, loops, functions, and files. Each task is a struct with the shared fields `id`, `title`, `description`, `done`, and `created_at`. The program keeps a `Vec<Task>` in memory, shows a numbered menu, and saves the list to `todos.json` when asked and on exit.

Saving uses the teaching JSON helper from Lesson 8.5, included here so the example runs on its own. Each task is converted to a `Json::Object` for saving and rebuilt from one when loading, and the conversion refuses a record with a missing field. At start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program. The timestamp is computed from the system clock in UTC with a short date algorithm, because the standard library has no date formatting.

In the sample session the user adds two tasks, views the list, marks task 2 done, views it again, tries an invalid menu choice, views the list, and quits.

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
    format!("{year:04}-{month:02}-{day:02}T{:02}:{:02}:{:02}", rest / 3600, rest % 3600 / 60, rest % 60)
}

fn to_json(task: &Task) -> Json {
    let mut map = BTreeMap::new();
    map.insert("id".to_string(), Json::Int(task.id));
    map.insert("title".to_string(), Json::Str(task.title.clone()));
    map.insert("description".to_string(), Json::Str(task.description.clone()));
    map.insert("done".to_string(), Json::Bool(task.done));
    map.insert("created_at".to_string(), Json::Str(task.created_at.clone()));
    Json::Object(map)
}

fn text_field(map: &BTreeMap<String, Json>, key: &str) -> Result<String, String> {
    match map.get(key) {
        Some(Json::Str(text)) => Ok(text.clone()),
        _ => Err(format!("missing field {key}")),
    }
}

fn from_json(value: &Json) -> Result<Task, String> {
    let Json::Object(map) = value else {
        return Err("a task must be an object".to_string());
    };
    let id = match map.get("id") {
        Some(Json::Int(number)) => *number,
        _ => return Err("missing field id".to_string()),
    };
    Ok(Task {
        id,
        title: text_field(map, "title")?,
        description: text_field(map, "description")?,
        done: map.get("done") == Some(&Json::Bool(true)),
        created_at: text_field(map, "created_at")?,
    })
}

fn load_todos() -> Vec<Task> {
    let text = match fs::read_to_string("todos.json") {
        Ok(text) => text,
        Err(_) => {
            println!("No existing tasks found.");
            return Vec::new();
        }
    };
    let loaded = match decode(&text) {
        Ok(Json::List(items)) => items.iter().map(from_json).collect::<Result<Vec<Task>, String>>(),
        Ok(_) => Err("expected a list".to_string()),
        Err(message) => Err(message),
    };
    match loaded {
        Ok(tasks) => {
            println!("Tasks loaded.");
            tasks
        }
        Err(_) => {
            println!("Error: todos.json is not valid JSON. Starting with an empty list.");
            Vec::new()
        }
    }
}

fn save_todos(todos: &[Task]) -> io::Result<()> {
    let list = Json::List(todos.iter().map(to_json).collect());
    fs::write("todos.json", encode(&list))?;
    println!("Tasks saved.");
    Ok(())
}

fn add_task(todos: &mut Vec<Task>, title: &str, description: &str) {
    if title.trim().is_empty() {
        println!("A title is required.");
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
    println!("Task '{}' added.", title.trim());
}

fn view_tasks(todos: &[Task]) {
    if todos.is_empty() {
        println!("No tasks in your list.");
        return;
    }
    println!("--- Your To-Do List ---");
    for task in todos {
        let status = if task.done { "done" } else { "not done" };
        println!("{}. {} ({})", task.id, task.title, status);
    }
    println!("-----------------------");
}

fn mark_done(todos: &mut [Task], text: &str) {
    let Ok(id) = text.trim().parse::<i64>() else {
        println!("Please enter a whole number.");
        return;
    };
    match todos.iter_mut().find(|task| task.id == id) {
        Some(task) => {
            task.done = true;
            println!("Task '{}' marked as done.", task.title);
        }
        None => println!("No task has that number."),
    }
}

fn show_menu() {
    println!();
    println!("--- To-Do List Menu ---");
    println!("1. Add Task");
    println!("2. View Tasks");
    println!("3. Mark Task Done");
    println!("4. Save Tasks");
    println!("5. Load Tasks");
    println!("6. Quit");
    println!("-----------------------");
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
        println!("Enter your choice (1-6):");
        let choice = next_line().unwrap_or_else(|| "6".to_string());
        match choice.as_str() {
            "1" => {
                println!("Enter task title:");
                let title = next_line().unwrap_or_default();
                println!("Enter task description:");
                let description = next_line().unwrap_or_default();
                add_task(&mut todos, &title, &description);
            }
            "2" => view_tasks(&todos),
            "3" => {
                view_tasks(&todos);
                println!("Enter task number to mark done:");
                let text = next_line().unwrap_or_default();
                mark_done(&mut todos, &text);
            }
            "4" => save_todos(&todos)?,
            "5" => todos = load_todos(),
            "6" => {
                save_todos(&todos)?;
                println!("Goodbye!");
                return Ok(());
            }
            _ => println!("Invalid choice. Please try again."),
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
1
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
```

the program prints:
```text
No existing tasks found.

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
```

With no standard input at all, the program ends cleanly and prints:
```text
No existing tasks found.

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
```

### Common Mistakes
1. Saving the file but never loading it, so tasks disappear between runs.
2. Reusing a deleted task's id, which can confuse saved references.
3. Letting a damaged `todos.json` crash the program instead of printing a message.

### Activities
1. Run the sample session, then run the program again typing `2` and `6` to see the saved tasks.
2. Add a command to delete a task by number.
3. Open `todos.json` and read the saved text. Edit it to remove a bracket and run the program again.
4. Show each task's description in the view command.

### Accessibility Practice

Every menu is printed as numbered lines and every prompt is on its own line. The status words are `done` and `not done`, not symbols, so the list reads clearly in speech and braille.

### Skills Checklist
- [ ] I can keep records with the shared fields.
- [ ] I can save and load JSON.
- [ ] I handle a missing or damaged file.
- [ ] I keep ids unique.
- [ ] I show status in words.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 10.5: Accessible interaction and validation

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Accessible interaction and validation using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Build an application in vertical slices: requirements, state model, command handling, validation, and accessible output. Separate domain logic from terminal interaction so it can be tested without simulating a user. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
use std::io::{self,Write};fn main(){print!("Task title: ");io::stdout().flush().unwrap();let mut s=String::new();io::stdin().read_line(&mut s).unwrap();let s=s.trim();if s.is_empty(){println!("A title is required.");}else{println!("Accepted task: {s}");}}
```

**Expected behavior:** Accepts a nonempty task title and rejects blank input.

### Common Mistakes
1. Combining input, validation, state changes, and output in one oversized function.
2. Using numeric indexes without checking bounds.
3. Making prompts depend on color, animation, or cursor position.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical to-do and capstone record fields and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (accessible interaction and validation); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain accessible interaction and validation using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
- [The Rust Programming Language: Recoverable Errors with Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [The Rust Programming Language: Option](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 10.5: Refining User Experience and Validation

### Learning Objectives
- Write reusable validation functions.
- Limit retries and handle the end of input.
- Write clear, accessible messages.

### Concept Explanation

Reusable validation functions make every menu and form consistent. `ask_number(prompt, low, high, attempts)` prints a prompt, reads a line, converts it, checks the range, and either returns `Some(number)` or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns `None`. `ask_yes_no(prompt)` returns `Option<bool>` and accepts `y`, `yes`, `n`, and `no` in any letter case. The `Option` return type makes the caller deal with the failure case.

Good messages say *what was wrong* and *what to do*: "Enter a whole number from 0 to 100," not "Invalid." They never depend on color, position, or symbols alone, and they use the same wording every time.

The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y.

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

fn ask_number(prompt: &str, low: i32, high: i32, attempts: u32) -> Option<i32> {
    for attempt in 1..=attempts {
        println!("{prompt}");
        let text = next_line()?;
        if let Ok(number) = text.parse::<i32>() {
            if (low..=high).contains(&number) {
                return Some(number);
            }
        }
        println!("Enter a whole number from {low} to {high}. You have {} attempt(s) left.", attempts - attempt);
    }
    None
}

fn ask_yes_no(prompt: &str) -> Option<bool> {
    loop {
        println!("{prompt} (yes or no)");
        let text = next_line()?.to_lowercase();
        match text.as_str() {
            "y" | "yes" => return Some(true),
            "n" | "no" => return Some(false),
            _ => println!("Please answer yes or no."),
        }
    }
}

fn main() {
    match ask_number("Enter a score from 0 to 100:", 0, 100, 3) {
        Some(score) => println!("Accepted score: {score}"),
        None => println!("No valid score was entered."),
    }

    let keep = ask_yes_no("Save this score?");
    println!("Save answer: {:?}", keep);
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
abc
105
88
maybe
y
```

the program prints:
```text
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 2 attempt(s) left.
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 1 attempt(s) left.
Enter a score from 0 to 100:
Accepted score: 88
Save this score? (yes or no)
Please answer yes or no.
Save this score? (yes or no)
Save answer: Some(true)
```

With no standard input at all, the program ends cleanly and prints:
```text
Enter a score from 0 to 100:
No valid score was entered.
Save this score? (yes or no)
Save answer: None
```

### Common Mistakes
1. Writing the message "Invalid" without saying what is valid.
2. Accepting a decimal such as 88.5 for a field that requires a whole number.
3. Looping forever on bad input instead of limiting attempts.

### Activities
1. Run the sample input and read each message aloud.
2. Run with three invalid numbers and read the final message.
3. Add `ask_text(prompt) -> Option<String>` that rejects empty answers.
4. Rewrite two messages from earlier lessons so they say what to do next.

### Accessibility Practice

Check that every error message ends with an action the user can take, and that the same situation always produces the same words.

### Skills Checklist
- [ ] I can write reusable validation functions.
- [ ] I limit retries.
- [ ] I handle the end of input.
- [ ] I write messages that say what to do.
- [ ] I keep wording consistent.

---
>>>>>>> 2067a20 (curriculum clearning and updates)
