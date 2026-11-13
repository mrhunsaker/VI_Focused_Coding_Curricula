# Unit 5: User Input and `while` Loops

## Overview

This unit focuses on obtaining diverse input from users and controlling program execution through indefinite loops.

**Objectives:**
- Implement indefinite loops using `while` statements.
- Control `while` loop execution with `break` and `continue`.
- Avoid infinite loops.

---

## Lesson 5.1: How the `input()` Function Works

### Reading References
- Matthes: Chapter 7 (User Input and while Loops), the section on how the `input()` function works
- Zelle: Chapter 2 (Writing Simple Programs), the section on input

### Learning Objectives
- Effectively use `input()` to get user data.
- Confirm that `input()`'s return value is always a string.
- Convert user input to a numeric type when necessary.

### Concept Explanation

`input(prompt)` shows the prompt, waits for the user to press Enter, and returns what was typed as a **string**, even when the user typed digits. To use the value as a number, convert it with `int()` or `float()`. Checking first with `isdigit()` avoids an error for text that is not a whole number; Lesson 8.3 shows the general solution, exceptions.

#### Key Reminder

`input()` **always returns a string**. Convert to numeric types as needed.

```python
age_input = input("How old are you? ")
print(f"Type: {type(age_input)}")    # <class 'str'>

age_int = int(age_input)
print(f"In 5 years: {age_int + 5}")
```

### Worked Example

```python
text = input("How old are you? ")
print("Type:", type(text).__name__)
if text.isdigit():
    age = int(text)
    print("In 5 years:", age + 5)
else:
    print("That was not a whole number.")
```

### Expected Behavior or Output

Sample run typing `16`:
```
How old are you? 16
Type: str
In 5 years: 21
```

Sample run typing `abc`:
```
How old are you? abc
Type: str
That was not a whole number.
```

### Common Mistakes

1. Adding to the value returned by `input()` without converting it. `"16" + 5` raises a `TypeError`.
2. Calling `int()` on text such as `"abc"` or an empty answer, which raises a `ValueError`.
3. Using `isdigit()` for numbers with a minus sign or a decimal point, which it rejects.

### Activities

1. Run the program typing `16`, then `abc`, then just Enter. Compare the three outputs.
2. Change the program so that it accepts an age only from 0 to 120.
3. Write a program that asks for a name and a number and prints one sentence using both.
4. Explain why `type(text)` is `str` even when you typed 16.

### Accessibility Practice

Each prompt ends with a space and says what to type. When you test, listen to whether your screen reader reads the prompt in full before you start typing, and write the prompt text so it still makes sense when read on its own.

### Skills Checklist

- [ ] I can effectively use `input()` to get user data.
- [ ] I can confirm that `input()`'s return value is always a string.
- [ ] I can convert user input to a numeric type when necessary.

---

## Lesson 5.2: The `while` Loop in Action

### Reading References
- Matthes: Chapter 7 (User Input and while Loops)
- Zelle: Chapter 8 (Loop Structures and Booleans)

### Learning Objectives
- Explain the difference between a `for` loop and a `while` loop.
- Write a basic `while` loop.
- Make sure my `while` loop has a way to stop.

### Concept Explanation

#### `for` vs. `while` Loop Comparison

| Feature | `for` Loop | `while` Loop |
|---------|-----------|--------------|
| **Purpose** | Definite iteration (known count) | Indefinite iteration (condition-based) |
| **When to Use** | Iterating over lists, ranges | Repeating until a condition is met |
| **Control Variable** | Automatically updated | Must be manually updated |
| **Risk** | Less prone to infinite loops | High risk if condition never becomes false |

### Worked Example

```python
count = 1
while count <= 5:
    print(count)
    count += 1
print("Counting finished!")

message = input("Enter a message, or type quit to exit: ")
while message != "quit":
    print("You said: " + message)
    message = input("Enter a message, or type quit to exit: ")
print("Goodbye!")
```

### Expected Behavior or Output

Sample run typing `hello`, `scores`, and `quit`:
```
1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit: hello
You said: hello
Enter a message, or type quit to exit: scores
You said: scores
Enter a message, or type quit to exit: quit
Goodbye!
```

### Common Mistakes

1. Forgetting to change the loop variable, which creates an endless loop.
2. Reading input only before the loop and never again inside it, so the same message repeats forever.
3. Comparing the sentinel with different capitalization (`Quit` and `quit`) and never stopping.

### Activities

1. Predict the output for the typed lines `hello`, `scores`, and `quit`.
2. Change the sentinel to `exit` and update the prompt.
3. Count how many messages were entered and print the count at the end.
4. Rewrite the counting loop as a `for` loop with `range` and compare the two.

### Accessibility Practice

Each prompt is a full sentence that names the way to stop. The response begins with the label `You said:` so the conversation can be followed in order by ear. If a loop floods the screen reader with output, stop it with Ctrl+C.

### Skills Checklist

- [ ] I can explain the difference between a `for` loop and a `while` loop.
- [ ] I can write a basic `while` loop.
- [ ] I can make sure my `while` loop has a way to stop.

---

## Lesson 5.3: Using Flags and `break` to Exit Loops

### Reading References
- Matthes: Chapter 7 (User Input and while Loops)

### Learning Objectives
- Use a Boolean "flag" variable to control a `while` loop.
- Use the `break` statement to exit a loop early.

### Concept Explanation

#### Flag Variable

```python
active = True
while active:
    message = input("Say something (or 'quit' to stop): ")
    if message == 'quit':
        active = False
    else:
        print(f"You said: {message}")
```

#### `break` Statement

```python
while True:
    city = input("Enter a city (or 'done' to finish): ")
    if city == 'done':
        break
    print(f"I've heard {city} is a great place!")
```

### Worked Example

**Example: Stopping a Search with a Flag and `break` (shared scores)**
```python
scores = [82, 91, 76, 88]
found = False
index = 0

while index < len(scores):
    if scores[index] >= 90:
        found = True
        break
    index += 1

if found:
    print(f"First score of 90 or higher: {scores[index]} at index {index}")
else:
    print("No score of 90 or higher.")
```

### Expected Behavior or Output

Expected output:
```
First score of 90 or higher: 91 at index 1
```

### Common Mistakes

1. Setting the flag but running more code in the same pass that should have been skipped.
2. Forgetting to set the result variable before the loop and misreading an old value afterward.
3. Using `break` in an inner loop and expecting it to leave the outer loop. It leaves only the innermost loop.

### Activities

1. Change the search to find the first score below 80 and predict the index.
2. Rewrite a flag-controlled loop so that it uses `break` and compare the two versions.
3. Write a loop that stops when the user types `quit` and also stops after 5 attempts.
4. Explain in two sentences when a flag is clearer than `break`.

### Accessibility Practice

Report search results as complete sentences that include both the value and its position, so the sentence is understood without any layout. Remember that Python indexes start at 0, and say 'index 1' aloud rather than 'second' to avoid confusion.

### Skills Checklist

- [ ] I can use a Boolean "flag" variable to control a `while` loop.
- [ ] I can use the `break` statement to exit a loop early.

---

## Lesson 5.4: Using `continue` in Loops

### Reading References
- Matthes: Chapter 7 (User Input and while Loops), the section on using `continue`

### Learning Objectives
- Use `continue` to skip the rest of the current loop iteration.
- Identify scenarios where `continue` would be useful.

### Concept Explanation

#### `continue` — Skip the Current Iteration

```python
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue        # Skip even numbers
    print(number)       # Prints 1, 3, 5, 7, 9
```

#### `continue` vs. `break`

- `break` — **exits the loop entirely**
- `continue` — **skips only the current iteration**, loop continues

### Worked Example

**Example: Skipping Invalid Entries with `continue`**
```python
raw_scores = [82, -5, 91, 105, 76, 88]
valid_total = 0
valid_count = 0

for raw in raw_scores:
    if raw < 0 or raw > 100:
        print(f"Skipping invalid score: {raw}")
        continue
    valid_total += raw
    valid_count += 1

print(f"Valid scores: {valid_count}, total: {valid_total}")
```

### Expected Behavior or Output

Expected output:
```
Skipping invalid score: -5
Skipping invalid score: 105
Valid scores: 4, total: 337
```

### Common Mistakes

1. Placing statements that must always run after `continue`, so they are skipped.
2. Using `continue` in a `while` loop before changing the loop variable, which creates an endless loop.
3. Confusing `continue` (skip this pass) with `break` (leave the loop).

### Activities

1. Predict the printed lines and the final total of the invalid-scores example.
2. Skip scores below 80 instead.
3. Rewrite the invalid-scores loop with an `if`/`else` and no `continue`, and compare the readability.
4. Write a loop over `range(1, 10)` that prints only odd numbers using `continue`.

### Accessibility Practice

Print a line for every skipped entry, so the screen reader announces what was ignored. Never skip silently when a user needs to know what the program did with their data.

### Skills Checklist

- [ ] I can use `continue` to skip the rest of the current loop iteration.
- [ ] I can identify scenarios where `continue` would be useful.

---

## Lesson 5.5: Avoiding Infinite Loops

### Reading References
- Matthes: Chapter 7 (User Input and while Loops), the sections on avoiding infinite loops
- Zelle: Chapter 8 (Loop Structures and Booleans)

### Learning Objectives
- Define what an infinite loop is.
- Identify common causes of infinite loops.
- Stop a running program in an infinite loop.

### Concept Explanation

An **infinite loop** never ends because its condition always remains `True`.

**Common causes:**
1. Forgetting to update the loop variable.
2. Updating the variable in the wrong direction.
3. Using an incorrect logical condition.

```python
# INFINITE LOOP — Don't run!
count = 1
while count <= 5:
    print(count)
    # Missing: count += 1

# CORRECT
count = 1
while count <= 5:
    print(count)
    count += 1
```

**To stop a running infinite loop:** Press `Ctrl + C` in the terminal.

### Worked Example

```python
MAX_ATTEMPTS = 3
attempts = 0
score = None

while attempts < MAX_ATTEMPTS:
    attempts += 1
    text = input(f"Enter a score from 0 to 100 (attempt {attempts} of {MAX_ATTEMPTS}): ")
    if text.isdigit() and 0 <= int(text) <= 100:
        score = int(text)
        break
    print("Invalid score: " + text)

if score is not None:
    print("Accepted score:", score)
else:
    print("No valid score was entered.")
```

### Expected Behavior or Output

Sample run typing `abc`, `105`, and `88`:
```
Enter a score from 0 to 100 (attempt 1 of 3): abc
Invalid score: abc
Enter a score from 0 to 100 (attempt 2 of 3): 105
Invalid score: 105
Enter a score from 0 to 100 (attempt 3 of 3): 88
Accepted score: 88
```

Sample run typing three invalid lines (`x`, `y`, `z`):
```
Enter a score from 0 to 100 (attempt 1 of 3): x
Invalid score: x
Enter a score from 0 to 100 (attempt 2 of 3): y
Invalid score: y
Enter a score from 0 to 100 (attempt 3 of 3): z
Invalid score: z
No valid score was entered.
```

### Common Mistakes

1. Forgetting to increase `attempts`, so the limit is never reached.
2. Testing the wrong variable in the loop condition, so it never becomes false.
3. Not knowing the interrupt key. Press Ctrl+C in the terminal to stop a program that will not end.

### Activities

1. Run the sample with `abc`, `105`, and `88` and confirm the accepted score.
2. Run it with three invalid lines and read the final message.
3. Change the limit to 5 and test it.
4. For each loop you have written so far, write down what makes it stop.

### Accessibility Practice

A loop that cannot be stopped is an accessibility problem as well as a bug, because it can flood a screen reader with output. Learn Ctrl+C before running loops, give every input loop a limit, and write error messages that say what is valid.

### Skills Checklist

- [ ] I can define what an infinite loop is.
- [ ] I can identify common causes of infinite loops.
- [ ] I know how to stop a running program in an infinite loop.

---
