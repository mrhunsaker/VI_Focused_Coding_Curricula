# Unit 7: Object-Oriented Programming

## Overview

Swift models data with structs, classes, enums, and protocols. Structs and enums have value semantics; classes have reference semantics. Protocols specify behavior, and composition models relationships without relying on inheritance.

## Lesson 7.1: Types and object models

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain types and object models using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift models data with structs, classes, enums, and protocols. Structs and enums have value semantics; classes have reference semantics. Protocols specify behavior, and composition models relationships without relying on inheritance.

**Lesson focus:** Types and object models. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
struct Student {
    let name: String
    var age: Int
}
let learner = Student(name: "Avery", age: 16)
print("\(learner.name) is \(learner.age)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- A `struct` instance is a value; mutating methods require a `var` receiver.
- Use `class` only when reference identity or shared mutation is required.
- Protocols define requirements; they are not concrete class inheritance.

### Activities
1. Model Avery or an inventory item with a Swift struct.
2. Create multiple instances and inspect stored and computed properties.
3. Define a protocol and conform a custom type to it.
4. Compare value semantics and reference semantics with a copied value.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain types and object models in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.2: Creating instances

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain creating instances using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift models data with structs, classes, enums, and protocols. Structs and enums have value semantics; classes have reference semantics. Protocols specify behavior, and composition models relationships without relying on inheritance.

**Lesson focus:** Creating instances. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
struct InventoryItem {
    let name: String
    var quantity: Int
}
let notebook = InventoryItem(name: "Notebook", quantity: 3)
let pencil = InventoryItem(name: "Pencil", quantity: 10)
print("\(notebook.name): \(notebook.quantity); \(pencil.name): \(pencil.quantity)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- A `struct` instance is a value; mutating methods require a `var` receiver.
- Use `class` only when reference identity or shared mutation is required.
- Protocols define requirements; they are not concrete class inheritance.

### Activities
1. Model Avery or an inventory item with a Swift struct.
2. Create multiple instances and inspect stored and computed properties.
3. Define a protocol and conform a custom type to it.
4. Compare value semantics and reference semantics with a copied value.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain creating instances in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.3: Properties and methods

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain properties and methods using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift models data with structs, classes, enums, and protocols. Structs and enums have value semantics; classes have reference semantics. Protocols specify behavior, and composition models relationships without relying on inheritance.

**Lesson focus:** Properties and methods. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
struct Circle {
    var radius: Double
    var area: Double { Double.pi * radius * radius }
    mutating func scale(by factor: Double) { radius *= factor }
}
var circle = Circle(radius: 2)
print(circle.area)
circle.scale(by: 2)
print(circle.area)
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- A `struct` instance is a value; mutating methods require a `var` receiver.
- Use `class` only when reference identity or shared mutation is required.
- Protocols define requirements; they are not concrete class inheritance.

### Activities
1. Model Avery or an inventory item with a Swift struct.
2. Create multiple instances and inspect stored and computed properties.
3. Define a protocol and conform a custom type to it.
4. Compare value semantics and reference semantics with a copied value.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain properties and methods in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.4: Protocols and inheritance

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain protocols and inheritance using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift models data with structs, classes, enums, and protocols. Structs and enums have value semantics; classes have reference semantics. Protocols specify behavior, and composition models relationships without relying on inheritance.

**Lesson focus:** Protocols and inheritance. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
protocol Describable {
    var summary: String { get }
}
struct Task: Describable {
    let title: String
    var isComplete: Bool
    var summary: String { "\(title): \(isComplete ? "complete" : "open")" }
}
let task = Task(title: "Read Swift lesson", isComplete: false)
print(task.summary)
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- A `struct` instance is a value; mutating methods require a `var` receiver.
- Use `class` only when reference identity or shared mutation is required.
- Protocols define requirements; they are not concrete class inheritance.

### Activities
1. Model Avery or an inventory item with a Swift struct.
2. Create multiple instances and inspect stored and computed properties.
3. Define a protocol and conform a custom type to it.
4. Compare value semantics and reference semantics with a copied value.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain protocols and inheritance in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.5: Composition and value semantics

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain composition and value semantics using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift models data with structs, classes, enums, and protocols. Structs and enums have value semantics; classes have reference semantics. Protocols specify behavior, and composition models relationships without relying on inheritance.

**Lesson focus:** Composition and value semantics. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
struct Address {
    var city: String
}
struct Person {
    let name: String
    var address: Address
}
var person = Person(name: "Avery", address: Address(city: "Farmington"))
var updatedPerson = person
updatedPerson.address.city = "Ogden"
print(person.address.city)
print(updatedPerson.address.city)
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- A `struct` instance is a value; mutating methods require a `var` receiver.
- Use `class` only when reference identity or shared mutation is required.
- Protocols define requirements; they are not concrete class inheritance.

### Activities
1. Model Avery or an inventory item with a Swift struct.
2. Create multiple instances and inspect stored and computed properties.
3. Define a protocol and conform a custom type to it.
4. Compare value semantics and reference semantics with a copied value.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain composition and value semantics in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
