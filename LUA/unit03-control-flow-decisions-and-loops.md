# Unit 3: Control Flow — Decisions and Loops

## Overview

Make decisions with `if`/`elseif`, classify the shared scores with the shared grade thresholds, and learn tables as lists, loops, and strings.

## Lesson 3.1: Boolean Expressions and if Statements

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (Getting Started), the sections on control structures
- Lua 5.4 Reference Manual: Section 3.3.4 (Control Structures)
- Matching Python lesson: Lesson 3.1 Boolean Expressions and if Statements

### Learning Objectives
- Write comparisons and combine them with `and`, `or`, and `not`.
- Use `if` ... `then` ... `else` ... `end`.
- Explain which Lua values count as false.

### Concept Explanation
A *Boolean expression* is true or false. Comparison operators are `==`, `~=`, `<`, `<=`, `>`, and `>=`. Conditions combine with `and`, `or`, and `not`.

An `if` statement runs a block when its condition is true: `if condition then ... end`, with an optional `else`. Every `if` closes with `end`.

Lua's rule for truth is unusual and important: **only `nil` and `false` count as false.** The number 0, the empty string `""`, and an empty table are all *true*. Programmers used to other languages often expect 0 to be false.

`and` and `or` return one of their operands rather than always `true` or `false`. `a and b` returns `a` if `a` is false, otherwise `b`. `a or b` returns `a` if `a` is true, otherwise `b`. The idiom `condition and "yes" or "no"` therefore works as a one-line choice, provided the "yes" value is never `nil` or `false`.

The shared score is 82. It passes (at least 60), it falls between 80 and 89, and it is not at least 90.

### Worked Example
```lua
local score = 82

if score >= 60 then
  print("Avery passed.")
else
  print("Avery did not pass.")
end

print(score >= 80 and score < 90)
print(score < 60 or score > 100)
print(not (score >= 90))

if 0 then print("0 counts as true") end
if "" then print("the empty string counts as true") end
if not nil then print("nil counts as false") end
print(score > 90 and "high" or "not high")
```

### Expected Behavior or Output
The program prints:
```text
Avery passed.
true
false
true
0 counts as true
the empty string counts as true
nil counts as false
not high
```

### Common Mistakes
1. Expecting `0` or `""` to be false.
2. Forgetting `then` after the condition, or forgetting the closing `end`.
3. Writing `score >= 80 and < 90` instead of repeating the variable in each comparison.

### Activities
1. Change the score to 59 and predict which lines change.
2. Write a condition that is true only for scores from 70 to 79 inclusive.
3. Predict `print(nil == false)` and `print(not nil)` before running them.
4. Explain why `x and "yes" or "no"` can give a wrong answer when the middle value is `false`.

### Accessibility Practice
Read each condition aloud with the operator names (`greater than or equal to`, `and`, `not`), and check that your screen reader announces `~=` so you do not confuse it with `==`.

### Skills Checklist
- [ ] I can write comparisons and combine them.
- [ ] I can write a complete `if` statement with `end`.
- [ ] I know that only `nil` and `false` are false.
- [ ] I can use `and`/`or` to choose a value.
- [ ] I can read a condition aloud.

## Lesson 3.2: Chained Conditionals and Grade Classification

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (control structures)
- Lua 5.4 Reference Manual: Section 3.3.4 (Control Structures)
- Matching Python lesson: Lesson 3.2 Chained Conditionals (elif, else)

### Learning Objectives
- Use `elseif` to test conditions in order.
- Classify the shared grade thresholds.
- Test boundary scores.

### Concept Explanation
Lua chains conditions with `elseif` (one word) and finishes with an optional `else` and a single `end`. Lua tests the conditions from top to bottom and runs only the first block whose condition is true.

The shared grade thresholds are: 90 or more is A, 80 or more is B, 70 or more is C, 60 or more is D, and anything lower is F. Because the conditions are tested in order, each later test only needs a lower bound.

*Boundary scores* sit exactly on or just below a threshold. The test scores 90, 89, 80, 79, 70, 69, 60, and 59 check every boundary. A function that returns a value is used here so the same rule can be reused; functions are explained fully in Unit 6.

Writing `else if` as two words is legal Lua but opens a new nested `if`, which then needs its own `end`; write `elseif`.

### Worked Example
```lua
local function classify(score)
  if score >= 90 then
    return "A"
  elseif score >= 80 then
    return "B"
  elseif score >= 70 then
    return "C"
  elseif score >= 60 then
    return "D"
  else
    return "F"
  end
end

for _, score in ipairs({90, 89, 80, 79, 70, 69, 60, 59}) do
  print(string.format("%d %s", score, classify(score)))
end
```

### Expected Behavior or Output

```text
90 A
89 B
80 B
79 C
70 C
69 D
60 D
59 F
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
