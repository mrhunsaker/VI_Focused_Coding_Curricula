# Unit 2: Numeric Computations

## Overview

This unit covers development process, expressions, assignment, input/output, conversions, arithmetic, math library. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 2.1: Design and tracing

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Design and tracing is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: calculate the tip from the bill and keep the rate as a fraction; separate intermediate values to make tracing possible.

### Worked Example
```cpp
const double bill = 24.50; const double tip = bill * 0.15; std::cout << "Tip: $" << tip << "; total: $" << bill + tip << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Tip: $3.675; total: $28.175
```

### Common Mistakes
- Printing currency without a defined rounding/formatting policy can misrepresent fractional cents.
- Calculate the tip from the bill and keep the rate as a fraction.
- Separate intermediate values to make tracing possible.

### Activities
1. Trace the design and tracing example and predict its output before compiling.
2. Adapt the example to the $24.50 bill and 15% tip and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C++ terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 2.2: Expressions and assignment

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Expressions and assignment is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: use compound assignment without overwriting prior values; distinguish percentage rates from percentage points; avoid narrowing conversions.

### Worked Example
```cpp
double score = 70.0; score += 12.5; score *= 1.1; std::cout << "Adjusted score: " << score << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Adjusted score: 90.75
```

### Common Mistakes
- Use compound assignment without overwriting prior values.
- Distinguish percentage rates from percentage points.
- Avoid narrowing conversions.

### Activities
1. Trace the expressions and assignment example and predict its output before compiling.
2. Adapt the example to the $24.50 bill and 15% tip and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C++ terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 2.3: Input and output

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Input and output is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: check stream extraction before using input; handle multiword text with getline; account for the pending newline after formatted input.

### Worked Example
```cpp
std::istringstream input("Avery 6 7"); std::string name; int first = 0, second = 0; if (input >> name >> first >> second) std::cout << "Hello, " << name << "; sum: " << first + second << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Hello, Avery; sum: 13
```

### Common Mistakes
- Check stream extraction before using input.
- Handle multiword text with getline.
- Account for the pending newline after formatted input.

### Activities
1. Trace the input and output example and predict its output before compiling.
2. Adapt the example to the $24.50 bill and 15% tip and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C++ terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 2.4: Numeric conversions and mathematics

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Numeric conversions and mathematics is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: cast before division to avoid integer truncation; define behavior for invalid square-root inputs; distinguish rounding from truncation.

### Worked Example
```cpp
const int completed = 7, total = 10; const double ratio = static_cast<double>(completed) / total; std::cout << "Percent: " << ratio * 100.0 << "; rounded: " << std::round(ratio * 100.0) << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Percent: 70; rounded: 70
```

### Common Mistakes
- Cast before division to avoid integer truncation.
- Define behavior for invalid square-root inputs.
- Distinguish rounding from truncation.

### Activities
1. Trace the numeric conversions and mathematics example and predict its output before compiling.
2. Adapt the example to the $24.50 bill and 15% tip and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain numeric conversions and mathematics using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for the $24.50 bill and 15% tip without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

## Lesson 2.5: Using the Math Library

### Reading References
- C++ standard library documentation for `<cmath>`.
- Python Unit 2.5 for the corresponding circle and distance problems.

### Learning Objectives
- Include and use mathematical functions from `<cmath>`.
- Calculate a circle's area and circumference.
- Calculate distance from the origin using the Pythagorean theorem.

### Concept Explanation
C++ provides common mathematical functions through `<cmath>`, including `std::sqrt`, `std::pow`, and `std::round`. Prefer direct multiplication for simple squares when it improves clarity. Use floating-point types for measurements and check domain constraints before calling functions such as square root.

### Worked Example
```cpp
#include <cmath>
#include <iostream>
int main() {
    const double radius = 3.0;
    const double pi = std::acos(-1.0);
    const double area = pi * radius * radius;
    const double circumference = 2.0 * pi * radius;
    const double distance = std::sqrt(3.0 * 3.0 + 4.0 * 4.0);
    std::cout << "Area: " << area << '\n';
    std::cout << "Circumference: " << circumference << '\n';
    std::cout << "Distance: " << distance << '\n';
}

```

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Area: 28.2743
Circumference: 18.8496
Distance: 5
```

### Common Mistakes
- Calling a math function without including `<cmath>` or qualifying it with `std::`.
- Using integer variables for measurements and losing fractional precision.
- Passing a negative value to `std::sqrt` without defining an error policy.

### Activities
1. Change the radius to 5 and calculate the expected area and circumference before running.
2. Calculate the distance for coordinates (5, 12), then compare it with the expected 13.
3. Add a guard for a negative radicand and explain the chosen behavior.
4. Format the results to two decimal places and compare rounded output with the unrounded values.

### Accessibility Practice
Read each intermediate variable and output label in source order. Keep units and labels in text output rather than communicating values through a visual chart.

### Skills Checklist
- [ ] I can include and call functions from `<cmath>`.
- [ ] I can calculate circle area and circumference.
- [ ] I can calculate distance from coordinates using `std::sqrt`.
- [ ] I can explain floating-point precision and domain validation.
- [ ] I can format calculated measurements with meaningful labels and units.
