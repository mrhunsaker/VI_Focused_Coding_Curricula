# Unit 11: Capstone Project — Accessible Personal Data Manager

## Overview
Build a complete command-line personal data manager in JavaScript and Node.js. The implementation may choose a Contact Manager, Book Tracker, Recipe Collection, or Budget Tracker, but the data model, operations, persistence, accessibility, and acceptance tests must be equivalent across the language tracks. Unlike the Python implementation, which introduces NiceGUI, this JavaScript track uses a terminal interface so the core capstone remains independent of a browser UI.

## Lesson 11.1: Project Introduction and Interface Design

### Reading References
- Python source counterpart: Unit 11, Lesson 11.1.
- Node.js documentation: readline/promises.

### Learning Objectives
- Select a capstone domain.
- Translate requirements into a menu and command set.
- Design a keyboard-first text interface.

### Concept Explanation
The capstone is assessed on data operations and accessibility, not visual interface fluency. The terminal interface must support adding, viewing, searching, editing, deleting, and saving records. A help command must list all commands.

### Worked Example
A minimal command menu might list: add, view, search, edit, delete, help, and quit. Each command maps to one named function.

### Expected Behavior or Output
The project plan contains a selected domain, a record schema, command descriptions, and acceptance tests.

### Common Mistakes
- Choosing a domain before identifying required fields and operations.
- Designing a visual-only interaction when the project requires an accessible text interface.
- Omitting help and invalid-command behavior.

### Activities
1. Choose one project domain.
2. List the fields each record requires.
3. Design the menu and exact prompt wording.
4. Write acceptance tests for all required operations.

### Accessibility Practice
Every action must be possible from the keyboard. Prompts must name the expected field and format. Output must be sequential and understandable without visual layout.

### Skills Checklist
- [ ] I can select a project domain.
- [ ] I can define a record schema.
- [ ] I can design a text-only command interface.
- [ ] I can write acceptance tests.

## Lesson 11.2: Data Model and Storage

### Reading References
- Python source counterpart: Unit 11, Lesson 11.2.
- Node.js documentation: fs/promises and JSON.

### Learning Objectives
- Define a record model.
- Persist records to JSON.
- Handle missing, malformed, and inaccessible files.

### Concept Explanation

The data model defines the fields and invariants of each record. JSON persistence stores the records between runs; load and save operations must handle file and parse failures.

#### Canonical Record Fields

Use these shared fields for the generic personal data manager: `id`, `title`, `description`, `category`, `created_at`, and `updated_at`. A selected domain may add fields, but must not remove the shared fields.

### Worked Example

A record contains id, title, description, category, created_at, and updated_at. The id is unique; timestamps use ISO 8601 strings.

### Expected Behavior or Output

After saving and reloading, all record fields and values are preserved. Missing files can initialize an empty collection; malformed JSON produces a clear error.

### Common Mistakes

- Treating parsed JSON as trusted data without validation.
- Reusing record identifiers.
- Overwriting valid data after a parse failure without informing the user.

### Activities
1. Define the record shape and document each field.
2. Create a sample JSON file containing at least three records.
3. Implement load and save functions.
4. Test missing files, malformed JSON, and an empty data set.

### Accessibility Practice
Use human-readable JSON during development. Provide explicit save/load confirmations and specific error messages.

### Skills Checklist

- [ ] I can define the record schema.
- [ ] I can load and save JSON.
- [ ] I can preserve timestamps and identifiers.
- [ ] I can handle missing and malformed data.

### Concept Explanation
The data model defines the fields and invariants of each record. JSON persistence stores the records between runs; load and save operations must handle file and parse failures.


## Lesson 11.3: Displaying Items

### Reading References
- Python source counterpart: Unit 11, Lesson 11.3.
- Node.js documentation: console output and Array iteration.

### Learning Objectives
- Display every record with a one-based number.
- Print each field with an explicit label.
- Handle an empty collection.

### Concept Explanation
Displaying records is a read operation. A one-based display number is a temporary selection aid; the stored identifier remains the stable record identity.

### Worked Example
```javascript
function displayItems(items) {
  if (items.length === 0) {
    console.log("No items have been saved.");
    return;
  }
  items.forEach((item, index) => {
    console.log(`Item ${index + 1}:`);
    console.log(`  Title: ${item.title}`);
    console.log(`  Category: ${item.category}`);
    console.log(`  Description: ${item.description}`);
  });
}
```

### Expected Behavior or Output
Each record is announced with its number and labeled fields. An empty collection prints the no-items message.

### Common Mistakes
- Omitting field labels.
- Using zero-based indexes as the displayed number.
- Failing to handle an empty collection.

### Activities
1. Display three sample records in order.
2. Display an empty list and confirm the message is clear.
3. Include the record identifier and timestamps in the output.
4. Review output using sequential screen-reader navigation.

### Accessibility Practice
Use labels, stable ordering, and one record at a time. Do not rely on columns, color, or icons to convey record fields.

### Skills Checklist
- [ ] I can display all records.
- [ ] I can number records for selection.
- [ ] I can handle an empty collection.
- [ ] I can label every displayed field.

## Lesson 11.4: Searching, Adding, and Editing Items

### Reading References
- Python source counterpart: Unit 11, Lessons 11.3–11.5.
- Node.js documentation: Array methods and Date.

### Learning Objectives
- Add validated records with unique identifiers.
- Search records by keyword.
- Edit selected fields and update timestamps.

### Concept Explanation
Searching filters records without changing the stored collection. Editing changes only permitted fields and updates the updated_at timestamp.

### Worked Example
```javascript
function searchItems(items, keyword) {
  const query = keyword.trim().toLowerCase();
  return items.filter(item =>
    item.title.toLowerCase().includes(query) ||
    item.description.toLowerCase().includes(query)
  );
}

function updateItem(item, changes) {
  const allowed = ["title", "description", "category"];
  for (const field of allowed) {
    if (Object.hasOwn(changes, field)) item[field] = changes[field];
  }
  item.updated_at = new Date().toISOString();
}
```

### Expected Behavior or Output
Search returns matching titles or descriptions. A successful edit changes the requested field and refreshes updated_at.

### Common Mistakes
- Searching case-sensitively without documenting that behavior.
- Allowing edits to immutable identifiers.
- Failing to update the modification timestamp.

### Activities
1. Search records by a word in the title.
2. Search by a word in the description.
3. Edit a title and verify that updated_at changes.
4. Reject an edit that contains only blank required fields.

### Accessibility Practice
Report the number of matches and identify each result by its title and record number. Confirm every successful edit.

### Skills Checklist
- [ ] I can search records by keyword.
- [ ] I can add a validated record.
- [ ] I can update selected fields.
- [ ] I can maintain the updated_at timestamp.

## Lesson 11.5: Deleting Items, Persistence, and Final Verification

### Reading References
- Python source counterpart: Unit 11, Lessons 11.3–11.5.
- Node.js documentation: fs/promises and JSON.

### Learning Objectives
- Delete a record by its identifier or displayed number.
- Save changes and reload them between program runs.
- Verify the full CRUD workflow and error handling.

### Concept Explanation
Deleting removes a selected record from the collection. Persistence must happen after the mutation so the deletion remains effective after the next program launch.

### Worked Example
```javascript
function deleteItem(items, id) {
  const index = items.findIndex(item => item.id === id);
  if (index < 0) return false;
  items.splice(index, 1);
  return true;
}
```

### Expected Behavior or Output
After deleting and saving a record, reloading the JSON file confirms that the record is absent.

### Common Mistakes
- Deleting by a stale array index.
- Failing to save after a deletion.
- Omitting confirmation for an irreversible action.

### Activities
1. Delete one record and confirm the title of the deleted item.
2. Save the remaining records to JSON.
3. Restart the application and verify the deleted record is still absent.
4. Run the full acceptance checklist: add, view, search, edit, delete, invalid input, missing file, malformed JSON, and help.

### Accessibility Practice
Ask for confirmation before irreversible deletion. Announce success or failure in text and preserve predictable menu navigation.

### Runnable Reference Implementation

The repository includes a tested JavaScript domain and JSON-storage reference core in [capstone/README.md](capstone/README.md). Run `node --test JAVASCRIPT/capstone/records.test.js` from the repository root. The reference core does not replace the requirement to build and evaluate an accessible user interface.

### Skills Checklist
- [ ] I can delete a record safely.
- [ ] I can persist and reload records.
- [ ] I can verify the complete CRUD workflow.
- [ ] I can test invalid input and storage failures.

## Assessment Criteria

### Functionality (60%)
- [ ] All create, read, update, and delete operations work.
- [ ] Data persists to JSON between program runs.
- [ ] Search works by at least one field.
- [ ] Invalid input is handled without crashing.

### Code Quality (20%)
- [ ] Functions have focused responsibilities.
- [ ] Names are descriptive and consistent.
- [ ] Code is organized into modules.
- [ ] Key functions include JSDoc comments.

### Accessibility and User Experience (15%)
- [ ] Prompts are descriptive and clear.
- [ ] Every state-changing operation has a confirmation.
- [ ] Output is sequential and predictable.
- [ ] A help system is available.
- [ ] Keyboard-only operation is supported.

### Documentation and Tests (5%)
- [ ] README includes setup and usage instructions.
- [ ] At least five unit tests cover key functions.
- [ ] README includes screen-reader usage tips and a reflection.

## Deliverables
- Source files organized into modules.
- A data folder with example JSON records.
- A README with installation, run instructions, commands, screen-reader tips, and a reflection.
- A test suite with at least five meaningful tests.

## JavaScript Module Note
CommonJS and ECMAScript modules are both valid JavaScript module systems. For this curriculum, choose one mode explicitly in package.json and use it consistently. If using CommonJS, use `require()` and `module.exports`; if using ES modules, use `import` and `export`. Do not mix both systems in a single file.

## AI Use Policy
AI may be used for personal conceptual explanations and reinforcement only. It may not write, autocomplete, repair, complete, or generate course code or assessment solutions. Students must be able to explain and independently produce their submitted work.
