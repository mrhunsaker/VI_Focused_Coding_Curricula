# C Curriculum

C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs.

## Course structure

A complete introductory sequence aligned to Python Units 0–11: setup; foundations; numeric computation; control flow; data structures; input and iteration; functions; object-oriented design; files and exceptions; testing and data analysis; projects; and capstone. The same core problem contexts recur across languages so students focus on syntax, types, runtime behavior, libraries, and idioms.

## Environment

Install GCC or Clang (C17); compile with cc -std=c17 -Wall -Wextra -Wpedantic -g main.c -o main; run ./main.

Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md) and [terminal prerequisite](../TERMINAL/TERMINAL_README.md). The course supports keyboard-first work with screen readers, braille displays, magnification, or other access technology.

- [Complete lessons](lessons.md)
- [Topic index](INDEX.md)

## Shared Python-aligned examples

The C lessons reuse the canonical student profile (Avery, age 16, height 1.72 m), $24.50 bill with a 15% tip, grade boundaries, scores (82, 91, 76, 88), inventory records (Notebook, Pencil, Folder), coordinates (3, 4), the shared text sample, CSV field names, and the capstone record fields. C-specific adaptations are explicit: arrays and structs replace Python lists and dictionaries; error codes and return values replace exceptions; an accessible terminal interface replaces the Python-only NiceGUI implementation; and JSON persistence requires a documented external C library.

The lesson examples are written for C17 and should be compiled with warnings enabled. External-library examples must document their dependency and linker settings. No claim is made that every example has been compiled on every supported toolchain; verify examples with the compiler and platform used by the course.
