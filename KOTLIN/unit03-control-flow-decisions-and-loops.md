# Unit 3: Control Flow — Decisions and Loops

## Overview

Make decisions, classify the shared scores with the shared grade thresholds, and learn collections, loops, and strings.

---


## Lesson 3.1: Boolean Expressions and if

### Reading References
- [Control flow](https://kotlinlang.org/docs/control-flow.html)
- Matching Python lesson: Lesson 3.1: Boolean Expressions and if Statements

### Learning Objectives
- Write comparisons and combine them with `&&`, `||`, and `!`.
- Use `if` as a statement and as an expression.
- Test a range with `in`.

### Concept Explanation

A *Boolean expression* is `true` or `false`. Comparisons use `==`, `!=`, `<`, `<=`, `>`, `>=`, and conditions combine with `&&` (and), `||` (or), and `!` (not). A condition must be a real `Boolean`: Kotlin never treats 0, an empty string, or `null` as false.

`if` can be a *statement* that chooses what to run, or an *expression* that produces a value: `val label = if (score >= 90) "high" else "not high"`. When `if` is used as an expression, `else` is required. `in 80..89` tests whether a value is inside a range, both ends included.

The shared score is 82. It passes (at least 60), it is in the 80 to 89 range, and it is not at least 90.

### Worked Example

```kotlin
fun main() {
    val score = 82

    if (score >= 60) {
        println("Avery passed.")
    } else {
        println("Avery did not pass.")
    }

    println(score >= 80 && score < 90)
    println(score < 60 || score > 100)
    println(!(score >= 90))
    println(score in 80..89)

    val label = if (score >= 90) "high" else "not high"
    println(label)
}
```

### Expected Behavior or Output

The program prints:
```text
Avery passed.
true
false
true
true
not high
```

### Common Mistakes
1. Writing `=` where `==` is meant, which does not compile as a condition.
2. Leaving out `else` when `if` is used as an expression.
3. Expecting a number or text to act as a condition. It must be a `Boolean`.

### Activities
1. Change the score to 59 and predict which lines change.
2. Write a condition that is true only for scores from 70 to 79 inclusive, in two ways.
3. Rewrite the `label` line as an `if` statement.
4. Explain why `if (score)` is not allowed in Kotlin.

### Accessibility Practice

Read each condition aloud with 'greater than or equal to', 'and', 'or', and 'not'. Check that your screen reader announces `&&` and `||` so you do not confuse them with single symbols.

### Skills Checklist
- [ ] I can write comparisons and combine them.
- [ ] I can write `if` and `else`.
- [ ] I can use `if` as an expression.
- [ ] I can test a range with `in`.
- [ ] I know conditions must be `Boolean`.

---

## Lesson 3.2: Chained Conditions with when

### Reading References
- [Control flow: when](https://kotlinlang.org/docs/control-flow.html#when-expression)
- Matching Python lesson: Lesson 3.2: Chained Conditionals (elif, else)

### Learning Objectives
- Use `when` to choose among several conditions.
- Classify the shared grade thresholds.
- Test boundary scores.

### Concept Explanation

Kotlin has no `elif`. Use `else if` for a short chain, or `when`, which tests conditions from top to bottom and runs the first branch that is true. `when` without an argument takes a Boolean condition for each branch, and it is an *expression* when you use its value; then an `else` branch is required.

The shared grade thresholds are 90 or more for A, 80 or more for B, 70 or more for C, 60 or more for D, and anything lower for F. Because branches are tested in order, each later test needs only a lower bound.

*Boundary scores* sit exactly on or just below a threshold. The scores 90, 89, 80, 79, 70, 69, 60, and 59 check every boundary.

### Worked Example

```kotlin
fun classify(score: Int): String = when {
    score >= 90 -> "A"
    score >= 80 -> "B"
    score >= 70 -> "C"
    score >= 60 -> "D"
    else -> "F"
}

fun main() {
    for (score in listOf(90, 89, 80, 79, 70, 69, 60, 59)) {
        println("$score ${classify(score)}")
    }
}
```

### Expected Behavior or Output

The program prints:
```text
90 A
89 B
80 B
79 C
70 C
69 D
60 D
59 F
```

### Common Mistakes
1. Putting the branches in the wrong order, such as testing `score >= 60` first so every passing score is a D.
2. Using `>` instead of `>=`, so exactly 90 receives a B.
3. Forgetting the `else` branch in a `when` expression, which does not compile.

### Activities
1. Trace the score 82 through each branch and say which one runs.
2. Add the scores 100 and 0 to the list and predict their grades.
3. Reorder the branches so `score >= 60` is first, run it, and explain the wrong output.
4. Write `isPassing(score)` that returns a `Boolean` using `when`.

### Accessibility Practice

Read the eight output lines in order. Each is a number, a space, and a letter, so they are easy to follow by ear and in braille.

### Skills Checklist
- [ ] I can write a `when` chain.
- [ ] I know branch order matters.
- [ ] I can classify with the shared thresholds.
- [ ] I can choose boundary tests.
- [ ] I know a `when` expression needs `else`.

---

## Lesson 3.3: Lists

### Reading References
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- [List-specific operations](https://kotlinlang.org/docs/list-operations.html)
- Matching Python lesson: Lesson 3.3: Introduction to Lists

### Learning Objectives
- Create read-only and mutable lists.
- Index from 0 and use `size`, `last()`, and `getOrNull`.
- Explain the difference between a read-only view and a copy.

### Concept Explanation

`listOf(...)` creates a **read-only** list and `mutableListOf(...)` creates a list you can change. Indexes start at 0, so `scores[0]` is the first item, `scores.last()` is the last, and `scores.size` is the length. Reading outside the list with `[]` throws an `IndexOutOfBoundsException`; `getOrNull(index)` returns `null` instead.

*Read-only* is a property of the **type**, not of the data. A `List<Int>` variable cannot change the list, but if it refers to the same list as a `MutableList<Int>`, the other reference can still change it. To protect a list, make a copy with `toList()`.

The shared list is 82, 91, 76, 88. Python uses the same 0-based indexes.

### Worked Example

```kotlin
fun main() {
    val scores = mutableListOf(82, 91, 76, 88)
    println(scores[0])
    println(scores.last())
    println(scores.size)

    scores[2] = 80
    println(scores)

    val readOnlyView: List<Int> = scores
    val copy = scores.toList()
    scores[0] = 100
    println("view: ${readOnlyView[0]}, copy: ${copy[0]}")
    println(scores.getOrNull(10))
}
```

### Expected Behavior or Output

The program prints:
```text
82
88
4
[82, 91, 80, 88]
view: 100, copy: 82
null
```

### Common Mistakes
1. Using index 1 for the first item. The first item is at index 0.
2. Using `[10]` on a short list and crashing instead of using `getOrNull`.
3. Assuming a `List` variable guarantees the data cannot change.

### Activities
1. Predict each of the seven outputs before running.
2. Replace the second score with 95 and print the list.
3. Make a copy of the list and show that changing the original does not change the copy.
4. Explain, in two sentences, why `List` is called read-only rather than immutable.

### Accessibility Practice

Print a whole list on one line and its size on another, so the screen reader announces a complete state in one pass. When reading `scores[0]` aloud, say 'scores, open bracket, zero, close bracket'.

### Skills Checklist
- [ ] I can create `List` and `MutableList` values.
- [ ] I can index from 0.
- [ ] I can use `getOrNull`.
- [ ] I can make a copy with `toList()`.
- [ ] I can explain read-only versus immutable.

---

## Lesson 3.4: Loops

### Reading References
- [Control flow: for loops](https://kotlinlang.org/docs/control-flow.html#for-loops)
- Matching Python lesson: Lesson 3.4: Iterating with for Loops

### Learning Objectives
- Use `for` with ranges, `until`, `downTo`, and `step`.
- Visit a list by value and with its index.
- Compute the total and average of the shared scores.

### Concept Explanation

`for (x in collection)` visits every element. A range `1..3` includes both ends, `1 until 3` excludes the end, `10 downTo 1` counts down, and `step 3` skips values: `for (i in 10 downTo 1 step 3)`. `withIndex()` gives each element with its position: `for ((index, value) in scores.withIndex())`.

The standard library can do common work without a loop: `sum()` adds a list of numbers and `average()` returns the mean as a `Double`. A loop is still the way to learn what those functions do.

The shared scores 82, 91, 76, 88 total 337 and average 84.25.

### Worked Example

```kotlin
fun main() {
    val scores = listOf(82, 91, 76, 88)
    var total = 0
    for ((index, score) in scores.withIndex()) {
        println("Adding score ${index + 1}: $score")
        total += score
    }
    println("Total: $total")
    println("Average: ${total.toDouble() / scores.size}")
    println("Same results: ${scores.sum()} and ${scores.average()}")

    for (i in 1..3) println("Count: $i")
    for (i in 1 until 3) println("Until: $i")
    for (i in 10 downTo 1 step 3) println("Step: $i")
}
```

### Expected Behavior or Output

The program prints:
```text
Adding score 1: 82
Adding score 2: 91
Adding score 3: 76
Adding score 4: 88
Total: 337
Average: 84.25
Same results: 337 and 84.25
Count: 1
Count: 2
Count: 3
Until: 1
Until: 2
Step: 10
Step: 7
Step: 4
Step: 1
```

### Common Mistakes
1. Using `1..scores.size` as indexes, which reads one position past the end of a 0-based list.
2. Forgetting that `..` includes the end while `until` excludes it.
3. Dividing the `Int` total by the size and getting a truncated result.

### Activities
1. Predict the last seven output lines before running.
2. Change the loop to print only the scores above 80.
3. Write a loop that counts from 20 down to 0 by 5.
4. Explain why `scores.average()` prints `84.25` and not `84`.

### Accessibility Practice

Each output line starts with a label and a number, so the running total is read step by step. Count the lines to confirm that the loop ran four times.

### Skills Checklist
- [ ] I can use ranges, `until`, `downTo`, and `step`.
- [ ] I can visit a list with its index.
- [ ] I can total and average a list.
- [ ] I know `..` includes its end.
- [ ] I can use `sum()` and `average()`.

---

## Lesson 3.5: Strings

### Reading References
- [Strings](https://kotlinlang.org/docs/strings.html)
- [Basic types](https://kotlinlang.org/docs/basic-types.html)
- Matching Python lesson: Lesson 3.5: Basic String Operations

### Learning Objectives
- Use `length`, `lowercase`, `contains`, `indexOf`, and `trim`.
- Normalize a name and search the shared text sample.
- Explain that strings are immutable.

### Concept Explanation

A Kotlin `String` is an immutable sequence of characters. `length` is its size, and `text[0]` is the first character. Functions such as `lowercase()` and `uppercase()` return a **new** string; they never change the original.

Useful functions: `trim()`, `contains(text)`, `indexOf(text)` (which returns `-1` when the text is missing), `replace`, `startsWith`, and `replaceFirstChar { it.uppercase() }` to capitalize. `Regex("programming").findAll(text).count()` counts non-overlapping matches.

The shared text sample is "A student studies programming. Programming develops problem-solving skills." It has 75 characters and contains `programming` twice (once in each case), found at index 18 after lowercasing.

### Worked Example

```kotlin
fun main() {
    val rawName = "  avery  "
    val cleanName = rawName.trim().replaceFirstChar { it.uppercase() }
    println("Name: '$cleanName'")

    val text = "A student studies programming. Programming develops problem-solving skills."
    val lowered = text.lowercase()
    println("Characters: ${text.length}")
    println("Contains 'programming': ${lowered.contains("programming")}")
    println("First index of 'programming': ${lowered.indexOf("programming")}")
    println("Times 'programming' appears: ${Regex("programming").findAll(lowered).count()}")
    println("Missing word index: ${lowered.indexOf("kotlin")}")
    println(text.uppercase().take(9))
}
```

### Expected Behavior or Output

The program prints:
```text
Name: 'Avery'
Characters: 75
Contains 'programming': true
First index of 'programming': 18
Times 'programming' appears: 2
Missing word index: -1
A STUDENT
```

### Common Mistakes
1. Expecting `text.uppercase()` to change `text`. Assign or print the result.
2. Treating `indexOf` as an error when it returns `-1`.
3. Counting positions from 1. The first character is at index 0.

### Activities
1. Predict the printed values, then run and compare.
2. Find the index of the word `student` in the sample text.
3. Replace every `programming` with `coding` and print the result.
4. Write code that trims and capitalizes `"  riley  "`.

### Accessibility Practice

Strings with many quotation marks are hard to read by ear. Say 'single quote' and 'double quote' aloud when checking a line, and print results inside labelled sentences so values are not run together.

### Skills Checklist
- [ ] I can use common `String` functions.
- [ ] I can search text and find positions.
- [ ] I can trim and capitalize a name.
- [ ] I know strings are immutable.
- [ ] I can count matches with `Regex`.

---
