# Unit 6: Functions

## Overview

Define typed functions, arguments, return values, and collection-processing functions. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.
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

---

---

## Lesson 5.2: The while loop in action

### Reading References
- Python source counterpart: Unit 5 lesson 5.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Repeat a prompt until a sentinel command is entered.
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

## Overview

Define typed functions, arguments, return values, and collection-processing functions. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 6.1: Defining functions

### Reading References
- Python source counterpart: Unit 6 lesson 6.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Define a typed function that calculates a tip and total.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A function packages reusable behavior. Parameter types describe accepted inputs and a return type describes the result. A function can return a value without printing it.

### Worked Example
```typescript
function calculateTip(bill: number, rate: number): number {
  return bill * rate;
}
console.log(calculateTip(24.5, 0.15).toFixed(2));
```

### Expected Behavior or Output
The tip amount is 3.68 when formatted to two decimal places.

### Common Mistakes
- Omitting a return on one branch of a typed function.
- Printing instead of returning a result needed by the caller.
- Using overly broad any types.

### Activities
1. Write a function that returns a tip amount.
2. Add a function that returns bill plus tip.
3. Test the canonical bill and rate.

### Accessibility Practice
Keep the signature on one line and read parameter and return types explicitly. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can declare a function.
- [ ] I can type parameters and return values.
- [ ] I can distinguish returning from printing.

---

---

## Lesson 6.2: Passing arguments

### Reading References
- Python source counterpart: Unit 6 lesson 6.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Use positional, optional, and default parameters in typed function calls.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
TypeScript supports positional arguments and default values. It does not have Python-style named keyword arguments; use an options object when callers need named configuration.

### Worked Example
```typescript
interface TipOptions { rate?: number; includeTotal?: boolean }
function describeTip(bill: number, options: TipOptions = {}): string {
  const rate = options.rate ?? 0.15;
  const tip = bill * rate;
  return options.includeTotal ? `Tip ${tip.toFixed(2)}, total ${(bill + tip).toFixed(2)}` : `Tip ${tip.toFixed(2)}`;
}
console.log(describeTip(24.5, { rate: 0.2, includeTotal: true }));
```

### Expected Behavior or Output
The output is `Tip 4.90, total 29.40`.

### Common Mistakes
- Assuming TypeScript supports named keyword arguments.
- Using || when zero is a meaningful option value.
- Making an options field required when a default is intended.

### Activities
1. Call a function with positional arguments.
2. Add a default tip rate.
3. Use an options object to request the total.

### Accessibility Practice
Read option names and values explicitly. Avoid deeply nested option objects in beginner examples. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can pass positional arguments.
- [ ] I can use default and optional parameters.
- [ ] I can model named options with an interface.

---

---

## Lesson 6.3: Return values

### Reading References
- Python source counterpart: Unit 6 lesson 6.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Return computed values and handle empty collections explicitly.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A return value is data supplied to the caller. A return type can include null to represent an absent result; strictNullChecks requires the caller to handle that possibility.

### Worked Example
```typescript
function average(values: number[]): number | null {
  if (values.length === 0) return null;
  return values.reduce((sum, value) => sum + value, 0) / values.length;
}
console.log(average([82, 91, 76, 88]));
console.log(average([]));
```

### Expected Behavior or Output
The averages are 84.25 and null.

### Common Mistakes
- Returning undefined accidentally on an empty path.
- Ignoring a nullable return value.
- Confusing a side effect with a computed result.

### Activities
1. Calculate the canonical score average.
2. Call the function with an empty array.
3. Use a null check before formatting the result.

### Accessibility Practice
Explain every possible return value before showing the caller. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can return a computed value.
- [ ] I can express an absent result with null.
- [ ] I can handle a union return type.

---

---

## Lesson 6.4: Functions with arrays and objects

### Reading References
- Python source counterpart: Unit 6 lesson 6.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Pass typed arrays and inventory records to reusable processing functions.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Arrays and objects are reference values. A function can mutate caller-visible data. Use readonly parameters or copy inputs when mutation is not part of the contract.

### Worked Example
```typescript
interface Item { name: string; quantity: number; unitPrice: number }
function inventoryValue(items: readonly Item[]): number {
  return items.reduce((sum, item) => sum + item.quantity * item.unitPrice, 0);
}
const items: Item[] = [
  { name: "Notebook", quantity: 3, unitPrice: 2.5 },
  { name: "Pencil", quantity: 10, unitPrice: 0.5 },
  { name: "Folder", quantity: 4, unitPrice: 1.25 }
];
console.log(inventoryValue(items).toFixed(2));
```

### Expected Behavior or Output
The inventory value is 17.50.

### Common Mistakes
- Mutating an input collection unexpectedly.
- Using an object shape inconsistent with the interface.
- Forgetting that readonly is a compile-time constraint, not deep freezing.

### Activities
1. Write a function that totals inventory value.
2. Write a function that returns scores above 80.
3. Explain whether each function mutates its input.

### Accessibility Practice
Use named fields and one output line per record. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can type an object interface.
- [ ] I can accept readonly arrays.
- [ ] I can write a collection-processing function.

---

---

## Lesson 6.5: Arbitrary numbers of arguments

### Reading References
- Python source counterpart: Unit 6 lesson 6.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Use typed rest parameters and options objects to handle variable inputs.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A rest parameter gathers remaining positional arguments into an array. TypeScript requires the rest parameter's element type. An options object is a clear alternative to Python-style keyword arguments.

### Worked Example
```typescript
function sum(...values: number[]): number {
  return values.reduce((total, value) => total + value, 0);
}
console.log(sum(10, 20, 30));
console.log(sum(82, 91, 76, 88));
```

### Expected Behavior or Output
The results are 60 and 337.

### Common Mistakes
- Treating the rest parameter as a single number.
- Placing parameters after a rest parameter.
- Using any[] instead of a meaningful element type.

### Activities
1. Call sum with three values.
2. Call sum with the canonical scores.
3. Compare a rest parameter with an options object.

### Accessibility Practice
Describe the collected values as an ordered list. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can declare a typed rest parameter.
- [ ] I can pass a variable number of values.
- [ ] I can explain the difference between rest parameters and options objects.

---
