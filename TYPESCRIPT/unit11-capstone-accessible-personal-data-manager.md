# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

Integrate typed records, terminal interaction, persistence, CRUD, testing, and accessibility. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

---

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
