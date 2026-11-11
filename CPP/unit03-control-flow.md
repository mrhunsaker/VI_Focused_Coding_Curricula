# Unit 3: Control Flow

## Overview

This unit covers Boolean expressions, conditionals, lists or arrays, iteration, string operations. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 3.1: Boolean expressions

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Boolean expressions is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: use && and || for logical operations; compare with ==; use boolalpha when textual boolean output is required.

### Worked Example
```cpp
const int score = 82; const bool passed = score >= 60 && score <= 100; std::cout << std::boolalpha << "Valid passing score: " << passed << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Valid passing score: true
```

### Common Mistakes
- Use && and || for logical operations.
- Compare with ==.
- Use boolalpha when textual boolean output is required.

### Activities
1. Trace the boolean expressions example and predict its output before compiling.
2. Adapt the example to grade thresholds and score collections and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 3.2: Chained conditionals

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Chained conditionals is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: test the most restrictive grade threshold first; include exact boundary values; make score ranges exhaustive and non-overlapping.

### Worked Example
```cpp
for (int score : {59, 60, 79, 80, 89, 90, 100}) { const char grade = score >= 90 ? 'A' : score >= 80 ? 'B' : score >= 70 ? 'C' : score >= 60 ? 'D' : 'F'; std::cout << score << ": " << grade << '\n'; }

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
59: F
60: D
79: C
80: B
89: B
90: A
100: A
```

### Common Mistakes
- Test the most restrictive grade threshold first.
- Include exact boundary values.
- Make score ranges exhaustive and non-overlapping.

### Activities
1. Trace the chained conditionals example and predict its output before compiling.
2. Adapt the example to grade thresholds and score collections and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 3.3: Sequences and indexing

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Sequences and indexing is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: check vector bounds and emptiness; remember zero-based indexing; treat size as a count rather than a final index.

### Worked Example
```cpp
std::vector<int> scores{82, 91, 76, 88}; std::cout << "First: " << scores.at(0) << "; fourth: " << scores.at(3) << "; count: " << scores.size() << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
First: 82; fourth: 88; count: 4
```

### Common Mistakes
- Check vector bounds and emptiness.
- Remember zero-based indexing.
- Treat size as a count rather than a final index.

### Activities
1. Trace the sequences and indexing example and predict its output before compiling.
2. Adapt the example to grade thresholds and score collections and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 3.4: For loops and iteration

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
For loops and iteration is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: avoid invalidating iterators while traversing; use an accumulator with a suitable type; define the empty-collection case.

### Worked Example
```cpp
const std::vector<int> scores{82, 91, 76, 88}; int sum = 0; for (int score : scores) sum += score; std::cout << "Total: " << sum << "; average: " << static_cast<double>(sum) / scores.size() << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
Total: 337; average: 84.25
```

### Common Mistakes
- Avoid invalidating iterators while traversing.
- Use an accumulator with a suitable type.
- Define the empty-collection case.

### Activities
1. Trace the for loops and iteration example and predict its output before compiling.
2. Adapt the example to grade thresholds and score collections and preserve the same observable requirement using idiomatic C++20.
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

## Lesson 3.5: String operations

### Reading References
- Official C++ language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C++ terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
String operations is taught through the shared course datasets and requirements. The Python curriculum supplies a common problem context, not syntax to translate mechanically. In C++, make the type system, object lifetime, standard-library contracts, ownership, and failure behavior explicit. This lesson focuses on: treat std::string indexing as byte-oriented; pass unsigned char to cctype functions; remember substr takes a length.

### Worked Example
```cpp
std::string text = "Avery Studies Programming"; std::transform(text.begin(), text.end(), text.begin(), [](unsigned char ch) { return static_cast<char>(std::tolower(ch)); }); std::cout << text << "; length: " << text.size() << '\n';

```

**Trace:** predict the output before compiling. Identify declarations, values, control-flow decisions, and state changes in order. Then compile and compare actual output with the prediction. The lesson example is intended to be independently compilable.

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (g++ 13.3, C++20; the text of the output does not depend on the operating system):

```text
avery studies programming; length: 25
```

### Common Mistakes
- Treat std::string indexing as byte-oriented.
- Pass unsigned char to cctype functions.
- Remember substr takes a length.

### Activities
1. Trace the string operations example and predict its output before compiling.
2. Adapt the example to grade thresholds and score collections and preserve the same observable requirement using idiomatic C++20.
3. Add one boundary case and one invalid or missing-data case; state the expected result and implement the handling.
4. Write a short test or trace table, then explain the C++ type, lifetime, ownership, iterator, or error-handling rule that matters here.

### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain string operations using correct C++ terminology and distinguish it from the closest Python equivalent.
- [ ] I can trace the example and justify its output using C++ rules.
- [ ] I can implement the same requirement for grade thresholds and score collections without copying Python syntax.
- [ ] I can test a normal case, a boundary case, and a relevant invalid or failure case.
- [ ] I can compile the program, interpret diagnostics, and navigate source and terminal output using my access technology.
