# Unit 5: User Input and while Loops

## Overview

Read and validate input, write sentinel and flag loops, skip entries, and prevent endless loops.

---


## Lesson 5.1: How Console Input Works

### Reading References
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- [Null safety](https://kotlinlang.org/docs/null-safety.html)
- Matching Python lesson: Lesson 5.1: How the input() Function Works

### Learning Objectives
- Read a line and recognize it as text.
- Convert it safely and handle failure.
- Handle the end of input.

### Concept Explanation

`readlnOrNull()` returns the next line as a `String?`, or `null` when the input has ended. It never returns a number: typed digits are text until you convert them. `toIntOrNull()` returns an `Int?`, and a `null` result means the text was not a whole number.

A program that reads input must plan for three cases: a valid value, an invalid value, and no value at all. The example reads an age and then a second value, so you can see the valid, invalid, and missing cases. With the typed value 16 the age five years later is 21; the second value, `abc`, is rejected.

### Worked Example

```kotlin
fun main() {
    println("How old are you?")
    val text = readlnOrNull()
    println("Read: ${if (text == null) "nothing" else text::class.simpleName}")

    val age = text?.trim()?.toIntOrNull()
    if (age != null) {
        println("In 5 years: ${age + 5}")
    } else {
        println("That was not a whole number.")
    }

    println("Enter another value:")
    val second = readlnOrNull()?.trim()?.toIntOrNull()
    if (second != null) {
        println("Number: $second")
    } else {
        println("Not a number; toIntOrNull returned null.")
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
16
abc
```

the program prints:
```text
How old are you?
Read: String
In 5 years: 21
Enter another value:
Not a number; toIntOrNull returned null.
```

With no standard input at all, the program ends cleanly and prints:
```text
How old are you?
Read: nothing
That was not a whole number.
Enter another value:
Not a number; toIntOrNull returned null.
```

### Common Mistakes
1. Adding to the text without converting it, which does not compile or gives joined text.
2. Using `toInt()` on user input and crashing on `abc`.
3. Forgetting that an empty answer is not a number, so `toIntOrNull()` is `null`.

### Activities
1. Run with 16 and then `abc` and compare with the shown output.
2. Run with no input and explain every line printed.
3. Accept an age only from 0 to 120.
4. Rewrite the program using `readln()` and describe what happens at the end of input.

### Accessibility Practice

Each prompt is a complete sentence on its own line. Run the program twice, once typing and once with piped input, and compare what your screen reader announces.

### Skills Checklist
- [ ] I can read a line of input.
- [ ] I can convert and validate it.
- [ ] I handle `null` at the end of input.
- [ ] I know typed input is text.
- [ ] I can write a clear prompt.

---

## Lesson 5.2: The while Loop in Action

### Reading References
- [Control flow: while loops](https://kotlinlang.org/docs/control-flow.html#while-loops)
- Matching Python lesson: Lesson 5.2: The while Loop in Action

### Learning Objectives
- Write a counting `while` loop.
- Write a sentinel loop that ends on a command.
- Stop at the end of input.

### Concept Explanation

`while (condition) { ... }` repeats while the condition is true, testing **before** each pass. A loop needs a way to make its condition false, normally by changing a variable inside the body: `count++` adds one.

A *sentinel* is a special input that tells the loop to stop. Here it is the word `quit`. The standard pattern reads once before the loop and again at the end of each pass, and tests for `null` as well, so the loop ends when input runs out even without `quit`.

The example counts from 1 to 5, then repeats a message prompt until the user types `quit`.

### Worked Example

```kotlin
fun main() {
    var count = 1
    while (count <= 5) {
        println(count)
        count++
    }
    println("Counting finished!")

    println("Enter a message, or type quit to exit:")
    var message = readlnOrNull()
    while (message != null && message != "quit") {
        println("You said: $message")
        println("Enter a message, or type quit to exit:")
        message = readlnOrNull()
    }
    println("Goodbye!")
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
hello
scores
quit
```

the program prints:
```text
1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit:
You said: hello
Enter a message, or type quit to exit:
You said: scores
Enter a message, or type quit to exit:
Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit:
Goodbye!
```

### Common Mistakes
1. Forgetting to change the loop variable, which creates an endless loop.
2. Testing for `quit` but not for `null`, so the loop reads forever after input ends.
3. Reading input only before the loop and never again inside it.

### Activities
1. Predict the output for the typed lines hello, scores, and quit.
2. Change the sentinel to `exit` and update the prompt.
3. Count the messages entered and print the count at the end.
4. Rewrite the counting loop with `for (count in 1..5)` and compare.

### Accessibility Practice

Each prompt is on its own line and each response begins with `You said:`, so the conversation can be followed in order by ear. If a loop floods the screen reader, stop it with Ctrl+C.

### Skills Checklist
- [ ] I can write a counting `while` loop.
- [ ] I can write a sentinel loop.
- [ ] I test for `null` as well as the sentinel.
- [ ] I update the loop variable.
- [ ] I can compare `while` with `for`.

---

## Lesson 5.3: Flags, break, and Labels

### Reading References
- [Returns and jumps](https://kotlinlang.org/docs/returns.html)
- Matching Python lesson: Lesson 5.3: Using Flags and break to Exit Loops

### Learning Objectives
- Control a loop with a Boolean flag.
- Leave a loop with `break` and an outer loop with a label.
- Search a list and remember the position.

### Concept Explanation

A *flag* is a Boolean variable that controls a loop: the loop runs while `running` is true, and the body sets it to `false` to stop. `break` leaves the nearest enclosing loop at once.

A search keeps its answer in a variable (here `-1` means "not found"), sets it when the item is found, and uses `break`. After the loop, the variable says whether a match was found. List positions start at 0.

A *label* lets `break` leave an outer loop from inside an inner one: write `outer@ for (...)` and `break@outer`.

The shared scores 82, 91, 76, 88 have their first score of 90 or higher at index 1, with the value 91.

### Worked Example

```kotlin
fun main() {
    var running = true
    var handled = 0
    while (running) {
        println("Say something, or type quit to stop:")
        val message = readlnOrNull()
        if (message == null || message == "quit") {
            running = false
        } else {
            handled++
            println("You said: $message")
        }
    }
    println("Messages handled: $handled")

    val scores = listOf(82, 91, 76, 88)
    var foundIndex = -1
    for ((index, score) in scores.withIndex()) {
        if (score >= 90) {
            foundIndex = index
            break
        }
    }
    if (foundIndex >= 0) {
        println("First score of 90 or higher: ${scores[foundIndex]} at index $foundIndex")
    } else {
        println("No score of 90 or higher.")
    }

    outer@ for (row in 1..3) {
        for (col in 1..3) {
            if (row * col == 4) {
                println("Stopped at row $row, column $col")
                break@outer
            }
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
hello
quit
ignored
```

the program prints:
```text
Say something, or type quit to stop:
You said: hello
Say something, or type quit to stop:
Messages handled: 1
First score of 90 or higher: 91 at index 1
Stopped at row 2, column 2
```

With no standard input at all, the program ends cleanly and prints:
```text
Say something, or type quit to stop:
Messages handled: 0
First score of 90 or higher: 91 at index 1
Stopped at row 2, column 2
```

### Common Mistakes
1. Setting the flag but running more code in the same pass that should be skipped.
2. Forgetting to give the result variable a starting value, then misreading it after the loop.
3. Using `break` in an inner loop and expecting it to leave the outer loop.

### Activities
1. Run with hello and quit and confirm the count is 1.
2. Change the search to the first score below 80 and predict the index.
3. Rewrite the first loop without a flag, using `break`.
4. Explain in two sentences when a flag is clearer than `break`.

### Accessibility Practice

Report search results as complete sentences that include both the value and its position. Remember that Kotlin indexes start at 0, and say 'index 1' aloud to avoid confusing it with 'the first'.

### Skills Checklist
- [ ] I can control a loop with a flag.
- [ ] I can use `break`.
- [ ] I can use a label to leave an outer loop.
- [ ] I can search a list and keep the position.
- [ ] I can explain flag versus `break`.

---

## Lesson 5.4: Skipping Entries with continue

### Reading References
- [Returns and jumps](https://kotlinlang.org/docs/returns.html)
- Matching Python lesson: Lesson 5.4: Using continue in Loops

### Learning Objectives
- Skip one pass of a loop with `continue`.
- Skip invalid scores in a list.
- Compare `continue` with `filter`.

### Concept Explanation

`continue` skips the rest of the current pass and goes straight to the next one. It is useful for ignoring invalid entries while still reporting them. In a `while` loop, make sure that the loop variable is updated *before* `continue`, or the loop never ends.

Kotlin also lets you filter first: `rawScores.filter { it in 0..100 }` builds a list of the valid scores, which is shorter when you do not need to report each skipped entry.

The example skips the invalid scores -5 and 105 in the list 82, -5, 91, 105, 76, 88. The four valid scores total 337.

### Worked Example

```kotlin
fun main() {
    val rawScores = listOf(82, -5, 91, 105, 76, 88)
    var validTotal = 0
    var validCount = 0

    for (raw in rawScores) {
        if (raw < 0 || raw > 100) {
            println("Skipping invalid score: $raw")
            continue
        }
        validTotal += raw
        validCount++
    }
    println("Valid scores: $validCount, total: $validTotal")

    for (number in 1..9) {
        if (number % 2 == 0) continue
        println(number)
    }

    println(rawScores.filter { it in 0..100 }.sum())
}
```

### Expected Behavior or Output

The program prints:
```text
Skipping invalid score: -5
Skipping invalid score: 105
Valid scores: 4, total: 337
1
3
5
7
9
337
```

### Common Mistakes
1. Putting statements that must always run after `continue`, so they are skipped.
2. Using `continue` in a `while` loop before updating the counter, which creates an endless loop.
3. Confusing `continue` (skip this pass) with `break` (leave the loop).

### Activities
1. Predict the printed lines and the final total.
2. Skip scores below 80 instead.
3. Rewrite the first loop with an `if`/`else` and no `continue`.
4. Rewrite it with `filter` and explain what you no longer report.

### Accessibility Practice

Print a line for each skipped entry, so the screen reader announces what was ignored. Never skip silently when a user needs to know what happened to their data.

### Skills Checklist
- [ ] I can use `continue`.
- [ ] I can skip invalid entries.
- [ ] I know where the counter must be updated.
- [ ] I can use `filter` as an alternative.
- [ ] I can tell `continue` from `break`.

---

## Lesson 5.5: Avoiding Infinite Loops

### Reading References
- [Control flow: do-while](https://kotlinlang.org/docs/control-flow.html#while-loops)
- Matching Python lesson: Lesson 5.5: Avoiding Infinite Loops

### Learning Objectives
- Identify what makes a loop stop.
- Add an attempt limit and handle the end of input.
- Use `do ... while`.

### Concept Explanation

An *infinite loop* never ends because its condition never becomes false. Common causes are forgetting to change the loop variable, testing the wrong variable, and waiting for input that never arrives. In a terminal, stop a running program with Ctrl+C.

Protect every loop with a *progress rule* and a *limit*: count attempts, and stop when the limit is reached or the input ends.

`do { ... } while (condition)` runs the body first and tests afterward, so it always runs at least once. A variable declared inside the body is visible in the `while` condition.

The example allows three attempts to enter a score from 0 to 100. With the typed lines abc, 105, and 88, the first two are rejected and the third is accepted.

### Worked Example

```kotlin
fun main() {
    val maxAttempts = 3
    var attempts = 0
    var score: Int? = null

    while (attempts < maxAttempts && score == null) {
        attempts++
        println("Enter a score from 0 to 100 (attempt $attempts of $maxAttempts):")
        val text = readlnOrNull()
        if (text == null) {
            println("No more input.")
            break
        }
        val number = text.trim().toIntOrNull()
        if (number != null && number in 0..100) {
            score = number
        } else {
            println("Invalid score: $text")
        }
    }

    if (score != null) {
        println("Accepted score: $score")
    } else {
        println("No valid score was entered.")
    }

    var count = 1
    do {
        println(count)
        count++
    } while (count <= 3)
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
abc
105
88
```

the program prints:
```text
Enter a score from 0 to 100 (attempt 1 of 3):
Invalid score: abc
Enter a score from 0 to 100 (attempt 2 of 3):
Invalid score: 105
Enter a score from 0 to 100 (attempt 3 of 3):
Accepted score: 88
1
2
3
```

With no standard input at all, the program ends cleanly and prints:
```text
Enter a score from 0 to 100 (attempt 1 of 3):
No more input.
No valid score was entered.
1
2
3
```

### Common Mistakes
1. Forgetting to increase `attempts`, so the limit is never reached.
2. Not handling `null` from `readlnOrNull()`, so the loop never ends or crashes when input closes.
3. Writing `while (count < 3)` after a `do` body and stopping one pass early.

### Activities
1. Run with abc, 105, and 88 and confirm the accepted score.
2. Run with three invalid lines and read the final message.
3. Change the limit to 5 and test it.
4. For each loop in the example, write down what makes it stop.

### Accessibility Practice

A loop that cannot be stopped is an accessibility problem, because it can flood a screen reader with output. Learn Ctrl+C before running loops, give every input loop a limit, and write error messages that say what is valid.

### Skills Checklist
- [ ] I can name what ends each loop.
- [ ] I can add an attempt limit.
- [ ] I handle the end of input.
- [ ] I can use `do ... while`.
- [ ] I know how to interrupt a program.

---

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

# Unit 7: Classes and Object-Oriented Programming

## Overview

Model the shared inventory item as an object: constructors, methods, inheritance, and composition.

---


## Lesson 7.1: Why Learn About Classes?

### Reading References
- [Classes](https://kotlinlang.org/docs/classes.html)
- [Visibility modifiers](https://kotlinlang.org/docs/visibility-modifiers.html)
- Matching Python lesson: Lesson 7.1: Why Learn About Classes?

### Learning Objectives
- Explain a class as data plus behavior.
- Hide a property's setter to protect it.
- Describe encapsulation.

### Concept Explanation

A *class* describes what a kind of thing knows (its *properties*) and what it can do (its *functions*). An *object* is one actual thing made from a class. Bundling data with the functions that work on it is called **encapsulation**. The shared example is an inventory *item* with a name, a quantity, and a unit price.

Kotlin lets you protect a property with a *private setter*: `var quantity: Int = quantity` followed by `private set` on the next line means code outside the class can read `quantity` but cannot assign to it. Changes must go through a function such as `restock`, which can check them.

Kotlin does not have a `new` keyword: you create an object by calling the class like a function, `Item("Notebook", 3, 2.50)`.

A Notebook with quantity 3 and unit price 2.50 is worth 7.50. Restocking 2 raises that to 12.50, and a negative restock is refused.

### Worked Example

```kotlin
class Item(val name: String, quantity: Int, val unitPrice: Double) {
    var quantity: Int = quantity
        private set

    fun restock(amount: Int): Boolean {
        if (amount < 0) return false
        quantity += amount
        return true
    }

    fun totalValue(): Double = quantity * unitPrice

    fun describe() {
        println("$name: $quantity at ${"%.2f".format(unitPrice)} each, value ${"%.2f".format(totalValue())}")
    }
}

fun main() {
    val notebook = Item("Notebook", 3, 2.50)
    notebook.describe()
    println(notebook.restock(2))
    notebook.describe()
    println(notebook.restock(-1))
    println(notebook.quantity)
    // notebook.quantity = 99   // would not compile: the setter is private
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
true
Notebook: 5 at 2.50 each, value 12.50
false
5
```

### Common Mistakes
1. Treating a class as one single thing. A class is a blueprint; each call such as `Item(...)` makes a separate object.
2. Making every property public and changeable, so outside code can put the object into an invalid state.
3. Looking for a `new` keyword, which Kotlin does not have.

### Activities
1. Predict the five printed lines before running.
2. Add a function `isLowStock()` that returns true when the quantity is below 5.
3. Uncomment the assignment, read the compiler message, and restore the comment.
4. Explain what encapsulation means and why a private setter helps.

### Accessibility Practice

Describe a class as a list read in order: the name, then each property, then each function. Reading a class aloud works best by saying 'class Item, open parenthesis, val name colon String...' and listening for the braces that show structure.

### Skills Checklist
- [ ] I can explain data plus behavior.
- [ ] I can use a private setter.
- [ ] I can create an object without `new`.
- [ ] I can describe encapsulation.
- [ ] I can read a class definition aloud.

---

## Lesson 7.2: Creating Classes and Objects

### Reading References
- [Classes](https://kotlinlang.org/docs/classes.html)
- [Exceptions: require](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 7.2: Creating and Using a Class

### Learning Objectives
- Declare a class with a primary constructor.
- Validate in an `init` block with `require`.
- Create several objects with the same properties.

### Concept Explanation

A class declares its constructor right after its name: `class Item(val name: String, val quantity: Int, val unitPrice: Double)`. Writing `val` or `var` in front of a constructor parameter makes it a property in one step.

An `init` block runs whenever an object is created, so it is the place to check the values. `require(condition) { message }` throws an `IllegalArgumentException` with the message when the condition is false. An object that cannot be created invalid never needs to be checked again.

The example creates the three shared inventory items. Each has the same properties with different values. A class is a blueprint and each object is one *instance*.

### Worked Example

```kotlin
class Item(val name: String, val quantity: Int, val unitPrice: Double) {
    init {
        require(quantity >= 0) { "quantity must not be negative" }
        require(unitPrice >= 0.0) { "unit price must not be negative" }
    }
}

fun main() {
    val notebook = Item("Notebook", 3, 2.50)
    val pencil = Item("Pencil", 10, 0.50)
    val folder = Item("Folder", 4, 1.25)

    for (item in listOf(notebook, pencil, folder)) {
        println("${item.name}: ${item.quantity} at ${"%.2f".format(item.unitPrice)}")
    }

    val attempt = runCatching { Item("Broken", -1, 1.0) }
    println(attempt.exceptionOrNull()?.message)
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50
Pencil: 10 at 0.50
Folder: 4 at 1.25
quantity must not be negative
```

### Common Mistakes
1. Forgetting `val` in the constructor, so the parameter is not a property and cannot be read later.
2. Validating in each caller instead of once in `init`.
3. Catching the `IllegalArgumentException` and ignoring it, so the program continues with no object.

### Activities
1. Create a fourth item with your own values and print it.
2. Add a rule that the name must not be blank.
3. Create two items with the same name and different quantities and show that they are separate objects.
4. Explain what `init` does and when it runs.

### Accessibility Practice

Say the constructor aloud in order and check that the closing parenthesis and brace match. Print each object on its own line with its name so the output can be matched to the objects by ear.

### Skills Checklist
- [ ] I can write a primary constructor.
- [ ] I can validate with `init` and `require`.
- [ ] I can create several objects.
- [ ] I know what an instance is.
- [ ] I can read a class header aloud.

---

## Lesson 7.3: Properties and Functions

### Reading References
- [Properties](https://kotlinlang.org/docs/properties.html)
- [Classes](https://kotlinlang.org/docs/classes.html)
- Matching Python lesson: Lesson 7.3: Working with Attributes and Methods

### Learning Objectives
- Define a computed property and member functions.
- Change properties directly and through functions.
- Validate in a function.

### Concept Explanation

A *property* can be stored (`var quantity`) or *computed*: `val totalValue: Double get() = quantity * unitPrice` has no stored value and is calculated each time it is read. Callers use it like any property, without parentheses.

A *member function* works on the object: `item.restock(2)`. A function that validates its input protects the object from invalid data. Directly changing a public `var` skips that protection, so make a property `var` only when any value is acceptable.

The example adds a computed value, a validity check, a restock function, and a describe function to the shared Notebook.

### Worked Example

```kotlin
class Item(val name: String, var quantity: Int, val unitPrice: Double) {
    val totalValue: Double
        get() = quantity * unitPrice

    fun isValid(): Boolean = name.isNotBlank() && quantity >= 0 && unitPrice >= 0.0

    fun restock(amount: Int) {
        if (amount < 0) {
            println("Cannot restock a negative amount.")
            return
        }
        quantity += amount
    }

    fun describe() {
        println("$name: $quantity at ${"%.2f".format(unitPrice)} each, value ${"%.2f".format(totalValue)}")
    }
}

fun main() {
    val notebook = Item("Notebook", 3, 2.50)
    notebook.describe()
    notebook.restock(2)
    notebook.describe()
    notebook.quantity = 4
    notebook.describe()
    notebook.restock(-1)
    println(notebook.isValid())
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
Notebook: 5 at 2.50 each, value 12.50
Notebook: 4 at 2.50 each, value 10.00
Cannot restock a negative amount.
true
```

### Common Mistakes
1. Writing `totalValue()` with parentheses for a property, or `isValid` without them for a function.
2. Changing a public `var` directly and skipping the validation that a function would perform.
3. Storing a value that can be computed, so it goes out of date when the inputs change.

### Activities
1. Predict the output of all six calls before running.
2. Add a function `discounted(rate: Double): Double` that returns the value after a discount without changing the item.
3. Make `quantity` have a private setter and see which lines stop compiling.
4. Explain the difference between a stored and a computed property.

### Accessibility Practice

Name functions after actions (`restock`, `describe`) so a call reads as a sentence. Print one line per call, so the screen reader announces the effect of each step in order.

### Skills Checklist
- [ ] I can write a computed property.
- [ ] I can write member functions.
- [ ] I can validate in a function.
- [ ] I know when to use a private setter.
- [ ] I can tell a property from a function when reading.

---

## Lesson 7.4: Inheritance

### Reading References
- [Inheritance](https://kotlinlang.org/docs/inheritance.html)
- Matching Python lesson: Lesson 7.4: Inheritance

### Learning Objectives
- Declare an `open` class and a subclass.
- Override a function and call the parent's version.
- Explain polymorphism.

### Concept Explanation

Kotlin classes are **final by default**: nothing can inherit from them. Mark a class `open` to allow subclasses, and mark each function that may be replaced `open` as well. A subclass names its parent after a colon and passes constructor values up: `class DiscountedItem(...) : Item(name, quantity, unitPrice)`. A function that replaces a parent's function is marked `override`, and `super.totalValue()` calls the parent's version.

*Polymorphism* means that the same function name behaves differently for different classes. Here `describe`, written once in `Item`, calls `totalValue()`, so a `DiscountedItem` prints its discounted value automatically.

The example discounts the shared Folder (4 at 1.25) by 20 percent, so its value is 4.00 instead of 5.00.

### Worked Example

```kotlin
open class Item(val name: String, val quantity: Int, val unitPrice: Double) {
    open fun totalValue(): Double = quantity * unitPrice

    fun describe() {
        println("$name: $quantity at ${"%.2f".format(unitPrice)} each, value ${"%.2f".format(totalValue())}")
    }
}

class DiscountedItem(name: String, quantity: Int, unitPrice: Double, val discountRate: Double) :
    Item(name, quantity, unitPrice) {
    override fun totalValue(): Double = super.totalValue() * (1 - discountRate)
}

fun main() {
    val folder = DiscountedItem("Folder", 4, 1.25, 0.20)
    folder.describe()
    println(folder is Item)

    val items: List<Item> = listOf(Item("Notebook", 3, 2.50), folder)
    for (item in items) println("${item.name}: ${"%.2f".format(item.totalValue())}")
}
```

### Expected Behavior or Output

The program prints:
```text
Folder: 4 at 1.25 each, value 4.00
true
Notebook: 7.50
Folder: 4.00
```

### Common Mistakes
1. Forgetting `open`, so the compiler refuses to let another class inherit or override.
2. Forgetting `override` on a function that replaces a parent's function, which is a compile error.
3. Using inheritance for a "has a" relationship; use composition instead (Lesson 7.5).

### Activities
1. Predict the output before running.
2. Add a subclass `PerishableItem` with an `expires` property and override `describe` by making it `open`.
3. Explain why `describe` prints the discounted value without being redefined.
4. List the order in which Kotlin looks for `totalValue` on a `DiscountedItem`.

### Accessibility Practice

Describe inheritance as an ordered list: the subclass first, then its parent. Speaking the chain aloud ('DiscountedItem, then Item') is clearer than a diagram.

### Skills Checklist
- [ ] I can declare an open class and a subclass.
- [ ] I can override a function.
- [ ] I can call `super`.
- [ ] I can explain polymorphism.
- [ ] I know classes are final by default.

---

## Lesson 7.5: Composition

### Reading References
- [Classes](https://kotlinlang.org/docs/classes.html)
- Matching Python lesson: Lesson 7.5: Instances as Attributes (Composition)

### Learning Objectives
- Explain composition ("has a").
- Hold a list of objects inside another object.
- Build an inventory from the shared items.

### Concept Explanation

*Composition* means that one object contains other objects. An inventory *has* items; it is not a kind of item. Composition is usually simpler and safer than inheritance when objects are related by containment.

The container keeps a private list of its parts and exposes functions that loop over the parts and call each part's own functions, so the container does not need to know how a part works. Keeping the list `private` forces other code to use `add` and `report`.

The example builds an `Inventory` with the three shared items and reports each quantity and the total value, 17.50.

### Worked Example

```kotlin
class Item(val name: String, val quantity: Int, val unitPrice: Double) {
    fun totalValue(): Double = quantity * unitPrice
}

class Inventory {
    private val items = mutableListOf<Item>()

    fun add(item: Item) {
        items.add(item)
    }

    fun find(name: String): Item? = items.firstOrNull { it.name == name }

    fun totalValue(): Double = items.sumOf { it.totalValue() }

    fun report() {
        for (item in items) {
            println("${item.name}: ${item.quantity}")
        }
        println("Total value: " + "%.2f".format(totalValue()))
    }
}

fun main() {
    val inventory = Inventory()
    inventory.add(Item("Notebook", 3, 2.50))
    inventory.add(Item("Pencil", 10, 0.50))
    inventory.add(Item("Folder", 4, 1.25))
    inventory.report()
    println(inventory.find("Pencil")?.quantity)
    println(inventory.find("Eraser"))
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3
Pencil: 10
Folder: 4
Total value: 17.50
10
null
```

### Common Mistakes
1. Using inheritance where a "has a" relationship is meant.
2. Making the list public so other code changes it without going through `add`.
3. Letting the container read each item's properties directly instead of calling the item's functions.

### Activities
1. Predict the output.
2. Add `remove(name)` to `Inventory` and test it.
3. Add a function that returns the names of items with a quantity below 5.
4. Explain "is a" versus "has a" with two examples.

### Accessibility Practice

Report the inventory as one labelled line per item and a final total line, so the screen reader reads a complete summary in order.

### Skills Checklist
- [ ] I can explain composition.
- [ ] I can hold a list of objects in an object.
- [ ] I can keep a list private.
- [ ] I can say "is a" versus "has a".
- [ ] I can build the shared inventory.

---

# Unit 8: Files and Exceptions

## Overview

Read and write files, handle errors, release resources reliably, and store records as JSON.

---


## Lesson 8.1: Reading from a File

### Reading References
- [Kotlin standard library: kotlin.io](https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.io/)
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 8.1: Reading from a File

### Learning Objectives
- Read a whole file and read it line by line.
- Check that a file exists before reading.
- Report a missing file clearly.

### Concept Explanation

`java.io.File` represents a path. `readText()` returns the whole file as a string, `readLines()` returns a list of lines, and `forEachLine { ... }` processes one line at a time. A relative path such as `notes.txt` starts from the program's working directory, so a program run from another folder will not find it.

`File.exists()` tests whether a file is there. Reading a file that does not exist throws a `FileNotFoundException`, which Lesson 8.3 handles.

To keep the lesson self-contained, the example first writes the two-line `notes.txt` that every language track uses, then reads it three ways and checks a file that does not exist.

### Worked Example

```kotlin
import java.io.File

fun main() {
    val notes = File("notes.txt")
    notes.writeText("Practice Kotlin.\nReview lists and functions.\n")

    println(notes.readText())

    for (line in notes.readLines()) {
        println(line)
    }
    println(notes.readLines().size)

    notes.forEachLine { println(it.uppercase()) }

    val missing = File("missing_notes.txt")
    if (!missing.exists()) {
        println("missing_notes.txt was not found.")
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Practice Kotlin.
Review lists and functions.

Practice Kotlin.
Review lists and functions.
2
PRACTICE KOTLIN.
REVIEW LISTS AND FUNCTIONS.
missing_notes.txt was not found.
```

### Common Mistakes
1. Reading a file that does not exist without checking or catching the error.
2. Running from a different folder, so the relative path points to the wrong place.
3. Forgetting that `readText()` keeps the final newline, so `println` adds a blank line.

### Activities
1. Run the program and describe each block of output.
2. Add a third line to the file text and predict the new count.
3. Print each line with its line number.
4. Print a friendly message that includes the missing file's name.

### Accessibility Practice

Read the output aloud in order. Make an error message a complete sentence that includes the file name so that it is clear without seeing the screen.

### Skills Checklist
- [ ] I can read a file whole and by line.
- [ ] I can check that a file exists.
- [ ] I know relative paths use the working directory.
- [ ] I can report a missing file.
- [ ] I can write a file for the example.

---

## Lesson 8.2: Writing to a File

### Reading References
- [Kotlin standard library: kotlin.io](https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.io/)
- Matching Python lesson: Lesson 8.2: Writing to a File

### Learning Objectives
- Write with `writeText` and append with `appendText`.
- Include line endings correctly.
- Read the file back to verify it.

### Concept Explanation

`writeText(text)` creates the file or **replaces** its contents. `appendText(text)` adds to the end. Neither adds a line ending for you, so end each line with `\n`. `printWriter()` and `bufferedWriter()` write in pieces and should be closed with `use` (Lesson 8.4).

Reading the file back is the simplest way to confirm what was saved. The example writes the first notes line, appends the second, and reads the file back.

### Worked Example

```kotlin
import java.io.File

fun main() {
    val file = File("notes.txt")
    file.writeText("Practice Kotlin.\n")
    file.appendText("Review lists and functions.\n")
    print(file.readText())
    println("Lines: ${file.readLines().size}")
}
```

### Expected Behavior or Output

The program prints:
```text
Practice Kotlin.
Review lists and functions.
Lines: 2
```

### Common Mistakes
1. Using `writeText` when `appendText` was intended, which erases earlier content.
2. Forgetting `\n`, so all written lines run together.
3. Not reading the file back to check what was actually saved.

### Activities
1. Predict the output, then run.
2. Replace the second call with `writeText` and explain the difference.
3. Append a third line with the current number of lines.
4. Write the shared scores, one per line, then read them back and total them.

### Accessibility Practice

Always read a written file back in the terminal to confirm it, using line navigation, so you do not depend on assumptions about what was saved.

### Skills Checklist
- [ ] I can write and append.
- [ ] I know `writeText` replaces.
- [ ] I can include line endings.
- [ ] I can verify by reading back.
- [ ] I can count lines in a file.

---

## Lesson 8.3: Exceptions

### Reading References
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 8.3: Exceptions - Handling Errors

### Learning Objectives
- Catch specific exceptions with `try` and `catch`.
- Use `finally` and `runCatching`.
- Raise errors with `require` and `error`.

### Concept Explanation

An *exception* is an error that stops the program unless it is caught. `try { ... } catch (e: SomeException) { ... }` runs the risky code and handles the failure. Catch the **specific** exception you expect (`FileNotFoundException`, `NumberFormatException`, `ArithmeticException`), never everything, so mistakes in your own code are not hidden. A `finally` block runs whether or not an exception happened.

Kotlin has no checked exceptions: the compiler does not force you to catch anything. `runCatching { ... }` runs a block and returns a `Result` that holds either the value or the exception, and `exceptionOrNull()?.message` reads the message.

`require(condition) { message }` rejects a bad argument and `error(message)` throws an `IllegalStateException`. Integer division by zero throws an `ArithmeticException`; division of `Double` values by zero gives infinity instead.

### Worked Example

```kotlin
import java.io.File
import java.io.FileNotFoundException

fun main() {
    try {
        File("missing_notes.txt").readText()
    } catch (e: FileNotFoundException) {
        println("Error: missing_notes.txt was not found.")
    }

    try {
        "abc".toInt()
    } catch (e: NumberFormatException) {
        println("Error: 'abc' is not a valid score.")
    }

    val zero = 0
    try {
        println(10 / zero)
    } catch (e: ArithmeticException) {
        println("Error: ${e.message}")
    }
    println(10.0 / zero)

    val result = runCatching { require(false) { "custom failure" } }
    println(result.exceptionOrNull()?.message)

    try {
        error("raised by error()")
    } catch (e: IllegalStateException) {
        println(e.message)
    } finally {
        println("Cleanup runs either way.")
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score.
Error: / by zero
Infinity
custom failure
raised by error()
Cleanup runs either way.
```

### Common Mistakes
1. Catching `Exception` for everything, which hides mistakes in your own code.
2. Using `toInt()` on untrusted text without a catch or `toIntOrNull()`.
3. Expecting `10.0 / 0` to throw. It gives `Infinity`.

### Activities
1. Predict each printed line before running.
2. Wrap `readln().toInt()` so invalid input prints a clear message and asks again.
3. Catch `ArithmeticException` in a function that computes an average of an empty list.
4. Explain when to catch an exception and when to let it stop the program.

### Accessibility Practice

Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.' Read the exception's class name aloud when you see a stack trace, then jump to the first line that names your own file.

### Skills Checklist
- [ ] I can catch specific exceptions.
- [ ] I can use `finally` and `runCatching`.
- [ ] I can raise errors with `require` and `error`.
- [ ] I know integer and decimal division by zero differ.
- [ ] I can write clear error messages.

---

## Lesson 8.4: Cleanup with use and finally

### Reading References
- [Exceptions: finally](https://kotlinlang.org/docs/exceptions.html#the-finally-block)
- Matching Python lesson: Lesson 8.4: The else and finally Blocks

### Learning Objectives
- Close files reliably with `use`.
- Show that a resource is released even after an error.
- Use `finally` for cleanup.

### Concept Explanation

A file reader or writer holds a resource from the operating system, so it must be closed. The extension function `use { ... }` runs a block and then closes the resource, **even if the block throws an exception**. It is the Kotlin equivalent of try-with-resources in Java.

`finally` is the general tool: its block runs after the `try` block whether or not an exception happened. Use `use` for anything that can be closed, and `finally` for other cleanup.

The example writes a file with `use`, reads it back, throws an exception inside a second `use` block, and shows that a reader that was closed by `use` refuses to read.

### Worked Example

```kotlin
import java.io.File

fun main() {
    val file = File("cleanup_demo.txt")
    file.bufferedWriter().use { it.write("Some data.\n") }
    println(file.readText().trim())

    val reader = file.bufferedReader()
    val firstLine = reader.use { it.readLine() }
    println(firstLine)

    val result = runCatching {
        file.bufferedReader().use { r ->
            r.readLine()
            throw IllegalStateException("failure while reading")
        }
    }
    println(result.exceptionOrNull()?.message)

    try {
        println("working")
    } finally {
        println("finally block ran")
    }

    println(runCatching { reader.readLine() }.exceptionOrNull() != null)
}
```

### Expected Behavior or Output

The program prints:
```text
Some data.
Some data.
failure while reading
working
finally block ran
true
```

### Common Mistakes
1. Opening a reader or writer and forgetting to close it.
2. Putting `return` in a `finally` block, which can hide an earlier exception.
3. Using the reader after `use` has closed it.

### Activities
1. Predict the six printed lines.
2. Rewrite the first example with an explicit `try` and `finally` and compare the length.
3. Throw an exception before the write and confirm that the file is still closed.
4. Explain why cleanup matters even if the program is about to end.

### Accessibility Practice

Print a short labelled line after each step, so the screen reader announces which path ran. Labelled lines make the order of cleanup audible.

### Skills Checklist
- [ ] I can close files with `use`.
- [ ] I can use `finally`.
- [ ] I know `use` closes after an error.
- [ ] I can show a closed reader refuses to read.
- [ ] I can explain why cleanup matters.

---

## Lesson 8.5: Storing Data with JSON

### Reading References
- Kotlin serialization documentation (kotlinlang.org/docs/serialization.html)
- JSON specification: https://www.json.org
- Matching Python lesson: Lesson 8.5: Storing Data with JSON

### Learning Objectives
- Explain why this lesson includes a JSON helper.
- Encode and decode the shared task records.
- Handle a missing or malformed file.

### Concept Explanation

The Kotlin standard library has no JSON support. Real projects add the `kotlinx.serialization` library through Gradle, which also requires a compiler plugin. To keep this course free of build tooling, the example includes a *teaching implementation*, `object Json`, with `encode` and `decode`. It handles strings, numbers, booleans, `null`, lists, and maps, writes object keys in sorted order, and reports malformed text with an exception that includes the position. It is not a replacement for a production library.

JSON text stores data in a standard format: `{ ... }` holds key-value pairs, `[ ... ]` holds ordered items, and text is in double quotation marks. Decoded data is untyped (`Map<String, Any?>`), so check each field before using it. Numbers without a decimal point decode as `Long`.

The shared to-do record has the fields `id`, `title`, `description`, `done`, and `created_at`. The example saves two tasks and loads them back, then shows the message for a malformed file.

The teaching helper decodes JSON `null` as `null` and numbers without a decimal point as `Long`. It does not handle every number edge case that a full parser must.

### Worked Example

```kotlin
object Json {
    fun encode(value: Any?): String = when (value) {
        null -> "null"
        is String -> quote(value)
        is Boolean, is Int, is Long, is Double -> value.toString()
        is Map<*, *> -> value.entries.sortedBy { it.key.toString() }
            .joinToString(",", "{", "}") { quote(it.key.toString()) + ":" + encode(it.value) }
        is List<*> -> value.joinToString(",", "[", "]") { encode(it) }
        else -> throw IllegalArgumentException("cannot encode ${value::class.simpleName}")
    }

    private fun quote(text: String): String {
        val out = StringBuilder("\"")
        for (c in text) {
            when {
                c == '"' -> out.append("\\\"")
                c == '\\' -> out.append("\\\\")
                c == '\n' -> out.append("\\n")
                c == '\r' -> out.append("\\r")
                c == '\t' -> out.append("\\t")
                c < ' ' -> out.append("\\u%04x".format(c.code))
                else -> out.append(c)
            }
        }
        return out.append('"').toString()
    }

    fun decode(text: String): Any? = Parser(text).parse()

    private class Parser(private val text: String) {
        private var pos = 0

        private fun fail(message: String): Nothing =
            throw IllegalArgumentException("$message at position $pos")

        private fun skip() {
            while (pos < text.length && text[pos].isWhitespace()) pos++
        }

        fun parse(): Any? {
            val result = value()
            skip()
            if (pos < text.length) fail("unexpected extra text")
            return result
        }

        private fun value(): Any? {
            skip()
            if (pos >= text.length) fail("unexpected end of text")
            val c = text[pos]
            return when {
                c == '{' -> obj()
                c == '[' -> list()
                c == '"' -> str()
                text.startsWith("true", pos) -> { pos += 4; true }
                text.startsWith("false", pos) -> { pos += 5; false }
                text.startsWith("null", pos) -> { pos += 4; null }
                c == '-' || c.isDigit() -> number()
                else -> fail("unexpected character")
            }
        }

        private fun number(): Any {
            val start = pos
            if (text[pos] == '-') pos++
            while (pos < text.length && (text[pos].isDigit() || text[pos] in ".eE+-")) pos++
            val token = text.substring(start, pos)
            return token.toLongOrNull() ?: token.toDoubleOrNull() ?: fail("bad number")
        }

        private fun str(): String {
            pos++
            val out = StringBuilder()
            while (true) {
                if (pos >= text.length) fail("unterminated string")
                val c = text[pos++]
                if (c == '"') return out.toString()
                if (c != '\\') { out.append(c); continue }
                if (pos >= text.length) fail("bad escape")
                when (text[pos++]) {
                    'n' -> out.append('\n')
                    't' -> out.append('\t')
                    'r' -> out.append('\r')
                    '"' -> out.append('"')
                    '\\' -> out.append('\\')
                    '/' -> out.append('/')
                    'u' -> {
                        if (pos + 4 > text.length) fail("bad escape")
                        out.append(text.substring(pos, pos + 4).toInt(16).toChar())
                        pos += 4
                    }
                    else -> fail("bad escape")
                }
            }
        }

        private fun obj(): Map<String, Any?> {
            pos++
            val map = LinkedHashMap<String, Any?>()
            skip()
            if (pos < text.length && text[pos] == '}') { pos++; return map }
            while (true) {
                skip()
                if (pos >= text.length || text[pos] != '"') fail("expected a key")
                val key = str()
                skip()
                if (pos >= text.length || text[pos] != ':') fail("expected ':'")
                pos++
                map[key] = value()
                skip()
                if (pos >= text.length) fail("unterminated object")
                val d = text[pos++]
                if (d == '}') return map
                if (d != ',') { pos--; fail("expected ',' or '}'") }
            }
        }

        private fun list(): List<Any?> {
            pos++
            val items = ArrayList<Any?>()
            skip()
            if (pos < text.length && text[pos] == ']') { pos++; return items }
            while (true) {
                items.add(value())
                skip()
                if (pos >= text.length) fail("unterminated list")
                val d = text[pos++]
                if (d == ']') return items
                if (d != ',') { pos--; fail("expected ',' or ']'") }
            }
        }
    }
}

fun main() {
    val tasks = listOf(
        mapOf("id" to 1, "title" to "Study programming", "description" to "Finish Unit 8",
            "done" to false, "created_at" to "2026-01-15T09:00:00"),
        mapOf("id" to 2, "title" to "Review scores", "description" to "Check the four scores",
            "done" to true, "created_at" to "2026-01-15T09:30:00"),
    )

    val file = java.io.File("tasks.json")
    file.writeText(Json.encode(tasks))

    if (!file.exists()) {
        println("Tasks file not found.")
        return
    }
    val loaded = try {
        Json.decode(file.readText()) as List<*>
    } catch (e: IllegalArgumentException) {
        println("Error: could not decode tasks file: ${e.message}")
        return
    }
    for (entry in loaded) {
        val task = entry as Map<*, *>
        val status = if (task["done"] == true) "done" else "not done"
        println("${task["id"]}: ${task["title"]} ($status)")
    }

    println(runCatching { Json.decode("[{\"id\": 1,") }.exceptionOrNull()?.message)
}
```

### Expected Behavior or Output

The program prints:
```text
1: Study programming (not done)
2: Review scores (done)
expected a key at position 10
```

### Common Mistakes
1. Assuming Kotlin has built-in JSON support.
2. Trusting decoded data without checking that each field exists and has the right type.
3. Overwriting a good data file with an empty list after a failed load.

### Activities
1. Run the program and read the saved JSON text from `tasks.json`.
2. Edit `tasks.json` by hand to remove a closing bracket and run the loading part again. Read the message.
3. Add a third task and confirm that it is saved and loaded.
4. Explain why a production project should use `kotlinx.serialization`.

### Accessibility Practice

Open `tasks.json` in the terminal and read it as text. JSON in a single line is difficult to navigate, so practise stepping through it by word or character.

### Skills Checklist
- [ ] I know Kotlin has no built-in JSON.
- [ ] I can encode and decode records.
- [ ] I handle missing and malformed files.
- [ ] I check decoded fields.
- [ ] I know when to use a library.

---
