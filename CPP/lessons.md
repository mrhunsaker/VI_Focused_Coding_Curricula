# C++: Complete Curriculum — Units 0–11

## Course Overview

C++ is used in game engines, simulation, robotics, finance, desktop software, and performance-critical systems.

This course intentionally parallels the original Python curriculum. It reuses problem contexts—greetings, profiles, a calculator, grade decisions, score collections, inventory, functions, text files, tests, text analysis, CSV, a to-do list, and a personal-data manager—so the principal new learning target is the C++ language. The syntax and implementation remain idiomatic, not a mechanical translation.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install and verify the compiler or interpreter, create a project, and test keyboard and screen-reader access.

### Lesson 0.1: Install and Verify C++

Install a C++20 compiler (GCC, Clang, or MSVC). Verify `c++ --version` (or the platform equivalent), then compile with `c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror -g main.cpp -o main` and run the executable. Use the same compiler and language standard in the editor and terminal.

### Lesson 0.2: Workspace and First Run
Create a course folder, save a source file named `main.cpp`, run it from the terminal, and read standard output and errors. Distinguish source code, compiler/interpreter, and executable/runtime.

### Lesson 0.3: Editor and Accessibility Workflow
Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md). Test editor navigation, punctuation announcement, indentation, terminal focus, diagnostics, and project navigation. Install only the language tooling needed for this course.

### Skills Checklist
- [ ] I can verify the selected C++20 compiler and record its version.
- [ ] I can compile, link, and run a complete source file from the terminal.
- [ ] I can distinguish compiler diagnostics from runtime output.
- [ ] I can navigate source, build output, and terminal errors using my access technology.

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

### Overview
Organize source, headers, build output, and third-party dependencies. Use the terminal from the project root and make build commands reproducible.

### Learning Objectives
- Explain the working directory and the role of source, header, object, and executable files.
- Compile a multi-file project and identify compile and link stages.
- Document compiler flags, external libraries, and build steps.

### Worked Example
```sh
c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror -g main.cpp -o app
./app
```

### Common Mistakes
- Running a relative path from the wrong working directory.
- Treating a missing header as a linker error; header lookup occurs during preprocessing/compilation.
- Omitting a required translation unit or library from the link command.

### Activities
1. Compile a one-file program from the project root and record the exact command.
2. Run the same command from another directory and explain any path failure.
3. Split a program into a header, implementation file, and `main.cpp`; compile and link all translation units.
4. Record compiler version, standard flag, dependencies, and build steps in a README.

### Accessibility Practice
Navigate each project file and terminal diagnostic by keyboard. Confirm that build errors are understandable without color or mouse-only controls.

Use the terminal from the project root and understand the current working directory. Keep each project in its own folder and distinguish source files, build output, and dependency metadata. Use one folder per C++ project and keep source, headers, and build output organized. For larger projects, introduce CMake and an out-of-source build directory. Explain compiler flags and linking when libraries are added.

### Skills Checklist
- [ ] I can identify the project root and run commands from it.
- [ ] I can explain where project dependencies are recorded, if applicable.
- [ ] I can run the program or test command from the terminal and read its output.

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
#include <iostream>
int main() { std::cout << "Hello, World!\n"; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Common Mistakes
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
#include <iostream>
int main() { std::cout << "Hello, World!\n"; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Common Mistakes
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
#include <iostream>
int main() { std::cout << "Hello, World!\n"; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
double bill = 24.50, tip = bill * 0.15;
std::cout << "Tip: " << tip << "; total: " << bill + tip << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Common Mistakes
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
double bill = 24.50, tip = bill * 0.15;
std::cout << "Tip: " << tip << "; total: " << bill + tip << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
double bill = 24.50, tip = bill * 0.15;
std::cout << "Tip: " << tip << "; total: " << bill + tip << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
double bill = 24.50, tip = bill * 0.15;
std::cout << "Tip: " << tip << "; total: " << bill + tip << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int score = 82;
if (score >= 90) std::cout << "A\n"; else if (score >= 80) std::cout << "B\n"; else std::cout << "Keep practicing\n";
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int score = 82;
if (score >= 90) std::cout << "A\n"; else if (score >= 80) std::cout << "B\n"; else std::cout << "Keep practicing\n";
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int score = 82;
if (score >= 90) std::cout << "A\n"; else if (score >= 80) std::cout << "B\n"; else std::cout << "Keep practicing\n";
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int score = 82;
if (score >= 90) std::cout << "A\n"; else if (score >= 80) std::cout << "B\n"; else std::cout << "Keep practicing\n";
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int score = 82;
if (score >= 90) std::cout << "A\n"; else if (score >= 80) std::cout << "B\n"; else std::cout << "Keep practicing\n";
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <string>
struct Item { std::string name; int quantity; };
Item book{"Notebook", 3};
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <string>
struct Item { std::string name; int quantity; };
Item book{"Notebook", 3};
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <string>
struct Item { std::string name; int quantity; };
Item book{"Notebook", 3};
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <string>
struct Item { std::string name; int quantity; };
Item book{"Notebook", 3};
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <string>
struct Item { std::string name; int quantity; };
Item book{"Notebook", 3};
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int score = 82;
if (score >= 90) std::cout << "A\n"; else if (score >= 80) std::cout << "B\n"; else std::cout << "Keep practicing\n";
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int score = 82;
if (score >= 90) std::cout << "A\n"; else if (score >= 80) std::cout << "B\n"; else std::cout << "Keep practicing\n";
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int score = 82;
if (score >= 90) std::cout << "A\n"; else if (score >= 80) std::cout << "B\n"; else std::cout << "Keep practicing\n";
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int score = 82;
if (score >= 90) std::cout << "A\n"; else if (score >= 80) std::cout << "B\n"; else std::cout << "Keep practicing\n";
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int score = 82;
if (score >= 90) std::cout << "A\n"; else if (score >= 80) std::cout << "B\n"; else std::cout << "Keep practicing\n";
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int add(int a, int b) { return a + b; }
// use: int total = add(4, 5);
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int add(int a, int b) { return a + b; }
// use: int total = add(4, 5);
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int add(int a, int b) { return a + b; }
// use: int total = add(4, 5);
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int add(int a, int b) { return a + b; }
// use: int total = add(4, 5);
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
int add(int a, int b) { return a + b; }
// use: int total = add(4, 5);
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <string>
struct Item { std::string name; int quantity; };
Item book{"Notebook", 3};
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <string>
struct Item { std::string name; int quantity; };
Item book{"Notebook", 3};
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <string>
struct Item { std::string name; int quantity; };
Item book{"Notebook", 3};
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <string>
struct Item { std::string name; int quantity; };
Item book{"Notebook", 3};
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <string>
struct Item { std::string name; int quantity; };
Item book{"Notebook", 3};
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <fstream>
std::ifstream file("notes.txt"); std::string line;
while (std::getline(file, line)) std::cout << line << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <fstream>
std::ifstream file("notes.txt"); std::string line;
while (std::getline(file, line)) std::cout << line << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <fstream>
std::ifstream file("notes.txt"); std::string line;
while (std::getline(file, line)) std::cout << line << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <fstream>
std::ifstream file("notes.txt"); std::string line;
while (std::getline(file, line)) std::cout << line << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <fstream>
std::ifstream file("notes.txt"); std::string line;
while (std::getline(file, line)) std::cout << line << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <cassert>
#include <iostream>
int add(int a, int b) { return a + b; }
int main() { assert(add(2, 3) == 5); assert(add(-2, 2) == 0); std::cout << "Tests passed\n"; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <cassert>
int add(int a,int b){return a+b;}
int main(){assert(add(2,3)==5);}
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <cassert>
int add(int a,int b){return a+b;}
int main(){assert(add(2,3)==5);}
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <cassert>
int add(int a,int b){return a+b;}
int main(){assert(add(2,3)==5);}
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <cassert>
int add(int a,int b){return a+b;}
int main(){assert(add(2,3)==5);}
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <iostream>
#include <vector>
#include <string>
int main() { std::vector<std::string> requirements{"create records", "find by ID", "validate fields", "save and reload"}; for (const auto& item : requirements) std::cout << "Requirement: " << item << '\n'; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <iostream>
#include <map>
#include <string>
int main() { std::map<std::string, std::string> exits{{"north", "Library"}, {"east", "Garden"}}; std::string direction = "north", room = "Atrium"; if (exits.contains(direction)) room = exits.at(direction); std::cout << room << '\n'; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
int main() { std::vector<std::string> inventory{"key", "map"}; if (std::find(inventory.begin(), inventory.end(), "key") != inventory.end()) inventory.push_back("chest reward"); for (const auto& item : inventory) std::cout << item << '\n'; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
struct Task { int id; std::string title; bool done; };
int main() { std::vector<Task> tasks{{1, "Read lesson", false}}; tasks.push_back({2, "Run tests", true}); tasks.at(0).done = true; tasks.erase(std::remove_if(tasks.begin(), tasks.end(), [](const Task& task) { return task.id == 2; }), tasks.end()); for (const auto& task : tasks) std::cout << task.id << ": " << task.title << " " << task.done << '\n'; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <iostream>
#include <string>
int main() { std::cout << "Accessible interaction: numbered menu, clear prompts, explicit errors, and stable output order\\n"; std::cout << "Validation: reject blank names and malformed email fields before saving\\n"; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <iostream>
#include <vector>
#include <string>
int main() { std::vector<std::string> requirements{"create records", "find by ID", "validate fields", "save and reload"}; for (const auto& item : requirements) std::cout << "Requirement: " << item << '\n'; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <iostream>
#include <string>
#include <vector>
struct Person { int id; std::string name; std::string email; };
int main() { std::vector<Person> people{{1, "Avery", "avery@example.test"}}; for (const auto& person : people) std::cout << person.id << "," << person.name << "," << person.email << '\n'; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
struct Task { int id; std::string title; bool done; };
int main() { std::vector<Task> tasks{{1, "Read lesson", false}}; tasks.push_back({2, "Run tests", true}); tasks.at(0).done = true; tasks.erase(std::remove_if(tasks.begin(), tasks.end(), [](const Task& task) { return task.id == 2; }), tasks.end()); for (const auto& task : tasks) std::cout << task.id << ": " << task.title << " " << task.done << '\n'; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <cassert>
#include <iostream>
int add(int a, int b) { return a + b; }
int main() { assert(add(2, 3) == 5); assert(add(-2, 2) == 0); std::cout << "Tests passed\n"; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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
#include <iostream>
int main() { std::cout << "Build: c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror main.cpp -o app\n"; std::cout << "Test: create, read, update, delete, invalid input, missing file\n"; }
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

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

## AI and Academic Integrity

AI may be used only for personal conceptual explanations and reinforcement when the instructor permits. Do not use AI to write, complete, autocomplete, repair, or generate course code or assessment solutions. Students must explain every submitted statement independently.

## Further Learning

Use the official C++ language specification, standard-library documentation, and the linked setup resources. Verify APIs against the documentation for the installed toolchain.