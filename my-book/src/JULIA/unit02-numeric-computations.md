# Unit 2: Numeric Computations

## Overview

This unit covers development process, expressions, assignment, input/output, conversions, arithmetic, math library. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 2.1: Design and tracing

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain design and tracing using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia evaluates expressions and binds names with `=`. Numeric text must be converted before arithmetic; use `parse` for trusted input and `tryparse` when conversion may fail. `π`, `hypot`, exponentiation with `^`, and `round(...; digits=...)` support common calculations.

**Lesson focus:** Design and tracing. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
bill = 24.50; rate = 0.15
println("Tip: ", bill * rate, "; total: ", bill * (1 + rate))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Use `==` for equality; `=` binds a value.
- Validate uncertain text with `tryparse` before arithmetic.
- Avoid rounding intermediate values before the final result.

### Activities
1. Trace each expression and record intermediate values.
2. Calculate the canonical $24.50 bill with a 15% tip.
3. Test a boundary and invalid input; state the intended behavior.
4. Refactor the calculation into a function without changing its result.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain design and tracing in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.2: Expressions and assignment

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain expressions and assignment using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia evaluates expressions and binds names with `=`. Numeric text must be converted before arithmetic; use `parse` for trusted input and `tryparse` when conversion may fail. `π`, `hypot`, exponentiation with `^`, and `round(...; digits=...)` support common calculations.

**Lesson focus:** Expressions and assignment. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
subtotal = 18.00 + 6.50
println("Subtotal: ", subtotal, "; tax: ", subtotal * 0.08)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Use `==` for equality; `=` binds a value.
- Validate uncertain text with `tryparse` before arithmetic.
- Avoid rounding intermediate values before the final result.

### Activities
1. Trace each expression and record intermediate values.
2. Calculate the canonical $24.50 bill with a 15% tip.
3. Test a boundary and invalid input; state the intended behavior.
4. Refactor the calculation into a function without changing its result.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain expressions and assignment in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.3: Input and output

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain input and output using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia evaluates expressions and binds names with `=`. Numeric text must be converted before arithmetic; use `parse` for trusted input and `tryparse` when conversion may fail. `π`, `hypot`, exponentiation with `^`, and `round(...; digits=...)` support common calculations.

**Lesson focus:** Input and output. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
print("Name: "); name = readline()
println("Hello, ", name)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Use `==` for equality; `=` binds a value.
- Validate uncertain text with `tryparse` before arithmetic.
- Avoid rounding intermediate values before the final result.

### Activities
1. Trace each expression and record intermediate values.
2. Calculate the canonical $24.50 bill with a 15% tip.
3. Test a boundary and invalid input; state the intended behavior.
4. Refactor the calculation into a function without changing its result.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain input and output in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.4: Numeric conversions and mathematics

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain numeric conversions and mathematics using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia evaluates expressions and binds names with `=`. Numeric text must be converted before arithmetic; use `parse` for trusted input and `tryparse` when conversion may fail. `π`, `hypot`, exponentiation with `^`, and `round(...; digits=...)` support common calculations.

**Lesson focus:** Numeric conversions and mathematics. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
weight_kg = parse(Float64, "68.5")
println("Weight in grams: ", weight_kg * 1000)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Use `==` for equality; `=` binds a value.
- Validate uncertain text with `tryparse` before arithmetic.
- Avoid rounding intermediate values before the final result.

### Activities
1. Trace each expression and record intermediate values.
2. Calculate the canonical $24.50 bill with a 15% tip.
3. Test a boundary and invalid input; state the intended behavior.
4. Refactor the calculation into a function without changing its result.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain numeric conversions and mathematics in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.5: Using the Math Library

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain using the math library using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia evaluates expressions and binds names with `=`. Numeric text must be converted before arithmetic; use `parse` for trusted input and `tryparse` when conversion may fail. `π`, `hypot`, exponentiation with `^`, and `round(...; digits=...)` support common calculations.

**Lesson focus:** Using the Math Library. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
radius = 3.0
println("Area: ", π * radius^2, "; circumference: ", 2π * radius, "; distance: ", hypot(3,4))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Use `==` for equality; `=` binds a value.
- Validate uncertain text with `tryparse` before arithmetic.
- Avoid rounding intermediate values before the final result.

### Activities
1. Trace each expression and record intermediate values.
2. Calculate the canonical $24.50 bill with a 15% tip.
3. Test a boundary and invalid input; state the intended behavior.
4. Refactor the calculation into a function without changing its result.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain using the math library in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
