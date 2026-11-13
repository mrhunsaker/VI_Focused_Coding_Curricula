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
