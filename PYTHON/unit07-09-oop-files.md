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

### Learning Objectives
- Explain the basic idea of Object-Oriented Programming.
- Describe a class as a blueprint and an object as an instance.

### Concept Explanation

A *class* describes what a kind of thing knows (its *attributes*) and what it can do (its *methods*). An *object* is one actual thing made from a class. Bundling data with the functions that work on it is called **encapsulation**, and it keeps related code together so a change in one place does not break unrelated code.

#### Classes as Blueprints

A **class** is a blueprint or template for creating objects. An **object** is a concrete instance created from that blueprint.

**Analogy:** An "Item" class defines that every inventory item has a `name`, a `quantity`, and a `unit_price` (attributes) and can report its `total_value()` (a method). A Notebook and a Pencil are two separate **objects** of the same "Item" class. This course models the same inventory item in every language.

#### Key OOP Concepts

- **Encapsulation** — Bundling data and methods into a single unit.
- **Abstraction** — Hiding complexity from the outside.
- **Inheritance** — New class reuses functionality of existing class.
- **Polymorphism** — Same method name behaves differently for different classes.

### Worked Example

A student profile kept as loose variables is easy to mix up. As an object, the same data and the operations on it travel together:
```python
class Item:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        return self.quantity * self.unit_price


notebook = Item("Notebook", 3, 2.50)
print(notebook.name, notebook.total_value())
```

### Expected Behavior or Output

Output of example 1:
```
Notebook 7.5
```

### Common Mistakes

1. Treating a class as one single thing. A class is a blueprint, and each call such as `Item(...)` makes a separate object.
2. Putting unrelated data into one class so that it has no clear purpose.
3. Skipping the design step and creating classes before knowing what data and operations are needed.

### Activities

1. List the attributes and methods of a `Student` class for the shared profile (Avery, 16, 1.72, Computer Science).
2. Describe in two sentences how a class differs from an object, using `Item` and `notebook`.
3. Name three real things and for each write one attribute and one method.
4. Explain what encapsulation means and why it helps when a program grows.

### Accessibility Practice

Describe a class as a list read in order: its name, then its attributes, then its methods. Reading a class definition aloud works best by saying 'class Item, colon, define init, open parenthesis, self, comma, name...' and listening for the colons and indentation that show structure.

### Skills Checklist

- [ ] I can explain the basic idea of Object-Oriented Programming.
- [ ] I can describe a class as a blueprint and an object as an instance.

---

## Lesson 7.2: Creating and Using a Class

### Reading References
- Zelle: Chapter 10, pages 248–254
- Matthes: Chapter 9, pages 158–162

### Learning Objectives
- Define a basic Python class.
- Define the `__init__` method within a class.
- Understand the purpose of the `self` parameter.
- Create an instance (object) of a class.

### Concept Explanation

#### Class Syntax

The `__init__()` method runs automatically when a new object is created. `self` refers to the specific instance being created. Each of the three objects above has the same fields (`name`, `quantity`, `unit_price`) with different values. Keeping the attributes inside the object, and changing them only through methods, is called **encapsulation**.

### Worked Example

```python
class Item:
    """An inventory item with a name, a quantity, and a unit price."""

    def __init__(self, name, quantity, unit_price):
        """Initialize the item's attributes."""
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price


notebook = Item("Notebook", 3, 2.50)
pencil = Item("Pencil", 10, 0.50)
folder = Item("Folder", 4, 1.25)

print(f"{notebook.name}: {notebook.quantity} at {notebook.unit_price}")
print(f"{pencil.name}: {pencil.quantity} at {pencil.unit_price}")
print(f"{folder.name}: {folder.quantity} at {folder.unit_price}")
```

### Expected Behavior or Output

Expected output:
```
Notebook: 3 at 2.5
Pencil: 10 at 0.5
Folder: 4 at 1.25
```

### Common Mistakes

1. Forgetting `self` as the first parameter of `__init__`, which raises a `TypeError` when an object is created.
2. Writing `name = name` instead of `self.name = name`, so the value is lost when `__init__` ends.
3. Writing `__init__` with one underscore on each side, so it is not recognized.

### Activities

1. Create a fourth item with your own values and print its fields.
2. Add a check in `__init__` that rejects a negative quantity by printing a message.
3. Create two items with the same name and different quantities and show that changing one does not change the other.
4. Explain what `self` refers to in your own words.

### Accessibility Practice

Say the double underscores aloud ('dunder init') and confirm that your screen reader announces them, because `_init_` with a single underscore fails silently. Print each object on its own line with its name, so the output can be matched to the objects by ear.

### Skills Checklist

- [ ] I can define a basic Python class.
- [ ] I can define the `__init__` method within a class.
- [ ] I understand the purpose of the `self` parameter.
- [ ] I can create an instance (object) of a class.

---

## Lesson 7.3: Working with Attributes and Methods

### Reading References
- Matthes: Chapter 9, pages 162–166

### Learning Objectives
- Access an object's attributes using dot notation.
- Define and call methods within a class.
- Use a method to change an object's attribute.

### Concept Explanation

#### Calling Methods

### Worked Example

```python
class Item:
    """An inventory item with a name, a quantity, and a unit price."""

    def __init__(self, name, quantity, unit_price):
        """Initialize the item's attributes."""
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        """Return quantity multiplied by unit price."""
        return self.quantity * self.unit_price

    def is_valid(self):
        """An item is valid if it has a name and non-negative numbers."""
        return bool(self.name) and self.quantity >= 0 and self.unit_price >= 0

    def restock(self, amount):
        """Add stock; reject a negative amount."""
        if amount < 0:
            print("Cannot restock a negative amount.")
            return
        self.quantity += amount

    def describe(self):
        print(f"{self.name}: {self.quantity} at {self.unit_price:.2f} each, "
              f"value {self.total_value():.2f}")


notebook = Item("Notebook", 3, 2.50)
notebook.describe()
notebook.restock(2)          # method-based modification
notebook.describe()
notebook.quantity = 4        # direct attribute modification
notebook.describe()
notebook.restock(-1)         # validation message
print(notebook.is_valid())
```

### Expected Behavior or Output

Expected output:
```
Notebook: 3 at 2.50 each, value 7.50
Notebook: 5 at 2.50 each, value 12.50
Notebook: 4 at 2.50 each, value 10.00
Cannot restock a negative amount.
True
```

### Common Mistakes

1. Calling a method without parentheses (`notebook.describe`), which refers to the method but does not run it.
2. Changing an attribute directly and skipping the validation that a method would have performed.
3. Forgetting `self.` when a method uses an attribute, which raises a `NameError`.

### Activities

1. Predict the output of each call in the example before running it.
2. Add a method `discount(rate)` that returns the value after a discount without changing the item.
3. Call `restock(-1)` and read the message. Then change the method to reject zero as well.
4. Explain the difference between changing `quantity` directly and calling `restock`.

### Accessibility Practice

Name methods after actions (`restock`, `describe`) so the call reads as a sentence. Print one line per method call, so a screen reader announces the effect of every step in order.

### Skills Checklist

- [ ] I can access an object's attributes using dot notation.
- [ ] I can define and call methods within a class.
- [ ] I can use a method to change an object's attribute.

---

## Lesson 7.4: Inheritance

### Reading References
- Zelle: Chapter 12, pages 351–352
- Matthes: Chapter 9, pages 167–170

### Learning Objectives
- Define a child class that inherits from a parent class.
- Use `super().__init__()` to properly initialize inherited attributes.
- Add new attributes and methods to a child class.
- Override a parent method in a child class.

### Concept Explanation

#### Creating a Child Class



#### `super()` Function

`super().__init__()` calls the parent class's `__init__()` method, ensuring inherited attributes are properly initialized. In the example, `DiscountedItem` overrides `total_value()`; the inherited `describe()` automatically uses the new version. This is **polymorphism**: the same method name behaves differently for different classes.

### Worked Example

```python
class Item:
    """An inventory item with a name, a quantity, and a unit price."""

    def __init__(self, name, quantity, unit_price):
        """Initialize the item's attributes."""
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        return self.quantity * self.unit_price

    def describe(self):
        print(f"{self.name}: {self.quantity} at {self.unit_price:.2f} each, "
              f"value {self.total_value():.2f}")


class DiscountedItem(Item):
    """An item sold at a discount; inherits from Item."""

    def __init__(self, name, quantity, unit_price, discount_rate):
        super().__init__(name, quantity, unit_price)   # Call parent's __init__
        self.discount_rate = discount_rate

    def total_value(self):                              # Override
        return super().total_value() * (1 - self.discount_rate)


folder = DiscountedItem("Folder", 4, 1.25, 0.20)
folder.describe()        # inherited describe() calls the overridden total_value()
print(isinstance(folder, Item))
```

### Expected Behavior or Output

Expected output:
```
Folder: 4 at 1.25 each, value 4.00
True
```

### Common Mistakes

1. Forgetting to call `super().__init__()`, so the parent's attributes are never created.
2. Overriding a method but changing what it returns, so code that uses the parent version breaks.
3. Using inheritance for a "has a" relationship; use composition (Lesson 7.5) instead.

### Activities

1. Predict the printed value and the final `True` of the example before running it.
2. Add a subclass `PerishableItem` with an `expires` attribute and override `describe`.
3. Explain why `describe` prints the discounted value without being redefined.
4. List the lookup order Python uses to find `describe` for a `DiscountedItem`.

### Accessibility Practice

Describe inheritance as an ordered list: the object's own class first, then its parent. Speaking the chain aloud ('DiscountedItem, then Item') is clearer than a diagram.

### Skills Checklist

- [ ] I can define a child class that inherits from a parent class.
- [ ] I can use `super().__init__()` to properly initialize inherited attributes.
- [ ] I can add new attributes and methods to a child class.
- [ ] I can override a parent method in a child class.

---

## Lesson 7.5: Instances as Attributes (Composition)

### Reading References
- Matthes: Chapter 9 (Classes), the section on instances as attributes
- Zelle: Chapter 10 (Defining Classes)

### Learning Objectives
- Explain the concept of composition in OOP.
- Create an instance of one class and assign it as an attribute of another.
- Access attributes and methods of a nested object.

### Concept Explanation

#### Composition — "Has-A" Relationship

Instead of inheriting, a class **contains an instance of another class** as an attribute.

### Worked Example

```python
class Item:
    """An inventory item with a name, a quantity, and a unit price."""

    def __init__(self, name, quantity, unit_price):
        """Initialize the item's attributes."""
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        return self.quantity * self.unit_price


class Inventory:
    """An Inventory HAS-A list of Item objects (composition)."""

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total_value(self):
        return sum(item.total_value() for item in self.items)

    def report(self):
        for item in self.items:
            print(f"{item.name}: {item.quantity}")
        print(f"Total value: {self.total_value():.2f}")


inventory = Inventory()
inventory.add(Item("Notebook", 3, 2.50))
inventory.add(Item("Pencil", 10, 0.50))
inventory.add(Item("Folder", 4, 1.25))
inventory.report()
```

### Expected Behavior or Output

Expected output:
```
Notebook: 3
Pencil: 10
Folder: 4
Total value: 17.50
```

### Common Mistakes

1. Using inheritance where a "has a" relationship is meant.
2. Letting the container reach into each item's attributes instead of calling the item's own methods.
3. Creating the list in a default argument or at class level, so every `Inventory` shares one list.

### Activities

1. Predict the output of the example.
2. Add `Inventory.find(name)` that returns the item with that name or `None`.
3. Add `Inventory.remove(name)` and test it.
4. Explain the difference between "is a" and "has a" with two examples.

### Accessibility Practice

Report the inventory as one labelled line per item and a final total line, so a screen reader reads a complete summary in order.

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

### Learning Objectives
- Open a file for reading using `with open()`.
- Read the entire content of a file into a string.
- Read a file line by line using a `for` loop.
- Remove whitespace/newlines using `.strip()`.

### Concept Explanation

#### Reading Files

Create a file named `notes.txt` in your project folder containing exactly these two lines:
```text
Practice Python.
Review lists and functions.
```



The `with` statement **automatically closes the file** even if an error occurs.

#### File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read (default) |
| `'w'` | Write (creates new or overwrites) |
| `'a'` | Append (adds to end) |

### Worked Example

```python
# Reading entire file
with open('notes.txt', 'r') as file_object:
    contents = file_object.read()
print(contents)

# Reading line by line
with open('notes.txt', 'r') as file_object:
    for line in file_object:
        print(line.strip())

# Reading all lines into a list
with open('notes.txt', 'r') as file_object:
    lines = file_object.readlines()
print(len(lines))
```

### Expected Behavior or Output

Expected output:
```
Practice Python.
Review lists and functions.

Practice Python.
Review lists and functions.
2
```

### Common Mistakes

1. Opening a file that does not exist without handling the `FileNotFoundError`.
2. Forgetting that a relative path starts from the working directory, not from the program's folder.
3. Forgetting that `readlines()` keeps the newline at the end of each line.

### Activities

1. Run the example and describe each block of output.
2. Add a third line to `notes.txt` and predict the new line count.
3. Print each line with its line number.
4. Open a file that does not exist and print a friendly message that includes the file name.

### Accessibility Practice

Read the output aloud in order. Make any error message a complete sentence that includes the file name, so it is clear without seeing the screen.

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

### Learning Objectives
- Open a file for writing using `"w"` mode.
- Open a file for appending using `"a"` mode.
- Write a string to a file.
- Add newlines to a file using `\n`.

### Concept Explanation

**Important:** The `.write()` method does not add newlines automatically. Use `\n`.

### Worked Example

```python
# Write mode (overwrites existing content)
with open('notes.txt', 'w') as f:
    f.write("Practice Python.\n")

# Append mode (adds to end)
with open('notes.txt', 'a') as f:
    f.write("Review lists and functions.\n")

with open('notes.txt', 'r') as f:
    print(f.read())
```

### Expected Behavior or Output

Expected output:
```
Practice Python.
Review lists and functions.
```

### Common Mistakes

1. Using mode `'w'` when `'a'` was intended, which erases earlier content.
2. Forgetting `\n`, so all written lines run together.
3. Not using `with`, so the file may stay open if an error occurs.

### Activities

1. Predict the output, then run.
2. Change the second open to mode `'w'` and explain the difference.
3. Append a third line with the current number of lines.
4. Write the shared scores, one per line, then read them back and total them.

### Accessibility Practice

Always read a written file back in the terminal to confirm it, using line navigation, so you do not depend on assumptions about what was saved.

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

### Learning Objectives
- Use a `try-except` block to handle errors.
- Name common exception types and what causes them.
- Catch specific exception types.

### Concept Explanation

#### `try-except` Block

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
print("Program continues after error handling.")
```

#### Common Exception Types

| Exception | When it occurs |
|-----------|---------------|
| `ValueError` | Invalid value (e.g., `int("abc")`) |
| `ZeroDivisionError` | Division by zero |
| `FileNotFoundError` | File doesn't exist |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key doesn't exist |
| `TypeError` | Wrong type (e.g., `"5" + 5`) |

### Worked Example

**Example 8.3.1: Handling ZeroDivisionError**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```

**Example 8.3.3: Missing File and Malformed Data**
```python
try:
    with open("missing_notes.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: missing_notes.txt was not found.")

try:
    score = int("abc")
except ValueError:
    print("Error: 'abc' is not a valid score.")
```


**Example 8.3.2: Handling ValueError**
```python
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Error: That was not a valid number.")
```

### Expected Behavior or Output

Expected output:
```
Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score.
```

### Common Mistakes

1. Using a bare `except:` that hides every error, including mistakes in your own code.
2. Putting too much code inside `try`, so it is unclear which line failed.
3. Catching an error and printing nothing, so the user does not know what happened.

### Activities

1. Predict each printed line of the missing-file example before running it.
2. Wrap `int(input(...))` so that invalid input prints a clear message and asks again.
3. Catch `ZeroDivisionError` in a function that computes an average of an empty list.
4. Explain when to catch an exception and when to let it stop the program.

### Accessibility Practice

Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.' Read the exception name aloud when you see it in a traceback, then jump to the last line of the traceback.

### Skills Checklist

- [ ] I can use a `try-except` block to handle errors.
- [ ] I can name common exception types and what causes them.
- [ ] I can catch specific exception types.

---

## Lesson 8.4: The `else` and `finally` Blocks

### Reading References
- Matthes: Chapter 10 (Files and Exceptions), the sections on the `else` block
- Zelle: Chapter 5 (Sequences: Strings, Lists, and Files)

### Learning Objectives
- Use an `else` block for code that runs only on success.
- Use a `finally` block for code that always runs.

### Concept Explanation

#### `else` Block — Runs only on success

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a number.")
else:
    print(f"You entered {num}.")   # Only runs if no exception
```

#### `finally` Block — Always runs (cleanup)

### Worked Example

```python
# For file I/O, prefer a with statement. This example demonstrates
# finally for cleanup of a resource managed manually.
file_handle = None
try:
    file_handle = open('cleanup_demo.txt', 'w')
    file_handle.write("Some data.")
except TypeError:
    print("A type error occurred.")
finally:
    if file_handle:
        file_handle.close()     # Always closes the file
        print("File closed.")
```

### Expected Behavior or Output

Output of example 1:
```
File closed.
```

### Common Mistakes

1. Putting code in `else` that can itself fail, so its errors are not handled.
2. Relying on `finally` to return a value, which can hide an earlier error.
3. Closing a file manually and forgetting to do so when an error occurs; prefer `with`.

### Activities

1. Predict the output of both runs of the example.
2. Add a `finally` block that prints a message even when an error occurs.
3. Rewrite the example with `with` and explain why it is shorter and safer.
4. Explain in two sentences what `else` adds to `try` and `except`.

### Accessibility Practice

Print a status line in each block (`try`, `except`, `else`, `finally`), so a screen reader announces which path ran. Short, labelled lines make the control flow audible.

### Skills Checklist

- [ ] I can use an `else` block for code that runs only on success.
- [ ] I can use a `finally` block for code that always runs.

---

## Lesson 8.5: Storing Data with JSON

### Reading References
- Matthes: Chapter 10, pages 200–204

### Learning Objectives
- Explain what JSON is and why it's used.
- Use `json.dump()` to save Python data to a JSON file.
- Use `json.load()` to load JSON data from a file.
- Save and load lists of dictionaries using JSON.

### Concept Explanation

#### The `json` Module

JSON (JavaScript Object Notation) is a lightweight format for storing and exchanging data. Python's `json` module converts between Python objects and JSON.

#### JSON ↔ Python Mapping

| JSON | Python |
|------|--------|
| Object `{}` | Dictionary `{}` |
| Array `[]` | List `[]` |
| String | `str` |
| Number | `int` or `float` |
| Boolean | `bool` |
| null | `None` |

### Worked Example

```python
import json

tasks = [
    {"id": 1, "title": "Study programming", "description": "Finish Unit 8",
     "done": False, "created_at": "2026-01-15T09:00:00"},
    {"id": 2, "title": "Review scores", "description": "Check the four scores",
     "done": True, "created_at": "2026-01-15T09:30:00"},
]

with open('tasks.json', 'w') as f:
    json.dump(tasks, f, indent=4)

try:
    with open('tasks.json', 'r') as f:
        loaded = json.load(f)
    for task in loaded:
        status = "done" if task["done"] else "not done"
        print(f"{task['id']}: {task['title']} ({status})")
except FileNotFoundError:
    print("Tasks file not found.")
except json.JSONDecodeError:
    print("Error: Could not decode tasks file.")
```

### Expected Behavior or Output

Expected output:
```
1: Study programming (not done)
2: Review scores (done)
```

### Common Mistakes

1. Calling `json.dump` with a file opened in read mode.
2. Trying to save an object that JSON cannot represent, such as a custom class instance.
3. Not handling `json.JSONDecodeError`, so a damaged file crashes the program.

### Activities

1. Run the example and read the saved JSON text from `tasks.json`.
2. Edit `tasks.json` by hand to remove a closing bracket and run the program again.
3. Add a third task and confirm that it is saved and loaded.
4. Explain why `True` in Python becomes `true` in the JSON file.

### Accessibility Practice

Open `tasks.json` in the terminal and read it as text. Because `indent=4` puts one field per line, the file reads line by line with a screen reader. Practise moving through it by word or character.

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

### Learning Objectives
- Create a basic test class using `unittest.TestCase`.
- Define test methods within a test class.
- Use `assertEqual()` to check for expected results.
- Run unit tests from the terminal.

### Concept Explanation

#### Unit Testing with `unittest`

```python
# my_functions.py
def add(a, b):
    return a + b


def calculate_tip(bill, rate):
    return bill * rate


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
```

```python
# test_my_functions.py
import unittest
from my_functions import add, calculate_tip, classify


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(10, -4), 6)

    def test_tip(self):
        # Decimal results are compared with a tolerance, not exact equality.
        self.assertAlmostEqual(calculate_tip(24.5, 0.15), 3.675)
        self.assertEqual(calculate_tip(0, 0.15), 0)

    def test_classify_boundaries(self):
        self.assertEqual(classify(90), "A")
        self.assertEqual(classify(89), "B")
        self.assertEqual(classify(60), "D")
        self.assertEqual(classify(59), "F")


if __name__ == '__main__':
    unittest.main()
```

Run the tests from the terminal with `python test_my_functions.py` or `python -m unittest`. Expected output (the timing line will differ):
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

The three tests check the same inputs and expected results in every language track: `add(5, 3)` is 8, the tip for a bill of 24.50 at 0.15 is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F.

### Worked Example

```python
# my_functions.py
def add(a, b):
    return a + b


def calculate_tip(bill, rate):
    return bill * rate


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
```

```python
# test_my_functions.py
import unittest
from my_functions import add, calculate_tip, classify


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(10, -4), 6)

    def test_tip(self):
        # Decimal results are compared with a tolerance, not exact equality.
        self.assertAlmostEqual(calculate_tip(24.5, 0.15), 3.675)
        self.assertEqual(calculate_tip(0, 0.15), 0)

    def test_classify_boundaries(self):
        self.assertEqual(classify(90), "A")
        self.assertEqual(classify(89), "B")
        self.assertEqual(classify(60), "D")
        self.assertEqual(classify(59), "F")


if __name__ == '__main__':
    unittest.main()
```

Run the tests from the terminal with `python test_my_functions.py` or `python -m unittest`.

### Expected Behavior or Output

Expected output (the timing line differs from run to run):
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

The three tests check the same inputs and expected results in every language track: `add(5, 3)` is 8, the tip for a bill of 24.50 at 0.15 is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F.

### Common Mistakes

1. Comparing decimal results with `assertEqual`. Use `assertAlmostEqual`, because floating-point results are approximations.
2. Naming a test method without the `test_` prefix, so `unittest` never runs it.
3. Testing only typical values and skipping the boundaries 90, 89, 60, and 59.

### Activities

1. Change one expected value so a test fails, read the failure message, and then restore it.
2. Add tests for the grades at 80, 79, 70, and 69.
3. Write the tests for `is_passing(score)` before you write the function.
4. Explain why the tip test uses a tolerance.

### Accessibility Practice

A passing run prints a short summary (`Ran 3 tests ... OK`) that is quick to read. A failing run prints the test name and the expected and actual values on separate lines; jump to those lines first. Name each test as a sentence that completes 'This test checks that...'.

### Skills Checklist

- [ ] I can create a basic test class using `unittest.TestCase`.
- [ ] I can define test methods within a test class.
- [ ] I can use `assertEqual()` to check for expected results.
- [ ] I can run unit tests from the terminal.

---

## Lesson 9.2: Testing a Class

### Reading References
- Matthes: Chapter 11 (Testing Your Code), the sections on testing a class

### Learning Objectives
- Write tests for a Python class.
- Use `setUp()` to prepare my tests.

### Concept Explanation

#### The `setUp()` Method

`setUp()` runs **before every test method**, providing a fresh instance each time:

```python
# item.py  (the Item class from Unit 7, with a restock method)
class Item:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        return self.quantity * self.unit_price

    def restock(self, amount):
        if amount < 0:
            raise ValueError("amount must not be negative")
        self.quantity += amount
```

```python
# test_item.py
import unittest
from item import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        """Create a fresh Notebook for every test method."""
        self.item = Item("Notebook", 3, 2.50)

    def test_total_value(self):
        self.assertAlmostEqual(self.item.total_value(), 7.5)

    def test_restock(self):
        self.item.restock(2)
        self.assertEqual(self.item.quantity, 5)

    def test_restock_rejects_negative_amount(self):
        with self.assertRaises(ValueError):
            self.item.restock(-1)


if __name__ == '__main__':
    unittest.main()
```

Expected output (the timing line will differ):
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

Because `setUp()` runs before each test, `test_restock` changing the quantity to 5 does not affect `test_total_value`, which still sees 3 notebooks.

### Worked Example

```python
# item.py  (the Item class from Unit 7, with a restock method)
class Item:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        return self.quantity * self.unit_price

    def restock(self, amount):
        if amount < 0:
            raise ValueError("amount must not be negative")
        self.quantity += amount
```

```python
# test_item.py
import unittest
from item import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        """Create a fresh Notebook for every test method."""
        self.item = Item("Notebook", 3, 2.50)

    def test_total_value(self):
        self.assertAlmostEqual(self.item.total_value(), 7.5)

    def test_restock(self):
        self.item.restock(2)
        self.assertEqual(self.item.quantity, 5)

    def test_restock_rejects_negative_amount(self):
        with self.assertRaises(ValueError):
            self.item.restock(-1)


if __name__ == '__main__':
    unittest.main()
```

### Expected Behavior or Output

Expected output (the timing line differs):
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

Because `setUp()` runs before each test, `test_restock` changing the quantity to 5 does not affect `test_total_value`, which still sees 3 notebooks.

### Common Mistakes

1. Sharing one object between tests so that an earlier test changes the later ones; use `setUp`.
2. Testing only the successful path and never the error path.
3. Forgetting `self.` inside a test method, so the fixture object is not found.

### Activities

1. Add a test that `restock(0)` leaves the quantity unchanged.
2. Add a test for the `is_valid` method from Unit 7.
3. Break `restock` on purpose and read the failure report.
4. Explain why `setUp` creates a new item for each test.

### Accessibility Practice

Name each test as a short sentence that says what behavior it checks, so the PASS or FAIL report reads as a clear statement. Read the summary line first, and open the failure details only when it says FAILED.

### Skills Checklist

- [ ] I can write tests for a Python class.
- [ ] I can use `setUp()` to prepare my tests.

---

## Lesson 9.3: Introduction to Random Numbers

### Reading References
- Matthes: Chapter 9 (Classes), the section on the `random` module
- Zelle: Chapter 9 (Simulation and Design)

### Learning Objectives
- Import the `random` module.
- Generate a random integer within a range.
- Select a random item from a list.

### Concept Explanation

Without the `random.seed(...)` line the values change on every run. Use a seed when you need to test or reproduce a result.

### Worked Example

```python
import random

random.seed(42)   # a fixed seed makes the "random" results repeatable

die_roll = random.randint(1, 6)          # random integer (inclusive)
print(f"You rolled: {die_roll}")

rand_float = random.random()             # random float from 0.0 up to 1.0
print(f"Random decimal: {rand_float:.4f}")

scores = [82, 91, 76, 88]
chosen = random.choice(scores)           # random choice from a list
print(f"Chosen score: {chosen}")
```

### Expected Behavior or Output

Expected output with `random.seed(42)` on Python 3.12:
```
You rolled: 6
Random decimal: 0.1113
Chosen score: 76
```

### Common Mistakes

1. Testing for specific random values that change between Python versions; test properties such as the range instead.
2. Calling `random.seed()` in every loop pass, which repeats the same value.
3. Forgetting that `randint(1, 6)` includes both ends, while `randrange(1, 6)` does not include 6.

### Activities

1. Run the example three times with the seed line and then three times without it; compare.
2. Change the seed and check that the ranges still hold.
3. Simulate 600 rolls and count how many of each face appeared (the counts will differ).
4. Explain why a test should check a property rather than a specific random number.

### Accessibility Practice

When output is random, print yes or no results about properties (`All rolls between 1 and 6: True`) so the screen reader announces the same result on every run and does not read unpredictable values.

### Skills Checklist

- [ ] I can import the `random` module.
- [ ] I can generate a random integer within a range.
- [ ] I can select a random item from a list.

---

## Lesson 9.4: Analyzing Text Data

### Reading References
- Matthes: Chapter 6 (Dictionaries), the section on counting with dictionaries
- Zelle: Chapter 5 (Sequences: Strings, Lists, and Files)

### Learning Objectives
- Read text content from a file.
- Split a string of text into individual words.
- Use a dictionary to count the frequency of words.

### Concept Explanation



### Worked Example

```python
text = "A student studies programming. Programming develops problem-solving skills."
words = text.lower().replace(".", "").split()

word_frequencies = {}
for word in words:
    if word in word_frequencies:
        word_frequencies[word] += 1
    else:
        word_frequencies[word] = 1

print("Word count:", len(words))
print("Word Frequencies:")
for word, count in word_frequencies.items():
    print(f"'{word}': {count}")

letter_counts = {}
for ch in text.lower():
    if ch.isalpha():
        letter_counts[ch] = letter_counts.get(ch, 0) + 1

top_three = sorted(letter_counts.items(), key=lambda pair: (-pair[1], pair[0]))[:3]
print("Most common letters:", top_three)
```

### Expected Behavior or Output

Expected output:
```
Word count: 8
Word Frequencies:
'a': 1
'student': 1
'studies': 1
'programming': 2
'develops': 1
'problem-solving': 1
'skills': 1
Most common letters: [('s', 7), ('e', 5), ('g', 5)]
```

### Common Mistakes

1. Counting punctuation as part of a word, so `programming.` and `programming` become different words.
2. Forgetting to convert text to lower case before counting, so `Programming` and `programming` are counted separately.
3. Sorting a dictionary by key when the count was intended.

### Activities

1. Predict the word count and the count for `programming` before running.
2. Count the words longer than 8 letters.
3. Print the longest word.
4. Change the sort so ties are listed in reverse alphabetical order.

### Accessibility Practice

Read the frequency list in its fixed order. Because the order is stable, you can learn it and compare runs by ear. Print each pair as a short sentence (`'programming': 2`) with the same wording every time.

### Skills Checklist

- [ ] I can read text content from a file.
- [ ] I can split a string of text into individual words.
- [ ] I can use a dictionary to count the frequency of words.

---

## Lesson 9.5: Working with CSV Data

### Reading References
- Matthes: Chapter 10 (Files and Exceptions), the section on CSV files
- Zelle: Chapter 5 (Sequences: Strings, Lists, and Files)

### Learning Objectives
- Explain what CSV data is.
- Read a CSV file line by line.
- Split a line of CSV data into individual values.

### Concept Explanation

Save this as `students.csv` (the same file is used in every language track):
```csv
student_id,first_name,last_name,score,active
1,Avery,Student,91,true
2,Jordan,Lee,82,true
3,Casey,Smith,76,false
```


The `csv` module handles quoted fields and embedded commas correctly. Splitting each line on commas with `line.split(',')` works only for simple files where no value contains a comma.

### Worked Example

```python
import csv

filename = 'students.csv'
try:
    with open(filename, 'r', newline='') as file_object:
        reader = csv.DictReader(file_object)
        print(f"Columns: {reader.fieldnames}")
        scores = []
        active_count = 0
        for row in reader:
            scores.append(int(row["score"]))
            if row["active"] == "true":
                active_count += 1
            print(f"{row['student_id']}: {row['first_name']} {row['last_name']} scored {row['score']}")
    print(f"Students: {len(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.2f}")
    print(f"Active students: {active_count}")
except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")
```

### Expected Behavior or Output

Expected output:
```
Columns: ['student_id', 'first_name', 'last_name', 'score', 'active']
1: Avery Student scored 91
2: Jordan Lee scored 82
3: Casey Smith scored 76
Students: 3
Average score: 83.00
Active students: 2
```

### Common Mistakes

1. Splitting a CSV line at every comma when a value itself contains a quoted comma; use the `csv` module.
2. Forgetting to convert the text in the score column to a number.
3. Opening a CSV file without `newline=''`, which can produce blank rows on some systems.

### Activities

1. Predict the printed lines before running.
2. Add a fourth student and check the new average.
3. Print only the active students.
4. Explain, with an example, why `"Smith, Jr."` breaks `line.split(',')`.

### Accessibility Practice

Print one student per line with the same wording each time, so the screen reader announces a repeating pattern that is easy to compare line by line. Read the column names aloud once at the start so the values that follow have meaning.

### Skills Checklist

- [ ] I can explain what CSV data is.
- [ ] I can read a CSV file line by line.
- [ ] I can split a line of CSV data into individual values.

---
