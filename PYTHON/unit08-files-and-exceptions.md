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
