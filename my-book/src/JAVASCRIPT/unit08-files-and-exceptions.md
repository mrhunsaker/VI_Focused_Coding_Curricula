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

### Concept Explanation
The `node:fs/promises` API returns promises for file operations. UTF-8 decoding returns a string; omitting the encoding returns a Buffer.

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

### Expected Behavior or Output
With the sample notes.txt file present, both note lines are printed under the File contents label.

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

### Concept Explanation
`writeFile()` creates or replaces file content; `appendFile()` adds content. Await each operation before relying on its result.

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

### Expected Behavior or Output
The two note lines are printed, followed by `Notes saved.`.

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

### Concept Explanation
An exception interrupts normal control flow. `try/catch` handles expected failures, and custom Error subclasses can carry additional context.

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

### Expected Behavior or Output
The valid age 16 is printed; invalid age -1 produces the field-specific validation message.

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

### Expected Behavior or Output
The final status message is printed whether the read succeeds or fails. The success message and file contents appear only when the read succeeds.

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

### Concept Explanation
JSON is a text representation of structured data. `JSON.stringify()` serializes supported JavaScript values; `JSON.parse()` reconstructs values from valid JSON text.

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

### Expected Behavior or Output
The example prints `Loaded 2 tasks.` and `First task: Review arrays` after saving and reloading the data.

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
