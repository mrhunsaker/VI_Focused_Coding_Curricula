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
print("Hello, World!")
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
print("Hello, World!")
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
print("Hello, World!")
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
local name = "Avery"; local age = 16; local height = 1.72
print(name .. " is " .. age .. " years old.")
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
local name = "Avery"; local age = 16; local height = 1.72
print(name .. " is " .. age .. " years old.")
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
local name = "Avery"; local age = 16; local height = 1.72
print(name .. " is " .. age .. " years old.")
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
local name = "Avery"; local age = 16; local height = 1.72
print(name .. " is " .. age .. " years old.")
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
local bill = 24.50; local tip = bill * 0.15
print(string.format("Tip: %.2f; total: %.2f", tip, bill + tip))
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
local bill = 24.50; local tip = bill * 0.15
print(string.format("Tip: %.2f; total: %.2f", tip, bill + tip))
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
local bill = 24.50; local tip = bill * 0.15
print(string.format("Tip: %.2f; total: %.2f", tip, bill + tip))
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
local bill = 24.50; local tip = bill * 0.15
print(string.format("Tip: %.2f; total: %.2f", tip, bill + tip))
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
local bill = 24.50; local tip = bill * 0.15
print(string.format("Tip: %.2f; total: %.2f", tip, bill + tip))
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
local score = 82
if score >= 90 then print("A") elseif score >= 80 then print("B") else print("Keep practicing") end
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
local score = 82
if score >= 90 then print("A") elseif score >= 80 then print("B") else print("Keep practicing") end
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
local score = 82
if score >= 90 then print("A") elseif score >= 80 then print("B") else print("Keep practicing") end
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
local score = 82
if score >= 90 then print("A") elseif score >= 80 then print("B") else print("Keep practicing") end
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
local score = 82
if score >= 90 then print("A") elseif score >= 80 then print("B") else print("Keep practicing") end
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
local scores = {82, 91, 76, 88}
for index, score in ipairs(scores) do print(index, score) end
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
local scores = {82, 91, 76, 88}
for index, score in ipairs(scores) do print(index, score) end
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
local scores = {82, 91, 76, 88}
for index, score in ipairs(scores) do print(index, score) end
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
local scores = {82, 91, 76, 88}
for index, score in ipairs(scores) do print(index, score) end
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
local scores = {82, 91, 76, 88}
for index, score in ipairs(scores) do print(index, score) end
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
local item = {name="Notebook", quantity=3}
print(item.name, item.quantity)
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
local item = {name="Notebook", quantity=3}
print(item.name, item.quantity)
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
local item = {name="Notebook", quantity=3}
print(item.name, item.quantity)
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
local item = {name="Notebook", quantity=3}
print(item.name, item.quantity)
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
local item = {name="Notebook", quantity=3}
print(item.name, item.quantity)
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
local function add(a, b) return a + b end
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
local function add(a, b) return a + b end
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
local function add(a, b) return a + b end
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
local function add(a, b) return a + b end
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
local function add(a, b) return a + b end
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
local file, err = io.open("notes.txt", "r")
if not file then error(err) end
local text = file:read("*a"); file:close(); print(text)
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
local file, err = io.open("notes.txt", "r")
if not file then error(err) end
local text = file:read("*a"); file:close(); print(text)
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
local file, err = io.open("notes.txt", "r")
if not file then error(err) end
local text = file:read("*a"); file:close(); print(text)
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
local file, err = io.open("notes.txt", "r")
if not file then error(err) end
local text = file:read("*a"); file:close(); print(text)
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
local file, err = io.open("notes.txt", "r")
if not file then error(err) end
local text = file:read("*a"); file:close(); print(text)
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
assert(2 + 3 == 5)
-- Put repeatable assertions in a test script.
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
assert(2 + 3 == 5)
-- Put repeatable assertions in a test script.
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
assert(2 + 3 == 5)
-- Put repeatable assertions in a test script.
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
assert(2 + 3 == 5)
-- Put repeatable assertions in a test script.
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
assert(2 + 3 == 5)
-- Put repeatable assertions in a test script.
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
local tasks = {{id=1,title="Read",done=false},{id=2,title="Practice",done=true}}
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
local tasks = {{id=1,title="Read",done=false},{id=2,title="Practice",done=true}}
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
local tasks = {{id=1,title="Read",done=false},{id=2,title="Practice",done=true}}
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
local tasks = {{id=1,title="Read",done=false},{id=2,title="Practice",done=true}}
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
local tasks = {{id=1,title="Read",done=false},{id=2,title="Practice",done=true}}
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
-- Capstone: menu-driven personal-data manager using tables, modules, and serialized data.
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
-- Capstone: menu-driven personal-data manager using tables, modules, and serialized data.
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
-- Capstone: menu-driven personal-data manager using tables, modules, and serialized data.
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
-- Capstone: menu-driven personal-data manager using tables, modules, and serialized data.
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
-- Capstone: menu-driven personal-data manager using tables, modules, and serialized data.
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