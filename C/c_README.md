# Introduction to C

## Standalone beginner curriculum

C is a procedural, statically typed, compiled language. It is widely used for operating systems, embedded firmware, device drivers, networking stacks, language runtimes, and performance-sensitive libraries.

## What information is a good fit?

C is appropriate when software must work directly with bytes, fixed-width integers, memory buffers, binary records, or data structures whose layout and lifetime must be controlled. Programmers must validate sizes and manage memory carefully; C does not provide automatic bounds checking or garbage collection.

## Lessons

1. Compiler, source files, and translation units.
2. Types, expressions, and formatted input/output.
3. Conditions and loops.
4. Functions, headers, and separate compilation.
5. Arrays, strings, and pointer fundamentals.
6. Structs, enums, and data modeling.
7. Dynamic memory and ownership discipline.
8. Files, error codes, and defensive input.
9. Debugging, sanitizers, and unit tests.
10. Systems-oriented capstone.

## First program

~~~c
#include <stdio.h>
int main(void) {
    int count = 3;
    printf("Count: %d\n", count);
    return 0;
}
~~~

Toolchain: GCC or Clang. Compile with warnings enabled and a declared language standard. This course follows keyboard-first, text-based practice; read compiler diagnostics carefully and test boundary conditions.

See [C lessons](lessons.md) and [topic index](INDEX.md).
