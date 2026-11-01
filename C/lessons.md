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
Computer science and problem solving. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
#include <stdio.h>
int main(void) { printf("Hello, World!\n"); return 0; }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Your first program. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
#include <stdio.h>
int main(void) { printf("Hello, World!\n"); return 0; }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Variables and data types. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
#include <stdio.h>
int main(void) { printf("Hello, World!\n"); return 0; }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Design and tracing. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
double bill = 24.50; double tip = bill * 0.15;
printf("Tip: %.2f; total: %.2f\n", tip, bill + tip);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Expressions and assignment. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
double bill = 24.50; double tip = bill * 0.15;
printf("Tip: %.2f; total: %.2f\n", tip, bill + tip);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Input and output. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
double bill = 24.50; double tip = bill * 0.15;
printf("Tip: %.2f; total: %.2f\n", tip, bill + tip);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Numeric conversions and mathematics. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
double bill = 24.50; double tip = bill * 0.15;
printf("Tip: %.2f; total: %.2f\n", tip, bill + tip);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Boolean expressions. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int score = 82;
if (score >= 90) puts("A"); else if (score >= 80) puts("B"); else puts("Keep practicing");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Chained conditionals. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int score = 82;
if (score >= 90) puts("A"); else if (score >= 80) puts("B"); else puts("Keep practicing");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Sequences and indexing. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int score = 82;
if (score >= 90) puts("A"); else if (score >= 80) puts("B"); else puts("Keep practicing");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
For loops and iteration. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int score = 82;
if (score >= 90) puts("A"); else if (score >= 80) puts("B"); else puts("Keep practicing");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
String operations. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int score = 82;
if (score >= 90) puts("A"); else if (score >= 80) puts("B"); else puts("Keep practicing");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Mutable sequences. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
struct Item { char name[40]; int quantity; };
struct Item book = {"Notebook", 3}; printf("%s: %d\n", book.name, book.quantity);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Sorting and organizing data. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
struct Item { char name[40]; int quantity; };
struct Item book = {"Notebook", 3}; printf("%s: %d\n", book.name, book.quantity);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Immutable records. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
struct Item { char name[40]; int quantity; };
struct Item book = {"Notebook", 3}; printf("%s: %d\n", book.name, book.quantity);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Maps and key-value data. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
struct Item { char name[40]; int quantity; };
struct Item book = {"Notebook", 3}; printf("%s: %d\n", book.name, book.quantity);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Collection traversal. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
struct Item { char name[40]; int quantity; };
struct Item book = {"Notebook", 3}; printf("%s: %d\n", book.name, book.quantity);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Input and validation. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int score = 82;
if (score >= 90) puts("A"); else if (score >= 80) puts("B"); else puts("Keep practicing");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
While loops. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int score = 82;
if (score >= 90) puts("A"); else if (score >= 80) puts("B"); else puts("Keep practicing");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Flags and break. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int score = 82;
if (score >= 90) puts("A"); else if (score >= 80) puts("B"); else puts("Keep practicing");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Continue and filtering. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int score = 82;
if (score >= 90) puts("A"); else if (score >= 80) puts("B"); else puts("Keep practicing");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Infinite-loop prevention. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int score = 82;
if (score >= 90) puts("A"); else if (score >= 80) puts("B"); else puts("Keep practicing");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Defining functions. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int add(int a, int b) { return a + b; }
/* use: int total = add(4, 5); */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Parameters and arguments. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int add(int a, int b) { return a + b; }
/* use: int total = add(4, 5); */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Return values. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int add(int a, int b) { return a + b; }
/* use: int total = add(4, 5); */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Functions over collections. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int add(int a, int b) { return a + b; }
/* use: int total = add(4, 5); */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Scope and variadic arguments. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
int add(int a, int b) { return a + b; }
/* use: int total = add(4, 5); */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Types and object models. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
struct Item { char name[40]; int quantity; };
struct Item book = {"Notebook", 3}; printf("%s: %d\n", book.name, book.quantity);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Creating instances. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
struct Item { char name[40]; int quantity; };
struct Item book = {"Notebook", 3}; printf("%s: %d\n", book.name, book.quantity);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Fields and methods. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
struct Item { char name[40]; int quantity; };
struct Item book = {"Notebook", 3}; printf("%s: %d\n", book.name, book.quantity);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Inheritance and interfaces. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
struct Item { char name[40]; int quantity; };
struct Item book = {"Notebook", 3}; printf("%s: %d\n", book.name, book.quantity);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Composition. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
struct Item { char name[40]; int quantity; };
struct Item book = {"Notebook", 3}; printf("%s: %d\n", book.name, book.quantity);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Reading text files. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
FILE *file = fopen("notes.txt", "r");
if (file == NULL) { perror("notes.txt"); return 1; }
char line[256]; while (fgets(line, sizeof line, file)) fputs(line, stdout);
fclose(file);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Writing and appending files. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
FILE *file = fopen("notes.txt", "r");
if (file == NULL) { perror("notes.txt"); return 1; }
char line[256]; while (fgets(line, sizeof line, file)) fputs(line, stdout);
fclose(file);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Errors and exceptions. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
FILE *file = fopen("notes.txt", "r");
if (file == NULL) { perror("notes.txt"); return 1; }
char line[256]; while (fgets(line, sizeof line, file)) fputs(line, stdout);
fclose(file);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Resource cleanup. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
FILE *file = fopen("notes.txt", "r");
if (file == NULL) { perror("notes.txt"); return 1; }
char line[256]; while (fgets(line, sizeof line, file)) fputs(line, stdout);
fclose(file);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
JSON persistence. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
FILE *file = fopen("notes.txt", "r");
if (file == NULL) { perror("notes.txt"); return 1; }
char line[256]; while (fgets(line, sizeof line, file)) fputs(line, stdout);
fclose(file);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Testing functions. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
#include <assert.h>
int add(int a, int b) { return a + b; }
int main(void) { assert(add(2, 3) == 5); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Testing stateful objects. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
#include <assert.h>
int add(int a, int b) { return a + b; }
int main(void) { assert(add(2, 3) == 5); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Random values. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
#include <assert.h>
int add(int a, int b) { return a + b; }
int main(void) { assert(add(2, 3) == 5); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Text analysis. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
#include <assert.h>
int add(int a, int b) { return a + b; }
int main(void) { assert(add(2, 3) == 5); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
CSV records. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
#include <assert.h>
int add(int a, int b) { return a + b; }
int main(void) { assert(add(2, 3) == 5); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Requirements and design. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
/* Build a menu-driven personal data manager using structs, arrays, validation, and files. */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Text adventure: rooms and movement. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
/* Build a menu-driven personal data manager using structs, arrays, validation, and files. */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Text adventure: inventory and puzzles. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
/* Build a menu-driven personal data manager using structs, arrays, validation, and files. */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Command-line to-do manager. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
/* Build a menu-driven personal data manager using structs, arrays, validation, and files. */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Accessible UX and validation. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
/* Build a menu-driven personal data manager using structs, arrays, validation, and files. */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Capstone requirements. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
/* Build a menu-driven personal data manager using structs, arrays, validation, and files. */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Data model and storage. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
/* Build a menu-driven personal data manager using structs, arrays, validation, and files. */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Create/read/update/delete. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
/* Build a menu-driven personal data manager using structs, arrays, validation, and files. */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Validation and testing. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
/* Build a menu-driven personal data manager using structs, arrays, validation, and files. */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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
Documentation and presentation. C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic C syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```c
/* Build a menu-driven personal data manager using structs, arrays, validation, and files. */
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

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