# Unit 9: Testing and Data Analysis

## Overview

Test functions and state changes, use pseudo-random values responsibly, and analyze text and CSV records while recognizing the limits of byte-oriented C examples and simple parsers.

Prerequisite: Unit 8. Learners should understand functions, structs, files, and error handling.

## Lesson 9.1: Testing functions

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Test deterministic functions with known inputs and expected results. C has no standard unit-test framework; begin with assertions from `assert.h`, then introduce a test framework if a project grows. Compile tests separately from the application and ensure tests cover ordinary values, boundaries, and invalid inputs.

### Worked Example
```c
#include <assert.h>
int add_two_numbers(int a, int b) { return a + b; }
int main(void)
{
    assert(add_two_numbers(5, 3) == 8);
    assert(add_two_numbers(-5, -3) == -8);
    assert(add_two_numbers(10, -4) == 6);
    return 0;
}
```
No output and exit status 0 indicate that all assertions passed. An assertion failure prints a diagnostic and terminates the test executable.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

The program prints nothing and exits normally.
### Common Mistakes
- Testing only one ordinary input and omitting boundaries and invalid cases.
- Writing assertions that duplicate implementation details instead of checking expected behavior.
- Compiling with `NDEBUG` and assuming assertions still execute.

### Activities
1. Test addition with positive, negative, and zero values.
2. Create one failing assertion and inspect the diagnostic.
3. Compile with and without `NDEBUG` and explain the effect on assertions.
4. Write the expected test result and explain what a failing assertion or diagnostic would indicate.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Testing functions" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 9.2: Testing stateful objects

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Test stateful records by creating a fresh instance for each test, changing its state through the public operations, and checking the resulting fields. In C, write explicit setup code in each test or a helper function; there is no built-in `setUp` lifecycle.

### Worked Example
```c
#include <assert.h>
typedef struct { int quantity; } Item;
void add_stock(Item *item, int amount) { if (amount > 0) item->quantity += amount; }
int main(void)
{
    Item notebook = {.quantity = 3};
    add_stock(&notebook, 2);
    assert(notebook.quantity == 5);
    add_stock(&notebook, -1);
    assert(notebook.quantity == 5);
    return 0;
}
```
The assertions verify that a positive restock changes quantity and a negative restock is rejected.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

The program prints nothing and exits normally.
### Common Mistakes
- Allowing one test's mutation to leak into another test.
- Checking only the function result rather than the changed item state.
- Failing to verify that a rejected restock leaves quantity unchanged.

### Activities
1. Restock by a positive amount and verify quantity changes.
2. Try zero and negative restock amounts and verify state remains unchanged.
3. Create fresh records for each test to prevent test-order dependence.
4. Write the expected test result and explain what a failing assertion or diagnostic would indicate.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Testing stateful objects" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 9.3: Random values

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use the pseudo-random number generator in `stdlib.h`. Seed once with `srand`, then obtain values with `rand`. The sequence is deterministic for a given implementation and seed; use a fixed seed in tests. Avoid modulo bias for applications requiring statistically sound sampling or security; `rand` is not cryptographically secure.

### Worked Example
```c
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    srand(42);
    int die = rand() % 6 + 1;
    printf("Die roll: %d\n", die);
    return 0;
}
```
The output is reproducible for a given C library implementation and seed, but the exact value may differ across implementations. Do not use `rand` for passwords or security tokens.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Die roll: 1
```
### Common Mistakes
- Treating `rand()` as cryptographically secure.
- Assuming `% 6` produces perfectly unbiased die rolls.
- Expecting the exact sequence to be portable across different C library implementations.

### Activities
1. Run twice with the same seed on the same C library and compare results.
2. Generate 1000 die values and verify each is between 1 and 6.
3. Explain why modulo reduction may be biased and why `rand` is not for secrets.
4. Write the expected test result and explain what a failing assertion or diagnostic would indicate.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Random values" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 9.4: Text analysis

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Analyze the same shared text sample by splitting it into words and counting frequencies. C requires explicit tokenization and storage. For a beginner exercise, normalize ASCII letters and count a small fixed set of words; explain that a production tokenizer must handle punctuation, UTF-8, and dynamic word storage correctly.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    char text[] = "A student studies programming. Programming develops problem-solving skills.";
    for (size_t i = 0; text[i]; ++i) text[i] = (char)tolower((unsigned char)text[i]);
    const char *word = "programming";
    int count = 0;
    char *p = text;
    while ((p = strstr(p, word)) != NULL) { ++count; p += strlen(word); }
    printf("Occurrences of programming: %d\n", count);
    return 0;
}
```
Expected output: 2 occurrences. This counts substring matches, not general word tokens; extend it to tokenize and count all words.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Occurrences of programming: 2
```
### Common Mistakes
- Counting substring matches as whole words.
- Passing a negative plain `char` to `tolower`.
- Treating ASCII byte operations as Unicode-aware tokenization.

### Activities
1. Count the two `programming` occurrences in the canonical sample.
2. Change case and punctuation and compare substring count with whole-word count.
3. Test a UTF-8 input and document the limits of byte-wise lowercase conversion.
4. Write the expected test result and explain what a failing assertion or diagnostic would indicate.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Text analysis" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 9.5: CSV records

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
CSV is a delimited text format with quoting rules; splitting every line on commas is not a correct general CSV parser because quoted fields may contain commas, quotes, and newlines. Use a documented CSV library for production data. For the first exercise, read a simple known CSV file and state that the format excludes quoted commas.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    FILE *file = fopen("students.csv", "r");
    char line[256];
    if (!file) { perror("students.csv"); return 1; }
    if (fgets(line, sizeof line, file)) printf("Columns: %s", line);
    while (fgets(line, sizeof line, file)) printf("Record: %s", line);
    fclose(file);
    return 0;
}
```
Create a header with `student_id,first_name,last_name,score,active` and at least two rows. The program prints the header and each record line. A production parser must handle CSV quoting correctly.

### Expected Behavior or Output

With `students.csv` in the working directory, containing:
```text
student_id,first_name,last_name,score,active
1,Avery,Student,91,true
2,Jordan,Lee,82,true
3,Casey,Smith,76,false
```

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Columns: student_id,first_name,last_name,score,active
Record: 1,Avery,Student,91,true
Record: 2,Jordan,Lee,82,true
Record: 3,Casey,Smith,76,false
```

### Common Mistakes
- Splitting every CSV line on commas despite quoted commas and escaped quotes.
- Ignoring overlong lines or malformed rows.
- Assuming every row contains the same number of fields without validating it.

### Activities
1. Create the canonical students.csv header and two data rows.
2. Test missing file, empty file, and an overlong row.
3. Add a quoted comma and explain why naive comma splitting is invalid CSV parsing.
4. Write the expected test result and explain what a failing assertion or diagnostic would indicate.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "CSV records" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
