[Header 2 ("unit-8-files-and-exceptions", [], []) [Str "Unit 8: Files and Exceptions"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops files and exceptions through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing."], Para [Strong [Str "Unit objectives:"], Str " explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects."], Header 3 ("lesson-81-reading-from-a-file", ["unnumbered", "unlisted"], []) [Str "Lesson 8.1: Reading from a File"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 8.1: Reading from a File"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Read a whole file and read it line by line."]], [Plain [Str "Check that a file exists before reading."]], [Plain [Str "Report a missing file clearly."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "java.nio.file.Path", Str " represents a location and ", Code ("", [], []) "java.nio.file.Files", Str " does the work. ", Code ("", [], []) "Files.readString(path)", Str " returns the whole file, ", Code ("", [], []) "Files.readAllLines(path)", Str " returns a list of lines, and ", Code ("", [], []) "Files.lines(path)", Str " returns a ", Emph [Str "stream"], Str " of lines that must be closed, so it is used in try-with-resources. ", Code ("", [], []) "Files.exists(path)", Str " tests whether a file is there. A relative path such as ", Code ("", [], []) "notes.txt", Str " starts from the program's working directory."], Para [Str "Most file methods throw the ", Emph [Str "checked"], Str " exception ", Code ("", [], []) "IOException", Str ", which the compiler forces you to handle: either catch it or declare ", Code ("", [], []) "throws IOException", Str " on the method. A missing file throws a ", Code ("", [], []) "NoSuchFileException", Str "."], Para [Str "To keep the lesson self-contained, the example first writes the two-line ", Code ("", [], []) "notes.txt", Str " that every language track uses, then reads it three ways and checks a file that does not exist."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.Stream;

public class Lesson_8_1 {
    public static void main(String[] args) throws IOException {
        Path notes = Path.of(\"notes.txt\");
        Files.writeString(notes, \"Practice Java.\\nReview lists and methods.\\n\");

        System.out.println(Files.readString(notes));

        for (String line : Files.readAllLines(notes)) {
            System.out.println(line);
        }
        System.out.println(Files.readAllLines(notes).size());

        try (Stream<String> lines = Files.lines(notes)) {
            lines.map(String::toUpperCase).forEach(System.out::println);
        }

        Path missing = Path.of(\"missing_notes.txt\");
        if (!Files.exists(missing)) {
            System.out.println(\"missing_notes.txt was not found.\");
        }
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating reading from a file. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Leaving a stream open instead of using try-with-resources or ignoring IOException."]], [Plain [Str "Catching Exception broadly and hiding failures that should be reported or propagated."]], [Plain [Str "Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Read and write a temporary file, then verify the file content and clean up the resource."]], [Plain [Str "Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions."]], [Plain [Str "Explain which resources are closed by try-with-resources and which code executes in finally."]], [Plain [Str "Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]], Header 3 ("lesson-82-writing-to-a-file", ["unnumbered", "unlisted"], []) [Str "Lesson 8.2: Writing to a File"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 documentation"] ("https://docs.oracle.com/en/java/", ""), Str "."]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", ""), Str "."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the purpose and vocabulary of writing to a file."]], [Plain [Str "Apply the relevant Java syntax and APIs in a small, complete program."]], [Plain [Str "Compile, run, inspect, and adapt the example using keyboard-accessible tools."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "This lesson develops writing to a file through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. File APIs can fail with IOException; use Path and Files for common operations and try-with-resources for closeable streams. Catch only failures you can handle. JSON is not built into the Java SE standard library, so robust JSON parsing requires a documented external library such as Jackson or Gson."], Para [Str "Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "public class Lesson_8_2 {
    public static void main(String[] args) {
        try {
            java.nio.file.Path file = java.nio.file.Files.createTempFile(\"java-write\", \".txt\");
            java.nio.file.Files.writeString(file, \"Avery,92\\\\nRiley,85\\\\n\");
            System.out.println(java.nio.file.Files.size(file) + \" bytes written\");
            java.nio.file.Files.deleteIfExists(file);
        } catch (java.io.IOException ex) { System.out.println(ex.getMessage()); }
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating writing to a file. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Leaving a stream open instead of using try-with-resources or ignoring IOException."]], [Plain [Str "Catching Exception broadly and hiding failures that should be reported or propagated."]], [Plain [Str "Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Read and write a temporary file, then verify the file content and clean up the resource."]], [Plain [Str "Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions."]], [Plain [Str "Explain which resources are closed by try-with-resources and which code executes in finally."]], [Plain [Str "Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]], Header 3 ("lesson-83-exceptions-and-handling-errors", ["unnumbered", "unlisted"], []) [Str "Lesson 8.3: Exceptions and Handling Errors"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 documentation"] ("https://docs.oracle.com/en/java/", ""), Str "."]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", ""), Str "."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the purpose and vocabulary of exceptions and handling errors."]], [Plain [Str "Apply the relevant Java syntax and APIs in a small, complete program."]], [Plain [Str "Compile, run, inspect, and adapt the example using keyboard-accessible tools."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "This lesson develops exceptions and handling errors through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. File APIs can fail with IOException; use Path and Files for common operations and try-with-resources for closeable streams. Catch only failures you can handle. JSON is not built into the Java SE standard library, so robust JSON parsing requires a documented external library such as Jackson or Gson."], Para [Str "Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "public class Lesson_8_3 {
    public static void main(String[] args) {
        String raw = \"not-a-number\";
        try {
            int value = Integer.parseInt(raw);
            System.out.println(value);
        } catch (NumberFormatException ex) {
            System.out.println(\"Invalid integer: \" + raw);
        }
    }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score.
Error: / by zero
Infinity
raised on purpose
Cleanup runs either way.
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Catching ", Code ("", [], []) "Exception", Str " for everything, which hides mistakes in your own code."]], [Plain [Str "Using ", Code ("", [], []) "Integer.parseInt", Str " on untrusted text without a catch."]], [Plain [Str "Expecting ", Code ("", [], []) "10.0 / 0", Str " to throw. It gives ", Code ("", [], []) "Infinity", Str "."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict each printed line before running."]], [Plain [Str "Wrap ", Code ("", [], []) "Integer.parseInt(scanner.nextLine())", Str " so invalid input prints a clear message and asks again."]], [Plain [Str "Catch ", Code ("", [], []) "ArithmeticException", Str " in a method that computes an average of an empty list."]], [Plain [Str "Explain when to catch an exception and when to let it stop the program."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.' Read the exception's class name aloud when you see a stack trace, then jump to the first line that names your own file."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can catch specific exceptions."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "finally", Str " and multi-catch."]], [Plain [Str "\9744", Space, Str "I can explain checked versus unchecked."]], [Plain [Str "\9744", Space, Str "I know integer and decimal division by zero differ."]], [Plain [Str "\9744", Space, Str "I can write clear error messages."]]], HorizontalRule, Header 3 ("lesson-84-cleanup-with-try-with-resources", ["unnumbered", "unlisted"], []) [Str "Lesson 8.4: Cleanup with try-with-resources"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 8.4: The else and finally Blocks"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Close files reliably with try-with-resources."]], [Plain [Str "Show that a resource is released even after an error."]], [Plain [Str "Use ", Code ("", [], []) "finally", Str " for cleanup."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A reader or writer holds a resource from the operating system, so it must be closed. ", Emph [Str "Try-with-resources"], Str " declares the resource in parentheses after ", Code ("", [], []) "try", Str ": ", Code ("", [], []) "try (BufferedReader reader = ...) { ... }", Str ". Java closes it automatically when the block ends, ", Strong [Str "even if the block throws an exception"], Str ". Since Java 9, an existing variable that is not reassigned can be listed too: ", Code ("", [], []) "try (reader) { ... }", Str "."], Para [Code ("", [], []) "finally", Str " is the general tool: its block runs after the ", Code ("", [], []) "try", Str " block whether or not an exception happened. Use try-with-resources for anything that can be closed, and ", Code ("", [], []) "finally", Str " for other cleanup."], Para [Str "The example writes a file, reads it back, throws an exception inside a second block, and shows that a reader closed by try-with-resources refuses to read."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Lesson_8_4 {
    public static void main(String[] args) throws IOException {
        Path file = Path.of(\"cleanup_demo.txt\");
        try (BufferedWriter writer = Files.newBufferedWriter(file)) {
            writer.write(\"Some data.\\n\");
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
            throw new IllegalStateException(\"failure while reading\");
        } catch (IllegalStateException e) {
            System.out.println(e.getMessage());
        }

        try {
            System.out.println(\"working\");
        } finally {
            System.out.println(\"finally block ran\");
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
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating the catch, finally, and try-with-resources patterns. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Leaving a stream open instead of using try-with-resources or ignoring IOException."]], [Plain [Str "Catching Exception broadly and hiding failures that should be reported or propagated."]], [Plain [Str "Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Read and write a temporary file, then verify the file content and clean up the resource."]], [Plain [Str "Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions."]], [Plain [Str "Explain which resources are closed by try-with-resources and which code executes in finally."]], [Plain [Str "Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]], Header 3 ("lesson-85-storing-data-with-json", ["unnumbered", "unlisted"], []) [Str "Lesson 8.5: Storing Data with JSON"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Str "JSON specification: https://www.json.org"]], [Plain [Str "Matching Python lesson: Lesson 8.5: Storing Data with JSON"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain why this lesson includes a JSON helper."]], [Plain [Str "Encode and decode the shared task records."]], [Plain [Str "Handle a missing or malformed file."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The Java standard library has no JSON support. Real projects add a library such as Jackson or Gson through Maven or Gradle. To keep this course free of build tooling, the example includes a ", Emph [Str "teaching implementation"], Str ", the nested class ", Code ("", [], []) "Json", Str ", with ", Code ("", [], []) "encode", Str " and ", Code ("", [], []) "decode", Str ". It handles strings, numbers, booleans, ", Code ("", [], []) "null", Str ", lists, and maps, writes object keys in sorted order, and reports malformed text with an exception that includes the position. It is not a replacement for a production library."], Para [Str "JSON text stores data in a standard format: ", Code ("", [], []) "{ ... }", Str " holds key-value pairs, ", Code ("", [], []) "[ ... ]", Str " holds ordered items, and text is in double quotation marks. Decoded data is untyped (", Code ("", [], []) "Map<String, Object>", Str " and ", Code ("", [], []) "List<Object>", Str "), so check each field before using it. Numbers without a decimal point decode as ", Code ("", [], []) "Long", Str "."], Para [Str "The shared to-do record has the fields ", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "done", Str ", and ", Code ("", [], []) "created_at", Str ". The example saves two tasks, loads them back, and shows the message for a malformed file."], Para [Str "The teaching helper decodes JSON ", Code ("", [], []) "null", Str " as ", Code ("", [], []) "null", Str " and numbers without a decimal point as ", Code ("", [], []) "Long", Str ". It does not handle every number edge case that a full parser must."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class Lesson_8_5 {
    static final class Json {
        private Json() {}

        static String encode(Object value) {
            if (value == null) {
                return \"null\";
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
                StringBuilder out = new StringBuilder(\"{\");
                for (int i = 0; i < keys.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(quote(keys.get(i))).append(':').append(encode(map.get(keys.get(i))));
                }
                return out.append('}').toString();
            }
            if (value instanceof List<?> list) {
                StringBuilder out = new StringBuilder(\"[\");
                for (int i = 0; i < list.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(encode(list.get(i)));
                }
                return out.append(']').toString();
            }
            throw new IllegalArgumentException(\"cannot encode \" + value.getClass().getSimpleName());
        }

        private static String quote(String text) {
            StringBuilder out = new StringBuilder(\"\\\"\");
            for (char c : text.toCharArray()) {
                switch (c) {
                    case '\"' -> out.append(\"\\\\\\\"\");
                    case '\\\\' -> out.append(\"\\\\\\\\\");
                    case '\\n' -> out.append(\"\\\\n\");
                    case '\\r' -> out.append(\"\\\\r\");
                    case '\\t' -> out.append(\"\\\\t\");
                    default -> {
                        if (c < ' ') {
                            out.append(String.format(\"\\\\u%04x\", (int) c));
                        } else {
                            out.append(c);
                        }
                    }
                }
            }
            return out.append('\"').toString();
        }

        static Object decode(String text) {
            Parser parser = new Parser(text);
            Object result = parser.value();
            parser.skip();
            if (parser.pos < text.length()) {
                throw parser.fail(\"unexpected extra text\");
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
                return new IllegalArgumentException(message + \" at position \" + pos);
            }

            void skip() {
                while (pos < text.length() && Character.isWhitespace(text.charAt(pos))) {
                    pos++;
                }
            }

            Object value() {
                skip();
                if (pos >= text.length()) {
                    throw fail(\"unexpected end of text\");
                }
                char c = text.charAt(pos);
                if (c == '{') return object();
                if (c == '[') return list();
                if (c == '\"') return string();
                if (text.startsWith(\"true\", pos)) { pos += 4; return Boolean.TRUE; }
                if (text.startsWith(\"false\", pos)) { pos += 5; return Boolean.FALSE; }
                if (text.startsWith(\"null\", pos)) { pos += 4; return null; }
                if (c == '-' || Character.isDigit(c)) return number();
                throw fail(\"unexpected character\");
            }

            Object number() {
                int start = pos;
                if (text.charAt(pos) == '-') {
                    pos++;
                }
                while (pos < text.length() && (Character.isDigit(text.charAt(pos)) || \".eE+-\".indexOf(text.charAt(pos)) >= 0)) {
                    pos++;
                }
                String token = text.substring(start, pos);
                try {
                    return Long.parseLong(token);
                } catch (NumberFormatException notWhole) {
                    try {
                        return Double.parseDouble(token);
                    } catch (NumberFormatException notNumber) {
                        throw fail(\"bad number\");
                    }
                }
            }

            String string() {
                pos++;
                StringBuilder out = new StringBuilder();
                while (true) {
                    if (pos >= text.length()) {
                        throw fail(\"unterminated string\");
                    }
                    char c = text.charAt(pos++);
                    if (c == '\"') {
                        return out.toString();
                    }
                    if (c != '\\\\') {
                        out.append(c);
                        continue;
                    }
                    if (pos >= text.length()) {
                        throw fail(\"bad escape\");
                    }
                    char e = text.charAt(pos++);
                    switch (e) {
                        case 'n' -> out.append('\\n');
                        case 't' -> out.append('\\t');
                        case 'r' -> out.append('\\r');
                        case '\"' -> out.append('\"');
                        case '\\\\' -> out.append('\\\\');
                        case '/' -> out.append('/');
                        case 'u' -> {
                            if (pos + 4 > text.length()) {
                                throw fail(\"bad escape\");
                            }
                            out.append((char) Integer.parseInt(text.substring(pos, pos + 4), 16));
                            pos += 4;
                        }
                        default -> throw fail(\"bad escape\");
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
                    if (pos >= text.length() || text.charAt(pos) != '\"') {
                        throw fail(\"expected a key\");
                    }
                    String key = string();
                    skip();
                    if (pos >= text.length() || text.charAt(pos) != ':') {
                        throw fail(\"expected ':'\");
                    }
                    pos++;
                    map.put(key, value());
                    skip();
                    if (pos >= text.length()) {
                        throw fail(\"unterminated object\");
                    }
                    char d = text.charAt(pos++);
                    if (d == '}') {
                        return map;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail(\"expected ',' or '}'\");
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
                        throw fail(\"unterminated list\");
                    }
                    char d = text.charAt(pos++);
                    if (d == ']') {
                        return items;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail(\"expected ',' or ']'\");
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        List<Map<String, Object>> tasks = List.of(
            Map.of(\"id\", 1, \"title\", \"Study programming\", \"description\", \"Finish Unit 8\",
                \"done\", false, \"created_at\", \"2026-01-15T09:00:00\"),
            Map.of(\"id\", 2, \"title\", \"Review scores\", \"description\", \"Check the four scores\",
                \"done\", true, \"created_at\", \"2026-01-15T09:30:00\"));

        Path file = Path.of(\"tasks.json\");
        Files.writeString(file, Json.encode(tasks));

        if (!Files.exists(file)) {
            System.out.println(\"Tasks file not found.\");
            return;
        }
        List<?> loaded;
        try {
            loaded = (List<?>) Json.decode(Files.readString(file));
        } catch (IllegalArgumentException e) {
            System.out.println(\"Error: could not decode tasks file: \" + e.getMessage());
            return;
        }
        for (Object entry : loaded) {
            Map<?, ?> task = (Map<?, ?>) entry;
            String status = Boolean.TRUE.equals(task.get(\"done\")) ? \"done\" : \"not done\";
            System.out.println(task.get(\"id\") + \": \" + task.get(\"title\") + \" (\" + status + \")\");
        }

        try {
            Json.decode(\"[{\\\"id\\\": 1,\");
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating storing data with json. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Leaving a stream open instead of using try-with-resources or ignoring IOException."]], [Plain [Str "Catching Exception broadly and hiding failures that should be reported or propagated."]], [Plain [Str "Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Read and write a temporary file, then verify the file content and clean up the resource."]], [Plain [Str "Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions."]], [Plain [Str "Explain which resources are closed by try-with-resources and which code executes in finally."]], [Plain [Str "Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]]]