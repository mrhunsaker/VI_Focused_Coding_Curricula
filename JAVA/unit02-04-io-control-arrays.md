# Unit 2: Writing Simple Programs and Input/Output

## Overview

This unit covers getting user input, type conversions, and working with the Math library in Java.

---

## Lesson 2.1: The Software Development Process

*(See Python Unit 2.1 — the same design principles apply: analyze, design, implement, test.)*

---

## Lesson 2.2: Getting User Input with Scanner

### The `Scanner` Class

Java uses the `Scanner` class to read input from the user:

```java
import java.util.Scanner;

public class UserInput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("What is your name? ");
        String name = scanner.nextLine();

        System.out.print("How old are you? ");
        int age = scanner.nextInt();

        System.out.println("Hello, " + name + "!");
        System.out.println("Next year you will be " + (age + 1) + " years old.");

        scanner.close();
    }
}
```

### Scanner Methods

| Method | Reads | Example |
|--------|-------|---------|
| `nextLine()` | Entire line as String | `String name = scanner.nextLine();` |
| `next()` | Single word (up to whitespace) | `String word = scanner.next();` |
| `nextInt()` | Integer | `int n = scanner.nextInt();` |
| `nextDouble()` | Double | `double d = scanner.nextDouble();` |
| `nextBoolean()` | Boolean | `boolean b = scanner.nextBoolean();` |

### Common Pitfall: `nextInt()` + `nextLine()`

After calling `nextInt()`, there is a leftover newline character. Call `scanner.nextLine()` to consume it before reading another string:

```java
int age = scanner.nextInt();
scanner.nextLine();            // Consume leftover newline
String name = scanner.nextLine();  // Now reads correctly
```

### Examples

**Example 2.2.1: Temperature Converter**
```java
import java.util.Scanner;

public class TempConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter temperature in Fahrenheit: ");
        double fahrenheit = scanner.nextDouble();

        double celsius = (fahrenheit - 32) * 5.0 / 9.0;

        System.out.printf("%.1f°F is %.1f°C%n", fahrenheit, celsius);
        scanner.close();
    }
}
```

**Example 2.2.2: Circle Calculator**
```java
import java.util.Scanner;

public class CircleCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the radius: ");
        double radius = scanner.nextDouble();

        double area = Math.PI * radius * radius;
        double circumference = 2 * Math.PI * radius;

        System.out.printf("Area: %.2f%n", area);
        System.out.printf("Circumference: %.2f%n", circumference);
        scanner.close();
    }
}
```

### Skills Checklist
- [ ] I can import and create a `Scanner` object.
- [ ] I can read different types of input from the user.
- [ ] I can handle the `nextInt()`/`nextLine()` newline issue.

---

## Lesson 2.3: The Math Class

```java
// Math class provides static methods — no import needed
double squareRoot = Math.sqrt(25.0);     // 5.0
double power = Math.pow(2, 10);           // 1024.0
double absolute = Math.abs(-7.5);         // 7.5
int ceiling = (int) Math.ceil(4.2);       // 5
int floor = (int) Math.floor(4.8);        // 4
double rounded = Math.round(4.6);         // 5
double maxVal = Math.max(10, 20);         // 20
double minVal = Math.min(10, 20);         // 10
double piValue = Math.PI;                 // 3.14159...
double eValue = Math.E;                   // 2.71828...
double sinVal = Math.sin(Math.PI / 2);   // 1.0
double logVal = Math.log(Math.E);        // 1.0  (natural log)
double log10 = Math.log10(100);          // 2.0
```

### Skills Checklist
- [ ] I can use common `Math` class methods.
- [ ] I can use `Math.PI` for circle calculations.

---

# Unit 3: Control Flow — Decisions and Loops

## Overview

This unit introduces conditional statements and loops in Java.

**Objectives:**
- Use `if`, `else if`, and `else` for decision-making.
- Use `for`, `while`, and `do-while` loops.
- Use `break` and `continue`.

---

## Lesson 3.1: Boolean Expressions and `if` Statements

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `age == 18` |
| `!=` | Not equal to | `score != 0` |
| `<` | Less than | `temp < 0` |
| `>` | Greater than | `score > 90` |
| `<=` | Less than or equal | `age <= 17` |
| `>=` | Greater than or equal | `score >= 60` |

### Logical Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `&&` | AND (both true) | `age >= 18 && hasId == true` |
| `\|\|` | OR (at least one true) | `day.equals("Sat") \|\| day.equals("Sun")` |
| `!` | NOT (negates) | `!isRaining` |

### `if-else if-else`

```java
int score = 85;

if (score >= 90) {
    System.out.println("Grade: A");
} else if (score >= 80) {
    System.out.println("Grade: B");
} else if (score >= 70) {
    System.out.println("Grade: C");
} else {
    System.out.println("Grade: F");
}
```

### String Comparison

**Important:** Never use `==` to compare Strings. Use `.equals()`:

```java
String color = "blue";
if (color.equals("blue")) {
    System.out.println("It's blue!");
}
if (color.equalsIgnoreCase("BLUE")) {
    System.out.println("Case-insensitive match!");
}
```

### `switch` Statement

```java
int day = 3;
switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    case 3:
        System.out.println("Wednesday");
        break;
    default:
        System.out.println("Other day");
}
```

### Examples

**Example 3.1.1: Age Check**
```java
import java.util.Scanner;

public class AgeCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        if (age >= 18) {
            System.out.println("You are an adult.");
        } else {
            System.out.println("You are a minor.");
        }
        scanner.close();
    }
}
```

**Example 3.1.2: Grade Calculator**
```java
import java.util.Scanner;

public class GradeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your score (0-100): ");
        int score = scanner.nextInt();

        String grade;
        if (score >= 90) {
            grade = "A";
        } else if (score >= 80) {
            grade = "B";
        } else if (score >= 70) {
            grade = "C";
        } else if (score >= 60) {
            grade = "D";
        } else {
            grade = "F";
        }

        System.out.println("Your grade: " + grade);
        scanner.close();
    }
}
```

### Skills Checklist
- [ ] I can write `if`, `else if`, and `else` statements in Java.
- [ ] I can use `&&`, `||`, and `!` to combine conditions.
- [ ] I use `.equals()` (not `==`) to compare Strings.
- [ ] I can write a `switch` statement.

---

## Lesson 3.2: `for` Loops

```java
// Basic for loop
for (int i = 0; i < 5; i++) {
    System.out.println("i = " + i);
}

// Counting down
for (int i = 10; i > 0; i--) {
    System.out.println(i);
}
System.out.println("Blast off!");

// Stepping by 2
for (int i = 0; i <= 10; i += 2) {
    System.out.println(i);
}
```

### Enhanced `for` Loop (for-each)

```java
String[] fruits = {"apple", "banana", "cherry"};
for (String fruit : fruits) {
    System.out.println("I like " + fruit + ".");
}

int[] numbers = {1, 2, 3, 4, 5};
int sum = 0;
for (int num : numbers) {
    sum += num;
}
System.out.println("Sum: " + sum);
```

### Examples

**Example 3.2.1: Multiplication Table**
```java
public class MultiplicationTable {
    public static void main(String[] args) {
        int n = 5;
        System.out.println("Multiplication table for " + n + ":");
        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " x " + i + " = " + (n * i));
        }
    }
}
```

### Skills Checklist
- [ ] I can write a basic `for` loop with initialization, condition, and update.
- [ ] I can use an enhanced `for` loop to iterate over an array.

---

## Lesson 3.3: `while` and `do-while` Loops

### `while` Loop

```java
int count = 1;
while (count <= 5) {
    System.out.println("Count: " + count);
    count++;
}
```

### `do-while` Loop

The `do-while` loop runs at least once before checking the condition:

```java
Scanner scanner = new Scanner(System.in);
String input;
do {
    System.out.print("Enter a positive number: ");
    int number = scanner.nextInt();
    System.out.println("You entered: " + number);
    System.out.print("Continue? (yes/no): ");
    input = scanner.next();
} while (input.equals("yes"));
```

### `break` and `continue`

```java
// break — exit the loop entirely
for (int i = 0; i < 10; i++) {
    if (i == 5) break;
    System.out.println(i);   // Prints 0, 1, 2, 3, 4
}

// continue — skip the current iteration
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) continue;
    System.out.println(i);   // Prints 1, 3, 5, 7, 9
}
```

### Skills Checklist
- [ ] I can write a `while` loop.
- [ ] I can write a `do-while` loop.
- [ ] I can use `break` to exit a loop early.
- [ ] I can use `continue` to skip an iteration.

---

# Unit 4: Data Structures — Arrays and ArrayLists

## Overview

This unit introduces Java's built-in array type and the flexible `ArrayList` class.

---

## Lesson 4.1: Arrays

### Declaring and Initializing Arrays

```java
// Declare and allocate
int[] numbers = new int[5];            // [0, 0, 0, 0, 0]

// Declare and initialize with values
String[] colors = {"red", "blue", "green", "yellow"};

// Access elements (zero-based index)
System.out.println(colors[0]);         // "red"
System.out.println(colors[colors.length - 1]);  // "yellow"

// Modify an element
colors[1] = "purple";

// Loop through array
for (int i = 0; i < numbers.length; i++) {
    numbers[i] = i * 2;
    System.out.println("numbers[" + i + "] = " + numbers[i]);
}
```

### Common Array Operations

```java
import java.util.Arrays;

int[] data = {5, 2, 9, 1, 7, 3};

// Sort
Arrays.sort(data);
System.out.println(Arrays.toString(data));   // [1, 2, 3, 5, 7, 9]

// Search (array must be sorted first)
int index = Arrays.binarySearch(data, 7);
System.out.println("Found 7 at index: " + index);

// Copy
int[] copy = Arrays.copyOf(data, data.length);
int[] partial = Arrays.copyOfRange(data, 1, 4);  // [2, 3, 5]
```

### Skills Checklist
- [ ] I can declare and initialize an array in Java.
- [ ] I can access and modify array elements by index.
- [ ] I can iterate over an array using a `for` loop.
- [ ] I can use `Arrays.sort()` and `Arrays.toString()`.

---

## Lesson 4.2: ArrayLists

`ArrayList` is a resizable array that can grow or shrink dynamically.

```java
import java.util.ArrayList;

ArrayList<String> shoppingList = new ArrayList<>();

// Add items
shoppingList.add("milk");
shoppingList.add("bread");
shoppingList.add("eggs");
shoppingList.add(1, "butter");   // Insert at index 1

// Access items
System.out.println(shoppingList.get(0));          // "milk"
System.out.println(shoppingList.size());           // 4

// Remove items
shoppingList.remove("bread");                     // Remove by value
shoppingList.remove(0);                           // Remove by index

// Check membership
boolean hasMilk = shoppingList.contains("milk");

// Loop through
for (String item : shoppingList) {
    System.out.println("- " + item);
}
```

### ArrayList vs. Array

| Feature | `Array` | `ArrayList` |
|---------|---------|-------------|
| Size | Fixed | Dynamic |
| Type | Primitive or Object | Objects only |
| Syntax | `int[]` | `ArrayList<Integer>` |
| `.length` / `.size()` | `.length` | `.size()` |
| Performance | Slightly faster | More flexible |

### Skills Checklist
- [ ] I can create an `ArrayList` with a generic type.
- [ ] I can add, access, remove, and search items in an `ArrayList`.
- [ ] I can explain when to use an array vs. an `ArrayList`.

---

## Lesson 4.3: Multidimensional Arrays

```java
// 2D array (matrix)
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Access element at row 1, column 2
System.out.println(matrix[1][2]);   // 6

// Loop through 2D array
for (int row = 0; row < matrix.length; row++) {
    for (int col = 0; col < matrix[row].length; col++) {
        System.out.print(matrix[row][col] + " ");
    }
    System.out.println();
}
```

### Skills Checklist
- [ ] I can declare and initialize a 2D array.
- [ ] I can access elements using row and column indices.
- [ ] I can iterate through a 2D array using nested loops.
