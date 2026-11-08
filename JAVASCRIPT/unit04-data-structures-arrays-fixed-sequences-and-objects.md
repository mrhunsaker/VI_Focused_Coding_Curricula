# Unit 4: Data Structures — Arrays, Fixed Sequences, and Objects

## Overview
This unit maps Python lists, tuples, and dictionaries to idiomatic JavaScript. JavaScript arrays are mutable sequences; a frozen array can express fixed-sequence intent; plain objects represent records; and `Map` represents a dynamic key-value collection.

## Lesson 4.1: More on Arrays
<<<<<<< HEAD
### Concept Explanation
Array methods such as `push()`, `pop()`, and `splice()` mutate an array. Methods such as `slice()` return a new array. Numeric sorting requires a comparator because the default sort is lexicographic.


### Reading References
=======

### Reading References

>>>>>>> 2067a20 (curriculum clearning and updates)
- Python source counterpart: Unit 4, Lesson 4.1.
- MDN: Array methods.

### Learning Objectives
<<<<<<< HEAD
=======

>>>>>>> 2067a20 (curriculum clearning and updates)
- Add, insert, update, and remove array elements.
- Distinguish mutating methods from methods that return a new array.
- Preserve and process the canonical score data.

<<<<<<< HEAD
### Worked Example
=======
### Concept Explanation

Array methods such as `push()`, `pop()`, and `splice()` mutate an array. Methods such as `slice()` return a new array. Numeric sorting requires a comparator because the default sort is lexicographic.

### Worked Example

>>>>>>> 2067a20 (curriculum clearning and updates)
```javascript
const scores = [82, 91, 76, 88];
scores.push(95);
scores.splice(1, 0, 85);
const removed = scores.pop();
console.log(`Removed: ${removed}`);
console.log(`Scores: ${scores.join(", ")}`);
```

Expected output:
```text
Removed: 95
Scores: 82, 85, 91, 76, 88
```

### Expected Behavior or Output
<<<<<<< HEAD
The example removes 95 and prints the remaining scores in the order 82, 85, 91, 76, 88.

### Common Mistakes
=======

The example removes 95 and prints the remaining scores in the order 82, 85, 91, 76, 88.

### Common Mistakes

>>>>>>> 2067a20 (curriculum clearning and updates)
- Confusing `splice()` (mutates) with `slice()` (returns a copy).
- Assuming `pop()` returns the updated array rather than the removed element.
- Sorting numbers without a numeric comparator.

### Activities
<<<<<<< HEAD
=======

>>>>>>> 2067a20 (curriculum clearning and updates)
1. Append 95 to the canonical scores.
2. Insert 85 at index 1.
3. Remove the final element and report the returned value.
4. Sort a copy numerically with `(a, b) => a - b`.

### Accessibility Practice
<<<<<<< HEAD
Announce whether an operation mutates the original array or returns a new one. Read resulting values sequentially.

### Skills Checklist
=======

Announce whether an operation mutates the original array or returns a new one. Read resulting values sequentially.

### Skills Checklist

>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can add and remove array elements.
- [ ] I can insert at an index.
- [ ] I can distinguish mutating and non-mutating methods.
- [ ] I can sort numeric arrays correctly.

## Lesson 4.2: Organizing Arrays
<<<<<<< HEAD
### Concept Explanation
Sorting and reversing can mutate their receiver. Spread syntax creates a shallow copy, allowing a separate primitive-value array to be sorted or reversed without changing the original.


### Reading References
=======

### Reading References

>>>>>>> 2067a20 (curriculum clearning and updates)
- Python source counterpart: Unit 4, Lesson 4.2.
- MDN: Array sorting and iteration methods.

### Learning Objectives
<<<<<<< HEAD
=======

>>>>>>> 2067a20 (curriculum clearning and updates)
- Sort and reverse arrays.
- Create filtered and transformed arrays.
- Explain mutation and copying.

<<<<<<< HEAD
### Worked Example
=======
### Concept Explanation

Sorting and reversing can mutate their receiver. Spread syntax creates a shallow copy, allowing a separate primitive-value array to be sorted or reversed without changing the original.

### Worked Example

>>>>>>> 2067a20 (curriculum clearning and updates)
```javascript
const scores = [82, 91, 76, 88];
const sorted = [...scores].sort((a, b) => a - b);
const reversed = [...sorted].reverse();
console.log(`Original: ${scores.join(", ")}`);
console.log(`Sorted: ${sorted.join(", ")}`);
console.log(`Reversed: ${reversed.join(", ")}`);
```

Expected output:
```text
Original: 82, 91, 76, 88
Sorted: 76, 82, 88, 91
Reversed: 91, 88, 82, 76
```

### Expected Behavior or Output
<<<<<<< HEAD
The original order remains 82, 91, 76, 88; the sorted copy is 76, 82, 88, 91; the reversed copy is 91, 88, 82, 76.

### Common Mistakes
=======

The original order remains 82, 91, 76, 88; the sorted copy is 76, 82, 88, 91; the reversed copy is 91, 88, 82, 76.

### Common Mistakes

>>>>>>> 2067a20 (curriculum clearning and updates)
- Calling `sort()` without a comparator for numeric data.
- Reversing the original array when a copy was intended.
- Assuming spread syntax makes a deep copy of nested objects.

### Activities
<<<<<<< HEAD
=======

>>>>>>> 2067a20 (curriculum clearning and updates)
1. Sort the canonical scores from lowest to highest.
2. Reverse a copy and preserve the original order.
3. Filter scores of 80 or higher.
4. Explain why a shallow copy is sufficient for an array of primitive numbers but not necessarily for nested objects.

### Accessibility Practice
<<<<<<< HEAD
Label each result as original, sorted, reversed, or filtered. Avoid presenting the distinction only through visual ordering.

### Skills Checklist
=======

Label each result as original, sorted, reversed, or filtered. Avoid presenting the distinction only through visual ordering.

### Skills Checklist

>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can sort numbers with a comparator.
- [ ] I can reverse a copy of an array.
- [ ] I can filter an array.
- [ ] I can explain shallow copying.

## Lesson 4.3: Tuples — Immutable Sequences in JavaScript

### Reading References
- Python source counterpart: Unit 4, Lesson 4.3.
- MDN: Object.freeze().

### Learning Objectives
- Explain that JavaScript has no built-in tuple type with Python tuple semantics.
- Use a frozen array to express fixed-sequence intent.
- Distinguish a constant binding from immutable object contents.

### Concept Explanation
JavaScript has no native tuple type. For a short fixed sequence, a frozen array can communicate that the values should not be changed. `Object.freeze()` is shallow: nested objects are not automatically frozen. TypeScript has tuple types, but those are outside this JavaScript unit.

### Worked Example
```javascript
"use strict";
const coordinates = Object.freeze([3, 4]);
console.log(`x: ${coordinates[0]}`);
console.log(`y: ${coordinates[1]}`);
console.log(`Distance: ${Math.hypot(coordinates[0], coordinates[1])}`);
```

### Expected Behavior or Output
```text
x: 3
y: 4
Distance: 5
```
Attempting to change a frozen array element in strict mode throws a TypeError.

### Common Mistakes
- Assuming `const` freezes array contents.
- Assuming `Object.freeze()` is deep.
- Describing a frozen array as a true language-level tuple.

### Activities
1. Create a frozen coordinate pair using the canonical values (3, 4).
2. Read each coordinate by index and by a descriptive label.
3. Attempt to change an element in strict mode and observe the error.
4. Compare the frozen coordinates with a mutable scores array.

### Accessibility Practice
Identify each position by semantic name (x or y), not only by index. Read the fixed-sequence contract aloud before attempting mutation.

### Skills Checklist
- [ ] I can explain why JavaScript has no direct Python tuple equivalent.
- [ ] I can use a frozen array for fixed-sequence intent.
- [ ] I can distinguish const binding from object immutability.
- [ ] I can explain the shallow behavior of Object.freeze().

## Lesson 4.4: Introducing Dictionaries — JavaScript Objects and Map

### Reading References
- Python source counterpart: Unit 4, Lesson 4.4.
- MDN: Working with objects and Map.

### Learning Objectives
- Represent a record with an object literal.
- Use Map for dynamic key-value storage.
- Add, retrieve, update, and test entries.

### Concept Explanation
A plain object is appropriate for a record with named fields such as name, quantity, and unit price. `Map` is appropriate for a dynamic key-value collection and supports keys of any value type. A missing object property or Map key returns `undefined`, not zero.

### Worked Example
```javascript
const inventory = [
  { name: "Notebook", quantity: 3, unitPrice: 2.50 },
  { name: "Pencil", quantity: 10, unitPrice: 0.50 },
  { name: "Folder", quantity: 4, unitPrice: 1.25 }
];

const quantities = new Map(inventory.map(item => [item.name, item.quantity]));
console.log(quantities.get("Notebook"));
console.log(quantities.has("Pencil"));
quantities.set("Pencil", 12);
console.log(quantities.get("Pencil"));
```

### Expected Behavior or Output
```text
3
true
12
```
The canonical inventory contains three records. Its total value is $17.50.

### Common Mistakes
- Confusing object properties with Map entries.
- Using bracket notation on a Map instead of `get()` and `set()`.
- Assuming a missing key returns zero rather than `undefined`.

### Activities
1. Create the three canonical inventory records.
2. Create a Map from item names to quantities.
3. Update the Pencil quantity from 10 to 12.
4. Calculate the total value of the original inventory and explain the effect of the quantity update.

### Accessibility Practice
Print item names, quantities, and prices as labeled text. Use one inventory record per output line.

### Skills Checklist
- [ ] I can represent a record with a plain object.
- [ ] I can create and use a Map.
- [ ] I can add, retrieve, update, and test Map entries.
- [ ] I can distinguish objects from Maps.

## Lesson 4.5: Looping Through Objects and Maps

### Reading References
- Python source counterpart: Unit 4, Lesson 4.5.
- MDN: Object.entries() and Map iteration.

### Learning Objectives
- Traverse object keys, values, and key-value pairs.
- Iterate over Map entries.
- Produce readable reports from structured data.

### Concept Explanation
Use `Object.keys()`, `Object.values()`, or `Object.entries()` to traverse an object. A Map is directly iterable and yields key-value pairs. Choose the method that matches the data structure rather than assuming the APIs are interchangeable.

### Worked Example
```javascript
const student = {
  name: "Avery",
  age: 16,
  heightM: 1.72,
  favoriteSubject: "Computer Science"
};

for (const [key, value] of Object.entries(student)) {
  console.log(`${key}: ${value}`);
}
```

### Expected Behavior or Output
```text
name: Avery
age: 16
heightM: 1.72
favoriteSubject: Computer Science
```

### Common Mistakes
- Iterating over object keys when key-value pairs are needed.
- Modifying a collection during traversal without considering the effect.
- Assuming Map and object iteration APIs are interchangeable.

### Activities
1. Print every field in Avery's canonical student profile.
2. Iterate over the inventory Map and print each item and quantity.
3. Calculate the total number of inventory units.
4. Compare `Object.keys()`, `Object.values()`, and `Object.entries()`.

### Accessibility Practice
Provide one key-value pair per line and announce when iteration begins and ends. Keep output order stable for instructional examples.

### Skills Checklist
- [ ] I can traverse object keys, values, and entries.
- [ ] I can traverse Map entries.
- [ ] I can choose the appropriate traversal API.
- [ ] I can produce sequential textual reports.
<<<<<<< HEAD
=======

>>>>>>> 2067a20 (curriculum clearning and updates)
