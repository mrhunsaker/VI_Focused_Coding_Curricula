# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 10.1 Project Design and Requirements

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Translate requirements into data structures, commands, and acceptance tests before coding. This room graph is the common adventure map.

### Worked Example

```lua
local rooms = {
  start_room = {exits = {north = "tunnel"}, items = {"shiny key"}},
  tunnel = {exits = {south = "start_room", east = "clearing"}, items = {}},
  clearing = {exits = {west = "tunnel", north = "locked_door_room"}, items = {}},
  locked_door_room = {exits = {south = "clearing", north = "treasure_room"}, items = {}},
  treasure_room = {exits = {}, items = {}}
}
print(rooms.tunnel.exits.east)
```

### Expected Behavior or Output

```text
clearing
```

### Common Mistakes

- Dropping one of the six required capstone record fields during serialization.
- Updating a record without refreshing updated_at.
- Claiming screen-reader compatibility without testing keyboard and assistive-technology workflows.

### Activities

1. Create a record containing all six canonical capstone fields and validate each field.
2. Exercise add, list, search, update, and delete with both existing and missing IDs.
3. Save and reload a record; compare every field before and after persistence.
4. Write a text-only keyboard interaction guide and list the accessibility tests still required.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 10.2 Adventure Game: Rooms and Movement

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Represent each room by a record containing description and exits. Reject movement when an exit is absent.

### Worked Example

```lua
local rooms = {
  start_room = {description = "Cave", exits = {north = "tunnel"}},
  tunnel = {description = "Tunnel", exits = {south = "start_room", east = "clearing"}},
  clearing = {description = "Clearing", exits = {west = "tunnel", north = "locked_door_room"}},
  locked_door_room = {description = "Antechamber", exits = {south = "clearing", north = "treasure_room"}},
  treasure_room = {description = "Treasure", exits = {}}
}
local current = "start_room"
local command = "north"
current = rooms[current].exits[command] or current
print(current, rooms[current].description)
```

### Expected Behavior or Output

```text
tunnel	Tunnel
```

### Common Mistakes

- Accepting a movement command that is not an exit from the current room.
- Removing an item before confirming it exists in the current room.
- Allowing the locked-door transition without checking both location and key possession.

### Activities

1. Trace movement from start_room to tunnel to clearing and back using only defined exits.
2. Attempt an invalid direction and confirm that the current room does not change.
3. Pick up the shiny key, inspect inventory, and verify it is removed from the room.
4. Attempt the puzzle without the key and then with the key; verify the win condition.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 10.3 Adventure Game: Inventory and Puzzle

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Inventory is a sequence table; room items are sequences too. A puzzle must check both player location and possession of the required item.

### Worked Example

```lua
local rooms = {
  start_room = {exits = {north = "tunnel"}, items = {"shiny key"}},
  tunnel = {exits = {south = "start_room", east = "clearing"}, items = {}},
  clearing = {exits = {west = "tunnel", north = "locked_door_room"}, items = {}},
  locked_door_room = {exits = {south = "clearing", north = "treasure_room"}, items = {}},
  treasure_room = {exits = {}, items = {}}
}
local current_room = "start_room"
local inventory = {}
local door_locked = true

local function take_key()
  local items = rooms[current_room].items
  for index, item in ipairs(items) do
    if item == "shiny key" then
      inventory[#inventory + 1] = item
      table.remove(items, index)
      return true
    end
  end
  return false
end

local function move(direction)
  if current_room == "locked_door_room" and direction == "north" and door_locked then
    print("The door is locked.")
    return
  end
  local destination = rooms[current_room].exits[direction]
  if destination then
    current_room = destination
    print("Current room:", current_room)
  else
    print("You cannot go that way.")
  end
end

local function use_key()
  if current_room == "locked_door_room" then
    for _, item in ipairs(inventory) do
      if item == "shiny key" then
        door_locked = false
        print("Door unlocked:", not door_locked)
        return true
      end
    end
  end
  print("The key cannot be used here.")
  return false
end

print("Picked up key:", take_key())
move("north")
move("east")
move("north")
move("north")
use_key()
move("north")
print("You win:", current_room == "treasure_room")
```

### Expected Behavior or Output

```text
Picked up key:	true
Current room:	tunnel
Current room:	clearing
Current room:	locked_door_room
The door is locked.
Door unlocked:	true
Current room:	treasure_room
You win:	true
```

### Common Mistakes

- Treating a Lua table map as if it had a guaranteed iteration order.
- Confusing a missing key (nil) with a key whose value is false.
- Using the sequence length operator to count named inventory keys.

### Activities

1. Represent Notebook, Pencil, and Folder with name, quantity, and unit_price fields.
2. Calculate each line value and verify the shared inventory total of $17.50.
3. Add a missing-item lookup and print a clear message when the key is absent.
4. Sort a separate list of item names before displaying map values in deterministic order.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 10.4 Command-Line To-Do Manager

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

The task record must include id, title, description, done, and created_at. Keep CRUD operations separate from the input loop.

### Worked Example

```lua
local tasks = {}
local function add_task(id, title, description, created_at)
  assert(title ~= nil and title ~= "", "title is required")
  tasks[#tasks + 1] = {id = id, title = title, description = description,
    done = false, created_at = created_at}
end
add_task(1, "Practice Lua", "Complete the shared examples", "2025-01-15T09:00:00Z")
print(tasks[1].id, tasks[1].title, tasks[1].done)
```

### Expected Behavior or Output

```text
1	Practice Lua	false
```

### Common Mistakes

- Omitting one or more required task fields from a stored record.
- Using a list position as a permanent task identifier after deletion or reordering.
- Treating malformed persistence data as an empty task list without reporting the error.

### Activities

1. Create a task with all five canonical fields and list it in a stable format.
2. Update its done state, then search for it by identifier.
3. Delete an existing ID and attempt to delete a missing ID; compare the messages.
4. Save and reload the records, then verify every field is preserved.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 10.5 Refinement and Accessibility

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

A command-line application needs explicit help, validation, confirmations, and readable errors. Keep all critical information in text.

### Worked Example

```lua
local function validate_title(title)
  if title == nil or title:match("^%s*$") then
    return false, "Title is required; enter at least one non-space character."
  end
  return true, "Title accepted."
end
local ok, message = validate_title("   ")
print(message)
```

### Expected Behavior or Output

```text
Title is required; enter at least one non-space character.
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 10.5 Refinement and Accessibility worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 10.5 refinement and accessibility.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Overview

Plan a text project, build the shared text adventure in two parts, build the command-line to-do manager, and refine input validation.

## Lesson 10.1: Planning a Text-Based Project

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions) and Chapter 5 (Tables)
- Lua 5.4 Reference Manual: Section 3.3 (Statements)
- Matching Python lesson: Lesson 10.1 Project Planning and Design

### Learning Objectives
- Write a short requirements list.
- Design a command loop with a table of handlers.
- Plan in small steps and test each one.

### Concept Explanation
A project is easier to finish when you plan it in small steps. Write down *what the program must do* (requirements), *what information it keeps* (data), and *the commands a person can give* (interface). Build one small piece, test it, and then add the next.

Text-based projects share a *command loop*: show a prompt, read a line, find the matching action, and repeat until the user quits. A good Lua design stores actions in a table whose keys are command names and whose values are functions. A new command is then one new entry, and an unknown command is a failed lookup that prints a helpful message.

The loop must stop when the input ends (`nil`) as well as on `quit`.

The example is a skeleton with three commands. Typing `help`, `look`, an unknown word, and `quit` shows each path.

### Worked Example
```lua
local commands = {
  help = function() print("Commands: help, look, quit") end,
  look = function() print("You are in a dark cave.") end,
}

print("Type a command:")
local line = io.read()
while line ~= nil and line ~= "quit" do
  local handler = commands[line]
  if handler then
    handler()
  else
    print("I don't understand that command. Type help for a list.")
  end
  print("Type a command:")
  line = io.read()
end
print("Goodbye!")
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
help
look
dance
quit
```

the program prints:
```text
Type a command:
Commands: help, look, quit
Type a command:
You are in a dark cave.
Type a command:
I don't understand that command. Type help for a list.
Type a command:
Goodbye!
```

### Common Mistakes
1. Starting to code before listing the requirements.
2. Using a long chain of `if` statements for commands instead of a table of handlers.
3. Forgetting that an unknown command should explain what to do next.

### Activities
1. Write five requirements for the text adventure and the to-do list.
2. Add a `score` command that prints the shared scores.
3. Add the command aliases `h` and `l` without copying the functions.
4. Describe the data for the capstone in three sentences.

### Accessibility Practice
Prompts and responses are on separate lines and every response is a complete sentence. Test the prompts by listening to them before you add features.

### Skills Checklist
- [ ] I can list requirements.
- [ ] I can design a command loop.
- [ ] I can use a table of handlers.
- [ ] I handle unknown commands.
- [ ] I handle the end of input.

## Lesson 10.2: Text Adventure, Part 1: Rooms and Movement

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables)
- Lua 5.4 Reference Manual: Section 3.4.9 (Table Constructors)
- Matching Python lesson: Lesson 10.2 Building a Text-Based Adventure Game (Part 1)

### Learning Objectives
- Represent rooms and exits with tables.
- Move the player by command.
- Handle impossible moves and the end of input.

### Concept Explanation
A room is a table with a `description` and an `exits` table that maps a direction to the name of another room. The program remembers the player's location in one variable, `current_room`. A move looks up the command in the current room's exits; if it is found, `current_room` changes, otherwise the program explains that the move is impossible.

This is the same three-room layout as the Python course: a cave, a tunnel, and a clearing. Part 2 adds items and a locked door.

The example is played with the commands north, east, west, up, south, and quit. The command `up` is not an exit anywhere, so it prints the help message.

### Worked Example
```lua
local rooms = {
  start_room = {
    description = "You are in a dimly lit cave. There's a narrow passage to the NORTH.",
    exits = {north = "tunnel"},
  },
  tunnel = {
    description = "The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.",
    exits = {south = "start_room", east = "clearing"},
  },
  clearing = {
    description = "You've reached a small, sunny clearing. A faint path leads WEST.",
    exits = {west = "tunnel"},
  },
}

local current_room = "start_room"

while true do
  print("---")
  print(rooms[current_room].description)
  print("What do you want to do?")
  local command = io.read()
  if command == nil then command = "quit" end
  command = command:lower()

  if rooms[current_room].exits[command] then
    current_room = rooms[current_room].exits[command]
  elseif command == "quit" then
    print("Exiting game. Goodbye!")
    break
  else
    print("I don't understand that command or you can't go that way.")
  end
end
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
north
east
west
up
south
quit
```

the program prints:
```text
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You've reached a small, sunny clearing. A faint path leads WEST.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
I don't understand that command or you can't go that way.
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Looking up a direction that is not in `exits` and expecting an error. The lookup returns `nil`, which is the signal to explain the move is impossible.
2. Forgetting to treat the end of input as `quit`, so the program loops forever when input is piped in.
3. Misspelling a room name in `exits`, so the move leads to a room that does not exist.

### Activities
1. Trace the six commands by hand and write the room after each one.
2. Add a fourth room reached from the clearing and test it.
3. Add the aliases `n`, `s`, `e`, and `w`.
4. Check that every exit names a real room by writing a loop that tests the whole table.

### Accessibility Practice
Each turn prints a separator line, the description, and the prompt on its own line. Listen to a whole turn to confirm that a player could follow it without seeing the screen.

### Skills Checklist
- [ ] I can represent rooms with tables.
- [ ] I can move the player by command.
- [ ] I can handle an impossible move.
- [ ] I treat end of input as quit.
- [ ] I can trace a game by hand.

## Lesson 10.3: Text Adventure, Part 2: Items and a Locked Door

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables) and Chapter 6 (Functions)
- Lua 5.4 Reference Manual: Section 6.6 (Table Manipulation)
- Matching Python lesson: Lesson 10.3 Building a Text-Based Adventure Game (Part 2)

### Learning Objectives
- Keep items in rooms and in an inventory.
- Implement take and use commands.
- Block and then allow a move with a locked door.

### Concept Explanation
Part 2 adds *state*: items in rooms, an inventory, and a door that is locked until the player uses the key. This is the shared specification used by every language track: three rooms (`start`, `locked_door_room`, `treasure_room`); the commands `north`, `south`, `east`, `west`, `take shiny key`, `use shiny key`, and `quit`; the door between the chamber and the treasure room stays locked until the key is used there; reaching the treasure room ends the game.

Items are lists of names. Taking an item removes it from the room's list and appends it to the inventory. The locked door is a Boolean variable, `door_locked`. A move through the door checks it first.

The program is played with: north (into the chamber), north (the locked door refuses), south, take shiny key, north, use shiny key, north (the treasure room).

### Worked Example
```lua
local rooms = {
  start = {
    description = "A dark cave.",
    exits = {north = "locked_door_room"},
    items = {"shiny key"},
  },
  locked_door_room = {
    description = "A small chamber with a heavy door to the NORTH.",
    exits = {south = "start", north = "treasure_room"},
    items = {},
  },
  treasure_room = {
    description = "A glittering room full of treasure. You win!",
    exits = {south = "locked_door_room"},
    items = {},
  },
}

local function index_of(list, value)
  for index, item in ipairs(list) do
    if item == value then return index end
  end
  return nil
end

local current_room = "start"
local inventory = {}
local door_locked = true

while true do
  local room = rooms[current_room]
  print("")
  print(room.description)
  if current_room == "treasure_room" then break end
  if #room.items > 0 then print("You see: " .. table.concat(room.items, ", ")) end
  print("Your inventory: " .. (#inventory > 0 and table.concat(inventory, ", ") or "empty"))
  print("What do you want to do?")

  local command = io.read()
  if command == nil then command = "quit" end
  command = command:lower()

  if command == "take shiny key" and index_of(room.items, "shiny key") then
    table.remove(room.items, index_of(room.items, "shiny key"))
    inventory[#inventory + 1] = "shiny key"
    print("You picked up the shiny key.")
  elseif command == "use shiny key" and current_room == "locked_door_room" and index_of(inventory, "shiny key") then
    door_locked = false
    print("You unlocked the door!")
  elseif room.exits[command] then
    if current_room == "locked_door_room" and command == "north" and door_locked then
      print("The door is locked! You need a key.")
    else
      current_room = room.exits[command]
    end
  elseif command == "quit" then
    print("Exiting game. Goodbye!")
    break
  else
    print("I don't understand that command.")
  end
end
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
north
north
south
take shiny key
north
use shiny key
north
```

the program prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?
The door is locked! You need a key.

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?
You picked up the shiny key.

A dark cave.
Your inventory: shiny key
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?
You unlocked the door!

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?

A glittering room full of treasure. You win!
```

### Common Mistakes
1. Making the door's locked state part of the exits so that the "locked" message can never be reached.
2. Defining an exit to a room that is missing from the `rooms` table, which crashes when the player arrives.
3. Printing a fixed room description that still mentions an item after the player has taken it.

### Activities
1. Play the program with the shown commands and follow each turn on paper.
2. Try `use shiny key` in the cave and describe what happens.
3. Add a second item and require both to open the door.
4. Write a short list of the game's states (location, inventory, door) and say which command changes each.

### Accessibility Practice
The room description never mentions the key. The separate line 'You see:' lists items, so the description stays true after the key is taken and the screen reader announces the current state.

### Skills Checklist
- [ ] I can store items in rooms and an inventory.
- [ ] I can implement take and use commands.
- [ ] I can block and allow a move.
- [ ] I can list the game's state variables.
- [ ] I can keep descriptions true after state changes.

## Lesson 10.4: Command-Line To-Do List

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 15 (Data Files and Serialization)
- Lua 5.4 Reference Manual: Section 6.8 (Input and Output Facilities)
- Matching Python lesson: Lesson 10.4 Building a Command-Line To-Do List

### Learning Objectives
- Keep records with the shared fields.
- Save and load them as JSON.
- Offer add, view, mark-done, save, load, and quit commands.

### Concept Explanation
A to-do list ties together records, loops, functions, and files. Each task has the shared fields `id`, `title`, `description`, `done`, and `created_at`. The program keeps a list of tasks in memory, shows a numbered menu, and saves the list to `todos.json` when asked and on exit.

Saving uses the teaching JSON helper from Lesson 8.5 (included here so the example runs on its own). On start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program: it prints a message and starts with an empty list.

New ids are one more than the highest existing id, so ids stay unique even after a task is removed. The status is shown as the words `done` and `not done`, never with a symbol or color alone.

In the sample session the user adds two tasks, views the list, marks task 2 as done, views it again, tries an invalid menu choice, views the list, and quits.

### Worked Example
```lua
local json = {}

local escapes = {['"'] = '\\"', ['\\'] = '\\\\', ['\n'] = '\\n', ['\r'] = '\\r', ['\t'] = '\\t'}

function json.encode(value)
  local kind = type(value)
  if kind == "string" then
    return '"' .. value:gsub('[%c"\\]', function(c)
      return escapes[c] or string.format("\\u%04x", c:byte())
    end) .. '"'
  elseif kind == "number" then
    return math.type(value) == "integer" and tostring(value) or string.format("%.14g", value)
  elseif kind == "boolean" then
    return tostring(value)
  elseif kind == "nil" then
    return "null"
  elseif kind == "table" then
    local parts = {}
    if value[1] ~= nil or next(value) == nil then
      for _, item in ipairs(value) do parts[#parts + 1] = json.encode(item) end
      return "[" .. table.concat(parts, ",") .. "]"
    end
    local keys = {}
    for key in pairs(value) do keys[#keys + 1] = key end
    table.sort(keys)
    for _, key in ipairs(keys) do
      parts[#parts + 1] = json.encode(tostring(key)) .. ":" .. json.encode(value[key])
    end
    return "{" .. table.concat(parts, ",") .. "}"
  end
  error("cannot encode a value of type " .. kind, 0)
end

function json.decode(text)
  local position = 1
  local read_value

  local function skip()
    position = text:find("%S", position) or #text + 1
  end

  local function fail(message)
    error(message .. " at position " .. position, 0)
  end

  local function read_string()
    local pieces = {}
    position = position + 1
    while true do
      local c = text:sub(position, position)
      if c == "" then fail("unterminated string") end
      if c == '"' then
        position = position + 1
        return table.concat(pieces)
      elseif c == "\\" then
        local n = text:sub(position + 1, position + 1)
        local simple = {n = "\n", t = "\t", r = "\r", ['"'] = '"', ["\\"] = "\\", ["/"] = "/"}
        if n == "u" then
          pieces[#pieces + 1] = utf8.char(tonumber(text:sub(position + 2, position + 5), 16))
          position = position + 6
        elseif simple[n] then
          pieces[#pieces + 1] = simple[n]
          position = position + 2
        else
          fail("bad escape")
        end
      else
        pieces[#pieces + 1] = c
        position = position + 1
      end
    end
  end

  function read_value()
    skip()
    local c = text:sub(position, position)
    if c == "{" then
      local object = {}
      position = position + 1
      skip()
      if text:sub(position, position) == "}" then position = position + 1; return object end
      while true do
        skip()
        if text:sub(position, position) ~= '"' then fail("expected a key") end
        local key = read_string()
        skip()
        if text:sub(position, position) ~= ":" then fail("expected ':'") end
        position = position + 1
        object[key] = read_value()
        skip()
        local d = text:sub(position, position)
        position = position + 1
        if d == "}" then return object end
        if d ~= "," then position = position - 1; fail("expected ',' or '}'") end
      end
    elseif c == "[" then
      local list = {}
      position = position + 1
      skip()
      if text:sub(position, position) == "]" then position = position + 1; return list end
      while true do
        list[#list + 1] = read_value()
        skip()
        local d = text:sub(position, position)
        position = position + 1
        if d == "]" then return list end
        if d ~= "," then position = position - 1; fail("expected ',' or ']'") end
      end
    elseif c == '"' then
      return read_string()
    elseif text:find("^true", position) then
      position = position + 4; return true
    elseif text:find("^false", position) then
      position = position + 5; return false
    elseif text:find("^null", position) then
      position = position + 4; return nil
    end
    local number = text:match("^-?%d+%.?%d*[eE]?[+-]?%d*", position)
    if not number or number == "" then fail("unexpected character") end
    position = position + #number
    return tonumber(number)
  end

  local result = read_value()
  skip()
  if position <= #text then fail("unexpected extra text") end
  return result
end

local TODO_FILE = "todos.json"
local todos = {}

local function load_todos()
  local file = io.open(TODO_FILE, "r")
  if not file then
    print("No existing tasks found.")
    todos = {}
    return
  end
  local text = file:read("a")
  file:close()
  local ok, data = pcall(json.decode, text)
  if ok and type(data) == "table" then
    todos = data
    print("Tasks loaded.")
  else
    print("Error: todos.json is not valid JSON. Starting with an empty list.")
    todos = {}
  end
end

local function save_todos()
  local file = assert(io.open(TODO_FILE, "w"))
  file:write(json.encode(todos))
  file:close()
  print("Tasks saved.")
end

local function next_id()
  local highest = 0
  for _, task in ipairs(todos) do
    if task.id > highest then highest = task.id end
  end
  return highest + 1
end

local function add_task(title, description)
  title = (title or ""):match("^%s*(.-)%s*$")
  if title == "" then
    print("A title is required.")
    return
  end
  todos[#todos + 1] = {
    id = next_id(),
    title = title,
    description = (description or ""):match("^%s*(.-)%s*$"),
    done = false,
    created_at = os.date("!%Y-%m-%dT%H:%M:%S"),
  }
  print("Task '" .. title .. "' added.")
end

local function view_tasks()
  if #todos == 0 then
    print("No tasks in your list.")
    return
  end
  print("--- Your To-Do List ---")
  for _, task in ipairs(todos) do
    print(string.format("%d. %s (%s)", task.id, task.title, task.done and "done" or "not done"))
  end
  print("-----------------------")
end

local function mark_done(text)
  local id = tonumber(text)
  if not id then
    print("Please enter a whole number.")
    return
  end
  for _, task in ipairs(todos) do
    if task.id == id then
      task.done = true
      print("Task '" .. task.title .. "' marked as done.")
      return
    end
  end
  print("No task has that number.")
end

local function show_menu()
  print("")
  print("--- To-Do List Menu ---")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task Done")
  print("4. Save Tasks")
  print("5. Load Tasks")
  print("6. Quit")
  print("-----------------------")
end

load_todos()
while true do
  show_menu()
  print("Enter your choice (1-6):")
  local choice = io.read()
  if choice == nil then choice = "6" end

  if choice == "1" then
    print("Enter task title:")
    local title = io.read()
    print("Enter task description:")
    local description = io.read()
    add_task(title, description)
  elseif choice == "2" then
    view_tasks()
  elseif choice == "3" then
    view_tasks()
    print("Enter task number to mark done:")
    mark_done(io.read())
  elseif choice == "4" then
    save_todos()
  elseif choice == "5" then
    load_todos()
  elseif choice == "6" then
    save_todos()
    print("Goodbye!")
    break
  else
    print("Invalid choice. Please try again.")
  end
end
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
1
Study programming
Finish Unit 10
1
Review scores
Check the four scores
2
3
2
3
7
2
6
```

the program prints:
```text
No existing tasks found.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Study programming' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Review scores' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------
Enter task number to mark done:
Task 'Review scores' marked as done.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------
Enter task number to mark done:
No task has that number.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Tasks saved.
Goodbye!
```

### Common Mistakes
1. Saving the file but never loading it, so tasks disappear between runs.
2. Reusing a deleted task's id, which can confuse saved references.
3. Letting a damaged `todos.json` crash the program instead of printing a message.

### Activities
1. Run the sample session and then run the program again with the input `2` then `6` to see the saved tasks.
2. Add a command to delete a task by number.
3. Open `todos.json` and read the saved text. Edit it to remove a bracket and rerun.
4. Add a `description` display to the view command.

### Accessibility Practice
Every menu is printed as numbered lines and each prompt is on its own line. The status words are `done` and `not done`, not symbols, so the list reads clearly in speech and braille.

### Skills Checklist
- [ ] I can keep records with the shared fields.
- [ ] I can save and load JSON.
- [ ] I handle a missing or damaged file.
- [ ] I keep ids unique.
- [ ] I show status in words.

## Lesson 10.5: User Experience and Input Validation

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions) and Chapter 16 (Compilation, Execution, and Errors)
- Lua 5.4 Reference Manual: Section 6.8 (io.read)
- Matching Python lesson: Lesson 10.5 Refining User Experience and Validation

### Learning Objectives
- Write reusable validation functions.
- Limit retries and handle the end of input.
- Write clear, accessible messages.

### Concept Explanation
Reusable validation functions make every menu and form consistent. `ask_number(prompt, low, high, attempts)` prints a prompt, reads a line, converts it, checks the range, and either returns the number or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns `nil` and a reason. `ask_yes_no(prompt)` accepts `y`, `yes`, `n`, and `no`, in any letter case.

Good messages say *what was wrong* and *what to do*: "Enter a whole number from 0 to 100," not "Invalid." They never depend on color, position, or symbols alone, and they use the same wording every time.

The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y.

### Worked Example
```lua
local function ask_number(prompt, low, high, attempts)
  for attempt = 1, attempts do
    print(prompt)
    local text = io.read()
    if text == nil then return nil, "No more input." end
    local number = tonumber(text)
    if number and number == math.floor(number) and number >= low and number <= high then
      return math.tointeger(number)
    end
    print(string.format("Enter a whole number from %d to %d. You have %d attempt(s) left.", low, high, attempts - attempt))
  end
  return nil, "Too many invalid attempts."
end

local function ask_yes_no(prompt)
  while true do
    print(prompt .. " (yes or no)")
    local text = io.read()
    if text == nil then return nil end
    text = text:lower()
    if text == "y" or text == "yes" then return true end
    if text == "n" or text == "no" then return false end
    print("Please answer yes or no.")
  end
end

local score, reason = ask_number("Enter a score from 0 to 100:", 0, 100, 3)
if score then
  print("Accepted score: " .. score)
else
  print("No score: " .. reason)
end

local keep = ask_yes_no("Save this score?")
print("Save answer:", keep)
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
abc
105
88
maybe
y
```

the program prints:
```text
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 2 attempt(s) left.
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 1 attempt(s) left.
Enter a score from 0 to 100:
Accepted score: 88
Save this score? (yes or no)
Please answer yes or no.
Save this score? (yes or no)
Save answer:	true
```

### Common Mistakes
1. Writing the message "Invalid" without saying what is valid.
2. Accepting a decimal such as 88.5 for a field that requires a whole number.
3. Looping forever on bad input instead of limiting attempts.

### Activities
1. Run the sample input and read each message aloud.
2. Run with three invalid numbers and read the final message.
3. Add a function `ask_text(prompt)` that rejects empty answers.
4. Rewrite two messages from earlier lessons so they say what to do next.

### Accessibility Practice
Check that every error message ends with an action the user can take, and that the same situation always produces the same words.

### Skills Checklist
- [ ] I can write reusable validation functions.
- [ ] I limit retries.
- [ ] I handle the end of input.
- [ ] I write messages that say what to do.
- [ ] I keep wording consistent.
