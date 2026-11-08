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
