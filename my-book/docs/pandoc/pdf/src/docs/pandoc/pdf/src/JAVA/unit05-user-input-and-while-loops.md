[Header 2 ("unit-5-user-input-and-while-loops", [], []) [Str "Unit 5: User Input and while Loops"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops user input and while loops through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing."], Para [Strong [Str "Unit objectives:"], Str " explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects."], Header 3 ("lesson-51-how-console-input-works", ["unnumbered", "unlisted"], []) [Str "Lesson 5.1: How Console Input Works"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 5.1: How the input() Function Works"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Read a line and recognize it as text."]], [Plain [Str "Convert it safely and handle failure."]], [Plain [Str "Handle the end of input."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "Scanner.nextLine()", Str " returns the next line as a ", Code ("", [], []) "String", Str ". A program must check ", Code ("", [], []) "hasNextLine()", Str " first, because at the end of input ", Code ("", [], []) "nextLine()", Str " throws. It never returns a number: typed digits are text until you convert them. ", Code ("", [], []) "Integer.parseInt", Str " converts text and throws ", Code ("", [], []) "NumberFormatException", Str " when the text is not a whole number."], Para [Str "A program that reads input must plan for three cases: a valid value, an invalid value, and no value at all. The example uses a small ", Code ("", [], []) "next", Str " helper that returns ", Code ("", [], []) "null", Str " at the end of input, and a ", Code ("", [], []) "toInt", Str " helper that returns ", Code ("", [], []) "null", Str " for bad text. With the typed value 16 the age five years later is 21; the second value, ", Code ("", [], []) "abc", Str ", is rejected."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.Scanner;

public class Lesson_5_1 {
    static String next(Scanner in) {
        return in.hasNextLine() ? in.nextLine() : null;
    }

    static Integer toInt(String text) {
        if (text == null) {
            return null;
        }
        try {
            return Integer.parseInt(text.trim());
        } catch (NumberFormatException e) {
            return null;
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println(\"How old are you?\");
        String text = next(in);
        System.out.println(\"Read: \" + (text == null ? \"nothing\" : text.getClass().getSimpleName()));

        Integer age = toInt(text);
        if (age != null) {
            System.out.println(\"In 5 years: \" + (age + 5));
        } else {
            System.out.println(\"That was not a whole number.\");
        }

        System.out.println(\"Enter another value:\");
        Integer second = toInt(next(in));
        if (second != null) {
            System.out.println(\"Number: \" + second);
        } else {
            System.out.println(\"Not a number; toInt returned null.\");
        }
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating how scanner input works. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Mixing nextInt/next with nextLine without consuming the pending line terminator."]], [Plain [Str "Writing a sentinel loop that fails to stop at the sentinel or does not handle end-of-input."]], [Plain [Str "Using continue or break in a way that skips required state updates and creates a nonterminating loop."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Feed several lines of input, including an empty line and the sentinel, to the Scanner workflow."]], [Plain [Str "Trace the loop condition and state update for every iteration, including end-of-input."]], [Plain [Str "Add an attempt limit and a clear exit command to prevent an infinite prompt loop."]], [Plain [Str "Test that continue skips only the intended processing step and does not skip required updates."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]], Header 3 ("lesson-52-the-while-loop-in-action", ["unnumbered", "unlisted"], []) [Str "Lesson 5.2: The while Loop in Action"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 documentation"] ("https://docs.oracle.com/en/java/", ""), Str "."]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", ""), Str "."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the purpose and vocabulary of the while loop in action."]], [Plain [Str "Apply the relevant Java syntax and APIs in a small, complete program."]], [Plain [Str "Compile, run, inspect, and adapt the example using keyboard-accessible tools."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "This lesson develops the while loop in action through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens."], Para [Str "Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "public class Lesson_5_2 {
    public static void main(String[] args) {
        java.util.Scanner input = new java.util.Scanner(\"3 2 1 0\");
        int count = 0;
        while (input.hasNextInt()) {
            int value = input.nextInt();
            if (value == 0) break;
            count += value;
        }
        System.out.println(\"sum before sentinel=\" + count);
        input.close();
    }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "hello
scores
quit
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit:
You said: hello
Enter a message, or type quit to exit:
You said: scores
Enter a message, or type quit to exit:
Goodbye!
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit:
Goodbye!
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to change the loop variable, which creates an endless loop."]], [Plain [Str "Testing for ", Code ("", [], []) "quit", Str " but not for ", Code ("", [], []) "null", Str ", so the loop reads forever after input ends."]], [Plain [Str "Comparing with ", Code ("", [], []) "message == \"quit\"", Str " instead of ", Code ("", [], []) "equals", Str "."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output for the typed lines hello, scores, and quit."]], [Plain [Str "Change the sentinel to ", Code ("", [], []) "exit", Str " and update the prompt."]], [Plain [Str "Count the messages entered and print the count at the end."]], [Plain [Str "Rewrite the counting loop as a ", Code ("", [], []) "for", Str " loop and compare."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each prompt is on its own line and each response begins with ", Code ("", [], []) "You said:", Str ", so the conversation can be followed in order by ear. If a loop floods the screen reader, stop it with Ctrl+C."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a counting ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "\9744", Space, Str "I can write a sentinel loop."]], [Plain [Str "\9744", Space, Str "I test for ", Code ("", [], []) "null", Str " as well as the sentinel."]], [Plain [Str "\9744", Space, Str "I update the loop variable."]], [Plain [Str "\9744", Space, Str "I compare strings with ", Code ("", [], []) "equals", Str "."]]], HorizontalRule, Header 3 ("lesson-53-flags-break-and-labels", ["unnumbered", "unlisted"], []) [Str "Lesson 5.3: Flags, break, and Labels"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 5.3: Using Flags and break to Exit Loops"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Control a loop with a Boolean flag."]], [Plain [Str "Leave a loop with ", Code ("", [], []) "break", Str " and an outer loop with a label."]], [Plain [Str "Search a list and remember the position."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "flag"], Str " is a ", Code ("", [], []) "boolean", Str " variable that controls a loop: the loop runs while ", Code ("", [], []) "running", Str " is true, and the body sets it to ", Code ("", [], []) "false", Str " to stop. ", Code ("", [], []) "break", Str " leaves the nearest enclosing loop at once."], Para [Str "A search keeps its answer in a variable (here ", Code ("", [], []) "-1", Str " means \"not found\"), sets it when the item is found, and uses ", Code ("", [], []) "break", Str ". After the loop, the variable says whether a match was found. List positions start at 0."], Para [Str "A ", Emph [Str "label"], Str " lets ", Code ("", [], []) "break", Str " leave an outer loop from inside an inner one: write ", Code ("", [], []) "outer:", Str " before the outer loop and ", Code ("", [], []) "break outer;", Str " inside."], Para [Str "The shared scores 82, 91, 76, 88 have their first score of 90 or higher at index 1, with the value 91."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.List;
import java.util.Scanner;

public class Lesson_5_3 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        boolean running = true;
        int handled = 0;
        while (running) {
            System.out.println(\"Say something, or type quit to stop:\");
            String message = in.hasNextLine() ? in.nextLine() : null;
            if (message == null || message.equals(\"quit\")) {
                running = false;
            } else {
                handled++;
                System.out.println(\"You said: \" + message);
            }
        }
        System.out.println(\"Messages handled: \" + handled);

        List<Integer> scores = List.of(82, 91, 76, 88);
        int foundIndex = -1;
        for (int i = 0; i < scores.size(); i++) {
            if (scores.get(i) >= 90) {
                foundIndex = i;
                break;
            }
        }
        if (foundIndex >= 0) {
            System.out.println(\"First score of 90 or higher: \" + scores.get(foundIndex) + \" at index \" + foundIndex);
        } else {
            System.out.println(\"No score of 90 or higher.\");
        }

        outer:
        for (int row = 1; row <= 3; row++) {
            for (int col = 1; col <= 3; col++) {
                if (row * col == 4) {
                    System.out.println(\"Stopped at row \" + row + \", column \" + col);
                    break outer;
                }
            }
        }
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating using flags and break to exit loops. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Mixing nextInt/next with nextLine without consuming the pending line terminator."]], [Plain [Str "Writing a sentinel loop that fails to stop at the sentinel or does not handle end-of-input."]], [Plain [Str "Using continue or break in a way that skips required state updates and creates a nonterminating loop."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Feed several lines of input, including an empty line and the sentinel, to the Scanner workflow."]], [Plain [Str "Trace the loop condition and state update for every iteration, including end-of-input."]], [Plain [Str "Add an attempt limit and a clear exit command to prevent an infinite prompt loop."]], [Plain [Str "Test that continue skips only the intended processing step and does not skip required updates."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]], Header 3 ("lesson-54-using-continue-in-loops", ["unnumbered", "unlisted"], []) [Str "Lesson 5.4: Using continue in Loops"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 documentation"] ("https://docs.oracle.com/en/java/", ""), Str "."]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", ""), Str "."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the purpose and vocabulary of using continue in loops."]], [Plain [Str "Apply the relevant Java syntax and APIs in a small, complete program."]], [Plain [Str "Compile, run, inspect, and adapt the example using keyboard-accessible tools."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "This lesson develops using continue in loops through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens."], Para [Str "Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "public class Lesson_5_4 {
    public static void main(String[] args) {
        for (int value = 1; value <= 8; value++) {
            if (value % 2 == 0) continue;
            System.out.println(\"odd=\" + value);
        }
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating using continue in loops. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Mixing nextInt/next with nextLine without consuming the pending line terminator."]], [Plain [Str "Writing a sentinel loop that fails to stop at the sentinel or does not handle end-of-input."]], [Plain [Str "Using continue or break in a way that skips required state updates and creates a nonterminating loop."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Feed several lines of input, including an empty line and the sentinel, to the Scanner workflow."]], [Plain [Str "Trace the loop condition and state update for every iteration, including end-of-input."]], [Plain [Str "Add an attempt limit and a clear exit command to prevent an infinite prompt loop."]], [Plain [Str "Test that continue skips only the intended processing step and does not skip required updates."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]], Header 3 ("lesson-55-avoiding-infinite-loops", ["unnumbered", "unlisted"], []) [Str "Lesson 5.5: Avoiding Infinite Loops"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 5.5: Avoiding Infinite Loops"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Identify what makes a loop stop."]], [Plain [Str "Add an attempt limit and handle the end of input."]], [Plain [Str "Use ", Code ("", [], []) "do ... while", Str "."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "An ", Emph [Str "infinite loop"], Str " never ends because its condition never becomes false. Common causes are forgetting to change the loop variable, testing the wrong variable, and waiting for input that never arrives. In a terminal, stop a running program with Ctrl+C."], Para [Str "Protect every loop with a ", Emph [Str "progress rule"], Str " and a ", Emph [Str "limit"], Str ": count attempts, and stop when the limit is reached or the input ends."], Para [Code ("", [], []) "do { ... } while (condition);", Str " runs the body first and tests afterward, so it always runs at least once; note the semicolon after the condition."], Para [Str "The example allows three attempts to enter a score from 0 to 100. With the typed lines abc, 105, and 88, the first two are rejected and the third is accepted."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.Scanner;

public class Lesson_5_5 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int maxAttempts = 3;
        int attempts = 0;
        Integer score = null;

        while (attempts < maxAttempts && score == null) {
            attempts++;
            System.out.println(\"Enter a score from 0 to 100 (attempt \" + attempts + \" of \" + maxAttempts + \"):\");
            if (!in.hasNextLine()) {
                System.out.println(\"No more input.\");
                break;
            }
            String text = in.nextLine();
            try {
                int number = Integer.parseInt(text.trim());
                if (number >= 0 && number <= 100) {
                    score = number;
                } else {
                    System.out.println(\"Invalid score: \" + text);
                }
            } catch (NumberFormatException e) {
                System.out.println(\"Invalid score: \" + text);
            }
        }

        if (score != null) {
            System.out.println(\"Accepted score: \" + score);
        } else {
            System.out.println(\"No valid score was entered.\");
        }

        int count = 1;
        do {
            System.out.println(count);
            count++;
        } while (count <= 3);
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating avoiding infinite loops. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Mixing nextInt/next with nextLine without consuming the pending line terminator."]], [Plain [Str "Writing a sentinel loop that fails to stop at the sentinel or does not handle end-of-input."]], [Plain [Str "Using continue or break in a way that skips required state updates and creates a nonterminating loop."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Feed several lines of input, including an empty line and the sentinel, to the Scanner workflow."]], [Plain [Str "Trace the loop condition and state update for every iteration, including end-of-input."]], [Plain [Str "Add an attempt limit and a clear exit command to prevent an infinite prompt loop."]], [Plain [Str "Test that continue skips only the intended processing step and does not skip required updates."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]]]