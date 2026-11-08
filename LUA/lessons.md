# Lua: Complete Curriculum — Units 0–11

## Course Overview

Lua is a lightweight embeddable scripting language used in games, embedded applications, configuration, automation, and extensible software. This course follows the Python curriculum's problem contexts and shared datasets so learners can focus on Lua syntax and semantics. It teaches Lua 5.4's tables (used as lists, records, dictionaries, and objects), functions as values, multiple returns, metatables, closures, modules, file handling, error handling with `pcall`, and testing, using only the standard library.

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md), which explains the language-neutral vocabulary and concepts used in this track.

**Shared data.** The examples use the same data as every language track: student Avery (age 16, height 1.72 meters, favorite subject Computer Science); a bill of 24.50 with a tip rate of 0.15; the scores 82, 91, 76, and 88; the inventory Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25); and the text sample "A student studies programming. Programming develops problem-solving skills."

**Lua-specific points that differ from the Python course.**
- Lists start at index 1, and `#` gives a list's length.
- Only `nil` and `false` are false. The number 0 and the empty string are true.
- Tables are the only collection type. There are no tuples, no `continue` keyword, no keyword arguments, and no JSON library in the standard library; each lesson shows the Lua idiom.
- `pairs` does not guarantee an order, so lessons sort keys before printing.
- Floating-point display follows the C library: the shared tip of 3.675 displays as 3.67 with `%.2f`.

**Verification status.** Every example in this track was run with Lua 5.4.6, and the "Expected Behavior or Output" blocks are the captured output of those runs (with the standard input shown where a program reads input). This has not been tested with screen readers or braille displays; see [VALIDATION.md](VALIDATION.md).

# Unit 0: Accessible Environment and Toolchain

## Overview

Install Lua 5.4, create a project folder, set up a keyboard-first editor workflow, and learn how Lua finds modules. No programming experience is needed beyond Unit P.

## Lesson 0.1: Install and Verify Lua

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (Getting Started)
- Lua 5.4 Reference Manual: Section 7 (Lua Standalone)
- Matching Python lesson: Lesson 0.1 Installing Python and uv

### Learning Objectives
- Install Lua 5.4 using a trusted source for your operating system.
- Verify the installed version from the terminal.
- Run a one-line program with the interpreter before creating any file.

### Concept Explanation
Lua is a small interpreted language. The program that reads and runs Lua source is called the *interpreter*. Installing Lua therefore means installing one command-line program. This course targets **Lua 5.4**; features such as integer and float number subtypes, `//` integer division, and `<close>` variables belong to Lua 5.3 and 5.4, so an older 5.1 or 5.2 interpreter will not run every example.

Choose one installation route and write down which one you used:

- Debian or Ubuntu Linux: the package manager provides `lua5.4`, and the command is `lua5.4`.
- macOS: a package manager such as Homebrew provides a `lua` formula. After installing, check the version, because the command is usually named `lua`.
- Windows: use a Lua 5.4 binary distribution or a package manager you already trust, then confirm the command name and that it is on your PATH.
- Any system: Lua can be built from the source archive at lua.org if you prefer.

The command name differs by system (`lua5.4` or `lua`). This course writes `lua5.4`; substitute your own command everywhere. Always confirm the version with `-v` rather than assuming, because a computer can have an old Lua installed alongside a new one.

The `-e` option runs a statement given on the command line, which proves the interpreter works before you create a project.

### Worked Example
```bash
lua5.4 -v
lua5.4 -e "print('Hello from Lua')"
```

### Expected Behavior or Output
Expected output (the patch number and year depend on the version you installed; this was observed with Lua 5.4.6):
```text
Lua 5.4.6  Copyright (C) 1994-2023 Lua.org, PUC-Rio
Hello from Lua
```

### Common Mistakes
1. Installing a package named `lua` and assuming it is Lua 5.4. Run the version command to confirm.
2. Mixing up the command name: typing `lua` when the installed command is `lua5.4`, then concluding the install failed.
3. Running a Lua statement in a shell without noticing that the shell's own quoting rules changed the quotation marks.

### Activities
1. Install Lua and record the exact output of the version command.
2. Run `lua5.4 -e "print(1 + 1)"` and explain each part of the command in your own words.
3. Find out which command name your system uses and write it on the first line of your course notes file.
4. Explain the difference between the interpreter and the source file it reads.

### Accessibility Practice
Run each command from the keyboard only. After pressing Enter, use your screen reader's review commands to read the output line by line, and confirm that the version number is announced. If you use a braille display, check that the quotation marks in the second command are shown.

### Skills Checklist
- [ ] I can install Lua 5.4 and say which route I used.
- [ ] I can run the version command and read the result.
- [ ] I know which command name my computer uses.
- [ ] I can run a one-line Lua statement from the terminal.
- [ ] I can say what the interpreter does.

## Lesson 0.2: Workspace and First Run

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (Getting Started)
- Lua 5.4 Reference Manual: Section 7 (Lua Standalone)
- Matching Python lesson: Lesson 0.2 Installing and configuring VS Code or Theia IDE

### Learning Objectives
- Create a course folder with a first source file.
- Run the file from the terminal and read the result.
- Read a Lua error message and find the file name and line number.

### Concept Explanation
A *project folder* keeps one program's files together. Create a folder named `lua-course`, and inside it save a file named `main.lua`. Lua source files conventionally end in `.lua`. From the terminal, change into the folder (this is your *working directory*) and run the file by giving its name to the interpreter: `lua5.4 main.lua`.

Lua runs the file from top to bottom as one unit called a *chunk*. `print` writes its arguments to the terminal and ends with a new line. The global variable `_VERSION` holds the language version as text, which is a quick way to confirm that the file ran under Lua 5.4.

If a file contains a mistake, the interpreter prints a message of the form `lua5.4: main.lua:3: ...`. Read it in three parts: the program name, the file name and line number (`main.lua:3`), and a description of the problem. Always go to that line first.

To check syntax without running a program, use the compiler front end: `luac5.4 -p main.lua`. It prints nothing when the file is syntactically valid.

### Worked Example
```lua
-- main.lua: the first program in the course project folder
print("Hello, Lua!")
print(_VERSION)
```

### Expected Behavior or Output
The program prints:
```text
Hello, Lua!
Lua 5.4
```

### Common Mistakes
1. Running the command from the wrong folder, so the interpreter reports that it cannot open `main.lua`.
2. Saving the file with a hidden extra extension such as `main.lua.txt`, so the file name does not match.
3. Ignoring the line number in an error message and re-reading the whole file instead.

### Activities
1. Create the folder and file, then run them. Record the working directory shown by `pwd` (macOS and Linux) or `cd` (Windows).
2. Remove the closing quotation mark on line 2, run the file, and write down the file name, line number, and description in the error message. Then restore the file.
3. Run `luac5.4 -p main.lua` before and after the mistake and compare what is printed.
4. Add a third line that prints your own name, and predict the output before running it.

### Accessibility Practice
Use a keyboard-only route to create the folder and file (terminal commands or your editor's keyboard commands). Read your error message with the screen reader's line-by-line review, and find the line number without relying on a mouse or on color.

### Skills Checklist
- [ ] I can create a project folder and a `.lua` file.
- [ ] I can run the file from the terminal.
- [ ] I can say what the working directory is.
- [ ] I can read the file name and line number in an error.
- [ ] I can check syntax with `luac5.4 -p`.

## Lesson 0.3: Editor and Accessibility Workflow

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (Getting Started)
- This repository: [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md)
- Matching Python lesson: Lesson 0.3 Editor extensions and project workspace

### Learning Objectives
- Configure an editor so Lua source can be read by speech or braille.
- Choose a punctuation announcement level that distinguishes brackets, braces, and quotation marks.
- Practice navigating a Lua file by line, word, and character.

### Concept Explanation
Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md) first. Then adapt the editor for Lua:

- Install only a Lua language extension from a source you trust, such as a Lua language server, and read what permissions it requests. An extension is optional; the course works with a plain text editor and the terminal.
- Set your screen reader's punctuation level high enough to hear the symbols that carry meaning in Lua: braces `{ }` that surround tables, square brackets `[ ]` for indexing, the length operator `#`, the concatenation operator `..`, the not-equal operator `~=`, and the comment marker `--`.
- Lua does not use indentation to decide structure. Blocks end with the keyword `end`, so each `if`, `for`, `while`, and `function` needs a matching `end`. Indentation is for people, and your editor's indentation guides or announcements still help you count nesting levels.

Practise reading the example below aloud, saying each symbol: "local scores equals open brace eighty-two comma ninety-one comma seventy-six comma eighty-eight close brace." Then say what `#scores` and `scores[1]` mean.

### Worked Example
```lua
local scores = {82, 91, 76, 88}
print(string.format("count=%d first=%d last=%d", #scores, scores[1], scores[#scores]))
```

### Expected Behavior or Output
The program prints:
```text
count=4 first=82 last=88
```

### Common Mistakes
1. Setting punctuation announcement so low that `{`, `}`, and `..` are never spoken, then misreading a table or a string join.
2. Forgetting that a Lua block closes with `end`, and relying on indentation alone.
3. Installing several overlapping extensions and getting duplicate, confusing diagnostics.

### Activities
1. Test your editor with the example. Record the punctuation level at which every symbol in line 1 is announced.
2. Navigate the file by line, then by word, then by character, and note the keyboard commands you used.
3. Introduce a missing `end` in a small `if` block, save, and find how your editor reports the problem. Then fix it.
4. Write a half-page note describing your edit, run, and fix cycle using only the keyboard.

### Accessibility Practice
This whole lesson is accessibility practice. Verify that you can open the file, move to a given line number, read a line character by character, run the program in the terminal, and read the output. Do not describe this workflow as screen-reader tested for others; record only what you tested yourself, with the names of your operating system, editor, and access technology.

### Skills Checklist
- [ ] I can configure my editor for keyboard-only use.
- [ ] I can hear or feel every symbol in a Lua table and string join.
- [ ] I can explain why Lua blocks end with `end`.
- [ ] I can navigate a file by line, word, and character.
- [ ] I can run and read a program entirely from the keyboard.

## Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 17 (Modules and Packages)
- Lua 5.4 Reference Manual: Section 6.3 (Modules)
- Matching Python lesson: Lesson 0.4 Python environments and terminal usage

### Learning Objectives
- Keep each project in its own folder and run commands from its root.
- Load code from a second file with `require` and explain `package.path`.
- Explain what LuaRocks is and when it is needed.

### Concept Explanation
Run commands from the *project root*, the folder that holds your main file. Keep different projects in different folders so their files never mix.

A Lua *module* is a file that returns a value, usually a table of functions. The function `require("name")` finds the file `name.lua`, runs it once, and returns what it returned. Lua searches the places listed in `package.path`, a text value where each template uses `?` as a stand-in for the module name. Adding `./?.lua;` to the front tells Lua to look in the current folder first.

The standard library is enough for this course. **LuaRocks** is Lua's package manager for external packages; it records a package in a *rockspec* file and can install either system-wide or into a local tree. Use it only when a project needs an external package, and prefer a local tree so a project does not change the whole computer.

The example below is self-contained: it writes a tiny module file, then loads it with `require`, so the same lesson works in an empty folder.

### Worked Example
```lua
-- Create a small module file, then load it with require.
local file = assert(io.open("pricing.lua", "w"))
file:write([[
local M = {}
function M.line_total(quantity, unit_price)
  return quantity * unit_price
end
return M
]])
file:close()

package.path = "./?.lua;" .. package.path
local pricing = require("pricing")
print(pricing.line_total(3, 2.50))
```

### Expected Behavior or Output
The program prints:
```text
7.5
```

### Common Mistakes
1. Running a program from a different folder, so `require` cannot find a module in the current folder.
2. Forgetting that a module file must `return` its table; without it `require` returns `true` and calls such as `pricing.line_total` fail.
3. Installing every package system-wide instead of keeping dependencies with the project.

### Activities
1. Run the example, then open the new `pricing.lua` file and read it aloud, line by line.
2. Add a second function, `line_value_with_discount`, to the module and call it from the main file.
3. Run the program from a different folder and record the error message. Explain why it happened.
4. Print `package.path` and write down, in your own words, what the first template means.

### Accessibility Practice
Keep one project per folder and begin every session by confirming your working directory with a command and reading the result. Read the long text in `package.path` with character navigation, noting where each semicolon separates one template from the next.

### Skills Checklist
- [ ] I can identify the project root and run commands from it.
- [ ] I can load a module with `require`.
- [ ] I can explain what `package.path` contains.
- [ ] I can say when LuaRocks is needed.
- [ ] I can run a program from the terminal and read its output.

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

# Unit 2: Numeric Computations

## Overview

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

# Unit 3: Control Flow

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
The program prints:
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
1. Writing `else if` and forgetting the extra `end` it requires.
2. Putting the conditions in the wrong order, such as testing `score >= 60` first so every passing score is a D.
3. Using `>` instead of `>=`, so exactly 90 receives a B.

### Activities
1. Trace the score 82 by hand through each test and say which block runs.
2. Add the score 100 and the score 0 to the test list and predict their grades.
3. Reorder the tests so that `score >= 60` comes first, run it, and explain the wrong output.
4. Write a function that returns `true` when a grade is passing (D or better).

### Accessibility Practice
Read the eight output lines in order. Each line is a number, a space, and a letter, so the pairs are easy to follow with a screen reader and a braille display.

### Skills Checklist
- [ ] I can write an `if`/`elseif`/`else` chain.
- [ ] I can explain why test order matters.
- [ ] I can classify with the shared thresholds.
- [ ] I can choose boundary test values.
- [ ] I can explain `elseif` versus `else if`.

## Lesson 3.3: Tables as Lists

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables)
- Lua 5.4 Reference Manual: Section 3.4.7 (Table Constructors) and Section 3.4.7 (Length Operator)
- Matching Python lesson: Lesson 3.3 Introduction to Lists

### Learning Objectives
- Create a list with a table constructor.
- Index a list starting at 1 and use `#` for its length.
- Change an element.

### Concept Explanation
Lua has one structure for collections, the *table*. A table used as a list is written with braces, such as `{82, 91, 76, 88}`. **Lua indexes lists from 1**, so the first score is `scores[1]` and the last is `scores[#scores]`. `scores[0]` does not exist and yields `nil`.

The *length operator* `#` gives the number of items in a list: `#scores` is 4. It is reliable for lists with no gaps; do not assign `nil` into the middle of a list.

A table is changed in place: `scores[3] = 80` replaces the third score. Tables are *references*: a second variable assigned from the first refers to the same table, not a copy.

`table.concat(list, ", ")` joins the items into one string for display. It is an efficient way to show a whole list on one line.

The shared list is 82, 91, 76, 88. Python indexes the same list from 0, so Python's `scores[2]` is Lua's `scores[3]`.

### Worked Example
```lua
local scores = {82, 91, 76, 88}

print(scores[1])
print(scores[#scores])
print(#scores)
print(scores[0])

scores[3] = 80
print(table.concat(scores, ", "))

local alias = scores
alias[1] = 100
print(scores[1])
```

### Expected Behavior or Output
The program prints:
```text
82
88
4
nil
82, 91, 80, 88
100
```

### Common Mistakes
1. Using `scores[0]` for the first item. It is `nil` in Lua.
2. Assuming `alias = scores` makes a copy. Both names refer to the same table.
3. Leaving a gap by assigning `nil` in the middle of a list and then trusting `#`.

### Activities
1. Predict each of the six outputs before running.
2. Replace the second score with 95 and print the whole list with `table.concat`.
3. Print the third score using `scores[3]` and then explain how the same value is reached in a zero-based language.
4. Make a real copy of the list using a loop and show that changing the copy does not change the original.

### Accessibility Practice
When reading `scores[#scores]` aloud, say 'scores, open bracket, hash scores, close bracket' so the nesting of the brackets is clear.

### Skills Checklist
- [ ] I can create a list in a table constructor.
- [ ] I can use 1-based indexing and `#`.
- [ ] I can change an element.
- [ ] I know that tables are references.
- [ ] I can display a list with `table.concat`.

## Lesson 3.4: Iterating with for Loops

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 and Chapter 18 (Iterators and the Generic for)
- Lua 5.4 Reference Manual: Section 3.3.5 (For Statement)
- Matching Python lesson: Lesson 3.4 Iterating with for Loops

### Learning Objectives
- Use the numeric `for` loop with start, stop, and step.
- Use `ipairs` to visit a list in order.
- Compute the total and average of the shared scores.

### Concept Explanation
Lua has two `for` loops. The *numeric* `for` counts: `for i = 1, 5 do ... end` runs with `i` equal to 1 through 5, inclusive of both ends. A third value is the step: `for i = 10, 1, -3` counts down by 3. Lua evaluates the limits once and the loop variable is local to the loop.

The *generic* `for` walks a collection. `for index, value in ipairs(list) do ... end` visits positions 1, 2, 3, ... in order and stops at the first `nil`. Use `ipairs` for lists and `pairs` for tables with named keys (Unit 4).

Looping to total and average is the same algorithm as Unit 1, now with a loop you can explain: the total starts at 0, each pass adds one score, and the average is the total divided by `#scores`.

Strings can be walked one character at a time with `for char in word:gmatch(".") do ... end`, though most work uses string functions (Lesson 3.5).

### Worked Example
```lua
local scores = {82, 91, 76, 88}
local total = 0
for index, score in ipairs(scores) do
  print(string.format("Adding score %d: %d", index, score))
  total = total + score
end
print("Total: " .. total)
print("Average: " .. total / #scores)

for i = 1, 3 do print("Count: " .. i) end
for i = 10, 1, -3 do print("Step: " .. i) end
```

### Expected Behavior or Output
The program prints:
```text
Adding score 1: 82
Adding score 2: 91
Adding score 3: 76
Adding score 4: 88
Total: 337
Average: 84.25
Count: 1
Count: 2
Count: 3
Step: 10
Step: 7
Step: 4
Step: 1
```

### Common Mistakes
1. Using `for i = 0, #scores` and reading past the end of the list, which yields `nil`.
2. Forgetting that the loop limit is inclusive, so `for i = 1, 3` runs three times.
3. Using `pairs` on a list and assuming the order matches the list order.

### Activities
1. Predict the last four lines of output before running.
2. Change the loop to print only the scores above 80.
3. Write a loop that counts from 20 down to 0 by 5.
4. Explain why the average prints as `84.25` and not `84`.

### Accessibility Practice
Each output line starts with a label and a number, so a screen reader can read the running total step by step. Count the lines to check that the loop ran four times.

### Skills Checklist
- [ ] I can write a numeric `for` loop with a step.
- [ ] I can use `ipairs` on a list.
- [ ] I know the numeric limit is inclusive.
- [ ] I can total and average a list.
- [ ] I can explain the difference between `ipairs` and `pairs`.

## Lesson 3.5: Basic String Operations

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 4 (Strings)
- Lua 5.4 Reference Manual: Section 6.4 (String Manipulation)
- Matching Python lesson: Lesson 3.5 Basic String Operations

### Learning Objectives
- Use `#`, `string.lower`, `string.upper`, `string.sub`, and `string.find`.
- Normalize a name and search the shared text sample.
- Explain that strings are immutable.

### Concept Explanation
A Lua string is a sequence of bytes. `#text` gives its length in bytes, which equals the number of characters for ordinary ASCII text. Strings are *immutable*: functions such as `text:upper()` return a new string and never change the original. The colon call `text:upper()` is shorthand for `string.upper(text)`.

Useful functions: `lower`, `upper`, `sub(i, j)` (positions start at 1 and are inclusive), `find(pattern, init, plain)` (returns the start and end positions, or `nil`), `gsub` (replace; also returns a count), `rep` (repeat), and `format`.

`find` treats its second argument as a *pattern* with special characters. Pass `true` as the fourth argument for a plain text search. Positions are 1-based, so the first character is at position 1.

The example normalizes the name "  avery  " by trimming spaces with a pattern and capitalizing the first letter, then explores the shared text sample: its length, whether it contains "programming", where the first match starts, and how many times it appears.

### Worked Example
```lua
local raw_name = "  avery  "
local clean = raw_name:match("^%s*(.-)%s*$")
clean = clean:sub(1, 1):upper() .. clean:sub(2)
print("Name: '" .. clean .. "'")

local text = "A student studies programming. Programming develops problem-solving skills."
local lowered = text:lower()
print("Characters:", #text)
print("Contains 'programming':", lowered:find("programming", 1, true) ~= nil)
print("First position of 'programming':", (lowered:find("programming", 1, true)))
local _, count = lowered:gsub("programming", "")
print("Times 'programming' appears:", count)
print(("ab"):rep(3), text:sub(1, 9))
```

### Expected Behavior or Output
The program prints:
```text
Name: 'Avery'
Characters:	75
Contains 'programming':	true
First position of 'programming':	19
Times 'programming' appears:	2
ababab	A student
```

### Common Mistakes
1. Expecting `text:upper()` to change `text`. Strings are immutable; assign the result.
2. Counting positions from 0. The first character is at position 1.
3. Searching for text that contains pattern characters such as `.` or `-` without passing `true` for a plain search.

### Activities
1. Predict the printed values, then run and compare.
2. Find the position of the word `student` in the sample text.
3. Use `gsub` to replace every `programming` with `coding` and print the result.
4. Write code that trims and capitalizes the name "  riley  ".

### Accessibility Practice
Pattern strings such as `^%s*(.-)%s*$` are punctuation-dense. Read them one symbol at a time and say 'caret', 'percent s', 'star', 'open parenthesis', 'dot', 'dash', so you can check each piece.

### Skills Checklist
- [ ] I can find a string's length and substrings.
- [ ] I can search text plainly and by position.
- [ ] I can transform case and trim a string.
- [ ] I know strings are immutable.
- [ ] I can read a pattern one symbol at a time.

# Unit 4: Data Structures

## Overview

Work with list tables, sorting, fixed and read-only records, dictionaries, and stable traversal of the shared inventory.

## Lesson 4.1: More on Sequence Tables

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables) and Chapter 14 (Data Structures)
- Lua 5.4 Reference Manual: Section 6.6 (Table Manipulation)
- Matching Python lesson: Lesson 4.1 More on Lists

### Learning Objectives
- Append, insert, replace, and remove list items.
- Search a list for a value.
- Use `table.insert` and `table.remove` correctly.

### Concept Explanation
`table.insert(list, value)` appends. `table.insert(list, position, value)` inserts at a position and shifts later items up. `table.remove(list, position)` removes the item at a position, shifts later items down, and returns the removed item; `table.remove(list)` removes and returns the last item. Assigning `list[i] = value` replaces an item without shifting.

Lua has no built-in "remove by value," so write a short loop that finds the index with `ipairs` and then calls `table.remove`. Searching a list this way takes time proportional to its length.

Because Lua lists start at 1, positions in this lesson are one more than the matching Python index.

The example applies the same operations as the Python course to the shared scores.

### Worked Example
```lua
local scores = {82, 91, 76, 88}

table.insert(scores, 95)
table.insert(scores, 2, 85)
scores[3] = 93

local function remove_value(list, value)
  for index, item in ipairs(list) do
    if item == value then
      return table.remove(list, index)
    end
  end
  return nil
end

remove_value(scores, 76)
local last = table.remove(scores)

print(table.concat(scores, ", "))
print(#scores, last)

local function contains(list, value)
  for _, item in ipairs(list) do
    if item == value then return true end
  end
  return false
end
print(contains(scores, 88), contains(scores, 100))
```

### Expected Behavior or Output
The program prints:
```text
82, 85, 93, 88
4	95
true	false
```

### Common Mistakes
1. Calling `table.insert(list, position, value)` with the arguments in the wrong order.
2. Using `list[#list + 2] = value`, which leaves a gap and breaks `#`.
3. Removing items while looping forward over the same list, which skips the item after each removal.

### Activities
1. Trace the list after every operation and write each version.
2. Use `table.remove(scores, 1)` and explain what happens to the other items.
3. Write `remove_all(list, value)` that removes every matching item safely.
4. Print the position of the first score above 90.

### Accessibility Practice
After each change, print the whole list with `table.concat` on one line so a screen reader reads a complete state in one pass.

### Skills Checklist
- [ ] I can append, insert, replace, and remove items.
- [ ] I can return a removed item from `table.remove`.
- [ ] I can search a list with a loop.
- [ ] I know positions start at 1.
- [ ] I can show a list in one line.

## Lesson 4.2: Sorting and Organizing Tables

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions), the section on sort
- Lua 5.4 Reference Manual: Section 6.6 (table.sort)
- Matching Python lesson: Lesson 4.2 Organizing Lists

### Learning Objectives
- Sort a list ascending and descending.
- Reverse a list and sort a copy so the original is unchanged.
- Write a comparison function.

### Concept Explanation
`table.sort(list)` sorts the list *in place* from smallest to largest. For another order, pass a *comparison function* that returns `true` when its first argument must come before its second: `table.sort(list, function(a, b) return a > b end)` sorts from largest to smallest.

The comparison function must be consistent. Using `>=` can cause the error "invalid order function for sorting". Use strict `<` or `>`.

`table.sort` has no stable-order guarantee for equal items. To keep the original order, sort a *copy*. `table.move(source, 1, #source, 1, {})` copies a list into a new table.

Lua has no built-in reverse for lists; reverse with two indexes that swap and move toward each other.

The example sorts the shared scores: ascending is 76, 82, 88, 91 and descending is 91, 88, 82, 76.

### Worked Example
```lua
local scores = {82, 91, 76, 88}

local sorted_copy = table.move(scores, 1, #scores, 1, {})
table.sort(sorted_copy)
print("Original:", table.concat(scores, ", "))
print("Ascending:", table.concat(sorted_copy, ", "))

table.sort(scores, function(a, b) return a > b end)
print("Descending:", table.concat(scores, ", "))

local function reverse(list)
  local i, j = 1, #list
  while i < j do
    list[i], list[j] = list[j], list[i]
    i = i + 1
    j = j - 1
  end
end
reverse(scores)
print("Reversed:", table.concat(scores, ", "))
```

### Expected Behavior or Output
The program prints:
```text
Original:	82, 91, 76, 88
Ascending:	76, 82, 88, 91
Descending:	91, 88, 82, 76
Reversed:	76, 82, 88, 91
```

### Common Mistakes
1. Using `>=` in a comparison function, which can raise an invalid-order error.
2. Expecting `table.sort` to return the sorted list. It returns nothing and sorts in place.
3. Sorting a list that mixes numbers and strings, which raises a comparison error.

### Activities
1. Predict the four printed lines before running.
2. Sort the scores descending without changing the original by sorting a copy.
3. Sort the words `{"pencil", "folder", "notebook"}` and print them.
4. Explain why `list[i], list[j] = list[j], list[i]` swaps without a temporary variable.

### Accessibility Practice
Print each result on its own labelled line. Compare the lines by listening for the first and last numbers, which are quickest to check.

### Skills Checklist
- [ ] I can sort in place and sort a copy.
- [ ] I can write a comparison function.
- [ ] I can reverse a list with a loop.
- [ ] I know `table.sort` returns nothing.
- [ ] I know why comparison functions must be strict.

## Lesson 4.3: Fixed Records and Read-Only Tables

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions), multiple results; Chapter 20 (Metatables and Metamethods)
- Lua 5.4 Reference Manual: Section 2.4 (Metatables and Metamethods)
- Matching Python lesson: Lesson 4.3 Tuples - Immutable Lists

### Learning Objectives
- Return and receive several values from a function.
- Explain why Lua has no tuple type.
- Create a read-only table with a metatable.

### Concept Explanation
Lua has no tuple type. Two idioms cover the same needs. First, a function can return *multiple values*, and the caller can receive them with `local x, y = point()`. Second, a fixed collection can be a small table such as `{3, 4}` or `{x = 3, y = 4}`.

A plain table can always be changed. To make a table *read-only*, return an empty proxy table whose metatable forwards reads to the real table with `__index` and rejects writes with `__newindex`. The length operator needs a `__len` metamethod because the proxy itself is empty.

`pcall(f)` (protected call) runs a function and returns `false` plus an error message instead of stopping the program. The error here uses level 0 so the message has no file name or line number and prints the same on every computer.

The shared coordinates are x = 3 and y = 4.

### Worked Example
```lua
local function point()
  return 3, 4
end
local x, y = point()
print(x, y)

local function readonly(source)
  return setmetatable({}, {
    __index = source,
    __len = function() return #source end,
    __newindex = function()
      error("attempt to modify a read-only table", 0)
    end,
  })
end

local coordinates = readonly({3, 4})
print(coordinates[1], coordinates[2], #coordinates)

local ok, message = pcall(function() coordinates[1] = 10 end)
print(ok, message)
```

### Expected Behavior or Output
The program prints:
```text
3	4
3	4	2
false	attempt to modify a read-only table
```

### Common Mistakes
1. Expecting `coordinates[1] = 10` to fail on a normal table. Only the proxy rejects writes.
2. Forgetting `__len`, so `#coordinates` is 0 on the empty proxy.
3. Using a read-only proxy for iteration with `pairs` and being surprised that it appears empty.

### Activities
1. Run the program and explain each of the five printed values.
2. Write a function that returns a name, an age, and a height, and receive all three.
3. Add `__newindex` rejection for a table of the shared inventory item and test it with `pcall`.
4. Explain in two sentences why a tuple is not needed in Lua.

### Accessibility Practice
Read the proxy code in short pieces: the real table, the metatable, `__index`, `__len`, `__newindex`. Check closing braces by counting the levels aloud.

### Skills Checklist
- [ ] I can return and receive multiple values.
- [ ] I can explain why Lua has no tuples.
- [ ] I can make a read-only proxy table.
- [ ] I can use `pcall` to catch an error.
- [ ] I can read nested braces aloud.

## Lesson 4.4: Tables as Dictionaries

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables)
- Lua 5.4 Reference Manual: Section 3.4.9 (Table Constructors)
- Matching Python lesson: Lesson 4.4 Introducing Dictionaries

### Learning Objectives
- Create records with named keys.
- Add, change, and remove a key.
- Model the shared inventory item.

### Concept Explanation
A table with named keys works as a dictionary or a record. Write `{name = "Avery", age = 16}` and read a field with `profile.name` or `profile["name"]`. The two forms are equivalent for plain names; use brackets when the key is in a variable or contains spaces.

Assigning to a new key adds it, assigning to an existing key changes it, and **assigning `nil` removes it**. Reading a key that does not exist yields `nil`, not an error.

The length operator `#` counts only list items, so it does not count named keys. To count keys, loop with `pairs`.

The shared student profile has name Avery, age 16, height 1.72 meters, and favorite subject Computer Science. The shared inventory item is Notebook with quantity 3 and unit price 2.50.

### Worked Example
```lua
local student_profile = {
  name = "Avery",
  age = 16,
  height_m = 1.72,
  favorite_subject = "Computer Science",
}

student_profile.age = 17
student_profile.grade_level = 11
student_profile.height_m = nil
print(student_profile.name, student_profile.age, student_profile.grade_level, student_profile.height_m)

local function count_keys(t)
  local n = 0
  for _ in pairs(t) do n = n + 1 end
  return n
end
print("Keys:", count_keys(student_profile), "Length operator:", #student_profile)

local item = {name = "Notebook", quantity = 3, unit_price = 2.50}
item.quantity = item.quantity + 2
item.location = "Shelf A"
print(string.format("%s: %d at %.2f = %.2f", item.name, item.quantity, item.unit_price, item.quantity * item.unit_price))
```

### Expected Behavior or Output
The program prints:
```text
Avery	17	11	nil
Keys:	4	Length operator:	0
Notebook: 5 at 2.50 = 12.50
```

### Common Mistakes
1. Using `#` to count keys. It returns 0 for a table with only named keys.
2. Assuming a missing key causes an error. It returns `nil`.
3. Using a number as a key by accident (`t[1]`) when the intended key is the text `"1"`.

### Activities
1. Predict the printed values, then run.
2. Remove `favorite_subject` and show that reading it gives `nil`.
3. Add `discount = 0.20` to the item and print the discounted line value.
4. Write a function that returns `true` if a record has all of the keys `name`, `quantity`, and `unit_price`.

### Accessibility Practice
Use field names that read well aloud, such as `unit_price`. Read records one key per line so a screen reader announces each key with its value.

### Skills Checklist
- [ ] I can create a record with named keys.
- [ ] I can add, change, and remove keys.
- [ ] I know `nil` assignment removes a key.
- [ ] I can count keys with `pairs`.
- [ ] I can model the shared inventory item.

## Lesson 4.5: Traversing Tables with pairs and ipairs

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 18 (Iterators and the Generic for)
- Lua 5.4 Reference Manual: Section 6.1 (pairs and ipairs)
- Matching Python lesson: Lesson 4.5 Looping Through Dictionaries

### Learning Objectives
- Traverse keys, values, and key-value pairs.
- Explain why `pairs` order is not guaranteed.
- Produce stable, sorted output.

### Concept Explanation
`pairs(table)` visits every key and value, but **the order is not defined** and can differ between runs or Lua versions. Code that prints such a traversal can give different output on different computers, which hurts testing and makes output confusing to follow by ear.

To produce stable output, collect the keys in a list, sort the list, then visit the keys in order. `ipairs` is different: it visits list positions 1, 2, 3, ... in a guaranteed order.

A common stable design is a list of records, each with its own name, when order matters, or a dictionary plus a sorted key list when lookup by name matters.

The shared inventory is Notebook (quantity 3, price 2.50), Pencil (10, 0.50), and Folder (4, 1.25). The total value is 7.50 + 5.00 + 5.00 = 17.50.

### Worked Example
```lua
local inventory = {
  Notebook = {quantity = 3, unit_price = 2.50},
  Pencil = {quantity = 10, unit_price = 0.50},
  Folder = {quantity = 4, unit_price = 1.25},
}

local names = {}
for name in pairs(inventory) do names[#names + 1] = name end
table.sort(names)

print("Keys:")
for _, name in ipairs(names) do print(name) end

print("Quantities:")
for _, name in ipairs(names) do print(inventory[name].quantity) end

local total_value = 0
for _, name in ipairs(names) do
  local details = inventory[name]
  local line_value = details.quantity * details.unit_price
  print(string.format("%s: %d in stock, value %.2f", name, details.quantity, line_value))
  total_value = total_value + line_value
end
print(string.format("Total inventory value: %.2f", total_value))
```

### Expected Behavior or Output
The program prints:
```text
Keys:
Folder
Notebook
Pencil
Quantities:
4
3
10
Folder: 4 in stock, value 5.00
Notebook: 3 in stock, value 7.50
Pencil: 10 in stock, value 5.00
Total inventory value: 17.50
```

### Common Mistakes
1. Printing results straight from `pairs` and expecting the same order every time.
2. Using `ipairs` on a dictionary and getting no output, because `ipairs` visits only positions 1, 2, 3, ...
3. Changing the table (adding keys) during a `pairs` traversal, which gives undefined behavior.

### Activities
1. Run the program and write out the three key-value lines in order.
2. Print the inventory in descending order of line value.
3. Print only the items with a quantity below 5.
4. Explain why the program sorts the key names before printing.

### Accessibility Practice
Sorted output matters for accessibility: a screen reader user can learn the order and trust it. Always sort keys before reading a dictionary aloud.

### Skills Checklist
- [ ] I can traverse a dictionary with `pairs`.
- [ ] I can traverse a list with `ipairs`.
- [ ] I know `pairs` order is not guaranteed.
- [ ] I can sort keys for stable output.
- [ ] I can total the shared inventory.

# Unit 5: Input and Iteration

## Overview

Read and validate input, write sentinel and flag loops, skip entries without a `continue` keyword, and prevent endless loops.

## Lesson 5.1: How io.read Works

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 7 (The External World)
- Lua 5.4 Reference Manual: Section 6.8 (io.read)
- Matching Python lesson: Lesson 5.1 How the input() Function Works

### Learning Objectives
- Read a line and recognize that it is text.
- Convert it with `tonumber` and test for failure.
- Handle the end of input.

### Concept Explanation
`io.read()` (the same as `io.read("l")`) reads one line and returns it as a string. Other formats exist: `io.read("n")` reads a number directly and `io.read("a")` reads everything that remains. This course uses line reading with explicit conversion because it is easier to validate.

`io.read` returns `nil` when there is no more input. A program that keeps reading must check for `nil`, or it will crash on the first run with no input.

Converting text to a number is a separate step: `tonumber(text)` returns the number or `nil`. Test the result before using it.

With the typed value 16, the program converts the text to the number 16 and prints the age five years later, 21. A second value, `abc`, is rejected because `tonumber` returns `nil`.

### Worked Example
```lua
print("How old are you?")
local text = io.read()
print("Type:", type(text))

local age = tonumber(text)
if age then
  print("In 5 years:", age + 5)
else
  print("That was not a number.")
end

print("Enter another value:")
local second = tonumber(io.read())
if second then
  print("Number:", second)
else
  print("Not a number; tonumber returned nil.")
end
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
16
abc
```

the program prints:
```text
How old are you?
Type:	string
In 5 years:	21
Enter another value:
Not a number; tonumber returned nil.
```

### Common Mistakes
1. Calling arithmetic on the text without converting it first.
2. Not checking for `nil` from `io.read` at the end of input.
3. Forgetting that `tonumber("")` is `nil`, so an empty answer is invalid.

### Activities
1. Run with 16 and then `abc`. Compare with the shown output.
2. Run with no input and explain each line printed.
3. Make the program accept an age only between 0 and 120.
4. Write the program using `io.read("n")` and explain what happens when the user types a word.

### Accessibility Practice
Prompts are on their own lines. Run the program twice, once typing and once with piped input, and compare what your screen reader announces.

### Skills Checklist
- [ ] I can read a line of input.
- [ ] I can convert and validate it.
- [ ] I handle `nil` at end of input.
- [ ] I can explain that typed input is text.
- [ ] I can use `io.read` formats.

## Lesson 5.2: The while Loop in Action

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (control structures)
- Lua 5.4 Reference Manual: Section 3.3.4 (While Statement)
- Matching Python lesson: Lesson 5.2 The while Loop in Action

### Learning Objectives
- Write a counting `while` loop.
- Write a sentinel loop that ends on a command.
- Stop at the end of input.

### Concept Explanation
A `while` loop repeats its block as long as the condition is true: `while condition do ... end`. The condition is tested *before* each pass. A loop needs a way to make the condition false, normally by changing a variable inside the body.

A *sentinel* is a special value that tells the loop to stop. Here the sentinel is the word `quit`. The standard pattern reads once before the loop and again at the end of each pass, and checks for `nil` as well, so the loop ends when input runs out.

The example first counts from 1 to 5, then repeats a message prompt until the user types `quit`.

### Worked Example
```lua
local count = 1
while count <= 5 do
  print(count)
  count = count + 1
end
print("Counting finished!")

print("Enter a message, or type quit to exit:")
local message = io.read()
while message ~= nil and message ~= "quit" do
  print("You said: " .. message)
  print("Enter a message, or type quit to exit:")
  message = io.read()
end
print("Goodbye!")
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
hello
scores
quit
```

the program prints:
```text
1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit:
You said: hello
Enter a message, or type quit to exit:
You said: scores
Enter a message, or type quit to exit:
Goodbye!
```

### Common Mistakes
1. Forgetting to change the loop variable, creating an endless loop.
2. Testing `message ~= "quit"` without testing for `nil`, so input that ends without `quit` crashes the loop.
3. Reading input only before the loop and never again inside it.

### Activities
1. Predict the output for the typed lines hello, scores, quit.
2. Change the sentinel to `exit` and update the prompt.
3. Count how many messages were entered and print the count at the end.
4. Rewrite the counting loop as a numeric `for` loop and compare.

### Accessibility Practice
Each prompt appears on its own line and each response begins with the label `You said:`, so the conversation can be followed in order by ear.

### Skills Checklist
- [ ] I can write a counting `while` loop.
- [ ] I can write a sentinel loop.
- [ ] I check for `nil` as well as the sentinel.
- [ ] I update the loop variable.
- [ ] I can compare `while` with numeric `for`.

## Lesson 5.3: Using Flags and break to Exit Loops

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (control structures)
- Lua 5.4 Reference Manual: Section 3.3.4 (Break and Goto)
- Matching Python lesson: Lesson 5.3 Using Flags and break to Exit Loops

### Learning Objectives
- Use a Boolean flag to control a loop.
- Use `break` to leave a loop early.
- Search a list and remember where the item was found.

### Concept Explanation
A *flag* is a Boolean variable that controls a loop: the loop runs while `running` is true, and the body sets it to `false` when it is time to stop. `break` leaves the nearest enclosing loop immediately.

A flag makes the stopping rule visible in one place. `break` is shorter and is clearest for searches that can stop as soon as the answer is found.

For a search, keep a variable for the result (initially `nil`), set it when the item is found, then `break`. After the loop, test the variable to see whether a match was found. Positions in Lua lists start at 1.

The shared scores are 82, 91, 76, 88. The first score of 90 or higher is 91 at position 2.

### Worked Example
```lua
local running = true
local handled = 0
while running do
  print("Say something, or type quit to stop:")
  local message = io.read()
  if message == nil or message == "quit" then
    running = false
  else
    handled = handled + 1
    print("You said: " .. message)
  end
end
print("Messages handled: " .. handled)

local scores = {82, 91, 76, 88}
local found_index
for index, score in ipairs(scores) do
  if score >= 90 then
    found_index = index
    break
  end
end
if found_index then
  print(string.format("First score of 90 or higher: %d at position %d", scores[found_index], found_index))
else
  print("No score of 90 or higher.")
end
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
hello
quit
ignored
```

the program prints:
```text
Say something, or type quit to stop:
You said: hello
Say something, or type quit to stop:
Messages handled: 1
First score of 90 or higher: 91 at position 2
```

### Common Mistakes
1. Setting the flag but then running more code in the same pass that should be skipped.
2. Forgetting to initialize the result variable and misreading an old value after the loop.
3. Using `break` to leave an outer loop from an inner loop. It only leaves the innermost loop.

### Activities
1. Run with the lines hello and quit and confirm the count is 1.
2. Change the search to the first score below 80 and predict the position.
3. Rewrite the first loop without a flag, using `break`.
4. Explain in two sentences when a flag is clearer than `break`.

### Accessibility Practice
Announce results with complete sentences. The search result includes both the value and its position so the sentence is understandable without any layout.

### Skills Checklist
- [ ] I can control a loop with a flag.
- [ ] I can leave a loop with `break`.
- [ ] I can search a list and keep the position.
- [ ] I know `break` leaves one loop.
- [ ] I can explain flag versus `break`.

## Lesson 5.4: Skipping Entries with goto continue

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 8 (Filling some Gaps), goto
- Lua 5.4 Reference Manual: Section 3.3.4 (Goto Statement)
- Matching Python lesson: Lesson 5.4 Using continue in Loops

### Learning Objectives
- Skip a loop pass with `goto continue`.
- Write the same skip with a nested `if`.
- Skip invalid scores in a list.

### Concept Explanation
Lua has no `continue` statement. Two idioms skip the rest of one pass. The first is `goto continue` with a label `::continue::` at the very end of the loop body. The label name is a convention, not a keyword. A `goto` cannot jump into the scope of a local variable, so the label belongs at the end of the block.

The second idiom avoids `goto` entirely: wrap the work in an `if` that handles only the wanted case. For short loops this is usually clearer.

The example skips invalid scores (below 0 or above 100) in the list 82, -5, 91, 105, 76, 88, then lists the odd numbers from 1 to 9 with the `if` form. The four valid scores total 337.

### Worked Example
```lua
local raw_scores = {82, -5, 91, 105, 76, 88}
local valid_total, valid_count = 0, 0

for _, raw in ipairs(raw_scores) do
  if raw < 0 or raw > 100 then
    print("Skipping invalid score: " .. raw)
    goto continue
  end
  valid_total = valid_total + raw
  valid_count = valid_count + 1
  ::continue::
end
print("Valid scores: " .. valid_count .. ", total: " .. valid_total)

for number = 1, 9 do
  if number % 2 ~= 0 then
    print(number)
  end
end
```

### Expected Behavior or Output
The program prints:
```text
Skipping invalid score: -5
Skipping invalid score: 105
Valid scores: 4, total: 337
1
3
5
7
9
```

### Common Mistakes
1. Looking for a `continue` keyword. It does not exist in Lua.
2. Declaring a local variable after the `goto` and before the label in the same block, which is a compile error.
3. Placing the label in the middle of the body so statements after it still run.

### Activities
1. Predict the printed lines and the final total.
2. Skip the scores below 80 instead.
3. Rewrite the first loop with the nested `if` form and compare readability.
4. Explain why the label must come at the end of the loop body.

### Accessibility Practice
Each skipped entry prints its own line, so the screen reader announces what was ignored. Never skip silently when accessibility depends on knowing what happened.

### Skills Checklist
- [ ] I know Lua has no `continue`.
- [ ] I can use `goto continue` correctly.
- [ ] I can use a nested `if` instead.
- [ ] I can skip invalid entries.
- [ ] I can explain where the label goes.

## Lesson 5.5: Avoiding Infinite Loops

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (control structures)
- Lua 5.4 Reference Manual: Section 3.3.4 (Repeat Statement)
- Matching Python lesson: Lesson 5.5 Avoiding Infinite Loops

### Learning Objectives
- Identify what makes a loop stop.
- Add an attempt limit to an input loop.
- Use `repeat ... until`.

### Concept Explanation
An *infinite loop* never ends because its condition never becomes false. Typical causes are forgetting to change the loop variable, testing the wrong variable, or waiting for input that never arrives. In a terminal, stop a running program with Ctrl+C.

Defend against endless loops by giving every loop a *progress rule* and a *limit*. Count attempts, and stop when the limit is reached or the input ends.

`repeat ... until condition` runs the body first and tests afterward, so the body always runs at least once. Unlike other loops, variables declared inside the body are visible in the `until` test.

The example allows three attempts to enter a score from 0 to 100. With the typed lines abc, 105, and 88 the first two fail validation and the third is accepted.

### Worked Example
```lua
local MAX_ATTEMPTS = 3
local attempts = 0
local score

while attempts < MAX_ATTEMPTS do
  attempts = attempts + 1
  print(string.format("Enter a score from 0 to 100 (attempt %d of %d):", attempts, MAX_ATTEMPTS))
  local text = io.read()
  if text == nil then
    print("No more input.")
    break
  end
  local number = tonumber(text)
  if number and number >= 0 and number <= 100 then
    score = number
    break
  end
  print("Invalid score: " .. text)
end

if score then
  print("Accepted score: " .. score)
else
  print("No valid score was entered.")
end

local count = 1
repeat
  print(count)
  count = count + 1
until count > 3
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
abc
105
88
```

the program prints:
```text
Enter a score from 0 to 100 (attempt 1 of 3):
Invalid score: abc
Enter a score from 0 to 100 (attempt 2 of 3):
Invalid score: 105
Enter a score from 0 to 100 (attempt 3 of 3):
Accepted score: 88
1
2
3
```

### Common Mistakes
1. Forgetting to increase `attempts`, so the limit is never reached.
2. Waiting for input without handling `nil`, so a closed input stream ends in an error instead of a message.
3. Writing `until count < 3` and ending after one pass because the condition is true at once.

### Activities
1. Run with abc, 105, and 88 and confirm the accepted score.
2. Run with three invalid lines and read the final message.
3. Change the limit to 5 and test it.
4. Write down, for each loop in the example, what makes it stop.

### Accessibility Practice
A loop that cannot be stopped is an accessibility problem as well as a bug, because output may flood a screen reader. Learn the interrupt key (Ctrl+C) before you run loops, and give every input loop a limit.

### Skills Checklist
- [ ] I can name what ends each loop.
- [ ] I can add an attempt limit.
- [ ] I handle the end of input.
- [ ] I can use `repeat ... until`.
- [ ] I know how to interrupt a running program.

# Unit 6: Functions

## Overview

Define functions, pass positional and named arguments, return one or several values, pass tables by reference, and accept variable arguments.

## Lesson 6.1: Defining Functions

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions)
- Lua 5.4 Reference Manual: Section 3.4.11 (Function Definitions)
- Matching Python lesson: Lesson 6.1 Defining Functions

### Learning Objectives
- Define and call a function.
- Pass values as parameters.
- Explain that functions are values.

### Concept Explanation
A *function* is a named block of code that can be called many times. Define one with `local function name(parameters) ... end` and call it with `name(arguments)`. The *parameters* are the names in the definition; the *arguments* are the values supplied by the caller.

In Lua, functions are ordinary *values*. They can be stored in variables, put in tables, and passed to other functions. `local function f() end` is shorthand for creating a function value and storing it in a local variable that the function can also use to call itself.

If a call supplies too few arguments, the missing parameters are `nil`. If it supplies too many, the extra ones are ignored. Neither case is an error, so a function that needs its inputs should check them.

The example defines greetings and a reusable tip calculator using the shared values: a bill of 24.50 and a tip rate of 0.15.

### Worked Example
```lua
local function greet_user()
  print("Hello, Lua programmer!")
end
greet_user()
greet_user()

local function greet_name(name)
  print("Hello, " .. name .. "!")
end
greet_name("Avery")
greet_name("Riley")

local function show_tip(bill, tip_rate)
  local tip = bill * tip_rate
  print(string.format("Tip: %.2f", tip))
  print(string.format("Total: %.2f", bill + tip))
end
show_tip(24.5, 0.15)

local alias = show_tip
print(type(alias))
```

### Expected Behavior or Output
The program prints:
```text
Hello, Lua programmer!
Hello, Lua programmer!
Hello, Avery!
Hello, Riley!
Tip: 3.67
Total: 28.18
function
```

### Common Mistakes
1. Writing `greet_user` without parentheses and expecting the function to run. That only refers to the function.
2. Passing arguments in the wrong order, such as `show_tip(0.15, 24.5)`.
3. Assuming a missing argument is an error. It is `nil` and may fail later with a confusing message.

### Activities
1. Call `show_tip(100, 0.2)` and predict both lines.
2. Write a function `describe_student(name, age)` that prints one sentence.
3. Call `greet_name()` with no argument and read the error message carefully.
4. Explain the difference between a parameter and an argument using the example.

### Accessibility Practice
Choose function names that read as actions when spoken, such as `show_tip`. Print complete sentences from functions so that a screen reader announces the result of each call separately.

### Skills Checklist
- [ ] I can define and call a function.
- [ ] I can distinguish parameters from arguments.
- [ ] I know functions are values.
- [ ] I know missing arguments are `nil`.
- [ ] I can read a function definition aloud.

## Lesson 6.2: Passing Arguments

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions)
- Lua 5.4 Reference Manual: Section 3.4.10 (Function Calls)
- Matching Python lesson: Lesson 6.2 Passing Arguments

### Learning Objectives
- Pass arguments by position.
- Give a parameter a default with `or`.
- Pass named arguments with a table.

### Concept Explanation
Lua has no default parameter values and no keyword arguments. Two idioms provide the same behavior.

For a *default value*, write `tip_rate = tip_rate or 0.15` at the top of the function. If the caller passes `nil` (or nothing), the default is used. This idiom treats `false` the same as `nil`, so do not use it for a parameter that may legitimately be `false`.

For *named arguments*, accept a single table and read its fields: `calculate_total{bill = 24.5, tip_rate = 0.10}`. When a function is called with one table constructor, the parentheses are optional. Named arguments make a call self-describing and make the order irrelevant.

With the shared bill of 24.50, the total at the default rate 0.15 is 28.18, at 0.20 it is 29.40, and at 0.10 it is 26.95.

### Worked Example
```lua
local function calculate_total(bill, tip_rate)
  tip_rate = tip_rate or 0.15
  return bill + bill * tip_rate
end

print(string.format("%.2f", calculate_total(24.5)))
print(string.format("%.2f", calculate_total(24.5, 0.20)))

local function total_named(options)
  local rate = options.tip_rate or 0.15
  return options.bill + options.bill * rate
end

print(string.format("%.2f", total_named{bill = 24.5, tip_rate = 0.10}))
print(string.format("%.2f", total_named{bill = 24.5}))
```

### Expected Behavior or Output
The program prints:
```text
28.18
29.40
26.95
28.18
```

### Common Mistakes
1. Expecting Lua to provide keyword arguments like `calculate_total(tip_rate=0.10, bill=24.5)`. Pass one table instead.
2. Using `x = x or default` for a parameter where `false` is a valid value; it would replace `false` with the default.
3. Forgetting that the table call `f{...}` passes exactly one argument.

### Activities
1. Predict all four totals before running.
2. Add a third option `round` that rounds the total to a whole number when true.
3. Call `total_named{}` with no fields and read the error. Then add a check that prints a clear message instead.
4. Explain why the default idiom is risky for Boolean parameters.

### Accessibility Practice
Named-argument calls read well aloud: 'total named, open brace, bill equals 24.5, comma, tip rate equals 0.10, close brace'. Practise saying the braces so nesting is clear.

### Skills Checklist
- [ ] I can pass positional arguments.
- [ ] I can give a default with `or`.
- [ ] I can pass named arguments with a table.
- [ ] I know the risk of `or` with Boolean parameters.
- [ ] I can read a table call aloud.

## Lesson 6.3: Return Values

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions)
- Lua 5.4 Reference Manual: Section 3.3.4 (Return Statement)
- Matching Python lesson: Lesson 6.3 Return Values

### Learning Objectives
- Return a computed result.
- Return multiple values.
- Return `nil` and a message to report a problem.

### Concept Explanation
A function sends a result back with `return`. Unlike `print`, a returned value can be stored, tested, and used in later calculations. A function that ends without `return` returns nothing.

A Lua function may return *several* values: `return minimum, maximum`. The caller receives them with `local low, high = min_max(list)`. Extra values are dropped and missing values are `nil`.

A common convention for reporting a problem is to return `nil` plus an error message: `return nil, "list is empty"`. The caller checks the first result. This convention is used by the standard library, for example by `io.open`.

The example returns the average of the shared scores, classifies the average with the shared grade thresholds, and shows both a multiple return and an error return.

### Worked Example
```lua
local function average(scores)
  if #scores == 0 then
    return nil, "no scores to average"
  end
  local total = 0
  for _, score in ipairs(scores) do total = total + score end
  return total / #scores
end

local function classify(score)
  if score >= 90 then return "A"
  elseif score >= 80 then return "B"
  elseif score >= 70 then return "C"
  elseif score >= 60 then return "D"
  end
  return "F"
end

local function min_max(list)
  local low, high = list[1], list[1]
  for _, value in ipairs(list) do
    if value < low then low = value end
    if value > high then high = value end
  end
  return low, high
end

local scores = {82, 91, 76, 88}
local avg = average(scores)
print("Average: " .. avg)
print("Grade for the average: " .. classify(avg))
local low, high = min_max(scores)
print("Lowest and highest:", low, high)
print(average({}))
```

### Expected Behavior or Output
The program prints:
```text
Average: 84.25
Grade for the average: B
Lowest and highest:	76	91
nil	no scores to average
```

### Common Mistakes
1. Printing inside the function and then trying to use the result in a calculation. The function returned nothing.
2. Ignoring the error value from a function that returns `nil, message`.
3. Forgetting that `return` must be the last statement in its block.

### Activities
1. Predict the four printed results before running.
2. Write `total(list)` that returns the sum.
3. Write `contains(list, value)` that returns `true` or `false`.
4. Explain how a caller should use a function that returns `nil, message`.

### Accessibility Practice
Return values instead of printing inside logic functions, so that the same function can be tested and its result read aloud once by the caller.

### Skills Checklist
- [ ] I can return a value.
- [ ] I can return and receive multiple values.
- [ ] I can return `nil` plus a message.
- [ ] I can use a returned value in a calculation.
- [ ] I can classify an average with the shared thresholds.

## Lesson 6.4: Functions with Tables

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables) and Chapter 6 (Functions)
- Lua 5.4 Reference Manual: Section 2.1 (Values and Types)
- Matching Python lesson: Lesson 6.4 Functions with Lists and Dictionaries

### Learning Objectives
- Explain that tables are passed by reference.
- Modify a list in a function and protect the original with a copy.
- Process the shared inventory with a function.

### Concept Explanation
When a table is passed to a function, the function receives a *reference* to the same table. Changes the function makes to the table are visible to the caller. Numbers, strings, and booleans are copied, so changes to a parameter holding one of those do not affect the caller.

This makes functions that update lists simple, but it also makes accidental changes possible. To protect the caller's data, copy the table first: `table.move(list, 1, #list, 1, {})` makes a shallow copy of a list.

A function that only reads a table should not change it. A function that changes a table should say so in its name, such as `add_score`.

The shared inventory is Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25). Its total value is 17.50.

### Worked Example
```lua
local function add_score(score_list, new_score)
  table.insert(score_list, new_score)
end

local scores = {82, 91, 76, 88}
add_score(scores, 95)
print(table.concat(scores, ", "))

local safe_copy = table.move(scores, 1, #scores, 1, {})
add_score(safe_copy, 100)
print(#scores, #safe_copy)

local function inventory_value(inventory)
  local total = 0
  for _, details in ipairs(inventory) do
    total = total + details.quantity * details.unit_price
  end
  return total
end

local inventory = {
  {name = "Notebook", quantity = 3, unit_price = 2.50},
  {name = "Pencil", quantity = 10, unit_price = 0.50},
  {name = "Folder", quantity = 4, unit_price = 1.25},
}
print(string.format("Total inventory value: %.2f", inventory_value(inventory)))
```

### Expected Behavior or Output
The program prints:
```text
82, 91, 76, 88, 95
5	6
Total inventory value: 17.50
```

### Common Mistakes
1. Expecting a function to receive its own copy of a table.
2. Changing a table inside a function used only for reading, which surprises the caller.
3. Making a copy with `copy = original` and assuming it is separate.

### Activities
1. Predict the three printed lines before running.
2. Write `scale_prices(inventory, factor)` that changes the prices in place, and show the effect on the caller.
3. Rewrite it so it returns a new inventory and leaves the original unchanged.
4. Explain the difference between copying a number and copying a table.

### Accessibility Practice
State aloud, before each call, whether the function changes its argument. Printing the list before and after a call lets a screen reader user hear the effect.

### Skills Checklist
- [ ] I know tables are passed by reference.
- [ ] I can modify a list in a function.
- [ ] I can copy a list.
- [ ] I can process the shared inventory.
- [ ] I can say when a function changes its input.

## Lesson 6.5: Variable Numbers of Arguments

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions), variadic functions
- Lua 5.4 Reference Manual: Section 3.4.11 (Varargs)
- Matching Python lesson: Lesson 6.5 Arbitrary Number of Arguments

### Learning Objectives
- Write a function with `...`.
- Use `select("#", ...)` and `table.pack`.
- Handle the case of no arguments.

### Concept Explanation
A function whose parameter list ends in `...` accepts any number of arguments. Inside the function, `...` stands for the extra values. Convert them to a table with `{...}` or, to keep `nil` values and the count, with `table.pack(...)`, which sets a field `n`. `select("#", ...)` returns the number of arguments.

`table.unpack(list)` turns a list back into separate values, for example to call a function with a list of scores.

Handle the case of zero arguments explicitly: dividing a total by a count of 0 would give `nan` for floats. The example returns `nil` with a message instead.

The shared scores 82, 91, 76, and 88 have an average of 84.25. The average of 90 and 80 is 85.0, a float, because `/` always returns a float.

### Worked Example
```lua
local function average(...)
  local count = select("#", ...)
  if count == 0 then
    return nil, "no scores given"
  end
  local total = 0
  for _, value in ipairs({...}) do total = total + value end
  return total / count
end

print(average(82, 91, 76, 88))
print(average(90, 80))
print(average())

local scores = {82, 91, 76, 88}
print(average(table.unpack(scores)))

local packed = table.pack(1, nil, 3)
print(packed.n)
```

### Expected Behavior or Output
The program prints:
```text
84.25
85.0
nil	no scores given
84.25
3
```

### Common Mistakes
1. Using `#{...}` to count arguments when some are `nil`. Use `select("#", ...)` or `table.pack`.
2. Forgetting to handle the call with no arguments.
3. Using `...` outside a variadic function, which is a compile error.

### Activities
1. Predict each printed result.
2. Write `maximum(...)` that returns the largest argument.
3. Write `join(separator, ...)` that joins any number of strings.
4. Explain the difference between `{...}` and `table.pack(...)`.

### Accessibility Practice
Read variadic signatures aloud: 'function average, open parenthesis, three dots, close parenthesis'. Make sure your screen reader announces the three dots.

### Skills Checklist
- [ ] I can write a function with `...`.
- [ ] I can count arguments correctly.
- [ ] I can use `table.unpack`.
- [ ] I handle the no-argument case.
- [ ] I can explain `table.pack`.

# Unit 7: Object-Oriented Programming

## Overview

Build objects from tables, closures, and metatables: constructors, methods, inheritance, and composition, using the shared inventory item.

## Lesson 7.1: Why Learn About Objects?

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming) and Chapter 9 (Closures)
- Lua 5.4 Reference Manual: Section 3.4.11 (Function Definitions)
- Matching Python lesson: Lesson 7.1 Why Learn About Classes?

### Learning Objectives
- Explain objects as data plus behavior.
- Hide data with a closure.
- Describe encapsulation.

### Concept Explanation
An *object* bundles data with the functions that work on that data. Lua has no `class` keyword; objects are built from tables and functions. The shared example is an inventory *item* with a name, a quantity, and a unit price, and the ability to report its total value.

*Encapsulation* means hiding data so other code uses only the operations you provide. A *closure* is a function that remembers the local variables around where it was created. If a constructor keeps `quantity` as a local variable and returns only functions that use it, outside code cannot read or change `quantity` directly.

Other approaches, built on metatables (Lesson 7.2), share one set of functions between all objects and are the usual Lua style. The closure style protects the data more strongly but creates new function values for every object.

The example makes a Notebook with quantity 3 and unit price 2.50. Restocking by 2 raises the quantity to 5 and the value to 12.50.

### Worked Example
```lua
local function make_item(name, quantity, unit_price)
  local self = {}

  function self.total_value()
    return quantity * unit_price
  end

  function self.restock(amount)
    if amount < 0 then return false end
    quantity = quantity + amount
    return true
  end

  function self.describe()
    print(string.format("%s: %d at %.2f each, value %.2f", name, quantity, unit_price, self.total_value()))
  end

  return self
end

local notebook = make_item("Notebook", 3, 2.50)
notebook.describe()
notebook.restock(2)
notebook.describe()
print(notebook.quantity)
```

### Expected Behavior or Output
The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
Notebook: 5 at 2.50 each, value 12.50
nil
```

### Common Mistakes
1. Expecting a `class` keyword. Lua builds objects from tables.
2. Assuming data in a closure can be reached with `object.quantity`. It is hidden, so the result is `nil`.
3. Creating a new set of functions for thousands of objects without noticing the memory cost.

### Activities
1. Predict the three printed lines.
2. Add a method `is_valid()` that returns `true` when the quantity and price are not negative.
3. Create a Pencil and a Folder with the shared values and describe both.
4. Explain in your own words why `notebook.quantity` is `nil`.

### Accessibility Practice
Read an object definition as a list: the data, then each operation. Print one line per operation so the screen reader announces what each call did.

### Skills Checklist
- [ ] I can explain data plus behavior.
- [ ] I can hide data with a closure.
- [ ] I can say what encapsulation means.
- [ ] I can create several objects from one constructor.
- [ ] I can describe the cost of the closure style.

## Lesson 7.2: Creating Objects with Metatables

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming) and Chapter 20 (Metatables and Metamethods)
- Lua 5.4 Reference Manual: Section 2.4 (Metatables and Metamethods)
- Matching Python lesson: Lesson 7.2 Creating and Using a Class

### Learning Objectives
- Build a class table with a constructor.
- Use `setmetatable` and `__index`.
- Create several objects with the same fields.

### Concept Explanation
The common Lua pattern for a *class* is a table that holds the shared functions. Set `Item.__index = Item` so the table can serve as a metatable. The constructor `Item.new` builds a new table for the object's own data and calls `setmetatable(object, Item)`. When code reads a field that the object does not have, Lua looks it up in `Item` through `__index`, so every object shares the same functions.

`self` is not a keyword; it is the conventional name of the first parameter of a method (Lesson 7.3). Each object stores its own `name`, `quantity`, and `unit_price`.

The example creates the three shared inventory items. Each has the same fields with different values. A class is a blueprint and each table made by `Item.new` is one object, or *instance*.

### Worked Example
```lua
local Item = {}
Item.__index = Item

function Item.new(name, quantity, unit_price)
  local object = {name = name, quantity = quantity, unit_price = unit_price}
  return setmetatable(object, Item)
end

local notebook = Item.new("Notebook", 3, 2.50)
local pencil = Item.new("Pencil", 10, 0.50)
local folder = Item.new("Folder", 4, 1.25)

for _, item in ipairs({notebook, pencil, folder}) do
  print(string.format("%s: %d at %.2f", item.name, item.quantity, item.unit_price))
end

print(getmetatable(notebook) == Item)
```

### Expected Behavior or Output
The program prints:
```text
Notebook: 3 at 2.50
Pencil: 10 at 0.50
Folder: 4 at 1.25
true
```

### Common Mistakes
1. Forgetting `Item.__index = Item`, so the objects cannot find the class functions.
2. Putting the object's data fields on the class table, which shares them between all objects.
3. Forgetting to return the object from the constructor.

### Activities
1. Predict the four printed lines.
2. Add an `Item.new` check that raises an error for a negative quantity.
3. Create a fourth item with your own values.
4. Explain how `__index` lets `notebook` find a function stored in `Item`.

### Accessibility Practice
Read the constructor out loud in order: the data table, the call to `setmetatable`, the return. Check that the closing braces and the `end` keyword match.

### Skills Checklist
- [ ] I can write a constructor.
- [ ] I can use `setmetatable` and `__index`.
- [ ] I can create several objects.
- [ ] I can say what an instance is.
- [ ] I can read a class definition aloud.

## Lesson 7.3: Methods and Attributes

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming)
- Lua 5.4 Reference Manual: Section 3.4.11 (Method Calls and Definitions)
- Matching Python lesson: Lesson 7.3 Working with Attributes and Methods

### Learning Objectives
- Define a method with the colon syntax.
- Explain how `:` differs from `.`.
- Change attributes directly and through methods.

### Concept Explanation
A *method* is a function stored in the class that works on an object. Define it with a colon, `function Item:total_value() ... end`, which adds a hidden first parameter named `self`. Call it with a colon, `notebook:total_value()`, which passes the object as `self`.

`object.method()` (a dot) does *not* pass the object, so `self` is `nil` and the method fails. The dot and colon forms are the most common Lua method mistake.

Attributes can be read and changed directly (`notebook.quantity = 4`), or through methods that check the change. A method that validates its input protects the object from invalid data.

The example adds methods to report the value, check validity, restock, and describe.

### Worked Example
```lua
local Item = {}
Item.__index = Item

function Item.new(name, quantity, unit_price)
  return setmetatable({name = name, quantity = quantity, unit_price = unit_price}, Item)
end

function Item:total_value()
  return self.quantity * self.unit_price
end

function Item:is_valid()
  return self.name ~= "" and self.quantity >= 0 and self.unit_price >= 0
end

function Item:restock(amount)
  if amount < 0 then
    print("Cannot restock a negative amount.")
    return
  end
  self.quantity = self.quantity + amount
end

function Item:describe()
  print(string.format("%s: %d at %.2f each, value %.2f", self.name, self.quantity, self.unit_price, self:total_value()))
end

local notebook = Item.new("Notebook", 3, 2.50)
notebook:describe()
notebook:restock(2)
notebook:describe()
notebook.quantity = 4
notebook:describe()
notebook:restock(-1)
print(notebook:is_valid())
```

### Expected Behavior or Output
The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
Notebook: 5 at 2.50 each, value 12.50
Notebook: 4 at 2.50 each, value 10.00
Cannot restock a negative amount.
true
```

### Common Mistakes
1. Calling `notebook.describe()` with a dot, which leaves `self` as `nil`.
2. Defining `function Item.describe()` with a dot and then using `self` inside, so `self` is a global that does not exist.
3. Changing attributes directly and skipping validation that a method would have done.

### Activities
1. Predict the output of all six calls.
2. Change one call to use a dot and read the error message.
3. Add a method `discount(rate)` that returns the value after a discount without changing the item.
4. Explain what the colon adds to a definition and to a call.

### Accessibility Practice
Say 'colon' aloud in `notebook:describe()` and confirm that your screen reader announces it, since a dot and a colon look similar on screen but behave differently.

### Skills Checklist
- [ ] I can define a method with a colon.
- [ ] I can explain dot versus colon.
- [ ] I can change attributes directly and by method.
- [ ] I can validate in a method.
- [ ] I can read a method call aloud.

## Lesson 7.4: Inheritance

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming), inheritance
- Lua 5.4 Reference Manual: Section 2.4 (Metatables and Metamethods)
- Matching Python lesson: Lesson 7.4 Inheritance

### Learning Objectives
- Create a subclass that inherits from a class.
- Override a method.
- Call the parent's constructor.

### Concept Explanation
*Inheritance* lets one class reuse and extend another. In Lua, a subclass table uses the parent as its metatable's `__index`: `setmetatable(DiscountedItem, {__index = Item})`. The subclass also sets its own `__index`, so its objects find subclass methods first and parent methods next.

The subclass constructor calls the parent constructor, `Item.new(...)`, to build the base object, adds its own fields, and then switches the object's metatable to the subclass.

*Overriding* means defining a method with the same name in the subclass. The inherited `describe` method calls `self:total_value()`, so it automatically uses the overridden version. This is *polymorphism*: one method name, different behavior for different classes.

The example discounts the shared Folder (4 at 1.25) by 20 percent, so its value is 4.00 instead of 5.00.

### Worked Example
```lua
local Item = {}
Item.__index = Item

function Item.new(name, quantity, unit_price)
  return setmetatable({name = name, quantity = quantity, unit_price = unit_price}, Item)
end

function Item:total_value()
  return self.quantity * self.unit_price
end

function Item:describe()
  print(string.format("%s: %d at %.2f each, value %.2f", self.name, self.quantity, self.unit_price, self:total_value()))
end

local DiscountedItem = setmetatable({}, {__index = Item})
DiscountedItem.__index = DiscountedItem

function DiscountedItem.new(name, quantity, unit_price, discount_rate)
  local object = Item.new(name, quantity, unit_price)
  object.discount_rate = discount_rate
  return setmetatable(object, DiscountedItem)
end

function DiscountedItem:total_value()
  return Item.total_value(self) * (1 - self.discount_rate)
end

local folder = DiscountedItem.new("Folder", 4, 1.25, 0.20)
folder:describe()
print(getmetatable(folder) == DiscountedItem)
```

### Expected Behavior or Output
The program prints:
```text
Folder: 4 at 1.25 each, value 4.00
true
```

### Common Mistakes
1. Forgetting to give the subclass its own `__index`, so its objects cannot find subclass methods.
2. Calling `Item.new` and forgetting to change the metatable, so the object is still a plain `Item`.
3. Calling `Item.total_value()` with a dot and no object, which leaves `self` as `nil`.

### Activities
1. Predict the printed value and the final `true` or `false`.
2. Add a subclass `PerishableItem` with an `expires` field and override `describe`.
3. Explain why `describe` prints the discounted value without being redefined.
4. Draw the lookup chain from `folder` to `DiscountedItem` to `Item` as a numbered list.

### Accessibility Practice
Describe inheritance as an ordered lookup list: the object, then its class, then the parent. Speaking the chain aloud is clearer than a diagram.

### Skills Checklist
- [ ] I can create a subclass.
- [ ] I can override a method.
- [ ] I can call the parent constructor.
- [ ] I can explain polymorphism.
- [ ] I can describe the lookup chain.

## Lesson 7.5: Composition

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming)
- Lua 5.4 Reference Manual: Section 3.4.9 (Table Constructors)
- Matching Python lesson: Lesson 7.5 Instances as Attributes (Composition)

### Learning Objectives
- Explain composition ("has a").
- Store objects inside another object.
- Build an inventory from the shared items.

### Concept Explanation
*Composition* means one object contains other objects. An inventory *has* items, as opposed to an item *being* a kind of inventory. Composition is often simpler and safer than inheritance when objects are related by containment.

In Lua, the container keeps a list of its parts. The container's methods loop over the parts and call each part's own methods, so the container does not need to know how a part works.

The example builds an `Inventory` with the three shared items and reports each quantity and the total value, 17.50.

### Worked Example
```lua
local Item = {}
Item.__index = Item
function Item.new(name, quantity, unit_price)
  return setmetatable({name = name, quantity = quantity, unit_price = unit_price}, Item)
end
function Item:total_value()
  return self.quantity * self.unit_price
end

local Inventory = {}
Inventory.__index = Inventory
function Inventory.new()
  return setmetatable({items = {}}, Inventory)
end
function Inventory:add(item)
  self.items[#self.items + 1] = item
end
function Inventory:total_value()
  local total = 0
  for _, item in ipairs(self.items) do total = total + item:total_value() end
  return total
end
function Inventory:report()
  for _, item in ipairs(self.items) do
    print(string.format("%s: %d", item.name, item.quantity))
  end
  print(string.format("Total value: %.2f", self:total_value()))
end

local inventory = Inventory.new()
inventory:add(Item.new("Notebook", 3, 2.50))
inventory:add(Item.new("Pencil", 10, 0.50))
inventory:add(Item.new("Folder", 4, 1.25))
inventory:report()
```

### Expected Behavior or Output
The program prints:
```text
Notebook: 3
Pencil: 10
Folder: 4
Total value: 17.50
```

### Common Mistakes
1. Using inheritance where a "has a" relationship is meant.
2. Letting the container reach into each item's fields instead of calling the item's methods.
3. Giving every new `Inventory` the same shared `items` table by putting it on the class instead of in `new`.

### Activities
1. Predict the output.
2. Add `Inventory:find(name)` that returns the item with that name or `nil`.
3. Add `Inventory:remove(name)` and test it.
4. Explain the difference between "is a" and "has a" with two examples.

### Accessibility Practice
Report the inventory as one labelled line per item and a final total line, so a screen reader reads a complete summary in sequence.

### Skills Checklist
- [ ] I can explain composition.
- [ ] I can store objects inside an object.
- [ ] I can loop over parts and call their methods.
- [ ] I can say "is a" versus "has a".
- [ ] I can build the shared inventory.

# Unit 8: Files and Exceptions

## Overview

Read and write files, handle errors with `pcall`, close resources reliably, and store records as JSON with a small teaching helper.

## Lesson 8.1: Reading from a File

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 7 (The External World)
- Lua 5.4 Reference Manual: Section 6.8 (File Operations)
- Matching Python lesson: Lesson 8.1 Reading from a File

### Learning Objectives
- Open a file for reading and check the result.
- Read the whole file or one line at a time.
- Report a missing file clearly.

### Concept Explanation
`io.open(path, mode)` returns a file handle, or `nil` plus an error message and an error number when it fails. Always check the result. Mode `"r"` reads. Methods are called with a colon on the handle: `file:read("a")` reads everything, `file:read("l")` reads one line, and `file:lines()` gives an iterator over the lines.

A relative path starts from the working directory, so a program run from a different folder will not find the file. A file handle uses a system resource, so close it with `file:close()` when finished.

To keep this lesson self-contained, the example first writes the two-line `notes.txt` used by every language track, then reads it back three ways. The missing-file case prints the message that `io.open` returns.

### Worked Example
```lua
local out = assert(io.open("notes.txt", "w"))
out:write("Practice Lua.\nReview tables and functions.\n")
out:close()

local file, err = io.open("notes.txt", "r")
if not file then
  print("Could not open notes.txt: " .. err)
  return
end
local contents = file:read("a")
file:close()
print(contents)

for line in io.lines("notes.txt") do
  print(line)
end

local count = 0
for _ in io.lines("notes.txt") do count = count + 1 end
print(count)

local missing, message = io.open("missing_notes.txt", "r")
print(missing, message)
```

### Expected Behavior or Output
The program prints:
```text
Practice Lua.
Review tables and functions.

Practice Lua.
Review tables and functions.
2
nil	missing_notes.txt: No such file or directory
```

### Common Mistakes
1. Not checking the result of `io.open` and then calling a method on `nil`.
2. Forgetting to close the file.
3. Using a relative path from a different working directory.

### Activities
1. Run the program and describe each block of output.
2. Add a third line to `notes.txt` and predict the new count.
3. Print each line with its line number.
4. Open a file that does not exist and print a friendly message that includes the file name.

### Accessibility Practice
Read the output aloud in order. Make error messages complete sentences that include the file name, so they are clear without seeing the screen.

### Skills Checklist
- [ ] I can open a file and check the result.
- [ ] I can read it whole or by line.
- [ ] I can close a file.
- [ ] I can report a missing file.
- [ ] I can explain the working directory.

## Lesson 8.2: Writing to a File

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 7 (The External World)
- Lua 5.4 Reference Manual: Section 6.8 (file:write)
- Matching Python lesson: Lesson 8.2 Writing to a File

### Learning Objectives
- Write with mode `"w"` and append with mode `"a"`.
- Check for failure when writing.
- Read the file back to verify.

### Concept Explanation
Mode `"w"` creates the file or *overwrites* an existing one. Mode `"a"` adds to the end. `file:write(text)` writes exactly the text you give, so include `\n` where a line should end. `file:write` returns the file handle on success and `nil` plus a message on failure, so it can also be checked.

A closed file is the only way to be certain that the data reached storage. Always close, then reopen to verify.

The example writes the first notes line, appends the second, and reads the file back.

### Worked Example
```lua
local file = assert(io.open("notes.txt", "w"))
file:write("Practice Lua.\n")
file:close()

file = assert(io.open("notes.txt", "a"))
file:write("Review tables and functions.\n")
file:close()

file = assert(io.open("notes.txt", "r"))
print(file:read("a"))
file:close()
```

### Expected Behavior or Output
The program prints:
```text
Practice Lua.
Review tables and functions.
```

### Common Mistakes
1. Using `"w"` when `"a"` was intended, which erases earlier content.
2. Forgetting `\n`, so all lines run together.
3. Not closing the file before reading it back.

### Activities
1. Predict the output, then run.
2. Change the second open to mode `"w"` and explain the difference.
3. Append a third line with the current count of lines.
4. Write the shared scores, one per line, then read them back and total them.

### Accessibility Practice
Always read a written file back in the terminal to confirm it, using line navigation, so you do not rely on assumptions about what was saved.

### Skills Checklist
- [ ] I can write and append.
- [ ] I know `"w"` overwrites.
- [ ] I can include new lines.
- [ ] I can verify by reading back.
- [ ] I can check for a write failure.

## Lesson 8.3: Errors and pcall

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 16 (Compilation, Execution, and Errors)
- Lua 5.4 Reference Manual: Section 2.3 (Error Handling) and Section 6.1 (pcall, error, assert)
- Matching Python lesson: Lesson 8.3 Exceptions - Handling Errors

### Learning Objectives
- Raise an error with `error` and `assert`.
- Catch an error with `pcall`.
- Handle a missing file and malformed data.

### Concept Explanation
Lua reports problems in two ways. Library functions such as `io.open` and `tonumber` usually *return* `nil` plus a message. Other problems *raise an error*, which stops the program unless it is caught. `error(message, level)` raises an error. `assert(value, message)` raises an error when `value` is false or `nil`.

`pcall(function)` runs a function in *protected mode*. It returns `true` plus the function's results on success, or `false` plus the error value on failure, and the program continues.

Error messages from `error` normally start with a file name and line number. Pass level `0` to leave the position out, which makes a message easier to test. An error value may be any value, including a table.

Integer division by zero (`10 // 0`) raises an error, while float division (`10 / 0`) returns `inf`. Runtime error messages from Lua include the file name and line number, and their exact wording can differ between Lua versions, so the example prints only the type of that error value. The example catches a missing file, an invalid number, and an integer division by zero.

### Worked Example
```lua
local file, message = io.open("missing_notes.txt", "r")
if not file then
  print("Error: missing_notes.txt was not found.")
end

local score = tonumber("abc")
if not score then
  print("Error: 'abc' is not a valid score.")
end

local ok, err = pcall(function() return 10 // 0 end)
print(ok, type(err))
print(10 / 0)

local ok2, err2 = pcall(function() error("custom failure", 0) end)
print(ok2, err2)

local ok3, err3 = pcall(assert, false, "assertion message")
print(ok3, err3)
```

### Expected Behavior or Output
The program prints:
```text
Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score.
false	string
inf
false	custom failure
false	assertion message
```

### Common Mistakes
1. Using `pcall` to hide errors without reporting them.
2. Forgetting that `error` messages include a position unless the level is 0.
3. Expecting `10 / 0` to raise an error. It returns `inf`; only integer division by zero raises one.

### Activities
1. Predict each printed line before running, then print `err` to see the full message including the file name and line.
2. Wrap a call to `tonumber` and arithmetic so invalid input prints a clear message.
3. Raise an error with a table value and read its fields after catching it.
4. Explain when to return `nil, message` and when to call `error`.

### Accessibility Practice
Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.'

### Skills Checklist
- [ ] I can raise and catch errors.
- [ ] I can use `assert` and `pcall`.
- [ ] I know `io.open` returns a message instead of raising.
- [ ] I know integer and float division by zero differ.
- [ ] I can write clear error messages.

## Lesson 8.4: Cleanup and Resource Safety

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 16 (Compilation, Execution, and Errors)
- Lua 5.4 Reference Manual: Section 3.3.8 (To-be-closed Variables)
- Matching Python lesson: Lesson 8.4 The else and finally Blocks

### Learning Objectives
- Close files reliably, even when an error occurs.
- Use a to-be-closed variable (`<close>`).
- Use `pcall` to guarantee cleanup.

### Concept Explanation
Lua has no `try`/`finally`. Two techniques make cleanup reliable. The manual technique runs the risky work inside `pcall`, closes the resource afterward, then re-raises the error if there was one.

Lua 5.4 adds *to-be-closed variables*: `local file <close> = io.open(...)`. When the variable goes out of scope (normally or through an error) Lua calls its `__close` metamethod. File handles already provide it, so the file is closed automatically. `<close>` needs Lua 5.4.

`io.type(handle)` reports `"file"`, `"closed file"`, or `nil`. The example keeps a reference to each handle so it can check that the file is closed after the block ends and after an error.

### Worked Example
```lua
local saved
do
  local file <close> = assert(io.open("cleanup_demo.txt", "w"))
  saved = file
  file:write("Some data.\n")
end
print(io.type(saved))

local saved2
local ok, err = pcall(function()
  local file <close> = assert(io.open("cleanup_demo.txt", "w"))
  saved2 = file
  error("failure while writing", 0)
end)
print(ok, err, io.type(saved2))

local manual = assert(io.open("cleanup_demo.txt", "r"))
local ok3, content = pcall(function() return manual:read("a") end)
manual:close()
print(ok3, content, io.type(manual))
```

### Expected Behavior or Output
The program prints:
```text
closed file
false	failure while writing	closed file
true		closed file
```

### Common Mistakes
1. Using `<close>` on Lua 5.3 or earlier, where it is a syntax error.
2. Returning from a function before closing a manually opened file.
3. Closing a file twice and reading the error.

### Activities
1. Predict the three printed lines.
2. Rewrite the manual example with `<close>`.
3. Raise an error before the write in the second example and confirm the file is still closed.
4. Explain why cleanup matters even if the program is about to end.

### Accessibility Practice
Print the file state (`io.type`) after each step. Short, labelled status lines are easy to follow with a screen reader.

### Skills Checklist
- [ ] I can close files reliably.
- [ ] I can use `<close>`.
- [ ] I can protect cleanup with `pcall`.
- [ ] I can check a handle with `io.type`.
- [ ] I know `<close>` needs Lua 5.4.

## Lesson 8.5: Storing Data with JSON

### Reading References
- Programming in Lua, 4th edition: Chapter 15 (Data Files and Serialization)
- Lua 5.4 Reference Manual: Section 6.8 (Input and Output Facilities)
- JSON specification: https://www.json.org
- Matching Python lesson: Lesson 8.5 Storing Data with JSON

### Learning Objectives
- Explain why Lua needs a JSON helper.
- Encode and decode the shared task records.
- Handle a missing or malformed file.

### Concept Explanation
Lua's standard library has no JSON support. Real projects install a maintained library through LuaRocks, such as `dkjson` or `lua-cjson`. To keep this course free of external dependencies, the example includes a *teaching implementation* of `json.encode` and `json.decode`. It is intentionally small: it handles strings, numbers, booleans, `null`, lists, and objects, writes object keys in sorted order, and reports malformed text with an error that includes the position. It is not a replacement for a production library.

JSON text stores data in a standard format. An object `{ ... }` holds key-value pairs, a list `[ ... ]` holds ordered items, and text is in double quotation marks. Decoding turns text into Lua tables, so decoded data should be validated before use.

The shared to-do record has the fields `id`, `title`, `description`, `done`, and `created_at`. The example saves two tasks and loads them back. It also shows what a malformed file produces.

### Language-Specific Semantics
The helper's `json.decode` turns JSON `null` into `nil`, so a key with a `null` value is simply absent from the decoded table. It does not handle every escape or number edge case that a full parser must, and it assumes the text is valid UTF-8.

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

local tasks = {
  {id = 1, title = "Study programming", description = "Finish Unit 8", done = false, created_at = "2026-01-15T09:00:00"},
  {id = 2, title = "Review scores", description = "Check the four scores", done = true, created_at = "2026-01-15T09:30:00"},
}

local file = assert(io.open("tasks.json", "w"))
file:write(json.encode(tasks))
file:close()

local input = io.open("tasks.json", "r")
if not input then
  print("Tasks file not found.")
  return
end
local text = input:read("a")
input:close()

local ok, loaded = pcall(json.decode, text)
if not ok then
  print("Error: could not decode tasks file: " .. loaded)
  return
end
for _, task in ipairs(loaded) do
  print(string.format("%d: %s (%s)", task.id, task.title, task.done and "done" or "not done"))
end

print(pcall(json.decode, '[{"id": 1,'))
```

### Expected Behavior or Output
The program prints:
```text
1: Study programming (not done)
2: Review scores (done)
false	expected a key at position 11
```

### Common Mistakes
1. Assuming Lua has built-in JSON support.
2. Trusting decoded data without checking that each field exists and has the right type.
3. Overwriting a good data file with an empty table after a failed load.

### Activities
1. Run the program and read the saved JSON text from `tasks.json`.
2. Edit `tasks.json` by hand to remove a closing bracket and rerun. Read the error message.
3. Add a third task and confirm it is saved and loaded.
4. Explain why a production project should use a maintained JSON library.

### Accessibility Practice
Open `tasks.json` in the terminal and read it as text. JSON in a single line is difficult to navigate, so practise stepping through it by word or character.

### Skills Checklist
- [ ] I know Lua has no built-in JSON.
- [ ] I can encode and decode records.
- [ ] I handle missing and malformed files.
- [ ] I validate decoded data.
- [ ] I know when to use a library.

# Unit 9: Testing and Data Analysis

## Overview

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

# Unit 10: Project-Based Learning

## Overview

Plan a text project, build the shared text adventure in two parts, build the command-line to-do manager, and refine input validation.

## Lesson 10.1: Planning a Text-Based Project

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions) and Chapter 5 (Tables)
- Lua 5.4 Reference Manual: Section 3.3 (Statements)
- Matching Python lesson: Lesson 10.1 Project Planning and Design

### Learning Objectives
- Write a short requirements list.
- Design a command loop with a table of handlers.
- Plan in small steps and test each one.

### Concept Explanation
A project is easier to finish when you plan it in small steps. Write down *what the program must do* (requirements), *what information it keeps* (data), and *the commands a person can give* (interface). Build one small piece, test it, and then add the next.

Text-based projects share a *command loop*: show a prompt, read a line, find the matching action, and repeat until the user quits. A good Lua design stores actions in a table whose keys are command names and whose values are functions. A new command is then one new entry, and an unknown command is a failed lookup that prints a helpful message.

The loop must stop when the input ends (`nil`) as well as on `quit`.

The example is a skeleton with three commands. Typing `help`, `look`, an unknown word, and `quit` shows each path.

### Worked Example
```lua
local commands = {
  help = function() print("Commands: help, look, quit") end,
  look = function() print("You are in a dark cave.") end,
}

print("Type a command:")
local line = io.read()
while line ~= nil and line ~= "quit" do
  local handler = commands[line]
  if handler then
    handler()
  else
    print("I don't understand that command. Type help for a list.")
  end
  print("Type a command:")
  line = io.read()
end
print("Goodbye!")
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
help
look
dance
quit
```

the program prints:
```text
Type a command:
Commands: help, look, quit
Type a command:
You are in a dark cave.
Type a command:
I don't understand that command. Type help for a list.
Type a command:
Goodbye!
```

### Common Mistakes
1. Starting to code before listing the requirements.
2. Using a long chain of `if` statements for commands instead of a table of handlers.
3. Forgetting that an unknown command should explain what to do next.

### Activities
1. Write five requirements for the text adventure and the to-do list.
2. Add a `score` command that prints the shared scores.
3. Add the command aliases `h` and `l` without copying the functions.
4. Describe the data for the capstone in three sentences.

### Accessibility Practice
Prompts and responses are on separate lines and every response is a complete sentence. Test the prompts by listening to them before you add features.

### Skills Checklist
- [ ] I can list requirements.
- [ ] I can design a command loop.
- [ ] I can use a table of handlers.
- [ ] I handle unknown commands.
- [ ] I handle the end of input.

## Lesson 10.2: Text Adventure, Part 1: Rooms and Movement

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables)
- Lua 5.4 Reference Manual: Section 3.4.9 (Table Constructors)
- Matching Python lesson: Lesson 10.2 Building a Text-Based Adventure Game (Part 1)

### Learning Objectives
- Represent rooms and exits with tables.
- Move the player by command.
- Handle impossible moves and the end of input.

### Concept Explanation
A room is a table with a `description` and an `exits` table that maps a direction to the name of another room. The program remembers the player's location in one variable, `current_room`. A move looks up the command in the current room's exits; if it is found, `current_room` changes, otherwise the program explains that the move is impossible.

This is the same three-room layout as the Python course: a cave, a tunnel, and a clearing. Part 2 adds items and a locked door.

The example is played with the commands north, east, west, up, south, and quit. The command `up` is not an exit anywhere, so it prints the help message.

### Worked Example
```lua
local rooms = {
  start_room = {
    description = "You are in a dimly lit cave. There's a narrow passage to the NORTH.",
    exits = {north = "tunnel"},
  },
  tunnel = {
    description = "The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.",
    exits = {south = "start_room", east = "clearing"},
  },
  clearing = {
    description = "You've reached a small, sunny clearing. A faint path leads WEST.",
    exits = {west = "tunnel"},
  },
}

local current_room = "start_room"

while true do
  print("---")
  print(rooms[current_room].description)
  print("What do you want to do?")
  local command = io.read()
  if command == nil then command = "quit" end
  command = command:lower()

  if rooms[current_room].exits[command] then
    current_room = rooms[current_room].exits[command]
  elseif command == "quit" then
    print("Exiting game. Goodbye!")
    break
  else
    print("I don't understand that command or you can't go that way.")
  end
end
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
north
east
west
up
south
quit
```

the program prints:
```text
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You've reached a small, sunny clearing. A faint path leads WEST.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
I don't understand that command or you can't go that way.
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Looking up a direction that is not in `exits` and expecting an error. The lookup returns `nil`, which is the signal to explain the move is impossible.
2. Forgetting to treat the end of input as `quit`, so the program loops forever when input is piped in.
3. Misspelling a room name in `exits`, so the move leads to a room that does not exist.

### Activities
1. Trace the six commands by hand and write the room after each one.
2. Add a fourth room reached from the clearing and test it.
3. Add the aliases `n`, `s`, `e`, and `w`.
4. Check that every exit names a real room by writing a loop that tests the whole table.

### Accessibility Practice
Each turn prints a separator line, the description, and the prompt on its own line. Listen to a whole turn to confirm that a player could follow it without seeing the screen.

### Skills Checklist
- [ ] I can represent rooms with tables.
- [ ] I can move the player by command.
- [ ] I can handle an impossible move.
- [ ] I treat end of input as quit.
- [ ] I can trace a game by hand.

## Lesson 10.3: Text Adventure, Part 2: Items and a Locked Door

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables) and Chapter 6 (Functions)
- Lua 5.4 Reference Manual: Section 6.6 (Table Manipulation)
- Matching Python lesson: Lesson 10.3 Building a Text-Based Adventure Game (Part 2)

### Learning Objectives
- Keep items in rooms and in an inventory.
- Implement take and use commands.
- Block and then allow a move with a locked door.

### Concept Explanation
Part 2 adds *state*: items in rooms, an inventory, and a door that is locked until the player uses the key. This is the shared specification used by every language track: three rooms (`start`, `locked_door_room`, `treasure_room`); the commands `north`, `south`, `east`, `west`, `take shiny key`, `use shiny key`, and `quit`; the door between the chamber and the treasure room stays locked until the key is used there; reaching the treasure room ends the game.

Items are lists of names. Taking an item removes it from the room's list and appends it to the inventory. The locked door is a Boolean variable, `door_locked`. A move through the door checks it first.

The program is played with: north (into the chamber), north (the locked door refuses), south, take shiny key, north, use shiny key, north (the treasure room).

### Worked Example
```lua
local rooms = {
  start = {
    description = "A dark cave.",
    exits = {north = "locked_door_room"},
    items = {"shiny key"},
  },
  locked_door_room = {
    description = "A small chamber with a heavy door to the NORTH.",
    exits = {south = "start", north = "treasure_room"},
    items = {},
  },
  treasure_room = {
    description = "A glittering room full of treasure. You win!",
    exits = {south = "locked_door_room"},
    items = {},
  },
}

local function index_of(list, value)
  for index, item in ipairs(list) do
    if item == value then return index end
  end
  return nil
end

local current_room = "start"
local inventory = {}
local door_locked = true

while true do
  local room = rooms[current_room]
  print("")
  print(room.description)
  if current_room == "treasure_room" then break end
  if #room.items > 0 then print("You see: " .. table.concat(room.items, ", ")) end
  print("Your inventory: " .. (#inventory > 0 and table.concat(inventory, ", ") or "empty"))
  print("What do you want to do?")

  local command = io.read()
  if command == nil then command = "quit" end
  command = command:lower()

  if command == "take shiny key" and index_of(room.items, "shiny key") then
    table.remove(room.items, index_of(room.items, "shiny key"))
    inventory[#inventory + 1] = "shiny key"
    print("You picked up the shiny key.")
  elseif command == "use shiny key" and current_room == "locked_door_room" and index_of(inventory, "shiny key") then
    door_locked = false
    print("You unlocked the door!")
  elseif room.exits[command] then
    if current_room == "locked_door_room" and command == "north" and door_locked then
      print("The door is locked! You need a key.")
    else
      current_room = room.exits[command]
    end
  elseif command == "quit" then
    print("Exiting game. Goodbye!")
    break
  else
    print("I don't understand that command.")
  end
end
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
north
north
south
take shiny key
north
use shiny key
north
```

the program prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?
The door is locked! You need a key.

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?
You picked up the shiny key.

A dark cave.
Your inventory: shiny key
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?
You unlocked the door!

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?

A glittering room full of treasure. You win!
```

### Common Mistakes
1. Making the door's locked state part of the exits so that the "locked" message can never be reached.
2. Defining an exit to a room that is missing from the `rooms` table, which crashes when the player arrives.
3. Printing a fixed room description that still mentions an item after the player has taken it.

### Activities
1. Play the program with the shown commands and follow each turn on paper.
2. Try `use shiny key` in the cave and describe what happens.
3. Add a second item and require both to open the door.
4. Write a short list of the game's states (location, inventory, door) and say which command changes each.

### Accessibility Practice
The room description never mentions the key. The separate line 'You see:' lists items, so the description stays true after the key is taken and the screen reader announces the current state.

### Skills Checklist
- [ ] I can store items in rooms and an inventory.
- [ ] I can implement take and use commands.
- [ ] I can block and allow a move.
- [ ] I can list the game's state variables.
- [ ] I can keep descriptions true after state changes.

## Lesson 10.4: Command-Line To-Do List

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 15 (Data Files and Serialization)
- Lua 5.4 Reference Manual: Section 6.8 (Input and Output Facilities)
- Matching Python lesson: Lesson 10.4 Building a Command-Line To-Do List

### Learning Objectives
- Keep records with the shared fields.
- Save and load them as JSON.
- Offer add, view, mark-done, save, load, and quit commands.

### Concept Explanation
A to-do list ties together records, loops, functions, and files. Each task has the shared fields `id`, `title`, `description`, `done`, and `created_at`. The program keeps a list of tasks in memory, shows a numbered menu, and saves the list to `todos.json` when asked and on exit.

Saving uses the teaching JSON helper from Lesson 8.5 (included here so the example runs on its own). On start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program: it prints a message and starts with an empty list.

New ids are one more than the highest existing id, so ids stay unique even after a task is removed. The status is shown as the words `done` and `not done`, never with a symbol or color alone.

In the sample session the user adds two tasks, views the list, marks task 2 as done, views it again, tries an invalid menu choice, views the list, and quits.

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

local TODO_FILE = "todos.json"
local todos = {}

local function load_todos()
  local file = io.open(TODO_FILE, "r")
  if not file then
    print("No existing tasks found.")
    todos = {}
    return
  end
  local text = file:read("a")
  file:close()
  local ok, data = pcall(json.decode, text)
  if ok and type(data) == "table" then
    todos = data
    print("Tasks loaded.")
  else
    print("Error: todos.json is not valid JSON. Starting with an empty list.")
    todos = {}
  end
end

local function save_todos()
  local file = assert(io.open(TODO_FILE, "w"))
  file:write(json.encode(todos))
  file:close()
  print("Tasks saved.")
end

local function next_id()
  local highest = 0
  for _, task in ipairs(todos) do
    if task.id > highest then highest = task.id end
  end
  return highest + 1
end

local function add_task(title, description)
  title = (title or ""):match("^%s*(.-)%s*$")
  if title == "" then
    print("A title is required.")
    return
  end
  todos[#todos + 1] = {
    id = next_id(),
    title = title,
    description = (description or ""):match("^%s*(.-)%s*$"),
    done = false,
    created_at = os.date("!%Y-%m-%dT%H:%M:%S"),
  }
  print("Task '" .. title .. "' added.")
end

local function view_tasks()
  if #todos == 0 then
    print("No tasks in your list.")
    return
  end
  print("--- Your To-Do List ---")
  for _, task in ipairs(todos) do
    print(string.format("%d. %s (%s)", task.id, task.title, task.done and "done" or "not done"))
  end
  print("-----------------------")
end

local function mark_done(text)
  local id = tonumber(text)
  if not id then
    print("Please enter a whole number.")
    return
  end
  for _, task in ipairs(todos) do
    if task.id == id then
      task.done = true
      print("Task '" .. task.title .. "' marked as done.")
      return
    end
  end
  print("No task has that number.")
end

local function show_menu()
  print("")
  print("--- To-Do List Menu ---")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task Done")
  print("4. Save Tasks")
  print("5. Load Tasks")
  print("6. Quit")
  print("-----------------------")
end

load_todos()
while true do
  show_menu()
  print("Enter your choice (1-6):")
  local choice = io.read()
  if choice == nil then choice = "6" end

  if choice == "1" then
    print("Enter task title:")
    local title = io.read()
    print("Enter task description:")
    local description = io.read()
    add_task(title, description)
  elseif choice == "2" then
    view_tasks()
  elseif choice == "3" then
    view_tasks()
    print("Enter task number to mark done:")
    mark_done(io.read())
  elseif choice == "4" then
    save_todos()
  elseif choice == "5" then
    load_todos()
  elseif choice == "6" then
    save_todos()
    print("Goodbye!")
    break
  else
    print("Invalid choice. Please try again.")
  end
end
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
1
Study programming
Finish Unit 10
1
Review scores
Check the four scores
2
3
2
3
7
2
6
```

the program prints:
```text
No existing tasks found.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Study programming' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Review scores' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------
Enter task number to mark done:
Task 'Review scores' marked as done.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------
Enter task number to mark done:
No task has that number.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Tasks saved.
Goodbye!
```

### Common Mistakes
1. Saving the file but never loading it, so tasks disappear between runs.
2. Reusing a deleted task's id, which can confuse saved references.
3. Letting a damaged `todos.json` crash the program instead of printing a message.

### Activities
1. Run the sample session and then run the program again with the input `2` then `6` to see the saved tasks.
2. Add a command to delete a task by number.
3. Open `todos.json` and read the saved text. Edit it to remove a bracket and rerun.
4. Add a `description` display to the view command.

### Accessibility Practice
Every menu is printed as numbered lines and each prompt is on its own line. The status words are `done` and `not done`, not symbols, so the list reads clearly in speech and braille.

### Skills Checklist
- [ ] I can keep records with the shared fields.
- [ ] I can save and load JSON.
- [ ] I handle a missing or damaged file.
- [ ] I keep ids unique.
- [ ] I show status in words.

## Lesson 10.5: User Experience and Input Validation

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions) and Chapter 16 (Compilation, Execution, and Errors)
- Lua 5.4 Reference Manual: Section 6.8 (io.read)
- Matching Python lesson: Lesson 10.5 Refining User Experience and Validation

### Learning Objectives
- Write reusable validation functions.
- Limit retries and handle the end of input.
- Write clear, accessible messages.

### Concept Explanation
Reusable validation functions make every menu and form consistent. `ask_number(prompt, low, high, attempts)` prints a prompt, reads a line, converts it, checks the range, and either returns the number or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns `nil` and a reason. `ask_yes_no(prompt)` accepts `y`, `yes`, `n`, and `no`, in any letter case.

Good messages say *what was wrong* and *what to do*: "Enter a whole number from 0 to 100," not "Invalid." They never depend on color, position, or symbols alone, and they use the same wording every time.

The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y.

### Worked Example
```lua
local function ask_number(prompt, low, high, attempts)
  for attempt = 1, attempts do
    print(prompt)
    local text = io.read()
    if text == nil then return nil, "No more input." end
    local number = tonumber(text)
    if number and number == math.floor(number) and number >= low and number <= high then
      return math.tointeger(number)
    end
    print(string.format("Enter a whole number from %d to %d. You have %d attempt(s) left.", low, high, attempts - attempt))
  end
  return nil, "Too many invalid attempts."
end

local function ask_yes_no(prompt)
  while true do
    print(prompt .. " (yes or no)")
    local text = io.read()
    if text == nil then return nil end
    text = text:lower()
    if text == "y" or text == "yes" then return true end
    if text == "n" or text == "no" then return false end
    print("Please answer yes or no.")
  end
end

local score, reason = ask_number("Enter a score from 0 to 100:", 0, 100, 3)
if score then
  print("Accepted score: " .. score)
else
  print("No score: " .. reason)
end

local keep = ask_yes_no("Save this score?")
print("Save answer:", keep)
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
abc
105
88
maybe
y
```

the program prints:
```text
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 2 attempt(s) left.
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 1 attempt(s) left.
Enter a score from 0 to 100:
Accepted score: 88
Save this score? (yes or no)
Please answer yes or no.
Save this score? (yes or no)
Save answer:	true
```

### Common Mistakes
1. Writing the message "Invalid" without saying what is valid.
2. Accepting a decimal such as 88.5 for a field that requires a whole number.
3. Looping forever on bad input instead of limiting attempts.

### Activities
1. Run the sample input and read each message aloud.
2. Run with three invalid numbers and read the final message.
3. Add a function `ask_text(prompt)` that rejects empty answers.
4. Rewrite two messages from earlier lessons so they say what to do next.

### Accessibility Practice
Check that every error message ends with an action the user can take, and that the same situation always produces the same words.

### Skills Checklist
- [ ] I can write reusable validation functions.
- [ ] I limit retries.
- [ ] I handle the end of input.
- [ ] I write messages that say what to do.
- [ ] I keep wording consistent.

# Unit 11: Capstone

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
