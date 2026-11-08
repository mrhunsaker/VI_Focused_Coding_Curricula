# Unit 2: Numeric Computation

## Overview

Use C expressions, numeric types, input/output, conversions, and the math library to solve the shared calculator and measurement problems. Focus on operator precedence, integer versus floating-point arithmetic, validated input, and predictable formatting.

Prerequisite: Unit 1. Learners should be able to compile a C program and declare basic variables.

## Lesson 2.1: Design and tracing

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use the design–implement–test cycle. Design identifies inputs, outputs, constraints, and edge cases; implementation translates the algorithm into C; testing compares actual behavior with expected behavior. Compile incrementally with warnings enabled and test both ordinary and boundary inputs.

### Worked Example
<<<<<<< HEAD
For the canonical calculator, input is bill = 24.50 and rate = 0.15. Calculate tip = bill * rate and total = bill + tip. Expected unrounded values are 3.675 and 28.175; formatted to cents they appear as 3.68 and 28.18. Test zero, typical, and large bills.
=======
For the canonical calculator, input is bill = 24.50 and rate = 0.15. Calculate tip = bill * rate and total = bill + tip. Expected unrounded values are 3.675 and 28.175; formatted to cents with `printf("%.2f")` they appear as 3.67 and 28.18 (the stored tip is 3.67499999999999982). Test zero, typical, and large bills.

### Expected Behavior or Output

No program is run in this lesson. The expected result is a trace table written as sentences: bill 24.50, rate 0.15, tip 3.675, total 28.175, and test cases for zero, typical, and large bills with the result predicted before any code is written.
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
- Coding before writing down the bill, rate, tip, and total as separate inputs/intermediate/output values.
- Testing only $24.50 and missing zero, negative, or unusually large bill values.
- Rounding intermediate arithmetic and then obtaining a different displayed total.

### Activities
1. Write pseudocode for the $24.50 bill and 15% tip, naming each input and intermediate result.
2. Create acceptance cases for bills 0.00, 24.50, and -1.00.
3. Trace the values 24.50, 0.15, 3.675, and 28.175 in order.
4. Record the exact expected numeric result before running the modified program; include 3.675 tip and 28.175 total before two-decimal display where the calculator context applies.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Design and tracing" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 2.2: Expressions and assignment

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Expressions combine operands and operators. C follows operator precedence; parentheses make intent explicit. Assignment (`=`) stores a value, while equality (`==`) compares values. Integer division discards the fractional part; at least one operand must be floating point for a fractional quotient.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int score = 50;
    printf("Initial score: %d\n", score);
    score = score + 20;
    printf("New score: %d\n", score);
    printf("Integer expression: %d\n", 10 / 3 + 3);
    printf("Floating expression: %.2f\n", 10.0 / 3 + 3);
    return 0;
}
```
Expected score values are 50 and 70. The integer expression is 6; the floating expression is approximately 6.33.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Initial score: 50
New score: 70
Integer expression: 6
Floating expression: 6.33
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Using integer division in a calculation that requires cents or a fractional average.
- Using `=` in a condition where `==` is intended.
- Depending on implicit precedence rather than making the intended grouping explicit.

### Activities
1. Predict the results of `10 / 3`, `10.0 / 3`, and `10 / 3.0` before compiling.
2. Rewrite a compound expression with parentheses to show the intended precedence.
3. Change the score assignment from 50 to 70 and trace the printed values.
4. Record the exact expected numeric result before running the modified program; include 3.675 tip and 28.175 total before two-decimal display where the calculator context applies.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Expressions and assignment" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 2.3: Input and output

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use `printf` for formatted output. For line input, use `fgets` with a fixed-size buffer and check its return value. Convert numeric text with `strtol` or `strtod`; do not assume input is valid. Unlike Python's `input`, C input requires explicit buffer management and conversion.

### Worked Example
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void)
{
    char name[80], line[80], *end;
    long first, second;
    printf("Name: ");
    if (!fgets(name, sizeof name, stdin)) return 1;
    name[strcspn(name, "\n")] = '\0';
    printf("First whole number: ");
    if (!fgets(line, sizeof line, stdin)) return 1;
    first = strtol(line, &end, 10);
    if (end == line) { puts("Invalid number."); return 1; }
    printf("Second whole number: ");
    if (!fgets(line, sizeof line, stdin)) return 1;
    second = strtol(line, &end, 10);
    if (end == line) { puts("Invalid number."); return 1; }
    printf("Hello, %s!\nSum: %ld\n", name, first + second);
    return 0;
}
```
For inputs Avery, 12, and 8, output includes `Hello, Avery!` and `Sum: 20`. A production parser should also validate trailing characters and range errors.

<<<<<<< HEAD
=======
### Expected Behavior or Output

With these lines typed as standard input:
```text
Avery
12
8
```

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Name: First whole number: Second whole number: Hello, Avery!
Sum: 20
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Reading a full name with `%s`, which stops at whitespace.
- Ignoring the return from `fgets` or accepting a numeric prefix followed by junk.
- Failing to detect a number outside the destination type's range.

### Activities
1. Enter Avery, 12, and 8; verify the greeting and sum.
2. Enter a name containing spaces and confirm that the entire line is retained.
3. Extend the parser to reject `12abc`, blank input, and an out-of-range integer.
4. Record the exact expected numeric result before running the modified program; include 3.675 tip and 28.175 total before two-decimal display where the calculator context applies.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Input and output" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 2.4: Numeric conversions and mathematics

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C integer types represent whole numbers; `float` and `double` represent approximate floating-point values. Converting a floating value to an integer truncates toward zero. Convert text with `strtol` or `strtod`, validate the end pointer, and check range errors. Mixed arithmetic follows the usual arithmetic conversions.

### Worked Example
```c
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    char age_text[] = "16", weight_text[] = "52.5", *end;
    long age = strtol(age_text, &end, 10);
    double weight = strtod(weight_text, &end);
    printf("Age doubled: %ld\nWeight plus age: %.1f\n", age * 2, weight + age);
    printf("Integer division: %d\nFloating division: %.1f\n", 5 / 2, 5.0 / 2);
    return 0;
}
```
Expected values: 32, 68.5, 2, and 2.5. Extend the example to reject trailing characters and check `errno` for overflow.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Age doubled: 32
Weight plus age: 68.5
Integer division: 2
Floating division: 2.5
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Assuming a cast rounds rather than truncates toward zero.
- Passing the wrong type to `printf` or using an incompatible format specifier.
- Failing to check `strtol`/`strtod` conversion end pointers and range errors.

### Activities
1. Predict the results for age 16 and weight 52.5 before running the conversion example.
2. Convert -2.9 to an integer and explain truncation toward zero.
3. Add end-pointer and `errno` checks for malformed and out-of-range text.
4. Record the exact expected numeric result before running the modified program; include 3.675 tip and 28.175 total before two-decimal display where the calculator context applies.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Numeric conversions and mathematics" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 2.5: Using the C Math Library

### Reading References
- C17 standard library reference: `math.h`.
- Python curriculum Lesson 2.5: Using the Math Library.

### Learning Objectives
- Include and use the C math library.
- Calculate circle area and circumference.
- Calculate distance from the origin using the Pythagorean theorem.
- Explain radians and the platform-specific math-library linker option.

### Concept Explanation
The C math library declares functions such as `sqrt`, `pow`, `ceil`, `floor`, and trigonometric functions in `math.h`. Some GCC/Clang environments require linking with `-lm`. Trigonometric functions use radians. The standard C17 interface does not require the non-standard `M_PI` macro; `acos(-1.0)` is a portable way to obtain pi. Check function domains before calling functions such as `sqrt`.

### Worked Example
```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    const double pi = acos(-1.0);
    const double radius = 5.0;
    const double x = 3.0;
    const double y = 4.0;
    double area = pi * radius * radius;
    double circumference = 2.0 * pi * radius;
    double distance = sqrt(x * x + y * y);

    printf("Area: %.2f\n", area);
    printf("Circumference: %.2f\n", circumference);
    printf("Distance from origin: %.2f\n", distance);
    return 0;
}
```

Expected output: area 78.54, circumference 31.42, and distance 5.00. Compile with `cc -std=c17 -Wall -Wextra -Wpedantic math_example.c -o math_example -lm` on systems that require explicit math-library linking.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Area: 78.54
Circumference: 31.42
Distance from origin: 5.00
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Forgetting `math.h` or the `-lm` linker option where needed.
- Passing degrees to trig functions that expect radians.
- Assuming `M_PI` is guaranteed by C17 or passing a negative value to `sqrt`.

### Activities
1. Change the radius to 2.5 and predict area and circumference.
2. Calculate `sqrt(81.0)`, `ceil(4.2)`, and `floor(4.8)` by hand and verify.
3. Add validated radius input and reject negative values.
4. Record the exact expected numeric result before running the modified program; include 3.675 tip and 28.175 total before two-decimal display where the calculator context applies.
### Accessibility Practice
Read the complete source line by line and inspect the punctuation in the function calls and arithmetic expressions. Run the compile command in the terminal and read compiler or linker diagnostics sequentially. Confirm that each output label identifies its value without relying on visual formatting.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Using the C Math Library" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.

---
