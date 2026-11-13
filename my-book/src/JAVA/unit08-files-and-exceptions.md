# Unit 8: Files and Exceptions

## Overview

This unit develops files and exceptions through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 8.1: Reading from a File

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 8.1: Reading from a File

### Learning Objectives
- Read a whole file and read it line by line.
- Check that a file exists before reading.
- Report a missing file clearly.

### Concept Explanation

`java.nio.file.Path` represents a location and `java.nio.file.Files` does the work. `Files.readString(path)` returns the whole file, `Files.readAllLines(path)` returns a list of lines, and `Files.lines(path)` returns a *stream* of lines that must be closed, so it is used in try-with-resources. `Files.exists(path)` tests whether a file is there. A relative path such as `notes.txt` starts from the program's working directory.

Most file methods throw the *checked* exception `IOException`, which the compiler forces you to handle: either catch it or declare `throws IOException` on the method. A missing file throws a `NoSuchFileException`.

To keep the lesson self-contained, the example first writes the two-line `notes.txt` that every language track uses, then reads it three ways and checks a file that does not exist.

### Worked Example

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.Stream;

public class Lesson_8_1 {
    public static void main(String[] args) throws IOException {
        Path notes = Path.of("notes.txt");
        Files.writeString(notes, "Practice Java.\nReview lists and methods.\n");

        System.out.println(Files.readString(notes));

        for (String line : Files.readAllLines(notes)) {
            System.out.println(line);
        }
        System.out.println(Files.readAllLines(notes).size());

        try (Stream<String> lines = Files.lines(notes)) {
            lines.map(String::toUpperCase).forEach(System.out::println);
        }

        Path missing = Path.of("missing_notes.txt");
        if (!Files.exists(missing)) {
            System.out.println("missing_notes.txt was not found.");
        }
    }
}
```

**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating reading from a file. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Leaving a stream open instead of using try-with-resources or ignoring IOException.
- Catching Exception broadly and hiding failures that should be reported or propagated.
- Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation.
### Activities
1. Read and write a temporary file, then verify the file content and clean up the resource.
2. Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions.
3. Explain which resources are closed by try-with-resources and which code executes in finally.
4. Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 8.2: Writing to a File

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of writing to a file.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops writing to a file through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. File APIs can fail with IOException; use Path and Files for common operations and try-with-resources for closeable streams. Catch only failures you can handle. JSON is not built into the Java SE standard library, so robust JSON parsing requires a documented external library such as Jackson or Gson.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_8_2 {
    public static void main(String[] args) {
        try {
            java.nio.file.Path file = java.nio.file.Files.createTempFile("java-write", ".txt");
            java.nio.file.Files.writeString(file, "Avery,92\\nRiley,85\\n");
            System.out.println(java.nio.file.Files.size(file) + " bytes written");
            java.nio.file.Files.deleteIfExists(file);
        } catch (java.io.IOException ex) { System.out.println(ex.getMessage()); }
    }
}
```

**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating writing to a file. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Leaving a stream open instead of using try-with-resources or ignoring IOException.
- Catching Exception broadly and hiding failures that should be reported or propagated.
- Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation.
### Activities
1. Read and write a temporary file, then verify the file content and clean up the resource.
2. Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions.
3. Explain which resources are closed by try-with-resources and which code executes in finally.
4. Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 8.3: Exceptions and Handling Errors

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of exceptions and handling errors.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops exceptions and handling errors through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. File APIs can fail with IOException; use Path and Files for common operations and try-with-resources for closeable streams. Catch only failures you can handle. JSON is not built into the Java SE standard library, so robust JSON parsing requires a documented external library such as Jackson or Gson.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_8_3 {
    public static void main(String[] args) {
        String raw = "not-a-number";
        try {
            int value = Integer.parseInt(raw);
            System.out.println(value);
        } catch (NumberFormatException ex) {
            System.out.println("Invalid integer: " + raw);
        }
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
raised on purpose
Cleanup runs either way.
```

### Common Mistakes
1. Catching `Exception` for everything, which hides mistakes in your own code.
2. Using `Integer.parseInt` on untrusted text without a catch.
3. Expecting `10.0 / 0` to throw. It gives `Infinity`.

### Activities
1. Predict each printed line before running.
2. Wrap `Integer.parseInt(scanner.nextLine())` so invalid input prints a clear message and asks again.
3. Catch `ArithmeticException` in a method that computes an average of an empty list.
4. Explain when to catch an exception and when to let it stop the program.

### Accessibility Practice

Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.' Read the exception's class name aloud when you see a stack trace, then jump to the first line that names your own file.

### Skills Checklist
- [ ] I can catch specific exceptions.
- [ ] I can use `finally` and multi-catch.
- [ ] I can explain checked versus unchecked.
- [ ] I know integer and decimal division by zero differ.
- [ ] I can write clear error messages.

---

## Lesson 8.4: Cleanup with try-with-resources

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 8.4: The else and finally Blocks

### Learning Objectives
- Close files reliably with try-with-resources.
- Show that a resource is released even after an error.
- Use `finally` for cleanup.

### Concept Explanation

A reader or writer holds a resource from the operating system, so it must be closed. *Try-with-resources* declares the resource in parentheses after `try`: `try (BufferedReader reader = ...) { ... }`. Java closes it automatically when the block ends, **even if the block throws an exception**. Since Java 9, an existing variable that is not reassigned can be listed too: `try (reader) { ... }`.

`finally` is the general tool: its block runs after the `try` block whether or not an exception happened. Use try-with-resources for anything that can be closed, and `finally` for other cleanup.

The example writes a file, reads it back, throws an exception inside a second block, and shows that a reader closed by try-with-resources refuses to read.

### Worked Example

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Lesson_8_4 {
    public static void main(String[] args) throws IOException {
        Path file = Path.of("cleanup_demo.txt");
        try (BufferedWriter writer = Files.newBufferedWriter(file)) {
            writer.write("Some data.\n");
        }
        System.out.println(Files.readString(file).trim());

        BufferedReader reader = Files.newBufferedReader(file);
        String firstLine;
        try (reader) {
            firstLine = reader.readLine();
        }
        System.out.println(firstLine);

        try (BufferedReader second = Files.newBufferedReader(file)) {
            second.readLine();
            throw new IllegalStateException("failure while reading");
        } catch (IllegalStateException e) {
            System.out.println(e.getMessage());
        }

        try {
            System.out.println("working");
        } finally {
            System.out.println("finally block ran");
        }

        boolean refused = false;
        try {
            reader.readLine();
        } catch (IOException e) {
            refused = true;
        }
        System.out.println(refused);
    }
}
```

**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating the catch, finally, and try-with-resources patterns. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Leaving a stream open instead of using try-with-resources or ignoring IOException.
- Catching Exception broadly and hiding failures that should be reported or propagated.
- Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation.
### Activities
1. Read and write a temporary file, then verify the file content and clean up the resource.
2. Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions.
3. Explain which resources are closed by try-with-resources and which code executes in finally.
4. Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 8.5: Storing Data with JSON

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- JSON specification: https://www.json.org
- Matching Python lesson: Lesson 8.5: Storing Data with JSON

### Learning Objectives
- Explain why this lesson includes a JSON helper.
- Encode and decode the shared task records.
- Handle a missing or malformed file.

### Concept Explanation

The Java standard library has no JSON support. Real projects add a library such as Jackson or Gson through Maven or Gradle. To keep this course free of build tooling, the example includes a *teaching implementation*, the nested class `Json`, with `encode` and `decode`. It handles strings, numbers, booleans, `null`, lists, and maps, writes object keys in sorted order, and reports malformed text with an exception that includes the position. It is not a replacement for a production library.

JSON text stores data in a standard format: `{ ... }` holds key-value pairs, `[ ... ]` holds ordered items, and text is in double quotation marks. Decoded data is untyped (`Map<String, Object>` and `List<Object>`), so check each field before using it. Numbers without a decimal point decode as `Long`.

The shared to-do record has the fields `id`, `title`, `description`, `done`, and `created_at`. The example saves two tasks, loads them back, and shows the message for a malformed file.

The teaching helper decodes JSON `null` as `null` and numbers without a decimal point as `Long`. It does not handle every number edge case that a full parser must.

### Worked Example

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class Lesson_8_5 {
    static final class Json {
        private Json() {}

        static String encode(Object value) {
            if (value == null) {
                return "null";
            }
            if (value instanceof String text) {
                return quote(text);
            }
            if (value instanceof Boolean || value instanceof Integer || value instanceof Long || value instanceof Double) {
                return value.toString();
            }
            if (value instanceof Map<?, ?> map) {
                List<String> keys = new ArrayList<>();
                for (Object key : map.keySet()) {
                    keys.add(key.toString());
                }
                Collections.sort(keys);
                StringBuilder out = new StringBuilder("{");
                for (int i = 0; i < keys.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(quote(keys.get(i))).append(':').append(encode(map.get(keys.get(i))));
                }
                return out.append('}').toString();
            }
            if (value instanceof List<?> list) {
                StringBuilder out = new StringBuilder("[");
                for (int i = 0; i < list.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(encode(list.get(i)));
                }
                return out.append(']').toString();
            }
            throw new IllegalArgumentException("cannot encode " + value.getClass().getSimpleName());
        }

        private static String quote(String text) {
            StringBuilder out = new StringBuilder("\"");
            for (char c : text.toCharArray()) {
                switch (c) {
                    case '"' -> out.append("\\\"");
                    case '\\' -> out.append("\\\\");
                    case '\n' -> out.append("\\n");
                    case '\r' -> out.append("\\r");
                    case '\t' -> out.append("\\t");
                    default -> {
                        if (c < ' ') {
                            out.append(String.format("\\u%04x", (int) c));
                        } else {
                            out.append(c);
                        }
                    }
                }
            }
            return out.append('"').toString();
        }

        static Object decode(String text) {
            Parser parser = new Parser(text);
            Object result = parser.value();
            parser.skip();
            if (parser.pos < text.length()) {
                throw parser.fail("unexpected extra text");
            }
            return result;
        }

        private static final class Parser {
            private final String text;
            private int pos = 0;

            Parser(String text) {
                this.text = text;
            }

            IllegalArgumentException fail(String message) {
                return new IllegalArgumentException(message + " at position " + pos);
            }

            void skip() {
                while (pos < text.length() && Character.isWhitespace(text.charAt(pos))) {
                    pos++;
                }
            }

            Object value() {
                skip();
                if (pos >= text.length()) {
                    throw fail("unexpected end of text");
                }
                char c = text.charAt(pos);
                if (c == '{') return object();
                if (c == '[') return list();
                if (c == '"') return string();
                if (text.startsWith("true", pos)) { pos += 4; return Boolean.TRUE; }
                if (text.startsWith("false", pos)) { pos += 5; return Boolean.FALSE; }
                if (text.startsWith("null", pos)) { pos += 4; return null; }
                if (c == '-' || Character.isDigit(c)) return number();
                throw fail("unexpected character");
            }

            Object number() {
                int start = pos;
                if (text.charAt(pos) == '-') {
                    pos++;
                }
                while (pos < text.length() && (Character.isDigit(text.charAt(pos)) || ".eE+-".indexOf(text.charAt(pos)) >= 0)) {
                    pos++;
                }
                String token = text.substring(start, pos);
                try {
                    return Long.parseLong(token);
                } catch (NumberFormatException notWhole) {
                    try {
                        return Double.parseDouble(token);
                    } catch (NumberFormatException notNumber) {
                        throw fail("bad number");
                    }
                }
            }

            String string() {
                pos++;
                StringBuilder out = new StringBuilder();
                while (true) {
                    if (pos >= text.length()) {
                        throw fail("unterminated string");
                    }
                    char c = text.charAt(pos++);
                    if (c == '"') {
                        return out.toString();
                    }
                    if (c != '\\') {
                        out.append(c);
                        continue;
                    }
                    if (pos >= text.length()) {
                        throw fail("bad escape");
                    }
                    char e = text.charAt(pos++);
                    switch (e) {
                        case 'n' -> out.append('\n');
                        case 't' -> out.append('\t');
                        case 'r' -> out.append('\r');
                        case '"' -> out.append('"');
                        case '\\' -> out.append('\\');
                        case '/' -> out.append('/');
                        case 'u' -> {
                            if (pos + 4 > text.length()) {
                                throw fail("bad escape");
                            }
                            out.append((char) Integer.parseInt(text.substring(pos, pos + 4), 16));
                            pos += 4;
                        }
                        default -> throw fail("bad escape");
                    }
                }
            }

            Map<String, Object> object() {
                pos++;
                Map<String, Object> map = new LinkedHashMap<>();
                skip();
                if (pos < text.length() && text.charAt(pos) == '}') {
                    pos++;
                    return map;
                }
                while (true) {
                    skip();
                    if (pos >= text.length() || text.charAt(pos) != '"') {
                        throw fail("expected a key");
                    }
                    String key = string();
                    skip();
                    if (pos >= text.length() || text.charAt(pos) != ':') {
                        throw fail("expected ':'");
                    }
                    pos++;
                    map.put(key, value());
                    skip();
                    if (pos >= text.length()) {
                        throw fail("unterminated object");
                    }
                    char d = text.charAt(pos++);
                    if (d == '}') {
                        return map;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail("expected ',' or '}'");
                    }
                }
            }

            List<Object> list() {
                pos++;
                List<Object> items = new ArrayList<>();
                skip();
                if (pos < text.length() && text.charAt(pos) == ']') {
                    pos++;
                    return items;
                }
                while (true) {
                    items.add(value());
                    skip();
                    if (pos >= text.length()) {
                        throw fail("unterminated list");
                    }
                    char d = text.charAt(pos++);
                    if (d == ']') {
                        return items;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail("expected ',' or ']'");
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        List<Map<String, Object>> tasks = List.of(
            Map.of("id", 1, "title", "Study programming", "description", "Finish Unit 8",
                "done", false, "created_at", "2026-01-15T09:00:00"),
            Map.of("id", 2, "title", "Review scores", "description", "Check the four scores",
                "done", true, "created_at", "2026-01-15T09:30:00"));

        Path file = Path.of("tasks.json");
        Files.writeString(file, Json.encode(tasks));

        if (!Files.exists(file)) {
            System.out.println("Tasks file not found.");
            return;
        }
        List<?> loaded;
        try {
            loaded = (List<?>) Json.decode(Files.readString(file));
        } catch (IllegalArgumentException e) {
            System.out.println("Error: could not decode tasks file: " + e.getMessage());
            return;
        }
        for (Object entry : loaded) {
            Map<?, ?> task = (Map<?, ?>) entry;
            String status = Boolean.TRUE.equals(task.get("done")) ? "done" : "not done";
            System.out.println(task.get("id") + ": " + task.get("title") + " (" + status + ")");
        }

        try {
            Json.decode("[{\"id\": 1,");
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating storing data with json. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Leaving a stream open instead of using try-with-resources or ignoring IOException.
- Catching Exception broadly and hiding failures that should be reported or propagated.
- Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation.
### Activities
1. Read and write a temporary file, then verify the file content and clean up the resource.
2. Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions.
3. Explain which resources are closed by try-with-resources and which code executes in finally.
4. Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.
