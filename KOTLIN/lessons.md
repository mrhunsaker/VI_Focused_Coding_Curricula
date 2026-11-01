# Kotlin: Lessons and Guided Practice

## Toolchain and first run

Install a stable Kotlin compiler and a supported JDK. Save the first program as Main.kt, compile with kotlinc Main.kt -include-runtime -d app.jar, and run with java -jar app.jar. For larger projects, use Gradle with the Kotlin JVM plugin and project wrapper.

## Lesson 1: Program structure

Study fun main(), statements, blocks, comments, imports, and println. Kotlin does not require a class around every top-level function. Exercise: add labeled output and explain parentheses, braces, quotes, and string interpolation.

## Lesson 2: Variables, types, and expressions

Use val for read-only bindings and var for reassignment. Learn Int, Long, Double, Boolean, Char, String, inference, operators, and explicit conversions such as toDouble(). Exercise: calculate a mean and explain integer versus floating-point division.

## Lesson 3: Null safety

Distinguish String from String?. Practice safe calls (?.), the Elvis operator (?:), and safe casts. Treat !! as a risky assertion, not a routine solution. Exercise: parse an optional field and choose a documented fallback without crashing.

## Lesson 4: Input and control flow

Read console input as text, validate it, then convert. Use if, when, for, while, ranges, and Boolean expressions. Exercise: implement a validated menu with explicit responses for unknown choices.

## Lesson 5: Functions and scope

Declare functions with fun, typed parameters, return types, default arguments, and named arguments. Explain local scope and expression-bodied functions. Exercise: separate parsing, validation, calculation, and reporting into functions.

## Lesson 6: Classes and data classes

Study primary constructors, properties, visibility, regular classes, data classes, enums, and interfaces. Kotlin classes are final by default. Exercise: represent a course result as a data class and summarize it.

## Lesson 7: Collections and lambdas

Compare read-only List, Set, and Map interfaces with mutable counterparts. Practice iteration, filtering, mapping, sorting, and lambdas. A read-only interface does not guarantee deep immutability. Exercise: group records and compute a summary.

## Lesson 8: Files, exceptions, and interoperability

Read and write text files using Kotlin/JVM APIs; handle expected exceptions and close resources safely. Java platform types may have uncertain nullability. Exercise: load a file, validate each record, and report invalid rows with line numbers.

## Lesson 9: Coroutines, testing, and debugging

Coroutines provide structured concurrency and suspension; they are not simply threads. Introduce suspend functions, coroutine scopes, cancellation, and exception propagation conceptually. Test boundaries, empty data, invalid values, and nullability.

## Lesson 10: Capstone

Build a terminal-based record-processing tool with validated input, data classes, collections, file persistence, and tests. Include a README and explain where nullability is checked and how failures are reported.
