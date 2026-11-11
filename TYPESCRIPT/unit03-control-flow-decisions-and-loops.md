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
