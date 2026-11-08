# Unit 5: User Input and while Loops

## Overview

This unit develops user input and while loops through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

<<<<<<< HEAD
## Lesson 5.1: How Scanner Input Works

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of how scanner input works.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops how scanner input works through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_5_1 {
    public static void main(String[] args) {
        java.util.Scanner input = new java.util.Scanner("Avery\n17\n");
        System.out.print("Name: ");
        String name = input.nextLine();
        int age = Integer.parseInt(input.nextLine());
        System.out.println(name + " will be " + (age + 1));
        input.close();
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
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
=======
### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
16
abc
```

the program prints:
```text
How old are you?
Read: String
In 5 years: 21
Enter another value:
Not a number; toInt returned null.
```

With no standard input at all, the program ends cleanly and prints:
```text
How old are you?
Read: nothing
That was not a whole number.
Enter another value:
Not a number; toInt returned null.
```

### Common Mistakes
1. Adding to the text without converting it, which joins strings instead of adding.
2. Calling `nextLine()` at the end of input and crashing.
3. Using `Integer.parseInt` on user input and crashing on `abc`.

### Activities
1. Run with 16 and then `abc` and compare with the shown output.
2. Run with no input and explain every line printed.
3. Accept an age only from 0 to 120.
4. Rewrite the program using `nextInt()` and describe what happens with `abc`.

### Accessibility Practice

Each prompt is a complete sentence on its own line. Run the program twice, once typing and once with piped input, and compare what your screen reader announces.

### Skills Checklist
- [ ] I can read a line of input.
- [ ] I can convert and validate it.
- [ ] I handle the end of input.
- [ ] I know typed input is text.
- [ ] I can write a clear prompt.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 5.2: The while Loop in Action

### Reading References
<<<<<<< HEAD
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
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 5.2: The while Loop in Action

### Learning Objectives
- Write a counting `while` loop.
- Write a sentinel loop that ends on a command.
- Stop at the end of input.

### Concept Explanation

`while (condition) { ... }` repeats while the condition is true, testing **before** each pass. A loop needs a way to make its condition false, normally by changing a variable inside the body: `count++` adds one.

A *sentinel* is a special input that tells the loop to stop, here the word `quit`. The standard pattern reads once before the loop and again at the end of each pass, and tests for `null` as well, so the loop ends when input runs out even without `quit`. Compare strings with `equals`: `"quit".equals(message)` is safe even when `message` is `null`.

The example counts from 1 to 5, then repeats a message prompt until the user types `quit`.

### Worked Example

```java
import java.util.Scanner;

public class Lesson_5_2 {
    public static void main(String[] args) {
        int count = 1;
        while (count <= 5) {
            System.out.println(count);
            count++;
        }
        System.out.println("Counting finished!");

        Scanner in = new Scanner(System.in);
        System.out.println("Enter a message, or type quit to exit:");
        String message = in.hasNextLine() ? in.nextLine() : null;
        while (message != null && !"quit".equals(message)) {
            System.out.println("You said: " + message);
            System.out.println("Enter a message, or type quit to exit:");
            message = in.hasNextLine() ? in.nextLine() : null;
        }
        System.out.println("Goodbye!");
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating the while loop in action. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

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

## Lesson 5.3: Using Flags and break to Exit Loops

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of using flags and break to exit loops.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops using flags and break to exit loops through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_5_3 {
    public static void main(String[] args) {
        java.util.Scanner input = new java.util.Scanner("open stop ignored");
        boolean finished = false;
        while (input.hasNext() && !finished) {
            String command = input.next();
            if (command.equals("stop")) { finished = true; break; }
            System.out.println("command=" + command);
        }
        System.out.println("finished=" + finished);
        input.close();
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
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
=======
### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
hello
quit
ignored
```

the program prints:
```text
Say something, or type quit to stop:
You said: hello
Say something, or type quit to stop:
Messages handled: 1
First score of 90 or higher: 91 at index 1
Stopped at row 2, column 2
```

With no standard input at all, the program ends cleanly and prints:
```text
Say something, or type quit to stop:
Messages handled: 0
First score of 90 or higher: 91 at index 1
Stopped at row 2, column 2
```

### Common Mistakes
1. Setting the flag but running more code in the same pass that should be skipped.
2. Forgetting to give the result variable a starting value, then misreading it after the loop.
3. Using `break` in an inner loop and expecting it to leave the outer loop.

### Activities
1. Run with hello and quit and confirm the count is 1.
2. Change the search to the first score below 80 and predict the index.
3. Rewrite the first loop without a flag, using `break`.
4. Explain in two sentences when a flag is clearer than `break`.

### Accessibility Practice

Report search results as complete sentences that include both the value and its position. Remember that Java indexes start at 0, and say 'index 1' aloud to avoid confusing it with 'the first'.

### Skills Checklist
- [ ] I can control a loop with a flag.
- [ ] I can use `break`.
- [ ] I can use a label to leave an outer loop.
- [ ] I can search a list and keep the position.
- [ ] I can explain flag versus `break`.

---

## Lesson 5.4: Skipping Entries with continue

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 5.4: Using continue in Loops

### Learning Objectives
- Skip one pass of a loop with `continue`.
- Skip invalid scores in a list.
- Compare `continue` with filtering.

### Concept Explanation

`continue` skips the rest of the current pass and goes straight to the next one. It is useful for ignoring invalid entries while still reporting them. In a `while` loop, make sure that the loop variable is updated *before* `continue`, or the loop never ends.

A stream can filter first: `scores.stream().filter(s -> s >= 0 && s <= 100)` keeps only the valid scores, which is shorter when you do not need to report each skipped entry.

The example skips the invalid scores -5 and 105 in the list 82, -5, 91, 105, 76, 88. The four valid scores total 337.

### Worked Example

```java
import java.util.List;

public class Lesson_5_4 {
    public static void main(String[] args) {
        List<Integer> rawScores = List.of(82, -5, 91, 105, 76, 88);
        int validTotal = 0;
        int validCount = 0;

        for (int raw : rawScores) {
            if (raw < 0 || raw > 100) {
                System.out.println("Skipping invalid score: " + raw);
                continue;
            }
            validTotal += raw;
            validCount++;
        }
        System.out.println("Valid scores: " + validCount + ", total: " + validTotal);

        for (int number = 1; number <= 9; number++) {
            if (number % 2 == 0) {
                continue;
            }
            System.out.println(number);
        }

        System.out.println(rawScores.stream().filter(s -> s >= 0 && s <= 100).mapToInt(Integer::intValue).sum());
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
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
=======
### Expected Behavior or Output

The program prints:
```text
Skipping invalid score: -5
Skipping invalid score: 105
Valid scores: 4, total: 337
1
3
5
7
9
337
```

### Common Mistakes
1. Putting statements that must always run after `continue`, so they are skipped.
2. Using `continue` in a `while` loop before updating the counter, which creates an endless loop.
3. Confusing `continue` (skip this pass) with `break` (leave the loop).

### Activities
1. Predict the printed lines and the final total.
2. Skip scores below 80 instead.
3. Rewrite the first loop with an `if`/`else` and no `continue`.
4. Rewrite it with a stream filter and explain what you no longer report.

### Accessibility Practice

Print a line for each skipped entry, so the screen reader announces what was ignored. Never skip silently when a user needs to know what happened to their data.

### Skills Checklist
- [ ] I can use `continue`.
- [ ] I can skip invalid entries.
- [ ] I know where the counter must be updated.
- [ ] I can use a stream filter as an alternative.
- [ ] I can tell `continue` from `break`.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 5.5: Avoiding Infinite Loops

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of avoiding infinite loops.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops avoiding infinite loops through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_5_5 {
    public static void main(String[] args) {
        int attempts = 0;
        while (attempts < 3) {
            attempts++;
            System.out.println("attempt " + attempts);
        }
        System.out.println("loop ended at " + attempts);
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
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
=======
### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
abc
105
88
```

the program prints:
```text
Enter a score from 0 to 100 (attempt 1 of 3):
Invalid score: abc
Enter a score from 0 to 100 (attempt 2 of 3):
Invalid score: 105
Enter a score from 0 to 100 (attempt 3 of 3):
Accepted score: 88
1
2
3
```

With no standard input at all, the program ends cleanly and prints:
```text
Enter a score from 0 to 100 (attempt 1 of 3):
No more input.
No valid score was entered.
1
2
3
```

### Common Mistakes
1. Forgetting to increase `attempts`, so the limit is never reached.
2. Calling `nextLine()` without `hasNextLine()`, so a closed input stream crashes the program.
3. Forgetting the semicolon after `while (...)` in a `do` loop.

### Activities
1. Run with abc, 105, and 88 and confirm the accepted score.
2. Run with three invalid lines and read the final message.
3. Change the limit to 5 and test it.
4. For each loop in the example, write down what makes it stop.

### Accessibility Practice

A loop that cannot be stopped is an accessibility problem, because it can flood a screen reader with output. Learn Ctrl+C before running loops, give every input loop a limit, and write error messages that say what is valid.

### Skills Checklist
- [ ] I can name what ends each loop.
- [ ] I can add an attempt limit.
- [ ] I handle the end of input.
- [ ] I can use `do ... while`.
- [ ] I know how to interrupt a program.

---
>>>>>>> 2067a20 (curriculum clearning and updates)
