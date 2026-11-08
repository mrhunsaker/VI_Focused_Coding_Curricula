# Unit 9: Testing and Data Analysis

## Overview

This unit covers unit tests, testing stateful types, randomness, text analysis, CSV processing. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 9.1: Testing functions

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain testing functions using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The `Test` standard library provides assertions, and `Random` supports seeded sequences. Text analysis uses `split`, regular expressions, and dictionaries. Use CSV.jl for quoted delimiters, escaped quotes, and embedded newlines.

**Lesson focus:** Testing functions. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
using Test
@test 2 + 3 == 5
println("Arithmetic tests passed")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Seed random generators when tests require reproducibility.
- Use approximate comparison for floating-point results where appropriate.
- A `split`-based CSV demonstration is not a full quoted-field parser.

### Activities
1. Test normal, boundary, and invalid cases.
2. Seed random operations and verify reproducibility.
3. Analyze the canonical text sample and verify word counts.
4. Process the CSV columns and document unsupported quoting cases.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain testing functions in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.2: Testing stateful objects

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain testing stateful objects using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The `Test` standard library provides assertions, and `Random` supports seeded sequences. Text analysis uses `split`, regular expressions, and dictionaries. Use CSV.jl for quoted delimiters, escaped quotes, and embedded newlines.

**Lesson focus:** Testing stateful objects. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
using Test
mutable struct TaskState; title::String; done::Bool; end
t=TaskState("Study",false); @test !t.done
t.done=true; @test t.done
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Seed random generators when tests require reproducibility.
- Use approximate comparison for floating-point results where appropriate.
- A `split`-based CSV demonstration is not a full quoted-field parser.

### Activities
1. Test normal, boundary, and invalid cases.
2. Seed random operations and verify reproducibility.
3. Analyze the canonical text sample and verify word counts.
4. Process the CSV columns and document unsupported quoting cases.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain testing stateful objects in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.3: Random values

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain random values using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The `Test` standard library provides assertions, and `Random` supports seeded sequences. Text analysis uses `split`, regular expressions, and dictionaries. Use CSV.jl for quoted delimiters, escaped quotes, and embedded newlines.

**Lesson focus:** Random values. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
using Random
Random.seed!(2026)
println(rand(1:10)); println(rand())
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Seed random generators when tests require reproducibility.
- Use approximate comparison for floating-point results where appropriate.
- A `split`-based CSV demonstration is not a full quoted-field parser.

### Activities
1. Test normal, boundary, and invalid cases.
2. Seed random operations and verify reproducibility.
3. Analyze the canonical text sample and verify word counts.
4. Process the CSV columns and document unsupported quoting cases.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain random values in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.4: Text analysis

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain text analysis using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The `Test` standard library provides assertions, and `Random` supports seeded sequences. Text analysis uses `split`, regular expressions, and dictionaries. Use CSV.jl for quoted delimiters, escaped quotes, and embedded newlines.

**Lesson focus:** Text analysis. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
sample="A student studies programming. Programming builds skills."
words=split(lowercase(sample),r"[^a-z]+")
filter!(x -> !isempty(x), words)
println(length(words))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Seed random generators when tests require reproducibility.
- Use approximate comparison for floating-point results where appropriate.
- A `split`-based CSV demonstration is not a full quoted-field parser.

### Activities
1. Test normal, boundary, and invalid cases.
2. Seed random operations and verify reproducibility.
3. Analyze the canonical text sample and verify word counts.
4. Process the CSV columns and document unsupported quoting cases.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain text analysis in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.5: CSV records

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain csv records using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The `Test` standard library provides assertions, and `Random` supports seeded sequences. Text analysis uses `split`, regular expressions, and dictionaries. Use CSV.jl for quoted delimiters, escaped quotes, and embedded newlines.

**Lesson focus:** CSV records. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
csv="id,first_name,score\n1,Avery,91\n2,Jordan,84"
for row in split.(split(chomp(csv),'\n')[2:end], ',')
    println(row[2], ": ", parse(Int,row[3]))
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Seed random generators when tests require reproducibility.
- Use approximate comparison for floating-point results where appropriate.
- A `split`-based CSV demonstration is not a full quoted-field parser.

### Activities
1. Test normal, boundary, and invalid cases.
2. Seed random operations and verify reproducibility.
3. Analyze the canonical text sample and verify word counts.
4. Process the CSV columns and document unsupported quoting cases.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain csv records in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
