# C Curriculum

<<<<<<< HEAD
=======
**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

>>>>>>> 2067a20 (curriculum clearning and updates)
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

## GUI, visualization, and workbench accessibility

See the shared [GUI, visualization, and workbench accessibility reference](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) for screen-reader support by toolkit, platform-specific activation settings, recommended alternatives, and interfaces that must not be required without an equivalent accessible route.
<<<<<<< HEAD
=======

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)

## Recommended introductory books

- King, K. N. *C Programming: A Modern Approach*, 2nd edition. W. W. Norton, 2008. A thorough first-course textbook with extensive exercises and careful explanations of C's core features. It teaches C99; use the course's C17 notes and current compiler documentation for later-standard differences.
- Perry, Greg, and Dean Miller. *C Programming Absolute Beginner's Guide*, 3rd edition. Que Publishing, 2014. A task-oriented introduction covering program structure, expressions, functions, arrays, pointers, and input/output. It targets C11. [Publisher page](https://www.pearson.com/en-us/subject-catalog/p/c-programming-absolute-beginner-s-guide/P200000000531/9780789751980).
- Downey, Allen B. *Think C*. Green Tea Press. A free, concise introduction to computational problem solving using C. [Book resources](https://greenteapress.com/wp/think-c/).

**Suggested use:** King's text is a strong full textbook companion; Perry and Miller provide a more task-oriented alternative. C has evolved since these books were published, so follow the course's C17 baseline and consult current compiler and language references for standard-specific details.
