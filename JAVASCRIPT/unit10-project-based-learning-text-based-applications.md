# Unit 10: Project-Based Learning — Text-Based Applications

## Overview
The projects preserve the Python track's requirements and user interaction. The text adventure uses the shared five-room graph (`start_room`, `tunnel`, `clearing`, `locked_door_room`, and `treasure_room`) and the shiny-key puzzle. The command-line to-do manager supports add, view, complete, delete, and JSON persistence.

## Lesson 10.1: Designing Your Project

### Reading References
- Python source counterpart: Unit 10, Lesson 10.1.
- MDN: JavaScript modules and functions.

### Learning Objectives
- Apply top-down design to a multi-part program.
- Identify inputs, outputs, data, and edge cases.
- Write pseudocode and acceptance tests before implementation.

### Concept Explanation
Top-down design breaks a large task into smaller responsibilities. The project should have separate functions for input, state changes, display, and persistence. Define command names and error behavior before writing code.

### Worked Example
Text-adventure pseudocode:
```text
CREATE rooms and exits
PLACE items in selected rooms
CREATE player at starting room
REPEAT
  DISPLAY current room and player status
  READ command
  VALIDATE command
  APPLY movement or inventory action
UNTIL player enters quit
```

### Expected Behavior or Output
The learner produces pseudocode, a room/command specification, and acceptance tests before implementation.

### Common Mistakes
- Starting implementation before defining the project requirements.
- Combining input, state changes, and display in one large function.
- Omitting invalid-command and boundary cases.

### Activities
1. Draw or describe the five-room map in text.
2. List every valid movement command and its destination.
3. Define the to-do manager's five menu operations.
4. Write at least five acceptance tests before implementation.

### Accessibility Practice
Use keyboard-operable commands, descriptive prompts, and predictable text output. Do not require maps, color, drag-and-drop, or mouse-only interaction.

### Skills Checklist
- [ ] I can decompose a project into functions or modules.
- [ ] I can define inputs and outputs.
- [ ] I can write pseudocode.
- [ ] I can define acceptance tests and error cases.

## Lesson 10.2: Building a Text-Based Adventure Game (Part 1)

### Reading References
- Python source counterpart: Unit 10, Lesson 10.2.
- Node.js documentation: readline/promises.

### Learning Objectives
- Model the five canonical rooms and their exits.
- Move through connected rooms without changing state on invalid directions.
- Explain the locked north exit from locked_door_room.

### Shared Project Specification
Use the canonical five-room graph: start_room north to tunnel; tunnel south to start_room and east to clearing; clearing west to tunnel and north to locked_door_room; locked_door_room south to clearing and conditionally north to treasure_room after using shiny key. The player starts in start_room. Valid commands include north, south, east, west, take shiny key, use shiny key, and quit.

### Concept Explanation
A room is represented by its identifier, description, and a map of valid exits. Movement looks up the requested direction and changes the player's current room only when the exit exists.

### Worked Example
```javascript
const rooms = {
  start_room: { exits: { north: "tunnel" }, items: ["shiny key"] },
  tunnel: { exits: { south: "start_room", east: "clearing" }, items: [] },
  clearing: { exits: { west: "tunnel", north: "locked_door_room" }, items: [] },
  locked_door_room: { exits: { south: "clearing" }, items: [] },
  treasure_room: { exits: {}, items: [] }
};
function move(currentRoom, direction) {
  return rooms[currentRoom].exits[direction] ?? null;
}
console.log(move("start_room", "north"));
console.log(move("start_room", "west"));
```

Expected output:
```text
tunnel
null
```

### Expected Behavior or Output
Moving north from start_room returns tunnel. Moving west from start_room returns null; the locked-door north exit is added only after the key puzzle is solved.

### Common Mistakes
- Adding an exit in one direction but forgetting the reverse connection.
- Accepting an exit that does not exist.
- Confusing a room key with its display name.

### Activities
1. Build the five canonical rooms and their unconditional exits.
2. Test north from start_room, east from tunnel, and north from clearing.
3. Test an invalid movement without changing the current room.
4. Add the conditional north exit from locked_door_room only after the key is used.

### Accessibility Practice
Announce the current room, description, and available exits in a consistent order. Never make the map available only as a graphic.

### Skills Checklist
- [ ] I can represent rooms and exits as objects.
- [ ] I can move between connected rooms.
- [ ] I can reject invalid directions.
- [ ] I can display room information sequentially.

## Lesson 10.3: Building a Text-Based Adventure Game (Part 2)

### Reading References
- Python source counterpart: Unit 10, Lesson 10.3.
- MDN: Array methods and object methods.

### Learning Objectives
- Place shiny key in start_room and transfer it to inventory exactly once.
- Require the key to be used in locked_door_room.
- Unlock the conditional north exit to treasure_room.

### Shared Project Specification
Place only the shiny key in start_room. The player uses `take shiny key` and `use shiny key`. The key must be used while in locked_door_room; this unlocks its north exit to treasure_room. Preserve these item names and rules across language tracks.

### Concept Explanation
An item belongs either to a room or to the player's inventory. Picking it up removes it from the room and adds it to inventory as one state transition.

### Worked Example
```javascript
const rooms = {
  start_room: { exits: { north: "tunnel" } },
  tunnel: { exits: { south: "start_room", east: "clearing" } },
  clearing: { exits: { west: "tunnel", north: "locked_door_room" } },
  locked_door_room: { exits: { south: "clearing" } },
  treasure_room: { exits: {} }
};
const roomItems = { start_room: ["shiny key"], tunnel: [], clearing: [], locked_door_room: [], treasure_room: [] };
const inventory = [];
let doorLocked = true;
function takeItem(room, requestedName) {
  const items = roomItems[room];
  const index = items.findIndex(item => item.toLowerCase() === requestedName.toLowerCase());
  if (index < 0) return false;
  inventory.push(items.splice(index, 1)[0]);
  return true;
}
function useKey(room, items) {
  if (room !== "locked_door_room") return "You must be at the locked door to use the key.";
  if (!items.includes("shiny key")) return "The door is locked.";
  doorLocked = false;
  rooms.locked_door_room.exits.north = "treasure_room";
  return "The door unlocks; north now leads to treasure_room.";
}
console.log(takeItem("start_room", "shiny key"));
console.log(inventory.join(", "));
console.log(useKey("clearing", inventory));
console.log(useKey("locked_door_room", inventory));
console.log(doorLocked);
console.log(rooms.locked_door_room.exits.north);
```

Expected output:
```text
true
shiny key
You must be at the locked door to use the key.
The door unlocks; north now leads to treasure_room.
false
treasure_room
```

### Expected Behavior or Output
Taking shiny key from start_room returns true and inventory contains shiny key. Using it outside locked_door_room is rejected; using it there unlocks the north exit.

### Common Mistakes
- Allowing an item to be picked up repeatedly after it has been removed.
- Failing to normalize item names consistently.
- Updating the room but not the inventory, or vice versa.

### Activities
1. Take shiny key from start_room.
2. Attempt to take it a second time and verify inventory does not change.
3. Attempt to use the key outside locked_door_room.
4. Use the key in locked_door_room and verify the north exit leads to treasure_room.

### Accessibility Practice
Confirm each successful pickup by item name. When pickup fails, explain whether the item is absent or the command is invalid.

### Skills Checklist
- [ ] I can store items in rooms.
- [ ] I can transfer an item to inventory.
- [ ] I can display inventory contents.
- [ ] I can implement and test a puzzle condition.

## Lesson 10.4: Developing a Command-Line To-Do Tool

### Reading References
- Python source counterpart: Unit 10, Lesson 10.4.
- Node.js documentation: File system and readline.

### Learning Objectives
- Implement add, view, complete, delete, and quit operations.
- Validate a one-based task number.
- Persist task data in JSON.

### Concept Explanation

A command-line task manager separates data operations from prompts and display. Task numbers shown to users are one-based, while array indexes are zero-based.

#### Shared Project Specification

Each task has an identifier, description, completion state, and creation timestamp. The menu supports add task, view tasks, mark complete, delete, and quit. Save after every state-changing operation.

### Worked Example

Core task operations:
```javascript
function addTask(tasks, description, createdAt = new Date().toISOString()) {
  if (description.trim() === "") {
    throw new Error("Task description cannot be empty.");
  }
  tasks.push({
    id: tasks.length + 1,
    description: description.trim(),
    completed: false,
    createdAt
  });
}

function markComplete(tasks, taskNumber) {
  const index = taskNumber - 1;
  if (!Number.isInteger(taskNumber) || index < 0 || index >= tasks.length) {
    return false;
  }
  tasks[index].completed = true;
  return true;
}
```

### Expected Behavior or Output
A valid task description is added with completed false and a timestamp; a valid task number marks the corresponding task complete.

### Common Mistakes

- Confusing the user's one-based task number with a zero-based array index.
- Allowing empty descriptions.
- Saving only when the program exits, so an interrupted run loses changes.
- Reusing task identifiers after deletion without a documented policy.

### Activities
1. Add two tasks and view them in numbered order.
2. Mark the first task complete.
3. Delete the second task.
4. Save and reload the task list using JSON and verify the state persists.

### Accessibility Practice
Number every task and include an explicit completion label such as "complete" or "not complete". Confirm every add, update, and delete action in text.

### Skills Checklist

- [ ] I can add and display tasks.
- [ ] I can mark a task complete.
- [ ] I can delete a task by number.
- [ ] I can persist tasks as JSON.
- [ ] I can validate task descriptions and numbers.

## Lesson 10.5: Refinement and User Experience

### Reading References
- Python source counterpart: Unit 10, Lesson 10.5.
- Node.js documentation: Process exit codes and error handling.

### Learning Objectives
- Improve prompt clarity and validation.
- Test invalid commands and boundary cases.
- Review output for predictable keyboard and screen-reader use.

### Concept Explanation
A usable text program gives the same kind of response for the same kind of action. Prompts should state valid input, errors should explain the problem, and successful operations should confirm what changed. A help command should list every supported operation.

### Expected Behavior or Output
The refined application handles blank input, unknown commands, invalid record numbers, empty lists, and malformed stored data with explicit text messages.

### Worked Example
```javascript
function validateMenuChoice(choice) {
  const validChoices = ["add", "view", "search", "edit", "delete", "help", "quit"];
  if (!validChoices.includes(choice.trim().toLowerCase())) {
    return "Invalid choice. Enter add, view, search, edit, delete, help, or quit.";
  }
  return "Command accepted.";
}
console.log(validateMenuChoice("unknown"));
```

### Expected Behavior or Output

The refined application handles blank input, unknown commands, invalid record numbers, empty lists, and malformed stored data with explicit text messages.

### Common Mistakes

- Printing "Invalid input" without explaining valid choices.
- Failing to confirm a successful action.
- Letting malformed stored data crash the entire program.
- Relying on visual formatting without textual labels.

### Activities
1. Add a help command to the to-do tool.
2. Test blank input, unknown commands, invalid task numbers, and an empty task list.
3. Review every prompt for a clear expected input format.
4. Ask a partner to complete all tasks using keyboard navigation only and record obstacles.

### Accessibility Practice
Use consistent separators, descriptive prompts, explicit errors, and sequential output. Do not claim a screen-reader test unless it has actually been performed.

### Skills Checklist

- [ ] I can validate user input.
- [ ] I can provide specific error messages.
- [ ] I can confirm successful operations.
- [ ] I can review a CLI for keyboard and screen-reader usability.
