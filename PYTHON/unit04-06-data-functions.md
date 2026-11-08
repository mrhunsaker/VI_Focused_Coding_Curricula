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

### Reading References
- Matthes: Chapter 3 (Introducing Lists) and Chapter 4 (Working with Lists)

### Learning Objectives
- Add an item to the end of a list using `.append()`.
- Insert an item at a specific position using `.insert()`.
- Remove an item by index using `del`.
- Remove an item and retrieve its value using `.pop()`.
- Remove the first occurrence of a value using `.remove()`.

### Concept Explanation

#### Adding and Removing Elements

```python
my_list = [10, 20, 30]

my_list.append(40)          # Add to end → [10, 20, 30, 40]
my_list.insert(1, 15)       # Insert at index 1 → [10, 15, 20, 30, 40]
del my_list[0]              # Delete by index → [15, 20, 30, 40]
removed = my_list.pop()     # Remove and return last → removed=40, list=[15, 20, 30]
my_list.remove(20)          # Remove by value → [15, 30]
```

### Worked Example

```python
scores = [82, 91, 76, 88]

scores.append(95)        # [82, 91, 76, 88, 95]
scores.insert(1, 85)     # [82, 85, 91, 76, 88, 95]
scores[2] = 93           # [82, 85, 93, 76, 88, 95]
scores.remove(76)        # [82, 85, 93, 88, 95]
last_score = scores.pop()  # last_score is 95

print(scores)
print(len(scores))
print(88 in scores)
```

### Expected Behavior or Output

Expected output:
```
[82, 85, 93, 88]
4
True
```

### Common Mistakes

1. Using `list.insert(value, position)`. The position comes first: `scores.insert(1, 85)`.
2. Calling `remove()` with a value that is not in the list, which raises a `ValueError`; check with `in` first.
3. Removing items from a list while looping over it, which skips the item after each removal.

### Activities

1. Trace the list after each operation in the example and write each version as one sentence.
2. Remove the first score with `pop(0)` and explain what happens to the other scores.
3. Write code that removes every score below 80 safely.
4. Print the position of the first score above 90 with `index()`, and explain what happens if none exists.

### Accessibility Practice

After every change, print the whole list on one line so a screen reader reads a complete state in one pass. Say the comments aloud as part of each line, since they hold the expected value after the change.

### Skills Checklist

- [ ] I can add an item to the end of a list using `.append()`.
- [ ] I can insert an item at a specific position using `.insert()`.
- [ ] I can remove an item by index using `del`.
- [ ] I can remove an item and retrieve its value using `.pop()`.
- [ ] I can remove the first occurrence of a value using `.remove()`.

---

## Lesson 4.2: Organizing Lists

### Reading References
- Matthes: Chapter 3 (Introducing Lists) and Chapter 4 (Working with Lists)

### Learning Objectives
- Sort a list permanently using `.sort()`.
- Get a temporarily sorted version using `sorted()`.
- Reverse a list using `.reverse()`.
- Find how many items are in a list using `len()`.

### Concept Explanation

Lists can be reordered in two ways. `sort()` changes the list *in place* and returns nothing. `sorted()` returns a *new* sorted list and leaves the original unchanged. Both accept `reverse=True` for descending order.

#### Sorting and Reversing

### Worked Example

```python
scores = [82, 91, 76, 88]
scores.sort()                           # Permanent sort in-place
print(scores)                           # [76, 82, 88, 91]

fruits = ["orange", "apple", "banana"]
sorted_fruits = sorted(fruits)          # Temporary sort — original unchanged
print(fruits)                           # ['orange', 'apple', 'banana']
print(sorted_fruits)                    # ['apple', 'banana', 'orange']

scores.reverse()                        # Reverse in-place -> [91, 88, 82, 76]
scores.sort(reverse=True)               # Sort descending -> [91, 88, 82, 76]
print(scores)                           # [91, 88, 82, 76]
print(len(scores))                      # Length: 4
```

### Expected Behavior or Output

Output of example 1:
```
[76, 82, 88, 91]
['orange', 'apple', 'banana']
['apple', 'banana', 'orange']
[91, 88, 82, 76]
4
```

### Common Mistakes

1. Writing `scores = scores.sort()`. `sort()` returns `None`, so the list is lost.
2. Sorting a list that mixes numbers and text, which raises a `TypeError`.
3. Expecting `reverse()` to sort. It only flips the current order.

### Activities

1. Predict the result of `scores.sort()` and `scores.sort(reverse=True)` on the shared scores, then check.
2. Use `sorted(scores)` and show that the original list is unchanged.
3. Sort the words `["pencil", "folder", "notebook"]` and print them.
4. Explain the difference between `sort()` and `sorted()` in two sentences.

### Accessibility Practice

Print each sorted version on its own labelled line (`Ascending:`, `Descending:`). The first and last numbers are the quickest to check by ear.

### Skills Checklist

- [ ] I can sort a list permanently using `.sort()`.
- [ ] I can get a temporarily sorted version using `sorted()`.
- [ ] I can reverse a list using `.reverse()`.
- [ ] I can find how many items are in a list using `len()`.

---

## Lesson 4.3: Tuples — Immutable Lists

### Reading References
- Matthes: Chapter 4 (Working with Lists), the section on tuples

### Learning Objectives
- Create a tuple in Python.
- Explain the main difference between a list and a tuple (mutability).
- Access items in a tuple by their index.

### Concept Explanation

A *tuple* is an ordered collection like a list, written with parentheses, but it cannot be changed after it is created. Use a tuple for a fixed group of values such as the shared coordinates (3, 4). Because it cannot change, a tuple can also be used where Python needs a value that never changes, such as a dictionary key.

#### Tuples

Tuples are defined with parentheses and **cannot be changed** after creation.


**When to use tuples:** For data that should remain constant (coordinates, RGB values, fixed settings).

### Worked Example

```python
coordinates = (3, 4)
x, y = coordinates        # tuple unpacking
print(coordinates[0])     # 3
print(coordinates[-1])    # 4
print(x, y)               # 3 4

# This would cause a TypeError:
# coordinates[1] = 5
```

### Expected Behavior or Output

Output of example 1:
```
3
4
3 4
```

### Common Mistakes

1. Writing `(5)` for a one-item tuple. A one-item tuple needs a comma: `(5,)`.
2. Trying to assign to an item (`coordinates[1] = 5`), which raises a `TypeError`.
3. Using a list when the data should never change, so an accidental change goes unnoticed.

### Activities

1. Create the tuple `(3, 4)`, unpack it into `x` and `y`, and print both.
2. Write a function that returns a name, an age, and a height as a tuple and unpack all three.
3. Try to change one item of a tuple and read the error message aloud.
4. Explain, in two sentences, when a tuple is a better choice than a list.

### Accessibility Practice

Say the parentheses and the commas aloud when reading a tuple, because a one-item tuple differs from a plain value only by its trailing comma. Read error messages from the last line upward to find the problem quickly.

### Skills Checklist

- [ ] I can create a tuple in Python.
- [ ] I can explain the main difference between a list and a tuple (mutability).
- [ ] I can access items in a tuple by their index.

---

## Lesson 4.4: Introducing Dictionaries

### Reading References
- Zelle: Chapter 11, pages 307–309
- Matthes: Chapter 6, pages 91–98

### Learning Objectives
- Create a dictionary in Python.
- Explain what a key-value pair is.
- Access a value in a dictionary using its key.
- Add, modify, and remove key-value pairs.

### Concept Explanation

#### Dictionary Basics

A dictionary stores **key-value pairs**. Keys must be unique and immutable (strings, numbers, tuples). Values can be anything.

```python
student_profile = {
    "name": "Avery",
    "age": 16,
    "height_m": 1.72,

    "favorite_subject": "Computer Science",
}

print(student_profile["name"])
print(student_profile["favorite_subject"])

# Demonstrate adding and removing a temporary key without changing
# the four-field canonical student record.
student_profile["temporary_note"] = "Dictionary example"
del student_profile["temporary_note"]
print(sorted(student_profile))
