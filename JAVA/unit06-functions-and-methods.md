# Unit 6: Functions and Methods

## Overview

This unit develops functions and methods through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 6.1: Defining Methods

### Reading References
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
    }
}
```

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
    }
}
```

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
