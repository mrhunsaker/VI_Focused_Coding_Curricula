# Unit 2: Numeric Computations

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


# Unit 3: Control Flow — Decisions and Loops

## Overview

Use boolean logic, grade decisions, arrays, iteration, and text operations. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.
=======
>>>>>>> 2067a20 (curriculum clearning and updates)

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


# Unit 3: Control Flow — Decisions and Loops

## Overview

Use boolean logic, grade decisions, arrays, iteration, and text operations. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 3.1: Boolean expressions and if statements

### Reading References
- Python source counterpart: Unit 3 lesson 3.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Combine comparisons and boolean operators to validate a score.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A boolean expression evaluates to true or false. `&&`, `||`, and `!` combine or reverse conditions. TypeScript requires conditions to be boolean in strict code.

### Worked Example
```typescript
const score = 82;
const valid = score >= 0 && score <= 100;
if (valid && score >= 60) {
  console.log("Valid passing score.");
} else {
  console.log("Review score.");
}
```

### Expected Behavior or Output
For score 82, the program prints `Valid passing score.`

### Common Mistakes
- Using & instead of && for logical conjunction.
- Forgetting range validation before classification.
- Assuming a numeric value is itself a boolean.

### Activities
1. Test scores -1, 0, 59, 60, 82, and 100.
2. Combine two conditions with &&.
3. Explain the difference between a comparison and a boolean variable.

### Accessibility Practice
State each condition in words before reading its punctuation. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can write comparisons.
- [ ] I can combine boolean conditions.
- [ ] I can validate a score range.

---

---

## Lesson 3.2: Chained conditionals and grade classification

### Reading References
- Python source counterpart: Unit 3 lesson 3.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Classify scores using the shared A–F thresholds and ordered branches.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An if/else-if/else chain evaluates conditions in order and executes the first matching branch. Order matters when conditions overlap.

### Worked Example
```typescript
function getGrade(score: number): string {
  if (score >= 90) return "A";
  else if (score >= 80) return "B";
  else if (score >= 70) return "C";
  else if (score >= 60) return "D";
  else return "F";
}
for (const score of [82, 91, 76, 88]) {
  console.log(`${score}: ${getGrade(score)}`);
}
```

### Expected Behavior or Output
The classifications are 82:B, 91:A, 76:C, and 88:B.

### Common Mistakes
- Checking a lower threshold before a higher threshold.
- Omitting the boundary score 60 or 90 from tests.
- Accepting scores outside 0–100 without validation.

### Activities
1. Classify the canonical scores.
2. Test every threshold and the value immediately below it.
3. Add a guard for scores outside 0–100.

### Accessibility Practice
Use one result per line and include the original score in the output. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can write a chained conditional.
- [ ] I can classify the canonical scores.
- [ ] I can test boundary conditions.

---

---

## Lesson 3.3: Introduction to arrays

### Reading References
- Python source counterpart: Unit 3 lesson 3.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create, index, and modify the canonical score array.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An array stores an ordered sequence. TypeScript uses `number[]` or `Array<number>` to describe a numeric array. Indexes begin at zero.

### Worked Example
```typescript
const scores: number[] = [82, 91, 76, 88];
console.log(scores.length);
console.log(scores[0]);
scores[2] = 80;
console.log(scores[2]);
```

### Expected Behavior or Output
The array length is 4; the first score is 82; after modification, the third score is 80.

### Common Mistakes
- Using one-based indexes.
- Reading an index that may be out of range without checking.
- Assuming a const array cannot have its elements changed.

### Activities
1. Create the four canonical scores.
2. Read the first and last values safely.
3. Change the third value to 80 and print the array.

### Accessibility Practice
Announce indexes as zero-based and read values with their positions. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can declare a typed array.
- [ ] I can access and update elements.
- [ ] I can explain zero-based indexing.

---

---

## Lesson 3.4: Iterating with for loops

### Reading References
- Python source counterpart: Unit 3 lesson 3.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Iterate through scores and calculate their total and average.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A for...of loop visits each array value. A traditional for loop exposes the index. Choose the form that makes the task easiest to understand.

### Worked Example
```typescript
const scores: number[] = [82, 91, 76, 88];
let total = 0;
for (const score of scores) {
  total += score;
}
console.log(`Total: ${total}`);
console.log(`Average: ${total / scores.length}`);
```

### Expected Behavior or Output
Total 337 and average 84.25.

### Common Mistakes
- Adding array indexes instead of values.
- Dividing by zero for an empty collection.
- Changing the array while iterating without planning the effect.

### Activities
1. Print every score on a separate line.
2. Calculate the canonical total and average.
3. Repeat using an indexed for loop.

### Accessibility Practice
Keep loop output sequential and label totals and averages. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can use for...of to visit values.
- [ ] I can accumulate a total.
- [ ] I can calculate an average safely.

---

---

## Lesson 3.5: Basic string operations

### Reading References
- Python source counterpart: Unit 3 lesson 3.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Normalize names and search text using immutable string methods.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Strings are immutable. Methods such as trim, toUpperCase, and includes return values rather than modifying the original string. Template literals interpolate expressions.

### Worked Example
```typescript
const rawName = "  Avery Student  ";
const name = rawName.trim();
const sentence = "A student studies programming. Programming develops problem-solving skills.";
console.log(name);
console.log(name.toUpperCase());
console.log(sentence.toLowerCase().includes("programming"));
console.log(name.length);
```

### Expected Behavior or Output
Output includes `Avery Student`, uppercase form, true, and character count 13.

### Common Mistakes
- Expecting trim or toUpperCase to mutate the original string.
- Searching without considering case normalization.
- Counting spaces that should have been trimmed.

### Activities
1. Trim the canonical name.
2. Search the canonical text case-insensitively.
3. Count characters before and after trimming.

### Accessibility Practice
Print original and normalized values with clear labels. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can use common string methods.
- [ ] I can explain string immutability.
- [ ] I can normalize and search text.

---


# Unit 4: Data Structures — Arrays, Tuples, and Objects

## Overview

Manipulate arrays and model fixed sequences, records, Maps, and object iteration. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

<<<<<<< HEAD
---

# Unit 4: Data Structures — Arrays, Tuples, and Objects

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


# Unit 5: User Input and while Loops

## Overview

Build input validation and sentinel-controlled loops. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

---

=======
>>>>>>> 2067a20 (curriculum clearning and updates)
