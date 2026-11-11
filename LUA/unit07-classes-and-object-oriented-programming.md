# Unit 7: Classes and Object-Oriented Programming

## Overview

This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 7.1 Why Learn About Classes?

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua has no class keyword. Tables and functions can model state and behavior; a metatable can provide method lookup.

### Worked Example

```lua
local student = {name = "Avery", age = 16}
local function describe(record)
  return record.name .. " is " .. record.age
end
print(describe(student))
```

### Expected Behavior or Output

```text
Avery is 16
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

## Lesson 7.2 Creating and Using a Class

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

A constructor function creates records with a shared shape. This is a common lightweight Lua object pattern.

### Worked Example

```lua
local function Student(name, age)
  return {name = name, age = age}
end
local a = Student("Avery", 16)
local b = Student("Riley", 17)
print(a.name, b.name)
```

### Expected Behavior or Output

```text
Avery	Riley
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

## Lesson 7.3 Attributes and Methods

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

A method is a function stored on a table. The colon syntax passes self as the first argument.

### Worked Example

```lua
local Item = {}
function Item:new(name, quantity)
  return setmetatable({name = name, quantity = quantity}, {__index = self})
end
function Item:display()
  print(self.name .. ": " .. self.quantity)
end
local notebook = Item:new("Notebook", 3)
notebook:display()
```

### Expected Behavior or Output

```text
Notebook: 3
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

## Lesson 7.4 Inheritance and Metatables

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Metatable __index can delegate missing method lookups to a parent table. Explain this lookup behavior rather than implying Lua has built-in classes.

### Worked Example

```lua
local Base = {kind = "record"}
function Base:describe() return self.name .. " (" .. self.kind .. ")" end
local Student = setmetatable({}, {__index = Base})
local a = setmetatable({name = "Avery", kind = "student"}, {__index = Student})
print(a:describe())
```

### Expected Behavior or Output

```text
Avery (student)
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

## Lesson 7.5 Composition

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Composition stores one record inside another. This is often simpler than building a deep inheritance hierarchy.

### Worked Example

```lua
local profile = {name = "Avery", contact = {email = "avery@example.test"}}
print(profile.name)
print(profile.contact.email)
```

### Expected Behavior or Output

```text
Avery
avery@example.test
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
