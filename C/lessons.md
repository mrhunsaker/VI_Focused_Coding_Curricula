# C: Complete Curriculum — Units 0–11

## Course Overview

C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs.

This course intentionally parallels the original Python curriculum. It reuses problem contexts—greetings, profiles, a calculator, grade decisions, score collections, inventory, functions, text files, tests, text analysis, CSV, a to-do list, and a personal-data manager—so the principal new learning target is the C language. The syntax and implementation remain idiomatic, not a mechanical translation.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install and verify the compiler or interpreter, create a project, and test keyboard and screen-reader access.

### Lesson 0.1: Install and Verify C

Install a C17 compiler such as GCC or Clang. Compile with `cc -std=c17 -Wall -Wextra -Wpedantic -g main.c -o main`; run `./main` (Windows: `main.exe`).

### Lesson 0.2: Workspace and First Run
Create a course folder, save a source file named `main.c`, run it from the terminal, and read standard output and errors. Distinguish source code, compiler/interpreter, and executable/runtime.

### Lesson 0.3: Editor and Accessibility Workflow
Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md). Test editor navigation, punctuation announcement, indentation, terminal focus, diagnostics, and project navigation. Install only the language tooling needed for this course.

### Skills Checklist
- [ ] I can verify the C toolchain.
- [ ] I can create and run a source file from the terminal.
- [ ] I can navigate the editor and read output accessibly.

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

Use the terminal from the project root and understand the current working directory. Keep each project in its own folder and distinguish source files, build output, and dependency metadata. Use one folder per C project. Keep source, headers, and generated executable organized separately. Run the compiler from the project folder; do not assume a virtual environment is needed for the C standard library. Learn include paths and linker arguments only when a project adds external libraries.

### Skills Checklist
- [ ] I can identify the project root and run commands from it.
- [ ] I can explain where project dependencies are recorded, if applicable.
- [ ] I can run the program or test command from the terminal and read its output.

# Unit 1: Foundations of Computing

## Overview

This unit covers computer science, hardware/software, algorithms, first program, variables, primitive types. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 1.1: Computer science and problem solving

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Computer science is the study of representing problems and designing precise algorithms. Hardware includes the CPU, RAM, keyboard, and storage; software is the instructions and data executed by the machine. C is widely used for operating systems, embedded systems, libraries, and performance-sensitive programs. An algorithm must state inputs, processing steps, and outputs unambiguously.

### Worked Example
Plan the canonical tip-calculator problem without coding: read a bill amount, calculate 15 percent of it, add the tip to the bill, and display both amounts. For a bill of $24.50, the unrounded tip is $3.675 and the unrounded total is $28.175. Displaying two decimal places yields $3.68 and $28.18.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 1.2: Your first program

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
A C program begins at `main`. `#include <stdio.h>` makes standard I/O declarations available. `puts` writes a string and newline. Braces delimit the function body and semicolons terminate statements. The compiler translates this source into an executable.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    puts("Hello, World!");
    return 0;
}
```
Expected output: `Hello, World!` followed by a newline. Compile with `cc -std=c17 -Wall -Wextra -Wpedantic hello.c -o hello`.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 1.3: Variables and data types

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C is statically typed. Use `int` for age, `double` for fractional measurements, `char` for one character, and a null-terminated character array or `const char *` for text. A C string buffer has a finite capacity and must include room for its terminating null character. Format specifiers in `printf` must match argument types.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    const char *name = "Avery";
    int age = 16;
    double height_m = 1.72;
    const char *favorite = "Computer Science";
    printf("Name: %s\nAge: %d\nHeight: %.2f m\nFavorite subject: %s\n",
           name, age, height_m, favorite);
    return 0;
}
```
Expected output labels Avery, 16, 1.72 m, and Computer Science on separate lines. `%s`, `%d`, and `%.2f` correspond to string, integer, and floating-point arguments.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 2: Numeric Computations

## Overview

This unit covers development process, expressions, assignment, input/output, conversions, arithmetic, math library. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

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
For the canonical calculator, input is bill = 24.50 and rate = 0.15. Calculate tip = bill * rate and total = bill + tip. Expected unrounded values are 3.675 and 28.175; formatted to cents they appear as 3.68 and 28.18. Test zero, typical, and large bills.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

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

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

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

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

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

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

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

### Common Mistakes
- Calling a math function without including `math.h`.
- Forgetting the `-lm` linker option on systems that require it.
- Supplying degrees to a trigonometric function that expects radians.
- Passing a negative value to `sqrt` when a real result is expected.
- Depending on non-standard macros such as `M_PI` without checking portability.

### Activities
1. Change the radius to 2.5 and predict the new area and circumference.
2. Calculate `sqrt(81.0)`, `ceil(4.2)`, and `floor(4.8)`.
3. Extend the program to read a radius and coordinates with validated numeric input.
4. Explain why the point (3, 4) is exactly 5 units from the origin.

### Accessibility Practice
Read the complete source line by line and inspect the punctuation in the function calls and arithmetic expressions. Run the compile command in the terminal and read compiler or linker diagnostics sequentially. Confirm that each output label identifies its value without relying on visual formatting.

### Skills Checklist
- [ ] I can include `math.h` and call common math functions.
- [ ] I can calculate circle area and circumference.
- [ ] I can calculate Euclidean distance from the origin.
- [ ] I can explain radians and compile with the required linker flags.
- [ ] I can test a boundary case and read the output accessibly.

---

# Unit 3: Control Flow

## Overview

This unit covers Boolean expressions, conditionals, lists or arrays, iteration, string operations. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 3.1: Boolean expressions

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Relational operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) produce an integer truth value: zero is false and nonzero is true. Logical operators are `&&`, `||`, and `!`; `&&` and `||` short-circuit. Use braces for conditional blocks.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int score = 82, attendance = 95;
    if (score >= 70 && attendance >= 80) puts("Meets the course criteria.");
    if (score == 100 || attendance == 100) puts("At least one perfect result.");
    if (!(score < 0)) puts("Score is not negative.");
    return 0;
}
```
Expected output: `Meets the course criteria.` and `Score is not negative.`

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.2: Chained conditionals

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use `if`, `else if`, and `else` for mutually exclusive choices. Apply the shared grade thresholds from highest to lowest and reject scores outside 0–100 before classification.

### Worked Example
```c
#include <stdio.h>
char grade_for(int score)
{
    if (score < 0 || score > 100) return '?';
    if (score >= 90) return 'A';
    else if (score >= 80) return 'B';
    else if (score >= 70) return 'C';
    else if (score >= 60) return 'D';
    else return 'F';
}
int main(void)
{
    int tests[] = {91, 90, 82, 80, 76, 70, 60, 0, -1, 101};
    for (size_t i = 0; i < sizeof tests / sizeof tests[0]; ++i)
        printf("%d -> %c\n", tests[i], grade_for(tests[i]));
    return 0;
}
```
Expected mapping: 91/A, 90/A, 82/B, 80/B, 76/C, 70/C, 60/D, 0/F; -1 and 101 are invalid (`?`).

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.3: Sequences and indexing

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C arrays store a fixed number of elements of one type. Indexing begins at zero and C does not automatically check bounds. A four-element array has valid indices 0–3. When an array is passed to a function, pass its length separately.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    size_t count = sizeof scores / sizeof scores[0];
    printf("First: %d\nLast: %d\nCount: %zu\n", scores[0], scores[count - 1], count);
    scores[2] = 80;
    printf("Updated third score: %d\n", scores[2]);
    return 0;
}
```
Expected output: first 82, last 88, count 4, updated third score 80.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.4: For loops and iteration

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
A `for` loop has initialization, continuation condition, and update expression. Traverse the shared score array with a known count. Use `size_t` for indices and convert the total to `double` before calculating the average.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    size_t count = sizeof scores / sizeof scores[0];
    int total = 0;
    for (size_t i = 0; i < count; ++i) { printf("Score %zu: %d\n", i + 1, scores[i]); total += scores[i]; }
    printf("Total: %d\nAverage: %.2f\n", total, (double) total / count);
    return 0;
}
```
Expected total: 337; average: 84.25.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.5: String operations

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C strings are null-terminated character sequences. Use `strlen`, `strcmp`, and `strstr` from `string.h`; ensure every destination buffer has enough capacity. This example processes ASCII bytes. `strlen` counts bytes, not user-perceived Unicode characters.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    const char sample[] = "A student studies programming. Programming develops problem-solving skills.";
    char normalized[sizeof sample];
    size_t length = strlen(sample);
    for (size_t i = 0; i <= length; ++i) normalized[i] = (char)tolower((unsigned char)sample[i]);
    printf("Byte length: %zu\n", length);
    printf("Lowercase: %s\n", normalized);
    printf("Contains programming: %s\n", strstr(normalized, "programming") ? "yes" : "no");
    return 0;
}
```
Expected byte length: 75; substring result: yes. The cast to `unsigned char` is required for safe use of `tolower`.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 4: Data Structures

## Overview

This unit covers sequence mutation, sorting, immutable records, maps, dictionaries, traversal. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 4.1: Mutable sequences

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C arrays have fixed capacity. For a resizable sequence, manage a dynamically allocated buffer with a pointer, element count, and capacity. Every allocation must be checked and every successful allocation must eventually be released with `free`.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int scores[8] = {82, 91, 76, 88};
    size_t count = 4;
    scores[count++] = 95;
    scores[count++] = 84;
    printf("Count: %zu; last: %d\n", count, scores[count - 1]);
    return 0;
}
```
Expected output: `Count: 6; last: 84`. The array has capacity 8 and currently contains 6 values; do not confuse capacity with count.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.2: Sorting and organizing data

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use `qsort` from `stdlib.h` to sort an array. The comparator must return a negative value, zero, or a positive value and must avoid subtraction that could overflow. Sorting changes the order of the original array.

### Worked Example
```c
#include <stdio.h>
#include <stdlib.h>
int compare_ints(const void *a, const void *b)
{
    int left = *(const int *)a, right = *(const int *)b;
    return (left > right) - (left < right);
}
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    size_t n = sizeof scores / sizeof scores[0];
    qsort(scores, n, sizeof scores[0], compare_ints);
    for (size_t i = 0; i < n; ++i) printf("%d ", scores[i]);
    puts("");
    return 0;
}
```
Expected ascending order: 76 82 88 91. Reverse traversal prints descending order.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.3: Immutable records

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Python tuples are immutable sequences. C has no direct tuple type; use a `struct` for a named record and make the object `const` when it must not be modified. A struct groups fields that may have different types.

### Worked Example
```c
#include <stdio.h>
typedef struct { int x; int y; } Point;
int main(void)
{
    const Point origin_offset = {3, 4};
    printf("x: %d\ny: %d\n", origin_offset.x, origin_offset.y);
    return 0;
}
```
Expected output: x: 3 and y: 4. `const` prevents modifying the fields through this object.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.4: Maps and key-value data

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C does not include a built-in dictionary or hash map. For a small fixed inventory, use an array of structs and search by key; for larger data, introduce a hash-table implementation or a library. The key and value fields must be represented explicitly.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *name; int quantity; double unit_price; } Item;
int main(void)
{
    Item inventory[] = {{"Notebook",3,2.50},{"Pencil",10,0.50},{"Folder",4,1.25}};
    for (size_t i = 0; i < sizeof inventory / sizeof inventory[0]; ++i)
        printf("%s: %d at $%.2f each\n", inventory[i].name, inventory[i].quantity, inventory[i].unit_price);
    return 0;
}
```
Expected records: Notebook 3 at $2.50; Pencil 10 at $0.50; Folder 4 at $1.25.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.5: Collection traversal

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Traverse an array of records with an index and explicit count. A struct member is accessed with the dot operator. When passing records to helper functions, use pointers to avoid unnecessary copies and `const` when the function should not modify the record.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *name; int quantity; double unit_price; } Item;
void show_item(const Item *item)
{
    printf("%s: quantity %d; value $%.2f\n", item->name, item->quantity, item->quantity * item->unit_price);
}
int main(void)
{
    Item items[] = {{"Notebook",3,2.50},{"Pencil",10,0.50},{"Folder",4,1.25}};
    for (size_t i = 0; i < sizeof items / sizeof items[0]; ++i) show_item(&items[i]);
    return 0;
}
```
Expected inventory values: $7.50, $5.00, and $5.00.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 5: Input and Iteration

## Overview

This unit covers input validation, sentinel loops, while loops, flags, break/continue, infinite-loop prevention. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 5.1: Input and validation

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Read user input as text with `fgets`, then parse and validate it. A robust parser checks whether any digits were consumed, whether trailing characters remain, and whether the value is in range. Keep prompting until valid input arrives or end-of-file is reached.

### Worked Example
```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
int main(void)
{
    char line[80], *end;
    long value;
    for (;;) {
        printf("Enter a score from 0 to 100: ");
        if (!fgets(line, sizeof line, stdin)) return 1;
        value = strtol(line, &end, 10);
        while (isspace((unsigned char)*end)) ++end;
        if (end != line && *end == '\0' && value >= 0 && value <= 100) break;
        puts("Invalid score. Enter a whole number from 0 to 100.");
    }
    printf("Accepted score: %ld\n", value);
    return 0;
}
```
For input 82, output is `Accepted score: 82`; invalid values cause another prompt.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.2: While loops

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
A `while` loop repeats while its condition is nonzero. Update the condition's state inside the loop so it eventually becomes false. A sentinel-controlled loop is useful for repeated menu input; document the sentinel and handle end-of-file.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int value, total = 0;
    puts("Enter scores; enter -1 to finish.");
    while (scanf("%d", &value) == 1 && value != -1) {
        total += value;
        printf("Running total: %d\n", total);
    }
    printf("Final total: %d\n", total);
    return 0;
}
```
For input 82, 91, -1, the running totals are 82 and 173; final total is 173. This compact example assumes integer tokens; the previous lesson's `fgets` parser is safer for robust input.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.3: Flags and break

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
A Boolean-like flag records whether a condition has occurred. Use `break` to leave the nearest loop once a search succeeds. Initialize the flag before the loop and update it at the point where the condition is met.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    int found = 0;
    for (size_t i = 0; i < sizeof scores / sizeof scores[0]; ++i) {
        if (scores[i] == 76) { found = 1; break; }
    }
    puts(found ? "Score found." : "Score not found.");
    return 0;
}
```
Expected output: `Score found.` Change the search value to 100 to exercise the not-found path.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.4: Continue and filtering

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use `continue` to skip the remainder of the current loop iteration. It is useful for filtering records, but the condition must be explicit and understandable. Avoid using it to conceal complex control flow.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    for (size_t i = 0; i < sizeof scores / sizeof scores[0]; ++i) {
        if (scores[i] < 80) continue;
        printf("Passing score: %d\n", scores[i]);
    }
    return 0;
}
```
Expected output: Passing score: 82, 91, and 88, each on its own line.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.5: Infinite-loop prevention

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
An infinite loop occurs when the termination condition never becomes false or the state used by the condition is not updated. Check loop invariants, increment/decrement operations, sentinel handling, and all paths that can exit. Prefer a clear loop condition over an unconditional loop unless an explicit `break` is guaranteed.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int remaining = 3;
    while (remaining > 0) {
        printf("%d\n", remaining);
        --remaining;
    }
    puts("Finished.");
    return 0;
}
```
Expected output: 3, 2, 1, then Finished. Removing `--remaining` creates a non-terminating loop; diagnose it by tracing the condition and state.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 6: Functions

## Overview

This unit covers definitions, parameters, arguments, return values, scope, collection parameters, variadic functions. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 6.1: Defining functions

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
A function gives a name to a reusable operation. Declare its return type, name, and parameter types. Put a prototype before the first call when the definition appears later. Keep one clear responsibility per function.

### Worked Example
```c
#include <stdio.h>
double calculate_tip(double bill, double rate)
{
    return bill * rate;
}
int main(void)
{
    double tip = calculate_tip(24.50, 0.15);
    printf("Tip: $%.2f\n", tip);
    return 0;
}
```
Expected tip display: $3.68. The function returns a value and does not print it itself.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.2: Parameters and arguments

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Arguments are the values supplied at a call site; parameters are the local variables receiving them. C passes arguments by value. To modify a caller's object, pass its address using a pointer. C has no default or named arguments; use explicit wrapper functions or configuration structs when needed.

### Worked Example
```c
#include <stdio.h>
double total_with_tip(double bill, double rate)
{
    return bill + bill * rate;
}
int main(void)
{
    printf("Total: $%.2f\n", total_with_tip(24.50, 0.15));
    return 0;
}
```
Expected total display: $28.18. Swap the two arguments and explain why the result changes; C uses positional arguments.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.3: Return values

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
A non-void function returns a value using `return`. The caller can store it, pass it to another function, or print it. Use a `void` return type only when no value is returned. Every control-flow path in a non-void function must return an appropriate value.

### Worked Example
```c
#include <stdio.h>
int sum_scores(const int scores[], size_t count)
{
    int total = 0;
    for (size_t i = 0; i < count; ++i) total += scores[i];
    return total;
}
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    printf("Total: %d\n", sum_scores(scores, 4));
    return 0;
}
```
Expected total: 337. The function receives the array pointer and its length separately.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.4: Functions over collections

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Pass arrays to functions with an explicit element count. Use `const` when the function only reads the collection. A pointer parameter does not contain the original array length; the caller and callee must agree on the count.

### Worked Example
```c
#include <stdio.h>
double average(const int values[], size_t count)
{
    int total = 0;
    for (size_t i = 0; i < count; ++i) total += values[i];
    return count ? (double) total / count : 0.0;
}
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    printf("Average: %.2f\n", average(scores, 4));
    return 0;
}
```
Expected average: 84.25. Add a separate function that searches the inventory array by item name.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.5: Scope and variadic arguments

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Local variables have block scope. A variable declared inside a function is not directly accessible elsewhere. C supports variadic functions through `<stdarg.h>`, but a format string or another explicit count is needed to describe the extra arguments. Prefer a typed array-plus-count interface for beginner exercises because it is easier to validate.

### Worked Example
```c
#include <stdio.h>
#include <stdarg.h>
int sum_values(size_t count, ...)
{
    int total = 0;
    va_list args;
    va_start(args, count);
    for (size_t i = 0; i < count; ++i) total += va_arg(args, int);
    va_end(args);
    return total;
}
int main(void)
{
    printf("Sum: %d\n", sum_values(4, 82, 91, 76, 88));
    return 0;
}
```
Expected sum: 337. The caller must pass the correct count and types; variadic arguments are not type-checked by the function signature.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 7: Object-Oriented Programming

## Overview

This unit covers types/classes, instances, fields, methods, inheritance or interfaces, composition. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 7.1: Types and object models

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C does not have classes in the C++/Java sense. Use `struct` to group related data and functions that operate on the data to model an object. Encapsulation is a design discipline in C: expose an interface in a header and keep implementation details in a source file. The shared domain is a student or inventory item.

### Worked Example
```c
typedef struct {
    char name[40];
    int quantity;
    double unit_price;
} Item;
```
This record models one inventory item with the same fields used throughout the course: name, quantity, and unit price. A C struct stores fields; it does not automatically provide constructors, methods, or memory management.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.2: Creating instances

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Declare a struct variable to create an instance. Initialize each field deliberately; aggregate initialization follows field order unless designated initializers are used. Copying a struct copies its fields, including pointer values, not the memory referenced by those pointers.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *name; int quantity; double unit_price; } Item;
int main(void)
{
    Item notebook = {.name = "Notebook", .quantity = 3, .unit_price = 2.50};
    Item pencil = {.name = "Pencil", .quantity = 10, .unit_price = 0.50};
    printf("%s: %d; %s: %d\n", notebook.name, notebook.quantity, pencil.name, pencil.quantity);
    return 0;
}
```
Expected output: Notebook: 3; Pencil: 10. The two variables are separate struct instances.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.3: Fields and methods

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Access struct fields with `.` when you have an object and `->` when you have a pointer to an object. Functions that operate on a struct can receive a pointer; use `const` for read-only access. Keep data and operations conceptually together even though C does not have member methods.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *name; int quantity; double unit_price; } Item;
double item_value(const Item *item)
{
    return item->quantity * item->unit_price;
}
int main(void)
{
    Item notebook = {"Notebook", 3, 2.50};
    printf("%s inventory value: $%.2f\n", notebook.name, item_value(&notebook));
    return 0;
}
```
Expected output: Notebook inventory value: $7.50.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.4: Inheritance and interfaces

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C has no built-in class inheritance. Model shared behavior with composition, function pointers, or tagged unions when appropriate. Do not force an inheritance hierarchy into C. For a simple specialization, use a base record as a field in a larger record and document the relationship explicitly.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *name; int quantity; double unit_price; } Item;
typedef struct { Item item; int reorder_level; } StockedItem;
int needs_reorder(const StockedItem *stock)
{
    return stock->item.quantity <= stock->reorder_level;
}
int main(void)
{
    StockedItem notebook = {{"Notebook", 3, 2.50}, 3};
    printf("%s reorder required: %s\n", notebook.item.name,
           needs_reorder(&notebook) ? "yes" : "no");
    return 0;
}
```
Expected output: Notebook reorder required: yes. This is composition, not language-level inheritance.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.5: Composition

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Composition builds a larger object from smaller related records. For the course's personal data manager, a manager can contain an array of items plus a count and capacity. Define ownership clearly: decide which function allocates and frees any dynamically allocated memory.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *title; int done; } Task;
typedef struct { Task tasks[10]; size_t count; } TaskManager;
int main(void)
{
    TaskManager manager = {.tasks = {{"Review C arrays", 0}, {"Practice functions", 1}}, .count = 2};
    for (size_t i = 0; i < manager.count; ++i)
        printf("%s: %s\n", manager.tasks[i].title, manager.tasks[i].done ? "done" : "not done");
    return 0;
}
```
Expected output lists the two tasks and their completion states.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 8: Files and Exceptions

## Overview

This unit covers read/write text, resource lifetime, error handling, JSON serialization and persistence. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 8.1: Reading text files

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Open a text file with `fopen` and check for `NULL` before reading. Read lines with `fgets` into a bounded buffer; process each line before reading the next. Always close a successfully opened file. Use a relative path resolved from the program's working directory.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    FILE *file = fopen("notes.txt", "r");
    char line[256];
    if (file == NULL) { perror("notes.txt"); return 1; }
    while (fgets(line, sizeof line, file) != NULL) fputs(line, stdout);
    if (ferror(file)) { perror("Reading notes.txt"); fclose(file); return 1; }
    fclose(file);
    return 0;
}
```
Create `notes.txt` with two lines before running. The program reproduces those lines. A missing file produces a diagnostic and a nonzero exit status.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.2: Writing and appending files

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Open a file with mode `w` to create or truncate it, and mode `a` to append. Check both the `fopen` result and the return value of write operations. Close the file and check for errors when durability matters. Do not overwrite a user's file without explaining the effect.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    FILE *file = fopen("notes.txt", "a");
    if (file == NULL) { perror("notes.txt"); return 1; }
    if (fprintf(file, "Practice the C file API.\n") < 0) {
        perror("Writing notes.txt"); fclose(file); return 1;
    }
    if (fclose(file) == EOF) { perror("Closing notes.txt"); return 1; }
    puts("Note appended.");
    return 0;
}
```
Expected output: `Note appended.` The new line is added to the end of `notes.txt`.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.3: Errors and exceptions

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C does not have language-level exceptions. Standard library functions report errors through return values, error indicators, or `errno`. Check each function's documented failure convention and use `perror` or `strerror` to report system errors. Return status codes from functions so callers can respond.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    FILE *file = fopen("missing_notes.txt", "r");
    if (file == NULL) {
        perror("Unable to open missing_notes.txt");
        return 1;
    }
    fclose(file);
    return 0;
}
```
If the file is absent, the program prints an operating-system diagnostic and exits with status 1. This is explicit error handling, not a thrown exception.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.4: Resource cleanup

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C resource lifetime is manual for resources such as `FILE *` handles and dynamically allocated memory. Every successful acquisition must have a corresponding release on all control-flow paths. Use a single cleanup section when multiple operations can fail; do not close an uninitialized or already-closed resource.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int status = 1;
    FILE *file = fopen("notes.txt", "r");
    if (file == NULL) { perror("notes.txt"); goto cleanup; }
    puts("File opened successfully.");
    status = 0;
cleanup:
    if (file != NULL && fclose(file) == EOF) { perror("fclose"); status = 1; }
    return status;
}
```
The cleanup path closes the file exactly once if opening succeeded. In larger programs, structure functions so cleanup remains easy to audit.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.5: JSON persistence

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
The C standard library does not include a JSON parser or serializer. Choose and document a maintained JSON library for projects that need JSON, and do not hand-parse arbitrary JSON with string operations. Teach the shared record schema independently of the library: `id`, `title`, `description`, `category`, `created_at`, and `updated_at`. Explain how JSON strings, numbers, booleans, arrays, and objects map to C data.

### Worked Example
```c
typedef struct {
    int id;
    char title[80];
    char description[240];
    char category[40];
    char created_at[32];
    char updated_at[32];
} DataItem;
```
This C struct is the in-memory shape of one capstone record. The JSON library layer must serialize every field and validate required fields when loading. Record the selected library and its build/link instructions in the project README.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 9: Testing and Data Analysis

## Overview

This unit covers unit tests, testing stateful types, randomness, text analysis, CSV processing. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 9.1: Testing functions

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Test deterministic functions with known inputs and expected results. C has no standard unit-test framework; begin with assertions from `assert.h`, then introduce a test framework if a project grows. Compile tests separately from the application and ensure tests cover ordinary values, boundaries, and invalid inputs.

### Worked Example
```c
#include <assert.h>
int add_two_numbers(int a, int b) { return a + b; }
int main(void)
{
    assert(add_two_numbers(5, 3) == 8);
    assert(add_two_numbers(-5, -3) == -8);
    assert(add_two_numbers(10, -4) == 6);
    return 0;
}
```
No output and exit status 0 indicate that all assertions passed. An assertion failure prints a diagnostic and terminates the test executable.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.2: Testing stateful objects

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Test stateful records by creating a fresh instance for each test, changing its state through the public operations, and checking the resulting fields. In C, write explicit setup code in each test or a helper function; there is no built-in `setUp` lifecycle.

### Worked Example
```c
#include <assert.h>
typedef struct { int quantity; } Item;
void add_stock(Item *item, int amount) { if (amount > 0) item->quantity += amount; }
int main(void)
{
    Item notebook = {.quantity = 3};
    add_stock(&notebook, 2);
    assert(notebook.quantity == 5);
    add_stock(&notebook, -1);
    assert(notebook.quantity == 5);
    return 0;
}
```
The assertions verify that a positive restock changes quantity and a negative restock is rejected.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.3: Random values

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use the pseudo-random number generator in `stdlib.h`. Seed once with `srand`, then obtain values with `rand`. The sequence is deterministic for a given implementation and seed; use a fixed seed in tests. Avoid modulo bias for applications requiring statistically sound sampling or security; `rand` is not cryptographically secure.

### Worked Example
```c
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    srand(42);
    int die = rand() % 6 + 1;
    printf("Die roll: %d\n", die);
    return 0;
}
```
The output is reproducible for a given C library implementation and seed, but the exact value may differ across implementations. Do not use `rand` for passwords or security tokens.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.4: Text analysis

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Analyze the same shared text sample by splitting it into words and counting frequencies. C requires explicit tokenization and storage. For a beginner exercise, normalize ASCII letters and count a small fixed set of words; explain that a production tokenizer must handle punctuation, UTF-8, and dynamic word storage correctly.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    char text[] = "A student studies programming. Programming develops problem-solving skills.";
    for (size_t i = 0; text[i]; ++i) text[i] = (char)tolower((unsigned char)text[i]);
    const char *word = "programming";
    int count = 0;
    char *p = text;
    while ((p = strstr(p, word)) != NULL) { ++count; p += strlen(word); }
    printf("Occurrences of programming: %d\n", count);
    return 0;
}
```
Expected output: 2 occurrences. This counts substring matches, not general word tokens; extend it to tokenize and count all words.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.5: CSV records

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
CSV is a delimited text format with quoting rules; splitting every line on commas is not a correct general CSV parser because quoted fields may contain commas, quotes, and newlines. Use a documented CSV library for production data. For the first exercise, read a simple known CSV file and state that the format excludes quoted commas.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    FILE *file = fopen("students.csv", "r");
    char line[256];
    if (!file) { perror("students.csv"); return 1; }
    if (fgets(line, sizeof line, file)) printf("Columns: %s", line);
    while (fgets(line, sizeof line, file)) printf("Record: %s", line);
    fclose(file);
    return 0;
}
```
Create a header with `student_id,first_name,last_name,score,active` and at least two rows. The program prints the header and each record line. A production parser must handle CSV quoting correctly.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 10: Project-Based Learning

## Overview

This unit covers requirements, top-down design, text adventure, command-line to-do manager, accessible validation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 10.1: Requirements and design

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use top-down design to break an application into input, processing, storage, and output functions. Preserve the same requirements as the Python project: clear prompts, labeled output, confirmation messages, validation, and text-only operation. Write pseudocode and acceptance tests before coding.

### Worked Example
Design the to-do manager around the operations add task, view tasks, mark task complete, save tasks, load tasks, and quit. Define the task fields as `id`, `title`, `description`, `done`, and `created_at`. Specify the behavior for an empty list, an invalid task number, and a missing data file.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Represent rooms as records containing a room identifier, description, and exits. Track the current room by index or identifier. A movement command is valid only if the current room has an exit in that direction. Normalize commands consistently and always provide a textual description of the new location.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
typedef struct { const char *name; const char *description; int north, east, south, west; } Room;
int main(void)
{
    Room rooms[] = {
        {"start_room", "You are in a dimly lit cave. A passage leads NORTH.", 1, -1, -1, -1},
        {"tunnel", "The tunnel is damp and cold. You can go SOUTH or EAST.", -1, 2, 0, -1},
        {"clearing", "You are in a sunny clearing. A path leads WEST.", -1, -1, -1, 1}
    };
    int current = 0;
    printf("%s\n", rooms[current].description);
    current = rooms[current].north;
    printf("%s\n", rooms[current].description);
    return 0;
}
```
The first room leads north to the tunnel; the tunnel leads east to the clearing and south back to the cave. Extend this model with a command parser and a `quit` command. `-1` means that no exit exists in that direction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Extend the same cave-and-tunnel adventure with a shiny key, a player inventory, and a locked door. An item must be removed from the room when picked up and added to the inventory. The door unlocks only when the player is in the correct room and has the key. Keep command responses explicit.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    int key_in_room = 1, has_key = 0, door_locked = 1;
    char command[80];
    puts("A dark cave. There is a shiny key here.");
    printf("Command (take key): ");
    if (!fgets(command, sizeof command, stdin)) return 1;
    command[strcspn(command, "\n")] = '\0';
    if (strcmp(command, "take key") == 0 && key_in_room) {
        key_in_room = 0; has_key = 1; puts("You picked up the shiny key.");
    }
    if (has_key && door_locked) { door_locked = 0; puts("The key can unlock the door."); }
    return 0;
}
```
This is a small state-transition demonstration, not the complete game. Extend it with the same room movement rules from Lesson 10.2, then test taking the key twice, trying to unlock without the key, and using the key in the wrong room.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.4: Command-line to-do manager

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Build a command-line to-do tool with a menu loop and separate functions for adding, viewing, completing, saving, and loading tasks. Use the shared task fields and provide confirmations. C has no standard JSON support; for this project either choose a maintained JSON library and document its build instructions, or use a clearly documented simple text format while teaching JSON serialization separately in Lesson 8.5. Do not label a custom text format as JSON.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
typedef struct { char title[80]; int done; } Task;
void show_tasks(const Task tasks[], size_t count)
{
    if (count == 0) { puts("No tasks in your list."); return; }
    for (size_t i = 0; i < count; ++i)
        printf("%zu. [%c] %s\n", i + 1, tasks[i].done ? 'X' : ' ', tasks[i].title);
}
int main(void)
{
    Task tasks[50] = {0}; size_t count = 0; char line[100];
    for (;;) {
        puts("1 Add task  2 View tasks  3 Quit");
        printf("Choice: ");
        if (!fgets(line, sizeof line, stdin)) break;
        if (line[0] == '1' && count < 50) {
            printf("Task title: ");
            if (!fgets(tasks[count].title, sizeof tasks[count].title, stdin)) break;
            tasks[count].title[strcspn(tasks[count].title, "\n")] = '\0';
            tasks[count++].done = 0; puts("Task added.");
        } else if (line[0] == '2') show_tasks(tasks, count);
        else if (line[0] == '3') break;
        else puts("Invalid choice.");
    }
    return 0;
}
```
This starter implements add, view, and quit with a fixed capacity of 50 tasks. Extend it with completion and persistence, checking every input and file operation.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.5: Accessible UX and validation

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Accessible text interfaces use explicit prompts, consistent labels, predictable menu order, and clear confirmations. Validate all input before changing state. On errors, state what was wrong and how to correct it. Do not rely on color, position, or symbols alone to convey task status. For a screen-reader workflow, ensure output is announced in a useful sequence.

### Worked Example
```c
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    char line[80], *end;
    long age;
    for (;;) {
        printf("Enter your age as a positive whole number: ");
        if (!fgets(line, sizeof line, stdin)) return 1;
        age = strtol(line, &end, 10);
        if (end != line && age > 0) break;
        puts("Invalid age. Enter a whole number greater than zero.");
    }
    printf("You entered age: %ld\n", age);
    return 0;
}
```
The program repeats until it receives a positive integer. Improve it by rejecting trailing non-whitespace characters and checking `errno` for overflow.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 11: Capstone

## Overview

This unit covers accessible personal-data manager, model, persistence, CRUD, tests, documentation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 11.1: Capstone requirements

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
The Python capstone uses NiceGUI, but that framework is Python-specific. The C course must preserve the same user-facing data-manager requirements without pretending that NiceGUI has a C equivalent. Implement a keyboard-operable terminal interface first; a graphical interface is an optional extension using a separately selected C-compatible toolkit. The core record fields, operations, validation, persistence, tests, and accessibility acceptance criteria remain the same.

### Worked Example
Choose one collection: contacts, books/movies, to-do tasks, or inventory. Define fields, required values, validation rules, and the five required operations: add, view, edit, delete, save/load. For the to-do option, use `id`, `title`, `description`, `done`, and `created_at`. Document that the reference Python GUI is replaced by an accessible terminal interface in this C implementation.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.2: Data model and storage

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Define a C struct for the shared capstone record and choose a clear ownership strategy for strings. Fixed-size arrays are acceptable for a small beginner project if maximum lengths are documented and input is bounded. For persistent data, use a maintained JSON library and document its version, dependency setup, and error handling. The C standard library does not provide JSON serialization.

### Worked Example
```c
#include <stddef.h>
typedef struct {
    int id;
    char title[80];
    char description[240];
    char category[40];
    char created_at[32];
    char updated_at[32];
} DataItem;
```
The record contains the exact canonical capstone fields. Define which fields are required, how empty strings are handled, and how IDs and timestamps are generated. The serialization layer must preserve all fields when saving and loading.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.3: Create/read/update/delete

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Implement create, read, update, and delete operations as separate functions that operate on the same collection and report success or failure. Validate an identifier before modifying a record. After every operation, refresh the displayed list and persist successful changes. Avoid returning pointers to local stack variables.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
typedef struct { int id; char title[80]; int done; } Task;
int find_task(const Task tasks[], size_t count, int id)
{
    for (size_t i = 0; i < count; ++i) if (tasks[i].id == id) return (int)i;
    return -1;
}
int main(void)
{
    Task tasks[] = {{1, "Read C lesson", 0}, {2, "Practice arrays", 1}};
    size_t count = sizeof tasks / sizeof tasks[0];
    int index = find_task(tasks, count, 1);
    if (index >= 0) { strcpy(tasks[index].title, "Review C arrays"); tasks[index].done = 1; }
    for (size_t i = 0; i < count; ++i)
        printf("%d: %s (%s)\n", tasks[i].id, tasks[i].title, tasks[i].done ? "done" : "open");
    return 0;
}
```
Expected state: task 1 is renamed to Review C arrays and marked done; task 2 is unchanged. Add bounds-safe input and implement add/delete operations using the same ID lookup.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.4: Validation and testing

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Validate required fields before creating or updating a record. Test duplicate IDs, empty titles, overlong input, missing files, malformed JSON, and operations on unknown IDs. Keep deterministic logic separate from terminal input so it can be tested. In C, use assertions or a test framework and run with compiler warnings; consider AddressSanitizer and UndefinedBehaviorSanitizer during development.

### Worked Example
```c
#include <assert.h>
#include <string.h>
int valid_title(const char *title)
{
    return title != NULL && title[0] != '\0';
}
int main(void)
{
    assert(valid_title("Read C lesson"));
    assert(!valid_title(""));
    assert(!valid_title(NULL));
    return 0;
}
```
All assertions pass with exit status 0. Add tests for the full CRUD functions and compile a debug build with `-fsanitize=address,undefined -fno-omit-frame-pointer` where supported.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.5: Documentation and presentation

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
The deliverable includes source code, sample data, a README, build/run instructions, a description of the data format, and a reflection on accessibility. Document the compiler version, exact build command, external dependencies, file locations, and keyboard commands. Ensure prompts and status messages are meaningful when read linearly. Do not claim screen-reader testing unless it has actually been performed.

### Worked Example
README acceptance checklist: explain the selected data-manager domain; list the exact fields; document add/view/edit/delete/save/load; provide compile and run commands; describe how to navigate the menu by keyboard; explain how to recover from invalid input; include sample data and known limitations; record the screen reader and operating-system tests actually performed.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic C constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Course-Wide Assessment and Portfolio

Submit runnable exercises, prediction notes, debugging notes, tests, and the text adventure and personal-data manager projects. Assessment focuses on correctness, idiomatic C, code explanation, independent debugging, and accessible interaction—not speed or visual editor use.

## AI and Academic Integrity

AI may be used only for personal conceptual explanations and reinforcement when the instructor permits. Do not use AI to write, complete, autocomplete, repair, or generate course code or assessment solutions. Students must explain every submitted statement independently.

## Further Learning

Use the official C language specification, standard-library documentation, and the linked setup resources. Verify APIs against the documentation for the installed toolchain.