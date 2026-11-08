# Kotlin: Complete Standalone Lessons

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

This reference introduces Kotlin/JVM and complements the standardized 57-lesson sequence.

## Kotlin and Java

Kotlin and Java compile to JVM bytecode and can use the same Java class libraries. Kotlin files can call Java classes and Java code can call Kotlin declarations. This supports gradual migration rather than requiring a complete rewrite.

| Concept | Java | Kotlin |
| --- | --- | --- |
| Variable | `int count = 3;` | `val count: Int = 3` |
| Reassignment | `count = 4;` | Declare with `var`; `val` cannot be reassigned |
| Nullability | Reference may be null | Nullable type uses `?` |
| String interpolation | Concatenation/formatting | `"Hello, $name"` |
| Data holder | Class or record | `data class` |
| Conditional | `if` / `switch` | `if` / `when` expressions |
| Function placement | Usually class members | Top-level functions are supported |

## Toolchain and first program

Install a supported JDK and Kotlin compiler. Verify `java -version` and `kotlinc -version`. Save as `Hello.kt`:

```kotlin
fun main() {
    println("Hello, Kotlin!")
}
```

Compile and run:

```bash
kotlinc Hello.kt -include-runtime -d hello.jar
java -jar hello.jar
```

For projects, use the Gradle wrapper and Kotlin/JVM plugin. See the [official Kotlin documentation](https://kotlinlang.org/docs/).

## Variables, types, and null safety

```kotlin
val studentName: String = "Avery"
val completedLessons = 4
var score: Int = 85
score = 92
var optionalName: String? = null
val displayName = optionalName ?: "Guest"
println("$studentName completed $completedLessons lessons; score=$score; name=$displayName")
```

Kotlin is statically typed even when a declaration's type is inferred. Nullable types use `?`. Safe calls (`?.`) avoid dereferencing null; the Elvis operator (`?:`) supplies a fallback. The not-null assertion (`!!`) can throw and should not replace validation. Java platform types and external data still require defensive checks.

## Functions, control flow, and collections

```kotlin
fun letterGrade(score: Int): String = when {
    score >= 90 -> "A"
    score >= 80 -> "B"
    score >= 70 -> "C"
    score >= 60 -> "D"
    else -> "F"
}

fun main() {
    val scores = listOf(82, 91, 76, 88)
    println(scores.average())
    println(scores.map(::letterGrade))
}
```

Use `List` and `Map` for read-only access and mutable collection interfaces only when mutation is required. A read-only interface does not guarantee deep immutability. Kotlin uses `vararg` for variable argument counts and supports lambdas and standard collection operations.

## Classes and JVM interoperability

```kotlin
data class CourseResult(val studentName: String, val courseName: String, val score: Int)

class Student(val name: String, var score: Int) {
    fun isPassing(): Boolean = score >= 60
}
```

Kotlin classes are final by default. Use `open` when inheritance is intentional; consider interfaces and composition. Java APIs are available directly, but platform types, Java generic signatures, and runtime exceptions require attention.

## Files, JSON, CSV, and testing

Use `java.nio.file.Files` and `Path` for JVM file access. Use `use` for resource cleanup. Use maintained serialization and CSV libraries rather than hand-written parsers for general JSON/CSV. Test deterministic behavior with Kotlin test/JUnit and include boundary, malformed-input, missing-file, and persistence cases.

## Accessibility

Teach symbol names explicitly, use keyboard-first navigation, and verify the language server, build output, and diagnostics with the learner's screen reader. Expand dense expressions into named values where useful. The course's text-first application workflow avoids making visual GUI inspection a prerequisite.

## Full aligned sequence

See [Unit 0–1](unit00-01-setup-foundations.md), [Unit 2–4](unit02-04-io-control-data.md), [Unit 5–8](unit05-08-strings-functions-oop-files.md), [Unit 9–11](unit09-11-collections-projects.md), and the [topic index](INDEX.md).
