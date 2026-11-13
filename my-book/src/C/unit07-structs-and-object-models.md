# Unit 7: Structs and Object Models

## Overview

Use structs and functions to organize related data and behavior. C does not provide class methods or built-in inheritance; use composition and explicit interfaces, and document pointer ownership and object lifetime.

Prerequisite: Unit 6. Learners should understand functions, pointers, and record fields.

## Lesson 7.1: Types and object models

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C does not have classes in the C++/Java sense. Use `struct` to group related data and functions that operate on the data to model an object. Encapsulation is a design discipline in C: expose an interface in a header and keep implementation details in a source file. The shared domain is a student or inventory item.

### Worked Example
```c
typedef struct {
    char name[40];
    int quantity;
    double unit_price;
} Item;
```
This record models one inventory item with the same fields used throughout the course: name, quantity, and unit price. A C struct stores fields; it does not automatically provide constructors, methods, or memory management.

### Expected Behavior or Output

The struct definition prints nothing by itself, and it is not a complete program. Use it in a program that creates an `Item` (see Lesson 7.2) to see output. A correct answer to the activities lists the three fields and says that C leaves construction, validation, and cleanup to your own functions.

### Common Mistakes
- Describing a C struct as a class with built-in methods and constructors.
- Failing to separate public declarations from implementation details in headers and source files.
- Using pointer fields without documenting ownership and lifetime.

### Activities
1. Define an `Item` struct with name, quantity, and unit price.
2. Move the declaration into a header and include it from a source file.
3. Explain why C structs group fields but do not supply methods or automatic constructors.
4. Document the struct fields, initialization values, ownership rules, and the expected state after one operation.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Types and object models" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 7.2: Creating instances

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Declare a struct variable to create an instance. Initialize each field deliberately; aggregate initialization follows field order unless designated initializers are used. Copying a struct copies its fields, including pointer values, not the memory referenced by those pointers.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *name; int quantity; double unit_price; } Item;
int main(void)
{
    Item notebook = {.name = "Notebook", .quantity = 3, .unit_price = 2.50};
    Item pencil = {.name = "Pencil", .quantity = 10, .unit_price = 0.50};
    printf("%s: %d; %s: %d\n", notebook.name, notebook.quantity, pencil.name, pencil.quantity);
    return 0;
}
```
Expected output: Notebook: 3; Pencil: 10. The two variables are separate struct instances.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Notebook: 3; Pencil: 10
```
### Common Mistakes
- Using field-order initialization incorrectly.
- Leaving a field unintentionally uninitialized in an automatic object.
- Assuming struct assignment performs a deep copy of pointer members.

### Activities
1. Initialize Notebook, Pencil, and Folder with designated initializers.
2. Copy one record and explain which data is copied when a member is a pointer.
3. Change one record's quantity and verify the other instance is unchanged.
4. Document the struct fields, initialization values, ownership rules, and the expected state after one operation.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Creating instances" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 7.3: Fields and methods

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Access struct fields with `.` when you have an object and `->` when you have a pointer to an object. Functions that operate on a struct can receive a pointer; use `const` for read-only access. Keep data and operations conceptually together even though C does not have member methods.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *name; int quantity; double unit_price; } Item;
double item_value(const Item *item)
{
    return item->quantity * item->unit_price;
}
int main(void)
{
    Item notebook = {"Notebook", 3, 2.50};
    printf("%s inventory value: $%.2f\n", notebook.name, item_value(&notebook));
    return 0;
}
```
Expected output: Notebook inventory value: $7.50.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Notebook inventory value: $7.50
```
### Common Mistakes
- Confusing `.` and `->` member access.
- Dereferencing a null pointer.
- Omitting `const` when a function should only inspect an item.

### Activities
1. Calculate the value of three notebooks through `item_value`.
2. Compare `.` member access on an object with `->` on a pointer.
3. Add a null-pointer check and a `const` parameter.
4. Document the struct fields, initialization values, ownership rules, and the expected state after one operation.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Fields and methods" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 7.4: Inheritance and interfaces

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C has no built-in class inheritance. Model shared behavior with composition, function pointers, or tagged unions when appropriate. Do not force an inheritance hierarchy into C. For a simple specialization, use a base record as a field in a larger record and document the relationship explicitly.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *name; int quantity; double unit_price; } Item;
typedef struct { Item item; int reorder_level; } StockedItem;
int needs_reorder(const StockedItem *stock)
{
    return stock->item.quantity <= stock->reorder_level;
}
int main(void)
{
    StockedItem notebook = {{"Notebook", 3, 2.50}, 3};
    printf("%s reorder required: %s\n", notebook.item.name,
           needs_reorder(&notebook) ? "yes" : "no");
    return 0;
}
```
Expected output: Notebook reorder required: yes. This is composition, not language-level inheritance.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Notebook reorder required: yes
```
### Common Mistakes
- Claiming C has native class inheritance or virtual dispatch.
- Treating an embedded struct as automatically substitutable for its containing type.
- Using function pointers without a matching declared signature.

### Activities
1. Create a `StockedItem` by embedding an `Item` and a reorder threshold.
2. Test quantities below, equal to, and above the threshold.
3. Explain why this composition is not C++-style inheritance.
4. Document the struct fields, initialization values, ownership rules, and the expected state after one operation.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Inheritance and interfaces" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 7.5: Composition

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Composition builds a larger object from smaller related records. For the course's personal data manager, a manager can contain an array of items plus a count and capacity. Define ownership clearly: decide which function allocates and frees any dynamically allocated memory.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *title; int done; } Task;
typedef struct { Task tasks[10]; size_t count; } TaskManager;
int main(void)
{
    TaskManager manager = {.tasks = {{"Review C arrays", 0}, {"Practice functions", 1}}, .count = 2};
    for (size_t i = 0; i < manager.count; ++i)
        printf("%s: %s\n", manager.tasks[i].title, manager.tasks[i].done ? "done" : "not done");
    return 0;
}
```
Expected output lists the two tasks and their completion states.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Review C arrays: not done
Practice functions: done
```
### Common Mistakes
- Calling composition inheritance.
- Allowing the task count to exceed the fixed array capacity.
- Failing to define whether nested strings are owned or borrowed.

### Activities
1. Create a task manager with two tasks and print completion states.
2. Attempt to add an eleventh task to a ten-slot manager and handle capacity safely.
3. Document whether the manager owns task strings or borrows pointers.
4. Document the struct fields, initialization values, ownership rules, and the expected state after one operation.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Composition" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
