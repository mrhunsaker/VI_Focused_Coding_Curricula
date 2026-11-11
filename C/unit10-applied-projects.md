# Unit 10: Applied Projects

## Overview

Apply C data structures, control flow, input validation, and state transitions to a text adventure and a command-line to-do manager. Prioritize explicit feedback, keyboard navigation, and safe handling of fixed-capacity data.

Prerequisite: Units 1–9. Learners should be able to build and test a small multi-function program.

## Lesson 10.1: Requirements and design

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Use top-down design to break an application into input, processing, storage, and output functions. Preserve the same requirements as the Python project: clear prompts, labeled output, confirmation messages, validation, and text-only operation. Write pseudocode and acceptance tests before coding.

### Worked Example
Design the to-do manager around the operations add task, view tasks, mark task complete, save tasks, load tasks, and quit. Define the task fields as `id`, `title`, `description`, `done`, and `created_at`. Specify the behavior for an empty list, an invalid task number, and a missing data file.

### Expected Behavior or Output

No program is run in this lesson. The expected result is a written design: the six operations, the five task fields, and the exact messages for an empty list, an invalid task number, and a missing data file.

### Common Mistakes
- Starting implementation without defining acceptance criteria and failure cases.
- Omitting empty-list, duplicate-ID, invalid-input, and unavailable-storage behavior.
- Selecting a persistence format without documenting its limitations.

### Activities
1. Write acceptance criteria for add, view, edit, delete, and save/load operations.
2. Define behavior for empty data, duplicate IDs, unknown IDs, and unavailable storage.
3. Draw a module plan separating input, validation, data operations, persistence, and output.
4. Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Requirements and design" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Represent rooms as records containing a room identifier, description, and exits. Track the current room by index or identifier. A movement command is valid only if the current room has an exit in that direction. Normalize commands consistently and always provide a textual description of the new location.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
typedef struct { const char *name; const char *description; int north, east, south, west; } Room;
int main(void)
{
    Room rooms[] = {
        {"start_room", "You are in a dimly lit cave. A passage leads NORTH.", 1, -1, -1, -1},
        {"tunnel", "The tunnel is damp and cold. You can go SOUTH or EAST.", -1, 2, 0, -1},
        {"clearing", "You are in a sunny clearing. A path leads WEST.", -1, -1, -1, 1}
    };
    int current = 0;
    printf("%s\n", rooms[current].description);
    current = rooms[current].north;
    printf("%s\n", rooms[current].description);
    return 0;
}
```
The first room leads north to the tunnel; the tunnel leads east to the clearing and south back to the cave. Extend this model with a command parser and a `quit` command. `-1` means that no exit exists in that direction.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
You are in a dimly lit cave. A passage leads NORTH.
The tunnel is damp and cold. You can go SOUTH or EAST.
```
### Common Mistakes
- Using a room exit index without checking that it is valid.
- Changing the current room before confirming the requested exit exists.
- Giving no feedback when a direction is blocked or unknown.

### Activities
1. Move north from the start room and verify the tunnel description.
2. Attempt west from the start room and verify that the room does not change.
3. Add case-insensitive direction commands and a quit command.
4. Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Text adventure: rooms and movement" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Extend the same cave-and-tunnel adventure with a shiny key, a player inventory, and a locked door. An item must be removed from the room when picked up and added to the inventory. The door unlocks only when the player is in the correct room and has the key. Keep command responses explicit.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    int key_in_room = 1, has_key = 0, door_locked = 1;
    char command[80];
    puts("A dark cave. There is a shiny key here.");
    printf("Command (take key): ");
    if (!fgets(command, sizeof command, stdin)) return 1;
    command[strcspn(command, "\n")] = '\0';
    if (strcmp(command, "take key") == 0 && key_in_room) {
        key_in_room = 0; has_key = 1; puts("You picked up the shiny key.");
    }
    if (has_key && door_locked) { door_locked = 0; puts("The key can unlock the door."); }
    return 0;
}
```
This is a small state-transition demonstration, not the complete game. Extend it with the same room movement rules from Lesson 10.2, then test taking the key twice, trying to unlock without the key, and using the key in the wrong room.

### Expected Behavior or Output

With these lines typed as standard input:
```text
take key
```

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
A dark cave. There is a shiny key here.
Command (take key): You picked up the shiny key.
The key can unlock the door.
```

### Common Mistakes
- Allowing the key to be collected more than once.
- Unlocking the door without checking both the inventory and the player's room.
- Updating item location and inventory inconsistently, duplicating or losing the key.

### Activities
1. Take the key and verify it leaves the room and enters inventory.
2. Try taking the key twice and verify the second attempt is rejected.
3. Test unlocking without the key and from the wrong room.
4. Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Text adventure: inventory and puzzles" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 10.4: Command-line to-do manager

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Build a command-line to-do tool with a menu loop and separate functions for adding, viewing, completing, saving, and loading tasks. Use the shared task fields and provide confirmations. C has no standard JSON support; for this project either choose a maintained JSON library and document its build instructions, or use a clearly documented simple text format while teaching JSON serialization separately in Lesson 8.5. Do not label a custom text format as JSON.

### Worked Example
```c
#include <stdio.h>
#include <string.h>
typedef struct { char title[80]; int done; } Task;
void show_tasks(const Task tasks[], size_t count)
{
    if (count == 0) { puts("No tasks in your list."); return; }
    for (size_t i = 0; i < count; ++i)
        printf("%zu. [%c] %s\n", i + 1, tasks[i].done ? 'X' : ' ', tasks[i].title);
}
int main(void)
{
    Task tasks[50] = {0}; size_t count = 0; char line[100];
    for (;;) {
        puts("1 Add task  2 View tasks  3 Quit");
        printf("Choice: ");
        if (!fgets(line, sizeof line, stdin)) break;
        if (line[0] == '1' && count < 50) {
            printf("Task title: ");
            if (!fgets(tasks[count].title, sizeof tasks[count].title, stdin)) break;
            tasks[count].title[strcspn(tasks[count].title, "\n")] = '\0';
            tasks[count++].done = 0; puts("Task added.");
        } else if (line[0] == '2') show_tasks(tasks, count);
        else if (line[0] == '3') break;
        else puts("Invalid choice.");
    }
    return 0;
}
```
This starter implements add, view, and quit with a fixed capacity of 50 tasks. Extend it with completion and persistence, checking every input and file operation.

### Expected Behavior or Output

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
1 Add task  2 View tasks  3 Quit
Choice: 
```
### Common Mistakes
- Writing beyond the fixed task array's capacity.
- Treating the first character of a menu line as fully validated input.
- Completing or deleting a task by index without checking the selected range.

### Activities
1. Add two tasks and view them in insertion order.
2. Complete a task by ID and reject an unknown ID.
3. Implement save/load and verify data remains after restarting.
4. Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Command-line to-do manager" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
## Lesson 10.5: Accessible UX and validation

### Reading References
- Official C language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain this concept using C terminology.
- Trace a short program and predict its behavior before execution.
- Modify and test the example independently.

### Concept Explanation
Accessible text interfaces use explicit prompts, consistent labels, predictable menu order, and clear confirmations. Validate all input before changing state. On errors, state what was wrong and how to correct it. Do not rely on color, position, or symbols alone to convey task status. For a screen-reader workflow, ensure output is announced in a useful sequence.

### Worked Example
```c
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    char line[80], *end;
    long age;
    for (;;) {
        printf("Enter your age as a positive whole number: ");
        if (!fgets(line, sizeof line, stdin)) return 1;
        age = strtol(line, &end, 10);
        if (end != line && age > 0) break;
        puts("Invalid age. Enter a whole number greater than zero.");
    }
    printf("You entered age: %ld\n", age);
    return 0;
}
```
The program repeats until it receives a positive integer. Improve it by rejecting trailing non-whitespace characters and checking `errno` for overflow.

### Expected Behavior or Output

With these lines typed as standard input:
```text
abc
-4
16
```

Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):

```text
Enter your age as a positive whole number: Invalid age. Enter a whole number greater than zero.
Enter your age as a positive whole number: Invalid age. Enter a whole number greater than zero.
Enter your age as a positive whole number: You entered age: 16
```

### Common Mistakes
- Using color or a symbol as the only indication of completion.
- Displaying an error without telling the user how to correct it.
- Silently truncating an overlong title or failing to announce a successful operation.

### Activities
1. Complete the menu workflow using keyboard only and read prompts sequentially.
2. Submit blank, overlong, and invalid menu input and verify corrective instructions.
3. Test with a named screen reader and OS; record observed results rather than assuming compatibility.
4. Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the C rule demonstrated by "Accessible UX and validation" without relying on Python terminology.
- [ ] I can predict and verify the exact behavior of this lesson's worked example.
- [ ] I can complete the lesson-specific boundary or extension tests above and explain the result.
- [ ] I can recognize the three C-specific failure modes listed in this lesson and apply a correction.
- [ ] I can navigate, compile, run, and inspect the source and output using my chosen access technology.
