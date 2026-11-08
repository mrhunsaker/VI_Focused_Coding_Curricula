# Unit 11: Capstone: Personal Data Manager

## Overview

Plan, implement, test, document, and present a C personal-data manager using the shared record fields and required CRUD/persistence behavior. Preserve the Python capstone's data and functional requirements while using a C-appropriate terminal-first interface.

Prerequisite: Units 1–10. Learners should be able to organize structs, functions, files, validation, and tests.

## Lesson 11.1: Capstone requirements

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
The Python capstone uses NiceGUI, but that framework is Python-specific. The C course must preserve the same user-facing data-manager requirements without pretending that NiceGUI has a C equivalent. Implement a keyboard-operable terminal interface first; a graphical interface is an optional extension using a separately selected C-compatible toolkit. The core record fields, operations, validation, persistence, tests, and accessibility acceptance criteria remain the same.

### Worked Example
Choose one collection: contacts, books/movies, to-do tasks, or inventory. Define fields, required values, validation rules, and the five required operations: add, view, edit, delete, save/load. For the to-do option, use `id`, `title`, `description`, `done`, and `created_at`. Document that the reference Python GUI is replaced by an accessible terminal interface in this C implementation.

<<<<<<< HEAD
=======
### Expected Behavior or Output

No program is run in this lesson. The expected result is a written specification that names the chosen collection, lists the shared record fields, states the validation rules, and describes the five required operations and the terminal interface.

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Omitting one of add, view, edit, delete, save, or load from the requirements.
- Designing a GUI-specific solution despite selecting a terminal interface.
- Failing to define required fields, validation, and acceptance tests.

### Activities
1. Choose a capstone domain and list fields, validation rules, and user operations.
2. Write acceptance tests for add, view, edit, delete, save, and load before implementation.
3. Document why the C implementation uses a terminal interface rather than the Python-specific NiceGUI framework.
4. Add one capstone acceptance-test case to the project test plan, including test data, expected persisted fields, and failure behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Capstone requirements" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 11.2: Data model and storage

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Define a C struct for the shared capstone record and choose a clear ownership strategy for strings. Fixed-size arrays are acceptable for a small beginner project if maximum lengths are documented and input is bounded. For persistent data, use a maintained JSON library and document its version, dependency setup, and error handling. The C standard library does not provide JSON serialization.

### Worked Example
```c
#include <stddef.h>
typedef struct {
    int id;
    char title[80];
    char description[240];
    char category[40];
    char created_at[32];
    char updated_at[32];
} DataItem;
```
The record contains the exact canonical capstone fields. Define which fields are required, how empty strings are handled, and how IDs and timestamps are generated. The serialization layer must preserve all fields when saving and loading.

<<<<<<< HEAD
=======
### Expected Behavior or Output

The struct definition prints nothing by itself, and it is not a complete program. The expected result is a written storage design: which fields are required, how empty strings are treated, how IDs and timestamps are produced, and how a save followed by a load preserves every field.

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Using fixed-size fields without documenting maximum lengths and truncation policy.
- Generating duplicate IDs or inconsistent timestamp formats.
- Serializing only part of the canonical record or trusting loaded fields without validation.

### Activities
1. Define every C record field and its maximum length or allocation strategy.
2. Specify ID generation, timestamp format, and string ownership.
3. Round-trip a record through the chosen JSON library and compare every field.
4. Add one capstone acceptance-test case to the project test plan, including test data, expected persisted fields, and failure behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Data model and storage" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 11.3: Create/read/update/delete

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Implement create, read, update, and delete operations as separate functions that operate on the same collection and report success or failure. Validate an identifier before modifying a record. After every operation, refresh the displayed list and persist successful changes. Avoid returning pointers to local stack variables.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
typedef struct { int id; char title[80]; int done; } Task;
int find_task(const Task tasks[], size_t count, int id)
{
    for (size_t i = 0; i < count; ++i) if (tasks[i].id == id) return (int)i;
    return -1;
}
int main(void)
{
    Task tasks[] = {{1, "Read C lesson", 0}, {2, "Practice arrays", 1}};
    size_t count = sizeof tasks / sizeof tasks[0];
    int index = find_task(tasks, count, 1);
    if (index >= 0) { strcpy(tasks[index].title, "Review C arrays"); tasks[index].done = 1; }
    for (size_t i = 0; i < count; ++i)
        printf("%d: %s (%s)\n", tasks[i].id, tasks[i].title, tasks[i].done ? "done" : "open");
    return 0;
}
```
Expected state: task 1 is renamed to Review C arrays and marked done; task 2 is unchanged. Add bounds-safe input and implement add/delete operations using the same ID lookup.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
1: Review C arrays (done)
2: Practice arrays (done)
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Using an unchecked lookup result as an array index.
- Copying a title into a fixed-size buffer without checking length.
- Changing in-memory state before persistence succeeds without a recovery strategy.

### Activities
1. Add two records and verify their stable display order.
2. Edit one record by ID and confirm unrelated fields remain unchanged.
3. Delete an existing record, then attempt to delete the same ID again.
4. Add one capstone acceptance-test case to the project test plan, including test data, expected persisted fields, and failure behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Create/read/update/delete" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 11.4: Validation and testing

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Validate required fields before creating or updating a record. Test duplicate IDs, empty titles, overlong input, missing files, malformed JSON, and operations on unknown IDs. Keep deterministic logic separate from terminal input so it can be tested. In C, use assertions or a test framework and run with compiler warnings; consider AddressSanitizer and UndefinedBehaviorSanitizer during development.

### Worked Example
```c
#include <assert.h>
#include <string.h>
int valid_title(const char *title)
{
    return title != NULL && title[0] != '\0';
}
int main(void)
{
    assert(valid_title("Read C lesson"));
    assert(!valid_title(""));
    assert(!valid_title(NULL));
    return 0;
}
```
All assertions pass with exit status 0. Add tests for the full CRUD functions and compile a debug build with `-fsanitize=address,undefined -fno-omit-frame-pointer` where supported.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

The program prints nothing and exits normally.
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Testing only successful operations and ignoring malformed input or missing files.
- Ignoring compiler warnings or sanitizer diagnostics.
- Using assertions for recoverable user input errors in the release application.

### Activities
1. Create a test matrix for valid, boundary, malformed, missing-file, and unknown-ID cases.
2. Compile with warnings and address every diagnostic.
3. Run AddressSanitizer and UndefinedBehaviorSanitizer where available and investigate reports.
4. Add one capstone acceptance-test case to the project test plan, including test data, expected persisted fields, and failure behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Validation and testing" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 11.5: Documentation and presentation

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
The deliverable includes source code, sample data, a README, build/run instructions, a description of the data format, and a reflection on accessibility. Document the compiler version, exact build command, external dependencies, file locations, and keyboard commands. Ensure prompts and status messages are meaningful when read linearly. Do not claim screen-reader testing unless it has actually been performed.

### Worked Example
README acceptance checklist: explain the selected data-manager domain; list the exact fields; document add/view/edit/delete/save/load; provide compile and run commands; describe how to navigate the menu by keyboard; explain how to recover from invalid input; include sample data and known limitations; record the screen reader and operating-system tests actually performed.

<<<<<<< HEAD
=======
### Expected Behavior or Output

No program is run in this lesson. The expected result is a README that satisfies the acceptance checklist, with compile and run commands that another person can follow from an empty folder, and a record of the screen reader and operating-system tests you actually performed.

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Omitting compiler version, build command, or dependency setup from the README.
- Claiming assistive-technology compatibility without testing a named screen reader and OS.
- Leaving sample data, menu commands, or known limitations undocumented.

### Activities
1. Build and run the project from a clean checkout using only the README instructions.
2. Document compiler, dependency versions, build command, file paths, and menu commands.
3. Test the documented keyboard workflow with a named access technology and record limitations.
4. Add one capstone acceptance-test case to the project test plan, including test data, expected persisted fields, and failure behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Documentation and presentation" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
<<<<<<< HEAD
=======

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)
