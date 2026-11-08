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
