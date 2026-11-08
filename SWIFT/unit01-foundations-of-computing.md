# Unit 1: Foundations of Computing

## Overview

Computer science expresses problems as precise inputs, transformations, and outputs. A program executes statements in order unless control flow changes that order. Swift is statically typed with type inference; `let` creates an immutable binding and `var` a mutable binding.

## Lesson 1.1: Computer science and problem solving

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain computer science and problem solving using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Computer science expresses problems as precise inputs, transformations, and outputs. A program executes statements in order unless control flow changes that order. Swift is statically typed with type inference; `let` creates an immutable binding and `var` a mutable binding.

**Lesson focus:** Computer science and problem solving. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let problem = "Calculate a class average"
let inputs = ["82", "91", "76", "88"]
let steps = ["collect scores", "validate each score", "calculate the mean", "report the result"]
for (index, step) in steps.enumerated() {
    print("\(index + 1). \(step)")
}
print("Problem: \(problem); inputs: \(inputs.count)\n")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Prefer `let` for bindings that never change; use `var` only when mutation is required.
- Swift uses static typing with inference; a binding's type is fixed after initialization.
- Do not assume Python indexing, collection, or string semantics carry over.

### Activities
1. Trace the algorithm and state the input, process, and output.
2. Change the canonical learner data and predict the printed result.
3. Write a short sequence of steps for calculating a class average.
4. Run the example and explain its output without syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain computer science and problem solving in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 1.2: Your first program and sequential execution

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain your first program and sequential execution using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Computer science expresses problems as precise inputs, transformations, and outputs. A program executes statements in order unless control flow changes that order. Swift is statically typed with type inference; `let` creates an immutable binding and `var` a mutable binding.

**Lesson focus:** Your first program and sequential execution. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
print("Hello, Swift!")
print("Swift version is reported by the swift --version command.")
let greeting = "Welcome to the course"
print(greeting)
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Prefer `let` for bindings that never change; use `var` only when mutation is required.
- Swift uses static typing with inference; a binding's type is fixed after initialization.
- Do not assume Python indexing, collection, or string semantics carry over.

### Activities
1. Trace the algorithm and state the input, process, and output.
2. Change the canonical learner data and predict the printed result.
3. Write a short sequence of steps for calculating a class average.
4. Run the example and explain its output without syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain your first program and sequential execution in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 1.3: Variables, constants, type inference, and primitive types

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain variables, constants, type inference, and primitive types using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Computer science expresses problems as precise inputs, transformations, and outputs. A program executes statements in order unless control flow changes that order. Swift is statically typed with type inference; `let` creates an immutable binding and `var` a mutable binding.

**Lesson focus:** Variables, constants, type inference, and primitive types. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let studentName: String = "Avery"
var completedLessons = 3
let averageScore = 84.25
let isEnrolled = true
completedLessons += 1
print("\(studentName): \(completedLessons), average \(averageScore), enrolled \(isEnrolled)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Prefer `let` for bindings that never change; use `var` only when mutation is required.
- Swift uses static typing with inference; a binding's type is fixed after initialization.
- Do not assume Python indexing, collection, or string semantics carry over.

### Activities
1. Trace the algorithm and state the input, process, and output.
2. Change the canonical learner data and predict the printed result.
3. Write a short sequence of steps for calculating a class average.
4. Run the example and explain its output without syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain variables, constants, type inference, and primitive types in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
