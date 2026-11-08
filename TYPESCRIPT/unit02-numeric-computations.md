# Unit 2: Numeric Computations

## Overview

Translate requirements into programs, expressions, input, conversions, and mathematical calculations. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

---

=======
>>>>>>> 2067a20 (curriculum clearning and updates)

## Overview

Translate requirements into programs, expressions, input, conversions, and mathematical calculations. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 2.1: The software development process

### Reading References
- Python source counterpart: Unit 2 lesson 2.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Apply the design, implementation, and testing cycle to the canonical tip calculator.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A problem statement becomes requirements, an algorithm, an implementation, and tests. The shared calculator uses a $24.50 bill and a 15% tip rate.

### Worked Example
```typescript
const bill = 24.50;
const tipRate = 0.15;
const tip = bill * tipRate;
const total = bill + tip;
console.log(`Tip: $${tip.toFixed(2)}`);
console.log(`Total: $${total.toFixed(2)}`);
```

### Expected Behavior or Output
<<<<<<< HEAD
The tip is $3.68 and the total is $28.18 when rounded using JavaScript number formatting.
=======
The tip is $3.67 and the total is $28.18 when rounded with `toFixed(2)`. The exact product 3.675 is stored as 3.67499999999999982, so `toFixed(2)` rounds the tip down.
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
- Coding before identifying inputs and expected results.
- Confusing the tip amount with the final total.
- Assuming binary floating-point represents every decimal exactly.

### Activities
1. Write requirements for the tip calculator.
2. Predict the result before running the example.
3. Test a zero tip rate and a different bill amount.

### Accessibility Practice
State the input values and output labels explicitly. Explain rounding rather than relying on visual currency formatting. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can describe the development cycle.
- [ ] I can translate requirements into an algorithm.
- [ ] I can compare expected and actual results.
<<<<<<< HEAD

---

---

## Lesson 2.2: Expressions and assignment

### Reading References
- Python source counterpart: Unit 2 lesson 2.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Evaluate arithmetic expressions and update a score using typed variables.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An expression produces a value. Assignment stores a value in a variable. Parentheses make grouping explicit and TypeScript checks the declared value types.

### Worked Example
```typescript
let score: number = 10;
score = score + 5;
const subtotal = 2 + 3 * 4;
const grouped = (2 + 3) * 4;
console.log(score, subtotal, grouped);
```

### Expected Behavior or Output
The output values are 15, 14, and 20.

### Common Mistakes
- Assuming multiplication and addition have equal precedence.
- Using const for a variable that must be reassigned.
- Confusing equality comparison with assignment.

### Activities
1. Predict the value of expressions with and without parentheses.
2. Update a score by adding 5.
3. Use a comparison expression and identify its boolean result.

### Accessibility Practice
Keep each expression on a separate line and narrate operator order. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can evaluate arithmetic expressions.
- [ ] I can explain assignment and reassignment.
- [ ] I can use parentheses to make precedence clear.

---

---

## Lesson 2.3: Input and output in Node.js

### Reading References
- Python source counterpart: Unit 2 lesson 2.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Prompt for a name and two numbers using asynchronous terminal input.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Node.js readline/promises returns Promises. `await` pauses the async function until the user responds. Input arrives as text and must be converted and validated.

### Worked Example
```typescript
import { createInterface } from "node:readline/promises";
import { stdin, stdout } from "node:process";

async function main(): Promise<void> {
  const rl = createInterface({ input: stdin, output: stdout });
  try {
    const name = await rl.question("Enter your name: ");
    const first = Number(await rl.question("First number: "));
    const second = Number(await rl.question("Second number: "));
    if (!Number.isFinite(first) || !Number.isFinite(second)) {
      console.log("Enter valid numbers.");
      return;
    }
    console.log(`Hello, ${name}!`);
    console.log(`Sum: ${first + second}`);
  } finally {
    rl.close();
  }
}
void main();
```

### Expected Behavior or Output
For name Avery and numbers 12 and 8, output is `Hello, Avery!` and `Sum: 20`. The interface closes on both success and early return.

### Common Mistakes
- Forgetting that terminal input is text.
- Using a number without checking whether conversion succeeded.
- Leaving the readline interface open so the process does not exit.

### Activities
1. Prompt for a name and two numbers.
2. Try blank and nonnumeric input.
3. Explain why await and finally are used.

### Accessibility Practice
Use clear prompts with trailing spaces and one question at a time. Announce validation errors in plain text. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can collect terminal input asynchronously.
- [ ] I can convert and validate numeric text.
- [ ] I can close the input interface reliably.

---

---

## Lesson 2.4: Computing with numbers and type conversions

### Reading References
- Python source counterpart: Unit 2 lesson 2.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Convert numeric text explicitly and calculate age, measurement, and validation results.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
TypeScript's static types do not change runtime parsing. `Number` converts text; `Number.isFinite` rejects NaN and infinities. The source type must reflect values after validation.

### Worked Example
```typescript
const ageText: string = "16";
const age = Number(ageText);
const heightM = 1.72;
const heightCm = heightM * 100;
console.log(`Age next year: ${age + 1}`);
console.log(`Height: ${heightCm} cm`);
console.log(Number.isFinite(age));
console.log(Number.isFinite(Number("sixteen")));
```

### Expected Behavior or Output
Output: age next year 17, height 172 cm, true, false.

### Common Mistakes
- Assuming a type annotation validates text received at runtime.
- Treating Number("") as invalid even though it becomes zero.
- Failing to check NaN after conversion.

### Activities
1. Convert the string 16 to a number.
2. Compare Number("16"), Number(""), and Number("sixteen").
3. Validate a user-entered age within a reasonable range.

### Accessibility Practice
Explain the difference between compile-time type checking and runtime input validation. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can convert numeric strings.
- [ ] I can detect invalid numeric conversion.
- [ ] I can explain why external values need runtime checks.

---

---

## Lesson 2.5: Using the Math object

### Reading References
- Python source counterpart: Unit 2 lesson 2.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Use Math constants and functions for circle measurements and distance.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
JavaScript and TypeScript expose mathematical functions through the built-in Math object. `Math.PI`, `Math.hypot`, `Math.ceil`, and `Math.floor` avoid unnecessary imports.

### Worked Example
```typescript
const radius = 5;
const area = Math.PI * radius ** 2;
const circumference = 2 * Math.PI * radius;
const distance = Math.hypot(3, 4);
console.log(area.toFixed(2));
console.log(circumference.toFixed(2));
console.log(distance.toFixed(2));
```

### Expected Behavior or Output
Area 78.54, circumference 31.42, and distance 5.00.

### Common Mistakes
- Using degrees where a function expects radians.
- Using the wrong exponent or formula for area.
- Rounding intermediate values instead of formatting final output.

### Activities
1. Calculate a circle's area and circumference for radius 5.
2. Calculate distance from coordinates (3, 4).
3. Compare Math.ceil and Math.floor for 4.2.

### Accessibility Practice
Print each result with a descriptive label and units. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can use Math constants and functions.
- [ ] I can calculate circle measurements.
- [ ] I can calculate distance from the origin.

---
