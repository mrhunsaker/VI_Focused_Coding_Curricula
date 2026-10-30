# Unit 5: Strings and String Processing

## Overview

**JDK baseline:** Examples target standard Java SE 25 using JDK 25 LTS. They do not require preview features or vendor-specific APIs. Use the latest security update in the JDK 25 line.


Java's `String` class is rich with methods for text manipulation.

---

## Lesson 5.1: Working with Strings

### String Basics

```java
String name = "Alice Smith";

// Length
System.out.println(name.length());           // 11

// Accessing characters
System.out.println(name.charAt(0));          // 'A'
System.out.println(name.charAt(name.length() - 1));  // 'h'

// Substrings
System.out.println(name.substring(6));       // "Smith"
System.out.println(name.substring(0, 5));    // "Alice"

// Case conversion
System.out.println(name.toUpperCase());      // "ALICE SMITH"
System.out.println(name.toLowerCase());      // "alice smith"

// Trimming whitespace
String padded = "  hello  ";
System.out.println(padded.trim());           // "hello"
System.out.println(padded.strip());          // "hello" (better Unicode support)

// Searching
System.out.println(name.indexOf("Smith"));   // 6
System.out.println(name.contains("Alice"));  // true
System.out.println(name.startsWith("Ali"));  // true
System.out.println(name.endsWith("ith"));    // true

// Replacing
String result = name.replace("Alice", "Bob");   // "Bob Smith"
String clean = "a,b,c".replace(",", " ");       // "a b c"

// Splitting
String sentence = "the quick brown fox";
String[] words = sentence.split(" ");
for (String word : words) {
    System.out.println(word);
}

// Checking equality
String s1 = "hello";
String s2 = "hello";
System.out.println(s1.equals(s2));           // true (correct)
System.out.println(s1.equalsIgnoreCase("HELLO")); // true

// Converting other types to String
String fromInt = String.valueOf(42);
String fromDouble = String.valueOf(3.14);
String formatted = String.format("Name: %-10s Age: %3d", "Alice", 15);
```

### `StringBuilder` for Efficient Concatenation

Use `StringBuilder` when building strings in a loop (more efficient than `+`):

```java
StringBuilder sb = new StringBuilder();
for (int i = 1; i <= 5; i++) {
    sb.append("Item ").append(i).append("\n");
}
System.out.println(sb.toString());
```

### Examples

**Example 5.1.1: String Analysis**
```java
import java.util.Scanner;

public class StringAnalysis {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String sentence = scanner.nextLine();

        String[] words = sentence.trim().split("\\s+");

        System.out.println("Original: " + sentence);
        System.out.println("Character count: " + sentence.length());
        System.out.println("Word count: " + words.length);
        System.out.println("Uppercase: " + sentence.toUpperCase());
        System.out.println("Lowercase: " + sentence.toLowerCase());

        scanner.close();
    }
}
```

**Example 5.1.2: Word Frequency Counter**
```java
import java.util.HashMap;
import java.util.Map;

public class WordFrequency {
    public static void main(String[] args) {
        String text = "the quick brown fox jumps over the lazy dog the quick brown fox";
        String[] words = text.toLowerCase().split("\\s+");

        Map<String, Integer> frequency = new HashMap<>();
        for (String word : words) {
            frequency.put(word, frequency.getOrDefault(word, 0) + 1);
        }

        System.out.println("Word Frequencies:");
        for (Map.Entry<String, Integer> entry : frequency.entrySet()) {
            System.out.println("'" + entry.getKey() + "': " + entry.getValue());
        }
    }
}
```

### Skills Checklist
- [ ] I can use common `String` methods in Java.
- [ ] I can compare strings using `.equals()`.
- [ ] I can split a string into an array of words.
- [ ] I can use `StringBuilder` for efficient string building.

---

# Unit 6: Methods (Functions)

## Overview

Java organizes reusable code into **methods** (the Java equivalent of Python functions).

---

## Lesson 6.1: Defining and Calling Methods

### Method Syntax

```java
accessModifier returnType methodName(paramType paramName, ...) {
    // method body
    return value;  // if returnType is not void
}
```

### Examples

**Example 6.1.1: Simple Greeting Method**
```java
public class GreetingDemo {

    public static void greetUser() {
        System.out.println("Hello, Java programmer!");
    }

    public static void greetByName(String name) {
        System.out.println("Hello, " + name + "!");
    }

    public static void main(String[] args) {
        greetUser();
        greetByName("Alice");
        greetByName("Bob");
    }
}
```

**Example 6.1.2: Return Values**
```java
public class Calculator {

    public static int addNumbers(int a, int b) {
        return a + b;
    }

    public static double calculateCircleArea(double radius) {
        return Math.PI * radius * radius;
    }

    public static String getGrade(int score) {
        if (score >= 90) return "A";
        else if (score >= 80) return "B";
        else if (score >= 70) return "C";
        else if (score >= 60) return "D";
        else return "F";
    }

    public static void main(String[] args) {
        int sum = addNumbers(5, 3);
        System.out.println("Sum: " + sum);

        double area = calculateCircleArea(5.0);
        System.out.printf("Circle area: %.2f%n", area);

        System.out.println("Grade for 85: " + getGrade(85));
    }
}
```

### Method Overloading

Java allows multiple methods with the same name but different parameters:

```java
public static int add(int a, int b) { return a + b; }
public static double add(double a, double b) { return a + b; }
public static int add(int a, int b, int c) { return a + b + c; }
```

### Passing Arrays to Methods

```java
public static int sum(int[] numbers) {
    int total = 0;
    for (int num : numbers) {
        total += num;
    }
    return total;
}

// Calling:
int[] data = {1, 2, 3, 4, 5};
System.out.println("Sum: " + sum(data));
```

### Varargs (Variable Arguments)

```java
public static int sumAll(int... numbers) {
    int total = 0;
    for (int num : numbers) {
        total += num;
    }
    return total;
}

// Calling:
System.out.println(sumAll(1, 2, 3));          // 6
System.out.println(sumAll(10, 20, 30, 40));    // 100
```

### Skills Checklist
- [ ] I can define a method with a return type and parameters.
- [ ] I can call a method and use its return value.
- [ ] I understand the difference between `void` and non-`void` methods.
- [ ] I can overload methods with different parameter lists.
- [ ] I can pass arrays to methods.

---

# Unit 7: Classes and Object-Oriented Programming

## Overview

Java is fundamentally object-oriented. This unit covers defining and using classes.

---

## Lesson 7.1: Why Learn About Classes?

*(See Python Unit 7.1 for conceptual content — OOP concepts are language-agnostic.)*

Java is a **class-based** language — every Java program is a class. Understanding OOP is essential for Java.

---

## Lesson 7.2: Creating and Using a Class

### Class Syntax

```java
public class Dog {
    // Instance variables (fields)
    private String name;
    private int age;

    // Constructor
    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Methods
    public void sit() {
        System.out.println(name + " is now sitting.");
    }

    public void rollOver() {
        System.out.println(name + " rolled over!");
    }

    public void getOlder(int years) {
        this.age += years;
        System.out.println(name + " is now " + age + " years old.");
    }

    // Getters and Setters
    public String getName() { return name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }

    @Override
    public String toString() {
        return "Dog{name='" + name + "', age=" + age + "}";
    }
}
```

### Using the Class

```java
public class DogDemo {
    public static void main(String[] args) {
        Dog myDog = new Dog("Buddy", 3);
        Dog yourDog = new Dog("Lucy", 1);

        System.out.println("My dog's name is " + myDog.getName() + ".");
        myDog.sit();
        myDog.rollOver();
        myDog.getOlder(2);

        System.out.println(myDog);
    }
}
```

### Access Modifiers

| Modifier | Access Level |
|----------|-------------|
| `public` | Accessible from anywhere |
| `private` | Only within the same class |
| `protected` | Within the class and subclasses |
| (default) | Within the same package |

**Best practice:** Make instance variables `private` and provide `public` getter/setter methods — this is **encapsulation**.

### Skills Checklist
- [ ] I can define a Java class with fields, a constructor, and methods.
- [ ] I can create instances of a class using `new`.
- [ ] I understand the purpose of `this` in Java.
- [ ] I can write getter and setter methods.
- [ ] I understand access modifiers (`public`, `private`).

---

## Lesson 7.3: Inheritance

```java
public class Vehicle {
    protected String make;
    protected String model;
    protected int year;

    public Vehicle(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    public String getDescriptiveName() {
        return year + " " + make + " " + model;
    }

    public void readOdometer() {
        System.out.println("No odometer reading available.");
    }
}

public class Car extends Vehicle {
    private int odometer;

    public Car(String make, String model, int year) {
        super(make, model, year);   // Call parent constructor
        this.odometer = 0;
    }

    @Override
    public void readOdometer() {
        System.out.println("This car has " + odometer + " miles on it.");
    }

    public void updateOdometer(int miles) {
        if (miles >= odometer) {
            odometer = miles;
        } else {
            System.out.println("Error: Cannot roll back odometer.");
        }
    }
}

public class ElectricCar extends Car {
    private int batterySize;

    public ElectricCar(String make, String model, int year) {
        super(make, model, year);
        this.batterySize = 75;
    }

    public void describeBattery() {
        System.out.println("This car has a " + batterySize + "-kWh battery.");
    }
}
```

### Abstract Classes and Interfaces

```java
// Abstract class — cannot be instantiated
public abstract class Shape {
    public abstract double area();      // Abstract method — no body
    public abstract double perimeter(); // Must be implemented by subclasses

    public void printInfo() {           // Concrete method — has body
        System.out.printf("Area: %.2f, Perimeter: %.2f%n", area(), perimeter());
    }
}

public class Circle extends Shape {
    private double radius;

    public Circle(double radius) { this.radius = radius; }

    @Override
    public double area() { return Math.PI * radius * radius; }

    @Override
    public double perimeter() { return 2 * Math.PI * radius; }
}

// Interface — defines a contract
public interface Drawable {
    void draw();
    default void resize(double factor) {
        System.out.println("Resizing by factor " + factor);
    }
}
```

### Skills Checklist
- [ ] I can create a subclass that extends a parent class.
- [ ] I can use `super()` to call the parent constructor.
- [ ] I can override methods using `@Override`.
- [ ] I understand abstract classes and interfaces.

---

# Unit 8: Files and Exception Handling

## Overview

This unit covers reading and writing files in Java and handling exceptions.

---

## Lesson 8.1: Reading from Files

```java
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import java.util.Scanner

public class FileReaderDemo {
    public static void main(String[] args) {
        // Reading entire file using Scanner
        try (Scanner fileScanner = new Scanner(new File("my_notes.txt"))) {
            while (fileScanner.hasNextLine()) {
                String line = fileScanner.nextLine();
                System.out.println(line);
            }
        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found - " + e.getMessage());
        }

        // Reading with BufferedReader (more efficient for large files)
        try (BufferedReader reader = new BufferedReader(new FileReader("my_notes.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }

        // Reading all lines into a List
        try {
            List<String> lines = java.nio.file.Files.readAllLines(
                java.nio.file.Paths.get("my_notes.txt")
            );
            for (String line : lines) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

### Simpler approach using `java.nio.file`

```java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.io.IOException;
import java.util.List;

public class ModernFileReader {
    public static void main(String[] args) {
        Path filePath = Paths.get("my_notes.txt");

        try {
            // Read all lines
            List<String> lines = Files.readAllLines(filePath);
            for (String line : lines) {
                System.out.println(line);
            }

            // Read entire file as one string
            String content = Files.readString(filePath);
            System.out.println(content);

        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }
}
```

---

## Lesson 8.2: Writing to Files

```java
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class FileWriterDemo {
    public static void main(String[] args) {
        // Writing with PrintWriter (creates new or overwrites)
        try (PrintWriter writer = new PrintWriter("output.txt")) {
            writer.println("Hello, Java file I/O!");
            writer.println("Writing is easy.");
            writer.printf("Value: %d%n", 42);
        } catch (FileNotFoundException e) {
            System.out.println("Error: Could not create file.");
        }

        // Appending with FileWriter(true = append mode)
        try (PrintWriter appender = new PrintWriter(new FileWriter("output.txt", true))) {
            appender.println("This line is appended.");
        } catch (IOException e) {
            System.out.println("Error appending to file.");
        }

        // Modern NIO approach
        try {
            String content = "Hello from NIO!\nSecond line.";
            Files.writeString(Paths.get("modern_output.txt"), content);

            // Append
            Files.writeString(Paths.get("modern_output.txt"),
                "\nAppended line.",
                StandardOpenOption.APPEND);
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

---

## Lesson 8.3: Exception Handling

### `try-catch-finally`

```java
public class ExceptionHandling {
    public static void main(String[] args) {
        // Basic try-catch
        try {
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        }

        // Multiple catch blocks
        try {
            String input = "abc";
            int number = Integer.parseInt(input);
        } catch (NumberFormatException e) {
            System.out.println("Invalid number format: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Unexpected error: " + e.getMessage());
        }

        // try-catch-finally
        PrintWriter writer = null;
        try {
            writer = new PrintWriter("data.txt");
            writer.println("Some data");
        } catch (FileNotFoundException e) {
            System.out.println("Could not create file.");
        } finally {
            if (writer != null) {
                writer.close();
                System.out.println("File closed.");
            }
        }

        // try-with-resources (automatically closes resources)
        try (PrintWriter pw = new PrintWriter("data2.txt")) {
            pw.println("Better approach!");
        } catch (FileNotFoundException e) {
            System.out.println("Could not create file.");
        }
    }
}
```

### Common Java Exceptions

| Exception | When it occurs |
|-----------|---------------|
| `ArithmeticException` | Division by zero |
| `NumberFormatException` | Invalid number conversion (e.g., `Integer.parseInt("abc")`) |
| `ArrayIndexOutOfBoundsException` | Array index out of range |
| `NullPointerException` | Calling method on null reference |
| `FileNotFoundException` | File doesn't exist |
| `IOException` | General I/O error |
| `ClassCastException` | Invalid type cast |

### Custom Exceptions

```java
public class InsufficientFundsException extends Exception {
    private double amount;

    public InsufficientFundsException(double amount) {
        super("Insufficient funds: need " + amount + " more.");
        this.amount = amount;
    }

    public double getAmount() { return amount; }
}

// Usage:
public void withdraw(double amount) throws InsufficientFundsException {
    if (amount > balance) {
        throw new InsufficientFundsException(amount - balance);
    }
    balance -= amount;
}
```

### Skills Checklist
- [ ] I can read from a file using `Scanner` or `BufferedReader`.
- [ ] I can write to a file using `PrintWriter`.
- [ ] I can use `try-catch-finally` to handle exceptions.
- [ ] I can use try-with-resources for automatic resource cleanup.
- [ ] I know common Java exception types.
