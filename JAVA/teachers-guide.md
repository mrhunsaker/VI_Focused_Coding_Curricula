# Teacher's Guide: Introduction to Computer Science with Java

## For Students with Visual Impairments --- Complete Instructor Edition


## How to use this teacher's guide

This guide is a companion for instructors, not a script that must be followed word for word. Read the philosophy, learner-context, and technology sections before the first lesson; use the unit notes while planning; and return to the assessment, differentiation, AI, and quick-reference sections throughout the course. Adapt procedures to the learner's actual assistive technology, operating system, course goals, and prior experience. Confirm tool-specific instructions in current official documentation because editor, screen-reader, and runtime behavior changes over time.

Plan for both programming learning and access to the programming environment. Establish what the student can already do independently, what access skills need instruction, what supports are already in place, and how the learner prefers to receive feedback. Never assume a diagnosis predicts a student's preferred tools or level of independence.

---

## JDK 25 LTS baseline and current Java conventions

Use **JDK 25 LTS** for the learner materials. JDK 25 is the current LTS release as of October 30, 2026; install its latest security update. JDK 27 is newer but is not the LTS baseline. Teach and assess against standard Java 25, not preview features or vendor-specific extensions. Keep classic class-based program structure in the early lessons even though newer Java releases offer more concise launch forms; this keeps the progression explicit and transferable.

Model current Java conventions consistently: PascalCase types; camelCase fields, methods, parameters, and local variables; UPPER_SNAKE_CASE constants; explicit imports; generics instead of raw types; interfaces such as List/Map in declarations; braces for all control-flow blocks; and meaningful method boundaries. Use String.equals for content equality, never ==. Prefer try-with-resources for files and scanners that own resources. Use var only for local variables when the initializer makes the type obvious; keep explicit types in beginner code. Use descriptive exception handling and avoid swallowing exceptions. Avoid preview features unless a lesson explicitly identifies them.

## Table of Contents

1. [Philosophy and Why Java](#1-philosophy-and-why-java)
2. [Java-Specific Accessibility Challenges](#2-java-specific-accessibility-challenges)
3. [Classroom Setup and Configuration](#3-classroom-setup-and-configuration)
4. [Spoken Java Conventions](#4-spoken-java-conventions)
5. [Unit 0--1: Setup and Foundations](#5-unit-01-setup-and-foundations)
6. [Unit 2: I/O and the Math Class](#6-unit-2-io-and-the-math-class)
7. [Unit 3: Control Flow](#7-unit-3-control-flow)
8. [Unit 4: Arrays and ArrayLists](#8-unit-4-arrays-and-arraylists)
9. [Unit 5: Strings and String Processing](#9-unit-5-strings-and-string-processing)
10. [Unit 6: Methods](#10-unit-6-methods)
11. [Unit 7: Classes and OOP](#11-unit-7-classes-and-oop)
12. [Unit 8: Files and Exception Handling](#12-unit-8-files-and-exception-handling)
13. [Unit 9: Collections, Analysis, and Testing](#13-unit-9-collections-analysis-and-testing)
14. [Units 10--11: Projects and Capstone](#14-units-1011-projects-and-capstone)
15. [Bridging from Python to Java](#15-bridging-from-python-to-java)
16. [Assessment Strategies](#16-assessment-strategies)
17. [Supporting Diverse Needs](#17-supporting-diverse-needs)
18. [Alternative and Supplementary Resources](#18-alternative-and-supplementary-resources)
19. [Quick Reference Sheets](#19-quick-reference-sheets)
20. [Teaching AI Tools Responsibly](#20-teaching-ai-tools-responsibly)
21. [Comprehensive Instructional Planning and Course Implementation](#21-comprehensive-instructional-planning-and-course-implementation)

---

## 1. Philosophy and Why Java

### The Case for Teaching Java to Blind Students

Java is not the easiest language for beginners, and its verbosity creates overhead that requires specific pedagogical attention. Despite this, Java has genuine advantages for visually impaired learners that are often overlooked:

**Compile-time error detection.** Java's compiler catches type errors, name errors, and structural mistakes before any code runs. A blind student does not need to search through runtime output for subtle type mismatches --- the compiler announces them precisely and immediately with file name, line number, and error description.

**Strong, static typing is auditorily informative.** When IntelliSense in VS Code suggests methods, it includes the return type: "`double getBalance()` --- returns a double." This type information helps a screen reader user understand what a method does without having to navigate to its definition.

**Enforced code structure.** Every Java program requires a class; every executable program requires a `main` method with a specific signature. This structure is more overhead to type but less ambiguity about how programs are organized. For a student who cannot visually scan a file for structure, predictable structural conventions reduce cognitive load.

**Exception specification.** Java's checked exceptions force programmers to declare which exceptions a method can throw. This means a screen reader user reading a method signature gets information about failure modes that Python provides only through documentation.

**Enterprise relevance.** Java remains a dominant language in enterprise software, Android development, and many backend systems. A student who learns Java learns patterns that transfer directly to professional employment.

---

## 2. Java-Specific Accessibility Challenges

### The Verbosity Problem

Java requires significantly more text than Python to accomplish the same task:

```java
// Java: Hello, World
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

```python
# Python: Hello, World
print("Hello, World!")
```

For a sighted student, extra text is a visual annoyance. For a blind student, it is additional audio before they reach the meaningful code. **Mitigation strategies:**

1. **Code templates.** Provide a starter file the student copies for every new program. They modify only the method body for early lessons. This reduces the typing burden and prevents structural errors while the student is learning concepts.

2. **JShell (Java REPL).** Java includes an interactive shell since Java 9: run `jshell` in the terminal. JShell strips away class and method boilerplate. For exploration and experimentation, JShell is far more accessible than creating files:

   ```
   jshell> int x = 5;
   x ==> 5
   jshell> System.out.println(x * 2);
   10
   ```

3. **Progressive disclosure.** In early lessons, treat `public static void main(String[] args) {` as a formula, not something to understand. Students learn to recognize it by ear. Explain each word only when the concept it relates to (access modifiers, static methods, arrays) is being taught.

### Integer Division Surprises

Java's `/` operator performs integer division when both operands are integers:

- `15 / 4` = `3` (not `3.75`)
- `15.0 / 4` = `3.75`
- `(double) 15 / 4` = `3.75`

This is silent --- there is no error or warning. A blind student may not catch a calculation that silently discards its decimal portion. Teach the rule explicitly: **if you want a decimal result, at least one operand must be a `double`.**

### The String Equality Trap

`==` on Strings compares memory addresses, not content. Two strings with identical characters in different memory locations are `==` false but `.equals()` true. This never appears in Python; blind students coming from Python are not conditioned to suspect `==` as a source of String bugs.

**Teaching approach:** Show the broken behavior explicitly. Use `new String("hello") == new String("hello")` which is guaranteed to be `false` even though the strings are identical. Then show `.equals()` which is `true`. Make `.equals()` for Strings a non-negotiable rule from day one.

### Null Pointer Exceptions

`NullPointerException` is the most common Java runtime error. It occurs when you call a method or access a field on a variable that holds `null` (no object reference). Unlike Python's `AttributeError` which gives useful context, Java's NPE message is often terse. Teaching students to recognize and debug NPEs is essential.

---

## 3. Classroom Setup and Configuration

### IDE Configuration

**Visual Studio Code with Extension Pack for Java:**
This is the primary documented setup. The Extension Pack includes Language Support for Java (Red Hat), Debugger for Java, Java Test Runner, Maven for Java, and Project Manager for Java.

**Theia IDE:** [Theia IDE](https://theia-ide.org/#theiaide) is an alternative with the keyboard- and screen-reader-oriented accessibility workflows expected in this course. Check the Open VSX registry for compatible Java language support, debugging, and test extensions. Not every VS Code extension is available or behaves identically, so verify the student's actual workflow.

**Other tools:** BlueJ, DrJava, and Eclipse may be considered only when their accessibility and feature set fit the learner and the lesson. JetBrains IDEs (including IntelliJ IDEA) are intentionally not recommended for this introductory course. They are capable products, but their extensive feature set and complexity add unnecessary overhead for beginning programmers.

**VS Code Java Specific Settings:**

```json
{
  "java.completion.enabled": true,
  "java.format.enabled": true,
  "editor.formatOnSave": true,
  "java.saveActions.organizeImports": true,
  "java.completion.importOrder": ["java", "javax", "com", ""],
  "editor.suggestOnTriggerCharacters": true
}
```

**Key accessibility setting:** Enable "Trigger suggestions" on `.` so that typing `myObject.` causes IntelliSense to announce available methods. This allows audio exploration of an object's API.

### JDK Installation Verification

```bash
java --version      # Runtime version
javac --version     # Compiler version
jshell              # Start REPL (Ctrl+D or /exit to quit)
```

**Windows PowerShell (Windows 11):**

```powershell
java --version      # Runtime version
javac --version     # Compiler version
jshell              # Start REPL (Ctrl+D or /exit to quit)
```

All three must work before proceeding. If `jshell` is not found, the student may have installed only the JRE (runtime), not the full JDK. The JDK must be installed.

---

## 4. Spoken Java Conventions

Extend the Python symbol conventions with Java-specific additions:

| Symbol/Pattern                   | Spoken Form                      |
| -------------------------------- | -------------------------------- |
| `public`                         | "public"                         |
| `private`                        | "private"                        |
| `static`                         | "static"                         |
| `void`                           | "void" (returns nothing)         |
| `new`                            | "new"                            |
| `this.`                          | "this dot"                       |
| `super.`                         | "super dot"                      |
| `@Override`                      | "at-override annotation"         |
| `// comment`                     | "double-slash comment"           |
| `/* ... */`                      | "block comment"                  |
| `/** ... */`                     | "JavaDoc comment"                |
| `String[]`                       | "String array"                   |
| `ArrayList<String>`              | "ArrayList of String"            |
| `HashMap<String, Integer>`       | "HashMap from String to Integer" |
| `throws IOException`             | "throws IOException"             |
| `System.out.println()`           | "sysout" or "system-out-println" |
| `System.out.printf()`            | "system-out-printf"              |
| `Integer.parseInt()`             | "Integer-parse-int"              |
| `(int) x`                        | "cast to int"                    |
| `null`                           | "null"                           |
| `NullPointerException`           | "null pointer exception"         |
| `ArrayIndexOutOfBoundsException` | "array index out of bounds"      |

**Reading a method signature:**

```java
public double calculateArea(double radius) throws IllegalArgumentException
```

_"public double method calculateArea, takes a double called radius, may throw IllegalArgumentException"_

---

## 5. Unit 0--1: Setup and Foundations

### Lesson 0.1: Installing the JDK

#### Instructional Cues

- **Use Adoptium (Eclipse Temurin) rather than Oracle JDK.** The Oracle JDK requires account creation and license agreement navigation. Adoptium is fully open-source and simpler to download.
- **Verify the download before running.** Adoptium provides SHA checksums. Teaching students to verify downloads is a security habit worth establishing.
- **Windows installer tip:** The Adoptium `.msi` installer includes a checkbox for "Set JAVA_HOME variable." Ensure this is checked. Many Java tools (Maven, Gradle, some IDEs) require `JAVA_HOME` to be set.

#### JShell as the First Environment

Before any file-based Java, spend time in JShell:

```
$ jshell
|  Welcome to JShell -- Version 17.0.x
|  For an introduction type: /help intro

jshell> 5 + 3
$1 ==> 8

jshell> "Hello " + "World"
$2 ==> "Hello World"

jshell> int x = 42;
x ==> 42

jshell> System.out.println("Value: " + x);
Value: 42
```

JShell gives immediate auditory feedback --- type an expression, hear the result. This is much more accessible for early exploration than the compile-run-read cycle.

JShell commands to teach:

- `/list` --- show all code entered so far
- `/edit` --- open in editor
- `/vars` --- show all variables
- `/methods` --- show all methods defined
- `/exit` --- quit JShell

#### Thought Experiments

1. _"Python is interpreted --- each line runs immediately. Java compiles to bytecode first, then runs. What does this mean for the kind of errors you encounter, and when? If you have a SyntaxError on line 50, in Python you might not discover it until the program reaches line 50. In Java, when do you discover it?"_

2. _"The Java Virtual Machine (JVM) allows the same Java bytecode to run on Windows, macOS, and Linux. The JVM is different on each platform, but the bytecode is the same. What does this tell you about how Java achieves portability? What alternative approaches could a language designer take?"_

3. _"JShell is a Read-Eval-Print Loop (REPL). Python has one; JavaScript has one; many languages have one. But Java didn't have one until 2016. Why might a language's designers add a REPL 20 years after the language was created? What did programmers do without it?"_

4. _"Java was originally designed for embedded systems (like televisions), then became dominant for web servers, then for Android apps. Each time it succeeded in a new domain, it required extending the language. What does this history suggest about the relationship between a language's design and the problems it eventually solves?"_

---

### Lesson 1.2: Your First Java Program

#### Instructional Cues

**Anatomy reading exercise --- before typing any code:**
Read the Hello World program aloud, symbol by symbol, using the pronunciation table:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

_"public class HelloWorld open-brace newline four-spaces public static void main open-paren String array args close-paren open-brace newline eight-spaces System dot out dot println open-paren quote Hello comma World! close-quote close-paren semicolon newline four-spaces close-brace newline close-brace"_

This exercise establishes pattern recognition for the boilerplate that the student will type hundreds of times. Making it auditorily familiar early reduces cognitive load later.

**Three `System.out` methods:**

```java
System.out.println("With newline at end");     // Most common
System.out.print("No newline at end");          // For prompts
System.out.printf("Pi is %.2f%n", Math.PI);    // Formatted
```

For accessible programs, `printf` is extremely valuable --- it produces consistent, predictable output formatting that reads cleanly with a screen reader.

#### Thought Experiments

1. _"Every Java program requires a `public class` whose name matches the file name. Why does Java enforce this one-to-one correspondence? What would break if you could put multiple public classes in one file?"_

2. _"The `main` method signature is exactly `public static void main(String[] args)`. It cannot be `public void main()` or `static void main(String[] args)`. Why is this signature fixed? What does each word contribute?"_

3. _"Java uses curly braces `{}` to delimit code blocks; Python uses indentation. From an accessibility perspective --- for a blind programmer --- which approach provides better information about structure when read aloud? Consider that braces can be read as 'open block' and 'close block,' while indentation changes require screen reader configuration."_

4. _"`System.out.println()` is long to type but descriptively named. Python's `print()` is short. What naming philosophy does each represent? When does conciseness become ambiguity?"_

---

### Lesson 1.3: Variables and Primitive Data Types

#### Instructional Cues

**Type declaration as specification:**
Frame Java's type declarations positively: _"When you write `int score = 85`, you're telling Java: this variable will always hold a whole number. Java then protects you --- if you accidentally try to put a name or a decimal into it, the compiler tells you immediately."_

**The eight primitive types --- prioritize four:**
In this curriculum, students need: `int`, `double`, `boolean`, `char`. The others (`byte`, `short`, `long`, `float`) exist but are rarely needed in beginner programs. Introduce the four primary types fully before acknowledging the others exist.

**Type casting demonstration:**

```java
// Widening (automatic)
int i = 100;
double d = i;   // 100 -> 100.0, automatic

// Narrowing (explicit, may lose data)
double pi = 3.14159;
int truncated = (int) pi;  // 3.14159 -> 3, data LOST

System.out.println("Truncated: " + truncated);  // 3, not 4!
```

The truncation behavior (not rounding) is consistently surprising. Demonstrate it with `(int) 3.9` producing `3`, and ask: "Is this rounding or truncating? What is the difference? When would truncation cause a bug?"

#### Non-Obvious Accessibility Strategies

- **`System.out.printf()` for consistent numeric output:** `printf("Balance: $%.2f%n", balance)` always produces exactly 2 decimal places. Without formatting, `double` values may produce varying numbers of decimal places (`3.0`, `3.14`, `3.1415926535...`) that read differently each time. Consistent formatting makes output more predictable.

- **`Scanner.hasNext___()` methods:** Before calling `scanner.nextInt()`, check `scanner.hasNextInt()`. If the user typed a non-integer, this returns `false` and prevents the exception, allowing graceful re-prompting. For a blind student who may not immediately catch an exception in terminal output, this is defensive programming with real accessibility value.

#### Thought Experiments

1. _"Java's `int` holds values from about -2.1 billion to +2.1 billion. What happens if you exceed this limit (integer overflow)? The value silently wraps around to the opposite extreme. Name a real-world system where integer overflow has caused a documented failure."_

2. _"Java has `int` (primitive) and `Integer` (object). They hold the same values but behave differently. `int` cannot be null; `Integer` can. `int` cannot be used in a `List<int>` --- you need `List<Integer>`. Why would a language designer make this distinction? What does it cost? What does it protect against?"_

3. _"Java's `char` holds a single Unicode character. `char c = 'A'` stores the letter A. But `char` is also a numeric type --- `(int) 'A'` is `65`. What does this dual nature (character and number) tell you about how computers store text internally?"_

---

## 6. Unit 2: I/O and the Math Class

### Lesson 2.2: Scanner for User Input

#### Instructional Cues

**The Scanner as a wrapper --- explain the layers:**

```
Keyboard
  V produces bytes
System.in (InputStream)
  V raw byte stream
new Scanner(System.in)
  V wraps with text-reading methods
scanner.nextLine(), scanner.nextInt(), etc.
```

This layered model explains why `Scanner` is needed rather than reading from `System.in` directly. It also foreshadows file reading where `new Scanner(new File(...))` replaces `new Scanner(System.in)`.

**`nextInt()` / `nextLine()` pitfall --- mandatory demonstration:**

```java
Scanner scanner = new Scanner(System.in);
System.out.print("Enter your age: ");
int age = scanner.nextInt();          // Reads "25", leaves "\n" in buffer
System.out.print("Enter your name: ");
String name = scanner.nextLine();     // Reads the leftover "\n" --- gets EMPTY string!
System.out.println("Hello " + name + ", age " + age);
// Output: "Hello , age 25" --- name is empty!
```

The fix:

```java
int age = scanner.nextInt();
scanner.nextLine();          // Consume the leftover newline
String name = scanner.nextLine();   // Now reads properly
```

Run the broken version first. The student should hear the incorrect output and understand why before seeing the fix.

#### Thought Experiments

1. _"The `Scanner` reads from a 'stream' of input. A stream is a sequence of data that flows from a source to a destination. `System.in` is the keyboard stream. What other streams exist in a typical program? (Think about file streams, network streams, the output stream.)"_

2. _"After `scanner.nextInt()`, there's a leftover newline in the buffer. What IS a buffer? Why does the operating system buffer keyboard input rather than delivering each character the moment a key is pressed?"_

3. _"In GUI (graphical) programs, users fill out forms with text fields and click buttons. There's no `scanner.nextLine()`. What mechanism do GUI programs use to collect user input? How does event-driven GUI input differ from sequential console input?"_

---

## 7. Unit 3: Control Flow

### Lessons 3.1--3.3

#### Instructional Cues

**String comparison --- immediate practice:**

```java
String day = "Wednesday";

// Wrong --- compares memory addresses
if (day == "Wednesday") {
    System.out.println("Middle of the week");  // May or may not print
}

// Correct --- compares content
if (day.equals("Wednesday")) {
    System.out.println("Middle of the week");  // Always correct
}

// Case-insensitive
if (day.equalsIgnoreCase("wednesday")) {
    System.out.println("This works too");
}
```

Create a practice file with 10 comparisons, half using `==` and half using `.equals()`. Ask the student to predict which ones will work correctly before running.

**Switch expressions (Java 14+):**

Modern Java supports switch expressions that return a value:

```java
String dayType = switch (day) {
    case "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" -> "Weekday";
    case "Saturday", "Sunday" -> "Weekend";
    default -> "Unknown";
};
System.out.println(day + " is a " + dayType);
```

This eliminates the fallthrough problem and is more concise. Teach both traditional `switch` (for reading legacy code) and switch expressions (for writing new code).

#### Thought Experiments

1. _"Java uses `&&` for AND, `||` for OR, `!` for NOT. Python uses the words `and`, `or`, `not`. Which approach is more readable when heard aloud by a screen reader? Is there a meaningful accessibility argument for one over the other?"_

2. _"The enhanced for loop `for (String item : list)` is simpler to write than the traditional `for (int i = 0; i < list.size(); i++)`. But sometimes you need the index. Name three operations you can do with the traditional loop that you cannot do (directly) with the enhanced loop."_

3. _"Java's `switch` statement traditionally falls through from one case to the next unless you write `break`. This 'feature' has caused countless bugs. Modern Java (14+) has switch expressions that don't fall through. What does this change tell you about how programming language design evolves in response to real-world usage patterns?"_

4. _"Short-circuit evaluation: `if (obj != null && obj.getValue() > 0)` --- if `obj` is null, the second condition is never evaluated. This prevents a NullPointerException. How does this behavior make certain coding patterns possible that would otherwise crash?"_

---

## 8. Unit 4: Arrays and ArrayLists

### Lesson 4.1: Arrays

#### Instructional Cues

**The fixed-size limitation --- demonstrate, don't just describe:**

```java
String[] fruits = new String[3];
fruits[0] = "apple";
fruits[1] = "banana";
fruits[2] = "cherry";
fruits[3] = "date";   // ArrayIndexOutOfBoundsException!
```

Let the student hear the exception and analyze the message: `Index 3 out of bounds for length 3`. Ask: "The message gives you two numbers. What are they? What does each tell you?"

**`Arrays.toString()` as mandatory print method:**

The first time `print(fruits)` produces `[Ljava.lang.String;@7a5d012b`, stop and explain: "This is the memory address of the array, not its contents. Java arrays don't have a built-in 'print nicely' behavior. Always use `Arrays.toString(fruits)` or loop through manually."

**The `for` vs `for-each` tradeoff --- make it concrete:**

```java
// for-each: simple, clear, but no index
for (String fruit : fruits) {
    System.out.println(fruit);
}

// traditional: more complex, but gives index
for (int i = 0; i < fruits.length; i++) {
    System.out.println(i + ": " + fruits[i]);
}

// The numbered version is more accessible!
```

For blind students, numbered output (showing both index and value) is generally more useful than unnumbered output. Teach the traditional `for` loop for array printing specifically because it enables indexed output.

#### Thought Experiments

1. _"Arrays are stored in contiguous memory --- all elements in a row, one after another. This is why accessing by index is fast: the address of element `i` is just the start address plus `i × element size`. Why does this contiguous storage make inserting into the middle of an array slow? What must happen to all the elements after the insertion point?"_

2. _"If you create `String[] arr = new String[5]`, what are the initial values of `arr[0]` through `arr[4]`? Now create `int[] nums = new int[5]` --- what are the initial values? Why are the defaults different between String arrays and int arrays?"_

3. _"Two-dimensional arrays in Java are 'arrays of arrays.' This means each row can have a different length --- a 'jagged array.' When would a jagged array be more appropriate than a rectangular 2D array? Give a real-world data example."_

---

### Lesson 4.2: ArrayLists

#### Instructional Cues

**Autoboxing --- explain the invisibility:**

```java
ArrayList<Integer> numbers = new ArrayList<>();
numbers.add(42);        // 42 (int) is auto-boxed to Integer(42)
int first = numbers.get(0);  // Integer(42) is auto-unboxed to 42
```

This happens invisibly but has a performance cost. For the course, tell students: "Use `ArrayList<Integer>` when you need a flexible list of integers. The boxing/unboxing is automatic but slightly less efficient than an array of `int`."

**Removal by index vs. by value:**

```java
ArrayList<String> list = new ArrayList<>(Arrays.asList("a", "b", "c", "b", "d"));
list.remove(1);            // Removes by INDEX --- removes "b" at position 1
list.remove("b");          // Removes by VALUE --- removes first "b" found
list.removeAll(Arrays.asList("b", "c"));  // Removes all matching values
```

Ask the student: "If I call `list.remove(0)` on a list of integers `[10, 20, 30]`, does this remove the element at index 0 (which is `10`) or remove the value `0` (which doesn't exist)? How does Java decide?" (Answer: removes index 0, because `0` is an `int`, not an `Integer`.)

#### Thought Experiments

1. _"An `ArrayList` doubles its internal capacity when it runs out of space. If you start with capacity 16 and keep adding elements, when does reallocation occur? Trace the capacity: 16 -> 32 -> 64 -> 128... What is the total cost (in element moves) of adding 1000 elements to an initially empty ArrayList this way? Is this efficient?"_

2. _"Java generics `ArrayList<String>` enforce type safety at compile time. Python lists can hold any types mixed together. When is a typed list (Java style) better? When is a mixed list (Python style) more flexible? Which approach produces more reliable programs?"_

---

## 9. Unit 5: Strings and String Processing

#### Instructional Cues

**String immutability --- the Java version:**

In Java, Strings are immutable for the same reason as Python. But Java's `String` object is also **interned** --- the JVM may reuse the same `String` object for two variables holding the same literal value. This is why `==` sometimes works for String comparison (when both refer to the same interned object) but is not reliable.

**`StringBuilder` motivation:**

```java
// Inefficient --- creates 100,000 String objects
String result = "";
for (int i = 0; i < 100000; i++) {
    result += "x";
}

// Efficient --- modifies a single buffer
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 100000; i++) {
    sb.append("x");
}
String result = sb.toString();
```

The `+` in a loop creates a new String object on every iteration, then discards the old one. For small loops this is fine; for large loops it's a significant performance problem. `StringBuilder` maintains a mutable buffer.

#### Thought Experiments

1. _"String concatenation with `+` is convenient but expensive in loops. In Python, the equivalent is also discouraged --- use `''.join(list)` instead. What does this common advice across two languages tell you about how immutable strings interact with loops?"_

2. _"Java's `String.format()` and `printf()` use format specifiers like `%s`, `%d`, `%f`. Python uses f-strings with `{}`. What are the accessibility tradeoffs of each approach? Which reads more naturally when heard aloud? Which is easier to type?"_

3. _"Regular expressions are a tiny language inside a programming language. `\\d+` matches one or more digits. `[a-zA-Z]+` matches one or more letters. Why do programmers use regular expressions despite their difficult-to-read syntax? What would the alternative be for complex pattern matching?"_

---

## 10. Unit 6: Methods

#### Instructional Cues

**Method overloading --- auditory navigation:**

```java
public static int add(int a, int b) { return a + b; }
public static double add(double a, double b) { return a + b; }
public static int add(int a, int b, int c) { return a + b + c; }
```

When IntelliSense shows overloads in VS Code, pressing `Shift+Alt+F2` (Accessible View) lists them all. Teach students to use this to discover available overloads.

**`void` vs. return type --- make the distinction tangible:**

```java
// void: for side effects only
public static void printGreeting(String name) {
    System.out.println("Hello, " + name + "!");
}

// Return type: for computation
public static double calculateTip(double billAmount, double rate) {
    return billAmount * rate;
}

// Using them:
printGreeting("Alice");                      // Standalone call
double tip = calculateTip(50.00, 0.18);      // Must capture return value
System.out.printf("Tip: $%.2f%n", tip);
```

_"`void` methods exist to DO something. Return-type methods exist to CALCULATE something and give you the result. Ask: 'Do I need to use the output later in my code?' If yes, it needs a return type."_

#### Thought Experiments

1. _"Java methods can throw exceptions: `public double sqrt(double n) throws IllegalArgumentException`. This signature tells callers that the method might fail in a specific way. Python has no equivalent syntax. What is the programmer's obligation when they see `throws` in a method signature?"_

2. _"Static methods belong to the class, not to any instance: `Math.sqrt(25)` --- you don't need a `Math` object. Instance methods belong to an object: `myString.length()`. What is the conceptual difference? When should a method be static vs. instance?"_

3. _"Method parameters in Java are 'pass by value' for primitives and 'pass by reference' for objects. For primitives: the method gets a copy, and modifying the parameter doesn't affect the original. For objects: the method gets the reference, and modifications to the object's fields DO affect the original. Design a test to confirm this behavior for both cases."_

4. _"Recursion: a method that calls itself. `int factorial(int n) { return n == 0 ? 1 : n _ factorial(n-1); }`. Every recursive solution has an iterative equivalent. When is the recursive version clearer? What is the risk of deep recursion (many nested calls)?"\*

---

## 11. Unit 7: Classes and OOP

### Extended Instructional Cues

**The mandatory `__str__` equivalent in Java --- `toString()`:**

Every student-defined class must override `toString()`. Without it, `System.out.println(myObject)` produces an unreadable string. The `@Override` annotation makes this explicit:

```java
@Override
public String toString() {
    return String.format("Dog[name=%s, age=%d]", name, age);
}
```

Require this in every class from Unit 7 onward. Explain: "When your screen reader reads `System.out.println(myDog)`, it reads whatever `toString()` returns. If you don't define `toString()`, you'll hear a memory address. That's useless."

**JavaDoc comments as accessible documentation:**

Teach this format for every method:

```java
/**
 * Calculates the area of this circle.
 *
 * @return the area as a double, in square units
 * @throws IllegalArgumentException if radius is negative
 */
public double getArea() {
    if (radius < 0) throw new IllegalArgumentException("Radius cannot be negative");
    return Math.PI * radius * radius;
}
```

When IntelliSense shows this method in VS Code, pressing `Shift+Alt+F2` reads the JavaDoc aloud. This makes the student's own code navigable via audio --- a profound accessibility benefit.

**The VS Code symbol navigator:**
`Ctrl+Shift+O` opens a dropdown listing all methods in the current file. Type a few letters to filter. This allows jumping to any method by name --- much more efficient than arrow-key navigation through a long file.

**Access modifiers --- enforce from day one:**

| Modifier                           | Rule        | Reason                                      |
| ---------------------------------- | ----------- | ------------------------------------------- |
| `private` on fields                | Always      | Encapsulation; prevents direct manipulation |
| `public` on getters/setters        | When needed | Controlled access                           |
| `private` on helper methods        | Yes         | Internal implementation detail              |
| `public` on methods the user calls | Yes         | Interface to the class                      |

Establish this as a non-negotiable habit, not a preference. _"Private fields, public interface. Every time."_

#### Thought Experiments

1. _"Encapsulation means the internal state of an object is private. Only its public methods can access or modify it. Why would you want to prevent direct access to `account.balance`? What bugs could occur if balance were public?"_

2. _"Inheritance creates a hierarchy. A `SavingsAccount` extends `BankAccount`. Every `SavingsAccount` is-a `BankAccount`, but not every `BankAccount` is-a `SavingsAccount`. What are the type-safety implications of this? If you have a `BankAccount` variable, can it hold a `SavingsAccount` object?"_

3. _"Java interfaces define contracts --- a list of methods that any implementing class must provide. A class can implement multiple interfaces but can only extend one class. Why this asymmetry? What problem does single inheritance solve? What does it prevent?"_

4. _"Design Pattern: the Factory Method creates objects without specifying the exact class. Instead of `new Dog()`, you'd call `AnimalFactory.create("dog")`. What is the advantage of this indirection? When would it be useful?"_

5. _"Object-oriented programming was supposed to model the real world. A `Dog` is-a `Animal`. But real-world relationships are complex --- a `FlyingFish` is both a `Fish` and can fly like a `Bird`. How does Java's single-inheritance model handle this situation? What alternatives exist?"_

6. _"Polymorphism means one interface, many implementations. `Animal[] animals = {new Dog(), new Cat(), new Bird()}; for (Animal a : animals) { a.speak(); }` --- each animal speaks differently. Why is this more flexible than checking `instanceof` and calling different methods explicitly?"_

#### Alternative Resources

- **"Head First Design Patterns" by Freeman, Robson et al.:** Visual book, but audio-describable concepts. Covers fundamental OOP design patterns. For advanced students.
- **"Effective Java" by Joshua Bloch:** The definitive book on Java best practices. Dense but invaluable for understanding WHY Java is designed the way it is.
- **Oracle Java Tutorials (docs.oracle.com/javase/tutorial/):** Comprehensive, plain HTML, fully accessible. Covers OOP concepts with extensive examples.

---

## 12. Unit 8: Files and Exception Handling

#### Instructional Cues

**Checked vs. unchecked exceptions --- the core distinction:**

| Type                             | Examples                                                                             | Must Handle?              | Why?                                                        |
| -------------------------------- | ------------------------------------------------------------------------------------ | ------------------------- | ----------------------------------------------------------- |
| **Checked**                      | `IOException`, `FileNotFoundException`, `SQLException`                               | Yes --- compiler enforces | These are recoverable; programmer should handle them        |
| **Unchecked (RuntimeException)** | `NullPointerException`, `ArrayIndexOutOfBoundsException`, `IllegalArgumentException` | No --- optional           | Usually indicate programming errors; may not be recoverable |

_"Checked exceptions are like warning labels: 'This operation can fail. You must decide what to do if it does.' Unchecked exceptions are usually bugs --- the program did something wrong."_

**Try-with-resources --- teach first, manual close second:**

```java
// Modern: try-with-resources (always teach this first)
try (BufferedReader reader = new BufferedReader(new FileReader("data.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    System.out.println("Error reading file: " + e.getMessage());
}
// reader is automatically closed here, even if an exception occurred

// Legacy: manual close (show this so students understand what try-with-resources does)
BufferedReader reader = null;
try {
    reader = new BufferedReader(new FileReader("data.txt"));
    // ... use reader
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
} finally {
    if (reader != null) {
        try { reader.close(); } catch (IOException e) { /* ignore */ }
    }
}
```

Show the legacy version to explain why try-with-resources exists and what it simplifies.

#### Thought Experiments

1. _"Checked exceptions force you to handle failures at compile time. Critics argue this creates 'exception chaining hell' --- every method signature becomes littered with `throws` clauses. Defenders argue it makes failure modes explicit and programs more reliable. Which side do you find more persuasive? Why?"_

2. _"Java's `Path` and `Files` classes (java.nio.file) are a modern replacement for the older `File` class. The older `File` class's `delete()` method returns a `boolean` (true/false) instead of throwing an exception. What is the danger of reporting failure via a return value? What might a programmer accidentally do wrong?"_

3. _"A `NullPointerException` is called 'The Billion Dollar Mistake' by its inventor Tony Hoare. Explain why null references cause so many bugs. Newer languages (Kotlin, Swift) have built-in null safety. What would Java code look like if null didn't exist?"_

---

## 13. Unit 9: Collections, Analysis, and Testing

### JUnit Testing Deep Dive

#### Instructional Cues

**Test output is inherently accessible:**
JUnit produces plain text output: `.` for each passing test, `F` for failures, with descriptive failure messages. This is one of the most screen-reader-friendly outputs in the entire course. Let students experience testing by running a test suite and listening to the results before writing their own tests.

**Test naming convention --- sentence style:**

```java
@Test
public void calculateArea_withPositiveRadius_returnsCorrectValue() { }

@Test
public void calculateArea_withZeroRadius_returnsZero() { }

@Test
public void calculateArea_withNegativeRadius_throwsException() { }
```

The naming convention `methodName_condition_expectedBehavior` makes test names read as complete sentences when the test runner announces them. This is both good practice and an accessibility benefit --- each test announcement tells you exactly what was tested.

**`assertThrows` --- test that exceptions work correctly:**

```java
@Test
public void withdraw_withInsufficientFunds_throwsException() {
    BankAccount account = new BankAccount(100.0);
    assertThrows(InsufficientFundsException.class, () -> account.withdraw(200.0));
}
```

Testing for exceptions is as important as testing for correct outputs. Many beginners only test the "happy path."

#### Thought Experiments

1. _"Test-driven development (TDD) says: write the test first, then write the implementation. How does writing a test first change the way you think about a method? What is forced to be clear before you write a line of implementation?"_

2. _"Mocking means replacing real dependencies (like a database or file system) with fake versions for testing. Why would you want to test a method that reads from a database without using a real database? What complexity does mocking introduce?"_

3. _"A project has 100% test coverage --- tests execute every line. Is the software correct? Name a bug that 100% coverage would not catch. (Hint: think about a bug that only appears with certain combinations of inputs.)"_

---

## 14. Units 10--11: Projects and Capstone

### Java Project Architecture

For the capstone, encourage a clean package structure:

```
src/
|--- com/
|   +--- student/
|       +--- datamanager/
|           |--- model/
|           |   +--- Contact.java
|           |--- storage/
|           |   |--- DataManager.java
|           |   +--- JsonStorage.java
|           |--- ui/
|           |   +--- ConsoleUI.java
|           +--- Main.java
test/
+--- com/
    +--- student/
        +--- datamanager/
            |--- model/
            |   +--- ContactTest.java
            +--- storage/
                +--- DataManagerTest.java
```

Navigating packages in VS Code: `Ctrl+Shift+E` for Explorer (shows package tree), `Ctrl+P` to open any file by name, `Ctrl+Shift+O` for symbols within the current file.

### IDE-Generated Code Accessibility

VS Code and compatible Java IDE extensions can generate getters, setters, constructors, and toString. Teach these as time-savers, but require students to read and understand all generated code:

- `Ctrl+Shift+P` -> "Java: Generate Getters and Setters"
- `Ctrl+Shift+P` -> "Java: Override/Implement Methods"
- `Ctrl+Shift+P` -> "Java: Generate toString"

Generated code is correct but often not styled for accessibility (missing JavaDoc, generic names). Require students to add JavaDoc and verify `toString()` output is meaningful when heard.

#### Thought Experiments

1. _"Java in enterprise software is often criticized for having too much 'boilerplate' --- code that exists for structural reasons rather than to express logic. How does this boilerplate affect the experience of maintaining a large Java codebase? What tools and patterns does the Java ecosystem provide to reduce it?"_

2. _"Your capstone application stores data in a file. If your team adds a new field to the data class, existing saved files no longer match the new format. This is a 'schema migration' problem. How would you design your storage layer to handle this gracefully?"_

---

## 15. Bridging from Python to Java

For courses that teach Python before Java, use these comparison thought experiments to bridge the languages:

**Syntax bridge table:**

| Python              | Java                                               | Notes                                           |
| ------------------- | -------------------------------------------------- | ----------------------------------------------- |
| `print("Hello")`    | `System.out.println("Hello")`                      |                                                 |
| `x = 5`             | `int x = 5;`                                       | Java requires type declaration and semicolon    |
| `if condition:`     | `if (condition) {`                                 | Parens around condition; brace instead of colon |
| `elif`              | `else if`                                          | Two words in Java                               |
| `for item in list:` | `for (Type item : list) {`                         | Java requires type                              |
| `def func(x):`      | `public static void func(int x) {`                 | Return type and access modifier required        |
| `return x`          | `return x;`                                        | Semicolon                                       |
| `# comment`         | `// comment`                                       |                                                 |
| `None`              | `null`                                             |                                                 |
| `True`/`False`      | `true`/`false`                                     | Lowercase in Java                               |
| `len(list)`         | `list.size()`                                      | Method call, not function                       |
| `list.append(x)`    | `list.add(x)`                                      |                                                 |
| `dict["key"]`       | `map.get("key")`                                   |                                                 |
| `try/except`        | `try/catch`                                        |                                                 |
| `import math`       | `import java.lang.Math;` (or use `Math.` directly) |                                                 |

**Thought experiments for bridging:**

1. _"In Python you write `x = 5` and Python figures out the type. In Java you write `int x = 5` and declare the type explicitly. Which approach do you prefer after using both? Which one would you choose for a large team project? For a quick experiment?"_

2. _"Python lists can hold any mixture of types: `[1, 'hello', True, 3.14]`. Java's `ArrayList<String>` can only hold Strings. What bugs does Python's flexibility enable? What bugs does it prevent compared to Java?"_

3. _"Python functions are first-class objects --- you can store them in variables, pass them as arguments. In Java (before lambdas), this was much more complex. Java added lambdas in 2014. What does it mean for a language to add a major feature 19 years after it was created?"_

---

## 16. Assessment Strategies

### Alternative Assessment Forms

**Code review presentations:** The student explains their code out loud, as if presenting to a team. The teacher asks questions about design decisions. This tests understanding more authentically than multiple-choice questions.

**Bug-hunting assessments:** Provide a working program with 5--8 intentional bugs of different types. The student must find and fix them using only their screen reader and development tools. This directly tests real-world debugging skill.

**Design walkthroughs:** Give the student a problem and ask them to design the solution --- class structure, methods, data structures --- without writing any code. Assess the quality of the design, not the typing speed.

**Pair programming sessions:** Two students work on one computer. One dictates code; the other types. Roles swap every 10--15 minutes. This surfaces communication and reasoning skills that solo assessments miss.

---

## 17. Supporting Diverse Needs

### For Braille Display Users

Java's verbose syntax can be particularly burdensome on a braille display with limited width. Strategies:

- Keep lines under 79 characters (PEP 8 applies to style; the Java equivalent is generally under 100).
- Use shorter variable names for very long class hierarchies where the full name is unwieldy.
- Test the learner's chosen editor with their braille display and screen reader. Prefer the documented VS Code or Theia workflows and avoid adding IDE complexity before it is needed.

### For Students New to Screen Readers

If a student is still developing screen reader proficiency:

- Begin with JShell instead of file-based programming. Single-line interactions provide immediate feedback.
- Use pair work more extensively until independent navigation is fluent.
- Reduce the number of new concepts per session until screen reader fluency stabilizes.

---

## 18. Alternative and Supplementary Resources

### Textbooks and Reading

| Resource                                                      | Level                  | Format        | Accessibility                                                     |
| ------------------------------------------------------------- | ---------------------- | ------------- | ----------------------------------------------------------------- |
| **Introduction to Programming Using Java** (Eck, free online) | Beginner--Intermediate | Free HTML/PDF | HTML version excellent; comprehensive                             |
| **Big Java: Early Objects** (Horstmann)                       | Beginner               | Print/ebook   | Standard university text; clear explanations                      |
| **Effective Java, 3rd Ed.** (Bloch)                           | Intermediate--Advanced | Print/ebook   | Essential for understanding Java's design philosophy              |
| **Head First Java** (Sierra, Bates)                           | Beginner               | Print         | Very visual; but text portions accessible; engaging writing style |
| **Java: The Complete Reference** (Schildt)                    | Reference              | Print/ebook   | Encyclopedic; good for looking up specific features               |
| **Oracle Java Tutorials** (docs.oracle.com)                   | Beginner--Advanced     | Free HTML     | Excellent HTML accessibility; definitive                          |
| **Java Documentation** (javadoc)                              | Reference              | Free HTML     | Standard library docs; fully screen-reader-accessible             |

### Online Courses and Platforms

| Platform                             | Course                              | Accessibility | Notes                                         |
| ------------------------------------ | ----------------------------------- | ------------- | --------------------------------------------- |
| **edX / MITx 6.092**                 | Introduction to Programming in Java | High          | MIT course; video transcripts available       |
| **Coursera**                         | Java Programming (Duke)             | Medium        | Free audit available                          |
| **Codecademy**                       | Learn Java                          | Partial       | Some UI inaccessible; editor readable         |
| **MOOC.fi** (University of Helsinki) | Java Programming MOOC               | High          | Text-based exercises; excellent accessibility |
| **CodingBat Java**                   | Java practice problems              | High          | Plain HTML; no complex UI                     |
| **Exercism Java Track**              | Structured exercises with mentoring | High          | Terminal-based; excellent                     |
| **LeetCode**                         | Algorithm problems                  | Medium        | Code editor accessible; UI moderate           |

**MOOC.fi is especially recommended** for blind students --- the University of Helsinki's Java course has no-frills HTML exercises and very clear progression. It is one of the most accessible Java learning platforms available.

### Video and Audio Resources

| Resource                                       | Description                             | Accessibility             |
| ---------------------------------------------- | --------------------------------------- | ------------------------- |
| **CS50 AP** (Harvard)                          | AP Computer Science A course using Java | Captions and transcripts  |
| **Derek Banas Java Tutorials** (YouTube)       | Concise concept-by-concept tutorials    | Captions available        |
| **Cave of Programming Java** (YouTube/website) | Beginner Java series                    | Captions; text summaries  |
| **thenewboston Java** (YouTube)                | Large beginner series                   | Captions available        |
| **Coding with John** (YouTube)                 | Clear explanations of Java concepts     | Good pacing for beginners |

---

## 19. Quick Reference Sheets

### Java Compilation and Running

```bash
# Compile a single file
javac HelloWorld.java    # Creates HelloWorld.class

# Run compiled program
java HelloWorld          # No .class extension!

# Compile with output directory
javac -d bin src/HelloWorld.java

# Run JShell
jshell                   # Interactive REPL
/exit                    # Exit JShell

# Run tests (if using Maven)
mvn test

# Run tests (if using Gradle)
./gradlew test
```

**Windows PowerShell (Windows 11):**

```powershell
# Compile a single file
javac HelloWorld.java    # Creates HelloWorld.class
# Run compiled program
java HelloWorld          # No .class extension!
# Compile with output directory
javac -d bin src/HelloWorld.java
# Run JShell
jshell                   # Interactive REPL
/exit                    # Exit JShell
# Run tests (if using Maven)
mvn test
# Run tests (if using Gradle)
.\gradlew.bat test
```

### Error Type Quick Reference

| Error Type                                                     | Common Cause                                       | First Check                       |
| -------------------------------------------------------------- | -------------------------------------------------- | --------------------------------- |
| `cannot find symbol`                                           | Misspelled name or missing import                  | Spelling; check imports           |
| `incompatible types`                                           | Assigning wrong type or missing cast               | Type of both sides of assignment  |
| `';' expected`                                                 | Missing semicolon                                  | End of the line indicated         |
| `reached end of file while parsing`                            | Missing `}`                                        | Count open braces vs close braces |
| `non-static method cannot be referenced from a static context` | Calling instance method from `main` without object | Need to create an object first    |
| `NullPointerException`                                         | Calling method on null reference                   | Which variable is null            |
| `ArrayIndexOutOfBoundsException`                               | Index beyond array length                          | Print length and the index used   |
| `ClassCastException`                                           | Invalid cast                                       | Check `instanceof` before casting |
| `StackOverflowError`                                           | Infinite recursion                                 | Verify base case                  |
| `NumberFormatException`                                        | `parseInt()` on non-numeric string                 | Check input string before parsing |

### Scanner Method Reference

```java
Scanner scanner = new Scanner(System.in);

String line   = scanner.nextLine();     // Entire line as String
String word   = scanner.next();         // Single token (whitespace-delimited)
int n         = scanner.nextInt();      // Integer
double d      = scanner.nextDouble();   // Double
boolean b     = scanner.nextBoolean();  // Boolean (true/false)

// Safe versions with type checking
if (scanner.hasNextInt()) {
    int n = scanner.nextInt();
}

// After nextInt(), consume leftover newline:
scanner.nextLine();  // ALWAYS do this before reading a String

// From file
Scanner fileScanner = new Scanner(new File("data.txt"));
// Same methods work; wrap in try-catch for FileNotFoundException

scanner.close();  // Always close when done
```

### Accessible Output Template

```java
// Numbered list output
System.out.println("--- Contacts ---");
for (int i = 0; i < contacts.size(); i++) {
    System.out.printf("%d. %s%n", i + 1, contacts.get(i));
}
System.out.printf("Total: %d contacts%n", contacts.size());

// Menu
System.out.println("\n--- Main Menu ---");
System.out.println("1. Add contact");
System.out.println("2. View all contacts");
System.out.println("3. Search contacts");
System.out.println("4. Delete contact");
System.out.println("5. Save and quit");
System.out.println("-----------------");
System.out.print("Enter option (1-5): ");

// Confirmation messages
System.out.printf("Contact '%s' added successfully.%n", name);
System.out.printf("Found %d matching records.%n", count);
System.out.println("Data saved to contacts.json.");
System.out.println("Error: Name field cannot be empty. Please try again.");
```

## 20. Teaching AI Tools Responsibly

AI coding assistants can explain compiler messages, offer hints, compare designs, or suggest test cases. They can also invent Java APIs, use language features unsupported by the configured JDK, omit imports, produce incompatible types, mishandle exceptions, or create unnecessary class hierarchies. Treat generated answers as unverified drafts. The course must remain teachable without paid AI access or a personal account.

### Instructor use of AI during preparation

Instructors may use approved AI tools to brainstorm examples, draft alternate explanations, suggest test cases, or identify likely misconceptions. The instructor remains accountable for correctness and accessibility. Verify APIs and language features against the target JDK and official Java documentation; compile and test examples; inspect dependencies and build instructions; and test the workflow with the intended access technology. Never upload identifiable student work, accommodation plans, credentials, assessment answers, or confidential school information. Do not use AI-generated feedback as the sole basis for grading. Disclose substantive AI assistance when institutional policy or the publication process requires it.


### Learning goals and appropriate uses

Students should explain that generated responses can be plausible and incorrect, ask focused questions, verify claims against official Java documentation and compiler feedback, identify unfamiliar APIs and dependencies, review code for accessibility and security, and disclose assistance when required. When permitted, AI may explain a diagnostic, ask guiding questions, rephrase a concept, suggest tests, or critique a proposed class design.

### Java-specific risks

Review generated Java for:

- Language features or APIs requiring a newer JDK than the course environment.
- Incorrect imports, package declarations, class/file names, or `main` signatures.
- Incompatible types, unsafe casts, incorrect generics, and confusion between primitive and reference types.
- Incorrect use of `==` for String content comparison instead of `.equals()`.
- Null handling that can cause `NullPointerException`.
- Incorrect resource handling, file paths, exception declarations, or broad catch blocks.
- Confusion among `Scanner.next()`, `nextLine()`, and numeric input, including the pending-newline issue.
- Unnecessary frameworks, Maven/Gradle dependencies, or architecture beyond the lesson.
- Long declarations, deeply nested code, and IDE-generated scaffolding that is difficult to navigate.

Compile with the course's JDK, read the complete diagnostic, and run tests. Check API and language claims in official Java documentation and the Java Language Specification.

### Screen-reader and IDE review

Review whether the learner can navigate package and class declarations, fields, constructors, methods, and `main`; identify braces and nested blocks; understand method names, parameters, return types, and access modifiers; and access diagnostics as text with reliable file and line references. Prefer a small number of clear classes and methods over elaborate architecture. Explain generated boilerplate rather than treating it as magic.

### Privacy, security, copyright, and equity

Do not enter student records, credentials, API keys, private repositories, or confidential school information into public AI systems. Follow school policy, approved-tool lists, age requirements, and data-protection obligations. Treat generated shell commands, build files, and dependency recommendations as untrusted. Verify library coordinates and maintainers before adding dependencies. Do not assume generated code is original or correctly licensed. Provide a non-AI alternative and discuss assumptions about visual IDE workflows and graphical output.

### Verification protocol: Ask – Inspect – Verify – Adapt – Explain – Disclose

1. **Ask:** state the concept or error and what the student understands.
2. **Inspect:** identify unfamiliar types, APIs, dependencies, and assumptions.
3. **Verify:** consult official documentation, compile with the target JDK, and test normal, boundary, and invalid cases.
4. **Adapt:** simplify, correct, secure, and format for the learner's level and access workflow.
5. **Explain:** have the learner explain each class, method, type, and exception path and make a modification independently.
6. **Disclose:** record the tool and its contribution when required.

### Activity-specific policy

- **Practice:** hints, explanations, and test ideas may be allowed; full solutions should be reserved for explicit code-review activities.
- **Projects:** define permitted AI assistance in advance; require disclosure, tests, and an explanation of design decisions.
- **Individual assessments:** AI should not perform the skill being measured unless the assessment explicitly evaluates AI-assisted development or an accommodation requires it.
- **Accessibility:** screen readers, braille displays, magnification, and approved access tools are not prohibited answer-generation tools.

### Discussion prompts

- An AI example compiles on a newer JDK but not on class machines. How can the learner identify the version dependency?
- An assistant uses `==` to compare two strings. How can the student demonstrate the defect?
- A generated program catches every exception and prints "Something went wrong." Why is that inadequate?
- How can a learner distinguish understanding an object-oriented design from merely running it?

---

## 21. Comprehensive Instructional Planning and Course Implementation

This section consolidates practices that apply across the philosophy, learner-context, classroom setup, spoken-code, unit, assessment, differentiation, and resource sections above. Use it as a course-planning reference from intake through capstone evaluation.

### 21.1 Course planning and alignment

Map each unit to prerequisites, learning objectives, practice opportunities, and evidence of mastery. Do not assume every unit needs equal time.

- Identify outcomes: problem decomposition, code reading and writing, data representation, control flow, functions or methods, debugging, testing, and communication.
- Separate programming prerequisites from access-tool prerequisites.
- Record the operating system, editor/IDE, runtime, terminal, screen reader, braille display, magnification, and adaptive input technology used.
- Identify essential concepts, enrichment topics, and material that can be deferred without breaking later lessons.
- Plan checkpoints after each major concept group and adjust pacing using student evidence.
- Maintain a map linking each lesson to objectives, practice, assessment, accessibility considerations, and likely misconceptions.

A suggested progression is environment and navigation; computing foundations; expressions and data; input/output; decisions and loops; collections; functions or methods; object-oriented concepts; files and errors; testing; projects; capstone. Preserve prerequisites when reordering.

### 21.2 Readiness and learner partnership

Ask about preferred access methods, prior programming experience, keyboard navigation, file management, and what makes technical instruction usable. Ask about functional access requirements rather than requesting unnecessary diagnostic details.

Use a low-stakes baseline activity to observe how the learner opens and navigates a source file, moves by line/word/character/symbol, creates and saves a file, runs a command, locates output, and reads a diagnostic. Record strengths and supports, not just deficits. Revisit the baseline to recognize growth. Keep the learner central to decisions about tools and workflow.

### 21.3 Repeatable lesson architecture

1. **Purpose:** state the problem the lesson addresses.
2. **Prerequisite retrieval:** revisit the prior concept needed today.
3. **Vocabulary:** define technical terms and spoken symbol conventions.
4. **Explicit model:** demonstrate a small runnable example and narrate navigation and code changes.
5. **Trace:** read the code structurally and predict behavior.
6. **Guided practice:** solve a similar problem with prompts and fading support.
7. **Independent transfer:** apply the concept to a new requirement.
8. **Debug and reflect:** examine an intentional error or unexpected result.
9. **Exit check:** collect an explanation, prediction, code change, or test.

State one navigation action at a time, allow the learner to complete it, and confirm the result before continuing. Provide source files and commands in advance when possible. Narrate all actions in shared-screen demonstrations and provide an equivalent text-based route.

### 21.4 Explicit instruction for accessible code navigation

Teach file structure before reading every line. Identify current focus and how to return to a known location. Teach line, word, character, symbol, selection, search, and go-to-line navigation, plus navigation to functions, methods, classes, and diagnostics. Explain indentation and block boundaries. Use manageable line lengths and avoid unnecessarily nested expressions. Give students time to read diagnostics and output independently. Do not take over the keyboard without explaining the action and obtaining the learner's agreement.

### 21.5 Language-specific instructional emphasis: Java

Java's explicit types, compilation, and class structure require deliberate sequencing:
- Teach the JDK, compiler, runtime, source file, class, and `main` method before IDE-generated projects.
- State the target JDK version and explain when features require a newer release.
- Contrast primitive values and reference types, assignment and comparison, conversions, and integer versus floating-point division.
- Teach String content comparison with `.equals()`, not `==`, and explain null references.
- Model `Scanner` input carefully, especially the newline remaining after token or numeric reads.
- Teach array bounds, ArrayList operations, generic types, and collection selection with small examples.
- Separate method signature, parameter, argument, return type, and method call. Explain `static` versus instance behavior.
- Teach constructors, encapsulation, inheritance, and composition as design choices, not just syntax.
- Read compiler diagnostics before running; distinguish compile-time errors, runtime exceptions, and logic defects.
- Keep build tools and external dependencies out of early lessons unless required. Explain Maven or Gradle when introduced.

### 21.6 Misconceptions and diagnostic teaching

Ask learners to predict behavior, explain their prediction, run a small experiment, and revise their mental model.

| Common issue | Instructional response |
| --- | --- |
| Confusing assignment with comparison | Contrast operators and trace values before and after execution. |
| Treating input as already numeric | Identify input type, convert explicitly, and test valid and invalid values. |
| Off-by-one loop or index errors | Trace first, typical, and final iterations; state the valid index range. |
| Choosing an unsuitable collection | Describe access patterns and required operations before choosing a structure. |
| Writing one large function or method | Decompose the task by responsibility and test each part. |
| Treating a running program as necessarily correct | Define expected behavior and test normal, boundary, and invalid inputs. |
| Copying code without tracing it | Ask the learner to predict a new case and make a modification. |
| Misreading an error message | Locate the useful diagnostic, identify file and line, and inspect surrounding code. |

Language-specific pitfalls include: primitive versus reference values; integer division; String identity versus content equality; null references; array bounds; constructor and method signatures; static versus instance members; checked exceptions; and the Scanner newline behavior.

### 21.7 Differentiation without lowering the learning objective

Adjust the path, not the intellectual goal. Supports may include smaller task increments, additional practice, explicit worked examples, alternative information formats, extra navigation time, starter code with gradually faded scaffolding, oral explanation or accessible demonstration, pair programming with rotating roles, predictable routines, and enrichment tasks that deepen the same concept.

Do not assume all blind students need the same support or that all low-vision students prefer magnification. Ask, document, and review supports with the learner.

### 21.8 Formative assessment, feedback, and grading

Collect evidence frequently: explain a concept, predict output, trace a loop, justify a data structure, find and fix a bug, write a boundary test, refactor code, or demonstrate an accessible workflow.

A practical rubric can score each dimension from 1 (beginning) to 4 (independent and consistent):

| Dimension | Evidence |
| --- | --- |
| Conceptual reasoning | Explains the problem, algorithm, and language concepts |
| Implementation | Produces a solution that meets requirements |
| Code comprehension | Reads, traces, explains, and modifies code |
| Testing and debugging | Uses test cases and interprets diagnostics |
| Accessibility and communication | Produces understandable interaction and operates the workflow with access tools |
| Independence and reflection | Describes decisions, limitations, and next steps |

Share criteria before assessment. Feedback should name observed behavior, explain its impact, and identify an actionable next step. Do not grade screen-reader speed, typing speed, or visual formatting as proxies for programming competence.

### 21.9 Debugging and classroom support protocol

1. Ask the learner to describe expected behavior.
2. Ask what actually happened.
3. Read the complete error or diagnostic, including source and location.
4. Identify the smallest relevant code section.
5. Form one hypothesis.
6. Change one thing and rerun the program or test.
7. Record what the result taught the learner.

Distinguish environment failures, tool-access failures, syntax/compile errors, runtime errors, and logic errors. Maintain a troubleshooting record with environment, exact command, error text, attempted correction, and outcome. Remove credentials and private information before sharing logs.

### 21.10 Pair programming and collaboration

Use explicit roles: the **driver** controls the keyboard and implements the agreed step; the **navigator** reasons about the algorithm, checks requirements, proposes tests, and reviews the result. Rotate roles. Do not automatically assign a blind student the navigator role. Both learners should have opportunities to operate tools and write code. Provide shared source files and task instructions in accessible formats.

### 21.11 Project and capstone supervision

Require a proposal that includes the problem and intended user, functional requirements, out-of-scope features, input/output design, data representation, major functions/methods/classes, accessibility requirements, milestones, tests, and any libraries or AI assistance used.

Review milestones: requirements, design, first working slice, feature completion, tests, documentation, and final explanation. Encourage a modest, complete, well-tested project over an ambitious unfinished one.

### 21.12 Collaboration with families and support professionals

When appropriate and with learner consent, coordinate with special educators, teachers of students with visual impairments, assistive-technology specialists, interpreters, and families. Agree on who supports access technology, who teaches programming, and how the student obtains help. Keep the learner's agency central, share only necessary information, and follow school privacy policies. Do not make aides the default operators of the student's computer.

### 21.13 Instructor preparation checklist

Before each unit, complete the learner-facing activities; verify commands and versions on the classroom platform; test keyboard and assistive-technology workflows; prepare expected output and common error examples; identify vocabulary, symbols, misconceptions, and prerequisites; provide accessible instructions and assessment criteria; and decide how understanding will be observed.

After each unit, review student work and feedback, note barriers, adjust pacing and scaffolds, and record reproducible corrections. Document agreed accommodations rather than silently changing expectations.

### 21.14 Quality assurance and continuous improvement

Review links, software versions, commands, APIs, package recommendations, and assessment assumptions periodically. Test with actual screen readers and braille displays where possible; a successful build or visual inspection alone does not establish accessibility.

When reporting a barrier, include the page, reproduction steps, operating system, editor/runtime version, assistive technology and version, expected behavior, and actual behavior. Exclude personally identifying or sensitive student information. Submit corrections through the project contribution process.

---

