# Unit 11: Capstone

## Overview

This unit covers accessible personal-data manager, model, persistence, CRUD, tests, documentation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 11.1: Capstone requirements

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Capstone requirements is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: set measurable acceptance criteria; constrain scope; include accessibility and data portability requirements.

### Worked Example
```cpp
std::cout << "Personal data manager requirements: create, list, search, update, delete, validate, persist.\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Personal data manager requirements: create, list, search, update, delete, validate, persist.
```

### Common Mistakes
- Set measurable acceptance criteria.
- Constrain scope.
- Include accessibility and data portability requirements.

### Activities
1. Trace the capstone requirements example and predict its output before compiling.
2. Adapt the example to personal records with stable IDs and CRUD operations and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 11.2: Data model and storage

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Data model and storage is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: use stable IDs rather than vector offsets; document the persisted schema; minimize sensitive sample data.

### Worked Example
```cpp
struct Record { int id; std::string title; std::string description; std::string category; std::string created_at; std::string updated_at; }; const std::vector<Record> records{{1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01"}}; for (const auto& record : records) std::cout << record.id << "," << record.title << "," << record.description << "," << record.category << "," << record.created_at << "," << record.updated_at << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
1,Course project,Personal data manager,education,2026-11-01,2026-11-01
```

### Common Mistakes
- Use stable IDs rather than vector offsets.
- Document the persisted schema.
- Minimize sensitive sample data.

### Activities
1. Trace the data model and storage example and predict its output before compiling.
2. Adapt the example to personal records with stable IDs and CRUD operations and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 11.3: Create/read/update/delete

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Create/read/update/delete is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: locate records by ID; distinguish not-found from success; validate replacement fields before mutating state.

### Worked Example
```cpp
struct Record { int id; std::string title; std::string description; std::string category; std::string created_at; std::string updated_at; }; std::vector<Record> records{{1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01"}}; records.push_back({2, "Study C++", "Complete functions unit", "learning", "2026-11-01", "2026-11-01"}); auto found = std::find_if(records.begin(), records.end(), [](const Record& record) { return record.id == 1; }); if (found != records.end()) found->title = "Updated course project"; records.erase(std::remove_if(records.begin(), records.end(), [](const Record& record) { return record.id == 2; }), records.end()); for (const auto& record : records) std::cout << record.id << ": " << record.title << '\n';
```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
1: Updated course project
```

### Common Mistakes
- Locate records by ID.
- Distinguish not-found from success.
- Validate replacement fields before mutating state.

### Activities
1. Trace the create/read/update/delete example and predict its output before compiling.
2. Adapt the example to personal records with stable IDs and CRUD operations and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 11.4: Validation and testing

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Validation and testing is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: test duplicate IDs and missing records; use temporary test files; make tests independent of execution order.

### Worked Example
```cpp
const auto valid_email = [](const std::string& email) { const auto at = email.find('@'); return at != std::string::npos && at > 0 && email.find('.', at) != std::string::npos; }; assert(valid_email("avery@example.test")); assert(!valid_email("invalid")); std::cout << "Validation tests passed\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Validation tests passed
```

### Common Mistakes
- Test duplicate IDs and missing records.
- Use temporary test files.
- Make tests independent of execution order.

### Activities
1. Trace the validation and testing example and predict its output before compiling.
2. Adapt the example to personal records with stable IDs and CRUD operations and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 11.5: Documentation and presentation

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Documentation and presentation is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: document exact build and run commands; state actual serialization support accurately; disclose limitations and accessibility coverage.

### Worked Example
```cpp
std::cout << "Build: c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror main.cpp -o app\n"; std::cout << "Document: requirements, data format, tests, limitations, accessibility\n";

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Build: c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror main.cpp -o app
Document: requirements, data format, tests, limitations, accessibility
```

### Common Mistakes
- Document exact build and run commands.
- State actual serialization support accurately.
- Disclose limitations and accessibility coverage.

### Activities
1. Trace the documentation and presentation example and predict its output before compiling.
2. Adapt the example to personal records with stable IDs and CRUD operations and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Runnable Reference Implementation

The repository includes a tested C++ domain and JSON-storage reference core in [capstone/README.md](capstone/README.md). Install the JSON development dependency described there, then run the acceptance command:

`g++ -std=c++20 -Wall -Wextra -Werror -ICPP/capstone CPP/capstone/test_records.cpp -o /tmp/cpp-capstone-tests && /tmp/cpp-capstone-tests`

The reference core does not replace the requirement to build and evaluate an accessible user interface.

### Skills Checklist
- [ ] I can explain documentation and presentation using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for personal records with stable IDs and CRUD operations without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.

## Course-Wide Assessment and Portfolio

Submit runnable exercises, prediction notes, debugging notes, tests, and the text adventure and personal-data manager projects. Assessment focuses on correctness, idiomatic C++, code explanation, independent debugging, and accessible interaction—not speed or visual editor use.

## AI and Academic Integrity

AI may be used only for personal conceptual explanations and reinforcement when the instructor permits. Do not use AI to write, complete, autocomplete, repair, or generate course code or assessment solutions. Students must explain every submitted statement independently.

## Further Learning

Use the official C++ language specification, standard-library documentation, and the linked setup resources. Verify APIs against the documentation for the installed toolchain.
