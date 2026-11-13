# Unit 3: Control Flow

## Overview

This unit covers Boolean expressions, conditionals, lists or arrays, iteration, string operations. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 3.1: Boolean expressions

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Relational operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) produce an integer truth value: zero is false and nonzero is true. Logical operators are `&&`, `||`, and `!`; `&&` and `||` short-circuit. Use braces for conditional blocks.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int score = 82, attendance = 95;
    if (score >= 70 && attendance >= 80) puts("Meets the course criteria.");
    if (score == 100 || attendance == 100) puts("At least one perfect result.");
    if (!(score < 0)) puts("Score is not negative.");
    return 0;
}
```
Expected output: `Meets the course criteria.` and `Score is not negative.`

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Meets the course criteria.
Score is not negative.
```
### Common Mistakes
- Using bitwise `&`/`|` when short-circuit logical `&&`/`||` is required.
- Reversing the score and attendance conditions.
- Assuming true is represented only by integer 1; any nonzero value is true.

### Activities
1. Evaluate the score/attendance condition for (82,95), (69,95), and (82,70).
2. Create an expression where `&&` short-circuits and explain which operand is skipped.
3. Add a test for score zero and explain C's truth-value convention.
4. Write expected results for the shared scores 82, 91, 76, and 88, and include at least one boundary condition for the concept.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Boolean expressions" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 3.2: Chained conditionals

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use `if`, `else if`, and `else` for mutually exclusive choices. Apply the shared grade thresholds from highest to lowest and reject scores outside 0–100 before classification.

### Worked Example
```c
#include <stdio.h>
char grade_for(int score)
{
    if (score < 0 || score > 100) return '?';
    if (score >= 90) return 'A';
    else if (score >= 80) return 'B';
    else if (score >= 70) return 'C';
    else if (score >= 60) return 'D';
    else return 'F';
}
int main(void)
{
    int tests[] = {91, 90, 82, 80, 76, 70, 60, 0, -1, 101};
    for (size_t i = 0; i < sizeof tests / sizeof tests[0]; ++i)
        printf("%d -> %c\n", tests[i], grade_for(tests[i]));
    return 0;
}
```
Expected mapping: 91/A, 90/A, 82/B, 80/B, 76/C, 70/C, 60/D, 0/F; -1 and 101 are invalid (`?`).

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
91 -> A
90 -> A
82 -> B
80 -> B
76 -> C
70 -> C
60 -> D
0 -> F
-1 -> ?
101 -> ?
```
### Common Mistakes
- Checking a lower grade boundary before a higher one and making a branch unreachable.
- Omitting the 0–100 validity check before assigning a grade.
- Using independent `if` statements when exactly one grade branch should run.

### Activities
1. Run the grade function for 91, 90, 82, 80, 76, 70, 60, and 0.
2. Add tests for 89, 79, 69, and 59 and predict the grade at each boundary.
3. Verify that -1 and 101 are rejected rather than assigned a grade.
4. Write expected results for the shared scores 82, 91, 76, and 88, and include at least one boundary condition for the concept.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Chained conditionals" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 3.3: Sequences and indexing

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C arrays store a fixed number of elements of one type. Indexing begins at zero and C does not automatically check bounds. A four-element array has valid indices 0–3. When an array is passed to a function, pass its length separately.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    size_t count = sizeof scores / sizeof scores[0];
    printf("First: %d\nLast: %d\nCount: %zu\n", scores[0], scores[count - 1], count);
    scores[2] = 80;
    printf("Updated third score: %d\n", scores[2]);
    return 0;
}
```
Expected output: first 82, last 88, count 4, updated third score 80.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
First: 82
Last: 88
Count: 4
Updated third score: 80
```
### Common Mistakes
- Accessing an array at index `count` instead of `count - 1` for its last element.
- Assuming C performs bounds checks automatically.
- Calculating array length after it has decayed to a pointer in a function parameter.

### Activities
1. Print each score with both its zero-based index and one-based position.
2. Change the third score from 76 to 80 and verify the updated array.
3. Explain why the valid indices for four elements are 0 through 3.
4. Write expected results for the shared scores 82, 91, 76, and 88, and include at least one boundary condition for the concept.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Sequences and indexing" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 3.4: For loops and iteration

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
A `for` loop has initialization, continuation condition, and update expression. Traverse the shared score array with a known count. Use `size_t` for indices and convert the total to `double` before calculating the average.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    size_t count = sizeof scores / sizeof scores[0];
    int total = 0;
    for (size_t i = 0; i < count; ++i) { printf("Score %zu: %d\n", i + 1, scores[i]); total += scores[i]; }
    printf("Total: %d\nAverage: %.2f\n", total, (double) total / count);
    return 0;
}
```
Expected total: 337; average: 84.25.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Score 1: 82
Score 2: 91
Score 3: 76
Score 4: 88
Total: 337
Average: 84.25
```
### Common Mistakes
- Using `i <= count` and reading beyond the final score.
- Forgetting to update the index or updating it twice.
- Calculating the average with integer division.

### Activities
1. Trace the index, running total, and output for each of the four scores.
2. Count scores greater than or equal to 80 and report the result.
3. Calculate the average using integer division and floating-point division; compare.
4. Write expected results for the shared scores 82, 91, 76, and 88, and include at least one boundary condition for the concept.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "For loops and iteration" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 3.5: String operations

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C strings are null-terminated character sequences. Use `strlen`, `strcmp`, and `strstr` from `string.h`; ensure every destination buffer has enough capacity. This example processes ASCII bytes. `strlen` counts bytes, not user-perceived Unicode characters.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    const char sample[] = "A student studies programming. Programming develops problem-solving skills.";
    char normalized[sizeof sample];
    size_t length = strlen(sample);
    for (size_t i = 0; i <= length; ++i) normalized[i] = (char)tolower((unsigned char)sample[i]);
    printf("Byte length: %zu\n", length);
    printf("Lowercase: %s\n", normalized);
    printf("Contains programming: %s\n", strstr(normalized, "programming") ? "yes" : "no");
    return 0;
}
```
Expected byte length: 75; substring result: yes. The cast to `unsigned char` is required for safe use of `tolower`.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Byte length: 75
Lowercase: a student studies programming. programming develops problem-solving skills.
Contains programming: yes
```
### Common Mistakes
- Writing a lowercase result into a buffer without space for the null terminator.
- Passing a negative plain `char` to `tolower` rather than an `unsigned char` value.
- Assuming byte length from `strlen` equals Unicode character count.

### Activities
1. Print the byte length and lowercase form of the canonical text sample.
2. Count occurrences of `programming` and test a missing substring.
3. Add a non-ASCII UTF-8 character and explain why byte length is not character count.
4. Write expected results for the shared scores 82, 91, 76, and 88, and include at least one boundary condition for the concept.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "String operations" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
