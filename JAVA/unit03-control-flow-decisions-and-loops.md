# Unit 3: Control Flow — Decisions and Loops

## Overview

This unit develops control flow — decisions and loops through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

<<<<<<< HEAD
## Lesson 3.1: Boolean Expressions and if Statements

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of boolean expressions and if statements.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops boolean expressions and if statements through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
=======
## Lesson 3.1: Boolean Expressions and if

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 3.1: Boolean Expressions and if Statements

### Learning Objectives
- Write comparisons and combine them with `&&`, `||`, and `!`.
- Use `if` as a statement and the conditional operator as an expression.
- Explain that a condition must be a `boolean`.

### Concept Explanation

A *Boolean expression* is `true` or `false`. Comparisons use `==`, `!=`, `<`, `<=`, `>`, `>=`, and conditions combine with `&&` (and), `||` (or), and `!` (not). Java never treats 0, an empty string, or `null` as false: a condition must be a real `boolean`.

`&&` and `||` use *short-circuit* evaluation: the right side is evaluated only if it is needed, so `x != null && x.length() > 0` is safe. An `if` statement chooses what to run; the *conditional operator* `condition ? a : b` produces a value.

The shared score is 82. It passes (at least 60), it is in the 80 to 89 range, and it is not at least 90. Java has no range operator, so a range is two comparisons joined with `&&`.

### Worked Example

>>>>>>> 2067a20 (curriculum clearning and updates)
```java
public class Lesson_3_1 {
    public static void main(String[] args) {
        int score = 82;
<<<<<<< HEAD
        boolean inRange = score >= 0 && score <= 100;
        if (inRange && score >= 80) System.out.println("Meets target");
        else System.out.println("Needs review");
=======

        if (score >= 60) {
            System.out.println("Avery passed.");
        } else {
            System.out.println("Avery did not pass.");
        }

        System.out.println(score >= 80 && score < 90);
        System.out.println(score < 60 || score > 100);
        System.out.println(!(score >= 90));

        String label = score >= 90 ? "high" : "not high";
        System.out.println(label);

        String text = null;
        System.out.println(text != null && text.length() > 0);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating boolean expressions and if statements. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using == for String content comparison instead of equals or equalsIgnoreCase.
- Ordering chained score thresholds incorrectly so a higher grade is captured by a lower branch.
- Using an incorrect loop bound, modifying a collection during enhanced iteration, or confusing array length with collection size.
### Activities
1. Test each decision threshold immediately below, at, and above the boundary.
2. Process the four shared scores and verify count, total, and average.
3. Normalize a mixed-case sentence containing leading/trailing whitespace and punctuation.
4. Explain the difference between comparing primitive values and comparing String content.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 3.2: Chained Conditionals

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of chained conditionals.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops chained conditionals through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_3_2 {
    public static void main(String[] args) {
        int score = 77;
        String grade;
        if (score >= 90) grade = "A";
        else if (score >= 80) grade = "B";
        else if (score >= 70) grade = "C";
        else if (score >= 60) grade = "D";
        else grade = "F";
        System.out.println(grade);
=======
### Expected Behavior or Output

The program prints:
```text
Avery passed.
true
false
true
not high
false
```

### Common Mistakes
1. Writing `=` where `==` is meant. Inside an `if` this does not compile for numbers.
2. Using `&` or `|` where `&&` or `||` is intended, which skips short-circuiting.
3. Using `==` to compare `String` contents (Lesson 3.5).

### Activities
1. Change the score to 59 and predict which lines change.
2. Write a condition that is true only for scores from 70 to 79 inclusive.
3. Rewrite the `label` line as an `if` statement.
4. Explain why `if (score)` is not allowed in Java.

### Accessibility Practice

Read each condition aloud with 'greater than or equal to', 'and', 'or', and 'not'. Check that your screen reader announces `&&` and `||` so you do not confuse them with single symbols.

### Skills Checklist
- [ ] I can write comparisons and combine them.
- [ ] I can write `if` and `else`.
- [ ] I can use the conditional operator.
- [ ] I understand short-circuit evaluation.
- [ ] I know conditions must be `boolean`.

---

## Lesson 3.2: Chained Conditions and switch

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 3.2: Chained Conditionals (elif, else)

### Learning Objectives
- Use `else if` to test conditions in order.
- Use a `switch` expression for the same decision.
- Classify the shared grade thresholds and test the boundaries.

### Concept Explanation

Java has no `elif`; write `else if`. Conditions are tested from top to bottom and only the first true branch runs. The shared grade thresholds are 90 or more for A, 80 or more for B, 70 or more for C, 60 or more for D, and anything lower for F, so each later test needs only a lower bound.

A `switch` *expression* can replace a chain when the decision depends on a value. Dividing the score by 10 gives the tens digit, so `switch (score / 10) { case 10, 9 -> "A"; case 8 -> "B"; ... default -> "F"; }` gives the same grades for scores from 0 to 100. Arrow cases do not fall through, and a switch expression must cover every value, which `default` guarantees.

*Boundary scores* sit exactly on or just below a threshold. The scores 90, 89, 80, 79, 70, 69, 60, and 59 check every boundary.

### Worked Example

```java
public class Lesson_3_2 {
    static String classify(int score) {
        if (score >= 90) {
            return "A";
        } else if (score >= 80) {
            return "B";
        } else if (score >= 70) {
            return "C";
        } else if (score >= 60) {
            return "D";
        } else {
            return "F";
        }
    }

    static String classifyWithSwitch(int score) {
        return switch (score / 10) {
            case 10, 9 -> "A";
            case 8 -> "B";
            case 7 -> "C";
            case 6 -> "D";
            default -> "F";
        };
    }

    public static void main(String[] args) {
        int[] scores = {90, 89, 80, 79, 70, 69, 60, 59};
        for (int score : scores) {
            System.out.println(score + " " + classify(score) + " " + classifyWithSwitch(score));
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating chained conditionals. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using == for String content comparison instead of equals or equalsIgnoreCase.
- Ordering chained score thresholds incorrectly so a higher grade is captured by a lower branch.
- Using an incorrect loop bound, modifying a collection during enhanced iteration, or confusing array length with collection size.
### Activities
1. Test each decision threshold immediately below, at, and above the boundary.
2. Process the four shared scores and verify count, total, and average.
3. Normalize a mixed-case sentence containing leading/trailing whitespace and punctuation.
4. Explain the difference between comparing primitive values and comparing String content.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 3.3: Introduction to Lists

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of introduction to lists.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops introduction to lists through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_3_3 {
    public static void main(String[] args) {
        java.util.ArrayList<Integer> scores = new java.util.ArrayList<>(java.util.List.of(76, 88, 91, 84));
        scores.set(0, 80);
        scores.add(95);
        System.out.println(scores);
=======
### Expected Behavior or Output

The program prints:
```text
90 A A
89 B B
80 B B
79 C C
70 C C
69 D D
60 D D
59 F F
```

### Common Mistakes
1. Putting the branches in the wrong order, such as testing `score >= 60` first so every passing score is a D.
2. Using `>` instead of `>=`, so exactly 90 receives a B.
3. Using the `switch (score / 10)` form for scores above 109 or below 0 without a plan; they fall to `default`.

### Activities
1. Trace the score 82 through each branch and say which one runs.
2. Add the scores 100 and 0 to the array and predict their grades.
3. Reorder the branches so `score >= 60` is first, run it, and explain the wrong output.
4. Write `isPassing(int score)` that returns a `boolean`.

### Accessibility Practice

Read the eight output lines in order. Each is a number and two letters, so they are easy to follow by ear and in braille; the two methods must agree on every line.

### Skills Checklist
- [ ] I can write an `else if` chain.
- [ ] I know branch order matters.
- [ ] I can write a `switch` expression.
- [ ] I can choose boundary tests.
- [ ] I can classify with the shared thresholds.

---

## Lesson 3.3: Arrays and Lists

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 3.3: Introduction to Lists

### Learning Objectives
- Create an array and an `ArrayList`.
- Index from 0 and use `length` and `size()`.
- Explain the difference between an array and a list.

### Concept Explanation

An *array* has a fixed length set when it is created: `int[] scores = {82, 91, 76, 88}`. Indexes start at 0, `scores[0]` is the first item, and `scores.length` (no parentheses) is the length. Using an index outside the array throws `ArrayIndexOutOfBoundsException`.

An `ArrayList<Integer>` is a resizable list from `java.util`. It holds objects, so primitives are boxed automatically (`Integer`). Its length is `size()`, and it is read with `get(i)` and changed with `set(i, value)`. `List.of(...)` creates an **immutable** list that throws `UnsupportedOperationException` if you try to change it.

`Arrays.toString(array)` and `list.toString()` give a readable one-line form. The shared list is 82, 91, 76, 88; Python uses the same 0-based indexes.

### Worked Example

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Lesson_3_3 {
    public static void main(String[] args) {
        int[] array = {82, 91, 76, 88};
        System.out.println(array[0] + " " + array[array.length - 1] + " " + array.length);
        array[2] = 80;
        System.out.println(Arrays.toString(array));

        List<Integer> scores = new ArrayList<>(List.of(82, 91, 76, 88));
        System.out.println(scores.get(0) + " " + scores.get(scores.size() - 1) + " " + scores.size());
        scores.set(2, 80);
        System.out.println(scores);

        List<Integer> fixed = List.of(82, 91, 76, 88);
        try {
            fixed.set(0, 100);
        } catch (UnsupportedOperationException e) {
            System.out.println("List.of cannot be changed");
        }

        try {
            System.out.println(array[10]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Index 10 is outside the array");
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating introduction to lists. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using == for String content comparison instead of equals or equalsIgnoreCase.
- Ordering chained score thresholds incorrectly so a higher grade is captured by a lower branch.
- Using an incorrect loop bound, modifying a collection during enhanced iteration, or confusing array length with collection size.
### Activities
1. Test each decision threshold immediately below, at, and above the boundary.
2. Process the four shared scores and verify count, total, and average.
3. Normalize a mixed-case sentence containing leading/trailing whitespace and punctuation.
4. Explain the difference between comparing primitive values and comparing String content.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 3.4: Iterating with for Loops

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of iterating with for loops.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops iterating with for loops through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_3_4 {
    public static void main(String[] args) {
        int[] scores = {76, 88, 91, 84};
        int total = 0;
        for (int score : scores) total += score;
        double average = (double) total / scores.length;
        System.out.printf("total=%d average=%.2f%n", total, average);
=======
### Expected Behavior or Output

The program prints:
```text
82 88 4
[82, 91, 80, 88]
82 88 4
[82, 91, 80, 88]
List.of cannot be changed
Index 10 is outside the array
```

### Common Mistakes
1. Using `array.length()` or `list.length`. The array uses `length` and the list uses `size()`.
2. Using index 1 for the first item. The first item is at index 0.
3. Trying to change a list made by `List.of`, which throws.

### Activities
1. Predict each output line before running.
2. Replace the second score with 95 in both the array and the list and print them.
3. Make a copy of the list with `new ArrayList<>(scores)` and show that changing the original does not change the copy.
4. Explain when an array is better than a list and when a list is better.

### Accessibility Practice

Print a whole collection on one line and its size on another, so the screen reader announces a complete state in one pass. When reading `scores[0]` aloud, say 'scores, open bracket, zero, close bracket'.

### Skills Checklist
- [ ] I can create arrays and lists.
- [ ] I can index from 0.
- [ ] I know `length` versus `size()`.
- [ ] I know `List.of` is immutable.
- [ ] I can copy a list.

---

## Lesson 3.4: Loops

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 3.4: Iterating with for Loops

### Learning Objectives
- Use the classic `for`, the enhanced `for`, and `while`.
- Visit a list by value and by index.
- Compute the total and average of the shared scores.

### Concept Explanation

The *classic* `for` has three parts: `for (int i = 0; i < scores.size(); i++)` sets a start, a condition, and a step. Use it when you need the index. The *enhanced* `for`, `for (int score : scores)`, visits every element without an index and works for arrays and lists. A `while (condition)` loop repeats while the condition is true.

Streams can summarize a list without a loop: `scores.stream().mapToInt(Integer::intValue).sum()`. A loop is still the way to learn what such a call does.

The shared scores 82, 91, 76, 88 total 337 and average 84.25. Dividing two `int` values truncates, so convert one side to `double` first.

### Worked Example

```java
import java.util.List;

public class Lesson_3_4 {
    public static void main(String[] args) {
        List<Integer> scores = List.of(82, 91, 76, 88);
        int total = 0;
        for (int i = 0; i < scores.size(); i++) {
            System.out.println("Adding score " + (i + 1) + ": " + scores.get(i));
            total += scores.get(i);
        }
        System.out.println("Total: " + total);
        System.out.println("Average: " + (double) total / scores.size());
        System.out.println("Same total with a stream: " + scores.stream().mapToInt(Integer::intValue).sum());

        for (int score : scores) {
            if (score > 85) {
                System.out.println("Above 85: " + score);
            }
        }

        int count = 3;
        while (count > 0) {
            System.out.println("Countdown: " + count);
            count--;
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating iterating with for loops. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using == for String content comparison instead of equals or equalsIgnoreCase.
- Ordering chained score thresholds incorrectly so a higher grade is captured by a lower branch.
- Using an incorrect loop bound, modifying a collection during enhanced iteration, or confusing array length with collection size.
### Activities
1. Test each decision threshold immediately below, at, and above the boundary.
2. Process the four shared scores and verify count, total, and average.
3. Normalize a mixed-case sentence containing leading/trailing whitespace and punctuation.
4. Explain the difference between comparing primitive values and comparing String content.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 3.5: Basic String Operations

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of basic string operations.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops basic string operations through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Boolean conditions evaluate to true or false; Java does not implicitly convert numbers or references to booleans. Loops need a clear initialization, continuation condition, and state update. Guard sentinel and input loops against end-of-file and malformed tokens.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_3_5 {
    public static void main(String[] args) {
        String sentence = "  Java makes text processing explicit.  ";
        String normalized = sentence.trim().toLowerCase();
        System.out.println(normalized);
        System.out.println("characters=" + normalized.length());
        System.out.println("contains java=" + normalized.contains("java"));
=======
### Expected Behavior or Output

The program prints:
```text
Adding score 1: 82
Adding score 2: 91
Adding score 3: 76
Adding score 4: 88
Total: 337
Average: 84.25
Same total with a stream: 337
Above 85: 91
Above 85: 88
Countdown: 3
Countdown: 2
Countdown: 1
```

### Common Mistakes
1. Writing `i <= scores.size()`, which reads one position past the end.
2. Dividing the `int` total by the size and getting a truncated result.
3. Removing from a list inside an enhanced `for`, which throws `ConcurrentModificationException`.

### Activities
1. Predict the last six output lines before running.
2. Change the loop to print only the scores above 80.
3. Write a loop that counts from 20 down to 0 by 5.
4. Explain why the average prints `84.25` and not `84`.

### Accessibility Practice

Each output line starts with a label and a number, so the running total is read step by step. Count the lines to confirm that the loop ran four times.

### Skills Checklist
- [ ] I can write classic and enhanced `for` loops.
- [ ] I can write a `while` loop.
- [ ] I can total and average a list.
- [ ] I can avoid the off-by-one error.
- [ ] I can use a stream to sum.

---

## Lesson 3.5: Strings

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 3.5: Basic String Operations

### Learning Objectives
- Use `length`, `toLowerCase`, `contains`, `indexOf`, and `strip`.
- Compare strings with `equals`, not `==`.
- Normalize a name and search the shared text sample.

### Concept Explanation

A `String` is an immutable sequence of characters. `length()` is its size and `charAt(0)` is the first character. Methods such as `toUpperCase()` return a **new** string and never change the original.

Useful methods: `strip()` (trim whitespace), `contains(text)`, `indexOf(text)` (which returns `-1` when the text is missing), `substring(start, end)`, `replace`, `startsWith`, and `split(regex)`.

**Compare strings with `equals`, never `==`.** `==` compares whether two variables refer to the *same object*, which can be false even when the text is identical. `equalsIgnoreCase` ignores case.

The shared text sample is "A student studies programming. Programming develops problem-solving skills." It has 75 characters and contains `programming` twice (once in each case), first found at index 18 after lowercasing.

### Worked Example

```java
import java.util.regex.Pattern;

public class Lesson_3_5 {
    public static void main(String[] args) {
        String rawName = "  avery  ";
        String stripped = rawName.strip();
        String cleanName = stripped.substring(0, 1).toUpperCase() + stripped.substring(1);
        System.out.println("Name: '" + cleanName + "'");

        String text = "A student studies programming. Programming develops problem-solving skills.";
        String lowered = text.toLowerCase();
        System.out.println("Characters: " + text.length());
        System.out.println("Contains 'programming': " + lowered.contains("programming"));
        System.out.println("First index of 'programming': " + lowered.indexOf("programming"));
        System.out.println("Times 'programming' appears: " + Pattern.compile("programming").matcher(lowered).results().count());
        System.out.println("Missing word index: " + lowered.indexOf("java"));

        String a = new String("Avery");
        String b = new String("Avery");
        System.out.println(a == b);
        System.out.println(a.equals(b));
        System.out.println(a.equalsIgnoreCase("AVERY"));
        System.out.println(text.toUpperCase().substring(0, 9));
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating basic string operations. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using == for String content comparison instead of equals or equalsIgnoreCase.
- Ordering chained score thresholds incorrectly so a higher grade is captured by a lower branch.
- Using an incorrect loop bound, modifying a collection during enhanced iteration, or confusing array length with collection size.
### Activities
1. Test each decision threshold immediately below, at, and above the boundary.
2. Process the four shared scores and verify count, total, and average.
3. Normalize a mixed-case sentence containing leading/trailing whitespace and punctuation.
4. Explain the difference between comparing primitive values and comparing String content.
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
Name: 'Avery'
Characters: 75
Contains 'programming': true
First index of 'programming': 18
Times 'programming' appears: 2
Missing word index: -1
false
true
true
A STUDENT
```

### Common Mistakes
1. Comparing strings with `==`, which compares object identity.
2. Expecting `text.toUpperCase()` to change `text`. Assign or print the result.
3. Treating `indexOf` as an error when it returns `-1`.

### Activities
1. Predict the printed values, then run and compare.
2. Find the index of the word `student` in the sample text.
3. Replace every `programming` with `coding` and print the result.
4. Write code that strips and capitalizes `"  riley  "`.

### Accessibility Practice

Strings with many quotation marks are hard to read by ear. Say 'single quote' and 'double quote' aloud when checking a line, and print results inside labelled sentences so values are not run together.

### Skills Checklist
- [ ] I can use common `String` methods.
- [ ] I compare strings with `equals`.
- [ ] I can search text and find positions.
- [ ] I can strip and capitalize a name.
- [ ] I know strings are immutable.

---
>>>>>>> 2067a20 (curriculum clearning and updates)
