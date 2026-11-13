# Unit 5: Input and Iteration

## Overview

This unit covers input validation, sentinel loops, while loops, flags, break/continue, infinite-loop prevention. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 5.1: Input and validation

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain input and validation using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Interactive input arrives as text through `readline`; validate and convert it before use. A `while` loop repeats while its condition is true, `break` exits the nearest loop, and `continue` skips to the next iteration.

**Lesson focus:** Input and validation. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
raw = "82"; score = tryparse(Int, raw)
println(score === nothing ? "Invalid score" : "Accepted: $score")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Convert and validate `readline()` input before numeric operations.
- Every `while` loop needs progress or an explicit exit.
- Place `break` and `continue` at the intended loop nesting level.

### Activities
1. Test valid, invalid, and sentinel command input.
2. Trace loop state and condition on each iteration.
3. Stop a search at the first matching score.
4. Prove termination for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain input and validation in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.2: While loops

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain while loops using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Interactive input arrives as text through `readline`; validate and convert it before use. A `while` loop repeats while its condition is true, `break` exits the nearest loop, and `continue` skips to the next iteration.

**Lesson focus:** While loops. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
function run_commands()
    commands = ["list", "help", "quit"]
    index = 1
    while index <= length(commands)
        println(commands[index])
        commands[index] == "quit" && break
        index += 1
    end
end
run_commands()
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Convert and validate `readline()` input before numeric operations.
- Every `while` loop needs progress or an explicit exit.
- Place `break` and `continue` at the intended loop nesting level.

### Activities
1. Test valid, invalid, and sentinel command input.
2. Trace loop state and condition on each iteration.
3. Stop a search at the first matching score.
4. Prove termination for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain while loops in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.3: Flags and break

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain flags and break using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Interactive input arrives as text through `readline`; validate and convert it before use. A `while` loop repeats while its condition is true, `break` exits the nearest loop, and `continue` skips to the next iteration.

**Lesson focus:** Flags and break. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
scores = [82, 91, 76, 88]
for (i, score) in enumerate(scores)
    if score == 91
        println("Found at $i"); break
    end
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Convert and validate `readline()` input before numeric operations.
- Every `while` loop needs progress or an explicit exit.
- Place `break` and `continue` at the intended loop nesting level.

### Activities
1. Test valid, invalid, and sentinel command input.
2. Trace loop state and condition on each iteration.
3. Stop a search at the first matching score.
4. Prove termination for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain flags and break in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.4: Continue and filtering

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain continue and filtering using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Interactive input arrives as text through `readline`; validate and convert it before use. A `while` loop repeats while its condition is true, `break` exits the nearest loop, and `continue` skips to the next iteration.

**Lesson focus:** Continue and filtering. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
values = [82, -1, 91]
for value in values
    value < 0 && continue
    println(value)
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Convert and validate `readline()` input before numeric operations.
- Every `while` loop needs progress or an explicit exit.
- Place `break` and `continue` at the intended loop nesting level.

### Activities
1. Test valid, invalid, and sentinel command input.
2. Trace loop state and condition on each iteration.
3. Stop a search at the first matching score.
4. Prove termination for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain continue and filtering in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.5: Infinite-loop prevention

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain infinite-loop prevention using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Interactive input arrives as text through `readline`; validate and convert it before use. A `while` loop repeats while its condition is true, `break` exits the nearest loop, and `continue` skips to the next iteration.

**Lesson focus:** Infinite-loop prevention. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
for attempt in 1:3
    println("Attempt $attempt")
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Convert and validate `readline()` input before numeric operations.
- Every `while` loop needs progress or an explicit exit.
- Place `break` and `continue` at the intended loop nesting level.

### Activities
1. Test valid, invalid, and sentinel command input.
2. Trace loop state and condition on each iteration.
3. Stop a search at the first matching score.
4. Prove termination for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain infinite-loop prevention in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
