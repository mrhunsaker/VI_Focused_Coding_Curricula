# Unit 10: Project-Based Learning

## Overview

Projects begin with requirements and acceptance criteria. Implement a text-based adventure and todo manager using explicit state, validated commands, and predictable output. Accessible interaction uses keyboard-operable text prompts and readable error messages.

## Lesson 10.1: Requirements and top-down design

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and top-down design using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Projects begin with requirements and acceptance criteria. Implement a text-based adventure and todo manager using explicit state, validated commands, and predictable output. Accessible interaction uses keyboard-operable text prompts and readable error messages.

**Lesson focus:** Requirements and top-down design. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let requirements = [
    "List current records",
    "Add a record with a unique identifier",
    "Search by title",
    "Update completion state",
    "Reject blank titles"
]
for (number, requirement) in requirements.enumerated() {
    print("\(number + 1). \(requirement)")
}
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Write acceptance criteria before implementing project features.
- Reject invalid directions and unknown commands explicitly.
- Do not make interaction depend on color, animation, or mouse-only controls.

### Activities
1. Translate project requirements into acceptance tests.
2. Test valid room movement and unavailable exits.
3. Test inventory puzzles with and without required items.
4. Exercise todo list, add, completion, and invalid-title workflows.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain requirements and top-down design in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 10.2: Text adventure: five rooms and movement

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Dictionary](https://developer.apple.com/documentation/swift/dictionary)
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Represent all five canonical rooms and exits with Swift dictionaries and structs.
- Validate movement before changing the current room.
- Explain why treasure_room is not reachable until the key puzzle is implemented.

### Concept Explanation

The shared graph has five rooms: start_room, tunnel, clearing, locked_door_room, and treasure_room. A Room value stores a description and its exits. The player begins in start_room. Part 1 leaves the north exit from locked_door_room unavailable. Optional dictionary lookup makes a missing direction explicit, so invalid movement cannot change state.

### Worked Example

```swift
import Foundation

struct Room {
    let description: String
    let exits: [String: String]
}

let rooms: [String: Room] = [
    "start_room": Room(description: "A dimly lit cave. A narrow passage leads north.", exits: ["north": "tunnel"]),
    "tunnel": Room(description: "A damp tunnel. Passages lead south and east.", exits: ["south": "start_room", "east": "clearing"]),
    "clearing": Room(description: "A quiet clearing. An antechamber lies to the north.", exits: ["west": "tunnel", "north": "locked_door_room"]),
    "locked_door_room": Room(description: "A chamber with a heavy door to the north.", exits: ["south": "clearing"]),
    "treasure_room": Room(description: "You found the treasure. You win!", exits: [:])
]

var currentRoom = "start_room"
while true {
    let room = rooms[currentRoom]!
    print("---")
    print(room.description)
    print("What do you want to do?")
    let command = readLine()?.trimmingCharacters(in: .whitespacesAndNewlines).lowercased() ?? "quit"
    if command == "quit" {
        print("Exiting game. Goodbye!")
        break
    }
    if let destination = room.exits[command] {
        currentRoom = destination
    } else {
        print("You cannot go that way. Enter a listed direction or quit.")
    }
}
```

### Expected Behavior or Output

Enter north, east, north, north, quit. The player reaches tunnel, clearing, and locked_door_room. The second north is rejected and the current room does not change. The treasure room exists but has no incoming exit in Part 1.

### Common Mistakes
- Force-unwrapping a direction lookup that may be nil.
- Updating currentRoom before validating the exit.
- Defining a destination that is not one of the five room identifiers.
- Adding the treasure exit before implementing the key puzzle.

### Activities
1. Trace north, east, north, north and record the current room.
2. Try west from start_room and verify that the room does not change.
3. Check every exit destination against the room dictionary.
4. Explain why treasure_room cannot yet be reached.

### Accessibility Practice

Announce the room description and prompt in a consistent order. The invalid-movement response explains what happened and how to continue. Run from the terminal and inspect output sequentially with the learner's access technology.

### Skills Checklist
- [ ] I can model all five canonical rooms.
- [ ] I can represent exits with dictionaries.
- [ ] I can reject invalid movement without changing state.
- [ ] I can explain why the treasure room is not yet reachable.

---

## Lesson 10.3: Text adventure: shiny key and locked door

### Reading References
- [The Swift Programming Language: Collections](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/collection/)
- [Swift Array](https://developer.apple.com/documentation/swift/array)
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Place the shiny key in start_room and transfer it to inventory exactly once.
- Require key use in locked_door_room.
- Unlock the north exit only after the puzzle succeeds.
- End the game when the player reaches treasure_room.

### Concept Explanation

Keep the same five-room graph. Each Room reference stores a mutable item array and exit dictionary. Picking up the shiny key removes it from start_room and adds it to inventory. Using the key succeeds only in locked_door_room when inventory contains it. The north exit remains blocked until the key is used.

### Worked Example

```swift
import Foundation

final class Room {
    let description: String
    var exits: [String: String]
    var items: [String]

    init(_ description: String, exits: [String: String], items: [String] = []) {
        self.description = description
        self.exits = exits
        self.items = items
    }
}

let rooms: [String: Room] = [
    "start_room": Room("A dimly lit cave.", exits: ["north": "tunnel"], items: ["shiny key"]),
    "tunnel": Room("A damp tunnel. Passages lead south and east.", exits: ["south": "start_room", "east": "clearing"]),
    "clearing": Room("A quiet clearing. An antechamber lies to the north.", exits: ["west": "tunnel", "north": "locked_door_room"]),
    "locked_door_room": Room("A chamber with a heavy door to the north.", exits: ["south": "clearing", "north": "treasure_room"]),
    "treasure_room": Room("You found the treasure. You win!", exits: [:])
]

var currentRoom = "start_room"
var inventory: [String] = []
var doorLocked = true

while true {
    let room = rooms[currentRoom]!
    print()
    print(room.description)
    if currentRoom == "treasure_room" { break }
    if !room.items.isEmpty { print("You see: " + room.items.joined(separator: ", ")) }
    print("Your inventory: " + (inventory.isEmpty ? "empty" : inventory.joined(separator: ", ")))
    print("What do you want to do?")
    let command = readLine()?.trimmingCharacters(in: .whitespacesAndNewlines).lowercased() ?? "quit"

    if command == "quit" {
        print("You quit the adventure.")
        break
    } else if command == "take shiny key" {
        if let index = room.items.firstIndex(of: "shiny key") {
            room.items.remove(at: index)
            inventory.append("shiny key")
            print("You picked up the shiny key.")
        } else {
            print("There is no shiny key here to take.")
        }
    } else if command == "use shiny key" {
        if currentRoom != "locked_door_room" {
            print("You must be at the locked door to use the key.")
        } else if !inventory.contains("shiny key") {
            print("You do not have the shiny key.")
        } else {
            doorLocked = false
            print("You unlocked the door!")
        }
    } else if currentRoom == "locked_door_room" && command == "north" && doorLocked {
        print("The door is locked! You need to use the shiny key here.")
    } else if let destination = room.exits[command] {
        currentRoom = destination
    } else {
        print("Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.")
    }
}
```

### Expected Behavior or Output

Enter north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north. The first north from locked_door_room is rejected. Taking the key removes it from the room and adds it to inventory. Using it outside locked_door_room is rejected. Using it there unlocks the door; the final north reaches treasure_room and prints the win description.

### Common Mistakes
- Removing the key from the room without adding it to inventory.
- Unlocking the door outside locked_door_room.
- Unlocking the door without checking inventory.
- Allowing north movement before doorLocked becomes false.
- Treating an invalid optional lookup as a destination.

### Activities
1. Run the complete puzzle sequence and record room, items, inventory, and door state.
2. Attempt to take the key twice; the second attempt must be rejected.
3. Try to use the key outside locked_door_room.
4. Try north before and after unlocking.
5. Add a help command listing every supported command.

### Accessibility Practice

Announce the room, visible items, inventory, and prompt as separate text lines. Error messages explain the failed action. Test the complete interaction with keyboard-only input and sequential screen-reader output.

### Skills Checklist
- [ ] I can model the five canonical rooms.
- [ ] I can transfer the key from a room to inventory.
- [ ] I can prevent duplicate pickup.
- [ ] I can require key use in locked_door_room.
- [ ] I can block and unlock the north exit.
- [ ] I can end the game in treasure_room.

---

## Lesson 10.4: Command-line to-do manager

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain command-line to-do manager using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Projects begin with requirements and acceptance criteria. Implement a text-based adventure and todo manager using explicit state, validated commands, and predictable output. Accessible interaction uses keyboard-operable text prompts and readable error messages.

**Lesson focus:** Command-line to-do manager. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
struct Todo: Identifiable {
    let id: Int
    var title: String
    var isComplete: Bool
}
var tasks = [Todo(id: 1, title: "Read lesson", isComplete: false)]
tasks.append(Todo(id: 2, title: "Run examples", isComplete: true))
for task in tasks {
    print("[\(task.isComplete ? "x" : " ")] \(task.id): \(task.title)")
}
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Write acceptance criteria before implementing project features.
- Reject invalid directions and unknown commands explicitly.
- Do not make interaction depend on color, animation, or mouse-only controls.

### Activities
1. Translate project requirements into acceptance tests.
2. Test valid room movement and unavailable exits.
3. Test inventory puzzles with and without required items.
4. Exercise todo list, add, completion, and invalid-title workflows.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain command-line to-do manager in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 10.5: Accessible interaction and validation

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain accessible interaction and validation using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Projects begin with requirements and acceptance criteria. Implement a text-based adventure and todo manager using explicit state, validated commands, and predictable output. Accessible interaction uses keyboard-operable text prompts and readable error messages.

**Lesson focus:** Accessible interaction and validation. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
enum TitleError: Error { case blank }
import Foundation
func cleanTitle(_ raw: String) -> Result<String, TitleError> {
    let title = raw.trimmingCharacters(in: .whitespacesAndNewlines)
    return title.isEmpty ? .failure(.blank) : .success(title)
}
for raw in ["  Study Swift  ", "   "] {
    switch cleanTitle(raw) {
    case .success(let title): print("Accepted: \(title)")
    case .failure: print("Error: title cannot be blank")
    }
}
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Write acceptance criteria before implementing project features.
- Reject invalid directions and unknown commands explicitly.
- Do not make interaction depend on color, animation, or mouse-only controls.

### Activities
1. Translate project requirements into acceptance tests.
2. Test valid room movement and unavailable exits.
3. Test inventory puzzles with and without required items.
4. Exercise todo list, add, completion, and invalid-title workflows.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain accessible interaction and validation in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
