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

### Adding and Removing Elements

```python
my_list = [10, 20, 30]

my_list.append(40)          # Add to end → [10, 20, 30, 40]
my_list.insert(1, 15)       # Insert at index 1 → [10, 15, 20, 30, 40]
del my_list[0]              # Delete by index → [15, 20, 30, 40]
removed = my_list.pop()     # Remove and return last → removed=40, list=[15, 20, 30]
my_list.remove(20)          # Remove by value → [15, 30]
```

### Example

```python
todo_list = ["Buy groceries", "Walk the dog"]

todo_list.append("Call grandma")
todo_list.insert(0, "Wake up early")
del todo_list[1]
completed_task = todo_list.pop()
todo_list.remove("Walk the dog")
print(todo_list)
```

### Skills Checklist
- [ ] I can add an item to the end of a list using `.append()`.
- [ ] I can insert an item at a specific position using `.insert()`.
- [ ] I can remove an item by index using `del`.
- [ ] I can remove an item and retrieve its value using `.pop()`.
- [ ] I can remove the first occurrence of a value using `.remove()`.

---

## Lesson 4.2: Organizing Lists

### Sorting and Reversing

```python
numbers = [5, 2, 9, 1]
numbers.sort()                          # Permanent sort in-place
print(numbers)                          # [1, 2, 5, 9]

fruits = ["orange", "apple", "banana"]
sorted_fruits = sorted(fruits)          # Temporary sort — original unchanged
print(fruits)                           # ['orange', 'apple', 'banana']
print(sorted_fruits)                    # ['apple', 'banana', 'orange']

numbers.reverse()                       # Reverse in-place
numbers.sort(reverse=True)              # Sort descending
print(len(numbers))                     # Length
```

### Skills Checklist
- [ ] I can sort a list permanently using `.sort()`.
- [ ] I can get a temporarily sorted version using `sorted()`.
- [ ] I can reverse a list using `.reverse()`.
- [ ] I can find how many items are in a list using `len()`.

---

## Lesson 4.3: Tuples — Immutable Lists

### Tuples

Tuples are defined with parentheses and **cannot be changed** after creation.

```python
coordinates = (10, 20, 30)
print(coordinates[0])     # 10
print(coordinates[-1])    # 30

# This would cause a TypeError:
# coordinates[1] = 25
```

**When to use tuples:** For data that should remain constant (coordinates, RGB values, fixed settings).

### Skills Checklist
- [ ] I can create a tuple in Python.
- [ ] I can explain the main difference between a list and a tuple (mutability).
- [ ] I can access items in a tuple by their index.

---

## Lesson 4.4: Introducing Dictionaries

### Reading References
- Zelle: Chapter 11, pages 307–309
- Matthes: Chapter 6, pages 91–98

### Dictionary Basics

A dictionary stores **key-value pairs**. Keys must be unique and immutable (strings, numbers, tuples). Values can be anything.

```python
student_profile = {
    "name": "Emily",
    "age": 13,
    "grade": "7th",
    "favorite_subject": "Science"
}

print(student_profile["name"])      # "Emily"
student_profile["city"] = "Springfield"   # Add new key
student_profile["age"] = 14              # Modify existing key
del student_profile["grade"]             # Remove key
```

### Examples

**Example 4.4.1: Book Information Dictionary**
```python
my_book = {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "publication_year": 1979,
    "genre": "Science Fiction"
}

print(f"Title: {my_book['title']}")
print(f"Author: {my_book['author']}")

my_book["number_of_pages"] = 193
my_book["genre"] = "Comedy Science Fiction"
print(my_book)
```

### Skills Checklist
- [ ] I can create a dictionary in Python.
- [ ] I can explain what a key-value pair is.
- [ ] I can access a value in a dictionary using its key.
- [ ] I can add, modify, and remove key-value pairs.

---

## Lesson 4.5: Looping Through Dictionaries

### Dictionary Iteration Methods

```python
inventory = {"apples": 50, "bananas": 30, "oranges": 40}

# Loop through keys (default)
for item_name in inventory:
    print(item_name)

# Loop through values only
for count in inventory.values():
    print(count)

# Loop through key-value pairs
for item_name, count in inventory.items():
    print(f"{item_name}: {count} in stock")
```

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

### Key Reminder

`input()` **always returns a string**. Convert to numeric types as needed.

```python
age_input = input("How old are you? ")
print(f"Type: {type(age_input)}")    # <class 'str'>

age_int = int(age_input)
print(f"In 5 years: {age_int + 5}")
```

### Skills Checklist
- [ ] I can effectively use `input()` to get user data.
- [ ] I can confirm that `input()`'s return value is always a string.
- [ ] I can convert user input to a numeric type when necessary.

---

## Lesson 5.2: The `while` Loop in Action

### `for` vs. `while` Loop Comparison

| Feature | `for` Loop | `while` Loop |
|---------|-----------|--------------|
| **Purpose** | Definite iteration (known count) | Indefinite iteration (condition-based) |
| **When to Use** | Iterating over lists, ranges | Repeating until a condition is met |
| **Control Variable** | Automatically updated | Must be manually updated |
| **Risk** | Less prone to infinite loops | High risk if condition never becomes false |

### Examples

**Example 5.2.1: Simple Counter**
```python
count = 1
while count <= 5:
    print(count)
    count += 1
print("Counting finished!")
```

**Example 5.2.2: User Input Loop (Sentinel Value)**
```python
message = ""
while message != 'quit':
    message = input("Enter a message, or type 'quit' to exit: ")
    if message != 'quit':
        print(f"You said: {message}")
print("Goodbye!")
```

### Skills Checklist
- [ ] I can explain the difference between a `for` loop and a `while` loop.
- [ ] I can write a basic `while` loop.
- [ ] I can make sure my `while` loop has a way to stop.

---

## Lesson 5.3: Using Flags and `break` to Exit Loops

### Flag Variable

```python
active = True
while active:
    message = input("Say something (or 'quit' to stop): ")
    if message == 'quit':
        active = False
    else:
        print(f"You said: {message}")
```

### `break` Statement

```python
while True:
    city = input("Enter a city (or 'done' to finish): ")
    if city == 'done':
        break
    print(f"I've heard {city} is a great place!")
```

### Skills Checklist
- [ ] I can use a Boolean "flag" variable to control a `while` loop.
- [ ] I can use the `break` statement to exit a loop early.

---

## Lesson 5.4: Using `continue` in Loops

### `continue` — Skip the Current Iteration

```python
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue        # Skip even numbers
    print(number)       # Prints 1, 3, 5, 7, 9
```

### `continue` vs. `break`

- `break` — **exits the loop entirely**
- `continue` — **skips only the current iteration**, loop continues

### Skills Checklist
- [ ] I can use `continue` to skip the rest of the current loop iteration.
- [ ] I can identify scenarios where `continue` would be useful.

---

## Lesson 5.5: Avoiding Infinite Loops

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

### Function Syntax

```python
def function_name(parameter1, parameter2):
    """Docstring describing what the function does."""
    # Function body
    print(f"Hello, {parameter1}!")
```

### Examples

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

greet_name("Alice")
greet_name("Bob")
```

### Skills Checklist
- [ ] I can explain why functions are useful.
- [ ] I can define a simple function in Python.
- [ ] I can use parameters to specify function inputs.
- [ ] I can call a function by its name.

---

## Lesson 6.2: Passing Arguments

### Positional vs. Keyword Arguments

```python
def describe_animal(animal_type, animal_name):
    print(f"I have a {animal_type} named {animal_name}.")

# Positional arguments (order matters)
describe_animal("dog", "Buddy")

# Keyword arguments (order doesn't matter)
describe_animal(animal_name="Max", animal_type="cat")
```

### Default Values

```python
def make_shirt(size, message="I love Python"):
    print(f"Making a {size}-sized shirt: '{message}'")

make_shirt("large")                       # Uses default message
make_shirt("medium", "Hello World")       # Custom message
```

### Skills Checklist
- [ ] I can differentiate between a parameter and an argument.
- [ ] I can pass arguments using positional order.
- [ ] I can pass arguments using keyword arguments.

---

## Lesson 6.3: Return Values

### The `return` Statement

```python
def add_numbers(num1, num2):
    """Adds two numbers and returns the result."""
    total = num1 + num2
    return total

result = add_numbers(5, 3)
print(f"The sum is: {result}")   # 8
```

**Key difference:** `print()` displays a value; `return` sends a value back to the caller for further use.

### Skills Checklist
- [ ] I can use `return` to send a value back from a function.
- [ ] I can explain the difference between `print()` and `return`.
- [ ] I can store the returned value of a function in a variable.

---

## Lesson 6.4: Functions with Lists and Dictionaries

Since lists are **mutable**, modifying them inside a function changes the original:

```python
def add_new_user(user_list, new_user):
    user_list.append(new_user)

users = ['Alice', 'Bob']
add_new_user(users, 'Charlie')
print(users)   # ['Alice', 'Bob', 'Charlie']
```

To prevent modification, pass a copy:
```python
add_new_user(users[:], 'Charlie')   # Original unchanged
```

### Skills Checklist
- [ ] I can pass a list or dictionary as an argument to a function.
- [ ] I understand that modifying a list inside a function affects the original.
- [ ] I can create a copy of a list to avoid unintended modifications.

---

## Lesson 6.5: Arbitrary Number of Arguments

### `*args` — Arbitrary Positional Arguments

```python
def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with:")
    for topping in toppings:
        print(f"  - {topping}")

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
```

### `**kwargs` — Arbitrary Keyword Arguments

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

### Skills Checklist
- [ ] I can define a function using `*args` for arbitrary positional arguments.
- [ ] I can define a function using `**kwargs` for arbitrary keyword arguments.
