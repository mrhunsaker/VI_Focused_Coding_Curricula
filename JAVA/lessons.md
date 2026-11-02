# Java Curriculum — Complete Lesson Set

**Language baseline:** Java SE 25 LTS, JDK 25. Examples avoid preview features and third-party dependencies unless a lesson explicitly discusses an optional library.

This file is the consolidated, lesson-by-lesson teaching sequence for Java. The existing grouped unit files remain supplementary reference material; this file provides the complete standardized sequence and independently runnable examples.

## Course outcomes

Learners will install and verify a JDK, use an accessible editor and terminal, write and compile Java programs, reason about static types, use control flow and collections, decompose problems into methods and classes, handle files and exceptions, test behavior, and build an accessible command-line personal data manager.

# Unit 0: Accessible Java Development Environment

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
    }
}
```

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
    }
}
```

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
    }
}
```

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
    }
}
```

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

# Unit 1: Foundations of Computing and Java

## Overview

This unit develops foundations of computing and java through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 1.1: Welcome to Computer Science

### Reading References
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
    }
}
```

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

## Lesson 1.2: Your First Java Program

### Reading References
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
    }
}
```

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
    }
}
```

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

# Unit 2: Numeric Computations

## Overview

This unit develops numeric computations through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 2.1: The Software Development Process

### Reading References
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
    }
}
```

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

## Lesson 2.2: Expressions and Assignment

### Reading References
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
    }
}
```

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
    }
}
```

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
    }
}
```

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

## Lesson 2.5: Using the Math Library

### Reading References
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
    }
}
```

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
        boolean inRange = score >= 0 && score <= 100;
        if (inRange && score >= 80) System.out.println("Meets target");
        else System.out.println("Needs review");
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

# Unit 4: Data Structures — Lists and Dictionaries

## Overview

This unit develops data structures — lists and dictionaries through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 4.1: More on Lists

### Reading References
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
    }
}
```

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
    }
}
```

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
    }
}
```

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
    }
}
```

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
    }
}
```

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

# Unit 5: User Input and while Loops

## Overview

This unit develops user input and while loops through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

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

# Unit 6: Functions and Methods

## Overview

This unit develops functions and methods through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 6.1: Defining Methods

### Reading References
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
    }
}
```

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
    }
}
```

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

## Lesson 6.3: Return Values

### Reading References
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
    }
}
```

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
    }
}
```

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
    }
}
```

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

# Unit 7: Classes and Object-Oriented Programming

## Overview

This unit develops classes and object-oriented programming through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 7.1: Why Learn About Classes?

### Reading References
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
    }
}
```

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
    }
}
```

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
    }
}
```

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
    }
}
```

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
    }
}
```

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

# Unit 8: Files and Exceptions

## Overview

This unit develops files and exceptions through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 8.1: Reading from a File

### Reading References
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
    }
}
```

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

## Lesson 8.2: Writing to a File

### Reading References
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
    }
}
```

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
        }
    }
}
```

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
    }
}
```

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

## Lesson 8.5: Storing Data with JSON

### Reading References
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
    }
}
```

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

# Unit 9: Testing and Data Analysis

## Overview

This unit develops testing and data analysis through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

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
    }
}
```

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
    }
}
```

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
    }
}
```

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
    }
}
```

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
    }
}
```

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

# Unit 10: Project-Based Learning — Text Applications

## Overview

This unit develops project-based learning — text applications through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

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
    }
}
```

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
    }
}
```

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
        inventory.add("key");
        inventory.add("map");
        String event = inventory.remove("key") ? "The door unlocks." : "The door remains locked.";
        System.out.println(event + " Inventory: " + inventory);
    }
}
```

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
    }
}
```

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
    }
}
```

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

# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

This unit develops capstone — accessible personal data manager through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

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
    }
}
```

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
    }
}
```

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
    }
}
```

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
    }
}
```

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
    }
}
```

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

