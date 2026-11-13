[Header 2 ("unit-10-project-based-learning--text-based-applications", [], []) [Str "Unit 10: Project-Based Learning — Text-Based Applications"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python."], Header 3 ("lesson-101-project-design-and-requirements", ["unnumbered", "unlisted"], []) [Str "Lesson 10.1 Project Design and Requirements"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/"]], [Plain [Str "Programming in Lua: https://www.lua.org/pil/"]], [Plain [Str "Corresponding Python lesson in the canonical course map."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the concept using Lua terminology."]], [Plain [Str "Trace the worked example and predict its behavior."]], [Plain [Str "Modify and test the example while preserving the shared data contract."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Translate requirements into data structures, commands, and acceptance tests before coding. This room graph is the common adventure map."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local rooms = {
  start_room = {exits = {north = \"tunnel\"}, items = {\"shiny key\"}},
  tunnel = {exits = {south = \"start_room\", east = \"clearing\"}, items = {}},
  clearing = {exits = {west = \"tunnel\", north = \"locked_door_room\"}, items = {}},
  locked_door_room = {exits = {south = \"clearing\", north = \"treasure_room\"}, items = {}},
  treasure_room = {exits = {}, items = {}}
}
print(rooms.tunnel.exits.east)
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], CodeBlock ("", ["text"], []) "clearing
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Dropping one of the six required capstone record fields during serialization."]], [Plain [Str "Updating a record without refreshing updated_at."]], [Plain [Str "Claiming screen-reader compatibility without testing keyboard and assistive-technology workflows."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create a record containing all six canonical capstone fields and validate each field."]], [Plain [Str "Exercise add, list, search, update, and delete with both existing and missing IDs."]], [Plain [Str "Save and reload a record; compare every field before and after persistence."]], [Plain [Str "Write a text-only keyboard interaction guide and list the accessibility tests still required."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the concept in Lua terminology."]], [Plain [Str "\9744", Space, Str "I can trace and predict the example's behavior."]], [Plain [Str "\9744", Space, Str "I can run and modify the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can test a boundary or invalid case."]], [Plain [Str "\9744", Space, Str "I can explain the relevant Lua-specific semantic difference."]]], HorizontalRule, Header 3 ("lesson-102-text-adventure-part-1-five-rooms-and-movement", ["unnumbered", "unlisted"], []) [Str "Lesson 10.2: Text Adventure, Part 1: Five Rooms and Movement"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Lua 5.4 Reference Manual"] ("https://www.lua.org/manual/5.4/", "")]], [Plain [Link ("", [], []) [Str "Programming in Lua"] ("https://www.lua.org/pil/", "")]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Represent the five canonical rooms and their exits with Lua tables."]], [Plain [Str "Move through valid exits without changing location after an invalid command."]], [Plain [Str "Explain why the north exit from the locked-door room is not available yet."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The shared adventure has five rooms: start_room, tunnel, clearing, locked_door_room, and treasure_room. The unconditional connections are start north to tunnel; tunnel south to start and east to clearing; clearing west to tunnel and north to the locked-door room; and locked-door room south to clearing. The north exit to the treasure room is conditional and is added in Part 2 only after the shiny-key puzzle is solved."], Para [Str "Each room is a Lua table with a description and an exits table. A missing key lookup returns nil, so invalid movement can be rejected without changing the current room."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local rooms = {
  start_room = {
    description = \"A dimly lit cave. A narrow passage leads north.\",
    exits = {north = \"tunnel\"}
  },
  tunnel = {
    description = \"A damp tunnel. Passages lead south and east.\",
    exits = {south = \"start_room\", east = \"clearing\"}
  },
  clearing = {
    description = \"A quiet clearing. An antechamber lies to the north.\",
    exits = {west = \"tunnel\", north = \"locked_door_room\"}
  },
  locked_door_room = {
    description = \"A chamber with a heavy door to the north.\",
    exits = {south = \"clearing\"}
  },
  treasure_room = {
    description = \"You found the treasure. You win!\",
    exits = {}
  }
}

local current_room = \"start_room\"
while true do
  local room = rooms[current_room]
  print(\"---\")
  print(room.description)
  print(\"What do you want to do?\")
  local input = io.read(\"*l\")
  local command = (input or \"quit\"):match(\"^%s*(.-)%s*$\"):lower()

  if command == \"quit\" then
    print(\"Exiting game. Goodbye!\")
    break
  end

  local destination = room.exits[command]
  if destination then
    current_room = destination
  else
    print(\"You cannot go that way. Enter a listed direction or quit.\")
  end
end
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With north, east, north, north, quit entered as separate input lines, the player visits tunnel, clearing, and locked_door_room. The second north from locked_door_room is rejected and the current room does not change. The treasure room exists in the model but cannot be reached in Part 1."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Adding the treasure-room north exit before implementing the key puzzle."]], [Plain [Str "Updating current_room before confirming that the requested exit exists."]], [Plain [Str "Treating a missing table key as a valid destination."]], [Plain [Str "Defining an exit whose destination is not one of the five room identifiers."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace north, east, north, north and record the room after each command."]], [Plain [Str "Try west from start_room; confirm that the location does not change."]], [Plain [Str "Check that every destination in every unconditional exit exists in rooms."]], [Plain [Str "Explain why treasure_room has no incoming exit in Part 1."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the separator, room description, and prompt in order. The invalid-movement response explains what happened and how to continue. Test the sequence by listening to terminal output; do not rely on a visual map."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model all five canonical rooms."]], [Plain [Str "\9744", Space, Str "I can represent exits with Lua tables."]], [Plain [Str "\9744", Space, Str "I can move only when an exit exists."]], [Plain [Str "\9744", Space, Str "I can reject an invalid direction without changing state."]], [Plain [Str "\9744", Space, Str "I can explain why the treasure room is not yet reachable."]]], HorizontalRule, Header 3 ("lesson-103-text-adventure-part-2-shiny-key-and-locked-door", ["unnumbered", "unlisted"], []) [Str "Lesson 10.3: Text Adventure, Part 2: Shiny Key and Locked Door"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Lua 5.4 Reference Manual"] ("https://www.lua.org/manual/5.4/", "")]], [Plain [Link ("", [], []) [Str "Programming in Lua"] ("https://www.lua.org/pil/", "")]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Place the shiny key in start_room and transfer it to inventory exactly once."]], [Plain [Str "Require the player to use the key while in locked_door_room."]], [Plain [Str "Unlock the north exit to treasure_room only after the puzzle succeeds."]], [Plain [Str "End the game when the player reaches the treasure room."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Part 2 keeps the same five-room graph. The shiny key begins in start_room. The take shiny key command removes it from that room and adds it to inventory. The use shiny key command works only in locked_door_room and only when the key is in inventory. Attempting north from the locked-door room before that action prints a locked-door message and leaves the player in place. After the key is used, north leads to treasure_room."], Para [Str "Room descriptions do not claim that an item is still present. Room items and inventory are announced on separate lines."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local rooms = {
  start_room = {
    description = \"A dimly lit cave.\",
    exits = {north = \"tunnel\"},
    items = {\"shiny key\"}
  },
  tunnel = {
    description = \"A damp tunnel. Passages lead south and east.\",
    exits = {south = \"start_room\", east = \"clearing\"},
    items = {}
  },
  clearing = {
    description = \"A quiet clearing. Antechamber lies to the north.\",
    exits = {west = \"tunnel\", north = \"locked_door_room\"},
    items = {}
  },
  locked_door_room = {
    description = \"A chamber with a heavy door to the north.\",
    exits = {south = \"clearing\"},
    items = {}
  },
  treasure_room = {
    description = \"You found the treasure. You win!\",
    exits = {},
    items = {}
  }
}

local current_room = \"start_room\"
local inventory = {}
local door_locked = true

local function inventory_has(item_name)
  for _, item in ipairs(inventory) do
    if item == item_name then return true end
  end
  return false
end

while true do
  local room = rooms[current_room]
  print()
  print(room.description)
  if current_room == \"treasure_room\" then break end
  if #room.items > 0 then
    print(\"You see: \" .. table.concat(room.items, \", \"))
  end
  print(\"Your inventory: \" .. (#inventory == 0 and \"empty\" or table.concat(inventory, \", \")))
  print(\"What do you want to do?\")

  local input = io.read(\"*l\")
  local command = (input or \"quit\"):match(\"^%s*(.-)%s*$\"):lower()

  if command == \"quit\" then
    print(\"You quit the adventure.\")
    break
  elseif command == \"take shiny key\" then
    local found_index
    for index, item in ipairs(room.items) do
      if item == \"shiny key\" then
        found_index = index
        break
      end
    end
    if found_index then
      table.remove(room.items, found_index)
      inventory[#inventory + 1] = \"shiny key\"
      print(\"You picked up the shiny key.\")
    else
      print(\"There is no shiny key here to take.\")
    end
  elseif command == \"use shiny key\" then
    if current_room ~= \"locked_door_room\" then
      print(\"You must be at the locked door to use the key.\")
    elseif not inventory_has(\"shiny key\") then
      print(\"You do not have the shiny key.\")
    else
      door_locked = false
      rooms.locked_door_room.exits.north = \"treasure_room\"
      print(\"You unlocked the door!\")
    end
  elseif current_room == \"locked_door_room\" and command == \"north\" and door_locked then
    print(\"The door is locked! You need to use the shiny key here.\")
  elseif room.exits[command] then
    current_room = room.exits[command]
  else
    print(\"Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.\")
  end
end
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Use this sequence to verify the puzzle: north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north."], Para [Str "The first north attempt from locked_door_room must be rejected. Taking the key removes it from start_room and adds it to inventory. Using it outside locked_door_room must be rejected. Using it there prints You unlocked the door!; the next north reaches treasure_room and prints You found the treasure. You win!. End-of-file is treated as quit."], Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Leaving the shiny key in the room after adding it to inventory."]], [Plain [Str "Unlocking the door outside locked_door_room."]], [Plain [Str "Unlocking the door without checking inventory."]], [Plain [Str "Allowing north movement before door_locked becomes false."]], [Plain [Str "Describing the key as still on the floor after it has been collected."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the full sequence and record room, room items, inventory, and door state after every command."]], [Plain [Str "Try take shiny key twice; the second attempt must not duplicate the item."]], [Plain [Str "Try use shiny key in start_room and clearing; both attempts must be rejected."]], [Plain [Str "Try north from locked_door_room before and after unlocking."]], [Plain [Str "Add a look command that announces room, visible items, inventory, and exits in a consistent order."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Announce room description, visible items, inventory, and prompt as separate text lines. Every failed action explains why it failed. Listen to the full puzzle sequence and verify that key location and door state are unambiguous."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model the five canonical rooms."]], [Plain [Str "\9744", Space, Str "I can transfer the shiny key from a room to inventory."]], [Plain [Str "\9744", Space, Str "I can prevent duplicate pickup."]], [Plain [Str "\9744", Space, Str "I can require key use in the locked-door room."]], [Plain [Str "\9744", Space, Str "I can block and unlock the north exit."]], [Plain [Str "\9744", Space, Str "I can end the game when the treasure room is reached."]]], HorizontalRule, Header 3 ("lesson-104-command-line-to-do-manager", ["unnumbered", "unlisted"], []) [Str "Lesson 10.4 Command-Line To-Do Manager"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/"]], [Plain [Str "Programming in Lua: https://www.lua.org/pil/"]], [Plain [Str "Corresponding Python lesson in the canonical course map."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the concept using Lua terminology."]], [Plain [Str "Trace the worked example and predict its behavior."]], [Plain [Str "Modify and test the example while preserving the shared data contract."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The task record must include id, title, description, done, and created_at. Keep CRUD operations separate from the input loop."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local tasks = {}
local function add_task(id, title, description, created_at)
  assert(title ~= nil and title ~= \"\", \"title is required\")
  tasks[#tasks + 1] = {id = id, title = title, description = description,
    done = false, created_at = created_at}
end
add_task(1, \"Practice Lua\", \"Complete the shared examples\", \"2025-01-15T09:00:00Z\")
print(tasks[1].id, tasks[1].title, tasks[1].done)
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], CodeBlock ("", ["text"], []) "1	Practice Lua	false
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Omitting one or more required task fields from a stored record."]], [Plain [Str "Using a list position as a permanent task identifier after deletion or reordering."]], [Plain [Str "Treating malformed persistence data as an empty task list without reporting the error."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create a task with all five canonical fields and list it in a stable format."]], [Plain [Str "Update its done state, then search for it by identifier."]], [Plain [Str "Delete an existing ID and attempt to delete a missing ID; compare the messages."]], [Plain [Str "Save and reload the records, then verify every field is preserved."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the concept in Lua terminology."]], [Plain [Str "\9744", Space, Str "I can trace and predict the example's behavior."]], [Plain [Str "\9744", Space, Str "I can run and modify the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can test a boundary or invalid case."]], [Plain [Str "\9744", Space, Str "I can explain the relevant Lua-specific semantic difference."]]], HorizontalRule, Header 3 ("lesson-105-refinement-and-accessibility", ["unnumbered", "unlisted"], []) [Str "Lesson 10.5 Refinement and Accessibility"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/"]], [Plain [Str "Programming in Lua: https://www.lua.org/pil/"]], [Plain [Str "Corresponding Python lesson in the canonical course map."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the concept using Lua terminology."]], [Plain [Str "Trace the worked example and predict its behavior."]], [Plain [Str "Modify and test the example while preserving the shared data contract."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A command-line application needs explicit help, validation, confirmations, and readable errors. Keep all critical information in text."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local function validate_title(title)
  if title == nil or title:match(\"^%s*$\") then
    return false, \"Title is required; enter at least one non-space character.\"
  end
  return true, \"Title accepted.\"
end
local ok, message = validate_title(\"   \")
print(message)
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], CodeBlock ("", ["text"], []) "Title is required; enter at least one non-space character.
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Copying a Python assumption into Lua without checking the Lua 5.4 semantics."]], [Plain [Str "Changing the canonical input values and then comparing output against the shared fixture."]], [Plain [Str "Skipping a negative or boundary case for the lesson's main operation."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace the 10.5 Refinement and Accessibility worked example and explain each statement in Lua terms."]], [Plain [Str "Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution."]], [Plain [Str "Add a boundary or invalid-input test for the main operation in this lesson."]], [Plain [Str "Explain one semantic difference between Lua and Python that affects 10.5 refinement and accessibility."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the concept in Lua terminology."]], [Plain [Str "\9744", Space, Str "I can trace and predict the example's behavior."]], [Plain [Str "\9744", Space, Str "I can run and modify the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can test a boundary or invalid case."]], [Plain [Str "\9744", Space, Str "I can explain the relevant Lua-specific semantic difference."]]], HorizontalRule, Header 3 ("overview-1", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Plan a text project, build the shared text adventure in two parts, build the command-line to-do manager, and refine input validation."], Header 3 ("lesson-101-planning-a-text-based-project", ["unnumbered", "unlisted"], []) [Str "Lesson 10.1: Planning a Text-Based Project"], Header 4 ("reading-references-5", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions) and Chapter 5 (Tables)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 3.3 (Statements)"]], [Plain [Str "Matching Python lesson: Lesson 10.1 Project Planning and Design"]]], Header 4 ("learning-objectives-5", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write a short requirements list."]], [Plain [Str "Design a command loop with a table of handlers."]], [Plain [Str "Plan in small steps and test each one."]]], Header 4 ("concept-explanation-5", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A project is easier to finish when you plan it in small steps. Write down ", Emph [Str "what the program must do"], Str " (requirements), ", Emph [Str "what information it keeps"], Str " (data), and ", Emph [Str "the commands a person can give"], Str " (interface). Build one small piece, test it, and then add the next."], Para [Str "Text-based projects share a ", Emph [Str "command loop"], Str ": show a prompt, read a line, find the matching action, and repeat until the user quits. A good Lua design stores actions in a table whose keys are command names and whose values are functions. A new command is then one new entry, and an unknown command is a failed lookup that prints a helpful message."], Para [Str "The loop must stop when the input ends (", Code ("", [], []) "nil", Str ") as well as on ", Code ("", [], []) "quit", Str "."], Para [Str "The example is a skeleton with three commands. Typing ", Code ("", [], []) "help", Str ", ", Code ("", [], []) "look", Str ", an unknown word, and ", Code ("", [], []) "quit", Str " shows each path."], Header 4 ("worked-example-5", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local commands = {
  help = function() print(\"Commands: help, look, quit\") end,
  look = function() print(\"You are in a dark cave.\") end,
}

print(\"Type a command:\")
local line = io.read()
while line ~= nil and line ~= \"quit\" do
  local handler = commands[line]
  if handler then
    handler()
  else
    print(\"I don't understand that command. Type help for a list.\")
  end
  print(\"Type a command:\")
  line = io.read()
end
print(\"Goodbye!\")
", Header 4 ("expected-behavior-or-output-5", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):"], CodeBlock ("", ["text"], []) "help
look
dance
quit
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "Type a command:
Commands: help, look, quit
Type a command:
You are in a dark cave.
Type a command:
I don't understand that command. Type help for a list.
Type a command:
Goodbye!
", Header 4 ("common-mistakes-5", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Starting to code before listing the requirements."]], [Plain [Str "Using a long chain of ", Code ("", [], []) "if", Str " statements for commands instead of a table of handlers."]], [Plain [Str "Forgetting that an unknown command should explain what to do next."]]], Header 4 ("activities-5", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write five requirements for the text adventure and the to-do list."]], [Plain [Str "Add a ", Code ("", [], []) "score", Str " command that prints the shared scores."]], [Plain [Str "Add the command aliases ", Code ("", [], []) "h", Str " and ", Code ("", [], []) "l", Str " without copying the functions."]], [Plain [Str "Describe the data for the capstone in three sentences."]]], Header 4 ("accessibility-practice-5", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Prompts and responses are on separate lines and every response is a complete sentence. Test the prompts by listening to them before you add features."], Header 4 ("skills-checklist-5", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can list requirements."]], [Plain [Str "\9744", Space, Str "I can design a command loop."]], [Plain [Str "\9744", Space, Str "I can use a table of handlers."]], [Plain [Str "\9744", Space, Str "I handle unknown commands."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]]], Header 3 ("lesson-102-text-adventure-part-1-rooms-and-movement", ["unnumbered", "unlisted"], []) [Str "Lesson 10.2: Text Adventure, Part 1: Rooms and Movement"], Header 4 ("reading-references-6", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 3.4.9 (Table Constructors)"]], [Plain [Str "Matching Python lesson: Lesson 10.2 Building a Text-Based Adventure Game (Part 1)"]]], Header 4 ("learning-objectives-6", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Represent rooms and exits with tables."]], [Plain [Str "Move the player by command."]], [Plain [Str "Handle impossible moves and the end of input."]]], Header 4 ("concept-explanation-6", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A room is a table with a ", Code ("", [], []) "description", Str " and an ", Code ("", [], []) "exits", Str " table that maps a direction to the name of another room. The program remembers the player's location in one variable, ", Code ("", [], []) "current_room", Str ". A move looks up the command in the current room's exits; if it is found, ", Code ("", [], []) "current_room", Str " changes, otherwise the program explains that the move is impossible."], Para [Str "This is the same three-room layout as the Python course: a cave, a tunnel, and a clearing. Part 2 adds items and a locked door."], Para [Str "The example is played with the commands north, east, west, up, south, and quit. The command ", Code ("", [], []) "up", Str " is not an exit anywhere, so it prints the help message."], Header 4 ("worked-example-6", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local rooms = {
  start_room = {
    description = \"You are in a dimly lit cave. There's a narrow passage to the NORTH.\",
    exits = {north = \"tunnel\"},
  },
  tunnel = {
    description = \"The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.\",
    exits = {south = \"start_room\", east = \"clearing\"},
  },
  clearing = {
    description = \"You've reached a small, sunny clearing. A faint path leads WEST.\",
    exits = {west = \"tunnel\"},
  },
}

local current_room = \"start_room\"

while true do
  print(\"---\")
  print(rooms[current_room].description)
  print(\"What do you want to do?\")
  local command = io.read()
  if command == nil then command = \"quit\" end
  command = command:lower()

  if rooms[current_room].exits[command] then
    current_room = rooms[current_room].exits[command]
  elseif command == \"quit\" then
    print(\"Exiting game. Goodbye!\")
    break
  else
    print(\"I don't understand that command or you can't go that way.\")
  end
end
", Header 4 ("expected-behavior-or-output-6", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):"], CodeBlock ("", ["text"], []) "north
east
west
up
south
quit
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "---
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
", Header 4 ("common-mistakes-6", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Looking up a direction that is not in ", Code ("", [], []) "exits", Str " and expecting an error. The lookup returns ", Code ("", [], []) "nil", Str ", which is the signal to explain the move is impossible."]], [Plain [Str "Forgetting to treat the end of input as ", Code ("", [], []) "quit", Str ", so the program loops forever when input is piped in."]], [Plain [Str "Misspelling a room name in ", Code ("", [], []) "exits", Str ", so the move leads to a room that does not exist."]]], Header 4 ("activities-6", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace the six commands by hand and write the room after each one."]], [Plain [Str "Add a fourth room reached from the clearing and test it."]], [Plain [Str "Add the aliases ", Code ("", [], []) "n", Str ", ", Code ("", [], []) "s", Str ", ", Code ("", [], []) "e", Str ", and ", Code ("", [], []) "w", Str "."]], [Plain [Str "Check that every exit names a real room by writing a loop that tests the whole table."]]], Header 4 ("accessibility-practice-6", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each turn prints a separator line, the description, and the prompt on its own line. Listen to a whole turn to confirm that a player could follow it without seeing the screen."], Header 4 ("skills-checklist-6", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can represent rooms with tables."]], [Plain [Str "\9744", Space, Str "I can move the player by command."]], [Plain [Str "\9744", Space, Str "I can handle an impossible move."]], [Plain [Str "\9744", Space, Str "I treat end of input as quit."]], [Plain [Str "\9744", Space, Str "I can trace a game by hand."]]], Header 3 ("lesson-103-text-adventure-part-2-items-and-a-locked-door", ["unnumbered", "unlisted"], []) [Str "Lesson 10.3: Text Adventure, Part 2: Items and a Locked Door"], Header 4 ("reading-references-7", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables) and Chapter 6 (Functions)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 6.6 (Table Manipulation)"]], [Plain [Str "Matching Python lesson: Lesson 10.3 Building a Text-Based Adventure Game (Part 2)"]]], Header 4 ("learning-objectives-7", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Keep items in rooms and in an inventory."]], [Plain [Str "Implement take and use commands."]], [Plain [Str "Block and then allow a move with a locked door."]]], Header 4 ("concept-explanation-7", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Part 2 adds ", Emph [Str "state"], Str ": items in rooms, an inventory, and a door that is locked until the player uses the key. This is the shared specification used by every language track: three rooms (", Code ("", [], []) "start", Str ", ", Code ("", [], []) "locked_door_room", Str ", ", Code ("", [], []) "treasure_room", Str "); the commands ", Code ("", [], []) "north", Str ", ", Code ("", [], []) "south", Str ", ", Code ("", [], []) "east", Str ", ", Code ("", [], []) "west", Str ", ", Code ("", [], []) "take shiny key", Str ", ", Code ("", [], []) "use shiny key", Str ", and ", Code ("", [], []) "quit", Str "; the door between the chamber and the treasure room stays locked until the key is used there; reaching the treasure room ends the game."], Para [Str "Items are lists of names. Taking an item removes it from the room's list and appends it to the inventory. The locked door is a Boolean variable, ", Code ("", [], []) "door_locked", Str ". A move through the door checks it first."], Para [Str "The program is played with: north (into the chamber), north (the locked door refuses), south, take shiny key, north, use shiny key, north (the treasure room)."], Header 4 ("worked-example-7", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local rooms = {
  start = {
    description = \"A dark cave.\",
    exits = {north = \"locked_door_room\"},
    items = {\"shiny key\"},
  },
  locked_door_room = {
    description = \"A small chamber with a heavy door to the NORTH.\",
    exits = {south = \"start\", north = \"treasure_room\"},
    items = {},
  },
  treasure_room = {
    description = \"A glittering room full of treasure. You win!\",
    exits = {south = \"locked_door_room\"},
    items = {},
  },
}

local function index_of(list, value)
  for index, item in ipairs(list) do
    if item == value then return index end
  end
  return nil
end

local current_room = \"start\"
local inventory = {}
local door_locked = true

while true do
  local room = rooms[current_room]
  print(\"\")
  print(room.description)
  if current_room == \"treasure_room\" then break end
  if #room.items > 0 then print(\"You see: \" .. table.concat(room.items, \", \")) end
  print(\"Your inventory: \" .. (#inventory > 0 and table.concat(inventory, \", \") or \"empty\"))
  print(\"What do you want to do?\")

  local command = io.read()
  if command == nil then command = \"quit\" end
  command = command:lower()

  if command == \"take shiny key\" and index_of(room.items, \"shiny key\") then
    table.remove(room.items, index_of(room.items, \"shiny key\"))
    inventory[#inventory + 1] = \"shiny key\"
    print(\"You picked up the shiny key.\")
  elseif command == \"use shiny key\" and current_room == \"locked_door_room\" and index_of(inventory, \"shiny key\") then
    door_locked = false
    print(\"You unlocked the door!\")
  elseif room.exits[command] then
    if current_room == \"locked_door_room\" and command == \"north\" and door_locked then
      print(\"The door is locked! You need a key.\")
    else
      current_room = room.exits[command]
    end
  elseif command == \"quit\" then
    print(\"Exiting game. Goodbye!\")
    break
  else
    print(\"I don't understand that command.\")
  end
end
", Header 4 ("expected-behavior-or-output-7", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):"], CodeBlock ("", ["text"], []) "north
north
south
take shiny key
north
use shiny key
north
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "
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
", Header 4 ("common-mistakes-7", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Making the door's locked state part of the exits so that the \"locked\" message can never be reached."]], [Plain [Str "Defining an exit to a room that is missing from the ", Code ("", [], []) "rooms", Str " table, which crashes when the player arrives."]], [Plain [Str "Printing a fixed room description that still mentions an item after the player has taken it."]]], Header 4 ("activities-7", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Play the program with the shown commands and follow each turn on paper."]], [Plain [Str "Try ", Code ("", [], []) "use shiny key", Str " in the cave and describe what happens."]], [Plain [Str "Add a second item and require both to open the door."]], [Plain [Str "Write a short list of the game's states (location, inventory, door) and say which command changes each."]]], Header 4 ("accessibility-practice-7", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "The room description never mentions the key. The separate line 'You see:' lists items, so the description stays true after the key is taken and the screen reader announces the current state."], Header 4 ("skills-checklist-7", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can store items in rooms and an inventory."]], [Plain [Str "\9744", Space, Str "I can implement take and use commands."]], [Plain [Str "\9744", Space, Str "I can block and allow a move."]], [Plain [Str "\9744", Space, Str "I can list the game's state variables."]], [Plain [Str "\9744", Space, Str "I can keep descriptions true after state changes."]]], Header 3 ("lesson-104-command-line-to-do-list", ["unnumbered", "unlisted"], []) [Str "Lesson 10.4: Command-Line To-Do List"], Header 4 ("reading-references-8", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 15 (Data Files and Serialization)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 6.8 (Input and Output Facilities)"]], [Plain [Str "Matching Python lesson: Lesson 10.4 Building a Command-Line To-Do List"]]], Header 4 ("learning-objectives-8", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Keep records with the shared fields."]], [Plain [Str "Save and load them as JSON."]], [Plain [Str "Offer add, view, mark-done, save, load, and quit commands."]]], Header 4 ("concept-explanation-8", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A to-do list ties together records, loops, functions, and files. Each task has the shared fields ", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "done", Str ", and ", Code ("", [], []) "created_at", Str ". The program keeps a list of tasks in memory, shows a numbered menu, and saves the list to ", Code ("", [], []) "todos.json", Str " when asked and on exit."], Para [Str "Saving uses the teaching JSON helper from Lesson 8.5 (included here so the example runs on its own). On start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program: it prints a message and starts with an empty list."], Para [Str "New ids are one more than the highest existing id, so ids stay unique even after a task is removed. The status is shown as the words ", Code ("", [], []) "done", Str " and ", Code ("", [], []) "not done", Str ", never with a symbol or color alone."], Para [Str "In the sample session the user adds two tasks, views the list, marks task 2 as done, views it again, tries an invalid menu choice, views the list, and quits."], Header 4 ("worked-example-8", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local json = {}

local escapes = {['\"'] = '\\\\\"', ['\\\\'] = '\\\\\\\\', ['\\n'] = '\\\\n', ['\\r'] = '\\\\r', ['\\t'] = '\\\\t'}

function json.encode(value)
  local kind = type(value)
  if kind == \"string\" then
    return '\"' .. value:gsub('[%c\"\\\\]', function(c)
      return escapes[c] or string.format(\"\\\\u%04x\", c:byte())
    end) .. '\"'
  elseif kind == \"number\" then
    return math.type(value) == \"integer\" and tostring(value) or string.format(\"%.14g\", value)
  elseif kind == \"boolean\" then
    return tostring(value)
  elseif kind == \"nil\" then
    return \"null\"
  elseif kind == \"table\" then
    local parts = {}
    if value[1] ~= nil or next(value) == nil then
      for _, item in ipairs(value) do parts[#parts + 1] = json.encode(item) end
      return \"[\" .. table.concat(parts, \",\") .. \"]\"
    end
    local keys = {}
    for key in pairs(value) do keys[#keys + 1] = key end
    table.sort(keys)
    for _, key in ipairs(keys) do
      parts[#parts + 1] = json.encode(tostring(key)) .. \":\" .. json.encode(value[key])
    end
    return \"{\" .. table.concat(parts, \",\") .. \"}\"
  end
  error(\"cannot encode a value of type \" .. kind, 0)
end

function json.decode(text)
  local position = 1
  local read_value

  local function skip()
    position = text:find(\"%S\", position) or #text + 1
  end

  local function fail(message)
    error(message .. \" at position \" .. position, 0)
  end

  local function read_string()
    local pieces = {}
    position = position + 1
    while true do
      local c = text:sub(position, position)
      if c == \"\" then fail(\"unterminated string\") end
      if c == '\"' then
        position = position + 1
        return table.concat(pieces)
      elseif c == \"\\\\\" then
        local n = text:sub(position + 1, position + 1)
        local simple = {n = \"\\n\", t = \"\\t\", r = \"\\r\", ['\"'] = '\"', [\"\\\\\"] = \"\\\\\", [\"/\"] = \"/\"}
        if n == \"u\" then
          pieces[#pieces + 1] = utf8.char(tonumber(text:sub(position + 2, position + 5), 16))
          position = position + 6
        elseif simple[n] then
          pieces[#pieces + 1] = simple[n]
          position = position + 2
        else
          fail(\"bad escape\")
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
    if c == \"{\" then
      local object = {}
      position = position + 1
      skip()
      if text:sub(position, position) == \"}\" then position = position + 1; return object end
      while true do
        skip()
        if text:sub(position, position) ~= '\"' then fail(\"expected a key\") end
        local key = read_string()
        skip()
        if text:sub(position, position) ~= \":\" then fail(\"expected ':'\") end
        position = position + 1
        object[key] = read_value()
        skip()
        local d = text:sub(position, position)
        position = position + 1
        if d == \"}\" then return object end
        if d ~= \",\" then position = position - 1; fail(\"expected ',' or '}'\") end
      end
    elseif c == \"[\" then
      local list = {}
      position = position + 1
      skip()
      if text:sub(position, position) == \"]\" then position = position + 1; return list end
      while true do
        list[#list + 1] = read_value()
        skip()
        local d = text:sub(position, position)
        position = position + 1
        if d == \"]\" then return list end
        if d ~= \",\" then position = position - 1; fail(\"expected ',' or ']'\") end
      end
    elseif c == '\"' then
      return read_string()
    elseif text:find(\"^true\", position) then
      position = position + 4; return true
    elseif text:find(\"^false\", position) then
      position = position + 5; return false
    elseif text:find(\"^null\", position) then
      position = position + 4; return nil
    end
    local number = text:match(\"^-?%d+%.?%d*[eE]?[+-]?%d*\", position)
    if not number or number == \"\" then fail(\"unexpected character\") end
    position = position + #number
    return tonumber(number)
  end

  local result = read_value()
  skip()
  if position <= #text then fail(\"unexpected extra text\") end
  return result
end

local TODO_FILE = \"todos.json\"
local todos = {}

local function load_todos()
  local file = io.open(TODO_FILE, \"r\")
  if not file then
    print(\"No existing tasks found.\")
    todos = {}
    return
  end
  local text = file:read(\"a\")
  file:close()
  local ok, data = pcall(json.decode, text)
  if ok and type(data) == \"table\" then
    todos = data
    print(\"Tasks loaded.\")
  else
    print(\"Error: todos.json is not valid JSON. Starting with an empty list.\")
    todos = {}
  end
end

local function save_todos()
  local file = assert(io.open(TODO_FILE, \"w\"))
  file:write(json.encode(todos))
  file:close()
  print(\"Tasks saved.\")
end

local function next_id()
  local highest = 0
  for _, task in ipairs(todos) do
    if task.id > highest then highest = task.id end
  end
  return highest + 1
end

local function add_task(title, description)
  title = (title or \"\"):match(\"^%s*(.-)%s*$\")
  if title == \"\" then
    print(\"A title is required.\")
    return
  end
  todos[#todos + 1] = {
    id = next_id(),
    title = title,
    description = (description or \"\"):match(\"^%s*(.-)%s*$\"),
    done = false,
    created_at = os.date(\"!%Y-%m-%dT%H:%M:%S\"),
  }
  print(\"Task '\" .. title .. \"' added.\")
end

local function view_tasks()
  if #todos == 0 then
    print(\"No tasks in your list.\")
    return
  end
  print(\"--- Your To-Do List ---\")
  for _, task in ipairs(todos) do
    print(string.format(\"%d. %s (%s)\", task.id, task.title, task.done and \"done\" or \"not done\"))
  end
  print(\"-----------------------\")
end

local function mark_done(text)
  local id = tonumber(text)
  if not id then
    print(\"Please enter a whole number.\")
    return
  end
  for _, task in ipairs(todos) do
    if task.id == id then
      task.done = true
      print(\"Task '\" .. task.title .. \"' marked as done.\")
      return
    end
  end
  print(\"No task has that number.\")
end

local function show_menu()
  print(\"\")
  print(\"--- To-Do List Menu ---\")
  print(\"1. Add Task\")
  print(\"2. View Tasks\")
  print(\"3. Mark Task Done\")
  print(\"4. Save Tasks\")
  print(\"5. Load Tasks\")
  print(\"6. Quit\")
  print(\"-----------------------\")
end

load_todos()
while true do
  show_menu()
  print(\"Enter your choice (1-6):\")
  local choice = io.read()
  if choice == nil then choice = \"6\" end

  if choice == \"1\" then
    print(\"Enter task title:\")
    local title = io.read()
    print(\"Enter task description:\")
    local description = io.read()
    add_task(title, description)
  elseif choice == \"2\" then
    view_tasks()
  elseif choice == \"3\" then
    view_tasks()
    print(\"Enter task number to mark done:\")
    mark_done(io.read())
  elseif choice == \"4\" then
    save_todos()
  elseif choice == \"5\" then
    load_todos()
  elseif choice == \"6\" then
    save_todos()
    print(\"Goodbye!\")
    break
  else
    print(\"Invalid choice. Please try again.\")
  end
end
", Header 4 ("expected-behavior-or-output-8", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):"], CodeBlock ("", ["text"], []) "1
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
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "No existing tasks found.

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
", Header 4 ("common-mistakes-8", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Saving the file but never loading it, so tasks disappear between runs."]], [Plain [Str "Reusing a deleted task's id, which can confuse saved references."]], [Plain [Str "Letting a damaged ", Code ("", [], []) "todos.json", Str " crash the program instead of printing a message."]]], Header 4 ("activities-8", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the sample session and then run the program again with the input ", Code ("", [], []) "2", Str " then ", Code ("", [], []) "6", Str " to see the saved tasks."]], [Plain [Str "Add a command to delete a task by number."]], [Plain [Str "Open ", Code ("", [], []) "todos.json", Str " and read the saved text. Edit it to remove a bracket and rerun."]], [Plain [Str "Add a ", Code ("", [], []) "description", Str " display to the view command."]]], Header 4 ("accessibility-practice-8", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Every menu is printed as numbered lines and each prompt is on its own line. The status words are ", Code ("", [], []) "done", Str " and ", Code ("", [], []) "not done", Str ", not symbols, so the list reads clearly in speech and braille."], Header 4 ("skills-checklist-8", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can keep records with the shared fields."]], [Plain [Str "\9744", Space, Str "I can save and load JSON."]], [Plain [Str "\9744", Space, Str "I handle a missing or damaged file."]], [Plain [Str "\9744", Space, Str "I keep ids unique."]], [Plain [Str "\9744", Space, Str "I show status in words."]]], Header 3 ("lesson-105-user-experience-and-input-validation", ["unnumbered", "unlisted"], []) [Str "Lesson 10.5: User Experience and Input Validation"], Header 4 ("reading-references-9", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions) and Chapter 16 (Compilation, Execution, and Errors)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 6.8 (io.read)"]], [Plain [Str "Matching Python lesson: Lesson 10.5 Refining User Experience and Validation"]]], Header 4 ("learning-objectives-9", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write reusable validation functions."]], [Plain [Str "Limit retries and handle the end of input."]], [Plain [Str "Write clear, accessible messages."]]], Header 4 ("concept-explanation-9", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Reusable validation functions make every menu and form consistent. ", Code ("", [], []) "ask_number(prompt, low, high, attempts)", Str " prints a prompt, reads a line, converts it, checks the range, and either returns the number or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns ", Code ("", [], []) "nil", Str " and a reason. ", Code ("", [], []) "ask_yes_no(prompt)", Str " accepts ", Code ("", [], []) "y", Str ", ", Code ("", [], []) "yes", Str ", ", Code ("", [], []) "n", Str ", and ", Code ("", [], []) "no", Str ", in any letter case."], Para [Str "Good messages say ", Emph [Str "what was wrong"], Str " and ", Emph [Str "what to do"], Str ": \"Enter a whole number from 0 to 100,\" not \"Invalid.\" They never depend on color, position, or symbols alone, and they use the same wording every time."], Para [Str "The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y."], Header 4 ("worked-example-9", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local function ask_number(prompt, low, high, attempts)
  for attempt = 1, attempts do
    print(prompt)
    local text = io.read()
    if text == nil then return nil, \"No more input.\" end
    local number = tonumber(text)
    if number and number == math.floor(number) and number >= low and number <= high then
      return math.tointeger(number)
    end
    print(string.format(\"Enter a whole number from %d to %d. You have %d attempt(s) left.\", low, high, attempts - attempt))
  end
  return nil, \"Too many invalid attempts.\"
end

local function ask_yes_no(prompt)
  while true do
    print(prompt .. \" (yes or no)\")
    local text = io.read()
    if text == nil then return nil end
    text = text:lower()
    if text == \"y\" or text == \"yes\" then return true end
    if text == \"n\" or text == \"no\" then return false end
    print(\"Please answer yes or no.\")
  end
end

local score, reason = ask_number(\"Enter a score from 0 to 100:\", 0, 100, 3)
if score then
  print(\"Accepted score: \" .. score)
else
  print(\"No score: \" .. reason)
end

local keep = ask_yes_no(\"Save this score?\")
print(\"Save answer:\", keep)
", Header 4 ("expected-behavior-or-output-9", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):"], CodeBlock ("", ["text"], []) "abc
105
88
maybe
y
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 2 attempt(s) left.
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 1 attempt(s) left.
Enter a score from 0 to 100:
Accepted score: 88
Save this score? (yes or no)
Please answer yes or no.
Save this score? (yes or no)
Save answer:	true
", Header 4 ("common-mistakes-9", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing the message \"Invalid\" without saying what is valid."]], [Plain [Str "Accepting a decimal such as 88.5 for a field that requires a whole number."]], [Plain [Str "Looping forever on bad input instead of limiting attempts."]]], Header 4 ("activities-9", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the sample input and read each message aloud."]], [Plain [Str "Run with three invalid numbers and read the final message."]], [Plain [Str "Add a function ", Code ("", [], []) "ask_text(prompt)", Str " that rejects empty answers."]], [Plain [Str "Rewrite two messages from earlier lessons so they say what to do next."]]], Header 4 ("accessibility-practice-9", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Check that every error message ends with an action the user can take, and that the same situation always produces the same words."], Header 4 ("skills-checklist-9", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write reusable validation functions."]], [Plain [Str "\9744", Space, Str "I limit retries."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]], [Plain [Str "\9744", Space, Str "I write messages that say what to do."]], [Plain [Str "\9744", Space, Str "I keep wording consistent."]]]]