# C: Lessons and Guided Practice

## Toolchain and first run

Install GCC or Clang. Save a source file as main.c. Compile with gcc -std=c17 -Wall -Wextra -Wpedantic main.c -o app and run the resulting executable from the project directory.

## Lesson 1: Compiler and translation units

Learn source files, preprocessing, compilation, linking, headers, and the main function. Exercise: compile a one-file program and explain the compiler stages.

## Lesson 2: Types, expressions, and formatted I/O

Study integer and floating types, char, constants, operators, printf format specifiers, and scanf limitations. Prefer fgets plus checked conversion for robust text input. Exercise: calculate a mean and reject malformed input.

## Lesson 3: Conditions and loops

Use if, else, switch, for, while, and do-while. Trace branch conditions and loop termination. Exercise: process a sequence and count values meeting a condition.

## Lesson 4: Functions, headers, and separate compilation

Declare prototypes, define functions, pass arguments, return values, and split declarations from implementations. Exercise: separate validation and calculation into functions.

## Lesson 5: Arrays, strings, and pointers

Understand array bounds, null-terminated character arrays, pointer values, dereferencing, and pointer arithmetic. Exercise: process a string without reading or writing outside its bounds.

## Lesson 6: Structs, enums, and data modeling

Use struct and enum to represent records and finite states. Exercise: define a record with fields and write a function that summarizes it.

## Lesson 7: Dynamic memory

Study malloc, calloc, realloc, and free. Pair each successful allocation with a clear release path; check allocation results and avoid use-after-free, double-free, and leaks. Exercise: allocate a dynamic list and release it on every exit path.

## Lesson 8: Files and defensive input

Use fopen, fgets, fprintf, and fclose; check return values and distinguish end-of-file from errors. Exercise: read records, report malformed lines, and write a summary.

## Lesson 9: Debugging and tests

Use compiler warnings, a debugger, sanitizers, and assertions. Test empty, boundary, malformed, and maximum-size inputs. Add a regression test for each fixed defect.

## Lesson 10: Capstone

Build a text-based inventory or measurement tool with structs, dynamic memory, file input/output, validation, and tests. Document memory ownership and error handling.
