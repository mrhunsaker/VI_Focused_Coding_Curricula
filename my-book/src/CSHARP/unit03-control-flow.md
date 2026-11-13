# Unit 3: Control Flow

## Overview

This unit covers Boolean expressions, conditionals, lists or arrays, iteration, string operations. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 3.1: Boolean expressions

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Control flow in C# uses Boolean expressions, if/else, arrays, loops, and immutable string values. Array indexes start at zero; collection lengths and loop bounds must be checked. String methods return new strings rather than mutating the original.
### Worked Example
```cs
int score = 82;
bool validScore = score >= 0 && score <= 100, passed = validScore && score >= 60;
Console.WriteLine($"Valid: {validScore}; passed: {passed}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Valid: True; passed: True
```

### Common Mistakes
- Using an incorrect Boolean boundary or condition order.
- Assuming array indexes start at one or exceed the valid range.
- Assuming string operations mutate the original value.
### Activities
1. Trace the Boolean conditions, branches, collection indexes, or loop iterations in the example.
2. Apply the same operation to the canonical scores 82, 91, 76, and 88.
3. Test a boundary score, empty collection, missing match, or string edge case.
4. Explain the relevant C# control-flow or string/array rule and how you verified it.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write the required Boolean or control-flow construct.
- [ ] I can apply the shared score or text data correctly.
- [ ] I can avoid invalid indexing and loop bounds.
- [ ] I can test boundary and negative cases.
- [ ] I can explain the relevant C# array, string, or branch semantics.

## Lesson 3.2: Chained conditionals

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Control flow in C# uses Boolean expressions, if/else, arrays, loops, and immutable string values. Array indexes start at zero; collection lengths and loop bounds must be checked. String methods return new strings rather than mutating the original.
### Worked Example
```cs
int[] scores = { 59, 60, 70, 80, 90, 100 };
foreach (int score in scores) { string grade = score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : score >= 60 ? "D" : "F"; Console.WriteLine($"{score}: {grade}"); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
59: F
60: D
70: C
80: B
90: A
100: A
```

### Common Mistakes
- Using an incorrect Boolean boundary or condition order.
- Assuming array indexes start at one or exceed the valid range.
- Assuming string operations mutate the original value.
### Activities
1. Trace the Boolean conditions, branches, collection indexes, or loop iterations in the example.
2. Apply the same operation to the canonical scores 82, 91, 76, and 88.
3. Test a boundary score, empty collection, missing match, or string edge case.
4. Explain the relevant C# control-flow or string/array rule and how you verified it.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write the required Boolean or control-flow construct.
- [ ] I can apply the shared score or text data correctly.
- [ ] I can avoid invalid indexing and loop bounds.
- [ ] I can test boundary and negative cases.
- [ ] I can explain the relevant C# array, string, or branch semantics.

## Lesson 3.3: Sequences and indexing

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Control flow in C# uses Boolean expressions, if/else, arrays, loops, and immutable string values. Array indexes start at zero; collection lengths and loop bounds must be checked. String methods return new strings rather than mutating the original.
### Worked Example
```cs
int[] scores = { 82, 91, 76, 88 };
Console.WriteLine($"First: {scores[0]}; fourth: {scores[3]}"); scores[2] = 80;
Console.WriteLine($"Updated third score: {scores[2]}; count: {scores.Length}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
First: 82; fourth: 88
Updated third score: 80; count: 4
```

### Common Mistakes
- Using an incorrect Boolean boundary or condition order.
- Assuming array indexes start at one or exceed the valid range.
- Assuming string operations mutate the original value.
### Activities
1. Trace the Boolean conditions, branches, collection indexes, or loop iterations in the example.
2. Apply the same operation to the canonical scores 82, 91, 76, and 88.
3. Test a boundary score, empty collection, missing match, or string edge case.
4. Explain the relevant C# control-flow or string/array rule and how you verified it.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write the required Boolean or control-flow construct.
- [ ] I can apply the shared score or text data correctly.
- [ ] I can avoid invalid indexing and loop bounds.
- [ ] I can test boundary and negative cases.
- [ ] I can explain the relevant C# array, string, or branch semantics.

## Lesson 3.4: For loops and iteration

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Control flow in C# uses Boolean expressions, if/else, arrays, loops, and immutable string values. Array indexes start at zero; collection lengths and loop bounds must be checked. String methods return new strings rather than mutating the original.
### Worked Example
```cs
int[] scores = { 82, 91, 76, 88 }; int total = 0;
foreach (int score in scores) total += score;
double average = (double)total / scores.Length;
Console.WriteLine($"Total: {total}; average: {average:F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Total: 337; average: 84.25
```

### Common Mistakes
- Using an incorrect Boolean boundary or condition order.
- Assuming array indexes start at one or exceed the valid range.
- Assuming string operations mutate the original value.
### Activities
1. Trace the Boolean conditions, branches, collection indexes, or loop iterations in the example.
2. Apply the same operation to the canonical scores 82, 91, 76, and 88.
3. Test a boundary score, empty collection, missing match, or string edge case.
4. Explain the relevant C# control-flow or string/array rule and how you verified it.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write the required Boolean or control-flow construct.
- [ ] I can apply the shared score or text data correctly.
- [ ] I can avoid invalid indexing and loop bounds.
- [ ] I can test boundary and negative cases.
- [ ] I can explain the relevant C# array, string, or branch semantics.

## Lesson 3.5: String operations

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Control flow in C# uses Boolean expressions, if/else, arrays, loops, and immutable string values. Array indexes start at zero; collection lengths and loop bounds must be checked. String methods return new strings rather than mutating the original.
### Worked Example
```cs
string sample = "A student studies programming. Programming develops problem-solving skills.";
string normalized = sample.ToLowerInvariant();
Console.WriteLine($"Length: {normalized.Length}; contains programming: {normalized.Contains("programming")}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Length: 75; contains programming: True
```

### Common Mistakes
- Using an incorrect Boolean boundary or condition order.
- Assuming array indexes start at one or exceed the valid range.
- Assuming string operations mutate the original value.
### Activities
1. Trace the Boolean conditions, branches, collection indexes, or loop iterations in the example.
2. Apply the same operation to the canonical scores 82, 91, 76, and 88.
3. Test a boundary score, empty collection, missing match, or string edge case.
4. Explain the relevant C# control-flow or string/array rule and how you verified it.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write the required Boolean or control-flow construct.
- [ ] I can apply the shared score or text data correctly.
- [ ] I can avoid invalid indexing and loop bounds.
- [ ] I can test boundary and negative cases.
- [ ] I can explain the relevant C# array, string, or branch semantics.
