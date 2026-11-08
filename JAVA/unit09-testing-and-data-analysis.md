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
