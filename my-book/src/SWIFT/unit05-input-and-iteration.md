# Unit 5: Input and Iteration

## Overview

Console input arrives as an optional string. Convert and validate it before use. `while`, `break`, and `continue` control repetition; a loop must make progress or reach an exit condition.

## Lesson 5.1: Input and validation

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain input and validation using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Console input arrives as an optional string. Convert and validate it before use. `while`, `break`, and `continue` control repetition; a loop must make progress or reach an exit condition.

**Lesson focus:** Input and validation. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
print("Enter a score from 0 to 100:")
let input = readLine() ?? ""
if let score = Int(input), (0...100).contains(score) {
    print("Accepted score: \(score)")
} else {
    print("Invalid score")
}
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- A `while` loop must change state or terminate explicitly.
- Use `break` to exit the intended loop and `continue` to skip only the current iteration.
- Validate text before converting it to a numeric value.

### Activities
1. Test valid, invalid, and blank user input.
2. Trace a sentinel loop with both quit and non-quit commands.
3. Find the first matching score and stop immediately.
4. Prove a loop terminates for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain input and validation in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.2: While loops and sentinel repetition

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain while loops and sentinel repetition using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Console input arrives as an optional string. Convert and validate it before use. `while`, `break`, and `continue` control repetition; a loop must make progress or reach an exit condition.

**Lesson focus:** While loops and sentinel repetition. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
var commands = ["list", "help", "quit"]
var position = 0
while position < commands.count {
    let command = commands[position]
    print("Command: \(command)")
    position += 1
    if command == "quit" { break }
}
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- A `while` loop must change state or terminate explicitly.
- Use `break` to exit the intended loop and `continue` to skip only the current iteration.
- Validate text before converting it to a numeric value.

### Activities
1. Test valid, invalid, and blank user input.
2. Trace a sentinel loop with both quit and non-quit commands.
3. Find the first matching score and stop immediately.
4. Prove a loop terminates for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain while loops and sentinel repetition in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.3: Flags and early exits

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain flags and early exits using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Console input arrives as an optional string. Convert and validate it before use. `while`, `break`, and `continue` control repetition; a loop must make progress or reach an exit condition.

**Lesson focus:** Flags and early exits. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let scores = [82, 91, 76, 88]
var foundIndex: Int? = nil
for (index, score) in scores.enumerated() {
    if score == 91 {
        foundIndex = index
        break
    }
}
print("91 found at index: \(foundIndex.map(String.init) ?? "not found")")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- A `while` loop must change state or terminate explicitly.
- Use `break` to exit the intended loop and `continue` to skip only the current iteration.
- Validate text before converting it to a numeric value.

### Activities
1. Test valid, invalid, and blank user input.
2. Trace a sentinel loop with both quit and non-quit commands.
3. Find the first matching score and stop immediately.
4. Prove a loop terminates for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain flags and early exits in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.4: Continue and filtering

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain continue and filtering using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Console input arrives as an optional string. Convert and validate it before use. `while`, `break`, and `continue` control repetition; a loop must make progress or reach an exit condition.

**Lesson focus:** Continue and filtering. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let values = [82, -1, 91, 0, 76]
var positiveValues: [Int] = []
for value in values {
    if value <= 0 { continue }
    positiveValues.append(value)
}
print(positiveValues)
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- A `while` loop must change state or terminate explicitly.
- Use `break` to exit the intended loop and `continue` to skip only the current iteration.
- Validate text before converting it to a numeric value.

### Activities
1. Test valid, invalid, and blank user input.
2. Trace a sentinel loop with both quit and non-quit commands.
3. Find the first matching score and stop immediately.
4. Prove a loop terminates for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain continue and filtering in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.5: Preventing infinite loops

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain preventing infinite loops using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Console input arrives as an optional string. Convert and validate it before use. `while`, `break`, and `continue` control repetition; a loop must make progress or reach an exit condition.

**Lesson focus:** Preventing infinite loops. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
func countDown(from start: Int) {
    var current = start
    while current > 0 {
        print(current)
        current -= 1
    }
    print("Done")
}
countDown(from: 3)
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- A `while` loop must change state or terminate explicitly.
- Use `break` to exit the intended loop and `continue` to skip only the current iteration.
- Validate text before converting it to a numeric value.

### Activities
1. Test valid, invalid, and blank user input.
2. Trace a sentinel loop with both quit and non-quit commands.
3. Find the first matching score and stop immediately.
4. Prove a loop terminates for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain preventing infinite loops in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
