# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

Build a personal data manager with the shared record schema, storage, search and completion, acceptance tests, and a documentation and accessibility check.

---


## Lesson 11.1: Capstone: Requirements and Design

### Reading References
- [Data classes](https://kotlinlang.org/docs/data-classes.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 11.1: Introduction to NiceGUI (capstone planning)

### Learning Objectives
- Write requirements for a personal data manager.
- Define the shared record schema as a data class.
- Check records against the validation rules before building features.

### Concept Explanation

The capstone is a *personal data manager*: a program that keeps a list of records, lets the user add, view, search, change, complete, and delete them, and saves them to a file. In the Kotlin track it is a text program, so it runs from the terminal and is fully usable with a screen reader or braille display.

**Shared record schema (all general-purpose language tracks).** Every record has `id` (unique whole number), `title`, `description`, `category`, `created_at`, and `updated_at` (ISO 8601 text). A project may add fields, such as an optional `done` flag, but must not remove these. Kotlin property names use camel case (`createdAt`), and the stored JSON uses the shared names.

**Validation rules.** A record must have a non-empty title and a non-empty category. Timestamps are ISO 8601 text such as `2026-01-15T09:00:00`.

Design before coding: list the operations, then the data, then the messages. The example checks the three shared sample records against the rules and prints them as a plain-text list.

### Worked Example

```kotlin
data class Record(
    val id: Int,
    val title: String,
    val description: String,
    val category: String,
    val createdAt: String,
    val updatedAt: String,
)

fun validate(title: String?, category: String?): String? = when {
    title == null || title.isBlank() -> "A title is required."
    category == null || category.isBlank() -> "A category is required."
    else -> null
}

fun main() {
    val sample = listOf(
        Record(1, "Notebook", "Course notes", "supplies", "2026-01-15T09:00:00", "2026-01-15T09:00:00"),
        Record(2, "Pencil", "Box of 10", "supplies", "2026-01-15T09:05:00", "2026-01-15T09:05:00"),
        Record(3, "Study plan", "Weekly schedule", "planning", "2026-01-15T09:10:00", "2026-01-15T09:10:00"),
    )

    for (record in sample) {
        val problem = validate(record.title, record.category)
        println("${record.id}. ${record.title} [${record.category}] - ${problem ?: "valid"}")
    }

    println(validate("  ", "supplies"))
    println(validate("Ruler", ""))
}
```

### Expected Behavior or Output

The program prints:
```text
1. Notebook [supplies] - valid
2. Pencil [supplies] - valid
3. Study plan [planning] - valid
A title is required.
A category is required.
```

### Common Mistakes
1. Starting to build features before agreeing on the record fields.
2. Allowing a record with an empty title because the check was left for later.
3. Storing timestamps in different formats in different places.

### Activities
1. Write the seven operations as a numbered list of requirements.
2. Add one project-specific property and say how it is validated.
3. Write three sample records for your own project.
4. Describe in plain sentences what each shared field means.

### Accessibility Practice

Design the screen output as lines of plain text: one record per line, with the same field order each time. Decide the wording of every message now so that it can be tested.

### Skills Checklist
- [ ] I can write requirements.
- [ ] I know the shared record fields.
- [ ] I can write validation rules.
- [ ] I can describe sample data.
- [ ] I can plan messages before coding.

---

## Lesson 11.2: Capstone: Data Model and Storage

### Reading References
- [Data classes](https://kotlinlang.org/docs/data-classes.html)
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 11.2: Data Model and Storage

### Learning Objectives
- Store records as data class objects.
- Save and load them as JSON.
- Confirm that every field survives a round trip.

### Concept Explanation

Records are stored as a list of data class objects in memory and as a JSON array on disk. The storage layer has two functions: `saveRecords(path, records)` and `loadRecords(path)`. Loading returns a pair of the records and a message, so the caller decides what to do when the file is missing or damaged.

A `Record` is converted to a map for saving (`toMap`) and rebuilt from a decoded map when loading (`toRecord`), which checks that each field is present and has the right type. The optional `done` field defaults to `false`.

The example uses the teaching JSON helper from Lesson 8.5 (included so the program runs on its own). After saving and reloading it compares the lists; data classes compare by value, so this *round-trip test* checks every field of every record. It is the first acceptance test for storage.

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

data class Record(
    val id: Int,
    val title: String,
    val description: String,
    val category: String,
    val createdAt: String,
    val updatedAt: String,
    val done: Boolean = false,
)

fun Record.toMap(): Map<String, Any?> = mapOf(
    "id" to id, "title" to title, "description" to description, "category" to category,
    "created_at" to createdAt, "updated_at" to updatedAt, "done" to done,
)

fun toRecord(entry: Any?): Record {
    val map = entry as? Map<*, *> ?: throw IllegalArgumentException("a record must be an object")
    fun text(key: String) = map[key] as? String ?: throw IllegalArgumentException("missing field $key")
    val id = (map["id"] as? Long)?.toInt() ?: throw IllegalArgumentException("missing field id")
    return Record(id, text("title"), text("description"), text("category"),
        text("created_at"), text("updated_at"), map["done"] as? Boolean ?: false)
}

fun saveRecords(path: String, records: List<Record>) {
    java.io.File(path).writeText(Json.encode(records.map { it.toMap() }))
}

fun loadRecords(path: String): Pair<List<Record>, String?> {
    val file = java.io.File(path)
    if (!file.exists()) return Pair(emptyList(), "Could not open $path: file not found.")
    return try {
        Pair((Json.decode(file.readText()) as List<*>).map { toRecord(it) }, null)
    } catch (e: Exception) {
        Pair(emptyList(), "The data file is not valid: ${e.message}")
    }
}

fun main() {
    val sample = listOf(
        Record(1, "Notebook", "Course notes", "supplies", "2026-01-15T09:00:00", "2026-01-15T09:00:00"),
        Record(2, "Pencil", "Box of 10", "supplies", "2026-01-15T09:05:00", "2026-01-15T09:05:00"),
        Record(3, "Study plan", "Weekly schedule", "planning", "2026-01-15T09:10:00", "2026-01-15T09:10:00"),
    )

    saveRecords("records.json", sample)
    val (loaded, problem) = loadRecords("records.json")
    println("Round trip preserved all fields: ${loaded == sample}")
    println("Records loaded: ${loaded.size}")
    println(problem)

    println(loadRecords("missing.json").second)

    java.io.File("broken.json").writeText("[{\"id\": 1,")
    println(loadRecords("broken.json").second)
}
```

### Expected Behavior or Output

The program prints:
```text
Round trip preserved all fields: true
Records loaded: 3
null
Could not open missing.json: file not found.
The data file is not valid: expected a key at position 10
```

### Common Mistakes
1. Overwriting the data file with an empty list after a failed load.
2. Saving only some of the fields.
3. Assuming a loaded record has every field without checking.

### Activities
1. Run the program and open `records.json` to read the saved text.
2. Add a field to `Record`, save it, and confirm that it survives the round trip.
3. Make `toRecord` reject a record whose title is blank.
4. Explain why `loadRecords` returns a message and does not throw.

### Accessibility Practice

Messages that name the file and the problem read clearly in speech. After saving, read the file in the terminal to confirm it contains what you expect.

### Skills Checklist
- [ ] I can store records in data class objects.
- [ ] I can save and load JSON.
- [ ] I can run a round-trip test.
- [ ] I handle missing and damaged files.
- [ ] I do not overwrite good data after a failed load.

---

## Lesson 11.3: Capstone: Core Operations

### Reading References
- [Classes](https://kotlinlang.org/docs/classes.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 11.3: Displaying and Managing Items

### Learning Objectives
- Add, list, search, change, complete, and delete records.
- Assign new ids and update timestamps correctly.
- Return a message when an operation cannot be done.

### Concept Explanation

A `Manager` class holds the records and offers one function per operation. Each function that can fail returns a pair of the result and a message, so the user interface can show the message and decide what to do. New ids are one more than the highest id, so ids are never reused while higher ids exist. Updating a record sets `updatedAt` but never changes `createdAt`, which is a `val`. Completing a record sets the optional `done` field to `true` and counts as an update.

For repeatable output the example passes in a *fake clock* that returns a new fixed time on each call. A real program passes a function that reads the real time.

The example adds the three shared sample records, lists them, searches for "note", changes one description, completes one record, deletes one, and tries to delete a record that does not exist.

### Worked Example

```kotlin
data class Record(
    val id: Int,
    var title: String,
    var description: String,
    var category: String,
    val createdAt: String,
    var updatedAt: String,
    var done: Boolean = false,
)

fun validate(title: String?, category: String?): String? = when {
    title == null || title.isBlank() -> "A title is required."
    category == null || category.isBlank() -> "A category is required."
    else -> null
}

class Manager(private val clock: () -> String) {
    val records = mutableListOf<Record>()

    private fun nextId(): Int = (records.maxOfOrNull { it.id } ?: 0) + 1

    fun find(id: Int): Record? = records.firstOrNull { it.id == id }

    fun add(title: String, description: String, category: String): Pair<Record?, String?> {
        val problem = validate(title, category)
        if (problem != null) return Pair(null, problem)
        val stamp = clock()
        val record = Record(nextId(), title.trim(), description.trim(), category.trim(), stamp, stamp)
        records.add(record)
        return Pair(record, null)
    }

    fun update(
        id: Int,
        title: String? = null,
        description: String? = null,
        category: String? = null,
        done: Boolean? = null,
    ): Pair<Record?, String?> {
        val record = find(id) ?: return Pair(null, "No record has that id.")
        val problem = validate(title ?: record.title, category ?: record.category)
        if (problem != null) return Pair(null, problem)
        if (title != null) record.title = title.trim()
        if (description != null) record.description = description.trim()
        if (category != null) record.category = category.trim()
        if (done != null) record.done = done
        record.updatedAt = clock()
        return Pair(record, null)
    }

    fun complete(id: Int) = update(id, done = true)

    fun delete(id: Int): Pair<Boolean, String?> {
        val record = find(id) ?: return Pair(false, "No record has that id.")
        records.remove(record)
        return Pair(true, null)
    }

    fun search(text: String): List<Record> {
        val needle = text.trim().lowercase()
        return records.filter { it.title.lowercase().contains(needle) || it.description.lowercase().contains(needle) }
    }
}

fun describe(record: Record): String =
    "${record.id}. ${record.title} [${record.category}] (${if (record.done) "done" else "not done"})"

fun makeClock(): () -> String {
    var ticks = 0
    return {
        ticks++
        "2026-01-15T10:00:%02d".format(ticks)
    }
}

fun show(manager: Manager) {
    for (record in manager.records) println(describe(record))
}

fun main() {
    val manager = Manager(makeClock())
    manager.add("Notebook", "Course notes", "supplies")
    manager.add("Pencil", "Box of 10", "supplies")
    manager.add("Study plan", "Weekly schedule", "planning")
    show(manager)

    println("Search for 'note':")
    for (record in manager.search("note")) println(record.title)

    manager.update(2, description = "Box of 12")
    manager.complete(3)
    println("${manager.find(2)?.description} ${manager.find(2)?.updatedAt}")
    println(manager.delete(1))
    println(manager.delete(99))
    show(manager)
}
```

### Expected Behavior or Output

The program prints:
```text
1. Notebook [supplies] (not done)
2. Pencil [supplies] (not done)
3. Study plan [planning] (not done)
Search for 'note':
Notebook
Box of 12 2026-01-15T10:00:04
(true, null)
(false, No record has that id.)
2. Pencil [supplies] (not done)
3. Study plan [planning] (done)
```

### Common Mistakes
1. Reusing a deleted record's id by counting the list size instead of using the highest id.
2. Changing `createdAt` when updating a record (the property is a `val` to prevent this).
3. Throwing an exception for a missing record where a message to display is more helpful.

### Activities
1. Predict the output before running.
2. Add `listByCategory(category)` to `Manager`.
3. Add a rule that blocks completing a record that is already complete, with a message.
4. Explain how the fake clock makes the output repeatable.

### Accessibility Practice

List output uses the same fixed format for every record and the words `done` and `not done`. Search results print only titles, so each line is short.

### Skills Checklist
- [ ] I can implement add, list, search, change, complete, and delete.
- [ ] I assign unique ids.
- [ ] I update timestamps correctly.
- [ ] I return clear messages for failures.
- [ ] I can make output repeatable with a fake clock.

---

## Lesson 11.4: Capstone: Validation and Acceptance Tests

### Reading References
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- [Functions](https://kotlinlang.org/docs/functions.html)
- Matching Python lesson: Lesson 11.4: Testing and Refinement

### Learning Objectives
- Run the shared acceptance tests.
- Verify that validation rejects bad data.
- Read and interpret test results.

### Concept Explanation

The shared acceptance tests describe behavior that every language track's capstone must show:

1. Adding a record with an empty title is rejected with a clear message.
2. A new record receives an unused `id`.
3. Updating a record changes `updated_at` but not `created_at`.
4. Deleting a record removes only that record.
5. Saving and reloading preserves all fields and values (shown in Lesson 11.2).
6. Every message and control can be used without color or a mouse (checked by hand in Lesson 11.5).

This lesson automates tests 1 to 4 and also tests completion and the rejection of a blank title in an update. Each test builds a new `Manager`, so tests cannot affect each other. The fake clock keeps timestamps predictable so a test can check that `updatedAt` changed while `createdAt` did not.

### Worked Example

```kotlin
data class Record(
    val id: Int,
    var title: String,
    var description: String,
    var category: String,
    val createdAt: String,
    var updatedAt: String,
    var done: Boolean = false,
)

fun validate(title: String?, category: String?): String? = when {
    title == null || title.isBlank() -> "A title is required."
    category == null || category.isBlank() -> "A category is required."
    else -> null
}

class Manager(private val clock: () -> String) {
    val records = mutableListOf<Record>()

    private fun nextId(): Int = (records.maxOfOrNull { it.id } ?: 0) + 1

    fun find(id: Int): Record? = records.firstOrNull { it.id == id }

    fun add(title: String, description: String, category: String): Pair<Record?, String?> {
        val problem = validate(title, category)
        if (problem != null) return Pair(null, problem)
        val stamp = clock()
        val record = Record(nextId(), title.trim(), description.trim(), category.trim(), stamp, stamp)
        records.add(record)
        return Pair(record, null)
    }

    fun update(
        id: Int,
        title: String? = null,
        description: String? = null,
        category: String? = null,
        done: Boolean? = null,
    ): Pair<Record?, String?> {
        val record = find(id) ?: return Pair(null, "No record has that id.")
        val problem = validate(title ?: record.title, category ?: record.category)
        if (problem != null) return Pair(null, problem)
        if (title != null) record.title = title.trim()
        if (description != null) record.description = description.trim()
        if (category != null) record.category = category.trim()
        if (done != null) record.done = done
        record.updatedAt = clock()
        return Pair(record, null)
    }

    fun complete(id: Int) = update(id, done = true)

    fun delete(id: Int): Pair<Boolean, String?> {
        val record = find(id) ?: return Pair(false, "No record has that id.")
        records.remove(record)
        return Pair(true, null)
    }

    fun search(text: String): List<Record> {
        val needle = text.trim().lowercase()
        return records.filter { it.title.lowercase().contains(needle) || it.description.lowercase().contains(needle) }
    }
}

fun describe(record: Record): String =
    "${record.id}. ${record.title} [${record.category}] (${if (record.done) "done" else "not done"})"

fun makeClock(): () -> String {
    var ticks = 0
    return {
        ticks++
        "2026-01-15T10:00:%02d".format(ticks)
    }
}

var failures = 0

fun test(name: String, body: () -> Unit) {
    val result = runCatching(body)
    if (result.isSuccess) {
        println("PASS $name")
    } else {
        failures++
        println("FAIL $name: ${result.exceptionOrNull()?.message}")
    }
}

fun assertThat(condition: Boolean, message: String) {
    if (!condition) throw AssertionError(message)
}

fun fresh(): Manager {
    val manager = Manager(makeClock())
    manager.add("Notebook", "Course notes", "supplies")
    manager.add("Pencil", "Box of 10", "supplies")
    manager.add("Study plan", "Weekly schedule", "planning")
    return manager
}

fun main() {
    test("1. an empty title is rejected") {
        val manager = fresh()
        val (record, message) = manager.add("   ", "x", "supplies")
        assertThat(record == null && message == "A title is required.", "expected the title message")
        assertThat(manager.records.size == 3, "the list should be unchanged")
    }

    test("2. a new record gets an unused id") {
        val manager = fresh()
        manager.delete(2)
        val (record, _) = manager.add("Ruler", "30 cm", "supplies")
        assertThat(record?.id == 4, "expected id 4 but got ${record?.id}")
    }

    test("3. update changes updatedAt but not createdAt") {
        val manager = fresh()
        val before = manager.find(1)!!.copy()
        manager.update(1, description = "Lecture notes")
        val after = manager.find(1)!!
        assertThat(after.createdAt == before.createdAt, "createdAt changed")
        assertThat(after.updatedAt != before.updatedAt, "updatedAt did not change")
    }

    test("4. delete removes only that record") {
        val manager = fresh()
        manager.delete(2)
        val ids = manager.records.map { it.id }
        assertThat(ids == listOf(1, 3), "wrong records remain: $ids")
    }

    test("5. complete marks done and updates the record") {
        val manager = fresh()
        val (record, _) = manager.complete(3)
        assertThat(record?.done == true && record.updatedAt != record.createdAt, "completion not recorded")
    }

    test("6. a blank title cannot be saved by update") {
        val manager = fresh()
        val (record, message) = manager.update(1, title = "")
        assertThat(record == null && message == "A title is required.", "update accepted a blank title")
    }

    println(if (failures == 0) "All acceptance tests passed." else "$failures test(s) failed.")
}
```

### Expected Behavior or Output

The program prints:
```text
PASS 1. an empty title is rejected
PASS 2. a new record gets an unused id
PASS 3. update changes updatedAt but not createdAt
PASS 4. delete removes only that record
PASS 5. complete marks done and updates the record
PASS 6. a blank title cannot be saved by update
All acceptance tests passed.
```

### Common Mistakes
1. Sharing one manager between tests, so one test's deletions change the next test.
2. Checking only that no exception occurred, and not checking the result.
3. Writing the expected message differently from the program, so a correct program fails the test.

### Activities
1. Break `Manager.update` so it also changes `createdAt` (make the property a `var`) and watch test 3 fail. Restore it.
2. Add a test that searching ignores case.
3. Add a test that deleting an unknown id returns `false` and a message.
4. Explain why test 2 deletes record 2 before adding the new one.

### Accessibility Practice

The test names begin with the acceptance-test number, so PASS and FAIL lines can be matched to the specification. Read only the first word of each line to hear the overall result quickly.

### Skills Checklist
- [ ] I can run the shared acceptance tests.
- [ ] I can test validation failures.
- [ ] I can test timestamps with a fake clock.
- [ ] I can read PASS and FAIL lines.
- [ ] I use a fresh manager for every test.

---

## Lesson 11.5: Capstone: Documentation and Presentation

### Reading References
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- [Unit P, Lesson P.6](../FOUNDATIONS/unit-p-computing-foundations.md): files, data formats, and the shared accessible workflow
- Matching Python lesson: Lesson 11.5: Final Submission

### Learning Objectives
- Write a plain-text project summary.
- Report a count of records by category.
- Complete a manual accessibility check.

### Concept Explanation

Documentation tells a future reader what the program does and how to run it. Write it as plain text or Markdown with short headings, numbered steps, and complete sentences. Include: the purpose of the program, the compile and run commands, the shared record fields, the commands a user can give, the accessibility checks you carried out, and what you would improve next.

The example generates a summary from the shared sample data. It counts records by category and prints the categories in alphabetical order so the output is stable. It then prints the manual accessibility checklist. The unchecked boxes `[ ]` are for *you* to complete by hand with your own access technology; the program cannot verify them.

Acceptance test 6 is a manual check: every message and control can be used without color or a mouse. Test it with the keyboard only, and with the screen reader or braille display you actually use. Record what you tested and its version; do not claim compatibility with software you did not test.

### Worked Example

```kotlin
data class Record(val id: Int, val title: String, val category: String)

fun main() {
    val sample = listOf(
        Record(1, "Notebook", "supplies"),
        Record(2, "Pencil", "supplies"),
        Record(3, "Study plan", "planning"),
    )

    val counts = sample.groupingBy { it.category }.eachCount().toSortedMap()

    println("Personal Data Manager - Summary")
    println("Records: ${sample.size}")
    println("Categories:")
    for ((category, count) in counts) {
        println("- $category: $count")
    }

    println()
    println("Manual accessibility checklist (complete this by hand):")
    val checks = listOf(
        "[ ] Every command can be used with the keyboard only.",
        "[ ] Every message is a complete sentence that says what to do next.",
        "[ ] No meaning depends on color, position, or symbols alone.",
        "[ ] The output was read with my own screen reader or braille display.",
        "[ ] I recorded the operating system, program, and version I tested.",
    )
    for (check in checks) println(check)
}
```

### Expected Behavior or Output

The program prints:
```text
Personal Data Manager - Summary
Records: 3
Categories:
- planning: 1
- supplies: 2

Manual accessibility checklist (complete this by hand):
[ ] Every command can be used with the keyboard only.
[ ] Every message is a complete sentence that says what to do next.
[ ] No meaning depends on color, position, or symbols alone.
[ ] The output was read with my own screen reader or braille display.
[ ] I recorded the operating system, program, and version I tested.
```

### Common Mistakes
1. Writing documentation that only the author can follow.
2. Claiming that a program is accessible without recording what was tested and how.
3. Letting the documentation drift from the program after later changes.

### Activities
1. Write the project summary for your own capstone using the headings above.
2. Run the keyboard-only check and record each problem you find.
3. Ask a classmate to follow your run instructions from a fresh folder and note where they get stuck.
4. Write three improvements for the next version, ordered by user benefit.

### Accessibility Practice

This is the final accessibility lesson. Read your own documentation aloud from start to finish. Anything you have to look at the screen to understand needs rewriting.

### Skills Checklist
- [ ] I can write a plain-text project summary.
- [ ] I can report counts by category.
- [ ] I can run a manual accessibility check.
- [ ] I record what I tested.
- [ ] I do not claim untested compatibility.

---

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)
