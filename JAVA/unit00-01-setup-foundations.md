# Unit 0: Setting Up Your Java Development Environment

## Overview

This unit walks through installing Java and configuring VS Code for accessible Java development.

---

## Lesson 0.1: Installing the Java Development Kit (JDK)

### What Is the JDK?

The **JDK (Java Development Kit)** includes everything you need to write, compile, and run Java programs:
- **JDK** — Tools for developers (compiler, debugger).
- **JVM (Java Virtual Machine)** — Runs compiled Java programs.
- **JRE (Java Runtime Environment)** — Libraries and runtime support.

### Installing the JDK

**Recommended:** Download Eclipse Temurin (OpenJDK) from [https://adoptium.net/](https://adoptium.net/).

Choose **JDK 17 LTS** (Long Term Support) for stability.

#### Windows
1. Download the `.msi` installer.
2. **CRUCIAL STEP:** In the installer, ensure "Set JAVA_HOME variable" and "Add to PATH" are checked.
3. Activate "Install" and then "Finish".

#### macOS
1. Download the `.pkg` installer.
2. Follow the standard macOS installation steps.
3. The JDK is automatically added to your PATH.

#### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install openjdk-17-jdk
```

### Verify Installation
Open a terminal and run:
```bash
java --version
javac --version
```
You should hear the version number (e.g., "openjdk 17.0.x").

### Skills Checklist
- [ ] I have installed JDK 17 or later.
- [ ] Running `java --version` in the terminal shows the version number.
- [ ] Running `javac --version` in the terminal shows the compiler version.

---

## Lesson 0.2: Installing VS Code and the Java Extension Pack

1. Install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Open VS Code and press `Ctrl + Shift + X` to open Extensions.
3. Search for **"Extension Pack for Java"** by Microsoft. Install it.
   This installs: Language Support for Java, Debugger for Java, Java Test Runner, and Maven support.

### Configure Screen Reader Mode
- Press `Ctrl + Shift + P` → type "Toggle Screen Reader Optimized" → press Enter.

### VS Code Keyboard Shortcuts for Java

| Action | Shortcut |
|--------|----------|
| Run Java file | `Ctrl + F5` |
| Debug Java file | `F5` |
| Command Palette | `Ctrl + Shift + P` |
| Problems View | `Ctrl + Shift + M` |
| Next Error | `F8` |
| Go to Definition | `F12` |
| Format Code | `Shift + Alt + F` |

### Skills Checklist
- [ ] VS Code is installed with the Extension Pack for Java.
- [ ] I can toggle Screen Reader Optimized Mode.
- [ ] I can navigate errors using `F8`.

---

## Lesson 0.3: Your First Java Project

### Creating a Project
1. Press `Ctrl + Shift + P` → "Java: Create Java Project".
2. Select "No build tools".
3. Choose a folder and name the project `HelloWorld`.
4. VS Code will create a `src` folder with a sample file.

### Writing Hello World

Create a file `HelloWorld.java` in the `src` folder:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### Running the Program
- Press `Ctrl + F5` to run without debugging.
- Or open the terminal (`Ctrl + \``) and type:
```bash
javac HelloWorld.java
java HelloWorld
```

### Key Differences from Python

| Python | Java |
|--------|------|
| No required structure | Every program needs a `class` |
| No semicolons | Statements end with `;` |
| Indentation defines blocks | Curly braces `{}` define blocks |
| `print()` | `System.out.println()` |
| Interpreted | Compiled (`.java` → `.class` → run) |
| Dynamic typing | Static typing (declare variable types) |

### Skills Checklist
- [ ] I can create a new Java project in VS Code.
- [ ] I can write and run a Hello World program.
- [ ] I understand the basic structure of a Java program.

---

# Unit 1: Foundations of Computing and Getting Started with Java

## Overview

This unit introduces computer science concepts and the fundamentals of Java programming.

**Objectives:**
- Understand hardware vs. software.
- Write and run basic Java programs.
- Use variables and data types.

---

## Lesson 1.1: Welcome to Computer Science

*(See Python Unit 1.1 for conceptual content — hardware, software, algorithms, and problem-solving are language-agnostic.)*

### Java-Specific Notes

Java was created by James Gosling at Sun Microsystems in 1995. Key principles:
- **"Write Once, Run Anywhere"** — Java programs compile to bytecode that runs on any JVM.
- **Strongly typed** — Every variable must have a declared type.
- **Object-Oriented** — Everything lives inside classes.

---

## Lesson 1.2: Your First Java Program

### Anatomy of a Java Program

```java
// This is a comment
public class HelloWorld {                    // Class declaration
    public static void main(String[] args) { // Main method — program entry point
        System.out.println("Hello, World!"); // Print a line to the console
    }
}
```

**Key rules:**
- The file name **must match** the class name: `HelloWorld.java`.
- Every Java program starts execution from `public static void main(String[] args)`.
- Statements end with a semicolon `;`.
- Blocks of code are surrounded by curly braces `{}`.

### Output Methods

```java
System.out.println("This prints with a newline at the end.");
System.out.print("This prints without a newline.");
System.out.printf("My name is %s and I am %d years old.%n", "Alice", 15);
```

### Examples

**Example 1.2.1: Simple Greeting**
```java
public class SimpleGreeting {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("Welcome to Java programming!");
    }
}
```

**Example 1.2.2: Using printf for Formatted Output**
```java
public class FormattedOutput {
    public static void main(String[] args) {
        System.out.printf("Pi is approximately %.2f%n", 3.14159);
        System.out.printf("%-15s %5d%n", "Apples:", 42);
    }
}
```

### Skills Checklist
- [ ] I can write a basic Java program with a `main` method.
- [ ] I can use `System.out.println()` to display output.
- [ ] I understand that Java files must match their class name.

---

## Lesson 1.3: Variables and Primitive Data Types

### Primitive Data Types

| Type | Description | Size | Example |
|------|-------------|------|---------|
| `int` | Whole numbers | 32-bit | `int age = 25;` |
| `long` | Large whole numbers | 64-bit | `long population = 8000000000L;` |
| `double` | Decimal numbers | 64-bit | `double pi = 3.14159;` |
| `float` | Decimal (less precise) | 32-bit | `float price = 9.99f;` |
| `boolean` | True or False | 1-bit | `boolean isRaining = false;` |
| `char` | Single character | 16-bit | `char grade = 'A';` |

### String (Reference Type)

```java
String name = "Alice";
String message = "Hello, " + name + "!";  // Concatenation
```

### Variable Declaration and Assignment

```java
// Declare and assign in one line
int score = 100;
double price = 4.99;
boolean isActive = true;
String studentName = "Charlie";

// Declare first, assign later
int total;
total = 50 + 25;
```

### Constants

```java
final double PI = 3.14159265358979;
final int MAX_SIZE = 100;
```

### Type Conversion

```java
// Widening (automatic — safe)
int intValue = 42;
double doubleValue = intValue;   // 42 → 42.0

// Narrowing (explicit cast — may lose data)
double d = 9.99;
int i = (int) d;                 // 9.99 → 9

// String to number
int parsed = Integer.parseInt("123");
double parsedD = Double.parseDouble("3.14");

// Number to String
String s = String.valueOf(42);
String s2 = Integer.toString(42);
```

### Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` = `8` |
| `-` | Subtraction | `10 - 4` = `6` |
| `*` | Multiplication | `7 * 6` = `42` |
| `/` | Division | `15 / 4` = `3` (integer division!) |
| `%` | Modulo | `10 % 3` = `1` |
| `++` | Increment | `count++` |
| `--` | Decrement | `count--` |

**Important:** Integer division in Java truncates: `15 / 4` = `3`, not `3.75`.
To get a decimal result, use `double`: `15.0 / 4` = `3.75`.

### Examples

**Example 1.3.1: Variables and Arithmetic**
```java
public class VariablesDemo {
    public static void main(String[] args) {
        int appleCount = 5;
        int orangeCount = 3;
        int totalFruit = appleCount + orangeCount;
        System.out.println("You have " + totalFruit + " fruits in total.");

        double pricePerItem = 2.50;
        int quantity = 4;
        double totalCost = pricePerItem * quantity;
        System.out.println("The total cost is: " + totalCost);

        // Integer division
        int a = 10, b = 3;
        System.out.println("10 / 3 = " + (a / b));       // 3
        System.out.println("10.0 / 3 = " + (10.0 / b));  // 3.3333...
        System.out.println("10 % 3 = " + (a % b));        // 1
    }
}
```

### Activities

**Activity 1.3.1: Personal Information**
```java
public class PersonalInfo {
    public static void main(String[] args) {
        String myName = "Jamie";
        int favoriteNumber = 7;
        double heightInMeters = 1.75;
        boolean likesPizza = true;

        System.out.println("My name is: " + myName);
        System.out.println("Favorite number: " + favoriteNumber);
        System.out.printf("Height: %.2f meters%n", heightInMeters);
        System.out.println("Likes pizza: " + likesPizza);
    }
}
```

**Activity 1.3.2: Simple Math**
```java
public class SimpleMath {
    public static void main(String[] args) {
        int num1 = 15;
        int num2 = 7;

        System.out.println("Sum: " + (num1 + num2));
        System.out.println("Difference: " + (num1 - num2));
        System.out.println("Product: " + (num1 * num2));
        System.out.printf("Quotient: %.2f%n", (double) num1 / num2);
        System.out.println("Remainder: " + (num1 % num2));
    }
}
```

### Skills Checklist
- [ ] I can declare variables with the correct Java types.
- [ ] I can perform basic arithmetic operations in Java.
- [ ] I understand the difference between integer and floating-point division.
- [ ] I can convert between types using casting and parse methods.
- [ ] I can use `final` to declare constants.
