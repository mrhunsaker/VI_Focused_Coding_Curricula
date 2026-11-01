# Introduction to C++

## Standalone beginner curriculum

C++ is a compiled, statically typed, multi-paradigm language used for game engines, real-time systems, desktop software, simulation, high-performance computing, and performance-critical libraries.

## What information is a good fit?

C++ suits large structured objects, numerical arrays, resource-owning objects, event streams, and data requiring predictable performance. Modern C++ uses RAII and standard-library abstractions to manage resources safely; raw pointers and manual memory management still exist but should not be the default.

## Lessons

1. Compiler, source files, and build workflow.
2. Types, expressions, and console I/O.
3. Conditions, loops, and functions.
4. Strings, vectors, and standard containers.
5. References, pointers, and object lifetime.
6. Classes, constructors, and encapsulation.
7. RAII, smart pointers, and resource safety.
8. Templates, algorithms, and generic programming.
9. Files, exceptions, and testing.
10. Performance-aware capstone.

## First program

~~~cpp
#include <iostream>
#include <string>
int main() {
    const std::string name = "Avery";
    std::cout << "Hello, " << name << "!\n";
}
~~~

Toolchain: GCC, Clang, or MSVC. Use a modern standard such as C++20, enable warnings, and prefer standard-library types over manual resource management. See [C++ lessons](lessons.md).
