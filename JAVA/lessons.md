# Java Curriculum — Complete Lesson Set

<<<<<<< HEAD
**Language baseline:** Java SE 25 LTS, JDK 25. Examples avoid preview features and third-party dependencies unless a lesson explicitly discusses an optional library.

=======
**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

**Language baseline:** Java SE 25 LTS, JDK 25. Examples avoid preview features and third-party dependencies unless a lesson explicitly discusses an optional library.

**Verification status:** every lesson has one complete Java program that uses the shared datasets. All 57 programs compile with `javac` and run independently with empty standard input (checked on JDK 21; the baseline is JDK 25), and the "Expected Behavior or Output" blocks are the captured output of those programs, with the standard input shown where a program reads input. This has not been tested with screen readers or braille displays. Java prints the shared tip as 3.68 because its formatter rounds half up; Python, C, Go, and several other languages print 3.67 for the same stored value.

>>>>>>> 2067a20 (curriculum clearning and updates)
This file is the consolidated, lesson-by-lesson teaching sequence for Java. The existing grouped unit files remain supplementary reference material; this file provides the complete standardized sequence and independently runnable examples.

## Course outcomes

Learners will install and verify a JDK, use an accessible editor and terminal, write and compile Java programs, reason about static types, use control flow and collections, decompose problems into methods and classes, handle files and exceptions, test behavior, and build an accessible command-line personal data manager.

# Unit 0: Accessible Java Development Environment

<<<<<<< HEAD
## Lesson 0.1: Installing and Verifying JDK 25

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).
- [Eclipse Temurin JDK distributions](https://adoptium.net/).

### Learning Objectives
- Explain the purpose and vocabulary of installing and verifying jdk 25.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
Install a full JDK 25 distribution and verify java, javac, and JShell from a terminal.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_0_1 {
    public static void main(String[] args) {
        java.util.List<String> milestones = java.util.List.of("model", "implement", "test", "document", "demonstrate");
        for (String milestone : milestones) System.out.println("Completed: " + milestone);
=======
## Overview

Set up the language toolchain, a project folder, and a keyboard-first editor workflow that can be read with speech or braille, and learn how projects and dependencies are organized.

---

## Lesson 0.1: Installing the JDK

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java SE 25 documentation](https://docs.oracle.com/en/java/)
- Matching Python lesson: Lesson 0.1: Installing Python and uv

### Learning Objectives
- Install a JDK from a trusted source.
- Verify `java` and `javac` from the terminal.
- Compile and run a first program.

### Concept Explanation

Java programs are compiled to *bytecode* by `javac` and run by the Java Virtual Machine, started with `java`. Both tools come in the **JDK** (Java Development Kit). A JRE alone can run programs but cannot compile them. This course's documented baseline is JDK 25 (a long-term-support release); the examples avoid preview features and run on earlier recent releases too, but check the version you install.

Install a JDK from your operating system's package manager or from a vendor distribution, and write down which route you used. Then verify it:
```text
java -version
javac -version
```
Both commands must print a version, and they should report the same major number. If `java` works but `javac` is not found, only a runtime is installed. If the numbers differ, an old Java is earlier on your PATH.

To compile and run the example below, save it as `Lesson_0_1.java` (the file name must match the public class name exactly, including capital letters), then:
```text
javac Lesson_0_1.java
java Lesson_0_1
```

### Worked Example

```java
public class Lesson_0_1 {
    public static void main(String[] args) {
        System.out.println("Java toolchain ready.");
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating installing and verifying jdk 25. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Installing a JRE-only runtime instead of a full JDK that includes javac.
- Assuming editor extensions, terminal PATH, and configured project runtime automatically use the same JDK.
- Depending on a visual project explorer or color highlighting without verifying source paths and terminal commands.
### Activities
1. Verify the JDK, compiler, and runtime versions independently from both the system terminal and IDE terminal.
2. Navigate to the source file and run the same compile/run sequence without using editor buttons.
3. Use keyboard navigation and a screen reader to locate one compiler diagnostic and its source line.
4. Write a short setup checklist that another learner can reproduce.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 0.2: Configuring VS Code or Theia for Java

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).
- [Eclipse Temurin JDK distributions](https://adoptium.net/).

### Learning Objectives
- Explain the purpose and vocabulary of configuring vs code or theia for java.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
Configure Java language support, diagnostics, debugging, testing, keyboard navigation, and screen-reader mode.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_0_2 {
    public static void main(String[] args) {
        java.util.List<String> milestones = java.util.List.of("model", "implement", "test", "document", "demonstrate");
        for (String milestone : milestones) System.out.println("Completed: " + milestone);
=======
### Expected Behavior or Output

The program prints:
```text
Java toolchain ready.
```

### Common Mistakes
1. Installing only a runtime, so `javac` is not found.
2. Saving the file under a name that does not match the public class, which is a compile error.
3. Running `java Lesson_0_1.java` (source mode) and `java Lesson_0_1` (compiled class) and not noticing they are different routes.

### Activities
1. Install the JDK and record the exact output of both version commands.
2. Compile and run the example from the keyboard and list the files `javac` created.
3. Rename the file to `lesson.java`, compile it, and write down the error message.
4. Explain in two sentences the difference between the JDK, the JRE, and the JVM.

### Accessibility Practice

Run each command from the keyboard and read the output line by line with your screen reader. Confirm that the version numbers are announced digit by digit. Compiler messages name the file and line first, so jump to the first line of output to find the cause.

### Skills Checklist
- [ ] I can install a JDK.
- [ ] I can verify `java` and `javac`.
- [ ] I can compile and run a first program.
- [ ] I know the file name must match the public class.
- [ ] I can say which route I used.

---

## Lesson 0.2: Workspace and First Run

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 0.2: Configuring Your Screen Reader for VS Code or Theia IDE

### Learning Objectives
- Create a project folder with a first source file.
- Compile and run it from the terminal.
- Read a compiler error and find the file, line, and message.

### Concept Explanation

A *project folder* keeps one program's files together. Create a folder named `java-course`, save the source file inside it, and open a terminal in that folder (the *working directory*).

Every Java program starts at `public static void main(String[] args)` inside a class. Statements end with semicolons and blocks are enclosed in braces. Compile and run from the working directory:
```text
javac Lesson_0_2.java
java Lesson_0_2
```
JDK 11 and later can also compile and run a single file in one step with `java Lesson_0_2.java`, which is convenient for small examples; larger programs use `javac` and a class path.

If a file contains a mistake, `javac` prints `Lesson_0_2.java:5: error: ...`, then the offending line and a caret that marks the position. Read the file name and line first, then the message. Fix the first error before the others, because later errors are often caused by it.

### Worked Example

```java
public class Lesson_0_2 {
    public static void main(String[] args) {
        System.out.println("Hello, Avery!");
        System.out.println("Welcome to Java programming!");
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating configuring vs code or theia for java. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Installing a JRE-only runtime instead of a full JDK that includes javac.
- Assuming editor extensions, terminal PATH, and configured project runtime automatically use the same JDK.
- Depending on a visual project explorer or color highlighting without verifying source paths and terminal commands.
### Activities
1. Verify the JDK, compiler, and runtime versions independently from both the system terminal and IDE terminal.
2. Navigate to the source file and run the same compile/run sequence without using editor buttons.
3. Use keyboard navigation and a screen reader to locate one compiler diagnostic and its source line.
4. Write a short setup checklist that another learner can reproduce.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 0.3: Creating a Workspace and First Java Project

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).
- [Eclipse Temurin JDK distributions](https://adoptium.net/).

### Learning Objectives
- Explain the purpose and vocabulary of creating a workspace and first java project.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
Create a predictable project folder, source file, class, and terminal-based compile/run workflow.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_0_3 {
    public static void main(String[] args) {
        java.util.List<String> milestones = java.util.List.of("model", "implement", "test", "document", "demonstrate");
        for (String milestone : milestones) System.out.println("Completed: " + milestone);
=======
### Expected Behavior or Output

The program prints:
```text
Hello, Avery!
Welcome to Java programming!
```

### Common Mistakes
1. Running the commands from a different folder, so the compiler cannot find the file.
2. Fixing the last error message first. Start with the first one.
3. Forgetting a semicolon or a closing brace, which produces several confusing messages from one cause.

### Activities
1. Create the folder and file from the keyboard and run the program. Record the working directory.
2. Delete the closing quotation mark on one line, compile, and write down the file, line, and message. Then restore it.
3. Add a third `println` with your own name and predict the output before running.
4. Run the program with `java Lesson_0_2.java` and compare it with the two-step route.

### Accessibility Practice

Create the folder and file with terminal commands or your editor's keyboard commands. When the compiler reports an error, read the file name and line number first, then jump to that line in the editor. The caret line under the error is easy to miss, so ask your screen reader to read it by character.

### Skills Checklist
- [ ] I can create a project folder and source file.
- [ ] I can compile and run from the terminal.
- [ ] I can read the file and line of an error.
- [ ] I know a class needs a `main` method to start.
- [ ] I know what the working directory is.

---

## Lesson 0.3: Editor Extensions and Reading Java Aloud

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 0.3: Setting Up Your VS Code or Theia IDE Workspace

### Learning Objectives
- Configure an editor so Java source is readable by speech or braille.
- Choose a punctuation level that announces the symbols Java depends on.
- Read generics, lambdas, and method references aloud.

### Concept Explanation

Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md) first. Then adapt the editor for Java. A Java language extension is optional; the course works with a plain editor and the terminal. If you install one, take it only from a source you trust and read the permissions it requests.

Java depends on punctuation that a screen reader may skip at low settings. Learn to say these: `;` ends a statement, `{ }` hold blocks, `( )` hold parameters and arguments, `[ ]` index arrays, `< >` hold *generic* types (`List<String>` is "a list of strings", and `<>` alone is the *diamond*), `->` separates a lambda's parameters from its body, `::` makes a *method reference*, `@Override` is an *annotation*, and `?` and `:` form the *conditional operator*.

Java structure comes from braces, not indentation, so count the closing braces when you read a nested block.

Read the example aloud: "List open angle bracket String close angle bracket names equals new ArrayList open angle bracket close angle bracket open parenthesis close parenthesis semicolon." Then say what it prints.

### Worked Example

```java
import java.util.ArrayList;
import java.util.List;

public class Lesson_0_3 {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>();
        names.add("Avery");
        names.forEach(name -> System.out.println(name.length()));
        names.forEach(System.out::println);

        String missing = null;
        System.out.println(missing == null ? "no value" : missing);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating creating a workspace and first java project. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Installing a JRE-only runtime instead of a full JDK that includes javac.
- Assuming editor extensions, terminal PATH, and configured project runtime automatically use the same JDK.
- Depending on a visual project explorer or color highlighting without verifying source paths and terminal commands.
### Activities
1. Verify the JDK, compiler, and runtime versions independently from both the system terminal and IDE terminal.
2. Navigate to the source file and run the same compile/run sequence without using editor buttons.
3. Use keyboard navigation and a screen reader to locate one compiler diagnostic and its source line.
4. Write a short setup checklist that another learner can reproduce.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 0.4: Terminal, Packages, and Build-Tool Foundations

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).
- [Eclipse Temurin JDK distributions](https://adoptium.net/).

### Learning Objectives
- Explain the purpose and vocabulary of terminal, packages, and build-tool foundations.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
Navigate the project from the terminal, understand package paths and classpaths, and introduce Maven or Gradle wrappers only when needed.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_0_4 {
    public static void main(String[] args) {
        java.util.List<String> milestones = java.util.List.of("model", "implement", "test", "document", "demonstrate");
        for (String milestone : milestones) System.out.println("Completed: " + milestone);
=======
### Expected Behavior or Output

The program prints:
```text
5
Avery
no value
```

### Common Mistakes
1. Setting punctuation so low that `<`, `>`, and `->` are never spoken, then misreading generics or lambdas.
2. Relying on indentation alone to see where a block ends. Count the closing braces.
3. Installing several overlapping extensions and getting duplicate diagnostics.

### Activities
1. Test your editor with the example and record the punctuation level at which every symbol is announced.
2. Navigate the file by line, word, and character and note the commands you used.
3. Remove a closing brace, save, and find how your editor reports it. Then restore it.
4. Write a half-page note of your edit, compile, and run steps using only the keyboard.

### Accessibility Practice

This whole lesson is accessibility practice. Verify that you can open the file, move to a given line, read a line character by character, compile in the terminal, and read the output. Record the operating system, editor, and access technology you actually tested; do not describe the setup as verified for other combinations.

### Skills Checklist
- [ ] I can configure my editor for keyboard-only use.
- [ ] I can hear every symbol in a generic type.
- [ ] I can read a lambda and a method reference aloud.
- [ ] I know Java structure comes from braces.
- [ ] I can compile and read the output from the keyboard.

---

## Lesson 0.4: Java Toolchain, Terminal, and Command-Line Arguments

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 0.4: Python Environments, Terminal Usage, and Accessibility Tools

### Learning Objectives
- Run a program with command-line arguments.
- Describe the project root and the class path.
- Explain when a build tool is needed.

### Concept Explanation

A *command-line argument* is an extra word typed after the program name. `main(String[] args)` receives them in the array `args`. This is the simplest way to pass input without a prompt, and it is easy to test.

Keep each project in its own folder and run commands from the *project root*. The *class path* tells Java where to find compiled classes; `-cp .` means "the current folder". For a single file the commands from Lesson 0.2 are enough. When a project has many files, packages, or libraries, use a build tool such as Maven or Gradle and commit its wrapper so that every machine builds the same way. Do not add a build tool to a one-file exercise.

Compile and run this lesson's program with arguments:
```text
javac Lesson_0_4.java
java Lesson_0_4 red blue
```

### Worked Example

```java
public class Lesson_0_4 {
    public static void main(String[] args) {
        System.out.println("Argument count: " + args.length);
        for (int i = 0; i < args.length; i++) {
            System.out.println("Argument " + (i + 1) + ": " + args[i]);
        }
        if (args.length == 0) {
            System.out.println("No arguments were given.");
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating terminal, packages, and build-tool foundations. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Installing a JRE-only runtime instead of a full JDK that includes javac.
- Assuming editor extensions, terminal PATH, and configured project runtime automatically use the same JDK.
- Depending on a visual project explorer or color highlighting without verifying source paths and terminal commands.
### Activities
1. Verify the JDK, compiler, and runtime versions independently from both the system terminal and IDE terminal.
2. Navigate to the source file and run the same compile/run sequence without using editor buttons.
3. Use keyboard navigation and a screen reader to locate one compiler diagnostic and its source line.
4. Write a short setup checklist that another learner can reproduce.
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

Run with the command-line arguments `red blue`.

The program prints:
```text
Argument count: 2
Argument 1: red
Argument 2: blue
```

With no arguments it prints:
```text
Argument count: 0
No arguments were given.
```

### Common Mistakes
1. Reading `args[0]` when no arguments were given, which throws `ArrayIndexOutOfBoundsException`.
2. Counting arguments from 1. The first argument is at index 0.
3. Adding a build tool to a single-file exercise, which adds files and steps that are not needed.

### Activities
1. Run the program with `red blue` and then with no arguments. Compare the output.
2. Pass three words and a number and print the number plus one.
3. Print the arguments in reverse order.
4. Explain when a project needs Maven or Gradle and when it does not.

### Accessibility Practice

Arguments let you test a program without answering prompts, so every run produces plain text read in order. Read the output of the two runs aloud and compare them line by line.

### Skills Checklist
- [ ] I can run a program with arguments.
- [ ] I know `args` starts at index 0.
- [ ] I can say where the project root is.
- [ ] I know what the class path is for.
- [ ] I know when a build tool is needed.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

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

# Unit 2: Numeric Computations

## Overview

This unit develops numeric computations through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 2.1: The Software Development Process

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of the software development process.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops the software development process through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Use numeric types deliberately: integer division truncates, floating-point calculations can round, parsing may throw NumberFormatException, and Math exposes constants and operations such as PI, sqrt, pow, and hypot.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_2_1 {
    public static void main(String[] args) {
        double subtotal = 48.50;
        double tipRate = 0.18;
        double tip = subtotal * tipRate;
        double total = subtotal + tip;
        System.out.printf("Tip: $%.2f; total: $%.2f%n", tip, total);
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 2.1: The Software Development Process

### Learning Objectives
- Describe the design, implement, and test cycle.
- Write pseudocode for the tip calculator and implement it.
- Explain why money is formatted to two decimals and how the locale matters.

### Concept Explanation

Software is built in a cycle: understand the problem, design a solution, implement it, test it, and refine it. For the tip calculator the plan is: get the bill, calculate 15 percent of it as the tip, add the tip to the bill for the total, and print the tip and the total.

With the shared values (bill 24.50, tip rate 0.15) the exact tip is 3.675 and the total is 28.175. `String.format("%.2f", x)` formats a number with two decimals. Java's formatter rounds **half up** using the decimal digits of the `double`, so Java prints the tip as **3.68**; Python, C, Go, and several other languages print 3.67 for the same stored number. Both are correct displays of the same value.

Formatting uses the default *locale*. In a locale that writes decimals with a comma, `%.2f` prints a comma. Passing `Locale.US` as the first argument gives fixed output, which the example does through a small helper method.

### Worked Example

```java
import java.util.Locale;

public class Lesson_2_1 {
    static String money(double value) {
        return String.format(Locale.US, "%.2f", value);
    }

    public static void main(String[] args) {
        double bill = 24.5;
        double tipRate = 0.15;

        double tip = bill * tipRate;
        double total = bill + tip;

        System.out.println("Bill: " + money(bill));
        System.out.println("Tip: " + money(tip));
        System.out.println("Total: " + money(total));
        System.out.println("Unformatted tip: " + tip);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating the software development process. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using integer division where a decimal result is required, or applying an expression in the wrong order.
- Assuming Scanner parsing accepts malformed input or forgetting the newline left by token-based reads.
- Using an unchecked parse result or rounding intermediate Math values before the final calculation.
### Activities
1. Calculate the same tip, conversion, or circle result using hand arithmetic and Java, then compare precision.
2. Test zero, a negative value, and a nonnumeric string; document which should be accepted.
3. Compare integer and floating-point division using the same operands.
4. Add a validation message and verify it does not print a misleading result.
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
Bill: 24.50
Tip: 3.68
Total: 28.18
Unformatted tip: 3.675
```

### Common Mistakes
1. Writing the rate as 15 instead of 0.15, which makes the tip fifteen times too large.
2. Rounding the tip first and then adding it, which can change the total by a cent.
3. Assuming every language prints the same two-decimal text for 3.675.

### Activities
1. Trace the plan with the shared values and write each result as a sentence.
2. Change the rate to 0.20 and predict the tip and total (4.90 and 29.40).
3. Add a test for a bill of 100 with a written expected result before running.
4. Explain in two sentences why Java prints 3.68 even though the stored value is just below 3.675.

### Accessibility Practice

Print each result on its own labelled line (`Tip: 3.68`) so a screen reader announces one clear unit per line. Never use alignment or spacing to carry meaning.

### Skills Checklist
- [ ] I can name the stages of the development cycle.
- [ ] I can write pseudocode for a calculation.
- [ ] I can format a number with `String.format`.
- [ ] I know formatting depends on the locale.
- [ ] I can explain why displays can differ between languages.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 2.2: Expressions and Assignment

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of expressions and assignment.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops expressions and assignment through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Use numeric types deliberately: integer division truncates, floating-point calculations can round, parsing may throw NumberFormatException, and Math exposes constants and operations such as PI, sqrt, pow, and hypot.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_2_2 {
    public static void main(String[] args) {
        int score = 82;
        score += 8;
        score *= 2;
        System.out.println("Updated score: " + score);
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 2.2: Elements of Programs - Expressions and Assignment

### Learning Objectives
- Evaluate expressions using operator precedence.
- Predict integer division, remainder, and string joining.
- Use compound assignment.

### Concept Explanation

An *expression* produces a value. The arithmetic operators are `+`, `-`, `*`, `/`, and `%` (remainder). Multiplication, division, and remainder happen before addition and subtraction, and parentheses change the order, so `8 + 4 * 2` is 16 and `(8 + 4) * 2` is 24.

**Division depends on the types.** Two `int` values give an `int`, with the fraction dropped toward zero, so `7 / 2` is `3` and `-7 / 2` is `-3`. If either side is a `double`, the result is a `double`: `7 / 2.0` is `3.5`. The remainder keeps the sign of the left side, so `-7 % 2` is `-1`.

*Assignment* stores a value: `score = score + 9`, shortened to `score += 9`. `+` also joins strings, and the order matters: `1 + 2 + "3"` adds first and gives `"33"`, while `"1" + 2 + 3` joins left to right and gives `"123"`. Comparison uses `==`, `!=`, `<`, `<=`, `>`, and `>=`.

### Worked Example

```java
public class Lesson_2_2 {
    public static void main(String[] args) {
        System.out.println(8 + 4 * 2);
        System.out.println((8 + 4) * 2);

        int score = 82;
        score += 9;
        System.out.println("New score: " + score);

        System.out.println(7 / 2);
        System.out.println(7 / 2.0);
        System.out.println(7 % 2);
        System.out.println(-7 / 2);
        System.out.println(-7 % 2);
        System.out.println(5 != 6);
        System.out.println("Avery" + " " + "Student");
        System.out.println(1 + 2 + "3");
        System.out.println("1" + 2 + 3);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating expressions and assignment. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using integer division where a decimal result is required, or applying an expression in the wrong order.
- Assuming Scanner parsing accepts malformed input or forgetting the newline left by token-based reads.
- Using an unchecked parse result or rounding intermediate Math values before the final calculation.
### Activities
1. Calculate the same tip, conversion, or circle result using hand arithmetic and Java, then compare precision.
2. Test zero, a negative value, and a nonnumeric string; document which should be accepted.
3. Compare integer and floating-point division using the same operands.
4. Add a validation message and verify it does not print a misleading result.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 2.3: Input and Output Revisited

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of input and output revisited.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops input and output revisited through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Use numeric types deliberately: integer division truncates, floating-point calculations can round, parsing may throw NumberFormatException, and Math exposes constants and operations such as PI, sqrt, pow, and hypot.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_2_3 {
    public static void main(String[] args) {
        java.util.Scanner input = new java.util.Scanner("Avery\n12 30\n");
        String name = input.nextLine();
        int first = input.nextInt();
        int second = input.nextInt();
        System.out.println("Hello, " + name + "; sum = " + (first + second));
        input.close();
=======
### Expected Behavior or Output

The program prints:
```text
16
24
New score: 91
3
3.5
1
-3
-1
true
Avery Student
33
123
```

### Common Mistakes
1. Expecting `7 / 2` to be `3.5`. With two `int` values the fraction is dropped.
2. Expecting `"1" + 2 + 3` to be `"6"`. Once a string is involved, `+` joins.
3. Writing `score =+ 9` and storing positive nine instead of adding.

### Activities
1. Predict the twelve output lines before running, then compare.
2. Write an expression for the area and the perimeter of a 12 by 8 rectangle.
3. Explain why `-7 / 2` prints `-3` rather than `-4`.
4. Join your name, a space, and your age into one string in two different ways.

### Accessibility Practice

Say operators by name when reading code aloud ('slash', 'percent', 'plus equals'). Raise your punctuation level while checking expressions so that parentheses and operators are all announced.

### Skills Checklist
- [ ] I can apply operator precedence.
- [ ] I can predict `int` and `double` division.
- [ ] I can use `+=` and `%`.
- [ ] I know how `+` joins strings.
- [ ] I can read expressions aloud.

---

## Lesson 2.3: Console Input and Output

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 2.3: Input and Output Revisited

### Learning Objectives
- Read a line with `Scanner`.
- Convert text with `Integer.parseInt` and handle failure.
- Handle missing and invalid input.

### Concept Explanation

`java.util.Scanner` reads from standard input. `hasNextLine()` tells whether another line exists, and `nextLine()` returns it without the line ending. Calling `nextLine()` when there is no line throws `NoSuchElementException`, so check `hasNextLine()` first.

Typed text is always a `String`. `Integer.parseInt(text)` converts it and throws `NumberFormatException` if the text is not a whole number, so wrap it in `try` and `catch` (Lesson 8.3) and return `null` or a message for bad input. A method that may return no number can return the wrapper type `Integer`, which can be `null`.

The example reads a name and two numbers and prints a greeting and their sum. With Avery, 12, and 8 the sum is 20. Prompts are printed on their own lines so the screen reader reads each cleanly.

### Worked Example

```java
import java.util.Scanner;

public class Lesson_2_3 {
    static Integer readNumber(Scanner in) {
        if (!in.hasNextLine()) {
            return null;
        }
        try {
            return Integer.parseInt(in.nextLine().trim());
        } catch (NumberFormatException e) {
            return null;
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter your name:");
        String name = in.hasNextLine() ? in.nextLine() : null;
        System.out.println("Enter the first number:");
        Integer first = readNumber(in);
        System.out.println("Enter the second number:");
        Integer second = readNumber(in);

        if (name != null && first != null && second != null) {
            System.out.println("Hello, " + name + "!");
            System.out.println("The sum of " + first + " and " + second + " is " + (first + second) + ".");
        } else {
            System.out.println("Input was missing or not a number.");
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating input and output revisited. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using integer division where a decimal result is required, or applying an expression in the wrong order.
- Assuming Scanner parsing accepts malformed input or forgetting the newline left by token-based reads.
- Using an unchecked parse result or rounding intermediate Math values before the final calculation.
### Activities
1. Calculate the same tip, conversion, or circle result using hand arithmetic and Java, then compare precision.
2. Test zero, a negative value, and a nonnumeric string; document which should be accepted.
3. Compare integer and floating-point division using the same operands.
4. Add a validation message and verify it does not print a misleading result.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 2.4: Computing with Numbers and Type Conversions

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of computing with numbers and type conversions.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops computing with numbers and type conversions through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Use numeric types deliberately: integer division truncates, floating-point calculations can round, parsing may throw NumberFormatException, and Math exposes constants and operations such as PI, sqrt, pow, and hypot.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_2_4 {
    public static void main(String[] args) {
        String ageText = "24";
        int age = Integer.parseInt(ageText);
        double pounds = Double.parseDouble("150.5");
        double kilograms = pounds * 0.45359237;
        System.out.printf("Next year: %d; mass: %.2f kg%n", age + 1, kilograms);
=======
### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
Avery
12
8
```

the program prints:
```text
Enter your name:
Enter the first number:
Enter the second number:
Hello, Avery!
The sum of 12 and 8 is 20.
```

With no standard input at all, the program ends cleanly and prints:
```text
Enter your name:
Enter the first number:
Enter the second number:
Input was missing or not a number.
```

### Common Mistakes
1. Calling `nextLine()` without checking `hasNextLine()` and crashing at the end of input.
2. Calling `Integer.parseInt` on unchecked text and crashing on `abc`.
3. Mixing `nextInt()` and `nextLine()`, which leaves the line ending behind and makes the next `nextLine()` return an empty string.

### Activities
1. Run with Avery, 12, and 8 and confirm the output.
2. Type `twelve` for the first number and explain the result.
3. Run with no input and describe the output.
4. Change the program to subtract the second number from the first.

### Accessibility Practice

Every prompt is a complete sentence on its own line and every result is a complete sentence. When you test, listen for whether the prompt is read in full before you begin to type.

### Skills Checklist
- [ ] I can read a line with `Scanner`.
- [ ] I can convert text with `Integer.parseInt`.
- [ ] I check `hasNextLine()` first.
- [ ] I can write clear prompts.
- [ ] I handle missing and invalid input.

---

## Lesson 2.4: Numbers and Type Conversions

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 2.4: Computing with Numbers and Type Conversions

### Learning Objectives
- Convert between numbers and text.
- Explain truncation by a cast and rounding with `Math.round`.
- Explain why decimal arithmetic is approximate.

### Concept Explanation

`Integer.parseInt` and `Double.parseDouble` convert text to numbers and throw `NumberFormatException` for invalid text. `String.valueOf(x)` or `"" + x` converts a number to text.

A *cast* converts between numeric types: `(int) 3.9` is `3`, because casting a `double` to an `int` **truncates** toward zero. `Math.round(3.5)` rounds to the nearest whole number (halves go up) and returns a `long`. Converting to a narrower type can lose information, so Java requires you to write the cast.

A `double` is a binary approximation. `0.1 + 0.2` is `0.30000000000000004`, not `0.3`; this is correct behavior. Compare decimals with a tolerance and format them for display.

The shared student has age 16 and height 1.72 meters. The example converts text to those values and computes the height in centimeters.

### Worked Example

```java
import java.util.Locale;

public class Lesson_2_4 {
    public static void main(String[] args) {
        int age = Integer.parseInt("16");
        double height = Double.parseDouble("1.72");
        System.out.println(age + " " + height);

        try {
            Integer.parseInt("abc");
        } catch (NumberFormatException e) {
            System.out.println("abc is not a whole number");
        }
        System.out.println(String.valueOf(42) + " is now text");

        System.out.println((int) 3.9);
        System.out.println(Math.round(3.5));
        System.out.println(0.1 + 0.2);

        double heightCm = height * 100;
        System.out.println("Height in centimeters: " + String.format(Locale.US, "%.1f", heightCm));
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating computing with numbers and type conversions. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using integer division where a decimal result is required, or applying an expression in the wrong order.
- Assuming Scanner parsing accepts malformed input or forgetting the newline left by token-based reads.
- Using an unchecked parse result or rounding intermediate Math values before the final calculation.
### Activities
1. Calculate the same tip, conversion, or circle result using hand arithmetic and Java, then compare precision.
2. Test zero, a negative value, and a nonnumeric string; document which should be accepted.
3. Compare integer and floating-point division using the same operands.
4. Add a validation message and verify it does not print a misleading result.
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
16 1.72
abc is not a whole number
42 is now text
3
4
0.30000000000000004
Height in centimeters: 172.0
```

### Common Mistakes
1. Casting with `(int)` and expecting rounding. A cast truncates.
2. Calling `Integer.parseInt` on untrusted text without handling `NumberFormatException`.
3. Comparing decimals with `==` after arithmetic.

### Activities
1. Predict each output line before running, then compare.
2. Check what `Integer.parseInt(" 16 ")` does and explain the result.
3. Write a method that returns `null` for text that is not a number.
4. Explain the difference between `(int) 3.5` and `Math.round(3.5)`.

### Accessibility Practice

Format floating-point results so the screen reader reads short numbers. Read the exception name aloud when you see one, then jump to the line that names your own file.

### Skills Checklist
- [ ] I can convert between numbers and text.
- [ ] I know a cast truncates.
- [ ] I can use `Math.round`.
- [ ] I can handle `NumberFormatException`.
- [ ] I can explain why decimals are approximate.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 2.5: Using the Math Library

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of using the math library.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops using the math library through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Use numeric types deliberately: integer division truncates, floating-point calculations can round, parsing may throw NumberFormatException, and Math exposes constants and operations such as PI, sqrt, pow, and hypot.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_2_5 {
    public static void main(String[] args) {
        double radius = 2.5;
        double area = Math.PI * Math.pow(radius, 2);
        double circumference = 2 * Math.PI * radius;
        double distance = Math.hypot(6, 8);
        System.out.printf("area %.3f; circumference %.3f; distance %.1f%n", area, circumference, distance);
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 2.5: Using the Math Library

### Learning Objectives
- Use `Math.PI`, `Math.sqrt`, `Math.pow`, and `Math.hypot`.
- Compute circle area and circumference.
- Compute the distance from the origin.

### Concept Explanation

The `java.lang.Math` class provides `PI`, `sqrt`, `pow`, `abs`, `max`, `min`, `floor`, `ceil`, and `hypot`. It needs no import because `java.lang` is always available.

For a circle of radius 5 the area is `Math.PI * Math.pow(radius, 2)` (about 78.54) and the circumference is `2 * Math.PI * radius` (about 31.42). `Math.hypot(x, y)` computes the distance from the origin without overflow, so the shared point (3, 4) is 5.0 from the origin.

The math methods take and return `double` (some have `int` forms). `Math.sqrt(81)` returns `9.0`, which prints with a decimal point.

### Worked Example

```java
import java.util.Locale;

public class Lesson_2_5 {
    public static void main(String[] args) {
        double radius = 5.0;
        double area = Math.PI * Math.pow(radius, 2);
        double circumference = 2 * Math.PI * radius;
        System.out.println("Area: " + String.format(Locale.US, "%.2f", area));
        System.out.println("Circumference: " + String.format(Locale.US, "%.2f", circumference));

        System.out.println(Math.sqrt(81));
        System.out.println("Distance from origin: " + String.format(Locale.US, "%.2f", Math.hypot(3, 4)));
        System.out.println(Math.max(82, 91) + " " + Math.min(76, 88) + " " + Math.abs(-5));
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating using the math library. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using integer division where a decimal result is required, or applying an expression in the wrong order.
- Assuming Scanner parsing accepts malformed input or forgetting the newline left by token-based reads.
- Using an unchecked parse result or rounding intermediate Math values before the final calculation.
### Activities
1. Calculate the same tip, conversion, or circle result using hand arithmetic and Java, then compare precision.
2. Test zero, a negative value, and a nonnumeric string; document which should be accepted.
3. Compare integer and floating-point division using the same operands.
4. Add a validation message and verify it does not print a misleading result.
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
Area: 78.54
Circumference: 31.42
9.0
Distance from origin: 5.00
91 76 5
```

### Common Mistakes
1. Writing the area as `Math.PI * radius * 2`; the radius must be squared.
2. Using `^` for a power. In Java `^` is bitwise exclusive-or; use `Math.pow`.
3. Expecting `Math.sqrt(81)` to print `9`. It prints `9.0`.

### Activities
1. Predict each printed line and then run the program.
2. Compute the area for radius 2.5 by hand and with the program.
3. Change the point to (6, 8) and predict the distance before running.
4. Print the larger of two shared scores using `Math.max`.

### Accessibility Practice

Round results with `String.format` so the screen reader announces `78.54` rather than fifteen digits. Say 'dot' aloud in `Math.PI` and `Math.sqrt`.

### Skills Checklist
- [ ] I can use the `Math` class.
- [ ] I can compute circle area and circumference.
- [ ] I can compute distance with `hypot`.
- [ ] I can format results to two decimals.
- [ ] I know `^` is not a power operator in Java.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

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

# Unit 4: Data Structures — Lists and Dictionaries

## Overview

This unit develops data structures — lists and dictionaries through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 4.1: More on Lists

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of more on lists.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops more on lists through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Arrays have fixed length; List and ArrayList provide collection abstractions; Map associates keys with values. List.of creates an unmodifiable list. Use generics to retain element types and choose an implementation whose ordering and lookup behavior match the task.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_4_1 {
    public static void main(String[] args) {
        java.util.ArrayList<String> tasks = new java.util.ArrayList<>(java.util.List.of("read", "practice"));
        tasks.add("review");
        tasks.remove("practice");
        System.out.println(tasks + "; count=" + tasks.size());
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 4.1: More on Lists

### Learning Objectives
- Add, insert, replace, and remove list items.
- Remove by value and by position without confusing them.
- Search a list with `contains` and `indexOf`.

### Concept Explanation

An `ArrayList` changes with `add(value)` (append), `add(index, value)` (insert and shift), `set(index, value)` (replace), `remove(index)` (remove by **position**), and `remove(Object)` (remove the first matching **value**). For a `List<Integer>` the two forms are easy to confuse: `scores.remove(2)` removes the item at position 2, while `scores.remove(Integer.valueOf(76))` removes the number 76. `remove(index)` returns the removed item.

`contains(value)` tests membership and `indexOf(value)` returns the position or `-1`. These searches look at each item in turn, so they take longer for longer lists.

The example applies the same operations as the Python course to the shared scores, from [82, 91, 76, 88] to [82, 85, 93, 88].

### Worked Example

```java
import java.util.ArrayList;
import java.util.List;

public class Lesson_4_1 {
    public static void main(String[] args) {
        List<Integer> scores = new ArrayList<>(List.of(82, 91, 76, 88));

        scores.add(95);
        scores.add(1, 85);
        scores.set(2, 93);
        scores.remove(Integer.valueOf(76));
        int last = scores.remove(scores.size() - 1);

        System.out.println(scores);
        System.out.println(scores.size() + " items; removed " + last);
        System.out.println(scores.contains(88));
        System.out.println(scores.indexOf(88));
        System.out.println(scores.indexOf(100));
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating more on lists. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Assuming ArrayList and arrays have the same resizing behavior or index limits.
- Trying to modify a List created with List.of, which is unmodifiable.
- Assuming Map iteration order without choosing an ordered implementation, or treating a missing key as a stored zero.
### Activities
1. Apply add, update, remove, lookup, and iteration operations to the same inventory data.
2. Compare a fixed-size array, mutable ArrayList, and unmodifiable List.of value.
3. Choose HashMap or LinkedHashMap for a stated ordering requirement and justify the choice.
4. Test a missing key and distinguish null from a legitimate stored value.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 4.2: Organizing Lists

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of organizing lists.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops organizing lists through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Arrays have fixed length; List and ArrayList provide collection abstractions; Map associates keys with values. List.of creates an unmodifiable list. Use generics to retain element types and choose an implementation whose ordering and lookup behavior match the task.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_4_2 {
    public static void main(String[] args) {
        java.util.ArrayList<Integer> scores = new java.util.ArrayList<>(java.util.List.of(91, 72, 88, 65));
        java.util.Collections.sort(scores);
        System.out.println("ascending=" + scores);
        scores.sort(java.util.Comparator.reverseOrder());
        System.out.println("descending=" + scores);
=======
### Expected Behavior or Output

The program prints:
```text
[82, 85, 93, 88]
4 items; removed 95
true
3
-1
```

### Common Mistakes
1. Calling `scores.remove(76)` on a `List<Integer>` and removing position 76 (an error) instead of the value 76.
2. Removing items inside an enhanced `for`, which throws `ConcurrentModificationException`.
3. Calling `List.of(...).add(...)`, which throws because `List.of` is immutable.

### Activities
1. Trace the list after every operation and write each version as a sentence.
2. Remove the first score with `remove(0)` and describe what happens to the others.
3. Remove every score below 80 safely with `removeIf`.
4. Print the position of the first score above 90.

### Accessibility Practice

After every change, print the whole list on one line so the screen reader reads a complete state in one pass. Say the method names aloud and notice how `remove` with an index and `remove` with a value look alike but behave differently.

### Skills Checklist
- [ ] I can add, insert, replace, and remove items.
- [ ] I can tell remove-by-index from remove-by-value.
- [ ] I can search with `contains` and `indexOf`.
- [ ] I know `List.of` is immutable.
- [ ] I can show a list in one line.

---

## Lesson 4.2: Sorting and Organizing Lists

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 4.2: Organizing Lists

### Learning Objectives
- Sort a list ascending and descending.
- Sort a copy so the original is unchanged.
- Sort by a computed key with a `Comparator`.

### Concept Explanation

`Collections.sort(list)` and `list.sort(null)` sort a mutable list **in place** in natural order. `list.sort(Comparator.reverseOrder())` sorts in descending order, and `Collections.reverse(list)` flips the current order. A list made with `List.of` is immutable and cannot be sorted in place.

To keep the original, sort a *copy*: `new ArrayList<>(scores)`. A `Comparator` describes an order: `Comparator.comparingInt(String::length)` sorts words by length, and the sort is *stable*, so words of equal length keep their original order.

The shared scores sort to 76, 82, 88, 91 in ascending order and 91, 88, 82, 76 in descending order.

### Worked Example

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Lesson_4_2 {
    public static void main(String[] args) {
        List<Integer> scores = new ArrayList<>(List.of(82, 91, 76, 88));

        List<Integer> ascending = new ArrayList<>(scores);
        Collections.sort(ascending);
        List<Integer> descending = new ArrayList<>(scores);
        descending.sort(Comparator.reverseOrder());
        System.out.println("Original: " + scores);
        System.out.println("Ascending: " + ascending);
        System.out.println("Descending: " + descending);

        scores.sort(null);
        System.out.println("Sorted in place: " + scores);
        Collections.reverse(scores);
        System.out.println("Reversed in place: " + scores);

        List<String> words = new ArrayList<>(List.of("pencil", "folder", "notebook"));
        Collections.sort(words);
        System.out.println(words);
        words.sort(Comparator.comparingInt(String::length));
        System.out.println(words);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating organizing lists. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Assuming ArrayList and arrays have the same resizing behavior or index limits.
- Trying to modify a List created with List.of, which is unmodifiable.
- Assuming Map iteration order without choosing an ordered implementation, or treating a missing key as a stored zero.
### Activities
1. Apply add, update, remove, lookup, and iteration operations to the same inventory data.
2. Compare a fixed-size array, mutable ArrayList, and unmodifiable List.of value.
3. Choose HashMap or LinkedHashMap for a stated ordering requirement and justify the choice.
4. Test a missing key and distinguish null from a legitimate stored value.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 4.3: Tuples and Immutable Lists

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of tuples and immutable lists.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops tuples and immutable lists through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Arrays have fixed length; List and ArrayList provide collection abstractions; Map associates keys with values. List.of creates an unmodifiable list. Use generics to retain element types and choose an implementation whose ordering and lookup behavior match the task.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_4_3 {
    public static void main(String[] args) {
        java.util.List<String> days = java.util.List.of("Monday", "Tuesday", "Wednesday");
        System.out.println(days.get(0));
        try { days.add("Thursday"); }
        catch (UnsupportedOperationException ex) { System.out.println("List is unmodifiable"); }
=======
### Expected Behavior or Output

The program prints:
```text
Original: [82, 91, 76, 88]
Ascending: [76, 82, 88, 91]
Descending: [91, 88, 82, 76]
Sorted in place: [76, 82, 88, 91]
Reversed in place: [91, 88, 82, 76]
[folder, notebook, pencil]
[folder, pencil, notebook]
```

### Common Mistakes
1. Sorting a list made by `List.of`, which throws `UnsupportedOperationException`.
2. Expecting `Collections.sort` to return a sorted list. It returns nothing and sorts in place.
3. Using a comparator that is not consistent, which can throw `IllegalArgumentException`.

### Activities
1. Predict each printed line before running.
2. Print the scores in descending order without changing the original.
3. Sort the words by their last letter with a `Comparator`.
4. Explain the difference between sorting in place and sorting a copy.

### Accessibility Practice

Print each result on its own labelled line (`Ascending:`, `Descending:`). The first and last numbers are the quickest to check by ear.

### Skills Checklist
- [ ] I can sort ascending and descending.
- [ ] I can sort a copy.
- [ ] I can use a `Comparator`.
- [ ] I can reverse a list.
- [ ] I know why `List.of` cannot be sorted in place.

---

## Lesson 4.3: Records Instead of Tuples

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 4.3: Tuples - Immutable Lists

### Learning Objectives
- Declare a record for a small fixed group of values.
- Read components with accessor methods.
- Unpack a record with a record pattern.

### Concept Explanation

Java has no tuple type. A **record** is a short way to declare an immutable class: `record Point(int x, int y) {}` automatically provides a constructor, read methods named after the components (`p.x()`), `equals`, `hashCode`, and a readable `toString`. A record cannot change after it is created, so to get a changed version you create a new one.

A *record pattern* unpacks a record in one step: `if (p instanceof Point(int x, int y)) { ... }` declares `x` and `y` from the components.

Records can be declared inside a class, or inside a method as *local records*. The shared coordinates are x = 3 and y = 4.

### Worked Example

```java
import java.util.List;

public class Lesson_4_3 {
    record Point(int x, int y) {}

    record MinMax(int low, int high) {}

    static MinMax minMax(List<Integer> values) {
        int low = values.get(0);
        int high = values.get(0);
        for (int value : values) {
            if (value < low) low = value;
            if (value > high) high = value;
        }
        return new MinMax(low, high);
    }

    public static void main(String[] args) {
        Point point = new Point(3, 4);
        System.out.println(point);
        System.out.println(point.x() + " " + point.y());

        Point moved = new Point(point.x(), 10);
        System.out.println(point + " -> " + moved);
        System.out.println(point.equals(new Point(3, 4)));

        if (point instanceof Point(int x, int y)) {
            System.out.println("x=" + x + " y=" + y);
        }

        MinMax range = minMax(List.of(82, 91, 76, 88));
        System.out.println("low=" + range.low() + " high=" + range.high());

        record Profile(String name, int age, double height) {}
        Profile profile = new Profile("Avery", 16, 1.72);
        System.out.println(profile);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating tuples and immutable lists. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Assuming ArrayList and arrays have the same resizing behavior or index limits.
- Trying to modify a List created with List.of, which is unmodifiable.
- Assuming Map iteration order without choosing an ordered implementation, or treating a missing key as a stored zero.
### Activities
1. Apply add, update, remove, lookup, and iteration operations to the same inventory data.
2. Compare a fixed-size array, mutable ArrayList, and unmodifiable List.of value.
3. Choose HashMap or LinkedHashMap for a stated ordering requirement and justify the choice.
4. Test a missing key and distinguish null from a legitimate stored value.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 4.4: Introducing Dictionaries with Map

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of introducing dictionaries with map.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops introducing dictionaries with map through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Arrays have fixed length; List and ArrayList provide collection abstractions; Map associates keys with values. List.of creates an unmodifiable list. Use generics to retain element types and choose an implementation whose ordering and lookup behavior match the task.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_4_4 {
    public static void main(String[] args) {
        java.util.Map<String, Integer> inventory = new java.util.LinkedHashMap<>();
        inventory.put("notebook", 12);
        inventory.put("pen", 30);
        System.out.println("pens=" + inventory.get("pen"));
        System.out.println("missing=" + inventory.getOrDefault("eraser", 0));
=======
### Expected Behavior or Output

The program prints:
```text
Point[x=3, y=4]
3 4
Point[x=3, y=4] -> Point[x=3, y=10]
true
x=3 y=4
low=76 high=91
Profile[name=Avery, age=16, height=1.72]
```

### Common Mistakes
1. Looking for a setter such as `setX`. A record is immutable; create a new record instead.
2. Using `p.x` or `p.getX()`. The accessor is `p.x()`.
3. Using a record when the data needs to change over time, where a normal class is the better choice.

### Activities
1. Predict the output, then run.
2. Create a `Student` record for the shared profile and print it.
3. Write a method that returns a new student one year older.
4. Explain when a record is a better choice than a class.

### Accessibility Practice

Printing a record shows its name and every component, so the screen reader announces `Point[x=3, y=4]` as a complete sentence. Named accessors read better aloud than positions.

### Skills Checklist
- [ ] I can declare a record.
- [ ] I can read components with accessors.
- [ ] I can unpack with a record pattern.
- [ ] I know a record is immutable.
- [ ] I can choose between a record and a class.

---

## Lesson 4.4: Maps

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 4.4: Introducing Dictionaries

### Learning Objectives
- Create a map and read, add, change, and remove entries.
- Handle a missing key with `getOrDefault`.
- Model the shared inventory item with a record.

### Concept Explanation

A `Map<K, V>` pairs keys with values. `put(key, value)` adds or replaces an entry, `get(key)` reads one and returns `null` when the key is missing, `getOrDefault(key, fallback)` supplies a default, `remove(key)` deletes one, `containsKey(key)` tests for a key, and `size()` counts the entries.

There are several map classes. `HashMap` makes no promise about order. `LinkedHashMap` keeps **insertion order**, so output is stable. `TreeMap` keeps keys sorted. A `Map<String, Object>` holds values of different types but loses type checking, so when the fields are known a record is safer; the shared Notebook item is a record.

### Worked Example

```java
import java.util.LinkedHashMap;
import java.util.Map;

public class Lesson_4_4 {
    record Item(String name, int quantity, double unitPrice) {}

    public static void main(String[] args) {
        Map<String, Object> profile = new LinkedHashMap<>();
        profile.put("name", "Avery");
        profile.put("age", 16);
        profile.put("heightM", 1.72);
        profile.put("favoriteSubject", "Computer Science");

        System.out.println(profile.get("name"));
        profile.put("age", 17);
        profile.put("gradeLevel", 11);
        profile.remove("heightM");
        System.out.println(profile);
        System.out.println(profile.get("heightM"));
        System.out.println(profile.getOrDefault("heightM", "unknown"));
        System.out.println(profile.containsKey("gradeLevel"));

        Item item = new Item("Notebook", 3, 2.50);
        Item restocked = new Item(item.name(), item.quantity() + 2, item.unitPrice());
        System.out.println(item);
        System.out.println(restocked);
        System.out.println("Stock value: " + restocked.quantity() * restocked.unitPrice());
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating introducing dictionaries with map. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Assuming ArrayList and arrays have the same resizing behavior or index limits.
- Trying to modify a List created with List.of, which is unmodifiable.
- Assuming Map iteration order without choosing an ordered implementation, or treating a missing key as a stored zero.
### Activities
1. Apply add, update, remove, lookup, and iteration operations to the same inventory data.
2. Compare a fixed-size array, mutable ArrayList, and unmodifiable List.of value.
3. Choose HashMap or LinkedHashMap for a stated ordering requirement and justify the choice.
4. Test a missing key and distinguish null from a legitimate stored value.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 4.5: Looping Through Dictionaries

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of looping through dictionaries.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops looping through dictionaries through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Arrays have fixed length; List and ArrayList provide collection abstractions; Map associates keys with values. List.of creates an unmodifiable list. Use generics to retain element types and choose an implementation whose ordering and lookup behavior match the task.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_4_5 {
    public static void main(String[] args) {
        java.util.Map<String, Integer> scores = new java.util.LinkedHashMap<>();
        scores.put("Avery", 92);
        scores.put("Riley", 85);
        for (var entry : scores.entrySet()) System.out.println(entry.getKey() + ": " + entry.getValue());
=======
### Expected Behavior or Output

The program prints:
```text
Avery
{name=Avery, age=17, favoriteSubject=Computer Science, gradeLevel=11}
null
unknown
true
Item[name=Notebook, quantity=3, unitPrice=2.5]
Item[name=Notebook, quantity=5, unitPrice=2.5]
Stock value: 12.5
```

### Common Mistakes
1. Using a missing key and expecting an error. `get` returns `null`.
2. Calling a method on the `null` returned by `get`, which throws `NullPointerException`.
3. Using a `HashMap` and expecting the same print order every run.

### Activities
1. Predict the printed lines before running.
2. Add a `discount` component to a new record and print the discounted value.
3. Remove `favoriteSubject` and show what `get` returns.
4. Explain why a record is safer than `Map<String, Object>` for a known set of fields.

### Accessibility Practice

Print one entry per line when you need to read a map, because a one-line `{a=1, b=2}` is hard to navigate. Choose key names that read well aloud, such as `unitPrice`.

### Skills Checklist
- [ ] I can create and change a map.
- [ ] I know `get` can return `null`.
- [ ] I can supply a default with `getOrDefault`.
- [ ] I can choose a map class for the order I need.
- [ ] I can model an item with a record.

---

## Lesson 4.5: Traversing Maps

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 4.5: Looping Through Dictionaries

### Learning Objectives
- Visit keys, values, and entries.
- Explain which map classes keep a stable order.
- Sort keys and total the shared inventory.

### Concept Explanation

`map.keySet()` gives the keys, `map.values()` gives the values, and `map.entrySet()` gives key-value pairs: `for (Map.Entry<String, Stock> entry : inventory.entrySet())` with `entry.getKey()` and `entry.getValue()`.

For readable output the order must be stable. `LinkedHashMap` keeps insertion order; `new TreeMap<>(map)` gives alphabetical order; `HashMap` gives neither. Do not add or remove entries while looping over a map.

A stream can total the values: `values().stream().mapToDouble(...).sum()`. The shared inventory is Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25), worth 7.50 + 5.00 + 5.00 = 17.50.

### Worked Example

```java
import java.util.LinkedHashMap;
import java.util.Locale;
import java.util.Map;
import java.util.TreeMap;

public class Lesson_4_5 {
    record Stock(int quantity, double unitPrice) {}

    static String money(double value) {
        return String.format(Locale.US, "%.2f", value);
    }

    public static void main(String[] args) {
        Map<String, Stock> inventory = new LinkedHashMap<>();
        inventory.put("Notebook", new Stock(3, 2.50));
        inventory.put("Pencil", new Stock(10, 0.50));
        inventory.put("Folder", new Stock(4, 1.25));

        System.out.println("Keys:");
        for (String name : inventory.keySet()) {
            System.out.println(name);
        }

        System.out.println("Quantities:");
        for (Stock stock : inventory.values()) {
            System.out.println(stock.quantity());
        }

        double totalValue = 0;
        for (Map.Entry<String, Stock> entry : inventory.entrySet()) {
            Stock stock = entry.getValue();
            double lineValue = stock.quantity() * stock.unitPrice();
            System.out.println(entry.getKey() + ": " + stock.quantity() + " in stock, value " + money(lineValue));
            totalValue += lineValue;
        }
        System.out.println("Total inventory value: " + money(totalValue));

        System.out.println(new TreeMap<>(inventory).keySet());
        System.out.println(inventory.values().stream().mapToDouble(s -> s.quantity() * s.unitPrice()).sum());
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating looping through dictionaries. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Assuming ArrayList and arrays have the same resizing behavior or index limits.
- Trying to modify a List created with List.of, which is unmodifiable.
- Assuming Map iteration order without choosing an ordered implementation, or treating a missing key as a stored zero.
### Activities
1. Apply add, update, remove, lookup, and iteration operations to the same inventory data.
2. Compare a fixed-size array, mutable ArrayList, and unmodifiable List.of value.
3. Choose HashMap or LinkedHashMap for a stated ordering requirement and justify the choice.
4. Test a missing key and distinguish null from a legitimate stored value.
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
Keys:
Notebook
Pencil
Folder
Quantities:
3
10
4
Notebook: 3 in stock, value 7.50
Pencil: 10 in stock, value 5.00
Folder: 4 in stock, value 5.00
Total inventory value: 17.50
[Folder, Notebook, Pencil]
17.5
```

### Common Mistakes
1. Using a `HashMap` and expecting the same order every run.
2. Adding or removing entries while looping, which throws `ConcurrentModificationException`.
3. Calling `entry.getKey` without parentheses. Both accessors are methods.

### Activities
1. Run the example and write the three key-value lines in order.
2. Print only the items with a quantity below 5.
3. Print the items from the highest line value to the lowest.
4. Explain how `TreeMap` differs from `LinkedHashMap`.

### Accessibility Practice

Printing each inventory line as one sentence lets the screen reader announce the name, quantity, and value together. Because the order is stable, you can learn it and compare runs by ear.

### Skills Checklist
- [ ] I can visit keys, values, and entries.
- [ ] I know which maps keep a stable order.
- [ ] I can sort keys with `TreeMap`.
- [ ] I can total with a stream.
- [ ] I can total the shared inventory.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

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

# Unit 6: Functions and Methods

## Overview

This unit develops functions and methods through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 6.1: Defining Methods

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of defining methods.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops defining methods through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. A method signature includes its name and parameter types; Java passes argument values, including copied reference values. Return types are explicit, overloads differ by parameter lists, and varargs use a final array-like parameter.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_6_1 {
    public static void main(String[] args) {
        greet("Avery");
        }
        private static void greet(String name) {
            System.out.println("Hello, " + name + "!");
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 6.1: Defining Functions

### Learning Objectives
- Define and call static methods.
- Pass parameters and return nothing or a value.
- Use a method reference.

### Concept Explanation

In Java a function is a **method** inside a class. A *static* method belongs to the class and is called without an object. A method declaration states its return type, its name, and its typed parameters: `static void showTip(double bill, double tipRate)`. `void` means nothing is returned.

The *parameters* are the names in the definition and the *arguments* are the values you pass. Arguments are matched to parameters by position, and Java passes every argument **by value**: the method receives a copy of a number, or a copy of the reference to an object.

A *method reference* such as `Lesson_6_1::showTip` names a method so that it can be passed around and called later through a functional interface like `BiConsumer`.

### Worked Example

```java
import java.util.Locale;
import java.util.function.BiConsumer;

public class Lesson_6_1 {
    static String money(double value) {
        return String.format(Locale.US, "%.2f", value);
    }

    static void greetUser() {
        System.out.println("Hello, Java programmer!");
    }

    static void greetName(String name) {
        System.out.println("Hello, " + name + "!");
    }

    static void showTip(double bill, double tipRate) {
        double tip = bill * tipRate;
        System.out.println("Tip: " + money(tip));
        System.out.println("Total: " + money(bill + tip));
    }

    public static void main(String[] args) {
        greetUser();
        greetUser();
        greetName("Avery");
        greetName("Riley");
        showTip(24.5, 0.15);

        BiConsumer<Double, Double> reference = Lesson_6_1::showTip;
        reference.accept(100.0, 0.2);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating defining methods. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Confusing a method's parameter list with its return type or omitting a return on one control-flow path.
- Expecting Java to pass primitive variables by reference; arguments are passed by value.
- Placing a varargs parameter before another parameter or using an overload that is ambiguous.
### Activities
1. Extract repeated statements into a named method with an explicit parameter and return contract.
2. Call the method with typical, boundary, and empty collection arguments.
3. Add a method that accepts a List or Map and returns a computed result without modifying the input.
4. Overload a method or add a varargs form, then explain overload resolution.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 6.2: Passing Arguments

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of passing arguments.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops passing arguments through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. A method signature includes its name and parameter types; Java passes argument values, including copied reference values. Return types are explicit, overloads differ by parameter lists, and varargs use a final array-like parameter.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_6_2 {
    public static void main(String[] args) {
        System.out.println("total=" + add(12, 30));
        }
        private static int add(int first, int second) {
            return first + second;
=======
### Expected Behavior or Output

The program prints:
```text
Hello, Java programmer!
Hello, Java programmer!
Hello, Avery!
Hello, Riley!
Tip: 3.68
Total: 28.18
Tip: 20.00
Total: 120.00
```

### Common Mistakes
1. Writing `greetUser;` without parentheses, which is not a call.
2. Passing arguments in the wrong order, such as `showTip(0.15, 24.5)`.
3. Forgetting `static` and then calling the method from `main`, which is a compile error.

### Activities
1. Call `showTip(100.0, 0.2)` yourself and predict both lines.
2. Write `describeStudent(String name, int age)` that prints one sentence.
3. Call `greetName()` with no argument and read the compiler message.
4. Explain the difference between a parameter and an argument.

### Accessibility Practice

Choose method names that read as actions when spoken, such as `showTip`. Print complete sentences from a method so the screen reader announces each call's result separately.

### Skills Checklist
- [ ] I can define and call a static method.
- [ ] I can distinguish parameters from arguments.
- [ ] I know Java passes arguments by value.
- [ ] I can write a method reference.
- [ ] I can read a method signature aloud.

---

## Lesson 6.2: Overloading Instead of Default Arguments

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 6.2: Passing Arguments

### Learning Objectives
- Explain that Java has no default or named arguments.
- Use overloading to supply a default.
- Group related values in a record for readable calls.

### Concept Explanation

Java has no default parameter values and no named arguments. Two techniques give the same result. **Overloading** declares several methods with the same name and different parameter lists: `calculateTotal(double bill)` calls `calculateTotal(bill, 0.15)`. Java chooses the version by the number and types of the arguments.

When a call needs several values, a **record** groups them under names, so the call site is clear: `new TipRequest(24.5, 0.10)` makes the two numbers visible as a bill and a rate. A record can also supply a second constructor with a default.

With the shared bill of 24.50, the total at the default rate 0.15 is 28.18, at 0.20 it is 29.40, and at 0.10 it is 26.95.

### Worked Example

```java
import java.util.Locale;

public class Lesson_6_2 {
    static final double DEFAULT_RATE = 0.15;

    static String money(double value) {
        return String.format(Locale.US, "%.2f", value);
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
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating passing arguments. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Confusing a method's parameter list with its return type or omitting a return on one control-flow path.
- Expecting Java to pass primitive variables by reference; arguments are passed by value.
- Placing a varargs parameter before another parameter or using an overload that is ambiguous.
### Activities
1. Extract repeated statements into a named method with an explicit parameter and return contract.
2. Call the method with typical, boundary, and empty collection arguments.
3. Add a method that accepts a List or Map and returns a computed result without modifying the input.
4. Overload a method or add a varargs form, then explain overload resolution.
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
28.18
29.40
26.95
28.18
```

### Common Mistakes
1. Looking for default values in the parameter list. Java does not have them.
2. Declaring two overloads that differ only in return type, which does not compile.
3. Passing arguments in the wrong order to a method with two `double` parameters, which the compiler cannot detect.

### Activities
1. Predict the four totals before running.
2. Add an overload `calculateTotal(double bill, int percent)` and explain how Java chooses between the overloads.
3. Add a `roundTotal` component to the record.
4. Explain why a record helps a screen reader user.

### Accessibility Practice

A record call reads as a sentence: 'new TipRequest, open parenthesis, bill 24.5, tip rate 0.10'. Say the commas aloud and check that your screen reader announces them.

### Skills Checklist
- [ ] I know Java has no default arguments.
- [ ] I can overload a method.
- [ ] I can group values in a record.
- [ ] I can use a constant for a default.
- [ ] I can read an overloaded call aloud.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 6.3: Return Values

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of return values.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops return values through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. A method signature includes its name and parameter types; Java passes argument values, including copied reference values. Return types are explicit, overloads differ by parameter lists, and varargs use a final array-like parameter.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_6_3 {
    public static void main(String[] args) {
        int[] values = {4, 8, 12};
        System.out.println("average=" + average(values));
        }
        private static double average(int[] values) {
            if (values.length == 0) throw new IllegalArgumentException("values must not be empty");
            int sum = 0;
            for (int value : values) sum += value;
            return (double) sum / values.length;
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 6.3: Return Values

### Learning Objectives
- Return a computed value.
- Return `OptionalDouble` when a value may be missing.
- Return several values with a record.

### Concept Explanation

A method sends a value back with `return`, and its declared return type must match. When a result may not exist, such as the average of an empty list, returning `null` invites a crash. `OptionalDouble` states in the type that a value may be absent: `OptionalDouble.empty()` for no result, `OptionalDouble.of(x)` for a result, and `isPresent()`, `getAsDouble()`, or `orElse(fallback)` to read it.

To return several values, return a record and read its components. The example returns the average of the shared scores, classifies the average, returns a minimum and a maximum together, and shows the empty-list case.

### Worked Example

```java
import java.util.List;
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
        if (score >= 90) return "A";
        if (score >= 80) return "B";
        if (score >= 70) return "C";
        if (score >= 60) return "D";
        return "F";
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
        System.out.println("Average: " + avg);
        if (avg.isPresent()) {
            System.out.println("Grade for the average: " + classify(avg.getAsDouble()));
        }
        ScoreRange range = minMax(scores);
        System.out.println("Lowest and highest: " + range.low() + " and " + range.high());
        System.out.println(average(List.of()));
        System.out.println(average(List.of()).orElse(0.0));
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating return values. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Confusing a method's parameter list with its return type or omitting a return on one control-flow path.
- Expecting Java to pass primitive variables by reference; arguments are passed by value.
- Placing a varargs parameter before another parameter or using an overload that is ambiguous.
### Activities
1. Extract repeated statements into a named method with an explicit parameter and return contract.
2. Call the method with typical, boundary, and empty collection arguments.
3. Add a method that accepts a List or Map and returns a computed result without modifying the input.
4. Overload a method or add a varargs form, then explain overload resolution.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 6.4: Methods with Lists and Maps

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of methods with lists and maps.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops methods with lists and maps through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. A method signature includes its name and parameter types; Java passes argument values, including copied reference values. Return types are explicit, overloads differ by parameter lists, and varargs use a final array-like parameter.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_6_4 {
    public static void main(String[] args) {
        java.util.List<String> names = java.util.List.of("Avery", "Riley", "Jordan");
        printUppercase(names);
        }
        private static void printUppercase(java.util.List<String> names) {
            for (String name : names) System.out.println(name.toUpperCase());
=======
### Expected Behavior or Output

The program prints:
```text
Average: OptionalDouble[84.25]
Grade for the average: B
Lowest and highest: 76 and 91
OptionalDouble.empty
0.0
```

### Common Mistakes
1. Printing inside the method and then trying to use the result in a calculation.
2. Calling `getAsDouble()` on an empty `OptionalDouble`, which throws `NoSuchElementException`.
3. Writing code after a `return` in the same block, which the compiler rejects as unreachable.

### Activities
1. Predict the six printed lines before running.
2. Write `total(List<Integer> list)` that returns the sum.
3. Write `isPassing(int score)` that returns a `boolean`.
4. Explain how a caller should use a method that returns `OptionalDouble`.

### Accessibility Practice

Return values instead of printing inside logic methods, so the caller prints once and the screen reader announces each result a single time.

### Skills Checklist
- [ ] I can return a value.
- [ ] I can return `OptionalDouble` for a possibly missing value.
- [ ] I can return several values with a record.
- [ ] I can use a returned value in a calculation.
- [ ] I can classify an average with the shared thresholds.

---

## Lesson 6.4: Methods with Collections

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 6.4: Functions with Lists and Dictionaries

### Learning Objectives
- Explain that a list argument is a reference passed by value.
- Change a list in a method and protect the original with a copy.
- Process the shared inventory with a method.

### Concept Explanation

Java passes everything **by value**, but for an object the value is a *reference*. A method that receives a `List` can change the caller's list through that reference, so `addScore(scores, 95)` is visible to the caller. Reassigning the parameter inside the method does not change the caller's variable.

To produce a changed list without touching the original, return a *new* list: copy with `new ArrayList<>(list)` and add to the copy. `Collections.unmodifiableList(list)` or `List.copyOf(list)` give read-only versions that protect data from accidental changes.

The shared inventory is Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25), worth 17.50 in total.

### Worked Example

```java
import java.util.ArrayList;
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
        System.out.println(scores.size() + " " + longer.size());

        List<Item> inventory = List.of(
            new Item("Notebook", 3, 2.50),
            new Item("Pencil", 10, 0.50),
            new Item("Folder", 4, 1.25));
        System.out.println("Total inventory value: " + String.format(Locale.US, "%.2f", inventoryValue(inventory)));
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating methods with lists and maps. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Confusing a method's parameter list with its return type or omitting a return on one control-flow path.
- Expecting Java to pass primitive variables by reference; arguments are passed by value.
- Placing a varargs parameter before another parameter or using an overload that is ambiguous.
### Activities
1. Extract repeated statements into a named method with an explicit parameter and return contract.
2. Call the method with typical, boundary, and empty collection arguments.
3. Add a method that accepts a List or Map and returns a computed result without modifying the input.
4. Overload a method or add a varargs form, then explain overload resolution.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 6.5: Arbitrary Number of Arguments

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of arbitrary number of arguments.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops arbitrary number of arguments through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. A method signature includes its name and parameter types; Java passes argument values, including copied reference values. Return types are explicit, overloads differ by parameter lists, and varargs use a final array-like parameter.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_6_5 {
    public static void main(String[] args) {
        System.out.println(sum(2, 4, 6, 8));
        }
        private static int sum(int... values) {
            int total = 0;
            for (int value : values) total += value;
            return total;
=======
### Expected Behavior or Output

The program prints:
```text
[82, 91, 76, 88, 95]
5 6
Total inventory value: 17.50
```

### Common Mistakes
1. Expecting a method to receive its own copy of a list.
2. Changing a list inside a method that was meant only to read it.
3. Passing `List.of(...)` to a method that adds to it, which throws `UnsupportedOperationException`.

### Activities
1. Predict the three printed lines before running.
2. Write `scalePrices(inventory, factor)` that returns a new list with changed prices and leaves the original unchanged.
3. Write a version that changes a mutable list in place and compare the two designs.
4. Explain what "pass by value" means for an object reference.

### Accessibility Practice

State aloud before each call whether the method changes its argument, and name it accordingly (`addScore` changes, `withScore` returns a new list). Print the list before and after so the effect is heard.

### Skills Checklist
- [ ] I know a list argument is a reference passed by value.
- [ ] I can change a list in a method.
- [ ] I can return a new list instead.
- [ ] I can make a read-only copy.
- [ ] I can total the shared inventory in a method.

---

## Lesson 6.5: Variable Numbers of Arguments

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 6.5: Arbitrary Number of Arguments

### Learning Objectives
- Write a method with a varargs parameter.
- Pass an existing array as the varargs argument.
- Handle the case of no arguments.

### Concept Explanation

A final parameter written `int... scores` is a **varargs** parameter: callers may pass any number of `int` values, and inside the method `scores` is an `int[]` array. A caller may also pass an existing array directly: `average(array)`. A varargs parameter must be the last parameter.

Handle the case of zero arguments explicitly. Dividing a sum by a length of 0 would give a meaningless result, so the example returns an `OptionalDouble`.

The shared scores 82, 91, 76, 88 average 84.25, and the average of 90 and 80 is 85.0.

### Worked Example

```java
import java.util.OptionalDouble;

public class Lesson_6_5 {
    static OptionalDouble average(int... scores) {
        if (scores.length == 0) {
            return OptionalDouble.empty();
        }
        int total = 0;
        for (int score : scores) {
            total += score;
        }
        return OptionalDouble.of((double) total / scores.length);
    }

    static String describe(String label, int... values) {
        StringBuilder text = new StringBuilder(label + ":");
        for (int value : values) {
            text.append(' ').append(value);
        }
        return text.toString();
    }

    public static void main(String[] args) {
        System.out.println(average(82, 91, 76, 88));
        System.out.println(average(90, 80));
        System.out.println(average());

        int[] array = {82, 91, 76, 88};
        System.out.println(average(array));

        System.out.println(describe("scores", 82, 91, 76, 88));
        System.out.println(describe("nothing"));
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating arbitrary number of arguments. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Confusing a method's parameter list with its return type or omitting a return on one control-flow path.
- Expecting Java to pass primitive variables by reference; arguments are passed by value.
- Placing a varargs parameter before another parameter or using an overload that is ambiguous.
### Activities
1. Extract repeated statements into a named method with an explicit parameter and return contract.
2. Call the method with typical, boundary, and empty collection arguments.
3. Add a method that accepts a List or Map and returns a computed result without modifying the input.
4. Overload a method or add a varargs form, then explain overload resolution.
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
OptionalDouble[84.25]
OptionalDouble[85.0]
OptionalDouble.empty
OptionalDouble[84.25]
scores: 82 91 76 88
nothing:
```

### Common Mistakes
1. Calling `average()` with no arguments and dividing by zero.
2. Placing the varargs parameter before another parameter, which is a compile error.
3. Passing a `List<Integer>` where an `int...` is expected. A list is not an array.

### Activities
1. Predict each printed line.
2. Write `maximum(int... numbers)` that returns the largest or an empty result.
3. Write `joinWords(String separator, String... words)`.
4. Explain what happens to the varargs parameter inside the method.

### Accessibility Practice

Read varargs signatures aloud: 'static OptionalDouble average, open parenthesis, int, three dots, scores, close parenthesis'. Check that your screen reader announces the three dots.

### Skills Checklist
- [ ] I can write a varargs method.
- [ ] I can pass an array to a varargs parameter.
- [ ] I handle the no-argument case.
- [ ] I know varargs is an array inside the method.
- [ ] I know it must be the last parameter.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

# Unit 7: Classes and Object-Oriented Programming

## Overview

This unit develops classes and object-oriented programming through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 7.1: Why Learn About Classes?

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of why learn about classes?.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops why learn about classes? through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Objects combine state and behavior. Encapsulation protects invariants, constructors establish valid initial state, inheritance models a genuine is-a relationship, and composition models has-a collaboration. Prefer interfaces and composition when they reduce coupling.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_7_1 {
    public static void main(String[] args) {
        record Book(String title, int pages) {}
        Book book = new Book("Accessible Java", 240);
        System.out.println(book.title() + " has " + book.pages() + " pages.");
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 7.1: Why Learn About Classes?

### Learning Objectives
- Explain a class as data plus behavior.
- Hide fields with `private` and change them only through methods.
- Describe encapsulation.

### Concept Explanation

A *class* describes what a kind of thing knows (its *fields*) and what it can do (its *methods*). An *object* is one actual thing made from a class with `new`. Bundling data with the methods that work on it is called **encapsulation**. The shared example is an inventory *item* with a name, a quantity, and a unit price.

Marking a field `private` means only code inside the class can read or change it. Other code uses methods such as `getQuantity()` and `restock(amount)`, and `restock` can refuse invalid changes. `final` on a field means it is assigned once, in the constructor.

A source file may contain several classes, but only one may be `public` and it must match the file name. The helper class `Item` below is a normal, package-private class in the same file.

A Notebook with quantity 3 and unit price 2.50 is worth 7.50. Restocking 2 raises that to 12.50, and a negative restock is refused.

### Worked Example

```java
import java.util.Locale;

class Item {
    private final String name;
    private int quantity;
    private final double unitPrice;

    Item(String name, int quantity, double unitPrice) {
        this.name = name;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    boolean restock(int amount) {
        if (amount < 0) {
            return false;
        }
        quantity += amount;
        return true;
    }

    int getQuantity() {
        return quantity;
    }

    double totalValue() {
        return quantity * unitPrice;
    }

    void describe() {
        System.out.println(name + ": " + quantity + " at " + String.format(Locale.US, "%.2f", unitPrice)
            + " each, value " + String.format(Locale.US, "%.2f", totalValue()));
    }
}

public class Lesson_7_1 {
    public static void main(String[] args) {
        Item notebook = new Item("Notebook", 3, 2.50);
        notebook.describe();
        System.out.println(notebook.restock(2));
        notebook.describe();
        System.out.println(notebook.restock(-1));
        System.out.println(notebook.getQuantity());
        // notebook.quantity = 99;   // would not compile: the field is private
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating why learn about classes?. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Exposing mutable fields and allowing callers to bypass class invariants.
- Using inheritance for a has-a relationship or failing to call the appropriate superclass constructor.
- Confusing an overridden method with an overloaded method, or omitting @Override when overriding.
### Activities
1. Model one shared course entity with fields, constructor validation, and behavior methods.
2. Attempt an invalid state transition and verify encapsulation prevents it.
3. Demonstrate a true is-a relationship with overriding and runtime dispatch.
4. Replace an artificial inheritance relationship with composition and compare coupling.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 7.2: Creating and Using a Class

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of creating and using a class.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops creating and using a class through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Objects combine state and behavior. Encapsulation protects invariants, constructors establish valid initial state, inheritance models a genuine is-a relationship, and composition models has-a collaboration. Prefer interfaces and composition when they reduce coupling.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_7_2 {
    public static void main(String[] args) {
        Student student = new Student("Avery");
        student.enroll();
        System.out.println(student.name + ": " + student.active);
        }
        static class Student {
            String name;
            boolean active;
            Student(String name) { this.name = name; }
            void enroll() { active = true; }
=======
### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
true
Notebook: 5 at 2.50 each, value 12.50
false
5
```

### Common Mistakes
1. Making every field public, so outside code can put the object into an invalid state.
2. Forgetting `new`, which is a compile error: an object is made with `new Item(...)`.
3. Declaring two public classes in one file, which is a compile error.

### Activities
1. Predict the five printed lines before running.
2. Add a method `isLowStock()` that returns true when the quantity is below 5.
3. Uncomment the assignment, read the compiler message, and restore the comment.
4. Explain what encapsulation means and why `private` helps.

### Accessibility Practice

Describe a class as a list read in order: the name, then each field, then each method. Reading a class aloud works best by saying 'class Item, open brace, private final String name semicolon...' and listening for the braces that show structure.

### Skills Checklist
- [ ] I can explain data plus behavior.
- [ ] I can use `private` fields.
- [ ] I can create an object with `new`.
- [ ] I can describe encapsulation.
- [ ] I can read a class definition aloud.

---

## Lesson 7.2: Constructors and Validation

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 7.2: Creating and Using a Class

### Learning Objectives
- Write a constructor that sets the fields.
- Reject invalid values by throwing an exception.
- Create several objects with the same fields.

### Concept Explanation

A *constructor* has the same name as the class, no return type, and runs when `new` creates an object. `this.name = name` assigns the parameter to the field; `this` means "the object being built".

A constructor is the best place to check values. `throw new IllegalArgumentException(message)` stops the construction with a message, so an object can never exist in an invalid state. A caller that expects bad input catches the exception.

The example creates the three shared inventory items and then tries to create an invalid one. Each valid object has the same fields with different values; a class is a blueprint and each object is one *instance*.

### Worked Example

```java
import java.util.List;
import java.util.Locale;

class Item {
    final String name;
    final int quantity;
    final double unitPrice;

    Item(String name, int quantity, double unitPrice) {
        if (quantity < 0) {
            throw new IllegalArgumentException("quantity must not be negative");
        }
        if (unitPrice < 0) {
            throw new IllegalArgumentException("unit price must not be negative");
        }
        this.name = name;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }
}

public class Lesson_7_2 {
    public static void main(String[] args) {
        Item notebook = new Item("Notebook", 3, 2.50);
        Item pencil = new Item("Pencil", 10, 0.50);
        Item folder = new Item("Folder", 4, 1.25);

        for (Item item : List.of(notebook, pencil, folder)) {
            System.out.println(item.name + ": " + item.quantity + " at " + String.format(Locale.US, "%.2f", item.unitPrice));
        }

        try {
            new Item("Broken", -1, 1.0);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating creating and using a class. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Exposing mutable fields and allowing callers to bypass class invariants.
- Using inheritance for a has-a relationship or failing to call the appropriate superclass constructor.
- Confusing an overridden method with an overloaded method, or omitting @Override when overriding.
### Activities
1. Model one shared course entity with fields, constructor validation, and behavior methods.
2. Attempt an invalid state transition and verify encapsulation prevents it.
3. Demonstrate a true is-a relationship with overriding and runtime dispatch.
4. Replace an artificial inheritance relationship with composition and compare coupling.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 7.3: Working with Attributes and Methods

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of working with attributes and methods.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops working with attributes and methods through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Objects combine state and behavior. Encapsulation protects invariants, constructors establish valid initial state, inheritance models a genuine is-a relationship, and composition models has-a collaboration. Prefer interfaces and composition when they reduce coupling.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_7_3 {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(100.0);
        account.deposit(25.0);
        System.out.printf("balance=%.2f%n", account.balance());
        }
        static class BankAccount {
            private double balance;
            BankAccount(double opening) { if (opening < 0) throw new IllegalArgumentException(); balance = opening; }
            void deposit(double amount) { if (amount <= 0) throw new IllegalArgumentException(); balance += amount; }
            double balance() { return balance; }
=======
### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50
Pencil: 10 at 0.50
Folder: 4 at 1.25
quantity must not be negative
```

### Common Mistakes
1. Writing a return type such as `void Item(...)`, which makes it an ordinary method and not a constructor.
2. Forgetting `this.` and assigning a parameter to itself, so the field keeps its default value.
3. Catching the exception and ignoring it, so the program continues with no object.

### Activities
1. Create a fourth item with your own values and print it.
2. Add a rule that the name must not be blank.
3. Create two items with the same name and different quantities and show that they are separate objects.
4. Explain what `this` refers to in your own words.

### Accessibility Practice

Say the constructor aloud in order and check that the closing parenthesis and brace match. Print each object on its own line with its name so the output can be matched to the objects by ear.

### Skills Checklist
- [ ] I can write a constructor.
- [ ] I can validate by throwing an exception.
- [ ] I can create several objects.
- [ ] I know what an instance is.
- [ ] I know what `this` means.

---

## Lesson 7.3: Methods and Fields

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 7.3: Working with Attributes and Methods

### Learning Objectives
- Write getters, a computed method, and a validating method.
- Override `toString`.
- Change fields directly and through methods.

### Concept Explanation

A *getter* is a method that returns a field, conventionally named `getQuantity()`. A *computed* method such as `totalValue()` calculates a value from the fields each time, so it can never be out of date. A method that changes the object, such as `restock`, can validate its input.

`toString()` is a method every object has. Overriding it, marked with `@Override`, controls what `println(object)` shows, so the object prints as a useful sentence instead of a code like `Item@1b6d3586`.

The example adds a computed value, a validity check, a restock method, and a `toString` to the shared Notebook.

### Worked Example

```java
import java.util.Locale;

class Item {
    private final String name;
    private int quantity;
    private final double unitPrice;

    Item(String name, int quantity, double unitPrice) {
        this.name = name;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    int getQuantity() {
        return quantity;
    }

    void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    double totalValue() {
        return quantity * unitPrice;
    }

    boolean isValid() {
        return !name.isBlank() && quantity >= 0 && unitPrice >= 0;
    }

    void restock(int amount) {
        if (amount < 0) {
            System.out.println("Cannot restock a negative amount.");
            return;
        }
        quantity += amount;
    }

    @Override
    public String toString() {
        return name + ": " + quantity + " at " + String.format(Locale.US, "%.2f", unitPrice)
            + " each, value " + String.format(Locale.US, "%.2f", totalValue());
    }
}

public class Lesson_7_3 {
    public static void main(String[] args) {
        Item notebook = new Item("Notebook", 3, 2.50);
        System.out.println(notebook);
        notebook.restock(2);
        System.out.println(notebook);
        notebook.setQuantity(4);
        System.out.println(notebook);
        notebook.restock(-1);
        System.out.println(notebook.isValid());
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating working with attributes and methods. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Exposing mutable fields and allowing callers to bypass class invariants.
- Using inheritance for a has-a relationship or failing to call the appropriate superclass constructor.
- Confusing an overridden method with an overloaded method, or omitting @Override when overriding.
### Activities
1. Model one shared course entity with fields, constructor validation, and behavior methods.
2. Attempt an invalid state transition and verify encapsulation prevents it.
3. Demonstrate a true is-a relationship with overriding and runtime dispatch.
4. Replace an artificial inheritance relationship with composition and compare coupling.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 7.4: Inheritance and Overriding

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of inheritance and overriding.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops inheritance and overriding through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Objects combine state and behavior. Encapsulation protects invariants, constructors establish valid initial state, inheritance models a genuine is-a relationship, and composition models has-a collaboration. Prefer interfaces and composition when they reduce coupling.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_7_4 {
    public static void main(String[] args) {
        Animal animal = new Dog("Milo");
        animal.speak();
        }
        static class Animal {
            private final String name;
            Animal(String name) { this.name = name; }
            void speak() { System.out.println(name + " makes a sound"); }
        }
        static class Dog extends Animal {
            Dog(String name) { super(name); }
            @Override void speak() { System.out.println("Dog barks"); }
=======
### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
Notebook: 5 at 2.50 each, value 12.50
Notebook: 4 at 2.50 each, value 10.00
Cannot restock a negative amount.
true
```

### Common Mistakes
1. Forgetting `@Override`, so a misspelled `tostring()` silently becomes a new method.
2. Giving a field a public setter that skips the validation the object needs.
3. Storing a value that can be computed, so it goes out of date when the inputs change.

### Activities
1. Predict the output of all six lines before running.
2. Add a method `discounted(double rate)` that returns the value after a discount without changing the item.
3. Remove the `setQuantity` method and see which lines stop compiling.
4. Explain why `toString` is better than printing fields one by one.

### Accessibility Practice

Name methods after actions (`restock`) so a call reads as a sentence. Printing an object with a good `toString` gives the screen reader one complete line per object.

### Skills Checklist
- [ ] I can write getters and a computed method.
- [ ] I can validate in a method.
- [ ] I can override `toString`.
- [ ] I know why `@Override` helps.
- [ ] I can tell a stored from a computed value.

---

## Lesson 7.4: Inheritance

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 7.4: Inheritance

### Learning Objectives
- Declare a subclass with `extends`.
- Override a method and call the parent's version with `super`.
- Explain polymorphism.

### Concept Explanation

A subclass is declared with `extends`: `class DiscountedItem extends Item`. Its constructor must call the parent's constructor first with `super(...)`, which sets up the inherited fields. A method that replaces the parent's method is marked `@Override`, and `super.totalValue()` calls the parent's version. A class marked `final` cannot be extended, and a `private` field of the parent is not directly visible to the subclass.

*Polymorphism* means the same method call behaves differently for different classes. A variable of type `Item` can refer to a `DiscountedItem`, and calling `totalValue()` runs the discounted version. `describe` is written once in `Item` and calls `totalValue()`, so it prints the discounted value automatically.

The example discounts the shared Folder (4 at 1.25) by 20 percent, so its value is 4.00 instead of 5.00.

### Worked Example

```java
import java.util.List;
import java.util.Locale;

class Item {
    protected final String name;
    protected final int quantity;
    protected final double unitPrice;

    Item(String name, int quantity, double unitPrice) {
        this.name = name;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    double totalValue() {
        return quantity * unitPrice;
    }

    void describe() {
        System.out.println(name + ": " + quantity + " at " + String.format(Locale.US, "%.2f", unitPrice)
            + " each, value " + String.format(Locale.US, "%.2f", totalValue()));
    }
}

class DiscountedItem extends Item {
    private final double discountRate;

    DiscountedItem(String name, int quantity, double unitPrice, double discountRate) {
        super(name, quantity, unitPrice);
        this.discountRate = discountRate;
    }

    @Override
    double totalValue() {
        return super.totalValue() * (1 - discountRate);
    }
}

public class Lesson_7_4 {
    public static void main(String[] args) {
        DiscountedItem folder = new DiscountedItem("Folder", 4, 1.25, 0.20);
        folder.describe();
        System.out.println(folder instanceof Item);

        List<Item> items = List.of(new Item("Notebook", 3, 2.50), folder);
        for (Item item : items) {
            System.out.println(item.name + ": " + String.format(Locale.US, "%.2f", item.totalValue()));
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating inheritance and overriding. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Exposing mutable fields and allowing callers to bypass class invariants.
- Using inheritance for a has-a relationship or failing to call the appropriate superclass constructor.
- Confusing an overridden method with an overloaded method, or omitting @Override when overriding.
### Activities
1. Model one shared course entity with fields, constructor validation, and behavior methods.
2. Attempt an invalid state transition and verify encapsulation prevents it.
3. Demonstrate a true is-a relationship with overriding and runtime dispatch.
4. Replace an artificial inheritance relationship with composition and compare coupling.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 7.5: Instances as Attributes: Composition

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of instances as attributes: composition.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops instances as attributes: composition through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Objects combine state and behavior. Encapsulation protects invariants, constructors establish valid initial state, inheritance models a genuine is-a relationship, and composition models has-a collaboration. Prefer interfaces and composition when they reduce coupling.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_7_5 {
    public static void main(String[] args) {
        Order order = new Order(new Customer("Riley"));
        System.out.println(order.customer.name);
        }
        static class Customer { String name; Customer(String name) { this.name = name; } }
        static class Order { Customer customer; Order(Customer customer) { this.customer = customer; }
=======
### Expected Behavior or Output

The program prints:
```text
Folder: 4 at 1.25 each, value 4.00
true
Notebook: 7.50
Folder: 4.00
```

### Common Mistakes
1. Forgetting to call `super(...)` first in the constructor, which is a compile error when the parent has no no-argument constructor.
2. Forgetting `@Override` and accidentally creating a new method instead of replacing the parent's.
3. Using inheritance for a "has a" relationship; use composition instead (Lesson 7.5).

### Activities
1. Predict the output before running.
2. Add a subclass `PerishableItem` with an `expires` field and override `describe`.
3. Explain why `describe` prints the discounted value without being redefined.
4. List the order in which Java looks for `totalValue` on a `DiscountedItem`.

### Accessibility Practice

Describe inheritance as an ordered list: the subclass first, then its parent. Speaking the chain aloud ('DiscountedItem, then Item') is clearer than a diagram.

### Skills Checklist
- [ ] I can declare a subclass.
- [ ] I can override a method.
- [ ] I can call `super`.
- [ ] I can explain polymorphism.
- [ ] I know `final` stops inheritance.

---

## Lesson 7.5: Composition

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 7.5: Instances as Attributes (Composition)

### Learning Objectives
- Explain composition ("has a").
- Hold a list of objects inside another object.
- Build an inventory from the shared items.

### Concept Explanation

*Composition* means that one object contains other objects. An inventory *has* items; it is not a kind of item. Composition is usually simpler and safer than inheritance when objects are related by containment.

The container keeps a `private` list of its parts and exposes methods that loop over the parts and call each part's own methods, so the container does not need to know how a part works. Keeping the list private forces other code to use `add` and `report`. The method `find` returns an `Optional<Item>` because the item may not exist.

The example builds an `Inventory` with the three shared items and reports each quantity and the total value, 17.50.

### Worked Example

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Optional;

class Item {
    final String name;
    final int quantity;
    final double unitPrice;

    Item(String name, int quantity, double unitPrice) {
        this.name = name;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    double totalValue() {
        return quantity * unitPrice;
    }
}

class Inventory {
    private final List<Item> items = new ArrayList<>();

    void add(Item item) {
        items.add(item);
    }

    Optional<Item> find(String name) {
        for (Item item : items) {
            if (item.name.equals(name)) {
                return Optional.of(item);
            }
        }
        return Optional.empty();
    }

    double totalValue() {
        double total = 0;
        for (Item item : items) {
            total += item.totalValue();
        }
        return total;
    }

    void report() {
        for (Item item : items) {
            System.out.println(item.name + ": " + item.quantity);
        }
        System.out.println("Total value: " + String.format(Locale.US, "%.2f", totalValue()));
    }
}

public class Lesson_7_5 {
    public static void main(String[] args) {
        Inventory inventory = new Inventory();
        inventory.add(new Item("Notebook", 3, 2.50));
        inventory.add(new Item("Pencil", 10, 0.50));
        inventory.add(new Item("Folder", 4, 1.25));
        inventory.report();
        System.out.println(inventory.find("Pencil").map(item -> item.quantity).orElse(-1));
        System.out.println(inventory.find("Eraser").isPresent());
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating instances as attributes: composition. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Exposing mutable fields and allowing callers to bypass class invariants.
- Using inheritance for a has-a relationship or failing to call the appropriate superclass constructor.
- Confusing an overridden method with an overloaded method, or omitting @Override when overriding.
### Activities
1. Model one shared course entity with fields, constructor validation, and behavior methods.
2. Attempt an invalid state transition and verify encapsulation prevents it.
3. Demonstrate a true is-a relationship with overriding and runtime dispatch.
4. Replace an artificial inheritance relationship with composition and compare coupling.
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
Notebook: 3
Pencil: 10
Folder: 4
Total value: 17.50
10
false
```

### Common Mistakes
1. Using inheritance where a "has a" relationship is meant.
2. Making the list public so other code changes it without going through `add`.
3. Calling `get()` on an empty `Optional`, which throws `NoSuchElementException`.

### Activities
1. Predict the output.
2. Add `remove(String name)` to `Inventory` and test it.
3. Add a method that returns the names of items with a quantity below 5.
4. Explain "is a" versus "has a" with two examples.

### Accessibility Practice

Report the inventory as one labelled line per item and a final total line, so the screen reader reads a complete summary in order.

### Skills Checklist
- [ ] I can explain composition.
- [ ] I can hold a list of objects in an object.
- [ ] I can keep a list private.
- [ ] I can say "is a" versus "has a".
- [ ] I can use `Optional` for a missing result.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

# Unit 8: Files and Exceptions

## Overview

This unit develops files and exceptions through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 8.1: Reading from a File

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of reading from a file.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops reading from a file through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. File APIs can fail with IOException; use Path and Files for common operations and try-with-resources for closeable streams. Catch only failures you can handle. JSON is not built into the Java SE standard library, so robust JSON parsing requires a documented external library such as Jackson or Gson.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_8_1 {
    public static void main(String[] args) {
        try {
            java.nio.file.Path file = java.nio.file.Files.createTempFile("java-lesson", ".txt");
            java.nio.file.Files.writeString(file, "first line\\nsecond line\\n");
            for (String line : java.nio.file.Files.readAllLines(file)) System.out.println(line);
            java.nio.file.Files.deleteIfExists(file);
        } catch (java.io.IOException ex) { System.out.println(ex.getMessage()); }
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 8.1: Reading from a File

### Learning Objectives
- Read a whole file and read it line by line.
- Check that a file exists before reading.
- Report a missing file clearly.

### Concept Explanation

`java.nio.file.Path` represents a location and `java.nio.file.Files` does the work. `Files.readString(path)` returns the whole file, `Files.readAllLines(path)` returns a list of lines, and `Files.lines(path)` returns a *stream* of lines that must be closed, so it is used in try-with-resources. `Files.exists(path)` tests whether a file is there. A relative path such as `notes.txt` starts from the program's working directory.

Most file methods throw the *checked* exception `IOException`, which the compiler forces you to handle: either catch it or declare `throws IOException` on the method. A missing file throws a `NoSuchFileException`.

To keep the lesson self-contained, the example first writes the two-line `notes.txt` that every language track uses, then reads it three ways and checks a file that does not exist.

### Worked Example

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.Stream;

public class Lesson_8_1 {
    public static void main(String[] args) throws IOException {
        Path notes = Path.of("notes.txt");
        Files.writeString(notes, "Practice Java.\nReview lists and methods.\n");

        System.out.println(Files.readString(notes));

        for (String line : Files.readAllLines(notes)) {
            System.out.println(line);
        }
        System.out.println(Files.readAllLines(notes).size());

        try (Stream<String> lines = Files.lines(notes)) {
            lines.map(String::toUpperCase).forEach(System.out::println);
        }

        Path missing = Path.of("missing_notes.txt");
        if (!Files.exists(missing)) {
            System.out.println("missing_notes.txt was not found.");
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating reading from a file. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Leaving a stream open instead of using try-with-resources or ignoring IOException.
- Catching Exception broadly and hiding failures that should be reported or propagated.
- Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation.
### Activities
1. Read and write a temporary file, then verify the file content and clean up the resource.
2. Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions.
3. Explain which resources are closed by try-with-resources and which code executes in finally.
4. Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available.
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
Practice Java.
Review lists and methods.

Practice Java.
Review lists and methods.
2
PRACTICE JAVA.
REVIEW LISTS AND METHODS.
missing_notes.txt was not found.
```

### Common Mistakes
1. Reading a file that does not exist without checking or catching the error.
2. Forgetting `throws IOException` or a `catch`, which is a compile error for file methods.
3. Using `Files.lines` without closing the stream.

### Activities
1. Run the program and describe each block of output.
2. Add a third line to the file text and predict the new count.
3. Print each line with its line number.
4. Print a friendly message that includes the missing file's name.

### Accessibility Practice

Read the output aloud in order. Make an error message a complete sentence that includes the file name so it is clear without seeing the screen.

### Skills Checklist
- [ ] I can read a file whole and by line.
- [ ] I can check that a file exists.
- [ ] I know checked exceptions must be handled or declared.
- [ ] I can report a missing file.
- [ ] I can close a stream with try-with-resources.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 8.2: Writing to a File

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of writing to a file.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops writing to a file through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. File APIs can fail with IOException; use Path and Files for common operations and try-with-resources for closeable streams. Catch only failures you can handle. JSON is not built into the Java SE standard library, so robust JSON parsing requires a documented external library such as Jackson or Gson.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_8_2 {
    public static void main(String[] args) {
        try {
            java.nio.file.Path file = java.nio.file.Files.createTempFile("java-write", ".txt");
            java.nio.file.Files.writeString(file, "Avery,92\\nRiley,85\\n");
            System.out.println(java.nio.file.Files.size(file) + " bytes written");
            java.nio.file.Files.deleteIfExists(file);
        } catch (java.io.IOException ex) { System.out.println(ex.getMessage()); }
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 8.2: Writing to a File

### Learning Objectives
- Write with `Files.writeString` and append with `StandardOpenOption.APPEND`.
- Include line endings correctly.
- Read the file back to verify it.

### Concept Explanation

`Files.writeString(path, text)` creates the file or **replaces** its contents. To add to the end, pass the option `StandardOpenOption.APPEND`. Neither adds a line ending for you, so end each line with `\n`. `Files.newBufferedWriter` writes in pieces and must be closed (Lesson 8.4).

Reading the file back is the simplest way to confirm what was saved. The example writes the first notes line, appends the second, and reads the file back.

### Worked Example

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;

public class Lesson_8_2 {
    public static void main(String[] args) throws IOException {
        Path file = Path.of("notes.txt");
        Files.writeString(file, "Practice Java.\n");
        Files.writeString(file, "Review lists and methods.\n", StandardOpenOption.APPEND);
        System.out.print(Files.readString(file));
        System.out.println("Lines: " + Files.readAllLines(file).size());
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating writing to a file. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Leaving a stream open instead of using try-with-resources or ignoring IOException.
- Catching Exception broadly and hiding failures that should be reported or propagated.
- Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation.
### Activities
1. Read and write a temporary file, then verify the file content and clean up the resource.
2. Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions.
3. Explain which resources are closed by try-with-resources and which code executes in finally.
4. Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 8.3: Exceptions and Handling Errors

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of exceptions and handling errors.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops exceptions and handling errors through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. File APIs can fail with IOException; use Path and Files for common operations and try-with-resources for closeable streams. Catch only failures you can handle. JSON is not built into the Java SE standard library, so robust JSON parsing requires a documented external library such as Jackson or Gson.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_8_3 {
    public static void main(String[] args) {
        String raw = "not-a-number";
        try {
            int value = Integer.parseInt(raw);
            System.out.println(value);
        } catch (NumberFormatException ex) {
            System.out.println("Invalid integer: " + raw);
=======
### Expected Behavior or Output

The program prints:
```text
Practice Java.
Review lists and methods.
Lines: 2
```

### Common Mistakes
1. Using the replacing form when appending was intended, which erases earlier content.
2. Forgetting `\n`, so all written lines run together.
3. Not reading the file back to check what was actually saved.

### Activities
1. Predict the output, then run.
2. Remove the `APPEND` option and explain the difference.
3. Append a third line with the current number of lines.
4. Write the shared scores, one per line, then read them back and total them.

### Accessibility Practice

Always read a written file back in the terminal to confirm it, using line navigation, so you do not depend on assumptions about what was saved.

### Skills Checklist
- [ ] I can write and append.
- [ ] I know the default write replaces.
- [ ] I can include line endings.
- [ ] I can verify by reading back.
- [ ] I can count lines in a file.

---

## Lesson 8.3: Exceptions

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 8.3: Exceptions - Handling Errors

### Learning Objectives
- Catch specific exceptions with `try` and `catch`.
- Use `finally` and multi-catch.
- Explain checked versus unchecked exceptions.

### Concept Explanation

An *exception* is an error that stops the program unless it is caught. `try { ... } catch (SomeException e) { ... }` runs the risky code and handles the failure. Catch the **specific** exception you expect, never `Exception` for everything, so mistakes in your own code are not hidden. A `finally` block runs whether or not an exception happened. One `catch` may name several types: `catch (NumberFormatException | ArithmeticException e)`.

*Checked* exceptions such as `IOException` must be caught or declared; *unchecked* exceptions such as `NumberFormatException`, `ArithmeticException`, and `IllegalStateException` need not be. Integer division by zero throws an `ArithmeticException`; division of `double` values by zero gives infinity instead.

`e.getMessage()` returns the message. Some library messages depend on the Java version and the operating system, so the example prints only the messages that Java guarantees.

### Worked Example

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;

public class Lesson_8_3 {
    public static void main(String[] args) {
        try {
            Files.readString(Path.of("missing_notes.txt"));
        } catch (NoSuchFileException e) {
            System.out.println("Error: missing_notes.txt was not found.");
        } catch (IOException e) {
            System.out.println("Error: could not read the file.");
        }

        try {
            Integer.parseInt("abc");
        } catch (NumberFormatException e) {
            System.out.println("Error: 'abc' is not a valid score.");
        }

        int zero = 0;
        try {
            System.out.println(10 / zero);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        }
        System.out.println(10.0 / zero);

        try {
            throw new IllegalStateException("raised on purpose");
        } catch (IllegalStateException | IllegalArgumentException e) {
            System.out.println(e.getMessage());
        } finally {
            System.out.println("Cleanup runs either way.");
>>>>>>> 2067a20 (curriculum clearning and updates)
        }
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating exceptions and handling errors. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Leaving a stream open instead of using try-with-resources or ignoring IOException.
- Catching Exception broadly and hiding failures that should be reported or propagated.
- Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation.
### Activities
1. Read and write a temporary file, then verify the file content and clean up the resource.
2. Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions.
3. Explain which resources are closed by try-with-resources and which code executes in finally.
4. Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 8.4: The catch, finally, and try-with-resources Patterns

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of the catch, finally, and try-with-resources patterns.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops the catch, finally, and try-with-resources patterns through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. File APIs can fail with IOException; use Path and Files for common operations and try-with-resources for closeable streams. Catch only failures you can handle. JSON is not built into the Java SE standard library, so robust JSON parsing requires a documented external library such as Jackson or Gson.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_8_4 {
    public static void main(String[] args) {
        try {
            int divisor = 0;
            System.out.println(12 / divisor);
        } catch (ArithmeticException ex) {
            System.out.println("Cannot divide by zero");
        } finally {
            System.out.println("Cleanup runs after the try/catch");
        }
=======
### Expected Behavior or Output

The program prints:
```text
Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score.
Error: / by zero
Infinity
raised on purpose
Cleanup runs either way.
```

### Common Mistakes
1. Catching `Exception` for everything, which hides mistakes in your own code.
2. Using `Integer.parseInt` on untrusted text without a catch.
3. Expecting `10.0 / 0` to throw. It gives `Infinity`.

### Activities
1. Predict each printed line before running.
2. Wrap `Integer.parseInt(scanner.nextLine())` so invalid input prints a clear message and asks again.
3. Catch `ArithmeticException` in a method that computes an average of an empty list.
4. Explain when to catch an exception and when to let it stop the program.

### Accessibility Practice

Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.' Read the exception's class name aloud when you see a stack trace, then jump to the first line that names your own file.

### Skills Checklist
- [ ] I can catch specific exceptions.
- [ ] I can use `finally` and multi-catch.
- [ ] I can explain checked versus unchecked.
- [ ] I know integer and decimal division by zero differ.
- [ ] I can write clear error messages.

---

## Lesson 8.4: Cleanup with try-with-resources

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 8.4: The else and finally Blocks

### Learning Objectives
- Close files reliably with try-with-resources.
- Show that a resource is released even after an error.
- Use `finally` for cleanup.

### Concept Explanation

A reader or writer holds a resource from the operating system, so it must be closed. *Try-with-resources* declares the resource in parentheses after `try`: `try (BufferedReader reader = ...) { ... }`. Java closes it automatically when the block ends, **even if the block throws an exception**. Since Java 9, an existing variable that is not reassigned can be listed too: `try (reader) { ... }`.

`finally` is the general tool: its block runs after the `try` block whether or not an exception happened. Use try-with-resources for anything that can be closed, and `finally` for other cleanup.

The example writes a file, reads it back, throws an exception inside a second block, and shows that a reader closed by try-with-resources refuses to read.

### Worked Example

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Lesson_8_4 {
    public static void main(String[] args) throws IOException {
        Path file = Path.of("cleanup_demo.txt");
        try (BufferedWriter writer = Files.newBufferedWriter(file)) {
            writer.write("Some data.\n");
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
            throw new IllegalStateException("failure while reading");
        } catch (IllegalStateException e) {
            System.out.println(e.getMessage());
        }

        try {
            System.out.println("working");
        } finally {
            System.out.println("finally block ran");
        }

        boolean refused = false;
        try {
            reader.readLine();
        } catch (IOException e) {
            refused = true;
        }
        System.out.println(refused);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating the catch, finally, and try-with-resources patterns. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Leaving a stream open instead of using try-with-resources or ignoring IOException.
- Catching Exception broadly and hiding failures that should be reported or propagated.
- Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation.
### Activities
1. Read and write a temporary file, then verify the file content and clean up the resource.
2. Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions.
3. Explain which resources are closed by try-with-resources and which code executes in finally.
4. Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available.
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
Some data.
Some data.
failure while reading
working
finally block ran
true
```

### Common Mistakes
1. Opening a reader or writer and forgetting to close it.
2. Putting `return` in a `finally` block, which can hide an earlier exception.
3. Using the reader after try-with-resources has closed it.

### Activities
1. Predict the six printed lines.
2. Rewrite the first example with an explicit `try` and `finally` and compare the length.
3. Throw an exception before the write and confirm that the file is still closed.
4. Explain why cleanup matters even if the program is about to end.

### Accessibility Practice

Print a short labelled line after each step, so the screen reader announces which path ran. Labelled lines make the order of cleanup audible.

### Skills Checklist
- [ ] I can close files with try-with-resources.
- [ ] I can use `finally`.
- [ ] I know the resource closes after an error.
- [ ] I can show a closed reader refuses to read.
- [ ] I can explain why cleanup matters.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 8.5: Storing Data with JSON

### Reading References
<<<<<<< HEAD
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of storing data with json.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops storing data with json through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. File APIs can fail with IOException; use Path and Files for common operations and try-with-resources for closeable streams. Catch only failures you can handle. JSON is not built into the Java SE standard library, so robust JSON parsing requires a documented external library such as Jackson or Gson.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_8_5 {
    public static void main(String[] args) {
        String json = "{\\\"name\\\":\\\"Avery\\\",\\\"score\\\":92}";
        System.out.println(json);
        System.out.println("JSON is text; use a JSON library for robust parsing and escaping.");
=======
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- JSON specification: https://www.json.org
- Matching Python lesson: Lesson 8.5: Storing Data with JSON

### Learning Objectives
- Explain why this lesson includes a JSON helper.
- Encode and decode the shared task records.
- Handle a missing or malformed file.

### Concept Explanation

The Java standard library has no JSON support. Real projects add a library such as Jackson or Gson through Maven or Gradle. To keep this course free of build tooling, the example includes a *teaching implementation*, the nested class `Json`, with `encode` and `decode`. It handles strings, numbers, booleans, `null`, lists, and maps, writes object keys in sorted order, and reports malformed text with an exception that includes the position. It is not a replacement for a production library.

JSON text stores data in a standard format: `{ ... }` holds key-value pairs, `[ ... ]` holds ordered items, and text is in double quotation marks. Decoded data is untyped (`Map<String, Object>` and `List<Object>`), so check each field before using it. Numbers without a decimal point decode as `Long`.

The shared to-do record has the fields `id`, `title`, `description`, `done`, and `created_at`. The example saves two tasks, loads them back, and shows the message for a malformed file.

The teaching helper decodes JSON `null` as `null` and numbers without a decimal point as `Long`. It does not handle every number edge case that a full parser must.

### Worked Example

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class Lesson_8_5 {
    static final class Json {
        private Json() {}

        static String encode(Object value) {
            if (value == null) {
                return "null";
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
                StringBuilder out = new StringBuilder("{");
                for (int i = 0; i < keys.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(quote(keys.get(i))).append(':').append(encode(map.get(keys.get(i))));
                }
                return out.append('}').toString();
            }
            if (value instanceof List<?> list) {
                StringBuilder out = new StringBuilder("[");
                for (int i = 0; i < list.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(encode(list.get(i)));
                }
                return out.append(']').toString();
            }
            throw new IllegalArgumentException("cannot encode " + value.getClass().getSimpleName());
        }

        private static String quote(String text) {
            StringBuilder out = new StringBuilder("\"");
            for (char c : text.toCharArray()) {
                switch (c) {
                    case '"' -> out.append("\\\"");
                    case '\\' -> out.append("\\\\");
                    case '\n' -> out.append("\\n");
                    case '\r' -> out.append("\\r");
                    case '\t' -> out.append("\\t");
                    default -> {
                        if (c < ' ') {
                            out.append(String.format("\\u%04x", (int) c));
                        } else {
                            out.append(c);
                        }
                    }
                }
            }
            return out.append('"').toString();
        }

        static Object decode(String text) {
            Parser parser = new Parser(text);
            Object result = parser.value();
            parser.skip();
            if (parser.pos < text.length()) {
                throw parser.fail("unexpected extra text");
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
                return new IllegalArgumentException(message + " at position " + pos);
            }

            void skip() {
                while (pos < text.length() && Character.isWhitespace(text.charAt(pos))) {
                    pos++;
                }
            }

            Object value() {
                skip();
                if (pos >= text.length()) {
                    throw fail("unexpected end of text");
                }
                char c = text.charAt(pos);
                if (c == '{') return object();
                if (c == '[') return list();
                if (c == '"') return string();
                if (text.startsWith("true", pos)) { pos += 4; return Boolean.TRUE; }
                if (text.startsWith("false", pos)) { pos += 5; return Boolean.FALSE; }
                if (text.startsWith("null", pos)) { pos += 4; return null; }
                if (c == '-' || Character.isDigit(c)) return number();
                throw fail("unexpected character");
            }

            Object number() {
                int start = pos;
                if (text.charAt(pos) == '-') {
                    pos++;
                }
                while (pos < text.length() && (Character.isDigit(text.charAt(pos)) || ".eE+-".indexOf(text.charAt(pos)) >= 0)) {
                    pos++;
                }
                String token = text.substring(start, pos);
                try {
                    return Long.parseLong(token);
                } catch (NumberFormatException notWhole) {
                    try {
                        return Double.parseDouble(token);
                    } catch (NumberFormatException notNumber) {
                        throw fail("bad number");
                    }
                }
            }

            String string() {
                pos++;
                StringBuilder out = new StringBuilder();
                while (true) {
                    if (pos >= text.length()) {
                        throw fail("unterminated string");
                    }
                    char c = text.charAt(pos++);
                    if (c == '"') {
                        return out.toString();
                    }
                    if (c != '\\') {
                        out.append(c);
                        continue;
                    }
                    if (pos >= text.length()) {
                        throw fail("bad escape");
                    }
                    char e = text.charAt(pos++);
                    switch (e) {
                        case 'n' -> out.append('\n');
                        case 't' -> out.append('\t');
                        case 'r' -> out.append('\r');
                        case '"' -> out.append('"');
                        case '\\' -> out.append('\\');
                        case '/' -> out.append('/');
                        case 'u' -> {
                            if (pos + 4 > text.length()) {
                                throw fail("bad escape");
                            }
                            out.append((char) Integer.parseInt(text.substring(pos, pos + 4), 16));
                            pos += 4;
                        }
                        default -> throw fail("bad escape");
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
                    if (pos >= text.length() || text.charAt(pos) != '"') {
                        throw fail("expected a key");
                    }
                    String key = string();
                    skip();
                    if (pos >= text.length() || text.charAt(pos) != ':') {
                        throw fail("expected ':'");
                    }
                    pos++;
                    map.put(key, value());
                    skip();
                    if (pos >= text.length()) {
                        throw fail("unterminated object");
                    }
                    char d = text.charAt(pos++);
                    if (d == '}') {
                        return map;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail("expected ',' or '}'");
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
                        throw fail("unterminated list");
                    }
                    char d = text.charAt(pos++);
                    if (d == ']') {
                        return items;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail("expected ',' or ']'");
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        List<Map<String, Object>> tasks = List.of(
            Map.of("id", 1, "title", "Study programming", "description", "Finish Unit 8",
                "done", false, "created_at", "2026-01-15T09:00:00"),
            Map.of("id", 2, "title", "Review scores", "description", "Check the four scores",
                "done", true, "created_at", "2026-01-15T09:30:00"));

        Path file = Path.of("tasks.json");
        Files.writeString(file, Json.encode(tasks));

        if (!Files.exists(file)) {
            System.out.println("Tasks file not found.");
            return;
        }
        List<?> loaded;
        try {
            loaded = (List<?>) Json.decode(Files.readString(file));
        } catch (IllegalArgumentException e) {
            System.out.println("Error: could not decode tasks file: " + e.getMessage());
            return;
        }
        for (Object entry : loaded) {
            Map<?, ?> task = (Map<?, ?>) entry;
            String status = Boolean.TRUE.equals(task.get("done")) ? "done" : "not done";
            System.out.println(task.get("id") + ": " + task.get("title") + " (" + status + ")");
        }

        try {
            Json.decode("[{\"id\": 1,");
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating storing data with json. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Leaving a stream open instead of using try-with-resources or ignoring IOException.
- Catching Exception broadly and hiding failures that should be reported or propagated.
- Assuming JSON parsing is built into Java SE or constructing JSON with unsafe string concatenation.
### Activities
1. Read and write a temporary file, then verify the file content and clean up the resource.
2. Test a missing file and malformed numeric content; distinguish checked from unchecked exceptions.
3. Explain which resources are closed by try-with-resources and which code executes in finally.
4. Document why production JSON requires a parser/serializer library and test malformed JSON with that library when available.
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
1: Study programming (not done)
2: Review scores (done)
expected a key at position 10
```

### Common Mistakes
1. Assuming Java has built-in JSON support.
2. Trusting decoded data without checking that each field exists and has the right type.
3. Overwriting a good data file with an empty list after a failed load.

### Activities
1. Run the program and read the saved JSON text from `tasks.json`.
2. Edit `tasks.json` by hand to remove a closing bracket and run the loading part again. Read the message.
3. Add a third task and confirm that it is saved and loaded.
4. Explain why a production project should use a maintained JSON library.

### Accessibility Practice

Open `tasks.json` in the terminal and read it as text. JSON in a single line is difficult to navigate, so practise stepping through it by word or character.

### Skills Checklist
- [ ] I know Java has no built-in JSON.
- [ ] I can encode and decode records.
- [ ] I handle missing and malformed files.
- [ ] I check decoded fields.
- [ ] I know when to use a library.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

# Unit 9: Testing and Data Analysis

## Overview

This unit develops testing and data analysis through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

<<<<<<< HEAD
## Lesson 9.1: Testing a Method

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of testing a method.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops testing a method through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Separate deterministic logic from random generation, file I/O, and user interaction. Test methods and object invariants with assertions or a test framework such as JUnit. CSV quoting rules mean a comma split is only a teaching illustration, not a production parser.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_9_1 {
    public static void main(String[] args) {
        int actual = square(7);
        if (actual != 49) throw new AssertionError("expected 49, got " + actual);
        System.out.println("square test passed");
        }
        static int square(int value) { return value * value;
=======
## Lesson 9.1: Testing Functions

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 9.1: Testing Your Code

### Learning Objectives
- Write checks with chosen inputs and expected results.
- Compare decimals with a tolerance.
- Test boundary values and report failure with an exit status.

### Concept Explanation

A *test* runs code with chosen inputs and compares the result with a value decided in advance. Real Java projects use JUnit through Maven or Gradle. To keep this course free of build tooling, the example uses a tiny `check` method; the habits (inputs, expected values, boundaries) are the same.

Decimal results are compared with a *tolerance*, not `equals`, because of floating-point approximation: the tip for 24.50 at 0.15 is stored as 3.6749999999999998, so the test checks that it is within a tiny distance of 3.675.

The same tests appear in every language track: `add(5, 3)` is 8, `add(-5, -3)` is -8, `add(10, -4)` is 6, the tip is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F.

`System.exit(1)` ends the program with a failure status when any check fails, so other tools can notice.

### Worked Example

```java
import java.util.Objects;

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
        if (score >= 90) return "A";
        if (score >= 80) return "B";
        if (score >= 70) return "C";
        if (score >= 60) return "D";
        return "F";
    }

    static void check(String name, Object actual, Object expected) {
        if (Objects.equals(actual, expected)) {
            passed++;
            System.out.println("PASS " + name);
        } else {
            failed++;
            System.out.println("FAIL " + name + ": expected " + expected + " but got " + actual);
        }
    }

    static void checkClose(String name, double actual, double expected, double tolerance) {
        check(name, Math.abs(actual - expected) <= tolerance, true);
    }

    public static void main(String[] args) {
        check("add 5 and 3", add(5, 3), 8);
        check("add -5 and -3", add(-5, -3), -8);
        check("add 10 and -4", add(10, -4), 6);
        checkClose("tip on 24.50 at 0.15", calculateTip(24.5, 0.15), 3.675, 1e-9);
        check("tip on a zero bill", calculateTip(0, 0.15), 0.0);
        check("classify 90", classify(90), "A");
        check("classify 89", classify(89), "B");
        check("classify 60", classify(60), "D");
        check("classify 59", classify(59), "F");

        System.out.println(passed + " passed, " + failed + " failed");
        if (failed > 0) {
            System.exit(1);
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating testing a method. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Relying on Java's assert statements without enabling assertions, or testing implementation details instead of behavior.
- Allowing tests to share mutable state so their order affects results.
- Assuming a simple comma split handles quoted CSV fields or using an unseeded random source in a reproducibility exercise.
### Activities
1. Write one passing and one failing test for a pure method, then run the tests repeatedly.
2. Seed a Random instance and verify the exercise is reproducible.
3. Analyze a sentence for word counts after applying a documented normalization rule.
4. Test CSV data with quoted commas and explain why a production parser is required.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 9.2: Testing a Class

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of testing a class.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops testing a class through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Separate deterministic logic from random generation, file I/O, and user interaction. Test methods and object invariants with assertions or a test framework such as JUnit. CSV quoting rules mean a comma split is only a teaching illustration, not a production parser.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_9_2 {
    public static void main(String[] args) {
        Counter counter = new Counter();
        counter.increment();
        counter.increment();
        if (counter.value() != 2) throw new AssertionError("counter state incorrect");
        System.out.println("class behavior test passed");
        }
        static class Counter { private int value; void increment() { value++; } int value() { return value; }
=======
### Expected Behavior or Output

The program prints:
```text
PASS add 5 and 3
PASS add -5 and -3
PASS add 10 and -4
PASS tip on 24.50 at 0.15
PASS tip on a zero bill
PASS classify 90
PASS classify 89
PASS classify 60
PASS classify 59
9 passed, 0 failed
```

### Common Mistakes
1. Comparing decimal results with `equals` or `==`.
2. Testing only typical values and skipping the boundaries 90, 89, 60, and 59.
3. Writing the expected value after seeing the output, which turns the test into a copy of the bug.

### Activities
1. Change one expected value so a check fails, read the message, and restore it.
2. Add checks for the grades at 80, 79, 70, and 69.
3. Write checks for `isPassing(score)` before writing the method.
4. Explain why the tip check uses a tolerance.

### Accessibility Practice

Each check prints one complete line that starts with PASS or FAIL, and the last line gives the counts, so the result can be understood from the first word of each line and the final summary.

### Skills Checklist
- [ ] I can write a check with an expected value.
- [ ] I can compare decimals with a tolerance.
- [ ] I can choose boundary tests.
- [ ] I can read PASS and FAIL lines.
- [ ] I know how to signal failure with an exit status.

---

## Lesson 9.2: Testing Classes

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 9.2: Testing a Class

### Learning Objectives
- Create a fresh object for every test.
- Test a value, a change of state, and an error.
- Test that an exception is thrown.

### Concept Explanation

Each test should start from a known state, so create a new object for every test with a *setup* method. Tests that share an object can affect each other and fail in confusing ways.

Test three kinds of behavior: that a method returns the right value (`totalValue` for 3 at 2.50 is 7.5), that a method changes the object correctly (restocking 2 makes the quantity 5), and that invalid use is rejected (restocking a negative amount throws `IllegalArgumentException`).

To test that an exception **does** happen, call the method inside `try`, fail the test if no exception is thrown, and catch the expected exception type. JUnit's `assertThrows` does this in one line.

### Worked Example

```java
public class Lesson_9_2 {
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
                throw new IllegalArgumentException("amount must not be negative");
            }
            quantity += amount;
        }
    }

    static int failures = 0;

    static Item setup() {
        return new Item("Notebook", 3, 2.50);
    }

    static void assertThat(boolean condition, String message) {
        if (!condition) {
            throw new AssertionError(message);
        }
    }

    static void test(String name, Runnable body) {
        try {
            body.run();
            System.out.println("PASS " + name);
        } catch (AssertionError | RuntimeException e) {
            failures++;
            System.out.println("FAIL " + name + ": " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        test("total value is 7.5", () ->
            assertThat(Math.abs(setup().totalValue() - 7.5) < 1e-9, "wrong total"));

        test("restock adds to the quantity", () -> {
            Item item = setup();
            item.restock(2);
            assertThat(item.quantity == 5, "quantity should be 5");
        });

        test("restock rejects a negative amount", () -> {
            boolean thrown = false;
            try {
                setup().restock(-1);
            } catch (IllegalArgumentException e) {
                thrown = true;
            }
            assertThat(thrown, "an exception should have been thrown");
        });

        System.out.println(failures == 0 ? "All tests passed." : failures + " test(s) failed.");
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating testing a class. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Relying on Java's assert statements without enabling assertions, or testing implementation details instead of behavior.
- Allowing tests to share mutable state so their order affects results.
- Assuming a simple comma split handles quoted CSV fields or using an unseeded random source in a reproducibility exercise.
### Activities
1. Write one passing and one failing test for a pure method, then run the tests repeatedly.
2. Seed a Random instance and verify the exercise is reproducible.
3. Analyze a sentence for word counts after applying a documented normalization rule.
4. Test CSV data with quoted commas and explain why a production parser is required.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 9.3: Introduction to Random Numbers

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of introduction to random numbers.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops introduction to random numbers through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Separate deterministic logic from random generation, file I/O, and user interaction. Test methods and object invariants with assertions or a test framework such as JUnit. CSV quoting rules mean a comma split is only a teaching illustration, not a production parser.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_9_3 {
    public static void main(String[] args) {
        java.util.Random random = new java.util.Random(42);
        for (int i = 0; i < 5; i++) System.out.println(random.nextInt(10));
=======
### Expected Behavior or Output

The program prints:
```text
PASS total value is 7.5
PASS restock adds to the quantity
PASS restock rejects a negative amount
All tests passed.
```

### Common Mistakes
1. Sharing one object between tests, so an earlier test changes the later ones.
2. Testing only the successful path and never the error path.
3. Writing an assertion with no message, so a failure says nothing about what went wrong.

### Activities
1. Add a test that `restock(0)` leaves the quantity unchanged.
2. Add a test for an `isValid` method.
3. Break `restock` on purpose and read the failure line.
4. Explain why `setup` creates a new item each time.

### Accessibility Practice

Name each test as a short sentence that says what it checks, so the PASS and FAIL lines read as clear statements. Read the final summary line first.

### Skills Checklist
- [ ] I can create a fresh object per test.
- [ ] I can test a return value.
- [ ] I can test a change of state.
- [ ] I can test that an exception is thrown.
- [ ] I can write a clear test name.

---

## Lesson 9.3: Random Numbers

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 9.3: Random Numbers and Simulation

### Learning Objectives
- Generate random integers and decimals.
- Use a seed to make results repeatable.
- Test random code by its properties.

### Concept Explanation

`java.util.Random` produces random numbers. `random.nextInt(origin, bound)` returns an integer from `origin` up to but **not including** `bound`, so a die roll is `nextInt(1, 7)`. `nextDouble()` returns a decimal from 0.0 up to but not including 1.0.

`new Random(42)` creates a generator with a fixed *seed*: two generators with the same seed produce the same sequence. Without a seed the results change on every run. Because the exact sequence could differ between Java versions, tests should check *properties* (every roll is between 1 and 6) and repeatability, not particular values. For secure randomness (passwords, tokens) use `SecureRandom`, never `Random`.

### Worked Example

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Lesson_9_3 {
    public static void main(String[] args) {
        Random first = new Random(42);
        Random second = new Random(42);
        List<Integer> firstRolls = new ArrayList<>();
        List<Integer> secondRolls = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            firstRolls.add(first.nextInt(1, 7));
            secondRolls.add(second.nextInt(1, 7));
        }
        System.out.println("Same seed gives the same rolls: " + firstRolls.equals(secondRolls));

        Random random = new Random(7);
        boolean inRange = true;
        for (int i = 0; i < 1000; i++) {
            int roll = random.nextInt(1, 7);
            if (roll < 1 || roll > 6) {
                inRange = false;
            }
        }
        System.out.println("All rolls between 1 and 6: " + inRange);

        double decimal = random.nextDouble();
        System.out.println("Decimal in [0, 1): " + (decimal >= 0.0 && decimal < 1.0));

        List<Integer> scores = List.of(82, 91, 76, 88);
        int chosen = scores.get(random.nextInt(scores.size()));
        System.out.println("Chosen score is from the list: " + scores.contains(chosen));
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating introduction to random numbers. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Relying on Java's assert statements without enabling assertions, or testing implementation details instead of behavior.
- Allowing tests to share mutable state so their order affects results.
- Assuming a simple comma split handles quoted CSV fields or using an unseeded random source in a reproducibility exercise.
### Activities
1. Write one passing and one failing test for a pure method, then run the tests repeatedly.
2. Seed a Random instance and verify the exercise is reproducible.
3. Analyze a sentence for word counts after applying a documented normalization rule.
4. Test CSV data with quoted commas and explain why a production parser is required.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 9.4: Analyzing Text Data

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of analyzing text data.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops analyzing text data through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Separate deterministic logic from random generation, file I/O, and user interaction. Test methods and object invariants with assertions or a test framework such as JUnit. CSV quoting rules mean a comma split is only a teaching illustration, not a production parser.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_9_4 {
    public static void main(String[] args) {
        String text = "Java makes data processing testable. Java is explicit.";
        String normalized = text.toLowerCase();
        long count = java.util.Arrays.stream(normalized.split("[^a-z]+"))
            .filter(word -> word.equals("java")).count();
        System.out.println("java occurrences=" + count);
=======
### Expected Behavior or Output

The program prints:
```text
Same seed gives the same rolls: true
All rolls between 1 and 6: true
Decimal in [0, 1): true
Chosen score is from the list: true
```

### Common Mistakes
1. Using `nextInt(1, 6)` for a die and never rolling a 6. The upper limit is excluded.
2. Testing for specific random values that may change between versions.
3. Using `Random` for passwords or tokens, which it is not designed for.

### Activities
1. Run the program three times and compare.
2. Change the seeds and check that the property lines still print `true`.
3. Simulate 600 rolls and count how many of each face appeared (the counts depend on the seed).
4. Explain why a test should check a property rather than a specific random number.

### Accessibility Practice

Print yes or no style results for random behavior, so the announced output is the same on every run and the screen reader does not read unpredictable values.

### Skills Checklist
- [ ] I can use `nextInt` with an excluded upper bound.
- [ ] I can set a seed.
- [ ] I can test properties of random code.
- [ ] I know sequences can differ between versions.
- [ ] I can pick a random list item.

---

## Lesson 9.4: Text Analysis

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 9.4: Data Analysis - Text Analysis

### Learning Objectives
- Split text into words and count them.
- Count word and letter frequencies with a map.
- Produce stable, sorted output.

### Concept Explanation

`text.split(" ")` splits a string into an array of words. Counting uses a map from each word to its count: `counts.merge(word, 1, Integer::sum)` adds one, starting from 1 for a new word.

Map order is only stable if you choose the right class. `LinkedHashMap` keeps the order in which words first appeared. To order by count, copy the entries into a list and sort it with a comparator: count descending first, then letter ascending, so ties print in a fixed order.

The shared text sample is "A student studies programming. Programming develops problem-solving skills." After lower-casing and removing the periods it has 8 words, and `programming` appears twice.

### Worked Example

```java
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Lesson_9_4 {
    public static void main(String[] args) {
        String text = "A student studies programming. Programming develops problem-solving skills.";
        String[] words = text.toLowerCase().replace(".", "").split(" ");

        Map<String, Integer> frequencies = new LinkedHashMap<>();
        for (String word : words) {
            frequencies.merge(word, 1, Integer::sum);
        }

        System.out.println("Word count: " + words.length);
        System.out.println("Word frequencies:");
        for (Map.Entry<String, Integer> entry : frequencies.entrySet()) {
            System.out.println("'" + entry.getKey() + "': " + entry.getValue());
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
        System.out.println("Most common letters:");
        for (int i = 0; i < 3; i++) {
            System.out.println(entries.get(i).getKey() + ": " + entries.get(i).getValue());
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating analyzing text data. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Relying on Java's assert statements without enabling assertions, or testing implementation details instead of behavior.
- Allowing tests to share mutable state so their order affects results.
- Assuming a simple comma split handles quoted CSV fields or using an unseeded random source in a reproducibility exercise.
### Activities
1. Write one passing and one failing test for a pure method, then run the tests repeatedly.
2. Seed a Random instance and verify the exercise is reproducible.
3. Analyze a sentence for word counts after applying a documented normalization rule.
4. Test CSV data with quoted commas and explain why a production parser is required.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 9.5: Working with CSV Data

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of working with csv data.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops working with csv data through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Separate deterministic logic from random generation, file I/O, and user interaction. Test methods and object invariants with assertions or a test framework such as JUnit. CSV quoting rules mean a comma split is only a teaching illustration, not a production parser.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_9_5 {
    public static void main(String[] args) {
        String csv = "name,score\\nAvery,92\\nRiley,85";
        for (String line : csv.split("\\R")) System.out.println(java.util.Arrays.toString(line.split(",", -1)));
        System.out.println("For production CSV, use a parser that supports quoted fields and escaped commas.");
=======
### Expected Behavior or Output

The program prints:
```text
Word count: 8
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
```

### Common Mistakes
1. Counting punctuation as part of a word, so `programming.` and `programming` are different words.
2. Forgetting to lower-case first, so `Programming` and `programming` are counted separately.
3. Relying on `HashMap` order or on an unsorted tie.

### Activities
1. Predict the word count and the count for `programming` before running.
2. Count the words longer than 8 letters.
3. Print the longest word.
4. Change the sort so ties are listed in reverse alphabetical order.

### Accessibility Practice

Read the frequency list in its fixed order. Because the order is stable, you can learn it and compare runs by ear. Print each pair as a short sentence with the same wording every time.

### Skills Checklist
- [ ] I can split text into words.
- [ ] I can count frequencies with a map.
- [ ] I can sort with a tie-break.
- [ ] I can remove punctuation first.
- [ ] I can read a stable report.

---

## Lesson 9.5: Working with CSV Files

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 9.5: Data Analysis - CSV Files

### Learning Objectives
- Create and read a CSV file.
- Split lines into fields and convert numbers.
- Compute an average and a count.

### Concept Explanation

A CSV (comma-separated values) file stores a table as text. The first line names the columns and each later line is a record. The shared student file has the columns `student_id`, `first_name`, `last_name`, `score`, and `active`, and three records.

The standard library has no CSV reader. `line.split(",")` works only for **simple** files: a value that contains a comma inside quotation marks, such as `"Smith, Jr."`, would be split wrongly. For such files use a maintained library or write a real parser.

Every field is text. Convert the score with `Integer.parseInt` and compare `active` with the text `"true"`. With scores 91, 82, and 76 the average is 83.00, and two students are active.

### Worked Example

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Locale;

public class Lesson_9_5 {
    public static void main(String[] args) throws IOException {
        Path file = Path.of("students.csv");
        Files.writeString(file, String.join("\n",
            "student_id,first_name,last_name,score,active",
            "1,Avery,Student,91,true",
            "2,Jordan,Lee,82,true",
            "3,Casey,Smith,76,false") + "\n");

        if (!Files.exists(file)) {
            System.out.println("Error: students.csv was not found.");
            return;
        }
        List<String> lines = Files.readAllLines(file);
        System.out.println("Columns: " + String.join(", ", lines.get(0).split(",")));

        int total = 0;
        int active = 0;
        List<String> students = lines.subList(1, lines.size());
        for (String line : students) {
            String[] row = line.split(",");
            int score = Integer.parseInt(row[3]);
            total += score;
            if (row[4].equals("true")) {
                active++;
            }
            System.out.println(row[0] + ": " + row[1] + " " + row[2] + " scored " + score);
        }

        System.out.println("Students: " + students.size());
        System.out.println("Average score: " + String.format(Locale.US, "%.2f", (double) total / students.size()));
        System.out.println("Active students: " + active);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating working with csv data. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Relying on Java's assert statements without enabling assertions, or testing implementation details instead of behavior.
- Allowing tests to share mutable state so their order affects results.
- Assuming a simple comma split handles quoted CSV fields or using an unseeded random source in a reproducibility exercise.
### Activities
1. Write one passing and one failing test for a pure method, then run the tests repeatedly.
2. Seed a Random instance and verify the exercise is reproducible.
3. Analyze a sentence for word counts after applying a documented normalization rule.
4. Test CSV data with quoted commas and explain why a production parser is required.
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
Columns: student_id, first_name, last_name, score, active
1: Avery Student scored 91
2: Jordan Lee scored 82
3: Casey Smith scored 76
Students: 3
Average score: 83.00
Active students: 2
```

### Common Mistakes
1. Splitting a CSV line at every comma when a value contains a quoted comma.
2. Forgetting to convert the text in the score column to a number.
3. Not skipping the header line, so `parseInt` fails on the text `score`.

### Activities
1. Predict the printed lines before running.
2. Add a fourth student and check the new average.
3. Print only the active students.
4. Explain, with an example, why `"Smith, Jr."` breaks `split(",")`.

### Accessibility Practice

Print one student per line with the same wording each time, so the screen reader announces a repeating pattern that is easy to compare. Read the column names aloud once at the start.

### Skills Checklist
- [ ] I can write and read a CSV file.
- [ ] I can split a line into fields.
- [ ] I convert text fields to numbers.
- [ ] I can compute an average and a count.
- [ ] I know when `split` is not enough.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

# Unit 10: Project-Based Learning — Text Applications

## Overview

This unit develops project-based learning — text applications through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

<<<<<<< HEAD
## Lesson 10.1: Designing Your Project

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of designing your project.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops designing your project through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Treat the project as a set of observable requirements and milestones. Keep domain logic separate from command parsing and persistence, validate before mutation, report errors in plain language, and test normal, boundary, and failure paths.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_10_1 {
    public static void main(String[] args) {
        java.util.List<String> requirements = java.util.List.of("add record", "list records", "validate input", "save changes");
        for (int i = 0; i < requirements.size(); i++) System.out.println((i + 1) + ". " + requirements.get(i));
=======
## Lesson 10.1: Planning a Text-Based Project

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 10.1: Project Planning and Design

### Learning Objectives
- Write a short requirements list.
- Design a command loop with a map of handlers.
- Plan in small steps and test each one.

### Concept Explanation

A project is easier to finish when it is planned in small steps. Write down what the program must do (*requirements*), what information it keeps (*data*), and the commands a person can give (*interface*). Build one small piece, test it, then add the next.

Text-based projects share a *command loop*: show a prompt, read a line, find the matching action, and repeat until the user quits. In Java, a `Map<String, Runnable>` holds actions: the keys are command names and the values are *lambdas*, small unnamed methods. A new command is one new entry, and an unknown command is a failed lookup that prints a helpful message.

The loop stops on `quit` and also when input ends. The example is a skeleton with two commands; typing `help`, `look`, an unknown word, and `quit` shows each path.

### Worked Example

```java
import java.util.Map;
import java.util.Scanner;

public class Lesson_10_1 {
    public static void main(String[] args) {
        Map<String, Runnable> commands = Map.of(
            "help", () -> System.out.println("Commands: help, look, quit"),
            "look", () -> System.out.println("You are in a dark cave."));

        Scanner in = new Scanner(System.in);
        System.out.println("Type a command:");
        String line = in.hasNextLine() ? in.nextLine() : null;
        while (line != null && !line.equals("quit")) {
            Runnable handler = commands.get(line);
            if (handler != null) {
                handler.run();
            } else {
                System.out.println("I don't understand that command. Type help for a list.");
            }
            System.out.println("Type a command:");
            line = in.hasNextLine() ? in.nextLine() : null;
        }
        System.out.println("Goodbye!");
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating designing your project. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Starting implementation before writing observable requirements and acceptance tests.
- Mixing command parsing, domain state, and persistence into one method or class.
- Allowing invalid commands or list indexes to mutate project state without a clear error.
### Activities
1. Write user stories and acceptance criteria before adding a feature to the text application.
2. Implement one room transition or task operation and test the valid and invalid command paths.
3. Separate domain logic from the input/output loop and test the domain logic without terminal input.
4. Run a keyboard-only walkthrough and revise prompts, error messages, and help text.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 10.2: Building a Text Adventure: Rooms and Movement

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of building a text adventure: rooms and movement.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops building a text adventure: rooms and movement through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Treat the project as a set of observable requirements and milestones. Keep domain logic separate from command parsing and persistence, validate before mutation, report errors in plain language, and test normal, boundary, and failure paths.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_10_2 {
    public static void main(String[] args) {
        String currentRoom = "start_room";
        String command = "north";
        if (currentRoom.equals("start_room") && command.equals("north")) currentRoom = "tunnel";
        System.out.println("Current room: " + currentRoom);
=======
### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
help
look
dance
quit
```

the program prints:
```text
Type a command:
Commands: help, look, quit
Type a command:
You are in a dark cave.
Type a command:
I don't understand that command. Type help for a list.
Type a command:
Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
Type a command:
Goodbye!
```

### Common Mistakes
1. Starting to code before listing the requirements.
2. Using a long chain of `if` statements instead of a map of handlers.
3. Forgetting that an unknown command should say what to do next.

### Activities
1. Write five requirements for the text adventure and the to-do list.
2. Add a `score` command that prints the shared scores.
3. Add the aliases `h` and `l` without copying the lambdas.
4. Describe the data for the capstone in three sentences.

### Accessibility Practice

Prompts and responses are on separate lines and every response is a complete sentence. Test the prompts by listening to them before you add features.

### Skills Checklist
- [ ] I can list requirements.
- [ ] I can design a command loop.
- [ ] I can use a map of lambdas.
- [ ] I handle unknown commands.
- [ ] I handle the end of input.

---

## Lesson 10.2: Text Adventure, Part 1: Rooms and Movement

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 10.2: Building a Text-Based Adventure Game (Part 1)

### Learning Objectives
- Represent rooms and exits with a record and a map.
- Move the player by command.
- Handle impossible moves and the end of input.

### Concept Explanation

A room is a record with a `description` and an `exits` map from a direction to the *name* of another room. The program remembers the player's location in one variable. A move looks up the command in the current room's exits; if it is found, the location changes, otherwise the program explains that the move is impossible.

This is the same three-room layout as the Python course: a cave, a tunnel, and a clearing. Part 2 adds items and a locked door.

The example is played with north, east, west, up, south, and quit. The command `up` is not an exit anywhere, so it prints the help message.

### Worked Example

```java
import java.util.Map;
import java.util.Scanner;

public class Lesson_10_2 {
    record Room(String description, Map<String, String> exits) {}

    public static void main(String[] args) {
        Map<String, Room> rooms = Map.of(
            "start_room", new Room(
                "You are in a dimly lit cave. There's a narrow passage to the NORTH.",
                Map.of("north", "tunnel")),
            "tunnel", new Room(
                "The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.",
                Map.of("south", "start_room", "east", "clearing")),
            "clearing", new Room(
                "You've reached a small, sunny clearing. A faint path leads WEST.",
                Map.of("west", "tunnel")));

        Scanner in = new Scanner(System.in);
        String current = "start_room";
        while (true) {
            System.out.println("---");
            System.out.println(rooms.get(current).description());
            System.out.println("What do you want to do?");
            String command = (in.hasNextLine() ? in.nextLine() : "quit").toLowerCase();
            String next = rooms.get(current).exits().get(command);
            if (next != null) {
                current = next;
            } else if (command.equals("quit")) {
                System.out.println("Exiting game. Goodbye!");
                break;
            } else {
                System.out.println("I don't understand that command or you can't go that way.");
            }
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating building a text adventure: rooms and movement. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Starting implementation before writing observable requirements and acceptance tests.
- Mixing command parsing, domain state, and persistence into one method or class.
- Allowing invalid commands or list indexes to mutate project state without a clear error.
### Activities
1. Write user stories and acceptance criteria before adding a feature to the text application.
2. Implement one room transition or task operation and test the valid and invalid command paths.
3. Separate domain logic from the input/output loop and test the domain logic without terminal input.
4. Run a keyboard-only walkthrough and revise prompts, error messages, and help text.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 10.3: Building a Text Adventure: Inventory and Events

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of building a text adventure: inventory and events.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops building a text adventure: inventory and events through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Treat the project as a set of observable requirements and milestones. Keep domain logic separate from command parsing and persistence, validate before mutation, report errors in plain language, and test normal, boundary, and failure paths.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_10_3 {
    public static void main(String[] args) {
        java.util.Set<String> inventory = new java.util.LinkedHashSet<>();
        inventory.add("shiny key");
        inventory.add("map");
        String event = inventory.remove("shiny key") ? "The door unlocks." : "The door remains locked.";
        System.out.println(event + " Inventory: " + inventory);
=======
### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
north
east
west
up
south
quit
```

the program prints:
```text
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You've reached a small, sunny clearing. A faint path leads WEST.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
I don't understand that command or you can't go that way.
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Using a `Map` lookup result without checking for `null`, which throws `NullPointerException` for an unknown direction.
2. Forgetting to treat the end of input as `quit`, so the program loops forever when input is piped in.
3. Misspelling a room name in `exits`, so a move leads to a room that does not exist.

### Activities
1. Trace the six commands by hand and write the room after each one.
2. Add a fourth room reached from the clearing and test it.
3. Add the aliases `n`, `s`, `e`, and `w`.
4. Write a loop that checks that every exit names a real room.

### Accessibility Practice

Each turn prints a separator line, the description, and the prompt, so a whole turn can be read in order. Listen to one turn from start to finish to confirm that a player could follow it without seeing the screen.

### Skills Checklist
- [ ] I can represent rooms with a record.
- [ ] I can move the player by command.
- [ ] I can handle an impossible move.
- [ ] I treat end of input as quit.
- [ ] I can trace a game by hand.

---

## Lesson 10.3: Text Adventure, Part 2: Items and a Locked Door

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 10.3: Building a Text-Based Adventure Game (Part 2)

### Learning Objectives
- Keep items in rooms and in an inventory.
- Implement take and use commands.
- Block and then allow a move through a locked door.

### Concept Explanation

Part 2 adds *state*: items in rooms, an inventory, and a door that is locked until the player uses the key. This is the shared specification used by every language track: three rooms (`start`, `locked_door_room`, `treasure_room`); the commands `north`, `south`, `east`, `west`, `take shiny key`, `use shiny key`, and `quit`; the door between the chamber and the treasure room stays locked until the key is used there; reaching the treasure room ends the game.

Items are a mutable list of names inside each room. A record's fields cannot be reassigned, but a list held in a record can still change, which is what the game needs. Taking an item removes it from the room's list and adds it to the inventory. The locked door is a `boolean` variable, `doorLocked`, checked before a move through the door.

The example is played with: north (into the chamber), north (the locked door refuses), south, take shiny key, north, use shiny key, north (the treasure room).

### Worked Example

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Lesson_10_3 {
    record Room(String description, Map<String, String> exits, List<String> items) {}

    public static void main(String[] args) {
        Map<String, Room> rooms = Map.of(
            "start", new Room("A dark cave.", Map.of("north", "locked_door_room"),
                new ArrayList<>(List.of("shiny key"))),
            "locked_door_room", new Room("A small chamber with a heavy door to the NORTH.",
                Map.of("south", "start", "north", "treasure_room"), new ArrayList<>()),
            "treasure_room", new Room("A glittering room full of treasure. You win!",
                Map.of("south", "locked_door_room"), new ArrayList<>()));

        Scanner in = new Scanner(System.in);
        String current = "start";
        List<String> inventory = new ArrayList<>();
        boolean doorLocked = true;

        while (true) {
            Room room = rooms.get(current);
            System.out.println();
            System.out.println(room.description());
            if (current.equals("treasure_room")) {
                break;
            }
            if (!room.items().isEmpty()) {
                System.out.println("You see: " + String.join(", ", room.items()));
            }
            System.out.println("Your inventory: " + (inventory.isEmpty() ? "empty" : String.join(", ", inventory)));
            System.out.println("What do you want to do?");

            String command = (in.hasNextLine() ? in.nextLine() : "quit").toLowerCase();
            if (command.equals("take shiny key") && room.items().contains("shiny key")) {
                room.items().remove("shiny key");
                inventory.add("shiny key");
                System.out.println("You picked up the shiny key.");
            } else if (command.equals("use shiny key") && current.equals("locked_door_room")
                    && inventory.contains("shiny key")) {
                doorLocked = false;
                System.out.println("You unlocked the door!");
            } else if (room.exits().containsKey(command)) {
                if (current.equals("locked_door_room") && command.equals("north") && doorLocked) {
                    System.out.println("The door is locked! You need a key.");
                } else {
                    current = room.exits().get(command);
                }
            } else if (command.equals("quit")) {
                System.out.println("Exiting game. Goodbye!");
                break;
            } else {
                System.out.println("I don't understand that command.");
            }
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating building a text adventure: inventory and events. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Starting implementation before writing observable requirements and acceptance tests.
- Mixing command parsing, domain state, and persistence into one method or class.
- Allowing invalid commands or list indexes to mutate project state without a clear error.
### Activities
1. Write user stories and acceptance criteria before adding a feature to the text application.
2. Implement one room transition or task operation and test the valid and invalid command paths.
3. Separate domain logic from the input/output loop and test the domain logic without terminal input.
4. Run a keyboard-only walkthrough and revise prompts, error messages, and help text.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 10.4: Developing a Command-Line To-Do Tool

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of developing a command-line to-do tool.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops developing a command-line to-do tool through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Treat the project as a set of observable requirements and milestones. Keep domain logic separate from command parsing and persistence, validate before mutation, report errors in plain language, and test normal, boundary, and failure paths.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_10_4 {
    public static void main(String[] args) {
        java.util.List<String> tasks = new java.util.ArrayList<>(java.util.List.of("Read chapter", "Practice code"));
        tasks.add("Review notes");
        for (int i = 0; i < tasks.size(); i++) System.out.println((i + 1) + ". " + tasks.get(i));
=======
### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
north
north
south
take shiny key
north
use shiny key
north
```

the program prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?
The door is locked! You need a key.

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?
You picked up the shiny key.

A dark cave.
Your inventory: shiny key
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?
You unlocked the door!

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?

A glittering room full of treasure. You win!
```

With no standard input at all, the program ends cleanly and prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Making the door's locked state part of the exits so that the "locked" message can never be reached.
2. Defining an exit to a room that is missing from the `rooms` map, which crashes when the player arrives.
3. Printing a fixed room description that still mentions an item after the player has taken it.

### Activities
1. Play the program with the shown commands and follow each turn on paper.
2. Try `use shiny key` in the cave and describe what happens.
3. Add a second item and require both to open the door.
4. List the game's state (location, inventory, door) and say which command changes each part.

### Accessibility Practice

The room description never mentions the key. A separate 'You see:' line lists items, so the description stays true after the key is taken and the screen reader announces the current state.

### Skills Checklist
- [ ] I can store items in rooms and an inventory.
- [ ] I can implement take and use commands.
- [ ] I can block and allow a move.
- [ ] I can list the game's state.
- [ ] I can keep descriptions true after state changes.

---

## Lesson 10.4: Command-Line To-Do List

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 10.4: Building a Command-Line To-Do List

### Learning Objectives
- Keep records with the shared fields.
- Save and load them as JSON.
- Offer add, view, mark-done, save, load, and quit commands.

### Concept Explanation

A to-do list ties together records, loops, methods, and files. Each task has the shared fields `id`, `title`, `description`, `done`, and `created_at`. The program keeps a list of tasks in memory, shows a numbered menu, and saves the list to `todos.json` when asked and on exit.

Saving uses the teaching JSON helper from Lesson 8.5, included here so the example runs on its own. At start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program: it prints a message and starts with an empty list.

New ids are one more than the highest existing id. The status is shown as the words `done` and `not done`, never with a symbol or color alone.

In the sample session the user adds two tasks, views the list, marks task 2 done, views it again, tries an invalid menu choice, views the list, and quits.

### Worked Example

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class Lesson_10_4 {
    static final class Json {
        private Json() {}

        static String encode(Object value) {
            if (value == null) {
                return "null";
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
                StringBuilder out = new StringBuilder("{");
                for (int i = 0; i < keys.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(quote(keys.get(i))).append(':').append(encode(map.get(keys.get(i))));
                }
                return out.append('}').toString();
            }
            if (value instanceof List<?> list) {
                StringBuilder out = new StringBuilder("[");
                for (int i = 0; i < list.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(encode(list.get(i)));
                }
                return out.append(']').toString();
            }
            throw new IllegalArgumentException("cannot encode " + value.getClass().getSimpleName());
        }

        private static String quote(String text) {
            StringBuilder out = new StringBuilder("\"");
            for (char c : text.toCharArray()) {
                switch (c) {
                    case '"' -> out.append("\\\"");
                    case '\\' -> out.append("\\\\");
                    case '\n' -> out.append("\\n");
                    case '\r' -> out.append("\\r");
                    case '\t' -> out.append("\\t");
                    default -> {
                        if (c < ' ') {
                            out.append(String.format("\\u%04x", (int) c));
                        } else {
                            out.append(c);
                        }
                    }
                }
            }
            return out.append('"').toString();
        }

        static Object decode(String text) {
            Parser parser = new Parser(text);
            Object result = parser.value();
            parser.skip();
            if (parser.pos < text.length()) {
                throw parser.fail("unexpected extra text");
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
                return new IllegalArgumentException(message + " at position " + pos);
            }

            void skip() {
                while (pos < text.length() && Character.isWhitespace(text.charAt(pos))) {
                    pos++;
                }
            }

            Object value() {
                skip();
                if (pos >= text.length()) {
                    throw fail("unexpected end of text");
                }
                char c = text.charAt(pos);
                if (c == '{') return object();
                if (c == '[') return list();
                if (c == '"') return string();
                if (text.startsWith("true", pos)) { pos += 4; return Boolean.TRUE; }
                if (text.startsWith("false", pos)) { pos += 5; return Boolean.FALSE; }
                if (text.startsWith("null", pos)) { pos += 4; return null; }
                if (c == '-' || Character.isDigit(c)) return number();
                throw fail("unexpected character");
            }

            Object number() {
                int start = pos;
                if (text.charAt(pos) == '-') {
                    pos++;
                }
                while (pos < text.length() && (Character.isDigit(text.charAt(pos)) || ".eE+-".indexOf(text.charAt(pos)) >= 0)) {
                    pos++;
                }
                String token = text.substring(start, pos);
                try {
                    return Long.parseLong(token);
                } catch (NumberFormatException notWhole) {
                    try {
                        return Double.parseDouble(token);
                    } catch (NumberFormatException notNumber) {
                        throw fail("bad number");
                    }
                }
            }

            String string() {
                pos++;
                StringBuilder out = new StringBuilder();
                while (true) {
                    if (pos >= text.length()) {
                        throw fail("unterminated string");
                    }
                    char c = text.charAt(pos++);
                    if (c == '"') {
                        return out.toString();
                    }
                    if (c != '\\') {
                        out.append(c);
                        continue;
                    }
                    if (pos >= text.length()) {
                        throw fail("bad escape");
                    }
                    char e = text.charAt(pos++);
                    switch (e) {
                        case 'n' -> out.append('\n');
                        case 't' -> out.append('\t');
                        case 'r' -> out.append('\r');
                        case '"' -> out.append('"');
                        case '\\' -> out.append('\\');
                        case '/' -> out.append('/');
                        case 'u' -> {
                            if (pos + 4 > text.length()) {
                                throw fail("bad escape");
                            }
                            out.append((char) Integer.parseInt(text.substring(pos, pos + 4), 16));
                            pos += 4;
                        }
                        default -> throw fail("bad escape");
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
                    if (pos >= text.length() || text.charAt(pos) != '"') {
                        throw fail("expected a key");
                    }
                    String key = string();
                    skip();
                    if (pos >= text.length() || text.charAt(pos) != ':') {
                        throw fail("expected ':'");
                    }
                    pos++;
                    map.put(key, value());
                    skip();
                    if (pos >= text.length()) {
                        throw fail("unterminated object");
                    }
                    char d = text.charAt(pos++);
                    if (d == '}') {
                        return map;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail("expected ',' or '}'");
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
                        throw fail("unterminated list");
                    }
                    char d = text.charAt(pos++);
                    if (d == ']') {
                        return items;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail("expected ',' or ']'");
                    }
                }
            }
        }
    }

    static final Path TODO_FILE = Path.of("todos.json");
    static List<Map<String, Object>> todos = new ArrayList<>();

    static void loadTodos() throws IOException {
        if (!Files.exists(TODO_FILE)) {
            System.out.println("No existing tasks found.");
            todos = new ArrayList<>();
            return;
        }
        try {
            List<Map<String, Object>> loaded = new ArrayList<>();
            for (Object entry : (List<?>) Json.decode(Files.readString(TODO_FILE))) {
                Map<String, Object> task = new LinkedHashMap<>();
                for (Map.Entry<?, ?> field : ((Map<?, ?>) entry).entrySet()) {
                    task.put(field.getKey().toString(), field.getValue());
                }
                loaded.add(task);
            }
            todos = loaded;
            System.out.println("Tasks loaded.");
        } catch (IllegalArgumentException | ClassCastException e) {
            System.out.println("Error: todos.json is not valid JSON. Starting with an empty list.");
            todos = new ArrayList<>();
        }
    }

    static void saveTodos() throws IOException {
        Files.writeString(TODO_FILE, Json.encode(todos));
        System.out.println("Tasks saved.");
    }

    static long nextId() {
        long highest = 0;
        for (Map<String, Object> task : todos) {
            highest = Math.max(highest, (Long) task.get("id"));
        }
        return highest + 1;
    }

    static void addTask(String title, String description) {
        if (title.isBlank()) {
            System.out.println("A title is required.");
            return;
        }
        Map<String, Object> task = new LinkedHashMap<>();
        task.put("id", nextId());
        task.put("title", title.strip());
        task.put("description", description.strip());
        task.put("done", false);
        task.put("created_at", LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss")));
        todos.add(task);
        System.out.println("Task '" + title.strip() + "' added.");
    }

    static void viewTasks() {
        if (todos.isEmpty()) {
            System.out.println("No tasks in your list.");
            return;
        }
        System.out.println("--- Your To-Do List ---");
        for (Map<String, Object> task : todos) {
            String status = Boolean.TRUE.equals(task.get("done")) ? "done" : "not done";
            System.out.println(task.get("id") + ". " + task.get("title") + " (" + status + ")");
        }
        System.out.println("-----------------------");
    }

    static void markDone(String text) {
        long id;
        try {
            id = Long.parseLong(text.trim());
        } catch (NumberFormatException e) {
            System.out.println("Please enter a whole number.");
            return;
        }
        for (Map<String, Object> task : todos) {
            if (task.get("id").equals(id)) {
                task.put("done", true);
                System.out.println("Task '" + task.get("title") + "' marked as done.");
                return;
            }
        }
        System.out.println("No task has that number.");
    }

    static void showMenu() {
        System.out.println();
        System.out.println("--- To-Do List Menu ---");
        System.out.println("1. Add Task");
        System.out.println("2. View Tasks");
        System.out.println("3. Mark Task Done");
        System.out.println("4. Save Tasks");
        System.out.println("5. Load Tasks");
        System.out.println("6. Quit");
        System.out.println("-----------------------");
    }

    static String next(Scanner in, String fallback) {
        return in.hasNextLine() ? in.nextLine() : fallback;
    }

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        loadTodos();
        while (true) {
            showMenu();
            System.out.println("Enter your choice (1-6):");
            String choice = next(in, "6");
            switch (choice) {
                case "1" -> {
                    System.out.println("Enter task title:");
                    String title = next(in, "");
                    System.out.println("Enter task description:");
                    String description = next(in, "");
                    addTask(title, description);
                }
                case "2" -> viewTasks();
                case "3" -> {
                    viewTasks();
                    System.out.println("Enter task number to mark done:");
                    markDone(next(in, ""));
                }
                case "4" -> saveTodos();
                case "5" -> loadTodos();
                case "6" -> {
                    saveTodos();
                    System.out.println("Goodbye!");
                    return;
                }
                default -> System.out.println("Invalid choice. Please try again.");
            }
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating developing a command-line to-do tool. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Starting implementation before writing observable requirements and acceptance tests.
- Mixing command parsing, domain state, and persistence into one method or class.
- Allowing invalid commands or list indexes to mutate project state without a clear error.
### Activities
1. Write user stories and acceptance criteria before adding a feature to the text application.
2. Implement one room transition or task operation and test the valid and invalid command paths.
3. Separate domain logic from the input/output loop and test the domain logic without terminal input.
4. Run a keyboard-only walkthrough and revise prompts, error messages, and help text.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 10.5: Refinement, Accessibility, and User Experience

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of refinement, accessibility, and user experience.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops refinement, accessibility, and user experience through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Treat the project as a set of observable requirements and milestones. Keep domain logic separate from command parsing and persistence, validate before mutation, report errors in plain language, and test normal, boundary, and failure paths.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_10_5 {
    public static void main(String[] args) {
        String[] prompts = {"Enter a command", "Choose a numbered action", "Type quit to exit"};
        for (String prompt : prompts) System.out.println(prompt);
        System.out.println("Use consistent prompts and report validation errors in plain language.");
=======
### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
1
Study programming
Finish Unit 10
1
Review scores
Check the four scores
2
3
2
3
7
2
6
```

the program prints:
```text
No existing tasks found.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Study programming' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Review scores' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------
Enter task number to mark done:
Task 'Review scores' marked as done.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------
Enter task number to mark done:
No task has that number.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Tasks saved.
Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
No existing tasks found.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Tasks saved.
Goodbye!
```

### Common Mistakes
1. Saving the file but never loading it, so tasks disappear between runs.
2. Reusing a deleted task's id, which can confuse saved references.
3. Letting a damaged `todos.json` crash the program instead of printing a message.

### Activities
1. Run the sample session, then run the program again typing `2` and `6` to see the saved tasks.
2. Add a command to delete a task by number.
3. Open `todos.json` and read the saved text. Edit it to remove a bracket and run the program again.
4. Show each task's description in the view command.

### Accessibility Practice

Every menu is printed as numbered lines and every prompt is on its own line. The status words are `done` and `not done`, not symbols, so the list reads clearly in speech and braille.

### Skills Checklist
- [ ] I can keep records with the shared fields.
- [ ] I can save and load JSON.
- [ ] I handle a missing or damaged file.
- [ ] I keep ids unique.
- [ ] I show status in words.

---

## Lesson 10.5: User Experience and Input Validation

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 10.5: Refining User Experience and Validation

### Learning Objectives
- Write reusable validation methods.
- Limit retries and handle the end of input.
- Write clear, accessible messages.

### Concept Explanation

Reusable validation methods make every menu and form consistent. `askNumber(in, prompt, low, high, attempts)` prints a prompt, reads a line, converts it, checks the range, and either returns the number or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns `null`. `askYesNo(in, prompt)` accepts `y`, `yes`, `n`, and `no` in any letter case. Returning the wrapper types `Integer` and `Boolean` lets `null` mean "no answer".

Good messages say *what was wrong* and *what to do*: "Enter a whole number from 0 to 100," not "Invalid." They never depend on color, position, or symbols alone, and they use the same wording every time.

The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y.

### Worked Example

```java
import java.util.Scanner;

public class Lesson_10_5 {
    static Integer askNumber(Scanner in, String prompt, int low, int high, int attempts) {
        for (int attempt = 1; attempt <= attempts; attempt++) {
            System.out.println(prompt);
            if (!in.hasNextLine()) {
                return null;
            }
            String text = in.nextLine().trim();
            try {
                int number = Integer.parseInt(text);
                if (number >= low && number <= high) {
                    return number;
                }
            } catch (NumberFormatException e) {
                // fall through to the message below
            }
            System.out.println("Enter a whole number from " + low + " to " + high + ". You have "
                + (attempts - attempt) + " attempt(s) left.");
        }
        return null;
    }

    static Boolean askYesNo(Scanner in, String prompt) {
        while (true) {
            System.out.println(prompt + " (yes or no)");
            if (!in.hasNextLine()) {
                return null;
            }
            String text = in.nextLine().trim().toLowerCase();
            if (text.equals("y") || text.equals("yes")) {
                return true;
            }
            if (text.equals("n") || text.equals("no")) {
                return false;
            }
            System.out.println("Please answer yes or no.");
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Integer score = askNumber(in, "Enter a score from 0 to 100:", 0, 100, 3);
        if (score != null) {
            System.out.println("Accepted score: " + score);
        } else {
            System.out.println("No valid score was entered.");
        }

        Boolean keep = askYesNo(in, "Save this score?");
        System.out.println("Save answer: " + keep);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating refinement, accessibility, and user experience. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Starting implementation before writing observable requirements and acceptance tests.
- Mixing command parsing, domain state, and persistence into one method or class.
- Allowing invalid commands or list indexes to mutate project state without a clear error.
### Activities
1. Write user stories and acceptance criteria before adding a feature to the text application.
2. Implement one room transition or task operation and test the valid and invalid command paths.
3. Separate domain logic from the input/output loop and test the domain logic without terminal input.
4. Run a keyboard-only walkthrough and revise prompts, error messages, and help text.
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
maybe
y
```

the program prints:
```text
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 2 attempt(s) left.
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 1 attempt(s) left.
Enter a score from 0 to 100:
Accepted score: 88
Save this score? (yes or no)
Please answer yes or no.
Save this score? (yes or no)
Save answer: true
```

With no standard input at all, the program ends cleanly and prints:
```text
Enter a score from 0 to 100:
No valid score was entered.
Save this score? (yes or no)
Save answer: null
```

### Common Mistakes
1. Writing the message "Invalid" without saying what is valid.
2. Accepting a decimal such as 88.5 for a field that requires a whole number.
3. Looping forever on bad input instead of limiting attempts.

### Activities
1. Run the sample input and read each message aloud.
2. Run with three invalid numbers and read the final message.
3. Add `askText(in, prompt)` that rejects empty answers.
4. Rewrite two messages from earlier lessons so they say what to do next.

### Accessibility Practice

Check that every error message ends with an action the user can take, and that the same situation always produces the same words.

### Skills Checklist
- [ ] I can write reusable validation methods.
- [ ] I limit retries.
- [ ] I handle the end of input.
- [ ] I write messages that say what to do.
- [ ] I keep wording consistent.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

This unit develops capstone — accessible personal data manager through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

<<<<<<< HEAD
## Lesson 11.1: Capstone Requirements and Architecture

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of capstone requirements and architecture.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops capstone requirements and architecture through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Treat the project as a set of observable requirements and milestones. Keep domain logic separate from command parsing and persistence, validate before mutation, report errors in plain language, and test normal, boundary, and failure paths.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_11_1 {
    public static void main(String[] args) {
        java.util.List<String> features = java.util.List.of("keyboard-driven menu", "named records", "validated fields", "file persistence", "automated tests");
        System.out.println("Personal data manager requirements:");
        features.forEach(feature -> System.out.println("- " + feature));
=======
## Lesson 11.1: Capstone: Requirements and Design

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 11.1: Introduction to NiceGUI (capstone planning)

### Learning Objectives
- Write requirements for a personal data manager.
- Define the shared record schema as a Java record.
- Check records against the validation rules before building features.

### Concept Explanation

The capstone is a *personal data manager*: a program that keeps a list of records, lets the user add, view, search, change, complete, and delete them, and saves them to a file. In the Java track it is a text program, so it runs from the terminal and is fully usable with a screen reader or braille display.

**Shared record schema (all general-purpose language tracks).** Every record has `id` (unique whole number), `title`, `description`, `category`, `created_at`, and `updated_at` (ISO 8601 text). A project may add fields, such as an optional `done` flag, but must not remove these. Java names use camel case (`createdAt`), and the stored JSON uses the shared names. The class is called `Entry` here, because `Record` would hide `java.lang.Record`, the parent of all records.

**Validation rules.** A record must have a non-empty title and a non-empty category. Timestamps are ISO 8601 text such as `2026-01-15T09:00:00`.

Design before coding: list the operations, then the data, then the messages. The example checks the three shared sample records against the rules and prints them as a plain-text list.

### Worked Example

```java
import java.util.List;

public class Lesson_11_1 {
    record Entry(int id, String title, String description, String category, String createdAt, String updatedAt) {}

    static String validate(String title, String category) {
        if (title == null || title.isBlank()) {
            return "A title is required.";
        }
        if (category == null || category.isBlank()) {
            return "A category is required.";
        }
        return null;
    }

    public static void main(String[] args) {
        List<Entry> sample = List.of(
            new Entry(1, "Notebook", "Course notes", "supplies", "2026-01-15T09:00:00", "2026-01-15T09:00:00"),
            new Entry(2, "Pencil", "Box of 10", "supplies", "2026-01-15T09:05:00", "2026-01-15T09:05:00"),
            new Entry(3, "Study plan", "Weekly schedule", "planning", "2026-01-15T09:10:00", "2026-01-15T09:10:00"));

        for (Entry entry : sample) {
            String problem = validate(entry.title(), entry.category());
            System.out.println(entry.id() + ". " + entry.title() + " [" + entry.category() + "] - "
                + (problem == null ? "valid" : problem));
        }

        System.out.println(validate("  ", "supplies"));
        System.out.println(validate("Ruler", ""));
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating capstone requirements and architecture. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using record display or object identity as a substitute for a stable application identifier.
- Persisting data before validating it or overwriting a valid file after a failed update.
- Testing individual methods only and missing broken integration between menu, model, validation, and storage.
### Activities
1. Write a record schema and identify required, optional, and unique fields before implementation.
2. Test create, read, update, and delete operations against both in-memory and persisted data.
3. Simulate malformed or unavailable storage and verify existing valid data is not silently lost.
4. Demonstrate the complete manager from startup through validation, persistence, restart, and retrieval.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 11.2: Data Model and Storage

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of data model and storage.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops data model and storage through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Treat the project as a set of observable requirements and milestones. Keep domain logic separate from command parsing and persistence, validate before mutation, report errors in plain language, and test normal, boundary, and failure paths.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_11_2 {
    public static void main(String[] args) {
        record Record(int id, String title, String description, String category,
                      String createdAt, String updatedAt) {}
        java.util.List<Record> records = new java.util.ArrayList<>();
        records.add(new Record(1, "Course project", "Personal data manager", "education",
                               "2026-11-01", "2026-11-01"));
        System.out.println(records.get(0));
=======
### Expected Behavior or Output

The program prints:
```text
1. Notebook [supplies] - valid
2. Pencil [supplies] - valid
3. Study plan [planning] - valid
A title is required.
A category is required.
```

### Common Mistakes
1. Starting to build features before agreeing on the record fields.
2. Allowing a record with an empty title because the check was left for later.
3. Storing timestamps in different formats in different places.

### Activities
1. Write the seven operations as a numbered list of requirements.
2. Add one project-specific field and say how it is validated.
3. Write three sample records for your own project.
4. Describe in plain sentences what each shared field means.

### Accessibility Practice

Design the screen output as lines of plain text: one record per line, with the same field order each time. Decide the wording of every message now so that it can be tested.

### Skills Checklist
- [ ] I can write requirements.
- [ ] I know the shared record fields.
- [ ] I can write validation rules.
- [ ] I can describe sample data.
- [ ] I can plan messages before coding.

---

## Lesson 11.2: Capstone: Data Model and Storage

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 11.2: Data Model and Storage

### Learning Objectives
- Store records as record objects.
- Save and load them as JSON.
- Confirm that every field survives a round trip.

### Concept Explanation

Records are stored as a list of Java records in memory and as a JSON array on disk. The storage layer has two methods: `saveEntries(path, entries)` and `loadEntries(path)`. Loading returns a small record holding the entries and a message, so the caller decides what to do when the file is missing or damaged.

An `Entry` is converted to a map for saving (`toMap`) and rebuilt from a decoded map when loading (`toEntry`), which checks that each field is present and has the right type. The optional `done` field defaults to `false`.

The example uses the teaching JSON helper from Lesson 8.5 (included so the program runs on its own). After saving and reloading it compares the lists; records compare by value, so this *round-trip test* checks every field of every entry. It is the first acceptance test for storage.

### Worked Example

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class Lesson_11_2 {
    static final class Json {
        private Json() {}

        static String encode(Object value) {
            if (value == null) {
                return "null";
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
                StringBuilder out = new StringBuilder("{");
                for (int i = 0; i < keys.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(quote(keys.get(i))).append(':').append(encode(map.get(keys.get(i))));
                }
                return out.append('}').toString();
            }
            if (value instanceof List<?> list) {
                StringBuilder out = new StringBuilder("[");
                for (int i = 0; i < list.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(encode(list.get(i)));
                }
                return out.append(']').toString();
            }
            throw new IllegalArgumentException("cannot encode " + value.getClass().getSimpleName());
        }

        private static String quote(String text) {
            StringBuilder out = new StringBuilder("\"");
            for (char c : text.toCharArray()) {
                switch (c) {
                    case '"' -> out.append("\\\"");
                    case '\\' -> out.append("\\\\");
                    case '\n' -> out.append("\\n");
                    case '\r' -> out.append("\\r");
                    case '\t' -> out.append("\\t");
                    default -> {
                        if (c < ' ') {
                            out.append(String.format("\\u%04x", (int) c));
                        } else {
                            out.append(c);
                        }
                    }
                }
            }
            return out.append('"').toString();
        }

        static Object decode(String text) {
            Parser parser = new Parser(text);
            Object result = parser.value();
            parser.skip();
            if (parser.pos < text.length()) {
                throw parser.fail("unexpected extra text");
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
                return new IllegalArgumentException(message + " at position " + pos);
            }

            void skip() {
                while (pos < text.length() && Character.isWhitespace(text.charAt(pos))) {
                    pos++;
                }
            }

            Object value() {
                skip();
                if (pos >= text.length()) {
                    throw fail("unexpected end of text");
                }
                char c = text.charAt(pos);
                if (c == '{') return object();
                if (c == '[') return list();
                if (c == '"') return string();
                if (text.startsWith("true", pos)) { pos += 4; return Boolean.TRUE; }
                if (text.startsWith("false", pos)) { pos += 5; return Boolean.FALSE; }
                if (text.startsWith("null", pos)) { pos += 4; return null; }
                if (c == '-' || Character.isDigit(c)) return number();
                throw fail("unexpected character");
            }

            Object number() {
                int start = pos;
                if (text.charAt(pos) == '-') {
                    pos++;
                }
                while (pos < text.length() && (Character.isDigit(text.charAt(pos)) || ".eE+-".indexOf(text.charAt(pos)) >= 0)) {
                    pos++;
                }
                String token = text.substring(start, pos);
                try {
                    return Long.parseLong(token);
                } catch (NumberFormatException notWhole) {
                    try {
                        return Double.parseDouble(token);
                    } catch (NumberFormatException notNumber) {
                        throw fail("bad number");
                    }
                }
            }

            String string() {
                pos++;
                StringBuilder out = new StringBuilder();
                while (true) {
                    if (pos >= text.length()) {
                        throw fail("unterminated string");
                    }
                    char c = text.charAt(pos++);
                    if (c == '"') {
                        return out.toString();
                    }
                    if (c != '\\') {
                        out.append(c);
                        continue;
                    }
                    if (pos >= text.length()) {
                        throw fail("bad escape");
                    }
                    char e = text.charAt(pos++);
                    switch (e) {
                        case 'n' -> out.append('\n');
                        case 't' -> out.append('\t');
                        case 'r' -> out.append('\r');
                        case '"' -> out.append('"');
                        case '\\' -> out.append('\\');
                        case '/' -> out.append('/');
                        case 'u' -> {
                            if (pos + 4 > text.length()) {
                                throw fail("bad escape");
                            }
                            out.append((char) Integer.parseInt(text.substring(pos, pos + 4), 16));
                            pos += 4;
                        }
                        default -> throw fail("bad escape");
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
                    if (pos >= text.length() || text.charAt(pos) != '"') {
                        throw fail("expected a key");
                    }
                    String key = string();
                    skip();
                    if (pos >= text.length() || text.charAt(pos) != ':') {
                        throw fail("expected ':'");
                    }
                    pos++;
                    map.put(key, value());
                    skip();
                    if (pos >= text.length()) {
                        throw fail("unterminated object");
                    }
                    char d = text.charAt(pos++);
                    if (d == '}') {
                        return map;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail("expected ',' or '}'");
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
                        throw fail("unterminated list");
                    }
                    char d = text.charAt(pos++);
                    if (d == ']') {
                        return items;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail("expected ',' or ']'");
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
        map.put("id", entry.id());
        map.put("title", entry.title());
        map.put("description", entry.description());
        map.put("category", entry.category());
        map.put("created_at", entry.createdAt());
        map.put("updated_at", entry.updatedAt());
        map.put("done", entry.done());
        return map;
    }

    static String text(Map<?, ?> map, String key) {
        if (!(map.get(key) instanceof String value)) {
            throw new IllegalArgumentException("missing field " + key);
        }
        return value;
    }

    static Entry toEntry(Object raw) {
        if (!(raw instanceof Map<?, ?> map)) {
            throw new IllegalArgumentException("a record must be an object");
        }
        if (!(map.get("id") instanceof Long id)) {
            throw new IllegalArgumentException("missing field id");
        }
        boolean done = map.get("done") instanceof Boolean flag && flag;
        return new Entry(id.intValue(), text(map, "title"), text(map, "description"), text(map, "category"),
            text(map, "created_at"), text(map, "updated_at"), done);
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
            return new Loaded(List.of(), "Could not open " + path + ": file not found.");
        }
        try {
            List<Entry> entries = new ArrayList<>();
            for (Object raw : (List<?>) Json.decode(Files.readString(path))) {
                entries.add(toEntry(raw));
            }
            return new Loaded(entries, null);
        } catch (IllegalArgumentException | ClassCastException e) {
            return new Loaded(List.of(), "The data file is not valid: " + e.getMessage());
        }
    }

    public static void main(String[] args) throws IOException {
        List<Entry> sample = List.of(
            new Entry(1, "Notebook", "Course notes", "supplies", "2026-01-15T09:00:00", "2026-01-15T09:00:00", false),
            new Entry(2, "Pencil", "Box of 10", "supplies", "2026-01-15T09:05:00", "2026-01-15T09:05:00", false),
            new Entry(3, "Study plan", "Weekly schedule", "planning", "2026-01-15T09:10:00", "2026-01-15T09:10:00", false));

        Path file = Path.of("records.json");
        saveEntries(file, sample);
        Loaded loaded = loadEntries(file);
        System.out.println("Round trip preserved all fields: " + loaded.entries().equals(sample));
        System.out.println("Records loaded: " + loaded.entries().size());
        System.out.println(loaded.problem());

        System.out.println(loadEntries(Path.of("missing.json")).problem());

        Files.writeString(Path.of("broken.json"), "[{\"id\": 1,");
        System.out.println(loadEntries(Path.of("broken.json")).problem());
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating data model and storage. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using record display or object identity as a substitute for a stable application identifier.
- Persisting data before validating it or overwriting a valid file after a failed update.
- Testing individual methods only and missing broken integration between menu, model, validation, and storage.
### Activities
1. Write a record schema and identify required, optional, and unique fields before implementation.
2. Test create, read, update, and delete operations against both in-memory and persisted data.
3. Simulate malformed or unavailable storage and verify existing valid data is not silently lost.
4. Demonstrate the complete manager from startup through validation, persistence, restart, and retrieval.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 11.3: Displaying and Managing Records

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of displaying and managing records.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops displaying and managing records through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Treat the project as a set of observable requirements and milestones. Keep domain logic separate from command parsing and persistence, validate before mutation, report errors in plain language, and test normal, boundary, and failure paths.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_11_3 {
    public static void main(String[] args) {
        java.util.List<String> names = new java.util.ArrayList<>(java.util.List.of("Avery", "Riley"));
        System.out.println("Records: " + names.size());
        for (int i = 0; i < names.size(); i++) System.out.println((i + 1) + ": " + names.get(i));
        names.remove("Riley");
        System.out.println("After deletion: " + names);
=======
### Expected Behavior or Output

The program prints:
```text
Round trip preserved all fields: true
Records loaded: 3
null
Could not open missing.json: file not found.
The data file is not valid: expected a key at position 10
```

### Common Mistakes
1. Overwriting the data file with an empty list after a failed load.
2. Saving only some of the fields.
3. Assuming a loaded record has every field without checking.

### Activities
1. Run the program and open `records.json` to read the saved text.
2. Add a field to `Entry`, save it, and confirm that it survives the round trip.
3. Make `toEntry` reject a record whose title is blank.
4. Explain why `loadEntries` returns a message and does not throw.

### Accessibility Practice

Messages that name the file and the problem read clearly in speech. After saving, read the file in the terminal to confirm it contains what you expect.

### Skills Checklist
- [ ] I can store records in record objects.
- [ ] I can save and load JSON.
- [ ] I can run a round-trip test.
- [ ] I handle missing and damaged files.
- [ ] I do not overwrite good data after a failed load.

---

## Lesson 11.3: Capstone: Core Operations

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 11.3: Displaying and Managing Items

### Learning Objectives
- Add, list, search, change, complete, and delete records.
- Assign new ids and update timestamps correctly.
- Return a message when an operation cannot be done.

### Concept Explanation

A `Manager` class holds the entries and offers one method per operation. Each method that can fail returns an `Outcome` (the entry and a message) or a message, so the user interface can show it and decide what to do. New ids are one more than the highest id, so ids are never reused while higher ids exist. Updating an entry sets `updatedAt` but never changes `createdAt`, which is `final`. Completing an entry sets the optional `done` field to `true` and counts as an update.

For repeatable output the example passes in a *fake clock* that returns a new fixed time on each call. A real program passes a supplier that reads the real time.

The example adds the three shared sample records, lists them, searches for "note", changes one description, completes one entry, deletes one, and tries to delete an entry that does not exist.

### Worked Example

```java
import java.util.*;
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
        return id + ". " + title + " [" + category + "] (" + (done ? "done" : "not done") + ")";
    }
}

record Outcome(Entry entry, String message) {}

class Clocks {
    static Supplier<String> fake() {
        int[] ticks = {0};
        return () -> {
            ticks[0]++;
            return String.format("2026-01-15T10:00:%02d", ticks[0]);
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
            return "A title is required.";
        }
        if (category == null || category.isBlank()) {
            return "A category is required.";
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
            return new Outcome(null, "No record has that id.");
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
            return "No record has that id.";
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
        manager.add("Notebook", "Course notes", "supplies");
        manager.add("Pencil", "Box of 10", "supplies");
        manager.add("Study plan", "Weekly schedule", "planning");
        show(manager);

        System.out.println("Search for 'note':");
        for (Entry entry : manager.search("note")) {
            System.out.println(entry.title);
        }

        manager.update(2, null, "Box of 12", null, null);
        manager.complete(3);
        System.out.println(manager.find(2).description + " " + manager.find(2).updatedAt);

        String first = manager.delete(1);
        System.out.println(first == null ? "Deleted record 1." : first);
        String second = manager.delete(99);
        System.out.println(second == null ? "Deleted record 99." : second);
        show(manager);
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating displaying and managing records. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using record display or object identity as a substitute for a stable application identifier.
- Persisting data before validating it or overwriting a valid file after a failed update.
- Testing individual methods only and missing broken integration between menu, model, validation, and storage.
### Activities
1. Write a record schema and identify required, optional, and unique fields before implementation.
2. Test create, read, update, and delete operations against both in-memory and persisted data.
3. Simulate malformed or unavailable storage and verify existing valid data is not silently lost.
4. Demonstrate the complete manager from startup through validation, persistence, restart, and retrieval.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 11.4: Validation, Testing, and Error Recovery

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of validation, testing, and error recovery.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops validation, testing, and error recovery through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Treat the project as a set of observable requirements and milestones. Keep domain logic separate from command parsing and persistence, validate before mutation, report errors in plain language, and test normal, boundary, and failure paths.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_11_4 {
    public static void main(String[] args) {
        java.util.function.Predicate<String> validName = name -> name != null && !name.isBlank();
        for (String name : new String[] {"Avery", "", "Riley"})
            System.out.println("\"" + name + "\" valid=" + validName.test(name));
=======
### Expected Behavior or Output

The program prints:
```text
1. Notebook [supplies] (not done)
2. Pencil [supplies] (not done)
3. Study plan [planning] (not done)
Search for 'note':
Notebook
Box of 12 2026-01-15T10:00:04
Deleted record 1.
No record has that id.
2. Pencil [supplies] (not done)
3. Study plan [planning] (done)
```

### Common Mistakes
1. Reusing a deleted entry's id by counting the list size instead of using the highest id.
2. Changing `createdAt` when updating (the field is `final` to prevent this).
3. Throwing an exception for a missing record where a message to display is more helpful.

### Activities
1. Predict the output before running.
2. Add `listByCategory(category)` to `Manager`.
3. Add a rule that blocks completing an entry that is already complete, with a message.
4. Explain how the fake clock makes the output repeatable.

### Accessibility Practice

List output uses the same fixed format for every record and the words `done` and `not done`. Search results print only titles, so each line is short.

### Skills Checklist
- [ ] I can implement add, list, search, change, complete, and delete.
- [ ] I assign unique ids.
- [ ] I update timestamps correctly.
- [ ] I return clear messages for failures.
- [ ] I can make output repeatable with a fake clock.

---

## Lesson 11.4: Capstone: Validation and Acceptance Tests

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 11.4: Testing and Refinement

### Learning Objectives
- Run the shared acceptance tests.
- Verify that validation rejects bad data.
- Read and interpret test results.

### Concept Explanation

The shared acceptance tests describe behavior that every language track's capstone must show:

1. Adding a record with an empty title is rejected with a clear message.
2. A new record receives an unused `id`.
3. Updating a record changes `updated_at` but not `created_at`.
4. Deleting a record removes only that record.
5. Saving and reloading preserves all fields and values (shown in Lesson 11.2).
6. Every message and control can be used without color or a mouse (checked by hand in Lesson 11.5).

This lesson automates tests 1 to 4 and also tests completion and the rejection of a blank title in an update. Each test builds a new `Manager`, so tests cannot affect each other. The fake clock keeps timestamps predictable so a test can check that `updatedAt` changed while `createdAt` did not.

### Worked Example

```java
import java.util.*;
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
        return id + ". " + title + " [" + category + "] (" + (done ? "done" : "not done") + ")";
    }
}

record Outcome(Entry entry, String message) {}

class Clocks {
    static Supplier<String> fake() {
        int[] ticks = {0};
        return () -> {
            ticks[0]++;
            return String.format("2026-01-15T10:00:%02d", ticks[0]);
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
            return "A title is required.";
        }
        if (category == null || category.isBlank()) {
            return "A category is required.";
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
            return new Outcome(null, "No record has that id.");
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
            return "No record has that id.";
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
            System.out.println("PASS " + name);
        } catch (AssertionError | RuntimeException e) {
            failures++;
            System.out.println("FAIL " + name + ": " + e.getMessage());
        }
    }

    static Manager fresh() {
        Manager manager = new Manager(Clocks.fake());
        manager.add("Notebook", "Course notes", "supplies");
        manager.add("Pencil", "Box of 10", "supplies");
        manager.add("Study plan", "Weekly schedule", "planning");
        return manager;
    }

    public static void main(String[] args) {
        test("1. an empty title is rejected", () -> {
            Manager manager = fresh();
            Outcome outcome = manager.add("   ", "x", "supplies");
            assertThat(outcome.entry() == null && "A title is required.".equals(outcome.message()), "expected the title message");
            assertThat(manager.entries.size() == 3, "the list should be unchanged");
        });

        test("2. a new record gets an unused id", () -> {
            Manager manager = fresh();
            manager.delete(2);
            Outcome outcome = manager.add("Ruler", "30 cm", "supplies");
            assertThat(outcome.entry() != null && outcome.entry().id == 4, "expected id 4");
        });

        test("3. update changes updatedAt but not createdAt", () -> {
            Manager manager = fresh();
            Entry entry = manager.find(1);
            String createdBefore = entry.createdAt;
            String updatedBefore = entry.updatedAt;
            manager.update(1, null, "Lecture notes", null, null);
            assertThat(entry.createdAt.equals(createdBefore), "createdAt changed");
            assertThat(!entry.updatedAt.equals(updatedBefore), "updatedAt did not change");
        });

        test("4. delete removes only that record", () -> {
            Manager manager = fresh();
            manager.delete(2);
            List<Integer> ids = new ArrayList<>();
            for (Entry entry : manager.entries) {
                ids.add(entry.id);
            }
            assertThat(ids.equals(List.of(1, 3)), "wrong records remain: " + ids);
        });

        test("5. complete marks done and updates the record", () -> {
            Manager manager = fresh();
            Entry entry = manager.complete(3).entry();
            assertThat(entry != null && entry.done && !entry.updatedAt.equals(entry.createdAt), "completion not recorded");
        });

        test("6. a blank title cannot be saved by update", () -> {
            Manager manager = fresh();
            Outcome outcome = manager.update(1, "", null, null, null);
            assertThat(outcome.entry() == null && "A title is required.".equals(outcome.message()), "update accepted a blank title");
        });

        System.out.println(failures == 0 ? "All acceptance tests passed." : failures + " test(s) failed.");
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating validation, testing, and error recovery. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using record display or object identity as a substitute for a stable application identifier.
- Persisting data before validating it or overwriting a valid file after a failed update.
- Testing individual methods only and missing broken integration between menu, model, validation, and storage.
### Activities
1. Write a record schema and identify required, optional, and unique fields before implementation.
2. Test create, read, update, and delete operations against both in-memory and persisted data.
3. Simulate malformed or unavailable storage and verify existing valid data is not silently lost.
4. Demonstrate the complete manager from startup through validation, persistence, restart, and retrieval.
### Accessibility Practice
Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer.

### Skills Checklist
- [ ] I can explain the key concept in Java terms.
- [ ] I can trace and predict the worked example.
- [ ] I can compile and run the example from the terminal.
- [ ] I can identify and correct a Java-specific mistake.
- [ ] I can test a boundary case and navigate the workflow accessibly.

## Lesson 11.5: Integration, Documentation, and Demonstration

### Reading References
- [Java SE 25 documentation](https://docs.oracle.com/en/java/).
- [Java Language Specification, Java SE 25](https://docs.oracle.com/javase/specs/jls/se25/html/index.html).


### Learning Objectives
- Explain the purpose and vocabulary of integration, documentation, and demonstration.
- Apply the relevant Java syntax and APIs in a small, complete program.
- Compile, run, inspect, and adapt the example using keyboard-accessible tools.

### Concept Explanation
This lesson develops integration, documentation, and demonstration through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Treat the project as a set of observable requirements and milestones. Keep domain logic separate from command parsing and persistence, validate before mutation, report errors in plain language, and test normal, boundary, and failure paths.

Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts.

### Worked Example
```java
public class Lesson_11_5 {
    public static void main(String[] args) {
        java.util.List<String> milestones = java.util.List.of("model", "implement", "test", "document", "demonstrate");
        for (String milestone : milestones) System.out.println("Completed: " + milestone);
=======
### Expected Behavior or Output

The program prints:
```text
PASS 1. an empty title is rejected
PASS 2. a new record gets an unused id
PASS 3. update changes updatedAt but not createdAt
PASS 4. delete removes only that record
PASS 5. complete marks done and updates the record
PASS 6. a blank title cannot be saved by update
All acceptance tests passed.
```

### Common Mistakes
1. Sharing one manager between tests, so one test's deletions change the next test.
2. Checking only that no exception occurred, and not checking the result.
3. Writing the expected message differently from the program, so a correct program fails the test.

### Activities
1. Break `Manager.update` so it also changes `createdAt` (make the field non-final) and watch test 3 fail. Restore it.
2. Add a test that searching ignores case.
3. Add a test that deleting an unknown id returns a message.
4. Explain why test 2 deletes record 2 before adding the new one.

### Accessibility Practice

The test names begin with the acceptance-test number, so PASS and FAIL lines can be matched to the specification. Read only the first word of each line to hear the overall result quickly.

### Skills Checklist
- [ ] I can run the shared acceptance tests.
- [ ] I can test validation failures.
- [ ] I can test timestamps with a fake clock.
- [ ] I can read PASS and FAIL lines.
- [ ] I use a fresh manager for every test.

---

## Lesson 11.5: Capstone: Documentation and Presentation

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- [Unit P, Lesson P.6](../FOUNDATIONS/unit-p-computing-foundations.md): files, data formats, and the shared accessible workflow
- Matching Python lesson: Lesson 11.5: Final Submission

### Learning Objectives
- Write a plain-text project summary.
- Report a count of records by category.
- Complete a manual accessibility check.

### Concept Explanation

Documentation tells a future reader what the program does and how to run it. Write it as plain text or Markdown with short headings, numbered steps, and complete sentences. Include: the purpose of the program, the compile and run commands, the shared record fields, the commands a user can give, the accessibility checks you carried out, and what you would improve next.

The example generates a summary from the shared sample data. It counts records by category and prints the categories in alphabetical order (a `TreeMap` keeps its keys sorted) so the output is stable. It then prints the manual accessibility checklist. The unchecked boxes `[ ]` are for *you* to complete by hand with your own access technology; the program cannot verify them.

Acceptance test 6 is a manual check: every message and control can be used without color or a mouse. Test it with the keyboard only, and with the screen reader or braille display you actually use. Record what you tested and its version; do not claim compatibility with software you did not test.

### Worked Example

```java
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Lesson_11_5 {
    record Entry(int id, String title, String category) {}

    public static void main(String[] args) {
        List<Entry> sample = List.of(
            new Entry(1, "Notebook", "supplies"),
            new Entry(2, "Pencil", "supplies"),
            new Entry(3, "Study plan", "planning"));

        Map<String, Integer> counts = new TreeMap<>();
        for (Entry entry : sample) {
            counts.merge(entry.category(), 1, Integer::sum);
        }

        System.out.println("Personal Data Manager - Summary");
        System.out.println("Records: " + sample.size());
        System.out.println("Categories:");
        for (Map.Entry<String, Integer> category : counts.entrySet()) {
            System.out.println("- " + category.getKey() + ": " + category.getValue());
        }

        System.out.println();
        System.out.println("Manual accessibility checklist (complete this by hand):");
        String[] checks = {
            "[ ] Every command can be used with the keyboard only.",
            "[ ] Every message is a complete sentence that says what to do next.",
            "[ ] No meaning depends on color, position, or symbols alone.",
            "[ ] The output was read with my own screen reader or braille display.",
            "[ ] I recorded the operating system, program, and version I tested."
        };
        for (String check : checks) {
            System.out.println(check);
        }
>>>>>>> 2067a20 (curriculum clearning and updates)
    }
}
```

<<<<<<< HEAD
**Expected behavior:** The program compiles on JDK 25 and prints a deterministic result illustrating integration, documentation, and demonstration. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect.

### Common Mistakes
- Using record display or object identity as a substitute for a stable application identifier.
- Persisting data before validating it or overwriting a valid file after a failed update.
- Testing individual methods only and missing broken integration between menu, model, validation, and storage.
### Activities
1. Write a record schema and identify required, optional, and unique fields before implementation.
2. Test create, read, update, and delete operations against both in-memory and persisted data.
3. Simulate malformed or unavailable storage and verify existing valid data is not silently lost.
4. Demonstrate the complete manager from startup through validation, persistence, restart, and retrieval.
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
Personal Data Manager - Summary
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
```

### Common Mistakes
1. Writing documentation that only the author can follow.
2. Claiming that a program is accessible without recording what was tested and how.
3. Letting the documentation drift from the program after later changes.

### Activities
1. Write the project summary for your own capstone using the headings above.
2. Run the keyboard-only check and record each problem you find.
3. Ask a classmate to follow your run instructions from a fresh folder and note where they get stuck.
4. Write three improvements for the next version, ordered by user benefit.

### Accessibility Practice

This is the final accessibility lesson. Read your own documentation aloud from start to finish. Anything you have to look at the screen to understand needs rewriting.

### Skills Checklist
- [ ] I can write a plain-text project summary.
- [ ] I can report counts by category.
- [ ] I can run a manual accessibility check.
- [ ] I record what I tested.
- [ ] I do not claim untested compatibility.

---

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)
