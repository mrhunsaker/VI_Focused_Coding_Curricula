[Header 2 ("unit-10-project-based-learning", [], []) [Str "Unit 10: Project-Based Learning"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Projects begin with requirements and acceptance criteria. Implement a text-based adventure and todo manager using explicit state, validated commands, and predictable output. Accessible interaction uses keyboard-operable text prompts and readable error messages."], Header 3 ("lesson-101-requirements-and-top-down-design", ["unnumbered", "unlisted"], []) [Str "Lesson 10.1: Requirements and top-down design"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Swift Programming Language"] ("https://docs.swift.org/swift-book/documentation/the-swift-programming-language/", "")]], [Plain [Link ("", [], []) [Str "Swift Standard Library"] ("https://developer.apple.com/documentation/swift/swift-standard-library", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain requirements and top-down design using Swift terminology."]], [Plain [Str "Apply the relevant language and standard-library features correctly."]], [Plain [Str "Test normal, boundary, and invalid cases using the shared course data."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Projects begin with requirements and acceptance criteria. Implement a text-based adventure and todo manager using explicit state, validated commands, and predictable output. Accessible interaction uses keyboard-operable text prompts and readable error messages."], Para [Strong [Str "Lesson focus:"], Str " Requirements and top-down design. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["swift"], []) "let requirements = [
    \"List current records\",
    \"Add a record with a unique identifier\",
    \"Search by title\",
    \"Update completion state\",
    \"Reject blank titles\"
]
for (number, requirement) in requirements.enumerated() {
    print(\"\\(number + 1). \\(requirement)\")
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths."], Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Write acceptance criteria before implementing project features."]], [Plain [Str "Reject invalid directions and unknown commands explicitly."]], [Plain [Str "Do not make interaction depend on color, animation, or mouse-only controls."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Translate project requirements into acceptance tests."]], [Plain [Str "Test valid room movement and unavailable exits."]], [Plain [Str "Test inventory puzzles with and without required items."]], [Plain [Str "Exercise todo list, add, completion, and invalid-title workflows."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain requirements and top-down design in Swift terminology."]], [Plain [Str "\9744", Space, Str "I can trace the example and predict its behavior."]], [Plain [Str "\9744", Space, Str "I can adapt the example to the shared canonical data."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Swift-specific error or edge case."]], [Plain [Str "\9744", Space, Str "I can run and inspect the program using keyboard-accessible tools."]]], Header 3 ("lesson-102-text-adventure-five-rooms-and-movement", ["unnumbered", "unlisted"], []) [Str "Lesson 10.2: Text adventure: five rooms and movement"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Swift Programming Language"] ("https://docs.swift.org/swift-book/documentation/the-swift-programming-language/", "")]], [Plain [Link ("", [], []) [Str "Swift Dictionary"] ("https://developer.apple.com/documentation/swift/dictionary", "")]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Represent all five canonical rooms and exits with Swift dictionaries and structs."]], [Plain [Str "Validate movement before changing the current room."]], [Plain [Str "Explain why treasure_room is not reachable until the key puzzle is implemented."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The shared graph has five rooms: start_room, tunnel, clearing, locked_door_room, and treasure_room. A Room value stores a description and its exits. The player begins in start_room. Part 1 leaves the north exit from locked_door_room unavailable. Optional dictionary lookup makes a missing direction explicit, so invalid movement cannot change state."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["swift"], []) "import Foundation

struct Room {
    let description: String
    let exits: [String: String]
}

let rooms: [String: Room] = [
    \"start_room\": Room(description: \"A dimly lit cave. A narrow passage leads north.\", exits: [\"north\": \"tunnel\"]),
    \"tunnel\": Room(description: \"A damp tunnel. Passages lead south and east.\", exits: [\"south\": \"start_room\", \"east\": \"clearing\"]),
    \"clearing\": Room(description: \"A quiet clearing. An antechamber lies to the north.\", exits: [\"west\": \"tunnel\", \"north\": \"locked_door_room\"]),
    \"locked_door_room\": Room(description: \"A chamber with a heavy door to the north.\", exits: [\"south\": \"clearing\"]),
    \"treasure_room\": Room(description: \"You found the treasure. You win!\", exits: [:])
]

var currentRoom = \"start_room\"
while true {
    let room = rooms[currentRoom]!
    print(\"---\")
    print(room.description)
    print(\"What do you want to do?\")
    let command = readLine()?.trimmingCharacters(in: .whitespacesAndNewlines).lowercased() ?? \"quit\"
    if command == \"quit\" {
        print(\"Exiting game. Goodbye!\")
        break
    }
    if let destination = room.exits[command] {
        currentRoom = destination
    } else {
        print(\"You cannot go that way. Enter a listed direction or quit.\")
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Enter north, east, north, north, quit. The player reaches tunnel, clearing, and locked_door_room. The second north is rejected and the current room does not change. The treasure room exists but has no incoming exit in Part 1."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Force-unwrapping a direction lookup that may be nil."]], [Plain [Str "Updating currentRoom before validating the exit."]], [Plain [Str "Defining a destination that is not one of the five room identifiers."]], [Plain [Str "Adding the treasure exit before implementing the key puzzle."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace north, east, north, north and record the current room."]], [Plain [Str "Try west from start_room and verify that the room does not change."]], [Plain [Str "Check every exit destination against the room dictionary."]], [Plain [Str "Explain why treasure_room cannot yet be reached."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Announce the room description and prompt in a consistent order. The invalid-movement response explains what happened and how to continue. Run from the terminal and inspect output sequentially with the learner's access technology."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model all five canonical rooms."]], [Plain [Str "\9744", Space, Str "I can represent exits with dictionaries."]], [Plain [Str "\9744", Space, Str "I can reject invalid movement without changing state."]], [Plain [Str "\9744", Space, Str "I can explain why the treasure room is not yet reachable."]]], HorizontalRule, Header 3 ("lesson-103-text-adventure-shiny-key-and-locked-door", ["unnumbered", "unlisted"], []) [Str "Lesson 10.3: Text adventure: shiny key and locked door"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Swift Programming Language: Collections"] ("https://docs.swift.org/swift-book/documentation/the-swift-programming-language/collection/", "")]], [Plain [Link ("", [], []) [Str "Swift Array"] ("https://developer.apple.com/documentation/swift/array", "")]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Place the shiny key in start_room and transfer it to inventory exactly once."]], [Plain [Str "Require key use in locked_door_room."]], [Plain [Str "Unlock the north exit only after the puzzle succeeds."]], [Plain [Str "End the game when the player reaches treasure_room."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Keep the same five-room graph. Each Room reference stores a mutable item array and exit dictionary. Picking up the shiny key removes it from start_room and adds it to inventory. Using the key succeeds only in locked_door_room when inventory contains it. The north exit remains blocked until the key is used."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["swift"], []) "import Foundation

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
    \"start_room\": Room(\"A dimly lit cave.\", exits: [\"north\": \"tunnel\"], items: [\"shiny key\"]),
    \"tunnel\": Room(\"A damp tunnel. Passages lead south and east.\", exits: [\"south\": \"start_room\", \"east\": \"clearing\"]),
    \"clearing\": Room(\"A quiet clearing. An antechamber lies to the north.\", exits: [\"west\": \"tunnel\", \"north\": \"locked_door_room\"]),
    \"locked_door_room\": Room(\"A chamber with a heavy door to the north.\", exits: [\"south\": \"clearing\", \"north\": \"treasure_room\"]),
    \"treasure_room\": Room(\"You found the treasure. You win!\", exits: [:])
]

var currentRoom = \"start_room\"
var inventory: [String] = []
var doorLocked = true

while true {
    let room = rooms[currentRoom]!
    print()
    print(room.description)
    if currentRoom == \"treasure_room\" { break }
    if !room.items.isEmpty { print(\"You see: \" + room.items.joined(separator: \", \")) }
    print(\"Your inventory: \" + (inventory.isEmpty ? \"empty\" : inventory.joined(separator: \", \")))
    print(\"What do you want to do?\")
    let command = readLine()?.trimmingCharacters(in: .whitespacesAndNewlines).lowercased() ?? \"quit\"

    if command == \"quit\" {
        print(\"You quit the adventure.\")
        break
    } else if command == \"take shiny key\" {
        if let index = room.items.firstIndex(of: \"shiny key\") {
            room.items.remove(at: index)
            inventory.append(\"shiny key\")
            print(\"You picked up the shiny key.\")
        } else {
            print(\"There is no shiny key here to take.\")
        }
    } else if command == \"use shiny key\" {
        if currentRoom != \"locked_door_room\" {
            print(\"You must be at the locked door to use the key.\")
        } else if !inventory.contains(\"shiny key\") {
            print(\"You do not have the shiny key.\")
        } else {
            doorLocked = false
            print(\"You unlocked the door!\")
        }
    } else if currentRoom == \"locked_door_room\" && command == \"north\" && doorLocked {
        print(\"The door is locked! You need to use the shiny key here.\")
    } else if let destination = room.exits[command] {
        currentRoom = destination
    } else {
        print(\"Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.\")
    }
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Enter north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north. The first north from locked_door_room is rejected. Taking the key removes it from the room and adds it to inventory. Using it outside locked_door_room is rejected. Using it there unlocks the door; the final north reaches treasure_room and prints the win description."], Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Removing the key from the room without adding it to inventory."]], [Plain [Str "Unlocking the door outside locked_door_room."]], [Plain [Str "Unlocking the door without checking inventory."]], [Plain [Str "Allowing north movement before doorLocked becomes false."]], [Plain [Str "Treating an invalid optional lookup as a destination."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the complete puzzle sequence and record room, items, inventory, and door state."]], [Plain [Str "Attempt to take the key twice; the second attempt must be rejected."]], [Plain [Str "Try to use the key outside locked_door_room."]], [Plain [Str "Try north before and after unlocking."]], [Plain [Str "Add a help command listing every supported command."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Announce the room, visible items, inventory, and prompt as separate text lines. Error messages explain the failed action. Test the complete interaction with keyboard-only input and sequential screen-reader output."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model the five canonical rooms."]], [Plain [Str "\9744", Space, Str "I can transfer the key from a room to inventory."]], [Plain [Str "\9744", Space, Str "I can prevent duplicate pickup."]], [Plain [Str "\9744", Space, Str "I can require key use in locked_door_room."]], [Plain [Str "\9744", Space, Str "I can block and unlock the north exit."]], [Plain [Str "\9744", Space, Str "I can end the game in treasure_room."]]], HorizontalRule, Header 3 ("lesson-104-command-line-to-do-manager", ["unnumbered", "unlisted"], []) [Str "Lesson 10.4: Command-line to-do manager"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Swift Programming Language"] ("https://docs.swift.org/swift-book/documentation/the-swift-programming-language/", "")]], [Plain [Link ("", [], []) [Str "Swift Standard Library"] ("https://developer.apple.com/documentation/swift/swift-standard-library", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain command-line to-do manager using Swift terminology."]], [Plain [Str "Apply the relevant language and standard-library features correctly."]], [Plain [Str "Test normal, boundary, and invalid cases using the shared course data."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Projects begin with requirements and acceptance criteria. Implement a text-based adventure and todo manager using explicit state, validated commands, and predictable output. Accessible interaction uses keyboard-operable text prompts and readable error messages."], Para [Strong [Str "Lesson focus:"], Str " Command-line to-do manager. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["swift"], []) "struct Todo: Identifiable {
    let id: Int
    var title: String
    var isComplete: Bool
}
var tasks = [Todo(id: 1, title: \"Read lesson\", isComplete: false)]
tasks.append(Todo(id: 2, title: \"Run examples\", isComplete: true))
for task in tasks {
    print(\"[\\(task.isComplete ? \"x\" : \" \")] \\(task.id): \\(task.title)\")
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths."], Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Write acceptance criteria before implementing project features."]], [Plain [Str "Reject invalid directions and unknown commands explicitly."]], [Plain [Str "Do not make interaction depend on color, animation, or mouse-only controls."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Translate project requirements into acceptance tests."]], [Plain [Str "Test valid room movement and unavailable exits."]], [Plain [Str "Test inventory puzzles with and without required items."]], [Plain [Str "Exercise todo list, add, completion, and invalid-title workflows."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain command-line to-do manager in Swift terminology."]], [Plain [Str "\9744", Space, Str "I can trace the example and predict its behavior."]], [Plain [Str "\9744", Space, Str "I can adapt the example to the shared canonical data."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Swift-specific error or edge case."]], [Plain [Str "\9744", Space, Str "I can run and inspect the program using keyboard-accessible tools."]]], Header 3 ("lesson-105-accessible-interaction-and-validation", ["unnumbered", "unlisted"], []) [Str "Lesson 10.5: Accessible interaction and validation"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Swift Programming Language"] ("https://docs.swift.org/swift-book/documentation/the-swift-programming-language/", "")]], [Plain [Link ("", [], []) [Str "Swift Standard Library"] ("https://developer.apple.com/documentation/swift/swift-standard-library", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain accessible interaction and validation using Swift terminology."]], [Plain [Str "Apply the relevant language and standard-library features correctly."]], [Plain [Str "Test normal, boundary, and invalid cases using the shared course data."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Projects begin with requirements and acceptance criteria. Implement a text-based adventure and todo manager using explicit state, validated commands, and predictable output. Accessible interaction uses keyboard-operable text prompts and readable error messages."], Para [Strong [Str "Lesson focus:"], Str " Accessible interaction and validation. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["swift"], []) "enum TitleError: Error { case blank }
import Foundation
func cleanTitle(_ raw: String) -> Result<String, TitleError> {
    let title = raw.trimmingCharacters(in: .whitespacesAndNewlines)
    return title.isEmpty ? .failure(.blank) : .success(title)
}
for raw in [\"  Study Swift  \", \"   \"] {
    switch cleanTitle(raw) {
    case .success(let title): print(\"Accepted: \\(title)\")
    case .failure: print(\"Error: title cannot be blank\")
    }
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths."], Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Write acceptance criteria before implementing project features."]], [Plain [Str "Reject invalid directions and unknown commands explicitly."]], [Plain [Str "Do not make interaction depend on color, animation, or mouse-only controls."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Translate project requirements into acceptance tests."]], [Plain [Str "Test valid room movement and unavailable exits."]], [Plain [Str "Test inventory puzzles with and without required items."]], [Plain [Str "Exercise todo list, add, completion, and invalid-title workflows."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain accessible interaction and validation in Swift terminology."]], [Plain [Str "\9744", Space, Str "I can trace the example and predict its behavior."]], [Plain [Str "\9744", Space, Str "I can adapt the example to the shared canonical data."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Swift-specific error or edge case."]], [Plain [Str "\9744", Space, Str "I can run and inspect the program using keyboard-accessible tools."]]]]