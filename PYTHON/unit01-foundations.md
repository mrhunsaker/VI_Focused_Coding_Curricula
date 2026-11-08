# Unit 1: Foundations of Computing and Getting Started with Python

## Overview

**Compatibility:** All code examples in this curriculum target Python 3.12 and newer. The course avoids syntax and APIs introduced after Python 3.12.

This unit covers basic computer science concepts, setting up the Python environment, and writing and executing simple Python programs.

**Objectives:**
- Understand what computer science is and how hardware relates to software.
- Write and run your first Python program.
- Use variables to store and manipulate simple data types.

---

## Lesson 1.1: Welcome to Computer Science

### Reading References
- Zelle: Chapter 1, pages 1–7
- Matthes: Chapter 1, pages 3–14

### Learning Objectives
- Define what computer science is.
- Distinguish between computer hardware and software.
- Explain what a computer program is.
- Identify Python as a programming language.

### Concept Explanation

#### What Is Computer Science?

A computer is a **universal machine** — it can be programmed to solve any problem that can be broken down into a series of precise, logical steps. The true power of a computer doesn't come from its hardware but from the software we create.

**Computer science** is the study of problem-solving, not just programming. It's an interdisciplinary field involving breaking down complex problems, designing algorithms, and implementing efficient solutions.

#### Hardware vs. Software

| Component | Description |
|-----------|-------------|
| **Hardware** | Physical components you can touch: keyboard, screen, processor, memory |
| **Software** | Instructions that direct hardware: programs, operating systems, apps |
| **CPU** | The processor that executes instructions |
| **Memory (RAM)** | Temporary storage for active programs and data |
| **Storage** | Permanent storage for files |

**Analogy:** Think of a kitchen. The stove, refrigerator, and pots are **hardware**. A cookie recipe is **software** — it provides precise steps for the "hardware" (the cook) to follow.

#### Why Python?

Python is an ideal language for beginners because of its:
- **Readability** — English-like syntax makes code easy to understand.
- **Simplicity** — Less "boilerplate" code than other languages.
- **Versatility** — Used in web development, data science, AI, and more.

#### The Problem-Solving Approach

1. Understand the problem.
2. Break it down into smaller pieces.
3. Design a step-by-step solution (an algorithm).
4. Implement the solution in Python.
5. Test and refine your code.

### Worked Example

The problem-solving approach applied to a small task: find the total and average of the shared scores 82, 91, 76, and 88.

Algorithm in plain steps: set the total to 0; for each score, add it to the total; divide the total by the number of scores; report both.

```python
scores = [82, 91, 76, 88]
total = 0
for score in scores:
    total = total + score
average = total / len(scores)
print("Total:", total)
print("Average:", average)
```

### Expected Behavior or Output

Output of example 1:
```
Total: 337
Average: 84.25
```

### Common Mistakes

1. Writing code before writing the steps, then forgetting to divide by the number of scores.
2. Confusing the program with the algorithm. The algorithm is the plan; the program is one way of carrying it out.
3. Expecting a computer to fill in a step you did not state.

### Activities

**Activity 1.1.1: "Human Computer" Role-Play**
- In pairs, one student is the "computer" and the other is the "programmer."
- The programmer provides simple, precise instructions for a common task (e.g., "make a peanut butter and jelly sandwich").
- The "computer" follows only what is literally said.
- Purpose: Illustrate the need for precise, unambiguous instructions.

**Activity 1.1.2: Identify Hardware and Software**
- List five items you use daily.
- For each, identify whether it is hardware or software and explain your choice.

### Accessibility Practice

Write the plain-language steps as a numbered list and read it back with your screen reader before coding. Trace the loop by hand as numbered sentences (82, then 173, then 249, then 337) rather than as a table, so every state is read in order.

### Skills Checklist

- [ ] I can define what computer science is.
- [ ] I can distinguish between computer hardware and software.
- [ ] I can explain what a computer program is.
- [ ] I can identify Python as a programming language.

---

## Lesson 1.2: Your First Python Program — "Hello World!"

### Reading References
- Zelle: Chapter 1, pages 7–13
- Matthes: Chapter 1, pages 3–14

### Learning Objectives
- Write a `print()` statement in Python.
- Save a Python file with the `.py` extension.
- Execute a Python script from the terminal.
- Understand that the output of `print()` appears in the terminal.

### Concept Explanation

#### The `print()` Function

The `print()` function is Python's primary method for displaying output to the user.

```python
print("Hello, World!")
```

**Expected output:**
```
Hello, World!
```

#### Key Concepts

- **Strings** are text data enclosed in quotation marks (single or double).
- **Comments** start with `#` and are ignored by Python.
- Python executes code **line by line**, from top to bottom.

### Worked Example

**Example 1.2.1: Simple Greeting**
```python
# This program prints a classic greeting.
print("Hello, World!")
```

**Example 1.2.2: Personalized Message**
```python
# This program prints a message with your name.
print("Hello, Avery!")
print("Welcome to Python programming!")
```

### Expected Behavior or Output

Expected output:
```
Hello, Avery!
Welcome to Python programming!
```

### Common Mistakes

```python
print("Hello, World"        # Missing closing parenthesis — SyntaxError
print "Hello"               # Python 2 style — SyntaxError in Python 3
Print("Hello")              # Capital P — NameError
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
   - Omitting quotes: `print(Hello)` — expect a `NameError`.

### Accessibility Practice

Run the file from the terminal and read the output line by line. Check that your screen reader announces the quotation marks and parentheses in `print("Hello, Avery!")`, because a missing closing quotation mark is the most common first error. If the error message is long, jump to its last line, which names the problem.

### Skills Checklist

- [ ] I can write a `print()` statement in Python.
- [ ] I can save a Python file with the `.py` extension.
- [ ] I can execute a Python script from the terminal.
- [ ] I understand that the output of `print()` appears in the terminal.

---

## Lesson 1.3: Variables and Simple Data Types

### Reading References
- Zelle: Chapter 2, pages 24–26
- Matthes: Chapter 2, pages 15–32

### Learning Objectives
- Define what a variable is in programming.
- Create a valid variable name in Python.
- Assign string, integer, and float values to variables.
- Use `print()` to display the value of a variable.
- Perform basic arithmetic operations with numbers in Python.

### Concept Explanation

#### What Is a Variable?

A **variable** is a name that refers to a value stored in the computer's memory. The **assignment operator** `=` creates a connection between a name and a value.

```python
name = "Avery"
age = 16
height = 1.72
favorite_subject = "Computer Science"
```

**Rules for variable names:**
- Must start with a letter or underscore
- Can only contain letters, digits, and underscores
- Are case-sensitive (`age` is different from `Age`)
- Cannot be a Python keyword (`if`, `for`, `while`, etc.)

**Best practices:**
- Use descriptive names: `student_count`, not `sc`
- Use lowercase with underscores: `first_name`

#### Essential Data Types

| Type | Description | Examples |
|------|-------------|---------|
| `str` (String) | Text data | `"hello"`, `"Python"` |
| `int` (Integer) | Whole numbers | `10`, `-5`, `0` |
| `float` (Float) | Numbers with decimals | `3.14`, `9.99` |
| `bool` (Boolean) | True or False | `True`, `False` |

#### Key Table: Python Data Types and Operations

| Data Type | Description | Example Value | Common Operations |
|-----------|-------------|---------------|------------------|
| `str` | Text, words, sentences | `"Hello"`, `"Python"` | `+` (concatenation), `len()`, `.upper()` |
| `int` | Whole numbers | `10`, `-5`, `0` | `+`, `-`, `*`, `/`, `%` |
| `float` | Numbers with decimals | `3.14`, `9.99`, `0.0` | `+`, `-`, `*`, `/` |

### Worked Example

**Example 1.3.1: Storing and Printing a String**
```python
student_name = "Avery"
print("Hello, " + student_name + "!")
```


**Example 1.3.2: The Shared Student Profile and Notebook Cost**
The same student profile and inventory item are used in every language track, so you can compare how each language declares the same data.
```python
name = "Avery"
age = 16
height = 1.72
favorite_subject = "Computer Science"

print("Name:", name)
print("Age:", age)
print("Height in meters:", height)
print("Favorite subject:", favorite_subject)
print(type(name), type(age), type(height), type(favorite_subject))

notebook_price = 2.50
notebook_quantity = 3
notebook_total = notebook_price * notebook_quantity
print("Notebook total:", notebook_total)
```


Python decides each variable's type from the value you assign (dynamic typing). `type()` reports it: `str`, `int`, `float`, `str`.

### Expected Behavior or Output

Output:
```
Hello, Avery!
```

Expected output:
```
Name: Avery
Age: 16
Height in meters: 1.72
Favorite subject: Computer Science
<class 'str'> <class 'int'> <class 'float'> <class 'str'>
Notebook total: 7.5
```

### Common Mistakes

```python
2nd_number = 10         # Invalid variable name — starts with digit
print("Result: " + 42)  # TypeError — can't concatenate str and int
```

### Activities

**Activity 1.3.1: Personal Information Variables**
```python
my_name = "Avery"
favorite_number = 7
height_in_meters = 1.72
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

### Accessibility Practice

Say variable names aloud with their underscores (`favorite_subject`) and listen for the pause so you can tell one name from two words. Print each value on its own labelled line so the screen reader announces the name and the value together, and avoid relying on the spacing between printed items.

### Skills Checklist

- [ ] I can define what a variable is in programming.
- [ ] I can create a valid variable name in Python.
- [ ] I can assign string, integer, and float values to variables.
- [ ] I can use `print()` to display the value of a variable.
- [ ] I can perform basic arithmetic operations with numbers in Python.


## Canonical Shared Dataset — Student Profile

The parallel-language courses use the same student record. Keep these values unchanged when translating the example into another language.

```python
student_profile = {
    "name": "Avery",
    "age": 16,
    "height_m": 1.72,
    "favorite_subject": "Computer Science",
}
print(student_profile["name"])
print(student_profile["age"])
print(student_profile["height_m"])
print(student_profile["favorite_subject"])
```

Expected output:
```text
Avery
16
1.72
Computer Science
```

Use this record in place of unrelated personal-profile values in parallel-track comparison exercises. The earlier Hello World example remains a minimal first-program demonstration.
