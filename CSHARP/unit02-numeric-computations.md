# Unit 2: Numeric Computations

## Overview

This unit covers development process, expressions, assignment, input/output, conversions, arithmetic, math library. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 2.1: Design and tracing

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# uses statically typed expressions and the .NET Base Class Library. Follow values from input through conversion and calculation; use explicit types, named intermediate values, and a stated policy for parsing, culture, precision, and formatting.
### Worked Example
```cs
double bill = 24.50, tipRate = 0.15;
double tip = bill * tipRate, total = bill + tip;
Console.WriteLine($"Bill: {bill:F2}; tip: {tip:F2}; total: {total:F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Bill: 24.50; tip: 3.67; total: 28.18
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Using the wrong numeric type or conversion for the value being processed.
- Ignoring input parsing failures or culture-dependent formatting.
- Relying on implicit precedence or rounding without stating the intended calculation.
### Activities
1. Calculate the expected result for the canonical bill, score, or measurement before running the example.
2. Change one canonical input and verify which intermediate and final values change.
3. Test malformed text, a boundary value, or a different numeric representation as appropriate.
4. Explain the selected type, conversion, precedence, or formatting rule in C#.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose appropriate numeric types and conversions.
- [ ] I can explain the expression and calculation order.
- [ ] I can reproduce the canonical result.
- [ ] I can handle an invalid or boundary input.
- [ ] I can explain the relevant .NET numeric or Math API.

## Lesson 2.2: Expressions and assignment

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# uses statically typed expressions and the .NET Base Class Library. Follow values from input through conversion and calculation; use explicit types, named intermediate values, and a stated policy for parsing, culture, precision, and formatting.
### Worked Example
```cs
double score = 70.0;
double adjusted = (score + 12.5) * 1.10;
score += 12.5;
Console.WriteLine($"Adjusted: {adjusted:F2}; updated score: {score:F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Adjusted: 90.75; updated score: 82.50
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Using the wrong numeric type or conversion for the value being processed.
- Ignoring input parsing failures or culture-dependent formatting.
- Relying on implicit precedence or rounding without stating the intended calculation.
### Activities
1. Calculate the expected result for the canonical bill, score, or measurement before running the example.
2. Change one canonical input and verify which intermediate and final values change.
3. Test malformed text, a boundary value, or a different numeric representation as appropriate.
4. Explain the selected type, conversion, precedence, or formatting rule in C#.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose appropriate numeric types and conversions.
- [ ] I can explain the expression and calculation order.
- [ ] I can reproduce the canonical result.
- [ ] I can handle an invalid or boundary input.
- [ ] I can explain the relevant .NET numeric or Math API.

## Lesson 2.3: Input and output

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# uses statically typed expressions and the .NET Base Class Library. Follow values from input through conversion and calculation; use explicit types, named intermediate values, and a stated policy for parsing, culture, precision, and formatting.
### Worked Example
```cs
Console.SetIn(new StringReader("Avery\n6\n7\n"));
Console.Write("Name: "); string name = Console.ReadLine() ?? "";
int first = int.Parse(Console.ReadLine() ?? "0"), second = int.Parse(Console.ReadLine() ?? "0");
Console.WriteLine($"Hello, {name}. Sum: {first + second}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Name: Hello, Avery. Sum: 13
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Using the wrong numeric type or conversion for the value being processed.
- Ignoring input parsing failures or culture-dependent formatting.
- Relying on implicit precedence or rounding without stating the intended calculation.
### Activities
1. Calculate the expected result for the canonical bill, score, or measurement before running the example.
2. Change one canonical input and verify which intermediate and final values change.
3. Test malformed text, a boundary value, or a different numeric representation as appropriate.
4. Explain the selected type, conversion, precedence, or formatting rule in C#.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose appropriate numeric types and conversions.
- [ ] I can explain the expression and calculation order.
- [ ] I can reproduce the canonical result.
- [ ] I can handle an invalid or boundary input.
- [ ] I can explain the relevant .NET numeric or Math API.

## Lesson 2.4: Numeric conversions and mathematics

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# uses statically typed expressions and the .NET Base Class Library. Follow values from input through conversion and calculation; use explicit types, named intermediate values, and a stated policy for parsing, culture, precision, and formatting.
### Worked Example
```cs
string heightText = "1.72";
if (double.TryParse(heightText, System.Globalization.CultureInfo.InvariantCulture, out double heightM))
    Console.WriteLine($"{heightM:F2} m = {heightM * 100.0:F0} cm");
else Console.WriteLine("Enter a valid measurement.");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
1.72 m = 172 cm
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Using the wrong numeric type or conversion for the value being processed.
- Ignoring input parsing failures or culture-dependent formatting.
- Relying on implicit precedence or rounding without stating the intended calculation.
### Activities
1. Calculate the expected result for the canonical bill, score, or measurement before running the example.
2. Change one canonical input and verify which intermediate and final values change.
3. Test malformed text, a boundary value, or a different numeric representation as appropriate.
4. Explain the selected type, conversion, precedence, or formatting rule in C#.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose appropriate numeric types and conversions.
- [ ] I can explain the expression and calculation order.
- [ ] I can reproduce the canonical result.
- [ ] I can handle an invalid or boundary input.
- [ ] I can explain the relevant .NET numeric or Math API.

## Lesson 2.5: Using the Math Library

### Reading References
- Microsoft Learn: System.Math API reference.
- Corresponding Python lesson on mathematical functions and geometric calculations.

### Learning Objectives
- Use System.Math for common mathematical operations.
- Calculate circle area and circumference using Math.PI.
- Calculate distance from the origin using Math.Sqrt and Math.Pow.

### Concept Explanation
The .NET System.Math class provides mathematical constants and methods such as PI, Pow, Sqrt, Abs, and Round. C# accesses these static members through the Math type. The distance from the origin to (x, y) is the square root of x squared plus y squared. Floating-point values should be formatted or rounded according to an explicit display requirement.

### Worked Example
```cs
double radius = 3.0;
double area = Math.PI * Math.Pow(radius, 2);
double circumference = 2.0 * Math.PI * radius;
double distance = Math.Sqrt(Math.Pow(3.0, 2) + Math.Pow(4.0, 2));
Console.WriteLine($"Area: {area:F2}; circumference: {circumference:F2}; distance: {distance:F2}");
```

**Trace:** area is approximately 28.27, circumference is approximately 18.85, and distance from (3, 4) to the origin is 5.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Area: 28.27; circumference: 18.85; distance: 5.00
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Using an approximate value of pi when Math.PI is available.
- Passing a diameter where the formula expects a radius.
- Taking the square root before adding both squared coordinate values.

### Activities
1. Calculate area and circumference for a circle with radius 3.
2. Calculate distance from the origin to (3, 4) and verify the 5-unit result.
3. Change the radius to zero and predict the outputs.
4. Compare the full double value with F2 formatted output.

### Accessibility Practice
Read the complete expressions, including parentheses and method names. Verify that formatted values have explicit labels and units.

### Skills Checklist
- [ ] I can locate and use Math.PI, Math.Pow, and Math.Sqrt.
- [ ] I can calculate circle area and circumference.
- [ ] I can calculate distance from the origin.
- [ ] I can explain floating-point precision and formatting.
- [ ] I can test a zero-radius boundary case.
