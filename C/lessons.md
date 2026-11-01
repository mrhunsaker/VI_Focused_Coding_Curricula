# C: Complete Curriculum — Units 0–11

## Course Overview

C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs.

The repository includes an automated C17 syntax-check workflow for every fenced C example in this manuscript. It runs GCC and Clang with `-Wall -Wextra -Wpedantic -Werror`; this verifies translation-unit syntax and warning cleanliness, but does not by itself link or execute every example.

This course intentionally parallels the original Python curriculum. It reuses problem contexts—greetings, profiles, a calculator, grade decisions, score collections, inventory, functions, text files, tests, text analysis, CSV, a to-do list, and a personal-data manager—so the principal new learning target is the C language. The syntax and implementation remain idiomatic, not a mechanical translation.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install and verify a C17 compiler, create a project workspace, compile and run a source file from the terminal, and configure an editor workflow that can be operated with the learner's access technology. C has no standard-library virtual environment; external libraries are managed through documented system packages, source dependencies, include paths, and linker options.

### Lesson 0.1: Install and Verify C

#### Reading References
- GCC or Clang installation and user documentation.
- C language version and compiler options reference.

#### Learning Objectives
- Identify a C compiler and verify its version.
- Compile a minimal C17 program with warnings enabled.
- Distinguish compiler diagnostics from program output.

#### Concept Explanation
C is compiled: the compiler translates source files into an executable before the program runs. Install GCC or Clang using the supported package manager or official installer for the operating system. The command `cc --version` or the compiler-specific version command verifies that a compiler is available. The `-std=c17` option selects the C17 language mode; `-Wall -Wextra -Wpedantic` enables useful diagnostics. A compiler warning is not the same as runtime output, and a successful compile does not prove that the program's logic is correct.

#### Worked Example
Save the following as `hello.c`:

```c
#include <stdio.h>
int main(void)
{
    puts("C toolchain ready.");
    return 0;
}
```

Compile with `cc -std=c17 -Wall -Wextra -Wpedantic -g hello.c -o hello`. Run with `./hello` on Unix-like systems or `hello.exe` on Windows. Expected program output: `C toolchain ready.`

#### Common Mistakes
- Installing an editor extension but not installing an actual compiler.
- Using a compiler command that is not on the system PATH.
- Treating warnings, compiler errors, and program output as interchangeable.

#### Activities
1. Record the compiler name and version.
2. Compile the example with all listed warning flags and save the exact command.
3. Introduce a missing semicolon in a disposable copy, compile, and locate the diagnostic.
4. Restore the source and confirm the expected output.

#### Accessibility Practice
Use keyboard commands to open the terminal, type the compile command, and move through compiler diagnostics by line. Confirm that the terminal announces the command, exit status, and program output in sequence.

#### Skills Checklist
- [ ] I can identify whether GCC or Clang is installed.
- [ ] I can compile a C17 source file with warnings enabled.
- [ ] I can distinguish compiler diagnostics from runtime output.
- [ ] I can run the resulting executable from the terminal.

---

### Lesson 0.2: Workspace, Source Files, and First Run

#### Reading References
- Compiler documentation for source files and output files.
- Operating-system documentation for current working directories and file paths.

#### Learning Objectives
- Create a project folder and a C source file.
- Compile from the project root and run the executable.
- Explain the difference between source, executable, and working directory.

#### Concept Explanation
A source file such as `main.c` contains human-readable C code. The compiler reads the source and creates an executable such as `main` or `main.exe`. The current working directory is the directory from which the process is run; relative file paths are resolved from that directory, not automatically from the source file's location. Keep source files, headers, test files, data files, and generated binaries organized so that builds and file operations are predictable.

#### Worked Example
Create a folder named `c-first-run`, save `main.c` inside it, and use:

```sh
cd c-first-run
cc -std=c17 -Wall -Wextra -Wpedantic main.c -o main
./main
```

On Windows, run `main.exe`. The executable prints the output from Lesson 0.1. The `cd` command changes the working directory before compilation and execution.

#### Common Mistakes
- Running the compiler from a directory where the source file is not located.
- Confusing the source file name with the executable name.
- Assuming a relative data-file path is resolved relative to the source file.

#### Activities
1. Create the project folder and source file using only keyboard navigation.
2. Compile and run from the project root.
3. Run the executable from a different directory and observe how relative paths behave.
4. Rename the source file and update the compile command accordingly.

#### Accessibility Practice
Verify that the editor exposes the file tree, current file name, line numbers, and terminal focus. Navigate to the compiler command and output without using a mouse.

#### Skills Checklist
- [ ] I can create and navigate to a C project folder.
- [ ] I can identify source files and generated executables.
- [ ] I can compile and run from the project root.
- [ ] I can explain how the current working directory affects relative paths.

---

### Lesson 0.3: Editor and Accessibility Workflow

#### Reading References
- Shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md).
- Documentation for the selected editor and C language extension.

#### Learning Objectives
- Configure an editor for C source files.
- Navigate code, diagnostics, and terminal output with keyboard commands.
- Distinguish editor assistance from compiler validation.

#### Concept Explanation
A text editor edits source code; an integrated development environment may combine editing, project navigation, debugging, build commands, and language tooling. VS Code, VSCodium, and Theia can provide C language support through extensions, but the compiler remains a separate toolchain component. Configure the editor to expose diagnostics as text, preserve indentation, announce punctuation, and allow reliable keyboard movement between source, problems, and terminal panels. Extensions may provide completion and navigation, but the compiler determines whether the program is valid C for the selected language mode and target.

#### Worked Example
1. Open the `c-first-run` folder in the selected editor.
2. Open `main.c` and navigate by line and word.
3. Introduce a missing semicolon in a temporary copy.
4. Run the C17 compile command in the integrated terminal and read the diagnostic.
5. Restore the source and compile again.

Expected result: the editor allows source navigation, the compiler reports the deliberate syntax error, and the restored file compiles and runs.

#### Common Mistakes
- Assuming an editor extension installs GCC or Clang automatically.
- Relying on syntax coloring as proof that code compiles.
- Configuring a completion engine without checking whether its diagnostics are accessible.

#### Activities
1. Test keyboard-only navigation among the file tree, source editor, diagnostics, and terminal.
2. Confirm that indentation and punctuation are announced in a usable way.
3. Compare an editor warning with the compiler's diagnostic for the same source.
4. Record which editor features work with the learner's screen reader, braille display, or magnification setup.

#### Accessibility Practice
Use the learner's actual access technology and operating system. Test code navigation, punctuation verbosity, diagnostic announcements, terminal focus, and file-tree navigation. Record observed limitations rather than assuming every extension is accessible.

#### Skills Checklist
- [ ] I can open and navigate a C project without relying on a mouse.
- [ ] I can reach compiler diagnostics and terminal output.
- [ ] I can explain the difference between editor assistance and compiler validation.
- [ ] I have recorded which accessibility features were actually tested.

---

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

#### Reading References
- Compiler documentation for include paths and linker options.
- Operating-system package manager documentation.
- Shared [terminal prerequisite](../TERMINAL/TERMINAL_README.md).

#### Learning Objectives
- Identify the project root and run commands from it.
- Explain how C standard-library headers differ from external dependencies.
- Recognize include paths, library paths, and linker flags.
- Keep source, headers, build products, and project data organized.

#### Concept Explanation
C does not use a Python-style virtual environment for its standard library. The compiler toolchain provides standard headers and libraries. When a project depends on an external library, install or vendor that dependency using a documented method, then configure its header search path and linker arguments. Keep generated object files and executables separate from source. Record compiler version, dependency versions, include options, and linker options so another learner can reproduce the build.

#### Worked Example
A simple project may contain `src/main.c`, `include/`, `data/`, and `build/`. From the project root, compile with:

```sh
cc -std=c17 -Wall -Wextra -Wpedantic -Iinclude src/main.c -o build/app
```

The `-Iinclude` option adds a project header directory. External libraries may require additional `-L` and `-l` options. Do not add these options unless the selected dependency requires them.

#### Common Mistakes
- Assuming C has an automatic virtual environment or dependency resolver.
- Forgetting to document the external library version and installation method.
- Confusing compiler include paths (`-I`) with library search paths (`-L`) and linker names (`-l`).
- Committing generated executables or build output as if they were source files.

#### Activities
1. Create the `src`, `include`, `data`, and `build` folders.
2. Compile a source file from the project root using the `-Iinclude` option.
3. Record the compiler version and exact build command in a README.
4. Explain what additional information would be needed to build a project using an external JSON library.

#### Accessibility Practice
Use terminal commands to identify the current directory, list project files, change directories, compile, and run. Ensure that folder names, command output, and errors are announced sequentially by the chosen access technology.

#### Skills Checklist
- [ ] I can identify the project root and run commands from it.
- [ ] I can distinguish standard-library headers from external dependencies.
- [ ] I can explain the purpose of `-I`, `-L`, and `-l`.
- [ ] I can document a reproducible compiler command and dependency setup.

---

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
For the canonical calculator, input is bill = 24.50 and rate = 0.15. Calculate tip = bill * rate and total = bill + tip. Expected unrounded values are 3.675 and 28.175; formatted to cents they appear as 3.68 and 28.18. Test zero, typical, and large bills.

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
- Using bitwise `&`/`|` when short-circuit logical `&&`/`||` is required.
- Reversing the score and attendance conditions.
- Assuming true is represented only by integer 1; any nonzero value is true.

### Activities
1. Evaluate the score/attendance condition for (82,95), (69,95), and (82,70).
2. Create an expression where `&&` short-circuits and explain which operand is skipped.
3. Add a test for score zero and explain C's truth-value convention.
4. Write expected results for the shared scores 82, 91, 76, and 88, and include at least one boundary condition for the concept.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Boolean expressions" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Checking a lower grade boundary before a higher one and making a branch unreachable.
- Omitting the 0–100 validity check before assigning a grade.
- Using independent `if` statements when exactly one grade branch should run.

### Activities
1. Run the grade function for 91, 90, 82, 80, 76, 70, 60, and 0.
2. Add tests for 89, 79, 69, and 59 and predict the grade at each boundary.
3. Verify that -1 and 101 are rejected rather than assigned a grade.
4. Write expected results for the shared scores 82, 91, 76, and 88, and include at least one boundary condition for the concept.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Chained conditionals" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Accessing an array at index `count` instead of `count - 1` for its last element.
- Assuming C performs bounds checks automatically.
- Calculating array length after it has decayed to a pointer in a function parameter.

### Activities
1. Print each score with both its zero-based index and one-based position.
2. Change the third score from 76 to 80 and verify the updated array.
3. Explain why the valid indices for four elements are 0 through 3.
4. Write expected results for the shared scores 82, 91, 76, and 88, and include at least one boundary condition for the concept.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Sequences and indexing" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Using `i <= count` and reading beyond the final score.
- Forgetting to update the index or updating it twice.
- Calculating the average with integer division.

### Activities
1. Trace the index, running total, and output for each of the four scores.
2. Count scores greater than or equal to 80 and report the result.
3. Calculate the average using integer division and floating-point division; compare.
4. Write expected results for the shared scores 82, 91, 76, and 88, and include at least one boundary condition for the concept.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "For loops and iteration" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Writing a lowercase result into a buffer without space for the null terminator.
- Passing a negative plain `char` to `tolower` rather than an `unsigned char` value.
- Assuming byte length from `strlen` equals Unicode character count.

### Activities
1. Print the byte length and lowercase form of the canonical text sample.
2. Count occurrences of `programming` and test a missing substring.
3. Add a non-ASCII UTF-8 character and explain why byte length is not character count.
4. Write expected results for the shared scores 82, 91, 76, and 88, and include at least one boundary condition for the concept.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "String operations" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
# Unit 4: Data Structures

## Overview

Represent collections and records using C arrays, structs, pointers, and standard-library algorithms. Compare these explicit data structures with Python lists, tuples, and dictionaries, and document capacity and ownership.

Prerequisite: Unit 3. Learners should understand arrays, indexing, loops, and string basics.

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
- Treating array capacity as the number of currently valid elements.
- Appending after capacity is exhausted.
- Overwriting the original pointer with a failed `realloc` result.

### Activities
1. Append 95 and 84 while tracking count separately from capacity.
2. Attempt to append beyond capacity and design a safe rejection or growth policy.
3. Sketch a `realloc` helper that checks failure without losing the original pointer.
4. Write a small test case that proves the collection count and capacity remain distinct and that all inventory fields stay associated.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Mutable sequences" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Returning `a - b` from a comparator, which can overflow.
- Returning inconsistent results for equal values.
- Sorting only keys and accidentally separating them from their inventory record fields.

### Activities
1. Sort scores and verify the order 76, 82, 88, 91.
2. Change the comparator to descending order and test equal values.
3. Sort inventory records by quantity without separating fields from their item.
4. Write a small test case that proves the collection count and capacity remain distinct and that all inventory fields stay associated.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Sorting and organizing data" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Assuming C structs are immutable without `const`.
- Assuming copying a struct containing pointers also copies the pointed-to data.
- Relying on positional initializers when field order is unclear.

### Activities
1. Create a `Point` record for coordinates (3,4) and calculate its distance.
2. Compare designated and positional initialization for the same record.
3. Add a pointer member and explain why a struct copy is not a deep copy.
4. Write a small test case that proves the collection count and capacity remain distinct and that all inventory fields stay associated.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Immutable records" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Expecting a built-in C dictionary or hash map.
- Comparing string keys with `==` instead of `strcmp`.
- Using a search result without checking for the not-found case.

### Activities
1. Search the inventory for `Pencil` and display quantity and unit price.
2. Search for a missing key and report not found without using an invalid index.
3. Explain when an array scan becomes inefficient and a hash table is justified.
4. Write a small test case that proves the collection count and capacity remain distinct and that all inventory fields stay associated.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Maps and key-value data" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Passing an array without its count to a function.
- Using `.` on a pointer or `->` on a non-pointer object.
- Returning a pointer to a local record that no longer exists.

### Activities
1. Print all inventory items and calculate each quantity-times-price value.
2. Write a helper that receives a `const Item *` and explain the `->` operator.
3. Test the function with zero items and with all three inventory records.
4. Write a small test case that proves the collection count and capacity remain distinct and that all inventory fields stay associated.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Collection traversal" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
# Unit 5: Input and Iteration

## Overview

Build robust input loops, validate parsed values, and control repetition with while, break, continue, and explicit state. Practice the same score and menu contexts while accounting for C's input and conversion APIs.

Prerequisite: Unit 4. Learners should be able to traverse arrays and write simple conditions.

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
- Accepting `82abc` as a valid score because `strtol` parsed the numeric prefix.
- Failing to reject values outside 0–100 or detect overflow.
- Treating blank input or end-of-file as a valid score.

### Activities
1. Verify that 0, 82, and 100 are accepted as scores.
2. Verify that -1, 101, blank input, and `82abc` are rejected.
3. Test a value outside the range of `long` and check overflow handling.
4. Write a trace table for one valid input, one rejected input, and the exact state at loop termination.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Input and validation" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Failing to update the sentinel-controlled loop state.
- Ignoring `scanf`'s return value and repeatedly processing an invalid token.
- Choosing a sentinel that could also be a legitimate score without documenting the rule.

### Activities
1. Enter 82, 91, and -1 and trace the running total after each accepted score.
2. Enter -1 first and verify that the final total is zero.
3. Enter a nonnumeric token and explain why the unchecked `scanf` loop is not robust.
4. Write a trace table for one valid input, one rejected input, and the exact state at loop termination.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "While loops" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Setting the found flag before the equality test.
- Forgetting to set the flag when the target is found.
- Breaking out of the wrong loop in a nested search.

### Activities
1. Search for 76 and trace when the flag changes and when the loop breaks.
2. Search for 100 and verify the not-found branch.
3. Rewrite the search as a function returning the matching index or -1.
4. Write a trace table for one valid input, one rejected input, and the exact state at loop termination.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Flags and break" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Printing a score before applying the filter condition.
- Skipping a required state update with `continue` in a `while` loop.
- Using `< 80` when the intended filter is `>= 80`.

### Activities
1. Filter the scores and print only values greater than or equal to 80.
2. Change the threshold to 90 and predict the remaining values.
3. Rewrite the loop without `continue` and compare the trace.
4. Write a trace table for one valid input, one rejected input, and the exact state at loop termination.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Continue and filtering" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Leaving the variable in the loop condition unchanged.
- Moving the counter in the wrong direction or using a condition that cannot become false.
- Failing to trace early exits, EOF, and break conditions.

### Activities
1. Trace `remaining` from 3 to 0 and identify the terminating condition.
2. Remove the decrement in a disposable copy and explain why it loops indefinitely.
3. Add a maximum-iteration safeguard to a loop that processes untrusted input.
4. Write a trace table for one valid input, one rejected input, and the exact state at loop termination.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Infinite-loop prevention" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
# Unit 6: Functions

## Overview

Decompose programs into functions with clear parameter, return, array-count, and pointer contracts. Understand pass-by-value, scope, and the additional responsibilities of variadic interfaces.

Prerequisite: Unit 5. Learners should be comfortable with loops, arrays, and validated input.

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
- Calling a function before its prototype is visible.
- Declaring a non-void function but failing to return a value on every path.
- Combining calculation and printing so the function cannot be reused by another caller.

### Activities
1. Write `calculate_tip` and call it for a $24.50 bill at 15%.
2. Move the function below `main` and add a correct prototype.
3. Separate calculation from printing so a second caller can reuse the result.
4. Document the function contract: parameter types, return type, array count or pointer ownership where relevant, and the expected result for one call.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Defining functions" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Assuming C passes ordinary arguments by reference.
- Swapping positional arguments with the same type and expecting the compiler to detect intent.
- Passing a pointer where the function expects a value or vice versa.

### Activities
1. Call `total_with_tip(24.50, 0.15)` and predict the output.
2. Swap the arguments and explain why C cannot infer their semantic roles when types match.
3. Write a second function that modifies a caller's integer through a pointer.
4. Document the function contract: parameter types, return type, array count or pointer ownership where relevant, and the expected result for one call.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Parameters and arguments" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Omitting a return on one control-flow path.
- Returning a pointer to a local automatic variable.
- Returning a value that is silently converted to an unintended type.

### Activities
1. Call the score-summing function with the shared four values and verify 337.
2. Test a one-element array and an empty collection.
3. Add an average function and define behavior for count zero.
4. Document the function contract: parameter types, return type, array count or pointer ownership where relevant, and the expected result for one call.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Return values" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Assuming an array parameter carries its length.
- Passing a count larger than the actual array.
- Dividing by zero for an empty collection without defining a result.

### Activities
1. Calculate the average of the shared scores using the array-plus-count interface.
2. Test count zero and document the function's defined result.
3. Add a maximum function and test one-element and repeated-maximum arrays.
4. Document the function contract: parameter types, return type, array count or pointer ownership where relevant, and the expected result for one call.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Functions over collections" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Using a block-local variable outside its scope.
- Passing the wrong promoted type to `va_arg`.
- Forgetting `va_end` or passing a variadic count inconsistent with the arguments.

### Activities
1. Move a variable into a nested block and test its scope.
2. Call the variadic sum with the four shared scores and verify 337.
3. Replace the variadic interface with an array-plus-count function and compare type safety.
4. Document the function contract: parameter types, return type, array count or pointer ownership where relevant, and the expected result for one call.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Scope and variadic arguments" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
# Unit 7: Structs and Object Models

## Overview

Use structs and functions to organize related data and behavior. C does not provide class methods or built-in inheritance; use composition and explicit interfaces, and document pointer ownership and object lifetime.

Prerequisite: Unit 6. Learners should understand functions, pointers, and record fields.

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
- Describing a C struct as a class with built-in methods and constructors.
- Failing to separate public declarations from implementation details in headers and source files.
- Using pointer fields without documenting ownership and lifetime.

### Activities
1. Define an `Item` struct with name, quantity, and unit price.
2. Move the declaration into a header and include it from a source file.
3. Explain why C structs group fields but do not supply methods or automatic constructors.
4. Document the struct fields, initialization values, ownership rules, and the expected state after one operation.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Types and object models" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Using field-order initialization incorrectly.
- Leaving a field unintentionally uninitialized in an automatic object.
- Assuming struct assignment performs a deep copy of pointer members.

### Activities
1. Initialize Notebook, Pencil, and Folder with designated initializers.
2. Copy one record and explain which data is copied when a member is a pointer.
3. Change one record's quantity and verify the other instance is unchanged.
4. Document the struct fields, initialization values, ownership rules, and the expected state after one operation.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Creating instances" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Confusing `.` and `->` member access.
- Dereferencing a null pointer.
- Omitting `const` when a function should only inspect an item.

### Activities
1. Calculate the value of three notebooks through `item_value`.
2. Compare `.` member access on an object with `->` on a pointer.
3. Add a null-pointer check and a `const` parameter.
4. Document the struct fields, initialization values, ownership rules, and the expected state after one operation.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Fields and methods" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Claiming C has native class inheritance or virtual dispatch.
- Treating an embedded struct as automatically substitutable for its containing type.
- Using function pointers without a matching declared signature.

### Activities
1. Create a `StockedItem` by embedding an `Item` and a reorder threshold.
2. Test quantities below, equal to, and above the threshold.
3. Explain why this composition is not C++-style inheritance.
4. Document the struct fields, initialization values, ownership rules, and the expected state after one operation.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Inheritance and interfaces" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Calling composition inheritance.
- Allowing the task count to exceed the fixed array capacity.
- Failing to define whether nested strings are owned or borrowed.

### Activities
1. Create a task manager with two tasks and print completion states.
2. Attempt to add an eleventh task to a ten-slot manager and handle capacity safely.
3. Document whether the manager owns task strings or borrows pointers.
4. Document the struct fields, initialization values, ownership rules, and the expected state after one operation.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Composition" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
# Unit 8: Files, Errors, and Persistence

## Overview

Read and write files with explicit error checks and resource cleanup. Distinguish standard C error reporting from exceptions, and use a maintained external library for JSON rather than ad hoc parsing.

Prerequisite: Unit 7. Learners should understand structs, pointers, and function return contracts.

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
- Using a `FILE *` after `fopen` returned `NULL`.
- Treating every failed `fgets` as normal EOF without checking `ferror`.
- Assuming a relative path is based on the source file location rather than the current working directory.

### Activities
1. Create a two-line notes file and verify that both lines are read.
2. Run with the file missing and inspect the diagnostic and exit status.
3. Create an overlong line and explain how truncation can be detected.
4. Record the file or data operation's success result, failure result, and the resource cleanup expected on each path.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Reading text files" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Opening in `w` mode and truncating a file that should have been appended.
- Ignoring `fprintf` and `fclose` failure results.
- Assuming buffered output has necessarily reached durable storage before close.

### Activities
1. Append a second note and verify that the original contents remain.
2. Run the append program twice and count the resulting lines.
3. Change append mode to write mode in a disposable copy and observe truncation.
4. Record the file or data operation's success result, failure result, and the resource cleanup expected on each path.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Writing and appending files" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Expecting C to provide language-level exceptions.
- Ignoring a function's documented error return convention or `errno`.
- Continuing with invalid state after reporting an error.

### Activities
1. Run with a missing file and identify the error return and diagnostic.
2. Run with an existing file and verify the success path.
3. Write a helper that returns an error code to its caller rather than printing inside the helper.
4. Record the file or data operation's success result, failure result, and the resource cleanup expected on each path.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Errors and exceptions" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Returning from a function after acquiring a resource without releasing it.
- Closing a file twice or using it after close.
- Running cleanup on a resource that was never successfully acquired.

### Activities
1. Trace both the successful and failed `fopen` paths and locate the `fclose`.
2. Add a second resource and determine the correct cleanup order.
3. Introduce an early error after opening the file and verify that cleanup still occurs.
4. Record the file or data operation's success result, failure result, and the resource cleanup expected on each path.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Resource cleanup" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Trying to parse arbitrary JSON with comma splitting or substring search.
- Failing to validate required fields and JSON value types.
- Leaking parser-owned memory or retaining pointers after the JSON document is freed.

### Activities
1. Map each canonical capstone field to a C member and a JSON value type.
2. Select a maintained C JSON library and document its version and link command.
3. Test missing required fields, malformed JSON, and a valid round-trip record.
4. Record the file or data operation's success result, failure result, and the resource cleanup expected on each path.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "JSON persistence" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
# Unit 9: Testing and Data Analysis

## Overview

Test functions and state changes, use pseudo-random values responsibly, and analyze text and CSV records while recognizing the limits of byte-oriented C examples and simple parsers.

Prerequisite: Unit 8. Learners should understand functions, structs, files, and error handling.

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
- Testing only one ordinary input and omitting boundaries and invalid cases.
- Writing assertions that duplicate implementation details instead of checking expected behavior.
- Compiling with `NDEBUG` and assuming assertions still execute.

### Activities
1. Test addition with positive, negative, and zero values.
2. Create one failing assertion and inspect the diagnostic.
3. Compile with and without `NDEBUG` and explain the effect on assertions.
4. Write the expected test result and explain what a failing assertion or diagnostic would indicate.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Testing functions" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Allowing one test's mutation to leak into another test.
- Checking only the function result rather than the changed item state.
- Failing to verify that a rejected restock leaves quantity unchanged.

### Activities
1. Restock by a positive amount and verify quantity changes.
2. Try zero and negative restock amounts and verify state remains unchanged.
3. Create fresh records for each test to prevent test-order dependence.
4. Write the expected test result and explain what a failing assertion or diagnostic would indicate.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Testing stateful objects" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Treating `rand()` as cryptographically secure.
- Assuming `% 6` produces perfectly unbiased die rolls.
- Expecting the exact sequence to be portable across different C library implementations.

### Activities
1. Run twice with the same seed on the same C library and compare results.
2. Generate 1000 die values and verify each is between 1 and 6.
3. Explain why modulo reduction may be biased and why `rand` is not for secrets.
4. Write the expected test result and explain what a failing assertion or diagnostic would indicate.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Random values" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Counting substring matches as whole words.
- Passing a negative plain `char` to `tolower`.
- Treating ASCII byte operations as Unicode-aware tokenization.

### Activities
1. Count the two `programming` occurrences in the canonical sample.
2. Change case and punctuation and compare substring count with whole-word count.
3. Test a UTF-8 input and document the limits of byte-wise lowercase conversion.
4. Write the expected test result and explain what a failing assertion or diagnostic would indicate.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Text analysis" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Splitting every CSV line on commas despite quoted commas and escaped quotes.
- Ignoring overlong lines or malformed rows.
- Assuming every row contains the same number of fields without validating it.

### Activities
1. Create the canonical students.csv header and two data rows.
2. Test missing file, empty file, and an overlong row.
3. Add a quoted comma and explain why naive comma splitting is invalid CSV parsing.
4. Write the expected test result and explain what a failing assertion or diagnostic would indicate.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "CSV records" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
# Unit 10: Applied Projects

## Overview

Apply C data structures, control flow, input validation, and state transitions to a text adventure and a command-line to-do manager. Prioritize explicit feedback, keyboard navigation, and safe handling of fixed-capacity data.

Prerequisite: Units 1–9. Learners should be able to build and test a small multi-function program.

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
- Starting implementation without defining acceptance criteria and failure cases.
- Omitting empty-list, duplicate-ID, invalid-input, and unavailable-storage behavior.
- Selecting a persistence format without documenting its limitations.

### Activities
1. Write acceptance criteria for add, view, edit, delete, and save/load operations.
2. Define behavior for empty data, duplicate IDs, unknown IDs, and unavailable storage.
3. Draw a module plan separating input, validation, data operations, persistence, and output.
4. Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Requirements and design" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Using a room exit index without checking that it is valid.
- Changing the current room before confirming the requested exit exists.
- Giving no feedback when a direction is blocked or unknown.

### Activities
1. Move north from the start room and verify the tunnel description.
2. Attempt west from the start room and verify that the room does not change.
3. Add case-insensitive direction commands and a quit command.
4. Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Text adventure: rooms and movement" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Allowing the key to be collected more than once.
- Unlocking the door without checking both the inventory and the player's room.
- Updating item location and inventory inconsistently, duplicating or losing the key.

### Activities
1. Take the key and verify it leaves the room and enters inventory.
2. Try taking the key twice and verify the second attempt is rejected.
3. Test unlocking without the key and from the wrong room.
4. Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Text adventure: inventory and puzzles" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Writing beyond the fixed task array's capacity.
- Treating the first character of a menu line as fully validated input.
- Completing or deleting a task by index without checking the selected range.

### Activities
1. Add two tasks and view them in insertion order.
2. Complete a task by ID and reject an unknown ID.
3. Implement save/load and verify data remains after restarting.
4. Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Command-line to-do manager" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Using color or a symbol as the only indication of completion.
- Displaying an error without telling the user how to correct it.
- Silently truncating an overlong title or failing to announce a successful operation.

### Activities
1. Complete the menu workflow using keyboard only and read prompts sequentially.
2. Submit blank, overlong, and invalid menu input and verify corrective instructions.
3. Test with a named screen reader and OS; record observed results rather than assuming compatibility.
4. Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Accessible UX and validation" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
# Unit 11: Capstone: Personal Data Manager

## Overview

Plan, implement, test, document, and present a C personal-data manager using the shared record fields and required CRUD/persistence behavior. Preserve the Python capstone's data and functional requirements while using a C-appropriate terminal-first interface.

Prerequisite: Units 1–10. Learners should be able to organize structs, functions, files, validation, and tests.

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
- Omitting one of add, view, edit, delete, save, or load from the requirements.
- Designing a GUI-specific solution despite selecting a terminal interface.
- Failing to define required fields, validation, and acceptance tests.

### Activities
1. Choose a capstone domain and list fields, validation rules, and user operations.
2. Write acceptance tests for add, view, edit, delete, save, and load before implementation.
3. Document why the C implementation uses a terminal interface rather than the Python-specific NiceGUI framework.
4. Add one capstone acceptance-test case to the project test plan, including test data, expected persisted fields, and failure behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Capstone requirements" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Using fixed-size fields without documenting maximum lengths and truncation policy.
- Generating duplicate IDs or inconsistent timestamp formats.
- Serializing only part of the canonical record or trusting loaded fields without validation.

### Activities
1. Define every C record field and its maximum length or allocation strategy.
2. Specify ID generation, timestamp format, and string ownership.
3. Round-trip a record through the chosen JSON library and compare every field.
4. Add one capstone acceptance-test case to the project test plan, including test data, expected persisted fields, and failure behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Data model and storage" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Using an unchecked lookup result as an array index.
- Copying a title into a fixed-size buffer without checking length.
- Changing in-memory state before persistence succeeds without a recovery strategy.

### Activities
1. Add two records and verify their stable display order.
2. Edit one record by ID and confirm unrelated fields remain unchanged.
3. Delete an existing record, then attempt to delete the same ID again.
4. Add one capstone acceptance-test case to the project test plan, including test data, expected persisted fields, and failure behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Create/read/update/delete" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Testing only successful operations and ignoring malformed input or missing files.
- Ignoring compiler warnings or sanitizer diagnostics.
- Using assertions for recoverable user input errors in the release application.

### Activities
1. Create a test matrix for valid, boundary, malformed, missing-file, and unknown-ID cases.
2. Compile with warnings and address every diagnostic.
3. Run AddressSanitizer and UndefinedBehaviorSanitizer where available and investigate reports.
4. Add one capstone acceptance-test case to the project test plan, including test data, expected persisted fields, and failure behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Validation and testing" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
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
- Omitting compiler version, build command, or dependency setup from the README.
- Claiming assistive-technology compatibility without testing a named screen reader and OS.
- Leaving sample data, menu commands, or known limitations undocumented.

### Activities
1. Build and run the project from a clean checkout using only the README instructions.
2. Document compiler, dependency versions, build command, file paths, and menu commands.
3. Test the documented keyboard workflow with a named access technology and record limitations.
4. Add one capstone acceptance-test case to the project test plan, including test data, expected persisted fields, and failure behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Documentation and presentation" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
