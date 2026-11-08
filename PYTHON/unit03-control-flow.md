# Unit 3: Control Flow — Decisions and Loops

## Overview

**Compatibility:** All examples target Python 3.12 and newer; they avoid syntax and standard-library APIs introduced after Python 3.12.

This unit introduces how programs make decisions using `if` statements and perform repetitive tasks with `for` loops, along with fundamental string manipulation techniques.

**Objectives:**
- Control program flow with `if`, `elif`, and `else`.
- Iterate over sequences using `for` loops.
- Understand and manipulate strings.

---

## Lesson 3.1: Boolean Expressions and `if` Statements

### Reading References
- Zelle: Chapter 7, pages 165–173
- Matthes: Chapter 5, pages 71–78

### Learning Objectives
- Identify `True` and `False` as Boolean values.
- Use comparison operators to create Boolean expressions.
- Write a basic `if` statement.
- Correctly indent the code block belonging to an `if` statement.

### Concept Explanation

#### Comparison and Boolean Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 10` | `True` |
| `<` | Less than | `5 < 10` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `10 >= 5` | `True` |

| Boolean Operator | Description | Example | Result |
|-----------------|-------------|---------|--------|
| `and` | True if both are true | `True and False` | `False` |
| `or` | True if at least one is true | `True or False` | `True` |
| `not` | Inverts the truth value | `not True` | `False` |

#### The `if` Statement

```python
score = 59
if score >= 60:
    print("Passing score.")
print("Program finished.")  # This runs regardless
```

**Indentation defines which lines belong to the `if` block.**

### Worked Example

**Example 3.1.1: Comparing a Score**
```python
score = 82

if score >= 60:
    print("Avery passed.")
else:
    print("Avery did not pass.")

print(score >= 80 and score < 90)   # both conditions must be true
print(score < 60 or score > 100)    # at least one condition must be true
print(not score >= 90)              # reverses True and False
```


**Example 3.1.2: Password Length Check**
```python
password = "mysecret"
if len(password) < 8:
    print("Weak password: Must be at least 8 characters.")
```

### Expected Behavior or Output

Expected output:
```
Avery passed.
True
False
True
```

### Common Mistakes

1. Writing `=` where `==` is needed in a condition, which is a syntax error in Python.
2. Forgetting the colon at the end of the `if` line or the indentation of its block.
3. Writing `score >= 80 and < 90` instead of repeating the variable in each comparison.

### Activities

**Activity 3.1.1: Number Comparison Game**
```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
if num1 == num2:
    print("The numbers are equal.")
if num1 < num2:
    print(f"{num1} is less than {num2}.")
```

### Accessibility Practice

Read each condition aloud using the words 'greater than or equal to', 'and', 'or', and 'not'. Confirm that your screen reader announces the colon at the end of the `if` line and the indentation of the next line, because these decide which statements run.

### Skills Checklist

- [ ] I can identify `True` and `False` as Boolean values.
- [ ] I can use comparison operators to create Boolean expressions.
- [ ] I can write a basic `if` statement.
- [ ] I can correctly indent the code block belonging to an `if` statement.

---

## Lesson 3.2: Chained Conditionals (`elif`, `else`)

### Reading References
- Zelle: Chapter 7, pages 173–176
- Matthes: Chapter 5, pages 79–84

### Learning Objectives
- Use an `else` statement to provide an alternative path.
- Use `elif` to check multiple conditions in order.
- Use `and`, `or`, and `not` operators to combine conditions.

### Concept Explanation

#### `if-elif-else` Structure

Python checks each condition in **sequential order**. As soon as a condition is `True`, it runs that block and skips the rest.

```python
score = 82

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```
Output: `Grade: B`

### Worked Example

**Example 3.2.1: Grade Classification and Boundary Scores**
Every language track uses these same thresholds: A at 90, B at 80, C at 70, D at 60, otherwise F. The test scores sit exactly on and just below each boundary. (The `def` and `return` lines are explained fully in Unit 6; for now read `classify(score)` as "the grade for this score.")
```python
def classify(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for score in [90, 89, 80, 79, 70, 69, 60, 59]:
    print(score, classify(score))
```

### Expected Behavior or Output

Expected output:
```
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

1. Putting the conditions in the wrong order, such as testing `score >= 60` first so every passing score is reported as a D.
2. Using `>` instead of `>=`, so exactly 90 receives a B.
3. Using a separate `if` for each grade instead of `elif`, so more than one message can print.

### Activities

**Activity 3.2.1: Grade Checker**
```python
score = int(input("Enter a score from 0 to 100: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

Sample run (typed input shown after each prompt):
```
Enter a score from 0 to 100: 88
Grade: B
```

Run it again with 90, 89, 60, and 59 and confirm the grades A, B, D, and F.

### Accessibility Practice

Read the boundary results aloud in order (`90 A`, `89 B`, `80 B`, `79 C`...). Each line is a number, a space, and a letter, so it is easy to follow by ear and in braille. Do not rely on indentation alone to see which `elif` belongs to which `if`; count the lines that start at the left margin.

### Skills Checklist

- [ ] I can use an `else` statement to provide an alternative path.
- [ ] I can use `elif` to check multiple conditions in order.
- [ ] I can use `and`, `or`, and `not` operators to combine conditions.

---

## Lesson 3.3: Introduction to Lists

### Reading References
- Zelle: Chapter 5, pages 105–106
- Matthes: Chapter 3, pages 33–47

### Learning Objectives
- Create a list in Python.
- Access individual items in a list using their index.
- Access list items from the end using negative indices.
- Change the value of an item at a specific index.

### Concept Explanation

A *list* is an ordered collection of values written between square brackets. Each value has a position called an *index*, and **Python starts counting at 0**. Negative indexes count from the end, so `-1` is the last item. Lists are *mutable*: you can replace an item without creating a new list.

#### Creating and Accessing Lists

```python
scores = [82, 91, 76, 88]

print(scores[0])   # 82  (first item)
print(scores[-1])  # 88  (last item)
print(len(scores)) # 4
```

**Zero-based indexing:** The first item is at index `0`.

#### Modifying Lists

### Worked Example

```python
scores = [82, 91, 76, 88]
scores[2] = 80  # Change the third score (index 2) from 76 to 80
print(scores)   # [82, 91, 80, 88]
```

### Expected Behavior or Output

Output of example 1:
```
[82, 91, 80, 88]
```

### Common Mistakes

1. Using `scores[1]` for the first item. The first item is at index 0.
2. Using an index that is too large, which raises an `IndexError`. The last valid index is `len(scores) - 1`.
3. Assuming `copy = scores` makes a separate list. Both names refer to the same list.

### Activities

**Activity 3.3.1: My Top 3 Hobbies**
```python
hobbies = ["reading", "coding", "hiking"]
print("My hobbies:", hobbies)
print("My second hobby:", hobbies[1])
hobbies[2] = "swimming"
print("Updated hobbies:", hobbies)
```

### Accessibility Practice

When reading `scores[-1]` aloud, say 'scores, open bracket, minus one, close bracket' so the sign is not lost. Print a whole list on one line, and read its length separately, so the screen reader announces the state of the list in a single pass.

### Skills Checklist

- [ ] I can create a list in Python.
- [ ] I can access individual items in a list using their index.
- [ ] I can access list items from the end using negative indices.
- [ ] I can change the value of an item at a specific index.

---

## Lesson 3.4: Iterating with `for` Loops

### Reading References
- Zelle: Chapter 2, pages 34–36
- Matthes: Chapter 4, pages 49–60

### Learning Objectives
- Explain the purpose of a `for` loop.
- Write a `for` loop to iterate over items in a list.
- Write a `for` loop to iterate over characters in a string.
- Use the `range()` function to control how many times a loop runs.

### Concept Explanation

#### The `for` Loop Structure

```python
for item in sequence:
    # code that runs for each item
```

### Worked Example

**Example 3.4.1: Total and Average of the Shared Scores**
```python
scores = [82, 91, 76, 88]
total = 0

for score in scores:
    print(f"Adding {score}")
    total = total + score

average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average}")
```


**Example 3.4.2: Looping Through a String**
```python
word = "Python"
for char in word:
    print(char)
```

**Example 3.4.3: Using `range()`**
```python
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):   # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

### Expected Behavior or Output

Expected output:
```
Adding 82
Adding 91
Adding 76
Adding 88
Total: 337
Average: 84.25
```

### Common Mistakes

1. Forgetting the colon after the `for` line or indenting the loop body inconsistently.
2. Changing a list while looping over it, which can skip items.
3. Using `range(1, 4)` and expecting it to include 4. The stop value is not included.

### Activities

**Activity 3.4.1: My Favorite Things**
```python
favorite_things = ["sunshine", "coffee", "books", "music", "mountains"]
for thing in favorite_things:
    print(f"I love {thing}!")
```

**Activity 3.4.2: Countdown Timer**
```python
start = int(input("Enter a starting number: "))
for i in range(start, 0, -1):
    print(i)
print("Blast off!")
```

### Accessibility Practice

Print one labelled line per loop pass (`Adding 82`), so your screen reader reads each step. Count the lines to confirm the loop ran the expected number of times, since the loop's structure is carried by indentation and not by visible braces.

### Skills Checklist

- [ ] I can explain the purpose of a `for` loop.
- [ ] I can write a `for` loop to iterate over items in a list.
- [ ] I can write a `for` loop to iterate over characters in a string.
- [ ] I can use the `range()` function to control how many times a loop runs.

---

## Lesson 3.5: Basic String Operations

### Reading References
- Zelle: Chapter 5, pages 99–115
- Matthes: Chapter 2, pages 19–25

### Learning Objectives
- Combine strings using concatenation.
- Find the length of a string using `len()`.
- Convert a string to uppercase/lowercase.
- Remove extra spaces using `.strip()`.
- Replace parts of a string using `.replace()`.

### Concept Explanation

#### Common String Methods

```python
message = "  Hello Python!  "

message.strip()          # "Hello Python!"   — removes whitespace
message.upper()          # "  HELLO PYTHON!  "
message.lower()          # "  hello python!  "
message.replace("Hello", "Hi")  # "  Hi Python!  "
len(message)             # 17
```

**Important:** String methods return a **new string** — they do not modify the original.

### Worked Example

**Example 3.5.1: String Manipulation**
```python
message = "  Hello Python  "
print(f"Original: '{message}'")
print(f"Length: {len(message)}")
print(f"Uppercase: '{message.upper()}'")
print(f"Stripped: '{message.strip()}'")
```

**Example 3.5.2: Normalizing a Name and Searching the Shared Text Sample**
```python
raw_name = "  avery  "
clean_name = raw_name.strip().title()
print(f"Name: '{clean_name}'")

text = "A student studies programming. Programming develops problem-solving skills."
lowered = text.lower()
print("Characters:", len(text))
print("Contains 'programming':", "programming" in lowered)
print("First position of 'programming':", lowered.find("programming"))
print("Times 'programming' appears:", lowered.count("programming"))
```

### Expected Behavior or Output

Expected output:
```
Name: 'Avery'
Characters: 75
Contains 'programming': True
First position of 'programming': 18
Times 'programming' appears: 2
```

### Common Mistakes

1. Expecting `text.upper()` to change `text`. Strings are immutable; assign the result: `text = text.upper()`.
2. Forgetting that `find` returns `-1`, not an error, when the text is missing.
3. Counting positions from 1. The first character is at index 0.

### Activities

**Activity 3.5.1: Name Formatter**
```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
print(f"Uppercase: {full_name.upper()}")
print(f"Total characters: {len(full_name)}")
```

### Accessibility Practice

Strings with many quotation marks are hard to read by ear. Say 'single quote' and 'double quote' aloud when checking a line, and print results inside labelled sentences such as `Characters: 75` so the screen reader does not run values together.

### Skills Checklist

- [ ] I can combine strings using concatenation.
- [ ] I can find the length of a string using `len()`.
- [ ] I can convert a string to uppercase/lowercase.
- [ ] I can remove extra spaces using `.strip()`.
- [ ] I can replace parts of a string using `.replace()`.

<<<<<<< HEAD
## Canonical Shared Dataset — Grade Thresholds and Scores

All tracks must classify scores using A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, and F otherwise. Use the same score sequence.

```python
scores = [82, 91, 76, 88]

def grade_for(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

for score in scores:
    print(score, grade_for(score))

total = sum(scores)
average = total / len(scores)
print("Total:", total)
print("Average:", average)
```

Expected output:
```text
82 B
91 A
76 C
88 B
Total: 337
Average: 84.25
```

Boundary tests must include 90, 80, 70, 60, and 59. Do not silently change a threshold or replace the shared scores with a different set in a parallel example.
=======
---
>>>>>>> 2067a20 (curriculum clearning and updates)
