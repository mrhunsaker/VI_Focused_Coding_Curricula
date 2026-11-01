# Introduction to C#

## Standalone beginner curriculum

C# is a statically typed, managed, object-oriented language with functional features. It is used for business applications, web APIs, cloud services, desktop software, Unity game development, and cross-platform services on .NET.

## What information is a good fit?

C# is well suited to business entities, typed application models, JSON/API payloads, database records, and event-driven application state. Nullable reference types and validation help express assumptions, but external data still needs runtime checks.

## Lessons

1. .NET SDK, project structure, and compilation.
2. Variables, types, expressions, and interpolation.
3. Console input, conversion, and validation.
4. Conditions, loops, and methods.
5. Arrays, List<T>, and dictionaries.
6. Classes, records, properties, and interfaces.
7. Exceptions, nullable reference types, and LINQ.
8. Files, JSON, and asynchronous basics.
9. Unit testing and debugging.
10. .NET application capstone.

## First program

~~~csharp
using System;
string name = "Avery";
int count = 3;
Console.WriteLine($"{name}: {count}");
~~~

Toolchain: .NET SDK and dotnet CLI. Use a supported stable SDK and project-local dependencies. See [C# lessons](lessons.md).
