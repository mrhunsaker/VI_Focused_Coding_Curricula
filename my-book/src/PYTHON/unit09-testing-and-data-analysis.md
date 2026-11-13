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
sentence = "A student studies programming. Programming develops problem-solving skills."
words = sentence.lower().replace(".", "").split()

word_frequencies = {}
for word in words:
    word_frequencies[word] = word_frequencies.get(word, 0) + 1

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
