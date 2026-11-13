[Header 2 ("unit-10-project-based-learning--building-text-based-applications", [], []) [Str "Unit 10: Project-Based Learning — Building Text-Based Applications"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Strong [Str "Compatibility:"], Str " All examples target Python 3.12 and newer; they avoid syntax and standard-library APIs introduced after Python 3.12."], Para [Str "This unit guides students through designing and building larger, interactive text-based applications, integrating all previously learned concepts."], Para [Strong [Str "Objectives:"]], BulletList [[Plain [Str "Practice modular programming and code organization."]], [Plain [Str "Develop a text-based interactive program."]], [Plain [Str "Apply top-down design principles."]]], HorizontalRule, Header 3 ("lesson-101-designing-your-project", ["unnumbered", "unlisted"], []) [Str "Lesson 10.1: Designing Your Project"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 9, pages 225–235"]], [Plain [Str "Matthes: Part II: Projects, pages 225–226"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Break down a larger problem into smaller, manageable parts."]], [Plain [Str "Identify the key features required for a project."]], [Plain [Str "Plan which data structures will be most suitable for my project's data."]], [Plain [Str "Outline the main steps or flow of my program."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("top-down-design", ["unnumbered", "unlisted"], []) [Str "Top-Down Design"], Para [Strong [Str "Top-down design"], Str " (stepwise refinement) breaks a complex problem into smaller, more manageable subproblems."], Para [Strong [Str "The Design Process:"]], Para [Strong [Str "1. Analyze the Problem"]], BulletList [[Plain [Str "Identify ", Strong [Str "inputs"], Str " (information the program needs)."]], [Plain [Str "Identify ", Strong [Str "outputs"], Str " (results it must produce)."]], [Plain [Str "Define the scope of the project."]]], Para [Strong [Str "2. Determine the Major Components"], SoftBreak, Str "Write a high-level algorithm in plain English:"], CodeBlock ("", [""], []) "show_greeting()
get_user_input()
calculate_cost()
print_ticket()
", Para [Strong [Str "3. Refine Each Component"], SoftBreak, Str "Repeat the design process for each component, adding detail until simple enough to code."], Header 5 ("benefits-of-top-down-design", ["unnumbered", "unlisted"], []) [Str "Benefits of Top-Down Design"], BulletList [[Plain [Strong [Str "Reduces Complexity"], Str " — Focus on one piece at a time."]], [Plain [Strong [Str "Encourages Reusability"], Str " — Functions written for one part may be useful elsewhere."]], [Plain [Strong [Str "Simplifies Debugging"], Str " — Test each component in isolation."]], [Plain [Strong [Str "Improves Collaboration"], Str " — Clear plan for assigning work."]]], Header 5 ("accessibility-considerations-for-io-design", ["unnumbered", "unlisted"], []) [Str "Accessibility Considerations for I/O Design"], BulletList [[Plain [Str "Provide ", Strong [Str "clear, descriptive prompts"], Str " for all input."]], [Plain [Str "Provide ", Strong [Str "explicit, labeled output"], Str " — avoid relying on visual formatting."]], [Plain [Str "Print ", Strong [Str "confirmation messages"], Str " after every action."]], [Plain [Str "Use consistent ", Strong [Str "output separators"], Str " like ", Code ("", [], []) "---", Str " to group information."]]], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "Top-down design applied to the command-line to-do tool. The top-level plan names the major components, and the first runnable version contains only the first component:"], CodeBlock ("", [""], []) "show_menu()
get_choice()
add_task() / view_tasks() / mark_done() / save_tasks()
repeat until the user chooses to quit
", CodeBlock ("", ["python"], []) "def show_menu():
    print(\"1. Add task\")
    print(\"2. View tasks\")
    print(\"3. Quit\")


def run():
    show_menu()
    print(\"(The choices are not implemented yet.)\")


run()
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output of example 1:"], CodeBlock ("", [""], []) "1. Add task
2. View tasks
3. Quit
(The choices are not implemented yet.)
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Starting to code the whole program at once instead of building and testing one component at a time."]], [Plain [Str "Writing a design that names steps too vague to turn into code, such as \"handle the data\"."]], [Plain [Str "Forgetting the messages: a design that lists operations but not what the user sees after each one."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write the top-level design for the text adventure as a numbered list of components."]], [Plain [Str "Refine one component of your design into three smaller steps."]], [Plain [Str "Write the exact wording of five prompts and messages that your project will use."]], [Plain [Str "Explain in two sentences how the design lets you test one function in isolation."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Write the design as a numbered list and read it aloud before coding. Decide the wording of every prompt and message now, and check that none depends on color, layout, or symbols alone."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can break down a larger problem into smaller, manageable parts."]], [Plain [Str "\9744", Space, Str "I can identify the key features required for a project."]], [Plain [Str "\9744", Space, Str "I can plan which data structures will be most suitable for my project's data."]], [Plain [Str "\9744", Space, Str "I can outline the main steps or flow of my program."]]], HorizontalRule, Header 3 ("lesson-102-building-a-text-based-adventure-game-part-1", ["unnumbered", "unlisted"], []) [Str "Lesson 10.2: Building a Text-Based Adventure Game (Part 1)"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 6, pages 105–111"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Design a way to represent different locations in a text-based game."]], [Plain [Str "Implement player movement based on user commands."]], [Plain [Str "Update and track the player's current location."]], [Plain [Str "Parse simple commands from user input."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("room-definition-and-movement", ["unnumbered", "unlisted"], []) [Str "Room Definition and Movement"], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "room_descriptions = {
    \"start_room\": {
        \"description\": \"A dimly lit cave. A narrow passage leads north.\",
        \"exits\": {\"north\": \"tunnel\"},
        \"items\": [],
    },
    \"tunnel\": {
        \"description\": \"A damp tunnel. Passages lead south and east.\",
        \"exits\": {\"south\": \"start_room\", \"east\": \"clearing\"},
        \"items\": [],
    },
    \"clearing\": {
        \"description\": \"A quiet clearing. A small antechamber lies to the north.\",
        \"exits\": {\"west\": \"tunnel\", \"north\": \"locked_door_room\"},
        \"items\": [],
    },
    \"locked_door_room\": {
        \"description\": \"A chamber with a heavy locked door to the north.\",
        \"exits\": {\"south\": \"clearing\"},
        \"items\": [],
    },
    \"treasure_room\": {
        \"description\": \"You found the treasure. You win!\",
        \"exits\": {},
        \"items\": [],
    },
}

current_room = \"start_room\"

while True:
    print(\"---\")
    print(room_descriptions[current_room][\"description\"])
    command = input(\"What do you want to do? \").lower()

    if command in room_descriptions[current_room][\"exits\"]:
        current_room = room_descriptions[current_room][\"exits\"][command]
    elif command == \"quit\":
        print(\"Exiting game. Goodbye!\")
        break
    else:
        print(\"I don't understand that command or you can't go that way.\")
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Sample run typing ", Code ("", [], []) "north", Str ", ", Code ("", [], []) "east", Str ", ", Code ("", [], []) "north", Str ", ", Code ("", [], []) "north", Str ", ", Code ("", [], []) "quit", Str " (typed input shown after each prompt):"], CodeBlock ("", [""], []) "---
A dimly lit cave. A narrow passage leads north.
What do you want to do? north
---
A damp tunnel. Passages lead south and east.
What do you want to do? east
---
A quiet clearing. A small antechamber lies to the north.
What do you want to do? north
---
A chamber with a heavy locked door to the north.
What do you want to do? north
I don't understand that command or you can't go that way.
---
A chamber with a heavy locked door to the north.
What do you want to do? quit
Exiting game. Goodbye!
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Looking up a direction that is not in ", Code ("", [], []) "exits", Str " with square brackets, which raises a ", Code ("", [], []) "KeyError", Str ". Use ", Code ("", [], []) "in", Str " to test first."]], [Plain [Str "Forgetting that ", Code ("", [], []) "input()", Str " raises ", Code ("", [], []) "EOFError", Str " at the end of piped input; scripted tests should end with ", Code ("", [], []) "quit", Str "."]], [Plain [Str "Misspelling a room name in ", Code ("", [], []) "exits", Str ", so a move leads to a room that does not exist."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace north, east, north, north, quit and record the room after each command."]], [Plain [Str "Try west from start_room and verify that the location does not change."]], [Plain [Str "Verify that north from locked_door_room is rejected and leaves the player in that room."]], [Plain [Str "Write a loop that checks that every exit names a real room."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each turn prints a separator line, the description, and the prompt, so a whole turn can be read in order. Listen to one turn from start to finish to confirm that a player could follow it without seeing the screen."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can design a way to represent different locations in a text-based game."]], [Plain [Str "\9744", Space, Str "I can implement player movement based on user commands."]], [Plain [Str "\9744", Space, Str "I can update and track the player's current location."]], [Plain [Str "\9744", Space, Str "I can parse simple commands from user input."]]], HorizontalRule, Header 3 ("lesson-103-building-a-text-based-adventure-game-part-2", ["unnumbered", "unlisted"], []) [Str "Lesson 10.3: Building a Text-Based Adventure Game (Part 2)"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 6 (Dictionaries) and Chapter 8 (Functions)"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Add items to locations and manage a player's inventory."]], [Plain [Str "Implement commands for picking up and dropping items."]], [Plain [Str "Design and implement a simple puzzle."]], [Plain [Str "Define win/lose conditions for the game."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("adding-items-inventory-and-puzzles", ["unnumbered", "unlisted"], []) [Str "Adding Items, Inventory, and Puzzles"], Para [Str "These rules are the shared text-adventure specification for every language track: five rooms (", Code ("", [], []) "start_room", Str ", ", Code ("", [], []) "tunnel", Str ", ", Code ("", [], []) "clearing", Str ", ", Code ("", [], []) "locked_door_room", Str ", and ", Code ("", [], []) "treasure_room", Str "). The player starts in ", Code ("", [], []) "start_room", Str "; its north exit leads to ", Code ("", [], []) "tunnel", Str ". From ", Code ("", [], []) "tunnel", Str ", south returns to ", Code ("", [], []) "start_room", Str " and east leads to ", Code ("", [], []) "clearing", Str ". From ", Code ("", [], []) "clearing", Str ", west returns to ", Code ("", [], []) "tunnel", Str " and north leads to ", Code ("", [], []) "locked_door_room", Str ". From ", Code ("", [], []) "locked_door_room", Str ", south returns to ", Code ("", [], []) "clearing", Str "; north leads to ", Code ("", [], []) "treasure_room", Str " only after the player has taken the shiny key from ", Code ("", [], []) "start_room", Str " and used it in ", Code ("", [], []) "locked_door_room", Str ". The supported commands are ", Code ("", [], []) "north", Str ", ", Code ("", [], []) "south", Str ", ", Code ("", [], []) "east", Str ", ", Code ("", [], []) "west", Str ", ", Code ("", [], []) "take shiny key", Str ", ", Code ("", [], []) "use shiny key", Str ", and ", Code ("", [], []) "quit", Str ". Reaching ", Code ("", [], []) "treasure_room", Str " ends the game."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "rooms = {
    \"start_room\": {
        \"description\": \"A dimly lit cave. A shiny key rests on the ground.\",
        \"exits\": {\"north\": \"tunnel\"},
        \"items\": [\"shiny key\"],
    },
    \"tunnel\": {
        \"description\": \"A damp tunnel. Passages lead south and east.\",
        \"exits\": {\"south\": \"start_room\", \"east\": \"clearing\"},
        \"items\": [],
    },
    \"clearing\": {
        \"description\": \"A quiet clearing. A small antechamber lies to the north.\",
        \"exits\": {\"west\": \"tunnel\", \"north\": \"locked_door_room\"},
        \"items\": [],
    },
    \"locked_door_room\": {
        \"description\": \"A chamber with a heavy locked door to the north.\",
        \"exits\": {\"south\": \"clearing\", \"north\": \"treasure_room\"},
        \"items\": [],
    },
    \"treasure_room\": {
        \"description\": \"You found the treasure. You win!\",
        \"exits\": {},
        \"items\": [],
    },
}

current_room = \"start_room\"
player_inventory = []
door_locked = True

while True:
    print(\"\\n\" + rooms[current_room][\"description\"])
    if current_room == \"treasure_room\":
        break
    if rooms[current_room][\"items\"]:
        print(f\"You see: {', '.join(rooms[current_room]['items'])}\")
    print(f\"Your inventory: {', '.join(player_inventory) if player_inventory else 'empty'}\")

    if current_room == \"treasure_room\":
        break

    command = input(\"What do you want to do? \").strip().lower()

    if command == \"take shiny key\" and \"shiny key\" in rooms[current_room][\"items\"]:
        player_inventory.append(\"shiny key\")
        rooms[current_room][\"items\"].remove(\"shiny key\")
        print(\"You picked up the shiny key.\")
    elif command == \"use shiny key\" and current_room == \"locked_door_room\" and \"shiny key\" in player_inventory:
        door_locked = False
        print(\"You unlocked the door!\")
    elif command in rooms[current_room][\"exits\"]:
        if current_room == \"locked_door_room\" and command == \"north\" and door_locked:
            print(\"The door is locked! You need a key.\")
        else:
            current_room = rooms[current_room][\"exits\"][command]
    elif command == \"quit\":
        print(\"You quit the adventure.\")
        break
    else:
        print(\"Invalid command. Use a direction, 'take shiny key', 'use shiny key', or 'quit'.\")
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Sample play (typed input shown after each prompt). The player reaches the chamber, finds the door locked, returns to take the key, then unlocks the door and wins:"], CodeBlock ("", [""], []) "
A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do? north

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do? north
The door is locked! You need a key.

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do? south

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do? take shiny key
You picked up the shiny key.

A dark cave.
Your inventory: shiny key
What do you want to do? north

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do? use shiny key
You unlocked the door!

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do? north

A glittering room full of treasure. You win!
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Making the door's locked state part of the exits so the \"locked\" message can never be reached."]], [Plain [Str "Defining an exit to a room that is missing from the ", Code ("", [], []) "rooms", Str " dictionary, which crashes when the player arrives."]], [Plain [Str "Printing a fixed room description that still mentions an item after the player has taken it."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Play the program with the sample commands and follow each turn on paper."]], [Plain [Str "Try ", Code ("", [], []) "use shiny key", Str " in the cave and describe what happens."]], [Plain [Str "Add a second item and require both to open the door."]], [Plain [Str "List the game's state (location, inventory, door) and say which command changes each part."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "The room description never mentions the key. A separate 'You see:' line lists items, so the description stays true after the key is taken and the screen reader announces the current state."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can add items to locations and manage a player's inventory."]], [Plain [Str "\9744", Space, Str "I can implement commands for picking up and dropping items."]], [Plain [Str "\9744", Space, Str "I can design and implement a simple puzzle."]], [Plain [Str "\9744", Space, Str "I can define win/lose conditions for the game."]]], HorizontalRule, Header 3 ("lesson-104-developing-a-command-line-tool", ["unnumbered", "unlisted"], []) [Str "Lesson 10.4: Developing a Command-Line Tool"], Header 4 ("canonical-to-do-record-and-required-operations", ["unnumbered", "unlisted"], []) [Str "Canonical To-Do Record and Required Operations"], Para [Str "Every task must preserve exactly these fields:"], CodeBlock ("", ["python"], []) "task = {
    \"id\": 1,
    \"title\": \"Practice Python\",
    \"description\": \"Complete the shared dataset exercises\",
    \"done\": False,
    \"created_at\": \"2025-01-15T09:00:00Z\",
}
", Para [Str "Design the command-line interface around these operations:"], Table ("", [], []) (Caption Nothing []) [(AlignDefault, (ColWidth 0.5)), (AlignDefault, (ColWidth 0.5))] (TableHead ("", [], []) [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Operation"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Required behavior"]]]]) [(TableBody ("", [], []) (RowHeadColumns 0) [] [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Add"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Reject a blank title; assign a unique integer ID; initialize ", Code ("", [], []) "done", Str " to ", Code ("", [], []) "False", Str "; preserve all five fields"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "List"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Display tasks in ID order and state whether each is complete"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Complete/update"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Find by ID, update ", Code ("", [], []) "done", Str ", and report a missing or invalid ID"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Delete"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Remove by ID and report a missing or invalid ID"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Save"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Serialize the complete list as JSON"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Load"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Validate that the top level is a list and every task has exactly the five required fields and appropriate value types"]]]])] (TableFoot ("", [], []) []), Para [Str "Use the following function boundaries as a design scaffold. Implement and test each function as a separate exercise; this outline intentionally does not provide the project solution."], CodeBlock ("", ["python"], []) "def add_task(tasks, title, description, created_at):
    # TODO: validate title, allocate a unique ID, and append a five-field record
    raise NotImplementedError


def list_tasks(tasks):
    # TODO: display records in a stable order
    raise NotImplementedError


def update_task(tasks, task_id, *, done=None, title=None, description=None):
    # TODO: locate by ID, validate updates, and report a missing ID
    raise NotImplementedError


def delete_task(tasks, task_id):
    # TODO: remove by ID and report a missing ID
    raise NotImplementedError


def save_tasks(tasks, path):
    # TODO: write all five fields as JSON
    raise NotImplementedError


def load_tasks(path):
    # TODO: handle missing/malformed JSON and validate every record
    raise NotImplementedError
", Para [Str "Do not substitute list positions for IDs. Deleting or sorting a task must not change the identity of any remaining task. Use a deterministic timestamp fixture in tests; do not call the wall clock in expected-output tests."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can design an interactive menu system for a tool."]], [Plain [Str "\9744", Space, Str "I can use a ", Code ("", [], []) "while", Str " loop to maintain continuous user interaction."]], [Plain [Str "\9744", Space, Str "I can break down the tool's functionality into separate functions."]], [Plain [Str "\9744", Space, Str "I can implement file I/O to save and load data."]]], HorizontalRule, Header 3 ("lesson-105-refinement-and-user-experience", ["unnumbered", "unlisted"], []) [Str "Lesson 10.5: Refinement and User Experience"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 10 (Files and Exceptions), the sections on exceptions"]], [Plain [Str "Zelle: Chapter 8 (Loop Structures and Booleans)"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write clear, descriptive prompts for user input."]], [Plain [Str "Handle invalid input gracefully using ", Code ("", [], []) "try-except", Str "."]], [Plain [Str "Provide helpful error messages."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("principles-for-accessible-text-programs", ["unnumbered", "unlisted"], []) [Str "Principles for Accessible Text Programs"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Strong [Str "Clear prompts"], Str " — Tell the user exactly what to enter and in what format."]], [Plain [Strong [Str "Consistent output"], Str " — Use the same format for similar information."]], [Plain [Strong [Str "Graceful error handling"], Str " — Never let the program crash on bad input."]], [Plain [Strong [Str "Helpful error messages"], Str " — Tell the user what went wrong and how to fix it."]], [Plain [Strong [Str "\"Help\" commands"], Str " — Provide a way to list available commands."]], [Plain [Strong [Str "Confirmation messages"], Str " — Confirm every action taken."]]], Header 5 ("robust-input-validation", ["unnumbered", "unlisted"], []) [Str "Robust Input Validation"], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "def get_positive_number(prompt):
    \"\"\"Prompts user until a positive integer is entered.\"\"\"
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print(\"Please enter a positive number.\")
        except ValueError:
            print(\"Invalid input. Please enter a whole number.\")


age = get_positive_number(\"Enter your age: \")
print(f\"You entered age: {age}\")
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Sample run typing ", Code ("", [], []) "abc", Str ", ", Code ("", [], []) "-4", Str ", ", Code ("", [], []) "0", Str ", ", Code ("", [], []) "16", Str " (typed input shown after each prompt):"], CodeBlock ("", [""], []) "Enter your age: abc
Invalid input. Please enter a whole number.
Enter your age: -4
Please enter a positive number.
Enter your age: 0
Please enter a positive number.
Enter your age: 16
You entered age: 16
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing the message \"Invalid\" without saying what is valid."]], [Plain [Str "Accepting a decimal such as 88.5 for a field that requires a whole number."]], [Plain [Str "Looping forever on bad input instead of limiting attempts or providing a way to quit."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the example typing ", Code ("", [], []) "abc", Str ", ", Code ("", [], []) "-4", Str ", ", Code ("", [], []) "0", Str ", and ", Code ("", [], []) "16", Str ", and read each message aloud."]], [Plain [Str "Add an upper limit of 120 and a message that names it."]], [Plain [Str "Write ", Code ("", [], []) "get_yes_no(prompt)", Str " that accepts only yes or no in any letter case."]], [Plain [Str "Rewrite two messages from earlier lessons so they say what to do next."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Check that every error message ends with an action the user can take, and that the same situation always produces the same words. Test with your screen reader that a message is announced before the next prompt appears."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write clear, descriptive prompts for user input."]], [Plain [Str "\9744", Space, Str "I can handle invalid input gracefully using ", Code ("", [], []) "try-except", Str "."]], [Plain [Str "\9744", Space, Str "I can provide helpful error messages."]]], HorizontalRule]