# Unit 9: Testing and Data Analysis

## Overview

Write tests with expected results, test random code by its properties, analyze the shared text sample, and read the shared CSV file.

---


## Lesson 9.1: Testing Functions

### Reading References
- [Functions](https://kotlinlang.org/docs/functions.html)
- [Functions](https://kotlinlang.org/docs/functions.html)
- Matching Python lesson: Lesson 9.1: Testing Your Code

### Learning Objectives
- Write checks with chosen inputs and expected results.
- Compare decimals with a tolerance.
- Test boundary values and report failure with an exit status.

### Concept Explanation

A *test* runs code with chosen inputs and compares the result with a value decided in advance. Real Kotlin projects use the `kotlin.test` library with JUnit, added through Gradle. To keep this course free of build tooling, the example uses a tiny `check` function; the habits (inputs, expected values, boundaries) are the same.

Decimal results are compared with a *tolerance*, not `==`, because of floating-point approximation: the tip for 24.50 at 0.15 is stored as 3.6749999999999998, so the test checks that it is within a tiny distance of 3.675.

The same tests appear in every language track: `add(5, 3)` is 8, `add(-5, -3)` is -8, `add(10, -4)` is 6, the tip is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F.

`exitProcess(1)` ends the program with a failure status when any check fails, so other tools can notice.

### Worked Example

```kotlin
import kotlin.math.abs
import kotlin.system.exitProcess

fun add(a: Int, b: Int) = a + b

fun calculateTip(bill: Double, rate: Double) = bill * rate

fun classify(score: Int): String = when {
    score >= 90 -> "A"
    score >= 80 -> "B"
    score >= 70 -> "C"
    score >= 60 -> "D"
    else -> "F"
}

var passed = 0
var failed = 0

fun <T> check(name: String, actual: T, expected: T) {
    if (actual == expected) {
        passed++
        println("PASS $name")
    } else {
        failed++
        println("FAIL $name: expected $expected but got $actual")
    }
}

fun checkClose(name: String, actual: Double, expected: Double, tolerance: Double = 1e-9) {
    check(name, abs(actual - expected) <= tolerance, true)
}

fun main() {
    check("add 5 and 3", add(5, 3), 8)
    check("add -5 and -3", add(-5, -3), -8)
    check("add 10 and -4", add(10, -4), 6)
    checkClose("tip on 24.50 at 0.15", calculateTip(24.5, 0.15), 3.675)
    check("tip on a zero bill", calculateTip(0.0, 0.15), 0.0)
    check("classify 90", classify(90), "A")
    check("classify 89", classify(89), "B")
    check("classify 60", classify(60), "D")
    check("classify 59", classify(59), "F")

    println("$passed passed, $failed failed")
    if (failed > 0) exitProcess(1)
}
```

### Expected Behavior or Output

The program prints:
```text
PASS add 5 and 3
PASS add -5 and -3
PASS add 10 and -4
PASS tip on 24.50 at 0.15
PASS tip on a zero bill
PASS classify 90
PASS classify 89
PASS classify 60
PASS classify 59
9 passed, 0 failed
```

### Common Mistakes
1. Comparing decimal results with `==`.
2. Testing only typical values and skipping the boundaries 90, 89, 60, and 59.
3. Writing the expected value after seeing the output, which turns the test into a copy of the bug.

### Activities
1. Change one expected value so a check fails, read the message, and restore it.
2. Add checks for the grades at 80, 79, 70, and 69.
3. Write checks for `isPassing(score)` before writing the function.
4. Explain why the tip check uses a tolerance.

### Accessibility Practice

Each check prints one complete line that starts with PASS or FAIL, and the last line gives the counts, so the result can be understood from the first word of each line and the final summary.

### Skills Checklist
- [ ] I can write a check with an expected value.
- [ ] I can compare decimals with a tolerance.
- [ ] I can choose boundary tests.
- [ ] I can read PASS and FAIL lines.
- [ ] I know how to signal failure with an exit status.

---

## Lesson 9.2: Testing Classes

### Reading References
- [Classes](https://kotlinlang.org/docs/classes.html)
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 9.2: Testing a Class

### Learning Objectives
- Create a fresh object for every test.
- Test a value, a change of state, and an error.
- Use `runCatching` to test that an error occurs.

### Concept Explanation

Each test should start from a known state, so create a new object for every test with a *setup* function. Tests that share an object can affect each other and fail in confusing ways.

Test three kinds of behavior: that a function returns the right value (`totalValue` for 3 at 2.50 is 7.5), that a function changes the object correctly (restocking 2 makes the quantity 5), and that invalid use is rejected (restocking a negative amount throws).

`runCatching { ... }.isFailure` is true when the block throws, so a test can assert that an error *does* happen.

### Worked Example

```kotlin
import kotlin.math.abs

class Item(val name: String, var quantity: Int, val unitPrice: Double) {
    fun totalValue(): Double = quantity * unitPrice

    fun restock(amount: Int) {
        require(amount >= 0) { "amount must not be negative" }
        quantity += amount
    }
}

fun setup() = Item("Notebook", 3, 2.50)

var failures = 0

fun test(name: String, body: () -> Unit) {
    val result = runCatching(body)
    if (result.isSuccess) {
        println("PASS $name")
    } else {
        failures++
        println("FAIL $name: ${result.exceptionOrNull()?.message}")
    }
}

fun assertThat(condition: Boolean, message: String) {
    if (!condition) throw AssertionError(message)
}

fun main() {
    test("total value is 7.5") {
        assertThat(abs(setup().totalValue() - 7.5) < 1e-9, "wrong total")
    }

    test("restock adds to the quantity") {
        val item = setup()
        item.restock(2)
        assertThat(item.quantity == 5, "quantity should be 5")
    }

    test("restock rejects a negative amount") {
        val failed = runCatching { setup().restock(-1) }.isFailure
        assertThat(failed, "an error should have been thrown")
    }

    println(if (failures == 0) "All tests passed." else "$failures test(s) failed.")
}
```

### Expected Behavior or Output

The program prints:
```text
PASS total value is 7.5
PASS restock adds to the quantity
PASS restock rejects a negative amount
All tests passed.
```

### Common Mistakes
1. Sharing one object between tests, so an earlier test changes the later ones.
2. Testing only the successful path and never the error path.
3. Writing an `assertThat` with no message, so a failure says nothing about what went wrong.

### Activities
1. Add a test that `restock(0)` leaves the quantity unchanged.
2. Add a test for an `isValid` function.
3. Break `restock` on purpose and read the failure line.
4. Explain why `setup` creates a new item each time.

### Accessibility Practice

Name each test as a short sentence that says what it checks, so the PASS and FAIL lines read as clear statements. Read the final summary line first.

### Skills Checklist
- [ ] I can create a fresh object per test.
- [ ] I can test a return value.
- [ ] I can test a change of state.
- [ ] I can test that an error is thrown.
- [ ] I can write a clear test name.

---

## Lesson 9.3: Random Numbers

### Reading References
- [Kotlin standard library: kotlin.random](https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.random/)
- Matching Python lesson: Lesson 9.3: Random Numbers and Simulation

### Learning Objectives
- Generate random integers and decimals.
- Use a seed to make results repeatable.
- Test random code by its properties.

### Concept Explanation

`kotlin.random.Random` produces random numbers. `Random.nextInt(from, until)` returns an integer from `from` up to but **not including** `until`, so a die roll is `nextInt(1, 7)`. `Random.nextDouble()` returns a decimal from 0.0 up to but not including 1.0, and `list.random(random)` picks a list element.

`Random(42)` creates a generator with a fixed *seed*: two generators with the same seed produce the same sequence. Without a seed the results change on every run. Because the exact sequence may differ between Kotlin versions, tests should check *properties* (every roll is between 1 and 6) and repeatability, not particular values.

### Worked Example

```kotlin
import kotlin.random.Random

fun main() {
    val first = Random(42)
    val second = Random(42)
    val firstRolls = List(5) { first.nextInt(1, 7) }
    val secondRolls = List(5) { second.nextInt(1, 7) }
    println("Same seed gives the same rolls: ${firstRolls == secondRolls}")

    val random = Random(7)
    val inRange = List(1000) { random.nextInt(1, 7) }.all { it in 1..6 }
    println("All rolls between 1 and 6: $inRange")

    val decimal = random.nextDouble()
    println("Decimal in [0, 1): ${decimal >= 0.0 && decimal < 1.0}")

    val scores = listOf(82, 91, 76, 88)
    val chosen = scores.random(random)
    println("Chosen score is from the list: ${chosen in scores}")
}
```

### Expected Behavior or Output

The program prints:
```text
Same seed gives the same rolls: true
All rolls between 1 and 6: true
Decimal in [0, 1): true
Chosen score is from the list: true
```

### Common Mistakes
1. Using `nextInt(1, 6)` for a die and never rolling a 6. The upper limit is excluded.
2. Testing for specific random values that may change between versions.
3. Creating a new unseeded generator for every roll, which wastes work and can repeat values.

### Activities
1. Run the program three times and compare.
2. Change the seeds and check that the property lines still print `true`.
3. Simulate 600 rolls and count how many of each face appeared (the counts will differ with the seed).
4. Explain why a test should check a property rather than a specific random number.

### Accessibility Practice

Print yes or no style results for random behavior, so the announced output is the same on every run and the screen reader does not read unpredictable values.

### Skills Checklist
- [ ] I can use `nextInt` with an excluded upper limit.
- [ ] I can set a seed.
- [ ] I can test properties of random code.
- [ ] I know sequences can differ between versions.
- [ ] I can pick a random list item.

---

## Lesson 9.4: Text Analysis

### Reading References
- [Strings](https://kotlinlang.org/docs/strings.html)
- [Grouping](https://kotlinlang.org/docs/collection-grouping.html)
- Matching Python lesson: Lesson 9.4: Data Analysis - Text Analysis

### Learning Objectives
- Split text into words and count them.
- Count word and letter frequencies with `groupingBy`.
- Produce stable, sorted output.

### Concept Explanation

Splitting uses `split`: `cleaned.split(" ")` or a regular expression such as `Regex("\\s+")` for any run of spaces. Counting is a one-liner with `groupingBy { it }.eachCount()`, which returns a map from each item to its count.

Map order is only stable if you make it so. `eachCount()` keeps the order in which items first appeared, and sorting with `sortedWith(compareBy({ -it.value }, { it.key }))` orders by count (highest first) and then alphabetically, so ties print in a fixed order.

The shared text sample is "A student studies programming. Programming develops problem-solving skills." After lower-casing and removing the periods it has 8 words, and `programming` appears twice.

### Worked Example

```kotlin
fun main() {
    val text = "A student studies programming. Programming develops problem-solving skills."
    val words = text.lowercase().replace(".", "").split(" ")

    println("Word count: ${words.size}")
    println("Word frequencies:")
    for ((word, count) in words.groupingBy { it }.eachCount()) {
        println("'$word': $count")
    }

    val letters = text.lowercase().filter { it.isLetter() }.groupingBy { it }.eachCount()
    val topThree = letters.entries.sortedWith(compareBy({ -it.value }, { it.key })).take(3)
    println("Most common letters:")
    for ((letter, count) in topThree) {
        println("$letter: $count")
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Word count: 8
Word frequencies:
'a': 1
'student': 1
'studies': 1
'programming': 2
'develops': 1
'problem-solving': 1
'skills': 1
Most common letters:
s: 7
e: 5
g: 5
```

### Common Mistakes
1. Counting punctuation as part of a word, so `programming.` and `programming` are different words.
2. Forgetting to lower-case first, so `Programming` and `programming` are counted separately.
3. Relying on map order for tied counts without a tie-break.

### Activities
1. Predict the word count and the count for `programming` before running.
2. Count the words longer than 8 letters.
3. Print the longest word.
4. Change the sort so ties are listed in reverse alphabetical order.

### Accessibility Practice

Read the frequency list in its fixed order. Because the order is stable, you can learn it and compare runs by ear. Print each pair as a short sentence with the same wording every time.

### Skills Checklist
- [ ] I can split text into words.
- [ ] I can count frequencies with `groupingBy`.
- [ ] I can sort with a tie-break.
- [ ] I can remove punctuation first.
- [ ] I can read a stable report.

---

## Lesson 9.5: Working with CSV Files

### Reading References
- [Kotlin standard library: kotlin.io](https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.io/)
- [Strings](https://kotlinlang.org/docs/strings.html)
- Matching Python lesson: Lesson 9.5: Data Analysis - CSV Files

### Learning Objectives
- Create and read a CSV file.
- Split lines into fields and convert numbers.
- Compute an average and a count.

### Concept Explanation

A CSV (comma-separated values) file stores a table as text. The first line names the columns and each later line is a record. The shared student file has the columns `student_id`, `first_name`, `last_name`, `score`, and `active`, and three records.

The standard library has no CSV reader. `line.split(",")` works only for **simple** files: a value that contains a comma inside quotation marks, such as `"Smith, Jr."`, would be split wrongly. For such files use a maintained library or write a real parser.

Every field is text. Convert the score with `toInt()` and compare `active` with the text `"true"`. With scores 91, 82, and 76 the average is 83.00, and two students are active.

### Worked Example

```kotlin
import java.io.File

fun main() {
    val file = File("students.csv")
    file.writeText(
        "student_id,first_name,last_name,score,active\n" +
            "1,Avery,Student,91,true\n" +
            "2,Jordan,Lee,82,true\n" +
            "3,Casey,Smith,76,false\n"
    )

    if (!file.exists()) {
        println("Error: students.csv was not found.")
        return
    }
    val lines = file.readLines()
    println("Columns: " + lines.first().split(",").joinToString(", "))

    var total = 0
    var active = 0
    val students = lines.drop(1)
    for (line in students) {
        val row = line.split(",")
        val score = row[3].toInt()
        total += score
        if (row[4] == "true") active++
        println("${row[0]}: ${row[1]} ${row[2]} scored $score")
    }

    println("Students: ${students.size}")
    println("Average score: " + "%.2f".format(total.toDouble() / students.size))
    println("Active students: $active")
}
```

### Expected Behavior or Output

The program prints:
```text
Columns: student_id, first_name, last_name, score, active
1: Avery Student scored 91
2: Jordan Lee scored 82
3: Casey Smith scored 76
Students: 3
Average score: 83.00
Active students: 2
```

### Common Mistakes
1. Splitting a CSV line at every comma when a value contains a quoted comma.
2. Forgetting to convert the text in the score column to a number.
3. Not skipping the header line, so `toInt()` fails on the text `score`.

### Activities
1. Predict the printed lines before running.
2. Add a fourth student and check the new average.
3. Print only the active students.
4. Explain, with an example, why `"Smith, Jr."` breaks `split(",")`.

### Accessibility Practice

Print one student per line with the same wording each time, so the screen reader announces a repeating pattern that is easy to compare. Read the column names aloud once at the start.

### Skills Checklist
- [ ] I can write and read a CSV file.
- [ ] I can split a line into fields.
- [ ] I convert text fields to numbers.
- [ ] I can compute an average and a count.
- [ ] I know when `split` is not enough.

---
