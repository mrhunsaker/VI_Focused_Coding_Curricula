# Unit 2: Writing Simple Programs and Numeric Computations

## Overview

**Compatibility:** All code examples in this curriculum target Python 3.12 and newer. The course avoids syntax and APIs introduced after Python 3.12.

This unit explores the software development process, more complex numeric operations, and how to obtain and use input from users.

**Objectives:**
- Understand the phases of software development.
- Work with different numeric data types (integers, floats).
- Perform type conversions.
- Use mathematical operators and the math library.
- Get user input with `input()`.

---

## Lesson 2.1: The Software Development Process

### Reading References
- Zelle: Chapter 2, pages 21–22 and pages 35–36

### The Three-Phase Development Process

**1. Design (Plan first)**
Before writing any code, fully understand the problem:
- Identify **inputs** (information the program needs) and **outputs** (results it must produce).
- Write an **algorithm** — a step-by-step plan in plain English (**pseudocode**).
- Consider **edge cases** — unusual inputs that might break your program.

**2. Implement (Write the code)**
- Translate your design into Python syntax.
- Code **incrementally** — build in small pieces and test as you go.
- Follow coding standards and use descriptive variable names.

**3. Test and Debug (Verify it works)**
- Run with a variety of inputs, including normal values and edge cases.
- Read error messages carefully — they tell you the type of error and the line number.
- Use `print()` statements to check variable values during debugging.

### Why This Process Matters

- **Reduces frustration** — Having a plan prevents getting stuck.
- **Improves code quality** — A thoughtful design leads to cleaner code.
- **Simplifies debugging** — Test each component in isolation.
- **Saves time** — Good design prevents time-consuming rewrites.

### Activities

**Activity 2.1.1: Planning a Tip Calculator**
Write pseudocode before coding:
```
1. GET bill amount from user
2. CALCULATE tip as 15% of bill amount
3. CALCULATE total amount (bill + tip)
4. PRINT tip amount
5. PRINT total amount
```

**Activity 2.1.2: Tracing a Simple Program**
Without running the code, trace the execution and predict output:
```python
a = 10
b = 5
c = a * b
a = a + 2
print(c)
print(a)
```

### Skills Checklist
- [ ] I can describe the purpose of the software development process.
- [ ] I can list and briefly explain the main phases of software development.
- [ ] I understand that problem-solving and design happen before writing code.

---

## Lesson 2.2: Elements of Programs — Expressions and Assignment

### Reading References
- Zelle: Chapter 2, pages 24–26

### Expressions and Assignment

An **expression** is any combination of values, variables, and operators that evaluates to a single result. Python follows the standard mathematical order of operations (PEMDAS).

```python
result1 = 10 / 2 + 3  # 10/2 is 5, then 5+3 = 8.0
message = "Python" + " " + "is fun!"
```

**Assignment:**
```python
score = 50
score = score + 20  # score is now 70
```

### Examples

**Example 2.2.1: Expression Evaluation**
```python
result1 = 10 / 2 + 3
print("Result 1:", result1)   # Output: Result 1: 8.0

message = "Python" + " " + "is fun!"
print("Message:", message)    # Output: Message: Python is fun!
```

**Example 2.2.2: Reassigning Variables**
```python
score = 50
print("Initial score:", score)
score = score + 20
print("New score:", score)     # Output: New score: 70
```

### Skills Checklist
- [ ] I can identify an expression in Python code.
- [ ] I can predict the result of simple Python expressions.
- [ ] I can explain how the assignment operator `=` works.
- [ ] I can demonstrate how to update a variable's value.

---

## Lesson 2.3: Input and Output Revisited

### Reading References
- Zelle: Chapter 2, pages 27–33
- Matthes: Chapter 7, pages 114–116

### The `input()` Function

The `input()` function pauses program execution and waits for the user to type something and press Enter. **It always returns a string.**

```python
user_name = input("What is your name? ")
print(f"Hello, {user_name}! Nice to meet you.")
```

### F-Strings (Formatted String Literals)

F-strings provide a clean way to embed variable values directly into a string:

```python
name = "Alice"
age = 30
print(f"Hello, {name}! You are {age} years old.")
```

### Converting Input for Calculations

Since `input()` always returns a string, you must convert it for math:

```python
age_str = input("How old are you? ")
age_int = int(age_str)
print(f"Next year you will be {age_int + 1} years old.")
```

### Examples

**Example 2.3.1: Basic Input**
```python
user_name = input("What is your name? ")
print(f"Hello, {user_name}! Nice to meet you.")
```

**Example 2.3.2: Numeric Input and Calculation**
```python
num1_str = input("Enter the first number: ")
num1 = int(num1_str)

num2_str = input("Enter the second number: ")
num2 = int(num2_str)

sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")
```

### Activities

**Activity 2.3.1: Temperature Converter**
```python
fahrenheit_str = input("Enter temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F is {celsius:.2f}°C")
```

### Skills Checklist
- [ ] I can use the `input()` function to ask the user for information.
- [ ] I can provide a clear prompt message when using `input()`.
- [ ] I remember that `input()` returns a string, even for numbers.
- [ ] I can combine text and variable values in a `print()` statement using f-strings.

---

## Lesson 2.4: Computing with Numbers and Type Conversions

### Reading References
- Zelle: Chapter 3, pages 41–48
- Matthes: Chapter 2, pages 26–28

### Integers and Floats

| Type | Description | Example |
|------|-------------|---------|
| `int` | Whole numbers (exact) | `5`, `-20`, `1000000` |
| `float` | Numbers with decimals | `3.14`, `-2.5`, `6.0` |

**Key behaviors:**
- Division `/` always returns a float: `10 / 2` → `5.0`
- Floor division `//` returns the integer part: `10 // 3` → `3`
- Mixed operations promote to float: `10 + 3.5` → `13.5`

### Type Conversion Functions

```python
int("123")      # → 123  (truncates: int(3.9) → 3)
float("3.14")   # → 3.14
str(42)         # → "42"
```

### Examples

**Example 2.4.1: Type Conversion**
```python
num_str = "123"
num_int = int(num_str)
print(f"String '{num_str}' as integer: {num_int}, type: {type(num_int)}")

num_float = float(num_str)
print(f"String '{num_str}' as float: {num_float}, type: {type(num_float)}")

my_number = 42
my_text = str(my_number)
print(f"Integer {my_number} as string: '{my_text}', type: {type(my_text)}")
```

**Common Type Error:**
```python
# This will cause a TypeError:
# print("My age is " + 14)
# Fix: print("My age is " + str(14))
# Or: print(f"My age is {14}")
```

### Activities

**Activity 2.4.1: Mixed Bag Calculator**
```python
age_str = input("Enter your age: ")
age = int(age_str)

weight_str = input("Enter your weight in kg: ")
weight = float(weight_str)

phrase = input("Enter a short phrase: ")

print(f"Age doubled: {age * 2}")
print(f"Weight + age: {weight + age}")
print(f"Phrase length: {len(phrase)} characters")
```

### Skills Checklist
- [ ] I can identify when to use an integer versus a float.
- [ ] I can convert a string to an integer using `int()`.
- [ ] I can convert a string to a float using `float()`.
- [ ] I can convert a number to a string using `str()`.
- [ ] I can apply type conversions to perform calculations on user input.
- [ ] I understand and can apply the order of operations.

---

## Lesson 2.5: Using the Math Library

### Reading References
- Zelle: Chapter 3, pages 49–51

### Importing the Math Module

```python
import math
```

### Key Math Functions and Constants

| Function/Constant | Description | Example |
|-------------------|-------------|---------|
| `math.pi` | π ≈ 3.14159 | `math.pi` |
| `math.e` | e ≈ 2.71828 | `math.e` |
| `math.sqrt(x)` | Square root of x | `math.sqrt(25)` → `5.0` |
| `math.pow(x, y)` | x raised to power y | `math.pow(2, 4)` → `16.0` |
| `math.ceil(x)` | Round up | `math.ceil(4.2)` → `5` |
| `math.floor(x)` | Round down | `math.floor(4.8)` → `4` |
| `math.log(x, base)` | Logarithm | `math.log(100, 10)` → `2.0` |
| `math.sin(x)` | Sine (in radians) | `math.sin(math.pi/2)` → `1.0` |
| `math.radians(deg)` | Convert degrees to radians | `math.radians(90)` |

### Examples

**Example 2.5.1: Circle Calculations**
```python
import math

radius = 5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area of circle with radius {radius}: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

number = 81
square_root = math.sqrt(number)
print(f"Square root of {number}: {square_root}")
```

### Activities

**Activity 2.5.1: Circle Calculator**
```python
import math

radius_str = input("Enter the radius: ")
radius = float(radius_str)

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
```

**Activity 2.5.2: Distance Finder**
```python
import math

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
distance = math.sqrt(x**2 + y**2)
print(f"Distance from origin: {distance:.2f}")
```

### Skills Checklist
- [ ] I can explain what a Python module is.
- [ ] I can import the `math` module into my program.
- [ ] I can use `math.pi` and `math.sqrt()`.
- [ ] I can use `math.ceil()` to round up and `math.floor()` to round down.

## Canonical Shared Dataset — Calculator and Coordinates

Use the canonical bill and tip rate in every parallel-language implementation.

```python
from decimal import Decimal, ROUND_HALF_UP

bill = Decimal("24.50")
tip_rate = Decimal("0.15")
tip = (bill * tip_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
total = bill + tip
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
```

Expected output:
```text
Tip: $3.67
Total: $28.18
```

Use the same coordinate values for the math-library example:

```python
import math
x, y = 3, 4
distance = math.sqrt(x**2 + y**2)
print(distance)
```

Expected output: `5.0`. The shared monetary contract rounds the tip to cents using decimal half-up rounding before adding it to the bill. Use decimal arithmetic rather than binary floating-point formatting for currency.
