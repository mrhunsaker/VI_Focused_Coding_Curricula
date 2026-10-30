# Unit 1: Foundations of Computing and Getting Started with Python

## Overview

This unit covers basic computer science concepts, setting up the Python environment, and writing and executing simple Python programs.

**Objectives:**

- Understand what computer science is and how hardware relates to software.
- Write and run your first Python program.
- Use variables to store and manipulate simple data types.

---

## Lesson 1.1: Welcome to Computer Science

### Reading References

- Zelle: Chapter 1, pages 1--7
- Matthes: Chapter 1, pages 3--14

### What Is Computer Science?

A computer is a **universal machine** --- it can be programmed to solve any problem that can be broken down into a series of precise, logical steps. The true power of a computer doesn't come from its hardware but from the software we create.

**Computer science** is the study of problem-solving, not just programming. It's an interdisciplinary field involving breaking down complex problems, designing algorithms, and implementing efficient solutions.

### Hardware vs. Software

| Component        | Description                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| **Hardware**     | Physical components you can touch: keyboard, screen, processor, memory |
| **Software**     | Instructions that direct hardware: programs, operating systems, apps   |
| **CPU**          | The processor that executes instructions                               |
| **Memory (RAM)** | Temporary storage for active programs and data                         |
| **Storage**      | Permanent storage for files                                            |

**Analogy:** Think of a kitchen. The stove, refrigerator, and pots are **hardware**. A cookie recipe is **software** --- it provides precise steps for the "hardware" (the cook) to follow.

### Why Python?

Python is an ideal language for beginners because of its:

- **Readability** --- English-like syntax makes code easy to understand.
- **Simplicity** --- Less "boilerplate" code than other languages.
- **Versatility** --- Used in web development, data science, AI, and more.

### The Problem-Solving Approach

1. Understand the problem.
2. Break it down into smaller pieces.
3. Design a step-by-step solution (an algorithm).
4. Implement the solution in Python.
5. Test and refine your code.

### Activities

**Activity 1.1.1: "Human Computer" Role-Play**

- In pairs, one student is the "computer" and the other is the "programmer."
- The programmer provides simple, precise instructions for a common task (e.g., "make a peanut butter and jelly sandwich").
- The "computer" follows only what is literally said.
- Purpose: Illustrate the need for precise, unambiguous instructions.

**Activity 1.1.2: Identify Hardware and Software**

- List five items you use daily.
- For each, identify whether it is hardware or software and explain your choice.

### Skills Checklist

- [ ] I can define what computer science is.
- [ ] I can distinguish between computer hardware and software.
- [ ] I can explain what a computer program is.
- [ ] I can identify Python as a programming language.

---

## Lesson 1.2: Your First Python Program --- "Hello World!"

### Reading References

- Zelle: Chapter 1, pages 7--13
- Matthes: Chapter 1, pages 3--14

### The `print()` Function

The `print()` function is Python's primary method for displaying output to the user.

```python
print("Hello, World!")
```

**Expected output:**

```
Hello, World!
```

### Key Concepts

- **Strings** are text data enclosed in quotation marks (single or double).
- **Comments** start with `#` and are ignored by Python.
- Python executes code **line by line**, from top to bottom.

### Examples

**Example 1.2.1: Simple Greeting**

```python
# This program prints a classic greeting.
print("Hello, World!")
```

**Example 1.2.2: Personalized Message**

```python
# This program prints a message with your name.
print("Hello, Alice!")
print("Welcome to Python programming!")
```

Expected output:

```
Hello, Alice!
Welcome to Python programming!
```

### Common Mistakes

```python
print("Hello, World"        # Missing closing parenthesis --- SyntaxError
print "Hello"               # Python 2 style --- SyntaxError in Python 3
Print("Hello")              # Capital P --- NameError
```

### Activities

**Activity 1.2.1: My First Message**

1. Open VS Code and confirm the PythonProjects folder is open.
2. Create a new file as `my_message.py`.
3. Type:
   ```python
   print("My favorite color is blue.")
   print("My favorite animal is a dog.")
   ```
4. Save and run the file.

**Activity 1.2.2: Exploring Print Statements**

1. Experiment with:
   - Printing numbers: `print(123)`
   - Printing sentences with punctuation.
   - Omitting quotes: `print(Hello)` --- expect a `NameError`.

### Skills Checklist

- [ ] I can write a `print()` statement in Python.
- [ ] I can save a Python file with the `.py` extension.
- [ ] I can execute a Python script from the terminal.
- [ ] I understand that the output of `print()` appears in the terminal.

---

## Lesson 1.3: Variables and Simple Data Types

### Reading References

- Zelle: Chapter 2, pages 24--26
- Matthes: Chapter 2, pages 15--32

### What Is a Variable?

A **variable** is a name that refers to a value stored in the computer's memory. The **assignment operator** `=` creates a connection between a name and a value.

```python
age = 25
name = "Alice"
height = 5.6
```

**Rules for variable names:**

- Must start with a letter or underscore
- Can only contain letters, digits, and underscores
- Are case-sensitive (`age` is different from `Age`)
- Cannot be a Python keyword (`if`, `for`, `while`, etc.)

**Best practices:**

- Use descriptive names: `student_count`, not `sc`
- Use lowercase with underscores: `first_name`

### Essential Data Types

| Type             | Description           | Examples              |
| ---------------- | --------------------- | --------------------- |
| `str` (String)   | Text data             | `"hello"`, `"Python"` |
| `int` (Integer)  | Whole numbers         | `10`, `-5`, `0`       |
| `float` (Float)  | Numbers with decimals | `3.14`, `9.99`        |
| `bool` (Boolean) | True or False         | `True`, `False`       |

### Examples

**Example 1.3.1: Storing and Printing a String**

```python
student_name = "Charlie"
print("Hello, " + student_name + "!")
```

Output:

```
Hello, Charlie!
```

**Example 1.3.2: Storing and Printing Numbers**

```python
apple_count = 5
orange_count = 3
total_fruit = apple_count + orange_count
print("You have", total_fruit, "fruits in total.")

price_per_item = 2.50
quantity = 4
total_cost = price_per_item * quantity
print("The total cost is:", total_cost)
```

Output:

```
You have 8 fruits in total.
The total cost is: 10.0
```

### Common Errors

```python
2nd_number = 10         # Invalid variable name --- starts with digit
print("Result: " + 42)  # TypeError --- can't concatenate str and int
```

### Activities

**Activity 1.3.1: Personal Information Variables**

```python
my_name = "Jamie"
favorite_number = 7
height_in_meters = 1.75
favorite_food = "pizza"

print("My name is:", my_name)
print("My favorite number is:", favorite_number)
print("My height is:", height_in_meters, "meters")
print("My favorite food is:", favorite_food)
```

**Activity 1.3.2: Simple Math Challenge**

```python
num1 = 15
num2 = 7
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
```

### Key Table: Python Data Types and Operations

| Data Type | Description            | Example Value         | Common Operations                        |
| --------- | ---------------------- | --------------------- | ---------------------------------------- |
| `str`     | Text, words, sentences | `"Hello"`, `"Python"` | `+` (concatenation), `len()`, `.upper()` |
| `int`     | Whole numbers          | `10`, `-5`, `0`       | `+`, `-`, `*`, `/`, `%`                  |
| `float`   | Numbers with decimals  | `3.14`, `9.99`, `0.0` | `+`, `-`, `*`, `/`                       |

### Skills Checklist

- [ ] I can define what a variable is in programming.
- [ ] I can create a valid variable name in Python.
- [ ] I can assign string, integer, and float values to variables.
- [ ] I can use `print()` to display the value of a variable.
- [ ] I can perform basic arithmetic operations with numbers in Python.
