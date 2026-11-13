# Unit 3: Control Flow

## Overview

This unit covers Boolean expressions, conditionals, lists or arrays, iteration, string operations. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 3.1: Boolean expressions

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain boolean expressions using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia uses `if`/`elseif`/`else`/`end`, short-circuit Boolean operators, and one-based indexing. `for` iterates over values, `enumerate` supplies indices, and dotted operators broadcast. Strings are UTF-8, so character count and byte indexing differ.

**Lesson focus:** Boolean expressions. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
score = 82
println(score >= 80 && score <= 100)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Standard Julia arrays are one-based, not zero-based.
- Use `&&` and `||` for scalar conditions; dotted operators broadcast.
- Do not structurally mutate a collection while iterating over it.

### Activities
1. Test scores 82, 91, 76, and 88, including grade boundaries.
2. Test empty and single-element arrays.
3. Trace each loop iteration and collection state.
4. Modify a string and test indexing, normalization, and search.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain boolean expressions in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.2: Chained conditionals

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain chained conditionals using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia uses `if`/`elseif`/`else`/`end`, short-circuit Boolean operators, and one-based indexing. `for` iterates over values, `enumerate` supplies indices, and dotted operators broadcast. Strings are UTF-8, so character count and byte indexing differ.

**Lesson focus:** Chained conditionals. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
score = 82
grade = score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : score >= 60 ? "D" : "F"
println(grade)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Standard Julia arrays are one-based, not zero-based.
- Use `&&` and `||` for scalar conditions; dotted operators broadcast.
- Do not structurally mutate a collection while iterating over it.

### Activities
1. Test scores 82, 91, 76, and 88, including grade boundaries.
2. Test empty and single-element arrays.
3. Trace each loop iteration and collection state.
4. Modify a string and test indexing, normalization, and search.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain chained conditionals in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.3: Sequences and indexing

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain sequences and indexing using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia uses `if`/`elseif`/`else`/`end`, short-circuit Boolean operators, and one-based indexing. `for` iterates over values, `enumerate` supplies indices, and dotted operators broadcast. Strings are UTF-8, so character count and byte indexing differ.

**Lesson focus:** Sequences and indexing. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
scores = [82, 91, 76, 88]
println(scores[1], "; ", scores[4])
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Standard Julia arrays are one-based, not zero-based.
- Use `&&` and `||` for scalar conditions; dotted operators broadcast.
- Do not structurally mutate a collection while iterating over it.

### Activities
1. Test scores 82, 91, 76, and 88, including grade boundaries.
2. Test empty and single-element arrays.
3. Trace each loop iteration and collection state.
4. Modify a string and test indexing, normalization, and search.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain sequences and indexing in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.4: For loops and iteration

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain for loops and iteration using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia uses `if`/`elseif`/`else`/`end`, short-circuit Boolean operators, and one-based indexing. `for` iterates over values, `enumerate` supplies indices, and dotted operators broadcast. Strings are UTF-8, so character count and byte indexing differ.

**Lesson focus:** For loops and iteration. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
scores = [82, 91, 76, 88]
for (i, score) in enumerate(scores)
    println("Score $i: $score")
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Standard Julia arrays are one-based, not zero-based.
- Use `&&` and `||` for scalar conditions; dotted operators broadcast.
- Do not structurally mutate a collection while iterating over it.

### Activities
1. Test scores 82, 91, 76, and 88, including grade boundaries.
2. Test empty and single-element arrays.
3. Trace each loop iteration and collection state.
4. Modify a string and test indexing, normalization, and search.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain for loops and iteration in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.5: String operations

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain string operations using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia uses `if`/`elseif`/`else`/`end`, short-circuit Boolean operators, and one-based indexing. `for` iterates over values, `enumerate` supplies indices, and dotted operators broadcast. Strings are UTF-8, so character count and byte indexing differ.

**Lesson focus:** String operations. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
text = "Avery studies Julia programming."
println(lowercase(strip(text)))
println(occursin("Julia", text))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Standard Julia arrays are one-based, not zero-based.
- Use `&&` and `||` for scalar conditions; dotted operators broadcast.
- Do not structurally mutate a collection while iterating over it.

### Activities
1. Test scores 82, 91, 76, and 88, including grade boundaries.
2. Test empty and single-element arrays.
3. Trace each loop iteration and collection state.
4. Modify a string and test indexing, normalization, and search.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain string operations in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
