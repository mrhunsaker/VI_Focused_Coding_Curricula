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
