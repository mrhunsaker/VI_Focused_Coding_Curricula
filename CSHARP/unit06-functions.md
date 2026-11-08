# Unit 6: Functions

## Overview

This unit covers definitions, parameters, arguments, return values, scope, collection parameters, variadic functions. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 6.1: Defining functions

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# methods declare parameter and return types. Use parameters to make dependencies explicit, return values to separate computation from presentation, and collection interfaces or params when they improve the method contract.
### Worked Example
```cs
static double CalculateTotal(double bill, double rate) { double tip = bill * rate; return bill + tip; }
Console.WriteLine($"Total: {CalculateTotal(24.50, 0.15):F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Total: 28.18
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Confusing a parameter with an argument or a returned value with printed output.
- Choosing a method signature that does not express its input/output contract.
- Ignoring empty collections, optional values, or variadic edge cases.
### Activities
1. Call the method with the canonical bill/rate or score values and predict its return value.
2. Add a second call with different arguments, including a named or optional argument where relevant.
3. Test empty input, zero arguments, or another edge case for the method contract.
4. Explain the method signature, parameter semantics, and return behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can declare a method with an appropriate signature.
- [ ] I can pass arguments and use the return value correctly.
- [ ] I can handle the method's edge cases.
- [ ] I can reuse the method with different inputs.
- [ ] I can explain the method contract and C# parameter behavior.

## Lesson 6.2: Parameters and arguments

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# methods declare parameter and return types. Use parameters to make dependencies explicit, return values to separate computation from presentation, and collection interfaces or params when they improve the method contract.
### Worked Example
```cs
static string DescribeScore(string name, int score, string label = "Score") => $"{name} — {label}: {score}";
Console.WriteLine(DescribeScore("Avery", 92));
Console.WriteLine(DescribeScore(score: 92, name: "Avery", label: "Final"));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Avery — Score: 92
Avery — Final: 92
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Confusing a parameter with an argument or a returned value with printed output.
- Choosing a method signature that does not express its input/output contract.
- Ignoring empty collections, optional values, or variadic edge cases.
### Activities
1. Call the method with the canonical bill/rate or score values and predict its return value.
2. Add a second call with different arguments, including a named or optional argument where relevant.
3. Test empty input, zero arguments, or another edge case for the method contract.
4. Explain the method signature, parameter semantics, and return behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can declare a method with an appropriate signature.
- [ ] I can pass arguments and use the return value correctly.
- [ ] I can handle the method's edge cases.
- [ ] I can reuse the method with different inputs.
- [ ] I can explain the method contract and C# parameter behavior.

## Lesson 6.3: Return values

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# methods declare parameter and return types. Use parameters to make dependencies explicit, return values to separate computation from presentation, and collection interfaces or params when they improve the method contract.
### Worked Example
```cs
static double CalculateTip(double bill, double rate) => bill * rate;
double tip = CalculateTip(24.50, 0.15), total = 24.50 + tip;
Console.WriteLine($"Tip: {tip:F2}; total: {total:F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Tip: 3.67; total: 28.18
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Confusing a parameter with an argument or a returned value with printed output.
- Choosing a method signature that does not express its input/output contract.
- Ignoring empty collections, optional values, or variadic edge cases.
### Activities
1. Call the method with the canonical bill/rate or score values and predict its return value.
2. Add a second call with different arguments, including a named or optional argument where relevant.
3. Test empty input, zero arguments, or another edge case for the method contract.
4. Explain the method signature, parameter semantics, and return behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can declare a method with an appropriate signature.
- [ ] I can pass arguments and use the return value correctly.
- [ ] I can handle the method's edge cases.
- [ ] I can reuse the method with different inputs.
- [ ] I can explain the method contract and C# parameter behavior.

## Lesson 6.4: Functions over collections

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# methods declare parameter and return types. Use parameters to make dependencies explicit, return values to separate computation from presentation, and collection interfaces or params when they improve the method contract.
### Worked Example
```cs
static double Average(IReadOnlyList<int> scores) => scores.Count == 0 ? 0.0 : scores.Average();
int[] scores = { 82, 91, 76, 88 };
Console.WriteLine($"Average: {Average(scores):F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Average: 84.25
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Confusing a parameter with an argument or a returned value with printed output.
- Choosing a method signature that does not express its input/output contract.
- Ignoring empty collections, optional values, or variadic edge cases.
### Activities
1. Call the method with the canonical bill/rate or score values and predict its return value.
2. Add a second call with different arguments, including a named or optional argument where relevant.
3. Test empty input, zero arguments, or another edge case for the method contract.
4. Explain the method signature, parameter semantics, and return behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can declare a method with an appropriate signature.
- [ ] I can pass arguments and use the return value correctly.
- [ ] I can handle the method's edge cases.
- [ ] I can reuse the method with different inputs.
- [ ] I can explain the method contract and C# parameter behavior.

## Lesson 6.5: Scope and variadic arguments

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# methods declare parameter and return types. Use parameters to make dependencies explicit, return values to separate computation from presentation, and collection interfaces or params when they improve the method contract.
### Worked Example
```cs
static int Sum(params int[] values) { int total = 0; foreach (int value in values) total += value; return total; }
Console.WriteLine(Sum(2, 3, 4)); Console.WriteLine(Sum(82, 91, 76, 88));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
9
337
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Confusing a parameter with an argument or a returned value with printed output.
- Choosing a method signature that does not express its input/output contract.
- Ignoring empty collections, optional values, or variadic edge cases.
### Activities
1. Call the method with the canonical bill/rate or score values and predict its return value.
2. Add a second call with different arguments, including a named or optional argument where relevant.
3. Test empty input, zero arguments, or another edge case for the method contract.
4. Explain the method signature, parameter semantics, and return behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can declare a method with an appropriate signature.
- [ ] I can pass arguments and use the return value correctly.
- [ ] I can handle the method's edge cases.
- [ ] I can reuse the method with different inputs.
- [ ] I can explain the method contract and C# parameter behavior.
