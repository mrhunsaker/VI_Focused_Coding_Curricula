# Unit 5: Input and Iteration

## Overview

This unit covers input validation, sentinel loops, while loops, flags, break/continue, infinite-loop prevention. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 5.1: Input and validation

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Console input is text and must be parsed and validated before use. while, foreach, break, and continue control repetition; every loop needs a clear exit condition and progress toward termination.
### Worked Example
```cs
var input = new Queue<string>(new[] { "16", "abc", "131" });
while (input.Count > 0) { string candidate = input.Dequeue(); if (int.TryParse(candidate, out int age) && age >= 0 && age <= 130) Console.WriteLine($"Accepted age: {age}"); else Console.WriteLine($"Invalid age: {candidate}"); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Accepted age: 16
Invalid age: abc
Invalid age: 131
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Treating parsed text as valid domain data without checking it.
- Failing to update loop state or provide a terminating condition.
- Using break or continue when the other control-flow operation is intended.
### Activities
1. Trace the input or loop state after each iteration of the worked example.
2. Test valid input, malformed input, and one domain-boundary value.
3. Change the sentinel, flag, or attempt limit and predict when the loop terminates.
4. Explain how the code guarantees progress and avoids an unbounded loop.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can parse and validate input before using it.
- [ ] I can implement the required loop or control-flow operation.
- [ ] I can identify the loop's termination condition.
- [ ] I can test valid and invalid paths.
- [ ] I can explain how the code avoids an infinite loop.

## Lesson 5.2: While loops

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Console input is text and must be parsed and validated before use. while, foreach, break, and continue control repetition; every loop needs a clear exit condition and progress toward termination.
### Worked Example
```cs
int[] values = { 1, 2, 3, 0, 9 }; int index = 0, total = 0;
while (index < values.Length && values[index] != 0) { total += values[index]; index++; }
Console.WriteLine($"Sum before sentinel: {total}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Sum before sentinel: 6
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Treating parsed text as valid domain data without checking it.
- Failing to update loop state or provide a terminating condition.
- Using break or continue when the other control-flow operation is intended.
### Activities
1. Trace the input or loop state after each iteration of the worked example.
2. Test valid input, malformed input, and one domain-boundary value.
3. Change the sentinel, flag, or attempt limit and predict when the loop terminates.
4. Explain how the code guarantees progress and avoids an unbounded loop.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can parse and validate input before using it.
- [ ] I can implement the required loop or control-flow operation.
- [ ] I can identify the loop's termination condition.
- [ ] I can test valid and invalid paths.
- [ ] I can explain how the code avoids an infinite loop.

## Lesson 5.3: Flags and break

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Console input is text and must be parsed and validated before use. while, foreach, break, and continue control repetition; every loop needs a clear exit condition and progress toward termination.
### Worked Example
```cs
string[] names = { "Avery", "Jordan", "Sam" }; bool found = false;
foreach (string name in names) { if (name == "Jordan") { found = true; break; } }
Console.WriteLine($"Jordan found: {found}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Jordan found: True
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Treating parsed text as valid domain data without checking it.
- Failing to update loop state or provide a terminating condition.
- Using break or continue when the other control-flow operation is intended.
### Activities
1. Trace the input or loop state after each iteration of the worked example.
2. Test valid input, malformed input, and one domain-boundary value.
3. Change the sentinel, flag, or attempt limit and predict when the loop terminates.
4. Explain how the code guarantees progress and avoids an unbounded loop.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can parse and validate input before using it.
- [ ] I can implement the required loop or control-flow operation.
- [ ] I can identify the loop's termination condition.
- [ ] I can test valid and invalid paths.
- [ ] I can explain how the code avoids an infinite loop.

## Lesson 5.4: Continue and filtering

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Console input is text and must be parsed and validated before use. while, foreach, break, and continue control repetition; every loop needs a clear exit condition and progress toward termination.
### Worked Example
```cs
int[] values = { -2, 3, 0, 5, -1 };
foreach (int value in values) { if (value <= 0) continue; Console.WriteLine(value); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
3
5
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Treating parsed text as valid domain data without checking it.
- Failing to update loop state or provide a terminating condition.
- Using break or continue when the other control-flow operation is intended.
### Activities
1. Trace the input or loop state after each iteration of the worked example.
2. Test valid input, malformed input, and one domain-boundary value.
3. Change the sentinel, flag, or attempt limit and predict when the loop terminates.
4. Explain how the code guarantees progress and avoids an unbounded loop.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can parse and validate input before using it.
- [ ] I can implement the required loop or control-flow operation.
- [ ] I can identify the loop's termination condition.
- [ ] I can test valid and invalid paths.
- [ ] I can explain how the code avoids an infinite loop.

## Lesson 5.5: Infinite-loop prevention

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Console input is text and must be parsed and validated before use. while, foreach, break, and continue control repetition; every loop needs a clear exit condition and progress toward termination.
### Worked Example
```cs
int attempts = 0; bool valid = false;
while (!valid && attempts < 3) { attempts++; valid = attempts == 2; }
Console.WriteLine($"Attempts: {attempts}; valid: {valid}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Attempts: 2; valid: True
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Treating parsed text as valid domain data without checking it.
- Failing to update loop state or provide a terminating condition.
- Using break or continue when the other control-flow operation is intended.
### Activities
1. Trace the input or loop state after each iteration of the worked example.
2. Test valid input, malformed input, and one domain-boundary value.
3. Change the sentinel, flag, or attempt limit and predict when the loop terminates.
4. Explain how the code guarantees progress and avoids an unbounded loop.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can parse and validate input before using it.
- [ ] I can implement the required loop or control-flow operation.
- [ ] I can identify the loop's termination condition.
- [ ] I can test valid and invalid paths.
- [ ] I can explain how the code avoids an infinite loop.
