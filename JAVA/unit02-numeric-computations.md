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
