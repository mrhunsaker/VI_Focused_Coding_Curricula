# Unit 8: Files, Errors, and Persistence

## Overview

Read and write files with explicit error checks and resource cleanup. Distinguish standard C error reporting from exceptions, and use a maintained external library for JSON rather than ad hoc parsing.

Prerequisite: Unit 7. Learners should understand structs, pointers, and function return contracts.

## Lesson 8.1: Reading text files

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Open a text file with `fopen` and check for `NULL` before reading. Read lines with `fgets` into a bounded buffer; process each line before reading the next. Always close a successfully opened file. Use a relative path resolved from the program's working directory.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    FILE *file = fopen("notes.txt", "r");
    char line[256];
    if (file == NULL) { perror("notes.txt"); return 1; }
    while (fgets(line, sizeof line, file) != NULL) fputs(line, stdout);
    if (ferror(file)) { perror("Reading notes.txt"); fclose(file); return 1; }
    fclose(file);
    return 0;
}
```
Create `notes.txt` with two lines before running. The program reproduces those lines. A missing file produces a diagnostic and a nonzero exit status.

<<<<<<< HEAD
=======
### Expected Behavior or Output

With `notes.txt` in the working directory, containing:
```text
Practice C.
Review arrays and functions.
```

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Practice C.
Review arrays and functions.
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Using a `FILE *` after `fopen` returned `NULL`.
- Treating every failed `fgets` as normal EOF without checking `ferror`.
- Assuming a relative path is based on the source file location rather than the current working directory.

### Activities
1. Create a two-line notes file and verify that both lines are read.
2. Run with the file missing and inspect the diagnostic and exit status.
3. Create an overlong line and explain how truncation can be detected.
4. Record the file or data operation's success result, failure result, and the resource cleanup expected on each path.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Reading text files" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 8.2: Writing and appending files

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Open a file with mode `w` to create or truncate it, and mode `a` to append. Check both the `fopen` result and the return value of write operations. Close the file and check for errors when durability matters. Do not overwrite a user's file without explaining the effect.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    FILE *file = fopen("notes.txt", "a");
    if (file == NULL) { perror("notes.txt"); return 1; }
    if (fprintf(file, "Practice the C file API.\n") < 0) {
        perror("Writing notes.txt"); fclose(file); return 1;
    }
    if (fclose(file) == EOF) { perror("Closing notes.txt"); return 1; }
    puts("Note appended.");
    return 0;
}
```
Expected output: `Note appended.` The new line is added to the end of `notes.txt`.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Note appended.
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Opening in `w` mode and truncating a file that should have been appended.
- Ignoring `fprintf` and `fclose` failure results.
- Assuming buffered output has necessarily reached durable storage before close.

### Activities
1. Append a second note and verify that the original contents remain.
2. Run the append program twice and count the resulting lines.
3. Change append mode to write mode in a disposable copy and observe truncation.
4. Record the file or data operation's success result, failure result, and the resource cleanup expected on each path.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Writing and appending files" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 8.3: Errors and exceptions

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C does not have language-level exceptions. Standard library functions report errors through return values, error indicators, or `errno`. Check each function's documented failure convention and use `perror` or `strerror` to report system errors. Return status codes from functions so callers can respond.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    FILE *file = fopen("missing_notes.txt", "r");
    if (file == NULL) {
        perror("Unable to open missing_notes.txt");
        return 1;
    }
    fclose(file);
    return 0;
}
```
If the file is absent, the program prints an operating-system diagnostic and exits with status 1. This is explicit error handling, not a thrown exception.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Unable to open missing_notes.txt: No such file or directory
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Expecting C to provide language-level exceptions.
- Ignoring a function's documented error return convention or `errno`.
- Continuing with invalid state after reporting an error.

### Activities
1. Run with a missing file and identify the error return and diagnostic.
2. Run with an existing file and verify the success path.
3. Write a helper that returns an error code to its caller rather than printing inside the helper.
4. Record the file or data operation's success result, failure result, and the resource cleanup expected on each path.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Errors and exceptions" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 8.4: Resource cleanup

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C resource lifetime is manual for resources such as `FILE *` handles and dynamically allocated memory. Every successful acquisition must have a corresponding release on all control-flow paths. Use a single cleanup section when multiple operations can fail; do not close an uninitialized or already-closed resource.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int status = 1;
    FILE *file = fopen("notes.txt", "r");
    if (file == NULL) { perror("notes.txt"); goto cleanup; }
    puts("File opened successfully.");
    status = 0;
cleanup:
    if (file != NULL && fclose(file) == EOF) { perror("fclose"); status = 1; }
    return status;
}
```
The cleanup path closes the file exactly once if opening succeeded. In larger programs, structure functions so cleanup remains easy to audit.

<<<<<<< HEAD
=======
### Expected Behavior or Output

With `notes.txt` in the working directory, containing:
```text
Practice C.
Review arrays and functions.
```

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
File opened successfully.
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Returning from a function after acquiring a resource without releasing it.
- Closing a file twice or using it after close.
- Running cleanup on a resource that was never successfully acquired.

### Activities
1. Trace both the successful and failed `fopen` paths and locate the `fclose`.
2. Add a second resource and determine the correct cleanup order.
3. Introduce an early error after opening the file and verify that cleanup still occurs.
4. Record the file or data operation's success result, failure result, and the resource cleanup expected on each path.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Resource cleanup" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 8.5: JSON persistence

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
The C standard library does not include a JSON parser or serializer. Choose and document a maintained JSON library for projects that need JSON, and do not hand-parse arbitrary JSON with string operations. Teach the shared record schema independently of the library: `id`, `title`, `description`, `category`, `created_at`, and `updated_at`. Explain how JSON strings, numbers, booleans, arrays, and objects map to C data.

### Worked Example
```c
typedef struct {
    int id;
    char title[80];
    char description[240];
    char category[40];
    char created_at[32];
    char updated_at[32];
} DataItem;
```
This C struct is the in-memory shape of one capstone record. The JSON library layer must serialize every field and validate required fields when loading. Record the selected library and its build/link instructions in the project README.

<<<<<<< HEAD
=======
### Expected Behavior or Output

The struct definition prints nothing by itself, and it is not a complete program. The expected result of this lesson is a written plan that names the JSON library you chose, lists every field that must be saved and loaded, and says what happens when a field is missing.

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Trying to parse arbitrary JSON with comma splitting or substring search.
- Failing to validate required fields and JSON value types.
- Leaking parser-owned memory or retaining pointers after the JSON document is freed.

### Activities
1. Map each canonical capstone field to a C member and a JSON value type.
2. Select a maintained C JSON library and document its version and link command.
3. Test missing required fields, malformed JSON, and a valid round-trip record.
4. Record the file or data operation's success result, failure result, and the resource cleanup expected on each path.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "JSON persistence" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
