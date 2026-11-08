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

### Learning Objectives
- Explain why functions are useful.
- Define a simple function in Python.
- Use parameters to specify function inputs.
- Call a function by its name.

### Concept Explanation

#### Function Syntax

```python
def function_name(parameter1, parameter2):
    """Docstring describing what the function does."""
    # Function body
    print(f"Hello, {parameter1}!")
```

### Worked Example

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

greet_name("Avery")
greet_name("Riley")
```

**Example 6.1.3: A Reusable Tip Calculator (shared calculator values)**
```python
def show_tip(bill, tip_rate):
    """Print the tip and the total for a bill."""
    tip = bill * tip_rate
    print(f"Tip: {tip:.2f}")
    print(f"Total: {bill + tip:.2f}")

show_tip(24.5, 0.15)
```

### Expected Behavior or Output

Expected output:
```
Tip: 3.67
Total: 28.18
```

### Common Mistakes

1. Writing `greet_user` without parentheses and expecting the function to run.
2. Forgetting the colon after the `def` line, or the indentation of the body.
3. Passing arguments in the wrong order, such as `show_tip(0.15, 24.5)`.

### Activities

1. Call `show_tip(100, 0.2)` and predict both printed lines.
2. Write a function `describe_student(name, age)` that prints one sentence.
3. Call `greet_name()` with no argument and read the error message.
4. Explain the difference between a parameter and an argument using the example.

### Accessibility Practice

Choose function names that read as actions when spoken, such as `show_tip`. Print complete sentences from a function so the screen reader announces the result of each call separately, and say 'open parenthesis, close parenthesis' for an empty parameter list.

### Skills Checklist

- [ ] I can explain why functions are useful.
- [ ] I can define a simple function in Python.
- [ ] I can use parameters to specify function inputs.
- [ ] I can call a function by its name.

---

## Lesson 6.2: Passing Arguments

### Reading References
- Matthes: Chapter 8 (Functions), the sections on passing arguments
- Zelle: Chapter 6 (Defining Functions)

### Learning Objectives
- Differentiate between a parameter and an argument.
- Pass arguments using positional order.
- Pass arguments using keyword arguments.

### Concept Explanation

#### Positional vs. Keyword Arguments

```python
def describe_animal(animal_type, animal_name):
    print(f"I have a {animal_type} named {animal_name}.")

# Positional arguments (order matters)
describe_animal("dog", "Buddy")

# Keyword arguments (order doesn't matter)
describe_animal(animal_name="Max", animal_type="cat")
```

#### Default Values

```python
def make_shirt(size, message="I love Python"):
    print(f"Making a {size}-sized shirt: '{message}'")

make_shirt("large")                       # Uses default message
make_shirt("medium", "Hello World")       # Custom message
```

### Worked Example

**Example: Default, Positional, and Keyword Arguments (shared calculator values)**
```python
def calculate_total(bill, tip_rate=0.15):
    return bill + bill * tip_rate

print(f"{calculate_total(24.5):.2f}")                       # default rate
print(f"{calculate_total(24.5, 0.20):.2f}")                 # positional
print(f"{calculate_total(tip_rate=0.10, bill=24.5):.2f}")   # keyword
```

### Expected Behavior or Output

Expected output:
```
28.18
29.40
26.95
```

### Common Mistakes

1. Putting a parameter with a default before a parameter without one in the definition, which is a syntax error.
2. Mixing positional and keyword arguments in an order Python does not allow (positional first).
3. Using a mutable default such as `[]`, which is shared between calls.

### Activities

1. Predict the three totals in the example before running it.
2. Add a third parameter `round_total` with the default `False` and use it.
3. Call the function with the arguments in a different order using keywords.
4. Explain why `tip_rate=0.15` is called a default value.

### Accessibility Practice

Keyword arguments make a call read as a sentence: 'calculate total, bill equals 24.5, tip rate equals 0.10'. Say the equals signs aloud and check that your screen reader announces them.

### Skills Checklist

- [ ] I can differentiate between a parameter and an argument.
- [ ] I can pass arguments using positional order.
- [ ] I can pass arguments using keyword arguments.

---

## Lesson 6.3: Return Values

### Reading References
- Matthes: Chapter 8 (Functions), the section on return values
- Zelle: Chapter 6 (Defining Functions)

### Learning Objectives
- Use `return` to send a value back from a function.
- Explain the difference between `print()` and `return`.
- Store the returned value of a function in a variable.

### Concept Explanation

#### The `return` Statement

```python
def add_numbers(num1, num2):
    """Adds two numbers and returns the result."""
    total = num1 + num2
    return total

result = add_numbers(5, 3)
print(f"The sum is: {result}")   # 8
```



**Key difference:** `print()` displays a value; `return` sends a value back to the caller for further use.

### Worked Example

**Example: Returning Computed Results (shared scores)**
```python
def average(scores):
    """Return the average of a list of scores."""
    return sum(scores) / len(scores)

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

avg = average([82, 91, 76, 88])   # returned, not just printed
print(f"Average: {avg}")
print(f"Grade for the average: {classify(avg)}")
```

### Expected Behavior or Output

Expected output:
```
Average: 84.25
Grade for the average: B
```

### Common Mistakes

1. Printing inside a function and then trying to use the result in a calculation. The function returned `None`.
2. Writing statements after `return` in the same block. They never run.
3. Ignoring a returned value, so the work of the function is lost.

### Activities

1. Predict the two printed results of the example before running.
2. Write `total(list)` that returns the sum of a list of numbers.
3. Write `is_passing(score)` that returns `True` or `False` using the shared thresholds.
4. Explain the difference between `print` and `return` in two sentences.

### Accessibility Practice

Return values from functions and print them in one place. A function that prints and returns at the same time can announce a result twice. Read the single printed line aloud and check it matches the returned value.

### Skills Checklist

- [ ] I can use `return` to send a value back from a function.
- [ ] I can explain the difference between `print()` and `return`.
- [ ] I can store the returned value of a function in a variable.

---

## Lesson 6.4: Functions with Lists and Dictionaries

### Reading References
- Matthes: Chapter 8 (Functions), the section on passing a list to a function

### Learning Objectives
- Pass a list or dictionary as an argument to a function.
- Understand that modifying a list inside a function affects the original.
- Create a copy of a list to avoid unintended modifications.

### Concept Explanation

Since lists are **mutable**, modifying them inside a function changes the original:

```python
def add_score(score_list, new_score):
    score_list.append(new_score)

scores = [82, 91, 76, 88]
add_score(scores, 95)
print(scores)   # [82, 91, 76, 88, 95]  - the original list changed
```

Expected output:
```
[82, 91, 76, 88, 95]
```

To prevent modification, pass a copy:
```python
add_score(scores[:], 100)   # Original unchanged
```

### Worked Example

**Example: Processing the Shared Inventory with a Function**
```python
def inventory_value(inventory):
    total = 0
    for details in inventory.values():
        total += details["quantity"] * details["unit_price"]
    return total

inventory = {
    "Notebook": {"quantity": 3, "unit_price": 2.50},
    "Pencil": {"quantity": 10, "unit_price": 0.50},
    "Folder": {"quantity": 4, "unit_price": 1.25},
}
print(f"Total inventory value: {inventory_value(inventory):.2f}")
```

### Expected Behavior or Output

Expected output:
```
Total inventory value: 17.50
```

### Common Mistakes

1. Expecting a function to receive its own copy of a list. It receives the same list and can change it.
2. Changing a list inside a function that is meant only to read it.
3. Making a copy with `copy = original` instead of `original[:]` or `list(original)`.

### Activities

1. Predict the printed lists in the example before running it.
2. Write `scale_prices(inventory, factor)` that changes the prices in place and show the effect.
3. Rewrite it so it returns a new inventory and leaves the original unchanged.
4. Explain the difference between passing a number and passing a list to a function.

### Accessibility Practice

State aloud before each call whether the function changes its argument. Print the list before and after the call so a screen reader user hears the effect, and use names such as `add_score` that say a change will happen.

### Skills Checklist

- [ ] I can pass a list or dictionary as an argument to a function.
- [ ] I understand that modifying a list inside a function affects the original.
- [ ] I can create a copy of a list to avoid unintended modifications.

---

## Lesson 6.5: Arbitrary Number of Arguments

### Reading References
- Matthes: Chapter 8 (Functions), the section on passing an arbitrary number of arguments

### Learning Objectives
- Define a function using `*args` for arbitrary positional arguments.
- Define a function using `**kwargs` for arbitrary keyword arguments.

### Concept Explanation

#### `*args` — Arbitrary Positional Arguments

```python
def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with:")
    for topping in toppings:
        print(f"  - {topping}")

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
```

**Example: Variable Number of Scores**
```python
def average(*scores):
    return sum(scores) / len(scores)

print(average(82, 91, 76, 88))   # any number of arguments
print(average(90, 80))
```

Expected output:
```
84.25
85.0
```

#### `**kwargs` — Arbitrary Keyword Arguments

### Worked Example

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

### Expected Behavior or Output

Output of example 1:
```
{'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
```

### Common Mistakes

1. Calling `average()` with no arguments, which divides by zero. Check the count first.
2. Putting `*args` before a normal parameter and being unable to pass the normal one by position.
3. Forgetting that `*args` is a tuple, not a list, so it cannot be changed.

### Activities

1. Predict the result of `average(82, 91, 76, 88)` and `average(90, 80)`.
2. Write `maximum(*numbers)` that returns the largest argument.
3. Write `join_words(separator, *words)` that joins any number of words.
4. Explain what the `*` does in a call such as `average(*scores)`.

### Accessibility Practice

Read variadic signatures aloud: 'define average, open parenthesis, star scores, close parenthesis'. Make sure your screen reader announces the star, since it changes the meaning of the parameter.

### Skills Checklist

- [ ] I can define a function using `*args` for arbitrary positional arguments.
- [ ] I can define a function using `**kwargs` for arbitrary keyword arguments.

<<<<<<< HEAD
## Canonical Shared Dataset — Inventory, Collections, and Functions

Use the same inventory records for list, dictionary, iteration, and function examples.

```python
inventory = [
    {"name": "Notebook", "quantity": 3, "unit_price": 2.50},
    {"name": "Pencil", "quantity": 10, "unit_price": 0.50},
    {"name": "Folder", "quantity": 4, "unit_price": 1.25},
]

def item_value(item):
    return item["quantity"] * item["unit_price"]

for item in inventory:
    print(item["name"], item["quantity"], f"${item['unit_price']:.2f}",
          f"${item_value(item):.2f}")

grand_total = sum(item_value(item) for item in inventory)
print(f"Inventory total: ${grand_total:.2f}")
```

Expected output:
```text
Notebook 3 $2.50 $7.50
Pencil 10 $0.50 $5.00
Folder 4 $1.25 $5.00
Inventory total: $17.50
```

For sequence exercises, use the canonical scores `[82, 91, 76, 88]`. For immutable-sequence exercises, use coordinates `(3, 4)`. Keep language-specific collection types idiomatic while preserving record values and calculation results.
=======
---
>>>>>>> 2067a20 (curriculum clearning and updates)
