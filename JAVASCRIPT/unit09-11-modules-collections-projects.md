# Units 9–11: Testing, Data Analysis, Projects, and Capstone

**Runtime baseline:** Node.js 26.x. Unit 9 uses Node's built-in test runner for a dependency-free baseline. A Jest alternative may be introduced as an extension.

# Unit 9: Testing and Data Analysis

## Overview
This unit follows the Python sequence: test a function, test a class, generate random values, analyze text, and process CSV data. Reuse the canonical score list, text sample, inventory, and CSV column names.

## Lesson 9.1: Testing a Function

### Reading References
- Python source counterpart: Unit 9, Lesson 9.1.
- Node.js documentation: Test runner (`node:test`).

### Learning Objectives
- Write unit tests for deterministic functions.
- Use assertions for expected and actual values.
- Run tests from the terminal.

### Concept Explanation
A unit test calls a deterministic function with known inputs and compares the returned value with an expected result. Tests should include ordinary inputs and boundary conditions.

### Worked Example
Create `math.js`:
```javascript
function add(a, b) {
  return a + b;
}

function getGrade(score) {
  if (score >= 90) return "A";
  if (score >= 80) return "B";
  if (score >= 70) return "C";
  if (score >= 60) return "D";
  return "F";
}

module.exports = { add, getGrade };
```

Create `math.test.js`:
```javascript
const test = require("node:test");
const assert = require("node:assert/strict");
const { add, getGrade } = require("./math");

test("add returns the sum", () => {
  assert.equal(add(5, 3), 8);
  assert.equal(add(-5, -3), -8);
  assert.equal(add(0, 7), 7);
});

test("getGrade follows shared thresholds", () => {
  assert.equal(getGrade(90), "A");
  assert.equal(getGrade(82), "B");
  assert.equal(getGrade(76), "C");
  assert.equal(getGrade(60), "D");
  assert.equal(getGrade(59), "F");
});
```

Run with `node --test`.

Expected result: two passing tests and zero failures.

### Expected Behavior or Output
The Node.js test runner reports two passing tests and no failures when add() and getGrade() satisfy the stated contracts.

### Common Mistakes
- Testing only one typical value and ignoring boundaries.
- Writing assertions that merely repeat the implementation.
- Forgetting to export the function being tested.
- Making tests depend on execution order or shared mutable state.

### Activities
1. Add tests for the canonical scores 82, 91, 76, and 88.
2. Add boundary tests for every grade threshold.
3. Add a test for invalid scores and decide what the function contract should be.
4. Run the test file from the terminal and interpret the pass/fail summary.

### Accessibility Practice
Read each test name and assertion result. Ensure failures identify the expected and actual values in text.

### Skills Checklist
- [ ] I can write a test with `node:test`.
- [ ] I can assert expected values.
- [ ] I can test normal and boundary cases.
- [ ] I can run tests from the terminal.

## Lesson 9.2: Testing a Class

### Reading References
- Python source counterpart: Unit 9, Lesson 9.2.
- Node.js documentation: Test runner and assert.

### Learning Objectives
- Test object construction, state changes, and methods.
- Verify both valid and invalid operations.
- Keep test cases independent.

### Concept Explanation
A class test verifies observable behavior of an instance: construction, method results, valid state changes, and rejected invalid changes.

### Worked Example
Assume `InventoryItem` exposes `quantity`, `updateQuantity()`, and `lineValue()`. A test file can verify its public behavior:

```javascript
const test = require("node:test");
const assert = require("node:assert/strict");
const { InventoryItem } = require("./inventory-item");

test("inventory item updates quantity and calculates value", () => {
  const item = new InventoryItem("Notebook", 3, 2.50);
  assert.equal(item.lineValue(), 7.50);
  item.updateQuantity(5);
  assert.equal(item.lineValue(), 12.50);
});

test("inventory item rejects a negative quantity", () => {
  const item = new InventoryItem("Pencil", 10, 0.50);
  assert.throws(() => item.updateQuantity(-1), RangeError);
});
```

Expected result: both tests pass when the class enforces its stated contract.

### Expected Behavior or Output
Both tests pass when the item value updates from $7.50 to $12.50 and a negative quantity throws RangeError.

### Common Mistakes
- Testing private implementation details instead of public behavior.
- Reusing one mutated instance across unrelated tests.
- Forgetting to test invalid state transitions.

### Activities
1. Test a Notebook item with quantity 3 and unit price 2.50.
2. Verify its line value after changing quantity to 5.
3. Verify that a negative quantity is rejected.
4. Add a test for a zero quantity and explain whether it is valid.

### Accessibility Practice
Give each test a descriptive name that states the behavior being verified. Avoid ambiguous test labels such as "test 1".

### Skills Checklist
- [ ] I can instantiate an object in a test.
- [ ] I can test a method's return value.
- [ ] I can test a state change.
- [ ] I can assert that invalid operations throw.

## Lesson 9.3: Introduction to Random Numbers

### Reading References
- Python source counterpart: Unit 9, Lesson 9.3.
- MDN: Math.random.

### Learning Objectives
- Generate random floating-point values and bounded integers.
- Select a random element from an array.
- Explain why random tests should not depend on a specific result.

### Concept Explanation
Math.random() returns a pseudorandom floating-point value greater than or equal to zero and less than one. Transform it to a bounded integer with multiplication and Math.floor().

### Worked Example
```javascript
const randomDecimal = Math.random();
const randomInteger = Math.floor(Math.random() * 10) + 1;

const colors = ["red", "blue", "green"];
const randomChoice = colors[Math.floor(Math.random() * colors.length)];

console.log(`Decimal in [0, 1): ${randomDecimal >= 0 && randomDecimal < 1}`);
console.log(`Integer in 1..10: ${randomInteger >= 1 && randomInteger <= 10}`);
console.log(`Selected item is valid: ${colors.includes(randomChoice)}`);
```

Expected output: three lines containing `true`; the sampled values vary on each run.

### Expected Behavior or Output
Each run prints true for all three range and membership checks; the sampled values may differ.

### Common Mistakes
- Assuming `Math.random()` can return exactly 1.
- Forgetting that `Math.floor()` is needed for an integer index.
- Writing a test that expects one particular random result.

### Activities
1. Generate a random integer from 1 through 10.
2. Select one of the canonical inventory item names.
3. Run the program several times and observe that values vary.
4. Explain why randomness makes exact-output tests unreliable without a controllable source.

### Accessibility Practice
Label the range and meaning of each random value. Never require a visual animation to observe a random result.

### Skills Checklist
- [ ] I can use `Math.random()`.
- [ ] I can generate a bounded integer.
- [ ] I can select a random array element.
- [ ] I can test properties of random output rather than one exact sample.

## Lesson 9.4: Analyzing Text Data

### Reading References
- Python source counterpart: Unit 9, Lesson 9.4.
- MDN: String and Map.

### Learning Objectives
- Normalize text before analysis.
- Count words and character frequencies.
- Use a Map to store frequency counts.

### Concept Explanation
Text analysis requires explicit normalization and tokenization rules. A Map stores each token and its current frequency; the regular expression in this example treats hyphenated words as separate alphabetic tokens.

### Worked Example
```javascript
const sample = "A student studies programming. Programming develops problem-solving skills.";

function countWords(text) {
  const words = text.toLowerCase().match(/[a-z]+/g) ?? [];
  const counts = new Map();

  for (const word of words) {
    counts.set(word, (counts.get(word) ?? 0) + 1);
  }
  return counts;
}

const frequencies = countWords(sample);
for (const [word, count] of frequencies) {
  console.log(`${word}: ${count}`);
}
```

Expected output:
```text
a: 1
student: 1
studies: 1
programming: 2
develops: 1
problem: 1
solving: 1
skills: 1
```

### Expected Behavior or Output
The sample produces nine tokens and eight distinct token keys; programming has frequency 2 and every other displayed token has frequency 1.

### Common Mistakes
- Counting uppercase and lowercase forms as separate words.
- Splitting on a single space and retaining punctuation.
- Assuming a simple regular expression handles every language's word boundaries.

### Activities
1. Count the words in the canonical text sample.
2. Identify the most frequent word.
3. Count characters after normalizing case.
4. Explain how punctuation and hyphenation affect the result.

### Accessibility Practice
Print each word and count as a labeled pair. State the normalization rules so learners can understand why the counts have those values.

### Skills Checklist
- [ ] I can normalize text before counting.
- [ ] I can tokenize a simple English text sample.
- [ ] I can store frequencies in a Map.
- [ ] I can explain limitations of a simple tokenizer.

## Lesson 9.5: Working with CSV Data

### Reading References
- Python source counterpart: Unit 9, Lesson 9.5.
- npm documentation: `csv-parse`.

### Learning Objectives
- Explain rows, columns, headers, and records.
- Read CSV data with a standards-aware parser.
- Compute a summary from the canonical column set.

### Concept Explanation
CSV is a text format with quoting and escaping rules. Splitting every line on commas is not a correct general CSV parser because a quoted field may itself contain a comma or newline. Use a maintained parser for real CSV data. The canonical headers are `student_id`, `first_name`, `last_name`, `score`, and `active`.

### Worked Example
Install the parser with `npm install csv-parse`. Save a small fixture as `students.csv`:
```csv
student_id,first_name,last_name,score,active
1,Avery,Student,91,true
2,Jordan,Lee,82,true
3,Casey,Smith,76,false
```

Read it with `csv-parse`:
```javascript
const fs = require("node:fs");
const { parse } = require("csv-parse/sync");

const records = parse(fs.readFileSync("students.csv", "utf8"), {
  columns: true,
  skip_empty_lines: true,
  trim: true
});

const average = records.reduce((sum, row) => sum + Number(row.score), 0)
  / records.length;

console.log(`Loaded students: ${records.length}`);
console.log(`Average score: ${average.toFixed(2)}`);
```

Expected output:
```text
Loaded students: 3
Average score: 83.00
```

### Expected Behavior or Output
The sample CSV contains three records with scores 91, 82, and 76. The average is 83.00.

### Common Mistakes
- Splitting CSV lines on commas without handling quoted fields.
- Forgetting that parsed field values are strings until converted.
- Assuming every row contains every required column.
- Failing to handle a missing or empty file.

### Activities
1. Create a CSV with the five canonical column names.
2. Load the records and print each student's name and score.
3. Calculate the average score.
4. Add a quoted field containing a comma and verify that the parser reads it as one field.

### Accessibility Practice
Print one record per line with column names. Provide a textual summary of any malformed rows rather than relying on a spreadsheet's visual highlighting.

### Skills Checklist
- [ ] I can explain CSV headers and records.
- [ ] I can parse CSV with a standards-aware library.
- [ ] I can convert numeric fields before calculating.
- [ ] I can summarize a dataset with labeled output.

# Unit 10: Project-Based Learning — Text-Based Applications

## Overview
The projects preserve the Python track's requirements and user interaction. The text adventure uses the same three rooms, exits, torch, magic key, and movement commands. The command-line to-do manager supports add, view, complete, delete, and JSON persistence.

## Lesson 10.1: Designing Your Project

### Reading References
- Python source counterpart: Unit 10, Lesson 10.1.
- MDN: JavaScript modules and functions.

### Learning Objectives
- Apply top-down design to a multi-part program.
- Identify inputs, outputs, data, and edge cases.
- Write pseudocode and acceptance tests before implementation.

### Concept Explanation
Top-down design breaks a large task into smaller responsibilities. The project should have separate functions for input, state changes, display, and persistence. Define command names and error behavior before writing code.

### Worked Example
Text-adventure pseudocode:
```text
CREATE rooms and exits
PLACE items in selected rooms
CREATE player at starting room
REPEAT
  DISPLAY current room and player status
  READ command
  VALIDATE command
  APPLY movement or inventory action
UNTIL player enters quit
```

### Expected Behavior or Output
The learner produces pseudocode, a room/command specification, and acceptance tests before implementation.

### Common Mistakes
- Starting implementation before defining the project requirements.
- Combining input, state changes, and display in one large function.
- Omitting invalid-command and boundary cases.

### Activities
1. Draw or describe the three-room map in text.
2. List every valid movement command and its destination.
3. Define the to-do manager's five menu operations.
4. Write at least five acceptance tests before implementation.

### Accessibility Practice
Use keyboard-operable commands, descriptive prompts, and predictable text output. Do not require maps, color, drag-and-drop, or mouse-only interaction.

### Skills Checklist
- [ ] I can decompose a project into functions or modules.
- [ ] I can define inputs and outputs.
- [ ] I can write pseudocode.
- [ ] I can define acceptance tests and error cases.

## Lesson 10.2: Building a Text-Based Adventure Game (Part 1)

### Reading References
- Python source counterpart: Unit 10, Lesson 10.2.
- Node.js documentation: readline/promises.

### Learning Objectives
- Model the five canonical rooms and their exits.
- Move through connected rooms without changing state on invalid directions.
- Explain the locked north exit from locked_door_room.

### Shared Project Specification
Use the canonical five-room graph: start_room north to tunnel; tunnel south to start_room and east to clearing; clearing west to tunnel and north to locked_door_room; locked_door_room south to clearing and conditionally north to treasure_room after using shiny key. The player starts in start_room. Valid commands include north, south, east, west, take shiny key, use shiny key, and quit.

### Concept Explanation
A room is represented by its identifier, description, and a map of valid exits. Movement looks up the requested direction and changes the player's current room only when the exit exists.

### Worked Example
```javascript
const rooms = {
  start_room: { exits: { north: "tunnel" }, items: ["shiny key"] },
  tunnel: { exits: { south: "start_room", east: "clearing" }, items: [] },
  clearing: { exits: { west: "tunnel", north: "locked_door_room" }, items: [] },
  locked_door_room: { exits: { south: "clearing" }, items: [] },
  treasure_room: { exits: {}, items: [] }
};
function move(currentRoom, direction) {
  return rooms[currentRoom].exits[direction] ?? null;
}
console.log(move("start_room", "north"));
console.log(move("start_room", "west"));
```

Expected output:
```text
tunnel
null
```

### Expected Behavior or Output
Moving north from start_room returns tunnel. Moving west from start_room returns null; the locked-door north exit is added only after the key puzzle is solved.

### Common Mistakes
- Adding an exit in one direction but forgetting the reverse connection.
- Accepting an exit that does not exist.
- Confusing a room key with its display name.

### Activities
1. Build the five canonical rooms and their unconditional exits.
2. Test north from start_room, east from tunnel, and north from clearing.
3. Test an invalid movement without changing the current room.
4. Add the conditional north exit from locked_door_room only after the key is used.

### Accessibility Practice
Announce the current room, description, and available exits in a consistent order. Never make the map available only as a graphic.

### Skills Checklist
- [ ] I can represent rooms and exits as objects.
- [ ] I can move between connected rooms.
- [ ] I can reject invalid directions.
- [ ] I can display room information sequentially.

## Lesson 10.3: Building a Text-Based Adventure Game (Part 2)

### Reading References
- Python source counterpart: Unit 10, Lesson 10.3.
- MDN: Array methods and object methods.

### Learning Objectives
- Place shiny key in start_room and transfer it to inventory exactly once.
- Require the key to be used in locked_door_room.
- Unlock the conditional north exit to treasure_room.

### Shared Project Specification
Place only the shiny key in start_room. The player uses `take shiny key` and `use shiny key`. The key must be used while in locked_door_room; this unlocks its north exit to treasure_room. Preserve these item names and rules across language tracks.

### Concept Explanation
An item belongs either to a room or to the player's inventory. Picking it up removes it from the room and adds it to inventory as one state transition.

### Worked Example
```javascript
const roomItems = { start_room: ["shiny key"], tunnel: [], clearing: [], locked_door_room: [], treasure_room: [] };
const inventory = [];
function takeItem(room, requestedName) {
  const items = roomItems[room];
  const index = items.findIndex(item => item.toLowerCase() === requestedName.toLowerCase());
  if (index < 0) return false;
  inventory.push(items.splice(index, 1)[0]);
  return true;
}
function useKey(room, items) {
  if (room !== "locked_door_room") return "You must be at the locked door to use the key.";
  if (!items.includes("shiny key")) return "The door is locked.";
  return "The door unlocks; north now leads to treasure_room.";
}
console.log(takeItem("start_room", "shiny key"));
console.log(inventory.join(", "));
console.log(useKey("clearing", inventory));
console.log(useKey("locked_door_room", inventory));
```

Expected output:
```text
true
torch
The gate is locked.
The gate opens.
```

### Expected Behavior or Output
Taking shiny key from start_room returns true and inventory contains shiny key. Using it outside locked_door_room is rejected; using it there unlocks the north exit.

### Common Mistakes
- Allowing an item to be picked up repeatedly after it has been removed.
- Failing to normalize item names consistently.
- Updating the room but not the inventory, or vice versa.

### Activities
1. Take shiny key from start_room.
2. Attempt to take it a second time and verify inventory does not change.
3. Attempt to use the key outside locked_door_room.
4. Use the key in locked_door_room and verify the north exit leads to treasure_room.

### Accessibility Practice
Confirm each successful pickup by item name. When pickup fails, explain whether the item is absent or the command is invalid.

### Skills Checklist
- [ ] I can store items in rooms.
- [ ] I can transfer an item to inventory.
- [ ] I can display inventory contents.
- [ ] I can implement and test a puzzle condition.

## Lesson 10.4: Developing a Command-Line To-Do Tool

### Reading References
- Python source counterpart: Unit 10, Lesson 10.4.
- Node.js documentation: File system and readline.

### Learning Objectives
- Implement add, view, complete, delete, and quit operations.
- Validate a one-based task number.
- Persist task data in JSON.

### Shared Project Specification
Each task has an identifier, description, completion state, and creation timestamp. The menu supports add task, view tasks, mark complete, delete, and quit. Save after every state-changing operation.

### Concept Explanation
A command-line task manager separates data operations from prompts and display. Task numbers shown to users are one-based, while array indexes are zero-based.

### Worked Example
Core task operations:
```javascript
function addTask(tasks, description, createdAt = new Date().toISOString()) {
  if (description.trim() === "") {
    throw new Error("Task description cannot be empty.");
  }
  tasks.push({
    id: tasks.length + 1,
    description: description.trim(),
    completed: false,
    createdAt
  });
}

function markComplete(tasks, taskNumber) {
  const index = taskNumber - 1;
  if (!Number.isInteger(taskNumber) || index < 0 || index >= tasks.length) {
    return false;
  }
  tasks[index].completed = true;
  return true;
}
```

### Expected Behavior or Output
A valid task description is added with completed false and a timestamp; a valid task number marks the corresponding task complete.

### Common Mistakes
- Confusing the user's one-based task number with a zero-based array index.
- Allowing empty descriptions.
- Saving only when the program exits, so an interrupted run loses changes.
- Reusing task identifiers after deletion without a documented policy.

### Activities
1. Add two tasks and view them in numbered order.
2. Mark the first task complete.
3. Delete the second task.
4. Save and reload the task list using JSON and verify the state persists.

### Accessibility Practice
Number every task and include an explicit completion label such as "complete" or "not complete". Confirm every add, update, and delete action in text.

### Skills Checklist
- [ ] I can add and display tasks.
- [ ] I can mark a task complete.
- [ ] I can delete a task by number.
- [ ] I can persist tasks as JSON.
- [ ] I can validate task descriptions and numbers.

## Lesson 10.5: Refinement and User Experience

### Reading References
- Python source counterpart: Unit 10, Lesson 10.5.
- Node.js documentation: Process exit codes and error handling.

### Learning Objectives
- Improve prompt clarity and validation.
- Test invalid commands and boundary cases.
- Review output for predictable keyboard and screen-reader use.

### Concept Explanation
A usable text program gives the same kind of response for the same kind of action. Prompts should state valid input, errors should explain the problem, and successful operations should confirm what changed. A help command should list every supported operation.

### Expected Behavior or Output
The refined application handles blank input, unknown commands, invalid record numbers, empty lists, and malformed stored data with explicit text messages.

### Worked Example
```javascript
function validateMenuChoice(choice) {
  const validChoices = ["add", "view", "search", "edit", "delete", "help", "quit"];
  if (!validChoices.includes(choice.trim().toLowerCase())) {
    return "Invalid choice. Enter add, view, search, edit, delete, help, or quit.";
  }
  return "Command accepted.";
}
console.log(validateMenuChoice("unknown"));
```

### Common Mistakes
- Printing "Invalid input" without explaining valid choices.
- Failing to confirm a successful action.
- Letting malformed stored data crash the entire program.
- Relying on visual formatting without textual labels.

### Activities
1. Add a help command to the to-do tool.
2. Test blank input, unknown commands, invalid task numbers, and an empty task list.
3. Review every prompt for a clear expected input format.
4. Ask a partner to complete all tasks using keyboard navigation only and record obstacles.

### Accessibility Practice
Use consistent separators, descriptive prompts, explicit errors, and sequential output. Do not claim a screen-reader test unless it has actually been performed.

### Skills Checklist
- [ ] I can validate user input.
- [ ] I can provide specific error messages.
- [ ] I can confirm successful operations.
- [ ] I can review a CLI for keyboard and screen-reader usability.

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

### Canonical Record Fields
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
