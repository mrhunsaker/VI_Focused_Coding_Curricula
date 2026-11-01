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


# Unit 1: Foundations of Computing

## Overview

Introduce computer science, first programs, variables, and primitive types. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

---

