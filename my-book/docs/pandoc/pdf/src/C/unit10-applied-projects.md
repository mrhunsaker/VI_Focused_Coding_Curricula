[Header 2 ("unit-10-applied-projects", [], []) [Str "Unit 10: Applied Projects"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Apply C data structures, control flow, input validation, and state transitions to a text adventure and a command-line to-do manager. Prioritize explicit feedback, keyboard navigation, and safe handling of fixed-capacity data."], Para [Str "Prerequisite: Units 1–9. Learners should be able to build and test a small multi-function program."], Header 3 ("lesson-101-requirements-and-design", ["unnumbered", "unlisted"], []) [Str "Lesson 10.1: Requirements and design"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Official C language guide and standard-library documentation."]], [Plain [Str "Corresponding Python course lesson for the shared problem context and learning objective."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain this concept using C terminology."]], [Plain [Str "Trace a short program and predict its behavior before execution."]], [Plain [Str "Modify and test the example independently."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Use top-down design to break an application into input, processing, storage, and output functions. Preserve the same requirements as the Python project: clear prompts, labeled output, confirmation messages, validation, and text-only operation. Write pseudocode and acceptance tests before coding."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "Design the to-do manager around the operations add task, view tasks, mark task complete, save tasks, load tasks, and quit. Define the task fields as ", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "done", Str ", and ", Code ("", [], []) "created_at", Str ". Specify the behavior for an empty list, an invalid task number, and a missing data file."], Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "No program is run in this lesson. The expected result is a written design: the six operations, the five task fields, and the exact messages for an empty list, an invalid task number, and a missing data file."], Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Starting implementation without defining acceptance criteria and failure cases."]], [Plain [Str "Omitting empty-list, duplicate-ID, invalid-input, and unavailable-storage behavior."]], [Plain [Str "Selecting a persistence format without documenting its limitations."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write acceptance criteria for add, view, edit, delete, and save/load operations."]], [Plain [Str "Define behavior for empty data, duplicate IDs, unknown IDs, and unavailable storage."]], [Plain [Str "Draw a module plan separating input, validation, data operations, persistence, and output."]], [Plain [Str "Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the C rule demonstrated by \"Requirements and design\" without relying on Python terminology."]], [Plain [Str "\9744", Space, Str "I can predict and verify the exact behavior of this lesson's worked example."]], [Plain [Str "\9744", Space, Str "I can complete the lesson-specific boundary or extension tests above and explain the result."]], [Plain [Str "\9744", Space, Str "I can recognize the three C-specific failure modes listed in this lesson and apply a correction."]], [Plain [Str "\9744", Space, Str "I can navigate, compile, run, and inspect the source and output using my chosen access technology."]]], Header 3 ("lesson-102-text-adventure-five-rooms-and-movement", ["unnumbered", "unlisted"], []) [Str "Lesson 10.2: Text adventure: five rooms and movement"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "C language standard library: stdio.h, string.h, and ctype.h."]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Represent all five canonical rooms with C records and integer room indexes."]], [Plain [Str "Validate movement before changing the current room."]], [Plain [Str "Explain why the treasure room is not reachable until the key puzzle is implemented."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Use five fixed room indexes: start_room is 0, tunnel is 1, clearing is 2, locked_door_room is 3, and treasure_room is 4. Each exit stores a destination index or -1 when no exit exists. The graph is start north to tunnel; tunnel south to start and east to clearing; clearing west to tunnel and north to locked_door_room; and locked_door_room south to clearing. Part 1 deliberately has no north exit from locked_door_room."], Para [Str "The command loop reads a line, normalizes it to lowercase, checks the selected exit, and updates the current room only when the destination is valid. End-of-file acts like quit."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["c"], []) "#include <ctype.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    const char *id;
    const char *description;
    int north, east, south, west;
} Room;

int main(void) {
    Room rooms[5] = {
        {\"start_room\", \"A dimly lit cave. A narrow passage leads north.\", 1, -1, -1, -1},
        {\"tunnel\", \"A damp tunnel. Passages lead south and east.\", -1, 2, 0, -1},
        {\"clearing\", \"A quiet clearing. An antechamber lies to the north.\", 3, -1, -1, 1},
        {\"locked_door_room\", \"A chamber with a heavy door to the north.\", -1, -1, 2, -1},
        {\"treasure_room\", \"You found the treasure. You win!\", -1, -1, -1, -1}
    };
    int current = 0;
    char command[80];

    for (;;) {
        printf(\"---\\n%s\\nWhat do you want to do?\\n\", rooms[current].description);
        if (!fgets(command, sizeof command, stdin)) strcpy(command, \"quit\");
        command[strcspn(command, \"\\r\\n\")] = '\\0';
        for (size_t i = 0; command[i] != '\\0'; ++i)
            command[i] = (char)tolower((unsigned char)command[i]);

        if (strcmp(command, \"quit\") == 0) {
            puts(\"Exiting game. Goodbye!\");
            break;
        }

        int destination = -1;
        if (strcmp(command, \"north\") == 0) destination = rooms[current].north;
        else if (strcmp(command, \"east\") == 0) destination = rooms[current].east;
        else if (strcmp(command, \"south\") == 0) destination = rooms[current].south;
        else if (strcmp(command, \"west\") == 0) destination = rooms[current].west;

        if (destination >= 0 && destination < 5) current = destination;
        else puts(\"You cannot go that way. Enter a listed direction or quit.\");
    }
    return 0;
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Enter north, east, north, north, quit. The player reaches tunnel, clearing, and locked_door_room. The second north is rejected and the player remains in locked_door_room. The treasure room is present in the room table but has no incoming exit in Part 1."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Using -1 as an array index instead of checking it first."]], [Plain [Str "Updating the current room before validating the destination."]], [Plain [Str "Confusing a room index with the room's display name."]], [Plain [Str "Adding the treasure exit before the key puzzle is implemented."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace north, east, north and record the room index after each command."]], [Plain [Str "Try west from start_room and verify the current room does not change."]], [Plain [Str "Verify every nonnegative exit index is between 0 and 4."]], [Plain [Str "Explain why treasure_room is unreachable in Part 1."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the room description and prompt in order. The invalid-movement response explains what happened and how to continue. Compile and run from the terminal, then inspect output sequentially with the learner's access technology."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can represent all five rooms with C records."]], [Plain [Str "\9744", Space, Str "I can represent missing exits with a sentinel value."]], [Plain [Str "\9744", Space, Str "I validate an exit before changing rooms."]], [Plain [Str "\9744", Space, Str "I can reject an invalid direction without changing state."]], [Plain [Str "\9744", Space, Str "I can explain why the treasure room is not yet reachable."]]], HorizontalRule, Header 3 ("lesson-103-text-adventure-shiny-key-and-locked-door", ["unnumbered", "unlisted"], []) [Str "Lesson 10.3: Text adventure: shiny key and locked door"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "C language standard library: stdio.h, string.h, and ctype.h."]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Keep the shiny key in start_room until it is collected."]], [Plain [Str "Transfer the key to inventory exactly once."]], [Plain [Str "Require the player to use the key in locked_door_room before moving north to treasure_room."]], [Plain [Str "End the game after the player reaches treasure_room."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Keep the five-room graph from Lesson 10.2. The shiny key begins in start_room. The take shiny key command changes key_in_room to false and has_key to true. The use shiny key command succeeds only when the player is in locked_door_room and has_key is true. North from locked_door_room is blocked while door_locked is true. Reaching treasure_room ends the game."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["c"], []) "#include <ctype.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    const char *id;
    const char *description;
    int north, east, south, west;
} Room;

int main(void) {
    Room rooms[5] = {
        {\"start_room\", \"A dimly lit cave.\", 1, -1, -1, -1},
        {\"tunnel\", \"A damp tunnel. Passages lead south and east.\", -1, 2, 0, -1},
        {\"clearing\", \"A quiet clearing. An antechamber lies to the north.\", 3, -1, -1, 1},
        {\"locked_door_room\", \"A chamber with a heavy door to the north.\", 4, -1, 2, -1},
        {\"treasure_room\", \"You found the treasure. You win!\", -1, -1, -1, -1}
    };
    int current = 0, key_in_room = 1, has_key = 0, door_locked = 1;
    char command[80];

    for (;;) {
        printf(\"\\n%s\\n\", rooms[current].description);
        if (current == 4) break;
        if (current == 0 && key_in_room) puts(\"You see: shiny key\");
        puts(has_key ? \"Your inventory: shiny key\" : \"Your inventory: empty\");
        puts(\"What do you want to do?\");
        if (!fgets(command, sizeof command, stdin)) strcpy(command, \"quit\");
        command[strcspn(command, \"\\r\\n\")] = '\\0';
        for (size_t i = 0; command[i] != '\\0'; ++i)
            command[i] = (char)tolower((unsigned char)command[i]);

        if (strcmp(command, \"quit\") == 0) {
            puts(\"You quit the adventure.\");
            break;
        } else if (strcmp(command, \"take shiny key\") == 0) {
            if (current == 0 && key_in_room) {
                key_in_room = 0;
                has_key = 1;
                puts(\"You picked up the shiny key.\");
            } else puts(\"There is no shiny key here to take.\");
        } else if (strcmp(command, \"use shiny key\") == 0) {
            if (current != 3) puts(\"You must be at the locked door to use the key.\");
            else if (!has_key) puts(\"You do not have the shiny key.\");
            else {
                door_locked = 0;
                puts(\"You unlocked the door!\");
            }
        } else if (current == 3 && strcmp(command, \"north\") == 0 && door_locked) {
            puts(\"The door is locked! You need to use the shiny key here.\");
        } else {
            int destination = -1;
            if (strcmp(command, \"north\") == 0) destination = rooms[current].north;
            else if (strcmp(command, \"east\") == 0) destination = rooms[current].east;
            else if (strcmp(command, \"south\") == 0) destination = rooms[current].south;
            else if (strcmp(command, \"west\") == 0) destination = rooms[current].west;
            if (destination >= 0 && destination < 5) current = destination;
            else puts(\"Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.\");
        }
    }
    return 0;
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Enter north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north. The first north from locked_door_room is rejected. The key is removed from the room and added to inventory. Using it outside locked_door_room is rejected. Using it there unlocks the door; the final north reaches treasure_room and prints the win description. End-of-file acts like quit."], Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Allowing the key to be collected more than once."]], [Plain [Str "Unlocking the door without checking both room location and inventory."]], [Plain [Str "Allowing north movement before door_locked becomes false."]], [Plain [Str "Leaving the key listed in start_room after pickup."]], [Plain [Str "Treating a failed command as a state change."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the full command sequence and record room, key location, inventory, and door state."]], [Plain [Str "Try taking the key twice; the second attempt must be rejected."]], [Plain [Str "Try using the key in start_room and clearing; both attempts must be rejected."]], [Plain [Str "Try north from locked_door_room before and after unlocking."]], [Plain [Str "Add a help command that lists every supported command."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Announce the room, visible item, inventory, and prompt as separate text lines. Every failed action explains why it failed. Test the full sequence with a screen reader and verify that item and door state are unambiguous."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can implement the five-room graph."]], [Plain [Str "\9744", Space, Str "I can transfer the shiny key to inventory exactly once."]], [Plain [Str "\9744", Space, Str "I can require key use in the locked-door room."]], [Plain [Str "\9744", Space, Str "I can block and unlock the north exit."]], [Plain [Str "\9744", Space, Str "I can end the game in the treasure room."]]], HorizontalRule, Header 3 ("lesson-104-command-line-to-do-manager", ["unnumbered", "unlisted"], []) [Str "Lesson 10.4: Command-line to-do manager"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Official C language guide and standard-library documentation."]], [Plain [Str "Corresponding Python course lesson for the shared problem context and learning objective."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain this concept using C terminology."]], [Plain [Str "Trace a short program and predict its behavior before execution."]], [Plain [Str "Modify and test the example independently."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Build a command-line to-do tool with a menu loop and separate functions for adding, viewing, completing, saving, and loading tasks. Use the shared task fields and provide confirmations. C has no standard JSON support; for this project either choose a maintained JSON library and document its build instructions, or use a clearly documented simple text format while teaching JSON serialization separately in Lesson 8.5. Do not label a custom text format as JSON."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["c"], []) "#include <stdio.h>
#include <string.h>
typedef struct { char title[80]; int done; } Task;
void show_tasks(const Task tasks[], size_t count)
{
    if (count == 0) { puts(\"No tasks in your list.\"); return; }
    for (size_t i = 0; i < count; ++i)
        printf(\"%zu. [%c] %s\\n\", i + 1, tasks[i].done ? 'X' : ' ', tasks[i].title);
}
int main(void)
{
    Task tasks[50] = {0}; size_t count = 0; char line[100];
    for (;;) {
        puts(\"1 Add task  2 View tasks  3 Quit\");
        printf(\"Choice: \");
        if (!fgets(line, sizeof line, stdin)) break;
        if (line[0] == '1' && count < 50) {
            printf(\"Task title: \");
            if (!fgets(tasks[count].title, sizeof tasks[count].title, stdin)) break;
            tasks[count].title[strcspn(tasks[count].title, \"\\n\")] = '\\0';
            tasks[count++].done = 0; puts(\"Task added.\");
        } else if (line[0] == '2') show_tasks(tasks, count);
        else if (line[0] == '3') break;
        else puts(\"Invalid choice.\");
    }
    return 0;
}
", Para [Str "This starter implements add, view, and quit with a fixed capacity of 50 tasks. Extend it with completion and persistence, checking every input and file operation."], Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):"], CodeBlock ("", ["text"], []) "1 Add task  2 View tasks  3 Quit
Choice: 
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Writing beyond the fixed task array's capacity."]], [Plain [Str "Treating the first character of a menu line as fully validated input."]], [Plain [Str "Completing or deleting a task by index without checking the selected range."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Add two tasks and view them in insertion order."]], [Plain [Str "Complete a task by ID and reject an unknown ID."]], [Plain [Str "Implement save/load and verify data remains after restarting."]], [Plain [Str "Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the C rule demonstrated by \"Command-line to-do manager\" without relying on Python terminology."]], [Plain [Str "\9744", Space, Str "I can predict and verify the exact behavior of this lesson's worked example."]], [Plain [Str "\9744", Space, Str "I can complete the lesson-specific boundary or extension tests above and explain the result."]], [Plain [Str "\9744", Space, Str "I can recognize the three C-specific failure modes listed in this lesson and apply a correction."]], [Plain [Str "\9744", Space, Str "I can navigate, compile, run, and inspect the source and output using my chosen access technology."]]], Header 3 ("lesson-105-accessible-ux-and-validation", ["unnumbered", "unlisted"], []) [Str "Lesson 10.5: Accessible UX and validation"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Official C language guide and standard-library documentation."]], [Plain [Str "Corresponding Python course lesson for the shared problem context and learning objective."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain this concept using C terminology."]], [Plain [Str "Trace a short program and predict its behavior before execution."]], [Plain [Str "Modify and test the example independently."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Accessible text interfaces use explicit prompts, consistent labels, predictable menu order, and clear confirmations. Validate all input before changing state. On errors, state what was wrong and how to correct it. Do not rely on color, position, or symbols alone to convey task status. For a screen-reader workflow, ensure output is announced in a useful sequence."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["c"], []) "#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    char line[80], *end;
    long age;
    for (;;) {
        printf(\"Enter your age as a positive whole number: \");
        if (!fgets(line, sizeof line, stdin)) return 1;
        age = strtol(line, &end, 10);
        if (end != line && age > 0) break;
        puts(\"Invalid age. Enter a whole number greater than zero.\");
    }
    printf(\"You entered age: %ld\\n\", age);
    return 0;
}
", Para [Str "The program repeats until it receives a positive integer. Improve it by rejecting trailing non-whitespace characters and checking ", Code ("", [], []) "errno", Str " for overflow."], Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With these lines typed as standard input:"], CodeBlock ("", ["text"], []) "abc
-4
16
", Para [Str "Output observed when the worked example was run (gcc 13.3, C17; the text of the output does not depend on the operating system):"], CodeBlock ("", ["text"], []) "Enter your age as a positive whole number: Invalid age. Enter a whole number greater than zero.
Enter your age as a positive whole number: Invalid age. Enter a whole number greater than zero.
Enter your age as a positive whole number: You entered age: 16
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Using color or a symbol as the only indication of completion."]], [Plain [Str "Displaying an error without telling the user how to correct it."]], [Plain [Str "Silently truncating an overlong title or failing to announce a successful operation."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Complete the menu workflow using keyboard only and read prompts sequentially."]], [Plain [Str "Submit blank, overlong, and invalid menu input and verify corrective instructions."]], [Plain [Str "Test with a named screen reader and OS; record observed results rather than assuming compatibility."]], [Plain [Str "Write an acceptance test with the initial project state, user action, expected response, and unchanged state after a rejected action."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the C rule demonstrated by \"Accessible UX and validation\" without relying on Python terminology."]], [Plain [Str "\9744", Space, Str "I can predict and verify the exact behavior of this lesson's worked example."]], [Plain [Str "\9744", Space, Str "I can complete the lesson-specific boundary or extension tests above and explain the result."]], [Plain [Str "\9744", Space, Str "I can recognize the three C-specific failure modes listed in this lesson and apply a correction."]], [Plain [Str "\9744", Space, Str "I can navigate, compile, run, and inspect the source and output using my chosen access technology."]]]]