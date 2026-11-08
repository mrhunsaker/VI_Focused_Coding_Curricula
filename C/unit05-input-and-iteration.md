# Unit 5: Input and Iteration

## Overview

Build robust input loops, validate parsed values, and control repetition with while, break, continue, and explicit state. Practice the same score and menu contexts while accounting for C's input and conversion APIs.

Prerequisite: Unit 4. Learners should be able to traverse arrays and write simple conditions.

## Lesson 5.1: Input and validation

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Read user input as text with `fgets`, then parse and validate it. A robust parser checks whether any digits were consumed, whether trailing characters remain, and whether the value is in range. Keep prompting until valid input arrives or end-of-file is reached.

### Worked Example
```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
int main(void)
{
    char line[80], *end;
    long value;
    for (;;) {
        printf("Enter a score from 0 to 100: ");
        if (!fgets(line, sizeof line, stdin)) return 1;
        value = strtol(line, &end, 10);
        while (isspace((unsigned char)*end)) ++end;
        if (end != line && *end == '\0' && value >= 0 && value <= 100) break;
        puts("Invalid score. Enter a whole number from 0 to 100.");
    }
    printf("Accepted score: %ld\n", value);
    return 0;
}
```
For input 82, output is `Accepted score: 82`; invalid values cause another prompt.

<<<<<<< HEAD
=======
### Expected Behavior or Output

With these lines typed as standard input:
```text
abc
105
88
```

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Enter a score from 0 to 100: Invalid score. Enter a whole number from 0 to 100.
Enter a score from 0 to 100: Invalid score. Enter a whole number from 0 to 100.
Enter a score from 0 to 100: Accepted score: 88
```

>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Accepting `82abc` as a valid score because `strtol` parsed the numeric prefix.
- Failing to reject values outside 0–100 or detect overflow.
- Treating blank input or end-of-file as a valid score.

### Activities
1. Verify that 0, 82, and 100 are accepted as scores.
2. Verify that -1, 101, blank input, and `82abc` are rejected.
3. Test a value outside the range of `long` and check overflow handling.
4. Write a trace table for one valid input, one rejected input, and the exact state at loop termination.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Input and validation" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 5.2: While loops

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
A `while` loop repeats while its condition is nonzero. Update the condition's state inside the loop so it eventually becomes false. A sentinel-controlled loop is useful for repeated menu input; document the sentinel and handle end-of-file.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int value, total = 0;
    puts("Enter scores; enter -1 to finish.");
    while (scanf("%d", &value) == 1 && value != -1) {
        total += value;
        printf("Running total: %d\n", total);
    }
    printf("Final total: %d\n", total);
    return 0;
}
```
For input 82, 91, -1, the running totals are 82 and 173; final total is 173. This compact example assumes integer tokens; the previous lesson's `fgets` parser is safer for robust input.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Enter scores; enter -1 to finish.
Final total: 0
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Failing to update the sentinel-controlled loop state.
- Ignoring `scanf`'s return value and repeatedly processing an invalid token.
- Choosing a sentinel that could also be a legitimate score without documenting the rule.

### Activities
1. Enter 82, 91, and -1 and trace the running total after each accepted score.
2. Enter -1 first and verify that the final total is zero.
3. Enter a nonnumeric token and explain why the unchecked `scanf` loop is not robust.
4. Write a trace table for one valid input, one rejected input, and the exact state at loop termination.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "While loops" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 5.3: Flags and break

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
A Boolean-like flag records whether a condition has occurred. Use `break` to leave the nearest loop once a search succeeds. Initialize the flag before the loop and update it at the point where the condition is met.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    int found = 0;
    for (size_t i = 0; i < sizeof scores / sizeof scores[0]; ++i) {
        if (scores[i] == 76) { found = 1; break; }
    }
    puts(found ? "Score found." : "Score not found.");
    return 0;
}
```
Expected output: `Score found.` Change the search value to 100 to exercise the not-found path.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Score found.
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Setting the found flag before the equality test.
- Forgetting to set the flag when the target is found.
- Breaking out of the wrong loop in a nested search.

### Activities
1. Search for 76 and trace when the flag changes and when the loop breaks.
2. Search for 100 and verify the not-found branch.
3. Rewrite the search as a function returning the matching index or -1.
4. Write a trace table for one valid input, one rejected input, and the exact state at loop termination.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Flags and break" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 5.4: Continue and filtering

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use `continue` to skip the remainder of the current loop iteration. It is useful for filtering records, but the condition must be explicit and understandable. Avoid using it to conceal complex control flow.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    for (size_t i = 0; i < sizeof scores / sizeof scores[0]; ++i) {
        if (scores[i] < 80) continue;
        printf("Passing score: %d\n", scores[i]);
    }
    return 0;
}
```
Expected output: Passing score: 82, 91, and 88, each on its own line.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Passing score: 82
Passing score: 91
Passing score: 88
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Printing a score before applying the filter condition.
- Skipping a required state update with `continue` in a `while` loop.
- Using `< 80` when the intended filter is `>= 80`.

### Activities
1. Filter the scores and print only values greater than or equal to 80.
2. Change the threshold to 90 and predict the remaining values.
3. Rewrite the loop without `continue` and compare the trace.
4. Write a trace table for one valid input, one rejected input, and the exact state at loop termination.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Continue and filtering" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 5.5: Infinite-loop prevention

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
An infinite loop occurs when the termination condition never becomes false or the state used by the condition is not updated. Check loop invariants, increment/decrement operations, sentinel handling, and all paths that can exit. Prefer a clear loop condition over an unconditional loop unless an explicit `break` is guaranteed.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int remaining = 3;
    while (remaining > 0) {
        printf("%d\n", remaining);
        --remaining;
    }
    puts("Finished.");
    return 0;
}
```
Expected output: 3, 2, 1, then Finished. Removing `--remaining` creates a non-terminating loop; diagnose it by tracing the condition and state.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
3
2
1
Finished.
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Leaving the variable in the loop condition unchanged.
- Moving the counter in the wrong direction or using a condition that cannot become false.
- Failing to trace early exits, EOF, and break conditions.

### Activities
1. Trace `remaining` from 3 to 0 and identify the terminating condition.
2. Remove the decrement in a disposable copy and explain why it loops indefinitely.
3. Add a maximum-iteration safeguard to a loop that processes untrusted input.
4. Write a trace table for one valid input, one rejected input, and the exact state at loop termination.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Infinite-loop prevention" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
