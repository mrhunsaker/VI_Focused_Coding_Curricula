[Header 2 ("unit-6-functions-and-methods", [], []) [Str "Unit 6: Functions and Methods"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops functions and methods through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing."], Para [Strong [Str "Unit objectives:"], Str " explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects."], Header 3 ("lesson-61-defining-methods", ["unnumbered", "unlisted"], []) [Str "Lesson 6.1: Defining Methods"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 6.1: Defining Functions"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Define and call static methods."]], [Plain [Str "Pass parameters and return nothing or a value."]], [Plain [Str "Use a method reference."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "In Java a function is a ", Strong [Str "method"], Str " inside a class. A ", Emph [Str "static"], Str " method belongs to the class and is called without an object. A method declaration states its return type, its name, and its typed parameters: ", Code ("", [], []) "static void showTip(double bill, double tipRate)", Str ". ", Code ("", [], []) "void", Str " means nothing is returned."], Para [Str "The ", Emph [Str "parameters"], Str " are the names in the definition and the ", Emph [Str "arguments"], Str " are the values you pass. Arguments are matched to parameters by position, and Java passes every argument ", Strong [Str "by value"], Str ": the method receives a copy of a number, or a copy of the reference to an object."], Para [Str "A ", Emph [Str "method reference"], Str " such as ", Code ("", [], []) "Lesson_6_1::showTip", Str " names a method so that it can be passed around and called later through a functional interface like ", Code ("", [], []) "BiConsumer", Str "."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.Locale;
import java.util.function.BiConsumer;

public class Lesson_6_1 {
    static String money(double value) {
        return String.format(Locale.US, \"%.2f\", value);
    }

    static void greetUser() {
        System.out.println(\"Hello, Java programmer!\");
    }

    static void greetName(String name) {
        System.out.println(\"Hello, \" + name + \"!\");
    }

    static void showTip(double bill, double tipRate) {
        double tip = bill * tipRate;
        System.out.println(\"Tip: \" + money(tip));
        System.out.println(\"Total: \" + money(bill + tip));
    }

    public static void main(String[] args) {
        greetUser();
        greetUser();
        greetName(\"Avery\");
        greetName(\"Riley\");
        showTip(24.5, 0.15);

        BiConsumer<Double, Double> reference = Lesson_6_1::showTip;
        reference.accept(100.0, 0.2);
    }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Hello, Java programmer!
Hello, Java programmer!
Hello, Avery!
Hello, Riley!
Tip: 3.68
Total: 28.18
Tip: 20.00
Total: 120.00
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing ", Code ("", [], []) "greetUser;", Str " without parentheses, which is not a call."]], [Plain [Str "Passing arguments in the wrong order, such as ", Code ("", [], []) "showTip(0.15, 24.5)", Str "."]], [Plain [Str "Forgetting ", Code ("", [], []) "static", Str " and then calling the method from ", Code ("", [], []) "main", Str ", which is a compile error."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Call ", Code ("", [], []) "showTip(100.0, 0.2)", Str " yourself and predict both lines."]], [Plain [Str "Write ", Code ("", [], []) "describeStudent(String name, int age)", Str " that prints one sentence."]], [Plain [Str "Call ", Code ("", [], []) "greetName()", Str " with no argument and read the compiler message."]], [Plain [Str "Explain the difference between a parameter and an argument."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Choose method names that read as actions when spoken, such as ", Code ("", [], []) "showTip", Str ". Print complete sentences from a method so the screen reader announces each call's result separately."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can define and call a static method."]], [Plain [Str "\9744", Space, Str "I can distinguish parameters from arguments."]], [Plain [Str "\9744", Space, Str "I know Java passes arguments by value."]], [Plain [Str "\9744", Space, Str "I can write a method reference."]], [Plain [Str "\9744", Space, Str "I can read a method signature aloud."]]], HorizontalRule, Header 3 ("lesson-62-overloading-instead-of-default-arguments", ["unnumbered", "unlisted"], []) [Str "Lesson 6.2: Overloading Instead of Default Arguments"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 6.2: Passing Arguments"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain that Java has no default or named arguments."]], [Plain [Str "Use overloading to supply a default."]], [Plain [Str "Group related values in a record for readable calls."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Java has no default parameter values and no named arguments. Two techniques give the same result. ", Strong [Str "Overloading"], Str " declares several methods with the same name and different parameter lists: ", Code ("", [], []) "calculateTotal(double bill)", Str " calls ", Code ("", [], []) "calculateTotal(bill, 0.15)", Str ". Java chooses the version by the number and types of the arguments."], Para [Str "When a call needs several values, a ", Strong [Str "record"], Str " groups them under names, so the call site is clear: ", Code ("", [], []) "new TipRequest(24.5, 0.10)", Str " makes the two numbers visible as a bill and a rate. A record can also supply a second constructor with a default."], Para [Str "With the shared bill of 24.50, the total at the default rate 0.15 is 28.18, at 0.20 it is 29.40, and at 0.10 it is 26.95."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.Locale;

public class Lesson_6_2 {
    static final double DEFAULT_RATE = 0.15;

    static String money(double value) {
        return String.format(Locale.US, \"%.2f\", value);
    }

    static double calculateTotal(double bill, double tipRate) {
        return bill + bill * tipRate;
    }

    static double calculateTotal(double bill) {
        return calculateTotal(bill, DEFAULT_RATE);
    }

    record TipRequest(double bill, double tipRate) {
        TipRequest(double bill) {
            this(bill, DEFAULT_RATE);
        }

        double total() {
            return bill + bill * tipRate;
        }
    }

    public static void main(String[] args) {
        System.out.println(money(calculateTotal(24.5)));
        System.out.println(money(calculateTotal(24.5, 0.20)));
        System.out.println(money(new TipRequest(24.5, 0.10).total()));
        System.out.println(money(new TipRequest(24.5).total()));
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating passing arguments. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Confusing a method's parameter list with its return type or omitting a return on one control-flow path."]], [Plain [Str "Expecting Java to pass primitive variables by reference; arguments are passed by value."]], [Plain [Str "Placing a varargs parameter before another parameter or using an overload that is ambiguous."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Extract repeated statements into a named method with an explicit parameter and return contract."]], [Plain [Str "Call the method with typical, boundary, and empty collection arguments."]], [Plain [Str "Add a method that accepts a List or Map and returns a computed result without modifying the input."]], [Plain [Str "Overload a method or add a varargs form, then explain overload resolution."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]], Header 3 ("lesson-63-return-values", ["unnumbered", "unlisted"], []) [Str "Lesson 6.3: Return Values"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 6.3: Return Values"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Return a computed value."]], [Plain [Str "Return ", Code ("", [], []) "OptionalDouble", Str " when a value may be missing."]], [Plain [Str "Return several values with a record."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A method sends a value back with ", Code ("", [], []) "return", Str ", and its declared return type must match. When a result may not exist, such as the average of an empty list, returning ", Code ("", [], []) "null", Str " invites a crash. ", Code ("", [], []) "OptionalDouble", Str " states in the type that a value may be absent: ", Code ("", [], []) "OptionalDouble.empty()", Str " for no result, ", Code ("", [], []) "OptionalDouble.of(x)", Str " for a result, and ", Code ("", [], []) "isPresent()", Str ", ", Code ("", [], []) "getAsDouble()", Str ", or ", Code ("", [], []) "orElse(fallback)", Str " to read it."], Para [Str "To return several values, return a record and read its components. The example returns the average of the shared scores, classifies the average, returns a minimum and a maximum together, and shows the empty-list case."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.List;
import java.util.OptionalDouble;

public class Lesson_6_3 {
    record ScoreRange(int low, int high) {}

    static OptionalDouble average(List<Integer> scores) {
        if (scores.isEmpty()) {
            return OptionalDouble.empty();
        }
        int total = 0;
        for (int score : scores) {
            total += score;
        }
        return OptionalDouble.of((double) total / scores.size());
    }

    static String classify(double score) {
        if (score >= 90) return \"A\";
        if (score >= 80) return \"B\";
        if (score >= 70) return \"C\";
        if (score >= 60) return \"D\";
        return \"F\";
    }

    static ScoreRange minMax(List<Integer> scores) {
        int low = scores.get(0);
        int high = scores.get(0);
        for (int score : scores) {
            low = Math.min(low, score);
            high = Math.max(high, score);
        }
        return new ScoreRange(low, high);
    }

    public static void main(String[] args) {
        List<Integer> scores = List.of(82, 91, 76, 88);
        OptionalDouble avg = average(scores);
        System.out.println(\"Average: \" + avg);
        if (avg.isPresent()) {
            System.out.println(\"Grade for the average: \" + classify(avg.getAsDouble()));
        }
        ScoreRange range = minMax(scores);
        System.out.println(\"Lowest and highest: \" + range.low() + \" and \" + range.high());
        System.out.println(average(List.of()));
        System.out.println(average(List.of()).orElse(0.0));
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Average: OptionalDouble[84.25]
Grade for the average: B
Lowest and highest: 76 and 91
OptionalDouble.empty
0.0
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Printing inside the method and then trying to use the result in a calculation."]], [Plain [Str "Calling ", Code ("", [], []) "getAsDouble()", Str " on an empty ", Code ("", [], []) "OptionalDouble", Str ", which throws ", Code ("", [], []) "NoSuchElementException", Str "."]], [Plain [Str "Writing code after a ", Code ("", [], []) "return", Str " in the same block, which the compiler rejects as unreachable."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the six printed lines before running."]], [Plain [Str "Write ", Code ("", [], []) "total(List<Integer> list)", Str " that returns the sum."]], [Plain [Str "Write ", Code ("", [], []) "isPassing(int score)", Str " that returns a ", Code ("", [], []) "boolean", Str "."]], [Plain [Str "Explain how a caller should use a method that returns ", Code ("", [], []) "OptionalDouble", Str "."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Return values instead of printing inside logic methods, so the caller prints once and the screen reader announces each result a single time."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can return a value."]], [Plain [Str "\9744", Space, Str "I can return ", Code ("", [], []) "OptionalDouble", Str " for a possibly missing value."]], [Plain [Str "\9744", Space, Str "I can return several values with a record."]], [Plain [Str "\9744", Space, Str "I can use a returned value in a calculation."]], [Plain [Str "\9744", Space, Str "I can classify an average with the shared thresholds."]]], HorizontalRule, Header 3 ("lesson-64-methods-with-collections", ["unnumbered", "unlisted"], []) [Str "Lesson 6.4: Methods with Collections"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 6.4: Functions with Lists and Dictionaries"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain that a list argument is a reference passed by value."]], [Plain [Str "Change a list in a method and protect the original with a copy."]], [Plain [Str "Process the shared inventory with a method."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Java passes everything ", Strong [Str "by value"], Str ", but for an object the value is a ", Emph [Str "reference"], Str ". A method that receives a ", Code ("", [], []) "List", Str " can change the caller's list through that reference, so ", Code ("", [], []) "addScore(scores, 95)", Str " is visible to the caller. Reassigning the parameter inside the method does not change the caller's variable."], Para [Str "To produce a changed list without touching the original, return a ", Emph [Str "new"], Str " list: copy with ", Code ("", [], []) "new ArrayList<>(list)", Str " and add to the copy. ", Code ("", [], []) "Collections.unmodifiableList(list)", Str " or ", Code ("", [], []) "List.copyOf(list)", Str " give read-only versions that protect data from accidental changes."], Para [Str "The shared inventory is Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25), worth 17.50 in total."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Lesson_6_4 {
    record Item(String name, int quantity, double unitPrice) {}

    static void addScore(List<Integer> scoreList, int newScore) {
        scoreList.add(newScore);
    }

    static List<Integer> withScore(List<Integer> scoreList, int newScore) {
        List<Integer> copy = new ArrayList<>(scoreList);
        copy.add(newScore);
        return copy;
    }

    static double inventoryValue(List<Item> inventory) {
        double total = 0;
        for (Item item : inventory) {
            total += item.quantity() * item.unitPrice();
        }
        return total;
    }

    public static void main(String[] args) {
        List<Integer> scores = new ArrayList<>(List.of(82, 91, 76, 88));
        addScore(scores, 95);
        System.out.println(scores);

        List<Integer> longer = withScore(scores, 100);
        System.out.println(scores.size() + \" \" + longer.size());

        List<Item> inventory = List.of(
            new Item(\"Notebook\", 3, 2.50),
            new Item(\"Pencil\", 10, 0.50),
            new Item(\"Folder\", 4, 1.25));
        System.out.println(\"Total inventory value: \" + String.format(Locale.US, \"%.2f\", inventoryValue(inventory)));
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating methods with lists and maps. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Confusing a method's parameter list with its return type or omitting a return on one control-flow path."]], [Plain [Str "Expecting Java to pass primitive variables by reference; arguments are passed by value."]], [Plain [Str "Placing a varargs parameter before another parameter or using an overload that is ambiguous."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Extract repeated statements into a named method with an explicit parameter and return contract."]], [Plain [Str "Call the method with typical, boundary, and empty collection arguments."]], [Plain [Str "Add a method that accepts a List or Map and returns a computed result without modifying the input."]], [Plain [Str "Overload a method or add a varargs form, then explain overload resolution."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]], Header 3 ("lesson-65-arbitrary-number-of-arguments", ["unnumbered", "unlisted"], []) [Str "Lesson 6.5: Arbitrary Number of Arguments"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 documentation"] ("https://docs.oracle.com/en/java/", ""), Str "."]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", ""), Str "."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the purpose and vocabulary of arbitrary number of arguments."]], [Plain [Str "Apply the relevant Java syntax and APIs in a small, complete program."]], [Plain [Str "Compile, run, inspect, and adapt the example using keyboard-accessible tools."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "This lesson develops arbitrary number of arguments through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. A method signature includes its name and parameter types; Java passes argument values, including copied reference values. Return types are explicit, overloads differ by parameter lists, and varargs use a final array-like parameter."], Para [Str "Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "public class Lesson_6_5 {
    public static void main(String[] args) {
        System.out.println(sum(2, 4, 6, 8));
        }
        private static int sum(int... values) {
            int total = 0;
            for (int value : values) total += value;
            return total;
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating arbitrary number of arguments. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Confusing a method's parameter list with its return type or omitting a return on one control-flow path."]], [Plain [Str "Expecting Java to pass primitive variables by reference; arguments are passed by value."]], [Plain [Str "Placing a varargs parameter before another parameter or using an overload that is ambiguous."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Extract repeated statements into a named method with an explicit parameter and return contract."]], [Plain [Str "Call the method with typical, boundary, and empty collection arguments."]], [Plain [Str "Add a method that accepts a List or Map and returns a computed result without modifying the input."]], [Plain [Str "Overload a method or add a varargs form, then explain overload resolution."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]]]