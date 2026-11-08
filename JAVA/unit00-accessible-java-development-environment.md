# Unit 0: Accessible Java Development Environment

## Course overview

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
