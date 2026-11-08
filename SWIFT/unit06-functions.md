# Unit 6: Functions

## Overview

Functions declare parameter types, return types, and external argument labels. Swift supports default arguments, closures, and variadic parameters. Return optional values when a result may be absent; use `guard` for early validation exits.

## Lesson 6.1: Defining and calling functions

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain defining and calling functions using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Functions declare parameter types, return types, and external argument labels. Swift supports default arguments, closures, and variadic parameters. Return optional values when a result may be absent; use `guard` for early validation exits.

**Lesson focus:** Defining and calling functions. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
func greet(_ name: String) {
    print("Hello, \(name)!")
}
greet("Avery")
greet("Jordan")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift argument labels are part of a function's call-site API.
- A function returning an optional must handle the empty case explicitly.
- Closures capture values; understand capture semantics and avoid unnecessary shared mutable state.

### Activities
1. Write a function with a clear input and output contract.
2. Add argument labels and a default parameter value.
3. Test return values for normal, boundary, and invalid cases.
4. Compose a closure with a variadic reporting function.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain defining and calling functions in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.2: Parameters and argument labels

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain parameters and argument labels using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Functions declare parameter types, return types, and external argument labels. Swift supports default arguments, closures, and variadic parameters. Return optional values when a result may be absent; use `guard` for early validation exits.

**Lesson focus:** Parameters and argument labels. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
import Foundation
func invoiceTotal(subtotal: Double, tipRate: Double = 0.15) -> Double {
    return subtotal + subtotal * tipRate
}
print(String(format: "%.2f", invoiceTotal(subtotal: 24.50)))
print(String(format: "%.2f", invoiceTotal(subtotal: 24.50, tipRate: 0.20)))
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift argument labels are part of a function's call-site API.
- A function returning an optional must handle the empty case explicitly.
- Closures capture values; understand capture semantics and avoid unnecessary shared mutable state.

### Activities
1. Write a function with a clear input and output contract.
2. Add argument labels and a default parameter value.
3. Test return values for normal, boundary, and invalid cases.
4. Compose a closure with a variadic reporting function.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain parameters and argument labels in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.3: Return values

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain return values using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Functions declare parameter types, return types, and external argument labels. Swift supports default arguments, closures, and variadic parameters. Return optional values when a result may be absent; use `guard` for early validation exits.

**Lesson focus:** Return values. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
func letterGrade(for score: Int) -> String {
    guard (0...100).contains(score) else { return "Invalid" }
    switch score {
    case 90...100: return "A"
    case 80..<90: return "B"
    case 70..<80: return "C"
    case 60..<70: return "D"
    default: return "F"
    }
}
print(letterGrade(for: 82))
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift argument labels are part of a function's call-site API.
- A function returning an optional must handle the empty case explicitly.
- Closures capture values; understand capture semantics and avoid unnecessary shared mutable state.

### Activities
1. Write a function with a clear input and output contract.
2. Add argument labels and a default parameter value.
3. Test return values for normal, boundary, and invalid cases.
4. Compose a closure with a variadic reporting function.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain return values in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.4: Functions over collections

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain functions over collections using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Functions declare parameter types, return types, and external argument labels. Swift supports default arguments, closures, and variadic parameters. Return optional values when a result may be absent; use `guard` for early validation exits.

**Lesson focus:** Functions over collections. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
func mean(of values: [Double]) -> Double? {
    guard !values.isEmpty else { return nil }
    return values.reduce(0, +) / Double(values.count)
}
let scores = [82.0, 91.0, 76.0, 88.0]
print(mean(of: scores) ?? 0)
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift argument labels are part of a function's call-site API.
- A function returning an optional must handle the empty case explicitly.
- Closures capture values; understand capture semantics and avoid unnecessary shared mutable state.

### Activities
1. Write a function with a clear input and output contract.
2. Add argument labels and a default parameter value.
3. Test return values for normal, boundary, and invalid cases.
4. Compose a closure with a variadic reporting function.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain functions over collections in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.5: Scope, closures, and variadic parameters

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain scope, closures, and variadic parameters using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Functions declare parameter types, return types, and external argument labels. Swift supports default arguments, closures, and variadic parameters. Return optional values when a result may be absent; use `guard` for early validation exits.

**Lesson focus:** Scope, closures, and variadic parameters. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
func makeMultiplier(by factor: Int) -> (Int) -> Int {
    return { value in value * factor }
}
let triple = makeMultiplier(by: 3)
func report(_ title: String, scores: Int...) {
    print("\(title): \(scores.map(String.init).joined(separator: ", "))")
}
report("Tripled score", scores: triple(82), triple(91))
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift argument labels are part of a function's call-site API.
- A function returning an optional must handle the empty case explicitly.
- Closures capture values; understand capture semantics and avoid unnecessary shared mutable state.

### Activities
1. Write a function with a clear input and output contract.
2. Add argument labels and a default parameter value.
3. Test return values for normal, boundary, and invalid cases.
4. Compose a closure with a variadic reporting function.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain scope, closures, and variadic parameters in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
