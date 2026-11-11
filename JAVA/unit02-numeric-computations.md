# Unit 2: Numeric Computations

## Overview

This unit develops numeric computations through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 2.1: The Software Development Process

### Reading References
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
