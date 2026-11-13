# Unit 7: Classes and Object-Oriented Programming

## Overview

This unit develops classes and object-oriented programming through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 7.1: Why Learn About Classes?

### Reading References
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
    }
}
```

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
