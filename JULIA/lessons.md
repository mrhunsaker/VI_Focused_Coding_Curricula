# Julia: Complete Curriculum — Units 0–11

## Course Overview

Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research.

This course intentionally parallels the original Python curriculum. It reuses problem contexts—greetings, profiles, a calculator, grade decisions, score collections, inventory, functions, text files, tests, text analysis, CSV, a to-do list, and a personal-data manager—so the principal new learning target is the Julia language. The syntax and implementation remain idiomatic, not a mechanical translation.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install and verify the compiler or interpreter, create a project, and test keyboard and screen-reader access.

### Lesson 0.1: Install and Verify Julia

Install Julia from julialang.org. Verify `julia --version`; run a script with `julia main.jl` or experiment in the REPL.

### Lesson 0.2: Workspace and First Run
Create a course folder, save a source file named `main.jl`, run it from the terminal, and read standard output and errors. Distinguish source code, compiler/interpreter, and executable/runtime.

### Lesson 0.3: Editor and Accessibility Workflow
Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md). Test editor navigation, punctuation announcement, indentation, terminal focus, diagnostics, and project navigation. Install only the language tooling needed for this course.

### Skills Checklist
- [ ] I can verify the Julia toolchain.
- [ ] I can create and run a source file from the terminal.
- [ ] I can navigate the editor and read output accessibly.

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

Use the terminal from the project root and understand the current working directory. Keep each project in its own folder and distinguish source files, build output, and dependency metadata. Use Julia's project environment for reproducibility. Create or activate a project environment with `julia --project`, then use `import Pkg; Pkg.activate("."); Pkg.add("PackageName")`. Explain Project.toml and Manifest.toml and run scripts with `julia --project main.jl`.

### Skills Checklist
- [ ] I can identify the project root and run commands from it.
- [ ] I can explain where project dependencies are recorded, if applicable.
- [ ] I can run the program or test command from the terminal and read its output.

# Unit 1: Foundations of Computing

## Overview

This unit covers computer science, hardware/software, algorithms, first program, variables, primitive types. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 1.1: Computer science and problem solving

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Computer science and problem solving. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
println("Hello, World!")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 1.2: Your first program

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Your first program. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
println("Hello, World!")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 1.3: Variables and data types

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Variables and data types. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
println("Hello, World!")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 2: Numeric Computations

## Overview

This unit covers development process, expressions, assignment, input/output, conversions, arithmetic, math library. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 2.1: Design and tracing

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Design and tracing. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
bill = 24.50; tip = bill * 0.15
println("Tip: $(round(tip, digits=2)); total: $(round(bill+tip, digits=2))")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 2.2: Expressions and assignment

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Expressions and assignment. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
bill = 24.50; tip = bill * 0.15
println("Tip: $(round(tip, digits=2)); total: $(round(bill+tip, digits=2))")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 2.3: Input and output

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Input and output. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
bill = 24.50; tip = bill * 0.15
println("Tip: $(round(tip, digits=2)); total: $(round(bill+tip, digits=2))")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 2.4: Numeric conversions and mathematics

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Numeric conversions and mathematics. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
bill = 24.50; tip = bill * 0.15
println("Tip: $(round(tip, digits=2)); total: $(round(bill+tip, digits=2))")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 3: Control Flow

## Overview

This unit covers Boolean expressions, conditionals, lists or arrays, iteration, string operations. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 3.1: Boolean expressions

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Boolean expressions. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
score = 82
if score >= 90 println("A") elseif score >= 80 println("B") else println("Keep practicing") end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.2: Chained conditionals

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Chained conditionals. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
score = 82
if score >= 90 println("A") elseif score >= 80 println("B") else println("Keep practicing") end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.3: Sequences and indexing

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Sequences and indexing. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
score = 82
if score >= 90 println("A") elseif score >= 80 println("B") else println("Keep practicing") end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.4: For loops and iteration

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
For loops and iteration. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
score = 82
if score >= 90 println("A") elseif score >= 80 println("B") else println("Keep practicing") end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.5: String operations

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
String operations. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
score = 82
if score >= 90 println("A") elseif score >= 80 println("B") else println("Keep practicing") end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 4: Data Structures

## Overview

This unit covers sequence mutation, sorting, immutable records, maps, dictionaries, traversal. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 4.1: Mutable sequences

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Mutable sequences. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
item = (name="Notebook", quantity=3)
println("$(item.name): $(item.quantity)")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.2: Sorting and organizing data

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Sorting and organizing data. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
item = (name="Notebook", quantity=3)
println("$(item.name): $(item.quantity)")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.3: Immutable records

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Immutable records. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
item = (name="Notebook", quantity=3)
println("$(item.name): $(item.quantity)")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.4: Maps and key-value data

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Maps and key-value data. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
item = (name="Notebook", quantity=3)
println("$(item.name): $(item.quantity)")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.5: Collection traversal

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Collection traversal. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
item = (name="Notebook", quantity=3)
println("$(item.name): $(item.quantity)")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 5: Input and Iteration

## Overview

This unit covers input validation, sentinel loops, while loops, flags, break/continue, infinite-loop prevention. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 5.1: Input and validation

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Input and validation. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
score = 82
if score >= 90 println("A") elseif score >= 80 println("B") else println("Keep practicing") end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.2: While loops

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
While loops. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
score = 82
if score >= 90 println("A") elseif score >= 80 println("B") else println("Keep practicing") end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.3: Flags and break

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Flags and break. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
score = 82
if score >= 90 println("A") elseif score >= 80 println("B") else println("Keep practicing") end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.4: Continue and filtering

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Continue and filtering. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
score = 82
if score >= 90 println("A") elseif score >= 80 println("B") else println("Keep practicing") end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.5: Infinite-loop prevention

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Infinite-loop prevention. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
score = 82
if score >= 90 println("A") elseif score >= 80 println("B") else println("Keep practicing") end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 6: Functions

## Overview

This unit covers definitions, parameters, arguments, return values, scope, collection parameters, variadic functions. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 6.1: Defining functions

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Defining functions. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
add(a, b) = a + b
# use: total = add(4, 5)
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.2: Parameters and arguments

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Parameters and arguments. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
add(a, b) = a + b
# use: total = add(4, 5)
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.3: Return values

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Return values. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
add(a, b) = a + b
# use: total = add(4, 5)
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.4: Functions over collections

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Functions over collections. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
add(a, b) = a + b
# use: total = add(4, 5)
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.5: Scope and variadic arguments

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Scope and variadic arguments. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
add(a, b) = a + b
# use: total = add(4, 5)
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 7: Object-Oriented Programming

## Overview

This unit covers types/classes, instances, fields, methods, inheritance or interfaces, composition. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 7.1: Types and object models

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Types and object models. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
item = (name="Notebook", quantity=3)
println("$(item.name): $(item.quantity)")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.2: Creating instances

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Creating instances. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
item = (name="Notebook", quantity=3)
println("$(item.name): $(item.quantity)")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.3: Fields and methods

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Fields and methods. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
item = (name="Notebook", quantity=3)
println("$(item.name): $(item.quantity)")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.4: Inheritance and interfaces

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Inheritance and interfaces. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
item = (name="Notebook", quantity=3)
println("$(item.name): $(item.quantity)")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.5: Composition

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Composition. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
item = (name="Notebook", quantity=3)
println("$(item.name): $(item.quantity)")
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 8: Files and Exceptions

## Overview

This unit covers read/write text, resource lifetime, error handling, JSON serialization and persistence. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 8.1: Reading text files

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Reading text files. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
open("notes.txt", "r") do file
    for line in eachline(file) println(line) end
end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.2: Writing and appending files

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Writing and appending files. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
open("notes.txt", "r") do file
    for line in eachline(file) println(line) end
end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.3: Errors and exceptions

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Errors and exceptions. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
open("notes.txt", "r") do file
    for line in eachline(file) println(line) end
end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.4: Resource cleanup

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Resource cleanup. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
open("notes.txt", "r") do file
    for line in eachline(file) println(line) end
end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.5: JSON persistence

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
JSON persistence. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
open("notes.txt", "r") do file
    for line in eachline(file) println(line) end
end
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 9: Testing and Data Analysis

## Overview

This unit covers unit tests, testing stateful types, randomness, text analysis, CSV processing. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 9.1: Testing functions

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Testing functions. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
using Test
@test 2 + 3 == 5
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.2: Testing stateful objects

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Testing stateful objects. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
using Test
@test 2 + 3 == 5
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.3: Random values

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Random values. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
using Test
@test 2 + 3 == 5
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.4: Text analysis

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text analysis. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
using Test
@test 2 + 3 == 5
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.5: CSV records

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
CSV records. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
using Test
@test 2 + 3 == 5
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 10: Project-Based Learning

## Overview

This unit covers requirements, top-down design, text adventure, command-line to-do manager, accessible validation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 10.1: Requirements and design

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Requirements and design. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
# Build a text-first personal-data manager; optionally analyze records with arrays and DataFrames.
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text adventure: rooms and movement. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
# Build a text-first personal-data manager; optionally analyze records with arrays and DataFrames.
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text adventure: inventory and puzzles. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
# Build a text-first personal-data manager; optionally analyze records with arrays and DataFrames.
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.4: Command-line to-do manager

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Command-line to-do manager. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
# Build a text-first personal-data manager; optionally analyze records with arrays and DataFrames.
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.5: Accessible UX and validation

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Accessible UX and validation. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
# Build a text-first personal-data manager; optionally analyze records with arrays and DataFrames.
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 11: Capstone

## Overview

This unit covers accessible personal-data manager, model, persistence, CRUD, tests, documentation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 11.1: Capstone requirements

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Capstone requirements. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
# Build a text-first personal-data manager; optionally analyze records with arrays and DataFrames.
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.2: Data model and storage

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Data model and storage. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
# Build a text-first personal-data manager; optionally analyze records with arrays and DataFrames.
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.3: Create/read/update/delete

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Create/read/update/delete. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
# Build a text-first personal-data manager; optionally analyze records with arrays and DataFrames.
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.4: Validation and testing

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Validation and testing. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
# Build a text-first personal-data manager; optionally analyze records with arrays and DataFrames.
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.5: Documentation and presentation

### Reading References
- Official Julia language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using Julia terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Documentation and presentation. Julia targets numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. The Python course provides the sequence and problem contexts; this lesson teaches the idiomatic Julia syntax and semantics. Pay particular attention to static or dynamic typing, mutability, indexing, parameter passing, errors, and resource lifetime where they differ from Python.

### Worked Example
```jl
# Build a text-first personal-data manager; optionally analyze records with arrays and DataFrames.
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Copying Python syntax or assumptions instead of using idiomatic Julia constructs.
- Confusing assignment with equality or declaration with initialization.
- Assuming strings, arrays, slices, tables, maps, or records have the same indexing and mutation rules as Python.
- Ignoring compiler/interpreter diagnostics, return values, or resource errors.

### Activities
1. Reproduce and run the example in a new file.
2. Change one value and predict the result before running.
3. Add a boundary case and an invalid-input case; describe the outcome.
4. Explain each statement and its effect without relying on syntax coloring.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in Julia terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Course-Wide Assessment and Portfolio

Submit runnable exercises, prediction notes, debugging notes, tests, and the text adventure and personal-data manager projects. Assessment focuses on correctness, idiomatic Julia, code explanation, independent debugging, and accessible interaction—not speed or visual editor use.

## AI and Academic Integrity

AI may be used only for personal conceptual explanations and reinforcement when the instructor permits. Do not use AI to write, complete, autocomplete, repair, or generate course code or assessment solutions. Students must explain every submitted statement independently.

## Further Learning

Use the official Julia language specification, standard-library documentation, and the linked setup resources. Verify APIs against the documentation for the installed toolchain.