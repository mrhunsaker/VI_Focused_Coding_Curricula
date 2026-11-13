# Unit 4: Data Structures

## Overview

This unit covers sequence mutation, sorting, immutable records, maps, dictionaries, traversal. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 4.1: Mutable sequences

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain mutable sequences using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia provides mutable arrays, immutable tuples and named tuples, and dictionaries for key-value data. Mutating functions conventionally end in `!`. Sort keys or entries when deterministic report order matters.

**Lesson focus:** Mutable sequences. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
scores = [82, 91, 76, 88]
push!(scores, 95); insert!(scores, 2, 85)
println(scores)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Tuples and named tuples are immutable; arrays and dictionaries are mutable.
- Use `get` or `haskey` for possibly absent dictionary keys.
- A shallow copy does not duplicate nested mutable values.

### Activities
1. Represent the canonical inventory using a dictionary.
2. Add, update, and remove an entry, checking each state.
3. Compare tuple, named tuple, vector, and dictionary semantics.
4. Test a missing key and implement an explicit fallback.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain mutable sequences in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.2: Sorting and organizing data

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain sorting and organizing data using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia provides mutable arrays, immutable tuples and named tuples, and dictionaries for key-value data. Mutating functions conventionally end in `!`. Sort keys or entries when deterministic report order matters.

**Lesson focus:** Sorting and organizing data. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
scores = [82, 91, 76, 88]
println(sort(scores)); println(sort(scores, rev=true))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Tuples and named tuples are immutable; arrays and dictionaries are mutable.
- Use `get` or `haskey` for possibly absent dictionary keys.
- A shallow copy does not duplicate nested mutable values.

### Activities
1. Represent the canonical inventory using a dictionary.
2. Add, update, and remove an entry, checking each state.
3. Compare tuple, named tuple, vector, and dictionary semantics.
4. Test a missing key and implement an explicit fallback.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain sorting and organizing data in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.3: Immutable records

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain immutable records using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia provides mutable arrays, immutable tuples and named tuples, and dictionaries for key-value data. Mutating functions conventionally end in `!`. Sort keys or entries when deterministic report order matters.

**Lesson focus:** Immutable records. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
point = (x=3, y=4)
println(hypot(point.x, point.y))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Tuples and named tuples are immutable; arrays and dictionaries are mutable.
- Use `get` or `haskey` for possibly absent dictionary keys.
- A shallow copy does not duplicate nested mutable values.

### Activities
1. Represent the canonical inventory using a dictionary.
2. Add, update, and remove an entry, checking each state.
3. Compare tuple, named tuple, vector, and dictionary semantics.
4. Test a missing key and implement an explicit fallback.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain immutable records in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.4: Maps and key-value data

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain maps and key-value data using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia provides mutable arrays, immutable tuples and named tuples, and dictionaries for key-value data. Mutating functions conventionally end in `!`. Sort keys or entries when deterministic report order matters.

**Lesson focus:** Maps and key-value data. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
item = Dict("name" => "Notebook", "quantity" => 3, "price" => 2.50)
println(item["name"], ": ", item["quantity"])
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Tuples and named tuples are immutable; arrays and dictionaries are mutable.
- Use `get` or `haskey` for possibly absent dictionary keys.
- A shallow copy does not duplicate nested mutable values.

### Activities
1. Represent the canonical inventory using a dictionary.
2. Add, update, and remove an entry, checking each state.
3. Compare tuple, named tuple, vector, and dictionary semantics.
4. Test a missing key and implement an explicit fallback.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain maps and key-value data in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.5: Collection traversal

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain collection traversal using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia provides mutable arrays, immutable tuples and named tuples, and dictionaries for key-value data. Mutating functions conventionally end in `!`. Sort keys or entries when deterministic report order matters.

**Lesson focus:** Collection traversal. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
stock = Dict("Notebook"=>3, "Pencil"=>10, "Folder"=>4)
for key in sort(collect(keys(stock)))
    println(key, ": ", stock[key])
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Tuples and named tuples are immutable; arrays and dictionaries are mutable.
- Use `get` or `haskey` for possibly absent dictionary keys.
- A shallow copy does not duplicate nested mutable values.

### Activities
1. Represent the canonical inventory using a dictionary.
2. Add, update, and remove an entry, checking each state.
3. Compare tuple, named tuple, vector, and dictionary semantics.
4. Test a missing key and implement an explicit fallback.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain collection traversal in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
