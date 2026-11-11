# Unit 4: Data Structures

## Overview

This unit covers sequence mutation, sorting, immutable records, maps, dictionaries, traversal. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 4.1: Mutable sequences

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# offers generic collections such as List<T> and Dictionary<TKey,TValue>, plus records and structs for data modeling. Select a collection based on whether the problem needs ordered mutable elements, unique keys, or immutable value data.
### Worked Example
```cs
var items = new List<string> { "Notebook", "Pencil" };
items.Insert(1, "Folder"); items.Add("Eraser"); items[0] = "Journal"; items.Remove("Pencil");
Console.WriteLine(string.Join(", ", items));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Journal, Folder, Eraser
```

### Common Mistakes
- Choosing a collection whose mutability or lookup behavior does not fit the task.
- Using an invalid index or missing dictionary key without checking it.
- Assuming enumeration order or duplicate handling that the collection does not guarantee.
### Activities
1. Apply the collection operation to the canonical Notebook, Pencil, and Folder inventory.
2. Add, update, remove, sort, or traverse one additional item and predict the result.
3. Test a duplicate key, missing key, invalid index, or immutable-value constraint.
4. Explain why the chosen C# collection or record type fits this data.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose the appropriate generic collection or record type.
- [ ] I can perform the required add, update, remove, sort, or lookup operation.
- [ ] I can explain mutability, key uniqueness, or value semantics.
- [ ] I can test a missing, duplicate, or boundary case.
- [ ] I can traverse or inspect the data without relying on visual layout.

## Lesson 4.2: Sorting and organizing data

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# offers generic collections such as List<T> and Dictionary<TKey,TValue>, plus records and structs for data modeling. Select a collection based on whether the problem needs ordered mutable elements, unique keys, or immutable value data.
### Worked Example
```cs
var quantities = new List<int> { 10, 3, 4, 1 };
quantities.Sort(); quantities.Reverse();
Console.WriteLine(string.Join(" ", quantities));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
10 4 3 1
```

### Common Mistakes
- Choosing a collection whose mutability or lookup behavior does not fit the task.
- Using an invalid index or missing dictionary key without checking it.
- Assuming enumeration order or duplicate handling that the collection does not guarantee.
### Activities
1. Apply the collection operation to the canonical Notebook, Pencil, and Folder inventory.
2. Add, update, remove, sort, or traverse one additional item and predict the result.
3. Test a duplicate key, missing key, invalid index, or immutable-value constraint.
4. Explain why the chosen C# collection or record type fits this data.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose the appropriate generic collection or record type.
- [ ] I can perform the required add, update, remove, sort, or lookup operation.
- [ ] I can explain mutability, key uniqueness, or value semantics.
- [ ] I can test a missing, duplicate, or boundary case.
- [ ] I can traverse or inspect the data without relying on visual layout.

## Lesson 4.3: Immutable records

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# offers generic collections such as List<T> and Dictionary<TKey,TValue>, plus records and structs for data modeling. Select a collection based on whether the problem needs ordered mutable elements, unique keys, or immutable value data.
### Worked Example
```cs
var point = new Coordinate(3, 4);
Console.WriteLine($"Point: ({point.X}, {point.Y}); distance: {Math.Sqrt(point.X * point.X + point.Y * point.Y):F2}");
readonly record struct Coordinate(int X, int Y);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Point: (3, 4); distance: 5.00
```

### Common Mistakes
- Choosing a collection whose mutability or lookup behavior does not fit the task.
- Using an invalid index or missing dictionary key without checking it.
- Assuming enumeration order or duplicate handling that the collection does not guarantee.
### Activities
1. Apply the collection operation to the canonical Notebook, Pencil, and Folder inventory.
2. Add, update, remove, sort, or traverse one additional item and predict the result.
3. Test a duplicate key, missing key, invalid index, or immutable-value constraint.
4. Explain why the chosen C# collection or record type fits this data.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose the appropriate generic collection or record type.
- [ ] I can perform the required add, update, remove, sort, or lookup operation.
- [ ] I can explain mutability, key uniqueness, or value semantics.
- [ ] I can test a missing, duplicate, or boundary case.
- [ ] I can traverse or inspect the data without relying on visual layout.

## Lesson 4.4: Maps and key-value data

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# offers generic collections such as List<T> and Dictionary<TKey,TValue>, plus records and structs for data modeling. Select a collection based on whether the problem needs ordered mutable elements, unique keys, or immutable value data.
### Worked Example
```cs
var inventory = new Dictionary<string, int> { ["Notebook"] = 3, ["Pencil"] = 10, ["Folder"] = 4 };
inventory["Notebook"] += 1;
Console.WriteLine($"Notebook quantity: {inventory["Notebook"]}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Notebook quantity: 4
```

### Common Mistakes
- Choosing a collection whose mutability or lookup behavior does not fit the task.
- Using an invalid index or missing dictionary key without checking it.
- Assuming enumeration order or duplicate handling that the collection does not guarantee.
### Activities
1. Apply the collection operation to the canonical Notebook, Pencil, and Folder inventory.
2. Add, update, remove, sort, or traverse one additional item and predict the result.
3. Test a duplicate key, missing key, invalid index, or immutable-value constraint.
4. Explain why the chosen C# collection or record type fits this data.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose the appropriate generic collection or record type.
- [ ] I can perform the required add, update, remove, sort, or lookup operation.
- [ ] I can explain mutability, key uniqueness, or value semantics.
- [ ] I can test a missing, duplicate, or boundary case.
- [ ] I can traverse or inspect the data without relying on visual layout.

## Lesson 4.5: Collection traversal

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# offers generic collections such as List<T> and Dictionary<TKey,TValue>, plus records and structs for data modeling. Select a collection based on whether the problem needs ordered mutable elements, unique keys, or immutable value data.
### Worked Example
```cs
var inventory = new Dictionary<string, int> { ["Notebook"] = 3, ["Pencil"] = 10, ["Folder"] = 4 };
foreach (KeyValuePair<string, int> entry in inventory) Console.WriteLine($"{entry.Key} => {entry.Value}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Notebook => 3
Pencil => 10
Folder => 4
```

### Common Mistakes
- Choosing a collection whose mutability or lookup behavior does not fit the task.
- Using an invalid index or missing dictionary key without checking it.
- Assuming enumeration order or duplicate handling that the collection does not guarantee.
### Activities
1. Apply the collection operation to the canonical Notebook, Pencil, and Folder inventory.
2. Add, update, remove, sort, or traverse one additional item and predict the result.
3. Test a duplicate key, missing key, invalid index, or immutable-value constraint.
4. Explain why the chosen C# collection or record type fits this data.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose the appropriate generic collection or record type.
- [ ] I can perform the required add, update, remove, sort, or lookup operation.
- [ ] I can explain mutability, key uniqueness, or value semantics.
- [ ] I can test a missing, duplicate, or boundary case.
- [ ] I can traverse or inspect the data without relying on visual layout.
