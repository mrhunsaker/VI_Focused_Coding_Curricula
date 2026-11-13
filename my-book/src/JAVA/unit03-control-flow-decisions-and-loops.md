# Unit 3: Control Flow — Decisions and Loops

## Overview

This unit develops control flow — decisions and loops through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

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
```java
public class Lesson_3_1 {
    public static void main(String[] args) {
        int score = 82;
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
    }
}
```

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
    }
}
```

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
    }
}
```

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
    }
}
```

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
    }
}
```

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
