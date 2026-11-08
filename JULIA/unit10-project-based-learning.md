# Unit 10: Project-Based Learning

## Overview

This unit covers requirements, top-down design, text adventure, command-line to-do manager, accessible validation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 10.1: Requirements and design

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain requirements and design using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Begin projects with requirements, input/output contracts, and acceptance tests. Keep the text adventure and task manager text-based. Reject invalid commands and communicate status through text, not color alone.

**Lesson focus:** Requirements and design. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
requirements=["show location","move through valid exits","list inventory","save tasks"]
foreach(println,requirements)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Write input, output, and acceptance criteria before implementation.
- Reject unknown commands and unavailable room exits explicitly.
- Make status understandable without color or mouse interaction.

### Activities
1. Write requirements before implementing a feature.
2. Test valid movement, unavailable exits, and unknown commands.
3. Test inventory and puzzle states with and without required items.
4. Review prompts and errors using keyboard-only, sequential reading.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain requirements and design in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain text adventure: rooms and movement using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Begin projects with requirements, input/output contracts, and acceptance tests. Keep the text adventure and task manager text-based. Reject invalid commands and communicate status through text, not color alone.

**Lesson focus:** Text adventure: rooms and movement. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
<<<<<<< HEAD
rooms=Dict("start_room"=>Dict("north"=>"tunnel"),"tunnel"=>Dict("south"=>"start_room"))
println(get(rooms["start_room"],"north","No exit"))
=======
rooms=Dict("Atrium"=>Dict("north"=>"Lab"),"Lab"=>Dict("south"=>"Atrium"))
println(get(rooms["Atrium"],"north","No exit"))
>>>>>>> 2067a20 (curriculum clearning and updates)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Write input, output, and acceptance criteria before implementation.
- Reject unknown commands and unavailable room exits explicitly.
- Make status understandable without color or mouse interaction.

### Activities
1. Write requirements before implementing a feature.
2. Test valid movement, unavailable exits, and unknown commands.
3. Test inventory and puzzle states with and without required items.
4. Review prompts and errors using keyboard-only, sequential reading.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain text adventure: rooms and movement in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain text adventure: inventory and puzzles using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Begin projects with requirements, input/output contracts, and acceptance tests. Keep the text adventure and task manager text-based. Reject invalid commands and communicate status through text, not color alone.

**Lesson focus:** Text adventure: inventory and puzzles. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
<<<<<<< HEAD
inventory=Set(["shiny key","map"])
println("The cabinet opens: ", "shiny key" in inventory)
=======
inventory=Set(["key","map"])
println("The cabinet opens: ", "key" in inventory)
>>>>>>> 2067a20 (curriculum clearning and updates)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Write input, output, and acceptance criteria before implementation.
- Reject unknown commands and unavailable room exits explicitly.
- Make status understandable without color or mouse interaction.

### Activities
1. Write requirements before implementing a feature.
2. Test valid movement, unavailable exits, and unknown commands.
3. Test inventory and puzzle states with and without required items.
4. Review prompts and errors using keyboard-only, sequential reading.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain text adventure: inventory and puzzles in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 10.4: Command-line to-do manager

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain command-line to-do manager using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Begin projects with requirements, input/output contracts, and acceptance tests. Keep the text adventure and task manager text-based. Reject invalid commands and communicate status through text, not color alone.

**Lesson focus:** Command-line to-do manager. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
tasks=[(id=1,title="Read lesson",done=false),(id=2,title="Run example",done=true)]
foreach(t->println(t.done ? "[x] " : "[ ] ",t.title),tasks)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Write input, output, and acceptance criteria before implementation.
- Reject unknown commands and unavailable room exits explicitly.
- Make status understandable without color or mouse interaction.

### Activities
1. Write requirements before implementing a feature.
2. Test valid movement, unavailable exits, and unknown commands.
3. Test inventory and puzzle states with and without required items.
4. Review prompts and errors using keyboard-only, sequential reading.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain command-line to-do manager in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 10.5: Accessible UX and validation

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain accessible ux and validation using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Begin projects with requirements, input/output contracts, and acceptance tests. Keep the text adventure and task manager text-based. Reject invalid commands and communicate status through text, not color alone.

**Lesson focus:** Accessible UX and validation. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
function validate_title(s)
    t=strip(s); isempty(t) && return (false,"Title cannot be blank")
    return (true,t)
end
println(validate_title("  Study Julia  "))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Write input, output, and acceptance criteria before implementation.
- Reject unknown commands and unavailable room exits explicitly.
- Make status understandable without color or mouse interaction.

### Activities
1. Write requirements before implementing a feature.
2. Test valid movement, unavailable exits, and unknown commands.
3. Test inventory and puzzle states with and without required items.
4. Review prompts and errors using keyboard-only, sequential reading.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain accessible ux and validation in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.
