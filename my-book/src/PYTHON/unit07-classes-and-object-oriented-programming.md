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
