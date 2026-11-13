# Unit 9: Testing and Data Analysis

## Overview

This unit covers unit tests, testing stateful types, randomness, text analysis, CSV processing. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 9.1: Testing functions

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Testing and analysis should use deterministic inputs where possible. Verify expected results, test state transitions, seed pseudo-random generators when reproducibility matters, and define text/CSV parsing assumptions explicitly.
### Worked Example
```cs
static int Add(int left, int right) => left + right;
if (Add(2, 3) != 5 || Add(-2, 2) != 0) throw new Exception("Add tests failed");
Console.WriteLine("Add tests passed.");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Add tests passed.
```

### Common Mistakes
- Testing only a happy path and omitting boundary or failure cases.
- Using nondeterministic inputs without a reproducible test strategy.
- Assuming simple string splitting implements the complete text or CSV standard.
### Activities
1. Predict the expected result before running the test or analysis example.
2. Add a positive, negative, boundary, or invalid-data test case.
3. Change one data value and verify the test detects an incorrect result or changed count.
4. Explain the limits of the test, random source, tokenizer, or CSV parsing approach.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write or interpret a test with an explicit expected result.
- [ ] I can test normal, boundary, and failure cases.
- [ ] I can use reproducible inputs where appropriate.
- [ ] I can interpret the analysis result correctly.
- [ ] I can explain limitations in the chosen testing or parsing method.

## Lesson 9.2: Testing stateful objects

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Testing and analysis should use deterministic inputs where possible. Verify expected results, test state transitions, seed pseudo-random generators when reproducibility matters, and define text/CSV parsing assumptions explicitly.
### Worked Example
```cs
var stock = new StockItem("Notebook", 3); stock.Add(2);
if (stock.Quantity != 5) throw new Exception("Quantity test failed"); stock.Add(-1);
if (stock.Quantity != 5) throw new Exception("Invalid update changed quantity"); Console.WriteLine("StockItem state tests passed.");
class StockItem(string name, int quantity) { public string Name { get; } = name; public int Quantity { get; private set; } = quantity; public void Add(int amount) { if (amount > 0) Quantity += amount; } }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
StockItem state tests passed.
```

### Common Mistakes
- Testing only a happy path and omitting boundary or failure cases.
- Using nondeterministic inputs without a reproducible test strategy.
- Assuming simple string splitting implements the complete text or CSV standard.
### Activities
1. Predict the expected result before running the test or analysis example.
2. Add a positive, negative, boundary, or invalid-data test case.
3. Change one data value and verify the test detects an incorrect result or changed count.
4. Explain the limits of the test, random source, tokenizer, or CSV parsing approach.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write or interpret a test with an explicit expected result.
- [ ] I can test normal, boundary, and failure cases.
- [ ] I can use reproducible inputs where appropriate.
- [ ] I can interpret the analysis result correctly.
- [ ] I can explain limitations in the chosen testing or parsing method.

## Lesson 9.3: Random values

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Testing and analysis should use deterministic inputs where possible. Verify expected results, test state transitions, seed pseudo-random generators when reproducibility matters, and define text/CSV parsing assumptions explicitly.
### Worked Example
```cs
var random = new Random(42); int dieRoll = random.Next(1, 7); double sample = random.NextDouble();
string[] choices = { "red", "blue", "green" }; string choice = choices[random.Next(choices.Length)];
Console.WriteLine($"Roll: {dieRoll}; sample: {sample:F3}; choice: {choice}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Roll: 5; sample: 0.141; choice: red
```

### Common Mistakes
- Testing only a happy path and omitting boundary or failure cases.
- Using nondeterministic inputs without a reproducible test strategy.
- Assuming simple string splitting implements the complete text or CSV standard.
### Activities
1. Predict the expected result before running the test or analysis example.
2. Add a positive, negative, boundary, or invalid-data test case.
3. Change one data value and verify the test detects an incorrect result or changed count.
4. Explain the limits of the test, random source, tokenizer, or CSV parsing approach.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write or interpret a test with an explicit expected result.
- [ ] I can test normal, boundary, and failure cases.
- [ ] I can use reproducible inputs where appropriate.
- [ ] I can interpret the analysis result correctly.
- [ ] I can explain limitations in the chosen testing or parsing method.

## Lesson 9.4: Text analysis

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Testing and analysis should use deterministic inputs where possible. Verify expected results, test state transitions, seed pseudo-random generators when reproducibility matters, and define text/CSV parsing assumptions explicitly.
### Worked Example
```cs
string sample = "A student studies programming. Programming develops problem-solving skills.";
int letters = sample.Count(char.IsLetter), spaces = sample.Count(char.IsWhiteSpace);
int occurrences = sample.Split(' ', StringSplitOptions.RemoveEmptyEntries).Count(word => word.Trim('.', ',').Equals("programming", StringComparison.OrdinalIgnoreCase));
Console.WriteLine($"Letters: {letters}; spaces: {spaces}; programming occurrences: {occurrences}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Letters: 65; spaces: 7; programming occurrences: 2
```

### Common Mistakes
- Testing only a happy path and omitting boundary or failure cases.
- Using nondeterministic inputs without a reproducible test strategy.
- Assuming simple string splitting implements the complete text or CSV standard.
### Activities
1. Predict the expected result before running the test or analysis example.
2. Add a positive, negative, boundary, or invalid-data test case.
3. Change one data value and verify the test detects an incorrect result or changed count.
4. Explain the limits of the test, random source, tokenizer, or CSV parsing approach.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write or interpret a test with an explicit expected result.
- [ ] I can test normal, boundary, and failure cases.
- [ ] I can use reproducible inputs where appropriate.
- [ ] I can interpret the analysis result correctly.
- [ ] I can explain limitations in the chosen testing or parsing method.

## Lesson 9.5: CSV records

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Testing and analysis should use deterministic inputs where possible. Verify expected results, test state transitions, seed pseudo-random generators when reproducibility matters, and define text/CSV parsing assumptions explicitly.
### Worked Example
```cs
string row = "001,Avery,Student,92,true"; string[] fields = row.Split(',');
string studentId = fields[0], firstName = fields[1], lastName = fields[2]; int score = int.Parse(fields[3]); bool active = bool.Parse(fields[4]);
Console.WriteLine($"{studentId}: {firstName} {lastName}, score {score}, active {active}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
001: Avery Student, score 92, active True
```

### Common Mistakes
- Testing only a happy path and omitting boundary or failure cases.
- Using nondeterministic inputs without a reproducible test strategy.
- Assuming simple string splitting implements the complete text or CSV standard.
### Activities
1. Predict the expected result before running the test or analysis example.
2. Add a positive, negative, boundary, or invalid-data test case.
3. Change one data value and verify the test detects an incorrect result or changed count.
4. Explain the limits of the test, random source, tokenizer, or CSV parsing approach.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write or interpret a test with an explicit expected result.
- [ ] I can test normal, boundary, and failure cases.
- [ ] I can use reproducible inputs where appropriate.
- [ ] I can interpret the analysis result correctly.
- [ ] I can explain limitations in the chosen testing or parsing method.
