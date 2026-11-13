[Header 2 ("unit-11-capstone--accessible-personal-data-manager", [], []) [Str "Unit 11: Capstone — Accessible Personal Data Manager"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops capstone — accessible personal data manager through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing."], Para [Strong [Str "Unit objectives:"], Str " explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects."], Header 3 ("lesson-111-capstone-requirements-and-design", ["unnumbered", "unlisted"], []) [Str "Lesson 11.1: Capstone: Requirements and Design"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 11.1: Introduction to NiceGUI (capstone planning)"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write requirements for a personal data manager."]], [Plain [Str "Define the shared record schema as a Java record."]], [Plain [Str "Check records against the validation rules before building features."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The capstone is a ", Emph [Str "personal data manager"], Str ": a program that keeps a list of records, lets the user add, view, search, change, complete, and delete them, and saves them to a file. In the Java track it is a text program, so it runs from the terminal and is fully usable with a screen reader or braille display."], Para [Strong [Str "Shared record schema (all general-purpose language tracks)."], Str " Every record has ", Code ("", [], []) "id", Str " (unique whole number), ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "category", Str ", ", Code ("", [], []) "created_at", Str ", and ", Code ("", [], []) "updated_at", Str " (ISO 8601 text). A project may add fields, such as an optional ", Code ("", [], []) "done", Str " flag, but must not remove these. Java names use camel case (", Code ("", [], []) "createdAt", Str "), and the stored JSON uses the shared names. The class is called ", Code ("", [], []) "Entry", Str " here, because ", Code ("", [], []) "Record", Str " would hide ", Code ("", [], []) "java.lang.Record", Str ", the parent of all records."], Para [Strong [Str "Validation rules."], Str " A record must have a non-empty title and a non-empty category. Timestamps are ISO 8601 text such as ", Code ("", [], []) "2026-01-15T09:00:00", Str "."], Para [Str "Design before coding: list the operations, then the data, then the messages. The example checks the three shared sample records against the rules and prints them as a plain-text list."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.List;

public class Lesson_11_1 {
    record Entry(int id, String title, String description, String category, String createdAt, String updatedAt) {}

    static String validate(String title, String category) {
        if (title == null || title.isBlank()) {
            return \"A title is required.\";
        }
        if (category == null || category.isBlank()) {
            return \"A category is required.\";
        }
        return null;
    }

    public static void main(String[] args) {
        List<Entry> sample = List.of(
            new Entry(1, \"Notebook\", \"Course notes\", \"supplies\", \"2026-01-15T09:00:00\", \"2026-01-15T09:00:00\"),
            new Entry(2, \"Pencil\", \"Box of 10\", \"supplies\", \"2026-01-15T09:05:00\", \"2026-01-15T09:05:00\"),
            new Entry(3, \"Study plan\", \"Weekly schedule\", \"planning\", \"2026-01-15T09:10:00\", \"2026-01-15T09:10:00\"));

        for (Entry entry : sample) {
            String problem = validate(entry.title(), entry.category());
            System.out.println(entry.id() + \". \" + entry.title() + \" [\" + entry.category() + \"] - \"
                + (problem == null ? \"valid\" : problem));
        }

        System.out.println(validate(\"  \", \"supplies\"));
        System.out.println(validate(\"Ruler\", \"\"));
    }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "1. Notebook [supplies] - valid
2. Pencil [supplies] - valid
3. Study plan [planning] - valid
A title is required.
A category is required.
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Starting to build features before agreeing on the record fields."]], [Plain [Str "Allowing a record with an empty title because the check was left for later."]], [Plain [Str "Storing timestamps in different formats in different places."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write the seven operations as a numbered list of requirements."]], [Plain [Str "Add one project-specific field and say how it is validated."]], [Plain [Str "Write three sample records for your own project."]], [Plain [Str "Describe in plain sentences what each shared field means."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Design the screen output as lines of plain text: one record per line, with the same field order each time. Decide the wording of every message now so that it can be tested."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write requirements."]], [Plain [Str "\9744", Space, Str "I know the shared record fields."]], [Plain [Str "\9744", Space, Str "I can write validation rules."]], [Plain [Str "\9744", Space, Str "I can describe sample data."]], [Plain [Str "\9744", Space, Str "I can plan messages before coding."]]], HorizontalRule, Header 3 ("lesson-112-capstone-data-model-and-storage", ["unnumbered", "unlisted"], []) [Str "Lesson 11.2: Capstone: Data Model and Storage"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 11.2: Data Model and Storage"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Store records as record objects."]], [Plain [Str "Save and load them as JSON."]], [Plain [Str "Confirm that every field survives a round trip."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Records are stored as a list of Java records in memory and as a JSON array on disk. The storage layer has two methods: ", Code ("", [], []) "saveEntries(path, entries)", Str " and ", Code ("", [], []) "loadEntries(path)", Str ". Loading returns a small record holding the entries and a message, so the caller decides what to do when the file is missing or damaged."], Para [Str "An ", Code ("", [], []) "Entry", Str " is converted to a map for saving (", Code ("", [], []) "toMap", Str ") and rebuilt from a decoded map when loading (", Code ("", [], []) "toEntry", Str "), which checks that each field is present and has the right type. The optional ", Code ("", [], []) "done", Str " field defaults to ", Code ("", [], []) "false", Str "."], Para [Str "The example uses the teaching JSON helper from Lesson 8.5 (included so the program runs on its own). After saving and reloading it compares the lists; records compare by value, so this ", Emph [Str "round-trip test"], Str " checks every field of every entry. It is the first acceptance test for storage."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class Lesson_11_2 {
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

    record Entry(int id, String title, String description, String category,
                 String createdAt, String updatedAt, boolean done) {}

    record Loaded(List<Entry> entries, String problem) {}

    static Map<String, Object> toMap(Entry entry) {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put(\"id\", entry.id());
        map.put(\"title\", entry.title());
        map.put(\"description\", entry.description());
        map.put(\"category\", entry.category());
        map.put(\"created_at\", entry.createdAt());
        map.put(\"updated_at\", entry.updatedAt());
        map.put(\"done\", entry.done());
        return map;
    }

    static String text(Map<?, ?> map, String key) {
        if (!(map.get(key) instanceof String value)) {
            throw new IllegalArgumentException(\"missing field \" + key);
        }
        return value;
    }

    static Entry toEntry(Object raw) {
        if (!(raw instanceof Map<?, ?> map)) {
            throw new IllegalArgumentException(\"a record must be an object\");
        }
        if (!(map.get(\"id\") instanceof Long id)) {
            throw new IllegalArgumentException(\"missing field id\");
        }
        boolean done = map.get(\"done\") instanceof Boolean flag && flag;
        return new Entry(id.intValue(), text(map, \"title\"), text(map, \"description\"), text(map, \"category\"),
            text(map, \"created_at\"), text(map, \"updated_at\"), done);
    }

    static void saveEntries(Path path, List<Entry> entries) throws IOException {
        List<Object> maps = new ArrayList<>();
        for (Entry entry : entries) {
            maps.add(toMap(entry));
        }
        Files.writeString(path, Json.encode(maps));
    }

    static Loaded loadEntries(Path path) throws IOException {
        if (!Files.exists(path)) {
            return new Loaded(List.of(), \"Could not open \" + path + \": file not found.\");
        }
        try {
            List<Entry> entries = new ArrayList<>();
            for (Object raw : (List<?>) Json.decode(Files.readString(path))) {
                entries.add(toEntry(raw));
            }
            return new Loaded(entries, null);
        } catch (IllegalArgumentException | ClassCastException e) {
            return new Loaded(List.of(), \"The data file is not valid: \" + e.getMessage());
        }
    }

    public static void main(String[] args) throws IOException {
        List<Entry> sample = List.of(
            new Entry(1, \"Notebook\", \"Course notes\", \"supplies\", \"2026-01-15T09:00:00\", \"2026-01-15T09:00:00\", false),
            new Entry(2, \"Pencil\", \"Box of 10\", \"supplies\", \"2026-01-15T09:05:00\", \"2026-01-15T09:05:00\", false),
            new Entry(3, \"Study plan\", \"Weekly schedule\", \"planning\", \"2026-01-15T09:10:00\", \"2026-01-15T09:10:00\", false));

        Path file = Path.of(\"records.json\");
        saveEntries(file, sample);
        Loaded loaded = loadEntries(file);
        System.out.println(\"Round trip preserved all fields: \" + loaded.entries().equals(sample));
        System.out.println(\"Records loaded: \" + loaded.entries().size());
        System.out.println(loaded.problem());

        System.out.println(loadEntries(Path.of(\"missing.json\")).problem());

        Files.writeString(Path.of(\"broken.json\"), \"[{\\\"id\\\": 1,\");
        System.out.println(loadEntries(Path.of(\"broken.json\")).problem());
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Round trip preserved all fields: true
Records loaded: 3
null
Could not open missing.json: file not found.
The data file is not valid: expected a key at position 10
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Overwriting the data file with an empty list after a failed load."]], [Plain [Str "Saving only some of the fields."]], [Plain [Str "Assuming a loaded record has every field without checking."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program and open ", Code ("", [], []) "records.json", Str " to read the saved text."]], [Plain [Str "Add a field to ", Code ("", [], []) "Entry", Str ", save it, and confirm that it survives the round trip."]], [Plain [Str "Make ", Code ("", [], []) "toEntry", Str " reject a record whose title is blank."]], [Plain [Str "Explain why ", Code ("", [], []) "loadEntries", Str " returns a message and does not throw."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Messages that name the file and the problem read clearly in speech. After saving, read the file in the terminal to confirm it contains what you expect."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can store records in record objects."]], [Plain [Str "\9744", Space, Str "I can save and load JSON."]], [Plain [Str "\9744", Space, Str "I can run a round-trip test."]], [Plain [Str "\9744", Space, Str "I handle missing and damaged files."]], [Plain [Str "\9744", Space, Str "I do not overwrite good data after a failed load."]]], HorizontalRule, Header 3 ("lesson-113-capstone-core-operations", ["unnumbered", "unlisted"], []) [Str "Lesson 11.3: Capstone: Core Operations"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 11.3: Displaying and Managing Items"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Add, list, search, change, complete, and delete records."]], [Plain [Str "Assign new ids and update timestamps correctly."]], [Plain [Str "Return a message when an operation cannot be done."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Code ("", [], []) "Manager", Str " class holds the entries and offers one method per operation. Each method that can fail returns an ", Code ("", [], []) "Outcome", Str " (the entry and a message) or a message, so the user interface can show it and decide what to do. New ids are one more than the highest id, so ids are never reused while higher ids exist. Updating an entry sets ", Code ("", [], []) "updatedAt", Str " but never changes ", Code ("", [], []) "createdAt", Str ", which is ", Code ("", [], []) "final", Str ". Completing an entry sets the optional ", Code ("", [], []) "done", Str " field to ", Code ("", [], []) "true", Str " and counts as an update."], Para [Str "For repeatable output the example passes in a ", Emph [Str "fake clock"], Str " that returns a new fixed time on each call. A real program passes a supplier that reads the real time."], Para [Str "The example adds the three shared sample records, lists them, searches for \"note\", changes one description, completes one entry, deletes one, and tries to delete an entry that does not exist."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.*;
import java.util.function.Supplier;

class Entry {
    final int id;
    String title;
    String description;
    String category;
    final String createdAt;
    String updatedAt;
    boolean done;

    Entry(int id, String title, String description, String category, String createdAt) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.category = category;
        this.createdAt = createdAt;
        this.updatedAt = createdAt;
        this.done = false;
    }

    String describe() {
        return id + \". \" + title + \" [\" + category + \"] (\" + (done ? \"done\" : \"not done\") + \")\";
    }
}

record Outcome(Entry entry, String message) {}

class Clocks {
    static Supplier<String> fake() {
        int[] ticks = {0};
        return () -> {
            ticks[0]++;
            return String.format(\"2026-01-15T10:00:%02d\", ticks[0]);
        };
    }
}

class Manager {
    final List<Entry> entries = new ArrayList<>();
    private final Supplier<String> clock;

    Manager(Supplier<String> clock) {
        this.clock = clock;
    }

    static String validate(String title, String category) {
        if (title == null || title.isBlank()) {
            return \"A title is required.\";
        }
        if (category == null || category.isBlank()) {
            return \"A category is required.\";
        }
        return null;
    }

    private int nextId() {
        int highest = 0;
        for (Entry entry : entries) {
            highest = Math.max(highest, entry.id);
        }
        return highest + 1;
    }

    Entry find(int id) {
        for (Entry entry : entries) {
            if (entry.id == id) {
                return entry;
            }
        }
        return null;
    }

    Outcome add(String title, String description, String category) {
        String problem = validate(title, category);
        if (problem != null) {
            return new Outcome(null, problem);
        }
        Entry entry = new Entry(nextId(), title.strip(), description.strip(), category.strip(), clock.get());
        entries.add(entry);
        return new Outcome(entry, null);
    }

    Outcome update(int id, String title, String description, String category, Boolean done) {
        Entry entry = find(id);
        if (entry == null) {
            return new Outcome(null, \"No record has that id.\");
        }
        String problem = validate(title != null ? title : entry.title, category != null ? category : entry.category);
        if (problem != null) {
            return new Outcome(null, problem);
        }
        if (title != null) entry.title = title.strip();
        if (description != null) entry.description = description.strip();
        if (category != null) entry.category = category.strip();
        if (done != null) entry.done = done;
        entry.updatedAt = clock.get();
        return new Outcome(entry, null);
    }

    Outcome complete(int id) {
        return update(id, null, null, null, true);
    }

    String delete(int id) {
        Entry entry = find(id);
        if (entry == null) {
            return \"No record has that id.\";
        }
        entries.remove(entry);
        return null;
    }

    List<Entry> search(String text) {
        String needle = text.strip().toLowerCase();
        List<Entry> found = new ArrayList<>();
        for (Entry entry : entries) {
            if (entry.title.toLowerCase().contains(needle) || entry.description.toLowerCase().contains(needle)) {
                found.add(entry);
            }
        }
        return found;
    }
}

public class Lesson_11_3 {
    static void show(Manager manager) {
        for (Entry entry : manager.entries) {
            System.out.println(entry.describe());
        }
    }

    public static void main(String[] args) {
        Manager manager = new Manager(Clocks.fake());
        manager.add(\"Notebook\", \"Course notes\", \"supplies\");
        manager.add(\"Pencil\", \"Box of 10\", \"supplies\");
        manager.add(\"Study plan\", \"Weekly schedule\", \"planning\");
        show(manager);

        System.out.println(\"Search for 'note':\");
        for (Entry entry : manager.search(\"note\")) {
            System.out.println(entry.title);
        }

        manager.update(2, null, \"Box of 12\", null, null);
        manager.complete(3);
        System.out.println(manager.find(2).description + \" \" + manager.find(2).updatedAt);

        String first = manager.delete(1);
        System.out.println(first == null ? \"Deleted record 1.\" : first);
        String second = manager.delete(99);
        System.out.println(second == null ? \"Deleted record 99.\" : second);
        show(manager);
    }
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "1. Notebook [supplies] (not done)
2. Pencil [supplies] (not done)
3. Study plan [planning] (not done)
Search for 'note':
Notebook
Box of 12 2026-01-15T10:00:04
Deleted record 1.
No record has that id.
2. Pencil [supplies] (not done)
3. Study plan [planning] (done)
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Reusing a deleted entry's id by counting the list size instead of using the highest id."]], [Plain [Str "Changing ", Code ("", [], []) "createdAt", Str " when updating (the field is ", Code ("", [], []) "final", Str " to prevent this)."]], [Plain [Str "Throwing an exception for a missing record where a message to display is more helpful."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output before running."]], [Plain [Str "Add ", Code ("", [], []) "listByCategory(category)", Str " to ", Code ("", [], []) "Manager", Str "."]], [Plain [Str "Add a rule that blocks completing an entry that is already complete, with a message."]], [Plain [Str "Explain how the fake clock makes the output repeatable."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "List output uses the same fixed format for every record and the words ", Code ("", [], []) "done", Str " and ", Code ("", [], []) "not done", Str ". Search results print only titles, so each line is short."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can implement add, list, search, change, complete, and delete."]], [Plain [Str "\9744", Space, Str "I assign unique ids."]], [Plain [Str "\9744", Space, Str "I update timestamps correctly."]], [Plain [Str "\9744", Space, Str "I return clear messages for failures."]], [Plain [Str "\9744", Space, Str "I can make output repeatable with a fake clock."]]], HorizontalRule, Header 3 ("lesson-114-capstone-validation-and-acceptance-tests", ["unnumbered", "unlisted"], []) [Str "Lesson 11.4: Capstone: Validation and Acceptance Tests"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 11.4: Testing and Refinement"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Run the shared acceptance tests."]], [Plain [Str "Verify that validation rejects bad data."]], [Plain [Str "Read and interpret test results."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The shared acceptance tests describe behavior that every language track's capstone must show:"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Adding a record with an empty title is rejected with a clear message."]], [Plain [Str "A new record receives an unused ", Code ("", [], []) "id", Str "."]], [Plain [Str "Updating a record changes ", Code ("", [], []) "updated_at", Str " but not ", Code ("", [], []) "created_at", Str "."]], [Plain [Str "Deleting a record removes only that record."]], [Plain [Str "Saving and reloading preserves all fields and values (shown in Lesson 11.2)."]], [Plain [Str "Every message and control can be used without color or a mouse (checked by hand in Lesson 11.5)."]]], Para [Str "This lesson automates tests 1 to 4 and also tests completion and the rejection of a blank title in an update. Each test builds a new ", Code ("", [], []) "Manager", Str ", so tests cannot affect each other. The fake clock keeps timestamps predictable so a test can check that ", Code ("", [], []) "updatedAt", Str " changed while ", Code ("", [], []) "createdAt", Str " did not."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.*;
import java.util.function.Supplier;

class Entry {
    final int id;
    String title;
    String description;
    String category;
    final String createdAt;
    String updatedAt;
    boolean done;

    Entry(int id, String title, String description, String category, String createdAt) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.category = category;
        this.createdAt = createdAt;
        this.updatedAt = createdAt;
        this.done = false;
    }

    String describe() {
        return id + \". \" + title + \" [\" + category + \"] (\" + (done ? \"done\" : \"not done\") + \")\";
    }
}

record Outcome(Entry entry, String message) {}

class Clocks {
    static Supplier<String> fake() {
        int[] ticks = {0};
        return () -> {
            ticks[0]++;
            return String.format(\"2026-01-15T10:00:%02d\", ticks[0]);
        };
    }
}

class Manager {
    final List<Entry> entries = new ArrayList<>();
    private final Supplier<String> clock;

    Manager(Supplier<String> clock) {
        this.clock = clock;
    }

    static String validate(String title, String category) {
        if (title == null || title.isBlank()) {
            return \"A title is required.\";
        }
        if (category == null || category.isBlank()) {
            return \"A category is required.\";
        }
        return null;
    }

    private int nextId() {
        int highest = 0;
        for (Entry entry : entries) {
            highest = Math.max(highest, entry.id);
        }
        return highest + 1;
    }

    Entry find(int id) {
        for (Entry entry : entries) {
            if (entry.id == id) {
                return entry;
            }
        }
        return null;
    }

    Outcome add(String title, String description, String category) {
        String problem = validate(title, category);
        if (problem != null) {
            return new Outcome(null, problem);
        }
        Entry entry = new Entry(nextId(), title.strip(), description.strip(), category.strip(), clock.get());
        entries.add(entry);
        return new Outcome(entry, null);
    }

    Outcome update(int id, String title, String description, String category, Boolean done) {
        Entry entry = find(id);
        if (entry == null) {
            return new Outcome(null, \"No record has that id.\");
        }
        String problem = validate(title != null ? title : entry.title, category != null ? category : entry.category);
        if (problem != null) {
            return new Outcome(null, problem);
        }
        if (title != null) entry.title = title.strip();
        if (description != null) entry.description = description.strip();
        if (category != null) entry.category = category.strip();
        if (done != null) entry.done = done;
        entry.updatedAt = clock.get();
        return new Outcome(entry, null);
    }

    Outcome complete(int id) {
        return update(id, null, null, null, true);
    }

    String delete(int id) {
        Entry entry = find(id);
        if (entry == null) {
            return \"No record has that id.\";
        }
        entries.remove(entry);
        return null;
    }

    List<Entry> search(String text) {
        String needle = text.strip().toLowerCase();
        List<Entry> found = new ArrayList<>();
        for (Entry entry : entries) {
            if (entry.title.toLowerCase().contains(needle) || entry.description.toLowerCase().contains(needle)) {
                found.add(entry);
            }
        }
        return found;
    }
}

public class Lesson_11_4 {
    static int failures = 0;

    static void assertThat(boolean condition, String message) {
        if (!condition) {
            throw new AssertionError(message);
        }
    }

    static void test(String name, Runnable body) {
        try {
            body.run();
            System.out.println(\"PASS \" + name);
        } catch (AssertionError | RuntimeException e) {
            failures++;
            System.out.println(\"FAIL \" + name + \": \" + e.getMessage());
        }
    }

    static Manager fresh() {
        Manager manager = new Manager(Clocks.fake());
        manager.add(\"Notebook\", \"Course notes\", \"supplies\");
        manager.add(\"Pencil\", \"Box of 10\", \"supplies\");
        manager.add(\"Study plan\", \"Weekly schedule\", \"planning\");
        return manager;
    }

    public static void main(String[] args) {
        test(\"1. an empty title is rejected\", () -> {
            Manager manager = fresh();
            Outcome outcome = manager.add(\"   \", \"x\", \"supplies\");
            assertThat(outcome.entry() == null && \"A title is required.\".equals(outcome.message()), \"expected the title message\");
            assertThat(manager.entries.size() == 3, \"the list should be unchanged\");
        });

        test(\"2. a new record gets an unused id\", () -> {
            Manager manager = fresh();
            manager.delete(2);
            Outcome outcome = manager.add(\"Ruler\", \"30 cm\", \"supplies\");
            assertThat(outcome.entry() != null && outcome.entry().id == 4, \"expected id 4\");
        });

        test(\"3. update changes updatedAt but not createdAt\", () -> {
            Manager manager = fresh();
            Entry entry = manager.find(1);
            String createdBefore = entry.createdAt;
            String updatedBefore = entry.updatedAt;
            manager.update(1, null, \"Lecture notes\", null, null);
            assertThat(entry.createdAt.equals(createdBefore), \"createdAt changed\");
            assertThat(!entry.updatedAt.equals(updatedBefore), \"updatedAt did not change\");
        });

        test(\"4. delete removes only that record\", () -> {
            Manager manager = fresh();
            manager.delete(2);
            List<Integer> ids = new ArrayList<>();
            for (Entry entry : manager.entries) {
                ids.add(entry.id);
            }
            assertThat(ids.equals(List.of(1, 3)), \"wrong records remain: \" + ids);
        });

        test(\"5. complete marks done and updates the record\", () -> {
            Manager manager = fresh();
            Entry entry = manager.complete(3).entry();
            assertThat(entry != null && entry.done && !entry.updatedAt.equals(entry.createdAt), \"completion not recorded\");
        });

        test(\"6. a blank title cannot be saved by update\", () -> {
            Manager manager = fresh();
            Outcome outcome = manager.update(1, \"\", null, null, null);
            assertThat(outcome.entry() == null && \"A title is required.\".equals(outcome.message()), \"update accepted a blank title\");
        });

        System.out.println(failures == 0 ? \"All acceptance tests passed.\" : failures + \" test(s) failed.\");
    }
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "PASS 1. an empty title is rejected
PASS 2. a new record gets an unused id
PASS 3. update changes updatedAt but not createdAt
PASS 4. delete removes only that record
PASS 5. complete marks done and updates the record
PASS 6. a blank title cannot be saved by update
All acceptance tests passed.
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Sharing one manager between tests, so one test's deletions change the next test."]], [Plain [Str "Checking only that no exception occurred, and not checking the result."]], [Plain [Str "Writing the expected message differently from the program, so a correct program fails the test."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Break ", Code ("", [], []) "Manager.update", Str " so it also changes ", Code ("", [], []) "createdAt", Str " (make the field non-final) and watch test 3 fail. Restore it."]], [Plain [Str "Add a test that searching ignores case."]], [Plain [Str "Add a test that deleting an unknown id returns a message."]], [Plain [Str "Explain why test 2 deletes record 2 before adding the new one."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "The test names begin with the acceptance-test number, so PASS and FAIL lines can be matched to the specification. Read only the first word of each line to hear the overall result quickly."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can run the shared acceptance tests."]], [Plain [Str "\9744", Space, Str "I can test validation failures."]], [Plain [Str "\9744", Space, Str "I can test timestamps with a fake clock."]], [Plain [Str "\9744", Space, Str "I can read PASS and FAIL lines."]], [Plain [Str "\9744", Space, Str "I use a fresh manager for every test."]]], HorizontalRule, Header 3 ("lesson-115-capstone-documentation-and-presentation", ["unnumbered", "unlisted"], []) [Str "Lesson 11.5: Capstone: Documentation and Presentation"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Link ("", [], []) [Str "Unit P, Lesson P.6"] ("docs/pandoc/pdf/src/FOUNDATIONS/unit-p-computing-foundations.md#unit-p-computing-foundations-primer-complete-before-any-language-track", ""), Str ": files, data formats, and the shared accessible workflow"]], [Plain [Str "Matching Python lesson: Lesson 11.5: Final Submission"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write a plain-text project summary."]], [Plain [Str "Report a count of records by category."]], [Plain [Str "Complete a manual accessibility check."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Documentation tells a future reader what the program does and how to run it. Write it as plain text or Markdown with short headings, numbered steps, and complete sentences. Include: the purpose of the program, the compile and run commands, the shared record fields, the commands a user can give, the accessibility checks you carried out, and what you would improve next."], Para [Str "The example generates a summary from the shared sample data. It counts records by category and prints the categories in alphabetical order (a ", Code ("", [], []) "TreeMap", Str " keeps its keys sorted) so the output is stable. It then prints the manual accessibility checklist. The unchecked boxes ", Code ("", [], []) "[ ]", Str " are for ", Emph [Str "you"], Str " to complete by hand with your own access technology; the program cannot verify them."], Para [Str "Acceptance test 6 is a manual check: every message and control can be used without color or a mouse. Test it with the keyboard only, and with the screen reader or braille display you actually use. Record what you tested and its version; do not claim compatibility with software you did not test."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Lesson_11_5 {
    record Entry(int id, String title, String category) {}

    public static void main(String[] args) {
        List<Entry> sample = List.of(
            new Entry(1, \"Notebook\", \"supplies\"),
            new Entry(2, \"Pencil\", \"supplies\"),
            new Entry(3, \"Study plan\", \"planning\"));

        Map<String, Integer> counts = new TreeMap<>();
        for (Entry entry : sample) {
            counts.merge(entry.category(), 1, Integer::sum);
        }

        System.out.println(\"Personal Data Manager - Summary\");
        System.out.println(\"Records: \" + sample.size());
        System.out.println(\"Categories:\");
        for (Map.Entry<String, Integer> category : counts.entrySet()) {
            System.out.println(\"- \" + category.getKey() + \": \" + category.getValue());
        }

        System.out.println();
        System.out.println(\"Manual accessibility checklist (complete this by hand):\");
        String[] checks = {
            \"[ ] Every command can be used with the keyboard only.\",
            \"[ ] Every message is a complete sentence that says what to do next.\",
            \"[ ] No meaning depends on color, position, or symbols alone.\",
            \"[ ] The output was read with my own screen reader or braille display.\",
            \"[ ] I recorded the operating system, program, and version I tested.\"
        };
        for (String check : checks) {
            System.out.println(check);
        }
    }
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Personal Data Manager - Summary
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
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing documentation that only the author can follow."]], [Plain [Str "Claiming that a program is accessible without recording what was tested and how."]], [Plain [Str "Letting the documentation drift from the program after later changes."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write the project summary for your own capstone using the headings above."]], [Plain [Str "Run the keyboard-only check and record each problem you find."]], [Plain [Str "Ask a classmate to follow your run instructions from a fresh folder and note where they get stuck."]], [Plain [Str "Write three improvements for the next version, ordered by user benefit."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "This is the final accessibility lesson. Read your own documentation aloud from start to finish. Anything you have to look at the screen to understand needs rewriting."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a plain-text project summary."]], [Plain [Str "\9744", Space, Str "I can report counts by category."]], [Plain [Str "\9744", Space, Str "I can run a manual accessibility check."]], [Plain [Str "\9744", Space, Str "I record what I tested."]], [Plain [Str "\9744", Space, Str "I do not claim untested compatibility."]]], HorizontalRule, Header 3 ("ai-policy", ["unnumbered", "unlisted"], []) [Str "AI Policy"], Para [Str "AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions."]]