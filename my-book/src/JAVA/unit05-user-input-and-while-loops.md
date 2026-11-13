# Unit 5: User Input and while Loops

## Overview

This unit develops user input and while loops through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 5.1: How Console Input Works

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 5.1: How the input() Function Works

### Learning Objectives
- Read a line and recognize it as text.
- Convert it safely and handle failure.
- Handle the end of input.

### Concept Explanation

`Scanner.nextLine()` returns the next line as a `String`. A program must check `hasNextLine()` first, because at the end of input `nextLine()` throws. It never returns a number: typed digits are text until you convert them. `Integer.parseInt` converts text and throws `NumberFormatException` when the text is not a whole number.

A program that reads input must plan for three cases: a valid value, an invalid value, and no value at all. The example uses a small `next` helper that returns `null` at the end of input, and a `toInt` helper that returns `null` for bad text. With the typed value 16 the age five years later is 21; the second value, `abc`, is rejected.

### Worked Example

```java
import java.util.Scanner;

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
        System.out.println("How old are you?");
        String text = next(in);
        System.out.println("Read: " + (text == null ? "nothing" : text.getClass().getSimpleName()));

        Integer age = toInt(text);
        if (age != null) {
            System.out.println("In 5 years: " + (age + 5));
        } else {
            System.out.println("That was not a whole number.");
        }

        System.out.println("Enter another value:");
        Integer second = toInt(next(in));
        if (second != null) {
            System.out.println("Number: " + second);
        } else {
            System.out.println("Not a number; toInt returned null.");
        }
    }
}
```

**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating how scanner input works. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Mixing nextInt/next with nextLine without consuming the pending line terminator.
- Writing a sentinel loop that fails to stop at the sentinel or does not handle end-of-input.
- Using continue or break in a way that skips required state updates and creates a nonterminating loop.
### Activities
1. Feed several lines of input, including an empty line and the sentinel, to the Scanner workflow.
2. Trace the loop condition and state update for every iteration, including end-of-input.
3. Add an attempt limit and a clear exit command to prevent an infinite prompt loop.
4. Test that continue skips only the intended processing step and does not skip required updates.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 5.2: The while Loop in Action

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of the while loop in action.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops the while loop in action through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_5_2 {
    public static void main(String[] args) {
        java.util.Scanner input = new java.util.Scanner("3 2 1 0");
        int count = 0;
        while (input.hasNextInt()) {
            int value = input.nextInt();
            if (value == 0) break;
            count += value;
        }
        System.out.println("sum before sentinel=" + count);
        input.close();
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
hello
scores
quit
```

the program prints:
```text
1
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
```

With no standard input at all, the program ends cleanly and prints:
```text
1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit:
Goodbye!
```

### Common Mistakes
1. Forgetting to change the loop variable, which creates an endless loop.
2. Testing for `quit` but not for `null`, so the loop reads forever after input ends.
3. Comparing with `message == "quit"` instead of `equals`.

### Activities
1. Predict the output for the typed lines hello, scores, and quit.
2. Change the sentinel to `exit` and update the prompt.
3. Count the messages entered and print the count at the end.
4. Rewrite the counting loop as a `for` loop and compare.

### Accessibility Practice

Each prompt is on its own line and each response begins with `You said:`, so the conversation can be followed in order by ear. If a loop floods the screen reader, stop it with Ctrl+C.

### Skills Checklist
- [ ] I can write a counting `while` loop.
- [ ] I can write a sentinel loop.
- [ ] I test for `null` as well as the sentinel.
- [ ] I update the loop variable.
- [ ] I compare strings with `equals`.

---

## Lesson 5.3: Flags, break, and Labels

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 5.3: Using Flags and break to Exit Loops

### Learning Objectives
- Control a loop with a Boolean flag.
- Leave a loop with `break` and an outer loop with a label.
- Search a list and remember the position.

### Concept Explanation

A *flag* is a `boolean` variable that controls a loop: the loop runs while `running` is true, and the body sets it to `false` to stop. `break` leaves the nearest enclosing loop at once.

A search keeps its answer in a variable (here `-1` means "not found"), sets it when the item is found, and uses `break`. After the loop, the variable says whether a match was found. List positions start at 0.

A *label* lets `break` leave an outer loop from inside an inner one: write `outer:` before the outer loop and `break outer;` inside.

The shared scores 82, 91, 76, 88 have their first score of 90 or higher at index 1, with the value 91.

### Worked Example

```java
import java.util.List;
import java.util.Scanner;

public class Lesson_5_3 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        boolean running = true;
        int handled = 0;
        while (running) {
            System.out.println("Say something, or type quit to stop:");
            String message = in.hasNextLine() ? in.nextLine() : null;
            if (message == null || message.equals("quit")) {
                running = false;
            } else {
                handled++;
                System.out.println("You said: " + message);
            }
        }
        System.out.println("Messages handled: " + handled);

        List<Integer> scores = List.of(82, 91, 76, 88);
        int foundIndex = -1;
        for (int i = 0; i < scores.size(); i++) {
            if (scores.get(i) >= 90) {
                foundIndex = i;
                break;
            }
        }
        if (foundIndex >= 0) {
            System.out.println("First score of 90 or higher: " + scores.get(foundIndex) + " at index " + foundIndex);
        } else {
            System.out.println("No score of 90 or higher.");
        }

        outer:
        for (int row = 1; row <= 3; row++) {
            for (int col = 1; col <= 3; col++) {
                if (row * col == 4) {
                    System.out.println("Stopped at row " + row + ", column " + col);
                    break outer;
                }
            }
        }
    }
}
```

**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating using flags and break to exit loops. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Mixing nextInt/next with nextLine without consuming the pending line terminator.
- Writing a sentinel loop that fails to stop at the sentinel or does not handle end-of-input.
- Using continue or break in a way that skips required state updates and creates a nonterminating loop.
### Activities
1. Feed several lines of input, including an empty line and the sentinel, to the Scanner workflow.
2. Trace the loop condition and state update for every iteration, including end-of-input.
3. Add an attempt limit and a clear exit command to prevent an infinite prompt loop.
4. Test that continue skips only the intended processing step and does not skip required updates.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 5.4: Using continue in Loops

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of using continue in loops.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops using continue in loops through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_5_4 {
    public static void main(String[] args) {
        for (int value = 1; value <= 8; value++) {
            if (value % 2 == 0) continue;
            System.out.println("odd=" + value);
        }
    }
}
```

**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating using continue in loops. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Mixing nextInt/next with nextLine without consuming the pending line terminator.
- Writing a sentinel loop that fails to stop at the sentinel or does not handle end-of-input.
- Using continue or break in a way that skips required state updates and creates a nonterminating loop.
### Activities
1. Feed several lines of input, including an empty line and the sentinel, to the Scanner workflow.
2. Trace the loop condition and state update for every iteration, including end-of-input.
3. Add an attempt limit and a clear exit command to prevent an infinite prompt loop.
4. Test that continue skips only the intended processing step and does not skip required updates.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 5.5: Avoiding Infinite Loops

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 5.5: Avoiding Infinite Loops

### Learning Objectives
- Identify what makes a loop stop.
- Add an attempt limit and handle the end of input.
- Use `do ... while`.

### Concept Explanation

An *infinite loop* never ends because its condition never becomes false. Common causes are forgetting to change the loop variable, testing the wrong variable, and waiting for input that never arrives. In a terminal, stop a running program with Ctrl+C.

Protect every loop with a *progress rule* and a *limit*: count attempts, and stop when the limit is reached or the input ends.

`do { ... } while (condition);` runs the body first and tests afterward, so it always runs at least once; note the semicolon after the condition.

The example allows three attempts to enter a score from 0 to 100. With the typed lines abc, 105, and 88, the first two are rejected and the third is accepted.

### Worked Example

```java
import java.util.Scanner;

public class Lesson_5_5 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int maxAttempts = 3;
        int attempts = 0;
        Integer score = null;

        while (attempts < maxAttempts && score == null) {
            attempts++;
            System.out.println("Enter a score from 0 to 100 (attempt " + attempts + " of " + maxAttempts + "):");
            if (!in.hasNextLine()) {
                System.out.println("No more input.");
                break;
            }
            String text = in.nextLine();
            try {
                int number = Integer.parseInt(text.trim());
                if (number >= 0 && number <= 100) {
                    score = number;
                } else {
                    System.out.println("Invalid score: " + text);
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid score: " + text);
            }
        }

        if (score != null) {
            System.out.println("Accepted score: " + score);
        } else {
            System.out.println("No valid score was entered.");
        }

        int count = 1;
        do {
            System.out.println(count);
            count++;
        } while (count <= 3);
    }
}
```

**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating avoiding infinite loops. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Mixing nextInt/next with nextLine without consuming the pending line terminator.
- Writing a sentinel loop that fails to stop at the sentinel or does not handle end-of-input.
- Using continue or break in a way that skips required state updates and creates a nonterminating loop.
### Activities
1. Feed several lines of input, including an empty line and the sentinel, to the Scanner workflow.
2. Trace the loop condition and state update for every iteration, including end-of-input.
3. Add an attempt limit and a clear exit command to prevent an infinite prompt loop.
4. Test that continue skips only the intended processing step and does not skip required updates.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.
