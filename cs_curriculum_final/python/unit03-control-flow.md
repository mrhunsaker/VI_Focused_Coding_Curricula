# Unit 3: Control Flow --- Decisions and Loops

## Overview

This unit introduces how programs make decisions using `if` statements and perform repetitive tasks with `for` loops, along with fundamental string manipulation techniques.

**Objectives:**

- Control program flow with `if`, `elif`, and `else`.
- Iterate over sequences using `for` loops.
- Understand and manipulate strings.

---

## Lesson 3.1: Boolean Expressions and `if` Statements

### Reading References

- Zelle: Chapter 7, pages 165--173
- Matthes: Chapter 5, pages 71--78

### Comparison and Boolean Operators

| Operator | Meaning               | Example   | Result |
| -------- | --------------------- | --------- | ------ |
| `==`     | Equal to              | `5 == 5`  | `True` |
| `!=`     | Not equal to          | `5 != 10` | `True` |
| `<`      | Less than             | `5 < 10`  | `True` |
| `>`      | Greater than          | `10 > 5`  | `True` |
| `<=`     | Less than or equal to | `5 <= 5`  | `True` |
| `>=`     | Greater than or equal | `10 >= 5` | `True` |

| Boolean Operator | Description                  | Example          | Result  |
| ---------------- | ---------------------------- | ---------------- | ------- |
| `and`            | True if both are true        | `True and False` | `False` |
| `or`             | True if at least one is true | `True or False`  | `True`  |
| `not`            | Inverts the truth value      | `not True`       | `False` |

### The `if` Statement

```python
age = 15
if age >= 18:
    print("You are old enough to vote.")
print("Program finished.")  # This runs regardless
```

**Indentation defines which lines belong to the `if` block.**

### Examples

**Example 3.1.1: Simple Age Check**

```python
age = 17
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

**Example 3.1.2: Password Length Check**

```python
password = "mysecret"
if len(password) < 8:
    print("Weak password: Must be at least 8 characters.")
```

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

### Skills Checklist

- [ ] I can identify `True` and `False` as Boolean values.
- [ ] I can use comparison operators to create Boolean expressions.
- [ ] I can write a basic `if` statement.
- [ ] I can correctly indent the code block belonging to an `if` statement.

---

## Lesson 3.2: Chained Conditionals (`elif`, `else`)

### Reading References

- Zelle: Chapter 7, pages 173--176
- Matthes: Chapter 5, pages 79--84

### `if-elif-else` Structure

Python checks each condition in **sequential order**. As soon as a condition is `True`, it runs that block and skips the rest.

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

Output: `Grade: B`

### Examples

**Example 3.2.1: Stages of Life**

```python
age = 25
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
```

### Activities

**Activity 3.2.1: Movie Ticket Pricing**

```python
age = int(input("Enter your age: "))

if age <= 5:
    print("Ticket price: Free")
elif age <= 12:
    print("Ticket price: $7")
elif age <= 64:
    print("Ticket price: $12")
else:
    print("Ticket price: $5")
```

### Skills Checklist

- [ ] I can use an `else` statement to provide an alternative path.
- [ ] I can use `elif` to check multiple conditions in order.
- [ ] I can use `and`, `or`, and `not` operators to combine conditions.

---

## Lesson 3.3: Introduction to Lists

### Reading References

- Zelle: Chapter 5, pages 105--106
- Matthes: Chapter 3, pages 33--47

### Creating and Accessing Lists

```python
colors = ["red", "blue", "green", "yellow"]

print(colors[0])   # "red"   (first item)
print(colors[-1])  # "yellow" (last item)
print(len(colors)) # 4
```

**Zero-based indexing:** The first item is at index `0`.

### Modifying Lists

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "grape"  # Change "banana" to "grape"
print(fruits)         # ["apple", "grape", "cherry"]
```

### Activities

**Activity 3.3.1: My Top 3 Hobbies**

```python
hobbies = ["reading", "coding", "hiking"]
print("My hobbies:", hobbies)
print("My second hobby:", hobbies[1])
hobbies[2] = "swimming"
print("Updated hobbies:", hobbies)
```

### Skills Checklist

- [ ] I can create a list in Python.
- [ ] I can access individual items in a list using their index.
- [ ] I can access list items from the end using negative indices.
- [ ] I can change the value of an item at a specific index.

---

## Lesson 3.4: Iterating with `for` Loops

### Reading References

- Zelle: Chapter 2, pages 34--36
- Matthes: Chapter 4, pages 49--60

### The `for` Loop Structure

```python
for item in sequence:
    # code that runs for each item
```

### Examples

**Example 3.4.1: Looping Through a List**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}.")
print("Finished listing fruits.")
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

### Skills Checklist

- [ ] I can explain the purpose of a `for` loop.
- [ ] I can write a `for` loop to iterate over items in a list.
- [ ] I can write a `for` loop to iterate over characters in a string.
- [ ] I can use the `range()` function to control how many times a loop runs.

---

## Lesson 3.5: Basic String Operations

### Reading References

- Zelle: Chapter 5, pages 99--115
- Matthes: Chapter 2, pages 19--25

### Common String Methods

```python
message = "  Hello Python!  "

message.strip()          # "Hello Python!"   --- removes whitespace
message.upper()          # "  HELLO PYTHON!  "
message.lower()          # "  hello python!  "
message.replace("Hello", "Hi")  # "  Hi Python!  "
len(message)             # 17
```

**Important:** String methods return a **new string** --- they do not modify the original.

### Examples

**Example 3.5.1: String Manipulation**

```python
message = "  Hello Python  "
print(f"Original: '{message}'")
print(f"Length: {len(message)}")
print(f"Uppercase: '{message.upper()}'")
print(f"Stripped: '{message.strip()}'")
```

**Example 3.5.2: Combining Strings**

```python
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
```

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

### Skills Checklist

- [ ] I can combine strings using concatenation.
- [ ] I can find the length of a string using `len()`.
- [ ] I can convert a string to uppercase/lowercase.
- [ ] I can remove extra spaces using `.strip()`.
- [ ] I can replace parts of a string using `.replace()`.
