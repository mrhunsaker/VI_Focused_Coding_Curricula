# Unit 4: Data Structures — Arrays, Tuples, and Objects

## Overview

Manipulate arrays and model fixed sequences, records, Maps, and object iteration. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

<<<<<<< HEAD
---

## Overview

Manipulate arrays and model fixed sequences, records, Maps, and object iteration. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

=======
>>>>>>> 2067a20 (curriculum clearning and updates)
## Lesson 4.1: More on arrays

### Reading References
- Python source counterpart: Unit 4 lesson 4.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Add, insert, update, remove, and inspect elements in a typed array.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Array methods such as push, splice, and pop mutate an array. `slice` returns a shallow copy. Use types to constrain the values stored.

### Worked Example
```typescript
const scores: number[] = [82, 91, 76, 88];
scores.push(95);
scores.splice(1, 1);
console.log(scores.join(", "));
console.log(scores.length);
```

### Expected Behavior or Output
The resulting values are 82, 76, 88, 95 and the length is 4.

### Common Mistakes
- Confusing splice with slice.
- Using an invalid index without checking it.
- Assuming push returns the updated array rather than the new length.

### Activities
1. Append a score.
2. Remove a selected score with splice.
3. Compare the original array with a slice copy.

### Accessibility Practice
Read the mutation step before reporting the new array contents. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can add and remove array elements.
- [ ] I can distinguish splice from slice.
- [ ] I can inspect array length and contents.

---

---

## Lesson 4.2: Organizing arrays: sorting and reversing

### Reading References
- Python source counterpart: Unit 4 lesson 4.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Sort and reverse scores without unexpectedly changing the original collection.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The default sort compares values as strings. Numeric sorting needs a comparator. `toSorted` returns a sorted copy on supported modern runtimes; spread plus sort is a compatible alternative.

### Worked Example
```typescript
const scores = [82, 91, 76, 88];
const ascending = [...scores].sort((a, b) => a - b);
const descending = [...ascending].reverse();
console.log(scores.join(", "));
console.log(ascending.join(", "));
console.log(descending.join(", "));
```

### Expected Behavior or Output
Original: 82, 91, 76, 88. Ascending: 76, 82, 88, 91. Descending: 91, 88, 82, 76.

### Common Mistakes
- Using default lexicographic sort for numbers.
- Sorting the original when it must be preserved.
- Reversing a copy before it has been sorted.

### Activities
1. Sort the canonical scores ascending.
2. Create a descending copy.
3. Explain why the original array remains unchanged.

### Accessibility Practice
Print each sequence with a label so screen-reader users can distinguish them. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can sort numeric values with a comparator.
- [ ] I can reverse a sequence.
- [ ] I can preserve the original array.

---

---

## Lesson 4.3: Tuples and readonly data

### Reading References
- Python source counterpart: Unit 4 lesson 4.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Represent fixed coordinates with a TypeScript readonly tuple.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
TypeScript supports tuple types for fixed-length sequences with known positions. `readonly` prevents element reassignment during type checking; it does not create a runtime security boundary.

### Worked Example
```typescript
const coordinates: readonly [number, number] = [3, 4];
const [x, y] = coordinates;
console.log(`x: ${x}`);
console.log(`y: ${y}`);
console.log(`Distance: ${Math.hypot(x, y)}`);
```

### Expected Behavior or Output
The output is x 3, y 4, and distance 5.

### Common Mistakes
- Using a general number array when exactly two values are required.
- Assuming readonly adds deep runtime immutability.
- Reversing the semantic order of x and y.

### Activities
1. Declare the canonical coordinate tuple.
2. Destructure x and y into named variables.
3. Compare a tuple type with a general number array.

### Accessibility Practice
Use named variables and labels so tuple positions have clear meaning. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can declare a tuple type.
- [ ] I can use readonly for compile-time protection.
- [ ] I can explain tuple positions.

---

---

## Lesson 4.4: Introducing dictionaries: typed objects and records

### Reading References
- Python source counterpart: Unit 4 lesson 4.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Represent inventory items with interfaces and look up quantities with Map.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An interface describes the shape of an object. A Map stores dynamic key-value pairs and supports keys of different types. These structures serve different purposes.

### Worked Example
```typescript
interface InventoryItem { name: string; quantity: number; unitPrice: number }
const inventory: InventoryItem[] = [
  { name: "Notebook", quantity: 3, unitPrice: 2.5 },
  { name: "Pencil", quantity: 10, unitPrice: 0.5 },
  { name: "Folder", quantity: 4, unitPrice: 1.25 }
];
const quantities = new Map<string, number>(inventory.map(item => [item.name, item.quantity]));
console.log(quantities.get("Notebook"));
console.log(quantities.has("Pencil"));
```

### Expected Behavior or Output
The Notebook quantity is 3 and the Map contains Pencil.

### Common Mistakes
- Using a plain object when Map key semantics are needed.
- Using Map bracket notation instead of get and set.
- Forgetting to define a type for structured records.

### Activities
1. Create the three canonical inventory items.
2. Create a Map from item names to quantities.
3. Calculate the total inventory value of $17.50.

### Accessibility Practice
Print each inventory item as a labeled record rather than a visual table only. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can describe an object with an interface.
- [ ] I can create and query a Map.
- [ ] I can distinguish record types from dynamic key-value collections.

---

---
### TypeScript type-system extension

Interfaces describe object shapes; generic types let a function or collection preserve the type of the values it handles. A discriminated union represents a value that can be one of several known states.

```typescript
type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: string };

function first<T>(values: readonly T[]): T | undefined {
  return values[0];
}

function describeResult<T>(result: Result<T>): string {
  if (result.ok) return `Success: ${String(result.value)}`;
  return `Failure: ${result.error}`;
}

console.log(first<number>([82, 91, 76, 88]));
console.log(describeResult<number>({ ok: false, error: "No score" }));
```

The `ok` property narrows the union to its success or failure shape. Generic `T` preserves the element type rather than discarding it as `any`.


## Lesson 4.5: Looping through objects and Maps

### Reading References
- Python source counterpart: Unit 4 lesson 4.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Traverse object properties and Map entries to create readable reports.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
`Object.entries` returns key-value pairs from an object. Map is directly iterable and yields typed key-value pairs. Use explicit types to preserve useful information during traversal.

### Worked Example
```typescript
const student = { name: "Avery", age: 16, favoriteSubject: "Computer Science" };
for (const [key, value] of Object.entries(student)) {
  console.log(`${key}: ${value}`);
}
const counts = new Map<string, number>([["Notebook", 3], ["Pencil", 10]]);
for (const [item, quantity] of counts) {
  console.log(`${item}: ${quantity}`);
}
```

### Expected Behavior or Output
The program prints each student property and then the two inventory quantities.

### Common Mistakes
- Confusing object iteration with Map iteration.
- Assuming Object.entries preserves a domain-specific order contract.
- Using values without labeling their keys.

### Activities
1. Print the Avery profile one property per line.
2. Iterate over the inventory Map.
3. Compare Object.keys, Object.values, and Object.entries.

### Accessibility Practice
Keep one key-value pair per output line. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can traverse object entries.
- [ ] I can traverse Map entries.
- [ ] I can produce a sequential text report.

---
<<<<<<< HEAD
