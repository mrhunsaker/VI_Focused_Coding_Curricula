# Unit 8: Files and Exceptions

## Overview

This unit covers read/write text, resource lifetime, error handling, JSON serialization and persistence. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 8.1: Reading text files

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The .NET file and serialization APIs provide text I/O, exception handling, deterministic disposal, and JSON persistence. Resolve relative paths from the working directory, handle expected failures, and dispose IDisposable resources.
### Worked Example
```cs
string path = Path.Combine(Path.GetTempPath(), "csharp-notes.txt");
File.WriteAllLines(path, new[] { "First line", "Second line" });
foreach (string line in File.ReadLines(path)) Console.WriteLine(line);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
First line
Second line
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Resolving relative paths from the wrong working directory.
- Overwriting data when append or safe replacement is required.
- Failing to handle expected I/O/serialization errors or dispose resources.
### Activities
1. Run the file or serialization example using a temporary test file and inspect its contents.
2. Test a missing file, malformed JSON, or an access failure in a controlled case.
3. Change the operation from replace to append, or move resource use across its scope.
4. Explain path resolution, exception handling, serialization, or disposal behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can use the appropriate .NET file or serialization API.
- [ ] I can resolve paths from the correct working directory.
- [ ] I can handle expected I/O or data errors.
- [ ] I can dispose resources deterministically.
- [ ] I can verify stored and restored data.

## Lesson 8.2: Writing and appending files

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The .NET file and serialization APIs provide text I/O, exception handling, deterministic disposal, and JSON persistence. Resolve relative paths from the working directory, handle expected failures, and dispose IDisposable resources.
### Worked Example
```cs
string path = Path.Combine(Path.GetTempPath(), "csharp-notes.txt");
File.WriteAllText(path, "First note\n"); File.AppendAllText(path, "Second note\n");
Console.Write(File.ReadAllText(path));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
First note
Second note
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Resolving relative paths from the wrong working directory.
- Overwriting data when append or safe replacement is required.
- Failing to handle expected I/O/serialization errors or dispose resources.
### Activities
1. Run the file or serialization example using a temporary test file and inspect its contents.
2. Test a missing file, malformed JSON, or an access failure in a controlled case.
3. Change the operation from replace to append, or move resource use across its scope.
4. Explain path resolution, exception handling, serialization, or disposal behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can use the appropriate .NET file or serialization API.
- [ ] I can resolve paths from the correct working directory.
- [ ] I can handle expected I/O or data errors.
- [ ] I can dispose resources deterministically.
- [ ] I can verify stored and restored data.

## Lesson 8.3: Errors and exceptions

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The .NET file and serialization APIs provide text I/O, exception handling, deterministic disposal, and JSON persistence. Resolve relative paths from the working directory, handle expected failures, and dispose IDisposable resources.
### Worked Example
```cs
try { int score = int.Parse("not-a-number"); Console.WriteLine(score); }
catch (FormatException error) { Console.WriteLine($"Invalid numeric input: {error.Message}"); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Invalid numeric input: The input string 'not-a-number' was not in a correct format.
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Resolving relative paths from the wrong working directory.
- Overwriting data when append or safe replacement is required.
- Failing to handle expected I/O/serialization errors or dispose resources.
### Activities
1. Run the file or serialization example using a temporary test file and inspect its contents.
2. Test a missing file, malformed JSON, or an access failure in a controlled case.
3. Change the operation from replace to append, or move resource use across its scope.
4. Explain path resolution, exception handling, serialization, or disposal behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can use the appropriate .NET file or serialization API.
- [ ] I can resolve paths from the correct working directory.
- [ ] I can handle expected I/O or data errors.
- [ ] I can dispose resources deterministically.
- [ ] I can verify stored and restored data.

## Lesson 8.4: Resource cleanup

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The .NET file and serialization APIs provide text I/O, exception handling, deterministic disposal, and JSON persistence. Resolve relative paths from the working directory, handle expected failures, and dispose IDisposable resources.
### Worked Example
```cs
using (var writer = new StringWriter()) { writer.WriteLine("First record"); writer.WriteLine("Second record"); Console.Write(writer.ToString()); }
Console.WriteLine("Writer scope ended and the resource was disposed.");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
First record
Second record
Writer scope ended and the resource was disposed.
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Resolving relative paths from the wrong working directory.
- Overwriting data when append or safe replacement is required.
- Failing to handle expected I/O/serialization errors or dispose resources.
### Activities
1. Run the file or serialization example using a temporary test file and inspect its contents.
2. Test a missing file, malformed JSON, or an access failure in a controlled case.
3. Change the operation from replace to append, or move resource use across its scope.
4. Explain path resolution, exception handling, serialization, or disposal behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can use the appropriate .NET file or serialization API.
- [ ] I can resolve paths from the correct working directory.
- [ ] I can handle expected I/O or data errors.
- [ ] I can dispose resources deterministically.
- [ ] I can verify stored and restored data.

## Lesson 8.5: JSON persistence

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The .NET file and serialization APIs provide text I/O, exception handling, deterministic disposal, and JSON persistence. Resolve relative paths from the working directory, handle expected failures, and dispose IDisposable resources.
### Worked Example
```cs
var record = new CapstoneRecord(1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01");
string json = System.Text.Json.JsonSerializer.Serialize(record);
var restored = System.Text.Json.JsonSerializer.Deserialize<CapstoneRecord>(json);
Console.WriteLine(json); Console.WriteLine(restored?.Title);
record CapstoneRecord(int Id, string Title, string Description, string Category, string CreatedAt, string UpdatedAt);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
{"Id":1,"Title":"Course project","Description":"Personal data manager","Category":"education","CreatedAt":"2026-11-01","UpdatedAt":"2026-11-01"}
Course project
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Resolving relative paths from the wrong working directory.
- Overwriting data when append or safe replacement is required.
- Failing to handle expected I/O/serialization errors or dispose resources.
### Activities
1. Run the file or serialization example using a temporary test file and inspect its contents.
2. Test a missing file, malformed JSON, or an access failure in a controlled case.
3. Change the operation from replace to append, or move resource use across its scope.
4. Explain path resolution, exception handling, serialization, or disposal behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can use the appropriate .NET file or serialization API.
- [ ] I can resolve paths from the correct working directory.
- [ ] I can handle expected I/O or data errors.
- [ ] I can dispose resources deterministically.
- [ ] I can verify stored and restored data.
