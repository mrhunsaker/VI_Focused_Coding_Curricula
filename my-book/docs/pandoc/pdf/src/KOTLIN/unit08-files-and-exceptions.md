[Header 2 ("unit-8-files-and-exceptions", [], []) [Str "Unit 8: Files and Exceptions"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Read and write files, handle errors, release resources reliably, and store records as JSON."], HorizontalRule, Header 3 ("lesson-81-reading-from-a-file", ["unnumbered", "unlisted"], []) [Str "Lesson 8.1: Reading from a File"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Kotlin standard library: kotlin.io"] ("https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.io/", "")]], [Plain [Link ("", [], []) [Str "Exceptions"] ("https://kotlinlang.org/docs/exceptions.html", "")]], [Plain [Str "Matching Python lesson: Lesson 8.1: Reading from a File"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Read a whole file and read it line by line."]], [Plain [Str "Check that a file exists before reading."]], [Plain [Str "Report a missing file clearly."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "java.io.File", Str " represents a path. ", Code ("", [], []) "readText()", Str " returns the whole file as a string, ", Code ("", [], []) "readLines()", Str " returns a list of lines, and ", Code ("", [], []) "forEachLine { ... }", Str " processes one line at a time. A relative path such as ", Code ("", [], []) "notes.txt", Str " starts from the program's working directory, so a program run from another folder will not find it."], Para [Code ("", [], []) "File.exists()", Str " tests whether a file is there. Reading a file that does not exist throws a ", Code ("", [], []) "FileNotFoundException", Str ", which Lesson 8.3 handles."], Para [Str "To keep the lesson self-contained, the example first writes the two-line ", Code ("", [], []) "notes.txt", Str " that every language track uses, then reads it three ways and checks a file that does not exist."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "import java.io.File

fun main() {
    val notes = File(\"notes.txt\")
    notes.writeText(\"Practice Kotlin.\\nReview lists and functions.\\n\")

    println(notes.readText())

    for (line in notes.readLines()) {
        println(line)
    }
    println(notes.readLines().size)

    notes.forEachLine { println(it.uppercase()) }

    val missing = File(\"missing_notes.txt\")
    if (!missing.exists()) {
        println(\"missing_notes.txt was not found.\")
    }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Practice Kotlin.
Review lists and functions.

Practice Kotlin.
Review lists and functions.
2
PRACTICE KOTLIN.
REVIEW LISTS AND FUNCTIONS.
missing_notes.txt was not found.
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Reading a file that does not exist without checking or catching the error."]], [Plain [Str "Running from a different folder, so the relative path points to the wrong place."]], [Plain [Str "Forgetting that ", Code ("", [], []) "readText()", Str " keeps the final newline, so ", Code ("", [], []) "println", Str " adds a blank line."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program and describe each block of output."]], [Plain [Str "Add a third line to the file text and predict the new count."]], [Plain [Str "Print each line with its line number."]], [Plain [Str "Print a friendly message that includes the missing file's name."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the output aloud in order. Make an error message a complete sentence that includes the file name so that it is clear without seeing the screen."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can read a file whole and by line."]], [Plain [Str "\9744", Space, Str "I can check that a file exists."]], [Plain [Str "\9744", Space, Str "I know relative paths use the working directory."]], [Plain [Str "\9744", Space, Str "I can report a missing file."]], [Plain [Str "\9744", Space, Str "I can write a file for the example."]]], HorizontalRule, Header 3 ("lesson-82-writing-to-a-file", ["unnumbered", "unlisted"], []) [Str "Lesson 8.2: Writing to a File"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Kotlin standard library: kotlin.io"] ("https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.io/", "")]], [Plain [Str "Matching Python lesson: Lesson 8.2: Writing to a File"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write with ", Code ("", [], []) "writeText", Str " and append with ", Code ("", [], []) "appendText", Str "."]], [Plain [Str "Include line endings correctly."]], [Plain [Str "Read the file back to verify it."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "writeText(text)", Str " creates the file or ", Strong [Str "replaces"], Str " its contents. ", Code ("", [], []) "appendText(text)", Str " adds to the end. Neither adds a line ending for you, so end each line with ", Code ("", [], []) "\\n", Str ". ", Code ("", [], []) "printWriter()", Str " and ", Code ("", [], []) "bufferedWriter()", Str " write in pieces and should be closed with ", Code ("", [], []) "use", Str " (Lesson 8.4)."], Para [Str "Reading the file back is the simplest way to confirm what was saved. The example writes the first notes line, appends the second, and reads the file back."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "import java.io.File

fun main() {
    val file = File(\"notes.txt\")
    file.writeText(\"Practice Kotlin.\\n\")
    file.appendText(\"Review lists and functions.\\n\")
    print(file.readText())
    println(\"Lines: ${file.readLines().size}\")
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Practice Kotlin.
Review lists and functions.
Lines: 2
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) "writeText", Str " when ", Code ("", [], []) "appendText", Str " was intended, which erases earlier content."]], [Plain [Str "Forgetting ", Code ("", [], []) "\\n", Str ", so all written lines run together."]], [Plain [Str "Not reading the file back to check what was actually saved."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output, then run."]], [Plain [Str "Replace the second call with ", Code ("", [], []) "writeText", Str " and explain the difference."]], [Plain [Str "Append a third line with the current number of lines."]], [Plain [Str "Write the shared scores, one per line, then read them back and total them."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Always read a written file back in the terminal to confirm it, using line navigation, so you do not depend on assumptions about what was saved."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write and append."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "writeText", Str " replaces."]], [Plain [Str "\9744", Space, Str "I can include line endings."]], [Plain [Str "\9744", Space, Str "I can verify by reading back."]], [Plain [Str "\9744", Space, Str "I can count lines in a file."]]], HorizontalRule, Header 3 ("lesson-83-exceptions", ["unnumbered", "unlisted"], []) [Str "Lesson 8.3: Exceptions"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Exceptions"] ("https://kotlinlang.org/docs/exceptions.html", "")]], [Plain [Str "Matching Python lesson: Lesson 8.3: Exceptions - Handling Errors"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Catch specific exceptions with ", Code ("", [], []) "try", Str " and ", Code ("", [], []) "catch", Str "."]], [Plain [Str "Use ", Code ("", [], []) "finally", Str " and ", Code ("", [], []) "runCatching", Str "."]], [Plain [Str "Raise errors with ", Code ("", [], []) "require", Str " and ", Code ("", [], []) "error", Str "."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "An ", Emph [Str "exception"], Str " is an error that stops the program unless it is caught. ", Code ("", [], []) "try { ... } catch (e: SomeException) { ... }", Str " runs the risky code and handles the failure. Catch the ", Strong [Str "specific"], Str " exception you expect (", Code ("", [], []) "FileNotFoundException", Str ", ", Code ("", [], []) "NumberFormatException", Str ", ", Code ("", [], []) "ArithmeticException", Str "), never everything, so mistakes in your own code are not hidden. A ", Code ("", [], []) "finally", Str " block runs whether or not an exception happened."], Para [Str "Kotlin has no checked exceptions: the compiler does not force you to catch anything. ", Code ("", [], []) "runCatching { ... }", Str " runs a block and returns a ", Code ("", [], []) "Result", Str " that holds either the value or the exception, and ", Code ("", [], []) "exceptionOrNull()?.message", Str " reads the message."], Para [Code ("", [], []) "require(condition) { message }", Str " rejects a bad argument and ", Code ("", [], []) "error(message)", Str " throws an ", Code ("", [], []) "IllegalStateException", Str ". Integer division by zero throws an ", Code ("", [], []) "ArithmeticException", Str "; division of ", Code ("", [], []) "Double", Str " values by zero gives infinity instead."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "import java.io.File
import java.io.FileNotFoundException

fun main() {
    try {
        File(\"missing_notes.txt\").readText()
    } catch (e: FileNotFoundException) {
        println(\"Error: missing_notes.txt was not found.\")
    }

    try {
        \"abc\".toInt()
    } catch (e: NumberFormatException) {
        println(\"Error: 'abc' is not a valid score.\")
    }

    val zero = 0
    try {
        println(10 / zero)
    } catch (e: ArithmeticException) {
        println(\"Error: ${e.message}\")
    }
    println(10.0 / zero)

    val result = runCatching { require(false) { \"custom failure\" } }
    println(result.exceptionOrNull()?.message)

    try {
        error(\"raised by error()\")
    } catch (e: IllegalStateException) {
        println(e.message)
    } finally {
        println(\"Cleanup runs either way.\")
    }
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score.
Error: / by zero
Infinity
custom failure
raised by error()
Cleanup runs either way.
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Catching ", Code ("", [], []) "Exception", Str " for everything, which hides mistakes in your own code."]], [Plain [Str "Using ", Code ("", [], []) "toInt()", Str " on untrusted text without a catch or ", Code ("", [], []) "toIntOrNull()", Str "."]], [Plain [Str "Expecting ", Code ("", [], []) "10.0 / 0", Str " to throw. It gives ", Code ("", [], []) "Infinity", Str "."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict each printed line before running."]], [Plain [Str "Wrap ", Code ("", [], []) "readln().toInt()", Str " so invalid input prints a clear message and asks again."]], [Plain [Str "Catch ", Code ("", [], []) "ArithmeticException", Str " in a function that computes an average of an empty list."]], [Plain [Str "Explain when to catch an exception and when to let it stop the program."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.' Read the exception's class name aloud when you see a stack trace, then jump to the first line that names your own file."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can catch specific exceptions."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "finally", Str " and ", Code ("", [], []) "runCatching", Str "."]], [Plain [Str "\9744", Space, Str "I can raise errors with ", Code ("", [], []) "require", Str " and ", Code ("", [], []) "error", Str "."]], [Plain [Str "\9744", Space, Str "I know integer and decimal division by zero differ."]], [Plain [Str "\9744", Space, Str "I can write clear error messages."]]], HorizontalRule, Header 3 ("lesson-84-cleanup-with-use-and-finally", ["unnumbered", "unlisted"], []) [Str "Lesson 8.4: Cleanup with use and finally"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Exceptions: finally"] ("https://kotlinlang.org/docs/exceptions.html#the-finally-block", "")]], [Plain [Str "Matching Python lesson: Lesson 8.4: The else and finally Blocks"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Close files reliably with ", Code ("", [], []) "use", Str "."]], [Plain [Str "Show that a resource is released even after an error."]], [Plain [Str "Use ", Code ("", [], []) "finally", Str " for cleanup."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A file reader or writer holds a resource from the operating system, so it must be closed. The extension function ", Code ("", [], []) "use { ... }", Str " runs a block and then closes the resource, ", Strong [Str "even if the block throws an exception"], Str ". It is the Kotlin equivalent of try-with-resources in Java."], Para [Code ("", [], []) "finally", Str " is the general tool: its block runs after the ", Code ("", [], []) "try", Str " block whether or not an exception happened. Use ", Code ("", [], []) "use", Str " for anything that can be closed, and ", Code ("", [], []) "finally", Str " for other cleanup."], Para [Str "The example writes a file with ", Code ("", [], []) "use", Str ", reads it back, throws an exception inside a second ", Code ("", [], []) "use", Str " block, and shows that a reader that was closed by ", Code ("", [], []) "use", Str " refuses to read."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "import java.io.File

fun main() {
    val file = File(\"cleanup_demo.txt\")
    file.bufferedWriter().use { it.write(\"Some data.\\n\") }
    println(file.readText().trim())

    val reader = file.bufferedReader()
    val firstLine = reader.use { it.readLine() }
    println(firstLine)

    val result = runCatching {
        file.bufferedReader().use { r ->
            r.readLine()
            throw IllegalStateException(\"failure while reading\")
        }
    }
    println(result.exceptionOrNull()?.message)

    try {
        println(\"working\")
    } finally {
        println(\"finally block ran\")
    }

    println(runCatching { reader.readLine() }.exceptionOrNull() != null)
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Some data.
Some data.
failure while reading
working
finally block ran
true
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Opening a reader or writer and forgetting to close it."]], [Plain [Str "Putting ", Code ("", [], []) "return", Str " in a ", Code ("", [], []) "finally", Str " block, which can hide an earlier exception."]], [Plain [Str "Using the reader after ", Code ("", [], []) "use", Str " has closed it."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the six printed lines."]], [Plain [Str "Rewrite the first example with an explicit ", Code ("", [], []) "try", Str " and ", Code ("", [], []) "finally", Str " and compare the length."]], [Plain [Str "Throw an exception before the write and confirm that the file is still closed."]], [Plain [Str "Explain why cleanup matters even if the program is about to end."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print a short labelled line after each step, so the screen reader announces which path ran. Labelled lines make the order of cleanup audible."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can close files with ", Code ("", [], []) "use", Str "."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "finally", Str "."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "use", Str " closes after an error."]], [Plain [Str "\9744", Space, Str "I can show a closed reader refuses to read."]], [Plain [Str "\9744", Space, Str "I can explain why cleanup matters."]]], HorizontalRule, Header 3 ("lesson-85-storing-data-with-json", ["unnumbered", "unlisted"], []) [Str "Lesson 8.5: Storing Data with JSON"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Kotlin serialization documentation (kotlinlang.org/docs/serialization.html)"]], [Plain [Str "JSON specification: https://www.json.org"]], [Plain [Str "Matching Python lesson: Lesson 8.5: Storing Data with JSON"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain why this lesson includes a JSON helper."]], [Plain [Str "Encode and decode the shared task records."]], [Plain [Str "Handle a missing or malformed file."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The Kotlin standard library has no JSON support. Real projects add the ", Code ("", [], []) "kotlinx.serialization", Str " library through Gradle, which also requires a compiler plugin. To keep this course free of build tooling, the example includes a ", Emph [Str "teaching implementation"], Str ", ", Code ("", [], []) "object Json", Str ", with ", Code ("", [], []) "encode", Str " and ", Code ("", [], []) "decode", Str ". It handles strings, numbers, booleans, ", Code ("", [], []) "null", Str ", lists, and maps, writes object keys in sorted order, and reports malformed text with an exception that includes the position. It is not a replacement for a production library."], Para [Str "JSON text stores data in a standard format: ", Code ("", [], []) "{ ... }", Str " holds key-value pairs, ", Code ("", [], []) "[ ... ]", Str " holds ordered items, and text is in double quotation marks. Decoded data is untyped (", Code ("", [], []) "Map<String, Any?>", Str "), so check each field before using it. Numbers without a decimal point decode as ", Code ("", [], []) "Long", Str "."], Para [Str "The shared to-do record has the fields ", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "done", Str ", and ", Code ("", [], []) "created_at", Str ". The example saves two tasks and loads them back, then shows the message for a malformed file."], Para [Str "The teaching helper decodes JSON ", Code ("", [], []) "null", Str " as ", Code ("", [], []) "null", Str " and numbers without a decimal point as ", Code ("", [], []) "Long", Str ". It does not handle every number edge case that a full parser must."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "object Json {
    fun encode(value: Any?): String = when (value) {
        null -> \"null\"
        is String -> quote(value)
        is Boolean, is Int, is Long, is Double -> value.toString()
        is Map<*, *> -> value.entries.sortedBy { it.key.toString() }
            .joinToString(\",\", \"{\", \"}\") { quote(it.key.toString()) + \":\" + encode(it.value) }
        is List<*> -> value.joinToString(\",\", \"[\", \"]\") { encode(it) }
        else -> throw IllegalArgumentException(\"cannot encode ${value::class.simpleName}\")
    }

    private fun quote(text: String): String {
        val out = StringBuilder(\"\\\"\")
        for (c in text) {
            when {
                c == '\"' -> out.append(\"\\\\\\\"\")
                c == '\\\\' -> out.append(\"\\\\\\\\\")
                c == '\\n' -> out.append(\"\\\\n\")
                c == '\\r' -> out.append(\"\\\\r\")
                c == '\\t' -> out.append(\"\\\\t\")
                c < ' ' -> out.append(\"\\\\u%04x\".format(c.code))
                else -> out.append(c)
            }
        }
        return out.append('\"').toString()
    }

    fun decode(text: String): Any? = Parser(text).parse()

    private class Parser(private val text: String) {
        private var pos = 0

        private fun fail(message: String): Nothing =
            throw IllegalArgumentException(\"$message at position $pos\")

        private fun skip() {
            while (pos < text.length && text[pos].isWhitespace()) pos++
        }

        fun parse(): Any? {
            val result = value()
            skip()
            if (pos < text.length) fail(\"unexpected extra text\")
            return result
        }

        private fun value(): Any? {
            skip()
            if (pos >= text.length) fail(\"unexpected end of text\")
            val c = text[pos]
            return when {
                c == '{' -> obj()
                c == '[' -> list()
                c == '\"' -> str()
                text.startsWith(\"true\", pos) -> { pos += 4; true }
                text.startsWith(\"false\", pos) -> { pos += 5; false }
                text.startsWith(\"null\", pos) -> { pos += 4; null }
                c == '-' || c.isDigit() -> number()
                else -> fail(\"unexpected character\")
            }
        }

        private fun number(): Any {
            val start = pos
            if (text[pos] == '-') pos++
            while (pos < text.length && (text[pos].isDigit() || text[pos] in \".eE+-\")) pos++
            val token = text.substring(start, pos)
            return token.toLongOrNull() ?: token.toDoubleOrNull() ?: fail(\"bad number\")
        }

        private fun str(): String {
            pos++
            val out = StringBuilder()
            while (true) {
                if (pos >= text.length) fail(\"unterminated string\")
                val c = text[pos++]
                if (c == '\"') return out.toString()
                if (c != '\\\\') { out.append(c); continue }
                if (pos >= text.length) fail(\"bad escape\")
                when (text[pos++]) {
                    'n' -> out.append('\\n')
                    't' -> out.append('\\t')
                    'r' -> out.append('\\r')
                    '\"' -> out.append('\"')
                    '\\\\' -> out.append('\\\\')
                    '/' -> out.append('/')
                    'u' -> {
                        if (pos + 4 > text.length) fail(\"bad escape\")
                        out.append(text.substring(pos, pos + 4).toInt(16).toChar())
                        pos += 4
                    }
                    else -> fail(\"bad escape\")
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
                if (pos >= text.length || text[pos] != '\"') fail(\"expected a key\")
                val key = str()
                skip()
                if (pos >= text.length || text[pos] != ':') fail(\"expected ':'\")
                pos++
                map[key] = value()
                skip()
                if (pos >= text.length) fail(\"unterminated object\")
                val d = text[pos++]
                if (d == '}') return map
                if (d != ',') { pos--; fail(\"expected ',' or '}'\") }
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
                if (pos >= text.length) fail(\"unterminated list\")
                val d = text[pos++]
                if (d == ']') return items
                if (d != ',') { pos--; fail(\"expected ',' or ']'\") }
            }
        }
    }
}

fun main() {
    val tasks = listOf(
        mapOf(\"id\" to 1, \"title\" to \"Study programming\", \"description\" to \"Finish Unit 8\",
            \"done\" to false, \"created_at\" to \"2026-01-15T09:00:00\"),
        mapOf(\"id\" to 2, \"title\" to \"Review scores\", \"description\" to \"Check the four scores\",
            \"done\" to true, \"created_at\" to \"2026-01-15T09:30:00\"),
    )

    val file = java.io.File(\"tasks.json\")
    file.writeText(Json.encode(tasks))

    if (!file.exists()) {
        println(\"Tasks file not found.\")
        return
    }
    val loaded = try {
        Json.decode(file.readText()) as List<*>
    } catch (e: IllegalArgumentException) {
        println(\"Error: could not decode tasks file: ${e.message}\")
        return
    }
    for (entry in loaded) {
        val task = entry as Map<*, *>
        val status = if (task[\"done\"] == true) \"done\" else \"not done\"
        println(\"${task[\"id\"]}: ${task[\"title\"]} ($status)\")
    }

    println(runCatching { Json.decode(\"[{\\\"id\\\": 1,\") }.exceptionOrNull()?.message)
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "1: Study programming (not done)
2: Review scores (done)
expected a key at position 10
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming Kotlin has built-in JSON support."]], [Plain [Str "Trusting decoded data without checking that each field exists and has the right type."]], [Plain [Str "Overwriting a good data file with an empty list after a failed load."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program and read the saved JSON text from ", Code ("", [], []) "tasks.json", Str "."]], [Plain [Str "Edit ", Code ("", [], []) "tasks.json", Str " by hand to remove a closing bracket and run the loading part again. Read the message."]], [Plain [Str "Add a third task and confirm that it is saved and loaded."]], [Plain [Str "Explain why a production project should use ", Code ("", [], []) "kotlinx.serialization", Str "."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Open ", Code ("", [], []) "tasks.json", Str " in the terminal and read it as text. JSON in a single line is difficult to navigate, so practise stepping through it by word or character."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I know Kotlin has no built-in JSON."]], [Plain [Str "\9744", Space, Str "I can encode and decode records."]], [Plain [Str "\9744", Space, Str "I handle missing and malformed files."]], [Plain [Str "\9744", Space, Str "I check decoded fields."]], [Plain [Str "\9744", Space, Str "I know when to use a library."]]], HorizontalRule]