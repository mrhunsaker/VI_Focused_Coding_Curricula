# Unit 7: Classes and Object-Oriented Programming

## Overview

**Compatibility:** All examples target Python 3.12 and newer; they avoid syntax and standard-library APIs introduced after Python 3.12.

This unit introduces the fundamental concepts of Object-Oriented Programming (OOP) in Python, focusing on defining and using classes, attributes, methods, and inheritance.

**Objectives:**
- Define and instantiate classes.
- Work with attributes and methods.
- Understand inheritance and composition.

---

## Lesson 7.1: Why Learn About Classes?

### Reading References
- Zelle: Chapter 4, pages 65–67; Chapter 10, pages 247–248
- Matthes: Chapter 9, page 157

### Classes as Blueprints

A **class** is a blueprint or template for creating objects. An **object** is a concrete instance created from that blueprint.

**Analogy:** A "Car" class defines that every car has a `color` and a `speed` (attributes) and can `accelerate()` and `brake()` (methods). Your red sedan and your friend's blue pickup are two separate **objects** of the same "Car" class.

### Key OOP Concepts

- **Encapsulation** — Bundling data and methods into a single unit.
- **Abstraction** — Hiding complexity from the outside.
- **Inheritance** — New class reuses functionality of existing class.
- **Polymorphism** — Same method name behaves differently for different classes.

### Skills Checklist
- [ ] I can explain the basic idea of Object-Oriented Programming.
- [ ] I can describe a class as a blueprint and an object as an instance.

---

## Lesson 7.2: Creating and Using a Class

### Reading References
- Zelle: Chapter 10, pages 248–254
- Matthes: Chapter 9, pages 158–162

### Class Syntax

```python
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        print(f"A new dog named {self.name} has been created!")

# Create instances
my_dog = Dog("Buddy", 3)
your_dog = Dog("Lucy", 1)

print(f"My dog's name is {my_dog.name}.")
print(f"Your dog's name is {your_dog.name}.")
```

The `__init__()` method runs automatically when a new object is created. `self` refers to the specific instance being created.

### Skills Checklist
- [ ] I can define a basic Python class.
- [ ] I can define the `__init__` method within a class.
- [ ] I understand the purpose of the `self` parameter.
- [ ] I can create an instance (object) of a class.

---

## Lesson 7.3: Working with Attributes and Methods

### Reading References
- Matthes: Chapter 9, pages 162–166

### Calling Methods

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over."""
        print(f"{self.name} rolled over!")

    def get_older(self, years_to_add):
        """Add years to the dog's age."""
        self.age += years_to_add
        print(f"{self.name} is now {self.age} years old.")

my_dog = Dog("Buddy", 3)
my_dog.sit()
my_dog.roll_over()
my_dog.age = 4          # Direct attribute modification
my_dog.get_older(2)     # Method-based modification
```

### Skills Checklist
- [ ] I can access an object's attributes using dot notation.
- [ ] I can define and call methods within a class.
- [ ] I can use a method to change an object's attribute.

---

## Lesson 7.4: Inheritance

### Reading References
- Zelle: Chapter 12, pages 351–352
- Matthes: Chapter 9, pages 167–170

### Creating a Child Class

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)   # Call parent's __init__
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


my_ev = ElectricCar('ford', 'mustang mach e', 2023)
print(my_ev.get_descriptive_name())   # Inherited method
my_ev.describe_battery()              # New method
my_ev.read_odometer()                 # Inherited method
```

### `super()` Function

`super().__init__()` calls the parent class's `__init__()` method, ensuring inherited attributes are properly initialized.

### Skills Checklist
- [ ] I can define a child class that inherits from a parent class.
- [ ] I can use `super().__init__()` to properly initialize inherited attributes.
- [ ] I can add new attributes and methods to a child class.
- [ ] I can override a parent method in a child class.

---

## Lesson 7.5: Instances as Attributes (Composition)

### Composition — "Has-A" Relationship

Instead of inheriting, a class **contains an instance of another class** as an attribute.

```python
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range_miles = 260
        else:
            range_miles = 310
        print(f"About {range_miles} miles of range.")


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()   # Composition: ElectricCar HAS A Battery


my_ev = ElectricCar('ford', 'mustang mach e', 2023)
my_ev.battery.describe_battery()
my_ev.battery.get_range()
```

### Skills Checklist
- [ ] I can explain the concept of composition in OOP.
- [ ] I can create an instance of one class and assign it as an attribute of another.
- [ ] I can access attributes and methods of a nested object.

---

# Unit 8: Files and Exceptions

## Overview

This unit covers interacting with text files for reading and writing data, handling common errors gracefully using exceptions, and storing data using JSON.

**Objectives:**
- Read from and write to files.
- Handle exceptions with `try-except` blocks.
- Store and load data using JSON.

---

## Lesson 8.1: Reading from a File

### Reading References
- Zelle: Chapter 5, pages 125–127
- Matthes: Chapter 10, pages 184–189

### Reading Files

```python
# Reading entire file
with open('my_notes.txt', 'r') as file_object:
    contents = file_object.read()
print(contents)

# Reading line by line
with open('my_notes.txt', 'r') as file_object:
    for line in file_object:
        print(line.strip())

# Reading all lines into a list
with open('my_notes.txt', 'r') as file_object:
    lines = file_object.readlines()
```

The `with` statement **automatically closes the file** even if an error occurs.

### File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read (default) |
| `'w'` | Write (creates new or overwrites) |
| `'a'` | Append (adds to end) |

### Skills Checklist
- [ ] I can open a file for reading using `with open()`.
- [ ] I can read the entire content of a file into a string.
- [ ] I can read a file line by line using a `for` loop.
- [ ] I can remove whitespace/newlines using `.strip()`.

---

## Lesson 8.2: Writing to a File

### Reading References
- Zelle: Chapter 5, pages 127–128
- Matthes: Chapter 10, pages 190–192

```python
# Write mode (overwrites existing content)
with open('programming_message.txt', 'w') as f:
    f.write("I love programming in Python!\n")

# Append mode (adds to end)
with open('programming_message.txt', 'a') as f:
    f.write("It's a very versatile language.\n")
    f.write("I'm excited to learn more!\n")
```

**Important:** The `.write()` method does not add newlines automatically. Use `\n`.

### Skills Checklist
- [ ] I can open a file for writing using `"w"` mode.
- [ ] I can open a file for appending using `"a"` mode.
- [ ] I can write a string to a file.
- [ ] I can add newlines to a file using `\n`.

---

## Lesson 8.3: Exceptions — Handling Errors

### Reading References
- Zelle: Chapter 7, pages 177–179
- Matthes: Chapter 10, pages 192–199

### `try-except` Block

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
print("Program continues after error handling.")
```

### Common Exception Types

| Exception | When it occurs |
|-----------|---------------|
| `ValueError` | Invalid value (e.g., `int("abc")`) |
| `ZeroDivisionError` | Division by zero |
| `FileNotFoundError` | File doesn't exist |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key doesn't exist |
| `TypeError` | Wrong type (e.g., `"5" + 5`) |

### Examples

**Example 8.3.1: Handling ZeroDivisionError**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```

**Example 8.3.2: Handling ValueError**
```python
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Error: That was not a valid number.")
```

### Skills Checklist
- [ ] I can use a `try-except` block to handle errors.
- [ ] I can name common exception types and what causes them.
- [ ] I can catch specific exception types.

---

## Lesson 8.4: The `else` and `finally` Blocks

### `else` Block — Runs only on success

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a number.")
else:
    print(f"You entered {num}.")   # Only runs if no exception
```

### `finally` Block — Always runs (cleanup)

```python
# For file I/O, prefer a with statement. This example demonstrates
# finally for cleanup of a resource managed manually.
file_handle = None
try:
    file_handle = open('data.txt', 'w')
    file_handle.write("Some data.")
except TypeError:
    print("A type error occurred.")
finally:
    if file_handle:
        file_handle.close()     # Always closes the file
        print("File closed.")
```

### Skills Checklist
- [ ] I can use an `else` block for code that runs only on success.
- [ ] I can use a `finally` block for code that always runs.

---

## Lesson 8.5: Storing Data with JSON

### Reading References
- Matthes: Chapter 10, pages 200–204

### The `json` Module

JSON (JavaScript Object Notation) is a lightweight format for storing and exchanging data. Python's `json` module converts between Python objects and JSON.

```python
import json

# Save data
task = {
    "id": 1,
    "title": "Practice Python",
    "description": "Complete the shared dataset exercises",
    "done": False,
    "created_at": "2025-01-15T09:00:00Z",
}

with open("tasks.json", "w", encoding="utf-8") as file:
    json.dump([task], file, indent=4)

# Load and verify all five canonical fields.
try:
    with open("tasks.json", "r", encoding="utf-8") as file:
        loaded_tasks = json.load(file)
    loaded_task = loaded_tasks[0]
    required_fields = {"id", "title", "description", "done", "created_at"}
    if set(loaded_task) != required_fields:
        raise ValueError("Task record does not match the five-field schema")
    print(loaded_task["id"], loaded_task["title"], loaded_task["done"])
except FileNotFoundError:
    print("Task file not found.")
except (json.JSONDecodeError, ValueError) as error:
    print(f"Invalid task data: {error}")
```

### JSON ↔ Python Mapping

| JSON | Python |
|------|--------|
| Object `{}` | Dictionary `{}` |
| Array `[]` | List `[]` |
| String | `str` |
| Number | `int` or `float` |
| Boolean | `bool` |
| null | `None` |

### Skills Checklist
- [ ] I can explain what JSON is and why it's used.
- [ ] I can use `json.dump()` to save Python data to a JSON file.
- [ ] I can use `json.load()` to load JSON data from a file.
- [ ] I can save and load lists of dictionaries using JSON.

---

# Unit 9: Testing and Data Analysis

## Overview

This unit introduces testing code for correctness and explores basic text-based data analysis.

---

## Lesson 9.1: Testing a Function

### Reading References
- Matthes: Chapter 11, pages 209–217

### Unit Testing with `unittest`

```python
# my_functions.py
def add_two_numbers(a, b):
    return a + b
```

```python
# test_my_functions.py
import unittest
from my_functions import add_two_numbers

class TestAddNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        result = add_two_numbers(5, 3)
        self.assertEqual(result, 8)

    def test_negative_numbers(self):
        result = add_two_numbers(-5, -3)
        self.assertEqual(result, -8)

    def test_mixed_numbers(self):
        result = add_two_numbers(10, -4)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
```

### Common Assertion Methods

| Method | Description |
|--------|-------------|
| `assertEqual(a, b)` | Check a == b |
| `assertTrue(x)` | Check x is True |
| `assertFalse(x)` | Check x is False |
| `assertIn(a, b)` | Check a in b |
| `assertIsNone(x)` | Check x is None |

### Skills Checklist
- [ ] I can create a basic test class using `unittest.TestCase`.
- [ ] I can define test methods within a test class.
- [ ] I can use `assertEqual()` to check for expected results.
- [ ] I can run unit tests from the terminal.

---

## Lesson 9.2: Testing a Class

### The `setUp()` Method

`setUp()` runs **before every test method**, providing a fresh instance each time:

```python
class TestEmployee(unittest.TestCase):
    def setUp(self):
        """Create an employee instance for all test methods."""
        self.employee = Employee('janis', 'joplin', 60000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 65000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 70000)
```

### Skills Checklist
- [ ] I can write tests for a Python class.
- [ ] I can use `setUp()` to prepare my tests.

---

## Lesson 9.3: Introduction to Random Numbers

```python
import random

# Random integer (inclusive)
die_roll = random.randint(1, 6)
print(f"You rolled: {die_roll}")

# Random float between 0.0 and 1.0
rand_float = random.random()

# Random choice from list
colors = ["red", "blue", "green"]
chosen = random.choice(colors)
print(f"Chosen color: {chosen}")
```

### Skills Checklist
- [ ] I can import the `random` module.
- [ ] I can generate a random integer within a range.
- [ ] I can select a random item from a list.

---

## Lesson 9.4: Analyzing Text Data

```python
sentence = "A student studies programming. Programming develops problem-solving skills."
words = sentence.lower().replace(".", "").split()

word_frequencies = {}
for word in words:
    word_frequencies[word] = word_frequencies.get(word, 0) + 1

print("Words:", len(words))
print("Programming:", word_frequencies["programming"])
print("Problem-solving:", word_frequencies["problem-solving"])
```

### Skills Checklist
- [ ] I can read text content from a file.
- [ ] I can split a string of text into individual words.
- [ ] I can use a dictionary to count the frequency of words.

---

## Lesson 9.5: Working with CSV Data

```python
import csv

filename = 'students.csv'
try:
    with open(filename, 'r') as file_object:
        reader = csv.reader(file_object)
        header_row = next(reader)
        print(f"Columns: {header_row}")
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")
```

### Reading the Canonical CSV Schema

Use the standard `csv` module rather than splitting rows on commas. A quoted field may itself contain a comma.

```python
import csv
from io import StringIO

csv_text = """student_id,first_name,last_name,score,active
1001,Avery,Jordan,82,true
1002,Riley,Chen,91,true
1003,Sam,Patel,76,false
1004,Morgan,Diaz,88,true
"""

reader = csv.DictReader(StringIO(csv_text))
for row in reader:
    print(row["student_id"], row["first_name"], row["last_name"],
          row["score"], row["active"])
```

Expected output:
```text
1001 Avery Jordan 82 true
1002 Riley Chen 91 true
1003 Sam Patel 76 false
1004 Morgan Diaz 88 true
```

### Skills Checklist
- [ ] I can explain what CSV data is.
- [ ] I can read a CSV file line by line.
- [ ] I can split a line of CSV data into individual values.

## Canonical Shared Dataset — Text, CSV, Tasks, and Tests

### Text analysis

Use this exact sentence for word-count and character-processing exercises:

```python
text_sample = "A student studies programming. Programming develops problem-solving skills."
words = text_sample.lower().replace(".", "").split()
print("Words:", len(words))
print("Programming:", words.count("programming"))
```

Expected output:
```text
Words: 8
Programming: 2
```

### CSV schema

The shared CSV header is exactly `student_id,first_name,last_name,score,active`. Example rows:

```csv
student_id,first_name,last_name,score,active
1001,Avery,Jordan,82,true
1002,Riley,Chen,91,true
1003,Sam,Patel,76,false
1004,Morgan,Diaz,88,true
```

Use the `csv` module and named column positions; do not substitute a different three-column name/age/grade schema.

```python
import csv
from io import StringIO

csv_text = """student_id,first_name,last_name,score,active
1001,Avery,Jordan,82,true
1002,Riley,Chen,91,true
1003,Sam,Patel,76,false
1004,Morgan,Diaz,88,true
"""
for row in csv.DictReader(StringIO(csv_text)):
    print(row["student_id"], row["first_name"], row["last_name"],
          row["score"], row["active"])
```

Expected output:
```text
1001 Avery Jordan 82 true
1002 Riley Chen 91 true
1003 Sam Patel 76 false
1004 Morgan Diaz 88 true
```

### To-do record schema

Use all five fields in every serialized task record: `id`, `title`, `description`, `done`, and `created_at`.

```python
task = {
    "id": 1,
    "title": "Practice Python",
    "description": "Complete the shared dataset exercises",
    "done": False,
    "created_at": "2025-01-15T09:00:00Z",
}
```

```python
import json

task = {
    "id": 1,
    "title": "Practice Python",
    "description": "Complete the shared dataset exercises",
    "done": False,
    "created_at": "2025-01-15T09:00:00Z",
}
serialized = json.dumps([task])
loaded_tasks = json.loads(serialized)
loaded_task = loaded_tasks[0]
required_fields = {"id", "title", "description", "done", "created_at"}
assert set(loaded_task) == required_fields
print(loaded_task["id"], loaded_task["title"], loaded_task["done"])
```

Expected output:
```text
1 Practice Python False
```

Tests should assert deterministic results for the shared tip calculator, grade classifier, inventory total, and text sample. Random-number lessons must seed the generator when an exact result is asserted.
