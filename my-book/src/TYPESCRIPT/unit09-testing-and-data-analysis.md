# Unit 9: Testing and Data Analysis

## Overview

Test functions and classes, generate random values, analyze text, and parse CSV. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

---

## Lesson 9.1: Testing a function

### Reading References
- Python source counterpart: Unit 9 lesson 9.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Write built-in Node.js tests for arithmetic and grade classification functions.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Unit tests verify a function's contract with known inputs and expected outputs. Node's built-in node:test and node:assert/strict avoid a third-party test framework for introductory work.

### Worked Example
```typescript
import test from "node:test";
import assert from "node:assert/strict";
function add(a: number, b: number): number { return a + b; }
function getGrade(score: number): string { return score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : score >= 60 ? "D" : "F"; }
test("add returns the sum", () => assert.equal(add(5, 3), 8));
test("82 receives grade B", () => assert.equal(getGrade(82), "B"));
```

### Expected Behavior or Output
The test runner reports two passing tests and no failures.

### Common Mistakes
- Testing only one ordinary value.
- Using an incorrect expected value copied from the implementation.
- Failing to run tests after changing a function.

### Activities
1. Test add with positive, negative, and zero values.
2. Test every grade threshold and its lower neighbor.
3. Run tests with node --test after compiling the TypeScript test file.

### Accessibility Practice
Use descriptive test names that read as complete sentences. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can write a unit test.
- [ ] I can assert an expected result.
- [ ] I can test normal and boundary inputs.

---

---

## Lesson 9.2: Testing a class

### Reading References
- Python source counterpart: Unit 9 lesson 9.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Test class construction, state changes, and invalid operations.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A class test checks observable behavior: constructor values, method results, state updates, and rejected invalid states. Keep tests independent and deterministic.

### Worked Example
```typescript
import test from "node:test";
import assert from "node:assert/strict";
class StockItem {
  constructor(public name: string, public quantity: number) {}
  setQuantity(value: number): void { if (value < 0) throw new RangeError("Invalid quantity"); this.quantity = value; }
}
test("quantity can be updated", () => {
  const item = new StockItem("Pencil", 10);
  item.setQuantity(12);
  assert.equal(item.quantity, 12);
});
```

### Expected Behavior or Output
The test passes when the quantity changes from 10 to 12.

### Common Mistakes
- Sharing mutable state between tests.
- Testing private implementation details rather than behavior.
- Failing to test invalid state changes.

### Activities
1. Test a valid quantity update.
2. Assert that a negative quantity throws RangeError.
3. Create a fresh instance in each test.

### Accessibility Practice
Keep test names and failure output specific to the state being checked. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can test class behavior.
- [ ] I can test state changes.
- [ ] I can assert that invalid operations throw.

---

---

## Lesson 9.3: Introduction to random numbers

### Reading References
- Python source counterpart: Unit 9 lesson 9.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Generate bounded integers, decimals, and selections with Math.random.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Math.random returns a pseudorandom number in the range zero inclusive to one exclusive. Scale and floor it to produce a bounded integer; do not use it for security tokens.

### Worked Example
```typescript
const integer = Math.floor(Math.random() * 10) + 1;
const decimal = Math.random();
const choices = ["red", "blue", "green"];
const choice = choices[Math.floor(Math.random() * choices.length)];
console.log(integer >= 1 && integer <= 10);
console.log(decimal >= 0 && decimal < 1);
console.log(choices.includes(choice));
```

### Expected Behavior or Output
All three checks print true; sampled values can differ on each run.

### Common Mistakes
- Using Math.round and creating uneven endpoint probabilities.
- Forgetting that the upper bound is exclusive.
- Using Math.random for passwords or cryptographic secrets.

### Activities
1. Generate an integer from 1 to 10.
2. Generate a decimal in [0,1).
3. Choose one item from a typed array.

### Accessibility Practice
Report range checks as text; explain that the actual sample changes between runs. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can describe Math.random's range.
- [ ] I can generate a bounded integer.
- [ ] I can select a random array element.

---

---

## Lesson 9.4: Analyzing text data

### Reading References
- Python source counterpart: Unit 9 lesson 9.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Count words in the canonical text using normalization and a typed Map.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Text analysis requires explicit normalization and tokenization rules. A Map stores each token and its frequency. The regular expression below splits on non-letter characters.

### Worked Example
```typescript
const text = "A student studies programming. Programming develops problem-solving skills.";
const words = text.toLowerCase().match(/[a-z]+/g) ?? [];
const counts = new Map<string, number>();
for (const word of words) counts.set(word, (counts.get(word) ?? 0) + 1);
console.log(`Tokens: ${words.length}`);
console.log(`Programming: ${counts.get("programming")}`);
```

### Expected Behavior or Output
The sample produces 10 alphabetic tokens under this tokenization rule; programming appears twice.

### Common Mistakes
- Assuming punctuation and hyphens are words.
- Using a plain object without considering inherited property names.
- Failing to define how case and punctuation are normalized.

### Activities
1. Count all tokens in the canonical text.
2. Report the frequency of programming.
3. Compare token counts with a rule that treats problem-solving as one token.

### Accessibility Practice
State the tokenization rule before reporting counts. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can normalize text.
- [ ] I can count tokens with a Map.
- [ ] I can explain how tokenization affects results.

---

---

## Lesson 9.5: Working with CSV data

### Reading References
- Python source counterpart: Unit 9 lesson 9.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Read the shared CSV columns using a standards-aware parser.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
CSV supports quoted fields, commas inside quotes, and escaped quotation marks. Use a maintained parser rather than splitting lines on commas. Parsed records still need validation.

### Worked Example
```typescript
import { parse } from "csv-parse/sync";
const csv = "student_id,first_name,last_name,score,active\n1,Avery,Stone,91,true\n2,Jordan,Lee,82,false";
const records = parse(csv, { columns: true, skip_empty_lines: true }) as Array<Record<string, string>>;
const average = records.reduce((sum, row) => sum + Number(row.score), 0) / records.length;
console.log(`Records: ${records.length}`);
console.log(`Average: ${average.toFixed(2)}`);
```

### Expected Behavior or Output
The two sample records have scores 91 and 82; the average is 86.50.

### Common Mistakes
- Splitting CSV lines and fields manually.
- Assuming every parsed field is already a number or boolean.
- Ignoring malformed rows and missing columns.

### Activities
1. Parse the shared CSV columns.
2. Calculate the score average for the sample records.
3. Test a quoted name containing a comma.

### Accessibility Practice
Print record count and summary labels rather than a visual-only chart. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can parse CSV with a dedicated parser.
- [ ] I can validate parsed field values.
- [ ] I can calculate a summary from CSV records.

---
