# Unit 4: Data Structures

## Overview

Swift's Array, Dictionary, and Set are value types. Tuples group fixed related values; dictionaries map unique keys to values and return optionals on lookup. Collection methods such as `map`, `filter`, `sorted`, and `reduce` express transformations.

## Lesson 4.1: Array mutation and collection methods

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain array mutation and collection methods using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift's Array, Dictionary, and Set are value types. Tuples group fixed related values; dictionaries map unique keys to values and return optionals on lookup. Collection methods such as `map`, `filter`, `sorted`, and `reduce` express transformations.

**Lesson focus:** Array mutation and collection methods. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
var scores = [82, 91, 76, 88]
scores.append(95)
scores.insert(85, at: 1)
scores.remove(at: 0)
print(scores)
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Arrays and dictionaries are value types with copy-on-write behavior.
- Dictionary iteration order is not a stable presentation order; sort keys for deterministic output.
- A dictionary subscript returns an optional because the key may be absent.

### Activities
1. Add, update, and remove canonical inventory entries.
2. Sort inventory keys and explain why output order matters.
3. Represent a coordinate and learner record with tuples.
4. Test missing dictionary keys and empty collections.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain array mutation and collection methods in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.2: Sorting and organizing data

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain sorting and organizing data using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift's Array, Dictionary, and Set are value types. Tuples group fixed related values; dictionaries map unique keys to values and return optionals on lookup. Collection methods such as `map`, `filter`, `sorted`, and `reduce` express transformations.

**Lesson focus:** Sorting and organizing data. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let inventory = ["Notebook": 3, "Pencil": 10, "Folder": 4]
for item in inventory.keys.sorted() {
    print("\(item): \(inventory[item]!)")
}
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Arrays and dictionaries are value types with copy-on-write behavior.
- Dictionary iteration order is not a stable presentation order; sort keys for deterministic output.
- A dictionary subscript returns an optional because the key may be absent.

### Activities
1. Add, update, and remove canonical inventory entries.
2. Sort inventory keys and explain why output order matters.
3. Represent a coordinate and learner record with tuples.
4. Test missing dictionary keys and empty collections.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain sorting and organizing data in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.3: Tuples and immutable values

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain tuples and immutable values using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift's Array, Dictionary, and Set are value types. Tuples group fixed related values; dictionaries map unique keys to values and return optionals on lookup. Collection methods such as `map`, `filter`, `sorted`, and `reduce` express transformations.

**Lesson focus:** Tuples and immutable values. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let coordinate = (x: 3.0, y: 4.0)
let studentRecord = ("Avery", 16, "Computer Science")
print("point=(\(coordinate.x), \(coordinate.y))")
print("student=\(studentRecord.0), age=\(studentRecord.1)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Arrays and dictionaries are value types with copy-on-write behavior.
- Dictionary iteration order is not a stable presentation order; sort keys for deterministic output.
- A dictionary subscript returns an optional because the key may be absent.

### Activities
1. Add, update, and remove canonical inventory entries.
2. Sort inventory keys and explain why output order matters.
3. Represent a coordinate and learner record with tuples.
4. Test missing dictionary keys and empty collections.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain tuples and immutable values in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.4: Dictionaries and key-value data

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain dictionaries and key-value data using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift's Array, Dictionary, and Set are value types. Tuples group fixed related values; dictionaries map unique keys to values and return optionals on lookup. Collection methods such as `map`, `filter`, `sorted`, and `reduce` express transformations.

**Lesson focus:** Dictionaries and key-value data. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
var inventory: [String: Int] = ["Notebook": 3, "Pencil": 10]
inventory["Folder"] = 4
inventory["Pencil"] = nil
print("notebooks=\(inventory["Notebook"] ?? 0)")
print("keys=\(inventory.keys.sorted())")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Arrays and dictionaries are value types with copy-on-write behavior.
- Dictionary iteration order is not a stable presentation order; sort keys for deterministic output.
- A dictionary subscript returns an optional because the key may be absent.

### Activities
1. Add, update, and remove canonical inventory entries.
2. Sort inventory keys and explain why output order matters.
3. Represent a coordinate and learner record with tuples.
4. Test missing dictionary keys and empty collections.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain dictionaries and key-value data in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.5: Collection traversal

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain collection traversal using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift's Array, Dictionary, and Set are value types. Tuples group fixed related values; dictionaries map unique keys to values and return optionals on lookup. Collection methods such as `map`, `filter`, `sorted`, and `reduce` express transformations.

**Lesson focus:** Collection traversal. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let scores = [82, 91, 76, 88]
let passing = scores.filter { $0 >= 80 }
let doubled = scores.map { $0 * 2 }
let total = scores.reduce(0, +)
print("passing=\(passing), doubled=\(doubled), total=\(total)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Arrays and dictionaries are value types with copy-on-write behavior.
- Dictionary iteration order is not a stable presentation order; sort keys for deterministic output.
- A dictionary subscript returns an optional because the key may be absent.

### Activities
1. Add, update, and remove canonical inventory entries.
2. Sort inventory keys and explain why output order matters.
3. Represent a coordinate and learner record with tuples.
4. Test missing dictionary keys and empty collections.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain collection traversal in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
