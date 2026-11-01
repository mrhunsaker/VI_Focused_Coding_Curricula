# Lua: Complete Curriculum — Units 0–11

## Course Overview

Lua is a lightweight embeddable scripting language used in games, embedded applications, configuration, automation, and extensible software. This course follows the original Python curriculum's problem contexts so learners can focus on Lua syntax and semantics. It teaches Lua's tables, functions as values, multiple returns, metatables, modules, coroutines, and integration with host applications.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install Lua, create a project folder, and verify keyboard and screen-reader access.

### Lesson 0.1: Install and Verify Lua

Install Lua 5.4 from lua.org or your operating-system package manager. Verify `lua -v`; run a file with `lua main.lua` and experiment in the interpreter.

### Lesson 0.2: Workspace and First Run
Create a course folder, save `main.lua`, run `lua main.lua`, and read interpreter errors. Use the interactive interpreter for short experiments and files for saved programs.

### Lesson 0.3: Editor and Accessibility Workflow
Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md). Test keyboard navigation, punctuation announcement, indentation, terminal focus, diagnostics, and project navigation. Install only a trusted Lua language extension.

### Skills Checklist
- [ ] I can verify Lua installation.
- [ ] I can create and run a Lua source file.
- [ ] I can navigate the editor and read output accessibly.

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

Use the terminal from the project root and understand the current working directory. Keep each project in its own folder and distinguish source files, build output, and dependency metadata. Use LuaRocks only when an external package is required. Explain rockspec files and local versus system-wide installation. Keep the introductory exercises on the Lua standard library; run scripts from the project folder and learn module search paths before adding dependencies.

### Skills Checklist
- [ ] I can identify the project root and run commands from it.
- [ ] I can explain where project dependencies are recorded, if applicable.
- [ ] I can run the program or test command from the terminal and read its output.

# Unit 1: Foundations of Computing

## Overview

This unit follows the matching Python unit's objectives and familiar problem contexts. Lua's dynamic values, table model, and lightweight runtime are the language-specific learning targets.

## Lesson 1.1: Computer science and problem solving

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain computer science and problem solving in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Computer science and problem solving. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local item1 = {name = "Avery", score = 71}
print(item1.name, item1.score)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 1.2: Your first Lua program and interpreter

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain your first lua program and interpreter in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Your first Lua program and interpreter. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local values2 = {2, 3, 4}
local total2 = 0
for _, value in ipairs(values2) do total2 = total2 + value end
print(total2 / #values2)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 1.3: Variables, values, and dynamic types

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain variables, values, and dynamic types in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Variables, values, and dynamic types. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local text3 = "Lua lesson 3"
print(text3:upper())
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

# Unit 2: Numeric Computations

## Overview

This unit follows the matching Python unit's objectives and familiar problem contexts. Lua's dynamic values, table model, and lightweight runtime are the language-specific learning targets.

## Lesson 2.1: Software design and tracing

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain software design and tracing in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Software design and tracing. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local function scale4(value) return value * 6 end
print(scale4(4))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 2.2: Expressions, operators, and assignment

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain expressions, operators, and assignment in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Expressions, operators, and assignment. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local score5 = 45
if score5 >= 80 then print("meets target") else print("needs practice") end
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 2.3: Input and output

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain input and output in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Input and output. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local record6 = {id = 6, active = true}
print(record6.id, record6.active)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 2.4: Numeric conversions and math library

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain numeric conversions and math library in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Numeric conversions and math library. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local amount7 = 7.5
print(string.format("%.2f", amount7 * 1.15))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 2.5: Mathematical functions, circle geometry, and distance

### Reading References
- [Lua 5.4 math library](https://www.lua.org/manual/5.4/manual.html#6.7).

### Learning Objectives
- Use math.pi, math.sqrt, and exponentiation.
- Calculate circle area and circumference.
- Calculate distance from the origin.

### Concept Explanation
Lua exposes mathematical functions through the math table. Exponentiation uses ^; math.sqrt computes square roots. Use math.pi for circle calculations and validate that a radius is nonnegative.

### Worked Example
```lua
local radius = 2.5
assert(radius >= 0)
local area = math.pi * radius ^ 2
local circumference = 2 * math.pi * radius
local distance = math.sqrt(6 ^ 2 + 8 ^ 2)
print(string.format("area %.3f; circumference %.3f; distance %.1f", area, circumference, distance))
```

**Expected behavior:** area is approximately 19.635, circumference approximately 15.708, and distance is 10.0.

### Common Mistakes
- Treating ^ as a bitwise operator; in Lua it means exponentiation.
- Squaring the wrong quantity or omitting parentheses in compound expressions.
- Accepting a negative radius or using a rounded value for pi unnecessarily.

### Activities
1. Calculate area and circumference for radii 1, 5, and 10.
2. Verify the distance for a 3-4-5 triangle.
3. Reject a negative radius before calculating.
4. Format results to two decimal places and explain rounding.

### Accessibility Practice
Read the exponentiation operator, parentheses, and decimal formatting aloud; trace intermediate values and inspect terminal output.

### Skills Checklist
- [ ] I can use Lua's math library.
- [ ] I can calculate circle area and circumference.
- [ ] I can calculate distance using math.sqrt.
- [ ] I can validate numeric inputs.
- [ ] I can explain formatted output.

# Unit 3: Control Flow

## Overview

This unit follows the matching Python unit's objectives and familiar problem contexts. Lua's dynamic values, table model, and lightweight runtime are the language-specific learning targets.

## Lesson 3.1: Boolean expressions and if statements

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain boolean expressions and if statements in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Boolean expressions and if statements. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local tasks8 = {"read", "practice", "review"}
table.insert(tasks8, "reflect")
print(table.concat(tasks8, " -> "))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 3.2: Chained conditionals and grade classification

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain chained conditionals and grade classification in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Chained conditionals and grade classification. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local squares9 = {}
for i = 1, 4 do squares9[i] = i * i + 9 end
print(table.concat(squares9, ", "))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 3.3: Tables as sequences and arrays

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain tables as sequences and arrays in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Tables as sequences and arrays. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local number10 = tonumber("10")
assert(number10 ~= nil)
print(number10 + 0.5)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 3.4: Numeric and generic for loops

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain numeric and generic for loops in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Numeric and generic for loops. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local map11 = {first = "Avery", second = "Riley"}
for key, value in pairs(map11) do print(key, value) end
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 3.5: Strings and common operations

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain strings and common operations in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Strings and common operations. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local distance12 = math.sqrt(12 * 12 + 16)
print(string.format("%.2f", distance12))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

# Unit 4: Data Structures

## Overview

This unit follows the matching Python unit's objectives and familiar problem contexts. Lua's dynamic values, table model, and lightweight runtime are the language-specific learning targets.

## Lesson 4.1: Table insertion and removal

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain table insertion and removal in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Table insertion and removal. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local item13 = {name = "Avery", score = 83}
print(item13.name, item13.score)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 4.2: Sorting and organizing tables

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain sorting and organizing tables in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Sorting and organizing tables. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local values14 = {14, 15, 16}
local total14 = 0
for _, value in ipairs(values14) do total14 = total14 + value end
print(total14 / #values14)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 4.3: Multiple assignment and tuple-like returns

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain multiple assignment and tuple-like returns in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Multiple assignment and tuple-like returns. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local text15 = "Lua lesson 15"
print(text15:upper())
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 4.4: Tables as maps and records

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain tables as maps and records in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Tables as maps and records. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local function scale16(value) return value * 4 end
print(scale16(16))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 4.5: Traversing tables safely

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain traversing tables safely in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Traversing tables safely. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local score17 = 57
if score17 >= 80 then print("meets target") else print("needs practice") end
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

# Unit 5: Input and Iteration

## Overview

This unit follows the matching Python unit's objectives and familiar problem contexts. Lua's dynamic values, table model, and lightweight runtime are the language-specific learning targets.

## Lesson 5.1: Input and validation with io.read

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain input and validation with io.read in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Input and validation with io.read. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local record18 = {id = 18, active = true}
print(record18.id, record18.active)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 5.2: Repeat and while loops

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain repeat and while loops in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Repeat and while loops. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local amount19 = 19.5
print(string.format("%.2f", amount19 * 1.15))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 5.3: Flags and early exits

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain flags and early exits in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Flags and early exits. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local tasks20 = {"read", "practice", "review"}
table.insert(tasks20, "reflect")
print(table.concat(tasks20, " -> "))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 5.4: Filtering with break and conditional logic

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain filtering with break and conditional logic in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Filtering with break and conditional logic. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local squares21 = {}
for i = 1, 4 do squares21[i] = i * i + 21 end
print(table.concat(squares21, ", "))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 5.5: Preventing infinite loops

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain preventing infinite loops in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Preventing infinite loops. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local number22 = tonumber("22")
assert(number22 ~= nil)
print(number22 + 0.5)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

# Unit 6: Functions

## Overview

This unit follows the matching Python unit's objectives and familiar problem contexts. Lua's dynamic values, table model, and lightweight runtime are the language-specific learning targets.

## Lesson 6.1: Defining and calling functions

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain defining and calling functions in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Defining and calling functions. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local map23 = {first = "Avery", second = "Riley"}
for key, value in pairs(map23) do print(key, value) end
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 6.2: Parameters, arguments, and multiple returns

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain parameters, arguments, and multiple returns in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Parameters, arguments, and multiple returns. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local distance24 = math.sqrt(24 * 24 + 16)
print(string.format("%.2f", distance24))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 6.3: Return values and scope

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain return values and scope in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Return values and scope. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local item25 = {name = "Avery", score = 95}
print(item25.name, item25.score)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 6.4: Functions over tables

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain functions over tables in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Functions over tables. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local values26 = {26, 27, 28}
local total26 = 0
for _, value in ipairs(values26) do total26 = total26 + value end
print(total26 / #values26)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 6.5: Variadic arguments and closures

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain variadic arguments and closures in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Variadic arguments and closures. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local text27 = "Lua lesson 27"
print(text27:upper())
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

# Unit 7: Object-Oriented Programming

## Overview

This unit follows the matching Python unit's objectives and familiar problem contexts. Lua's dynamic values, table model, and lightweight runtime are the language-specific learning targets.

## Lesson 7.1: Tables as objects and prototypes

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain tables as objects and prototypes in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Tables as objects and prototypes. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local function scale28(value) return value * 2 end
print(scale28(28))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 7.2: Creating instances with constructors

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain creating instances with constructors in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Creating instances with constructors. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local score29 = 69
if score29 >= 80 then print("meets target") else print("needs practice") end
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 7.3: Methods and self

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain methods and self in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Methods and self. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local record30 = {id = 30, active = true}
print(record30.id, record30.active)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 7.4: Metatables and inheritance patterns

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain metatables and inheritance patterns in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Metatables and inheritance patterns. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local amount31 = 31.5
print(string.format("%.2f", amount31 * 1.15))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 7.5: Composition and collaboration

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain composition and collaboration in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Composition and collaboration. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local tasks32 = {"read", "practice", "review"}
table.insert(tasks32, "reflect")
print(table.concat(tasks32, " -> "))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

# Unit 8: Files and Exceptions

## Overview

This unit follows the matching Python unit's objectives and familiar problem contexts. Lua's dynamic values, table model, and lightweight runtime are the language-specific learning targets.

## Lesson 8.1: Reading text files

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain reading text files in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Reading text files. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local squares33 = {}
for i = 1, 4 do squares33[i] = i * i + 33 end
print(table.concat(squares33, ", "))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 8.2: Writing and appending files

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain writing and appending files in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Writing and appending files. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local number34 = tonumber("34")
assert(number34 ~= nil)
print(number34 + 0.5)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 8.3: Errors and pcall

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain errors and pcall in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Errors and pcall. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local map35 = {first = "Avery", second = "Riley"}
for key, value in pairs(map35) do print(key, value) end
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 8.4: Closing files and resource lifetime

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain closing files and resource lifetime in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Closing files and resource lifetime. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local distance36 = math.sqrt(36 * 36 + 16)
print(string.format("%.2f", distance36))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 8.5: JSON modules and persistence

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain json modules and persistence in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
JSON modules and persistence. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local item37 = {name = "Avery", score = 77}
print(item37.name, item37.score)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

# Unit 9: Testing and Data Analysis

## Overview

This unit follows the matching Python unit's objectives and familiar problem contexts. Lua's dynamic values, table model, and lightweight runtime are the language-specific learning targets.

## Lesson 9.1: Testing functions with assertions

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain testing functions with assertions in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Testing functions with assertions. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local values38 = {38, 39, 40}
local total38 = 0
for _, value in ipairs(values38) do total38 = total38 + value end
print(total38 / #values38)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 9.2: Testing object state

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain testing object state in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Testing object state. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local text39 = "Lua lesson 39"
print(text39:upper())
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 9.3: Random values

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain random values in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Random values. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local function scale40(value) return value * 7 end
print(scale40(40))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 9.4: Text analysis

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text analysis in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text analysis. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local score41 = 81
if score41 >= 80 then print("meets target") else print("needs practice") end
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 9.5: CSV records

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain csv records in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
CSV records. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local record42 = {id = 42, active = true}
print(record42.id, record42.active)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

# Unit 10: Project-Based Learning

## Overview

This unit follows the matching Python unit's objectives and familiar problem contexts. Lua's dynamic values, table model, and lightweight runtime are the language-specific learning targets.

## Lesson 10.1: Requirements and top-down design

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and top-down design in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Requirements and top-down design. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local amount43 = 43.5
print(string.format("%.2f", amount43 * 1.15))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: rooms and movement in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text adventure: rooms and movement. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local tasks44 = {"read", "practice", "review"}
table.insert(tasks44, "reflect")
print(table.concat(tasks44, " -> "))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: inventory and puzzles in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text adventure: inventory and puzzles. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local squares45 = {}
for i = 1, 4 do squares45[i] = i * i + 45 end
print(table.concat(squares45, ", "))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 10.4: Command-line to-do manager

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain command-line to-do manager in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Command-line to-do manager. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local number46 = tonumber("46")
assert(number46 ~= nil)
print(number46 + 0.5)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 10.5: Accessible interaction and validation

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain accessible interaction and validation in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Accessible interaction and validation. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local map47 = {first = "Avery", second = "Riley"}
for key, value in pairs(map47) do print(key, value) end
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

# Unit 11: Capstone

## Overview

This unit follows the matching Python unit's objectives and familiar problem contexts. Lua's dynamic values, table model, and lightweight runtime are the language-specific learning targets.

## Lesson 11.1: Requirements and design

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and design in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Requirements and design. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local distance48 = math.sqrt(48 * 48 + 16)
print(string.format("%.2f", distance48))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 11.2: Data model and storage

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain data model and storage in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Data model and storage. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local item49 = {name = "Avery", score = 89}
print(item49.name, item49.score)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 11.3: Create, read, update, delete

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain create, read, update, delete in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Create, read, update, delete. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local values50 = {50, 51, 52}
local total50 = 0
for _, value in ipairs(values50) do total50 = total50 + value end
print(total50 / #values50)
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 11.4: Validation and tests

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain validation and tests in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Validation and tests. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local text51 = "Lua lesson 51"
print(text51:upper())
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Lesson 11.5: Documentation and presentation

### Reading References
- Official Lua 5.4 reference manual and programming-in-Lua material.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain documentation and presentation in Lua terminology.
- Predict the program's behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Documentation and presentation. Lua has a small core language and uses tables as its central compound data structure. Tables can act as arrays, maps, records, and objects. Indexing conventions, truthiness, nil values, and function return behavior differ from Python and must be learned explicitly.

### Worked Example
```lua
local function scale52(value) return value * 5 end
print(scale52(52))
```

**Trace:** identify local declarations, table operations, control flow, function calls, and output. Predict the result, run the example, and compare actual behavior.

### Common Mistakes
- Forgetting `local` and unintentionally creating or changing a global variable.
- Confusing `nil` with `false` or assuming empty tables are false.
- Mixing one-based sequence indexing with zero-based assumptions from other languages.
- Failing to close a file or check an error return.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a missing-value case and an invalid-input case.
4. Explain how the table or function behaves without relying on syntax highlighting.

### Accessibility Practice
Navigate source by line, word, and character; inspect punctuation and table delimiters; run from the terminal; and read output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can identify a common error and correct it.
- [ ] I can read source and output accessibly.

## Course-Wide Assessment and Portfolio

Submit runnable exercises, prediction and debugging notes, tests, a text adventure, a command-line to-do manager, and a personal-data manager. Assessment focuses on correct behavior, idiomatic Lua, clear table and function design, independent debugging, and code explanation.

## AI Policy
AI may be used only for personal conceptual explanations and reinforcement when permitted. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.