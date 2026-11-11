# Unit 1: Foundations of Computing

## Overview

Connect problem solving and algorithms to a first program, then learn variables, values, and types using the shared student profile.

---


## Lesson 1.1: Welcome to Computer Science

### Reading References
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- [Control flow](https://kotlinlang.org/docs/control-flow.html)
- Matching Python lesson: Lesson 1.1: Welcome to Computer Science

### Learning Objectives
- Explain hardware, software, and algorithm in your own words.
- Turn a written algorithm into a short Kotlin program.
- Predict a program's output by hand before running it.

### Concept Explanation

Computers follow instructions exactly. *Hardware* is the machine, *software* is the set of instructions it follows, and an *algorithm* is an ordered, finite list of clear steps that solves a problem. Unit P of this repository covers these ideas in detail.

A reliable way to solve a problem is to understand it, break it into steps, write the steps in plain language, translate them into code, and test the result.

The plan here is: set a total to zero; for each score, add it to the total; divide the total by the number of scores; report both. In Kotlin, `val` makes a read-only name and `var` makes a name that can be reassigned, `for (score in scores)` visits a list in order, and `scores.size` is the number of items.

The shared scores are 82, 91, 76, and 88. Their total is 337 and their average is 84.25. A hand trace should reach the same numbers: 82, 173, 249, then 337.

### Worked Example

```kotlin
fun main() {
    val scores = listOf(82, 91, 76, 88)
    var total = 0
    for (score in scores) {
        total += score
    }
    val average = total.toDouble() / scores.size
    println("Total: $total")
    println("Average: $average")
}
```

### Expected Behavior or Output

The program prints:
```text
Total: 337
Average: 84.25
```

### Common Mistakes
1. Writing code before writing the steps, then forgetting to divide by the number of scores.
2. Dividing two integers and expecting a decimal. `337 / 4` is `84`; convert one side with `toDouble()`.
3. Declaring `total` with `val` and then trying to add to it, which is a compile error.

### Activities
1. Trace the loop by hand and write the running total after each score.
2. Change the list to 90 and 80 and predict the total and average before running.
3. Add a loop that finds the highest score and prints it.
4. Explain the difference between the algorithm and the program in two sentences.

### Accessibility Practice

Write the hand trace as numbered sentences, one for each loop pass, and read it back with your screen reader. Compare it with the two printed lines in order.

### Skills Checklist
- [ ] I can define hardware, software, and algorithm.
- [ ] I can describe an algorithm as ordered steps.
- [ ] I can trace a loop by hand.
- [ ] I can explain `val` versus `var`.
- [ ] I can run the program and compare it with my trace.

---

## Lesson 1.2: Your First Kotlin Program

### Reading References
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Matching Python lesson: Lesson 1.2: Your First Python Program - Hello World

### Learning Objectives
- Write and run a program that prints text.
- Use comments and string templates.
- Explain that statements run in order.

### Concept Explanation

A Kotlin program is a list of *statements* that run in order inside `main`. `println` writes its argument and ends the line; `print` writes without ending the line. Text in double quotation marks is a *string*.

A *string template* inserts a value into text: `$name` inserts a variable, and `${expression}` inserts the result of any expression. A line comment starts with `//` and a block comment is written between `/*` and `*/`. Triple quotation marks, `"""..."""`, make a *raw string* that can span lines.

Because Kotlin is a compiled language, a mistake such as a missing quotation mark is reported at compile time and no program is produced.

### Worked Example

```kotlin
fun main() {
    // This program greets the shared student.
    val name = "Avery"
    println("Hello, $name!")
    print("No new line here, ")
    println("then one here.")
    println("Name has ${name.length} letters.")
    println("""Two lines
in one raw string.""")
}
```

### Expected Behavior or Output

The program prints:
```text
Hello, Avery!
No new line here, then one here.
Name has 5 letters.
Two lines
in one raw string.
```

### Common Mistakes
1. Using a curly quotation mark pasted from a document instead of a straight one, which is a syntax error.
2. Writing `$name` where a longer expression needs `${...}`, such as `$name.length`, which inserts the name and then the text `.length`.
3. Forgetting that `print` does not end the line.

### Activities
1. Run the program and describe how the second and third lines differ from the others.
2. Change the greeting to use your own name and predict the output.
3. Print three lines: your name, the course name, and today's task.
4. Add a comment above every line and read the file aloud with the comments.

### Accessibility Practice

Run from the terminal and read the output line by line. Check that your screen reader announces the dollar sign and the braces in a string template, since they decide what the program prints.

### Skills Checklist
- [ ] I can write and run a program that prints text.
- [ ] I can use string templates.
- [ ] I can write comments.
- [ ] I know how `print` and `println` differ.
- [ ] I can read a first compile error.

---

## Lesson 1.3: Variables and Simple Data Types

### Reading References
- [Basic types](https://kotlinlang.org/docs/basic-types.html)
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Matching Python lesson: Lesson 1.3: Variables and Simple Data Types

### Learning Objectives
- Declare read-only and changeable variables.
- Name Kotlin's basic types and check a value's type.
- Explain type inference.

### Concept Explanation

Kotlin is *statically typed*: every value has a type that the compiler knows. You may write the type, as in `val age: Int = 16`, or let the compiler *infer* it from the value, as in `val age = 16`. The type is still fixed after inference; Kotlin is not dynamically typed.

`val` declares a read-only name that cannot be reassigned. `var` declares a name that can. Prefer `val`, and use `var` only when a value must change.

The basic types are `Int` and `Long` (whole numbers), `Double` and `Float` (decimals), `Boolean`, `Char`, and `String`. A whole-number literal such as 16 is an `Int`, and a literal with a decimal point such as 1.72 is a `Double`. `value::class.simpleName` reports a value's type name.

The shared student profile is name Avery, age 16, height 1.72 meters, and favorite subject Computer Science. The shared Notebook item has quantity 3 and unit price 2.50, so three notebooks cost 7.5.

### Worked Example

```kotlin
fun main() {
    val name = "Avery"
    val age = 16
    val height = 1.72
    val favoriteSubject = "Computer Science"
    println("$name, $age, $height, $favoriteSubject")
    println("${name::class.simpleName} ${age::class.simpleName} ${height::class.simpleName}")

    val notebookPrice = 2.50
    val notebookQuantity = 3
    println("Notebook total: ${notebookPrice * notebookQuantity}")

    var visits = 1
    visits += 1
    println("Visits: $visits")
}
```

### Expected Behavior or Output

The program prints:
```text
Avery, 16, 1.72, Computer Science
String Int Double
Notebook total: 7.5
Visits: 2
```

### Common Mistakes
1. Declaring with `val` and then reassigning, which is a compile error.
2. Assuming inference makes Kotlin dynamic. `val x = 16` can never hold text later.
3. Mixing `Int` and `Double` without conversion in a declaration that names the type, such as `val d: Double = 16`, which does not compile.

### Activities
1. Run the example and write each type name in the order printed.
2. Change `age` to `16L` and predict the type name.
3. Add a Boolean `likesCs` and print its type.
4. Explain, without code, when to choose `var` over `val`.

### Accessibility Practice

Say names with their capital letters aloud (`favoriteSubject`), and print each value inside a labelled sentence so that the screen reader announces the name and value together.

### Skills Checklist
- [ ] I can declare `val` and `var`.
- [ ] I can name Kotlin's basic types.
- [ ] I can explain type inference.
- [ ] I can check a value's type name.
- [ ] I can explain why `val` is preferred.

---
