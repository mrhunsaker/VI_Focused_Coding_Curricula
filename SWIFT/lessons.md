# Swift: Complete Curriculum — Units 0–11

## Course Overview

Swift is used for iOS, macOS, watchOS, tvOS, server applications, and systems components. Its static type system, optionals, value semantics, protocols, structured error handling, Codable, and concurrency support robust application development. This course follows the Python curriculum's unit sequence and shared problem contexts while teaching Swift-native design.

**Version baseline:** Swift 6 language mode and a current Swift 6 toolchain. Verify with `swift --version`. Run a single file with `swift main.swift`; use Swift Package Manager for multi-file projects and dependencies.

## Unit 0: Accessible Environment and Toolchain

### Overview

Install and verify the Swift toolchain, create a predictable workspace, configure an accessible editor, and understand Swift Package Manager. On macOS, Xcode provides the integrated toolchain and simulator; supported Linux and Windows distributions can use the Swift toolchain for command-line development. iOS application development requires macOS and Xcode.

### Lesson 0.1: Install and Verify Swift

#### Reading References
- [Swift.org downloads](https://www.swift.org/install/)
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)

#### Learning Objectives
- Install Swift 6 or Xcode with the Swift 6 toolchain.
- Verify compiler and interpreter availability.
- Distinguish the Swift REPL, script execution, and compilation.

#### Concept Explanation
On macOS, install Xcode or the official Swift toolchain. On supported Linux or Windows systems, follow the official Swift installation instructions for the platform. Open a new terminal and run `swift --version` and `swiftc --version`. Run a source file with `swift main.swift`; compile an executable with `swiftc main.swift -o main` and run it with `./main`. Xcode is required for Apple-platform SDKs and iOS simulators.

#### Worked Example
```swift
print("Swift toolchain is available.")
print("Run swift --version to inspect the installed version.")
```

#### Expected Behavior or Output
The program prints two lines confirming that the source file executes. The terminal version command reports the installed compiler version.

#### Common Mistakes
- Using a terminal session whose PATH has not refreshed after installation.
- Assuming the Swift REPL, script interpreter, compiler, and Xcode are interchangeable tools.
- Expecting iOS simulator tooling on a non-macOS host.

#### Activities
1. Install Swift or Xcode using the official platform instructions.
2. Record the output of `swift --version` and `swiftc --version`.
3. Run the worked example as a script and compile it as an executable.
4. Deliberately use an incorrect filename and read the compiler or runtime diagnostic.

#### Accessibility Practice
Navigate the installer and terminal by keyboard. Confirm that prompts, compiler messages, punctuation, and build output are announced by the learner's screen reader or braille display.

#### Skills Checklist
- [ ] I can install and identify a supported Swift toolchain.
- [ ] I can report the installed Swift version.
- [ ] I can run a Swift script from the terminal.
- [ ] I can compile and execute a standalone Swift program.
- [ ] I can read terminal output and diagnostics using my access technology.

### Lesson 0.2: Workspace and First Run

#### Reading References
- [Swift command-line usage](https://www.swift.org/documentation/)
- [Swift Package Manager](https://www.swift.org/documentation/package-manager/)

#### Learning Objectives
- Create and identify a project root and Swift source file.
- Distinguish source files from generated build artifacts.
- Explain how the process working directory affects relative file paths.

#### Concept Explanation
Create a course directory and save `main.swift` in its root. Use `pwd` in the terminal to confirm the current directory. Swift resolves relative file paths from the process working directory, not automatically from the source file's directory. Keep source, test, data, and generated files in predictable locations. Package builds create a `.build` directory.

#### Worked Example
```swift
import Foundation
print("Project: Swift course workspace")
print("Working directory: \(FileManager.default.currentDirectoryPath)")
```

#### Expected Behavior or Output
The program prints a project label and the absolute path of the directory from which it is running.

#### Common Mistakes
- Opening a parent directory instead of the intended project root.
- Assuming relative file paths are based on the source file's location.
- Editing or deleting generated files under `.build` instead of source files.

#### Activities
1. Create the project directory and verify it with `pwd`.
2. Save and run `main.swift` from the project root.
3. Change to a different working directory and observe how a relative path resolves.
4. Create a Swift package and identify its source and build directories.

#### Accessibility Practice
Use terminal history and directory commands without drag-and-drop. Verify that editor file navigation, indentation, build output, and diagnostics are exposed in a linear reading order.

#### Skills Checklist
- [ ] I can identify the project root and current working directory.
- [ ] I can create and run `main.swift`.
- [ ] I can explain how relative paths are resolved.
- [ ] I can distinguish source files from generated build artifacts.
- [ ] I can navigate the workspace without mouse-only actions.

### Lesson 0.3: Editor and Accessibility Workflow

#### Reading References
- [Swift tools and editors](https://www.swift.org/documentation/)
- [Shared IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md)

#### Learning Objectives
- Configure VS Code, VSCodium, Theia, or Xcode for Swift development.
- Navigate source, diagnostics, terminal, and project files by keyboard.
- Verify that editor language tooling uses the intended Swift toolchain.

#### Concept Explanation
Open the project root in the chosen editor and install compatible Swift language support. On macOS, Xcode provides integrated Swift editing and debugging. In VS Code or VSCodium, configure the Swift extension and sourcekit-lsp using the selected toolchain; extension availability differs across marketplaces. Theia may require a compatible extension distribution. Verify diagnostics and symbol navigation rather than relying on syntax coloring alone.

#### Worked Example
```swift
func greet(_ name: String) -> String {
    return "Hello, \(name)!"
}
print(greet("Avery"))
```

#### Expected Behavior or Output
The program prints `Hello, Avery!`. The editor should identify the function and its parameter type.

#### Common Mistakes
- Selecting a different Swift toolchain in the editor than in the terminal.
- Treating syntax coloring as proof that SourceKit-LSP diagnostics work.
- Depending on mouse-only navigation or inaccessible inline diagnostic panels.

#### Activities
1. Open the course project root in the selected editor.
2. Navigate the worked example by line, word, and character.
3. Introduce a type error, locate the diagnostic, and correct it.
4. Run the file from the integrated terminal and system terminal.

#### Accessibility Practice
Test punctuation verbosity, indentation announcements, completion popups, diagnostic navigation, terminal focus, and editor panels with the learner's access technology. Keep a terminal-first workflow available.

#### Skills Checklist
- [ ] I can open the project root and select the intended Swift toolchain.
- [ ] I can navigate and edit Swift source by keyboard.
- [ ] I can locate and correct a compiler or language-server diagnostic.
- [ ] I can run source code without mouse-dependent actions.
- [ ] I can describe editor accessibility limitations and use a workable alternative.

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

#### Reading References
- [Swift Package Manager](https://www.swift.org/documentation/package-manager/)
- [PackageDescription API](https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html)

#### Learning Objectives
- Create and inspect a Swift package.
- Explain the roles of `Package.swift`, source targets, and test targets.
- Add and resolve dependencies with Swift Package Manager.
- Build, test, and run a package from the terminal.

#### Concept Explanation
Use Swift Package Manager for multi-file applications and dependencies. Run `swift package init --type executable` from the project root. The package manifest `Package.swift` declares products, targets, and dependencies. Run `swift package resolve`, `swift build`, `swift test`, and `swift run`. Package artifacts are generated under `.build`; do not edit them directly. For Apple platform applications, Xcode projects and platform SDK configuration may also be required.

#### Worked Example
```swift
let manifestResponsibilities = ["package name", "products", "targets", "dependencies"]
print("Package.swift declares: \(manifestResponsibilities.joined(separator: ", "))")
```

#### Expected Behavior or Output
This manifest declares an executable package target named `CourseDemo`. Swift Package Manager uses it to determine how to build the package.

#### Common Mistakes
- Running package commands from a directory that does not contain `Package.swift`.
- Editing generated files in `.build` instead of the package sources or manifest.
- Adding a dependency without declaring the product in the appropriate target.

#### Activities
1. Initialize an executable package and inspect its directory structure.
2. Run `swift build` and `swift run`.
3. Add a test target and run `swift test`.
4. Add a small external dependency in a practice package and inspect the manifest and resolved package graph.

#### Accessibility Practice
Read `Package.swift` as source text and inspect build/test output sequentially. Document commands and error messages; do not rely on transient editor notifications or mouse-only build controls.

#### Skills Checklist
- [ ] I can initialize a Swift package.
- [ ] I can explain the purpose of `Package.swift` and its targets.
- [ ] I can resolve declared package dependencies.
- [ ] I can build, run, and test from the terminal.
- [ ] I can inspect package output using keyboard-accessible tools.

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

# Unit 8: Files and Exceptions

## Overview

Foundation provides file URLs, FileManager, String file I/O, FileHandle, and Codable. File APIs can throw; handle errors with `do`/`catch`, use `defer` for scope cleanup, and encode structured records with JSONEncoder and JSONDecoder.

## Lesson 8.1: Reading text files

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain reading text files using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Foundation provides file URLs, FileManager, String file I/O, FileHandle, and Codable. File APIs can throw; handle errors with `do`/`catch`, use `defer` for scope cleanup, and encode structured records with JSONEncoder and JSONDecoder.

**Lesson focus:** Reading text files. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
import Foundation
let folder = FileManager.default.temporaryDirectory
let file = folder.appendingPathComponent(UUID().uuidString + ".txt")
try! "Avery studies Swift.\nScores are stored safely.\n".write(to: file, atomically: true, encoding: .utf8)
let contents = try! String(contentsOf: file, encoding: .utf8)
print(contents.trimmingCharacters(in: .whitespacesAndNewlines))
try? FileManager.default.removeItem(at: file)
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- File operations can throw; handle errors instead of assuming success.
- Use explicit encodings and atomic writes for text-file safety.
- A `defer` block runs when the current scope exits, not at an arbitrary later time.

### Activities
1. Create a temporary file fixture and read its contents.
2. Test missing, empty, and malformed files.
3. Append to a file and verify cleanup after the operation.
4. Encode and decode a Codable record; inspect the JSON fields.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain reading text files in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.2: Writing and appending files

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain writing and appending files using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Foundation provides file URLs, FileManager, String file I/O, FileHandle, and Codable. File APIs can throw; handle errors with `do`/`catch`, use `defer` for scope cleanup, and encode structured records with JSONEncoder and JSONDecoder.

**Lesson focus:** Writing and appending files. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
import Foundation
let file = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString + ".txt")
try! "First line\n".write(to: file, atomically: true, encoding: .utf8)
let handle = try! FileHandle(forWritingTo: file)
try! handle.seekToEnd()
try! handle.write(contentsOf: Data("Appended line\n".utf8))
try! handle.close()
print(try! String(contentsOf: file, encoding: .utf8))
try? FileManager.default.removeItem(at: file)
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- File operations can throw; handle errors instead of assuming success.
- Use explicit encodings and atomic writes for text-file safety.
- A `defer` block runs when the current scope exits, not at an arbitrary later time.

### Activities
1. Create a temporary file fixture and read its contents.
2. Test missing, empty, and malformed files.
3. Append to a file and verify cleanup after the operation.
4. Encode and decode a Codable record; inspect the JSON fields.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain writing and appending files in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.3: Errors and throwing functions

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain errors and throwing functions using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Foundation provides file URLs, FileManager, String file I/O, FileHandle, and Codable. File APIs can throw; handle errors with `do`/`catch`, use `defer` for scope cleanup, and encode structured records with JSONEncoder and JSONDecoder.

**Lesson focus:** Errors and throwing functions. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
enum ScoreError: Error {
    case outOfRange
}
func validate(score: Int) throws -> Int {
    guard (0...100).contains(score) else { throw ScoreError.outOfRange }
    return score
}
do {
    print(try validate(score: 82))
    print(try validate(score: 120))
} catch {
    print("Rejected score: \(error)")
}
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- File operations can throw; handle errors instead of assuming success.
- Use explicit encodings and atomic writes for text-file safety.
- A `defer` block runs when the current scope exits, not at an arbitrary later time.

### Activities
1. Create a temporary file fixture and read its contents.
2. Test missing, empty, and malformed files.
3. Append to a file and verify cleanup after the operation.
4. Encode and decode a Codable record; inspect the JSON fields.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain errors and throwing functions in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.4: Resource lifetime and cleanup

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain resource lifetime and cleanup using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Foundation provides file URLs, FileManager, String file I/O, FileHandle, and Codable. File APIs can throw; handle errors with `do`/`catch`, use `defer` for scope cleanup, and encode structured records with JSONEncoder and JSONDecoder.

**Lesson focus:** Resource lifetime and cleanup. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
import Foundation
func writeTemporaryReport() throws -> URL {
    let url = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString + ".txt")
    defer { try? FileManager.default.removeItem(at: url) }
    try "Report complete".write(to: url, atomically: true, encoding: .utf8)
    print(try String(contentsOf: url, encoding: .utf8))
    return url
}
_ = try writeTemporaryReport()
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- File operations can throw; handle errors instead of assuming success.
- Use explicit encodings and atomic writes for text-file safety.
- A `defer` block runs when the current scope exits, not at an arbitrary later time.

### Activities
1. Create a temporary file fixture and read its contents.
2. Test missing, empty, and malformed files.
3. Append to a file and verify cleanup after the operation.
4. Encode and decode a Codable record; inspect the JSON fields.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain resource lifetime and cleanup in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.5: JSON with Codable

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain json with codable using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
Foundation provides file URLs, FileManager, String file I/O, FileHandle, and Codable. File APIs can throw; handle errors with `do`/`catch`, use `defer` for scope cleanup, and encode structured records with JSONEncoder and JSONDecoder.

**Lesson focus:** JSON with Codable. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
import Foundation
struct LearnerRecord: Codable {
    let id: Int
    let name: String
    let scores: [Int]
}
let learner = LearnerRecord(id: 1, name: "Avery", scores: [82, 91, 76])
let data = try! JSONEncoder().encode(learner)
let decoded = try! JSONDecoder().decode(LearnerRecord.self, from: data)
print(String(data: data, encoding: .utf8)!)
print(decoded.name, decoded.scores)
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- File operations can throw; handle errors instead of assuming success.
- Use explicit encodings and atomic writes for text-file safety.
- A `defer` block runs when the current scope exits, not at an arbitrary later time.

### Activities
1. Create a temporary file fixture and read its contents.
2. Test missing, empty, and malformed files.
3. Append to a file and verify cleanup after the operation.
4. Encode and decode a Codable record; inspect the JSON fields.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain json with codable in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

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

# Unit 11: Capstone

## Overview

The capstone is a personal-record manager with stable identifiers, validated create/read/update/delete operations, and Codable persistence. Separate the data model, validation, storage, and command-line interface; verify save/reload and document limitations.

## Lesson 11.1: Requirements and design

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and design using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
The capstone is a personal-record manager with stable identifiers, validated create/read/update/delete operations, and Codable persistence. Separate the data model, validation, storage, and command-line interface; verify save/reload and document limitations.

**Lesson focus:** Requirements and design. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let capstoneRequirements = [
    "Accessible text-first personal record manager",
    "Stable record identifiers",
    "Create, list, search, update, and delete",
    "Validate user input",
    "Save and reload records"
]
print("Capstone design:")
capstoneRequirements.forEach { print("- \($0)") }
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Keep stable identifiers separate from editable record fields.
- Validate before mutating stored records.
- Test save/reload, duplicate identifiers, missing records, and accessibility behavior.

### Activities
1. Specify the record schema and validation rules before coding.
2. Test create, list, search, update, and delete operations.
3. Test duplicate, missing, blank, and invalid values.
4. Test save/reload and document keyboard-first operation and limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain requirements and design in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.2: Data model and storage

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain data model and storage using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
The capstone is a personal-record manager with stable identifiers, validated create/read/update/delete operations, and Codable persistence. Separate the data model, validation, storage, and command-line interface; verify save/reload and document limitations.

**Lesson focus:** Data model and storage. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
import Foundation
struct PersonalRecord: Codable, Identifiable {
    let id: Int
    var title: String
    var description: String
    var category: String
    let createdAt: String
    var updatedAt: String
}
let record = PersonalRecord(id: 1, title: "Study Swift", description: "Review Codable",
                            category: "learning", createdAt: "2026-11-01", updatedAt: "2026-11-01")
print("\(record.id): \(record.title), \(record.category), updated=\(record.updatedAt)")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Keep stable identifiers separate from editable record fields.
- Validate before mutating stored records.
- Test save/reload, duplicate identifiers, missing records, and accessibility behavior.

### Activities
1. Specify the record schema and validation rules before coding.
2. Test create, list, search, update, and delete operations.
3. Test duplicate, missing, blank, and invalid values.
4. Test save/reload and document keyboard-first operation and limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain data model and storage in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.3: Create, read, update, delete

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain create, read, update, delete using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
The capstone is a personal-record manager with stable identifiers, validated create/read/update/delete operations, and Codable persistence. Separate the data model, validation, storage, and command-line interface; verify save/reload and document limitations.

**Lesson focus:** Create, read, update, delete. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
struct Record {
    let id: Int
    var title: String
}
var records = [Record(id: 1, title: "Study Swift")]
records.append(Record(id: 2, title: "Practice optionals"))
let found = records.first { $0.id == 1 }
if let found {
    records[records.firstIndex { $0.id == found.id }!].title = "Study Swift deeply"
}
records.removeAll { $0.id == 2 }
print(records.map(\.title))
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Keep stable identifiers separate from editable record fields.
- Validate before mutating stored records.
- Test save/reload, duplicate identifiers, missing records, and accessibility behavior.

### Activities
1. Specify the record schema and validation rules before coding.
2. Test create, list, search, update, and delete operations.
3. Test duplicate, missing, blank, and invalid values.
4. Test save/reload and document keyboard-first operation and limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain create, read, update, delete in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.4: Validation and tests

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain validation and tests using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
The capstone is a personal-record manager with stable identifiers, validated create/read/update/delete operations, and Codable persistence. Separate the data model, validation, storage, and command-line interface; verify save/reload and document limitations.

**Lesson focus:** Validation and tests. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
import Foundation
func validateTitle(_ value: String) -> Bool {
    !value.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
}
precondition(validateTitle("Study Swift"))
precondition(!validateTitle("   "))
let duplicateIDs = [1, 2, 1]
precondition(Set(duplicateIDs).count != duplicateIDs.count)
print("Validation checks passed")
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Keep stable identifiers separate from editable record fields.
- Validate before mutating stored records.
- Test save/reload, duplicate identifiers, missing records, and accessibility behavior.

### Activities
1. Specify the record schema and validation rules before coding.
2. Test create, list, search, update, and delete operations.
3. Test duplicate, missing, blank, and invalid values.
4. Test save/reload and document keyboard-first operation and limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain validation and tests in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.5: Documentation and presentation

### Reading References
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain documentation and presentation using Swift terminology.
- Apply the relevant language and standard-library features correctly.
- Test normal, boundary, and invalid cases using the shared course data.

### Concept Explanation
The capstone is a personal-record manager with stable identifiers, validated create/read/update/delete operations, and Codable persistence. Separate the data model, validation, storage, and command-line interface; verify save/reload and document limitations.

**Lesson focus:** Documentation and presentation. The example uses Swift-native semantics and a canonical course context rather than mechanically translating Python.

### Worked Example
```swift
let releaseNotes = [
    "Purpose: manage personal learning records",
    "Input: text commands and record fields",
    "Storage: Codable JSON document",
    "Accessibility: keyboard-first, plain-text prompts",
    "Testing: CRUD, validation, and save/reload"
]
print(releaseNotes.joined(separator: "\n"))
```

### Expected Behavior or Output
The example is a self-contained Swift program. Predict the output from the stated values before running it, then compare the actual result. Examples that read input accept a line from standard input; file examples use temporary paths.

### Common Mistakes
- Keep stable identifiers separate from editable record fields.
- Validate before mutating stored records.
- Test save/reload, duplicate identifiers, missing records, and accessibility behavior.

### Activities
1. Specify the record schema and validation rules before coding.
2. Test create, list, search, update, and delete operations.
3. Test duplicate, missing, blank, and invalid values.
4. Test save/reload and document keyboard-first operation and limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect punctuation, braces, optionals, argument labels, and compiler diagnostics. Run from the terminal and read prompts and output sequentially. Do not rely on syntax coloring, color-only status, or mouse-only actions.

### Skills Checklist
- [ ] I can explain documentation and presentation in Swift terminology.
- [ ] I can trace the example and predict its behavior.
- [ ] I can adapt the example to the shared canonical data.
- [ ] I can identify and correct a Swift-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Swift-specific platform and package notes

- Use Swift Package Manager for cross-platform command-line packages and reusable modules.
- iOS, watchOS, tvOS, and many macOS application workflows require Xcode and Apple platform SDKs.
- Foundation provides file handling, JSONEncoder/JSONDecoder, date and URL facilities, and string formatting.
- Use XCTest in a Swift package for a full test suite; the standalone examples use `precondition` for dependency-free smoke checks.
- The introductory CSV example handles simple unquoted rows only. Use a maintained CSV library for quoted commas, escaped quotes, and embedded newlines.
- Swift concurrency uses structured tasks and actors; add concurrency only when the problem requires it and test isolation and cancellation explicitly.
