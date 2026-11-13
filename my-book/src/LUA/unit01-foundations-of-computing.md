# Unit 1: Foundations of Computing

## Overview

Turn a written algorithm into Lua, run a first program, and learn variables, values, and Lua's dynamic types. The shared student profile appears here for the first time.

## Lesson 1.1: Computer Science and Problem Solving

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (Getting Started)
- Zelle: Chapter 1, pages 1-7 (shared with the Python track)
- Matching Python lesson: Lesson 1.1 Welcome to Computer Science

### Learning Objectives
- Explain hardware, software, and algorithms in your own words.
- Turn a written algorithm into a short Lua program.
- Predict a program's output by hand before running it.

### Concept Explanation
Computers follow instructions exactly. *Hardware* is the physical machine; *software* is the set of instructions it follows; an *algorithm* is an ordered, finite list of clear steps that solves a problem. The foundations unit of this repository (Unit P) covers these ideas in detail.

Computer science is mainly about solving problems, and programming is how a solution is carried out. A reliable approach is to understand the problem, break it into small steps, write the algorithm in plain language, translate it into code, and test it.

Here the algorithm is: "set a total to zero; for each score, add it to the total; divide the total by the number of scores; report both." Lua's `local` keyword creates a variable that exists only in its block, `for ... in ipairs(...)` visits a list in order, and `#` gives the length of a list.

The scores 82, 91, 76, and 88 are the course's shared data. Their total is 337 and their average is 84.25. A hand trace should reach the same numbers before the program is run.

### Worked Example
```lua
-- Algorithm: total and average of the shared scores.
local scores = {82, 91, 76, 88}
local total = 0
for _, score in ipairs(scores) do
  total = total + score
end
local average = total / #scores
print(string.format("Total: %d", total))
print(string.format("Average: %.2f", average))
```

### Expected Behavior or Output
The program prints:
```text
Total: 337
Average: 84.25
```

### Common Mistakes
1. Starting to code before writing the steps, then forgetting the step that divides by the number of scores.
2. Writing `local total` without giving it a value, so the first addition fails on `nil`.
3. Using `/` and expecting a whole number. In Lua 5.4, `/` always produces a float.

### Activities
1. Trace the program by hand, writing the running total after each score: 82, 173, 249, 337.
2. Change the list to {90, 80} and predict the total and average before running.
3. Add a line that reports the highest score using a second loop.
4. Explain, in two sentences, the difference between the algorithm and the Lua program.

### Accessibility Practice
Write your hand trace as numbered sentences, one per loop step, rather than as a table, and read it back with your screen reader. Compare it with the program's printed lines in order.

### Skills Checklist
- [ ] I can define hardware, software, and algorithm.
- [ ] I can describe an algorithm as ordered steps.
- [ ] I can trace a loop by hand.
- [ ] I can read a short Lua program aloud.
- [ ] I can run it and compare the output with my trace.

## Lesson 1.2: Your First Lua Program

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (Getting Started)
- Lua 5.4 Reference Manual: Section 3.1 (Blocks) and Section 3.3.5 (For Statement)
- Matching Python lesson: Lesson 1.2 Your First Python Program - Hello World

### Learning Objectives
- Write and run a program that prints text.
- Use comments to document code.
- Explain that Lua executes statements in order, top to bottom.

### Concept Explanation
A Lua program is a sequence of *statements* that run in order. `print` is a built-in function that writes its arguments to the terminal. Text in quotation marks is a *string*. Single or double quotes both work, and a string written with double square brackets, `[[ ... ]]`, can span several lines.

A line comment starts with `--` and runs to the end of the line; Lua ignores it. A long comment starts with `--[[` and ends with `]]`.

`print` separates multiple arguments with a tab character. `io.write` writes exactly what you give it with nothing added, so a new line must be written as the escape sequence `\n`. Knowing the difference matters because a screen reader may read a tab as a pause, and because exact output is easier to test.

### Worked Example
```lua
-- This program prints a greeting for the shared student.
print("Hello, Avery!")
print("Welcome to Lua programming!")
io.write("No new line here, ")
io.write("then one here.\n")
print("a", "b", "c")
```

### Expected Behavior or Output
The program prints:
```text
Hello, Avery!
Welcome to Lua programming!
No new line here, then one here.
a	b	c
```

### Common Mistakes
1. Using a curly quotation mark pasted from a document instead of a straight quotation mark, which causes a syntax error.
2. Expecting `io.write` to add a new line the way `print` does.
3. Writing `print 'Hello'` with a missing space or quotation mark and misreading the resulting error.

### Activities
1. Run the program and describe in words how the last line differs from the line before it.
2. Change the greeting to use your own name and predict the output.
3. Write a program that prints three lines: your name, the course name, and today's task.
4. Add a comment above each line and read the file aloud with comments included.

### Accessibility Practice
Run the file from the terminal and read the output in order. Note that `a`, `b`, and `c` on the last line are separated by tab characters; check whether your screen reader announces them.

### Skills Checklist
- [ ] I can write and run a program that prints text.
- [ ] I can write a line comment.
- [ ] I can explain how `print` and `io.write` differ.
- [ ] I can say that statements run in order.
- [ ] I can read a first error message.

## Lesson 1.3: Variables, Values, and Dynamic Types

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 3 (Numbers), Chapter 4 (Strings)
- Lua 5.4 Reference Manual: Section 2.1 (Values and Types)
- Matching Python lesson: Lesson 1.3 Variables and Simple Data Types

### Learning Objectives
- Create local variables and assign values.
- Name the basic Lua types and check a value's type.
- Explain `nil` and the difference between local and global variables.

### Concept Explanation
A *variable* is a name that refers to a value. In Lua, variables do not have types; *values* do. The same variable may refer to a number now and a string later. The basic types are `nil`, `boolean`, `number`, `string`, `table`, and `function`. The function `type(value)` returns the type name as a string.

Lua 5.4 numbers have two subtypes: *integer* (whole numbers such as 16) and *float* (numbers with a decimal point such as 1.72). `math.type(value)` reports `integer` or `float`.

Always declare variables with `local`. A variable assigned without `local` becomes a *global* variable visible to the whole program, which is a common source of hard-to-find bugs. A variable that has never been assigned has the value `nil`, which means "no value."

The shared student profile is name Avery, age 16, height 1.72 meters, and favorite subject Computer Science. The shared inventory item Notebook has quantity 3 and unit price 2.50, so three notebooks cost 7.5.

### Worked Example
```lua
local name = "Avery"
local age = 16
local height = 1.72
local favorite_subject = "Computer Science"

print(name, age, height, favorite_subject)
print(type(name), type(age), type(height), type(favorite_subject))
print(math.type(age), math.type(height))

local notebook_price = 2.50
local notebook_quantity = 3
print("Notebook total:", notebook_price * notebook_quantity)

local missing
print(missing, type(missing))
```

### Expected Behavior or Output
The program prints:
```text
Avery	16	1.72	Computer Science
string	number	number	string
integer	float
Notebook total:	7.5
nil	nil
```

### Common Mistakes
1. Forgetting `local`, which silently creates a global variable that other code can change.
2. Expecting Lua to report an error for an unassigned variable. It simply has the value `nil`.
3. Confusing `=` (assignment) with `==` (comparison).

### Activities
1. Run the example and write down each type name in the order it was printed.
2. Change `age` to 16.0 and predict what `math.type(age)` prints.
3. Add a boolean variable `likes_cs` set to `true` and print its type.
4. Explain, without code, why `type(nil)` is the string `nil` while a missing variable's value is the value `nil`.

### Accessibility Practice
Read the variable names aloud as part of each line, for example 'local favorite underscore subject'. Check that your screen reader pauses at the underscore so you can tell `favorite_subject` from two words.

### Skills Checklist
- [ ] I can declare local variables and assign values.
- [ ] I can name Lua's basic types.
- [ ] I can use `type` and `math.type`.
- [ ] I can explain `nil`.
- [ ] I can explain why `local` matters.
