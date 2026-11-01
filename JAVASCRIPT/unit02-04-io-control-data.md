# Unit 2: Numeric Computations and Input/Output

**Runtime baseline:** Node.js 26.x. Examples use built-in ECMAScript and Node.js APIs; no third-party package is required for these lessons.

## Overview
This unit follows the same design, expression, input/output, numeric-conversion, and mathematics sequence as the Python course. Use the shared bill of $24.50 and tip rate of 0.15, the student profile Avery (age 16, height 1.72 m), and the coordinates (3, 4). JavaScript is dynamically typed; input from a terminal arrives as text and must be converted and validated before arithmetic.

## Lesson 2.1: The Software Development Process

### Reading References
- Python source counterpart: Unit 2, Lesson 2.1.
- MDN: JavaScript Guide, Grammar and Types.

### Learning Objectives
- Separate problem analysis, design, implementation, and testing.
- Identify inputs, outputs, assumptions, and boundary cases before coding.
- Write language-neutral pseudocode before JavaScript.

### Concept Explanation
Use the same three-phase cycle for every language: **design**, **implement**, and **test/debug**. For a tip calculator, inputs are bill amount and tip rate; outputs are tip amount and total. State assumptions explicitly: the bill is nonnegative, the rate is a decimal fraction, and money is displayed to two decimal places. Pseudocode should describe the calculation without depending on JavaScript syntax.

### Worked Example
Pseudocode:
```text
GET bill amount
GET tip rate
CALCULATE tip = bill amount * tip rate
CALCULATE total = bill amount + tip
DISPLAY tip and total to two decimal places
```

JavaScript implementation using the canonical values:
```javascript
const bill = 24.50;
const tipRate = 0.15;
const tip = bill * tipRate;
const total = bill + tip;

console.log(`Tip: $${tip.toFixed(2)}`);
console.log(`Total: $${total.toFixed(2)}`);
```

Expected output:
```text
Tip: $3.68
Total: $28.18
```

### Common Mistakes
- Coding before deciding what the program should accept and display.
- Treating 15 as equivalent to 0.15 for a percentage rate.
- Forgetting to test zero, negative, and unusually large inputs.
- Rounding intermediate values when only the displayed result needs formatting.

### Activities
1. Write input/output tables for the tip calculator before coding.
2. Add a test case for a $0.00 bill and explain its expected result.
3. Change the tip rate to 0.20 and predict the output before running the program.
4. Describe one invalid input and the validation rule that should reject it.

### Accessibility Practice
Read the pseudocode and output in order. Use explicit labels for each displayed amount; do not rely on alignment, color, or visual placement to communicate which value is the tip and which is the total.

### Skills Checklist
- [ ] I can identify a program's inputs, outputs, assumptions, and edge cases.
- [ ] I can write pseudocode independently of JavaScript syntax.
- [ ] I can distinguish design, implementation, and testing.
- [ ] I can explain why expected results should be predicted before execution.

---

## Lesson 2.2: Expressions and Assignment

### Reading References
- Python source counterpart: Unit 2, Lesson 2.2.
- MDN: Expressions and operators.

### Learning Objectives
- Evaluate arithmetic expressions using precedence and parentheses.
- Assign and update variables with clear, predictable statements.
- Explain the difference between `=`, `===`, and arithmetic operators.

### Concept Explanation
An expression produces a value. An assignment stores a value in a variable. JavaScript evaluates multiplication and division before addition and subtraction; parentheses make intended grouping explicit. Use `===` for strict equality in beginner examples so that JavaScript does not silently coerce unlike types during comparison.

### Worked Example
```javascript
let score = 10;
score = score + 5;
const subtotal = 3 * 4 + 2;
const grouped = 3 * (4 + 2);

console.log(`Score: ${score}`);
console.log(`Subtotal: ${subtotal}`);
console.log(`Grouped: ${grouped}`);
console.log(`Is score 15? ${score === 15}`);
```

Expected output:
```text
Score: 15
Subtotal: 14
Grouped: 18
Is score 15? true
```

### Common Mistakes
- Using `=` when a comparison with `===` is intended.
- Forgetting that `const` prevents reassignment of the binding.
- Assuming arithmetic with a string will always behave like arithmetic with a number.
- Omitting parentheses when they would make a multi-step expression easier to audit.

### Activities
1. Predict and then verify `8 + 4 * 2` and `(8 + 4) * 2`.
2. Update a score from 82 by adding 9, then print the new value.
3. Create a bill expression with a 15% tip using the canonical $24.50 bill.
4. Explain why `"15" === 15` evaluates to false.

### Accessibility Practice
When reading code aloud, identify parentheses, operators, and assignment separately. Keep one calculation per line when that makes the sequence easier to navigate.

### Skills Checklist
- [ ] I can evaluate expressions using operator precedence.
- [ ] I can use parentheses to control grouping.
- [ ] I can update a variable with `let`.
- [ ] I can explain assignment versus strict equality.

---

## Lesson 2.3: Input and Output Revisited

### Reading References
- Python source counterpart: Unit 2, Lesson 2.3.
- Node.js documentation: readline.

### Learning Objectives
- Read terminal input with Node.js `readline/promises`.
- Explain that terminal input is returned as a string.
- Display a greeting and the sum of two validated numeric inputs.

### Concept Explanation
Unlike Python's built-in `input()`, Node.js uses an input API. The `readline/promises` module provides an asynchronous `question()` method. It returns text, so numeric input must be converted and checked. Always close the interface so the process can exit cleanly.

### Worked Example
Save as `sum-input.js` and run with `node sum-input.js`:

```javascript
const readline = require("node:readline/promises");
const { stdin, stdout } = require("node:process");

async function main() {
  const rl = readline.createInterface({ input: stdin, output: stdout });
  try {
    const name = await rl.question("What is your name? ");
    const firstText = await rl.question("Enter the first number: ");
    const secondText = await rl.question("Enter the second number: ");
    const first = Number(firstText);
    const second = Number(secondText);

    if (firstText.trim() === "" || secondText.trim() === ""
        || !Number.isFinite(first) || !Number.isFinite(second)) {
      console.log("Error: enter two valid numbers.");
      return;
    }

    console.log(`Hello, ${name}!`);
    console.log(`Sum: ${first + second}`);
  } finally {
    rl.close();
  }
}

main();
```

Example interaction:
```text
What is your name? Avery
Enter the first number: 12
Enter the second number: 8
Hello, Avery!
Sum: 20
```

### Common Mistakes
- Adding two input strings and getting concatenation instead of numeric addition.
- Treating `Number("")` as invalid even though it evaluates to zero; validate blank text explicitly.
- Forgetting to await `question()`.
- Leaving the readline interface open.

### Activities
1. Run the example with the name Avery and numbers 12 and 8.
2. Enter a blank value and confirm that the validation message appears.
3. Enter a decimal and a negative number; explain why both are valid numeric values.
4. Change the program to ask for the canonical age 16 and print the year of birth only after asking for a reference year.

### Accessibility Practice
Use prompts that state exactly what input is expected. Announce the full error message and re-prompt when extending this example. Keep the interaction linear and keyboard-only.

### Skills Checklist
- [ ] I can create a Node.js readline interface.
- [ ] I can read terminal input asynchronously.
- [ ] I can convert and validate numeric text.
- [ ] I can close the interface in a `finally` block.

---

## Lesson 2.4: Computing with Numbers and Type Conversions

### Reading References
- Python source counterpart: Unit 2, Lesson 2.4.
- MDN: Number, Number.isFinite, and Number.isInteger.

### Learning Objectives
- Distinguish JavaScript numbers from numeric strings.
- Convert text using `Number()` and parse integer text when appropriate.
- Detect invalid numeric values, including `NaN`.

### Concept Explanation
JavaScript has one ordinary `Number` type for integers and floating-point values. It uses IEEE 754 double-precision floating-point arithmetic. `Number("16")` returns 16; `Number("sixteen")` returns `NaN`. `parseInt()` parses an integer prefix, so it should not be used as a substitute for strict validation. Use `Number.isFinite()` to reject `NaN` and infinities.

### Worked Example
```javascript
const ageText = "16";
const heightText = "1.72";
const age = Number(ageText);
const height = Number(heightText);

console.log(`Age next year: ${age + 1}`);
console.log(`Height in centimeters: ${(height * 100).toFixed(0)}`);
console.log(`Is age valid? ${Number.isInteger(age) && age >= 0}`);
console.log(`Is 'sixteen' valid? ${Number.isFinite(Number("sixteen"))}`);
```

Expected output:
```text
Age next year: 17
Height in centimeters: 172
Is age valid? true
Is 'sixteen' valid? false
```

### Common Mistakes
- Assuming JavaScript separates integers and floats into different primitive types.
- Forgetting that `typeof NaN` is `"number"`.
- Using `parseInt("12abc")` and accepting the partial result 12 without checking the entire input.
- Comparing floating-point calculations for exact equality when a tolerance is needed.

### Activities
1. Convert the canonical age text `"16"` and height text `"1.72"` to numbers.
2. Convert `"abc"` and `""`; explain why blank input needs separate validation.
3. Calculate the bill total from $24.50 and a 0.15 tip rate.
4. Test whether 3.5 is an integer and whether `Infinity` is finite.

### Accessibility Practice
Use textual labels that name the value and its unit. State why a conversion failed rather than only printing `NaN`.

### Skills Checklist
- [ ] I can convert numeric strings with `Number()`.
- [ ] I can detect invalid numeric values with `Number.isFinite()`.
- [ ] I can distinguish integers from non-integer numbers.
- [ ] I can explain JavaScript's single ordinary Number type.

---

## Lesson 2.5: Using the Math Object

### Reading References
- Python source counterpart: Unit 2, Lesson 2.5.
- MDN: Math.

### Learning Objectives
- Use `Math.PI`, `Math.sqrt()`, `Math.ceil()`, and `Math.floor()`.
- Calculate circle area and circumference.
- Calculate distance from the origin using the canonical coordinates (3, 4).

### Concept Explanation
JavaScript's built-in `Math` object provides mathematical constants and functions. It is used directly; it is not imported. `Math.PI` is the value of pi, `Math.sqrt()` calculates a square root, `Math.ceil()` rounds upward, and `Math.floor()` rounds downward.

### Worked Example
```javascript
const radius = 5;
const area = Math.PI * radius ** 2;
const circumference = 2 * Math.PI * radius;

const x = 3;
const y = 4;
const distance = Math.sqrt(x ** 2 + y ** 2);

console.log(`Area: ${area.toFixed(2)}`);
console.log(`Circumference: ${circumference.toFixed(2)}`);
console.log(`Distance from origin: ${distance.toFixed(2)}`);
console.log(`Ceiling of 4.2: ${Math.ceil(4.2)}`);
console.log(`Floor of 4.8: ${Math.floor(4.8)}`);
```

Expected output:
```text
Area: 78.54
Circumference: 31.42
Distance from origin: 5.00
Ceiling of 4.2: 5
Floor of 4.8: 4
```

### Common Mistakes
- Writing `Math.pi` instead of the case-sensitive `Math.PI`.
- Calling `Math.sqrt` without parentheses.
- Confusing `Math.round()` with ceiling or floor.
- Forgetting that `toFixed()` returns a string for display.

### Activities
1. Calculate the area and circumference of a circle with radius 5.
2. Calculate the distance from (3, 4) to the origin.
3. Predict the results of `Math.ceil(2.01)` and `Math.floor(2.99)`.
4. Change the radius to 2.5 and report both results to two decimal places.

### Accessibility Practice
Read each result with its label. Preserve units in prompts and output. Ensure mathematical notation is also explained in words when students are using a screen reader or braille display.

### Skills Checklist
- [ ] I can use `Math.PI` and `Math.sqrt()`.
- [ ] I can calculate circle area and circumference.
- [ ] I can calculate distance from the origin.
- [ ] I can distinguish ceiling, floor, and rounding.


### Lesson 4.3: Tuples — Immutable Sequences in JavaScript

JavaScript has no built-in tuple type with Python's tuple semantics. Use a frozen array for a simple fixed sequence, while explaining that `Object.freeze()` is shallow and does not create a general-purpose static tuple type.

```javascript
const coordinates = Object.freeze([3, 4]);
console.log(`x: ${coordinates[0]}`);
console.log(`y: ${coordinates[1]}`);
console.log(`Distance: ${Math.hypot(coordinates[0], coordinates[1])}`);
```

Expected output:
```text
x: 3
y: 4
Distance: 5
```

**Common Mistakes:** assuming `const` freezes array contents; assuming `Object.freeze()` is deep; confusing fixed sequence intent with a language-enforced tuple type.

**Activities:** create a frozen coordinate pair; read each coordinate; attempt reassignment in strict mode and describe the result; compare the frozen pair with a mutable score array.

**Accessibility Practice:** identify each position by its semantic name (x or y), not only by index.

**Skills Checklist**
- [ ] I can explain why JavaScript has no direct Python tuple equivalent.
- [ ] I can use a frozen array for a fixed sequence.
- [ ] I can distinguish `const` binding from object immutability.

### Lesson 4.4: Introducing Dictionaries — JavaScript Objects and Map

A plain object is appropriate for a record with named fields; `Map` is appropriate for a dynamic key-value collection. Use the canonical inventory records and preserve their values.

```javascript
const inventory = [
  { name: "Notebook", quantity: 3, unitPrice: 2.50 },
  { name: "Pencil", quantity: 10, unitPrice: 0.50 },
  { name: "Folder", quantity: 4, unitPrice: 1.25 }
];

const quantities = new Map(inventory.map(item => [item.name, item.quantity]));
console.log(quantities.get("Notebook"));
console.log(quantities.has("Pencil"));
```

Expected output:
```text
3
true
```

**Common Mistakes:** confusing object properties with Map entries; using bracket notation on a Map; assuming a missing key returns zero rather than `undefined`.

**Activities:** build a record for each inventory item; create a Map from item names to quantities; update the Pencil quantity; calculate total inventory value.

**Accessibility Practice:** print item names, quantities, and prices as labeled text.

**Skills Checklist**
- [ ] I can explain when to use an object and when to use Map.
- [ ] I can add, retrieve, update, and test Map entries.
- [ ] I can represent the canonical inventory records.

### Lesson 4.5: Looping Through Objects and Maps

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

Expected output:
```text
name: Avery
age: 16
heightM: 1.72
favoriteSubject: Computer Science
```

**Common Mistakes:** iterating over object keys when key-value pairs are needed; modifying a collection during traversal; assuming Map and object iteration APIs are interchangeable.

**Activities:** print every Avery profile field; iterate over inventory Map entries; produce a total count of inventory units; compare `Object.keys()`, `Object.values()`, and `Object.entries()`.

**Accessibility Practice:** provide one key-value pair per line and announce when iteration begins and ends.

**Skills Checklist**
- [ ] I can traverse object keys, values, and entries.
- [ ] I can traverse Map entries.
- [ ] I can produce readable sequential reports from structured data.

