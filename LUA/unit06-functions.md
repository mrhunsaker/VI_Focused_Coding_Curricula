# Unit 6: Functions

## Overview

<<<<<<< HEAD
This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 6.1 Defining Functions

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Functions package a named operation. The function below calculates a tip and total from the canonical bill.

### Worked Example

```lua
local function calculate_total(bill_cents, rate_basis_points)
  -- 10,000 basis points = 100%; add 5,000 before integer division
  -- to implement half-up rounding to the nearest cent.
  local tip_cents = (bill_cents * rate_basis_points + 5000) // 10000
  return tip_cents, bill_cents + tip_cents
end
local tip_cents, total_cents = calculate_total(2450, 1500)
print(string.format("Tip: $%.2f", tip_cents / 100))
print(string.format("Total: $%.2f", total_cents / 100))
```

### Expected Behavior or Output

```text
Tip: $3.68
Total: $28.18
```8.18
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

## Lesson 6.2 Passing Arguments

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua uses positional arguments rather than Python-style keyword/default arguments. A nil parameter can be replaced with an explicit default.

### Worked Example

```lua
local function grade_for(score, passing_grade)
  passing_grade = passing_grade or "D"
  if score >= 60 then return passing_grade end
  return "F"
end
print(grade_for(75))
print(grade_for(75, "Pass"))
```

### Expected Behavior or Output

```text
D
Pass
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

## Lesson 6.3 Return Values

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

return sends values to the caller. Lua functions can return multiple values; capture them in matching local variables.

### Worked Example

```lua
local function summarize(values)
  local total = 0
  for _, value in ipairs(values) do total = total + value end
  return total, total / #values
end
local total, average = summarize({82, 91, 76, 88})
print(total, average)
```

### Expected Behavior or Output

```text
337	84.25
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

## Lesson 6.4 Functions with Tables

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Tables are passed by reference-like identity: mutating a table inside a function changes the same table the caller holds.

### Worked Example

```lua
local function add_score(scores, score)
  table.insert(scores, score)
end
local scores = {82, 91, 76, 88}
add_score(scores, 95)
print(#scores, scores[5])
```

### Expected Behavior or Output

```text
5	95
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

## Lesson 6.5 Variadic Functions

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

The ... expression captures variable arguments. Use select or a table pack when processing an arbitrary argument list.

### Worked Example

```lua
local function sum_all(...)
  local values = {...}
  local total = 0
  for _, value in ipairs(values) do total = total + value end
  return total
end
print(sum_all(82, 91, 76, 88))
```

### Expected Behavior or Output

```text
337
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
