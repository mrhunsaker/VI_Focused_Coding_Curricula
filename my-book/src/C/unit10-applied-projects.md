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
## Lesson 10.2: Text adventure: five rooms and movement

### Reading References
- C language standard library: stdio.h, string.h, and ctype.h.
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Represent all five canonical rooms with C records and integer room indexes.
- Validate movement before changing the current room.
- Explain why the treasure room is not reachable until the key puzzle is implemented.

### Concept Explanation

Use five fixed room indexes: start_room is 0, tunnel is 1, clearing is 2, locked_door_room is 3, and treasure_room is 4. Each exit stores a destination index or -1 when no exit exists. The graph is start north to tunnel; tunnel south to start and east to clearing; clearing west to tunnel and north to locked_door_room; and locked_door_room south to clearing. Part 1 deliberately has no north exit from locked_door_room.

The command loop reads a line, normalizes it to lowercase, checks the selected exit, and updates the current room only when the destination is valid. End-of-file acts like quit.

### Worked Example

```c
#include <ctype.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    const char *id;
    const char *description;
    int north, east, south, west;
} Room;

int main(void) {
    Room rooms[5] = {
        {"start_room", "A dimly lit cave. A narrow passage leads north.", 1, -1, -1, -1},
        {"tunnel", "A damp tunnel. Passages lead south and east.", -1, 2, 0, -1},
        {"clearing", "A quiet clearing. An antechamber lies to the north.", 3, -1, -1, 1},
        {"locked_door_room", "A chamber with a heavy door to the north.", -1, -1, 2, -1},
        {"treasure_room", "You found the treasure. You win!", -1, -1, -1, -1}
    };
    int current = 0;
    char command[80];

    for (;;) {
        printf("---\n%s\nWhat do you want to do?\n", rooms[current].description);
        if (!fgets(command, sizeof command, stdin)) strcpy(command, "quit");
        command[strcspn(command, "\r\n")] = '\0';
        for (size_t i = 0; command[i] != '\0'; ++i)
            command[i] = (char)tolower((unsigned char)command[i]);

        if (strcmp(command, "quit") == 0) {
            puts("Exiting game. Goodbye!");
            break;
        }

        int destination = -1;
        if (strcmp(command, "north") == 0) destination = rooms[current].north;
        else if (strcmp(command, "east") == 0) destination = rooms[current].east;
        else if (strcmp(command, "south") == 0) destination = rooms[current].south;
        else if (strcmp(command, "west") == 0) destination = rooms[current].west;

        if (destination >= 0 && destination < 5) current = destination;
        else puts("You cannot go that way. Enter a listed direction or quit.");
    }
    return 0;
}
```

### Expected Behavior or Output

Enter north, east, north, north, quit. The player reaches tunnel, clearing, and locked_door_room. The second north is rejected and the player remains in locked_door_room. The treasure room is present in the room table but has no incoming exit in Part 1.

### Common Mistakes
- Using -1 as an array index instead of checking it first.
- Updating the current room before validating the destination.
- Confusing a room index with the room's display name.
- Adding the treasure exit before the key puzzle is implemented.

### Activities
1. Trace north, east, north and record the room index after each command.
2. Try west from start_room and verify the current room does not change.
3. Verify every nonnegative exit index is between 0 and 4.
4. Explain why treasure_room is unreachable in Part 1.

### Accessibility Practice

Read the room description and prompt in order. The invalid-movement response explains what happened and how to continue. Compile and run from the terminal, then inspect output sequentially with the learner's access technology.

### Skills Checklist
- [ ] I can represent all five rooms with C records.
- [ ] I can represent missing exits with a sentinel value.
- [ ] I validate an exit before changing rooms.
- [ ] I can reject an invalid direction without changing state.
- [ ] I can explain why the treasure room is not yet reachable.

---

## Lesson 10.3: Text adventure: shiny key and locked door

### Reading References
- C language standard library: stdio.h, string.h, and ctype.h.
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Keep the shiny key in start_room until it is collected.
- Transfer the key to inventory exactly once.
- Require the player to use the key in locked_door_room before moving north to treasure_room.
- End the game after the player reaches treasure_room.

### Concept Explanation

Keep the five-room graph from Lesson 10.2. The shiny key begins in start_room. The take shiny key command changes key_in_room to false and has_key to true. The use shiny key command succeeds only when the player is in locked_door_room and has_key is true. North from locked_door_room is blocked while door_locked is true. Reaching treasure_room ends the game.

### Worked Example

```c
#include <ctype.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    const char *id;
    const char *description;
    int north, east, south, west;
} Room;

int main(void) {
    Room rooms[5] = {
        {"start_room", "A dimly lit cave.", 1, -1, -1, -1},
        {"tunnel", "A damp tunnel. Passages lead south and east.", -1, 2, 0, -1},
        {"clearing", "A quiet clearing. An antechamber lies to the north.", 3, -1, -1, 1},
        {"locked_door_room", "A chamber with a heavy door to the north.", 4, -1, 2, -1},
        {"treasure_room", "You found the treasure. You win!", -1, -1, -1, -1}
    };
    int current = 0, key_in_room = 1, has_key = 0, door_locked = 1;
    char command[80];

    for (;;) {
        printf("\n%s\n", rooms[current].description);
        if (current == 4) break;
        if (current == 0 && key_in_room) puts("You see: shiny key");
        puts(has_key ? "Your inventory: shiny key" : "Your inventory: empty");
        puts("What do you want to do?");
        if (!fgets(command, sizeof command, stdin)) strcpy(command, "quit");
        command[strcspn(command, "\r\n")] = '\0';
        for (size_t i = 0; command[i] != '\0'; ++i)
            command[i] = (char)tolower((unsigned char)command[i]);

        if (strcmp(command, "quit") == 0) {
            puts("You quit the adventure.");
            break;
        } else if (strcmp(command, "take shiny key") == 0) {
            if (current == 0 && key_in_room) {
                key_in_room = 0;
                has_key = 1;
                puts("You picked up the shiny key.");
            } else puts("There is no shiny key here to take.");
        } else if (strcmp(command, "use shiny key") == 0) {
            if (current != 3) puts("You must be at the locked door to use the key.");
            else if (!has_key) puts("You do not have the shiny key.");
            else {
                door_locked = 0;
                puts("You unlocked the door!");
            }
        } else if (current == 3 && strcmp(command, "north") == 0 && door_locked) {
            puts("The door is locked! You need to use the shiny key here.");
        } else {
            int destination = -1;
            if (strcmp(command, "north") == 0) destination = rooms[current].north;
            else if (strcmp(command, "east") == 0) destination = rooms[current].east;
            else if (strcmp(command, "south") == 0) destination = rooms[current].south;
            else if (strcmp(command, "west") == 0) destination = rooms[current].west;
            if (destination >= 0 && destination < 5) current = destination;
            else puts("Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.");
        }
    }
    return 0;
}
```

### Expected Behavior or Output

Enter north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north. The first north from locked_door_room is rejected. The key is removed from the room and added to inventory. Using it outside locked_door_room is rejected. Using it there unlocks the door; the final north reaches treasure_room and prints the win description. End-of-file acts like quit.

### Common Mistakes
- Allowing the key to be collected more than once.
- Unlocking the door without checking both room location and inventory.
- Allowing north movement before door_locked becomes false.
- Leaving the key listed in start_room after pickup.
- Treating a failed command as a state change.

### Activities
1. Run the full command sequence and record room, key location, inventory, and door state.
2. Try taking the key twice; the second attempt must be rejected.
3. Try using the key in start_room and clearing; both attempts must be rejected.
4. Try north from locked_door_room before and after unlocking.
5. Add a help command that lists every supported command.

### Accessibility Practice

Announce the room, visible item, inventory, and prompt as separate text lines. Every failed action explains why it failed. Test the full sequence with a screen reader and verify that item and door state are unambiguous.

### Skills Checklist
- [ ] I can implement the five-room graph.
- [ ] I can transfer the shiny key to inventory exactly once.
- [ ] I can require key use in the locked-door room.
- [ ] I can block and unlock the north exit.
- [ ] I can end the game in the treasure room.

---

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
