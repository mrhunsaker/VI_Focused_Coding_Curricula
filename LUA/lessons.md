# Lua 5.4 — Parallel Introductory Computer Science Course

## Course alignment and implementation notes

This course follows the Python canonical sequence in `lesson_standardization.json`. The shared problem contexts, inputs, records, boundaries, and expected results are preserved; Lua syntax and idioms are taught directly rather than transliterated from Python. Lua tables represent sequences, maps, and records; sequences are one-indexed; only `false` and `nil` are false; `pairs` does not guarantee order; `ipairs` traverses a consecutive sequence. Lua has no built-in class, tuple, continue statement, or JSON library. These differences are taught explicitly.

**Runtime:** Lua 5.4. Run a file with `lua5.4 filename.lua`; syntax-check with `luac5.4 -p filename.lua`. Use local variables by default. The Lua standard library does not include a JSON or general CSV parser; capstone persistence must declare and document an approved dependency (for example, dkjson), and CSV parsing must use a tested parser when quoted fields are in scope.

## Accessibility and lesson conventions

Use the terminal and keyboard for every exercise. Read code and output sequentially; describe braces, brackets, quotes, punctuation, and indentation in prose. Do not communicate status through color alone. Provide explicit prompts, errors, confirmations, and textual equivalents for any visual output. The course does not claim screen-reader or braille verification until those workflows have been tested on named platforms.

Each lesson includes a focused explanation, runnable worked example, expected behavior, common mistakes, practice, accessibility practice, and a skills check. Save each fenced example to a separate file or copy it into the Lua REPL.

# Unit 1: Foundations of Computing

## Overview

This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 1.1 Welcome to Computer Science

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Algorithms are precise sequences of steps. A computer follows instructions; it does not infer unstated intent.

### Worked Example

```lua
local steps = {"read the problem", "identify inputs", "plan steps", "test the result"}
for index, step in ipairs(steps) do
  print(index .. ". " .. step)
end
```

### Expected Behavior or Output

```text
1. read the problem
2. identify inputs
3. plan steps
4. test the result
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 1.1 Welcome to Computer Science worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 1.1 welcome to computer science.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 1.2 Your First Lua Program

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

The print function writes values to standard output. A Lua chunk executes statements in order.

### Worked Example

```lua
print("Hello, world!")
print("Lua statements run from top to bottom.")
```

### Expected Behavior or Output

```text
Hello, world!
Lua statements run from top to bottom.
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 1.2 Your First Lua Program worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 1.2 your first lua program.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 1.3 Variables and Simple Data Types

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua variables are dynamically typed. Use local for local scope; strings, numbers, and booleans are distinct values.

### Worked Example

```lua
local student = "Avery"
local age = 16
local height_m = 1.72
local favorite_subject = "Computer Science"
print(student, age, height_m, favorite_subject)
print(type(student), type(age), type(height_m), type(true))
```

### Expected Behavior or Output

```text
Avery	16	1.72	Computer Science
string	number	number	boolean
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 1.3 Variables and Simple Data Types worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 1.3 variables and simple data types.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

# Unit 2: Numeric Computations

## Overview

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
local tip_rate = 0.15
local tip_cents = math.floor(bill_cents * tip_rate + 0.5)
local total_cents = bill_cents + tip_cents
print(string.format("Tip: $%.2f", tip_cents / 100))
print(string.format("Total: $%.2f", total_cents / 100))
```

### Expected Behavior or Output

```text
Tip: $3.67
Total: $28.18
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
With input Avery: Hello, Avery!
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

# Unit 3: Control Flow — Decisions and Loops

## Overview

This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 3.1 Boolean Expressions and if Statements

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua treats only false and nil as false; zero and the empty string are truthy. Compare a score explicitly.

### Worked Example

```lua
local score = 82
if score >= 80 and score < 90 then
  print("Score is in the B range.")
end
```

### Expected Behavior or Output

```text
Score is in the B range.
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

## Lesson 3.2 Chained Conditionals

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Use an ordered if/elseif/else chain with the shared grade boundaries. Test boundary values as well as the sample scores.

### Worked Example

```lua
local function grade_for(score)
  if score >= 90 then return "A"
  elseif score >= 80 then return "B"
  elseif score >= 70 then return "C"
  elseif score >= 60 then return "D"
  else return "F" end
end
for _, score in ipairs({82, 91, 76, 88}) do
  print(score, grade_for(score))
end
```

### Expected Behavior or Output

```text
82	B
91	A
76	C
88	B
```

### Common Mistakes

- Checking lower grade thresholds before higher thresholds, causing scores to match the wrong branch.
- Using > where the shared boundary requires >=.
- Testing only the sample scores and omitting exact boundary values 90, 80, 70, 60, and 59.

### Activities

1. Trace each shared score (82, 91, 76, 88) through the conditional chain and record the selected grade.
2. Add tests for 90, 80, 70, 60, and 59; explain each branch taken.
3. Refactor the classifier into a local function and verify the four canonical outputs.
4. Compare the sum and average with 337 and 84.25; explain why the threshold order matters.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 3.3 Introduction to Lists

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua uses one-based sequence indices. Store the shared score sequence in an array-like table and update an element by index.

### Worked Example

```lua
local scores = {82, 91, 76, 88}
print(scores[1], scores[4], #scores)
scores[3] = 77
print(scores[3])
```

### Expected Behavior or Output

```text
82	88	4
77
```

### Common Mistakes

- Using index 0 for the first sequence element; Lua sequences start at index 1.
- Assuming #table counts sparse or map keys; it is reliable for a contiguous sequence.
- Using pairs where sequence order is required, or ipairs where arbitrary map keys are required.

### Activities

1. Print the first and last canonical score and explain the one-based indices.
2. Insert and remove one score, then show the sequence and its length.
3. Calculate the total and average with ipairs and compare with 337 and 84.25.
4. Create a sparse table and explain why # and ipairs do not provide a general map traversal.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 3.4 Iterating with for Loops

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

ipairs visits consecutive integer keys starting at 1. Use it to compute the shared score total and average.

### Worked Example

```lua
local scores = {82, 91, 76, 88}
local total = 0
for _, score in ipairs(scores) do total = total + score end
print("Total:", total)
print("Average:", total / #scores)
```

### Expected Behavior or Output

```text
Total:	337
Average:	84.25
```

### Common Mistakes

- Using index 0 for the first sequence element; Lua sequences start at index 1.
- Assuming #table counts sparse or map keys; it is reliable for a contiguous sequence.
- Using pairs where sequence order is required, or ipairs where arbitrary map keys are required.

### Activities

1. Print the first and last canonical score and explain the one-based indices.
2. Insert and remove one score, then show the sequence and its length.
3. Calculate the total and average with ipairs and compare with 337 and 84.25.
4. Create a sparse table and explain why # and ipairs do not provide a general map traversal.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 3.5 Basic String Operations

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua strings support methods through the string library. Normalize the canonical sentence before splitting it into words.

### Worked Example

```lua
local sentence = "A student studies programming. Programming develops problem-solving skills."
local normalized = string.lower(sentence)
local _, count = string.gsub(normalized, "[%w%-]+", "")
local _, programming_count = string.gsub(normalized, "programming", "")
print("Words:", count)
print("Programming:", programming_count)
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

# Unit 4: Data Structures — Lists and Dictionaries

## Overview

This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 4.1 More on Lists

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

table.insert appends or inserts at a position; table.remove deletes and returns an element. Preserve sequence order.

### Worked Example

```lua
local scores = {82, 91, 76, 88}
table.insert(scores, 2, 85)
local removed = table.remove(scores, 3)
print(table.concat(scores, ", "))
print("Removed:", removed)
```

### Expected Behavior or Output

```text
82, 85, 76, 88
Removed:	91
```

### Common Mistakes

- Using index 0 for the first sequence element; Lua sequences start at index 1.
- Assuming #table counts sparse or map keys; it is reliable for a contiguous sequence.
- Using pairs where sequence order is required, or ipairs where arbitrary map keys are required.

### Activities

1. Print the first and last canonical score and explain the one-based indices.
2. Insert and remove one score, then show the sequence and its length.
3. Calculate the total and average with ipairs and compare with 337 and 84.25.
4. Create a sparse table and explain why # and ipairs do not provide a general map traversal.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 4.2 Organizing Lists

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

table.sort sorts a sequence in place. Supply a comparator when descending order is required.

### Worked Example

```lua
local scores = {82, 91, 76, 88}
table.sort(scores)
print("Ascending:", table.concat(scores, ", "))
table.sort(scores, function(a, b) return a > b end)
print("Descending:", table.concat(scores, ", "))
```

### Expected Behavior or Output

```text
Ascending:	76, 82, 88, 91
Descending:	91, 88, 82, 76
```

### Common Mistakes

- Using index 0 for the first sequence element; Lua sequences start at index 1.
- Assuming #table counts sparse or map keys; it is reliable for a contiguous sequence.
- Using pairs where sequence order is required, or ipairs where arbitrary map keys are required.

### Activities

1. Print the first and last canonical score and explain the one-based indices.
2. Insert and remove one score, then show the sequence and its length.
3. Calculate the total and average with ipairs and compare with 337 and 84.25.
4. Create a sparse table and explain why # and ipairs do not provide a general map traversal.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 4.3 Tuples — Immutable-Style Values

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua has no built-in tuple type. Multiple assignment can bind coordinate values; do not mutate a value intended to be treated as a fixed pair.

### Worked Example

```lua
local x, y = 3, 4
local distance = math.sqrt(x * x + y * y)
print("Coordinates:", x, y)
print("Distance:", distance)
```

### Expected Behavior or Output

```text
Coordinates:	3	4
Distance:	5.0
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 4.3 Tuples — Immutable-Style Values worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 4.3 tuples — immutable-style values.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 4.4 Introducing Dictionaries

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

A Lua table can act as a map or record. Use named keys for inventory fields and numeric values for quantities and prices.

### Worked Example

```lua
local item = {name = "Notebook", quantity = 3, unit_price = 2.50}
print(item.name)
print(item.quantity)
print(string.format("$%.2f", item.unit_price))
```

### Expected Behavior or Output

```text
Notebook
3
$2.50
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 4.4 Introducing Dictionaries worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 4.4 introducing dictionaries.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 4.5 Looping Through Dictionaries

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

pairs iterates key-value entries without promising order. Use explicit keys or sort keys when output order matters.

### Worked Example

```lua
local inventory = {Notebook = 3, Pencil = 10, Folder = 4}
local names = {"Folder", "Notebook", "Pencil"}
table.sort(names)
for _, name in ipairs(names) do
  print(name, inventory[name])
end
```

### Expected Behavior or Output

```text
Folder	4
Notebook	3
Pencil	10
```

### Common Mistakes

- Using index 0 for the first sequence element; Lua sequences start at index 1.
- Assuming #table counts sparse or map keys; it is reliable for a contiguous sequence.
- Using pairs where sequence order is required, or ipairs where arbitrary map keys are required.

### Activities

1. Print the first and last canonical score and explain the one-based indices.
2. Insert and remove one score, then show the sequence and its length.
3. Calculate the total and average with ipairs and compare with 337 and 84.25.
4. Create a sparse table and explain why # and ipairs do not provide a general map traversal.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

# Unit 5: User Input and while Loops

## Overview

This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 5.1 How Input Works

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

io.read reads a line as text. Validate conversions before arithmetic; handle end-of-file explicitly.

### Worked Example

```lua
io.write("Enter a score: ")
local raw = io.read("*l")
local score = raw and tonumber(raw)
if score then print("Score:", score) else print("Please enter a number.") end
```

### Expected Behavior or Output

```text
With input 82: Score:	82
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

## Lesson 5.2 The while Loop in Action

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

A while loop repeats while its condition is true. Update the loop state so the condition eventually becomes false.

### Worked Example

```lua
local count = 1
while count <= 4 do
  print("Attempt", count)
  count = count + 1
end
print("Finished")
```

### Expected Behavior or Output

```text
Attempt	1
Attempt	2
Attempt	3
Attempt	4
Finished
```

### Common Mistakes

- Using index 0 for the first sequence element; Lua sequences start at index 1.
- Assuming #table counts sparse or map keys; it is reliable for a contiguous sequence.
- Using pairs where sequence order is required, or ipairs where arbitrary map keys are required.

### Activities

1. Print the first and last canonical score and explain the one-based indices.
2. Insert and remove one score, then show the sequence and its length.
3. Calculate the total and average with ipairs and compare with 337 and 84.25.
4. Create a sparse table and explain why # and ipairs do not provide a general map traversal.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 5.3 Flags and break

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

A Boolean flag records whether a search succeeded. break exits the loop as soon as the target is found.

### Worked Example

```lua
local scores = {82, 91, 76, 88}
local target = 91
local found = false
for index, score in ipairs(scores) do
  if score == target then
    found = true
    print("Found at index", index)
    break
  end
end
print("Found:", found)
```

### Expected Behavior or Output

```text
Found at index	2
Found:	true
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 5.3 Flags and break worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 5.3 flags and break.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 5.4 Using continue-equivalent logic

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua 5.4 has no continue keyword. Put the body in an if block to skip unwanted values without using a goto workaround.

### Worked Example

```lua
local scores = {82, -1, 91, 76}
for _, score in ipairs(scores) do
  if score >= 0 then print("Valid score:", score) end
end
```

### Expected Behavior or Output

```text
Valid score:	82
Valid score:	91
Valid score:	76
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 5.4 Using continue-equivalent logic worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 5.4 using continue-equivalent logic.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 5.5 Avoiding Infinite Loops

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

A loop needs a reachable termination condition and a state change. Check that the sentinel is handled before processing it.

### Worked Example

```lua
local commands = {"list", "done"}
local index = 1
while true do
  local command = commands[index]
  if command == "done" then break end
  print("Command:", command)
  index = index + 1
end
print("Menu closed")
```

### Expected Behavior or Output

```text
Command:	list
Menu closed
```

### Common Mistakes

- Using index 0 for the first sequence element; Lua sequences start at index 1.
- Assuming #table counts sparse or map keys; it is reliable for a contiguous sequence.
- Using pairs where sequence order is required, or ipairs where arbitrary map keys are required.

### Activities

1. Print the first and last canonical score and explain the one-based indices.
2. Insert and remove one score, then show the sequence and its length.
3. Calculate the total and average with ipairs and compare with 337 and 84.25.
4. Create a sparse table and explain why # and ipairs do not provide a general map traversal.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

# Unit 6: Functions

## Overview

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
local function calculate_total(bill_cents, rate)
  local tip_cents = math.floor(bill_cents * rate + 0.5)
  return tip_cents, bill_cents + tip_cents
end
local tip_cents, total_cents = calculate_total(2450, 0.15)
print(string.format("Tip: $%.2f", tip_cents / 100))
print(string.format("Total: $%.2f", total_cents / 100))
```

### Expected Behavior or Output

```text
Tip: $3.67
Total: $28.18
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

# Unit 8: Files and Exceptions

## Overview

This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 8.1 Reading from a File

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

io.open returns a file handle or nil plus an error message. Close files after reading; use a protected call or explicit cleanup on errors.

### Worked Example

```lua
local file, err = io.open("notes.txt", "r")
if not file then
  print("Could not open notes.txt:", err)
else
  local contents = file:read("*a")
  file:close()
  print(contents)
end
```

### Expected Behavior or Output

```text
When notes.txt contains Hello: Hello
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

## Lesson 8.2 Writing to a File

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Open with w to replace a file and a to append. Check the return value and close the handle.

### Worked Example

```lua
local file, err = io.open("notes.txt", "w")
if not file then error(err) end
file:write("Avery's programming notes\n")
file:close()
print("Saved notes.txt")
```

### Expected Behavior or Output

```text
Saved notes.txt
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

## Lesson 8.3 Handling Errors

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

pcall catches a runtime error and returns a success flag plus results. Validate user data before it reaches a risky operation.

### Worked Example

```lua
local ok, result = pcall(function()
  local value = assert(tonumber("not-a-number"), "score must be numeric")
  return value * 2
end)
print(ok)
print(string.find(result, "score must be numeric") ~= nil)
```

### Expected Behavior or Output

```text
false
[string "..."]:2: score must be numeric
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 8.3 Handling Errors worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 8.3 handling errors.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 8.4 Cleanup and Protected Calls

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua does not have Python's try/except/finally syntax. Use explicit cleanup and pcall; ensure resources are closed on both success and failure.

### Worked Example

```lua
local file = assert(io.open("notes.txt", "w"))
local ok, err = pcall(function() file:write("Saved safely\n") end)
file:close()
print("Write succeeded:", ok)
if not ok then print(err) end
```

### Expected Behavior or Output

```text
Write succeeded:	true
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 8.4 Cleanup and Protected Calls worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 8.4 cleanup and protected calls.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 8.5 JSON Data

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

JSON is not part of Lua's standard library. Use a documented dependency such as dkjson or another approved JSON module; keep the record schema independent of the library.

### Worked Example

```lua
local task = {
  id = 1, title = "Practice Lua",
  description = "Use the shared task schema",
  done = false, created_at = "2025-01-15T09:00:00Z"
}
print(task.id, task.title, task.done, task.created_at)
```

### Expected Behavior or Output

```text
1	Practice Lua	false	2025-01-15T09:00:00Z
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

# Unit 9: Testing and Data Analysis

## Overview

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
local function new_task(title)
  assert(title ~= nil and title ~= "", "title is required")
  return {title = title, done = false}
end
local task = new_task("Practice Lua")
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
print(table.concat(headers, ","))
local row = {"1001", "Avery", "Jordan", "82", "true"}
print(table.concat(row, ","))
```

### Expected Behavior or Output

```text
student_id,first_name,last_name,score,active
1001,Avery,Jordan,82,true
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

# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 10.1 Project Design and Requirements

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Translate requirements into data structures, commands, and acceptance tests before coding. This room graph is the common adventure map.

### Worked Example

```lua
local rooms = {
  start_room = {exits = {north = "tunnel"}},
  tunnel = {exits = {south = "start_room", east = "clearing"}},
  clearing = {exits = {west = "tunnel"}}
}
print(rooms.tunnel.exits.east)
```

### Expected Behavior or Output

```text
clearing
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

## Lesson 10.2 Adventure Game: Rooms and Movement

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Represent each room by a record containing description and exits. Reject movement when an exit is absent.

### Worked Example

```lua
local rooms = {
  start_room = {description = "Cave", exits = {north = "tunnel"}},
  tunnel = {description = "Tunnel", exits = {south = "start_room", east = "clearing"}},
  clearing = {description = "Clearing", exits = {west = "tunnel"}}
}
local current = "start_room"
local command = "north"
current = rooms[current].exits[command] or current
print(current, rooms[current].description)
```

### Expected Behavior or Output

```text
tunnel	Tunnel
```

### Common Mistakes

- Accepting a movement command that is not an exit from the current room.
- Removing an item before confirming it exists in the current room.
- Allowing the locked-door transition without checking both location and key possession.

### Activities

1. Trace movement from start_room to tunnel to clearing and back using only defined exits.
2. Attempt an invalid direction and confirm that the current room does not change.
3. Pick up the shiny key, inspect inventory, and verify it is removed from the room.
4. Attempt the puzzle without the key and then with the key; verify the win condition.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 10.3 Adventure Game: Inventory and Puzzle

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Inventory is a sequence table; room items are sequences too. A puzzle must check both player location and possession of the required item.

### Worked Example

```lua
local inventory = {}
local room_items = {"shiny key"}
local function take_key()
  for i, item in ipairs(room_items) do
    if item == "shiny key" then
      table.insert(inventory, item)
      table.remove(room_items, i)
      return true
    end
  end
  return false
end
print("Picked up key:", take_key())
print("Inventory:", table.concat(inventory, ", "))
```

### Expected Behavior or Output

```text
Picked up key:	true
Inventory:	shiny key
```

### Common Mistakes

- Treating a Lua table map as if it had a guaranteed iteration order.
- Confusing a missing key (nil) with a key whose value is false.
- Using the sequence length operator to count named inventory keys.

### Activities

1. Represent Notebook, Pencil, and Folder with name, quantity, and unit_price fields.
2. Calculate each line value and verify the shared inventory total of $17.50.
3. Add a missing-item lookup and print a clear message when the key is absent.
4. Sort a separate list of item names before displaying map values in deterministic order.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 10.4 Command-Line To-Do Manager

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

The task record must include id, title, description, done, and created_at. Keep CRUD operations separate from the input loop.

### Worked Example

```lua
local tasks = {}
local function add_task(id, title, description, created_at)
  assert(title ~= nil and title ~= "", "title is required")
  tasks[#tasks + 1] = {id = id, title = title, description = description,
    done = false, created_at = created_at}
end
add_task(1, "Practice Lua", "Complete the shared examples", "2025-01-15T09:00:00Z")
print(tasks[1].id, tasks[1].title, tasks[1].done)
```

### Expected Behavior or Output

```text
1	Practice Lua	false
```

### Common Mistakes

- Omitting one or more required task fields from a stored record.
- Using a list position as a permanent task identifier after deletion or reordering.
- Treating malformed persistence data as an empty task list without reporting the error.

### Activities

1. Create a task with all five canonical fields and list it in a stable format.
2. Update its done state, then search for it by identifier.
3. Delete an existing ID and attempt to delete a missing ID; compare the messages.
4. Save and reload the records, then verify every field is preserved.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 10.5 Refinement and Accessibility

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

A command-line application needs explicit help, validation, confirmations, and readable errors. Keep all critical information in text.

### Worked Example

```lua
local function validate_title(title)
  if title == nil or title:match("^%s*$") then
    return false, "Title is required; enter at least one non-space character."
  end
  return true, "Title accepted."
end
local ok, message = validate_title("   ")
print(message)
```

### Expected Behavior or Output

```text
Title is required; enter at least one non-space character.
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 10.5 Refinement and Accessibility worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 10.5 refinement and accessibility.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

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
local records = {{id = 1, title = "Notes", done = false}}
local function update_title(id, title)
  for _, record in ipairs(records) do
    if record.id == id then record.title = title; return true end
  end
  return false
end
print(update_title(1, "Revised notes"), records[1].title)
print(update_title(9, "Missing"))
```

### Expected Behavior or Output

```text
true	Revised notes
false
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
- Calculator: bill 24.50, tip rate 0.15; tip displays as $3.67 and total as $28.18.
- Grade thresholds: A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, otherwise F. Scores: 82, 91, 76, 88; total 337; average 84.25.
- Inventory: Notebook (3 at $2.50), Pencil (10 at $0.50), Folder (4 at $1.25); total $17.50.
- Coordinates: (3, 4); distance from origin 5.
- Text: `A student studies programming. Programming develops problem-solving skills.`
- CSV fields: `student_id, first_name, last_name, score, active`.
- To-do fields: `id, title, description, done, created_at`.
- Capstone fields: `id, title, description, category, created_at, updated_at`.

## Course projects and acceptance criteria

The text adventure uses the shared three-room graph `start_room` → `tunnel` → `clearing`, with the same reverse exits, movement commands, shiny-key inventory mechanic, locked-door puzzle, and win condition as the Python specification. The command-line to-do manager must implement create, list, update/complete, delete, save, and load with all five canonical fields. The capstone must implement list/display, add, search, update, delete, and persistence for the six-field record. A terminal interface is acceptable for Lua, but the data model, operations, acceptance tests, and keyboard/text accessibility requirements remain equivalent.

## AI and assessment integrity

AI must not write, complete, autocomplete, repair, or generate course code or assessment solutions. Students may use only instructor-authorized conceptual explanations that do not produce deliverable code. Do not recommend AI-generated code as a workflow or as a first draft.

## Validation status

The prior smoke-execution result applies to the previous version of this file, not this rewritten course. Run the Lua checker again, add exact expected-output fixtures for all 53 examples, and test project workflows and persistence before marking this course runtime- or output-verified.
