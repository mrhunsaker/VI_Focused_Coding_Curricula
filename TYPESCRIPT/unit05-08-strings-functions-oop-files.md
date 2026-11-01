# Unit 5: User Input and while Loops

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


# Unit 6: Functions

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


# Unit 7: Classes and Object-Oriented Programming

## Overview

Model state and behavior using classes, inheritance, and composition. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 7.1: Why learn about classes?

### Reading References
- Python source counterpart: Unit 7 lesson 7.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Explain classes, instances, encapsulation, and object state with an inventory example.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A class describes the state and behavior of objects. TypeScript classes add static type checking, access modifiers, and optional private fields; types are erased from emitted JavaScript.

### Worked Example
```typescript
class InventoryItem {
  constructor(public name: string, public quantity: number, public unitPrice: number) {}
  value(): number { return this.quantity * this.unitPrice; }
}
const notebook = new InventoryItem("Notebook", 3, 2.5);
console.log(`${notebook.name}: ${notebook.value().toFixed(2)}`);
```

### Expected Behavior or Output
The output is `Notebook: 7.50`.

### Common Mistakes
- Treating a class as only a data container without behavior.
- Confusing a class with an instance.
- Assuming TypeScript access modifiers create runtime security.

### Activities
1. Identify the fields and behavior of an inventory item.
2. Create two instances with different values.
3. Explain what the class and each instance represent.

### Accessibility Practice
Use meaningful instance names and print a labeled summary. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can explain class and instance.
- [ ] I can identify state and behavior.
- [ ] I can create a simple class.

---

## Lesson 7.2: Creating and using a class

### Reading References
- Python source counterpart: Unit 7 lesson 7.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create a Student class and instantiate the canonical learner profile.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A constructor initializes an instance. Parameter properties can declare and initialize fields in one place. Explicit types make the class contract readable.

### Worked Example
```typescript
class Student {
  constructor(public name: string, public age: number, public favoriteSubject: string) {}
  describe(): string { return `${this.name}, age ${this.age}, studies ${this.favoriteSubject}`; }
}
const learner = new Student("Avery", 16, "Computer Science");
console.log(learner.describe());
```

### Expected Behavior or Output
The output is `Avery, age 16, studies Computer Science`.

### Common Mistakes
- Forgetting new when constructing an instance.
- Using a parameter type that conflicts with the property type.
- Writing a method that refers to a variable instead of this.

### Activities
1. Create Avery's Student instance.
2. Create a second student instance.
3. Call describe on both instances.

### Accessibility Practice
Read constructor parameters in order and label each property. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define a constructor.
- [ ] I can instantiate a class.
- [ ] I can call an instance method.

---

## Lesson 7.3: Working with attributes and methods

### Reading References
- Python source counterpart: Unit 7 lesson 7.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Add validation and update behavior to a class.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Methods define operations over an instance's state. Encapsulation keeps validation close to the state it protects. Private fields and access modifiers guide compile-time access.

### Worked Example
```typescript
class StockItem {
  #quantity: number;
  constructor(public name: string, quantity: number) { this.#quantity = quantity; }
  get quantity(): number { return this.#quantity; }
  setQuantity(value: number): void {
    if (!Number.isInteger(value) || value < 0) throw new RangeError("Quantity must be a nonnegative integer.");
    this.#quantity = value;
  }
}
const pencil = new StockItem("Pencil", 10);
pencil.setQuantity(12);
console.log(pencil.quantity);
```

### Expected Behavior or Output
The output is 12. A negative or fractional quantity throws RangeError.

### Common Mistakes
- Changing state without validation.
- Assuming a private field is accessible outside its class.
- Allowing negative quantities.

### Activities
1. Update Pencil quantity to 12.
2. Try a negative quantity and inspect the error.
3. Explain the difference between a property and a method.

### Accessibility Practice
Use explicit validation messages and one state change per operation. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define methods and fields.
- [ ] I can protect state with private fields.
- [ ] I can validate state updates.

---

## Lesson 7.4: Inheritance

### Reading References
- Python source counterpart: Unit 7 lesson 7.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create a specialized item class that extends a base class.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Inheritance models an is-a relationship. A subclass uses extends and calls super before accessing this. Use inheritance only when the subtype genuinely satisfies the base contract.

### Worked Example
```typescript
class Item {
  constructor(public name: string, public quantity: number) {}
}
class PerishableItem extends Item {
  constructor(name: string, quantity: number, public expiresOn: string) {
    super(name, quantity);
  }
  describe(): string { return `${this.name}: ${this.quantity} in stock, expires ${this.expiresOn}`; }
}
console.log(new PerishableItem("Milk", 2, "2026-11-10").describe());
```

### Expected Behavior or Output
The output is `Milk: 2 in stock, expires 2026-11-10`.

### Common Mistakes
- Forgetting to call super before using this.
- Extending a class only to reuse unrelated code.
- Changing a subclass method so it violates the base contract.

### Activities
1. Create a PerishableItem.
2. Override or add a method with a clear contract.
3. Compare inheritance with composition.

### Accessibility Practice
Use a descriptive sentence for the specialized instance. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can extend a base class.
- [ ] I can call super in a constructor.
- [ ] I can explain when inheritance is appropriate.

---

## Lesson 7.5: Composition: instances as attributes

### Reading References
- Python source counterpart: Unit 7 lesson 7.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Build a record from related objects using composition.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Composition models a has-a relationship. A class stores another object as a property rather than inheriting its behavior. This often keeps responsibilities smaller.

### Worked Example
```typescript
class Course {
  constructor(public title: string) {}
}
class StudentRecord {
  constructor(public student: Student, public course: Course) {}
  describe(): string { return `${this.student.name} studies ${this.course.title}.`; }
}
const record = new StudentRecord(new Student("Avery", 16, "Computer Science"), new Course("Computer Science"));
console.log(record.describe());
```

### Expected Behavior or Output
The output is `Avery studies Computer Science.`

### Common Mistakes
- Using inheritance for a has-a relationship.
- Creating tightly coupled classes with unclear responsibilities.
- Duplicating data already stored in a related object.

### Activities
1. Create a StudentRecord containing a Student and Course.
2. Add a method that describes the relationship.
3. Draw a text outline of the object relationships.

### Accessibility Practice
Explain object relationships in words before reading nested property access. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model a has-a relationship.
- [ ] I can compose objects from instances.
- [ ] I can distinguish composition from inheritance.

---


# Unit 8: Files and Exceptions

## Overview

Read and write files, handle errors, and persist validated JSON. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 8.1: Reading from a file

### Reading References
- Python source counterpart: Unit 8 lesson 8.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Read a line-oriented notes file with the promise-based file system API.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The node:fs/promises API returns Promises. `readFile` with UTF-8 encoding returns a string. Await file operations and handle missing-file errors explicitly.

### Worked Example
```typescript
import { readFile } from "node:fs/promises";
async function main(): Promise<void> {
  const content = await readFile("notes.txt", "utf8");
  console.log("File contents:");
  console.log(content);
}
void main();
```

### Expected Behavior or Output
With the sample file containing two notes, both lines appear after `File contents:`.

### Common Mistakes
- Reading from the wrong working directory.
- Forgetting await and logging a Promise.
- Assuming a file exists without handling ENOENT.

### Activities
1. Create notes.txt with two lines.
2. Read and print the file contents.
3. Run from a different working directory and diagnose the path.

### Accessibility Practice
Print a label before file contents and explain the working directory. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can read a UTF-8 text file.
- [ ] I can await an asynchronous operation.
- [ ] I can identify the current working directory.

---

## Lesson 8.2: Writing to a file

### Reading References
- Python source counterpart: Unit 8 lesson 8.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create and append to the same notes file using promise-based file operations.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
`writeFile` creates or replaces content; `appendFile` adds content. Await each operation so writes happen in the intended order.

### Worked Example
```typescript
import { writeFile, appendFile, readFile } from "node:fs/promises";
async function main(): Promise<void> {
  await writeFile("notes.txt", "Review arrays\n", "utf8");
  await appendFile("notes.txt", "Practice typed functions\n", "utf8");
  console.log(await readFile("notes.txt", "utf8"));
}
void main();
```

### Expected Behavior or Output
The file contains `Review arrays` followed by `Practice typed functions`, each on its own line.

### Common Mistakes
- Using writeFile when existing content must be preserved.
- Not awaiting a write before reading the file.
- Writing to an unexpected path.

### Activities
1. Create a new notes file.
2. Append a second line.
3. Read the file and verify both lines and their order.

### Accessibility Practice
Announce whether an operation creates, replaces, appends, or reads data. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can write a UTF-8 file.
- [ ] I can append without replacing existing text.
- [ ] I can sequence asynchronous file operations.

---

## Lesson 8.3: Exceptions and error handling

### Reading References
- Python source counterpart: Unit 8 lesson 8.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Handle expected file and validation errors with try/catch.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An exception interrupts normal control flow. Catch expected failures and inspect unknown error values safely; do not assume every thrown value is an Error instance.

### Worked Example
```typescript
function validateAge(age: number): void {
  if (!Number.isInteger(age) || age < 0 || age > 120) {
    throw new RangeError("Age must be a whole number from 0 to 120.");
  }
}
try {
  validateAge(16);
  console.log("Age accepted.");
  validateAge(-1);
} catch (error: unknown) {
  if (error instanceof Error) console.log(error.message);
}
```

### Expected Behavior or Output
The program prints `Age accepted.` followed by the validation message.

### Common Mistakes
- Catching every error and silently ignoring it.
- Typing catch values as any.
- Using exceptions for ordinary expected branching.

### Activities
1. Test a valid age.
2. Test -1 and 121.
3. Handle a missing file separately from malformed file contents.

### Accessibility Practice
Use explicit error messages that identify the invalid field and recovery action. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can throw a validation error.
- [ ] I can catch unknown errors safely.
- [ ] I can distinguish expected failures.

---

## Lesson 8.4: The else and finally patterns

### Reading References
- Python source counterpart: Unit 8 lesson 8.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Separate successful operations from cleanup that must always occur.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
JavaScript has no try-else clause. Put success-only work after a successful try operation and use finally for cleanup. A finally block runs whether the try succeeds or fails.

### Worked Example
```typescript
async function loadMessage(): Promise<void> {
  let loaded = false;
  try {
    const message = "Notes loaded.";
    console.log(message);
    loaded = true;
  } catch (error: unknown) {
    console.log("Unable to load notes.");
  } finally {
    console.log("Load attempt finished.");
  }
  if (loaded) console.log("Ready to continue.");
}
void loadMessage();
```

### Expected Behavior or Output
On success, the program prints Notes loaded, Load attempt finished, and Ready to continue. On failure, the final status still prints.

### Common Mistakes
- Putting success-only code in finally.
- Assuming TypeScript has Python's try-else syntax.
- Returning from finally and accidentally overriding an earlier result.

### Activities
1. Trace success and failure paths.
2. Move the success message outside the try block.
3. Explain which cleanup must always run.

### Accessibility Practice
Label success, failure, and finalization messages distinctly. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model success and failure paths.
- [ ] I can use finally for cleanup.
- [ ] I can explain the absence of a try-else clause.

---

## Lesson 8.5: Storing structured data with JSON

### Reading References
- Python source counterpart: Unit 8 lesson 8.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Serialize typed records and validate parsed JSON before use.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
JSON.parse returns untrusted runtime data. A TypeScript assertion does not validate its shape. Parse into unknown and use a type guard before treating it as a record.

### Worked Example
```typescript
interface Task { id: number; title: string; done: boolean }
function isTask(value: unknown): value is Task {
  return typeof value === "object" && value !== null &&
    "id" in value && typeof value.id === "number" &&
    "title" in value && typeof value.title === "string" &&
    "done" in value && typeof value.done === "boolean";
}
const encoded = JSON.stringify({ id: 1, title: "Review arrays", done: false });
const parsed: unknown = JSON.parse(encoded);
if (isTask(parsed)) console.log(`${parsed.id}: ${parsed.title}`);
```

### Expected Behavior or Output
The program prints `1: Review arrays` only after validating the parsed object.

### Common Mistakes
- Using `as Task` as if it checked runtime data.
- Assuming JSON.parse cannot fail.
- Failing to validate each required field.

### Activities
1. Serialize a task object.
2. Parse it as unknown and validate it.
3. Test missing fields and wrong field types.

### Accessibility Practice
Print field names and validation errors as text. Never rely on color-only success indicators. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can serialize an object to JSON.
- [ ] I can parse JSON as unknown.
- [ ] I can validate external data with a type guard.

---


# Unit 9: Testing and Data Analysis

## Overview

Test functions and classes, generate random values, analyze text, and parse CSV. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

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


# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

Design, build, and refine equivalent command-line projects. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 10.1: Designing a text-based project

### Reading References
- Python source counterpart: Unit 10 lesson 10.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Plan requirements, data structures, commands, and acceptance tests before implementation.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Top-down design decomposes a project into smaller responsibilities. For an accessible terminal project, define prompts, commands, textual feedback, invalid-input behavior, and a quit path before coding.

### Worked Example
```typescript
const requirements = ["list rooms", "move by direction", "take item", "view inventory", "quit"];
for (const requirement of requirements) console.log(`Requirement: ${requirement}`);
```

### Expected Behavior or Output
Five requirements are printed in a stable order.

### Common Mistakes
- Starting implementation before writing acceptance criteria.
- Designing a visual-only interaction for a text-based project.
- Omitting error and quit behavior.

### Activities
1. Write the project requirements in plain language.
2. Identify input, state, and output for each command.
3. Write at least five acceptance tests before implementation.

### Accessibility Practice
Use a numbered text specification and test keyboard-only interaction. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can decompose a project.
- [ ] I can define commands and data.
- [ ] I can write acceptance tests before coding.

---

## Lesson 10.2: Text adventure part 1: rooms and movement

### Reading References
- Python source counterpart: Unit 10 lesson 10.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Model the shared cave, tunnel, and clearing with typed exits and movement.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A room has an identifier, description, and exits. A movement operation changes the current room only when the requested exit exists. A Record type can model a fixed set of room identifiers.

### Worked Example
```typescript
type RoomId = "cave" | "tunnel" | "clearing";
const exits: Record<RoomId, Partial<Record<string, RoomId>>> = {
  cave: { north: "tunnel" },
  tunnel: { south: "cave", east: "clearing" },
  clearing: { west: "tunnel" }
};
function move(room: RoomId, direction: string): RoomId | null {
  return exits[room][direction.toLowerCase()] ?? null;
}
console.log(move("cave", "north"));
console.log(move("cave", "west"));
```

### Expected Behavior or Output
Moving north from cave returns tunnel; moving west returns null.

### Common Mistakes
- Allowing movement through an exit that is not defined.
- Changing the room before validating the direction.
- Using arbitrary strings where a RoomId union is safer.

### Activities
1. Create all three rooms and exits.
2. Move north from cave and east from tunnel.
3. Attempt an invalid direction and report the result.

### Accessibility Practice
Announce current room and available exits as labeled text. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model rooms and exits.
- [ ] I can use a union type for room identifiers.
- [ ] I can validate movement.

---

## Lesson 10.3: Text adventure part 2: items, inventory, and puzzle

### Reading References
- Python source counterpart: Unit 10 lesson 10.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement item pickup and the shared magic-key puzzle.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An item moves from one room to inventory as one state transition. The player can take the torch in the cave and the magic key in the clearing; the key unlocks the gate.

### Worked Example
```typescript
const roomItems: Record<string, string[]> = { cave: ["torch"], tunnel: [], clearing: ["magic key"] };
const inventory: string[] = [];
function takeItem(room: string, item: string): boolean {
  const items = roomItems[room] ?? [];
  const index = items.findIndex(value => value.toLowerCase() === item.toLowerCase());
  if (index < 0) return false;
  inventory.push(items.splice(index, 1)[0]);
  return true;
}
function unlockGate(items: readonly string[]): string {
  return items.includes("magic key") ? "The gate opens." : "The gate is locked.";
}
console.log(takeItem("cave", "torch"));
console.log(inventory.join(", "));
console.log(unlockGate(["torch"]));
console.log(unlockGate(["torch", "magic key"]));
```

### Expected Behavior or Output
Output is true, torch, The gate is locked., and The gate opens.

### Common Mistakes
- Allowing the same item to be collected repeatedly.
- Updating inventory without removing the room item.
- Checking for the wrong key name or case.

### Activities
1. Take the torch from the cave.
2. Take the magic key from the clearing.
3. Test the gate with and without the key.

### Accessibility Practice
Confirm each pickup by item name and state whether the puzzle is locked or open. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can transfer an item into inventory.
- [ ] I can prevent duplicate pickup.
- [ ] I can implement the magic-key puzzle.

---

## Lesson 10.4: Developing a command-line to-do tool

### Reading References
- Python source counterpart: Unit 10 lesson 10.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement add, view, complete, delete, and quit operations with typed tasks.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A task has an id, title, description, done state, and creation timestamp. User-facing task numbers are one-based; array indexes are zero-based. Persist after every state-changing operation.

### Worked Example
```typescript
interface Todo { id: number; title: string; description: string; done: boolean; created_at: string }
const tasks: Todo[] = [];
function addTask(title: string, description: string): Todo {
  const task: Todo = { id: tasks.length + 1, title, description, done: false, created_at: new Date().toISOString() };
  tasks.push(task);
  return task;
}
console.log(addTask("Review arrays", "Practice typed collection methods").done);
```

### Expected Behavior or Output
A new task is added with done false and an ISO timestamp.

### Common Mistakes
- Using an array index as a permanent identifier.
- Failing to save after a state change.
- Accepting a blank task title.

### Activities
1. Add a task and view it.
2. Mark a task complete and delete another.
3. Persist and reload the task array as JSON.

### Accessibility Practice
Use one task per output block with field labels and a clear confirmation. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model a typed task.
- [ ] I can implement task creation.
- [ ] I can identify persistence points.

---

## Lesson 10.5: Refinement and accessible text user experience

### Reading References
- Python source counterpart: Unit 10 lesson 10.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Improve validation, prompts, error messages, and recovery paths.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A usable terminal interface has explicit prompts, predictable output, help text, and recoverable errors. A robust program validates untrusted values before changing state.

### Worked Example
```typescript
function normalizeCommand(input: string): string {
  return input.trim().toLowerCase();
}
function validateTitle(input: string): string | null {
  const title = input.trim();
  return title.length === 0 ? "Title cannot be blank." : null;
}
console.log(normalizeCommand("  VIEW "));
console.log(validateTitle("   "));
```

### Expected Behavior or Output
The output is view and Title cannot be blank.

### Common Mistakes
- Providing vague messages such as invalid input without a recovery hint.
- Using color as the only status indicator.
- Failing to test blank input, unknown commands, and empty collections.

### Activities
1. Add a help command.
2. Test blank, malformed, and unknown commands.
3. Review every message in sequential screen-reader output.

### Accessibility Practice
Provide text equivalents for every status and avoid cursor-position-dependent instructions. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can normalize command input.
- [ ] I can validate required fields.
- [ ] I can review a text interface for accessibility.

---


# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

Integrate typed records, terminal interaction, persistence, CRUD, testing, and accessibility. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 11.1: Capstone interface and requirements

### Reading References
- Python source counterpart: Unit 11 lesson 11.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Plan an accessible terminal interface for the personal data manager.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The Python source uses NiceGUI, but the TypeScript track uses a terminal interface to preserve the same user-facing requirements without requiring browser UI. Commands include list, add, search, update, delete, help, and quit.

### Worked Example
```typescript
const commands = ["list", "add", "search", "update", "delete", "help", "quit"];
console.log(commands.join(", "));
```

### Expected Behavior or Output
The command list contains all seven required operations.

### Common Mistakes
- Copying a GUI-specific implementation when the language track requires an accessible alternative.
- Omitting a help or quit command.
- Designing commands without defining expected output.

### Activities
1. Choose a terminal command syntax.
2. Write a help response for every command.
3. Define keyboard-only acceptance tests.

### Accessibility Practice
Specify prompt order and output as linear text. Do not require mouse use. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can explain the language-specific interface adaptation.
- [ ] I can define the required commands.
- [ ] I can create accessibility acceptance tests.

---

## Lesson 11.2: Capstone data model and JSON storage

### Reading References
- Python source counterpart: Unit 11 lesson 11.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Define the shared record schema and save/load records safely.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Each record has id, title, description, category, created_at, and updated_at. TypeScript interfaces describe the expected shape, but JSON input must be validated at runtime.

### Worked Example
```typescript
interface DataRecord { id: number; title: string; description: string; category: string; created_at: string; updated_at: string }
const record: DataRecord = { id: 1, title: "Course notes", description: "Review arrays", category: "Study", created_at: "2026-11-01T10:00:00.000Z", updated_at: "2026-11-01T10:00:00.000Z" };
const serialized = JSON.stringify([record], null, 2);
console.log(serialized.includes("Course notes"));
```

### Expected Behavior or Output
The check prints true and the JSON contains all six fields.

### Common Mistakes
- Using a type assertion instead of validating loaded JSON.
- Reusing record identifiers.
- Overwriting valid data after a parse failure without reporting it.

### Activities
1. Define the six-field interface.
2. Serialize one record and inspect the JSON.
3. Load and validate records before using them.

### Accessibility Practice
Read the schema field by field and keep timestamps in a consistent ISO format. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define the capstone record interface.
- [ ] I can serialize structured data.
- [ ] I can explain runtime validation of stored JSON.

---

## Lesson 11.3: Capstone list and display operations

### Reading References
- Python source counterpart: Unit 11 lesson 11.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Display records in a stable, labeled, sequential format.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Listing is a read operation and should not mutate data. Stable identifiers are distinct from temporary one-based display positions.

### Worked Example
```typescript
const records = [{ id: 7, title: "Course notes", category: "Study", done: false }];
for (const [index, record] of records.entries()) {
  console.log(`Item ${index + 1}`);
  console.log(`ID: ${record.id}`);
  console.log(`Title: ${record.title}`);
  console.log(`Category: ${record.category}`);
  console.log(`Done: ${record.done}`);
}
```

### Expected Behavior or Output
The record is displayed as Item 1 with ID 7 and its labeled fields.

### Common Mistakes
- Using the displayed list number as the permanent ID.
- Omitting labels and making output ambiguous.
- Failing to handle an empty collection.

### Activities
1. Display one record.
2. Display multiple records.
3. Display an empty list with a clear message.

### Accessibility Practice
Use stable labels and one field per line for sequential reading. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can display records with labels.
- [ ] I can distinguish display position from record ID.
- [ ] I can handle an empty collection.

---

## Lesson 11.4: Capstone add, search, and update operations

### Reading References
- Python source counterpart: Unit 11 lesson 11.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement creation, case-insensitive search, and safe record updates.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Create, search, and update are separate operations. Update only permitted fields and refresh updated_at. Search should not change stored records.

### Worked Example
```typescript
interface Entry { id: number; title: string; description: string; updated_at: string }
function search(entries: readonly Entry[], query: string): Entry[] {
  const term = query.trim().toLowerCase();
  return entries.filter(entry => `${entry.title} ${entry.description}`.toLowerCase().includes(term));
}
const entries: Entry[] = [{ id: 1, title: "Course notes", description: "Review arrays", updated_at: "2026-11-01T10:00:00.000Z" }];
console.log(search(entries, "ARRAYS").length);
```

### Expected Behavior or Output
The search returns one matching record.

### Common Mistakes
- Searching case-sensitively without documenting that choice.
- Allowing edits to immutable identifiers.
- Forgetting to refresh updated_at after an edit.

### Activities
1. Add a record with all required fields.
2. Search by title and description.
3. Update a title and verify the timestamp changes.

### Accessibility Practice
Confirm each successful action by record ID and field name. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can add a valid record.
- [ ] I can search without mutating records.
- [ ] I can update permitted fields and timestamps.

---

## Lesson 11.5: Capstone delete, completion, and final verification

### Reading References
- Python source counterpart: Unit 11 lesson 11.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement delete and completion behavior and verify persistence and accessibility.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Deletion removes a selected record by stable ID. Completion updates the record state. The capstone should have tests for CRUD behavior, JSON persistence, invalid input, and empty data.

### Worked Example
```typescript
interface TaskRecord { id: number; title: string; done: boolean }
function markDone(records: TaskRecord[], id: number): boolean {
  const record = records.find(item => item.id === id);
  if (!record) return false;
  record.done = true;
  return true;
}
const records: TaskRecord[] = [{ id: 4, title: "Test persistence", done: false }];
console.log(markDone(records, 4));
console.log(records[0].done);
```

### Expected Behavior or Output
The function returns true and the record's done field becomes true.

### Common Mistakes
- Deleting by a stale array index.
- Failing to save after a mutation.
- Testing only the successful path.

### Activities
1. Delete a record by ID and verify it remains absent after reload.
2. Mark a record complete and test missing IDs.
3. Run at least five tests covering CRUD, persistence, and validation.

### Accessibility Practice
Verify keyboard-only use, help text, confirmations, errors, and sequential output with the intended access technology. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can delete by stable identifier.
- [ ] I can update completion state.
- [ ] I can plan end-to-end and accessibility tests.

---


# Unit 6: Functions

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


# Unit 7: Classes and Object-Oriented Programming

## Overview

Model state and behavior using classes, inheritance, and composition. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 7.1: Why learn about classes?

### Reading References
- Python source counterpart: Unit 7 lesson 7.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Explain classes, instances, encapsulation, and object state with an inventory example.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A class describes the state and behavior of objects. TypeScript classes add static type checking, access modifiers, and optional private fields; types are erased from emitted JavaScript.

### Worked Example
```typescript
class InventoryItem {
  constructor(public name: string, public quantity: number, public unitPrice: number) {}
  value(): number { return this.quantity * this.unitPrice; }
}
const notebook = new InventoryItem("Notebook", 3, 2.5);
console.log(`${notebook.name}: ${notebook.value().toFixed(2)}`);
```

### Expected Behavior or Output
The output is `Notebook: 7.50`.

### Common Mistakes
- Treating a class as only a data container without behavior.
- Confusing a class with an instance.
- Assuming TypeScript access modifiers create runtime security.

### Activities
1. Identify the fields and behavior of an inventory item.
2. Create two instances with different values.
3. Explain what the class and each instance represent.

### Accessibility Practice
Use meaningful instance names and print a labeled summary. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can explain class and instance.
- [ ] I can identify state and behavior.
- [ ] I can create a simple class.

---

## Lesson 7.2: Creating and using a class

### Reading References
- Python source counterpart: Unit 7 lesson 7.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create a Student class and instantiate the canonical learner profile.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A constructor initializes an instance. Parameter properties can declare and initialize fields in one place. Explicit types make the class contract readable.

### Worked Example
```typescript
class Student {
  constructor(public name: string, public age: number, public favoriteSubject: string) {}
  describe(): string { return `${this.name}, age ${this.age}, studies ${this.favoriteSubject}`; }
}
const learner = new Student("Avery", 16, "Computer Science");
console.log(learner.describe());
```

### Expected Behavior or Output
The output is `Avery, age 16, studies Computer Science`.

### Common Mistakes
- Forgetting new when constructing an instance.
- Using a parameter type that conflicts with the property type.
- Writing a method that refers to a variable instead of this.

### Activities
1. Create Avery's Student instance.
2. Create a second student instance.
3. Call describe on both instances.

### Accessibility Practice
Read constructor parameters in order and label each property. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define a constructor.
- [ ] I can instantiate a class.
- [ ] I can call an instance method.

---

## Lesson 7.3: Working with attributes and methods

### Reading References
- Python source counterpart: Unit 7 lesson 7.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Add validation and update behavior to a class.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Methods define operations over an instance's state. Encapsulation keeps validation close to the state it protects. Private fields and access modifiers guide compile-time access.

### Worked Example
```typescript
class StockItem {
  #quantity: number;
  constructor(public name: string, quantity: number) { this.#quantity = quantity; }
  get quantity(): number { return this.#quantity; }
  setQuantity(value: number): void {
    if (!Number.isInteger(value) || value < 0) throw new RangeError("Quantity must be a nonnegative integer.");
    this.#quantity = value;
  }
}
const pencil = new StockItem("Pencil", 10);
pencil.setQuantity(12);
console.log(pencil.quantity);
```

### Expected Behavior or Output
The output is 12. A negative or fractional quantity throws RangeError.

### Common Mistakes
- Changing state without validation.
- Assuming a private field is accessible outside its class.
- Allowing negative quantities.

### Activities
1. Update Pencil quantity to 12.
2. Try a negative quantity and inspect the error.
3. Explain the difference between a property and a method.

### Accessibility Practice
Use explicit validation messages and one state change per operation. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define methods and fields.
- [ ] I can protect state with private fields.
- [ ] I can validate state updates.

---

## Lesson 7.4: Inheritance

### Reading References
- Python source counterpart: Unit 7 lesson 7.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create a specialized item class that extends a base class.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Inheritance models an is-a relationship. A subclass uses extends and calls super before accessing this. Use inheritance only when the subtype genuinely satisfies the base contract.

### Worked Example
```typescript
class Item {
  constructor(public name: string, public quantity: number) {}
}
class PerishableItem extends Item {
  constructor(name: string, quantity: number, public expiresOn: string) {
    super(name, quantity);
  }
  describe(): string { return `${this.name}: ${this.quantity} in stock, expires ${this.expiresOn}`; }
}
console.log(new PerishableItem("Milk", 2, "2026-11-10").describe());
```

### Expected Behavior or Output
The output is `Milk: 2 in stock, expires 2026-11-10`.

### Common Mistakes
- Forgetting to call super before using this.
- Extending a class only to reuse unrelated code.
- Changing a subclass method so it violates the base contract.

### Activities
1. Create a PerishableItem.
2. Override or add a method with a clear contract.
3. Compare inheritance with composition.

### Accessibility Practice
Use a descriptive sentence for the specialized instance. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can extend a base class.
- [ ] I can call super in a constructor.
- [ ] I can explain when inheritance is appropriate.

---

## Lesson 7.5: Composition: instances as attributes

### Reading References
- Python source counterpart: Unit 7 lesson 7.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Build a record from related objects using composition.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Composition models a has-a relationship. A class stores another object as a property rather than inheriting its behavior. This often keeps responsibilities smaller.

### Worked Example
```typescript
class Course {
  constructor(public title: string) {}
}
class StudentRecord {
  constructor(public student: Student, public course: Course) {}
  describe(): string { return `${this.student.name} studies ${this.course.title}.`; }
}
const record = new StudentRecord(new Student("Avery", 16, "Computer Science"), new Course("Computer Science"));
console.log(record.describe());
```

### Expected Behavior or Output
The output is `Avery studies Computer Science.`

### Common Mistakes
- Using inheritance for a has-a relationship.
- Creating tightly coupled classes with unclear responsibilities.
- Duplicating data already stored in a related object.

### Activities
1. Create a StudentRecord containing a Student and Course.
2. Add a method that describes the relationship.
3. Draw a text outline of the object relationships.

### Accessibility Practice
Explain object relationships in words before reading nested property access. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model a has-a relationship.
- [ ] I can compose objects from instances.
- [ ] I can distinguish composition from inheritance.

---


# Unit 8: Files and Exceptions

## Overview

Read and write files, handle errors, and persist validated JSON. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 8.1: Reading from a file

### Reading References
- Python source counterpart: Unit 8 lesson 8.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Read a line-oriented notes file with the promise-based file system API.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The node:fs/promises API returns Promises. `readFile` with UTF-8 encoding returns a string. Await file operations and handle missing-file errors explicitly.

### Worked Example
```typescript
import { readFile } from "node:fs/promises";
async function main(): Promise<void> {
  const content = await readFile("notes.txt", "utf8");
  console.log("File contents:");
  console.log(content);
}
void main();
```

### Expected Behavior or Output
With the sample file containing two notes, both lines appear after `File contents:`.

### Common Mistakes
- Reading from the wrong working directory.
- Forgetting await and logging a Promise.
- Assuming a file exists without handling ENOENT.

### Activities
1. Create notes.txt with two lines.
2. Read and print the file contents.
3. Run from a different working directory and diagnose the path.

### Accessibility Practice
Print a label before file contents and explain the working directory. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can read a UTF-8 text file.
- [ ] I can await an asynchronous operation.
- [ ] I can identify the current working directory.

---

## Lesson 8.2: Writing to a file

### Reading References
- Python source counterpart: Unit 8 lesson 8.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create and append to the same notes file using promise-based file operations.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
`writeFile` creates or replaces content; `appendFile` adds content. Await each operation so writes happen in the intended order.

### Worked Example
```typescript
import { writeFile, appendFile, readFile } from "node:fs/promises";
async function main(): Promise<void> {
  await writeFile("notes.txt", "Review arrays\n", "utf8");
  await appendFile("notes.txt", "Practice typed functions\n", "utf8");
  console.log(await readFile("notes.txt", "utf8"));
}
void main();
```

### Expected Behavior or Output
The file contains `Review arrays` followed by `Practice typed functions`, each on its own line.

### Common Mistakes
- Using writeFile when existing content must be preserved.
- Not awaiting a write before reading the file.
- Writing to an unexpected path.

### Activities
1. Create a new notes file.
2. Append a second line.
3. Read the file and verify both lines and their order.

### Accessibility Practice
Announce whether an operation creates, replaces, appends, or reads data. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can write a UTF-8 file.
- [ ] I can append without replacing existing text.
- [ ] I can sequence asynchronous file operations.

---

## Lesson 8.3: Exceptions and error handling

### Reading References
- Python source counterpart: Unit 8 lesson 8.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Handle expected file and validation errors with try/catch.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An exception interrupts normal control flow. Catch expected failures and inspect unknown error values safely; do not assume every thrown value is an Error instance.

### Worked Example
```typescript
function validateAge(age: number): void {
  if (!Number.isInteger(age) || age < 0 || age > 120) {
    throw new RangeError("Age must be a whole number from 0 to 120.");
  }
}
try {
  validateAge(16);
  console.log("Age accepted.");
  validateAge(-1);
} catch (error: unknown) {
  if (error instanceof Error) console.log(error.message);
}
```

### Expected Behavior or Output
The program prints `Age accepted.` followed by the validation message.

### Common Mistakes
- Catching every error and silently ignoring it.
- Typing catch values as any.
- Using exceptions for ordinary expected branching.

### Activities
1. Test a valid age.
2. Test -1 and 121.
3. Handle a missing file separately from malformed file contents.

### Accessibility Practice
Use explicit error messages that identify the invalid field and recovery action. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can throw a validation error.
- [ ] I can catch unknown errors safely.
- [ ] I can distinguish expected failures.

---

## Lesson 8.4: The else and finally patterns

### Reading References
- Python source counterpart: Unit 8 lesson 8.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Separate successful operations from cleanup that must always occur.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
JavaScript has no try-else clause. Put success-only work after a successful try operation and use finally for cleanup. A finally block runs whether the try succeeds or fails.

### Worked Example
```typescript
async function loadMessage(): Promise<void> {
  let loaded = false;
  try {
    const message = "Notes loaded.";
    console.log(message);
    loaded = true;
  } catch (error: unknown) {
    console.log("Unable to load notes.");
  } finally {
    console.log("Load attempt finished.");
  }
  if (loaded) console.log("Ready to continue.");
}
void loadMessage();
```

### Expected Behavior or Output
On success, the program prints Notes loaded, Load attempt finished, and Ready to continue. On failure, the final status still prints.

### Common Mistakes
- Putting success-only code in finally.
- Assuming TypeScript has Python's try-else syntax.
- Returning from finally and accidentally overriding an earlier result.

### Activities
1. Trace success and failure paths.
2. Move the success message outside the try block.
3. Explain which cleanup must always run.

### Accessibility Practice
Label success, failure, and finalization messages distinctly. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model success and failure paths.
- [ ] I can use finally for cleanup.
- [ ] I can explain the absence of a try-else clause.

---

## Lesson 8.5: Storing structured data with JSON

### Reading References
- Python source counterpart: Unit 8 lesson 8.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Serialize typed records and validate parsed JSON before use.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
JSON.parse returns untrusted runtime data. A TypeScript assertion does not validate its shape. Parse into unknown and use a type guard before treating it as a record.

### Worked Example
```typescript
interface Task { id: number; title: string; done: boolean }
function isTask(value: unknown): value is Task {
  return typeof value === "object" && value !== null &&
    "id" in value && typeof value.id === "number" &&
    "title" in value && typeof value.title === "string" &&
    "done" in value && typeof value.done === "boolean";
}
const encoded = JSON.stringify({ id: 1, title: "Review arrays", done: false });
const parsed: unknown = JSON.parse(encoded);
if (isTask(parsed)) console.log(`${parsed.id}: ${parsed.title}`);
```

### Expected Behavior or Output
The program prints `1: Review arrays` only after validating the parsed object.

### Common Mistakes
- Using `as Task` as if it checked runtime data.
- Assuming JSON.parse cannot fail.
- Failing to validate each required field.

### Activities
1. Serialize a task object.
2. Parse it as unknown and validate it.
3. Test missing fields and wrong field types.

### Accessibility Practice
Print field names and validation errors as text. Never rely on color-only success indicators. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can serialize an object to JSON.
- [ ] I can parse JSON as unknown.
- [ ] I can validate external data with a type guard.

---


# Unit 9: Testing and Data Analysis

## Overview

Test functions and classes, generate random values, analyze text, and parse CSV. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

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


# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

Design, build, and refine equivalent command-line projects. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 10.1: Designing a text-based project

### Reading References
- Python source counterpart: Unit 10 lesson 10.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Plan requirements, data structures, commands, and acceptance tests before implementation.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Top-down design decomposes a project into smaller responsibilities. For an accessible terminal project, define prompts, commands, textual feedback, invalid-input behavior, and a quit path before coding.

### Worked Example
```typescript
const requirements = ["list rooms", "move by direction", "take item", "view inventory", "quit"];
for (const requirement of requirements) console.log(`Requirement: ${requirement}`);
```

### Expected Behavior or Output
Five requirements are printed in a stable order.

### Common Mistakes
- Starting implementation before writing acceptance criteria.
- Designing a visual-only interaction for a text-based project.
- Omitting error and quit behavior.

### Activities
1. Write the project requirements in plain language.
2. Identify input, state, and output for each command.
3. Write at least five acceptance tests before implementation.

### Accessibility Practice
Use a numbered text specification and test keyboard-only interaction. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can decompose a project.
- [ ] I can define commands and data.
- [ ] I can write acceptance tests before coding.

---

## Lesson 10.2: Text adventure part 1: rooms and movement

### Reading References
- Python source counterpart: Unit 10 lesson 10.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Model the shared cave, tunnel, and clearing with typed exits and movement.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A room has an identifier, description, and exits. A movement operation changes the current room only when the requested exit exists. A Record type can model a fixed set of room identifiers.

### Worked Example
```typescript
type RoomId = "cave" | "tunnel" | "clearing";
const exits: Record<RoomId, Partial<Record<string, RoomId>>> = {
  cave: { north: "tunnel" },
  tunnel: { south: "cave", east: "clearing" },
  clearing: { west: "tunnel" }
};
function move(room: RoomId, direction: string): RoomId | null {
  return exits[room][direction.toLowerCase()] ?? null;
}
console.log(move("cave", "north"));
console.log(move("cave", "west"));
```

### Expected Behavior or Output
Moving north from cave returns tunnel; moving west returns null.

### Common Mistakes
- Allowing movement through an exit that is not defined.
- Changing the room before validating the direction.
- Using arbitrary strings where a RoomId union is safer.

### Activities
1. Create all three rooms and exits.
2. Move north from cave and east from tunnel.
3. Attempt an invalid direction and report the result.

### Accessibility Practice
Announce current room and available exits as labeled text. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model rooms and exits.
- [ ] I can use a union type for room identifiers.
- [ ] I can validate movement.

---

## Lesson 10.3: Text adventure part 2: items, inventory, and puzzle

### Reading References
- Python source counterpart: Unit 10 lesson 10.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement item pickup and the shared magic-key puzzle.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An item moves from one room to inventory as one state transition. The player can take the torch in the cave and the magic key in the clearing; the key unlocks the gate.

### Worked Example
```typescript
const roomItems: Record<string, string[]> = { cave: ["torch"], tunnel: [], clearing: ["magic key"] };
const inventory: string[] = [];
function takeItem(room: string, item: string): boolean {
  const items = roomItems[room] ?? [];
  const index = items.findIndex(value => value.toLowerCase() === item.toLowerCase());
  if (index < 0) return false;
  inventory.push(items.splice(index, 1)[0]);
  return true;
}
function unlockGate(items: readonly string[]): string {
  return items.includes("magic key") ? "The gate opens." : "The gate is locked.";
}
console.log(takeItem("cave", "torch"));
console.log(inventory.join(", "));
console.log(unlockGate(["torch"]));
console.log(unlockGate(["torch", "magic key"]));
```

### Expected Behavior or Output
Output is true, torch, The gate is locked., and The gate opens.

### Common Mistakes
- Allowing the same item to be collected repeatedly.
- Updating inventory without removing the room item.
- Checking for the wrong key name or case.

### Activities
1. Take the torch from the cave.
2. Take the magic key from the clearing.
3. Test the gate with and without the key.

### Accessibility Practice
Confirm each pickup by item name and state whether the puzzle is locked or open. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can transfer an item into inventory.
- [ ] I can prevent duplicate pickup.
- [ ] I can implement the magic-key puzzle.

---

## Lesson 10.4: Developing a command-line to-do tool

### Reading References
- Python source counterpart: Unit 10 lesson 10.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement add, view, complete, delete, and quit operations with typed tasks.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A task has an id, title, description, done state, and creation timestamp. User-facing task numbers are one-based; array indexes are zero-based. Persist after every state-changing operation.

### Worked Example
```typescript
interface Todo { id: number; title: string; description: string; done: boolean; created_at: string }
const tasks: Todo[] = [];
function addTask(title: string, description: string): Todo {
  const task: Todo = { id: tasks.length + 1, title, description, done: false, created_at: new Date().toISOString() };
  tasks.push(task);
  return task;
}
console.log(addTask("Review arrays", "Practice typed collection methods").done);
```

### Expected Behavior or Output
A new task is added with done false and an ISO timestamp.

### Common Mistakes
- Using an array index as a permanent identifier.
- Failing to save after a state change.
- Accepting a blank task title.

### Activities
1. Add a task and view it.
2. Mark a task complete and delete another.
3. Persist and reload the task array as JSON.

### Accessibility Practice
Use one task per output block with field labels and a clear confirmation. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model a typed task.
- [ ] I can implement task creation.
- [ ] I can identify persistence points.

---

## Lesson 10.5: Refinement and accessible text user experience

### Reading References
- Python source counterpart: Unit 10 lesson 10.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Improve validation, prompts, error messages, and recovery paths.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A usable terminal interface has explicit prompts, predictable output, help text, and recoverable errors. A robust program validates untrusted values before changing state.

### Worked Example
```typescript
function normalizeCommand(input: string): string {
  return input.trim().toLowerCase();
}
function validateTitle(input: string): string | null {
  const title = input.trim();
  return title.length === 0 ? "Title cannot be blank." : null;
}
console.log(normalizeCommand("  VIEW "));
console.log(validateTitle("   "));
```

### Expected Behavior or Output
The output is view and Title cannot be blank.

### Common Mistakes
- Providing vague messages such as invalid input without a recovery hint.
- Using color as the only status indicator.
- Failing to test blank input, unknown commands, and empty collections.

### Activities
1. Add a help command.
2. Test blank, malformed, and unknown commands.
3. Review every message in sequential screen-reader output.

### Accessibility Practice
Provide text equivalents for every status and avoid cursor-position-dependent instructions. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can normalize command input.
- [ ] I can validate required fields.
- [ ] I can review a text interface for accessibility.

---


# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

Integrate typed records, terminal interaction, persistence, CRUD, testing, and accessibility. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 11.1: Capstone interface and requirements

### Reading References
- Python source counterpart: Unit 11 lesson 11.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Plan an accessible terminal interface for the personal data manager.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The Python source uses NiceGUI, but the TypeScript track uses a terminal interface to preserve the same user-facing requirements without requiring browser UI. Commands include list, add, search, update, delete, help, and quit.

### Worked Example
```typescript
const commands = ["list", "add", "search", "update", "delete", "help", "quit"];
console.log(commands.join(", "));
```

### Expected Behavior or Output
The command list contains all seven required operations.

### Common Mistakes
- Copying a GUI-specific implementation when the language track requires an accessible alternative.
- Omitting a help or quit command.
- Designing commands without defining expected output.

### Activities
1. Choose a terminal command syntax.
2. Write a help response for every command.
3. Define keyboard-only acceptance tests.

### Accessibility Practice
Specify prompt order and output as linear text. Do not require mouse use. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can explain the language-specific interface adaptation.
- [ ] I can define the required commands.
- [ ] I can create accessibility acceptance tests.

---

## Lesson 11.2: Capstone data model and JSON storage

### Reading References
- Python source counterpart: Unit 11 lesson 11.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Define the shared record schema and save/load records safely.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Each record has id, title, description, category, created_at, and updated_at. TypeScript interfaces describe the expected shape, but JSON input must be validated at runtime.

### Worked Example
```typescript
interface DataRecord { id: number; title: string; description: string; category: string; created_at: string; updated_at: string }
const record: DataRecord = { id: 1, title: "Course notes", description: "Review arrays", category: "Study", created_at: "2026-11-01T10:00:00.000Z", updated_at: "2026-11-01T10:00:00.000Z" };
const serialized = JSON.stringify([record], null, 2);
console.log(serialized.includes("Course notes"));
```

### Expected Behavior or Output
The check prints true and the JSON contains all six fields.

### Common Mistakes
- Using a type assertion instead of validating loaded JSON.
- Reusing record identifiers.
- Overwriting valid data after a parse failure without reporting it.

### Activities
1. Define the six-field interface.
2. Serialize one record and inspect the JSON.
3. Load and validate records before using them.

### Accessibility Practice
Read the schema field by field and keep timestamps in a consistent ISO format. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define the capstone record interface.
- [ ] I can serialize structured data.
- [ ] I can explain runtime validation of stored JSON.

---

## Lesson 11.3: Capstone list and display operations

### Reading References
- Python source counterpart: Unit 11 lesson 11.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Display records in a stable, labeled, sequential format.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Listing is a read operation and should not mutate data. Stable identifiers are distinct from temporary one-based display positions.

### Worked Example
```typescript
const records = [{ id: 7, title: "Course notes", category: "Study", done: false }];
for (const [index, record] of records.entries()) {
  console.log(`Item ${index + 1}`);
  console.log(`ID: ${record.id}`);
  console.log(`Title: ${record.title}`);
  console.log(`Category: ${record.category}`);
  console.log(`Done: ${record.done}`);
}
```

### Expected Behavior or Output
The record is displayed as Item 1 with ID 7 and its labeled fields.

### Common Mistakes
- Using the displayed list number as the permanent ID.
- Omitting labels and making output ambiguous.
- Failing to handle an empty collection.

### Activities
1. Display one record.
2. Display multiple records.
3. Display an empty list with a clear message.

### Accessibility Practice
Use stable labels and one field per line for sequential reading. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can display records with labels.
- [ ] I can distinguish display position from record ID.
- [ ] I can handle an empty collection.

---

## Lesson 11.4: Capstone add, search, and update operations

### Reading References
- Python source counterpart: Unit 11 lesson 11.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement creation, case-insensitive search, and safe record updates.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Create, search, and update are separate operations. Update only permitted fields and refresh updated_at. Search should not change stored records.

### Worked Example
```typescript
interface Entry { id: number; title: string; description: string; updated_at: string }
function search(entries: readonly Entry[], query: string): Entry[] {
  const term = query.trim().toLowerCase();
  return entries.filter(entry => `${entry.title} ${entry.description}`.toLowerCase().includes(term));
}
const entries: Entry[] = [{ id: 1, title: "Course notes", description: "Review arrays", updated_at: "2026-11-01T10:00:00.000Z" }];
console.log(search(entries, "ARRAYS").length);
```

### Expected Behavior or Output
The search returns one matching record.

### Common Mistakes
- Searching case-sensitively without documenting that choice.
- Allowing edits to immutable identifiers.
- Forgetting to refresh updated_at after an edit.

### Activities
1. Add a record with all required fields.
2. Search by title and description.
3. Update a title and verify the timestamp changes.

### Accessibility Practice
Confirm each successful action by record ID and field name. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can add a valid record.
- [ ] I can search without mutating records.
- [ ] I can update permitted fields and timestamps.

---

## Lesson 11.5: Capstone delete, completion, and final verification

### Reading References
- Python source counterpart: Unit 11 lesson 11.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement delete and completion behavior and verify persistence and accessibility.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Deletion removes a selected record by stable ID. Completion updates the record state. The capstone should have tests for CRUD behavior, JSON persistence, invalid input, and empty data.

### Worked Example
```typescript
interface TaskRecord { id: number; title: string; done: boolean }
function markDone(records: TaskRecord[], id: number): boolean {
  const record = records.find(item => item.id === id);
  if (!record) return false;
  record.done = true;
  return true;
}
const records: TaskRecord[] = [{ id: 4, title: "Test persistence", done: false }];
console.log(markDone(records, 4));
console.log(records[0].done);
```

### Expected Behavior or Output
The function returns true and the record's done field becomes true.

### Common Mistakes
- Deleting by a stale array index.
- Failing to save after a mutation.
- Testing only the successful path.

### Activities
1. Delete a record by ID and verify it remains absent after reload.
2. Mark a record complete and test missing IDs.
3. Run at least five tests covering CRUD, persistence, and validation.

### Accessibility Practice
Verify keyboard-only use, help text, confirmations, errors, and sequential output with the intended access technology. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can delete by stable identifier.
- [ ] I can update completion state.
- [ ] I can plan end-to-end and accessibility tests.

---


# Unit 7: Classes and Object-Oriented Programming

## Overview

Model state and behavior using classes, inheritance, and composition. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 7.1: Why learn about classes?

### Reading References
- Python source counterpart: Unit 7 lesson 7.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Explain classes, instances, encapsulation, and object state with an inventory example.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A class describes the state and behavior of objects. TypeScript classes add static type checking, access modifiers, and optional private fields; types are erased from emitted JavaScript.

### Worked Example
```typescript
class InventoryItem {
  constructor(public name: string, public quantity: number, public unitPrice: number) {}
  value(): number { return this.quantity * this.unitPrice; }
}
const notebook = new InventoryItem("Notebook", 3, 2.5);
console.log(`${notebook.name}: ${notebook.value().toFixed(2)}`);
```

### Expected Behavior or Output
The output is `Notebook: 7.50`.

### Common Mistakes
- Treating a class as only a data container without behavior.
- Confusing a class with an instance.
- Assuming TypeScript access modifiers create runtime security.

### Activities
1. Identify the fields and behavior of an inventory item.
2. Create two instances with different values.
3. Explain what the class and each instance represent.

### Accessibility Practice
Use meaningful instance names and print a labeled summary. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can explain class and instance.
- [ ] I can identify state and behavior.
- [ ] I can create a simple class.

---

## Lesson 7.2: Creating and using a class

### Reading References
- Python source counterpart: Unit 7 lesson 7.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create a Student class and instantiate the canonical learner profile.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A constructor initializes an instance. Parameter properties can declare and initialize fields in one place. Explicit types make the class contract readable.

### Worked Example
```typescript
class Student {
  constructor(public name: string, public age: number, public favoriteSubject: string) {}
  describe(): string { return `${this.name}, age ${this.age}, studies ${this.favoriteSubject}`; }
}
const learner = new Student("Avery", 16, "Computer Science");
console.log(learner.describe());
```

### Expected Behavior or Output
The output is `Avery, age 16, studies Computer Science`.

### Common Mistakes
- Forgetting new when constructing an instance.
- Using a parameter type that conflicts with the property type.
- Writing a method that refers to a variable instead of this.

### Activities
1. Create Avery's Student instance.
2. Create a second student instance.
3. Call describe on both instances.

### Accessibility Practice
Read constructor parameters in order and label each property. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define a constructor.
- [ ] I can instantiate a class.
- [ ] I can call an instance method.

---

## Lesson 7.3: Working with attributes and methods

### Reading References
- Python source counterpart: Unit 7 lesson 7.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Add validation and update behavior to a class.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Methods define operations over an instance's state. Encapsulation keeps validation close to the state it protects. Private fields and access modifiers guide compile-time access.

### Worked Example
```typescript
class StockItem {
  #quantity: number;
  constructor(public name: string, quantity: number) { this.#quantity = quantity; }
  get quantity(): number { return this.#quantity; }
  setQuantity(value: number): void {
    if (!Number.isInteger(value) || value < 0) throw new RangeError("Quantity must be a nonnegative integer.");
    this.#quantity = value;
  }
}
const pencil = new StockItem("Pencil", 10);
pencil.setQuantity(12);
console.log(pencil.quantity);
```

### Expected Behavior or Output
The output is 12. A negative or fractional quantity throws RangeError.

### Common Mistakes
- Changing state without validation.
- Assuming a private field is accessible outside its class.
- Allowing negative quantities.

### Activities
1. Update Pencil quantity to 12.
2. Try a negative quantity and inspect the error.
3. Explain the difference between a property and a method.

### Accessibility Practice
Use explicit validation messages and one state change per operation. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define methods and fields.
- [ ] I can protect state with private fields.
- [ ] I can validate state updates.

---

## Lesson 7.4: Inheritance

### Reading References
- Python source counterpart: Unit 7 lesson 7.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create a specialized item class that extends a base class.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Inheritance models an is-a relationship. A subclass uses extends and calls super before accessing this. Use inheritance only when the subtype genuinely satisfies the base contract.

### Worked Example
```typescript
class Item {
  constructor(public name: string, public quantity: number) {}
}
class PerishableItem extends Item {
  constructor(name: string, quantity: number, public expiresOn: string) {
    super(name, quantity);
  }
  describe(): string { return `${this.name}: ${this.quantity} in stock, expires ${this.expiresOn}`; }
}
console.log(new PerishableItem("Milk", 2, "2026-11-10").describe());
```

### Expected Behavior or Output
The output is `Milk: 2 in stock, expires 2026-11-10`.

### Common Mistakes
- Forgetting to call super before using this.
- Extending a class only to reuse unrelated code.
- Changing a subclass method so it violates the base contract.

### Activities
1. Create a PerishableItem.
2. Override or add a method with a clear contract.
3. Compare inheritance with composition.

### Accessibility Practice
Use a descriptive sentence for the specialized instance. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can extend a base class.
- [ ] I can call super in a constructor.
- [ ] I can explain when inheritance is appropriate.

---

## Lesson 7.5: Composition: instances as attributes

### Reading References
- Python source counterpart: Unit 7 lesson 7.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Build a record from related objects using composition.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Composition models a has-a relationship. A class stores another object as a property rather than inheriting its behavior. This often keeps responsibilities smaller.

### Worked Example
```typescript
class Course {
  constructor(public title: string) {}
}
class StudentRecord {
  constructor(public student: Student, public course: Course) {}
  describe(): string { return `${this.student.name} studies ${this.course.title}.`; }
}
const record = new StudentRecord(new Student("Avery", 16, "Computer Science"), new Course("Computer Science"));
console.log(record.describe());
```

### Expected Behavior or Output
The output is `Avery studies Computer Science.`

### Common Mistakes
- Using inheritance for a has-a relationship.
- Creating tightly coupled classes with unclear responsibilities.
- Duplicating data already stored in a related object.

### Activities
1. Create a StudentRecord containing a Student and Course.
2. Add a method that describes the relationship.
3. Draw a text outline of the object relationships.

### Accessibility Practice
Explain object relationships in words before reading nested property access. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model a has-a relationship.
- [ ] I can compose objects from instances.
- [ ] I can distinguish composition from inheritance.

---


# Unit 8: Files and Exceptions

## Overview

Read and write files, handle errors, and persist validated JSON. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 8.1: Reading from a file

### Reading References
- Python source counterpart: Unit 8 lesson 8.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Read a line-oriented notes file with the promise-based file system API.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The node:fs/promises API returns Promises. `readFile` with UTF-8 encoding returns a string. Await file operations and handle missing-file errors explicitly.

### Worked Example
```typescript
import { readFile } from "node:fs/promises";
async function main(): Promise<void> {
  const content = await readFile("notes.txt", "utf8");
  console.log("File contents:");
  console.log(content);
}
void main();
```

### Expected Behavior or Output
With the sample file containing two notes, both lines appear after `File contents:`.

### Common Mistakes
- Reading from the wrong working directory.
- Forgetting await and logging a Promise.
- Assuming a file exists without handling ENOENT.

### Activities
1. Create notes.txt with two lines.
2. Read and print the file contents.
3. Run from a different working directory and diagnose the path.

### Accessibility Practice
Print a label before file contents and explain the working directory. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can read a UTF-8 text file.
- [ ] I can await an asynchronous operation.
- [ ] I can identify the current working directory.

---

## Lesson 8.2: Writing to a file

### Reading References
- Python source counterpart: Unit 8 lesson 8.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create and append to the same notes file using promise-based file operations.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
`writeFile` creates or replaces content; `appendFile` adds content. Await each operation so writes happen in the intended order.

### Worked Example
```typescript
import { writeFile, appendFile, readFile } from "node:fs/promises";
async function main(): Promise<void> {
  await writeFile("notes.txt", "Review arrays\n", "utf8");
  await appendFile("notes.txt", "Practice typed functions\n", "utf8");
  console.log(await readFile("notes.txt", "utf8"));
}
void main();
```

### Expected Behavior or Output
The file contains `Review arrays` followed by `Practice typed functions`, each on its own line.

### Common Mistakes
- Using writeFile when existing content must be preserved.
- Not awaiting a write before reading the file.
- Writing to an unexpected path.

### Activities
1. Create a new notes file.
2. Append a second line.
3. Read the file and verify both lines and their order.

### Accessibility Practice
Announce whether an operation creates, replaces, appends, or reads data. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can write a UTF-8 file.
- [ ] I can append without replacing existing text.
- [ ] I can sequence asynchronous file operations.

---

## Lesson 8.3: Exceptions and error handling

### Reading References
- Python source counterpart: Unit 8 lesson 8.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Handle expected file and validation errors with try/catch.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An exception interrupts normal control flow. Catch expected failures and inspect unknown error values safely; do not assume every thrown value is an Error instance.

### Worked Example
```typescript
function validateAge(age: number): void {
  if (!Number.isInteger(age) || age < 0 || age > 120) {
    throw new RangeError("Age must be a whole number from 0 to 120.");
  }
}
try {
  validateAge(16);
  console.log("Age accepted.");
  validateAge(-1);
} catch (error: unknown) {
  if (error instanceof Error) console.log(error.message);
}
```

### Expected Behavior or Output
The program prints `Age accepted.` followed by the validation message.

### Common Mistakes
- Catching every error and silently ignoring it.
- Typing catch values as any.
- Using exceptions for ordinary expected branching.

### Activities
1. Test a valid age.
2. Test -1 and 121.
3. Handle a missing file separately from malformed file contents.

### Accessibility Practice
Use explicit error messages that identify the invalid field and recovery action. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can throw a validation error.
- [ ] I can catch unknown errors safely.
- [ ] I can distinguish expected failures.

---

## Lesson 8.4: The else and finally patterns

### Reading References
- Python source counterpart: Unit 8 lesson 8.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Separate successful operations from cleanup that must always occur.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
JavaScript has no try-else clause. Put success-only work after a successful try operation and use finally for cleanup. A finally block runs whether the try succeeds or fails.

### Worked Example
```typescript
async function loadMessage(): Promise<void> {
  let loaded = false;
  try {
    const message = "Notes loaded.";
    console.log(message);
    loaded = true;
  } catch (error: unknown) {
    console.log("Unable to load notes.");
  } finally {
    console.log("Load attempt finished.");
  }
  if (loaded) console.log("Ready to continue.");
}
void loadMessage();
```

### Expected Behavior or Output
On success, the program prints Notes loaded, Load attempt finished, and Ready to continue. On failure, the final status still prints.

### Common Mistakes
- Putting success-only code in finally.
- Assuming TypeScript has Python's try-else syntax.
- Returning from finally and accidentally overriding an earlier result.

### Activities
1. Trace success and failure paths.
2. Move the success message outside the try block.
3. Explain which cleanup must always run.

### Accessibility Practice
Label success, failure, and finalization messages distinctly. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model success and failure paths.
- [ ] I can use finally for cleanup.
- [ ] I can explain the absence of a try-else clause.

---

## Lesson 8.5: Storing structured data with JSON

### Reading References
- Python source counterpart: Unit 8 lesson 8.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Serialize typed records and validate parsed JSON before use.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
JSON.parse returns untrusted runtime data. A TypeScript assertion does not validate its shape. Parse into unknown and use a type guard before treating it as a record.

### Worked Example
```typescript
interface Task { id: number; title: string; done: boolean }
function isTask(value: unknown): value is Task {
  return typeof value === "object" && value !== null &&
    "id" in value && typeof value.id === "number" &&
    "title" in value && typeof value.title === "string" &&
    "done" in value && typeof value.done === "boolean";
}
const encoded = JSON.stringify({ id: 1, title: "Review arrays", done: false });
const parsed: unknown = JSON.parse(encoded);
if (isTask(parsed)) console.log(`${parsed.id}: ${parsed.title}`);
```

### Expected Behavior or Output
The program prints `1: Review arrays` only after validating the parsed object.

### Common Mistakes
- Using `as Task` as if it checked runtime data.
- Assuming JSON.parse cannot fail.
- Failing to validate each required field.

### Activities
1. Serialize a task object.
2. Parse it as unknown and validate it.
3. Test missing fields and wrong field types.

### Accessibility Practice
Print field names and validation errors as text. Never rely on color-only success indicators. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can serialize an object to JSON.
- [ ] I can parse JSON as unknown.
- [ ] I can validate external data with a type guard.

---


# Unit 9: Testing and Data Analysis

## Overview

Test functions and classes, generate random values, analyze text, and parse CSV. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

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


# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

Design, build, and refine equivalent command-line projects. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 10.1: Designing a text-based project

### Reading References
- Python source counterpart: Unit 10 lesson 10.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Plan requirements, data structures, commands, and acceptance tests before implementation.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Top-down design decomposes a project into smaller responsibilities. For an accessible terminal project, define prompts, commands, textual feedback, invalid-input behavior, and a quit path before coding.

### Worked Example
```typescript
const requirements = ["list rooms", "move by direction", "take item", "view inventory", "quit"];
for (const requirement of requirements) console.log(`Requirement: ${requirement}`);
```

### Expected Behavior or Output
Five requirements are printed in a stable order.

### Common Mistakes
- Starting implementation before writing acceptance criteria.
- Designing a visual-only interaction for a text-based project.
- Omitting error and quit behavior.

### Activities
1. Write the project requirements in plain language.
2. Identify input, state, and output for each command.
3. Write at least five acceptance tests before implementation.

### Accessibility Practice
Use a numbered text specification and test keyboard-only interaction. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can decompose a project.
- [ ] I can define commands and data.
- [ ] I can write acceptance tests before coding.

---

## Lesson 10.2: Text adventure part 1: rooms and movement

### Reading References
- Python source counterpart: Unit 10 lesson 10.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Model the shared cave, tunnel, and clearing with typed exits and movement.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A room has an identifier, description, and exits. A movement operation changes the current room only when the requested exit exists. A Record type can model a fixed set of room identifiers.

### Worked Example
```typescript
type RoomId = "cave" | "tunnel" | "clearing";
const exits: Record<RoomId, Partial<Record<string, RoomId>>> = {
  cave: { north: "tunnel" },
  tunnel: { south: "cave", east: "clearing" },
  clearing: { west: "tunnel" }
};
function move(room: RoomId, direction: string): RoomId | null {
  return exits[room][direction.toLowerCase()] ?? null;
}
console.log(move("cave", "north"));
console.log(move("cave", "west"));
```

### Expected Behavior or Output
Moving north from cave returns tunnel; moving west returns null.

### Common Mistakes
- Allowing movement through an exit that is not defined.
- Changing the room before validating the direction.
- Using arbitrary strings where a RoomId union is safer.

### Activities
1. Create all three rooms and exits.
2. Move north from cave and east from tunnel.
3. Attempt an invalid direction and report the result.

### Accessibility Practice
Announce current room and available exits as labeled text. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model rooms and exits.
- [ ] I can use a union type for room identifiers.
- [ ] I can validate movement.

---

## Lesson 10.3: Text adventure part 2: items, inventory, and puzzle

### Reading References
- Python source counterpart: Unit 10 lesson 10.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement item pickup and the shared magic-key puzzle.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An item moves from one room to inventory as one state transition. The player can take the torch in the cave and the magic key in the clearing; the key unlocks the gate.

### Worked Example
```typescript
const roomItems: Record<string, string[]> = { cave: ["torch"], tunnel: [], clearing: ["magic key"] };
const inventory: string[] = [];
function takeItem(room: string, item: string): boolean {
  const items = roomItems[room] ?? [];
  const index = items.findIndex(value => value.toLowerCase() === item.toLowerCase());
  if (index < 0) return false;
  inventory.push(items.splice(index, 1)[0]);
  return true;
}
function unlockGate(items: readonly string[]): string {
  return items.includes("magic key") ? "The gate opens." : "The gate is locked.";
}
console.log(takeItem("cave", "torch"));
console.log(inventory.join(", "));
console.log(unlockGate(["torch"]));
console.log(unlockGate(["torch", "magic key"]));
```

### Expected Behavior or Output
Output is true, torch, The gate is locked., and The gate opens.

### Common Mistakes
- Allowing the same item to be collected repeatedly.
- Updating inventory without removing the room item.
- Checking for the wrong key name or case.

### Activities
1. Take the torch from the cave.
2. Take the magic key from the clearing.
3. Test the gate with and without the key.

### Accessibility Practice
Confirm each pickup by item name and state whether the puzzle is locked or open. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can transfer an item into inventory.
- [ ] I can prevent duplicate pickup.
- [ ] I can implement the magic-key puzzle.

---

## Lesson 10.4: Developing a command-line to-do tool

### Reading References
- Python source counterpart: Unit 10 lesson 10.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement add, view, complete, delete, and quit operations with typed tasks.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A task has an id, title, description, done state, and creation timestamp. User-facing task numbers are one-based; array indexes are zero-based. Persist after every state-changing operation.

### Worked Example
```typescript
interface Todo { id: number; title: string; description: string; done: boolean; created_at: string }
const tasks: Todo[] = [];
function addTask(title: string, description: string): Todo {
  const task: Todo = { id: tasks.length + 1, title, description, done: false, created_at: new Date().toISOString() };
  tasks.push(task);
  return task;
}
console.log(addTask("Review arrays", "Practice typed collection methods").done);
```

### Expected Behavior or Output
A new task is added with done false and an ISO timestamp.

### Common Mistakes
- Using an array index as a permanent identifier.
- Failing to save after a state change.
- Accepting a blank task title.

### Activities
1. Add a task and view it.
2. Mark a task complete and delete another.
3. Persist and reload the task array as JSON.

### Accessibility Practice
Use one task per output block with field labels and a clear confirmation. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model a typed task.
- [ ] I can implement task creation.
- [ ] I can identify persistence points.

---

## Lesson 10.5: Refinement and accessible text user experience

### Reading References
- Python source counterpart: Unit 10 lesson 10.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Improve validation, prompts, error messages, and recovery paths.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A usable terminal interface has explicit prompts, predictable output, help text, and recoverable errors. A robust program validates untrusted values before changing state.

### Worked Example
```typescript
function normalizeCommand(input: string): string {
  return input.trim().toLowerCase();
}
function validateTitle(input: string): string | null {
  const title = input.trim();
  return title.length === 0 ? "Title cannot be blank." : null;
}
console.log(normalizeCommand("  VIEW "));
console.log(validateTitle("   "));
```

### Expected Behavior or Output
The output is view and Title cannot be blank.

### Common Mistakes
- Providing vague messages such as invalid input without a recovery hint.
- Using color as the only status indicator.
- Failing to test blank input, unknown commands, and empty collections.

### Activities
1. Add a help command.
2. Test blank, malformed, and unknown commands.
3. Review every message in sequential screen-reader output.

### Accessibility Practice
Provide text equivalents for every status and avoid cursor-position-dependent instructions. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can normalize command input.
- [ ] I can validate required fields.
- [ ] I can review a text interface for accessibility.

---


# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

Integrate typed records, terminal interaction, persistence, CRUD, testing, and accessibility. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 11.1: Capstone interface and requirements

### Reading References
- Python source counterpart: Unit 11 lesson 11.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Plan an accessible terminal interface for the personal data manager.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The Python source uses NiceGUI, but the TypeScript track uses a terminal interface to preserve the same user-facing requirements without requiring browser UI. Commands include list, add, search, update, delete, help, and quit.

### Worked Example
```typescript
const commands = ["list", "add", "search", "update", "delete", "help", "quit"];
console.log(commands.join(", "));
```

### Expected Behavior or Output
The command list contains all seven required operations.

### Common Mistakes
- Copying a GUI-specific implementation when the language track requires an accessible alternative.
- Omitting a help or quit command.
- Designing commands without defining expected output.

### Activities
1. Choose a terminal command syntax.
2. Write a help response for every command.
3. Define keyboard-only acceptance tests.

### Accessibility Practice
Specify prompt order and output as linear text. Do not require mouse use. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can explain the language-specific interface adaptation.
- [ ] I can define the required commands.
- [ ] I can create accessibility acceptance tests.

---

## Lesson 11.2: Capstone data model and JSON storage

### Reading References
- Python source counterpart: Unit 11 lesson 11.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Define the shared record schema and save/load records safely.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Each record has id, title, description, category, created_at, and updated_at. TypeScript interfaces describe the expected shape, but JSON input must be validated at runtime.

### Worked Example
```typescript
interface DataRecord { id: number; title: string; description: string; category: string; created_at: string; updated_at: string }
const record: DataRecord = { id: 1, title: "Course notes", description: "Review arrays", category: "Study", created_at: "2026-11-01T10:00:00.000Z", updated_at: "2026-11-01T10:00:00.000Z" };
const serialized = JSON.stringify([record], null, 2);
console.log(serialized.includes("Course notes"));
```

### Expected Behavior or Output
The check prints true and the JSON contains all six fields.

### Common Mistakes
- Using a type assertion instead of validating loaded JSON.
- Reusing record identifiers.
- Overwriting valid data after a parse failure without reporting it.

### Activities
1. Define the six-field interface.
2. Serialize one record and inspect the JSON.
3. Load and validate records before using them.

### Accessibility Practice
Read the schema field by field and keep timestamps in a consistent ISO format. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define the capstone record interface.
- [ ] I can serialize structured data.
- [ ] I can explain runtime validation of stored JSON.

---

## Lesson 11.3: Capstone list and display operations

### Reading References
- Python source counterpart: Unit 11 lesson 11.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Display records in a stable, labeled, sequential format.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Listing is a read operation and should not mutate data. Stable identifiers are distinct from temporary one-based display positions.

### Worked Example
```typescript
const records = [{ id: 7, title: "Course notes", category: "Study", done: false }];
for (const [index, record] of records.entries()) {
  console.log(`Item ${index + 1}`);
  console.log(`ID: ${record.id}`);
  console.log(`Title: ${record.title}`);
  console.log(`Category: ${record.category}`);
  console.log(`Done: ${record.done}`);
}
```

### Expected Behavior or Output
The record is displayed as Item 1 with ID 7 and its labeled fields.

### Common Mistakes
- Using the displayed list number as the permanent ID.
- Omitting labels and making output ambiguous.
- Failing to handle an empty collection.

### Activities
1. Display one record.
2. Display multiple records.
3. Display an empty list with a clear message.

### Accessibility Practice
Use stable labels and one field per line for sequential reading. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can display records with labels.
- [ ] I can distinguish display position from record ID.
- [ ] I can handle an empty collection.

---

## Lesson 11.4: Capstone add, search, and update operations

### Reading References
- Python source counterpart: Unit 11 lesson 11.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement creation, case-insensitive search, and safe record updates.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Create, search, and update are separate operations. Update only permitted fields and refresh updated_at. Search should not change stored records.

### Worked Example
```typescript
interface Entry { id: number; title: string; description: string; updated_at: string }
function search(entries: readonly Entry[], query: string): Entry[] {
  const term = query.trim().toLowerCase();
  return entries.filter(entry => `${entry.title} ${entry.description}`.toLowerCase().includes(term));
}
const entries: Entry[] = [{ id: 1, title: "Course notes", description: "Review arrays", updated_at: "2026-11-01T10:00:00.000Z" }];
console.log(search(entries, "ARRAYS").length);
```

### Expected Behavior or Output
The search returns one matching record.

### Common Mistakes
- Searching case-sensitively without documenting that choice.
- Allowing edits to immutable identifiers.
- Forgetting to refresh updated_at after an edit.

### Activities
1. Add a record with all required fields.
2. Search by title and description.
3. Update a title and verify the timestamp changes.

### Accessibility Practice
Confirm each successful action by record ID and field name. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can add a valid record.
- [ ] I can search without mutating records.
- [ ] I can update permitted fields and timestamps.

---

## Lesson 11.5: Capstone delete, completion, and final verification

### Reading References
- Python source counterpart: Unit 11 lesson 11.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement delete and completion behavior and verify persistence and accessibility.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Deletion removes a selected record by stable ID. Completion updates the record state. The capstone should have tests for CRUD behavior, JSON persistence, invalid input, and empty data.

### Worked Example
```typescript
interface TaskRecord { id: number; title: string; done: boolean }
function markDone(records: TaskRecord[], id: number): boolean {
  const record = records.find(item => item.id === id);
  if (!record) return false;
  record.done = true;
  return true;
}
const records: TaskRecord[] = [{ id: 4, title: "Test persistence", done: false }];
console.log(markDone(records, 4));
console.log(records[0].done);
```

### Expected Behavior or Output
The function returns true and the record's done field becomes true.

### Common Mistakes
- Deleting by a stale array index.
- Failing to save after a mutation.
- Testing only the successful path.

### Activities
1. Delete a record by ID and verify it remains absent after reload.
2. Mark a record complete and test missing IDs.
3. Run at least five tests covering CRUD, persistence, and validation.

### Accessibility Practice
Verify keyboard-only use, help text, confirmations, errors, and sequential output with the intended access technology. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can delete by stable identifier.
- [ ] I can update completion state.
- [ ] I can plan end-to-end and accessibility tests.

---


# Unit 8: Files and Exceptions

## Overview

Read and write files, handle errors, and persist validated JSON. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 8.1: Reading from a file

### Reading References
- Python source counterpart: Unit 8 lesson 8.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Read a line-oriented notes file with the promise-based file system API.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The node:fs/promises API returns Promises. `readFile` with UTF-8 encoding returns a string. Await file operations and handle missing-file errors explicitly.

### Worked Example
```typescript
import { readFile } from "node:fs/promises";
async function main(): Promise<void> {
  const content = await readFile("notes.txt", "utf8");
  console.log("File contents:");
  console.log(content);
}
void main();
```

### Expected Behavior or Output
With the sample file containing two notes, both lines appear after `File contents:`.

### Common Mistakes
- Reading from the wrong working directory.
- Forgetting await and logging a Promise.
- Assuming a file exists without handling ENOENT.

### Activities
1. Create notes.txt with two lines.
2. Read and print the file contents.
3. Run from a different working directory and diagnose the path.

### Accessibility Practice
Print a label before file contents and explain the working directory. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can read a UTF-8 text file.
- [ ] I can await an asynchronous operation.
- [ ] I can identify the current working directory.

---

## Lesson 8.2: Writing to a file

### Reading References
- Python source counterpart: Unit 8 lesson 8.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create and append to the same notes file using promise-based file operations.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
`writeFile` creates or replaces content; `appendFile` adds content. Await each operation so writes happen in the intended order.

### Worked Example
```typescript
import { writeFile, appendFile, readFile } from "node:fs/promises";
async function main(): Promise<void> {
  await writeFile("notes.txt", "Review arrays\n", "utf8");
  await appendFile("notes.txt", "Practice typed functions\n", "utf8");
  console.log(await readFile("notes.txt", "utf8"));
}
void main();
```

### Expected Behavior or Output
The file contains `Review arrays` followed by `Practice typed functions`, each on its own line.

### Common Mistakes
- Using writeFile when existing content must be preserved.
- Not awaiting a write before reading the file.
- Writing to an unexpected path.

### Activities
1. Create a new notes file.
2. Append a second line.
3. Read the file and verify both lines and their order.

### Accessibility Practice
Announce whether an operation creates, replaces, appends, or reads data. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can write a UTF-8 file.
- [ ] I can append without replacing existing text.
- [ ] I can sequence asynchronous file operations.

---

## Lesson 8.3: Exceptions and error handling

### Reading References
- Python source counterpart: Unit 8 lesson 8.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Handle expected file and validation errors with try/catch.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An exception interrupts normal control flow. Catch expected failures and inspect unknown error values safely; do not assume every thrown value is an Error instance.

### Worked Example
```typescript
function validateAge(age: number): void {
  if (!Number.isInteger(age) || age < 0 || age > 120) {
    throw new RangeError("Age must be a whole number from 0 to 120.");
  }
}
try {
  validateAge(16);
  console.log("Age accepted.");
  validateAge(-1);
} catch (error: unknown) {
  if (error instanceof Error) console.log(error.message);
}
```

### Expected Behavior or Output
The program prints `Age accepted.` followed by the validation message.

### Common Mistakes
- Catching every error and silently ignoring it.
- Typing catch values as any.
- Using exceptions for ordinary expected branching.

### Activities
1. Test a valid age.
2. Test -1 and 121.
3. Handle a missing file separately from malformed file contents.

### Accessibility Practice
Use explicit error messages that identify the invalid field and recovery action. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can throw a validation error.
- [ ] I can catch unknown errors safely.
- [ ] I can distinguish expected failures.

---

## Lesson 8.4: The else and finally patterns

### Reading References
- Python source counterpart: Unit 8 lesson 8.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Separate successful operations from cleanup that must always occur.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
JavaScript has no try-else clause. Put success-only work after a successful try operation and use finally for cleanup. A finally block runs whether the try succeeds or fails.

### Worked Example
```typescript
async function loadMessage(): Promise<void> {
  let loaded = false;
  try {
    const message = "Notes loaded.";
    console.log(message);
    loaded = true;
  } catch (error: unknown) {
    console.log("Unable to load notes.");
  } finally {
    console.log("Load attempt finished.");
  }
  if (loaded) console.log("Ready to continue.");
}
void loadMessage();
```

### Expected Behavior or Output
On success, the program prints Notes loaded, Load attempt finished, and Ready to continue. On failure, the final status still prints.

### Common Mistakes
- Putting success-only code in finally.
- Assuming TypeScript has Python's try-else syntax.
- Returning from finally and accidentally overriding an earlier result.

### Activities
1. Trace success and failure paths.
2. Move the success message outside the try block.
3. Explain which cleanup must always run.

### Accessibility Practice
Label success, failure, and finalization messages distinctly. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model success and failure paths.
- [ ] I can use finally for cleanup.
- [ ] I can explain the absence of a try-else clause.

---

## Lesson 8.5: Storing structured data with JSON

### Reading References
- Python source counterpart: Unit 8 lesson 8.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Serialize typed records and validate parsed JSON before use.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
JSON.parse returns untrusted runtime data. A TypeScript assertion does not validate its shape. Parse into unknown and use a type guard before treating it as a record.

### Worked Example
```typescript
interface Task { id: number; title: string; done: boolean }
function isTask(value: unknown): value is Task {
  return typeof value === "object" && value !== null &&
    "id" in value && typeof value.id === "number" &&
    "title" in value && typeof value.title === "string" &&
    "done" in value && typeof value.done === "boolean";
}
const encoded = JSON.stringify({ id: 1, title: "Review arrays", done: false });
const parsed: unknown = JSON.parse(encoded);
if (isTask(parsed)) console.log(`${parsed.id}: ${parsed.title}`);
```

### Expected Behavior or Output
The program prints `1: Review arrays` only after validating the parsed object.

### Common Mistakes
- Using `as Task` as if it checked runtime data.
- Assuming JSON.parse cannot fail.
- Failing to validate each required field.

### Activities
1. Serialize a task object.
2. Parse it as unknown and validate it.
3. Test missing fields and wrong field types.

### Accessibility Practice
Print field names and validation errors as text. Never rely on color-only success indicators. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can serialize an object to JSON.
- [ ] I can parse JSON as unknown.
- [ ] I can validate external data with a type guard.

---


# Unit 9: Testing and Data Analysis

## Overview

Test functions and classes, generate random values, analyze text, and parse CSV. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

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


# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

Design, build, and refine equivalent command-line projects. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 10.1: Designing a text-based project

### Reading References
- Python source counterpart: Unit 10 lesson 10.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Plan requirements, data structures, commands, and acceptance tests before implementation.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Top-down design decomposes a project into smaller responsibilities. For an accessible terminal project, define prompts, commands, textual feedback, invalid-input behavior, and a quit path before coding.

### Worked Example
```typescript
const requirements = ["list rooms", "move by direction", "take item", "view inventory", "quit"];
for (const requirement of requirements) console.log(`Requirement: ${requirement}`);
```

### Expected Behavior or Output
Five requirements are printed in a stable order.

### Common Mistakes
- Starting implementation before writing acceptance criteria.
- Designing a visual-only interaction for a text-based project.
- Omitting error and quit behavior.

### Activities
1. Write the project requirements in plain language.
2. Identify input, state, and output for each command.
3. Write at least five acceptance tests before implementation.

### Accessibility Practice
Use a numbered text specification and test keyboard-only interaction. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can decompose a project.
- [ ] I can define commands and data.
- [ ] I can write acceptance tests before coding.

---

## Lesson 10.2: Text adventure part 1: rooms and movement

### Reading References
- Python source counterpart: Unit 10 lesson 10.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Model the shared cave, tunnel, and clearing with typed exits and movement.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A room has an identifier, description, and exits. A movement operation changes the current room only when the requested exit exists. A Record type can model a fixed set of room identifiers.

### Worked Example
```typescript
type RoomId = "cave" | "tunnel" | "clearing";
const exits: Record<RoomId, Partial<Record<string, RoomId>>> = {
  cave: { north: "tunnel" },
  tunnel: { south: "cave", east: "clearing" },
  clearing: { west: "tunnel" }
};
function move(room: RoomId, direction: string): RoomId | null {
  return exits[room][direction.toLowerCase()] ?? null;
}
console.log(move("cave", "north"));
console.log(move("cave", "west"));
```

### Expected Behavior or Output
Moving north from cave returns tunnel; moving west returns null.

### Common Mistakes
- Allowing movement through an exit that is not defined.
- Changing the room before validating the direction.
- Using arbitrary strings where a RoomId union is safer.

### Activities
1. Create all three rooms and exits.
2. Move north from cave and east from tunnel.
3. Attempt an invalid direction and report the result.

### Accessibility Practice
Announce current room and available exits as labeled text. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model rooms and exits.
- [ ] I can use a union type for room identifiers.
- [ ] I can validate movement.

---

## Lesson 10.3: Text adventure part 2: items, inventory, and puzzle

### Reading References
- Python source counterpart: Unit 10 lesson 10.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement item pickup and the shared magic-key puzzle.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An item moves from one room to inventory as one state transition. The player can take the torch in the cave and the magic key in the clearing; the key unlocks the gate.

### Worked Example
```typescript
const roomItems: Record<string, string[]> = { cave: ["torch"], tunnel: [], clearing: ["magic key"] };
const inventory: string[] = [];
function takeItem(room: string, item: string): boolean {
  const items = roomItems[room] ?? [];
  const index = items.findIndex(value => value.toLowerCase() === item.toLowerCase());
  if (index < 0) return false;
  inventory.push(items.splice(index, 1)[0]);
  return true;
}
function unlockGate(items: readonly string[]): string {
  return items.includes("magic key") ? "The gate opens." : "The gate is locked.";
}
console.log(takeItem("cave", "torch"));
console.log(inventory.join(", "));
console.log(unlockGate(["torch"]));
console.log(unlockGate(["torch", "magic key"]));
```

### Expected Behavior or Output
Output is true, torch, The gate is locked., and The gate opens.

### Common Mistakes
- Allowing the same item to be collected repeatedly.
- Updating inventory without removing the room item.
- Checking for the wrong key name or case.

### Activities
1. Take the torch from the cave.
2. Take the magic key from the clearing.
3. Test the gate with and without the key.

### Accessibility Practice
Confirm each pickup by item name and state whether the puzzle is locked or open. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can transfer an item into inventory.
- [ ] I can prevent duplicate pickup.
- [ ] I can implement the magic-key puzzle.

---

## Lesson 10.4: Developing a command-line to-do tool

### Reading References
- Python source counterpart: Unit 10 lesson 10.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement add, view, complete, delete, and quit operations with typed tasks.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A task has an id, title, description, done state, and creation timestamp. User-facing task numbers are one-based; array indexes are zero-based. Persist after every state-changing operation.

### Worked Example
```typescript
interface Todo { id: number; title: string; description: string; done: boolean; created_at: string }
const tasks: Todo[] = [];
function addTask(title: string, description: string): Todo {
  const task: Todo = { id: tasks.length + 1, title, description, done: false, created_at: new Date().toISOString() };
  tasks.push(task);
  return task;
}
console.log(addTask("Review arrays", "Practice typed collection methods").done);
```

### Expected Behavior or Output
A new task is added with done false and an ISO timestamp.

### Common Mistakes
- Using an array index as a permanent identifier.
- Failing to save after a state change.
- Accepting a blank task title.

### Activities
1. Add a task and view it.
2. Mark a task complete and delete another.
3. Persist and reload the task array as JSON.

### Accessibility Practice
Use one task per output block with field labels and a clear confirmation. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model a typed task.
- [ ] I can implement task creation.
- [ ] I can identify persistence points.

---

## Lesson 10.5: Refinement and accessible text user experience

### Reading References
- Python source counterpart: Unit 10 lesson 10.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Improve validation, prompts, error messages, and recovery paths.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A usable terminal interface has explicit prompts, predictable output, help text, and recoverable errors. A robust program validates untrusted values before changing state.

### Worked Example
```typescript
function normalizeCommand(input: string): string {
  return input.trim().toLowerCase();
}
function validateTitle(input: string): string | null {
  const title = input.trim();
  return title.length === 0 ? "Title cannot be blank." : null;
}
console.log(normalizeCommand("  VIEW "));
console.log(validateTitle("   "));
```

### Expected Behavior or Output
The output is view and Title cannot be blank.

### Common Mistakes
- Providing vague messages such as invalid input without a recovery hint.
- Using color as the only status indicator.
- Failing to test blank input, unknown commands, and empty collections.

### Activities
1. Add a help command.
2. Test blank, malformed, and unknown commands.
3. Review every message in sequential screen-reader output.

### Accessibility Practice
Provide text equivalents for every status and avoid cursor-position-dependent instructions. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can normalize command input.
- [ ] I can validate required fields.
- [ ] I can review a text interface for accessibility.

---


# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

Integrate typed records, terminal interaction, persistence, CRUD, testing, and accessibility. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 11.1: Capstone interface and requirements

### Reading References
- Python source counterpart: Unit 11 lesson 11.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Plan an accessible terminal interface for the personal data manager.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The Python source uses NiceGUI, but the TypeScript track uses a terminal interface to preserve the same user-facing requirements without requiring browser UI. Commands include list, add, search, update, delete, help, and quit.

### Worked Example
```typescript
const commands = ["list", "add", "search", "update", "delete", "help", "quit"];
console.log(commands.join(", "));
```

### Expected Behavior or Output
The command list contains all seven required operations.

### Common Mistakes
- Copying a GUI-specific implementation when the language track requires an accessible alternative.
- Omitting a help or quit command.
- Designing commands without defining expected output.

### Activities
1. Choose a terminal command syntax.
2. Write a help response for every command.
3. Define keyboard-only acceptance tests.

### Accessibility Practice
Specify prompt order and output as linear text. Do not require mouse use. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can explain the language-specific interface adaptation.
- [ ] I can define the required commands.
- [ ] I can create accessibility acceptance tests.

---

## Lesson 11.2: Capstone data model and JSON storage

### Reading References
- Python source counterpart: Unit 11 lesson 11.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Define the shared record schema and save/load records safely.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Each record has id, title, description, category, created_at, and updated_at. TypeScript interfaces describe the expected shape, but JSON input must be validated at runtime.

### Worked Example
```typescript
interface DataRecord { id: number; title: string; description: string; category: string; created_at: string; updated_at: string }
const record: DataRecord = { id: 1, title: "Course notes", description: "Review arrays", category: "Study", created_at: "2026-11-01T10:00:00.000Z", updated_at: "2026-11-01T10:00:00.000Z" };
const serialized = JSON.stringify([record], null, 2);
console.log(serialized.includes("Course notes"));
```

### Expected Behavior or Output
The check prints true and the JSON contains all six fields.

### Common Mistakes
- Using a type assertion instead of validating loaded JSON.
- Reusing record identifiers.
- Overwriting valid data after a parse failure without reporting it.

### Activities
1. Define the six-field interface.
2. Serialize one record and inspect the JSON.
3. Load and validate records before using them.

### Accessibility Practice
Read the schema field by field and keep timestamps in a consistent ISO format. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define the capstone record interface.
- [ ] I can serialize structured data.
- [ ] I can explain runtime validation of stored JSON.

---

## Lesson 11.3: Capstone list and display operations

### Reading References
- Python source counterpart: Unit 11 lesson 11.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Display records in a stable, labeled, sequential format.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Listing is a read operation and should not mutate data. Stable identifiers are distinct from temporary one-based display positions.

### Worked Example
```typescript
const records = [{ id: 7, title: "Course notes", category: "Study", done: false }];
for (const [index, record] of records.entries()) {
  console.log(`Item ${index + 1}`);
  console.log(`ID: ${record.id}`);
  console.log(`Title: ${record.title}`);
  console.log(`Category: ${record.category}`);
  console.log(`Done: ${record.done}`);
}
```

### Expected Behavior or Output
The record is displayed as Item 1 with ID 7 and its labeled fields.

### Common Mistakes
- Using the displayed list number as the permanent ID.
- Omitting labels and making output ambiguous.
- Failing to handle an empty collection.

### Activities
1. Display one record.
2. Display multiple records.
3. Display an empty list with a clear message.

### Accessibility Practice
Use stable labels and one field per line for sequential reading. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can display records with labels.
- [ ] I can distinguish display position from record ID.
- [ ] I can handle an empty collection.

---

## Lesson 11.4: Capstone add, search, and update operations

### Reading References
- Python source counterpart: Unit 11 lesson 11.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement creation, case-insensitive search, and safe record updates.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Create, search, and update are separate operations. Update only permitted fields and refresh updated_at. Search should not change stored records.

### Worked Example
```typescript
interface Entry { id: number; title: string; description: string; updated_at: string }
function search(entries: readonly Entry[], query: string): Entry[] {
  const term = query.trim().toLowerCase();
  return entries.filter(entry => `${entry.title} ${entry.description}`.toLowerCase().includes(term));
}
const entries: Entry[] = [{ id: 1, title: "Course notes", description: "Review arrays", updated_at: "2026-11-01T10:00:00.000Z" }];
console.log(search(entries, "ARRAYS").length);
```

### Expected Behavior or Output
The search returns one matching record.

### Common Mistakes
- Searching case-sensitively without documenting that choice.
- Allowing edits to immutable identifiers.
- Forgetting to refresh updated_at after an edit.

### Activities
1. Add a record with all required fields.
2. Search by title and description.
3. Update a title and verify the timestamp changes.

### Accessibility Practice
Confirm each successful action by record ID and field name. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can add a valid record.
- [ ] I can search without mutating records.
- [ ] I can update permitted fields and timestamps.

---

## Lesson 11.5: Capstone delete, completion, and final verification

### Reading References
- Python source counterpart: Unit 11 lesson 11.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement delete and completion behavior and verify persistence and accessibility.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Deletion removes a selected record by stable ID. Completion updates the record state. The capstone should have tests for CRUD behavior, JSON persistence, invalid input, and empty data.

### Worked Example
```typescript
interface TaskRecord { id: number; title: string; done: boolean }
function markDone(records: TaskRecord[], id: number): boolean {
  const record = records.find(item => item.id === id);
  if (!record) return false;
  record.done = true;
  return true;
}
const records: TaskRecord[] = [{ id: 4, title: "Test persistence", done: false }];
console.log(markDone(records, 4));
console.log(records[0].done);
```

### Expected Behavior or Output
The function returns true and the record's done field becomes true.

### Common Mistakes
- Deleting by a stale array index.
- Failing to save after a mutation.
- Testing only the successful path.

### Activities
1. Delete a record by ID and verify it remains absent after reload.
2. Mark a record complete and test missing IDs.
3. Run at least five tests covering CRUD, persistence, and validation.

### Accessibility Practice
Verify keyboard-only use, help text, confirmations, errors, and sequential output with the intended access technology. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can delete by stable identifier.
- [ ] I can update completion state.
- [ ] I can plan end-to-end and accessibility tests.

---

