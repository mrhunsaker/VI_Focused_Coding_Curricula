# Unit 11: Capstone

## Overview

This unit covers accessible personal-data manager, model, persistence, CRUD, tests, documentation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 11.1: Capstone requirements

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain capstone requirements using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The capstone is an accessible personal-data manager with list/add/search/update/delete/complete operations. Separate data model, validation, persistence, and interaction; test save/reload.

**Lesson focus:** Capstone requirements. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
println("Capstone: accessible personal data manager")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Pass application state explicitly rather than hiding it in mutable globals.
- Validate updates and preserve stable record identifiers.
- Do not claim persistence or accessibility without save/reload and keyboard tests.

### Activities
1. Specify record fields and validation rules before storage.
2. Test list, add, search, update, delete, and completion.
3. Test duplicate, missing, empty, and invalid values.
4. Create a save/reload test and document known limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain capstone requirements in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.2: Data model and storage

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain data model and storage using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The capstone is an accessible personal-data manager with list/add/search/update/delete/complete operations. Separate data model, validation, persistence, and interaction; test save/reload.

**Lesson focus:** Data model and storage. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
<<<<<<< HEAD
struct Record; id::Int; title::String; description::String; category::String; created_at::String; updated_at::String; end
println(Record(1,"Study Julia","Review arrays","learning","2026-11-01","2026-11-01"))
=======
struct Record; id::Int; title::String; description::String; category::String; end
println(Record(1,"Study","Read arrays","learning"))
>>>>>>> 2067a20 (curriculum clearning and updates)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Pass application state explicitly rather than hiding it in mutable globals.
- Validate updates and preserve stable record identifiers.
- Do not claim persistence or accessibility without save/reload and keyboard tests.

### Activities
1. Specify record fields and validation rules before storage.
2. Test list, add, search, update, delete, and completion.
3. Test duplicate, missing, empty, and invalid values.
4. Create a save/reload test and document known limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain data model and storage in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.3: Create/read/update/delete

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain create/read/update/delete using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The capstone is an accessible personal-data manager with list/add/search/update/delete/complete operations. Separate data model, validation, persistence, and interaction; test save/reload.

**Lesson focus:** Create/read/update/delete. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
records=[(id=1,title="Study",done=false),(id=2,title="Practice",done=true)]
println(filter(r->!r.done,records))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Pass application state explicitly rather than hiding it in mutable globals.
- Validate updates and preserve stable record identifiers.
- Do not claim persistence or accessibility without save/reload and keyboard tests.

### Activities
1. Specify record fields and validation rules before storage.
2. Test list, add, search, update, delete, and completion.
3. Test duplicate, missing, empty, and invalid values.
4. Create a save/reload test and document known limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain create/read/update/delete in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.4: Validation and testing

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain validation and testing using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The capstone is an accessible personal-data manager with list/add/search/update/delete/complete operations. Separate data model, validation, persistence, and interaction; test save/reload.

**Lesson focus:** Validation and testing. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
record=(id=1,title="Study",done=false)
function rename(r,title)
    cleaned=strip(title); isempty(cleaned) && throw(ArgumentError("blank title"))
    merge(r,(title=cleaned,))
end
println(rename(record,"Study Julia"))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Pass application state explicitly rather than hiding it in mutable globals.
- Validate updates and preserve stable record identifiers.
- Do not claim persistence or accessibility without save/reload and keyboard tests.

### Activities
1. Specify record fields and validation rules before storage.
2. Test list, add, search, update, delete, and completion.
3. Test duplicate, missing, empty, and invalid values.
4. Create a save/reload test and document known limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain validation and testing in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.5: Documentation and presentation

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain documentation and presentation using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The capstone is an accessible personal-data manager with list/add/search/update/delete/complete operations. Separate data model, validation, persistence, and interaction; test save/reload.

**Lesson focus:** Documentation and presentation. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
println("Acceptance: list, add, search, update, delete, complete; document persistence and keyboard workflow.")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Pass application state explicitly rather than hiding it in mutable globals.
- Validate updates and preserve stable record identifiers.
- Do not claim persistence or accessibility without save/reload and keyboard tests.

### Activities
1. Specify record fields and validation rules before storage.
2. Test list, add, search, update, delete, and completion.
3. Test duplicate, missing, empty, and invalid values.
4. Create a save/reload test and document known limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain documentation and presentation in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Julia-specific package and data-format notes

- The standard library includes `Test`, `Random`, and `TOML`.
- Julia does not include a general JSON parser in its standard library. Use JSON3.jl for JSON serialization and parsing, and record it in the active `Project.toml`.
- Use CSV.jl for quoted delimiters, escaped quotes, or embedded newlines. The introductory `split` approach is limited to simple sample data.
- Use DataFrames.jl only when tabular analysis justifies the dependency; begin with arrays, tuples, named tuples, and dictionaries.
- Standard Julia arrays are one-based. Use `eachindex` or `enumerate` when iteration needs indices.
<<<<<<< HEAD
=======

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)
