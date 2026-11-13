# Unit 7: Classes and Object-Oriented Programming

## Overview

Model the shared inventory item as an object: constructors, methods, inheritance, and composition.

---


## Lesson 7.1: Why Learn About Classes?

### Reading References
- [Classes](https://kotlinlang.org/docs/classes.html)
- [Visibility modifiers](https://kotlinlang.org/docs/visibility-modifiers.html)
- Matching Python lesson: Lesson 7.1: Why Learn About Classes?

### Learning Objectives
- Explain a class as data plus behavior.
- Hide a property's setter to protect it.
- Describe encapsulation.

### Concept Explanation

A *class* describes what a kind of thing knows (its *properties*) and what it can do (its *functions*). An *object* is one actual thing made from a class. Bundling data with the functions that work on it is called **encapsulation**. The shared example is an inventory *item* with a name, a quantity, and a unit price.

Kotlin lets you protect a property with a *private setter*: `var quantity: Int = quantity` followed by `private set` on the next line means code outside the class can read `quantity` but cannot assign to it. Changes must go through a function such as `restock`, which can check them.

Kotlin does not have a `new` keyword: you create an object by calling the class like a function, `Item("Notebook", 3, 2.50)`.

A Notebook with quantity 3 and unit price 2.50 is worth 7.50. Restocking 2 raises that to 12.50, and a negative restock is refused.

### Worked Example

```kotlin
class Item(val name: String, quantity: Int, val unitPrice: Double) {
    var quantity: Int = quantity
        private set

    fun restock(amount: Int): Boolean {
        if (amount < 0) return false
        quantity += amount
        return true
    }

    fun totalValue(): Double = quantity * unitPrice

    fun describe() {
        println("$name: $quantity at ${"%.2f".format(unitPrice)} each, value ${"%.2f".format(totalValue())}")
    }
}

fun main() {
    val notebook = Item("Notebook", 3, 2.50)
    notebook.describe()
    println(notebook.restock(2))
    notebook.describe()
    println(notebook.restock(-1))
    println(notebook.quantity)
    // notebook.quantity = 99   // would not compile: the setter is private
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
true
Notebook: 5 at 2.50 each, value 12.50
false
5
```

### Common Mistakes
1. Treating a class as one single thing. A class is a blueprint; each call such as `Item(...)` makes a separate object.
2. Making every property public and changeable, so outside code can put the object into an invalid state.
3. Looking for a `new` keyword, which Kotlin does not have.

### Activities
1. Predict the five printed lines before running.
2. Add a function `isLowStock()` that returns true when the quantity is below 5.
3. Uncomment the assignment, read the compiler message, and restore the comment.
4. Explain what encapsulation means and why a private setter helps.

### Accessibility Practice

Describe a class as a list read in order: the name, then each property, then each function. Reading a class aloud works best by saying 'class Item, open parenthesis, val name colon String...' and listening for the braces that show structure.

### Skills Checklist
- [ ] I can explain data plus behavior.
- [ ] I can use a private setter.
- [ ] I can create an object without `new`.
- [ ] I can describe encapsulation.
- [ ] I can read a class definition aloud.

---

## Lesson 7.2: Creating Classes and Objects

### Reading References
- [Classes](https://kotlinlang.org/docs/classes.html)
- [Exceptions: require](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 7.2: Creating and Using a Class

### Learning Objectives
- Declare a class with a primary constructor.
- Validate in an `init` block with `require`.
- Create several objects with the same properties.

### Concept Explanation

A class declares its constructor right after its name: `class Item(val name: String, val quantity: Int, val unitPrice: Double)`. Writing `val` or `var` in front of a constructor parameter makes it a property in one step.

An `init` block runs whenever an object is created, so it is the place to check the values. `require(condition) { message }` throws an `IllegalArgumentException` with the message when the condition is false. An object that cannot be created invalid never needs to be checked again.

The example creates the three shared inventory items. Each has the same properties with different values. A class is a blueprint and each object is one *instance*.

### Worked Example

```kotlin
class Item(val name: String, val quantity: Int, val unitPrice: Double) {
    init {
        require(quantity >= 0) { "quantity must not be negative" }
        require(unitPrice >= 0.0) { "unit price must not be negative" }
    }
}

fun main() {
    val notebook = Item("Notebook", 3, 2.50)
    val pencil = Item("Pencil", 10, 0.50)
    val folder = Item("Folder", 4, 1.25)

    for (item in listOf(notebook, pencil, folder)) {
        println("${item.name}: ${item.quantity} at ${"%.2f".format(item.unitPrice)}")
    }

    val attempt = runCatching { Item("Broken", -1, 1.0) }
    println(attempt.exceptionOrNull()?.message)
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50
Pencil: 10 at 0.50
Folder: 4 at 1.25
quantity must not be negative
```

### Common Mistakes
1. Forgetting `val` in the constructor, so the parameter is not a property and cannot be read later.
2. Validating in each caller instead of once in `init`.
3. Catching the `IllegalArgumentException` and ignoring it, so the program continues with no object.

### Activities
1. Create a fourth item with your own values and print it.
2. Add a rule that the name must not be blank.
3. Create two items with the same name and different quantities and show that they are separate objects.
4. Explain what `init` does and when it runs.

### Accessibility Practice

Say the constructor aloud in order and check that the closing parenthesis and brace match. Print each object on its own line with its name so the output can be matched to the objects by ear.

### Skills Checklist
- [ ] I can write a primary constructor.
- [ ] I can validate with `init` and `require`.
- [ ] I can create several objects.
- [ ] I know what an instance is.
- [ ] I can read a class header aloud.

---

## Lesson 7.3: Properties and Functions

### Reading References
- [Properties](https://kotlinlang.org/docs/properties.html)
- [Classes](https://kotlinlang.org/docs/classes.html)
- Matching Python lesson: Lesson 7.3: Working with Attributes and Methods

### Learning Objectives
- Define a computed property and member functions.
- Change properties directly and through functions.
- Validate in a function.

### Concept Explanation

A *property* can be stored (`var quantity`) or *computed*: `val totalValue: Double get() = quantity * unitPrice` has no stored value and is calculated each time it is read. Callers use it like any property, without parentheses.

A *member function* works on the object: `item.restock(2)`. A function that validates its input protects the object from invalid data. Directly changing a public `var` skips that protection, so make a property `var` only when any value is acceptable.

The example adds a computed value, a validity check, a restock function, and a describe function to the shared Notebook.

### Worked Example

```kotlin
class Item(val name: String, var quantity: Int, val unitPrice: Double) {
    val totalValue: Double
        get() = quantity * unitPrice

    fun isValid(): Boolean = name.isNotBlank() && quantity >= 0 && unitPrice >= 0.0

    fun restock(amount: Int) {
        if (amount < 0) {
            println("Cannot restock a negative amount.")
            return
        }
        quantity += amount
    }

    fun describe() {
        println("$name: $quantity at ${"%.2f".format(unitPrice)} each, value ${"%.2f".format(totalValue)}")
    }
}

fun main() {
    val notebook = Item("Notebook", 3, 2.50)
    notebook.describe()
    notebook.restock(2)
    notebook.describe()
    notebook.quantity = 4
    notebook.describe()
    notebook.restock(-1)
    println(notebook.isValid())
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
Notebook: 5 at 2.50 each, value 12.50
Notebook: 4 at 2.50 each, value 10.00
Cannot restock a negative amount.
true
```

### Common Mistakes
1. Writing `totalValue()` with parentheses for a property, or `isValid` without them for a function.
2. Changing a public `var` directly and skipping the validation that a function would perform.
3. Storing a value that can be computed, so it goes out of date when the inputs change.

### Activities
1. Predict the output of all six calls before running.
2. Add a function `discounted(rate: Double): Double` that returns the value after a discount without changing the item.
3. Make `quantity` have a private setter and see which lines stop compiling.
4. Explain the difference between a stored and a computed property.

### Accessibility Practice

Name functions after actions (`restock`, `describe`) so a call reads as a sentence. Print one line per call, so the screen reader announces the effect of each step in order.

### Skills Checklist
- [ ] I can write a computed property.
- [ ] I can write member functions.
- [ ] I can validate in a function.
- [ ] I know when to use a private setter.
- [ ] I can tell a property from a function when reading.

---

## Lesson 7.4: Inheritance

### Reading References
- [Inheritance](https://kotlinlang.org/docs/inheritance.html)
- Matching Python lesson: Lesson 7.4: Inheritance

### Learning Objectives
- Declare an `open` class and a subclass.
- Override a function and call the parent's version.
- Explain polymorphism.

### Concept Explanation

Kotlin classes are **final by default**: nothing can inherit from them. Mark a class `open` to allow subclasses, and mark each function that may be replaced `open` as well. A subclass names its parent after a colon and passes constructor values up: `class DiscountedItem(...) : Item(name, quantity, unitPrice)`. A function that replaces a parent's function is marked `override`, and `super.totalValue()` calls the parent's version.

*Polymorphism* means that the same function name behaves differently for different classes. Here `describe`, written once in `Item`, calls `totalValue()`, so a `DiscountedItem` prints its discounted value automatically.

The example discounts the shared Folder (4 at 1.25) by 20 percent, so its value is 4.00 instead of 5.00.

### Worked Example

```kotlin
open class Item(val name: String, val quantity: Int, val unitPrice: Double) {
    open fun totalValue(): Double = quantity * unitPrice

    fun describe() {
        println("$name: $quantity at ${"%.2f".format(unitPrice)} each, value ${"%.2f".format(totalValue())}")
    }
}

class DiscountedItem(name: String, quantity: Int, unitPrice: Double, val discountRate: Double) :
    Item(name, quantity, unitPrice) {
    override fun totalValue(): Double = super.totalValue() * (1 - discountRate)
}

fun main() {
    val folder = DiscountedItem("Folder", 4, 1.25, 0.20)
    folder.describe()
    println(folder is Item)

    val items: List<Item> = listOf(Item("Notebook", 3, 2.50), folder)
    for (item in items) println("${item.name}: ${"%.2f".format(item.totalValue())}")
}
```

### Expected Behavior or Output

The program prints:
```text
Folder: 4 at 1.25 each, value 4.00
true
Notebook: 7.50
Folder: 4.00
```

### Common Mistakes
1. Forgetting `open`, so the compiler refuses to let another class inherit or override.
2. Forgetting `override` on a function that replaces a parent's function, which is a compile error.
3. Using inheritance for a "has a" relationship; use composition instead (Lesson 7.5).

### Activities
1. Predict the output before running.
2. Add a subclass `PerishableItem` with an `expires` property and override `describe` by making it `open`.
3. Explain why `describe` prints the discounted value without being redefined.
4. List the order in which Kotlin looks for `totalValue` on a `DiscountedItem`.

### Accessibility Practice

Describe inheritance as an ordered list: the subclass first, then its parent. Speaking the chain aloud ('DiscountedItem, then Item') is clearer than a diagram.

### Skills Checklist
- [ ] I can declare an open class and a subclass.
- [ ] I can override a function.
- [ ] I can call `super`.
- [ ] I can explain polymorphism.
- [ ] I know classes are final by default.

---

## Lesson 7.5: Composition

### Reading References
- [Classes](https://kotlinlang.org/docs/classes.html)
- Matching Python lesson: Lesson 7.5: Instances as Attributes (Composition)

### Learning Objectives
- Explain composition ("has a").
- Hold a list of objects inside another object.
- Build an inventory from the shared items.

### Concept Explanation

*Composition* means that one object contains other objects. An inventory *has* items; it is not a kind of item. Composition is usually simpler and safer than inheritance when objects are related by containment.

The container keeps a private list of its parts and exposes functions that loop over the parts and call each part's own functions, so the container does not need to know how a part works. Keeping the list `private` forces other code to use `add` and `report`.

The example builds an `Inventory` with the three shared items and reports each quantity and the total value, 17.50.

### Worked Example

```kotlin
class Item(val name: String, val quantity: Int, val unitPrice: Double) {
    fun totalValue(): Double = quantity * unitPrice
}

class Inventory {
    private val items = mutableListOf<Item>()

    fun add(item: Item) {
        items.add(item)
    }

    fun find(name: String): Item? = items.firstOrNull { it.name == name }

    fun totalValue(): Double = items.sumOf { it.totalValue() }

    fun report() {
        for (item in items) {
            println("${item.name}: ${item.quantity}")
        }
        println("Total value: " + "%.2f".format(totalValue()))
    }
}

fun main() {
    val inventory = Inventory()
    inventory.add(Item("Notebook", 3, 2.50))
    inventory.add(Item("Pencil", 10, 0.50))
    inventory.add(Item("Folder", 4, 1.25))
    inventory.report()
    println(inventory.find("Pencil")?.quantity)
    println(inventory.find("Eraser"))
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3
Pencil: 10
Folder: 4
Total value: 17.50
10
null
```

### Common Mistakes
1. Using inheritance where a "has a" relationship is meant.
2. Making the list public so other code changes it without going through `add`.
3. Letting the container read each item's properties directly instead of calling the item's functions.

### Activities
1. Predict the output.
2. Add `remove(name)` to `Inventory` and test it.
3. Add a function that returns the names of items with a quantity below 5.
4. Explain "is a" versus "has a" with two examples.

### Accessibility Practice

Report the inventory as one labelled line per item and a final total line, so the screen reader reads a complete summary in order.

### Skills Checklist
- [ ] I can explain composition.
- [ ] I can hold a list of objects in an object.
- [ ] I can keep a list private.
- [ ] I can say "is a" versus "has a".
- [ ] I can build the shared inventory.

---
