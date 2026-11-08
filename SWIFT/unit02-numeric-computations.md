# Unit 2: Numeric Computations

## Overview

Design calculations by naming inputs, deriving intermediate values, and verifying results. Swift's numeric operators do not perform implicit conversions between integer and floating-point types. `readLine()` returns `String?`; unwrap or validate it before use. Foundation supplies formatting and common mathematical functions.

## Lesson 2.1: Software design and tracing

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain software design and tracing using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Design calculations by naming inputs, deriving intermediate values, and verifying results. Swift's numeric operators do not perform implicit conversions between integer and floating-point types. `readLine()` returns `String?`; unwrap or validate it before use. Foundation supplies formatting and common mathematical functions.

**Lesson focus:** Software design and tracing. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let scores = [82.0, 91.0, 76.0, 88.0]
let total = scores.reduce(0, +)
let average = total / Double(scores.count)
print("total=\(total), count=\(scores.count), average=\(average)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift does not implicitly convert between numeric types; convert explicitly.
- `readLine()` returns an optional string, not a guaranteed value.
- Use `Double` for fractional values and account for floating-point precision.

### Activities
1. Trace the calculator example and calculate each intermediate value.
2. Calculate a $24.50 bill with a 15% tip and compare formatted output.
3. Test zero, negative, and fractional inputs where meaningful.
4. Refactor a calculation into a named function and verify it.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain software design and tracing in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.2: Expressions, operators, and assignment

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain expressions, operators, and assignment using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Design calculations by naming inputs, deriving intermediate values, and verifying results. Swift's numeric operators do not perform implicit conversions between integer and floating-point types. `readLine()` returns `String?`; unwrap or validate it before use. Foundation supplies formatting and common mathematical functions.

**Lesson focus:** Expressions, operators, and assignment. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
import Foundation
let subtotal = 24.50
let tipRate = 0.15
let tip = subtotal * tipRate
let total = subtotal + tip
print(String(format: "subtotal=$%.2f tip=$%.2f total=$%.2f", subtotal, tip, total))
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift does not implicitly convert between numeric types; convert explicitly.
- `readLine()` returns an optional string, not a guaranteed value.
- Use `Double` for fractional values and account for floating-point precision.

### Activities
1. Trace the calculator example and calculate each intermediate value.
2. Calculate a $24.50 bill with a 15% tip and compare formatted output.
3. Test zero, negative, and fractional inputs where meaningful.
4. Refactor a calculation into a named function and verify it.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain expressions, operators, and assignment in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.3: Input and output

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain input and output using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Design calculations by naming inputs, deriving intermediate values, and verifying results. Swift's numeric operators do not perform implicit conversions between integer and floating-point types. `readLine()` returns `String?`; unwrap or validate it before use. Foundation supplies formatting and common mathematical functions.

**Lesson focus:** Input and output. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
print("Enter a learner name:")
let name = readLine() ?? ""
print("Hello, \(name.isEmpty ? "learner" : name)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift does not implicitly convert between numeric types; convert explicitly.
- `readLine()` returns an optional string, not a guaranteed value.
- Use `Double` for fractional values and account for floating-point precision.

### Activities
1. Trace the calculator example and calculate each intermediate value.
2. Calculate a $24.50 bill with a 15% tip and compare formatted output.
3. Test zero, negative, and fractional inputs where meaningful.
4. Refactor a calculation into a named function and verify it.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain input and output in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.4: Numeric types, conversions, and math

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain numeric types, conversions, and math using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Design calculations by naming inputs, deriving intermediate values, and verifying results. Swift's numeric operators do not perform implicit conversions between integer and floating-point types. `readLine()` returns `String?`; unwrap or validate it before use. Foundation supplies formatting and common mathematical functions.

**Lesson focus:** Numeric types, conversions, and math. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let wholeNumber = 7
let preciseNumber = Double(wholeNumber) / 2.0
let rounded = Int(preciseNumber.rounded())
print("precise=\(preciseNumber), rounded=\(rounded)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift does not implicitly convert between numeric types; convert explicitly.
- `readLine()` returns an optional string, not a guaranteed value.
- Use `Double` for fractional values and account for floating-point precision.

### Activities
1. Trace the calculator example and calculate each intermediate value.
2. Calculate a $24.50 bill with a 15% tip and compare formatted output.
3. Test zero, negative, and fractional inputs where meaningful.
4. Refactor a calculation into a named function and verify it.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain numeric types, conversions, and math in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.5: Using the Math Library

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain using the math library using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Design calculations by naming inputs, deriving intermediate values, and verifying results. Swift's numeric operators do not perform implicit conversions between integer and floating-point types. `readLine()` returns `String?`; unwrap or validate it before use. Foundation supplies formatting and common mathematical functions.

**Lesson focus:** Using the Math Library. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
import Foundation
let radius = 3.0
let area = Double.pi * pow(radius, 2)
let circumference = 2 * Double.pi * radius
let distance = hypot(3.0, 4.0)
print(String(format: "area=%.3f circumference=%.3f distance=%.1f", area, circumference, distance))
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift does not implicitly convert between numeric types; convert explicitly.
- `readLine()` returns an optional string, not a guaranteed value.
- Use `Double` for fractional values and account for floating-point precision.

### Activities
1. Trace the calculator example and calculate each intermediate value.
2. Calculate a $24.50 bill with a 15% tip and compare formatted output.
3. Test zero, negative, and fractional inputs where meaningful.
4. Refactor a calculation into a named function and verify it.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain using the math library in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
