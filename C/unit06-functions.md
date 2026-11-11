# Unit 6: Functions

## Overview

Decompose programs into functions with clear parameter, return, array-count, and pointer contracts. Understand pass-by-value, scope, and the additional responsibilities of variadic interfaces.

Prerequisite: Unit 5. Learners should be comfortable with loops, arrays, and validated input.

## Lesson 6.1: Defining functions

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
A function gives a name to a reusable operation. Declare its return type, name, and parameter types. Put a prototype before the first call when the definition appears later. Keep one clear responsibility per function.

### Worked Example
```c
#include <stdio.h>
double calculate_tip(double bill, double rate)
{
    return bill * rate;
}
int main(void)
{
    double tip = calculate_tip(24.50, 0.15);
    printf("Tip: $%.2f\n", tip);
    return 0;
}
```
Expected tip display: $3.67 (the exact product 3.675 is stored as 3.67499999999999982, so `%.2f` rounds down). The function returns a value and does not print it itself.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Tip: $3.67
```
### Common Mistakes
- Calling a function before its prototype is visible.
- Declaring a non-void function but failing to return a value on every path.
- Combining calculation and printing so the function cannot be reused by another caller.

### Activities
1. Write `calculate_tip` and call it for a $24.50 bill at 15%.
2. Move the function below `main` and add a correct prototype.
3. Separate calculation from printing so a second caller can reuse the result.
4. Document the function contract: parameter types, return type, array count or pointer ownership where relevant, and the expected result for one call.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Defining functions" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 6.2: Parameters and arguments

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Arguments are the values supplied at a call site; parameters are the local variables receiving them. C passes arguments by value. To modify a caller's object, pass its address using a pointer. C has no default or named arguments; use explicit wrapper functions or configuration structs when needed.

### Worked Example
```c
#include <stdio.h>
double total_with_tip(double bill, double rate)
{
    return bill + bill * rate;
}
int main(void)
{
    printf("Total: $%.2f\n", total_with_tip(24.50, 0.15));
    return 0;
}
```
Expected total display: $28.18. Swap the two arguments and explain why the result changes; C uses positional arguments.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Total: $28.18
```
### Common Mistakes
- Assuming C passes ordinary arguments by reference.
- Swapping positional arguments with the same type and expecting the compiler to detect intent.
- Passing a pointer where the function expects a value or vice versa.

### Activities
1. Call `total_with_tip(24.50, 0.15)` and predict the output.
2. Swap the arguments and explain why C cannot infer their semantic roles when types match.
3. Write a second function that modifies a caller's integer through a pointer.
4. Document the function contract: parameter types, return type, array count or pointer ownership where relevant, and the expected result for one call.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Parameters and arguments" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 6.3: Return values

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
A non-void function returns a value using `return`. The caller can store it, pass it to another function, or print it. Use a `void` return type only when no value is returned. Every control-flow path in a non-void function must return an appropriate value.

### Worked Example
```c
#include <stdio.h>
int sum_scores(const int scores[], size_t count)
{
    int total = 0;
    for (size_t i = 0; i < count; ++i) total += scores[i];
    return total;
}
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    printf("Total: %d\n", sum_scores(scores, 4));
    return 0;
}
```
Expected total: 337. The function receives the array pointer and its length separately.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Total: 337
```
### Common Mistakes
- Omitting a return on one control-flow path.
- Returning a pointer to a local automatic variable.
- Returning a value that is silently converted to an unintended type.

### Activities
1. Call the score-summing function with the shared four values and verify 337.
2. Test a one-element array and an empty collection.
3. Add an average function and define behavior for count zero.
4. Document the function contract: parameter types, return type, array count or pointer ownership where relevant, and the expected result for one call.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Return values" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 6.4: Functions over collections

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Pass arrays to functions with an explicit element count. Use `const` when the function only reads the collection. A pointer parameter does not contain the original array length; the caller and callee must agree on the count.

### Worked Example
```c
#include <stdio.h>
double average(const int values[], size_t count)
{
    int total = 0;
    for (size_t i = 0; i < count; ++i) total += values[i];
    return count ? (double) total / count : 0.0;
}
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    printf("Average: %.2f\n", average(scores, 4));
    return 0;
}
```
Expected average: 84.25. Add a separate function that searches the inventory array by item name.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Average: 84.25
```
### Common Mistakes
- Assuming an array parameter carries its length.
- Passing a count larger than the actual array.
- Dividing by zero for an empty collection without defining a result.

### Activities
1. Calculate the average of the shared scores using the array-plus-count interface.
2. Test count zero and document the function's defined result.
3. Add a maximum function and test one-element and repeated-maximum arrays.
4. Document the function contract: parameter types, return type, array count or pointer ownership where relevant, and the expected result for one call.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Functions over collections" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 6.5: Scope and variadic arguments

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Local variables have block scope. A variable declared inside a function is not directly accessible elsewhere. C supports variadic functions through `<stdarg.h>`, but a format string or another explicit count is needed to describe the extra arguments. Prefer a typed array-plus-count interface for beginner exercises because it is easier to validate.

### Worked Example
```c
#include <stdio.h>
#include <stdarg.h>
int sum_values(size_t count, ...)
{
    int total = 0;
    va_list args;
    va_start(args, count);
    for (size_t i = 0; i < count; ++i) total += va_arg(args, int);
    va_end(args);
    return total;
}
int main(void)
{
    printf("Sum: %d\n", sum_values(4, 82, 91, 76, 88));
    return 0;
}
```
Expected sum: 337. The caller must pass the correct count and types; variadic arguments are not type-checked by the function signature.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Sum: 337
```
### Common Mistakes
- Using a block-local variable outside its scope.
- Passing the wrong promoted type to `va_arg`.
- Forgetting `va_end` or passing a variadic count inconsistent with the arguments.

### Activities
1. Move a variable into a nested block and test its scope.
2. Call the variadic sum with the four shared scores and verify 337.
3. Replace the variadic interface with an array-plus-count function and compare type safety.
4. Document the function contract: parameter types, return type, array count or pointer ownership where relevant, and the expected result for one call.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Scope and variadic arguments" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
