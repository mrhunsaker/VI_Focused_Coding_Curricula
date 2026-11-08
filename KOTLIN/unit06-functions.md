# Unit 6: Functions

## Overview

Define functions, pass arguments, return results, process collections in functions, and accept a variable number of arguments.

---


## Lesson 6.1: Defining Functions

### Reading References
- [Functions](https://kotlinlang.org/docs/functions.html)
- Matching Python lesson: Lesson 6.1: Defining Functions

### Learning Objectives
- Define and call functions.
- Pass parameters and return nothing or a value.
- Treat a function as a value.

### Concept Explanation

A function is declared with `fun name(parameters): ReturnType { ... }`. Each parameter names its type: `fun showTip(bill: Double, tipRate: Double)`. A function with no result returns `Unit`, which you usually leave out. A function whose body is one expression can use `=`: `fun greetName(name: String) = println("Hello, $name!")`.

The *parameters* are the names in the definition and the *arguments* are the values you pass. Arguments are matched to parameters by position.

Functions are values. `::showTip` is a reference to the function, which can be stored in a variable and called like the function itself. Top-level functions are declared outside any class and can be called from anywhere in the same package.

### Worked Example

```kotlin
fun greetUser() {
    println("Hello, Kotlin programmer!")
}

fun greetName(name: String) = println("Hello, $name!")

fun showTip(bill: Double, tipRate: Double) {
    val tip = bill * tipRate
    println("Tip: " + "%.2f".format(tip))
    println("Total: " + "%.2f".format(bill + tip))
}

fun main() {
    greetUser()
    greetUser()
    greetName("Avery")
    greetName("Riley")
    showTip(24.5, 0.15)

    val reference = ::showTip
    reference(100.0, 0.2)
}
```

### Expected Behavior or Output

The program prints:
```text
Hello, Kotlin programmer!
Hello, Kotlin programmer!
Hello, Avery!
Hello, Riley!
Tip: 3.68
Total: 28.18
Tip: 20.00
Total: 120.00
```

### Common Mistakes
1. Writing `greetUser` without parentheses and expecting the function to run.
2. Passing arguments in the wrong order, such as `showTip(0.15, 24.5)`.
3. Omitting a parameter's type, which is a compile error.

### Activities
1. Call `showTip(100.0, 0.2)` yourself and predict both lines.
2. Write `describeStudent(name: String, age: Int)` that prints one sentence.
3. Call `greetName()` with no argument and read the compiler message.
4. Explain the difference between a parameter and an argument.

### Accessibility Practice

Choose function names that read as actions when spoken, such as `showTip`. Print complete sentences from a function so the screen reader announces each call's result separately.

### Skills Checklist
- [ ] I can define and call a function.
- [ ] I can distinguish parameters from arguments.
- [ ] I can write an expression-bodied function.
- [ ] I can store a function in a variable.
- [ ] I can read a function signature aloud.

---

## Lesson 6.2: Default and Named Arguments

### Reading References
- [Functions: default and named arguments](https://kotlinlang.org/docs/functions.html#default-arguments)
- Matching Python lesson: Lesson 6.2: Passing Arguments

### Learning Objectives
- Give a parameter a default value.
- Call a function with named arguments.
- Mix positional and named arguments correctly.

### Concept Explanation

Kotlin supports *default values*, written in the parameter list: `fun calculateTotal(bill: Double, tipRate: Double = 0.15)`. A caller may leave out an argument that has a default. It also supports *named arguments*: `calculateTotal(tipRate = 0.10, bill = 24.5)`. Named arguments make a call read like a sentence and let you give them in any order.

You may mix the two: positional arguments first, then named ones. With the shared bill of 24.50, the total at the default rate 0.15 is 28.18, at 0.20 it is 29.40, and at 0.10 it is 26.95.

### Worked Example

```kotlin
fun calculateTotal(bill: Double, tipRate: Double = 0.15): Double = bill + bill * tipRate

fun main() {
    println("%.2f".format(calculateTotal(24.5)))
    println("%.2f".format(calculateTotal(24.5, 0.20)))
    println("%.2f".format(calculateTotal(tipRate = 0.10, bill = 24.5)))
    println("%.2f".format(calculateTotal(24.5, tipRate = 0.0)))
}
```

### Expected Behavior or Output

The program prints:
```text
28.18
29.40
26.95
24.50
```

### Common Mistakes
1. Putting a positional argument after a named one in a way the compiler cannot match.
2. Changing a default value and forgetting that every caller that omitted it now gets the new value.
3. Using a very long list of positional parameters instead of named arguments.

### Activities
1. Predict the four totals before running.
2. Add a `roundTotal: Boolean = false` parameter and use it.
3. Call the function with the arguments in a different order using names.
4. Explain why named arguments help a screen reader user.

### Accessibility Practice

Named arguments make a call read as a sentence: 'calculate total, bill equals 24.5, tip rate equals 0.10'. Say the equals signs aloud and check that your screen reader announces them.

### Skills Checklist
- [ ] I can write default values.
- [ ] I can call with named arguments.
- [ ] I can mix positional and named arguments.
- [ ] I know defaults apply to omitted arguments.
- [ ] I can read a named call aloud.

---

## Lesson 6.3: Return Values

### Reading References
- [Functions](https://kotlinlang.org/docs/functions.html)
- [Null safety](https://kotlinlang.org/docs/null-safety.html)
- Matching Python lesson: Lesson 6.3: Return Values

### Learning Objectives
- Return a computed value.
- Return a nullable result when a value may be missing.
- Return several values with a data class.

### Concept Explanation

A function sends a value back with `return`, or with `=` for a single expression. The return type follows the parameters: `fun average(scores: List<Int>): Double?`. A `?` after the type means the function may return `null`; that is the Kotlin way to say "no result", for example the average of an empty list.

The caller must deal with `null` before using the value, usually with a check or with `?:`. To return several values, return a `Pair` or a small data class and destructure it.

The example returns the average of the shared scores, classifies that average, returns a minimum and maximum together, and shows the empty-list case.

### Worked Example

```kotlin
data class ScoreRange(val low: Int, val high: Int)

fun average(scores: List<Int>): Double? {
    if (scores.isEmpty()) return null
    return scores.sum().toDouble() / scores.size
}

fun classify(score: Double): String = when {
    score >= 90 -> "A"
    score >= 80 -> "B"
    score >= 70 -> "C"
    score >= 60 -> "D"
    else -> "F"
}

fun minMax(scores: List<Int>) = ScoreRange(scores.min(), scores.max())

fun main() {
    val scores = listOf(82, 91, 76, 88)
    val avg = average(scores)
    println("Average: $avg")
    if (avg != null) {
        println("Grade for the average: ${classify(avg)}")
    }
    val (low, high) = minMax(scores)
    println("Lowest and highest: $low and $high")
    println(average(emptyList()))
}
```

### Expected Behavior or Output

The program prints:
```text
Average: 84.25
Grade for the average: B
Lowest and highest: 76 and 91
null
```

### Common Mistakes
1. Printing inside the function and then trying to use the result in a calculation.
2. Ignoring the `null` case and crashing with `!!`.
3. Writing code after a `return` in the same block. It never runs.

### Activities
1. Predict the four printed lines before running.
2. Write `total(list: List<Int>)` that returns the sum.
3. Write `isPassing(score: Int)` that returns a `Boolean`.
4. Explain how a caller should use a function that returns `Double?`.

### Accessibility Practice

Return values instead of printing inside logic functions, so the caller prints once and the screen reader announces each result a single time.

### Skills Checklist
- [ ] I can return a value.
- [ ] I can return a nullable result.
- [ ] I can return several values with a data class.
- [ ] I can use a returned value in a calculation.
- [ ] I can classify an average with the shared thresholds.

---

## Lesson 6.4: Functions with Collections

### Reading References
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- [Functions](https://kotlinlang.org/docs/functions.html)
- Matching Python lesson: Lesson 6.4: Functions with Lists and Dictionaries

### Learning Objectives
- Explain that a collection argument refers to the same object.
- Change a list in a function and protect the original with a copy or a new list.
- Process the shared inventory with a function.

### Concept Explanation

A `List` or `MutableList` passed to a function is a *reference* to the same object. A function that takes a `MutableList` can change the caller's list; a function that takes a read-only `List` cannot change it through that parameter. Numbers and strings are copied or immutable, so they cannot be changed this way.

To produce a changed list without touching the original, return a *new* list: `scoreList + newScore` builds one. Choose the parameter type to say what the function does: `MutableList<Int>` means "I will change this", `List<Int>` means "I will only read this".

The shared inventory is Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25), worth 17.50 in total.

### Worked Example

```kotlin
data class Item(val name: String, val quantity: Int, val unitPrice: Double)

fun addScore(scoreList: MutableList<Int>, newScore: Int) {
    scoreList.add(newScore)
}

fun withScore(scoreList: List<Int>, newScore: Int): List<Int> = scoreList + newScore

fun inventoryValue(inventory: List<Item>): Double =
    inventory.sumOf { it.quantity * it.unitPrice }

fun main() {
    val scores = mutableListOf(82, 91, 76, 88)
    addScore(scores, 95)
    println(scores)

    val longer = withScore(scores, 100)
    println("${scores.size} ${longer.size}")

    val inventory = listOf(
        Item("Notebook", 3, 2.50),
        Item("Pencil", 10, 0.50),
        Item("Folder", 4, 1.25),
    )
    println("Total inventory value: " + "%.2f".format(inventoryValue(inventory)))
}
```

### Expected Behavior or Output

The program prints:
```text
[82, 91, 76, 88, 95]
5 6
Total inventory value: 17.50
```

### Common Mistakes
1. Expecting a function to receive its own copy of a list.
2. Changing a list inside a function that was meant only to read it.
3. Declaring a parameter `MutableList` when `List` is enough, which allows accidental changes.

### Activities
1. Predict the three printed lines before running.
2. Write `scalePrices(inventory, factor)` that returns a new list with changed prices and leaves the original unchanged.
3. Write a version that changes a `MutableList<Item>` in place and compare the two designs.
4. Explain the difference between passing a number and passing a list.

### Accessibility Practice

State aloud before each call whether the function changes its argument, and name it accordingly (`addScore` changes, `withScore` returns a new list). Print the list before and after so that the effect is heard.

### Skills Checklist
- [ ] I know collections are passed by reference.
- [ ] I can change a list in a function.
- [ ] I can return a new list instead.
- [ ] I can choose `List` or `MutableList` for a parameter.
- [ ] I can total the shared inventory in a function.

---

## Lesson 6.5: Variable Numbers of Arguments

### Reading References
- [Functions: variable number of arguments](https://kotlinlang.org/docs/functions.html#variable-number-of-arguments-varargs)
- Matching Python lesson: Lesson 6.5: Arbitrary Number of Arguments

### Learning Objectives
- Write a function with `vararg`.
- Pass an existing array with the spread operator `*`.
- Handle the case of no arguments.

### Concept Explanation

A parameter marked `vararg` accepts any number of arguments, and inside the function it is an array: `vararg scores: Int` is an `IntArray`. Pass an existing array with the *spread operator*: `average(*list.toIntArray())`. A list must be converted to an array first.

Handle the case of zero arguments explicitly. Dividing a sum by a size of 0 would give a meaningless result, so the example returns `null`.

The shared scores 82, 91, 76, 88 average 84.25, and the average of 90 and 80 is 85.0.

### Worked Example

```kotlin
fun average(vararg scores: Int): Double? =
    if (scores.isEmpty()) null else scores.sum().toDouble() / scores.size

fun describe(label: String, vararg values: Int): String =
    "$label: ${values.joinToString(", ")}"

fun main() {
    println(average(82, 91, 76, 88))
    println(average(90, 80))
    println(average())

    val list = listOf(82, 91, 76, 88)
    println(average(*list.toIntArray()))

    println(describe("scores", 82, 91, 76, 88))
    println(describe("nothing"))
}
```

### Expected Behavior or Output

The program prints:
```text
84.25
85.0
null
84.25
scores: 82, 91, 76, 88
nothing: 
```

### Common Mistakes
1. Calling `average()` with no arguments and dividing by zero.
2. Passing a list directly to a `vararg` parameter instead of spreading an array.
3. Placing `vararg` before other parameters and then needing named arguments for the rest.

### Activities
1. Predict each printed line.
2. Write `maximum(vararg numbers: Int)` that returns the largest or `null`.
3. Write `joinWords(separator: String, vararg words: String)`.
4. Explain what the `*` does in a call.

### Accessibility Practice

Read variadic signatures aloud: 'fun average, open parenthesis, vararg scores colon Int, close parenthesis'. Check that your screen reader announces `vararg` and the star.

### Skills Checklist
- [ ] I can write a `vararg` function.
- [ ] I can use the spread operator.
- [ ] I handle the no-argument case.
- [ ] I know `vararg` is an array inside the function.
- [ ] I can convert a list with `toIntArray()`.

---
