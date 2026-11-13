# Unit 3: Control Flow

## Overview

Swift uses `Bool` conditions, `if`/`else if`/`else`, `switch`, zero-based arrays, and `for-in` loops. Array subscripting requires a valid index. Strings are collections of extended grapheme clusters; use String APIs rather than assuming integer offsets are byte offsets.

## Lesson 3.1: Boolean expressions and if statements

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain boolean expressions and if statements using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift uses `Bool` conditions, `if`/`else if`/`else`, `switch`, zero-based arrays, and `for-in` loops. Array subscripting requires a valid index. Strings are collections of extended grapheme clusters; use String APIs rather than assuming integer offsets are byte offsets.

**Lesson focus:** Boolean expressions and if statements. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let score = 82
let isPassing = score >= 60 && score <= 100
let hasPerfectScore = score == 100
if isPassing {
    print("Passing: \(score)")
} else {
    print("Needs review")
}
print("Perfect: \(hasPerfectScore)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift Boolean conditions must be `Bool`; integers are not truthy or falsy.
- Array indices are zero-based and valid indices stop before `count`.
- Handle optional lookups and user input instead of force-unwrapping.

### Activities
1. Test scores 82, 91, 76, and 88 at grade boundaries.
2. Test empty and single-element collections.
3. Trace each loop iteration and its index.
4. Normalize the canonical text sample and search it case-insensitively.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain boolean expressions and if statements in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.2: Chained conditionals and grade classification

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain chained conditionals and grade classification using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift uses `Bool` conditions, `if`/`else if`/`else`, `switch`, zero-based arrays, and `for-in` loops. Array subscripting requires a valid index. Strings are collections of extended grapheme clusters; use String APIs rather than assuming integer offsets are byte offsets.

**Lesson focus:** Chained conditionals and grade classification. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let score = 91
let grade: String
if score >= 90 { grade = "A" }
else if score >= 80 { grade = "B" }
else if score >= 70 { grade = "C" }
else if score >= 60 { grade = "D" }
else { grade = "F" }
print("Score \(score) earns \(grade)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift Boolean conditions must be `Bool`; integers are not truthy or falsy.
- Array indices are zero-based and valid indices stop before `count`.
- Handle optional lookups and user input instead of force-unwrapping.

### Activities
1. Test scores 82, 91, 76, and 88 at grade boundaries.
2. Test empty and single-element collections.
3. Trace each loop iteration and its index.
4. Normalize the canonical text sample and search it case-insensitively.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain chained conditionals and grade classification in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.3: Arrays and indexing

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain arrays and indexing using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift uses `Bool` conditions, `if`/`else if`/`else`, `switch`, zero-based arrays, and `for-in` loops. Array subscripting requires a valid index. Strings are collections of extended grapheme clusters; use String APIs rather than assuming integer offsets are byte offsets.

**Lesson focus:** Arrays and indexing. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let scores = [82, 91, 76, 88]
print("first=\(scores[0]), last=\(scores[scores.count - 1])")
print("count=\(scores.count), contains 91=\(scores.contains(91))")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift Boolean conditions must be `Bool`; integers are not truthy or falsy.
- Array indices are zero-based and valid indices stop before `count`.
- Handle optional lookups and user input instead of force-unwrapping.

### Activities
1. Test scores 82, 91, 76, and 88 at grade boundaries.
2. Test empty and single-element collections.
3. Trace each loop iteration and its index.
4. Normalize the canonical text sample and search it case-insensitively.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain arrays and indexing in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.4: For loops and iteration

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain for loops and iteration using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift uses `Bool` conditions, `if`/`else if`/`else`, `switch`, zero-based arrays, and `for-in` loops. Array subscripting requires a valid index. Strings are collections of extended grapheme clusters; use String APIs rather than assuming integer offsets are byte offsets.

**Lesson focus:** For loops and iteration. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let scores = [82, 91, 76, 88]
for (index, score) in scores.enumerated() {
    print("Score \(index + 1): \(score)")
}
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift Boolean conditions must be `Bool`; integers are not truthy or falsy.
- Array indices are zero-based and valid indices stop before `count`.
- Handle optional lookups and user input instead of force-unwrapping.

### Activities
1. Test scores 82, 91, 76, and 88 at grade boundaries.
2. Test empty and single-element collections.
3. Trace each loop iteration and its index.
4. Normalize the canonical text sample and search it case-insensitively.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain for loops and iteration in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.5: Strings and common operations

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain strings and common operations using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Swift uses `Bool` conditions, `if`/`else if`/`else`, `switch`, zero-based arrays, and `for-in` loops. Array subscripting requires a valid index. Strings are collections of extended grapheme clusters; use String APIs rather than assuming integer offsets are byte offsets.

**Lesson focus:** Strings and common operations. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
import Foundation
let rawText = "  Avery studies Swift Programming.  "
let cleaned = rawText.trimmingCharacters(in: .whitespacesAndNewlines)
print(cleaned.lowercased())
print("contains Swift: \(cleaned.contains("Swift")); characters: \(cleaned.count)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Swift Boolean conditions must be `Bool`; integers are not truthy or falsy.
- Array indices are zero-based and valid indices stop before `count`.
- Handle optional lookups and user input instead of force-unwrapping.

### Activities
1. Test scores 82, 91, 76, and 88 at grade boundaries.
2. Test empty and single-element collections.
3. Trace each loop iteration and its index.
4. Normalize the canonical text sample and search it case-insensitively.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain strings and common operations in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
