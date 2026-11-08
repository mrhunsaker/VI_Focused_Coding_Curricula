# Unit 8: Files and Exceptions

## Overview

Read and write files, handle errors, release resources reliably, and store records as JSON.

---


## Lesson 8.1: Reading from a File

### Reading References
- [Kotlin standard library: kotlin.io](https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.io/)
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 8.1: Reading from a File

### Learning Objectives
- Read a whole file and read it line by line.
- Check that a file exists before reading.
- Report a missing file clearly.

### Concept Explanation

`java.io.File` represents a path. `readText()` returns the whole file as a string, `readLines()` returns a list of lines, and `forEachLine { ... }` processes one line at a time. A relative path such as `notes.txt` starts from the program's working directory, so a program run from another folder will not find it.

`File.exists()` tests whether a file is there. Reading a file that does not exist throws a `FileNotFoundException`, which Lesson 8.3 handles.

To keep the lesson self-contained, the example first writes the two-line `notes.txt` that every language track uses, then reads it three ways and checks a file that does not exist.

### Worked Example

```kotlin
import java.io.File

fun main() {
    val notes = File("notes.txt")
    notes.writeText("Practice Kotlin.\nReview lists and functions.\n")

    println(notes.readText())

    for (line in notes.readLines()) {
        println(line)
    }
    println(notes.readLines().size)

    notes.forEachLine { println(it.uppercase()) }

    val missing = File("missing_notes.txt")
    if (!missing.exists()) {
        println("missing_notes.txt was not found.")
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Practice Kotlin.
Review lists and functions.

Practice Kotlin.
Review lists and functions.
2
PRACTICE KOTLIN.
REVIEW LISTS AND FUNCTIONS.
missing_notes.txt was not found.
```

### Common Mistakes
1. Reading a file that does not exist without checking or catching the error.
2. Running from a different folder, so the relative path points to the wrong place.
3. Forgetting that `readText()` keeps the final newline, so `println` adds a blank line.

### Activities
1. Run the program and describe each block of output.
2. Add a third line to the file text and predict the new count.
3. Print each line with its line number.
4. Print a friendly message that includes the missing file's name.

### Accessibility Practice

Read the output aloud in order. Make an error message a complete sentence that includes the file name so that it is clear without seeing the screen.

### Skills Checklist
- [ ] I can read a file whole and by line.
- [ ] I can check that a file exists.
- [ ] I know relative paths use the working directory.
- [ ] I can report a missing file.
- [ ] I can write a file for the example.

---

## Lesson 8.2: Writing to a File

### Reading References
- [Kotlin standard library: kotlin.io](https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.io/)
- Matching Python lesson: Lesson 8.2: Writing to a File

### Learning Objectives
- Write with `writeText` and append with `appendText`.
- Include line endings correctly.
- Read the file back to verify it.

### Concept Explanation

`writeText(text)` creates the file or **replaces** its contents. `appendText(text)` adds to the end. Neither adds a line ending for you, so end each line with `\n`. `printWriter()` and `bufferedWriter()` write in pieces and should be closed with `use` (Lesson 8.4).

Reading the file back is the simplest way to confirm what was saved. The example writes the first notes line, appends the second, and reads the file back.

### Worked Example

```kotlin
import java.io.File

fun main() {
    val file = File("notes.txt")
    file.writeText("Practice Kotlin.\n")
    file.appendText("Review lists and functions.\n")
    print(file.readText())
    println("Lines: ${file.readLines().size}")
}
```

### Expected Behavior or Output

The program prints:
```text
Practice Kotlin.
Review lists and functions.
Lines: 2
```

### Common Mistakes
1. Using `writeText` when `appendText` was intended, which erases earlier content.
2. Forgetting `\n`, so all written lines run together.
3. Not reading the file back to check what was actually saved.

### Activities
1. Predict the output, then run.
2. Replace the second call with `writeText` and explain the difference.
3. Append a third line with the current number of lines.
4. Write the shared scores, one per line, then read them back and total them.

### Accessibility Practice

Always read a written file back in the terminal to confirm it, using line navigation, so you do not depend on assumptions about what was saved.

### Skills Checklist
- [ ] I can write and append.
- [ ] I know `writeText` replaces.
- [ ] I can include line endings.
- [ ] I can verify by reading back.
- [ ] I can count lines in a file.

---

## Lesson 8.3: Exceptions

### Reading References
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 8.3: Exceptions - Handling Errors

### Learning Objectives
- Catch specific exceptions with `try` and `catch`.
- Use `finally` and `runCatching`.
- Raise errors with `require` and `error`.

### Concept Explanation

An *exception* is an error that stops the program unless it is caught. `try { ... } catch (e: SomeException) { ... }` runs the risky code and handles the failure. Catch the **specific** exception you expect (`FileNotFoundException`, `NumberFormatException`, `ArithmeticException`), never everything, so mistakes in your own code are not hidden. A `finally` block runs whether or not an exception happened.

Kotlin has no checked exceptions: the compiler does not force you to catch anything. `runCatching { ... }` runs a block and returns a `Result` that holds either the value or the exception, and `exceptionOrNull()?.message` reads the message.

`require(condition) { message }` rejects a bad argument and `error(message)` throws an `IllegalStateException`. Integer division by zero throws an `ArithmeticException`; division of `Double` values by zero gives infinity instead.

### Worked Example

```kotlin
import java.io.File
import java.io.FileNotFoundException

fun main() {
    try {
        File("missing_notes.txt").readText()
    } catch (e: FileNotFoundException) {
        println("Error: missing_notes.txt was not found.")
    }

    try {
        "abc".toInt()
    } catch (e: NumberFormatException) {
        println("Error: 'abc' is not a valid score.")
    }

    val zero = 0
    try {
        println(10 / zero)
    } catch (e: ArithmeticException) {
        println("Error: ${e.message}")
    }
    println(10.0 / zero)

    val result = runCatching { require(false) { "custom failure" } }
    println(result.exceptionOrNull()?.message)

    try {
        error("raised by error()")
    } catch (e: IllegalStateException) {
        println(e.message)
    } finally {
        println("Cleanup runs either way.")
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score.
Error: / by zero
Infinity
custom failure
raised by error()
Cleanup runs either way.
```

### Common Mistakes
1. Catching `Exception` for everything, which hides mistakes in your own code.
2. Using `toInt()` on untrusted text without a catch or `toIntOrNull()`.
3. Expecting `10.0 / 0` to throw. It gives `Infinity`.

### Activities
1. Predict each printed line before running.
2. Wrap `readln().toInt()` so invalid input prints a clear message and asks again.
3. Catch `ArithmeticException` in a function that computes an average of an empty list.
4. Explain when to catch an exception and when to let it stop the program.

### Accessibility Practice

Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.' Read the exception's class name aloud when you see a stack trace, then jump to the first line that names your own file.

### Skills Checklist
- [ ] I can catch specific exceptions.
- [ ] I can use `finally` and `runCatching`.
- [ ] I can raise errors with `require` and `error`.
- [ ] I know integer and decimal division by zero differ.
- [ ] I can write clear error messages.

---

## Lesson 8.4: Cleanup with use and finally

### Reading References
- [Exceptions: finally](https://kotlinlang.org/docs/exceptions.html#the-finally-block)
- Matching Python lesson: Lesson 8.4: The else and finally Blocks

### Learning Objectives
- Close files reliably with `use`.
- Show that a resource is released even after an error.
- Use `finally` for cleanup.

### Concept Explanation

A file reader or writer holds a resource from the operating system, so it must be closed. The extension function `use { ... }` runs a block and then closes the resource, **even if the block throws an exception**. It is the Kotlin equivalent of try-with-resources in Java.

`finally` is the general tool: its block runs after the `try` block whether or not an exception happened. Use `use` for anything that can be closed, and `finally` for other cleanup.

The example writes a file with `use`, reads it back, throws an exception inside a second `use` block, and shows that a reader that was closed by `use` refuses to read.

### Worked Example

```kotlin
import java.io.File

fun main() {
    val file = File("cleanup_demo.txt")
    file.bufferedWriter().use { it.write("Some data.\n") }
    println(file.readText().trim())

    val reader = file.bufferedReader()
    val firstLine = reader.use { it.readLine() }
    println(firstLine)

    val result = runCatching {
        file.bufferedReader().use { r ->
            r.readLine()
            throw IllegalStateException("failure while reading")
        }
    }
    println(result.exceptionOrNull()?.message)

    try {
        println("working")
    } finally {
        println("finally block ran")
    }

    println(runCatching { reader.readLine() }.exceptionOrNull() != null)
}
```

### Expected Behavior or Output

The program prints:
```text
Some data.
Some data.
failure while reading
working
finally block ran
true
```

### Common Mistakes
1. Opening a reader or writer and forgetting to close it.
2. Putting `return` in a `finally` block, which can hide an earlier exception.
3. Using the reader after `use` has closed it.

### Activities
1. Predict the six printed lines.
2. Rewrite the first example with an explicit `try` and `finally` and compare the length.
3. Throw an exception before the write and confirm that the file is still closed.
4. Explain why cleanup matters even if the program is about to end.

### Accessibility Practice

Print a short labelled line after each step, so the screen reader announces which path ran. Labelled lines make the order of cleanup audible.

### Skills Checklist
- [ ] I can close files with `use`.
- [ ] I can use `finally`.
- [ ] I know `use` closes after an error.
- [ ] I can show a closed reader refuses to read.
- [ ] I can explain why cleanup matters.

---

## Lesson 8.5: Storing Data with JSON

### Reading References
- Kotlin serialization documentation (kotlinlang.org/docs/serialization.html)
- JSON specification: https://www.json.org
- Matching Python lesson: Lesson 8.5: Storing Data with JSON

### Learning Objectives
- Explain why this lesson includes a JSON helper.
- Encode and decode the shared task records.
- Handle a missing or malformed file.

### Concept Explanation

The Kotlin standard library has no JSON support. Real projects add the `kotlinx.serialization` library through Gradle, which also requires a compiler plugin. To keep this course free of build tooling, the example includes a *teaching implementation*, `object Json`, with `encode` and `decode`. It handles strings, numbers, booleans, `null`, lists, and maps, writes object keys in sorted order, and reports malformed text with an exception that includes the position. It is not a replacement for a production library.

JSON text stores data in a standard format: `{ ... }` holds key-value pairs, `[ ... ]` holds ordered items, and text is in double quotation marks. Decoded data is untyped (`Map<String, Any?>`), so check each field before using it. Numbers without a decimal point decode as `Long`.

The shared to-do record has the fields `id`, `title`, `description`, `done`, and `created_at`. The example saves two tasks and loads them back, then shows the message for a malformed file.

The teaching helper decodes JSON `null` as `null` and numbers without a decimal point as `Long`. It does not handle every number edge case that a full parser must.

### Worked Example

```kotlin
object Json {
    fun encode(value: Any?): String = when (value) {
        null -> "null"
        is String -> quote(value)
        is Boolean, is Int, is Long, is Double -> value.toString()
        is Map<*, *> -> value.entries.sortedBy { it.key.toString() }
            .joinToString(",", "{", "}") { quote(it.key.toString()) + ":" + encode(it.value) }
        is List<*> -> value.joinToString(",", "[", "]") { encode(it) }
        else -> throw IllegalArgumentException("cannot encode ${value::class.simpleName}")
    }

    private fun quote(text: String): String {
        val out = StringBuilder("\"")
        for (c in text) {
            when {
                c == '"' -> out.append("\\\"")
                c == '\\' -> out.append("\\\\")
                c == '\n' -> out.append("\\n")
                c == '\r' -> out.append("\\r")
                c == '\t' -> out.append("\\t")
                c < ' ' -> out.append("\\u%04x".format(c.code))
                else -> out.append(c)
            }
        }
        return out.append('"').toString()
    }

    fun decode(text: String): Any? = Parser(text).parse()

    private class Parser(private val text: String) {
        private var pos = 0

        private fun fail(message: String): Nothing =
            throw IllegalArgumentException("$message at position $pos")

        private fun skip() {
            while (pos < text.length && text[pos].isWhitespace()) pos++
        }

        fun parse(): Any? {
            val result = value()
            skip()
            if (pos < text.length) fail("unexpected extra text")
            return result
        }

        private fun value(): Any? {
            skip()
            if (pos >= text.length) fail("unexpected end of text")
            val c = text[pos]
            return when {
                c == '{' -> obj()
                c == '[' -> list()
                c == '"' -> str()
                text.startsWith("true", pos) -> { pos += 4; true }
                text.startsWith("false", pos) -> { pos += 5; false }
                text.startsWith("null", pos) -> { pos += 4; null }
                c == '-' || c.isDigit() -> number()
                else -> fail("unexpected character")
            }
        }

        private fun number(): Any {
            val start = pos
            if (text[pos] == '-') pos++
            while (pos < text.length && (text[pos].isDigit() || text[pos] in ".eE+-")) pos++
            val token = text.substring(start, pos)
            return token.toLongOrNull() ?: token.toDoubleOrNull() ?: fail("bad number")
        }

        private fun str(): String {
            pos++
            val out = StringBuilder()
            while (true) {
                if (pos >= text.length) fail("unterminated string")
                val c = text[pos++]
                if (c == '"') return out.toString()
                if (c != '\\') { out.append(c); continue }
                if (pos >= text.length) fail("bad escape")
                when (text[pos++]) {
                    'n' -> out.append('\n')
                    't' -> out.append('\t')
                    'r' -> out.append('\r')
                    '"' -> out.append('"')
                    '\\' -> out.append('\\')
                    '/' -> out.append('/')
                    'u' -> {
                        if (pos + 4 > text.length) fail("bad escape")
                        out.append(text.substring(pos, pos + 4).toInt(16).toChar())
                        pos += 4
                    }
                    else -> fail("bad escape")
                }
            }
        }

        private fun obj(): Map<String, Any?> {
            pos++
            val map = LinkedHashMap<String, Any?>()
            skip()
            if (pos < text.length && text[pos] == '}') { pos++; return map }
            while (true) {
                skip()
                if (pos >= text.length || text[pos] != '"') fail("expected a key")
                val key = str()
                skip()
                if (pos >= text.length || text[pos] != ':') fail("expected ':'")
                pos++
                map[key] = value()
                skip()
                if (pos >= text.length) fail("unterminated object")
                val d = text[pos++]
                if (d == '}') return map
                if (d != ',') { pos--; fail("expected ',' or '}'") }
            }
        }

        private fun list(): List<Any?> {
            pos++
            val items = ArrayList<Any?>()
            skip()
            if (pos < text.length && text[pos] == ']') { pos++; return items }
            while (true) {
                items.add(value())
                skip()
                if (pos >= text.length) fail("unterminated list")
                val d = text[pos++]
                if (d == ']') return items
                if (d != ',') { pos--; fail("expected ',' or ']'") }
            }
        }
    }
}

fun main() {
    val tasks = listOf(
        mapOf("id" to 1, "title" to "Study programming", "description" to "Finish Unit 8",
            "done" to false, "created_at" to "2026-01-15T09:00:00"),
        mapOf("id" to 2, "title" to "Review scores", "description" to "Check the four scores",
            "done" to true, "created_at" to "2026-01-15T09:30:00"),
    )

    val file = java.io.File("tasks.json")
    file.writeText(Json.encode(tasks))

    if (!file.exists()) {
        println("Tasks file not found.")
        return
    }
    val loaded = try {
        Json.decode(file.readText()) as List<*>
    } catch (e: IllegalArgumentException) {
        println("Error: could not decode tasks file: ${e.message}")
        return
    }
    for (entry in loaded) {
        val task = entry as Map<*, *>
        val status = if (task["done"] == true) "done" else "not done"
        println("${task["id"]}: ${task["title"]} ($status)")
    }

    println(runCatching { Json.decode("[{\"id\": 1,") }.exceptionOrNull()?.message)
}
```

### Expected Behavior or Output

The program prints:
```text
1: Study programming (not done)
2: Review scores (done)
expected a key at position 10
```

### Common Mistakes
1. Assuming Kotlin has built-in JSON support.
2. Trusting decoded data without checking that each field exists and has the right type.
3. Overwriting a good data file with an empty list after a failed load.

### Activities
1. Run the program and read the saved JSON text from `tasks.json`.
2. Edit `tasks.json` by hand to remove a closing bracket and run the loading part again. Read the message.
3. Add a third task and confirm that it is saved and loaded.
4. Explain why a production project should use `kotlinx.serialization`.

### Accessibility Practice

Open `tasks.json` in the terminal and read it as text. JSON in a single line is difficult to navigate, so practise stepping through it by word or character.

### Skills Checklist
- [ ] I know Kotlin has no built-in JSON.
- [ ] I can encode and decode records.
- [ ] I handle missing and malformed files.
- [ ] I check decoded fields.
- [ ] I know when to use a library.
>>>>>>> 2067a20 (curriculum clearning and updates)

---
