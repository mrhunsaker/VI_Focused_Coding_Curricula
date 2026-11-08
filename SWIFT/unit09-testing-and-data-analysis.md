# Unit 9: Testing and Data Analysis

## Overview

Test pure functions and stateful types with assertions or XCTest in a package. Floating-point comparisons often need tolerances. Foundation and Swift standard-library collections support text and data processing; robust CSV requires a parser that understands quoting and escaping.

## Lesson 9.1: Testing pure functions

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain testing pure functions using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Test pure functions and stateful types with assertions or XCTest in a package. Floating-point comparisons often need tolerances. Foundation and Swift standard-library collections support text and data processing; robust CSV requires a parser that understands quoting and escaping.

**Lesson focus:** Testing pure functions. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
func tip(for bill: Double, rate: Double) -> Double {
    bill * rate
}
precondition(tip(for: 20, rate: 0.2) == 4)
precondition(abs(tip(for: 24.50, rate: 0.15) - 3.675) < 0.000001)
print("Tip calculation tests passed")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Use tolerance-based assertions for floating-point calculations.
- Random results are not reproducible unless the generator and seed are controlled.
- A simple comma split is not a complete CSV parser for quoted fields.

### Activities
1. Test pure functions with ordinary and boundary inputs.
2. Test a stateful type before and after mutation.
3. Generate random values and discuss repeatability.
4. Analyze the canonical text sample and process simple CSV rows.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain testing pure functions in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.2: Testing stateful types

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain testing stateful types using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Test pure functions and stateful types with assertions or XCTest in a package. Floating-point comparisons often need tolerances. Foundation and Swift standard-library collections support text and data processing; robust CSV requires a parser that understands quoting and escaping.

**Lesson focus:** Testing stateful types. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
struct Counter {
    private(set) var value = 0
    mutating func increment() { value += 1 }
}
var counter = Counter()
counter.increment()
counter.increment()
precondition(counter.value == 2)
print("Counter state test passed: \(counter.value)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Use tolerance-based assertions for floating-point calculations.
- Random results are not reproducible unless the generator and seed are controlled.
- A simple comma split is not a complete CSV parser for quoted fields.

### Activities
1. Test pure functions with ordinary and boundary inputs.
2. Test a stateful type before and after mutation.
3. Generate random values and discuss repeatability.
4. Analyze the canonical text sample and process simple CSV rows.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain testing stateful types in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.3: Random values

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain random values using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Test pure functions and stateful types with assertions or XCTest in a package. Floating-point comparisons often need tolerances. Foundation and Swift standard-library collections support text and data processing; robust CSV requires a parser that understands quoting and escaping.

**Lesson focus:** Random values. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
import Foundation
var generator = SystemRandomNumberGenerator()
let diceRolls = (1...5).map { _ in Int.random(in: 1...6, using: &generator) }
print("Dice rolls: \(diceRolls)")
let seededLikeValues = (1...5).map { _ in Int.random(in: 1...10) }
print("Additional sample: \(seededLikeValues)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Use tolerance-based assertions for floating-point calculations.
- Random results are not reproducible unless the generator and seed are controlled.
- A simple comma split is not a complete CSV parser for quoted fields.

### Activities
1. Test pure functions with ordinary and boundary inputs.
2. Test a stateful type before and after mutation.
3. Generate random values and discuss repeatability.
4. Analyze the canonical text sample and process simple CSV rows.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain random values in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.4: Text analysis

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text analysis using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Test pure functions and stateful types with assertions or XCTest in a package. Floating-point comparisons often need tolerances. Foundation and Swift standard-library collections support text and data processing; robust CSV requires a parser that understands quoting and escaping.

**Lesson focus:** Text analysis. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let sample = "A student studies Swift. Swift helps students build useful programs."
let words = sample.lowercased().split { !$0.isLetter }
var counts: [String: Int] = [:]
for word in words { counts[String(word), default: 0] += 1 }
for word in counts.keys.sorted() { print("\(word): \(counts[word]!)") }
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Use tolerance-based assertions for floating-point calculations.
- Random results are not reproducible unless the generator and seed are controlled.
- A simple comma split is not a complete CSV parser for quoted fields.

### Activities
1. Test pure functions with ordinary and boundary inputs.
2. Test a stateful type before and after mutation.
3. Generate random values and discuss repeatability.
4. Analyze the canonical text sample and process simple CSV rows.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain text analysis in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.5: CSV records

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain csv records using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Test pure functions and stateful types with assertions or XCTest in a package. Floating-point comparisons often need tolerances. Foundation and Swift standard-library collections support text and data processing; robust CSV requires a parser that understands quoting and escaping.

**Lesson focus:** CSV records. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let csv = "id,first_name,score\n1,Avery,91\n2,Jordan,84"
let lines = csv.split(separator: "\n")
for line in lines.dropFirst() {
    let fields = line.split(separator: ",")
    if fields.count == 3, let score = Int(fields[2]) {
        print("\(fields[1]): \(score)")
    }
}
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Use tolerance-based assertions for floating-point calculations.
- Random results are not reproducible unless the generator and seed are controlled.
- A simple comma split is not a complete CSV parser for quoted fields.

### Activities
1. Test pure functions with ordinary and boundary inputs.
2. Test a stateful type before and after mutation.
3. Generate random values and discuss repeatability.
4. Analyze the canonical text sample and process simple CSV rows.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain csv records in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
