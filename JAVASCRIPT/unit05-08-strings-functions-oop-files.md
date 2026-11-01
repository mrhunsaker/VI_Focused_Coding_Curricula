# Units 5–8: Loops, Functions, Object-Oriented Programming, Files, and Exceptions

**Runtime baseline:** Node.js 26.x. Examples use built-in Node.js APIs and modern ECMAScript syntax.

# Unit 5: User Input and `while` Loops

## Overview
This unit builds on terminal input and introduces sentinel-controlled repetition, loop flags, `break`, and `continue`. The goal is to create predictable interactive programs with explicit stopping conditions.

## Lesson 5.1: How Terminal Input Works

### Reading References
- Python source counterpart: Unit 5, Lesson 5.1.
- Node.js documentation: `node:readline/promises`.

### Learning Objectives
- Explain why Node.js terminal input is asynchronous.
- Read, trim, and validate a text response.
- Close a readline interface reliably.

### Concept Explanation
Node.js does not provide a built-in synchronous `input()` function. Use `readline/promises` and `await question()` to obtain a response. The result is a string; conversion and validation are separate steps.

### Worked Example
```javascript
const readline = require("node:readline/promises");
const { stdin, stdout } = require("node:process");

async function main() {
  const rl = readline.createInterface({ input: stdin, output: stdout });
  try {
    const response = (await rl.question("Enter your favorite subject: ")).trim();
    if (response === "") {
      console.log("Error: a subject is required.");
    } else {
      console.log(`Favorite subject: ${response}`);
    }
  } finally {
    rl.close();
  }
}
main();
```

Example interaction:
```text
Enter your favorite subject: Computer Science
Favorite subject: Computer Science
```

### Common Mistakes
- Forgetting `await` before `question()`.
- Treating the response as a number without converting it.
- Failing to close the interface.
- Accepting an empty string when a nonempty response is required.

### Activities
1. Ask for the canonical student name Avery and print a greeting.
2. Ask for age, convert it with `Number()`, and reject blank or non-finite input.
3. Ask for a menu choice and normalize it with `trim()`.
4. Explain the purpose of `try/finally` around the readline interface.

### Accessibility Practice
Use descriptive prompts, announce validation errors in text, and keep the prompt sequence linear. All steps must work from the terminal without mouse interaction.

### Skills Checklist
- [ ] I can create a readline interface.
- [ ] I can await terminal input.
- [ ] I can validate and normalize text input.
- [ ] I can close the interface reliably.

## Lesson 5.2: The `while` Loop in Action

### Reading References
- Python source counterpart: Unit 5, Lesson 5.2.
- MDN: `while` statement.

### Learning Objectives
- Write a condition-controlled loop.
- Use a sentinel value to terminate repetition.
- Explain the difference between a `for` loop and a `while` loop.

### Concept Explanation
A `while` loop repeats as long as its condition is true. A sentinel is a special input value that signals completion. The loop must update state so its condition can eventually become false.

### Worked Example
```javascript
const scores = [82, 91, 76, 88];
let index = 0;
let total = 0;

while (index < scores.length) {
  total += scores[index];
  index += 1;
}

console.log(`Total: ${total}`);
console.log(`Average: ${(total / scores.length).toFixed(2)}`);
```

Expected output:
```text
Total: 337
Average: 84.25
```

### Common Mistakes
- Forgetting to increment the index.
- Using a condition that is already false before the first iteration.
- Updating the index after a branch that can skip the update.

### Activities
1. Count from 1 through 5 with a `while` loop.
2. Sum the canonical scores and calculate their average.
3. Design a sentinel-controlled menu that stops when the user enters "quit".
4. Trace the value of the loop index before and after each iteration.

### Accessibility Practice
State the loop condition and termination rule before running the program. Provide a textual completion message.

### Skills Checklist
- [ ] I can write a condition-controlled loop.
- [ ] I can use a sentinel to stop repetition.
- [ ] I can update loop state correctly.
- [ ] I can choose between `for` and `while`.

## Lesson 5.3: Using Flags and `break` to Exit Loops

### Reading References
- Python source counterpart: Unit 5, Lesson 5.3.
- MDN: `break` statement.

### Learning Objectives
- Use a Boolean flag to record a condition.
- Stop a loop early with `break`.
- Distinguish normal loop completion from early termination.

### Worked Example
```javascript
const scores = [82, 91, 76, 88];
let found = false;

for (const score of scores) {
  if (score > 90) {
    found = true;
    console.log(`First score above 90: ${score}`);
    break;
  }
}

if (!found) {
  console.log("No score above 90 was found.");
}
```

Expected output:
```text
First score above 90: 91
```

### Common Mistakes
- Using a string such as "false" instead of the Boolean value `false`.
- Forgetting to set the flag when the condition is met.
- Placing `break` outside a loop or switch statement.

### Activities
1. Search the canonical scores for the first score greater than 90.
2. Repeat the search for a score greater than 95 and report that none exists.
3. Use a flag to validate that a required inventory item exists.
4. Explain when `break` is clearer than changing the loop condition.

### Accessibility Practice
Report both the search result and whether a match was found. Do not rely on color or a visual marker.

### Skills Checklist
- [ ] I can initialize and update a Boolean flag.
- [ ] I can use `break` to stop a loop.
- [ ] I can report successful and unsuccessful searches.
- [ ] I can explain early termination.

## Lesson 5.4: Using `continue` in Loops

### Reading References
- Python source counterpart: Unit 5, Lesson 5.4.
- MDN: `continue` statement.

### Learning Objectives
- Skip the current iteration with `continue`.
- Validate data before processing it.
- Explain the difference between `continue` and `break`.

### Worked Example
```javascript
const entries = ["82", "", "91", "invalid", "76", "88"];
let total = 0;
let validCount = 0;

for (const entry of entries) {
  const score = Number(entry);
  if (entry.trim() === "" || !Number.isFinite(score)) {
    console.log("Skipping invalid score.");
    continue;
  }
  total += score;
  validCount += 1;
}

console.log(`Valid scores: ${validCount}`);
console.log(`Total: ${total}`);
```

Expected output:
```text
Skipping invalid score.
Skipping invalid score.
Valid scores: 4
Total: 337
```

### Common Mistakes
- Using `continue` when the entire loop should end.
- Skipping a loop-control update in a `while` loop.
- Failing to explain why an entry was skipped.

### Activities
1. Process the canonical scores while skipping negative values.
2. Add blank and nonnumeric entries and confirm they are rejected.
3. Count accepted and rejected entries separately.
4. Rewrite a short loop using `if/else` instead of `continue`; compare readability.

### Accessibility Practice
Print a concise reason for each rejected entry. Keep accepted and rejected counts explicit.

### Skills Checklist
- [ ] I can use `continue` to skip an iteration.
- [ ] I can validate data before processing.
- [ ] I can distinguish `continue` from `break`.
- [ ] I can report rejected input clearly.

## Lesson 5.5: Avoiding Infinite Loops

### Reading References
- Python source counterpart: Unit 5, Lesson 5.5.
- MDN: Loops and iteration.

### Learning Objectives
- Identify loop conditions that never become false.
- Trace and repair loop-control logic.
- Test both normal and boundary termination.

### Concept Explanation
An infinite loop occurs when the loop condition remains true indefinitely. Before execution, identify the variable that changes, the condition that ends the loop, and every path through the body. For interactive programs, include an explicit quit command.

### Worked Example
```javascript
let count = 1;
while (count <= 3) {
  console.log(`Count: ${count}`);
  count += 1;
}
console.log("Loop finished.");
```

Expected output:
```text
Count: 1
Count: 2
Count: 3
Loop finished.
```

### Common Mistakes
- Never changing a variable used in the condition.
- Incrementing in the wrong direction.
- Creating a path through the loop that bypasses the update.
- Testing only the normal path and not the stopping boundary.

### Activities
1. Trace the worked example by hand before running it.
2. Diagnose a loop that decrements a counter while testing whether it is less than 10.
3. Add a quit command to a menu loop.
4. Test the loop with its initial value already at the boundary.

### Accessibility Practice
Announce the expected maximum number of iterations for bounded examples. Stop runaway processes with the terminal interrupt command and describe the recovery procedure.

### Skills Checklist
- [ ] I can identify the termination condition.
- [ ] I can trace loop state changes.
- [ ] I can diagnose common infinite-loop causes.
- [ ] I can test loop boundary cases.

# Unit 6: Functions

## Overview
Functions support decomposition, reuse, and testing. JavaScript supports declarations, expressions, arrow functions, default parameters, rest parameters, and closures. Unlike Python, JavaScript does not support Python-style keyword arguments; use an options object when named configuration is useful.

## Lesson 6.1: Defining Functions

### Reading References
- Python source counterpart: Unit 6, Lesson 6.1.
- MDN: Functions.

### Learning Objectives
- Define and call a function.
- Explain parameters and function bodies.
- Choose a function declaration or expression.

### Worked Example
```javascript
function calculateTip(bill, rate) {
  return bill * rate;
}

const tip = calculateTip(24.50, 0.15);
console.log(`Tip: $${tip.toFixed(2)}`);
```

Expected output:
```text
Tip: $3.68
```

### Common Mistakes
- Calling a function before understanding its parameter order.
- Omitting `return` when the caller needs a result.
- Confusing a function definition with a function call.

### Activities
1. Define `calculateTip` using the canonical bill and tip rate.
2. Define a function that returns the average of the canonical scores.
3. Call each function with at least two different inputs.
4. Explain why returning a value is more reusable than printing inside the function.

### Accessibility Practice
Use descriptive function and parameter names. Read the function declaration, call, and returned result as separate steps.

### Skills Checklist
- [ ] I can define and call a function.
- [ ] I can identify parameters and arguments.
- [ ] I can return a computed value.
- [ ] I can use a function to reduce repeated code.

## Lesson 6.2: Passing Arguments

### Reading References
- Python source counterpart: Unit 6, Lesson 6.2.
- MDN: Function parameters.

### Learning Objectives
- Pass positional arguments in the correct order.
- Use default parameters.
- Use an options object to model named configuration.

### Concept Explanation
JavaScript arguments are positional. It does not have Python's `name=value` call syntax. For functions with several optional settings, pass one object whose properties describe each setting.

### Worked Example
```javascript
function calculateTotal(bill, tipRate = 0.15) {
  return bill + bill * tipRate;
}

function describeStudent({ name, age, favoriteSubject }) {
  return `${name}, age ${age}, studies ${favoriteSubject}.`;
}

console.log(calculateTotal(24.50).toFixed(2));
console.log(calculateTotal(24.50, 0.20).toFixed(2));
console.log(describeStudent({
  name: "Avery",
  age: 16,
  favoriteSubject: "Computer Science"
}));
```

Expected output:
```text
28.18
29.40
Avery, age 16, studies Computer Science.
```

### Common Mistakes
- Swapping positional arguments that have the same primitive type.
- Assuming JavaScript supports Python keyword arguments.
- Forgetting that a default parameter is used for an omitted or `undefined` argument, not for `null`.

### Activities
1. Call `calculateTotal` with the default rate and with a 0.20 rate.
2. Create an options object for the canonical student profile.
3. Omit one required property and decide how the function should validate it.
4. Explain the difference between omitted, `undefined`, and `null`.

### Accessibility Practice
Prefer clear property names over unexplained positional values when a function accepts several related settings.

### Skills Checklist
- [ ] I can pass positional arguments.
- [ ] I can define default parameters.
- [ ] I can use an options object.
- [ ] I can explain JavaScript's argument semantics.

## Lesson 6.3: Return Values

### Reading References
- Python source counterpart: Unit 6, Lesson 6.3.
- MDN: return.

### Learning Objectives
- Return values from functions.
- Distinguish returning from printing.
- Handle early returns for invalid inputs.

### Worked Example
```javascript
function average(scores) {
  if (!Array.isArray(scores) || scores.length === 0) {
    return null;
  }
  const total = scores.reduce((sum, score) => sum + score, 0);
  return total / scores.length;
}

const result = average([82, 91, 76, 88]);
console.log(`Average: ${result.toFixed(2)}`);
console.log(`Empty input: ${average([])}`);
```

Expected output:
```text
Average: 84.25
Empty input: null
```

### Common Mistakes
- Expecting a function that only calls `console.log()` to return a useful value.
- Forgetting that a function without an explicit return produces `undefined`.
- Returning a formatted string when later calculations require a number.

### Activities
1. Write a function that returns the total of the canonical scores.
2. Write a function that returns `null` for an empty list.
3. Use the returned average in a second calculation.
4. Compare a function that prints a result with one that returns it.

### Accessibility Practice
Keep calculation results and explanatory output distinct. Use explicit labels when displaying a returned value.

### Skills Checklist
- [ ] I can return a value from a function.
- [ ] I can use early returns for invalid cases.
- [ ] I can distinguish `undefined`, `null`, and a computed value.
- [ ] I can reuse returned values in later calculations.

## Lesson 6.4: Functions with Arrays and Objects

### Reading References
- Python source counterpart: Unit 6, Lesson 6.4.
- MDN: Working with objects and arrays.

### Learning Objectives
- Pass arrays and objects to functions.
- Process the canonical score and inventory data.
- Explain that object and array values are passed by sharing their references.

### Worked Example
```javascript
function inventoryValue(items) {
  return items.reduce(
    (total, item) => total + item.quantity * item.unitPrice,
    0
  );
}

const inventory = [
  { name: "Notebook", quantity: 3, unitPrice: 2.50 },
  { name: "Pencil", quantity: 10, unitPrice: 0.50 },
  { name: "Folder", quantity: 4, unitPrice: 1.25 }
];

console.log(`Inventory value: $${inventoryValue(inventory).toFixed(2)}`);
```

Expected output:
```text
Inventory value: $16.00
```

### Common Mistakes
- Mutating an array or object inside a function without documenting the side effect.
- Assuming a new variable created with `const` makes the referenced object immutable.
- Returning the wrong data shape for the caller.

### Activities
1. Write a function that returns the average of the canonical scores.
2. Write a function that returns the total value of the canonical inventory.
3. Add a new inventory item and verify the total changes by its line value.
4. Write a non-mutating function that returns a filtered list of scores at least 80.

### Accessibility Practice
Use named object properties and label each returned total. Explain whether a function changes the original collection.

### Skills Checklist
- [ ] I can pass arrays and objects to functions.
- [ ] I can process a collection with `reduce()` or a loop.
- [ ] I can explain reference sharing and mutation.
- [ ] I can return a predictable result shape.

## Lesson 6.5: Arbitrary Numbers of Arguments

### Reading References
- Python source counterpart: Unit 6, Lesson 6.5.
- MDN: Rest parameters.

### Learning Objectives
- Use rest parameters to collect arbitrary positional arguments.
- Use spread syntax to pass array elements as arguments.
- Explain the difference between rest and spread syntax.

### Worked Example
```javascript
function sumScores(...scores) {
  return scores.reduce((total, score) => total + score, 0);
}

const values = [82, 91, 76, 88];
console.log(sumScores(...values));
console.log(sumScores(10, 20, 30));
```

Expected output:
```text
337
60
```

### Common Mistakes
- Confusing rest parameters in a function definition with spread syntax in a call.
- Placing a rest parameter anywhere other than the final parameter position.
- Passing a whole array when the function expects individual numeric arguments.

### Activities
1. Call `sumScores` with the four canonical scores.
2. Call it with three different values.
3. Pass an array using spread syntax.
4. Explain why JavaScript rest parameters do not provide a direct equivalent to Python's `**kwargs`.

### Accessibility Practice
Use parameter names that communicate the expected value type. Keep the function's input contract explicit.

### Skills Checklist
- [ ] I can define a rest parameter.
- [ ] I can use spread syntax in a function call.
- [ ] I can distinguish rest from spread.
- [ ] I can explain the lack of Python-style keyword-argument collection.

# Unit 7: Classes and Object-Oriented Programming

## Overview
This unit uses the same student and inventory domains as the Python course. JavaScript classes use prototypes under the hood; private fields begin with `#`. Composition is often preferable to inheritance when one object contains another.

## Lesson 7.1: Why Learn About Classes?

### Reading References
- Python source counterpart: Unit 7, Lesson 7.1.
- MDN: Classes.

### Learning Objectives
- Explain classes, objects, attributes, and methods.
- Describe encapsulation and abstraction.
- Identify an appropriate domain object.

### Concept Explanation
A class defines the structure and behavior shared by its instances. An inventory item can store a name, quantity, and unit price and provide a method that calculates its line value.

### Worked Example
```javascript
class InventoryItem {
  constructor(name, quantity, unitPrice) {
    this.name = name;
    this.quantity = quantity;
    this.unitPrice = unitPrice;
  }

  lineValue() {
    return this.quantity * this.unitPrice;
  }
}

const notebook = new InventoryItem("Notebook", 3, 2.50);
console.log(`${notebook.name}: $${notebook.lineValue().toFixed(2)}`);
```

Expected output:
```text
Notebook: $7.50
```

### Common Mistakes
- Confusing the class with an instance.
- Omitting `this` when accessing instance properties.
- Defining behavior that belongs to an object as unrelated global variables.

### Activities
1. Create an InventoryItem for each canonical inventory record.
2. Print each item's line value.
3. Create a Student class using Avery's profile fields.
4. Explain which data belongs in an instance and which behavior belongs in a method.

### Accessibility Practice
Use descriptive property and method names. Announce object values by property name rather than relying on visual object inspection.

### Skills Checklist
- [ ] I can explain a class and an instance.
- [ ] I can define a constructor and method.
- [ ] I can use `this` to access instance properties.
- [ ] I can identify encapsulation in a small class.

## Lesson 7.2: Creating and Using a Class

### Reading References
- Python source counterpart: Unit 7, Lesson 7.2.
- MDN: constructor.

### Learning Objectives
- Define a class with a constructor.
- Instantiate multiple objects.
- Validate constructor arguments.

### Worked Example
```javascript
class Student {
  constructor(name, age, heightM, favoriteSubject) {
    if (typeof name !== "string" || name.trim() === "") {
      throw new TypeError("Student name is required.");
    }
    this.name = name;
    this.age = age;
    this.heightM = heightM;
    this.favoriteSubject = favoriteSubject;
  }
}

const student = new Student("Avery", 16, 1.72, "Computer Science");
console.log(`${student.name}, age ${student.age}`);
```

Expected output:
```text
Avery, age 16
```

### Common Mistakes
- Forgetting the `new` keyword.
- Using constructor parameters without assigning them to the instance.
- Failing to validate required data.

### Activities
1. Create two Student instances with different values.
2. Print each student's name and favorite subject.
3. Add validation that age is a nonnegative integer.
4. Deliberately pass an invalid name and read the error.

### Accessibility Practice
Make validation errors specific and textual. Keep constructor parameters in a consistent, documented order.

### Skills Checklist
- [ ] I can define a constructor.
- [ ] I can instantiate multiple objects.
- [ ] I can validate constructor inputs.
- [ ] I can explain the role of `new`.

## Lesson 7.3: Working with Attributes and Methods

### Reading References
- Python source counterpart: Unit 7, Lesson 7.3.
- MDN: Private class elements.

### Learning Objectives
- Read and update object properties.
- Define methods that validate or transform state.
- Use a private field for encapsulated state.

### Worked Example
```javascript
class InventoryItem {
  #quantity;

  constructor(name, quantity, unitPrice) {
    this.name = name;
    this.#quantity = quantity;
    this.unitPrice = unitPrice;
  }

  updateQuantity(newQuantity) {
    if (!Number.isInteger(newQuantity) || newQuantity < 0) {
      throw new RangeError("Quantity must be a nonnegative integer.");
    }
    this.#quantity = newQuantity;
  }

  describe() {
    return `${this.name}: quantity ${this.#quantity}`;
  }
}

const pencil = new InventoryItem("Pencil", 10, 0.50);
pencil.updateQuantity(12);
console.log(pencil.describe());
```

Expected output:
```text
Pencil: quantity 12
```

### Common Mistakes
- Accessing a private field from outside its class.
- Updating state without validating it.
- Confusing a method call with a property read.

### Activities
1. Add a method that returns the item's line value.
2. Reject a negative quantity.
3. Update the Notebook quantity from 3 to 5.
4. Explain why a private field can protect an object's invariants.

### Accessibility Practice
Use methods that return clear text or values. State the validation rule before asking learners to test it.

### Skills Checklist
- [ ] I can read and update public properties.
- [ ] I can define and call methods.
- [ ] I can use a private class field.
- [ ] I can validate state changes.

## Lesson 7.4: Inheritance

### Reading References
- Python source counterpart: Unit 7, Lesson 7.4.
- MDN: Inheritance and the prototype chain.

### Learning Objectives
- Define a subclass with `extends`.
- Call a parent constructor with `super()`.
- Override a method when specialized behavior is required.

### Worked Example
```javascript
class InventoryItem {
  constructor(name, quantity) {
    this.name = name;
    this.quantity = quantity;
  }

  describe() {
    return `${this.name}: ${this.quantity} in stock`;
  }
}

class PerishableItem extends InventoryItem {
  constructor(name, quantity, expirationDate) {
    super(name, quantity);
    this.expirationDate = expirationDate;
  }

  describe() {
    return `${super.describe()}, expires ${this.expirationDate}`;
  }
}

const milk = new PerishableItem("Milk", 2, "2026-11-10");
console.log(milk.describe());
```

Expected output:
```text
Milk: 2 in stock, expires 2026-11-10
```

### Common Mistakes
- Calling `this` before `super()` in a derived constructor.
- Forgetting to pass required parent arguments.
- Using inheritance when composition would be simpler.

### Activities
1. Create a PerishableItem subclass with an expiration date.
2. Override the description method.
3. Test an instance with the canonical inventory quantity.
4. Identify one situation where composition is preferable.

### Accessibility Practice
Describe the parent/child relationship explicitly. Keep overridden method behavior predictable and document what changes.

### Skills Checklist
- [ ] I can extend a class.
- [ ] I can call a parent constructor with `super()`.
- [ ] I can override a method.
- [ ] I can explain when inheritance is appropriate.

## Lesson 7.5: Instances as Attributes (Composition)

### Reading References
- Python source counterpart: Unit 7, Lesson 7.5.
- MDN: Working with objects.

### Learning Objectives
- Model a has-a relationship.
- Store one object inside another object.
- Explain composition as an alternative to inheritance.

### Worked Example
```javascript
class Student {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

class StudentRecord {
  constructor(student, favoriteSubject) {
    this.student = student;
    this.favoriteSubject = favoriteSubject;
  }

  describe() {
    return `${this.student.name} studies ${this.favoriteSubject}.`;
  }
}

const record = new StudentRecord(
  new Student("Avery", 16),
  "Computer Science"
);
console.log(record.describe());
```

Expected output:
```text
Avery studies Computer Science.
```

### Common Mistakes
- Copying an object's fields when a related object should be retained.
- Confusing has-a composition with is-a inheritance.
- Creating circular object references without a clear reason.

### Activities
1. Create a Student object for Avery.
2. Place the Student object inside a StudentRecord.
3. Add a second related object, such as a contact record.
4. Explain why StudentRecord is not a subclass of Student.

### Accessibility Practice
Use explicit relationship names such as `student` and `contact`. Print nested values with labels.

### Skills Checklist
- [ ] I can model a has-a relationship.
- [ ] I can store an object as another object's property.
- [ ] I can explain composition versus inheritance.
- [ ] I can access nested object properties.

# Unit 8: Files and Exceptions

## Overview
This unit uses the same `notes.txt` and structured task/student records as the Python course. Node.js file APIs are asynchronous by default; use promises and `try/catch/finally` to make resource behavior explicit.

## Lesson 8.1: Reading from a File

### Reading References
- Python source counterpart: Unit 8, Lesson 8.1.
- Node.js documentation: `node:fs/promises`.

### Learning Objectives
- Read a UTF-8 text file.
- Distinguish whole-file reads from line-by-line processing.
- Handle a missing file with a clear error.

### Worked Example
Create `notes.txt` containing:
```text
Practice JavaScript.
Review arrays and functions.
```

Read it:
```javascript
const fs = require("node:fs/promises");

async function main() {
  try {
    const contents = await fs.readFile("notes.txt", "utf8");
    console.log("File contents:");
    console.log(contents.trimEnd());
  } catch (error) {
    if (error.code === "ENOENT") {
      console.log("Error: notes.txt was not found.");
    } else {
      throw error;
    }
  }
}

main();
```

Expected output:
```text
File contents:
Practice JavaScript.
Review arrays and functions.
```

### Common Mistakes
- Omitting the encoding and receiving a Buffer.
- Using the wrong working directory for a relative path.
- Ignoring the rejected promise from file I/O.

### Activities
1. Create and read the canonical notes.txt file.
2. Rename the file and verify the missing-file message.
3. Read the file and count its lines.
4. Explain the difference between a relative and absolute path.

### Accessibility Practice
Report the file name and each line in reading order. Use textual errors that identify the missing path.

### Skills Checklist
- [ ] I can read a UTF-8 file with `fs.readFile()`.
- [ ] I can explain relative paths.
- [ ] I can handle a missing file.
- [ ] I can distinguish text from Buffer data.

## Lesson 8.2: Writing to a File

### Reading References
- Python source counterpart: Unit 8, Lesson 8.2.
- Node.js documentation: `writeFile()` and `appendFile()`.

### Learning Objectives
- Create or overwrite a text file.
- Append content without replacing existing content.
- Confirm successful file operations.

### Worked Example
```javascript
const fs = require("node:fs/promises");

async function main() {
  await fs.writeFile("notes.txt", "Practice JavaScript.\n", "utf8");
  await fs.appendFile("notes.txt", "Review arrays and functions.\n", "utf8");
  const saved = await fs.readFile("notes.txt", "utf8");
  console.log(saved.trimEnd());
  console.log("Notes saved.");
}

main().catch(error => {
  console.error(`File error: ${error.message}`);
  process.exitCode = 1;
});
```

Expected output:
```text
Practice JavaScript.
Review arrays and functions.
Notes saved.
```

### Common Mistakes
- Using write mode when the intention is to append.
- Forgetting to await a write before reading the file.
- Assuming a successful call means the path is the intended one.

### Activities
1. Write a one-line note to notes.txt.
2. Append a second line.
3. Run the program twice and explain whether the content is overwritten or appended.
4. Verify the saved text by reading it back programmatically.

### Accessibility Practice
Print a confirmation that identifies the file and operation. Do not rely on a file icon or color to indicate success.

### Skills Checklist
- [ ] I can write a text file.
- [ ] I can append to a text file.
- [ ] I can await file operations.
- [ ] I can verify saved content.

## Lesson 8.3: Exceptions — Handling Errors

### Reading References
- Python source counterpart: Unit 8, Lesson 8.3.
- MDN: Error and try...catch.

### Learning Objectives
- Handle exceptions with `try/catch`.
- Distinguish expected errors from unexpected errors.
- Define a custom error class.

### Worked Example
```javascript
class ValidationError extends Error {
  constructor(field, message) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}

function validateAge(age) {
  if (!Number.isInteger(age) || age < 0) {
    throw new ValidationError("age", "Age must be a nonnegative integer.");
  }
  return age;
}

try {
  console.log(validateAge(16));
  validateAge(-1);
} catch (error) {
  if (error instanceof ValidationError) {
    console.log(`Validation failed for ${error.field}: ${error.message}`);
  } else {
    throw error;
  }
}
```

Expected output:
```text
16
Validation failed for age: Age must be a nonnegative integer.
```

### Common Mistakes
- Catching every error and silently ignoring it.
- Throwing a string instead of an Error object.
- Failing to rethrow unexpected errors.

### Activities
1. Validate that Avery's age is 16.
2. Test negative age, decimal age, and text input.
3. Create a custom error for an invalid inventory quantity.
4. Explain why unexpected errors should not be hidden.

### Accessibility Practice
Error messages should identify the field, invalid value when safe, and correction expected. Keep error output textual.

### Skills Checklist
- [ ] I can use `try/catch`.
- [ ] I can throw an Error object.
- [ ] I can define a custom error class.
- [ ] I can distinguish expected and unexpected errors.

## Lesson 8.4: The `else` and `finally` Patterns

### Reading References
- Python source counterpart: Unit 8, Lesson 8.4.
- MDN: try...catch...finally.

### Learning Objectives
- Explain code that runs after success or regardless of success.
- Use `finally` for cleanup.
- Recognize that JavaScript does not have Python's `try/except/else` syntax.

### Concept Explanation
JavaScript has `try`, `catch`, and `finally`, but no direct `else` clause attached to a try statement. Put success-only work after the operation inside the try block. Put cleanup in `finally`.

### Worked Example
```javascript
async function loadNotes() {
  let contents;
  try {
    contents = await require("node:fs/promises").readFile("notes.txt", "utf8");
  } catch (error) {
    console.log(`Unable to read notes: ${error.message}`);
    return;
  } finally {
    console.log("Read attempt finished.");
  }

  console.log("Read succeeded.");
  console.log(contents.trimEnd());
}

loadNotes();
```

### Common Mistakes
- Assuming JavaScript supports Python's `try/except/else` syntax.
- Placing success-only code in `finally`.
- Returning from `finally` and unintentionally overriding an earlier return or exception.

### Activities
1. Run the example with notes.txt present.
2. Run it with notes.txt missing.
3. Identify which messages appear in each case.
4. Explain why cleanup belongs in `finally`.

### Accessibility Practice
Use separate success and failure messages. Ensure the final status is announced regardless of outcome.

### Skills Checklist
- [ ] I can explain JavaScript's try/catch/finally structure.
- [ ] I can identify success-only operations.
- [ ] I can use finally for cleanup.
- [ ] I can explain the absence of a direct try-else clause.

## Lesson 8.5: Storing Data with JSON

### Reading References
- Python source counterpart: Unit 8, Lesson 8.5.
- MDN: JSON.

### Learning Objectives
- Convert JavaScript objects to JSON text.
- Parse JSON text into JavaScript values.
- Save and reload structured records.

### Worked Example
```javascript
const fs = require("node:fs/promises");

async function main() {
  const tasks = [
    { id: 1, title: "Review arrays", done: false },
    { id: 2, title: "Practice functions", done: true }
  ];

  const jsonText = JSON.stringify(tasks, null, 2);
  await fs.writeFile("tasks.json", jsonText, "utf8");

  const loadedText = await fs.readFile("tasks.json", "utf8");
  const loadedTasks = JSON.parse(loadedText);
  console.log(`Loaded ${loadedTasks.length} tasks.`);
  console.log(`First task: ${loadedTasks[0].title}`);
}

main().catch(error => {
  console.error(`Storage error: ${error.message}`);
  process.exitCode = 1;
});
```

Expected output:
```text
Loaded 2 tasks.
First task: Review arrays
```

### Common Mistakes
- Passing an already serialized string to `JSON.stringify()` and double-encoding it.
- Parsing malformed JSON without catching SyntaxError.
- Assuming JSON preserves functions, undefined values, or every JavaScript type.

### Activities
1. Save and reload the canonical task fields: id, title, description, done, created_at.
2. Add a task and verify it survives a second program run.
3. Deliberately corrupt the JSON and handle the parse error.
4. Compare the in-memory object with the JSON text stored on disk.

### Accessibility Practice
Use pretty-printed JSON for manual inspection and provide a textual confirmation after saving or loading.

### Skills Checklist
- [ ] I can serialize objects with `JSON.stringify()`.
- [ ] I can parse JSON with `JSON.parse()`.
- [ ] I can save and reload structured data.
- [ ] I can handle malformed JSON.
