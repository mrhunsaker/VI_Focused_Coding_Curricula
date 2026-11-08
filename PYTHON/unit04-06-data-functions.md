# Unit 4: Data Structures — Lists and Dictionaries

## Overview

**Compatibility:** All examples target Python 3.12 and newer; they avoid syntax and standard-library APIs introduced after Python 3.12.

This unit deepens understanding of lists and introduces dictionaries as powerful mechanisms for organizing data.

**Objectives:**
- Add, remove, and organize list elements.
- Work with tuples (immutable lists).
- Use dictionaries for key-value pair storage.
- Loop through dictionaries.

---

## Lesson 4.1: More on Lists

### Reading References
- Matthes: Chapter 3 (Introducing Lists) and Chapter 4 (Working with Lists)

### Learning Objectives
- Add an item to the end of a list using `.append()`.
- Insert an item at a specific position using `.insert()`.
- Remove an item by index using `del`.
- Remove an item and retrieve its value using `.pop()`.
- Remove the first occurrence of a value using `.remove()`.

### Concept Explanation

#### Adding and Removing Elements

```python
my_list = [10, 20, 30]

my_list.append(40)          # Add to end → [10, 20, 30, 40]
my_list.insert(1, 15)       # Insert at index 1 → [10, 15, 20, 30, 40]
del my_list[0]              # Delete by index → [15, 20, 30, 40]
removed = my_list.pop()     # Remove and return last → removed=40, list=[15, 20, 30]
my_list.remove(20)          # Remove by value → [15, 30]
```

### Worked Example

```python
scores = [82, 91, 76, 88]

scores.append(95)        # [82, 91, 76, 88, 95]
scores.insert(1, 85)     # [82, 85, 91, 76, 88, 95]
scores[2] = 93           # [82, 85, 93, 76, 88, 95]
scores.remove(76)        # [82, 85, 93, 88, 95]
last_score = scores.pop()  # last_score is 95

print(scores)
print(len(scores))
print(88 in scores)
```

### Expected Behavior or Output

Expected output:
```
[82, 85, 93, 88]
4
True
```

### Common Mistakes

1. Using `list.insert(value, position)`. The position comes first: `scores.insert(1, 85)`.
2. Calling `remove()` with a value that is not in the list, which raises a `ValueError`; check with `in` first.
3. Removing items from a list while looping over it, which skips the item after each removal.

### Activities

1. Trace the list after each operation in the example and write each version as one sentence.
2. Remove the first score with `pop(0)` and explain what happens to the other scores.
3. Write code that removes every score below 80 safely.
4. Print the position of the first score above 90 with `index()`, and explain what happens if none exists.

### Accessibility Practice

After every change, print the whole list on one line so a screen reader reads a complete state in one pass. Say the comments aloud as part of each line, since they hold the expected value after the change.

### Skills Checklist

- [ ] I can add an item to the end of a list using `.append()`.
- [ ] I can insert an item at a specific position using `.insert()`.
- [ ] I can remove an item by index using `del`.
- [ ] I can remove an item and retrieve its value using `.pop()`.
- [ ] I can remove the first occurrence of a value using `.remove()`.

---

## Lesson 4.2: Organizing Lists

### Reading References
- Matthes: Chapter 3 (Introducing Lists) and Chapter 4 (Working with Lists)

### Learning Objectives
- Sort a list permanently using `.sort()`.
- Get a temporarily sorted version using `sorted()`.
- Reverse a list using `.reverse()`.
- Find how many items are in a list using `len()`.

### Concept Explanation

Lists can be reordered in two ways. `sort()` changes the list *in place* and returns nothing. `sorted()` returns a *new* sorted list and leaves the original unchanged. Both accept `reverse=True` for descending order.

#### Sorting and Reversing

### Worked Example

```python
scores = [82, 91, 76, 88]
scores.sort()                           # Permanent sort in-place
print(scores)                           # [76, 82, 88, 91]

fruits = ["orange", "apple", "banana"]
sorted_fruits = sorted(fruits)          # Temporary sort — original unchanged
print(fruits)                           # ['orange', 'apple', 'banana']
print(sorted_fruits)                    # ['apple', 'banana', 'orange']

scores.reverse()                        # Reverse in-place -> [91, 88, 82, 76]
scores.sort(reverse=True)               # Sort descending -> [91, 88, 82, 76]
print(scores)                           # [91, 88, 82, 76]
print(len(scores))                      # Length: 4
```

### Expected Behavior or Output

Output of example 1:
```
[76, 82, 88, 91]
['orange', 'apple', 'banana']
['apple', 'banana', 'orange']
[91, 88, 82, 76]
4
```

### Common Mistakes

1. Writing `scores = scores.sort()`. `sort()` returns `None`, so the list is lost.
2. Sorting a list that mixes numbers and text, which raises a `TypeError`.
3. Expecting `reverse()` to sort. It only flips the current order.

### Activities

1. Predict the result of `scores.sort()` and `scores.sort(reverse=True)` on the shared scores, then check.
2. Use `sorted(scores)` and show that the original list is unchanged.
3. Sort the words `["pencil", "folder", "notebook"]` and print them.
4. Explain the difference between `sort()` and `sorted()` in two sentences.

### Accessibility Practice

Print each sorted version on its own labelled line (`Ascending:`, `Descending:`). The first and last numbers are the quickest to check by ear.

### Skills Checklist

- [ ] I can sort a list permanently using `.sort()`.
- [ ] I can get a temporarily sorted version using `sorted()`.
- [ ] I can reverse a list using `.reverse()`.
- [ ] I can find how many items are in a list using `len()`.

---

## Lesson 4.3: Tuples — Immutable Lists

### Reading References
- Matthes: Chapter 4 (Working with Lists), the section on tuples

### Learning Objectives
- Create a tuple in Python.
- Explain the main difference between a list and a tuple (mutability).
- Access items in a tuple by their index.

### Concept Explanation

A *tuple* is an ordered collection like a list, written with parentheses, but it cannot be changed after it is created. Use a tuple for a fixed group of values such as the shared coordinates (3, 4). Because it cannot change, a tuple can also be used where Python needs a value that never changes, such as a dictionary key.

#### Tuples

Tuples are defined with parentheses and **cannot be changed** after creation.


**When to use tuples:** For data that should remain constant (coordinates, RGB values, fixed settings).

### Worked Example

```python
coordinates = (3, 4)
x, y = coordinates        # tuple unpacking
print(coordinates[0])     # 3
print(coordinates[-1])    # 4
print(x, y)               # 3 4

# This would cause a TypeError:
# coordinates[1] = 5
```

### Expected Behavior or Output

Output of example 1:
```
3
4
3 4
```

### Common Mistakes

1. Writing `(5)` for a one-item tuple. A one-item tuple needs a comma: `(5,)`.
2. Trying to assign to an item (`coordinates[1] = 5`), which raises a `TypeError`.
3. Using a list when the data should never change, so an accidental change goes unnoticed.

### Activities

1. Create the tuple `(3, 4)`, unpack it into `x` and `y`, and print both.
2. Write a function that returns a name, an age, and a height as a tuple and unpack all three.
3. Try to change one item of a tuple and read the error message aloud.
4. Explain, in two sentences, when a tuple is a better choice than a list.

### Accessibility Practice

Say the parentheses and the commas aloud when reading a tuple, because a one-item tuple differs from a plain value only by its trailing comma. Read error messages from the last line upward to find the problem quickly.

### Skills Checklist

- [ ] I can create a tuple in Python.
- [ ] I can explain the main difference between a list and a tuple (mutability).
- [ ] I can access items in a tuple by their index.

---

## Lesson 4.4: Introducing Dictionaries

### Reading References
- Zelle: Chapter 11, pages 307–309
- Matthes: Chapter 6, pages 91–98

### Learning Objectives
- Create a dictionary in Python.
- Explain what a key-value pair is.
- Access a value in a dictionary using its key.
- Add, modify, and remove key-value pairs.

### Concept Explanation

#### Dictionary Basics

A dictionary stores **key-value pairs**. Keys must be unique and immutable (strings, numbers, tuples). Values can be anything.

```python
student_profile = {
    "name": "Avery",
    "age": 16,
    "height_m": 1.72,
<<<<<<< HEAD
    "favorite_subject": "Computer Science",
}

print(student_profile["name"])
print(student_profile["favorite_subject"])

# Demonstrate adding and removing a temporary key without changing
# the four-field canonical student record.
student_profile["temporary_note"] = "Dictionary example"
del student_profile["temporary_note"]
print(sorted(student_profile))
=======
    "favorite_subject": "Computer Science"
}

print(student_profile["name"])            # Avery
student_profile["age"] = 17               # Modify existing key
student_profile["grade_level"] = 11       # Add new key
del student_profile["height_m"]           # Remove key
print(student_profile)
>>>>>>> 2067a20 (curriculum clearning and updates)
```

Expected output:
```
Avery
{'name': 'Avery', 'age': 17, 'favorite_subject': 'Computer Science', 'grade_level': 11}
```

### Worked Example

**Example 4.4.1: Inventory Item Dictionary**
```python
item = {
    "name": "Notebook",
    "quantity": 3,
    "unit_price": 2.50
}

print(f"Item: {item['name']}")
print(f"Quantity: {item['quantity']}")

item["quantity"] = item["quantity"] + 2    # restock two more
item["location"] = "Shelf A"               # add a new key
print(item)
print("Stock value:", item["quantity"] * item["unit_price"])
```

### Expected Behavior or Output

Expected output:
```
Item: Notebook
Quantity: 3
{'name': 'Notebook', 'quantity': 5, 'unit_price': 2.5, 'location': 'Shelf A'}
Stock value: 12.5
```

### Common Mistakes

1. Using a key that does not exist (`profile["grade"]`), which raises a `KeyError`; use `profile.get("grade")` to receive `None` instead.
2. Forgetting the quotation marks around a text key, so Python looks for a variable.
3. Expecting dictionary order to be sorted. Dictionaries keep insertion order, not alphabetical order.

### Activities

1. Predict the printed values before running the example, then run it.
2. Add a `"discount"` key to the item and print the discounted line value.
3. Remove `"favorite_subject"` from the profile with `del` and show what `get` returns afterward.
4. Write a check that tells whether an item has all of the keys `name`, `quantity`, and `unit_price`.

### Accessibility Practice

Choose key names that read well aloud, such as `unit_price`. Print one key and value per line, so the screen reader announces each pair separately, and avoid relying on curly braces alone to see where a dictionary ends.

### Skills Checklist

- [ ] I can create a dictionary in Python.
- [ ] I can explain what a key-value pair is.
- [ ] I can access a value in a dictionary using its key.
- [ ] I can add, modify, and remove key-value pairs.

---

## Lesson 4.5: Looping Through Dictionaries

### Reading References
- Matthes: Chapter 6 (Dictionaries), the sections on looping through a dictionary

### Learning Objectives
- Loop through all the keys in a dictionary.
- Loop through all the values in a dictionary.
- Loop through both keys and values at the same time.

### Concept Explanation

#### Dictionary Iteration Methods

### Worked Example

```python
inventory = {
    "Notebook": {"quantity": 3, "unit_price": 2.50},
    "Pencil": {"quantity": 10, "unit_price": 0.50},
    "Folder": {"quantity": 4, "unit_price": 1.25},
}

# Loop through keys (default)
for item_name in inventory:
    print(item_name)

<<<<<<< HEAD
# Loop through quantities only
for item in inventory.values():
    print(item["quantity"])

# Loop through key-value pairs
for item_name, item in inventory.items():
    line_total = item["quantity"] * item["unit_price"]
    print(f"{item_name}: {item['quantity']} in stock; value $" + f"{line_total:.2f}")
=======
# Loop through values only
for details in inventory.values():
    print(details["quantity"])

# Loop through key-value pairs
total_value = 0
for item_name, details in inventory.items():
    line_value = details["quantity"] * details["unit_price"]
    print(f"{item_name}: {details['quantity']} in stock, value {line_value:.2f}")
    total_value += line_value
print(f"Total inventory value: {total_value:.2f}")
>>>>>>> 2067a20 (curriculum clearning and updates)
```

### Expected Behavior or Output

Expected output:
```
Notebook
Pencil
Folder
3
10
4
Notebook: 3 in stock, value 7.50
Pencil: 10 in stock, value 5.00
Folder: 4 in stock, value 5.00
Total inventory value: 17.50
```

### Common Mistakes

1. Looping with `for item in inventory` and expecting the values. The default loop gives the keys.
2. Changing the dictionary's size while looping over it, which raises a `RuntimeError`.
3. Forgetting `.items()` when both the key and the value are needed.

### Activities

1. Run the example and write the three key-value lines in order.
2. Print only the items with a quantity below 5.
3. Print the inventory sorted by the line value, highest first.
4. Explain why `.items()` returns pairs and how the loop unpacks them.

### Accessibility Practice

Print each inventory item as one complete sentence so the screen reader reads the name, quantity, and value together. Python dictionaries keep insertion order, so the order is stable and can be learned by ear.

### Skills Checklist

- [ ] I can loop through all the keys in a dictionary.
- [ ] I can loop through all the values in a dictionary.
- [ ] I can loop through both keys and values at the same time.

---

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

# Unit 6: Functions

## Overview

This unit introduces functions, enabling organization of code into reusable blocks, passing arguments, and returning values.

**Objectives:**
- Define and call functions.
- Pass arguments to functions.
- Return values from functions.
- Understand the concept of scope.

---

## Lesson 6.1: Defining Functions

### Reading References
- Zelle: Chapter 6, pages 137–142
- Matthes: Chapter 8, pages 129–130

### Learning Objectives
- Explain why functions are useful.
- Define a simple function in Python.
- Use parameters to specify function inputs.
- Call a function by its name.

### Concept Explanation

#### Function Syntax

```python
def function_name(parameter1, parameter2):
    """Docstring describing what the function does."""
    # Function body
    print(f"Hello, {parameter1}!")
```

### Worked Example

**Example 6.1.1: Simple Greeting Function**
```python
def greet_user():
    """Prints a simple greeting message."""
    print("Hello, Python programmer!")

greet_user()   # Call the function
greet_user()   # Call it again
```

**Example 6.1.2: Function with a Parameter**
```python
def greet_name(name):
    """Prints a personalized greeting."""
    print(f"Hello, {name}!")

greet_name("Avery")
greet_name("Riley")
```

**Example 6.1.3: A Reusable Tip Calculator (shared calculator values)**
```python
def show_tip(bill, tip_rate):
    """Print the tip and the total for a bill."""
    tip = bill * tip_rate
    print(f"Tip: {tip:.2f}")
    print(f"Total: {bill + tip:.2f}")

show_tip(24.5, 0.15)
```

### Expected Behavior or Output

Expected output:
```
Tip: 3.67
Total: 28.18
```

### Common Mistakes

1. Writing `greet_user` without parentheses and expecting the function to run.
2. Forgetting the colon after the `def` line, or the indentation of the body.
3. Passing arguments in the wrong order, such as `show_tip(0.15, 24.5)`.

### Activities

1. Call `show_tip(100, 0.2)` and predict both printed lines.
2. Write a function `describe_student(name, age)` that prints one sentence.
3. Call `greet_name()` with no argument and read the error message.
4. Explain the difference between a parameter and an argument using the example.

### Accessibility Practice

Choose function names that read as actions when spoken, such as `show_tip`. Print complete sentences from a function so the screen reader announces the result of each call separately, and say 'open parenthesis, close parenthesis' for an empty parameter list.

### Skills Checklist

- [ ] I can explain why functions are useful.
- [ ] I can define a simple function in Python.
- [ ] I can use parameters to specify function inputs.
- [ ] I can call a function by its name.

---

## Lesson 6.2: Passing Arguments

### Reading References
- Matthes: Chapter 8 (Functions), the sections on passing arguments
- Zelle: Chapter 6 (Defining Functions)

### Learning Objectives
- Differentiate between a parameter and an argument.
- Pass arguments using positional order.
- Pass arguments using keyword arguments.

### Concept Explanation

#### Positional vs. Keyword Arguments

```python
def describe_animal(animal_type, animal_name):
    print(f"I have a {animal_type} named {animal_name}.")

# Positional arguments (order matters)
describe_animal("dog", "Buddy")

# Keyword arguments (order doesn't matter)
describe_animal(animal_name="Max", animal_type="cat")
```

#### Default Values

```python
def make_shirt(size, message="I love Python"):
    print(f"Making a {size}-sized shirt: '{message}'")

make_shirt("large")                       # Uses default message
make_shirt("medium", "Hello World")       # Custom message
```

### Worked Example

**Example: Default, Positional, and Keyword Arguments (shared calculator values)**
```python
def calculate_total(bill, tip_rate=0.15):
    return bill + bill * tip_rate

print(f"{calculate_total(24.5):.2f}")                       # default rate
print(f"{calculate_total(24.5, 0.20):.2f}")                 # positional
print(f"{calculate_total(tip_rate=0.10, bill=24.5):.2f}")   # keyword
```

### Expected Behavior or Output

Expected output:
```
28.18
29.40
26.95
```

### Common Mistakes

1. Putting a parameter with a default before a parameter without one in the definition, which is a syntax error.
2. Mixing positional and keyword arguments in an order Python does not allow (positional first).
3. Using a mutable default such as `[]`, which is shared between calls.

### Activities

1. Predict the three totals in the example before running it.
2. Add a third parameter `round_total` with the default `False` and use it.
3. Call the function with the arguments in a different order using keywords.
4. Explain why `tip_rate=0.15` is called a default value.

### Accessibility Practice

Keyword arguments make a call read as a sentence: 'calculate total, bill equals 24.5, tip rate equals 0.10'. Say the equals signs aloud and check that your screen reader announces them.

### Skills Checklist

- [ ] I can differentiate between a parameter and an argument.
- [ ] I can pass arguments using positional order.
- [ ] I can pass arguments using keyword arguments.

---

## Lesson 6.3: Return Values

### Reading References
- Matthes: Chapter 8 (Functions), the section on return values
- Zelle: Chapter 6 (Defining Functions)

### Learning Objectives
- Use `return` to send a value back from a function.
- Explain the difference between `print()` and `return`.
- Store the returned value of a function in a variable.

### Concept Explanation

#### The `return` Statement

```python
def add_numbers(num1, num2):
    """Adds two numbers and returns the result."""
    total = num1 + num2
    return total

result = add_numbers(5, 3)
print(f"The sum is: {result}")   # 8
```



**Key difference:** `print()` displays a value; `return` sends a value back to the caller for further use.

### Worked Example

**Example: Returning Computed Results (shared scores)**
```python
def average(scores):
    """Return the average of a list of scores."""
    return sum(scores) / len(scores)

def classify(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"

avg = average([82, 91, 76, 88])   # returned, not just printed
print(f"Average: {avg}")
print(f"Grade for the average: {classify(avg)}")
```

### Expected Behavior or Output

Expected output:
```
Average: 84.25
Grade for the average: B
```

### Common Mistakes

1. Printing inside a function and then trying to use the result in a calculation. The function returned `None`.
2. Writing statements after `return` in the same block. They never run.
3. Ignoring a returned value, so the work of the function is lost.

### Activities

1. Predict the two printed results of the example before running.
2. Write `total(list)` that returns the sum of a list of numbers.
3. Write `is_passing(score)` that returns `True` or `False` using the shared thresholds.
4. Explain the difference between `print` and `return` in two sentences.

### Accessibility Practice

Return values from functions and print them in one place. A function that prints and returns at the same time can announce a result twice. Read the single printed line aloud and check it matches the returned value.

### Skills Checklist

- [ ] I can use `return` to send a value back from a function.
- [ ] I can explain the difference between `print()` and `return`.
- [ ] I can store the returned value of a function in a variable.

---

## Lesson 6.4: Functions with Lists and Dictionaries

### Reading References
- Matthes: Chapter 8 (Functions), the section on passing a list to a function

### Learning Objectives
- Pass a list or dictionary as an argument to a function.
- Understand that modifying a list inside a function affects the original.
- Create a copy of a list to avoid unintended modifications.

### Concept Explanation

Since lists are **mutable**, modifying them inside a function changes the original:

```python
def add_score(score_list, new_score):
    score_list.append(new_score)

scores = [82, 91, 76, 88]
add_score(scores, 95)
print(scores)   # [82, 91, 76, 88, 95]  - the original list changed
```

Expected output:
```
[82, 91, 76, 88, 95]
```

To prevent modification, pass a copy:
```python
add_score(scores[:], 100)   # Original unchanged
```

### Worked Example

**Example: Processing the Shared Inventory with a Function**
```python
def inventory_value(inventory):
    total = 0
    for details in inventory.values():
        total += details["quantity"] * details["unit_price"]
    return total

inventory = {
    "Notebook": {"quantity": 3, "unit_price": 2.50},
    "Pencil": {"quantity": 10, "unit_price": 0.50},
    "Folder": {"quantity": 4, "unit_price": 1.25},
}
print(f"Total inventory value: {inventory_value(inventory):.2f}")
```

### Expected Behavior or Output

Expected output:
```
Total inventory value: 17.50
```

### Common Mistakes

1. Expecting a function to receive its own copy of a list. It receives the same list and can change it.
2. Changing a list inside a function that is meant only to read it.
3. Making a copy with `copy = original` instead of `original[:]` or `list(original)`.

### Activities

1. Predict the printed lists in the example before running it.
2. Write `scale_prices(inventory, factor)` that changes the prices in place and show the effect.
3. Rewrite it so it returns a new inventory and leaves the original unchanged.
4. Explain the difference between passing a number and passing a list to a function.

### Accessibility Practice

State aloud before each call whether the function changes its argument. Print the list before and after the call so a screen reader user hears the effect, and use names such as `add_score` that say a change will happen.

### Skills Checklist

- [ ] I can pass a list or dictionary as an argument to a function.
- [ ] I understand that modifying a list inside a function affects the original.
- [ ] I can create a copy of a list to avoid unintended modifications.

---

## Lesson 6.5: Arbitrary Number of Arguments

### Reading References
- Matthes: Chapter 8 (Functions), the section on passing an arbitrary number of arguments

### Learning Objectives
- Define a function using `*args` for arbitrary positional arguments.
- Define a function using `**kwargs` for arbitrary keyword arguments.

### Concept Explanation

#### `*args` — Arbitrary Positional Arguments

```python
def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with:")
    for topping in toppings:
        print(f"  - {topping}")

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
```

**Example: Variable Number of Scores**
```python
def average(*scores):
    return sum(scores) / len(scores)

print(average(82, 91, 76, 88))   # any number of arguments
print(average(90, 80))
```

Expected output:
```
84.25
85.0
```

#### `**kwargs` — Arbitrary Keyword Arguments

### Worked Example

```python
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

profile = build_profile('albert', 'einstein',
                        location='princeton',
                        field='physics')
print(profile)
```

### Expected Behavior or Output

Output of example 1:
```
{'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
```

### Common Mistakes

1. Calling `average()` with no arguments, which divides by zero. Check the count first.
2. Putting `*args` before a normal parameter and being unable to pass the normal one by position.
3. Forgetting that `*args` is a tuple, not a list, so it cannot be changed.

### Activities

1. Predict the result of `average(82, 91, 76, 88)` and `average(90, 80)`.
2. Write `maximum(*numbers)` that returns the largest argument.
3. Write `join_words(separator, *words)` that joins any number of words.
4. Explain what the `*` does in a call such as `average(*scores)`.

### Accessibility Practice

Read variadic signatures aloud: 'define average, open parenthesis, star scores, close parenthesis'. Make sure your screen reader announces the star, since it changes the meaning of the parameter.

### Skills Checklist

- [ ] I can define a function using `*args` for arbitrary positional arguments.
- [ ] I can define a function using `**kwargs` for arbitrary keyword arguments.

<<<<<<< HEAD
## Canonical Shared Dataset — Inventory, Collections, and Functions

Use the same inventory records for list, dictionary, iteration, and function examples.

```python
inventory = [
    {"name": "Notebook", "quantity": 3, "unit_price": 2.50},
    {"name": "Pencil", "quantity": 10, "unit_price": 0.50},
    {"name": "Folder", "quantity": 4, "unit_price": 1.25},
]

def item_value(item):
    return item["quantity"] * item["unit_price"]

for item in inventory:
    print(item["name"], item["quantity"], f"${item['unit_price']:.2f}",
          f"${item_value(item):.2f}")

grand_total = sum(item_value(item) for item in inventory)
print(f"Inventory total: ${grand_total:.2f}")
```

Expected output:
```text
Notebook 3 $2.50 $7.50
Pencil 10 $0.50 $5.00
Folder 4 $1.25 $5.00
Inventory total: $17.50
```

For sequence exercises, use the canonical scores `[82, 91, 76, 88]`. For immutable-sequence exercises, use coordinates `(3, 4)`. Keep language-specific collection types idiomatic while preserving record values and calculation results.
=======
---
>>>>>>> 2067a20 (curriculum clearning and updates)
