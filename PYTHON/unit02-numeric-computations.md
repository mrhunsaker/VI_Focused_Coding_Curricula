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

### Learning Objectives
- Describe the purpose of the software development process.
- List and briefly explain the main phases of software development.
- Understand that problem-solving and design happen before writing code.

### Concept Explanation

#### The Three-Phase Development Process

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

#### Why This Process Matters

- **Reduces frustration** — Having a plan prevents getting stuck.
- **Improves code quality** — A thoughtful design leads to cleaner code.
- **Simplifies debugging** — Test each component in isolation.
- **Saves time** — Good design prevents time-consuming rewrites.

### Worked Example

Implement the pseudocode from the activity below with the shared values (bill 24.50, tip rate 0.15):
```python
bill = 24.5
tip_rate = 0.15

tip = bill * tip_rate
total = bill + tip

print(f"Bill: {bill:.2f}")
print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
```

### Expected Behavior or Output

Output of example 1:
```
Bill: 24.50
Tip: 3.67
Total: 28.18
```

### Common Mistakes

1. Writing the rate as 15 instead of 0.15, which makes the tip fifteen times too large.
2. Rounding the tip before adding it to the bill, which can change the total by a cent.
3. Skipping tests for a zero bill or a negative bill.

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

Trace this plan with the shared calculator values: the bill is 24.50 and the tip rate is 0.15. The tip is 24.50 × 0.15 = 3.675 and the total is 24.50 + 3.675 = 28.175. Shown with two decimal places, Python displays the tip as 3.67 and the total as 28.18, because 3.675 cannot be stored exactly in binary floating point. You will implement this plan in Lesson 2.4.

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

### Accessibility Practice

Write the design steps as a numbered list and print every result on its own labelled line (`Tip: 3.67`), so a screen reader reads each result as one clear unit. Do not use alignment or spacing to convey meaning.

### Skills Checklist

- [ ] I can describe the purpose of the software development process.
- [ ] I can list and briefly explain the main phases of software development.
- [ ] I understand that problem-solving and design happen before writing code.

---

## Lesson 2.2: Elements of Programs — Expressions and Assignment

### Reading References
- Zelle: Chapter 2, pages 24–26

### Learning Objectives
- Identify an expression in Python code.
- Predict the result of simple Python expressions.
- Explain how the assignment operator `=` works.
- Demonstrate how to update a variable's value.

### Concept Explanation

#### Expressions and Assignment

An **expression** is any combination of values, variables, and operators that evaluates to a single result. Python follows the standard mathematical order of operations (PEMDAS).

```python
result1 = 10 / 2 + 3  # 10/2 is 5, then 5+3 = 8.0
message = "Python" + " " + "is fun!"
```

**Assignment:**
```python
score = 82
score = score + 9  # score is now 91
```

### Worked Example

**Example 2.2.1: Expression Evaluation**
```python
result1 = 10 / 2 + 3
print("Result 1:", result1)   # Output: Result 1: 8.0
print("Precedence:", 8 + 4 * 2)   # Output: Precedence: 16
print("Grouped:", (8 + 4) * 2)    # Output: Grouped: 24

message = "Python" + " " + "is fun!"
print("Message:", message)    # Output: Message: Python is fun!
```

**Example 2.2.2: Reassigning Variables**
```python
score = 82
print("Initial score:", score)
score = score + 9
print("New score:", score)     # Output: New score: 91
```

### Expected Behavior or Output

Output of example 1:
```
Result 1: 8.0
Precedence: 16
Grouped: 24
Message: Python is fun!
```

Output of example 2:
```
Initial score: 82
New score: 91
```

### Common Mistakes

1. Reading `=` as "equals". In an assignment it means "store the value on the right in the name on the left."
2. Forgetting that `/` always gives a float, so `10 / 2` is `5.0`, not `5`.
3. Expecting `8 + 4 * 2` to be 24. Multiplication happens first, so it is 16; use parentheses to change the order.

### Activities

1. Predict the value of `8 + 4 * 2`, `(8 + 4) * 2`, `7 // 2`, `7 % 2`, and `2 ** 3`, then check each in Python.
2. Start with `score = 82` and write two statements that raise it by 9 and then double it. Predict the result.
3. Join the strings `"Avery"` and `"Student"` with a space between them using `+`.
4. Explain, in two sentences, why `score = score + 9` is valid even though it looks like an impossible equation.

### Accessibility Practice

Say operators by name when reading code aloud: 'double star' for `**`, 'double slash' for `//`, 'percent' for `%`. Raise your screen reader's punctuation level while reading expressions so that parentheses and operators are all announced.

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

### Learning Objectives
- Use the `input()` function to ask the user for information.
- Provide a clear prompt message when using `input()`.
- Remember that `input()` returns a string, even for numbers.
- Combine text and variable values in a `print()` statement using f-strings.

### Concept Explanation

#### The `input()` Function

The `input()` function pauses program execution and waits for the user to type something and press Enter. **It always returns a string.**

```python
user_name = input("What is your name? ")
print(f"Hello, {user_name}! Nice to meet you.")
```

#### F-Strings (Formatted String Literals)

F-strings provide a clean way to embed variable values directly into a string:

```python
name = "Avery"
age = 16
print(f"Hello, {name}! You are {age} years old.")
```

#### Converting Input for Calculations

Since `input()` always returns a string, you must convert it for math:

```python
age_str = input("How old are you? ")
age_int = int(age_str)
print(f"Next year you will be {age_int + 1} years old.")
```

### Worked Example

**Example 2.3.1: Basic Input**
```python
user_name = input("What is your name? ")
print(f"Hello, {user_name}! Nice to meet you.")
```


**Example 2.3.2: Numeric Input and Calculation**
```python
user_name = input("Enter your name: ")

num1_str = input("Enter the first number: ")
num1 = int(num1_str)

num2_str = input("Enter the second number: ")
num2 = int(num2_str)

sum_result = num1 + num2
print(f"Hello, {user_name}!")
print(f"The sum of {num1} and {num2} is {sum_result}.")
```


If the user types text that is not a whole number, `int()` raises a `ValueError`. Lesson 8.3 shows how to handle that.

### Expected Behavior or Output

Sample run (typed input shown after each prompt):
```
What is your name? Avery
Hello, Avery! Nice to meet you.
```

Sample run (typed input shown after each prompt):
```
Enter your name: Avery
Enter the first number: 12
Enter the second number: 8
Hello, Avery!
The sum of 12 and 8 is 20.
```

### Common Mistakes

1. Forgetting that `input()` always returns text. `"12" + "8"` joins the text to make `"128"`, and does not add.
2. Calling `int()` on text that is not a whole number, which raises a `ValueError`.
3. Writing a prompt that does not say what to type, such as `input("> ")`.

### Activities

**Activity 2.3.1: Temperature Converter**
```python
fahrenheit_str = input("Enter temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F is {celsius:.2f}°C")
```

### Accessibility Practice

Write each prompt as a complete sentence that says what to enter, such as `Enter the first number: `, and end it with a space so the answer starts after it. Test the program with your screen reader to confirm the prompt is read before you start typing.

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

### Learning Objectives
- Identify when to use an integer versus a float.
- Convert a string to an integer using `int()`.
- Convert a string to a float using `float()`.
- Convert a number to a string using `str()`.
- Apply type conversions to perform calculations on user input.
- Understand and can apply the order of operations.

### Concept Explanation

#### Integers and Floats

| Type | Description | Example |
|------|-------------|---------|
| `int` | Whole numbers (exact) | `5`, `-20`, `1000000` |
| `float` | Numbers with decimals | `3.14`, `-2.5`, `6.0` |

**Key behaviors:**
- Division `/` always returns a float: `10 / 2` → `5.0`
- Floor division `//` returns the integer part: `10 // 3` → `3`
- Mixed operations promote to float: `10 + 3.5` → `13.5`

#### Type Conversion Functions

```python
int("123")      # → 123  (truncates: int(3.9) → 3)
float("3.14")   # → 3.14
str(42)         # → "42"
```

### Worked Example

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

**Example 2.4.2: Tip Calculator (shared calculator values)**
```python
bill = 24.5
tip_rate = 0.15

tip = bill * tip_rate
total = bill + tip

print(f"Bill: {bill:.2f}")
print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
```


The unrounded values are 3.675 and 28.175. Python's `:.2f` formatting displays 3.67 and 28.18. This is binary floating-point behavior, not a mistake in the program; other languages may round the tip to 3.68.

### Expected Behavior or Output

Expected output:
```
Bill: 24.50
Tip: 3.67
Total: 28.18
```

### Common Mistakes

1. Converting with `int()` and expecting rounding. `int(3.9)` is `3` because it removes the fraction.
2. Expecting `0.1 + 0.2` to equal exactly `0.3`. Floating-point numbers are approximations.
3. Forgetting to convert typed text before arithmetic, then seeing `TypeError` or joined text instead of a sum.

### Activities

**Activity 2.4.1: Mixed Bag Calculator**
```python
age_str = input("Enter your age: ")
age = int(age_str)

height_str = input("Enter your height in meters: ")
height = float(height_str)

phrase = input("Enter a short phrase: ")

print(f"Age doubled: {age * 2}")
print(f"Height in centimeters: {height * 100:.1f}")
print(f"Phrase length: {len(phrase)} characters")
```

Sample run (typed input shown after each prompt):
```
Enter your age: 16
Enter your height in meters: 1.72
Enter a short phrase: Computer Science
Age doubled: 32
Height in centimeters: 172.0
Phrase length: 16 characters
```

### Accessibility Practice

When printing floating-point results, format them (`:.2f`) so the screen reader reads a short number instead of a long unrounded one. Read the type names printed by `type()` aloud, and note that `<class 'int'>` is announced with its angle brackets.

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

### Learning Objectives
- Explain what a Python module is.
- Import the `math` module into my program.
- Use `math.pi` and `math.sqrt()`.
- Use `math.ceil()` to round up and `math.floor()` to round down.

### Concept Explanation

#### Importing the Math Module

```python
import math
```

#### Key Math Functions and Constants

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

### Worked Example

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

### Expected Behavior or Output

Output of example 1:
```
Area of circle with radius 5: 78.54
Circumference: 31.42
Square root of 81: 9.0
```

### Common Mistakes

1. Forgetting `import math`, so `math.sqrt` raises a `NameError`.
2. Writing `math.pi * radius * 2` for the area. The radius must be squared: `math.pi * radius ** 2`.
3. Expecting `math.sqrt(81)` to print `9`. It prints `9.0` because square roots are floats.

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

Sample run with the shared coordinates x = 3 and y = 4 (typed input shown after each prompt):
```
Enter x coordinate: 3
Enter y coordinate: 4
Distance from origin: 5.00
```

### Accessibility Practice

Round results with `:.2f` so the screen reader announces `78.54` rather than fifteen digits. Say the dotted names aloud ('math dot sqrt') and listen for the dot, since a missing dot is a common transcription mistake when reading code by ear.

### Skills Checklist

- [ ] I can explain what a Python module is.
- [ ] I can import the `math` module into my program.
- [ ] I can use `math.pi` and `math.sqrt()`.
- [ ] I can use `math.ceil()` to round up and `math.floor()` to round down.

---
