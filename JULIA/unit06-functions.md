# Unit 6: Functions

## Overview

This unit covers definitions, parameters, arguments, return values, scope, collection parameters, variadic functions. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 6.1: Defining functions

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain defining functions using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Functions are first-class values. Julia supports positional and keyword arguments, optional defaults, multiple dispatch, and variadic positional arguments with `...`. The final expression is returned implicitly.

**Lesson focus:** Defining functions. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
tip(bill, rate=0.15) = bill * rate
println(tip(24.50))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Printing a value is not the same as returning it.
- Distinguish positional arguments from keyword arguments after the semicolon.
- Use `...` deliberately when collecting variadic arguments.

### Activities
1. Call a function and inspect its return value independently of printing.
2. Add boundary and invalid-argument tests.
3. Use keyword or variadic arguments where appropriate.
4. Compose two functions without duplicating calculations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain defining functions in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.2: Parameters and arguments

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain parameters and arguments using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Functions are first-class values. Julia supports positional and keyword arguments, optional defaults, multiple dispatch, and variadic positional arguments with `...`. The final expression is returned implicitly.

**Lesson focus:** Parameters and arguments. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
function invoice_total(bill; rate=0.15, tax=0.0)
    bill + bill * rate + tax
end
println(invoice_total(24.50; tax=1.20))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Printing a value is not the same as returning it.
- Distinguish positional arguments from keyword arguments after the semicolon.
- Use `...` deliberately when collecting variadic arguments.

### Activities
1. Call a function and inspect its return value independently of printing.
2. Add boundary and invalid-argument tests.
3. Use keyword or variadic arguments where appropriate.
4. Compose two functions without duplicating calculations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain parameters and arguments in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.3: Return values

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain return values using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Functions are first-class values. Julia supports positional and keyword arguments, optional defaults, multiple dispatch, and variadic positional arguments with `...`. The final expression is returned implicitly.

**Lesson focus:** Return values. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
function grade(score)
    0 <= score <= 100 || throw(ArgumentError("score out of range"))
    return score >= 90 ? "A" : score >= 80 ? "B" : "C or below"
end
println(grade(82))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Printing a value is not the same as returning it.
- Distinguish positional arguments from keyword arguments after the semicolon.
- Use `...` deliberately when collecting variadic arguments.

### Activities
1. Call a function and inspect its return value independently of printing.
2. Add boundary and invalid-argument tests.
3. Use keyword or variadic arguments where appropriate.
4. Compose two functions without duplicating calculations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain return values in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.4: Functions over collections

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain functions over collections using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Functions are first-class values. Julia supports positional and keyword arguments, optional defaults, multiple dispatch, and variadic positional arguments with `...`. The final expression is returned implicitly.

**Lesson focus:** Functions over collections. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
average(values::AbstractVector{<:Real}) = sum(values) / length(values)
println(average([82,91,76,88]))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Printing a value is not the same as returning it.
- Distinguish positional arguments from keyword arguments after the semicolon.
- Use `...` deliberately when collecting variadic arguments.

### Activities
1. Call a function and inspect its return value independently of printing.
2. Add boundary and invalid-argument tests.
3. Use keyword or variadic arguments where appropriate.
4. Compose two functions without duplicating calculations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain functions over collections in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.5: Scope and variadic arguments

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain scope and variadic arguments using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Functions are first-class values. Julia supports positional and keyword arguments, optional defaults, multiple dispatch, and variadic positional arguments with `...`. The final expression is returned implicitly.

**Lesson focus:** Scope and variadic arguments. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
function report(label, scores...)
    println(label, ": ", join(scores, ", "))
end
report("Quiz", 82,91,76,88)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Printing a value is not the same as returning it.
- Distinguish positional arguments from keyword arguments after the semicolon.
- Use `...` deliberately when collecting variadic arguments.

### Activities
1. Call a function and inspect its return value independently of printing.
2. Add boundary and invalid-argument tests.
3. Use keyword or variadic arguments where appropriate.
4. Compose two functions without duplicating calculations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain scope and variadic arguments in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
