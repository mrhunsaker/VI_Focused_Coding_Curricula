# Swift: Complete Curriculum — Units 0–11

## Course Overview

Swift is used for iOS, macOS, watchOS, tvOS, server applications, and systems components. This course mirrors the original Python curriculum's problem contexts so students focus on Swift syntax and semantics. It teaches Swift-native optionals, value types, protocols, error handling, Codable, and concurrency rather than mechanically translating Python.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install Swift, create a project, and verify keyboard and screen-reader access.

### Lesson 0.1: Install and Verify Swift

Install Xcode on macOS or the Swift toolchain on a supported platform. Verify `swift --version`; run `swift main.swift` or create a package with `swift package init --type executable`.

### Lesson 0.2: Workspace and First Run
Create a project folder and a file named `main.swift`. Run it from the terminal, read standard output and diagnostics, and distinguish the Swift compiler/interpreter from the source file.

### Lesson 0.3: Editor and Accessibility Workflow
Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md). Test keyboard navigation, punctuation announcement, indentation, terminal focus, and diagnostics. Install only required Swift language tooling.

### Skills Checklist
- [ ] I can verify Swift installation.
- [ ] I can create and run a source file.
- [ ] I can navigate the editor and read output accessibly.

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

Use the terminal from the project root and understand the current working directory. Keep each project in its own folder and distinguish source files, build output, and dependency metadata. For multi-file work, use Swift Package Manager. Create a package with `swift package init --type executable`; add dependencies in Package.swift, run `swift package resolve`, build with `swift build`, and execute with `swift run`.

### Skills Checklist
- [ ] I can identify the project root and run commands from it.
- [ ] I can explain where project dependencies are recorded, if applicable.
- [ ] I can run the program or test command from the terminal and read its output.

# Unit 1: Foundations of Computing

## Overview

This unit follows the matching Python unit's objectives and examples. Its purpose is to make the programming concept familiar while Swift's type system and language features become the new learning target.

## Lesson 1.1: Computer science and problem solving

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain computer science and problem solving in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Computer science and problem solving. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
print("Hello, World!")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 1.2: Your first program and sequential execution

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain your first program and sequential execution in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Your first program and sequential execution. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
print("Hello, World!")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 1.3: Variables, constants, type inference, and primitive types

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain variables, constants, type inference, and primitive types in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Variables, constants, type inference, and primitive types. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
print("Hello, World!")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

# Unit 2: Numeric Computations

## Overview

This unit follows the matching Python unit's objectives and examples. Its purpose is to make the programming concept familiar while Swift's type system and language features become the new learning target.

## Lesson 2.1: Software design and tracing

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain software design and tracing in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Software design and tracing. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let name = "Avery"; let age = 16; let height = 1.72
print("\(name) is \(age) years old.")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 2.2: Expressions, operators, and assignment

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain expressions, operators, and assignment in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Expressions, operators, and assignment. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let name = "Avery"; let age = 16; let height = 1.72
print("\(name) is \(age) years old.")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 2.3: Input and output

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain input and output in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Input and output. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let name = "Avery"; let age = 16; let height = 1.72
print("\(name) is \(age) years old.")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 2.4: Numeric types, conversions, and math

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain numeric types, conversions, and math in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Numeric types, conversions, and math. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let name = "Avery"; let age = 16; let height = 1.72
print("\(name) is \(age) years old.")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

# Unit 3: Control Flow

## Overview

This unit follows the matching Python unit's objectives and examples. Its purpose is to make the programming concept familiar while Swift's type system and language features become the new learning target.

## Lesson 3.1: Boolean expressions and if statements

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain boolean expressions and if statements in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Boolean expressions and if statements. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let bill = 24.50; let tip = bill * 0.15
print("Tip: \(tip); total: \(bill + tip)")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 3.2: Chained conditionals and grade classification

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain chained conditionals and grade classification in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Chained conditionals and grade classification. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let bill = 24.50; let tip = bill * 0.15
print("Tip: \(tip); total: \(bill + tip)")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 3.3: Arrays and indexing

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain arrays and indexing in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Arrays and indexing. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let bill = 24.50; let tip = bill * 0.15
print("Tip: \(tip); total: \(bill + tip)")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 3.4: For loops and iteration

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain for loops and iteration in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
For loops and iteration. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let bill = 24.50; let tip = bill * 0.15
print("Tip: \(tip); total: \(bill + tip)")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 3.5: Strings and common operations

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain strings and common operations in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Strings and common operations. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let bill = 24.50; let tip = bill * 0.15
print("Tip: \(tip); total: \(bill + tip)")
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

# Unit 4: Data Structures

## Overview

This unit follows the matching Python unit's objectives and examples. Its purpose is to make the programming concept familiar while Swift's type system and language features become the new learning target.

## Lesson 4.1: Array mutation and collection methods

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain array mutation and collection methods in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Array mutation and collection methods. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let score = 82
if score >= 90 { print("A") } else if score >= 80 { print("B") } else { print("Keep practicing") }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 4.2: Sorting and organizing data

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain sorting and organizing data in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Sorting and organizing data. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let score = 82
if score >= 90 { print("A") } else if score >= 80 { print("B") } else { print("Keep practicing") }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 4.3: Tuples and immutable values

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain tuples and immutable values in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Tuples and immutable values. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let score = 82
if score >= 90 { print("A") } else if score >= 80 { print("B") } else { print("Keep practicing") }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 4.4: Dictionaries and key-value data

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain dictionaries and key-value data in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Dictionaries and key-value data. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let score = 82
if score >= 90 { print("A") } else if score >= 80 { print("B") } else { print("Keep practicing") }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 4.5: Collection traversal

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain collection traversal in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Collection traversal. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let score = 82
if score >= 90 { print("A") } else if score >= 80 { print("B") } else { print("Keep practicing") }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

# Unit 5: Input and Iteration

## Overview

This unit follows the matching Python unit's objectives and examples. Its purpose is to make the programming concept familiar while Swift's type system and language features become the new learning target.

## Lesson 5.1: Input and validation

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain input and validation in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Input and validation. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let scores = [82, 91, 76, 88]
for score in scores { print(score) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 5.2: While loops and sentinel repetition

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain while loops and sentinel repetition in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
While loops and sentinel repetition. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let scores = [82, 91, 76, 88]
for score in scores { print(score) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 5.3: Flags and early exits

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain flags and early exits in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Flags and early exits. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let scores = [82, 91, 76, 88]
for score in scores { print(score) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 5.4: Continue and filtering

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain continue and filtering in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Continue and filtering. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let scores = [82, 91, 76, 88]
for score in scores { print(score) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 5.5: Preventing infinite loops

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain preventing infinite loops in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Preventing infinite loops. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
let scores = [82, 91, 76, 88]
for score in scores { print(score) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

# Unit 6: Functions

## Overview

This unit follows the matching Python unit's objectives and examples. Its purpose is to make the programming concept familiar while Swift's type system and language features become the new learning target.

## Lesson 6.1: Defining and calling functions

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain defining and calling functions in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Defining and calling functions. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
struct Item { let name: String; var quantity: Int }
let book = Item(name: "Notebook", quantity: 3)
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 6.2: Parameters and argument labels

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain parameters and argument labels in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Parameters and argument labels. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
struct Item { let name: String; var quantity: Int }
let book = Item(name: "Notebook", quantity: 3)
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 6.3: Return values

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain return values in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Return values. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
struct Item { let name: String; var quantity: Int }
let book = Item(name: "Notebook", quantity: 3)
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 6.4: Functions over collections

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain functions over collections in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Functions over collections. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
struct Item { let name: String; var quantity: Int }
let book = Item(name: "Notebook", quantity: 3)
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 6.5: Scope, closures, and variadic parameters

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain scope, closures, and variadic parameters in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Scope, closures, and variadic parameters. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
struct Item { let name: String; var quantity: Int }
let book = Item(name: "Notebook", quantity: 3)
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

# Unit 7: Object-Oriented Programming

## Overview

This unit follows the matching Python unit's objectives and examples. Its purpose is to make the programming concept familiar while Swift's type system and language features become the new learning target.

## Lesson 7.1: Types and object models

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain types and object models in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Types and object models. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 7.2: Creating instances

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain creating instances in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Creating instances. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 7.3: Properties and methods

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain properties and methods in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Properties and methods. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 7.4: Protocols and inheritance

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain protocols and inheritance in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Protocols and inheritance. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 7.5: Composition and value semantics

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain composition and value semantics in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Composition and value semantics. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

# Unit 8: Files and Exceptions

## Overview

This unit follows the matching Python unit's objectives and examples. Its purpose is to make the programming concept familiar while Swift's type system and language features become the new learning target.

## Lesson 8.1: Reading text files

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain reading text files in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Reading text files. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
do { let text = try String(contentsOfFile: "notes.txt", encoding: .utf8); print(text) } catch { print(error) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 8.2: Writing and appending files

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain writing and appending files in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Writing and appending files. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
do { let text = try String(contentsOfFile: "notes.txt", encoding: .utf8); print(text) } catch { print(error) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 8.3: Errors and throwing functions

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain errors and throwing functions in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Errors and throwing functions. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
do { let text = try String(contentsOfFile: "notes.txt", encoding: .utf8); print(text) } catch { print(error) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 8.4: Resource lifetime and cleanup

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain resource lifetime and cleanup in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Resource lifetime and cleanup. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
do { let text = try String(contentsOfFile: "notes.txt", encoding: .utf8); print(text) } catch { print(error) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 8.5: JSON with Codable

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain json with codable in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
JSON with Codable. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
do { let text = try String(contentsOfFile: "notes.txt", encoding: .utf8); print(text) } catch { print(error) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

# Unit 9: Testing and Data Analysis

## Overview

This unit follows the matching Python unit's objectives and examples. Its purpose is to make the programming concept familiar while Swift's type system and language features become the new learning target.

## Lesson 9.1: Testing pure functions

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain testing pure functions in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Testing pure functions. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
import Testing
@Test func additionWorks() { #expect(2 + 3 == 5) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 9.2: Testing stateful types

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain testing stateful types in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Testing stateful types. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
import Testing
@Test func additionWorks() { #expect(2 + 3 == 5) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 9.3: Random values

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain random values in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Random values. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
import Testing
@Test func additionWorks() { #expect(2 + 3 == 5) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 9.4: Text analysis

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain text analysis in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Text analysis. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
import Testing
@Test func additionWorks() { #expect(2 + 3 == 5) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 9.5: CSV records

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain csv records in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
CSV records. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
import Testing
@Test func additionWorks() { #expect(2 + 3 == 5) }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

# Unit 10: Project-Based Learning

## Overview

This unit follows the matching Python unit's objectives and examples. Its purpose is to make the programming concept familiar while Swift's type system and language features become the new learning target.

## Lesson 10.1: Requirements and top-down design

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain requirements and top-down design in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Requirements and top-down design. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
struct TaskItem { let id: Int; var title: String; var done: Bool }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain text adventure: rooms and movement in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Text adventure: rooms and movement. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
struct TaskItem { let id: Int; var title: String; var done: Bool }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain text adventure: inventory and puzzles in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Text adventure: inventory and puzzles. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
struct TaskItem { let id: Int; var title: String; var done: Bool }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 10.4: Command-line to-do manager

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain command-line to-do manager in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Command-line to-do manager. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
struct TaskItem { let id: Int; var title: String; var done: Bool }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 10.5: Accessible interaction and validation

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain accessible interaction and validation in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Accessible interaction and validation. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
struct TaskItem { let id: Int; var title: String; var done: Bool }
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

# Unit 11: Capstone

## Overview

This unit follows the matching Python unit's objectives and examples. Its purpose is to make the programming concept familiar while Swift's type system and language features become the new learning target.

## Lesson 11.1: Requirements and design

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain requirements and design in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Requirements and design. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
// Capstone: Codable personal-data manager with CRUD operations and tests.
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 11.2: Data model and storage

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain data model and storage in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Data model and storage. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
// Capstone: Codable personal-data manager with CRUD operations and tests.
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 11.3: Create, read, update, delete

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain create, read, update, delete in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Create, read, update, delete. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
// Capstone: Codable personal-data manager with CRUD operations and tests.
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 11.4: Validation and tests

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain validation and tests in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Validation and tests. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
// Capstone: Codable personal-data manager with CRUD operations and tests.
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Lesson 11.5: Documentation and presentation

### Reading References
- Official Swift language guide and standard library documentation.
- Matching Python curriculum lesson for the problem context.

### Learning Objectives
- Explain documentation and presentation in Swift terms.
- Predict program behavior before running the example.
- Modify, run, and debug the example independently.

### Concept Explanation
Documentation and presentation. Swift is statically typed with type inference, value semantics, optionals, and a strong standard library. Use `let` for values that do not change and `var` for mutable values. Explain any semantic difference from Python rather than assuming the languages behave alike.

### Worked Example
```swift
// Capstone: Codable personal-data manager with CRUD operations and tests.
```

**Expected behavior:** the example demonstrates the unit's corresponding operation. Trace each declaration and expression before execution; then run it and compare the actual output.

### Common Mistakes
- Using `var` where a constant `let` is sufficient, or attempting to mutate a constant.
- Treating an optional as if it always contains a value; unwrap safely.
- Assuming arrays, dictionaries, strings, or structs have Python's semantics.
- Ignoring compiler diagnostics or thrown errors.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the result before execution.
3. Add one boundary case and one invalid-input case.
4. Explain the code and output without relying on syntax highlighting.

### Accessibility Practice
Navigate by line, word, and character; verify punctuation announcements; run from the terminal; and read output and diagnostics sequentially.

### Skills Checklist
- [ ] I can explain the concept in Swift terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output with my access technology.

## Course-Wide Assessment and Portfolio

Submit runnable exercises, prediction and debugging notes, tests, a text adventure, a command-line to-do manager, and an accessible personal-data manager. Assessment focuses on correct behavior, idiomatic Swift, independent debugging, and code explanation.

## AI Policy
AI may be used only for personal conceptual explanations and reinforcement when permitted. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.