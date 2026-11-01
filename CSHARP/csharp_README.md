# C# Curriculum

C# is a modern managed language for .NET services, web apps, desktop software, cloud systems, and Unity games.

## Course structure

A complete introductory sequence aligned to Python Units 0–11: setup; foundations; numeric computation; control flow; data structures; input and iteration; functions; object-oriented design; files and exceptions; testing and data analysis; projects; and capstone. The same core problem contexts recur across languages so students focus on syntax, types, runtime behavior, libraries, and idioms.

## Environment

Install the .NET 10 SDK (C# 14 toolchain); create with `dotnet new console`; run with `dotnet run`.

Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md) and [terminal prerequisite](../TERMINAL/TERMINAL_README.md). The course supports keyboard-first work with screen readers, braille displays, magnification, or other access technology.

- [Complete lessons](lessons.md)
- [Topic index](INDEX.md)


## Lesson structure and example verification

The complete course has four structured Unit 0 setup lessons and 53 numbered lessons across Units 1–11. The numbered lessons use the shared Python course datasets and problem contexts, with C#-specific language features and .NET APIs. Each numbered lesson includes three targeted common mistakes, four practice activities, and five mastery criteria.

- [C# lesson example validation script](../scripts/check_csharp_examples.py)
- [GitHub Actions .NET 10 / C# 14 workflow](../.github/workflows/csharp-examples.yml)

The automated check builds and executes every fenced C# example as a separate .NET 10 console program with nullable analysis enabled and compiler warnings treated as errors. [GitHub Actions run 41320247156](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41320247156) passed with .NET SDK 10.0.403; all 53 examples compiled, linked, and exited successfully. This is a smoke-execution check, not full behavioral validation: expected-output assertions, broader invalid-input/file fixtures, and the complete capstone application still require testing. Hands-on accessibility validation remains separate.
