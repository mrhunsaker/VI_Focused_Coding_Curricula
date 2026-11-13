# Unit 10: Project-Based Learning

## Overview

This unit covers requirements, top-down design, text adventure, command-line to-do manager, accessible validation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 10.1: Requirements and design

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Requirements and design is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: write observable acceptance criteria before implementation; include failure and empty-data scenarios; keep scope deliverable.

### Worked Example
```cpp
const std::vector<std::string> requirements{"create records", "search by ID", "validate input", "save changes"}; for (std::size_t i = 0; i < requirements.size(); ++i) std::cout << i + 1 << ". " << requirements[i] << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
1. create records
2. search by ID
3. validate input
4. save changes
```

### Common Mistakes
- Write observable acceptance criteria before implementation.
- Include failure and empty-data scenarios.
- Keep scope deliverable.

### Activities
1. Trace the requirements and design example and predict its output before compiling.
2. Adapt the example to text adventure and command-line to-do projects and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C++ terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.2: Text adventure: five rooms and movement

### Reading References
- [C++ standard library: map](https://en.cppreference.com/w/cpp/container/map)
- [C++ standard library: string](https://en.cppreference.com/w/cpp/string/basic_string)
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Represent all five canonical rooms with C++ structs and maps.
- Validate movement before changing the current room.
- Explain why the treasure room is not reachable until the key puzzle is implemented.

### Concept Explanation

Use the same five-room graph in every language. A Room stores a description and a map from direction strings to room identifiers. The player begins in start_room. Part 1 includes the unconditional connections but leaves the north exit from locked_door_room unavailable. A failed map lookup must not change the current room.

### Worked Example

```cpp
#include <iostream>
#include <map>
#include <string>

struct Room {
    std::string description;
    std::map<std::string, std::string> exits;
};

int main() {
    const std::map<std::string, Room> rooms{
        {"start_room", {"A dimly lit cave. A narrow passage leads north.", {{"north", "tunnel"}}}},
        {"tunnel", {"A damp tunnel. Passages lead south and east.", {{"south", "start_room"}, {"east", "clearing"}}}},
        {"clearing", {"A quiet clearing. An antechamber lies to the north.", {{"west", "tunnel"}, {"north", "locked_door_room"}}}},
        {"locked_door_room", {"A chamber with a heavy door to the north.", {{"south", "clearing"}}}},
        {"treasure_room", {"You found the treasure. You win!", {}}}
    };

    std::string current = "start_room";
    std::string command;
    while (true) {
        std::cout << "---\n" << rooms.at(current).description << "\nWhat do you want to do?\n";
        if (!std::getline(std::cin, command)) command = "quit";
        if (command == "quit") {
            std::cout << "Exiting game. Goodbye!\n";
            break;
        }
        const auto& exits = rooms.at(current).exits;
        const auto destination = exits.find(command);
        if (destination != exits.end()) current = destination->second;
        else std::cout << "You cannot go that way. Enter a listed direction or quit.\n";
    }
}
```

### Expected Behavior or Output

Enter north, east, north, north, quit. The player reaches tunnel, clearing, and locked_door_room. The second north is rejected and the current room does not change. The treasure room exists but has no incoming exit in Part 1.

### Common Mistakes
- Using map::at for a direction that may not exist.
- Updating current before checking the map lookup result.
- Defining a destination that is not one of the five room identifiers.
- Adding the treasure exit before implementing the key puzzle.

### Activities
1. Trace north, east, north, north and record the current room.
2. Try west from start_room and verify that the room does not change.
3. Check every exit destination against the room map.
4. Explain why treasure_room cannot yet be reached.

### Accessibility Practice

Announce the room description and prompt in a consistent order. The invalid-movement response explains what happened and how to continue. Compile and run from the terminal and inspect output sequentially with the learner's access technology.

### Skills Checklist
- [ ] I can model all five canonical rooms.
- [ ] I can use a map to represent exits.
- [ ] I can reject invalid movement without changing state.
- [ ] I can explain why the treasure room is not yet reachable.

---

## Lesson 10.3: Text adventure: shiny key and locked door

### Reading References
- [C++ standard library: vector](https://en.cppreference.com/w/cpp/container/vector)
- [C++ standard library: algorithm](https://en.cppreference.com/w/cpp/algorithm)
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Place the shiny key in start_room and transfer it to inventory exactly once.
- Require the key to be used in locked_door_room.
- Unlock the north exit only after the key puzzle succeeds.
- End the game when the player reaches treasure_room.

### Concept Explanation

Keep the same five-room graph. Each room has a vector of items. Picking up the shiny key removes it from the room and appends it to the inventory. The use command checks both the player's location and inventory. A north command from locked_door_room is rejected while the door is locked.

### Worked Example

```cpp
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

struct Room {
    std::string description;
    std::map<std::string, std::string> exits;
    std::vector<std::string> items;
};

int main() {
    std::map<std::string, Room> rooms{
        {"start_room", {"A dimly lit cave.", {{"north", "tunnel"}}, {"shiny key"}}},
        {"tunnel", {"A damp tunnel. Passages lead south and east.", {{"south", "start_room"}, {"east", "clearing"}}, {}}},
        {"clearing", {"A quiet clearing. An antechamber lies to the north.", {{"west", "tunnel"}, {"north", "locked_door_room"}}, {}}},
        {"locked_door_room", {"A chamber with a heavy door to the north.", {{"south", "clearing"}, {"north", "treasure_room"}}, {}}},
        {"treasure_room", {"You found the treasure. You win!", {}, {}}}
    };

    std::string current = "start_room";
    std::vector<std::string> inventory;
    bool door_locked = true;
    std::string command;

    while (true) {
        Room& room = rooms.at(current);
        std::cout << "\n" << room.description << "\n";
        if (current == "treasure_room") break;
        if (!room.items.empty()) {
            std::cout << "You see: ";
            for (const auto& item : room.items) std::cout << item << " ";
            std::cout << "\n";
        }
        std::cout << "Your inventory: ";
        if (inventory.empty()) std::cout << "empty";
        else for (const auto& item : inventory) std::cout << item << " ";
        std::cout << "\nWhat do you want to do?\n";

        if (!std::getline(std::cin, command)) command = "quit";
        if (command == "quit") {
            std::cout << "You quit the adventure.\n";
            break;
        } else if (command == "take shiny key") {
            auto item = std::find(room.items.begin(), room.items.end(), "shiny key");
            if (item != room.items.end()) {
                room.items.erase(item);
                inventory.push_back("shiny key");
                std::cout << "You picked up the shiny key.\n";
            } else std::cout << "There is no shiny key here to take.\n";
        } else if (command == "use shiny key") {
            if (current != "locked_door_room") std::cout << "You must be at the locked door to use the key.\n";
            else if (std::find(inventory.begin(), inventory.end(), "shiny key") == inventory.end())
                std::cout << "You do not have the shiny key.\n";
            else {
                door_locked = false;
                std::cout << "You unlocked the door!\n";
            }
        } else if (current == "locked_door_room" && command == "north" && door_locked) {
            std::cout << "The door is locked! You need to use the shiny key here.\n";
        } else {
            auto destination = room.exits.find(command);
            if (destination != room.exits.end()) current = destination->second;
            else std::cout << "Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.\n";
        }
    }
}
```

### Expected Behavior or Output

Enter north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north. The first north from locked_door_room is rejected. Taking the key removes it from the room and adds it to inventory. Using it outside locked_door_room is rejected. Using it in that room unlocks the door; the final north reaches treasure_room and prints the win description.

### Common Mistakes
- Erasing the key without adding it to inventory, or adding it without erasing it.
- Unlocking the door without checking the current room.
- Unlocking the door without checking inventory.
- Allowing north movement before door_locked becomes false.
- Using map::at for an unvalidated command.

### Activities
1. Run the complete puzzle sequence and record room, items, inventory, and door state.
2. Attempt to take the key twice and verify no duplicate is added.
3. Try to use the key outside locked_door_room.
4. Try north before and after unlocking.
5. Add a help command with all supported commands.

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
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Command-line to-do manager is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: use stable task IDs rather than vector positions; store completion separately; persist changes deliberately.

### Worked Example
```cpp
struct Task { int id; std::string title; std::string description; bool done; std::string created_at; }; std::vector<Task> tasks{{1, "Read lesson", "Review the C++ lesson", false, "2026-11-01"}}; tasks.at(0).done = true; for (const auto& task : tasks) std::cout << task.id << ": " << task.title << " [" << task.done << "] " << task.created_at << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
1: Read lesson [1] 2026-11-01
```

### Common Mistakes
- Use stable task IDs rather than vector positions.
- Store completion separately.
- Persist changes deliberately.

### Activities
1. Trace the command-line to-do manager example and predict its output before compiling.
2. Adapt the example to text adventure and command-line to-do projects and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the concept in C++ terminology.
- [ ] I can trace and predict the example.
- [ ] I can modify and run the code independently.
- [ ] I can identify and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.5: Accessible UX and validation

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Accessible UX and validation is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: validate each parsed argument; make errors identify the rejected field; keep prompts and status output predictable.

### Worked Example
```cpp
std::istringstream command("add Read chapter"); std::string action; command >> action; std::string title; std::getline(command >> std::ws, title); if (action == "add" && !title.empty()) std::cout << "Added task: " << title << '\n'; else std::cout << "Usage: add <task title>\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Added task: Read chapter
```

### Common Mistakes
- Validate each parsed argument.
- Make errors identify the rejected field.
- Keep prompts and status output predictable.

### Activities
1. Trace the accessible ux and validation example and predict its output before compiling.
2. Adapt the example to text adventure and command-line to-do projects and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain accessible ux and validation using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for text adventure and command-line to-do projects without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.
