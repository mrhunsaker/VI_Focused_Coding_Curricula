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
=======
Plan and build the tip calculator, learn Lua's operators and integer/float subtypes, read typed input safely, and use the math library.

## Lesson 2.1: Software Development Process

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 2 (Interlude: The Eight-Queen Puzzle) for stepwise design
- Lua 5.4 Reference Manual: Section 6.4 (String Manipulation, string.format)
- Matching Python lesson: Lesson 2.1 The Software Development Process

### Learning Objectives
- Describe the design, implement, and test cycle.
- Write pseudocode for a tip calculator and implement it in Lua.
- Explain why money is formatted to two decimal places.

### Concept Explanation
Software is developed in a cycle: understand the problem, design a solution, implement it, and test it. Design comes first. For a tip calculator the pseudocode is:

1. Get the bill amount.
2. Calculate the tip as 15 percent of the bill.
3. Calculate the total as the bill plus the tip.
4. Print the tip.
5. Print the total.

With the shared values (bill 24.50, tip rate 0.15) the unrounded tip is 3.675 and the total is 28.175. `string.format("%.2f", x)` rounds a number for display to two decimal places, using the C library's rules. Because 3.675 cannot be stored exactly in binary floating point, Lua displays the tip as 3.67 and the total as 28.18. Other languages may display the tip as 3.68. The stored values are the same; only the display rounding differs.

### Worked Example
```lua
local bill = 24.5
local tip_rate = 0.15

local tip = bill * tip_rate
local total = bill + tip

print(string.format("Bill: %.2f", bill))
print(string.format("Tip: %.2f", tip))
print(string.format("Total: %.2f", total))

-- Test a boundary case: a zero bill.
local zero_tip = 0 * tip_rate
print(string.format("Tip on a zero bill: %.2f", zero_tip))
```

### Expected Behavior or Output
The program prints:
```text
Bill: 24.50
Tip: 3.67
Total: 28.18
Tip on a zero bill: 0.00
```

### Common Mistakes
1. Writing the rate as 15 instead of 0.15, which makes the tip 15 times too large.
2. Rounding the tip first and then adding it to the bill, which can change the total by a cent.
3. Skipping the zero and negative bill test cases.

### Activities
1. Write the five-step plan in your own words, then trace it with the shared values.
2. Change the tip rate to 0.20 and predict the tip and total (4.90 and 29.40) before running.
3. Add a test for a bill of 100 and write down the expected values before running it.
4. Explain in two sentences why the program prints 3.67 even though the exact value is 3.675.

### Accessibility Practice
Print each result on its own line with a label, so a screen reader reads 'Tip: 3.67' as one clear unit, and never rely on alignment or color.

### Skills Checklist
- [ ] I can name the four stages of the development cycle.
- [ ] I can write pseudocode for a calculation.
- [ ] I can implement it with `string.format`.
- [ ] I can explain two-decimal rounding.
- [ ] I can name a boundary case to test.

## Lesson 2.2: Expressions and Assignment

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 3 (Numbers) and Chapter 4 (Strings)
- Lua 5.4 Reference Manual: Section 3.4 (Expressions)
- Matching Python lesson: Lesson 2.2 Elements of Programs - Expressions and Assignment

### Learning Objectives
- Evaluate arithmetic expressions using operator precedence.
- Use integer division, modulo, and exponent correctly.
- Update a variable and join strings with `..`.

### Concept Explanation
An *expression* produces a value. Lua's arithmetic operators are `+`, `-`, `*`, `/` (float division), `//` (floor division), `%` (modulo), and `^` (exponent, always a float). Multiplication, division, and modulo happen before addition and subtraction, and parentheses override that order, so `8 + 4 * 2` is 16 and `(8 + 4) * 2` is 24.

Assignment stores a value in a variable: `score = score + 9` computes the right side first and stores the result. The shared score 82 plus 9 becomes 91.

Strings are joined with the concatenation operator `..`, written with two dots. Numbers can be joined to strings, and Lua converts them to text, but `tostring` makes the conversion explicit. Comparison uses `==`, `<`, `<=`, `>`, `>=`, and `~=` for "not equal."

Division is the main trap for learners coming from other languages. In Lua 5.4, `7 / 2` is `3.5`, while `7 // 2` is `3`, and `7 % 2` is `1`.

### Worked Example
```lua
print(8 + 4 * 2)
print((8 + 4) * 2)

local score = 82
score = score + 9
print("New score:", score)

print(7 / 2, 7 // 2, 7 % 2, 2 ^ 3)
print("Python" .. " " .. "is fun!", "Lua" .. " " .. "is fun!")
print(5 ~= 6, 10 == 10.0)
```

### Expected Behavior or Output
The program prints:
```text
16
24
New score:	91
3.5	3	1	8.0
Python is fun!	Lua is fun!
true	true
```

### Common Mistakes
1. Reading `^` as bitwise exclusive-or, as in some other languages. In Lua it is exponentiation and always returns a float, so `2 ^ 3` is `8.0`.
2. Using `+` to join strings. Use `..` for joining; `+` tries to convert text to numbers.
3. Writing `!=` for not-equal; Lua uses `~=`.

### Activities
1. Predict each of the six output lines before running, then compare.
2. Write an expression for the area of a rectangle 12 by 8 and a second for its perimeter.
3. Replace `7 // 2` with `-7 // 2` and explain why the answer is -4.
4. Join your name, a space, and your age into one line using `..` and `tostring`.

### Accessibility Practice
Say each operator by name when reading code aloud: 'slash', 'double slash', 'percent', 'caret', 'double dot'. If your screen reader skips `..`, raise the punctuation level before you read joins.

### Skills Checklist
- [ ] I can apply operator precedence.
- [ ] I can use `/`, `//`, `%`, and `^` correctly.
- [ ] I can update a variable with assignment.
- [ ] I can join strings with `..`.
- [ ] I can use `~=` for not-equal.

## Lesson 2.3: Input and Output

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 7 (The External World)
- Lua 5.4 Reference Manual: Section 6.8 (Input and Output Facilities)
- Matching Python lesson: Lesson 2.3 Input and Output Revisited

### Learning Objectives
- Read a line of text with `io.read`.
- Convert typed text to a number with `tonumber`.
- Handle missing input safely.

### Concept Explanation
`io.read()` reads one line from *standard input* (the keyboard in a terminal, or a file when input is redirected) and returns it as a string without the trailing new line. At the end of the input it returns `nil`. Programs that read input must therefore always be ready for `nil`.

Typed text is always a string. `tonumber(text)` converts text such as "12" to a number, and returns `nil` if the text is not a valid number. Never assume that `tonumber` succeeds.

`io.write(prompt)` shows a prompt without moving to a new line. In this course, prompts are printed on their own line with `print` so that each prompt is read cleanly by a screen reader and the typed answer appears on the next line.

The example reads a name and two numbers, prints a greeting, and prints their sum. With the typed values Avery, 12, and 8, the sum is 20.

### Worked Example
```lua
print("Enter your name:")
local name = io.read()
print("Enter the first number:")
local first = tonumber(io.read())
print("Enter the second number:")
local second = tonumber(io.read())

if name and first and second then
  print("Hello, " .. name .. "!")
  print("The sum of " .. first .. " and " .. second .. " is " .. (first + second) .. ".")
else
  print("Input was missing or not a number.")
end
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
Avery
12
8
```

the program prints:
```text
Enter your name:
Enter the first number:
Enter the second number:
Hello, Avery!
The sum of 12 and 8 is 20.
```

### Common Mistakes
1. Adding two values read from `io.read` without converting them. Text is not a number, and the result may be a number only because Lua coerces strings in arithmetic, which hides errors.
2. Forgetting that `io.read` returns `nil` at the end of input, so the program crashes when run without input.
3. Using `tonumber` on a blank line and not noticing that the result is `nil`.

### Activities
1. Run the program in the terminal and type Avery, 12, and 8. Confirm the output.
2. Type the word `twelve` for the first number and read the message. Explain what happened.
3. Run the program with no input at all (`lua5.4 main.lua < /dev/null`, or the equivalent on your system) and describe the output.
4. Change the program to subtract the second number from the first.

### Accessibility Practice
Each prompt is on its own line and every result is a complete sentence, so the output reads clearly in order. When you test, listen for whether your screen reader reads the prompt before you begin typing.

### Skills Checklist
- [ ] I can read a line with `io.read`.
- [ ] I can convert text with `tonumber`.
- [ ] I know `io.read` returns `nil` at the end of input.
- [ ] I can write clear prompts.
- [ ] I can handle invalid or missing input with a message.

## Lesson 2.4: Numbers and Type Conversions

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 3 (Numbers)
- Lua 5.4 Reference Manual: Section 3.4.3 (Coercions and Conversions)
- Matching Python lesson: Lesson 2.4 Computing with Numbers and Type Conversions

### Learning Objectives
- Convert between text and numbers explicitly.
- Distinguish integer and float values.
- Explain why automatic string-to-number coercion can hide mistakes.

### Concept Explanation
`tonumber("16")` gives the integer 16, `tonumber("1.72")` gives the float 1.72, and `tonumber("abc")` gives `nil`. `tostring(42)` gives the text "42". `math.tointeger(3.0)` gives the integer 3 and returns `nil` when a float has a fractional part. `math.floor(3.9)` gives 3.

Lua also *coerces* automatically: `"10" + 5` is 15, because arithmetic converts numeric text to a number. This is convenient but risky, since it can hide a missing conversion. Prefer explicit `tonumber` and test the result for `nil`.

Mixed arithmetic follows simple rules: integer plus integer is an integer, but any operation with a float produces a float. `1.72 * 100` is the float `172.0`, which is printed with a decimal point. Use `math.floor` or `string.format("%d")` after checking the value if you need a whole-number display.

The shared student has age 16 and height 1.72 meters. The example converts text to those values and computes the height in centimeters.

### Worked Example
```lua
local age = tonumber("16")
local height = tonumber("1.72")
print(age, math.type(age))
print(height, math.type(height))

print(tonumber("abc"))
print(tonumber(""))
print(tostring(42) .. " is now text")
print("10" + 5)

local height_cm = height * 100
print(height_cm, math.type(height_cm))
print(string.format("Height in centimeters: %.1f", height_cm))
print(math.tointeger(3.0), math.floor(3.9))
```

### Expected Behavior or Output
The program prints:
```text
16	integer
1.72	float
nil
nil
42 is now text
15
172.0	float
Height in centimeters: 172.0
3	3
```

### Common Mistakes
1. Assuming `tonumber` always returns a number and then doing arithmetic on `nil`.
2. Relying on automatic coercion such as `"10" + 5` and missing that a value was never converted.
3. Expecting `1.72 * 100` to print `172` without a decimal point.

### Activities
1. Predict the ten output lines, then run and compare.
2. Check what `tonumber("  16  ")` and `tonumber("0x10")` return and explain each.
3. Write code that reads a line, converts it, and prints a message when conversion fails.
4. Explain the difference between `math.floor(3.9)` and `math.tointeger(3.9)`.

### Accessibility Practice
Read the type names that `math.type` prints aloud. Notice that `172.0` is announced with a decimal point, which signals a float.

### Skills Checklist
- [ ] I can convert text to numbers and numbers to text.
- [ ] I can tell integer from float.
- [ ] I can predict mixed arithmetic results.
- [ ] I can explain the risk of coercion.
- [ ] I can test a conversion result for `nil`.

## Lesson 2.5: Using the Math Library

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 3 (Numbers)
- Lua 5.4 Reference Manual: Section 6.7 (Mathematical Functions)
- Matching Python lesson: Lesson 2.5 Using the Math Library

### Learning Objectives
- Use `math.pi`, `math.sqrt`, and related functions.
- Compute circle area and circumference.
- Compute the distance from the origin.

### Concept Explanation
The `math` library provides constants and functions: `math.pi`, `math.sqrt`, `math.abs`, `math.max`, `math.min`, `math.floor`, and `math.ceil`. Lua has no built-in `hypot` function, so the distance from the origin to a point is `math.sqrt(x^2 + y^2)`.

For a circle of radius 5, the area is `math.pi * radius^2` (about 78.54) and the circumference is `2 * math.pi * radius` (about 31.42). For the shared coordinates x = 3 and y = 4, the distance from the origin is 5.0.

`math.sqrt` always returns a float, so the square root of 81 is `9.0`. Use `string.format("%.2f", value)` to display results with two decimal places.

### Worked Example
```lua
local radius = 5
local area = math.pi * radius ^ 2
local circumference = 2 * math.pi * radius
print(string.format("Area: %.2f", area))
print(string.format("Circumference: %.2f", circumference))

print(math.sqrt(81))

local x, y = 3, 4
local distance = math.sqrt(x ^ 2 + y ^ 2)
print(string.format("Distance from origin: %.2f", distance))

print(math.max(82, 91, 76, 88), math.min(82, 91, 76, 88), math.abs(-5))
```

### Expected Behavior or Output
The program prints:
```text
Area: 78.54
Circumference: 31.42
9.0
Distance from origin: 5.00
91	76	5
```

### Common Mistakes
1. Looking for `math.hypot`, which Lua does not have. Use `math.sqrt(x^2 + y^2)`.
2. Writing `math.pi * radius * 2` for the area; the radius must be squared.
3. Expecting `math.sqrt(81)` to print `9` rather than `9.0`.

### Activities
1. Predict each printed line and then run the program.
2. Compute the area for a radius of 2.5 by hand and with the program.
3. Change x and y to 6 and 8 and predict the distance (10.00) before running.
4. Write a function-free program that prints the larger of two shared scores using `math.max`.

### Accessibility Practice
Round all results with `string.format` so the screen reader announces short numbers, not the long unrounded value of `math.pi * 25`.

### Skills Checklist
- [ ] I can use `math.pi` and `math.sqrt`.
- [ ] I can compute circle area and circumference.
- [ ] I can compute distance from the origin.
- [ ] I can format numbers to two decimals.
- [ ] I know Lua has no `math.hypot`.

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
>>>>>>> 2067a20 (curriculum clearning and updates)
end
```

### Expected Behavior or Output
<<<<<<< HEAD

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
