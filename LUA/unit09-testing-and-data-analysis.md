# Unit 9: Testing and Data Analysis

## Overview

<<<<<<< HEAD
This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 9.1 Testing a Function

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Assertions make expected behavior executable. Test the shared score average and the exact tip calculation.

### Worked Example

```lua
local function average(values)
  local total = 0
  for _, value in ipairs(values) do total = total + value end
  return total / #values
end
assert(average({82, 91, 76, 88}) == 84.25)
print("average test passed")
```

### Expected Behavior or Output

```text
average test passed
```

### Common Mistakes

- Forgetting that a Lua function returns nil when it reaches the end without return.
- Confusing multiple return values with a single table result.
- Assuming Python keyword arguments or default-parameter syntax exists in Lua.

### Activities

1. Call the function with the canonical values and record every returned value.
2. Add a second return value and capture it explicitly at the call site.
3. Test a missing optional argument and apply a deliberate default.
4. Pass a table to the function, mutate it, and explain the shared table identity.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 9.2 Testing a Table-Based Object

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Test observable state changes on an object-like table. Include both normal and invalid cases.

### Worked Example

```lua
local function new_task(id, title, description, created_at)
  assert(type(id) == "number", "id must be numeric")
  assert(type(title) == "string" and title:match("%S"), "title is required")
  assert(type(description) == "string", "description must be text")
  assert(type(created_at) == "string", "created_at must be text")
  return {
    id = id,
    title = title,
    description = description,
    done = false,
    created_at = created_at
  }
end
local task = new_task(1, "Practice Lua", "Complete the shared exercises",
  "2025-01-15T09:00:00Z")
assert(task.done == false)
task.done = true
assert(task.done == true)
print("task tests passed")
```

### Expected Behavior or Output

```text
task tests passed
```

### Common Mistakes

- Describing Lua as having a built-in class keyword; this course uses tables and metatables.
- Forgetting that colon method syntax passes self as the first argument.
- Creating an __index chain without explaining which table supplies the missing method.

### Activities

1. Create two independent records using the constructor and compare their fields.
2. Add one method and call it with colon syntax, then show the equivalent explicit self call.
3. Extend the example with a composed record and read a nested field.
4. Trace method lookup through the metatable chain and explain the result.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 9.3 Random Numbers

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

math.random generates pseudorandom values. math.randomseed can make a sequence repeatable for a lesson or test.

### Worked Example

```lua
math.randomseed(12345)
local die = math.random(1, 6)
print("Die roll is in range:", die >= 1 and die <= 6)
```

### Expected Behavior or Output

```text
Die roll is in range:	true
```

### Common Mistakes

- Expecting an unseeded pseudorandom sequence to reproduce exactly across runs.
- Using a random value without checking the required range.
- Seeding repeatedly inside a tight loop, which can reduce randomness.

### Activities

1. Generate an integer in the range 1 through 6 and assert both bounds.
2. Seed once before a reproducibility demonstration and compare two controlled runs.
3. Generate a random selection from the canonical score list.
4. Explain why a statistical test should not require one specific unseeded value.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 9.4 Analyzing Text Data

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Count tokens in the canonical text sample. Lua patterns are not full regular expressions; document the pattern being used.

### Worked Example

```lua
local text = "A student studies programming. Programming develops problem-solving skills."
local normalized = string.lower(text)
local words = {}
for word in string.gmatch(normalized, "[%w%-]+") do
  words[#words + 1] = word
end
local count = 0
for _, word in ipairs(words) do if word == "programming" then count = count + 1 end end
print("Words:", #words)
print("Programming:", count)
```

### Expected Behavior or Output

```text
Words:	8
Programming:	2
```

### Common Mistakes

- Assuming Lua patterns are full regular expressions.
- Forgetting that string functions return additional values such as match counts.
- Changing case or punctuation inconsistently before counting words.

### Activities

1. Normalize the exact canonical text sample and list the tokens in order.
2. Count all eight words and verify that programming occurs twice.
3. Add punctuation and a hyphenated word; explain the chosen pattern behavior.
4. Read the output as plain text and explain how the counts were obtained.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 9.5 Working with CSV Data

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

CSV fields can contain quoted commas and escaped quotes; naive string splitting is not a correct general CSV parser. Use a vetted CSV library for production data.

### Worked Example

```lua
local headers = {"student_id", "first_name", "last_name", "score", "active"}
local rows = {
  {"1001", "Avery", "Jordan", "82", "true"},
  {"1002", "Riley", "Chen", "91", "true"},
  {"1003", "Sam", "Patel", "76", "false"},
  {"1004", "Morgan", "Diaz", "88", "true"}
}
print(table.concat(headers, ","))
for _, row in ipairs(rows) do
  print(table.concat(row, ","))
end
```

### Expected Behavior or Output

```text
student_id,first_name,last_name,score,active
1001,Avery,Jordan,82,true
1002,Riley,Chen,91,true
1003,Sam,Patel,76,false
1004,Morgan,Diaz,88,true
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
