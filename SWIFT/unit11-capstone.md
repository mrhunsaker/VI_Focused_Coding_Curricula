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
The encoder emits the six shared record fields using the canonical snake_case JSON names. Sorted keys make the captured output deterministic.

```text
{"category":"learning","created_at":"2026-11-01","description":"Review Codable","id":1,"title":"Study Swift","updated_at":"2026-11-01"}
Decoded record: 1, Study Swift, learning
```

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
do {
    let encoder = JSONEncoder()
    encoder.keyEncodingStrategy = .convertToSnakeCase
    encoder.outputFormatting = [.sortedKeys]
    let json = try encoder.encode(record)
    print(String(decoding: json, as: UTF8.self))
    let decoder = JSONDecoder()
    decoder.keyDecodingStrategy = .convertFromSnakeCase
    let restored = try decoder.decode(PersonalRecord.self, from: json)
    print("Decoded record: \(restored.id), \(restored.title), \(restored.category)")
} catch {
    print("JSON round trip failed: \(error)")
}
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
## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
