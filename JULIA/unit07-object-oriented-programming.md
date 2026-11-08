# Unit 7: Object-Oriented Programming

## Overview

This unit covers types/classes, instances, fields, methods, inheritance or interfaces, composition. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 7.1: Types and object models

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain types and object models using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Declare composite types with `struct` or `mutable struct`. Concrete types do not inherit from other concrete types; abstract types define dispatch hierarchies, and methods specialize on argument types. Composition models related data.

**Lesson focus:** Types and object models. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
struct Student
    name::String
    age::Int
end
println(Student("Avery",16))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Concrete Julia structs do not inherit from other concrete structs.
- An immutable `struct` cannot have its fields reassigned.
- Use abstract supertypes and multiple dispatch for polymorphic behavior.

### Activities
1. Model Avery or an inventory item with a Julia composite type.
2. Create multiple instances and inspect their fields.
3. Add a validation or display method using multiple dispatch.
4. Explain whether composition, immutability, or mutability fits the model.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain types and object models in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.2: Creating instances

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain creating instances using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Declare composite types with `struct` or `mutable struct`. Concrete types do not inherit from other concrete types; abstract types define dispatch hierarchies, and methods specialize on argument types. Composition models related data.

**Lesson focus:** Creating instances. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
struct Learner
    name::String
    subject::String
end
learners = [Learner("Avery","Computer Science"), Learner("Jordan","Math")]
foreach(println, learners)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Concrete Julia structs do not inherit from other concrete structs.
- An immutable `struct` cannot have its fields reassigned.
- Use abstract supertypes and multiple dispatch for polymorphic behavior.

### Activities
1. Model Avery or an inventory item with a Julia composite type.
2. Create multiple instances and inspect their fields.
3. Add a validation or display method using multiple dispatch.
4. Explain whether composition, immutability, or mutability fits the model.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain creating instances in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.3: Fields and methods

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain fields and methods using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Declare composite types with `struct` or `mutable struct`. Concrete types do not inherit from other concrete types; abstract types define dispatch hierarchies, and methods specialize on argument types. Composition models related data.

**Lesson focus:** Fields and methods. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
mutable struct Item
    name::String
    quantity::Int
end
item=Item("Notebook",3); item.quantity += 1
println(item.quantity)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Concrete Julia structs do not inherit from other concrete structs.
- An immutable `struct` cannot have its fields reassigned.
- Use abstract supertypes and multiple dispatch for polymorphic behavior.

### Activities
1. Model Avery or an inventory item with a Julia composite type.
2. Create multiple instances and inspect their fields.
3. Add a validation or display method using multiple dispatch.
4. Explain whether composition, immutability, or mutability fits the model.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain fields and methods in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.4: Inheritance and interfaces

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain inheritance and interfaces using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Declare composite types with `struct` or `mutable struct`. Concrete types do not inherit from other concrete types; abstract types define dispatch hierarchies, and methods specialize on argument types. Composition models related data.

**Lesson focus:** Inheritance and interfaces. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
abstract type Assessment end
struct Quiz <: Assessment; score::Int; end
struct Project <: Assessment; score::Int; end
score(x::Assessment)=x.score
println(score(Quiz(82))+score(Project(91)))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Concrete Julia structs do not inherit from other concrete structs.
- An immutable `struct` cannot have its fields reassigned.
- Use abstract supertypes and multiple dispatch for polymorphic behavior.

### Activities
1. Model Avery or an inventory item with a Julia composite type.
2. Create multiple instances and inspect their fields.
3. Add a validation or display method using multiple dispatch.
4. Explain whether composition, immutability, or mutability fits the model.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain inheritance and interfaces in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.5: Composition

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain composition using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Declare composite types with `struct` or `mutable struct`. Concrete types do not inherit from other concrete types; abstract types define dispatch hierarchies, and methods specialize on argument types. Composition models related data.

**Lesson focus:** Composition. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
struct Address; city::String; end
struct Person; name::String; address::Address; end
println(Person("Avery",Address("Farmington")))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Concrete Julia structs do not inherit from other concrete structs.
- An immutable `struct` cannot have its fields reassigned.
- Use abstract supertypes and multiple dispatch for polymorphic behavior.

### Activities
1. Model Avery or an inventory item with a Julia composite type.
2. Create multiple instances and inspect their fields.
3. Add a validation or display method using multiple dispatch.
4. Explain whether composition, immutability, or mutability fits the model.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain composition in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
