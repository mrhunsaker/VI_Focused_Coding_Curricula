# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

Design, build, and refine equivalent command-line projects. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.
## Lesson 10.1: Designing a text-based project

### Reading References
- Python source counterpart: Unit 10 lesson 10.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Plan requirements, data structures, commands, and acceptance tests before implementation.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Top-down design decomposes a project into smaller responsibilities. For an accessible terminal project, define prompts, commands, textual feedback, invalid-input behavior, and a quit path before coding.

### Worked Example
```typescript
const requirements = ["list rooms", "move by direction", "take item", "view inventory", "quit"];
for (const requirement of requirements) console.log(`Requirement: ${requirement}`);
```

### Expected Behavior or Output
Five requirements are printed in a stable order.

### Common Mistakes
- Starting implementation before writing acceptance criteria.
- Designing a visual-only interaction for a text-based project.
- Omitting error and quit behavior.

### Activities
1. Write the project requirements in plain language.
2. Identify input, state, and output for each command.
3. Write at least five acceptance tests before implementation.

### Accessibility Practice
Use a numbered text specification and test keyboard-only interaction. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can decompose a project.
- [ ] I can define commands and data.
- [ ] I can write acceptance tests before coding.

---

---

## Lesson 10.2: Text adventure part 1: rooms and movement

### Reading References
- Python source counterpart: Unit 10 lesson 10.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Model the five canonical rooms with typed exits and movement.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A room has an identifier, description, and exits. A movement operation changes the current room only when the requested exit exists. A Record type can model a fixed set of room identifiers.

### Worked Example
```typescript
type RoomId = "start_room" | "tunnel" | "clearing" | "locked_door_room" | "treasure_room";
const exits: Record<RoomId, Partial<Record<string, RoomId>>> = {
  start_room: { north: "tunnel" },
  tunnel: { south: "start_room", east: "clearing" },
  clearing: { west: "tunnel", north: "locked_door_room" },
  locked_door_room: { south: "clearing" },
  treasure_room: {}
};
function move(room: RoomId, direction: string): RoomId | null {
  return exits[room][direction.toLowerCase()] ?? null;
}
console.log(move("start_room", "north"));
console.log(move("start_room", "west"));
```

### Expected Behavior or Output
Moving north from start_room returns tunnel; moving west returns null. The north exit from locked_door_room is conditional on using shiny key.

### Common Mistakes
- Allowing movement through an exit that is not defined.
- Changing the room before validating the direction.
- Using arbitrary strings where a RoomId union is safer.

### Activities
1. Create all five canonical rooms and unconditional exits.
2. Move north from start_room and east from tunnel.
3. Attempt an invalid direction and report the result.
4. Add the conditional locked_door_room north exit only after the key is used.

### Accessibility Practice
Announce current room and available exits as labeled text. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model rooms and exits.
- [ ] I can use a union type for room identifiers.
- [ ] I can validate movement.

---

---

## Lesson 10.3: Text adventure part 2: items, inventory, and puzzle

### Reading References
- Python source counterpart: Unit 10 lesson 10.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement pickup of shiny key from start_room and the conditional locked-door puzzle.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
An item moves from one room to inventory as one state transition. The shiny key moves from start_room to inventory as one state transition. The player must use it in locked_door_room to unlock the north exit to treasure_room.

### Worked Example
```typescript
type RoomId = "start_room" | "tunnel" | "clearing" | "locked_door_room" | "treasure_room";
type Direction = "north" | "south" | "east" | "west";
const exits: Record<RoomId, Partial<Record<Direction, RoomId>>> = {
  start_room: { north: "tunnel" },
  tunnel: { south: "start_room", east: "clearing" },
  clearing: { west: "tunnel", north: "locked_door_room" },
  locked_door_room: { south: "clearing" },
  treasure_room: {}
};
const roomItems: Record<RoomId, string[]> = {
  start_room: ["shiny key"], tunnel: [], clearing: [], locked_door_room: [], treasure_room: []
};
const inventory: string[] = [];
let doorLocked = true;

function takeItem(room: RoomId, item: string): boolean {
  const items = roomItems[room];
  const index = items.findIndex(value => value.toLowerCase() === item.toLowerCase());
  if (index < 0) return false;
  inventory.push(items.splice(index, 1)[0]);
  return true;
}
function useKey(room: RoomId): string {
  if (room !== "locked_door_room") return "You must be at the locked door to use the key.";
  if (!inventory.includes("shiny key")) return "The door is locked.";
  doorLocked = false;
  exits.locked_door_room.north = "treasure_room";
  return "The door unlocks.";
}
console.log(takeItem("start_room", "shiny key"));
console.log(inventory.join(", "));
console.log(useKey("clearing"));
console.log(useKey("locked_door_room"));
console.log(doorLocked);
console.log(exits.locked_door_room.north);
```

### Expected Behavior or Output
The example prints the pickup result, inventory contents, a location error, the successful unlock message, the door state, and the newly available north exit:

```text
true
shiny key
You must be at the locked door to use the key.
The door unlocks.
false
treasure_room
```

### Common Mistakes
- Allowing the same item to be collected repeatedly.
- Updating inventory without removing the room item.
- Checking for the wrong key name or case.

### Activities
1. Take shiny key from start_room.
2. Attempt to take it twice and verify duplicate pickup is rejected.
3. Attempt to use the key outside locked_door_room.
4. Use the key in locked_door_room and verify the north exit is unlocked.

### Accessibility Practice
Confirm each pickup by item name and state whether the puzzle is locked or open. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can transfer an item into inventory.
- [ ] I can prevent duplicate pickup.
- [ ] I can implement the shiny-key puzzle: move the key from `start_room` to inventory, require its use in `locked_door_room`, and unlock the north exit to `treasure_room`.

---

---

## Lesson 10.4: Developing a command-line to-do tool

### Reading References
- Python source counterpart: Unit 10 lesson 10.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Implement add, view, complete, delete, and quit operations with typed tasks.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A task has an id, title, description, done state, and creation timestamp. User-facing task numbers are one-based; array indexes are zero-based. Persist after every state-changing operation.

### Worked Example
```typescript
interface Todo { id: number; title: string; description: string; done: boolean; created_at: string }
const tasks: Todo[] = [];
function addTask(title: string, description: string): Todo {
  const task: Todo = { id: tasks.length + 1, title, description, done: false, created_at: new Date().toISOString() };
  tasks.push(task);
  return task;
}
console.log(addTask("Review arrays", "Practice typed collection methods").done);
```

### Expected Behavior or Output
A new task is added with done false and an ISO timestamp.

### Common Mistakes
- Using an array index as a permanent identifier.
- Failing to save after a state change.
- Accepting a blank task title.

### Activities
1. Add a task and view it.
2. Mark a task complete and delete another.
3. Persist and reload the task array as JSON.

### Accessibility Practice
Use one task per output block with field labels and a clear confirmation. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model a typed task.
- [ ] I can implement task creation.
- [ ] I can identify persistence points.

---

---

## Lesson 10.5: Refinement and accessible text user experience

### Reading References
- Python source counterpart: Unit 10 lesson 10.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Improve validation, prompts, error messages, and recovery paths.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A usable terminal interface has explicit prompts, predictable output, help text, and recoverable errors. A robust program validates untrusted values before changing state.

### Worked Example
```typescript
function normalizeCommand(input: string): string {
  return input.trim().toLowerCase();
}
function validateTitle(input: string): string | null {
  const title = input.trim();
  return title.length === 0 ? "Title cannot be blank." : null;
}
console.log(normalizeCommand("  VIEW "));
console.log(validateTitle("   "));
```

### Expected Behavior or Output
The output is view and Title cannot be blank.

### Common Mistakes
- Providing vague messages such as invalid input without a recovery hint.
- Using color as the only status indicator.
- Failing to test blank input, unknown commands, and empty collections.

### Activities
1. Add a help command.
2. Test blank, malformed, and unknown commands.
3. Review every message in sequential screen-reader output.

### Accessibility Practice
Provide text equivalents for every status and avoid cursor-position-dependent instructions. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can normalize command input.
- [ ] I can validate required fields.
- [ ] I can review a text interface for accessibility.
