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
<<<<<<< HEAD
Plan the canonical tip-calculator problem without coding: read a bill amount, calculate 15 percent of it, add the tip to the bill, and display both amounts. For a bill of $24.50, the unrounded tip is $3.675 and the unrounded total is $28.175. Displaying two decimal places yields $3.68 and $28.18.
=======
Plan the canonical tip-calculator problem without coding: read a bill amount, calculate 15 percent of it, add the tip to the bill, and display both amounts. For a bill of $24.50, the unrounded tip is $3.675 and the unrounded total is $28.175. Displaying two decimal places with `printf("%.2f")` yields $3.67 and $28.18, because the stored value of the tip is 3.67499999999999982.

### Expected Behavior or Output

No program is run in this lesson. The expected result is a written plan with the four steps in order. A correct hand trace with the shared values gives a tip of 3.675 and a total of 28.175; later lessons show that C displays these with two decimals as 3.67 and 28.18.
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
- Confusing an algorithm's logical steps with C syntax or compiler behavior.
- Omitting an input constraint such as nonnegative bill amount or percentage range.
- Rounding the tip before adding it to the bill rather than formatting only the displayed result.

### Activities
1. Write the tip-calculator algorithm as input, processing, and output steps, then calculate the unrounded values for a $24.50 bill.
2. Identify the input validation rule for a negative bill and an invalid tip rate.
3. Explain why formatting a monetary result to two decimals is different from rounding every intermediate calculation.
4. Write an acceptance-test note for "Computer science and problem solving": state the exact input or source change and the expected observable result.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Computer science and problem solving" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Hello, World!
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Using `void main` instead of the standard `int main(void)` form.
- Omitting `#include <stdio.h>` or a statement terminator.
- Assuming a successful compile guarantees the executable is being run from the intended directory.

### Activities
1. Compile the hello program with C17 and all requested warnings; record every diagnostic.
2. Change the greeting and add a second output line, predicting the exact line order.
3. Remove a semicolon in a disposable copy, compile, and use the diagnostic to locate the syntax error.
4. Write an acceptance-test note for "Your first program": state the exact input or source change and the expected observable result.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Your first program" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Name: Avery
Age: 16
Height: 1.72 m
Favorite subject: Computer Science
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Using a format string that does not match the declared type.
- Forgetting that C strings need a null terminator and sufficient buffer capacity.
- Using an uninitialized local variable or assuming a variable has Python-like dynamic typing.

### Activities
1. Add student ID and a middle initial to Avery's profile, selecting appropriate C types.
2. Print the height using `%.1f`, `%.2f`, and `%.3f` and compare the displayed precision.
3. Explain why the string buffer size must include the terminating null byte.
4. Write an acceptance-test note for "Variables and data types": state the exact input or source change and the expected observable result.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Variables and data types" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
