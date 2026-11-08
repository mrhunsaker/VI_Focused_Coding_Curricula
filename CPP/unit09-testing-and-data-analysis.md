# Unit 9: Testing and Data Analysis

## Overview

This unit covers unit tests, testing stateful types, randomness, text analysis, CSV processing. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 9.1: Testing functions

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Testing functions is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: do not rely solely on assert in release builds; test independent expected results; include boundary and invalid inputs.

### Worked Example
```cpp
const auto add = [](int a, int b) { return a + b; }; assert(add(2, 3) == 5); assert(add(-2, 2) == 0); std::cout << "Function tests passed\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Function tests passed
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Do not rely solely on assert in release builds.
- Test independent expected results.
- Include boundary and invalid inputs.

### Activities
1. Trace the testing functions example and predict its output before compiling.
2. Adapt the example to unit tests, random values, and text analysis and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 9.2: Testing stateful objects

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Testing stateful objects is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: assert state after each operation; isolate setup between tests; avoid order-dependent shared state.

### Worked Example
```cpp
struct Inventory { int quantity{0}; void add(int amount) { if (amount > 0) quantity += amount; } }; Inventory stock; stock.add(3); stock.add(-1); assert(stock.quantity == 3); std::cout << "State test passed\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
State test passed
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Assert state after each operation.
- Isolate setup between tests.
- Avoid order-dependent shared state.

### Activities
1. Trace the testing stateful objects example and predict its output before compiling.
2. Adapt the example to unit tests, random values, and text analysis and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 9.3: Random values

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Random values is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: seed engines for reproducibility; use standard distributions rather than modulo; do not promise identical sequences across libraries.

### Worked Example
```cpp
std::mt19937 engine(42); std::uniform_int_distribution<int> die(1, 6); for (int i = 0; i < 5; ++i) std::cout << die(engine) << (i == 4 ? '\n' : ' ');

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
3 5 6 2 5
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Seed engines for reproducibility.
- Use standard distributions rather than modulo.
- Do not promise identical sequences across libraries.

### Activities
1. Trace the random values example and predict its output before compiling.
2. Adapt the example to unit tests, random values, and text analysis and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 9.4: Text analysis

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Text analysis is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: pass unsigned char to cctype; distinguish bytes from Unicode characters; document locale assumptions.

### Worked Example
```cpp
const std::string sample = "A student studies programming. Programming develops problem-solving skills."; int letters = 0, spaces = 0; for (unsigned char ch : sample) { if (std::isalpha(ch)) ++letters; if (std::isspace(ch)) ++spaces; } std::cout << "Letters: " << letters << "; spaces: " << spaces << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Letters: 65; spaces: 7
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Pass unsigned char to cctype.
- Distinguish bytes from Unicode characters.
- Document locale assumptions.

### Activities
1. Trace the text analysis example and predict its output before compiling.
2. Adapt the example to unit tests, random values, and text analysis and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 9.5: CSV records

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
CSV records is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: a comma split is not a complete quoted-CSV parser; validate field count; ensure stoi consumed the whole field.

### Worked Example
```cpp
std::istringstream row("001,Avery,Student,92,true"); std::string id, first_name, last_name, score_text, active; std::getline(row, id, ','); std::getline(row, first_name, ','); std::getline(row, last_name, ','); std::getline(row, score_text, ','); std::getline(row, active); const int score = std::stoi(score_text); std::cout << id << ": " << first_name << " " << last_name << ", score " << score << ", active " << active << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
001: Avery Student, score 92, active true
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- A comma split is not a complete quoted-CSV parser.
- Validate field count.
- Ensure stoi consumed the whole field.

### Activities
1. Trace the csv records example and predict its output before compiling.
2. Adapt the example to unit tests, random values, and text analysis and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain csv records using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for unit tests, random values, and text analysis without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.
