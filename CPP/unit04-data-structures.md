# Unit 4: Data Structures

## Overview

This unit covers sequence mutation, sorting, immutable records, maps, dictionaries, traversal. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 4.1: Mutable sequences

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Mutable sequences is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: check before pop_back; do not retain references across vector reallocation; use the iterator returned by erase.

### Worked Example
```cpp
std::vector<std::string> items{"Notebook", "Pencil"}; items.insert(items.begin() + 1, "Folder"); items.push_back("Eraser"); items.erase(items.begin()); for (const auto& item : items) std::cout << item << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Folder
Pencil
Eraser
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Check before pop_back.
- Do not retain references across vector reallocation.
- Use the iterator returned by erase.

### Activities
1. Trace the mutable sequences example and predict its output before compiling.
2. Adapt the example to inventory records and key-value quantities and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 4.2: Sorting and organizing data

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Sorting and organizing data is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: write a strict-weak-order comparator; sort by the field required by the task; use a compatible iterator category.

### Worked Example
```cpp
std::vector<int> quantities{10, 3, 4, 1}; std::sort(quantities.begin(), quantities.end()); std::reverse(quantities.begin(), quantities.end()); for (int quantity : quantities) std::cout << quantity << ' '; std::cout << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
10 4 3 1 
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Write a strict-weak-order comparator.
- Sort by the field required by the task.
- Use a compatible iterator category.

### Activities
1. Trace the sorting and organizing data example and predict its output before compiling.
2. Adapt the example to inventory records and key-value quantities and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 4.3: Immutable records

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Immutable records is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: understand const members' effect on assignment; avoid dangling references; distinguish const objects from mutable indirection.

### Worked Example
```cpp
struct Coordinate { const int x; const int y; }; const Coordinate point{3, 4}; std::cout << "Point: (" << point.x << ", " << point.y << ")\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Point: (3, 4)
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Understand const members' effect on assignment.
- Avoid dangling references.
- Distinguish const objects from mutable indirection.

### Activities
1. Trace the immutable records example and predict its output before compiling.
2. Adapt the example to inventory records and key-value quantities and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 4.4: Maps and key-value data

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Maps and key-value data is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: use find/contains for non-inserting lookup; remember map orders by key; avoid operator[] on const maps.

### Worked Example
```cpp
std::map<std::string, int> inventory{{"Notebook", 3}, {"Pencil", 10}, {"Folder", 4}}; inventory["Notebook"] += 1; std::cout << "Notebook count: " << inventory.at("Notebook") << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Notebook count: 4
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Use find/contains for non-inserting lookup.
- Remember map orders by key.
- Avoid operator[] on const maps.

### Activities
1. Trace the maps and key-value data example and predict its output before compiling.
2. Adapt the example to inventory records and key-value quantities and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 4.5: Collection traversal

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Collection traversal is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: prefer const auto& for read-only traversal; do not mutate the traversed container; initialize accumulators.

### Worked Example
```cpp
const std::map<std::string, int> inventory{{"Notebook", 3}, {"Pencil", 10}, {"Folder", 4}}; for (const auto& [name, quantity] : inventory) std::cout << name << " => " << quantity << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Folder => 4
Notebook => 3
Pencil => 10
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Prefer const auto& for read-only traversal.
- Do not mutate the traversed container.
- Initialize accumulators.

### Activities
1. Trace the collection traversal example and predict its output before compiling.
2. Adapt the example to inventory records and key-value quantities and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain collection traversal using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for inventory records and key-value quantities without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.
