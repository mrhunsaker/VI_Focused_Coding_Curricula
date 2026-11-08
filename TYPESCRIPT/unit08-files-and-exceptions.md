# Unit 8: Files and Exceptions

## Overview

Read and write files, handle errors, and persist validated JSON. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

<<<<<<< HEAD
---

## Overview

Read and write files, handle errors, and persist validated JSON. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

=======
>>>>>>> 2067a20 (curriculum clearning and updates)
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
<<<<<<< HEAD
