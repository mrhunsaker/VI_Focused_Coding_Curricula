# C++ Curriculum

C++ is used in game engines, simulation, robotics, finance, desktop software, and performance-critical systems.

## Course structure

A complete introductory sequence aligned to Python Units 0–11: setup; foundations; numeric computation; control flow; data structures; input and iteration; functions; object-oriented design; files and exceptions; testing and data analysis; projects; and capstone. The same core problem contexts recur across languages so students focus on syntax, types, runtime behavior, libraries, and idioms.

## Environment

Install GCC, Clang, or MSVC with C++20 support. On GCC/Clang, compile with `c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror main.cpp -o main`; run with `./main`.

Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md) and [terminal prerequisite](../TERMINAL/TERMINAL_README.md). The course supports keyboard-first work with screen readers, braille displays, magnification, or other access technology.

- [Complete lessons](lessons.md)
- [Topic index](INDEX.md)


## Lesson example verification

The course includes 53 numbered lessons across Units 1–11 and four structured setup lessons in Unit 0. The numbered lessons have distinct worked examples, lesson-specific mistakes, four practice activities, and five mastery checks.

- [C++ example validation script](../scripts/check_cpp_examples.py)
- [GCC/Clang GitHub Actions workflow](../.github/workflows/cpp-examples.yml)
- [Validation run 41318260153](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41318260153)

GCC 13.3.0 and Clang 18.1.3 each compiled and linked all 54 fenced C++ examples in C++20 mode with `-Wall -Wextra -Wpedantic -Werror`. The checker wraps lesson fragments in a minimal program and supplies common standard-library headers where needed.

This verifies compilation and linking only. The examples have not all been executed with representative input or file fixtures. A fresh mdBook build, complete link crawl, and hands-on screen-reader/braille testing remain outstanding.
