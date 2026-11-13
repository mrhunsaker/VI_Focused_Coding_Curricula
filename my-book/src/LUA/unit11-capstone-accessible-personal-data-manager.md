# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 11.1 Requirements and Interface Design

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Separate the core data model from the interface. A terminal interface is an appropriate Lua implementation while preserving the shared user-facing requirements.

### Worked Example

```lua
local required_fields = {"id", "title", "description", "category", "created_at", "updated_at"}
for _, field in ipairs(required_fields) do print(field) end
```

### Expected Behavior or Output

```text
id
title
description
category
created_at
updated_at
```

### Common Mistakes

- Dropping one of the six required capstone record fields during serialization.
- Updating a record without refreshing updated_at.
- Claiming screen-reader compatibility without testing keyboard and assistive-technology workflows.

### Activities

1. Create a record containing all six canonical capstone fields and validate each field.
2. Exercise add, list, search, update, and delete with both existing and missing IDs.
3. Save and reload a record; compare every field before and after persistence.
4. Write a text-only keyboard interaction guide and list the accessibility tests still required.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 11.2 Data Model and Storage

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

The capstone record has six required fields. Validate them before storage; keep timestamps in a consistent documented format.

### Worked Example

```lua
local record = {
  id = 1, title = "Programming notes",
  description = "Review lists and dictionaries",
  category = "Study",
  created_at = "2025-01-15T09:00:00Z",
  updated_at = "2025-01-15T09:00:00Z"
}
print(record.id, record.title, record.category)
```

### Expected Behavior or Output

```text
1	Programming notes	Study
```

### Common Mistakes

- Ignoring the second return value from io.open when a file cannot be opened.
- Leaving a file handle open after a successful or failed operation.
- Assuming Lua includes a standard JSON or full CSV parser.

### Activities

1. Test the file operation with an existing file and a missing-file path.
2. Add an explicit failure message using the error returned by io.open.
3. Close the file on every control path and explain the resource-lifetime rule.
4. Document the selected JSON/CSV dependency and test malformed and quoted-field inputs.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 11.3 Create, Read, Update, Delete

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Implement CRUD as separate functions. Updating a record should also update updated_at; deleting a missing ID should return a clear status.

### Worked Example

```lua
local records = {{
  id = 1,
  title = "Programming notes",
  description = "Review lists and dictionaries",
  category = "Study",
  created_at = "2025-01-15T09:00:00Z",
  updated_at = "2025-01-15T09:00:00Z"
}}
local function find_record(id)
  for _, record in ipairs(records) do
    if record.id == id then return record end
  end
  return nil
end
local function update_title(id, title, updated_at)
  local record = find_record(id)
  if not record then return false end
  record.title = title
  record.updated_at = updated_at
  return true
end
local function delete_record(id)
  for index, record in ipairs(records) do
    if record.id == id then
      table.remove(records, index)
      return true
    end
  end
  return false
end
local found = find_record(1)
print("Found:", found.title, found.category)
print("Updated:", update_title(1, "Revised notes", "2025-01-16T09:00:00Z"))
print("Updated title:", records[1].title)
print("Deleted:", delete_record(1))
print("Missing delete:", delete_record(9))
```

### Expected Behavior or Output

```text
Found:	Programming notes	Study
Updated:	true
Updated title:	Revised notes
Deleted:	true
Missing delete:	false
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 11.3 Create, Read, Update, Delete worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 11.3 create, read, update, delete.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 11.4 Validation and Tests

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Test required fields, duplicate identifiers, not-found behavior, and persistence failures. Assertions should verify results, not merely execute examples.

### Worked Example

```lua
local function valid_record(record)
  return type(record.id) == "number"
    and type(record.title) == "string" and record.title ~= ""
    and type(record.description) == "string"
    and type(record.category) == "string"
    and type(record.created_at) == "string"
    and type(record.updated_at) == "string"
end
assert(valid_record({id=1,title="A",description="B",category="C",created_at="now",updated_at="now"}))
print("record validation passed")
```

### Expected Behavior or Output

```text
record validation passed
```

### Common Mistakes

- Dropping one of the six required capstone record fields during serialization.
- Updating a record without refreshing updated_at.
- Claiming screen-reader compatibility without testing keyboard and assistive-technology workflows.

### Activities

1. Create a record containing all six canonical capstone fields and validate each field.
2. Exercise add, list, search, update, and delete with both existing and missing IDs.
3. Save and reload a record; compare every field before and after persistence.
4. Write a text-only keyboard interaction guide and list the accessibility tests still required.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 11.5 Documentation and Presentation

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Document installation, launch commands, data format, keyboard interaction, errors, and known limitations. A screen-reader claim requires hands-on testing.

### Worked Example

```lua
local help = {
  "Commands: list, add, search, update, delete, save, load, help, quit",
  "All actions report success or a textual error.",
  "Records use the shared six-field capstone schema."
}
for _, line in ipairs(help) do print(line) end
```

### Expected Behavior or Output

```text
Commands: list, add, search, update, delete, save, load, help, quit
All actions report success or a textual error.
Records use the shared six-field capstone schema.
```

### Common Mistakes

- Dropping one of the six required capstone record fields during serialization.
- Updating a record without refreshing updated_at.
- Claiming screen-reader compatibility without testing keyboard and assistive-technology workflows.

### Activities

1. Create a record containing all six canonical capstone fields and validate each field.
2. Exercise add, list, search, update, and delete with both existing and missing IDs.
3. Save and reload a record; compare every field before and after persistence.
4. Write a text-only keyboard interaction guide and list the accessibility tests still required.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Runnable Reference Implementation

The repository includes a tested Lua domain and JSON-storage reference core in [capstone/README.md](capstone/README.md). Install the JSON dependency and run the acceptance suite from the repository root using:

`luarocks install dkjson && lua LUA/capstone/test_records.lua`

The reference core does not replace the requirement to build and evaluate an accessible user interface.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Canonical shared data contract

The following values must remain identical to the Python source and the other general-purpose tracks:

- Student: Avery, age 16, height 1.72 meters, favorite subject Computer Science.
- Calculator: bill 24.50, tip rate 0.15; round half-up to the nearest cent; tip displays as $3.68 and total as $28.18.
- Grade thresholds: A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, otherwise F. Scores: 82, 91, 76, 88; total 337; average 84.25.
- Inventory: Notebook (3 at $2.50), Pencil (10 at $0.50), Folder (4 at $1.25); total $17.50.
- Coordinates: (3, 4); distance from origin 5.
- Text: `A student studies programming. Programming develops problem-solving skills.`
- CSV fields: `student_id, first_name, last_name, score, active`.
- To-do fields: `id, title, description, done, created_at`.
- Capstone fields: `id, title, description, category, created_at, updated_at`.

## Course projects and acceptance criteria

The text adventure uses the shared five-room graph: `start_room` (north → `tunnel`, shiny key), `tunnel` (south → `start_room`, east → `clearing`), `clearing` (west → `tunnel`, north → `locked_door_room`), `locked_door_room` (south → `clearing`, north → `treasure_room` only after unlocking), and terminal `treasure_room`. The player takes the shiny key in `start_room`, travels to `locked_door_room`, uses the key there, and enters `treasure_room` to win. Commands are `north`, `south`, `east`, `west`, `take shiny key`, `use shiny key`, and `quit`. The command-line to-do manager must implement create, list, update/complete, delete, save, and load with all five canonical fields. The capstone must implement list/display, add, search, update, delete, and persistence for the six-field record. A terminal interface is acceptable for Lua, but the data model, operations, acceptance tests, and keyboard/text accessibility requirements remain equivalent.

## AI and assessment integrity

AI must not write, complete, autocomplete, repair, or generate course code or assessment solutions. Students may use only instructor-authorized conceptual explanations that do not produce deliverable code. Do not recommend AI-generated code as a workflow or as a first draft.

## Validation status

The earlier smoke-execution result applies only to the previous version of this file. The current checker now compares exact stdout for all 53 lesson examples; run the updated Lua 5.4 workflow and complete end-to-end project/persistence tests before marking the projects verified.
