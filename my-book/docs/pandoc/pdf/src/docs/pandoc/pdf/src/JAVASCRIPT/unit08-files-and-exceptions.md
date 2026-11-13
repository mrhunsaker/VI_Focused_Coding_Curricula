[Header 2 ("unit-8-files-and-exceptions", [], []) [Str "Unit 8: Files and Exceptions"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit uses the same ", Code ("", [], []) "notes.txt", Str " and structured task/student records as the Python course. Node.js file APIs are asynchronous by default; use promises and ", Code ("", [], []) "try/catch/finally", Str " to make resource behavior explicit."], Header 3 ("lesson-81-reading-from-a-file", ["unnumbered", "unlisted"], []) [Str "Lesson 8.1: Reading from a File"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 8, Lesson 8.1."]], [Plain [Str "Node.js documentation: ", Code ("", [], []) "node:fs/promises", Str "."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Read a UTF-8 text file."]], [Plain [Str "Distinguish whole-file reads from line-by-line processing."]], [Plain [Str "Handle a missing file with a clear error."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The ", Code ("", [], []) "node:fs/promises", Str " API returns promises for file operations. UTF-8 decoding returns a string; omitting the encoding returns a Buffer."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "Create ", Code ("", [], []) "notes.txt", Str " containing:"], CodeBlock ("", ["text"], []) "Practice JavaScript.
Review arrays and functions.
", Para [Str "Read it:"], CodeBlock ("", ["javascript"], []) "const fs = require(\"node:fs/promises\");

async function main() {
  try {
    const contents = await fs.readFile(\"notes.txt\", \"utf8\");
    console.log(\"File contents:\");
    console.log(contents.trimEnd());
  } catch (error) {
    if (error.code === \"ENOENT\") {
      console.log(\"Error: notes.txt was not found.\");
    } else {
      throw error;
    }
  }
}

main();
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "File contents:
Practice JavaScript.
Review arrays and functions.
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the sample notes.txt file present, both note lines are printed under the File contents label."], Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Omitting the encoding and receiving a Buffer."]], [Plain [Str "Using the wrong working directory for a relative path."]], [Plain [Str "Ignoring the rejected promise from file I/O."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create and read the canonical notes.txt file."]], [Plain [Str "Rename the file and verify the missing-file message."]], [Plain [Str "Read the file and count its lines."]], [Plain [Str "Explain the difference between a relative and absolute path."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Report the file name and each line in reading order. Use textual errors that identify the missing path."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can read a UTF-8 file with ", Code ("", [], []) "fs.readFile()", Str "."]], [Plain [Str "\9744", Space, Str "I can explain relative paths."]], [Plain [Str "\9744", Space, Str "I can handle a missing file."]], [Plain [Str "\9744", Space, Str "I can distinguish text from Buffer data."]]], Header 3 ("lesson-82-writing-to-a-file", ["unnumbered", "unlisted"], []) [Str "Lesson 8.2: Writing to a File"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 8, Lesson 8.2."]], [Plain [Str "Node.js documentation: ", Code ("", [], []) "writeFile()", Str " and ", Code ("", [], []) "appendFile()", Str "."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create or overwrite a text file."]], [Plain [Str "Append content without replacing existing content."]], [Plain [Str "Confirm successful file operations."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "writeFile()", Str " creates or replaces file content; ", Code ("", [], []) "appendFile()", Str " adds content. Await each operation before relying on its result."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["javascript"], []) "const fs = require(\"node:fs/promises\");

async function main() {
  await fs.writeFile(\"notes.txt\", \"Practice JavaScript.\\n\", \"utf8\");
  await fs.appendFile(\"notes.txt\", \"Review arrays and functions.\\n\", \"utf8\");
  const saved = await fs.readFile(\"notes.txt\", \"utf8\");
  console.log(saved.trimEnd());
  console.log(\"Notes saved.\");
}

main().catch(error => {
  console.error(`File error: ${error.message}`);
  process.exitCode = 1;
});
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "Practice JavaScript.
Review arrays and functions.
Notes saved.
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The two note lines are printed, followed by ", Code ("", [], []) "Notes saved.", Str "."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Using write mode when the intention is to append."]], [Plain [Str "Forgetting to await a write before reading the file."]], [Plain [Str "Assuming a successful call means the path is the intended one."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write a one-line note to notes.txt."]], [Plain [Str "Append a second line."]], [Plain [Str "Run the program twice and explain whether the content is overwritten or appended."]], [Plain [Str "Verify the saved text by reading it back programmatically."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print a confirmation that identifies the file and operation. Do not rely on a file icon or color to indicate success."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a text file."]], [Plain [Str "\9744", Space, Str "I can append to a text file."]], [Plain [Str "\9744", Space, Str "I can await file operations."]], [Plain [Str "\9744", Space, Str "I can verify saved content."]]], Header 3 ("lesson-83-exceptions--handling-errors", ["unnumbered", "unlisted"], []) [Str "Lesson 8.3: Exceptions — Handling Errors"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 8, Lesson 8.3."]], [Plain [Str "MDN: Error and try...catch."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Handle exceptions with ", Code ("", [], []) "try/catch", Str "."]], [Plain [Str "Distinguish expected errors from unexpected errors."]], [Plain [Str "Define a custom error class."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "An exception interrupts normal control flow. ", Code ("", [], []) "try/catch", Str " handles expected failures, and custom Error subclasses can carry additional context."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["javascript"], []) "class ValidationError extends Error {
  constructor(field, message) {
    super(message);
    this.name = \"ValidationError\";
    this.field = field;
  }
}

function validateAge(age) {
  if (!Number.isInteger(age) || age < 0) {
    throw new ValidationError(\"age\", \"Age must be a nonnegative integer.\");
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
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "16
Validation failed for age: Age must be a nonnegative integer.
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The valid age 16 is printed; invalid age -1 produces the field-specific validation message."], Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Catching every error and silently ignoring it."]], [Plain [Str "Throwing a string instead of an Error object."]], [Plain [Str "Failing to rethrow unexpected errors."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Validate that Avery's age is 16."]], [Plain [Str "Test negative age, decimal age, and text input."]], [Plain [Str "Create a custom error for an invalid inventory quantity."]], [Plain [Str "Explain why unexpected errors should not be hidden."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Error messages should identify the field, invalid value when safe, and correction expected. Keep error output textual."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "try/catch", Str "."]], [Plain [Str "\9744", Space, Str "I can throw an Error object."]], [Plain [Str "\9744", Space, Str "I can define a custom error class."]], [Plain [Str "\9744", Space, Str "I can distinguish expected and unexpected errors."]]], Header 3 ("lesson-84-the-else-and-finally-patterns", ["unnumbered", "unlisted"], []) [Str "Lesson 8.4: The ", Code ("", [], []) "else", Str " and ", Code ("", [], []) "finally", Str " Patterns"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 8, Lesson 8.4."]], [Plain [Str "MDN: try...catch...finally."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain code that runs after success or regardless of success."]], [Plain [Str "Use ", Code ("", [], []) "finally", Str " for cleanup."]], [Plain [Str "Recognize that JavaScript does not have Python's ", Code ("", [], []) "try/except/else", Str " syntax."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "JavaScript has ", Code ("", [], []) "try", Str ", ", Code ("", [], []) "catch", Str ", and ", Code ("", [], []) "finally", Str ", but no direct ", Code ("", [], []) "else", Str " clause attached to a try statement. Put success-only work after the operation inside the try block. Put cleanup in ", Code ("", [], []) "finally", Str "."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["javascript"], []) "async function loadNotes() {
  let contents;
  try {
    contents = await require(\"node:fs/promises\").readFile(\"notes.txt\", \"utf8\");
  } catch (error) {
    console.log(`Unable to read notes: ${error.message}`);
    return;
  } finally {
    console.log(\"Read attempt finished.\");
  }

  console.log(\"Read succeeded.\");
  console.log(contents.trimEnd());
}

loadNotes();
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The final status message is printed whether the read succeeds or fails. The success message and file contents appear only when the read succeeds."], Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Assuming JavaScript supports Python's ", Code ("", [], []) "try/except/else", Str " syntax."]], [Plain [Str "Placing success-only code in ", Code ("", [], []) "finally", Str "."]], [Plain [Str "Returning from ", Code ("", [], []) "finally", Str " and unintentionally overriding an earlier return or exception."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the example with notes.txt present."]], [Plain [Str "Run it with notes.txt missing."]], [Plain [Str "Identify which messages appear in each case."]], [Plain [Str "Explain why cleanup belongs in ", Code ("", [], []) "finally", Str "."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use separate success and failure messages. Ensure the final status is announced regardless of outcome."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain JavaScript's try/catch/finally structure."]], [Plain [Str "\9744", Space, Str "I can identify success-only operations."]], [Plain [Str "\9744", Space, Str "I can use finally for cleanup."]], [Plain [Str "\9744", Space, Str "I can explain the absence of a direct try-else clause."]]], Header 3 ("lesson-85-storing-data-with-json", ["unnumbered", "unlisted"], []) [Str "Lesson 8.5: Storing Data with JSON"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 8, Lesson 8.5."]], [Plain [Str "MDN: JSON."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Convert JavaScript objects to JSON text."]], [Plain [Str "Parse JSON text into JavaScript values."]], [Plain [Str "Save and reload structured records."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "JSON is a text representation of structured data. ", Code ("", [], []) "JSON.stringify()", Str " serializes supported JavaScript values; ", Code ("", [], []) "JSON.parse()", Str " reconstructs values from valid JSON text."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["javascript"], []) "const fs = require(\"node:fs/promises\");

async function main() {
  const tasks = [
    { id: 1, title: \"Review arrays\", done: false },
    { id: 2, title: \"Practice functions\", done: true }
  ];

  const jsonText = JSON.stringify(tasks, null, 2);
  await fs.writeFile(\"tasks.json\", jsonText, \"utf8\");

  const loadedText = await fs.readFile(\"tasks.json\", \"utf8\");
  const loadedTasks = JSON.parse(loadedText);
  console.log(`Loaded ${loadedTasks.length} tasks.`);
  console.log(`First task: ${loadedTasks[0].title}`);
}

main().catch(error => {
  console.error(`Storage error: ${error.message}`);
  process.exitCode = 1;
});
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "Loaded 2 tasks.
First task: Review arrays
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The example prints ", Code ("", [], []) "Loaded 2 tasks.", Str " and ", Code ("", [], []) "First task: Review arrays", Str " after saving and reloading the data."], Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Passing an already serialized string to ", Code ("", [], []) "JSON.stringify()", Str " and double-encoding it."]], [Plain [Str "Parsing malformed JSON without catching SyntaxError."]], [Plain [Str "Assuming JSON preserves functions, undefined values, or every JavaScript type."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Save and reload the canonical task fields: id, title, description, done, created_at."]], [Plain [Str "Add a task and verify it survives a second program run."]], [Plain [Str "Deliberately corrupt the JSON and handle the parse error."]], [Plain [Str "Compare the in-memory object with the JSON text stored on disk."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use pretty-printed JSON for manual inspection and provide a textual confirmation after saving or loading."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can serialize objects with ", Code ("", [], []) "JSON.stringify()", Str "."]], [Plain [Str "\9744", Space, Str "I can parse JSON with ", Code ("", [], []) "JSON.parse()", Str "."]], [Plain [Str "\9744", Space, Str "I can save and reload structured data."]], [Plain [Str "\9744", Space, Str "I can handle malformed JSON."]]]]