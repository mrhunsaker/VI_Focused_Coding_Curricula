# Unit 2: Numeric Computations

## Overview

<<<<<<< HEAD
This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 2.1 The Software Development Process

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Plan, implement, and test the same tip-calculator problem. Separate input values from the calculation and presentation.

### Worked Example

```lua
local bill_cents = 2450
local tip_rate_percent = 15
-- Integer arithmetic avoids binary floating-point rounding errors.
local tip_cents = (bill_cents * tip_rate_percent + 50) // 100
local total_cents = bill_cents + tip_cents
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

- Using binary floating-point display rounding as a substitute for a currency-rounding policy.
- Skipping parentheses when operator precedence is not obvious.
- Assuming tonumber succeeds for every string.

### Activities

1. Calculate the shared $24.50 bill and 15% tip using integer cents and half-up rounding.
2. Trace each arithmetic intermediate and compare the displayed tip and total with $3.68 and $28.18.
3. Try a nonnumeric string and handle a nil conversion result.
4. Use coordinates (3, 4) to calculate distance 5 and explain the math-library call.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 2.2 Expressions and Assignment

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua uses arithmetic operators and parentheses for precedence. Assignment updates a variable; it is not an equality test.

### Worked Example

```lua
local score = 50
score = score + 20
local expression = 10 / 2 + 3
print("Score:", score)
print("Expression:", expression)
```

### Expected Behavior or Output

```text
Score:	70
Expression:	8.0
```

### Common Mistakes

- Using binary floating-point display rounding as a substitute for a currency-rounding policy.
- Skipping parentheses when operator precedence is not obvious.
- Assuming tonumber succeeds for every string.

### Activities

1. Calculate the shared $24.50 bill and 15% tip using integer cents and half-up rounding.
2. Trace each arithmetic intermediate and compare the displayed tip and total with $3.68 and $28.18.
3. Try a nonnumeric string and handle a nil conversion result.
4. Use coordinates (3, 4) to calculate distance 5 and explain the math-library call.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 2.3 Input and Output Revisited

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

io.read returns text or nil at end-of-file. Convert numeric text with tonumber and validate the conversion.

### Worked Example

```lua
io.write("Enter your name: ")
local name = io.read("*l")
if name == nil or name == "" then name = "Avery" end
print("Hello, " .. name .. "!")
```

### Expected Behavior or Output

```text
Enter your name: Hello, Avery!
```

### Common Mistakes

- Assuming io.read always returns a non-empty string; it can return nil at end-of-file.
- Calling tonumber and immediately doing arithmetic without checking for nil.
- Treating terminal input as already numeric.

### Activities

1. Run the prompt with a valid numeric string and record the converted Lua type.
2. Run it with alphabetic input and confirm that the program prints a useful error rather than crashing.
3. Simulate end-of-file and handle the nil result explicitly.
4. Explain the difference between the raw string and the converted number.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 2.4 Computing with Numbers and Type Conversions

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

tonumber converts valid numeric text and returns nil for invalid text. tostring converts values to text.

### Worked Example

```lua
local raw = "16"
local age = tonumber(raw)
if age then
  print(age + 1)
else
  print("Enter a valid number.")
end
print(tostring(16) .. " years")
```

### Expected Behavior or Output

```text
17
16 years
```

### Common Mistakes

- Using binary floating-point display rounding as a substitute for a currency-rounding policy.
- Skipping parentheses when operator precedence is not obvious.
- Assuming tonumber succeeds for every string.

### Activities

1. Calculate the shared $24.50 bill and 15% tip using integer cents and half-up rounding.
2. Trace each arithmetic intermediate and compare the displayed tip and total with $3.68 and $28.18.
3. Try a nonnumeric string and handle a nil conversion result.
4. Use coordinates (3, 4) to calculate distance 5 and explain the math-library call.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 2.5 Using the Math Library

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

The math library supplies sqrt and pi. Use the canonical coordinates (3, 4) to calculate distance from the origin.

### Worked Example

```lua
local x, y = 3, 4
local distance = math.sqrt(x * x + y * y)
local radius = 3
local circumference = 2 * math.pi * radius
print(distance)
print(string.format("%.2f", circumference))
```

### Expected Behavior or Output

```text
5.0
18.85
```

### Common Mistakes

- Using binary floating-point display rounding as a substitute for a currency-rounding policy.
- Skipping parentheses when operator precedence is not obvious.
- Assuming tonumber succeeds for every string.

### Activities

1. Calculate the shared $24.50 bill and 15% tip using integer cents and half-up rounding.
2. Trace each arithmetic intermediate and compare the displayed tip and total with $3.68 and $28.18.
3. Try a nonnumeric string and handle a nil conversion result.
4. Use coordinates (3, 4) to calculate distance 5 and explain the math-library call.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---
