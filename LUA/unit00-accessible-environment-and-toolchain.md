# Unit 0: Accessible Environment and Toolchain

## Course overview

# Lua 5.4 — Parallel Introductory Computer Science Course

## Course alignment and implementation notes

This course follows the Python canonical sequence in `lesson_standardization.json`. The shared problem contexts, inputs, records, boundaries, and expected results are preserved; Lua syntax and idioms are taught directly rather than transliterated from Python. Lua tables represent sequences, maps, and records; sequences are one-indexed; only `false` and `nil` are false; `pairs` does not guarantee order; `ipairs` traverses a consecutive sequence. Lua has no built-in class, tuple, continue statement, or JSON library. These differences are taught explicitly.

**Runtime:** Lua 5.4. Run a file with `lua5.4 filename.lua`; syntax-check with `luac5.4 -p filename.lua`. Use local variables by default. The Lua standard library does not include a JSON or general CSV parser; capstone persistence must declare and document an approved dependency (for example, dkjson), and CSV parsing must use a tested parser when quoted fields are in scope.

## Accessibility and lesson conventions

Use the terminal and keyboard for every exercise. Read code and output sequentially; describe braces, brackets, quotes, punctuation, and indentation in prose. Do not communicate status through color alone. Provide explicit prompts, errors, confirmations, and textual equivalents for any visual output. The course does not claim screen-reader or braille verification until those workflows have been tested on named platforms.

Each lesson includes a focused explanation, runnable worked example, expected behavior, common mistakes, practice, accessibility practice, and a skills check. Save each fenced example to a separate file or copy it into the Lua REPL.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)
