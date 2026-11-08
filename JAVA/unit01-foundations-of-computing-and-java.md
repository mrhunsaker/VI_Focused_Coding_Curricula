# Unit 1: Foundations of Computing and Java

## Overview

This unit develops foundations of computing and java through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 1.1: Welcome to Computer Science

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of welcome to computer science.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops welcome to computer science through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_1_1 {
    public static void main(String[] args) {
        String[] steps = {"identify the problem", "design an algorithm", "test the result"};
        for (int i = 0; i < steps.length; i++) System.out.println((i + 1) + ". " + steps[i]);
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 1.1: Welcome to Computer Science

### Learning Objectives
- Explain hardware, software, and algorithm in your own words.
- Turn a written algorithm into a short Java program.
- Predict a program's output by hand before running it.

### Concept Explanation

Computers follow instructions exactly. *Hardware* is the machine, *software* is the set of instructions it follows, and an *algorithm* is an ordered, finite list of clear steps that solves a problem. Unit P of this repository covers these ideas in detail.

A reliable way to solve a problem is to understand it, break it into steps, write the steps in plain language, translate them into code, and test the result.

The plan here is: set a total to zero; for each score, add it to the total; divide the total by the number of scores; report both. In Java, `int[] scores = {...}` creates an array of whole numbers, `for (int score : scores)` visits each one in order, and `scores.length` is the number of items.

The shared scores are 82, 91, 76, and 88. Their total is 337 and their average is 84.25. A hand trace should reach the same numbers: 82, 173, 249, then 337.

### Worked Example

```java
public class Lesson_1_1 {
    public static void main(String[] args) {
        int[] scores = {82, 91, 76, 88};
        int total = 0;
        for (int score : scores) {
            total += score;
        }
        double average = (double) total / scores.length;
        System.out.println("Total: " + total);
        System.out.println("Average: " + average);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating welcome to computer science. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Treating Java primitive values and object references as interchangeable types.
- Using an incorrect public class/file-name pairing or omitting the main entry-point signature.
- Reading an uninitialized local variable or narrowing a numeric value without checking for data loss.
### Activities
1. Explain the hardware/software or algorithmic context, then express the steps as ordered Java statements.
2. Change the learner profile values and identify the compile-time types of each field.
3. Add a constant and a safe numeric conversion, then explain what information could be lost.
4. Compile and run from the terminal after deliberately introducing and correcting one syntax error.
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
Total: 337
Average: 84.25
```

### Common Mistakes
1. Writing code before writing the steps, then forgetting to divide by the number of scores.
2. Dividing two `int` values and expecting a decimal. `337 / 4` is `84`; cast one side with `(double)`.
3. Writing `scores.length()` with parentheses. For an array, `length` is a field, not a method.

### Activities
1. Trace the loop by hand and write the running total after each score.
2. Change the array to 90 and 80 and predict the total and average before running.
3. Add a loop that finds the highest score and prints it.
4. Explain the difference between the algorithm and the program in two sentences.

### Accessibility Practice

Write the hand trace as numbered sentences, one for each loop pass, and read it back with your screen reader. Compare it with the two printed lines in order.

### Skills Checklist
- [ ] I can define hardware, software, and algorithm.
- [ ] I can describe an algorithm as ordered steps.
- [ ] I can trace a loop by hand.
- [ ] I can explain `(double)` in the average.
- [ ] I can run the program and compare it with my trace.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 1.2: Your First Java Program

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of your first java program.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops your first java program through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_1_2 {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
        System.out.println("A class contains the program entry point.");
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 1.2: Your First Python Program - Hello World

### Learning Objectives
- Write and run a program that prints text.
- Use comments, `printf`, and a text block.
- Explain that statements run in order.

### Concept Explanation

A Java program is a list of statements that run in order inside `main`. `System.out.println` writes text and ends the line, and `System.out.print` writes without ending the line. Text in double quotation marks is a `String`, and `+` joins strings.

`System.out.printf(format, values...)` inserts values into a template: `%d` is a whole number, `%s` is text, `%.2f` is a decimal with two places, and `%n` is a line ending that is right for the platform. A *text block* written with three quotation marks (`"""`) spans several lines and removes the common indentation. A line comment starts with `//` and a block comment is written between `/*` and `*/`.

Because Java is compiled, a mistake such as a missing quotation mark is reported at compile time and no program is produced.

### Worked Example

```java
public class Lesson_1_2 {
    public static void main(String[] args) {
        // This program greets the shared student.
        String name = "Avery";
        System.out.println("Hello, " + name + "!");
        System.out.print("No new line here, ");
        System.out.println("then one here.");
        System.out.printf("Name has %d letters.%n", name.length());

        String text = """
            Two lines
            in one text block.""";
        System.out.println(text);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating your first java program. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Treating Java primitive values and object references as interchangeable types.
- Using an incorrect public class/file-name pairing or omitting the main entry-point signature.
- Reading an uninitialized local variable or narrowing a numeric value without checking for data loss.
### Activities
1. Explain the hardware/software or algorithmic context, then express the steps as ordered Java statements.
2. Change the learner profile values and identify the compile-time types of each field.
3. Add a constant and a safe numeric conversion, then explain what information could be lost.
4. Compile and run from the terminal after deliberately introducing and correcting one syntax error.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 1.3: Variables and Primitive Data Types

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of variables and primitive data types.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops variables and primitive data types through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_1_3 {
    public static void main(String[] args) {
        String learner = "Avery";
        int age = 16;
        double heightMeters = 1.68;
        char grade = 'A';
        boolean enrolled = true;
        System.out.printf("%s %d %.2f %c %b%n", learner, age, heightMeters, grade, enrolled);
=======
### Expected Behavior or Output

The program prints:
```text
Hello, Avery!
No new line here, then one here.
Name has 5 letters.
Two lines
in one text block.
```

### Common Mistakes
1. Using a curly quotation mark pasted from a document instead of a straight one, which is a syntax error.
2. Using `\n` in `printf` where `%n` is the portable line ending.
3. Forgetting that `print` does not end the line.

### Activities
1. Run the program and describe how the second and third lines differ from the others.
2. Change the greeting to use your own name and predict the output.
3. Print three lines: your name, the course name, and today's task.
4. Add a comment above every line and read the file aloud with the comments.

### Accessibility Practice

Run from the terminal and read the output line by line. Check that your screen reader announces the percent signs in a `printf` template, since they decide what the program prints.

### Skills Checklist
- [ ] I can write and run a program that prints text.
- [ ] I can use `printf` formats.
- [ ] I can write comments.
- [ ] I know how `print` and `println` differ.
- [ ] I can read a first compile error.

---

## Lesson 1.3: Variables and Simple Data Types

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 1.3: Variables and Simple Data Types

### Learning Objectives
- Declare variables of the basic types.
- Explain primitive versus reference types and `null`.
- Use `final` and `var`.

### Concept Explanation

Java is *statically typed*: every variable has a type that the compiler knows. The *primitive* types are `int` and `long` (whole numbers), `double` and `float` (decimals), `boolean`, and `char`. `String` is a *reference* type: the variable refers to an object, and a reference may be `null`, which means "no object". Primitives are never null.

`final` makes a variable assignable only once. `var` lets the compiler infer the type of a local variable from its initializer (`var inferred = 16L;` is a `long`); the type is still fixed. A whole-number literal such as 16 is an `int` and 1.72 is a `double`; a trailing `L` makes a `long`.

Wrapper classes such as `Integer` and `Double` turn a primitive into an object when one is needed, for example in a collection.

The shared student profile is Avery, 16, 1.72 meters, and Computer Science. The shared Notebook item has quantity 3 and unit price 2.50, so three notebooks cost 7.5.

### Worked Example

```java
public class Lesson_1_3 {
    public static void main(String[] args) {
        String name = "Avery";
        int age = 16;
        double height = 1.72;
        String favoriteSubject = "Computer Science";
        boolean likesCs = true;
        System.out.println(name + ", " + age + ", " + height + ", " + favoriteSubject + ", " + likesCs);

        var inferred = 16L;
        Object boxedAge = age;
        Object boxedHeight = height;
        Object boxedInferred = inferred;
        System.out.println(boxedAge.getClass().getSimpleName() + " " + boxedHeight.getClass().getSimpleName()
            + " " + boxedInferred.getClass().getSimpleName());

        final double notebookPrice = 2.50;
        int notebookQuantity = 3;
        System.out.println("Notebook total: " + notebookPrice * notebookQuantity);

        int visits = 1;
        visits++;
        System.out.println("Visits: " + visits);

        Integer none = null;
        System.out.println(none);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating variables and primitive data types. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Treating Java primitive values and object references as interchangeable types.
- Using an incorrect public class/file-name pairing or omitting the main entry-point signature.
- Reading an uninitialized local variable or narrowing a numeric value without checking for data loss.
### Activities
1. Explain the hardware/software or algorithmic context, then express the steps as ordered Java statements.
2. Change the learner profile values and identify the compile-time types of each field.
3. Add a constant and a safe numeric conversion, then explain what information could be lost.
4. Compile and run from the terminal after deliberately introducing and correcting one syntax error.
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
Avery, 16, 1.72, Computer Science, true
Integer Double Long
Notebook total: 7.5
Visits: 2
null
```

### Common Mistakes
1. Assigning to a `final` variable a second time, which is a compile error.
2. Using a `null` reference as if it were an object, which throws `NullPointerException`.
3. Writing `long big = 3000000000;`. The literal is an `int` that is too large; write `3000000000L`.

### Activities
1. Run the example and write each type name in the order printed.
2. Change `age` to `16L` in the declaration and fix the compile error that results.
3. Add a `char` initial for the student and print it.
4. Explain, without code, why `int` can never be null but `Integer` can.

### Accessibility Practice

Say names with their capital letters aloud (`favoriteSubject`) and print each value inside a labelled sentence so the screen reader announces the name and the value together.

### Skills Checklist
- [ ] I can declare variables of the basic types.
- [ ] I can explain primitive versus reference types.
- [ ] I can use `final` and `var`.
- [ ] I know a reference can be null.
- [ ] I can explain why literals have types.

---
>>>>>>> 2067a20 (curriculum clearning and updates)
