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

## Lesson 10.2: Text adventure: five rooms and movement

### Reading References
- [Julia dictionaries](https://docs.julialang.org/en/v1/base/collections/#Dictionaries)
- [Julia input and output](https://docs.julialang.org/en/v1/base/io-network/)
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Represent all five canonical rooms and exits with Julia dictionaries.
- Validate movement before changing the current room.
- Explain why treasure_room is not reachable until the key puzzle is implemented.

### Concept Explanation

The shared graph has five rooms: start_room, tunnel, clearing, locked_door_room, and treasure_room. Each room stores a description and an exits dictionary. The player starts in start_room. Part 1 leaves the north exit from locked_door_room unavailable. The get function returns nothing for an absent direction, so an invalid command does not change state.

### Worked Example

```julia
function main()
rooms = Dict(
    "start_room" => (description = "A dimly lit cave. A narrow passage leads north.",
                     exits = Dict("north" => "tunnel")),
    "tunnel" => (description = "A damp tunnel. Passages lead south and east.",
                 exits = Dict("south" => "start_room", "east" => "clearing")),
    "clearing" => (description = "A quiet clearing. An antechamber lies to the north.",
                   exits = Dict("west" => "tunnel", "north" => "locked_door_room")),
    "locked_door_room" => (description = "A chamber with a heavy door to the north.",
                           exits = Dict("south" => "clearing")),
    "treasure_room" => (description = "You found the treasure. You win!",
                        exits = Dict())
)

current_room = "start_room"
while true
    room = rooms[current_room]
    println("---")
    println(room.description)
    println("What do you want to do?")
    command = eof(stdin) ? "quit" : lowercase(strip(readline()))
    if command == "quit"
        println("Exiting game. Goodbye!")
        break
    end
    destination = get(room.exits, command, nothing)
    if destination === nothing
        println("You cannot go that way. Enter a listed direction or quit.")
    else
        current_room = destination
    end
end
end

main()
```

### Expected Behavior or Output

Enter north, east, north, north, quit. The player reaches tunnel, clearing, and locked_door_room. The second north is rejected and the current room does not change. The treasure room exists but has no incoming exit in Part 1.

### Common Mistakes
- Indexing a dictionary with an unvalidated direction.
- Updating current_room before checking whether get returned nothing.
- Defining a destination that is not one of the five room identifiers.
- Adding the treasure exit before implementing the key puzzle.


- In Julia, place the interactive loop inside a function such as `main()` so assignments update the function-local `current_room` rather than triggering top-level soft-scope ambiguity.
### Activities
1. Trace north, east, north, north and record the current room.
2. Try west from start_room and verify that the room does not change.
3. Check every exit destination against the room dictionary.
4. Explain why treasure_room cannot yet be reached.

### Accessibility Practice

Announce the room description and prompt in a consistent order. The invalid-movement response explains what happened and how to continue. Run from the terminal and inspect output sequentially with the learner's access technology.

### Skills Checklist
- [ ] I can model all five canonical rooms.
- [ ] I can represent exits with dictionaries.
- [ ] I can reject invalid movement without changing state.
- [ ] I can explain why the treasure room is not yet reachable.

---

## Lesson 10.3: Text adventure: shiny key and locked door

### Reading References
- [Julia arrays](https://docs.julialang.org/en/v1/manual/arrays/)
- [Julia dictionaries](https://docs.julialang.org/en/v1/base/collections/#Dictionaries)
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Place the shiny key in start_room and transfer it to inventory exactly once.
- Require key use in locked_door_room.
- Unlock the north exit only after the puzzle succeeds.
- End the game when the player reaches treasure_room.

### Concept Explanation

Keep the same five-room graph. Each room has a mutable items vector. Taking the shiny key removes it from start_room and adds it to inventory. Using the key succeeds only in locked_door_room when inventory contains it. The north exit remains blocked until the key is used.

### Worked Example

```julia
function main()
rooms = Dict(
    "start_room" => (description = "A dimly lit cave.",
                     exits = Dict("north" => "tunnel"), items = ["shiny key"]),
    "tunnel" => (description = "A damp tunnel. Passages lead south and east.",
                 exits = Dict("south" => "start_room", "east" => "clearing"), items = String[]),
    "clearing" => (description = "A quiet clearing. Antechamber lies to the north.",
                   exits = Dict("west" => "tunnel", "north" => "locked_door_room"), items = String[]),
    "locked_door_room" => (description = "A chamber with a heavy door to the north.",
                           exits = Dict("south" => "clearing", "north" => "treasure_room"), items = String[]),
    "treasure_room" => (description = "You found the treasure. You win!",
                        exits = Dict(), items = String[])
)

current_room = "start_room"
inventory = String[]
door_locked = true

while true
    room = rooms[current_room]
    println()
    println(room.description)
    current_room == "treasure_room" && break
    !isempty(room.items) && println("You see: ", join(room.items, ", "))
    println("Your inventory: ", isempty(inventory) ? "empty" : join(inventory, ", "))
    println("What do you want to do?")
    command = eof(stdin) ? "quit" : lowercase(strip(readline()))

    if command == "quit"
        println("You quit the adventure.")
        break
    elseif command == "take shiny key"
        index = findfirst(==("shiny key"), room.items)
        if index === nothing
            println("There is no shiny key here to take.")
        else
            deleteat!(room.items, index)
            push!(inventory, "shiny key")
            println("You picked up the shiny key.")
        end
    elseif command == "use shiny key"
        if current_room != "locked_door_room"
            println("You must be at the locked door to use the key.")
        elseif !("shiny key" in inventory)
            println("You do not have the shiny key.")
        else
            door_locked = false
            println("You unlocked the door!")
        end
    elseif current_room == "locked_door_room" && command == "north" && door_locked
        println("The door is locked! You need to use the shiny key here.")
    elseif haskey(room.exits, command)
        current_room = room.exits[command]
    else
        println("Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.")
    end
end
end

main()
```

### Expected Behavior or Output

Enter north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north. The first north from locked_door_room is rejected. Taking the key removes it from the room and adds it to inventory. Using it outside locked_door_room is rejected. Using it there unlocks the door; the final north reaches treasure_room and prints the win description.

### Common Mistakes
- Deleting the key from the room without adding it to inventory.
- Unlocking the door outside locked_door_room.
- Unlocking the door without checking inventory.
- Allowing north movement before door_locked becomes false.
- Mutating a copied room collection instead of the stored mutable vector.


- In Julia, place the interactive loop inside a function such as `main()` so assignments update the function-local `current_room` rather than triggering top-level soft-scope ambiguity.
### Activities
1. Run the complete puzzle sequence and record room, items, inventory, and door state.
2. Attempt to take the key twice; the second attempt must be rejected.
3. Try to use the key outside locked_door_room.
4. Try north before and after unlocking.
5. Add a help command listing every supported command.

### Accessibility Practice

Announce the room, visible items, inventory, and prompt as separate text lines. Error messages explain the failed action. Test the complete interaction with keyboard-only input and sequential screen-reader output.

### Skills Checklist
- [ ] I can model the five canonical rooms.
- [ ] I can transfer the key from a room to inventory.
- [ ] I can prevent duplicate pickup.
- [ ] I can require key use in locked_door_room.
- [ ] I can block and unlock the north exit.
- [ ] I can end the game in treasure_room.

---

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
