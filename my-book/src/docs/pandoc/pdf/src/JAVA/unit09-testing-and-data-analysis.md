[Header 2 ("unit-9-testing-and-data-analysis", [], []) [Str "Unit 9: Testing and Data Analysis"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops testing and data analysis through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing."], Para [Strong [Str "Unit objectives:"], Str " explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects."], Header 3 ("lesson-91-testing-functions", ["unnumbered", "unlisted"], []) [Str "Lesson 9.1: Testing Functions"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 9.1: Testing Your Code"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write checks with chosen inputs and expected results."]], [Plain [Str "Compare decimals with a tolerance."]], [Plain [Str "Test boundary values and report failure with an exit status."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "test"], Str " runs code with chosen inputs and compares the result with a value decided in advance. Real Java projects use JUnit through Maven or Gradle. To keep this course free of build tooling, the example uses a tiny ", Code ("", [], []) "check", Str " method; the habits (inputs, expected values, boundaries) are the same."], Para [Str "Decimal results are compared with a ", Emph [Str "tolerance"], Str ", not ", Code ("", [], []) "equals", Str ", because of floating-point approximation: the tip for 24.50 at 0.15 is stored as 3.6749999999999998, so the test checks that it is within a tiny distance of 3.675."], Para [Str "The same tests appear in every language track: ", Code ("", [], []) "add(5, 3)", Str " is 8, ", Code ("", [], []) "add(-5, -3)", Str " is -8, ", Code ("", [], []) "add(10, -4)", Str " is 6, the tip is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F."], Para [Code ("", [], []) "System.exit(1)", Str " ends the program with a failure status when any check fails, so other tools can notice."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.Objects;

public class Lesson_9_1 {
    static int passed = 0;
    static int failed = 0;

    static int add(int a, int b) {
        return a + b;
    }

    static double calculateTip(double bill, double rate) {
        return bill * rate;
    }

    static String classify(int score) {
        if (score >= 90) return \"A\";
        if (score >= 80) return \"B\";
        if (score >= 70) return \"C\";
        if (score >= 60) return \"D\";
        return \"F\";
    }

    static void check(String name, Object actual, Object expected) {
        if (Objects.equals(actual, expected)) {
            passed++;
            System.out.println(\"PASS \" + name);
        } else {
            failed++;
            System.out.println(\"FAIL \" + name + \": expected \" + expected + \" but got \" + actual);
        }
    }

    static void checkClose(String name, double actual, double expected, double tolerance) {
        check(name, Math.abs(actual - expected) <= tolerance, true);
    }

    public static void main(String[] args) {
        check(\"add 5 and 3\", add(5, 3), 8);
        check(\"add -5 and -3\", add(-5, -3), -8);
        check(\"add 10 and -4\", add(10, -4), 6);
        checkClose(\"tip on 24.50 at 0.15\", calculateTip(24.5, 0.15), 3.675, 1e-9);
        check(\"tip on a zero bill\", calculateTip(0, 0.15), 0.0);
        check(\"classify 90\", classify(90), \"A\");
        check(\"classify 89\", classify(89), \"B\");
        check(\"classify 60\", classify(60), \"D\");
        check(\"classify 59\", classify(59), \"F\");

        System.out.println(passed + \" passed, \" + failed + \" failed\");
        if (failed > 0) {
            System.exit(1);
        }
    }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "PASS add 5 and 3
PASS add -5 and -3
PASS add 10 and -4
PASS tip on 24.50 at 0.15
PASS tip on a zero bill
PASS classify 90
PASS classify 89
PASS classify 60
PASS classify 59
9 passed, 0 failed
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Comparing decimal results with ", Code ("", [], []) "equals", Str " or ", Code ("", [], []) "==", Str "."]], [Plain [Str "Testing only typical values and skipping the boundaries 90, 89, 60, and 59."]], [Plain [Str "Writing the expected value after seeing the output, which turns the test into a copy of the bug."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Change one expected value so a check fails, read the message, and restore it."]], [Plain [Str "Add checks for the grades at 80, 79, 70, and 69."]], [Plain [Str "Write checks for ", Code ("", [], []) "isPassing(score)", Str " before writing the method."]], [Plain [Str "Explain why the tip check uses a tolerance."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each check prints one complete line that starts with PASS or FAIL, and the last line gives the counts, so the result can be understood from the first word of each line and the final summary."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a check with an expected value."]], [Plain [Str "\9744", Space, Str "I can compare decimals with a tolerance."]], [Plain [Str "\9744", Space, Str "I can choose boundary tests."]], [Plain [Str "\9744", Space, Str "I can read PASS and FAIL lines."]], [Plain [Str "\9744", Space, Str "I know how to signal failure with an exit status."]]], HorizontalRule, Header 3 ("lesson-92-testing-classes", ["unnumbered", "unlisted"], []) [Str "Lesson 9.2: Testing Classes"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 9.2: Testing a Class"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create a fresh object for every test."]], [Plain [Str "Test a value, a change of state, and an error."]], [Plain [Str "Test that an exception is thrown."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Each test should start from a known state, so create a new object for every test with a ", Emph [Str "setup"], Str " method. Tests that share an object can affect each other and fail in confusing ways."], Para [Str "Test three kinds of behavior: that a method returns the right value (", Code ("", [], []) "totalValue", Str " for 3 at 2.50 is 7.5), that a method changes the object correctly (restocking 2 makes the quantity 5), and that invalid use is rejected (restocking a negative amount throws ", Code ("", [], []) "IllegalArgumentException", Str ")."], Para [Str "To test that an exception ", Strong [Str "does"], Str " happen, call the method inside ", Code ("", [], []) "try", Str ", fail the test if no exception is thrown, and catch the expected exception type. JUnit's ", Code ("", [], []) "assertThrows", Str " does this in one line."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "public class Lesson_9_2 {
    static class Item {
        final String name;
        int quantity;
        final double unitPrice;

        Item(String name, int quantity, double unitPrice) {
            this.name = name;
            this.quantity = quantity;
            this.unitPrice = unitPrice;
        }

        double totalValue() {
            return quantity * unitPrice;
        }

        void restock(int amount) {
            if (amount < 0) {
                throw new IllegalArgumentException(\"amount must not be negative\");
            }
            quantity += amount;
        }
    }

    static int failures = 0;

    static Item setup() {
        return new Item(\"Notebook\", 3, 2.50);
    }

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

    public static void main(String[] args) {
        test(\"total value is 7.5\", () ->
            assertThat(Math.abs(setup().totalValue() - 7.5) < 1e-9, \"wrong total\"));

        test(\"restock adds to the quantity\", () -> {
            Item item = setup();
            item.restock(2);
            assertThat(item.quantity == 5, \"quantity should be 5\");
        });

        test(\"restock rejects a negative amount\", () -> {
            boolean thrown = false;
            try {
                setup().restock(-1);
            } catch (IllegalArgumentException e) {
                thrown = true;
            }
            assertThat(thrown, \"an exception should have been thrown\");
        });

        System.out.println(failures == 0 ? \"All tests passed.\" : failures + \" test(s) failed.\");
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating testing a class. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Relying on Java's assert statements without enabling assertions, or testing implementation details instead of behavior."]], [Plain [Str "Allowing tests to share mutable state so their order affects results."]], [Plain [Str "Assuming a simple comma split handles quoted CSV fields or using an unseeded random source in a reproducibility exercise."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write one passing and one failing test for a pure method, then run the tests repeatedly."]], [Plain [Str "Seed a Random instance and verify the exercise is reproducible."]], [Plain [Str "Analyze a sentence for word counts after applying a documented normalization rule."]], [Plain [Str "Test CSV data with quoted commas and explain why a production parser is required."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]], Header 3 ("lesson-93-introduction-to-random-numbers", ["unnumbered", "unlisted"], []) [Str "Lesson 9.3: Introduction to Random Numbers"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 documentation"] ("https://docs.oracle.com/en/java/", ""), Str "."]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", ""), Str "."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the purpose and vocabulary of introduction to random numbers."]], [Plain [Str "Apply the relevant Java syntax and APIs in a small, complete program."]], [Plain [Str "Compile, run, inspect, and adapt the example using keyboard-accessible tools."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "This lesson develops introduction to random numbers through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Separate deterministic logic from random generation, file I/O, and user interaction. Test methods and object invariants with assertions or a test framework such as JUnit. CSV quoting rules mean a comma split is only a teaching illustration, not a production parser."], Para [Str "Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "public class Lesson_9_3 {
    public static void main(String[] args) {
        java.util.Random random = new java.util.Random(42);
        for (int i = 0; i < 5; i++) System.out.println(random.nextInt(10));
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Same seed gives the same rolls: true
All rolls between 1 and 6: true
Decimal in [0, 1): true
Chosen score is from the list: true
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) "nextInt(1, 6)", Str " for a die and never rolling a 6. The upper limit is excluded."]], [Plain [Str "Testing for specific random values that may change between versions."]], [Plain [Str "Using ", Code ("", [], []) "Random", Str " for passwords or tokens, which it is not designed for."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program three times and compare."]], [Plain [Str "Change the seeds and check that the property lines still print ", Code ("", [], []) "true", Str "."]], [Plain [Str "Simulate 600 rolls and count how many of each face appeared (the counts depend on the seed)."]], [Plain [Str "Explain why a test should check a property rather than a specific random number."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print yes or no style results for random behavior, so the announced output is the same on every run and the screen reader does not read unpredictable values."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "nextInt", Str " with an excluded upper bound."]], [Plain [Str "\9744", Space, Str "I can set a seed."]], [Plain [Str "\9744", Space, Str "I can test properties of random code."]], [Plain [Str "\9744", Space, Str "I know sequences can differ between versions."]], [Plain [Str "\9744", Space, Str "I can pick a random list item."]]], HorizontalRule, Header 3 ("lesson-94-text-analysis", ["unnumbered", "unlisted"], []) [Str "Lesson 9.4: Text Analysis"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 9.4: Data Analysis - Text Analysis"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Split text into words and count them."]], [Plain [Str "Count word and letter frequencies with a map."]], [Plain [Str "Produce stable, sorted output."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "text.split(\" \")", Str " splits a string into an array of words. Counting uses a map from each word to its count: ", Code ("", [], []) "counts.merge(word, 1, Integer::sum)", Str " adds one, starting from 1 for a new word."], Para [Str "Map order is only stable if you choose the right class. ", Code ("", [], []) "LinkedHashMap", Str " keeps the order in which words first appeared. To order by count, copy the entries into a list and sort it with a comparator: count descending first, then letter ascending, so ties print in a fixed order."], Para [Str "The shared text sample is \"A student studies programming. Programming develops problem-solving skills.\" After lower-casing and removing the periods it has 8 words, and ", Code ("", [], []) "programming", Str " appears twice."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Lesson_9_4 {
    public static void main(String[] args) {
        String text = \"A student studies programming. Programming develops problem-solving skills.\";
        String[] words = text.toLowerCase().replace(\".\", \"\").split(\" \");

        Map<String, Integer> frequencies = new LinkedHashMap<>();
        for (String word : words) {
            frequencies.merge(word, 1, Integer::sum);
        }

        System.out.println(\"Word count: \" + words.length);
        System.out.println(\"Word frequencies:\");
        for (Map.Entry<String, Integer> entry : frequencies.entrySet()) {
            System.out.println(\"'\" + entry.getKey() + \"': \" + entry.getValue());
        }

        Map<Character, Integer> letters = new LinkedHashMap<>();
        for (char c : text.toLowerCase().toCharArray()) {
            if (Character.isLetter(c)) {
                letters.merge(c, 1, Integer::sum);
            }
        }
        List<Map.Entry<Character, Integer>> entries = new ArrayList<>(letters.entrySet());
        entries.sort(Comparator.<Map.Entry<Character, Integer>>comparingInt(Map.Entry::getValue).reversed()
            .thenComparing(Map.Entry::getKey));
        System.out.println(\"Most common letters:\");
        for (int i = 0; i < 3; i++) {
            System.out.println(entries.get(i).getKey() + \": \" + entries.get(i).getValue());
        }
    }
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Word count: 8
Word frequencies:
'a': 1
'student': 1
'studies': 1
'programming': 2
'develops': 1
'problem-solving': 1
'skills': 1
Most common letters:
s: 7
e: 5
g: 5
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Counting punctuation as part of a word, so ", Code ("", [], []) "programming.", Str " and ", Code ("", [], []) "programming", Str " are different words."]], [Plain [Str "Forgetting to lower-case first, so ", Code ("", [], []) "Programming", Str " and ", Code ("", [], []) "programming", Str " are counted separately."]], [Plain [Str "Relying on ", Code ("", [], []) "HashMap", Str " order or on an unsorted tie."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the word count and the count for ", Code ("", [], []) "programming", Str " before running."]], [Plain [Str "Count the words longer than 8 letters."]], [Plain [Str "Print the longest word."]], [Plain [Str "Change the sort so ties are listed in reverse alphabetical order."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the frequency list in its fixed order. Because the order is stable, you can learn it and compare runs by ear. Print each pair as a short sentence with the same wording every time."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can split text into words."]], [Plain [Str "\9744", Space, Str "I can count frequencies with a map."]], [Plain [Str "\9744", Space, Str "I can sort with a tie-break."]], [Plain [Str "\9744", Space, Str "I can remove punctuation first."]], [Plain [Str "\9744", Space, Str "I can read a stable report."]]], HorizontalRule, Header 3 ("lesson-95-working-with-csv-files", ["unnumbered", "unlisted"], []) [Str "Lesson 9.5: Working with CSV Files"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 9.5: Data Analysis - CSV Files"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create and read a CSV file."]], [Plain [Str "Split lines into fields and convert numbers."]], [Plain [Str "Compute an average and a count."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A CSV (comma-separated values) file stores a table as text. The first line names the columns and each later line is a record. The shared student file has the columns ", Code ("", [], []) "student_id", Str ", ", Code ("", [], []) "first_name", Str ", ", Code ("", [], []) "last_name", Str ", ", Code ("", [], []) "score", Str ", and ", Code ("", [], []) "active", Str ", and three records."], Para [Str "The standard library has no CSV reader. ", Code ("", [], []) "line.split(\",\")", Str " works only for ", Strong [Str "simple"], Str " files: a value that contains a comma inside quotation marks, such as ", Code ("", [], []) "\"Smith, Jr.\"", Str ", would be split wrongly. For such files use a maintained library or write a real parser."], Para [Str "Every field is text. Convert the score with ", Code ("", [], []) "Integer.parseInt", Str " and compare ", Code ("", [], []) "active", Str " with the text ", Code ("", [], []) "\"true\"", Str ". With scores 91, 82, and 76 the average is 83.00, and two students are active."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Locale;

public class Lesson_9_5 {
    public static void main(String[] args) throws IOException {
        Path file = Path.of(\"students.csv\");
        Files.writeString(file, String.join(\"\\n\",
            \"student_id,first_name,last_name,score,active\",
            \"1,Avery,Student,91,true\",
            \"2,Jordan,Lee,82,true\",
            \"3,Casey,Smith,76,false\") + \"\\n\");

        if (!Files.exists(file)) {
            System.out.println(\"Error: students.csv was not found.\");
            return;
        }
        List<String> lines = Files.readAllLines(file);
        System.out.println(\"Columns: \" + String.join(\", \", lines.get(0).split(\",\")));

        int total = 0;
        int active = 0;
        List<String> students = lines.subList(1, lines.size());
        for (String line : students) {
            String[] row = line.split(\",\");
            int score = Integer.parseInt(row[3]);
            total += score;
            if (row[4].equals(\"true\")) {
                active++;
            }
            System.out.println(row[0] + \": \" + row[1] + \" \" + row[2] + \" scored \" + score);
        }

        System.out.println(\"Students: \" + students.size());
        System.out.println(\"Average score: \" + String.format(Locale.US, \"%.2f\", (double) total / students.size()));
        System.out.println(\"Active students: \" + active);
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating working with csv data. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Relying on Java's assert statements without enabling assertions, or testing implementation details instead of behavior."]], [Plain [Str "Allowing tests to share mutable state so their order affects results."]], [Plain [Str "Assuming a simple comma split handles quoted CSV fields or using an unseeded random source in a reproducibility exercise."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write one passing and one failing test for a pure method, then run the tests repeatedly."]], [Plain [Str "Seed a Random instance and verify the exercise is reproducible."]], [Plain [Str "Analyze a sentence for word counts after applying a documented normalization rule."]], [Plain [Str "Test CSV data with quoted commas and explain why a production parser is required."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]]]