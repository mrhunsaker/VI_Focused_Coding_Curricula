# Unit 2: Numeric Computations

## Overview

Plan and build the tip calculator, learn the language's numeric operators and conversions, read typed input safely, and use the math library.

---


## Lesson 2.1: The Software Development Process

### Reading References
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- [Basic types](https://kotlinlang.org/docs/basic-types.html)
- Matching Python lesson: Lesson 2.1: The Software Development Process

### Learning Objectives
- Describe the design, implement, and test cycle.
- Write pseudocode for the tip calculator and implement it.
- Explain why money is formatted to two decimals.

### Concept Explanation

Software is built in a cycle: understand the problem, design a solution, implement it, test it, and refine it. Design comes first. For the tip calculator the plan is: get the bill, calculate 15 percent of it as the tip, add the tip to the bill for the total, and print the tip and the total.

With the shared values (bill 24.50, tip rate 0.15) the exact tip is 3.675 and the total is 28.175. `"%.2f".format(x)` formats a number with two decimals. On the JVM, formatting rounds half up using the decimal digits of the `Double`, so Kotlin and Java display the tip as **3.68**; Python, C, Go, and several other languages display 3.67 for the same stored number. Both are correct displays of the same value.

Formatting uses the default *locale*. In a locale that writes decimals with a comma, `"%.2f".format(x)` prints a comma. Pass `java.util.Locale.US` as the first argument for fixed output.

### Worked Example

```kotlin
fun main() {
    val bill = 24.5
    val tipRate = 0.15

    val tip = bill * tipRate
    val total = bill + tip

    println("Bill: " + "%.2f".format(bill))
    println("Tip: " + "%.2f".format(tip))
    println("Total: " + "%.2f".format(total))
    println("Tip with an explicit locale: " + "%.2f".format(java.util.Locale.US, tip))
    println("Unformatted tip: $tip")
}
```

### Expected Behavior or Output

The program prints:
```text
Bill: 24.50
Tip: 3.68
Total: 28.18
Tip with an explicit locale: 3.68
Unformatted tip: 3.675
```

### Common Mistakes
1. Writing the rate as 15 instead of 0.15, which makes the tip fifteen times too large.
2. Rounding the tip first and then adding it, which can change the total by a cent.
3. Assuming every language prints the same two-decimal text for 3.675.

### Activities
1. Trace the plan with the shared values and write each result as a sentence.
2. Change the rate to 0.20 and predict the tip and total (4.90 and 29.40).
3. Add a test for a bill of 100 with a written expected result before running.
4. Explain in two sentences why the program prints 3.68 even though the stored value is just below 3.675.

### Accessibility Practice

Print each result on its own labelled line (`Tip: 3.68`) so a screen reader announces one clear unit per line. Never use alignment or spacing to carry meaning.

### Skills Checklist
- [ ] I can name the stages of the development cycle.
- [ ] I can write pseudocode for a calculation.
- [ ] I can format a number with `format`.
- [ ] I know formatting depends on the locale.
- [ ] I can explain why displays can differ between languages.

---

## Lesson 2.2: Expressions and Assignment

### Reading References
- [Basic types](https://kotlinlang.org/docs/basic-types.html)
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Matching Python lesson: Lesson 2.2: Elements of Programs - Expressions and Assignment

### Learning Objectives
- Evaluate expressions using operator precedence.
- Use integer division, remainder, and compound assignment.
- Join strings with templates and `+`.

### Concept Explanation

An *expression* produces a value. The arithmetic operators are `+`, `-`, `*`, `/`, and `%` (remainder). Multiplication, division, and remainder happen before addition and subtraction, and parentheses change the order, so `8 + 4 * 2` is 16 and `(8 + 4) * 2` is 24.

**Division depends on the types.** Two `Int` values give an `Int`, so `7 / 2` is `3`. If either side is a `Double`, the result is a `Double`, so `7 / 2.0` is `3.5`. The remainder `7 % 2` is `1`.

*Assignment* stores a value: `score = score + 9`, shortened to `score += 9`. Only a `var` can be assigned again. Comparison uses `==`, `!=`, `<`, `<=`, `>`, and `>=`. In Kotlin `==` compares values, not identities.

Kotlin does not convert numbers automatically: you cannot add an `Int` variable to a `Long` variable without a conversion. This catches mistakes at compile time.

### Worked Example

```kotlin
fun main() {
    println(8 + 4 * 2)
    println((8 + 4) * 2)

    var score = 82
    score += 9
    println("New score: $score")

    println(7 / 2)
    println(7 / 2.0)
    println(7 % 2)
    println(-7 / 2)
    println(5 != 6)
    println("Avery" + " " + "Student")
}
```

### Expected Behavior or Output

The program prints:
```text
16
24
New score: 91
3
3.5
1
-3
true
Avery Student
```

### Common Mistakes
1. Expecting `7 / 2` to be `3.5`. With two `Int` values the fraction is dropped.
2. Reassigning a `val`, which is a compile error.
3. Writing `score =+ 9` and storing positive nine instead of adding.

### Activities
1. Predict the ten output lines before running, then compare.
2. Write an expression for the area and the perimeter of a 12 by 8 rectangle.
3. Explain why `-7 / 2` prints `-3` rather than `-4`.
4. Join your name, a space, and your age into one string in two different ways.

### Accessibility Practice

Say operators by name when reading code aloud ('slash', 'percent', 'plus equals'). Raise your punctuation level while checking expressions so that parentheses and operators are all announced.

### Skills Checklist
- [ ] I can apply operator precedence.
- [ ] I can predict `Int` and `Double` division.
- [ ] I can use `+=` and `%`.
- [ ] I know only `var` can be reassigned.
- [ ] I can join strings.

---

## Lesson 2.3: Console Input and Output

### Reading References
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- [Null safety](https://kotlinlang.org/docs/null-safety.html)
- Matching Python lesson: Lesson 2.3: Input and Output Revisited

### Learning Objectives
- Read a line with `readlnOrNull`.
- Convert text with `toIntOrNull`.
- Handle missing and invalid input.

### Concept Explanation

`readlnOrNull()` reads one line from standard input and returns a `String?`: the text without the line ending, or `null` at the end of input. `readln()` is similar but throws an exception at the end of input, so this course prefers `readlnOrNull()`.

Typed text is always a string. `toIntOrNull()` returns an `Int?`: the number, or `null` when the text is not a valid whole number. The safe-call operator `?.` stops a chain at `null`, so `readlnOrNull()?.trim()?.toIntOrNull()` reads, trims, and converts, and gives `null` if any step has nothing to work on.

After a null check on a `val`, Kotlin treats the value as non-null: this is a *smart cast*. The example reads a name and two numbers and prints a greeting and their sum. With Avery, 12, and 8 the sum is 20. Prompts are printed on their own lines so the screen reader reads each cleanly.

### Worked Example

```kotlin
fun main() {
    println("Enter your name:")
    val name = readlnOrNull()
    println("Enter the first number:")
    val first = readlnOrNull()?.trim()?.toIntOrNull()
    println("Enter the second number:")
    val second = readlnOrNull()?.trim()?.toIntOrNull()

    if (name != null && first != null && second != null) {
        println("Hello, $name!")
        println("The sum of $first and $second is ${first + second}.")
    } else {
        println("Input was missing or not a number.")
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
Avery
12
8
```

the program prints:
```text
Enter your name:
Enter the first number:
Enter the second number:
Hello, Avery!
The sum of 12 and 8 is 20.
```

With no standard input at all, the program ends cleanly and prints:
```text
Enter your name:
Enter the first number:
Enter the second number:
Input was missing or not a number.
```

### Common Mistakes
1. Using `readln()` and crashing at the end of input.
2. Doing arithmetic on a `String` read from input without converting it.
3. Using `!!` to silence the null check, which crashes on exactly the input the program should handle.

### Activities
1. Run with Avery, 12, and 8 and confirm the output.
2. Type `twelve` for the first number and explain the result.
3. Run with no input and describe the output.
4. Change the program to subtract the second number from the first.

### Accessibility Practice

Every prompt is a complete sentence on its own line and every result is a complete sentence. When you test, listen for whether the prompt is read in full before you begin to type.

### Skills Checklist
- [ ] I can read a line with `readlnOrNull`.
- [ ] I can convert text with `toIntOrNull`.
- [ ] I understand `String?` and `?.`.
- [ ] I can write clear prompts.
- [ ] I handle missing and invalid input.

---

## Lesson 2.4: Numbers and Type Conversions

### Reading References
- [Basic types](https://kotlinlang.org/docs/basic-types.html)
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Matching Python lesson: Lesson 2.4: Computing with Numbers and Type Conversions

### Learning Objectives
- Convert explicitly between numbers and text.
- Explain truncation and rounding.
- Explain why decimal arithmetic is approximate.

### Concept Explanation

Kotlin never converts numeric types for you. Use the conversion functions: `toInt()`, `toLong()`, `toDouble()`, and `toString()`. `"16".toInt()` converts text and throws an exception if the text is invalid, so for typed input prefer `toIntOrNull()` and `toDoubleOrNull()`, which return `null` instead.

`toInt()` on a `Double` **truncates** toward zero: `3.9.toInt()` is `3`. To round, use `kotlin.math.roundToInt()`, which rounds halves up: `3.5.roundToInt()` is `4`.

A `Double` is a binary approximation. `0.1 + 0.2` is `0.30000000000000004`, not `0.3`; this is correct behavior. Compare decimals with a tolerance and format them for display.

The shared student has age 16 and height 1.72 meters; the example converts text to those values and computes the height in centimeters.

### Worked Example

```kotlin
import kotlin.math.roundToInt

fun main() {
    val age = "16".toInt()
    val height = "1.72".toDouble()
    println("$age ${age::class.simpleName}")
    println("$height ${height::class.simpleName}")

    println("abc".toIntOrNull())
    println("".toIntOrNull())
    println(42.toString() + " is now text")

    println(3.9.toInt())
    println(3.5.roundToInt())
    println(0.1 + 0.2)

    val heightCm = height * 100
    println("Height in centimeters: " + "%.1f".format(heightCm))
}
```

### Expected Behavior or Output

The program prints:
```text
16 Int
1.72 Double
null
null
42 is now text
3
4
0.30000000000000004
Height in centimeters: 172.0
```

### Common Mistakes
1. Using `toInt()` on untrusted text and crashing with `NumberFormatException`.
2. Expecting `toInt()` to round. It truncates.
3. Comparing decimals with `==` after arithmetic.

### Activities
1. Predict each of the ten lines before running, then compare.
2. Check what `" 16 ".toIntOrNull()` and `"1e3".toDoubleOrNull()` return and explain each.
3. Write code that reads a line and prints a clear message when the conversion fails.
4. Explain the difference between `3.5.toInt()` and `3.5.roundToInt()`.

### Accessibility Practice

Format floating-point results so that the screen reader reads short numbers. Read the type names aloud and note that `Int` and `Double` are announced as words, not symbols.

### Skills Checklist
- [ ] I can convert between text and numbers.
- [ ] I know `toInt()` truncates.
- [ ] I can use `roundToInt()`.
- [ ] I can use `toIntOrNull()`.
- [ ] I can explain why decimals are approximate.

---

## Lesson 2.5: Using the Math Library

### Reading References
- [Basic types](https://kotlinlang.org/docs/basic-types.html)
- [Kotlin standard library: kotlin.math](https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.math/)
- Matching Python lesson: Lesson 2.5: Using the Math Library

### Learning Objectives
- Use `PI`, `sqrt`, `pow`, and `hypot` from `kotlin.math`.
- Compute circle area and circumference.
- Compute the distance from the origin.

### Concept Explanation

The `kotlin.math` package supplies `PI`, `sqrt`, `abs`, `max`, `min`, `floor`, `ceil`, `hypot`, and the `pow` extension function. Import what you use: `import kotlin.math.PI`, or `import kotlin.math.*` for everything.

For a circle of radius 5 the area is `PI * radius.pow(2)` (about 78.54) and the circumference is `2 * PI * radius` (about 31.42). Kotlin has a built-in hypotenuse function, so the distance from the origin to the shared point (3, 4) is `hypot(3.0, 4.0)`, which is 5.0.

The math functions take `Double` values. `sqrt(81.0)` returns `9.0`, a `Double`, so it prints with a decimal point.

### Worked Example

```kotlin
import kotlin.math.PI
import kotlin.math.abs
import kotlin.math.hypot
import kotlin.math.max
import kotlin.math.min
import kotlin.math.pow
import kotlin.math.sqrt

fun main() {
    val radius = 5.0
    val area = PI * radius.pow(2)
    val circumference = 2 * PI * radius
    println("Area: " + "%.2f".format(area))
    println("Circumference: " + "%.2f".format(circumference))

    println(sqrt(81.0))
    println("Distance from origin: " + "%.2f".format(hypot(3.0, 4.0)))
    println("${max(82, 91)} ${min(76, 88)} ${abs(-5)}")
}
```

### Expected Behavior or Output

The program prints:
```text
Area: 78.54
Circumference: 31.42
9.0
Distance from origin: 5.00
91 76 5
```

### Common Mistakes
1. Forgetting the import, so `sqrt` is an unresolved reference.
2. Passing an `Int` to `sqrt`, which needs a `Double`.
3. Writing the area as `PI * radius * 2`; the radius must be squared.

### Activities
1. Predict each printed line and then run the program.
2. Compute the area for radius 2.5 by hand and with the program.
3. Change the point to (6, 8) and predict the distance before running.
4. Print the larger of two shared scores using `max`.

### Accessibility Practice

Round results with `format` so that the screen reader announces `78.54` rather than fifteen digits. Say 'dot' aloud in `kotlin.math` and `radius.pow`.

### Skills Checklist
- [ ] I can import and use `kotlin.math`.
- [ ] I can compute circle area and circumference.
- [ ] I can compute distance with `hypot`.
- [ ] I can format results to two decimals.
- [ ] I know math functions take `Double`.

---

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

# Unit 4: Data Structures — Lists and Dictionaries

## Overview

Work with lists, sorting, fixed records, dictionaries, and stable traversal of the shared inventory.

---


## Lesson 4.1: More on Mutable Lists

### Reading References
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- [Adding and removing elements](https://kotlinlang.org/docs/collection-write.html)
- Matching Python lesson: Lesson 4.1: More on Lists

### Learning Objectives
- Add, insert, replace, and remove list items.
- Remove by value and by position without confusing them.
- Search a list with `in` and `indexOf`.

### Concept Explanation

A `MutableList` changes with `add(value)` (append), `add(index, value)` (insert and shift), `set` or `list[i] = value` (replace), `remove(value)` (remove the first matching **value**), and `removeAt(index)` (remove by **position**). For a list of `Int`, `remove(76)` removes the number 76, while `removeAt(76)` would try to remove position 76. `removeAt` returns the removed item.

`value in list` tests membership, and `indexOf(value)` returns the position or `-1`. These searches look at each item in turn, so they take longer for longer lists.

Avoid `removeLast()` in code that must run on several JDK versions: newer JDKs add a method with the same name to `List`, and the behavior depends on the JDK. `removeAt(lastIndex)` is portable.

The example applies the same operations as the Python course to the shared scores, from [82, 91, 76, 88] to [82, 85, 93, 88].

### Worked Example

```kotlin
fun main() {
    val scores = mutableListOf(82, 91, 76, 88)

    scores.add(95)
    scores.add(1, 85)
    scores[2] = 93
    scores.remove(76)
    val last = scores.removeAt(scores.lastIndex)

    println(scores)
    println("${scores.size} items; removed $last")
    println(88 in scores)
    println(scores.indexOf(88))
    println(scores.indexOf(100))
}
```

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
1. Confusing `remove(76)` (by value) with `removeAt(76)` (by position).
2. Removing items inside a `for` loop over the same list, which throws `ConcurrentModificationException`.
3. Calling `removeLast()` and getting different behavior on different JDKs.

### Activities
1. Trace the list after every operation and write each version as a sentence.
2. Remove the first score with `removeAt(0)` and describe what happens to the others.
3. Remove every score below 80 safely, using `removeAll { ... }`.
4. Print the position of the first score above 90 with `indexOfFirst`.

### Accessibility Practice

After every change, print the whole list on one line so the screen reader reads a complete state in one pass. Say the method names aloud, and notice how `remove` and `removeAt` sound different.

### Skills Checklist
- [ ] I can add, insert, replace, and remove items.
- [ ] I can tell `remove` from `removeAt`.
- [ ] I can search with `in` and `indexOf`.
- [ ] I know why `removeLast()` is avoided.
- [ ] I can show a list in one line.

---

## Lesson 4.2: Sorting and Organizing Lists

### Reading References
- [Ordering](https://kotlinlang.org/docs/collection-ordering.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 4.2: Organizing Lists

### Learning Objectives
- Sort a list ascending and descending.
- Tell `sorted()` (a new list) from `sort()` (in place).
- Sort by a computed key.

### Concept Explanation

Kotlin offers two families. **Returning** functions leave the original alone and give a new list: `sorted()`, `sortedDescending()`, `sortedBy { ... }`, and `reversed()`. **In-place** functions change a `MutableList`: `sort()`, `sortDescending()`, and `reverse()`. A read-only `List` has only the returning kind.

`sortedBy { it.length }` sorts by a computed key, here the length of each word, and keeps the original order of items with equal keys because the sort is *stable*.

The shared scores sort to 76, 82, 88, 91 in ascending order and 91, 88, 82, 76 in descending order.

### Worked Example

```kotlin
fun main() {
    val scores = mutableListOf(82, 91, 76, 88)

    println("Original: $scores")
    println("Ascending: ${scores.sorted()}")
    println("Descending: ${scores.sortedDescending()}")
    println("Still original: $scores")

    scores.sort()
    println("Sorted in place: $scores")
    scores.reverse()
    println("Reversed in place: $scores")

    val words = listOf("pencil", "folder", "notebook")
    println(words.sorted())
    println(words.sortedBy { it.length })
}
```

### Expected Behavior or Output

The program prints:
```text
Original: [82, 91, 76, 88]
Ascending: [76, 82, 88, 91]
Descending: [91, 88, 82, 76]
Still original: [82, 91, 76, 88]
Sorted in place: [76, 82, 88, 91]
Reversed in place: [91, 88, 82, 76]
[folder, notebook, pencil]
[pencil, folder, notebook]
```

### Common Mistakes
1. Expecting `sorted()` to change the list. It returns a new list.
2. Calling `sort()` on a read-only `List`, which does not compile.
3. Expecting `reverse()` to sort. It only flips the current order.

### Activities
1. Predict each printed line before running.
2. Print the scores in descending order without changing the original.
3. Sort the words by their last letter with `sortedBy`.
4. Explain the difference between `sorted()` and `sort()` in two sentences.

### Accessibility Practice

Print each result on its own labelled line (`Ascending:`, `Descending:`). The first and last numbers are the quickest to check by ear.

### Skills Checklist
- [ ] I can sort ascending and descending.
- [ ] I know which functions change the list.
- [ ] I can use `sortedBy`.
- [ ] I can reverse a list.
- [ ] I can keep the original order.

---

## Lesson 4.3: Pairs, Triples, and Data Classes

### Reading References
- [Data classes](https://kotlinlang.org/docs/data-classes.html)
- [Destructuring declarations](https://kotlinlang.org/docs/destructuring-declarations.html)
- Matching Python lesson: Lesson 4.3: Tuples - Immutable Lists

### Learning Objectives
- Use `Pair` and `Triple` for small fixed groups.
- Declare a data class with `val` properties.
- Unpack values with destructuring.

### Concept Explanation

Kotlin has no general tuple type. For two or three values, use `Pair(a, b)` and `Triple(a, b, c)`, whose parts are `first`, `second`, and `third`. For anything you will use more than briefly, a **data class** with named properties is clearer: `data class Point(val x: Int, val y: Int)`.

A data class automatically provides `toString()`, `equals()` (so two points with the same values are equal), `copy()` (a new object with some values changed), and *destructuring*: `val (x, y) = point`. With `val` properties, the object cannot change after it is created, so use `copy(y = 10)` to get a changed version.

The shared coordinates are x = 3 and y = 4.

### Worked Example

```kotlin
data class Point(val x: Int, val y: Int)

fun minMax(values: List<Int>): Pair<Int, Int> = Pair(values.min(), values.max())

fun main() {
    val (x, y) = Pair(3, 4)
    println("x=$x y=$y")

    val point = Point(3, 4)
    println(point)
    val moved = point.copy(y = 10)
    println("$point -> $moved")
    println(point == Point(3, 4))

    val (low, high) = minMax(listOf(82, 91, 76, 88))
    println("low=$low high=$high")

    val profile = Triple("Avery", 16, 1.72)
    println("${profile.first} ${profile.second} ${profile.third}")
}
```

### Expected Behavior or Output

The program prints:
```text
x=3 y=4
Point(x=3, y=4)
Point(x=3, y=4) -> Point(x=3, y=10)
true
low=76 high=91
Avery 16 1.72
```

### Common Mistakes
1. Using `var` properties in a data class and then being surprised when values change.
2. Expecting `copy()` to change the original. It returns a new object.
3. Using `Pair` with unclear meanings (`first`, `second`) in code that others must read.

### Activities
1. Predict the output, then run.
2. Create a `Student` data class for the shared profile and print it.
3. Use `copy` to make a student one year older and print both.
4. Explain when a data class is a better choice than a `Pair`.

### Accessibility Practice

Named properties read better aloud than `first` and `second`. Printing a data class shows its name and every property, so the screen reader announces `Point(x=3, y=4)` as a complete sentence.

### Skills Checklist
- [ ] I can use `Pair` and `Triple`.
- [ ] I can declare a data class.
- [ ] I can destructure values.
- [ ] I can use `copy()`.
- [ ] I can choose between a pair and a data class.

---

## Lesson 4.4: Maps

### Reading References
- [Map-specific operations](https://kotlinlang.org/docs/map-operations.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 4.4: Introducing Dictionaries

### Learning Objectives
- Create a map and read, add, change, and remove entries.
- Handle a missing key with `?:`.
- Model the shared inventory item with a data class.

### Concept Explanation

A `Map` pairs keys with values. `mapOf(...)` is read-only and `mutableMapOf(...)` can change. Read with `map[key]`, which returns a **nullable** value: it is `null` when the key is missing. Combine it with the Elvis operator to supply a default: `map[key] ?: "unknown"`.

`map[key] = value` adds or replaces an entry, `remove(key)` deletes one, `containsKey(key)` tests for a key, and `size` counts the entries. `mutableMapOf` keeps insertion order.

A map with values of different types, such as `MutableMap<String, Any>`, is flexible but loses type checking. When the fields are known, a data class is safer, so the shared Notebook item is a data class.

### Worked Example

```kotlin
data class Item(val name: String, var quantity: Int, val unitPrice: Double)

fun main() {
    val profile = mutableMapOf<String, Any>(
        "name" to "Avery",
        "age" to 16,
        "heightM" to 1.72,
        "favoriteSubject" to "Computer Science",
    )
    println(profile["name"])
    profile["age"] = 17
    profile["gradeLevel"] = 11
    profile.remove("heightM")
    println(profile)
    println(profile["heightM"])
    println(profile["heightM"] ?: "unknown")
    println(profile.containsKey("gradeLevel"))

    val item = Item("Notebook", 3, 2.50)
    item.quantity += 2
    println(item)
    println("Stock value: ${item.quantity * item.unitPrice}")
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
Item(name=Notebook, quantity=5, unitPrice=2.5)
Stock value: 12.5
```

### Common Mistakes
1. Using a missing key and expecting an error. The result is `null`.
2. Using `!!` on a map lookup, which crashes when the key is missing.
3. Storing mixed types in `Map<String, Any>` and then needing casts everywhere.

### Activities
1. Predict the printed lines before running.
2. Add a `discount` key to the item as a data class property and print the discounted value.
3. Remove `favoriteSubject` and show what the lookup returns.
4. Explain why a data class is safer than `Map<String, Any>` for a record.

### Accessibility Practice

Print one entry per line when you need to read a map, because a one-line `{a=1, b=2}` is hard to navigate. Choose key names that read well aloud, such as `unitPrice`.

### Skills Checklist
- [ ] I can create and change a map.
- [ ] I know a lookup returns a nullable value.
- [ ] I can supply a default with `?:`.
- [ ] I can model an item with a data class.
- [ ] I can test for a key.

---

## Lesson 4.5: Traversing Maps

### Reading References
- [Map-specific operations](https://kotlinlang.org/docs/map-operations.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 4.5: Looping Through Dictionaries

### Learning Objectives
- Visit keys, values, and key-value pairs.
- Explain which maps keep insertion order.
- Produce sorted output and total the shared inventory.

### Concept Explanation

`for (key in map.keys)` visits keys, `for (value in map.values)` visits values, and `for ((key, value) in map)` visits pairs with destructuring.

Order matters for readable output. `mutableMapOf`, `linkedMapOf`, and `mapOf` keep **insertion order**, so output is stable. `hashMapOf` makes no promise about order. To list keys alphabetically, use `toSortedMap()`.

`sumOf { ... }` adds a computed number for every element, which is the compact way to total the shared inventory: Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25) are worth 7.50 + 5.00 + 5.00 = 17.50.

### Worked Example

```kotlin
data class Stock(val quantity: Int, val unitPrice: Double)

fun main() {
    val inventory = linkedMapOf(
        "Notebook" to Stock(3, 2.50),
        "Pencil" to Stock(10, 0.50),
        "Folder" to Stock(4, 1.25),
    )

    println("Keys:")
    for (name in inventory.keys) println(name)

    println("Quantities:")
    for (stock in inventory.values) println(stock.quantity)

    var totalValue = 0.0
    for ((name, stock) in inventory) {
        val lineValue = stock.quantity * stock.unitPrice
        println("$name: ${stock.quantity} in stock, value ${"%.2f".format(lineValue)}")
        totalValue += lineValue
    }
    println("Total inventory value: ${"%.2f".format(totalValue)}")

    println(inventory.toSortedMap().keys)
    println(inventory.values.sumOf { it.quantity * it.unitPrice })
}
```

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
2. Adding or removing entries while looping over the map, which throws `ConcurrentModificationException`.
3. Forgetting the parentheses in `for ((name, stock) in inventory)` and iterating over entries without unpacking them.

### Activities
1. Run the example and write the three key-value lines in order.
2. Print only the items with a quantity below 5.
3. Print the items from the highest line value to the lowest.
4. Explain how `toSortedMap()` differs from the default order.

### Accessibility Practice

Printing each inventory line as one sentence lets the screen reader announce the name, quantity, and value together. Because the order is stable, you can learn it and compare runs by ear.

### Skills Checklist
- [ ] I can visit keys, values, and pairs.
- [ ] I know which maps keep insertion order.
- [ ] I can sort keys.
- [ ] I can total with `sumOf`.
- [ ] I can total the shared inventory.

---
