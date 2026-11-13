# Unit 5: User Input and while Loops

## Overview

Build input validation and sentinel-controlled loops. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

---



## Overview

Build input validation and sentinel-controlled loops. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 5.1: How terminal input works

### Reading References
- Python source counterpart: Unit 5 lesson 5.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Collect text from the user and validate it before using it.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The readline/promises interface returns a string for each answer. TypeScript's annotation does not convert or validate that string.

### Worked Example
```typescript
import { createInterface } from "node:readline/promises";
import { stdin, stdout } from "node:process";
async function main(): Promise<void> {
  const rl = createInterface({ input: stdin, output: stdout });
  try {
    const subject = await rl.question("Favorite subject: ");
    if (subject.trim() === "") console.log("A subject is required.");
    else console.log(`Favorite subject: ${subject.trim()}`);
  } finally { rl.close(); }
}
void main();
```

### Expected Behavior or Output
A valid answer prints `Favorite subject: Computer Science`; blank input prints the required-field message.

### Common Mistakes
- Declaring the input as number before parsing it.
- Forgetting to trim whitespace before checking blank input.
- Not closing the readline interface.

### Activities
1. Prompt for a favorite subject.
2. Test blank input and surrounding spaces.
3. Explain why the input variable has type string.

### Accessibility Practice
Use one prompt and one response at a time. State validation failures explicitly. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can collect a string from terminal input.
- [ ] I can reject blank input.
- [ ] I can close the readline interface.

## Overview

Build input validation and sentinel-controlled loops. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 5.1: How terminal input works

### Reading References
- Python source counterpart: Unit 5 lesson 5.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Collect text from the user and validate it before using it.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A while loop repeats while its condition is true. The loop body must eventually change the state used by the condition or exit explicitly.

### Worked Example
```typescript
const commands = ["view", "help", "quit"];
let index = 0;
while (commands[index] !== "quit") {
  console.log(`Command: ${commands[index]}`);
  index += 1;
}
console.log("Session ended.");
```

### Expected Behavior or Output
The program prints view, help, and Session ended. It does not print quit as an ordinary command.

### Common Mistakes
- Forgetting to update the loop index.
- Checking the wrong sentinel value.
- Accessing an array element without accounting for the end of the array.

### Activities
1. Trace each loop iteration on paper.
2. Change the sentinel command and predict termination.
3. Write a menu loop that ends on quit.

### Accessibility Practice
Show the loop condition and state update as separate lines. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can identify a while-loop condition.
- [ ] I can update state to ensure progress.
- [ ] I can use a sentinel to end a loop.

---

---

## Lesson 5.3: Using flags and break to exit loops

### Reading References
- Python source counterpart: Unit 5 lesson 5.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Use a boolean flag and break to stop a search at the first match.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A flag records whether a condition has been met. `break` exits the nearest loop immediately. TypeScript can infer a boolean flag or use an explicit annotation.

### Worked Example
```typescript
const scores = [82, 91, 76, 88];
let found = false;
for (const score of scores) {
  if (score > 90) {
    console.log(`First score above 90: ${score}`);
    found = true;
    break;
  }
}
if (!found) console.log("No score above 90.");
```

### Expected Behavior or Output
The first score above 90 is 91.

### Common Mistakes
- Setting the flag after a break that can never be reached.
- Using break outside a loop or switch.
- Failing to report the no-match case.

### Activities
1. Search for a score above 90.
2. Search for a score above 95 and test the fallback.
3. Compare flag-controlled termination with a return from a function.

### Accessibility Practice
Report the match or no-match result in text, not by color or sound alone. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can use a boolean flag.
- [ ] I can stop a loop with break.
- [ ] I can handle a search with no result.

---

---

## Lesson 5.4: Using continue in loops

### Reading References
- Python source counterpart: Unit 5 lesson 5.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Skip invalid values while continuing to process later entries.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
`continue` skips the rest of the current iteration and begins the next one. It does not terminate the loop. A typed array can still contain invalid values when values come from runtime sources.

### Worked Example
```typescript
const entries: string[] = ["82", "", "91", "not a score", "76", "88"];
let total = 0;
for (const entry of entries) {
  const score = Number(entry);
  if (!Number.isFinite(score)) continue;
  total += score;
}
console.log(total);
```

### Expected Behavior or Output
The valid entries total 337; the blank entry converts to zero with Number, so a stronger version should reject blank strings explicitly before conversion.

### Common Mistakes
- Assuming Number on blank text is an error.
- Using break when later values still need processing.
- Placing the update after continue so it is skipped.

### Activities
1. Add an explicit blank-string check.
2. Skip nonnumeric entries and count accepted values.
3. Compare continue and break with a traced example.

### Accessibility Practice
Print the number of accepted and skipped entries so outcomes are clear. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can use continue to skip an iteration.
- [ ] I can validate before conversion.
- [ ] I can distinguish continue from break.

---

---

## Lesson 5.5: Avoiding infinite loops

### Reading References
- Python source counterpart: Unit 5 lesson 5.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Diagnose loop termination by tracing the control variable and condition.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An infinite loop occurs when its continuation condition never becomes false. TypeScript cannot prove that a loop will terminate; test the control variable and every branch that updates it.

### Worked Example
```typescript
let count = 1;
while (count <= 3) {
  console.log(`Count ${count}`);
  count += 1;
}
console.log("Loop finished.");
```

### Expected Behavior or Output
The output is Count 1, Count 2, Count 3, then Loop finished.

### Common Mistakes
- Forgetting to increment or otherwise update the control variable.
- Using continue before the update statement.
- Using a boundary condition that never becomes false.

### Activities
1. Trace the value of count on each iteration.
2. Identify a continue path that skips an update.
3. Describe a safe way to stop a runaway terminal process.

### Accessibility Practice
Provide a keyboard-only recovery procedure and explicit termination message. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can trace loop state.
- [ ] I can identify non-terminating paths.
- [ ] I can design a loop with a clear exit.

---
