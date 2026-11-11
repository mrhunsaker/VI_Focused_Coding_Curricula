# Unit 4: Data Structures — Lists and Dictionaries

## Overview

Work with lists, sorting, fixed records, dictionaries, and stable traversal of the shared inventory.

---


## Lesson 4.1: More on Mutable Lists

### Reading References
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- [Adding and removing elements](https://kotlinlang.org/docs/collection-write.html)
- Matching Python lesson: Lesson 4.1: More on Lists

### Learning Objectives
- Add, insert, replace, and remove list items.
- Remove by value and by position without confusing them.
- Search a list with `in` and `indexOf`.

### Concept Explanation

A `MutableList` changes with `add(value)` (append), `add(index, value)` (insert and shift), `set` or `list[i] = value` (replace), `remove(value)` (remove the first matching **value**), and `removeAt(index)` (remove by **position**). For a list of `Int`, `remove(76)` removes the number 76, while `removeAt(76)` would try to remove position 76. `removeAt` returns the removed item.

`value in list` tests membership, and `indexOf(value)` returns the position or `-1`. These searches look at each item in turn, so they take longer for longer lists.

Avoid `removeLast()` in code that must run on several JDK versions: newer JDKs add a method with the same name to `List`, and the behavior depends on the JDK. `removeAt(lastIndex)` is portable.

The example applies the same operations as the Python course to the shared scores, from [82, 91, 76, 88] to [82, 85, 93, 88].

### Worked Example

```kotlin
fun main() {
    val scores = mutableListOf(82, 91, 76, 88)

    scores.add(95)
    scores.add(1, 85)
    scores[2] = 93
    scores.remove(76)
    val last = scores.removeAt(scores.lastIndex)

    println(scores)
    println("${scores.size} items; removed $last")
    println(88 in scores)
    println(scores.indexOf(88))
    println(scores.indexOf(100))
}
```

### Expected Behavior or Output

The program prints:
```text
[82, 85, 93, 88]
4 items; removed 95
true
3
-1
```

### Common Mistakes
1. Confusing `remove(76)` (by value) with `removeAt(76)` (by position).
2. Removing items inside a `for` loop over the same list, which throws `ConcurrentModificationException`.
3. Calling `removeLast()` and getting different behavior on different JDKs.

### Activities
1. Trace the list after every operation and write each version as a sentence.
2. Remove the first score with `removeAt(0)` and describe what happens to the others.
3. Remove every score below 80 safely, using `removeAll { ... }`.
4. Print the position of the first score above 90 with `indexOfFirst`.

### Accessibility Practice

After every change, print the whole list on one line so the screen reader reads a complete state in one pass. Say the method names aloud, and notice how `remove` and `removeAt` sound different.

### Skills Checklist
- [ ] I can add, insert, replace, and remove items.
- [ ] I can tell `remove` from `removeAt`.
- [ ] I can search with `in` and `indexOf`.
- [ ] I know why `removeLast()` is avoided.
- [ ] I can show a list in one line.

---

## Lesson 4.2: Sorting and Organizing Lists

### Reading References
- [Ordering](https://kotlinlang.org/docs/collection-ordering.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 4.2: Organizing Lists

### Learning Objectives
- Sort a list ascending and descending.
- Tell `sorted()` (a new list) from `sort()` (in place).
- Sort by a computed key.

### Concept Explanation

Kotlin offers two families. **Returning** functions leave the original alone and give a new list: `sorted()`, `sortedDescending()`, `sortedBy { ... }`, and `reversed()`. **In-place** functions change a `MutableList`: `sort()`, `sortDescending()`, and `reverse()`. A read-only `List` has only the returning kind.

`sortedBy { it.length }` sorts by a computed key, here the length of each word, and keeps the original order of items with equal keys because the sort is *stable*.

The shared scores sort to 76, 82, 88, 91 in ascending order and 91, 88, 82, 76 in descending order.

### Worked Example

```kotlin
fun main() {
    val scores = mutableListOf(82, 91, 76, 88)

    println("Original: $scores")
    println("Ascending: ${scores.sorted()}")
    println("Descending: ${scores.sortedDescending()}")
    println("Still original: $scores")

    scores.sort()
    println("Sorted in place: $scores")
    scores.reverse()
    println("Reversed in place: $scores")

    val words = listOf("pencil", "folder", "notebook")
    println(words.sorted())
    println(words.sortedBy { it.length })
}
```

### Expected Behavior or Output

The program prints:
```text
Original: [82, 91, 76, 88]
Ascending: [76, 82, 88, 91]
Descending: [91, 88, 82, 76]
Still original: [82, 91, 76, 88]
Sorted in place: [76, 82, 88, 91]
Reversed in place: [91, 88, 82, 76]
[folder, notebook, pencil]
[pencil, folder, notebook]
```

### Common Mistakes
1. Expecting `sorted()` to change the list. It returns a new list.
2. Calling `sort()` on a read-only `List`, which does not compile.
3. Expecting `reverse()` to sort. It only flips the current order.

### Activities
1. Predict each printed line before running.
2. Print the scores in descending order without changing the original.
3. Sort the words by their last letter with `sortedBy`.
4. Explain the difference between `sorted()` and `sort()` in two sentences.

### Accessibility Practice

Print each result on its own labelled line (`Ascending:`, `Descending:`). The first and last numbers are the quickest to check by ear.

### Skills Checklist
- [ ] I can sort ascending and descending.
- [ ] I know which functions change the list.
- [ ] I can use `sortedBy`.
- [ ] I can reverse a list.
- [ ] I can keep the original order.

---

## Lesson 4.3: Pairs, Triples, and Data Classes

### Reading References
- [Data classes](https://kotlinlang.org/docs/data-classes.html)
- [Destructuring declarations](https://kotlinlang.org/docs/destructuring-declarations.html)
- Matching Python lesson: Lesson 4.3: Tuples - Immutable Lists

### Learning Objectives
- Use `Pair` and `Triple` for small fixed groups.
- Declare a data class with `val` properties.
- Unpack values with destructuring.

### Concept Explanation

Kotlin has no general tuple type. For two or three values, use `Pair(a, b)` and `Triple(a, b, c)`, whose parts are `first`, `second`, and `third`. For anything you will use more than briefly, a **data class** with named properties is clearer: `data class Point(val x: Int, val y: Int)`.

A data class automatically provides `toString()`, `equals()` (so two points with the same values are equal), `copy()` (a new object with some values changed), and *destructuring*: `val (x, y) = point`. With `val` properties, the object cannot change after it is created, so use `copy(y = 10)` to get a changed version.

The shared coordinates are x = 3 and y = 4.

### Worked Example

```kotlin
data class Point(val x: Int, val y: Int)

fun minMax(values: List<Int>): Pair<Int, Int> = Pair(values.min(), values.max())

fun main() {
    val (x, y) = Pair(3, 4)
    println("x=$x y=$y")

    val point = Point(3, 4)
    println(point)
    val moved = point.copy(y = 10)
    println("$point -> $moved")
    println(point == Point(3, 4))

    val (low, high) = minMax(listOf(82, 91, 76, 88))
    println("low=$low high=$high")

    val profile = Triple("Avery", 16, 1.72)
    println("${profile.first} ${profile.second} ${profile.third}")
}
```

### Expected Behavior or Output

The program prints:
```text
x=3 y=4
Point(x=3, y=4)
Point(x=3, y=4) -> Point(x=3, y=10)
true
low=76 high=91
Avery 16 1.72
```

### Common Mistakes
1. Using `var` properties in a data class and then being surprised when values change.
2. Expecting `copy()` to change the original. It returns a new object.
3. Using `Pair` with unclear meanings (`first`, `second`) in code that others must read.

### Activities
1. Predict the output, then run.
2. Create a `Student` data class for the shared profile and print it.
3. Use `copy` to make a student one year older and print both.
4. Explain when a data class is a better choice than a `Pair`.

### Accessibility Practice

Named properties read better aloud than `first` and `second`. Printing a data class shows its name and every property, so the screen reader announces `Point(x=3, y=4)` as a complete sentence.

### Skills Checklist
- [ ] I can use `Pair` and `Triple`.
- [ ] I can declare a data class.
- [ ] I can destructure values.
- [ ] I can use `copy()`.
- [ ] I can choose between a pair and a data class.

---

## Lesson 4.4: Maps

### Reading References
- [Map-specific operations](https://kotlinlang.org/docs/map-operations.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 4.4: Introducing Dictionaries

### Learning Objectives
- Create a map and read, add, change, and remove entries.
- Handle a missing key with `?:`.
- Model the shared inventory item with a data class.

### Concept Explanation

A `Map` pairs keys with values. `mapOf(...)` is read-only and `mutableMapOf(...)` can change. Read with `map[key]`, which returns a **nullable** value: it is `null` when the key is missing. Combine it with the Elvis operator to supply a default: `map[key] ?: "unknown"`.

`map[key] = value` adds or replaces an entry, `remove(key)` deletes one, `containsKey(key)` tests for a key, and `size` counts the entries. `mutableMapOf` keeps insertion order.

A map with values of different types, such as `MutableMap<String, Any>`, is flexible but loses type checking. When the fields are known, a data class is safer, so the shared Notebook item is a data class.

### Worked Example

```kotlin
data class Item(val name: String, var quantity: Int, val unitPrice: Double)

fun main() {
    val profile = mutableMapOf<String, Any>(
        "name" to "Avery",
        "age" to 16,
        "heightM" to 1.72,
        "favoriteSubject" to "Computer Science",
    )
    println(profile["name"])
    profile["age"] = 17
    profile["gradeLevel"] = 11
    profile.remove("heightM")
    println(profile)
    println(profile["heightM"])
    println(profile["heightM"] ?: "unknown")
    println(profile.containsKey("gradeLevel"))

    val item = Item("Notebook", 3, 2.50)
    item.quantity += 2
    println(item)
    println("Stock value: ${item.quantity * item.unitPrice}")
}
```

### Expected Behavior or Output

The program prints:
```text
Avery
{name=Avery, age=17, favoriteSubject=Computer Science, gradeLevel=11}
null
unknown
true
Item(name=Notebook, quantity=5, unitPrice=2.5)
Stock value: 12.5
```

### Common Mistakes
1. Using a missing key and expecting an error. The result is `null`.
2. Using `!!` on a map lookup, which crashes when the key is missing.
3. Storing mixed types in `Map<String, Any>` and then needing casts everywhere.

### Activities
1. Predict the printed lines before running.
2. Add a `discount` key to the item as a data class property and print the discounted value.
3. Remove `favoriteSubject` and show what the lookup returns.
4. Explain why a data class is safer than `Map<String, Any>` for a record.

### Accessibility Practice

Print one entry per line when you need to read a map, because a one-line `{a=1, b=2}` is hard to navigate. Choose key names that read well aloud, such as `unitPrice`.

### Skills Checklist
- [ ] I can create and change a map.
- [ ] I know a lookup returns a nullable value.
- [ ] I can supply a default with `?:`.
- [ ] I can model an item with a data class.
- [ ] I can test for a key.

---

## Lesson 4.5: Traversing Maps

### Reading References
- [Map-specific operations](https://kotlinlang.org/docs/map-operations.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 4.5: Looping Through Dictionaries

### Learning Objectives
- Visit keys, values, and key-value pairs.
- Explain which maps keep insertion order.
- Produce sorted output and total the shared inventory.

### Concept Explanation

`for (key in map.keys)` visits keys, `for (value in map.values)` visits values, and `for ((key, value) in map)` visits pairs with destructuring.

Order matters for readable output. `mutableMapOf`, `linkedMapOf`, and `mapOf` keep **insertion order**, so output is stable. `hashMapOf` makes no promise about order. To list keys alphabetically, use `toSortedMap()`.

`sumOf { ... }` adds a computed number for every element, which is the compact way to total the shared inventory: Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25) are worth 7.50 + 5.00 + 5.00 = 17.50.

### Worked Example

```kotlin
data class Stock(val quantity: Int, val unitPrice: Double)

fun main() {
    val inventory = linkedMapOf(
        "Notebook" to Stock(3, 2.50),
        "Pencil" to Stock(10, 0.50),
        "Folder" to Stock(4, 1.25),
    )

    println("Keys:")
    for (name in inventory.keys) println(name)

    println("Quantities:")
    for (stock in inventory.values) println(stock.quantity)

    var totalValue = 0.0
    for ((name, stock) in inventory) {
        val lineValue = stock.quantity * stock.unitPrice
        println("$name: ${stock.quantity} in stock, value ${"%.2f".format(lineValue)}")
        totalValue += lineValue
    }
    println("Total inventory value: ${"%.2f".format(totalValue)}")

    println(inventory.toSortedMap().keys)
    println(inventory.values.sumOf { it.quantity * it.unitPrice })
}
```

### Expected Behavior or Output

The program prints:
```text
Keys:
Notebook
Pencil
Folder
Quantities:
3
10
4
Notebook: 3 in stock, value 7.50
Pencil: 10 in stock, value 5.00
Folder: 4 in stock, value 5.00
Total inventory value: 17.50
[Folder, Notebook, Pencil]
17.5
```

### Common Mistakes
1. Using a `HashMap` and expecting the same order every run.
2. Adding or removing entries while looping over the map, which throws `ConcurrentModificationException`.
3. Forgetting the parentheses in `for ((name, stock) in inventory)` and iterating over entries without unpacking them.

### Activities
1. Run the example and write the three key-value lines in order.
2. Print only the items with a quantity below 5.
3. Print the items from the highest line value to the lowest.
4. Explain how `toSortedMap()` differs from the default order.

### Accessibility Practice

Printing each inventory line as one sentence lets the screen reader announce the name, quantity, and value together. Because the order is stable, you can learn it and compare runs by ear.

### Skills Checklist
- [ ] I can visit keys, values, and pairs.
- [ ] I know which maps keep insertion order.
- [ ] I can sort keys.
- [ ] I can total with `sumOf`.
- [ ] I can total the shared inventory.

---
