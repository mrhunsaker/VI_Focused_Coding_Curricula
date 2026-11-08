# C++: Complete Curriculum — Units 0–11

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

## Course Overview

C++ is used in game engines, simulation, robotics, finance, desktop software, and performance-critical systems.

This course intentionally parallels the original Python curriculum. It reuses problem contexts—greetings, profiles, a calculator, grade decisions, score collections, inventory, functions, text files, tests, text analysis, CSV, a to-do list, and a personal-data manager—so the principal new learning target is the C++ language. The syntax and implementation remain idiomatic, not a mechanical translation.

# Unit 0: Accessible Environment and Toolchain

## Overview
Install a C++20 compiler, configure an editor, create a reproducible project workspace, and verify keyboard and assistive-technology access to source code, diagnostics, and terminal output.

## Lesson 0.1: Install and Verify C++

### Reading References
- GCC, Clang, or Microsoft C++ compiler installation documentation.
- C++ language support and compiler-version documentation.

### Learning Objectives
- Identify the compiler and its version.
- Compile, link, and run a minimal C++20 program.
- Explain the difference between a compiler diagnostic and program output.

### Concept Explanation
C++ is a compiled language. The compiler translates each translation unit; the linker combines object code and required libraries into an executable. The course uses C++20. Keep the compiler, editor language service, and command-line build on the same standard.

### Worked Example
```cpp
#include <iostream>
int main() {
    std::cout << "Hello, C++20!\n";
    return 0;
}

```
Compile with `c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror -g main.cpp -o main`; run with `./main` (or the platform executable form).

### Expected Behavior or Output

The compile command prints nothing when there are no warnings. Running the program prints one line:
```text
Hello, C++20!
```
This output was observed with g++ 13.3 on Linux.

### Common Mistakes
- Installing only editor syntax highlighting and assuming it includes a compiler.
- Omitting the C++20 standard flag and unknowingly using a different language baseline.
- Treating a compiler error as output produced by the running program.

### Activities
1. Install GCC, Clang, or MSVC and record its exact version.
2. Compile and run the example from the terminal.
3. Remove the semicolon after the output statement, compile again, and locate the diagnostic.
4. Restore the semicolon and confirm that the build succeeds.

### Accessibility Practice
Navigate the source by line, word, and character. Confirm that punctuation, braces, indentation, compiler diagnostics, and terminal output can be read without relying on color or mouse-only controls.

### Skills Checklist
- [ ] I can identify the installed compiler and version.
- [ ] I can compile and link a C++20 program from the terminal.
- [ ] I can run the executable and distinguish its output from diagnostics.
- [ ] I can navigate the source and diagnostic text with my access technology.

## Lesson 0.2: Workspace and First Run

### Reading References
- Compiler command-line documentation.
- The shared terminal prerequisite.

### Learning Objectives
- Create a course workspace and source file.
- Identify the current working directory and executable path.
- Rebuild and run a program after changing its source.

### Concept Explanation
A source file such as `main.cpp` is input to the compiler; it is not itself the executable. Relative paths are interpreted from the process's current working directory. Keep source files separate from generated executables and temporary build output.

### Worked Example
```sh
mkdir -p cpp-course/hello
cd cpp-course/hello
# Save the C++ example as main.cpp
c++ -std=c++20 -Wall -Wextra -Wpedantic main.cpp -o hello
./hello
```

### Expected Behavior or Output

Compiling prints nothing when the source is correct, and `./hello` prints:
```text
Hello, C++20!
```

### Common Mistakes
- Running the compile command from a directory that does not contain the source file.
- Editing one copy of a file while compiling a different copy.
- Confusing the source filename with the executable filename.

### Activities
1. Create a course folder and a `hello` subfolder.
2. Save the first program as `main.cpp` and compile it to `hello`.
3. Change the output text, rebuild, and verify the new output.
4. List the folder contents and identify source versus generated files.

### Accessibility Practice
Use terminal commands to confirm the working directory and list files. Navigate the folder tree with keyboard commands and verify the executable name from text output.

### Skills Checklist
- [ ] I can create and navigate a project directory.
- [ ] I can identify the current working directory.
- [ ] I can compile a named source file into a separate executable.
- [ ] I can rebuild after an edit and verify the changed output.

## Lesson 0.3: Editor and Accessibility Workflow

### Reading References
- [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md).
- Documentation for the chosen editor's C++ language extension and screen-reader support.

### Learning Objectives
- Open the project root rather than an individual source file only.
- Configure C++ language services and compiler selection.
- Navigate source, diagnostics, terminal, and project files by keyboard.

### Concept Explanation
An editor provides text editing; an IDE adds integrated language services, build, debugging, and project navigation. VS Code, VSCodium, and Theia can provide C++ support through extensions, but their extension marketplaces differ. A language server is not a substitute for an installed compiler.

### Worked Example
Open the folder containing `main.cpp`, install the appropriate C++ language extension, select the same compiler used in the terminal, and confirm that diagnostics identify a deliberately introduced syntax error.

### Expected Behavior or Output

The editor shows a diagnostic at the syntax error that you introduce, with a line number and message that match what the compiler prints in the terminal. After you fix the error, the editor and the compiler are both clean.

### Common Mistakes
- Opening only a file instead of the project root, preventing project-level configuration from loading.
- Installing an extension from a marketplace unavailable to the selected editor distribution.
- Assuming code completion or syntax highlighting proves that the compiler is configured.

### Activities
1. Open the project folder in VS Code, VSCodium, or Theia.
2. Verify language-server diagnostics and compiler selection.
3. Navigate to a line, inspect punctuation, and read a diagnostic using the screen reader.
4. Build and run from the integrated terminal, then repeat from the system terminal.

### Accessibility Practice
Test keyboard-only access to the editor, file tree, diagnostics panel, integrated terminal, and output. Adjust punctuation verbosity and indentation announcements to a usable level.

### Skills Checklist
- [ ] I can open the project root in my chosen editor.
- [ ] I can identify the C++ extension and compiler configuration.
- [ ] I can navigate diagnostics and terminal output by keyboard.
- [ ] I can complete the build/run workflow without mouse-only actions.

## Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

### Reading References
- CMake getting-started documentation.
- Compiler and linker command-line documentation.

### Learning Objectives
- Explain the working directory and the roles of source, header, object, and executable files.
- Compile and link a multi-file project.
- Record external dependencies and reproducible build instructions.

### Concept Explanation
C++ dependencies may be supplied by the standard library or external libraries. Header lookup happens during preprocessing/compilation; unresolved external symbols are generally linker errors. Larger projects should record build configuration and use an out-of-source build directory such as a CMake `build/` folder.

### Worked Example
```sh
c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror -g main.cpp helper.cpp -o app
./app
```

### Expected Behavior or Output

The compile command builds one program from both source files and prints nothing when it succeeds; `./app` then runs it. If `helper.cpp` is left off the command, the linker reports an undefined reference error.

### Common Mistakes
- Running a relative path from the wrong working directory.
- Treating a missing header as a linker error.
- Omitting a required implementation file or library from the link command.

### Activities
1. Compile a one-file program from the project root and record the exact command.
2. Split a program into a header, implementation file, and `main.cpp`; compile and link all translation units.
3. Remove one implementation file from the command and interpret the linker diagnostic.
4. Record compiler version, standard flag, dependencies, and build steps in a README.

### Accessibility Practice
Navigate each project file and terminal diagnostic by keyboard. Confirm that build errors can be read sequentially and are not communicated by color alone.

### Skills Checklist
- [ ] I can identify the project root and run commands from it.
- [ ] I can explain the difference between a header error and a linker error.
- [ ] I can compile and link a multi-file project.
- [ ] I can document dependencies and reproducible build steps.

# Unit 1: Foundations of Computing

## Overview

This unit covers computer science, hardware/software, algorithms, first program, variables, primitive types. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 1.1: Computer science and problem solving

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Computer science and problem solving is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: distinguish an algorithm from its C++ implementation; a clean build does not prove algorithmic correctness.

### Worked Example
```cpp
std::cout << "Computer science turns problems into precise, testable steps.\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Computer science turns problems into precise, testable steps.
```

### Common Mistakes
- A successful compile does not establish that the algorithm satisfies the requirement.
- Distinguish an algorithm from its C++ implementation.
- A clean build does not prove algorithmic correctness.

### Activities
1. Trace the computer science and problem solving example and predict its output before compiling.
2. Adapt the example to Avery's profile and greeting and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 1.2: Your first program

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Your first program is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: provide main with the correct signature; include the declaration header and use std::cout.

### Worked Example
```cpp
const std::string greeting_name = "Avery"; std::cout << "Hello, " << greeting_name << "!\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Hello, Avery!
```

### Common Mistakes
- Forgetting to rebuild after editing can leave an older executable on disk.
- Provide main with the correct signature.
- Include the declaration header and use std::cout.

### Activities
1. Trace the your first program example and predict its output before compiling.
2. Adapt the example to Avery's profile and greeting and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 1.3: Variables and data types

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Variables and data types is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: initialize every built-in variable; select types that preserve fractional values; distinguish assignment from equality.

### Worked Example
```cpp
const std::string name = "Avery"; const int age = 16; const double height_m = 1.72; const std::string favorite = "Computer Science"; std::cout << name << ", " << age << ", " << height_m << " m, " << favorite << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Avery, 16, 1.72 m, Computer Science
```

### Common Mistakes
- Initialize every built-in variable.
- Select types that preserve fractional values.
- Distinguish assignment from equality.

### Activities
1. Trace the variables and data types example and predict its output before compiling.
2. Adapt the example to Avery's profile and greeting and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain variables and data types using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for Avery's profile and greeting without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

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

# Unit 3: Control Flow

## Overview

This unit covers Boolean expressions, conditionals, lists or arrays, iteration, string operations. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 3.1: Boolean expressions

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Boolean expressions is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: use && and || for logical operations; compare with ==; use boolalpha when textual boolean output is required.

### Worked Example
```cpp
const int score = 82; const bool passed = score >= 60 && score <= 100; std::cout << std::boolalpha << "Valid passing score: " << passed << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Valid passing score: true
```

### Common Mistakes
- Use && and || for logical operations.
- Compare with ==.
- Use boolalpha when textual boolean output is required.

### Activities
1. Trace the boolean expressions example and predict its output before compiling.
2. Adapt the example to grade thresholds and score collections and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 3.2: Chained conditionals

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Chained conditionals is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: test the most restrictive grade threshold first; include exact boundary values; make score ranges exhaustive and non-overlapping.

### Worked Example
```cpp
for (int score : {59, 60, 79, 80, 89, 90, 100}) { const char grade = score >= 90 ? 'A' : score >= 80 ? 'B' : score >= 70 ? 'C' : score >= 60 ? 'D' : 'F'; std::cout << score << ": " << grade << '\n'; }

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
59: F
60: D
79: C
80: B
89: B
90: A
100: A
```

### Common Mistakes
- Test the most restrictive grade threshold first.
- Include exact boundary values.
- Make score ranges exhaustive and non-overlapping.

### Activities
1. Trace the chained conditionals example and predict its output before compiling.
2. Adapt the example to grade thresholds and score collections and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 3.3: Sequences and indexing

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Sequences and indexing is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: check vector bounds and emptiness; remember zero-based indexing; treat size as a count rather than a final index.

### Worked Example
```cpp
std::vector<int> scores{82, 91, 76, 88}; std::cout << "First: " << scores.at(0) << "; fourth: " << scores.at(3) << "; count: " << scores.size() << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
First: 82; fourth: 88; count: 4
```

### Common Mistakes
- Check vector bounds and emptiness.
- Remember zero-based indexing.
- Treat size as a count rather than a final index.

### Activities
1. Trace the sequences and indexing example and predict its output before compiling.
2. Adapt the example to grade thresholds and score collections and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 3.4: For loops and iteration

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
For loops and iteration is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: avoid invalidating iterators while traversing; use an accumulator with a suitable type; define the empty-collection case.

### Worked Example
```cpp
const std::vector<int> scores{82, 91, 76, 88}; int sum = 0; for (int score : scores) sum += score; std::cout << "Total: " << sum << "; average: " << static_cast<double>(sum) / scores.size() << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Total: 337; average: 84.25
```

### Common Mistakes
- Avoid invalidating iterators while traversing.
- Use an accumulator with a suitable type.
- Define the empty-collection case.

### Activities
1. Trace the for loops and iteration example and predict its output before compiling.
2. Adapt the example to grade thresholds and score collections and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 3.5: String operations

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
String operations is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: treat std::string indexing as byte-oriented; pass unsigned char to cctype functions; remember substr takes a length.

### Worked Example
```cpp
std::string text = "Avery Studies Programming"; std::transform(text.begin(), text.end(), text.begin(), [](unsigned char ch) { return static_cast<char>(std::tolower(ch)); }); std::cout << text << "; length: " << text.size() << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
avery studies programming; length: 25
```

### Common Mistakes
- Treat std::string indexing as byte-oriented.
- Pass unsigned char to cctype functions.
- Remember substr takes a length.

### Activities
1. Trace the string operations example and predict its output before compiling.
2. Adapt the example to grade thresholds and score collections and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain string operations using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for grade thresholds and score collections without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

# Unit 4: Data Structures

## Overview

This unit covers sequence mutation, sorting, immutable records, maps, dictionaries, traversal. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 4.1: Mutable sequences

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Mutable sequences is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: check before pop_back; do not retain references across vector reallocation; use the iterator returned by erase.

### Worked Example
```cpp
std::vector<std::string> items{"Notebook", "Pencil"}; items.insert(items.begin() + 1, "Folder"); items.push_back("Eraser"); items.erase(items.begin()); for (const auto& item : items) std::cout << item << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Folder
Pencil
Eraser
```

### Common Mistakes
- Check before pop_back.
- Do not retain references across vector reallocation.
- Use the iterator returned by erase.

### Activities
1. Trace the mutable sequences example and predict its output before compiling.
2. Adapt the example to inventory records and key-value quantities and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 4.2: Sorting and organizing data

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Sorting and organizing data is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: write a strict-weak-order comparator; sort by the field required by the task; use a compatible iterator category.

### Worked Example
```cpp
std::vector<int> quantities{10, 3, 4, 1}; std::sort(quantities.begin(), quantities.end()); std::reverse(quantities.begin(), quantities.end()); for (int quantity : quantities) std::cout << quantity << ' '; std::cout << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
10 4 3 1 
```

### Common Mistakes
- Write a strict-weak-order comparator.
- Sort by the field required by the task.
- Use a compatible iterator category.

### Activities
1. Trace the sorting and organizing data example and predict its output before compiling.
2. Adapt the example to inventory records and key-value quantities and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 4.3: Immutable records

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Immutable records is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: understand const members' effect on assignment; avoid dangling references; distinguish const objects from mutable indirection.

### Worked Example
```cpp
struct Coordinate { const int x; const int y; }; const Coordinate point{3, 4}; std::cout << "Point: (" << point.x << ", " << point.y << ")\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Point: (3, 4)
```

### Common Mistakes
- Understand const members' effect on assignment.
- Avoid dangling references.
- Distinguish const objects from mutable indirection.

### Activities
1. Trace the immutable records example and predict its output before compiling.
2. Adapt the example to inventory records and key-value quantities and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 4.4: Maps and key-value data

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Maps and key-value data is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: use find/contains for non-inserting lookup; remember map orders by key; avoid operator[] on const maps.

### Worked Example
```cpp
std::map<std::string, int> inventory{{"Notebook", 3}, {"Pencil", 10}, {"Folder", 4}}; inventory["Notebook"] += 1; std::cout << "Notebook count: " << inventory.at("Notebook") << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Notebook count: 4
```

### Common Mistakes
- Use find/contains for non-inserting lookup.
- Remember map orders by key.
- Avoid operator[] on const maps.

### Activities
1. Trace the maps and key-value data example and predict its output before compiling.
2. Adapt the example to inventory records and key-value quantities and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 4.5: Collection traversal

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Collection traversal is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: prefer const auto& for read-only traversal; do not mutate the traversed container; initialize accumulators.

### Worked Example
```cpp
const std::map<std::string, int> inventory{{"Notebook", 3}, {"Pencil", 10}, {"Folder", 4}}; for (const auto& [name, quantity] : inventory) std::cout << name << " => " << quantity << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Folder => 4
Notebook => 3
Pencil => 10
```

### Common Mistakes
- Prefer const auto& for read-only traversal.
- Do not mutate the traversed container.
- Initialize accumulators.

### Activities
1. Trace the collection traversal example and predict its output before compiling.
2. Adapt the example to inventory records and key-value quantities and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain collection traversal using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for inventory records and key-value quantities without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

# Unit 5: Input and Iteration

## Overview

This unit covers input validation, sentinel loops, while loops, flags, break/continue, infinite-loop prevention. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 5.1: Input and validation

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Input and validation is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: validate extraction and the allowed range; handle conversion exceptions; define a policy for empty input.

### Worked Example
```cpp
std::istringstream input("16"); int age = 0; if (!(input >> age) || age < 0 || age > 130) std::cout << "Enter a valid age from 0 to 130\n"; else std::cout << "Accepted age: " << age << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Accepted age: 16
```

### Common Mistakes
- Validate extraction and the allowed range.
- Handle conversion exceptions.
- Define a policy for empty input.

### Activities
1. Trace the input and validation example and predict its output before compiling.
2. Adapt the example to validated input and sentinel-driven loops and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 5.2: While loops

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
While loops is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: update the loop condition and sentinel correctly; decide whether the sentinel is data; stop cleanly on failed extraction.

### Worked Example
```cpp
std::istringstream input("1 2 3 0"); int value = 0, total = 0; while (input >> value && value != 0) total += value; std::cout << "Sum before sentinel: " << total << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Sum before sentinel: 6
```

### Common Mistakes
- Update the loop condition and sentinel correctly.
- Decide whether the sentinel is data.
- Stop cleanly on failed extraction.

### Activities
1. Trace the while loops example and predict its output before compiling.
2. Adapt the example to validated input and sentinel-driven loops and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 5.3: Flags and break

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Flags and break is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: place break in the intended loop; handle nested-loop exit deliberately; report the not-found case.

### Worked Example
```cpp
const std::vector<std::string> names{"Avery", "Jordan", "Sam"}; bool found = false; for (const auto& name : names) { if (name == "Jordan") { found = true; break; } } std::cout << "Jordan found: " << std::boolalpha << found << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Jordan found: true
```

### Common Mistakes
- Place break in the intended loop.
- Handle nested-loop exit deliberately.
- Report the not-found case.

### Activities
1. Trace the flags and break example and predict its output before compiling.
2. Adapt the example to validated input and sentinel-driven loops and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 5.4: Continue and filtering

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Continue and filtering is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: filter before producing output; ensure continue does not skip required state updates; verify comparison direction.

### Worked Example
```cpp
for (int value : {-2, 3, 0, 5, -1}) { if (value <= 0) continue; std::cout << value << ' '; } std::cout << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
3 5 
```

### Common Mistakes
- Filter before producing output.
- Ensure continue does not skip required state updates.
- Verify comparison direction.

### Activities
1. Trace the continue and filtering example and predict its output before compiling.
2. Adapt the example to validated input and sentinel-driven loops and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 5.5: Infinite-loop prevention

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Infinite-loop prevention is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: bound retries; increment the attempt count on every attempt; reset validation state before retrying.

### Worked Example
```cpp
int attempts = 0; bool valid = false; while (!valid && attempts < 3) { ++attempts; valid = attempts == 2; } std::cout << "Attempts: " << attempts << "; valid: " << std::boolalpha << valid << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Attempts: 2; valid: true
```

### Common Mistakes
- Bound retries.
- Increment the attempt count on every attempt.
- Reset validation state before retrying.

### Activities
1. Trace the infinite-loop prevention example and predict its output before compiling.
2. Adapt the example to validated input and sentinel-driven loops and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain infinite-loop prevention using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for validated input and sentinel-driven loops without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

# Unit 6: Functions

## Overview

This unit covers definitions, parameters, arguments, return values, scope, collection parameters, variadic functions. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 6.1: Defining functions

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Defining functions is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: declare functions before use; ensure every non-void path returns; match return types to the contract.

### Worked Example
```cpp
const auto calculate_total = [](double bill, double rate) { return bill * (1.0 + rate); }; std::cout << "Bill plus tip: $" << calculate_total(24.50, 0.15) << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Bill plus tip: $28.175
```

### Common Mistakes
- Declare functions before use.
- Ensure every non-void path returns.
- Match return types to the contract.

### Activities
1. Trace the defining functions example and predict its output before compiling.
2. Adapt the example to reusable score and inventory functions and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 6.2: Parameters and arguments

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Parameters and arguments is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: pass large read-only objects by const reference; use non-const references only for intended mutation; avoid shadowing.

### Worked Example
```cpp
const auto label = [](const std::string& name, int score) { return name + ": " + std::to_string(score); }; std::cout << label("Avery", 92) << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Avery: 92
```

### Common Mistakes
- Pass large read-only objects by const reference.
- Use non-const references only for intended mutation.
- Avoid shadowing.

### Activities
1. Trace the parameters and arguments example and predict its output before compiling.
2. Adapt the example to reusable score and inventory functions and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 6.3: Return values

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Return values is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: never return a reference to a local; document failure/sentinel behavior; distinguish returning a value from printing.

### Worked Example
```cpp
const auto tip_total = [](double bill, double rate) { return bill * (1.0 + rate); }; const double total = tip_total(24.50, 0.15); std::cout << "Total: $" << total << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Total: $28.175
```

### Common Mistakes
- Never return a reference to a local.
- Document failure/sentinel behavior.
- Distinguish returning a value from printing.

### Activities
1. Trace the return values example and predict its output before compiling.
2. Adapt the example to reusable score and inventory functions and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 6.4: Functions over collections

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Functions over collections is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: avoid copying a collection when a const reference suffices; define empty-input behavior; select an accumulator wide enough.

### Worked Example
```cpp
const auto average = [](const std::vector<int>& scores) { if (scores.empty()) return 0.0; const int sum = std::accumulate(scores.begin(), scores.end(), 0); return static_cast<double>(sum) / scores.size(); }; std::cout << "Average: " << average({82, 91, 76, 88}) << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Average: 84.25
```

### Common Mistakes
- Avoid copying a collection when a const reference suffices.
- Define empty-input behavior.
- Select an accumulator wide enough.

### Activities
1. Trace the functions over collections example and predict its output before compiling.
2. Adapt the example to reusable score and inventory functions and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 6.5: Scope and variadic arguments

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Scope and variadic arguments is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: respect block scope; write fold expressions that match the parameter pack; constrain or document mixed argument types.

### Worked Example
```cpp
const auto sum = []<typename... Values>(Values... values) { return (values + ...); }; std::cout << "Sum: " << sum(2, 3, 4) << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Sum: 9
```

### Common Mistakes
- Respect block scope.
- Write fold expressions that match the parameter pack.
- Constrain or document mixed argument types.

### Activities
1. Trace the scope and variadic arguments example and predict its output before compiling.
2. Adapt the example to reusable score and inventory functions and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain scope and variadic arguments using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for reusable score and inventory functions without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

# Unit 7: Object-Oriented Programming

## Overview

This unit covers types/classes, instances, fields, methods, inheritance or interfaces, composition. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 7.1: Types and object models

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Types and object models is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: distinguish a type declaration from an instance; understand struct-public and class-private defaults; initialize fields.

### Worked Example
```cpp
struct Item { std::string name; int quantity; }; const Item notebook{"Notebook", 3}; std::cout << notebook.name << ": " << notebook.quantity << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Notebook: 3
```

### Common Mistakes
- Distinguish a type declaration from an instance.
- Understand struct-public and class-private defaults.
- Initialize fields.

### Activities
1. Trace the types and object models example and predict its output before compiling.
2. Adapt the example to student records and object models and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 7.2: Creating instances

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Creating instances is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: initialize objects to satisfy invariants; use . for objects and -> for pointers; account for vector reference invalidation.

### Worked Example
```cpp
struct Item { std::string name; int quantity; }; const std::vector<Item> items{{"Notebook", 3}, {"Pencil", 10}, {"Folder", 4}}; for (const auto& item : items) std::cout << item.name << ": " << item.quantity << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Notebook: 3
Pencil: 10
Folder: 4
```

### Common Mistakes
- Initialize objects to satisfy invariants.
- Use . for objects and -> for pointers.
- Account for vector reference invalidation.

### Activities
1. Trace the creating instances example and predict its output before compiling.
2. Adapt the example to student records and object models and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 7.3: Fields and methods

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Fields and methods is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: distinguish member and local state; mark read-only methods const; understand the implicit object context.

### Worked Example
```cpp
struct Counter { int value{0}; void increment() { ++value; } int current() const { return value; } }; Counter clicks; clicks.increment(); clicks.increment(); std::cout << "Clicks: " << clicks.current() << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Clicks: 2
```

### Common Mistakes
- Distinguish member and local state.
- Mark read-only methods const.
- Understand the implicit object context.

### Activities
1. Trace the fields and methods example and predict its output before compiling.
2. Adapt the example to student records and object models and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 7.4: Inheritance and interfaces

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Inheritance and interfaces is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: give polymorphic bases virtual destructors; match override signatures; avoid object slicing.

### Worked Example
```cpp
struct Record { virtual ~Record() = default; virtual std::string kind() const { return "record"; } }; struct StudentRecord : Record { std::string kind() const override { return "student"; } }; StudentRecord student; const Record& view = student; std::cout << view.kind() << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
student
```

### Common Mistakes
- Give polymorphic bases virtual destructors.
- Match override signatures.
- Avoid object slicing.

### Activities
1. Trace the inheritance and interfaces example and predict its output before compiling.
2. Adapt the example to student records and object models and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 7.5: Composition

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Composition is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: model has-a relationships with composition; initialize members deliberately; avoid shared-ownership cycles.

### Worked Example
```cpp
struct Address { std::string city; }; struct Student { std::string name; Address address; }; const Student avery{"Avery", {"Farmington"}}; std::cout << avery.name << " lives in " << avery.address.city << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Avery lives in Farmington
```

### Common Mistakes
- Model has-a relationships with composition.
- Initialize members deliberately.
- Avoid shared-ownership cycles.

### Activities
1. Trace the composition example and predict its output before compiling.
2. Adapt the example to student records and object models and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain composition using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for student records and object models without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

# Unit 8: Files and Exceptions

## Overview

This unit covers read/write text, resource lifetime, error handling, JSON serialization and persistence. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 8.1: Reading text files

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Reading text files is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: check file-open state; remember getline removes the delimiter; resolve relative paths from the process working directory.

### Worked Example
```cpp
{ std::ofstream out("cpp_notes.txt"); out << "First line\nSecond line\n"; } std::ifstream in("cpp_notes.txt"); std::string line; while (std::getline(in, line)) std::cout << line << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
First line
Second line
```

### Common Mistakes
- Check file-open state.
- Remember getline removes the delimiter.
- Resolve relative paths from the process working directory.

### Activities
1. Trace the reading text files example and predict its output before compiling.
2. Adapt the example to notes files and personal-data persistence and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 8.2: Writing and appending files

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Writing and appending files is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: choose truncation or append mode deliberately; flush/close before dependent reads; check write state.

### Worked Example
```cpp
{ std::ofstream out("cpp_log.txt", std::ios::app); out << "Session complete\n"; } std::cout << "Appended one record\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Appended one record
```

### Common Mistakes
- Choose truncation or append mode deliberately.
- Flush/close before dependent reads.
- Check write state.

### Activities
1. Trace the writing and appending files example and predict its output before compiling.
2. Adapt the example to notes files and personal-data persistence and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 8.3: Errors and exceptions

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Errors and exceptions is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: catch standard exceptions by const reference; handle expected input errors directly; avoid uncaught exceptions.

### Worked Example
```cpp
try { throw std::runtime_error("invalid score"); } catch (const std::exception& error) { std::cout << "Handled: " << error.what() << '\n'; }

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Handled: invalid score
```

### Common Mistakes
- Catch standard exceptions by const reference.
- Handle expected input errors directly.
- Avoid uncaught exceptions.

### Activities
1. Trace the errors and exceptions example and predict its output before compiling.
2. Adapt the example to notes files and personal-data persistence and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 8.4: Resource cleanup

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Resource cleanup is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: prefer RAII to manual cleanup; check stream state after writes; do not copy unique resource owners.

### Worked Example
```cpp
{ std::ofstream output("cpp_raii.txt"); output << "The stream closes automatically at scope exit\n"; } std::cout << "RAII released the file stream\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
RAII released the file stream
```

### Common Mistakes
- Prefer RAII to manual cleanup.
- Check stream state after writes.
- Do not copy unique resource owners.

### Activities
1. Trace the resource cleanup example and predict its output before compiling.
2. Adapt the example to notes files and personal-data persistence and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 8.5: JSON persistence

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
JSON persistence is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: distinguish JSON serialization from parsing; escape special characters; use a documented JSON library for general data.

### Worked Example
```cpp
const std::string json = "{\"name\":\"Avery\",\"score\":92}"; std::cout << json << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
{"name":"Avery","score":92}
```

### Common Mistakes
- Distinguish JSON serialization from parsing.
- Escape special characters.
- Use a documented JSON library for general data.

### Activities
1. Trace the json persistence example and predict its output before compiling.
2. Adapt the example to notes files and personal-data persistence and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain json persistence using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for notes files and personal-data persistence without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

# Unit 9: Testing and Data Analysis

## Overview

This unit covers unit tests, testing stateful types, randomness, text analysis, CSV processing. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 9.1: Testing functions

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Testing functions is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: do not rely solely on assert in release builds; test independent expected results; include boundary and invalid inputs.

### Worked Example
```cpp
const auto add = [](int a, int b) { return a + b; }; assert(add(2, 3) == 5); assert(add(-2, 2) == 0); std::cout << "Function tests passed\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Function tests passed
```

### Common Mistakes
- Do not rely solely on assert in release builds.
- Test independent expected results.
- Include boundary and invalid inputs.

### Activities
1. Trace the testing functions example and predict its output before compiling.
2. Adapt the example to unit tests, random values, and text analysis and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 9.2: Testing stateful objects

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Testing stateful objects is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: assert state after each operation; isolate setup between tests; avoid order-dependent shared state.

### Worked Example
```cpp
struct Inventory { int quantity{0}; void add(int amount) { if (amount > 0) quantity += amount; } }; Inventory stock; stock.add(3); stock.add(-1); assert(stock.quantity == 3); std::cout << "State test passed\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
State test passed
```

### Common Mistakes
- Assert state after each operation.
- Isolate setup between tests.
- Avoid order-dependent shared state.

### Activities
1. Trace the testing stateful objects example and predict its output before compiling.
2. Adapt the example to unit tests, random values, and text analysis and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 9.3: Random values

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Random values is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: seed engines for reproducibility; use standard distributions rather than modulo; do not promise identical sequences across libraries.

### Worked Example
```cpp
std::mt19937 engine(42); std::uniform_int_distribution<int> die(1, 6); for (int i = 0; i < 5; ++i) std::cout << die(engine) << (i == 4 ? '\n' : ' ');

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
3 5 6 2 5
```

### Common Mistakes
- Seed engines for reproducibility.
- Use standard distributions rather than modulo.
- Do not promise identical sequences across libraries.

### Activities
1. Trace the random values example and predict its output before compiling.
2. Adapt the example to unit tests, random values, and text analysis and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 9.4: Text analysis

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text analysis is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: pass unsigned char to cctype; distinguish bytes from Unicode characters; document locale assumptions.

### Worked Example
```cpp
const std::string sample = "A student studies programming. Programming develops problem-solving skills."; int letters = 0, spaces = 0; for (unsigned char ch : sample) { if (std::isalpha(ch)) ++letters; if (std::isspace(ch)) ++spaces; } std::cout << "Letters: " << letters << "; spaces: " << spaces << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Letters: 65; spaces: 7
```

### Common Mistakes
- Pass unsigned char to cctype.
- Distinguish bytes from Unicode characters.
- Document locale assumptions.

### Activities
1. Trace the text analysis example and predict its output before compiling.
2. Adapt the example to unit tests, random values, and text analysis and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 9.5: CSV records

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
CSV records is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: a comma split is not a complete quoted-CSV parser; validate field count; ensure stoi consumed the whole field.

### Worked Example
```cpp
std::istringstream row("001,Avery,Student,92,true"); std::string id, first_name, last_name, score_text, active; std::getline(row, id, ','); std::getline(row, first_name, ','); std::getline(row, last_name, ','); std::getline(row, score_text, ','); std::getline(row, active); const int score = std::stoi(score_text); std::cout << id << ": " << first_name << " " << last_name << ", score " << score << ", active " << active << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
001: Avery Student, score 92, active true
```

### Common Mistakes
- A comma split is not a complete quoted-CSV parser.
- Validate field count.
- Ensure stoi consumed the whole field.

### Activities
1. Trace the csv records example and predict its output before compiling.
2. Adapt the example to unit tests, random values, and text analysis and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain csv records using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for unit tests, random values, and text analysis without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

# Unit 10: Project-Based Learning

## Overview

This unit covers requirements, top-down design, text adventure, command-line to-do manager, accessible validation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 10.1: Requirements and design

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Requirements and design is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: write observable acceptance criteria before implementation; include failure and empty-data scenarios; keep scope deliverable.

### Worked Example
```cpp
const std::vector<std::string> requirements{"create records", "search by ID", "validate input", "save changes"}; for (std::size_t i = 0; i < requirements.size(); ++i) std::cout << i + 1 << ". " << requirements[i] << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
1. create records
2. search by ID
3. validate input
4. save changes
```

### Common Mistakes
- Write observable acceptance criteria before implementation.
- Include failure and empty-data scenarios.
- Keep scope deliverable.

### Activities
1. Trace the requirements and design example and predict its output before compiling.
2. Adapt the example to text adventure and command-line to-do projects and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text adventure: rooms and movement is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: validate a direction before changing rooms; use consistent room identifiers; handle unknown exits.

### Worked Example
```cpp
const std::map<std::string, std::string> exits{{"north", "Library"}, {"east", "Garden"}}; std::string room = "Atrium"; const std::string direction = "north"; if (exits.contains(direction)) room = exits.at(direction); std::cout << "Current room: " << room << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Current room: Library
```

### Common Mistakes
- Validate a direction before changing rooms.
- Use consistent room identifiers.
- Handle unknown exits.

### Activities
1. Trace the text adventure: rooms and movement example and predict its output before compiling.
2. Adapt the example to text adventure and command-line to-do projects and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text adventure: inventory and puzzles is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: verify item ownership before puzzle actions; avoid erasing during unsafe traversal; test missing-item and repeated-use cases.

### Worked Example
```cpp
std::vector<std::string> inventory{"key", "map"}; const bool has_key = std::find(inventory.begin(), inventory.end(), "key") != inventory.end(); if (has_key) inventory.push_back("chest reward"); for (const auto& item : inventory) std::cout << item << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
key
map
chest reward
```

### Common Mistakes
- Verify item ownership before puzzle actions.
- Avoid erasing during unsafe traversal.
- Test missing-item and repeated-use cases.

### Activities
1. Trace the text adventure: inventory and puzzles example and predict its output before compiling.
2. Adapt the example to text adventure and command-line to-do projects and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 10.4: Command-line to-do manager

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Command-line to-do manager is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: use stable task IDs rather than vector positions; store completion separately; persist changes deliberately.

### Worked Example
```cpp
struct Task { int id; std::string title; std::string description; bool done; std::string created_at; }; std::vector<Task> tasks{{1, "Read lesson", "Review the C++ lesson", false, "2026-11-01"}}; tasks.at(0).done = true; for (const auto& task : tasks) std::cout << task.id << ": " << task.title << " [" << task.done << "] " << task.created_at << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
1: Read lesson [1] 2026-11-01
```

### Common Mistakes
- Use stable task IDs rather than vector positions.
- Store completion separately.
- Persist changes deliberately.

### Activities
1. Trace the command-line to-do manager example and predict its output before compiling.
2. Adapt the example to text adventure and command-line to-do projects and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 10.5: Accessible UX and validation

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Accessible UX and validation is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: validate each parsed argument; make errors identify the rejected field; keep prompts and status output predictable.

### Worked Example
```cpp
std::istringstream command("add Read chapter"); std::string action; command >> action; std::string title; std::getline(command >> std::ws, title); if (action == "add" && !title.empty()) std::cout << "Added task: " << title << '\n'; else std::cout << "Usage: add <task title>\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Added task: Read chapter
```

### Common Mistakes
- Validate each parsed argument.
- Make errors identify the rejected field.
- Keep prompts and status output predictable.

### Activities
1. Trace the accessible ux and validation example and predict its output before compiling.
2. Adapt the example to text adventure and command-line to-do projects and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain accessible ux and validation using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for text adventure and command-line to-do projects without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

# Unit 11: Capstone

## Overview

This unit covers accessible personal-data manager, model, persistence, CRUD, tests, documentation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 11.1: Capstone requirements

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Capstone requirements is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: set measurable acceptance criteria; constrain scope; include accessibility and data portability requirements.

### Worked Example
```cpp
std::cout << "Personal data manager requirements: create, list, search, update, delete, validate, persist.\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Personal data manager requirements: create, list, search, update, delete, validate, persist.
```

### Common Mistakes
- Set measurable acceptance criteria.
- Constrain scope.
- Include accessibility and data portability requirements.

### Activities
1. Trace the capstone requirements example and predict its output before compiling.
2. Adapt the example to personal records with stable IDs and CRUD operations and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 11.2: Data model and storage

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Data model and storage is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: use stable IDs rather than vector offsets; document the persisted schema; minimize sensitive sample data.

### Worked Example
```cpp
struct Record { int id; std::string title; std::string description; std::string category; std::string created_at; std::string updated_at; }; const std::vector<Record> records{{1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01"}}; for (const auto& record : records) std::cout << record.id << "," << record.title << "," << record.description << "," << record.category << "," << record.created_at << "," << record.updated_at << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
1,Course project,Personal data manager,education,2026-11-01,2026-11-01
```

### Common Mistakes
- Use stable IDs rather than vector offsets.
- Document the persisted schema.
- Minimize sensitive sample data.

### Activities
1. Trace the data model and storage example and predict its output before compiling.
2. Adapt the example to personal records with stable IDs and CRUD operations and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 11.3: Create/read/update/delete

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Create/read/update/delete is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: locate records by ID; distinguish not-found from success; validate replacement fields before mutating state.

### Worked Example
```cpp
struct Record { int id; std::string title; std::string description; std::string category; std::string created_at; std::string updated_at; }; std::vector<Record> records{{1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01"}}; records.push_back({2, "Study C++", "Complete functions unit", "learning", "2026-11-01", "2026-11-01"}); auto found = std::find_if(records.begin(), records.end(), [](const Record& record) { return record.id == 1; }); if (found != records.end()) found->title = "Updated course project"; records.erase(std::remove_if(records.begin(), records.end(), [](const Record& record) { return record.id == 2; }), records.end()); for (const auto& record : records) std::cout << record.id << ": " << record.title << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
1: Updated course project
```

### Common Mistakes
- Locate records by ID.
- Distinguish not-found from success.
- Validate replacement fields before mutating state.

### Activities
1. Trace the create/read/update/delete example and predict its output before compiling.
2. Adapt the example to personal records with stable IDs and CRUD operations and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 11.4: Validation and testing

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Validation and testing is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: test duplicate IDs and missing records; use temporary test files; make tests independent of execution order.

### Worked Example
```cpp
const auto valid_email = [](const std::string& email) { const auto at = email.find('@'); return at != std::string::npos && at > 0 && email.find('.', at) != std::string::npos; }; assert(valid_email("avery@example.test")); assert(!valid_email("invalid")); std::cout << "Validation tests passed\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Validation tests passed
```

### Common Mistakes
- Test duplicate IDs and missing records.
- Use temporary test files.
- Make tests independent of execution order.

### Activities
1. Trace the validation and testing example and predict its output before compiling.
2. Adapt the example to personal records with stable IDs and CRUD operations and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 11.5: Documentation and presentation

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Documentation and presentation is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: document exact build and run commands; state actual serialization support accurately; disclose limitations and accessibility coverage.

### Worked Example
```cpp
std::cout << "Build: c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror main.cpp -o app\n"; std::cout << "Document: requirements, data format, tests, limitations, accessibility\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Build: c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror main.cpp -o app
Document: requirements, data format, tests, limitations, accessibility
```

### Common Mistakes
- Document exact build and run commands.
- State actual serialization support accurately.
- Disclose limitations and accessibility coverage.

### Activities
1. Trace the documentation and presentation example and predict its output before compiling.
2. Adapt the example to personal records with stable IDs and CRUD operations and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain documentation and presentation using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for personal records with stable IDs and CRUD operations without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

## Course-Wide Assessment and Portfolio

Submit runnable exercises, prediction notes, debugging notes, tests, and the text adventure and personal-data manager projects. Assessment focuses on correctness, idiomatic C++, code explanation, independent debugging, and accessible interaction—not speed or visual editor use.

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.

## Further Learning

Use the official C++ language specification, standard-library documentation, and the linked setup resources. Verify APIs against the documentation for the installed toolchain.