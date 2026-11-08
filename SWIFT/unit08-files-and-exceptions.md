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
