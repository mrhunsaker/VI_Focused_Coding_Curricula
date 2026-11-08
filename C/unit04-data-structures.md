# Unit 4: Data Structures

## Overview

Represent collections and records using C arrays, structs, pointers, and standard-library algorithms. Compare these explicit data structures with Python lists, tuples, and dictionaries, and document capacity and ownership.

Prerequisite: Unit 3. Learners should understand arrays, indexing, loops, and string basics.

## Lesson 4.1: Mutable sequences

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C arrays have fixed capacity. For a resizable sequence, manage a dynamically allocated buffer with a pointer, element count, and capacity. Every allocation must be checked and every successful allocation must eventually be released with `free`.

### Worked Example
```c
#include <stdio.h>
int main(void)
{
    int scores[8] = {82, 91, 76, 88};
    size_t count = 4;
    scores[count++] = 95;
    scores[count++] = 84;
    printf("Count: %zu; last: %d\n", count, scores[count - 1]);
    return 0;
}
```
Expected output: `Count: 6; last: 84`. The array has capacity 8 and currently contains 6 values; do not confuse capacity with count.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Count: 6; last: 84
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Treating array capacity as the number of currently valid elements.
- Appending after capacity is exhausted.
- Overwriting the original pointer with a failed `realloc` result.

### Activities
1. Append 95 and 84 while tracking count separately from capacity.
2. Attempt to append beyond capacity and design a safe rejection or growth policy.
3. Sketch a `realloc` helper that checks failure without losing the original pointer.
4. Write a small test case that proves the collection count and capacity remain distinct and that all inventory fields stay associated.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Mutable sequences" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 4.2: Sorting and organizing data

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use `qsort` from `stdlib.h` to sort an array. The comparator must return a negative value, zero, or a positive value and must avoid subtraction that could overflow. Sorting changes the order of the original array.

### Worked Example
```c
#include <stdio.h>
#include <stdlib.h>
int compare_ints(const void *a, const void *b)
{
    int left = *(const int *)a, right = *(const int *)b;
    return (left > right) - (left < right);
}
int main(void)
{
    int scores[] = {82, 91, 76, 88};
    size_t n = sizeof scores / sizeof scores[0];
    qsort(scores, n, sizeof scores[0], compare_ints);
    for (size_t i = 0; i < n; ++i) printf("%d ", scores[i]);
    puts("");
    return 0;
}
```
Expected ascending order: 76 82 88 91. Reverse traversal prints descending order.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
76 82 88 91 
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Returning `a - b` from a comparator, which can overflow.
- Returning inconsistent results for equal values.
- Sorting only keys and accidentally separating them from their inventory record fields.

### Activities
1. Sort scores and verify the order 76, 82, 88, 91.
2. Change the comparator to descending order and test equal values.
3. Sort inventory records by quantity without separating fields from their item.
4. Write a small test case that proves the collection count and capacity remain distinct and that all inventory fields stay associated.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Sorting and organizing data" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 4.3: Immutable records

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Python tuples are immutable sequences. C has no direct tuple type; use a `struct` for a named record and make the object `const` when it must not be modified. A struct groups fields that may have different types.

### Worked Example
```c
#include <stdio.h>
typedef struct { int x; int y; } Point;
int main(void)
{
    const Point origin_offset = {3, 4};
    printf("x: %d\ny: %d\n", origin_offset.x, origin_offset.y);
    return 0;
}
```
Expected output: x: 3 and y: 4. `const` prevents modifying the fields through this object.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
x: 3
y: 4
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Assuming C structs are immutable without `const`.
- Assuming copying a struct containing pointers also copies the pointed-to data.
- Relying on positional initializers when field order is unclear.

### Activities
1. Create a `Point` record for coordinates (3,4) and calculate its distance.
2. Compare designated and positional initialization for the same record.
3. Add a pointer member and explain why a struct copy is not a deep copy.
4. Write a small test case that proves the collection count and capacity remain distinct and that all inventory fields stay associated.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Immutable records" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 4.4: Maps and key-value data

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
C does not include a built-in dictionary or hash map. For a small fixed inventory, use an array of structs and search by key; for larger data, introduce a hash-table implementation or a library. The key and value fields must be represented explicitly.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *name; int quantity; double unit_price; } Item;
int main(void)
{
    Item inventory[] = {{"Notebook",3,2.50},{"Pencil",10,0.50},{"Folder",4,1.25}};
    for (size_t i = 0; i < sizeof inventory / sizeof inventory[0]; ++i)
        printf("%s: %d at $%.2f each\n", inventory[i].name, inventory[i].quantity, inventory[i].unit_price);
    return 0;
}
```
Expected records: Notebook 3 at $2.50; Pencil 10 at $0.50; Folder 4 at $1.25.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Notebook: 3 at $2.50 each
Pencil: 10 at $0.50 each
Folder: 4 at $1.25 each
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Expecting a built-in C dictionary or hash map.
- Comparing string keys with `==` instead of `strcmp`.
- Using a search result without checking for the not-found case.

### Activities
1. Search the inventory for `Pencil` and display quantity and unit price.
2. Search for a missing key and report not found without using an invalid index.
3. Explain when an array scan becomes inefficient and a hash table is justified.
4. Write a small test case that proves the collection count and capacity remain distinct and that all inventory fields stay associated.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Maps and key-value data" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 4.5: Collection traversal

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Traverse an array of records with an index and explicit count. A struct member is accessed with the dot operator. When passing records to helper functions, use pointers to avoid unnecessary copies and `const` when the function should not modify the record.

### Worked Example
```c
#include <stdio.h>
typedef struct { const char *name; int quantity; double unit_price; } Item;
void show_item(const Item *item)
{
    printf("%s: quantity %d; value $%.2f\n", item->name, item->quantity, item->quantity * item->unit_price);
}
int main(void)
{
    Item items[] = {{"Notebook",3,2.50},{"Pencil",10,0.50},{"Folder",4,1.25}};
    for (size_t i = 0; i < sizeof items / sizeof items[0]; ++i) show_item(&items[i]);
    return 0;
}
```
Expected inventory values: $7.50, $5.00, and $5.00.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Notebook: quantity 3; value $7.50
Pencil: quantity 10; value $5.00
Folder: quantity 4; value $5.00
```
>>>>>>> 2067a20 (curriculum clearning and updates)
### Common Mistakes
- Passing an array without its count to a function.
- Using `.` on a pointer or `->` on a non-pointer object.
- Returning a pointer to a local record that no longer exists.

### Activities
1. Print all inventory items and calculate each quantity-times-price value.
2. Write a helper that receives a `const Item *` and explain the `->` operator.
3. Test the function with zero items and with all three inventory records.
4. Write a small test case that proves the collection count and capacity remain distinct and that all inventory fields stay associated.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Collection traversal" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
