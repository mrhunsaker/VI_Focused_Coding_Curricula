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

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
1. create records
2. search by ID
3. validate input
4. save changes
```

>>>>>>> 2067a20 (curriculum clearning and updates)
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

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text adventure: rooms and movement is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: validate a direction before changing rooms; use consistent room identifiers; handle unknown exits.

### Worked Example
```cpp
<<<<<<< HEAD
const std::map<std::string, std::string> exits{{"start_room:north", "tunnel"}}; std::string room = "start_room"; const std::string direction = "north"; const std::string transition = room + ":" + direction; if (exits.contains(transition)) room = exits.at(transition); std::cout << "Current room: " << room << '\n';
=======
const std::map<std::string, std::string> exits{{"north", "Library"}, {"east", "Garden"}}; std::string room = "Atrium"; const std::string direction = "north"; if (exits.contains(direction)) room = exits.at(direction); std::cout << "Current room: " << room << '\n';
>>>>>>> 2067a20 (curriculum clearning and updates)

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Current room: Library
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Validate a direction before changing rooms.
- Use consistent room identifiers.
- Handle unknown exits.

### Activities
1. Trace the text adventure: rooms and movement example and predict its output before compiling.
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

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text adventure: inventory and puzzles is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: verify item ownership before puzzle actions; avoid erasing during unsafe traversal; test missing-item and repeated-use cases.

### Worked Example
```cpp
<<<<<<< HEAD
std::vector<std::string> inventory{"shiny key", "map"}; const bool has_key = std::find(inventory.begin(), inventory.end(), "shiny key") != inventory.end(); if (has_key) inventory.push_back("chest reward"); for (const auto& item : inventory) std::cout << item << '\n';
=======
std::vector<std::string> inventory{"key", "map"}; const bool has_key = std::find(inventory.begin(), inventory.end(), "key") != inventory.end(); if (has_key) inventory.push_back("chest reward"); for (const auto& item : inventory) std::cout << item << '\n';
>>>>>>> 2067a20 (curriculum clearning and updates)

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
key
map
chest reward
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Verify item ownership before puzzle actions.
- Avoid erasing during unsafe traversal.
- Test missing-item and repeated-use cases.

### Activities
1. Trace the text adventure: inventory and puzzles example and predict its output before compiling.
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

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
1: Read lesson [1] 2026-11-01
```

>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Added task: Read chapter
```

>>>>>>> 2067a20 (curriculum clearning and updates)
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
