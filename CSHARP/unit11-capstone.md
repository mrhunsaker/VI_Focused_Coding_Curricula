# Unit 11: Capstone

## Overview

This unit covers accessible personal-data manager, model, persistence, CRUD, tests, documentation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 11.1: Capstone requirements

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The capstone is a structured personal-data manager. Preserve the canonical record fields, implement create/read/update/delete, validate input, persist JSON, test failure cases, and document verified keyboard and assistive-technology behavior.
### Worked Example
```cs
string[] acceptanceCriteria = { "create a record", "list all records", "edit a selected record", "delete a selected record", "save and reload JSON", "validate all user input", "provide screen-reader-friendly text feedback" };
foreach (string criterion in acceptanceCriteria) Console.WriteLine($"[ ] {criterion}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
[ ] create a record
[ ] list all records
[ ] edit a selected record
[ ] delete a selected record
[ ] save and reload JSON
[ ] validate all user input
[ ] provide screen-reader-friendly text feedback
```

### Common Mistakes
- Omitting a required record field or CRUD operation.
- Trusting persisted or user-supplied data without validation.
- Claiming behavior or accessibility that has not been verified.
### Activities
1. Map the example to one capstone requirement and identify its inputs and outputs.
2. Add or modify a canonical record using all required fields.
3. Test a failure path such as duplicate ID, blank title, malformed JSON, or missing record.
4. Document how the behavior is tested and what remains unverified.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can implement the required capstone data model and fields.
- [ ] I can implement the required CRUD operations.
- [ ] I can validate data and handle persistence errors.
- [ ] I can test the application against acceptance criteria.
- [ ] I can document setup, operation, accessibility, and limitations.

## Lesson 11.2: Data model and storage

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The capstone is a structured personal-data manager. Preserve the canonical record fields, implement create/read/update/delete, validate input, persist JSON, test failure cases, and document verified keyboard and assistive-technology behavior.
### Worked Example
```cs
var record = new CapstoneRecord(1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01");
var options = new System.Text.Json.JsonSerializerOptions { PropertyNamingPolicy = System.Text.Json.JsonNamingPolicy.SnakeCaseLower };
string json = System.Text.Json.JsonSerializer.Serialize(record, options); Console.WriteLine(json);
record CapstoneRecord(int Id, string Title, string Description, string Category, string CreatedAt, string UpdatedAt);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
{"id":1,"title":"Course project","description":"Personal data manager","category":"education","created_at":"2026-11-01","updated_at":"2026-11-01"}
```

### Common Mistakes
- Omitting a required record field or CRUD operation.
- Trusting persisted or user-supplied data without validation.
- Claiming behavior or accessibility that has not been verified.
### Activities
1. Map the example to one capstone requirement and identify its inputs and outputs.
2. Add or modify a canonical record using all required fields.
3. Test a failure path such as duplicate ID, blank title, malformed JSON, or missing record.
4. Document how the behavior is tested and what remains unverified.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can implement the required capstone data model and fields.
- [ ] I can implement the required CRUD operations.
- [ ] I can validate data and handle persistence errors.
- [ ] I can test the application against acceptance criteria.
- [ ] I can document setup, operation, accessibility, and limitations.

## Lesson 11.3: Create/read/update/delete

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The capstone is a structured personal-data manager. Preserve the canonical record fields, implement create/read/update/delete, validate input, persist JSON, test failure cases, and document verified keyboard and assistive-technology behavior.
### Worked Example
```cs
var records = new List<CapstoneRecord> { new(1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01") };
records.Add(new CapstoneRecord(2, "Study C#", "Complete functions unit", "learning", "2026-11-01", "2026-11-01"));
var found = records.FirstOrDefault(record => record.Id == 1);
if (found is not null) records[records.IndexOf(found)] = found with { Title = "Updated course project", UpdatedAt = "2026-11-02" };
records.RemoveAll(record => record.Id == 2); foreach (var item in records) Console.WriteLine($"{item.Id}: {item.Title}");
record CapstoneRecord(int Id, string Title, string Description, string Category, string CreatedAt, string UpdatedAt);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
1: Updated course project
```

### Common Mistakes
- Omitting a required record field or CRUD operation.
- Trusting persisted or user-supplied data without validation.
- Claiming behavior or accessibility that has not been verified.
### Activities
1. Map the example to one capstone requirement and identify its inputs and outputs.
2. Add or modify a canonical record using all required fields.
3. Test a failure path such as duplicate ID, blank title, malformed JSON, or missing record.
4. Document how the behavior is tested and what remains unverified.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can implement the required capstone data model and fields.
- [ ] I can implement the required CRUD operations.
- [ ] I can validate data and handle persistence errors.
- [ ] I can test the application against acceptance criteria.
- [ ] I can document setup, operation, accessibility, and limitations.

## Lesson 11.4: Validation and testing

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The capstone is a structured personal-data manager. Preserve the canonical record fields, implement create/read/update/delete, validate input, persist JSON, test failure cases, and document verified keyboard and assistive-technology behavior.
### Worked Example
```cs
static bool IsValidRecord(CapstoneRecord record) => record.Id > 0 && !string.IsNullOrWhiteSpace(record.Title) && !string.IsNullOrWhiteSpace(record.Category);
var sample = new CapstoneRecord(1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01");
if (!IsValidRecord(sample)) throw new Exception("Valid record rejected"); var invalid = sample with { Title = " " };
if (IsValidRecord(invalid)) throw new Exception("Invalid record accepted"); Console.WriteLine("Record validation tests passed.");
record CapstoneRecord(int Id, string Title, string Description, string Category, string CreatedAt, string UpdatedAt);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Record validation tests passed.
```

### Common Mistakes
- Omitting a required record field or CRUD operation.
- Trusting persisted or user-supplied data without validation.
- Claiming behavior or accessibility that has not been verified.
### Activities
1. Map the example to one capstone requirement and identify its inputs and outputs.
2. Add or modify a canonical record using all required fields.
3. Test a failure path such as duplicate ID, blank title, malformed JSON, or missing record.
4. Document how the behavior is tested and what remains unverified.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can implement the required capstone data model and fields.
- [ ] I can implement the required CRUD operations.
- [ ] I can validate data and handle persistence errors.
- [ ] I can test the application against acceptance criteria.
- [ ] I can document setup, operation, accessibility, and limitations.

## Lesson 11.5: Documentation and presentation

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The capstone is a structured personal-data manager. Preserve the canonical record fields, implement create/read/update/delete, validate input, persist JSON, test failure cases, and document verified keyboard and assistive-technology behavior.
### Worked Example
```cs
string[] documentation = { "Project: Accessible Personal Data Manager", "Runtime: .NET 10", "Build: dotnet build", "Run: dotnet run", "Test: dotnet test", "Data: JSON file with six documented fields", "Accessibility: keyboard-first commands and explicit text feedback" };
Console.WriteLine(string.Join(Environment.NewLine, documentation));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Project: Accessible Personal Data Manager
Runtime: .NET 10
Build: dotnet build
Run: dotnet run
Test: dotnet test
Data: JSON file with six documented fields
Accessibility: keyboard-first commands and explicit text feedback
```

### Common Mistakes
- Omitting a required record field or CRUD operation.
- Trusting persisted or user-supplied data without validation.
- Claiming behavior or accessibility that has not been verified.
### Activities
1. Map the example to one capstone requirement and identify its inputs and outputs.
2. Add or modify a canonical record using all required fields.
3. Test a failure path such as duplicate ID, blank title, malformed JSON, or missing record.
4. Document how the behavior is tested and what remains unverified.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can implement the required capstone data model and fields.
- [ ] I can implement the required CRUD operations.
- [ ] I can validate data and handle persistence errors.
- [ ] I can test the application against acceptance criteria.
- [ ] I can document setup, operation, accessibility, and limitations.
## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
