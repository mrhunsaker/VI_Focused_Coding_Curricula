# Unit 1: Foundations of Computing

## Overview

This unit covers computer science, hardware/software, algorithms, first program, variables, primitive types. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 1.1: Computer science and problem solving

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain computer science and problem solving using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia is a high-level, dynamically typed, JIT-compiled language. Values have concrete types and variables are bindings. Define inputs and outputs, choose a finite algorithm, and test ordinary and boundary cases.

**Lesson focus:** Computer science and problem solving. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
println("Computer science turns a problem into a finite sequence of precise steps.")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Inspect values with `typeof` rather than assuming a static declaration.
- Do not confuse a variable binding with a `const` binding.
- Read `UndefVarError` and `MethodError` diagnostics before changing code.

### Activities
1. Run the example and explain each expression in execution order.
2. Change a canonical profile value and predict the output.
3. Inspect each value with `typeof` and explain the result.
4. Introduce and correct an undefined-name error.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain computer science and problem solving in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 1.2: Your first program

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain your first program using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia is a high-level, dynamically typed, JIT-compiled language. Values have concrete types and variables are bindings. Define inputs and outputs, choose a finite algorithm, and test ordinary and boundary cases.

**Lesson focus:** Your first program. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
println("Hello, World!")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Inspect values with `typeof` rather than assuming a static declaration.
- Do not confuse a variable binding with a `const` binding.
- Read `UndefVarError` and `MethodError` diagnostics before changing code.

### Activities
1. Run the example and explain each expression in execution order.
2. Change a canonical profile value and predict the output.
3. Inspect each value with `typeof` and explain the result.
4. Introduce and correct an undefined-name error.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain your first program in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 1.3: Variables and data types

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain variables and data types using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia is a high-level, dynamically typed, JIT-compiled language. Values have concrete types and variables are bindings. Define inputs and outputs, choose a finite algorithm, and test ordinary and boundary cases.

**Lesson focus:** Variables and data types. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
profile = (name="Avery", age=16, height_m=1.72, favorite_subject="Computer Science")
println(profile)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Inspect values with `typeof` rather than assuming a static declaration.
- Do not confuse a variable binding with a `const` binding.
- Read `UndefVarError` and `MethodError` diagnostics before changing code.

### Activities
1. Run the example and explain each expression in execution order.
2. Change a canonical profile value and predict the output.
3. Inspect each value with `typeof` and explain the result.
4. Introduce and correct an undefined-name error.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain variables and data types in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
