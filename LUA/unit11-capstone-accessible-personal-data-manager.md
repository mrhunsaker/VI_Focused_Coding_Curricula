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
=======
Write checks and class tests, test random code by its properties, analyze the shared text sample, and read the shared CSV file.

## Lesson 9.1: Testing Functions

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 16 (Compilation, Execution, and Errors), assert
- Lua 5.4 Reference Manual: Section 6.1 (assert)
- Matching Python lesson: Lesson 9.1 Testing Your Code

### Learning Objectives
- Write small checks with expected results.
- Compare decimal results with a tolerance.
- Test boundary values.

### Concept Explanation
A *test* runs code with chosen inputs and compares the result to a value decided in advance. Lua's standard library has no test framework, so this course uses a tiny check function; larger projects often use a library such as `busted` or `luaunit` (not required here).

Decimal results are compared with a *tolerance*, not `==`, because of floating-point approximation: the tip for 24.50 at 0.15 is stored as 3.6749999999999998, so the test checks that the difference from 3.675 is smaller than a small number.

Test the same inputs in every language track: `add(5, 3)` is 8, `add(-5, -3)` is -8, `add(10, -4)` is 6, the tip is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F.

The program exits with a non-zero status if any check fails, which lets other tools notice the failure. `os.exit(1)` sets that status.

### Worked Example
```lua
local function add(a, b) return a + b end
local function calculate_tip(bill, rate) return bill * rate end
local function classify(score)
  if score >= 90 then return "A"
  elseif score >= 80 then return "B"
  elseif score >= 70 then return "C"
  elseif score >= 60 then return "D"
  end
  return "F"
end

local passed, failed = 0, 0
local function check(name, actual, expected, tolerance)
  local ok
  if tolerance then
    ok = math.abs(actual - expected) <= tolerance
  else
    ok = actual == expected
  end
  if ok then
    passed = passed + 1
    print("PASS " .. name)
  else
    failed = failed + 1
    print(string.format("FAIL %s: expected %s but got %s", name, tostring(expected), tostring(actual)))
  end
end

check("add 5 and 3", add(5, 3), 8)
check("add -5 and -3", add(-5, -3), -8)
check("add 10 and -4", add(10, -4), 6)
check("tip on 24.50 at 0.15", calculate_tip(24.5, 0.15), 3.675, 1e-9)
check("tip on a zero bill", calculate_tip(0, 0.15), 0)
check("classify 90", classify(90), "A")
check("classify 89", classify(89), "B")
check("classify 60", classify(60), "D")
check("classify 59", classify(59), "F")

print(string.format("%d passed, %d failed", passed, failed))
if failed > 0 then os.exit(1) end
```

### Expected Behavior or Output
The program prints:
```text
PASS add 5 and 3
PASS add -5 and -3
PASS add 10 and -4
PASS tip on 24.50 at 0.15
PASS tip on a zero bill
PASS classify 90
PASS classify 89
PASS classify 60
PASS classify 59
9 passed, 0 failed
```

### Common Mistakes
1. Comparing decimal results with `==`.
2. Testing only typical values and skipping boundaries such as 90, 89, 60, and 59.
3. Writing the expected value after seeing the output, which turns the test into a copy of the bug.

### Activities
1. Change one expected value so a check fails, and read the failure message. Then restore it.
2. Add checks for the grades at 80, 79, 70, and 69.
3. Write `check` calls for a function `is_passing(score)` before you write the function.
4. Explain why the tip check uses a tolerance.

### Accessibility Practice
Each check prints one complete line starting with PASS or FAIL, and the last line gives the counts, so the result can be understood by reading only the first word of each line and the final summary.

### Skills Checklist
- [ ] I can write a check with an expected value.
- [ ] I can compare decimals with a tolerance.
- [ ] I can choose boundary tests.
- [ ] I can read PASS and FAIL lines.
- [ ] I know how to signal failure with an exit status.

## Lesson 9.2: Testing Classes

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming)
- Lua 5.4 Reference Manual: Section 6.1 (pcall)
- Matching Python lesson: Lesson 9.2 Testing a Class

### Learning Objectives
- Create a fresh object for every test.
- Test attributes, methods, and error cases.
- Use `pcall` to test that an error occurs.

### Concept Explanation
Each test should start from a known state, so create a new object for every test with a *setup* function. Tests that share an object can influence each other and fail in confusing ways.

Test three things: that a method returns the right value (`total_value` for 3 at 2.50 is 7.5), that a method changes the object correctly (restocking 2 makes the quantity 5), and that invalid use is rejected (restocking a negative amount raises an error).

`pcall` runs a call and reports whether it raised an error, so a test can assert that an error *does* happen.

### Worked Example
```lua
local Item = {}
Item.__index = Item

function Item.new(name, quantity, unit_price)
  return setmetatable({name = name, quantity = quantity, unit_price = unit_price}, Item)
end
function Item:total_value() return self.quantity * self.unit_price end
function Item:restock(amount)
  if amount < 0 then error("amount must not be negative", 0) end
  self.quantity = self.quantity + amount
end

local function setup() return Item.new("Notebook", 3, 2.50) end

local failures = 0
local function test(name, body)
  local ok, err = pcall(body)
  if ok then
    print("PASS " .. name)
  else
    failures = failures + 1
    print("FAIL " .. name .. ": " .. tostring(err))
  end
end

test("total value is 7.5", function()
  assert(math.abs(setup():total_value() - 7.5) < 1e-9, "wrong total")
end)

test("restock adds to the quantity", function()
  local item = setup()
  item:restock(2)
  assert(item.quantity == 5, "quantity should be 5")
end)

test("restock rejects a negative amount", function()
  local ok = pcall(function() setup():restock(-1) end)
  assert(not ok, "an error should have been raised")
end)

print(failures == 0 and "All tests passed." or (failures .. " test(s) failed."))
```

### Expected Behavior or Output
The program prints:
```text
PASS total value is 7.5
PASS restock adds to the quantity
PASS restock rejects a negative amount
All tests passed.
```

### Common Mistakes
1. Sharing one object between tests so an earlier test changes the later ones.
2. Testing only the successful path and never the error path.
3. Forgetting that `assert` messages describe the failure; leaving them out makes failures hard to read.

### Activities
1. Add a test that `restock(0)` leaves the quantity unchanged.
2. Add a test for a method `is_valid` from Unit 7.
3. Break `restock` on purpose and read the failure line.
4. Explain why `setup` creates a new item each time.

### Accessibility Practice
Name each test with a short sentence that completes 'This test checks that ...' so the PASS and FAIL lines read as clear statements.

### Skills Checklist
- [ ] I can create a fresh object per test.
- [ ] I can test a return value.
- [ ] I can test a change of state.
- [ ] I can test that an error is raised.
- [ ] I can write a clear test name.

## Lesson 9.3: Random Numbers

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 3 (Numbers)
- Lua 5.4 Reference Manual: Section 6.7 (math.random and math.randomseed)
- Matching Python lesson: Lesson 9.3 Random Numbers and Simulation

### Learning Objectives
- Generate random integers and decimals.
- Use a seed to make results repeatable.
- Test random code by its properties.

### Concept Explanation
`math.random(m, n)` returns a random integer from m to n inclusive. `math.random()` returns a float from 0 up to but not including 1. `math.random(n)` returns an integer from 1 to n, which is convenient for choosing a list position: `scores[math.random(#scores)]`.

Lua 5.4 seeds the generator randomly at start-up. `math.randomseed(42)` sets a fixed seed, so a run with the same seed produces the same sequence. The exact numbers can differ between Lua versions, so tests should check *properties* (every roll is between 1 and 6) and repeatability, not particular values.

The example rolls a die many times, checks that every roll is in range, checks that two runs with the same seed match, and picks one of the shared scores at random.

### Worked Example
```lua
math.randomseed(42)
local first = {}
for i = 1, 5 do first[i] = math.random(1, 6) end

math.randomseed(42)
local second = {}
for i = 1, 5 do second[i] = math.random(1, 6) end

local same = true
for i = 1, 5 do
  if first[i] ~= second[i] then same = false end
end
print("Same seed gives the same rolls:", same)

local in_range = true
for _ = 1, 1000 do
  local roll = math.random(1, 6)
  if roll < 1 or roll > 6 then in_range = false end
end
print("All rolls between 1 and 6:", in_range)

local decimal = math.random()
print("Decimal in [0, 1):", decimal >= 0 and decimal < 1)

local scores = {82, 91, 76, 88}
local chosen = scores[math.random(#scores)]
local is_member = false
for _, score in ipairs(scores) do
  if score == chosen then is_member = true end
end
print("Chosen score is from the list:", is_member)
```

### Expected Behavior or Output
The program prints:
```text
Same seed gives the same rolls:	true
All rolls between 1 and 6:	true
Decimal in [0, 1):	true
Chosen score is from the list:	true
```

### Common Mistakes
1. Testing for specific random values that change between Lua versions.
2. Calling `math.randomseed` repeatedly inside a loop, which can repeat values.
3. Calling `math.random(0)` expecting an error range; in Lua 5.4 it returns a random integer with all bits random.

### Activities
1. Run the program three times and compare the output.
2. Change the seed and check that the property lines still print `true`.
3. Simulate 600 rolls and count how many of each face appeared (counts will differ).
4. Explain why a test should check a property instead of a number.

### Accessibility Practice
Print only yes or no style results for random behavior, so the announced output stays the same on every run and your screen reader does not read unpredictable values.

### Skills Checklist
- [ ] I can use `math.random` in three forms.
- [ ] I can set a seed.
- [ ] I can test properties of random code.
- [ ] I know values differ between versions.
- [ ] I can pick a random list item.

## Lesson 9.4: Text Analysis

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 11 (Interlude: Most Frequent Words) and Chapter 10 (Pattern Matching)
- Lua 5.4 Reference Manual: Section 6.4.1 (Patterns)
- Matching Python lesson: Lesson 9.4 Data Analysis - Text Analysis

### Learning Objectives
- Split text into words with `gmatch`.
- Count word and letter frequencies.
- Produce stable, sorted output.

### Concept Explanation
`text:gmatch(pattern)` returns an iterator over every match. The pattern `"%S+"` matches runs of non-space characters, which splits text into words. `%a` matches a letter, `%d` a digit, and `%s` whitespace.

To count words, store counts in a dictionary: `counts[word] = (counts[word] or 0) + 1`. Because `pairs` order is not stable, remember the first-seen order in a list (or sort the keys) before printing.

The shared text sample is "A student studies programming. Programming develops problem-solving skills." After lower-casing and removing periods it has 8 words, and `programming` appears twice. Letter counts are sorted by count (highest first) and then alphabetically so ties print in a fixed order.

### Worked Example
```lua
local text = "A student studies programming. Programming develops problem-solving skills."
local cleaned = text:lower():gsub("%.", "")

local order, counts, total_words = {}, {}, 0
for word in cleaned:gmatch("%S+") do
  total_words = total_words + 1
  if not counts[word] then
    counts[word] = 0
    order[#order + 1] = word
  end
  counts[word] = counts[word] + 1
end

print("Word count: " .. total_words)
print("Word frequencies:")
for _, word in ipairs(order) do
  print(string.format("'%s': %d", word, counts[word]))
end

local letters = {}
for letter in text:lower():gmatch("%a") do
  letters[letter] = (letters[letter] or 0) + 1
end
local letter_list = {}
for letter, count in pairs(letters) do letter_list[#letter_list + 1] = {letter = letter, count = count} end
table.sort(letter_list, function(a, b)
  if a.count ~= b.count then return a.count > b.count end
  return a.letter < b.letter
end)
print("Most common letters:")
for i = 1, 3 do
  print(string.format("%s: %d", letter_list[i].letter, letter_list[i].count))
end
```

### Expected Behavior or Output
The program prints:
```text
Word count: 8
Word frequencies:
'a': 1
'student': 1
'studies': 1
'programming': 2
'develops': 1
'problem-solving': 1
'skills': 1
Most common letters:
s: 7
e: 5
g: 5
```

### Common Mistakes
1. Forgetting that `gsub` returns two values and passing both to a function that expects one.
2. Printing a `pairs` traversal and getting a different order on another computer.
3. Counting punctuation as part of a word, so `programming.` and `programming` become different words.

### Activities
1. Predict the word count and the count for `programming` before running.
2. Count words longer than 8 letters.
3. Find the longest word and print it.
4. Change the sort so ties are listed in reverse alphabetical order.

### Accessibility Practice
Read the frequency list in its fixed order. Because the order is stable, you can learn it and compare runs by ear.

### Skills Checklist
- [ ] I can split text with `gmatch`.
- [ ] I can count frequencies.
- [ ] I can sort results so output is stable.
- [ ] I can use `%a`, `%s`, and `%S`.
- [ ] I can clean punctuation from text.

## Lesson 9.5: Working with CSV Files

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 15 (Data Files and Serialization)
- Lua 5.4 Reference Manual: Section 6.4.1 (Patterns)
- Matching Python lesson: Lesson 9.5 Data Analysis - CSV Files

### Learning Objectives
- Create and read a CSV file.
- Split a line into fields.
- Compute an average and a count from the data.

### Concept Explanation
A CSV (comma-separated values) file stores a table as text. The first line names the columns and each later line is one record. The shared student file has the columns `student_id`, `first_name`, `last_name`, `score`, and `active`, and three records.

Lua has no CSV reader in the standard library. A simple splitter finds each run of characters up to the next comma. This works only for *simple* files. A value that contains a comma inside quotation marks (for example `"Smith, Jr."`) will be split wrongly; for such files, use a maintained library or write a proper parser.

Every field is text. Convert the score with `tonumber` and compare the `active` field with the text `"true"`. With scores 91, 82, and 76 the average is 83.00, and two students are active.

### Worked Example
```lua
local file = assert(io.open("students.csv", "w"))
file:write("student_id,first_name,last_name,score,active\n")
file:write("1,Avery,Student,91,true\n")
file:write("2,Jordan,Lee,82,true\n")
file:write("3,Casey,Smith,76,false\n")
file:close()

local function split(line, separator)
  local fields = {}
  for field in (line .. separator):gmatch("([^" .. separator .. "]*)" .. separator) do
    fields[#fields + 1] = field
  end
  return fields
end

local input, message = io.open("students.csv", "r")
if not input then
  print("Error: students.csv was not found. " .. message)
  return
end

local header = split(input:read("l"), ",")
print("Columns: " .. table.concat(header, ", "))

local total, count, active = 0, 0, 0
for line in input:lines() do
  local row = split(line, ",")
  local score = tonumber(row[4])
  total = total + score
  count = count + 1
  if row[5] == "true" then active = active + 1 end
  print(string.format("%s: %s %s scored %d", row[1], row[2], row[3], score))
end
input:close()

print("Students: " .. count)
print(string.format("Average score: %.2f", total / count))
print("Active students: " .. active)
```

### Expected Behavior or Output
The program prints:
```text
Columns: student_id, first_name, last_name, score, active
1: Avery Student scored 91
2: Jordan Lee scored 82
3: Casey Smith scored 76
Students: 3
Average score: 83.00
Active students: 2
```

### Common Mistakes
1. Splitting a CSV line at every comma when a value itself contains a quoted comma.
2. Forgetting to convert the text in the score column to a number.
3. Not checking for an empty last line, which gives a row with missing fields.

### Activities
1. Predict the printed lines before running.
2. Add a fourth student and check the new average.
3. Print only the active students.
4. Explain, with an example, why `"Smith, Jr."` breaks the simple splitter.

### Accessibility Practice
Print one student per line with the same wording, so the screen reader announces a repeating pattern that is easy to compare line by line.

### Skills Checklist
- [ ] I can write and read a CSV file.
- [ ] I can split a line into fields.
- [ ] I convert text fields to numbers.
- [ ] I can compute an average and a count.
- [ ] I know when a simple splitter is not enough.

## Overview

Build a personal data manager with the shared record schema, JSON storage, search and completion, acceptance tests, and a documentation and accessibility check.

## Lesson 11.1: Capstone: Requirements and Design

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables) and Chapter 6 (Functions)
- Lua 5.4 Reference Manual: Section 3.4.9 (Table Constructors)
- Matching Python lesson: Lesson 11.1 Capstone Project - Planning

### Learning Objectives
- Write requirements for a personal data manager.
- Define the shared record schema.
- Check records against validation rules before building features.

### Concept Explanation
The capstone is a *personal data manager*: a program that keeps a list of records, lets the user add, view, search, update, complete, and delete them, and saves them to a file. In the Lua track it is a text program, so it runs from the terminal and is fully usable with a screen reader or braille display.

**Shared record schema (all general-purpose language tracks).** Every record has `id` (unique whole number), `title`, `description`, `category`, `created_at`, and `updated_at` (ISO 8601 text). A project may add fields, such as an optional `done` flag, but must not remove these.

**Shared sample data.** The three records in the example are used for demonstrations and tests.

**Validation rules.** A record must have a non-empty title and a non-empty category. Timestamps are ISO 8601 text such as `2026-01-15T09:00:00`.

Design before coding: list the operations, then the data, then the messages. The example checks the sample records against the rules and prints them as a plain-text list.

### Worked Example
```lua
local sample = {
  {id = 1, title = "Notebook", description = "Course notes", category = "supplies",
   created_at = "2026-01-15T09:00:00", updated_at = "2026-01-15T09:00:00"},
  {id = 2, title = "Pencil", description = "Box of 10", category = "supplies",
   created_at = "2026-01-15T09:05:00", updated_at = "2026-01-15T09:05:00"},
  {id = 3, title = "Study plan", description = "Weekly schedule", category = "planning",
   created_at = "2026-01-15T09:10:00", updated_at = "2026-01-15T09:10:00"},
}

local function validate(record)
  if type(record.title) ~= "string" or record.title:match("^%s*$") then
    return false, "A title is required."
  end
  if type(record.category) ~= "string" or record.category:match("^%s*$") then
    return false, "A category is required."
  end
  return true
end

for _, record in ipairs(sample) do
  local ok, message = validate(record)
  print(string.format("%d. %s [%s] - %s", record.id, record.title, record.category, ok and "valid" or message))
end

print(select(2, validate({title = "  ", category = "supplies"})))
print(select(2, validate({title = "Ruler", category = ""})))
```

### Expected Behavior or Output
The program prints:
```text
1. Notebook [supplies] - valid
2. Pencil [supplies] - valid
3. Study plan [planning] - valid
A title is required.
A category is required.
```

### Common Mistakes
1. Starting to build features before agreeing on the record fields.
2. Allowing a record with an empty title because the check was left for later.
3. Storing timestamps in different formats in different places.

### Activities
1. Write the six operations as a numbered list of requirements.
2. Add one project-specific field to the schema and say how it is validated.
3. Write three sample records for your own project.
4. Describe, in plain sentences, what each of the shared fields means.

### Accessibility Practice
Design the screen output as lines of plain text: one record per line, with the same field order each time. Decide the wording of every message now so it can be tested.

### Skills Checklist
- [ ] I can write requirements.
- [ ] I know the shared record fields.
- [ ] I can write validation rules.
- [ ] I can describe sample data.
- [ ] I can plan messages before coding.

## Lesson 11.2: Capstone: Data Model and Storage

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 15 (Data Files and Serialization)
- Lua 5.4 Reference Manual: Section 6.8 (Input and Output Facilities)
- Matching Python lesson: Lesson 11.2 Capstone Project - Core Features (Part 1)

### Learning Objectives
- Store records in a list of tables.
- Save and load records as JSON.
- Confirm that every field survives a round trip.

### Concept Explanation
Records are stored as a list of tables in memory and as a JSON array on disk. Using one format everywhere keeps the program simple. The storage layer has two functions: `save_records(path, records)` and `load_records(path)`. Loading returns `nil` and a message when the file is missing or damaged, so the caller decides what to do.

The example uses the shared three sample records and the teaching JSON helper from Lesson 8.5 (included so the program runs on its own). After saving and reloading, it compares every field of every record to confirm that nothing changed. This *round-trip test* is the first acceptance test for storage.

### Worked Example
```lua
local json = {}

local escapes = {['"'] = '\\"', ['\\'] = '\\\\', ['\n'] = '\\n', ['\r'] = '\\r', ['\t'] = '\\t'}

function json.encode(value)
  local kind = type(value)
  if kind == "string" then
    return '"' .. value:gsub('[%c"\\]', function(c)
      return escapes[c] or string.format("\\u%04x", c:byte())
    end) .. '"'
  elseif kind == "number" then
    return math.type(value) == "integer" and tostring(value) or string.format("%.14g", value)
  elseif kind == "boolean" then
    return tostring(value)
  elseif kind == "nil" then
    return "null"
  elseif kind == "table" then
    local parts = {}
    if value[1] ~= nil or next(value) == nil then
      for _, item in ipairs(value) do parts[#parts + 1] = json.encode(item) end
      return "[" .. table.concat(parts, ",") .. "]"
    end
    local keys = {}
    for key in pairs(value) do keys[#keys + 1] = key end
    table.sort(keys)
    for _, key in ipairs(keys) do
      parts[#parts + 1] = json.encode(tostring(key)) .. ":" .. json.encode(value[key])
    end
    return "{" .. table.concat(parts, ",") .. "}"
  end
  error("cannot encode a value of type " .. kind, 0)
end

function json.decode(text)
  local position = 1
  local read_value

  local function skip()
    position = text:find("%S", position) or #text + 1
  end

  local function fail(message)
    error(message .. " at position " .. position, 0)
  end

  local function read_string()
    local pieces = {}
    position = position + 1
    while true do
      local c = text:sub(position, position)
      if c == "" then fail("unterminated string") end
      if c == '"' then
        position = position + 1
        return table.concat(pieces)
      elseif c == "\\" then
        local n = text:sub(position + 1, position + 1)
        local simple = {n = "\n", t = "\t", r = "\r", ['"'] = '"', ["\\"] = "\\", ["/"] = "/"}
        if n == "u" then
          pieces[#pieces + 1] = utf8.char(tonumber(text:sub(position + 2, position + 5), 16))
          position = position + 6
        elseif simple[n] then
          pieces[#pieces + 1] = simple[n]
          position = position + 2
        else
          fail("bad escape")
        end
      else
        pieces[#pieces + 1] = c
        position = position + 1
      end
    end
  end

  function read_value()
    skip()
    local c = text:sub(position, position)
    if c == "{" then
      local object = {}
      position = position + 1
      skip()
      if text:sub(position, position) == "}" then position = position + 1; return object end
      while true do
        skip()
        if text:sub(position, position) ~= '"' then fail("expected a key") end
        local key = read_string()
        skip()
        if text:sub(position, position) ~= ":" then fail("expected ':'") end
        position = position + 1
        object[key] = read_value()
        skip()
        local d = text:sub(position, position)
        position = position + 1
        if d == "}" then return object end
        if d ~= "," then position = position - 1; fail("expected ',' or '}'") end
      end
    elseif c == "[" then
      local list = {}
      position = position + 1
      skip()
      if text:sub(position, position) == "]" then position = position + 1; return list end
      while true do
        list[#list + 1] = read_value()
        skip()
        local d = text:sub(position, position)
        position = position + 1
        if d == "]" then return list end
        if d ~= "," then position = position - 1; fail("expected ',' or ']'") end
      end
    elseif c == '"' then
      return read_string()
    elseif text:find("^true", position) then
      position = position + 4; return true
    elseif text:find("^false", position) then
      position = position + 5; return false
    elseif text:find("^null", position) then
      position = position + 4; return nil
    end
    local number = text:match("^-?%d+%.?%d*[eE]?[+-]?%d*", position)
    if not number or number == "" then fail("unexpected character") end
    position = position + #number
    return tonumber(number)
  end

  local result = read_value()
  skip()
  if position <= #text then fail("unexpected extra text") end
  return result
end

local sample = {
  {id = 1, title = "Notebook", description = "Course notes", category = "supplies",
   created_at = "2026-01-15T09:00:00", updated_at = "2026-01-15T09:00:00"},
  {id = 2, title = "Pencil", description = "Box of 10", category = "supplies",
   created_at = "2026-01-15T09:05:00", updated_at = "2026-01-15T09:05:00"},
  {id = 3, title = "Study plan", description = "Weekly schedule", category = "planning",
   created_at = "2026-01-15T09:10:00", updated_at = "2026-01-15T09:10:00"},
}

local function save_records(path, records)
  local file, message = io.open(path, "w")
  if not file then return false, message end
  file:write(json.encode(records))
  file:close()
  return true
end

local function load_records(path)
  local file, message = io.open(path, "r")
  if not file then return nil, "Could not open " .. path .. ": " .. message end
  local text = file:read("a")
  file:close()
  local ok, data = pcall(json.decode, text)
  if not ok or type(data) ~= "table" then return nil, "The data file is not valid JSON." end
  return data
end

print(save_records("records.json", sample))
local loaded, problem = load_records("records.json")

local same = #loaded == #sample
for index, record in ipairs(sample) do
  for key, value in pairs(record) do
    if loaded[index][key] ~= value then same = false end
  end
end
print("Round trip preserved all fields:", same)
print("Records loaded: " .. #loaded)

print(select(2, load_records("missing.json")))

local bad = assert(io.open("broken.json", "w"))
bad:write('[{"id": 1,')
bad:close()
print(select(2, load_records("broken.json")))
```

### Expected Behavior or Output
The program prints:
```text
true
Round trip preserved all fields:	true
Records loaded: 3
Could not open missing.json: missing.json: No such file or directory
The data file is not valid JSON.
```

### Common Mistakes
1. Overwriting the data file with an empty list after a failed load.
2. Saving only some of the fields.
3. Assuming a loaded record has every field without checking.

### Activities
1. Run the program and open `records.json` to read the saved text.
2. Add a `done` field to the sample and confirm that it survives the round trip.
3. Make `load_records` check that each record has an `id` and a `title`.
4. Explain why `load_records` returns a message and does not raise an error.

### Accessibility Practice
Messages that name the file and the problem read clearly in speech. After saving, read the file in the terminal to confirm that it contains what you expect.

### Skills Checklist
- [ ] I can store records in a list of tables.
- [ ] I can save and load JSON.
- [ ] I can run a round-trip test.
- [ ] I handle missing and damaged files.
- [ ] I do not overwrite good data after a failed load.

## Lesson 11.3: Capstone: Core Operations

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming)
- Lua 5.4 Reference Manual: Section 6.6 (Table Manipulation)
- Matching Python lesson: Lesson 11.3 Capstone Project - Core Features (Part 2)

### Learning Objectives
- Add, list, search, update, complete, and delete records.
- Assign new ids and update timestamps correctly.
- Return a message when an operation cannot be done.

### Concept Explanation
A `Manager` object holds the records and offers one method per operation. Each method that can fail returns `nil` and a message, so the user interface can show it and decide what to do. New ids are one more than the highest id, so ids are never reused while higher ids exist. Updating a record sets `updated_at` but never changes `created_at`. Completing a record sets the optional `done` field to `true` and counts as an update.

For repeatable output the example passes in a *fake clock* that returns a new fixed time on every call. A real program passes a function that reads the real time, for example `os.date("!%Y-%m-%dT%H:%M:%S")`.

The example adds the three shared sample records, lists them, searches for "note", updates one description, completes one record, deletes one, and tries to delete a record that does not exist.

### Worked Example
```lua
local function trim(text) return (text:gsub("^%s*(.-)%s*$", "%1")) end

local function validate(record)
  if type(record.title) ~= "string" or trim(record.title) == "" then
    return false, "A title is required."
  end
  if type(record.category) ~= "string" or trim(record.category) == "" then
    return false, "A category is required."
  end
  return true
end

local Manager = {}
Manager.__index = Manager

function Manager.new(clock)
  return setmetatable({records = {}, clock = clock}, Manager)
end

function Manager:next_id()
  local highest = 0
  for _, record in ipairs(self.records) do
    if record.id > highest then highest = record.id end
  end
  return highest + 1
end

function Manager:find(id)
  for index, record in ipairs(self.records) do
    if record.id == id then return record, index end
  end
  return nil
end

function Manager:add(title, description, category)
  local ok, message = validate({title = title, category = category})
  if not ok then return nil, message end
  local stamp = self.clock()
  local record = {
    id = self:next_id(), title = trim(title), description = trim(description or ""),
    category = trim(category), done = false, created_at = stamp, updated_at = stamp,
  }
  self.records[#self.records + 1] = record
  return record
end

function Manager:update(id, changes)
  local record = self:find(id)
  if not record then return nil, "No record has that id." end
  local ok, message = validate({title = changes.title or record.title, category = changes.category or record.category})
  if not ok then return nil, message end
  for key, value in pairs(changes) do
    if key ~= "id" and key ~= "created_at" then record[key] = value end
  end
  record.updated_at = self.clock()
  return record
end

function Manager:complete(id)
  return self:update(id, {done = true})
end

function Manager:delete(id)
  local record, index = self:find(id)
  if not record then return false, "No record has that id." end
  table.remove(self.records, index)
  return true
end

function Manager:search(text)
  local needle, found = text:lower(), {}
  for _, record in ipairs(self.records) do
    if record.title:lower():find(needle, 1, true) or record.description:lower():find(needle, 1, true) then
      found[#found + 1] = record
    end
  end
  return found
end

local ticks = 0
local function fake_clock()
  ticks = ticks + 1
  return string.format("2026-01-15T10:00:%02d", ticks)
end

local function show(manager)
  for _, record in ipairs(manager.records) do
    print(string.format("%d. %s [%s] (%s)", record.id, record.title, record.category, record.done and "done" or "not done"))
  end
end

local manager = Manager.new(fake_clock)
manager:add("Notebook", "Course notes", "supplies")
manager:add("Pencil", "Box of 10", "supplies")
manager:add("Study plan", "Weekly schedule", "planning")
show(manager)

print("Search for 'note':")
for _, record in ipairs(manager:search("note")) do print(record.title) end

manager:update(2, {description = "Box of 12"})
manager:complete(3)
print(manager:find(2).description, manager:find(2).updated_at)
print(manager:delete(1))
print(manager:delete(99))
show(manager)
```

### Expected Behavior or Output
The program prints:
```text
1. Notebook [supplies] (not done)
2. Pencil [supplies] (not done)
3. Study plan [planning] (not done)
Search for 'note':
Notebook
Box of 12	2026-01-15T10:00:04
true
false	No record has that id.
2. Pencil [supplies] (not done)
3. Study plan [planning] (done)
```

### Common Mistakes
1. Reusing a deleted record's id by counting the list length instead of using the highest id.
2. Changing `created_at` when updating a record.
3. Raising an error for a missing record where a message to display is more helpful.

### Activities
1. Predict the output before running.
2. Add a `list_by_category(category)` method.
3. Add a rule that blocks completing a record that is already complete, with a message.
4. Explain how the fake clock makes the output repeatable.

### Accessibility Practice
List output uses the same fixed format for every record and uses the words `done` and `not done`. Search results print only titles, so each line is short.

### Skills Checklist
- [ ] I can implement add, list, search, update, complete, and delete.
- [ ] I assign unique ids.
- [ ] I update timestamps correctly.
- [ ] I return clear messages for failures.
- [ ] I can make output repeatable with a fake clock.

## Lesson 11.4: Capstone: Validation and Acceptance Tests

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 16 (Compilation, Execution, and Errors)
- Lua 5.4 Reference Manual: Section 6.1 (assert and pcall)
- Matching Python lesson: Lesson 11.4 Capstone Project - Testing and Refinement

### Learning Objectives
- Run the shared acceptance tests.
- Verify that validation rejects bad data.
- Read and interpret test results.

### Concept Explanation
The shared acceptance tests describe behavior that every language track's capstone must show:

1. Adding a record with an empty title is rejected with a clear message.
2. A new record receives an unused `id`.
3. Updating a record changes `updated_at` but not `created_at`.
4. Deleting a record removes only that record.
5. Saving and reloading preserves all fields and values (shown in Lesson 11.2).
6. Every message and control can be used without color or a mouse (checked by hand in Lesson 11.5).

This lesson automates tests 1 to 4 and also tests that completing a record updates it. Each test builds a new `Manager`, so tests cannot affect each other. The fake clock keeps timestamps predictable, which lets a test check that `updated_at` changed while `created_at` did not.

### Worked Example
```lua
local function trim(text) return (text:gsub("^%s*(.-)%s*$", "%1")) end

local function validate(record)
  if type(record.title) ~= "string" or trim(record.title) == "" then
    return false, "A title is required."
  end
  if type(record.category) ~= "string" or trim(record.category) == "" then
    return false, "A category is required."
  end
  return true
end

local Manager = {}
Manager.__index = Manager

function Manager.new(clock)
  return setmetatable({records = {}, clock = clock}, Manager)
end

function Manager:next_id()
  local highest = 0
  for _, record in ipairs(self.records) do
    if record.id > highest then highest = record.id end
  end
  return highest + 1
end

function Manager:find(id)
  for index, record in ipairs(self.records) do
    if record.id == id then return record, index end
  end
  return nil
end

function Manager:add(title, description, category)
  local ok, message = validate({title = title, category = category})
  if not ok then return nil, message end
  local stamp = self.clock()
  local record = {
    id = self:next_id(), title = trim(title), description = trim(description or ""),
    category = trim(category), done = false, created_at = stamp, updated_at = stamp,
  }
  self.records[#self.records + 1] = record
  return record
end

function Manager:update(id, changes)
  local record = self:find(id)
  if not record then return nil, "No record has that id." end
  local ok, message = validate({title = changes.title or record.title, category = changes.category or record.category})
  if not ok then return nil, message end
  for key, value in pairs(changes) do
    if key ~= "id" and key ~= "created_at" then record[key] = value end
  end
  record.updated_at = self.clock()
  return record
end

function Manager:complete(id)
  return self:update(id, {done = true})
end

function Manager:delete(id)
  local record, index = self:find(id)
  if not record then return false, "No record has that id." end
  table.remove(self.records, index)
  return true
end

function Manager:search(text)
  local needle, found = text:lower(), {}
  for _, record in ipairs(self.records) do
    if record.title:lower():find(needle, 1, true) or record.description:lower():find(needle, 1, true) then
      found[#found + 1] = record
    end
  end
  return found
end

local ticks = 0
local function fake_clock()
  ticks = ticks + 1
  return string.format("2026-01-15T10:00:%02d", ticks)
end

local failures = 0
local function test(name, body)
  local ok, err = pcall(body)
  if ok then
    print("PASS " .. name)
  else
    failures = failures + 1
    print("FAIL " .. name .. ": " .. tostring(err))
  end
end

local function fresh()
  ticks = 0
  local manager = Manager.new(fake_clock)
  manager:add("Notebook", "Course notes", "supplies")
  manager:add("Pencil", "Box of 10", "supplies")
  manager:add("Study plan", "Weekly schedule", "planning")
  return manager
end

test("1. an empty title is rejected", function()
  local manager = fresh()
  local record, message = manager:add("   ", "x", "supplies")
  assert(record == nil and message == "A title is required.", "expected the title message")
  assert(#manager.records == 3, "the list should be unchanged")
end)

test("2. a new record gets an unused id", function()
  local manager = fresh()
  manager:delete(2)
  local record = manager:add("Ruler", "30 cm", "supplies")
  assert(record.id == 4, "expected id 4 but got " .. record.id)
end)

test("3. update changes updated_at but not created_at", function()
  local manager = fresh()
  local before = {created = manager:find(1).created_at, updated = manager:find(1).updated_at}
  manager:update(1, {description = "Lecture notes"})
  assert(manager:find(1).created_at == before.created, "created_at changed")
  assert(manager:find(1).updated_at ~= before.updated, "updated_at did not change")
end)

test("4. delete removes only that record", function()
  local manager = fresh()
  manager:delete(2)
  assert(#manager.records == 2 and manager:find(1) and manager:find(3) and not manager:find(2), "wrong records remain")
end)

test("5. complete marks done and updates the record", function()
  local manager = fresh()
  local record = manager:complete(3)
  assert(record.done == true and record.updated_at ~= record.created_at, "completion not recorded")
end)

test("6. a blank title cannot be saved by update", function()
  local manager = fresh()
  local record, message = manager:update(1, {title = ""})
  assert(record == nil and message == "A title is required.", "update accepted a blank title")
end)

print(failures == 0 and "All acceptance tests passed." or (failures .. " test(s) failed."))
```

### Expected Behavior or Output
The program prints:
```text
PASS 1. an empty title is rejected
PASS 2. a new record gets an unused id
PASS 3. update changes updated_at but not created_at
PASS 4. delete removes only that record
PASS 5. complete marks done and updates the record
PASS 6. a blank title cannot be saved by update
All acceptance tests passed.
```

### Common Mistakes
1. Sharing one manager between tests, so one test's deletions change the next test.
2. Checking only that no error occurred, and not checking the result.
3. Writing the expected message differently from the program, so a correct program fails the test.

### Activities
1. Break `Manager:update` so it also changes `created_at` and watch test 3 fail. Restore it.
2. Add a test that searching is case-insensitive.
3. Add a test that deleting an unknown id returns `false` and a message.
4. Explain why test 2 deletes record 2 before adding the new one.

### Accessibility Practice
The test names begin with the acceptance-test number, so the PASS and FAIL lines can be matched to the specification. Read only the first word of each line to hear the overall result quickly.

### Skills Checklist
- [ ] I can run the shared acceptance tests.
- [ ] I can test validation failures.
- [ ] I can test timestamps with a fake clock.
- [ ] I can read PASS and FAIL lines.
- [ ] I use a fresh manager for every test.

## Lesson 11.5: Capstone: Documentation and Presentation

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 16 (Compilation, Execution, and Errors)
- [Unit P, Lesson P.6](../FOUNDATIONS/unit-p-computing-foundations.md): files, data formats, and the shared accessible workflow
- Matching Python lesson: Lesson 11.5 Capstone Project - Final Submission

### Learning Objectives
- Write a plain-text project summary.
- Report a count of records by category.
- Complete a manual accessibility check.

### Concept Explanation
Documentation tells a future reader what the program does and how to run it. Write it as plain text or Markdown with short headings, numbered steps, and complete sentences. Include: the purpose of the program, the command that starts it, the shared record fields, the commands a user can give, the accessibility checks you carried out, and what you would improve next.

The example generates a summary from the shared sample data. It counts records by category and prints the categories in alphabetical order so the output is stable. It then prints the manual accessibility checklist. The unchecked boxes `[ ]` are for *you* to complete by hand with your own access technology; the program cannot verify them.

Acceptance test 6 is a manual check: every message and control can be used without color or a mouse. Test it with the keyboard only, and with the screen reader or braille display you actually use. Record what you tested and its version; do not claim compatibility with software you did not test.

### Worked Example
```lua
local sample = {
  {id = 1, title = "Notebook", description = "Course notes", category = "supplies",
   created_at = "2026-01-15T09:00:00", updated_at = "2026-01-15T09:00:00"},
  {id = 2, title = "Pencil", description = "Box of 10", category = "supplies",
   created_at = "2026-01-15T09:05:00", updated_at = "2026-01-15T09:05:00"},
  {id = 3, title = "Study plan", description = "Weekly schedule", category = "planning",
   created_at = "2026-01-15T09:10:00", updated_at = "2026-01-15T09:10:00"},
}

local counts, categories = {}, {}
for _, record in ipairs(sample) do
  if not counts[record.category] then
    counts[record.category] = 0
    categories[#categories + 1] = record.category
  end
  counts[record.category] = counts[record.category] + 1
end
table.sort(categories)

print("Personal Data Manager - Summary")
print("Records: " .. #sample)
print("Categories:")
for _, category in ipairs(categories) do
  print(string.format("- %s: %d", category, counts[category]))
end

print("")
print("Manual accessibility checklist (complete this by hand):")
local checks = {
  "[ ] Every command can be used with the keyboard only.",
  "[ ] Every message is a complete sentence that says what to do next.",
  "[ ] No meaning depends on color, position, or symbols alone.",
  "[ ] The output was read with my own screen reader or braille display.",
  "[ ] I recorded the operating system, program, and version I tested.",
}
for _, check in ipairs(checks) do print(check) end
```

### Expected Behavior or Output
The program prints:
```text
Personal Data Manager - Summary
Records: 3
Categories:
- planning: 1
- supplies: 2

Manual accessibility checklist (complete this by hand):
[ ] Every command can be used with the keyboard only.
[ ] Every message is a complete sentence that says what to do next.
[ ] No meaning depends on color, position, or symbols alone.
[ ] The output was read with my own screen reader or braille display.
[ ] I recorded the operating system, program, and version I tested.
```

### Common Mistakes
1. Writing documentation that only the author can follow.
2. Claiming that a program is accessible without recording what was tested and how.
3. Letting the documentation drift from the program after later changes.

### Activities
1. Write the project summary for your own capstone using the headings above.
2. Run the keyboard-only check and record each problem you find.
3. Ask a classmate to follow your run instructions from a fresh folder and note where they get stuck.
4. Write three improvements for the next version, ordered by user benefit.

### Accessibility Practice
This is the final accessibility lesson. Read your own documentation aloud from start to finish. Anything you have to look at the screen to understand needs rewriting.

### Skills Checklist
- [ ] I can write a plain-text project summary.
- [ ] I can report counts by category.
- [ ] I can run a manual accessibility check.
- [ ] I record what I tested.
- [ ] I do not claim untested compatibility.

## Course-Wide Assessment and Portfolio

Submit runnable exercises, prediction and debugging notes, tests, a text adventure, a command-line to-do manager, and a personal-data manager. Assessment focuses on correct behavior, idiomatic Lua, clear table and function design, independent debugging, and code explanation.

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)
