# Unit 8: Files and Exceptions

## Overview

This unit covers read/write text, resource lifetime, error handling, JSON serialization and persistence. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 8.1: Reading text files

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain reading text files using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Use `open(path) do io ... end` to close files even when operations fail. `eachline` supports line processing. Julia has TOML in its standard library but no general JSON parser; use JSON3.jl for JSON.

**Lesson focus:** Reading text files. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
mktemp() do path, io
    write(io,"Avery studies Julia.\n"); close(io)
    open(path,"r") do file
        foreach(println, eachline(file))
    end
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Relative paths are resolved from the process working directory.
- Use `open(path) do io` to guarantee resource cleanup.
- Catch expected exceptions specifically rather than hiding all failures.

### Activities
1. Create a temporary file fixture and read it line by line.
2. Test empty, missing, and malformed files.
3. Verify resources close after successful and exceptional paths.
4. Document the file format and parser limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain reading text files in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.2: Writing and appending files

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain writing and appending files using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Use `open(path) do io ... end` to close files even when operations fail. `eachline` supports line processing. Julia has TOML in its standard library but no general JSON parser; use JSON3.jl for JSON.

**Lesson focus:** Writing and appending files. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
mktemp() do path, io
    write(io,"First note\n"); close(io)
    open(path,"a") do file; write(file,"Second note\n"); end
    println(read(path,String))
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Relative paths are resolved from the process working directory.
- Use `open(path) do io` to guarantee resource cleanup.
- Catch expected exceptions specifically rather than hiding all failures.

### Activities
1. Create a temporary file fixture and read it line by line.
2. Test empty, missing, and malformed files.
3. Verify resources close after successful and exceptional paths.
4. Document the file format and parser limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain writing and appending files in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.3: Errors and exceptions

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain errors and exceptions using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Use `open(path) do io ... end` to close files even when operations fail. `eachline` supports line processing. Julia has TOML in its standard library but no general JSON parser; use JSON3.jl for JSON.

**Lesson focus:** Errors and exceptions. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
for raw in ["42","bad"]
    try
        println(parse(Int,raw))
    catch error
        error isa ArgumentError || rethrow()
        println("Invalid integer: $raw")
    end
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Relative paths are resolved from the process working directory.
- Use `open(path) do io` to guarantee resource cleanup.
- Catch expected exceptions specifically rather than hiding all failures.

### Activities
1. Create a temporary file fixture and read it line by line.
2. Test empty, missing, and malformed files.
3. Verify resources close after successful and exceptional paths.
4. Document the file format and parser limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain errors and exceptions in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.4: Resource cleanup

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain resource cleanup using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Use `open(path) do io ... end` to close files even when operations fail. `eachline` supports line processing. Julia has TOML in its standard library but no general JSON parser; use JSON3.jl for JSON.

**Lesson focus:** Resource cleanup. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
mktemp() do path, io
    write(io,"temporary"); close(io)
    open(path,"r") do file; println(read(file,String)); end
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Relative paths are resolved from the process working directory.
- Use `open(path) do io` to guarantee resource cleanup.
- Catch expected exceptions specifically rather than hiding all failures.

### Activities
1. Create a temporary file fixture and read it line by line.
2. Test empty, missing, and malformed files.
3. Verify resources close after successful and exceptional paths.
4. Document the file format and parser limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain resource cleanup in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.5: JSON persistence

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain json persistence using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Use `open(path) do io ... end` to close files even when operations fail. `eachline` supports line processing. Julia has TOML in its standard library but no general JSON parser; use JSON3.jl for JSON.

**Lesson focus:** JSON persistence. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
using TOML
record=Dict("id"=>1,"title"=>"Study Julia","done"=>false)
restored=TOML.parse(sprint(TOML.print,record))
println(restored["title"])
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Relative paths are resolved from the process working directory.
- Use `open(path) do io` to guarantee resource cleanup.
- Catch expected exceptions specifically rather than hiding all failures.

### Activities
1. Create a temporary file fixture and read it line by line.
2. Test empty, missing, and malformed files.
3. Verify resources close after successful and exceptional paths.
4. Document the file format and parser limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain json persistence in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
