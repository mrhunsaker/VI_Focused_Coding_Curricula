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

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: rooms and movement using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Projects begin with requirements and acceptance criteria. Implement a text-based adventure and todo manager using explicit state, validated commands, and predictable output. Accessible interaction uses keyboard-operable text prompts and readable error messages.

**Lesson focus:** Text adventure: rooms and movement. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let exits = ["start_room": ["north": "tunnel"], "tunnel": ["south": "start_room"]]
let currentRoom = "start_room"
let direction = "north"
if let destination = exits[currentRoom]?[direction] {
    print("You move to the \(destination).")
} else {
    print("There is no exit that way.")
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
- [ ] I can explain text adventure: rooms and movement in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: inventory and puzzles using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Projects begin with requirements and acceptance criteria. Implement a text-based adventure and todo manager using explicit state, validated commands, and predictable output. Accessible interaction uses keyboard-operable text prompts and readable error messages.

**Lesson focus:** Text adventure: inventory and puzzles. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
var inventory: Set<String> = ["shiny key", "map"]
let requiredItem = "shiny key"
if inventory.contains(requiredItem) {
    print("The cabinet unlocks.")
    inventory.remove(requiredItem)
} else {
    print("You need a key.")
}
print("Inventory: \(inventory.sorted())")
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
- [ ] I can explain text adventure: inventory and puzzles in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

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
