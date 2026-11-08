# Unit 10: Project-Based Learning — Building Text-Based Applications

## Overview

**Compatibility:** All examples target Python 3.12 and newer; they avoid syntax and standard-library APIs introduced after Python 3.12.

This unit guides students through designing and building larger, interactive text-based applications, integrating all previously learned concepts.

**Objectives:**
- Practice modular programming and code organization.
- Develop a text-based interactive program.
- Apply top-down design principles.

---

## Lesson 10.1: Designing Your Project

### Reading References
- Zelle: Chapter 9, pages 225–235
- Matthes: Part II: Projects, pages 225–226

### Learning Objectives
- Break down a larger problem into smaller, manageable parts.
- Identify the key features required for a project.
- Plan which data structures will be most suitable for my project's data.
- Outline the main steps or flow of my program.

### Concept Explanation

#### Top-Down Design

**Top-down design** (stepwise refinement) breaks a complex problem into smaller, more manageable subproblems.

**The Design Process:**

**1. Analyze the Problem**
- Identify **inputs** (information the program needs).
- Identify **outputs** (results it must produce).
- Define the scope of the project.

**2. Determine the Major Components**
Write a high-level algorithm in plain English:
```
show_greeting()
get_user_input()
calculate_cost()
print_ticket()
```

**3. Refine Each Component**
Repeat the design process for each component, adding detail until simple enough to code.

#### Benefits of Top-Down Design

- **Reduces Complexity** — Focus on one piece at a time.
- **Encourages Reusability** — Functions written for one part may be useful elsewhere.
- **Simplifies Debugging** — Test each component in isolation.
- **Improves Collaboration** — Clear plan for assigning work.

#### Accessibility Considerations for I/O Design

- Provide **clear, descriptive prompts** for all input.
- Provide **explicit, labeled output** — avoid relying on visual formatting.
- Print **confirmation messages** after every action.
- Use consistent **output separators** like `---` to group information.

### Worked Example

Top-down design applied to the command-line to-do tool. The top-level plan names the major components, and the first runnable version contains only the first component:
```
show_menu()
get_choice()
add_task() / view_tasks() / mark_done() / save_tasks()
repeat until the user chooses to quit
```
```python
def show_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")


def run():
    show_menu()
    print("(The choices are not implemented yet.)")


run()
```

### Expected Behavior or Output

Output of example 1:
```
1. Add task
2. View tasks
3. Quit
(The choices are not implemented yet.)
```

### Common Mistakes

1. Starting to code the whole program at once instead of building and testing one component at a time.
2. Writing a design that names steps too vague to turn into code, such as "handle the data".
3. Forgetting the messages: a design that lists operations but not what the user sees after each one.

### Activities

1. Write the top-level design for the text adventure as a numbered list of components.
2. Refine one component of your design into three smaller steps.
3. Write the exact wording of five prompts and messages that your project will use.
4. Explain in two sentences how the design lets you test one function in isolation.

### Accessibility Practice

Write the design as a numbered list and read it aloud before coding. Decide the wording of every prompt and message now, and check that none depends on color, layout, or symbols alone.

### Skills Checklist

- [ ] I can break down a larger problem into smaller, manageable parts.
- [ ] I can identify the key features required for a project.
- [ ] I can plan which data structures will be most suitable for my project's data.
- [ ] I can outline the main steps or flow of my program.

---

## Lesson 10.2: Building a Text-Based Adventure Game (Part 1)

### Reading References
- Matthes: Chapter 6, pages 105–111

### Learning Objectives
- Design a way to represent different locations in a text-based game.
- Implement player movement based on user commands.
- Update and track the player's current location.
- Parse simple commands from user input.

### Concept Explanation

#### Room Definition and Movement

### Worked Example

```python
room_descriptions = {
    "start_room": {
        "description": "A dimly lit cave. A shiny key rests on the ground.",
        "exits": {"north": "tunnel"},
        "items": ["shiny key"],
    },
    "tunnel": {
        "description": "A damp tunnel. Passages lead south and east.",
        "exits": {"south": "start_room", "east": "clearing"},
        "items": [],
    },
    "clearing": {
        "description": "A quiet clearing. A small antechamber lies to the north.",
        "exits": {"west": "tunnel", "north": "locked_door_room"},
        "items": [],
    },
    "locked_door_room": {
        "description": "A chamber with a heavy locked door to the north.",
        "exits": {"south": "clearing"},
        "items": [],
    },
    "treasure_room": {
        "description": "You found the treasure. You win!",
        "exits": {},
        "items": [],
    },
}

current_room = "start_room"

while True:
    print("---")
    print(room_descriptions[current_room]["description"])
    command = input("What do you want to do? ").lower()

    if command in room_descriptions[current_room]["exits"]:
        current_room = room_descriptions[current_room]["exits"][command]
    elif command == "quit":
        print("Exiting game. Goodbye!")
        break
    else:
        print("I don't understand that command or you can't go that way.")
```

### Expected Behavior or Output

Sample run typing `north`, `east`, `west`, `up`, `south`, `quit` (typed input shown after each prompt):
```
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do? north
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do? east
---
You've reached a small, sunny clearing. A faint path leads WEST.
What do you want to do? west
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do? up
I don't understand that command or you can't go that way.
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do? south
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do? quit
Exiting game. Goodbye!
```

### Common Mistakes

1. Looking up a direction that is not in `exits` with square brackets, which raises a `KeyError`. Use `in` to test first.
2. Forgetting that `input()` raises `EOFError` at the end of piped input; scripted tests should end with `quit`.
3. Misspelling a room name in `exits`, so a move leads to a room that does not exist.

### Activities

1. Trace the six commands in the sample run by hand and write the room after each one.
2. Add a fourth room reached from the clearing and test it.
3. Add the short commands `n`, `s`, `e`, and `w`.
4. Write a loop that checks that every exit names a real room.

### Accessibility Practice

Each turn prints a separator line, the description, and the prompt, so a whole turn can be read in order. Listen to one turn from start to finish to confirm that a player could follow it without seeing the screen.

### Skills Checklist

- [ ] I can design a way to represent different locations in a text-based game.
- [ ] I can implement player movement based on user commands.
- [ ] I can update and track the player's current location.
- [ ] I can parse simple commands from user input.

---

## Lesson 10.3: Building a Text-Based Adventure Game (Part 2)

### Reading References
- Matthes: Chapter 6 (Dictionaries) and Chapter 8 (Functions)

### Learning Objectives
- Add items to locations and manage a player's inventory.
- Implement commands for picking up and dropping items.
- Design and implement a simple puzzle.
- Define win/lose conditions for the game.

### Concept Explanation

#### Adding Items, Inventory, and Puzzles

These rules are the shared text-adventure specification for every language track: three rooms (`start`, `locked_door_room`, `treasure_room`); commands `north`, `south`, `east`, `west`, `take shiny key`, `use shiny key`, and `quit`; the door between the chamber and the treasure room stays locked until the player uses the key; reaching the treasure room ends the game.

### Worked Example

```python
rooms = {
<<<<<<< HEAD
    "start_room": {
        "description": "A dimly lit cave. A shiny key rests on the ground.",
        "exits": {"north": "tunnel"},
        "items": ["shiny key"],
    },
    "tunnel": {
        "description": "A damp tunnel. Passages lead south and east.",
        "exits": {"south": "start_room", "east": "clearing"},
        "items": [],
    },
    "clearing": {
        "description": "A quiet clearing. A small antechamber lies to the north.",
        "exits": {"west": "tunnel", "north": "locked_door_room"},
        "items": [],
    },
    "locked_door_room": {
        "description": "A chamber with a heavy locked door to the north.",
        "exits": {"south": "clearing"},
        "items": [],
    },
    "treasure_room": {
        "description": "You found the treasure. You win!",
        "exits": {},
        "items": [],
    },
=======
    "start": {
        "description": "A dark cave.",
        "exits": {"north": "locked_door_room"},
        "items": ["shiny key"]
    },
    "locked_door_room": {
        "description": "A small chamber with a heavy door to the NORTH.",
        "exits": {"south": "start", "north": "treasure_room"},
        "items": []
    },
    "treasure_room": {
        "description": "A glittering room full of treasure. You win!",
        "exits": {"south": "locked_door_room"},
        "items": []
    }
>>>>>>> 2067a20 (curriculum clearning and updates)
}

current_room = "start_room"
player_inventory = []
door_locked = True

while True:
    print("\n" + rooms[current_room]["description"])
    if current_room == "treasure_room":
        break
    if rooms[current_room]["items"]:
        print(f"You see: {', '.join(rooms[current_room]['items'])}")
    print(f"Your inventory: {', '.join(player_inventory) if player_inventory else 'empty'}")

    if current_room == "treasure_room":
        break

    command = input("What do you want to do? ").strip().lower()

    if command == "take shiny key" and "shiny key" in rooms[current_room]["items"]:
        player_inventory.append("shiny key")
        rooms[current_room]["items"].remove("shiny key")
        print("You picked up the shiny key.")
    elif command == "use shiny key" and current_room == "locked_door_room" and "shiny key" in player_inventory:
        door_locked = False
        print("You unlocked the door!")
    elif command in rooms[current_room]["exits"]:
        if current_room == "locked_door_room" and command == "north" and door_locked:
            print("The door is locked! You need a key.")
        else:
            current_room = rooms[current_room]["exits"][command]
    elif command == "quit":
<<<<<<< HEAD
        print("You quit the adventure.")
=======
        print("Exiting game. Goodbye!")
>>>>>>> 2067a20 (curriculum clearning and updates)
        break
    else:
        print("Invalid command. Use a direction, 'take shiny key', 'use shiny key', or 'quit'.")
```

### Expected Behavior or Output

Sample play (typed input shown after each prompt). The player reaches the chamber, finds the door locked, returns to take the key, then unlocks the door and wins:
```

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
```

### Common Mistakes

1. Making the door's locked state part of the exits so the "locked" message can never be reached.
2. Defining an exit to a room that is missing from the `rooms` dictionary, which crashes when the player arrives.
3. Printing a fixed room description that still mentions an item after the player has taken it.

### Activities

1. Play the program with the sample commands and follow each turn on paper.
2. Try `use shiny key` in the cave and describe what happens.
3. Add a second item and require both to open the door.
4. List the game's state (location, inventory, door) and say which command changes each part.

### Accessibility Practice

The room description never mentions the key. A separate 'You see:' line lists items, so the description stays true after the key is taken and the screen reader announces the current state.

### Skills Checklist

- [ ] I can add items to locations and manage a player's inventory.
- [ ] I can implement commands for picking up and dropping items.
- [ ] I can design and implement a simple puzzle.
- [ ] I can define win/lose conditions for the game.

---

## Lesson 10.4: Developing a Command-Line Tool

<<<<<<< HEAD
### Canonical To-Do Record and Required Operations

Every task must preserve exactly these fields:

```python
task = {
    "id": 1,
    "title": "Practice Python",
    "description": "Complete the shared dataset exercises",
    "done": False,
    "created_at": "2025-01-15T09:00:00Z",
}
```

Design the command-line interface around these operations:

| Operation | Required behavior |
|---|---|
| Add | Reject a blank title; assign a unique integer ID; initialize `done` to `False`; preserve all five fields |
| List | Display tasks in ID order and state whether each is complete |
| Complete/update | Find by ID, update `done`, and report a missing or invalid ID |
| Delete | Remove by ID and report a missing or invalid ID |
| Save | Serialize the complete list as JSON |
| Load | Validate that the top level is a list and every task has exactly the five required fields and appropriate value types |

Use the following function boundaries as a design scaffold. Implement and test each function as a separate exercise; this outline intentionally does not provide the project solution.

```python
def add_task(tasks, title, description, created_at):
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
```

Do not substitute list positions for IDs. Deleting or sorting a task must not change the identity of any remaining task. Use a deterministic timestamp fixture in tests; do not call the wall clock in expected-output tests.
=======
### Reading References
- Matthes: Chapter 10 (Files and Exceptions), the section on storing data

### Learning Objectives
- Design an interactive menu system for a tool.
- Use a `while` loop to maintain continuous user interaction.
- Break down the tool's functionality into separate functions.
- Implement file I/O to save and load data.

### Concept Explanation

#### Simple To-Do List Tool

The task fields `id`, `title`, `description`, `done`, and `created_at` are the shared to-do record used in every language track. The menu reports status with the words "done" and "not done", never with symbols or color alone.

### Worked Example

```python
import json
from datetime import datetime

TODO_FILE = 'todos.json'
todos = []


def load_todos():
    global todos
    try:
        with open(TODO_FILE, 'r') as f:
            todos = json.load(f)
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No existing tasks found.")
        todos = []
    except json.JSONDecodeError:
        print("Error: todos.json is not valid JSON. Starting with an empty list.")
        todos = []


def save_todos():
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)
    print("Tasks saved.")


def next_id():
    return max((task["id"] for task in todos), default=0) + 1


def add_task(title, description=""):
    if not title.strip():
        print("A title is required.")
        return
    todos.append({
        "id": next_id(),
        "title": title.strip(),
        "description": description.strip(),
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    })
    print(f"Task '{title.strip()}' added.")


def view_tasks():
    if not todos:
        print("No tasks in your list.")
        return
    print("--- Your To-Do List ---")
    for task in todos:
        status = "done" if task["done"] else "not done"
        print(f"{task['id']}. {task['title']} ({status})")
    print("-----------------------")


def mark_completed(task_id_text):
    try:
        task_id = int(task_id_text)
    except ValueError:
        print("Please enter a whole number.")
        return
    for task in todos:
        if task["id"] == task_id:
            task["done"] = True
            print(f"Task '{task['title']}' marked as done.")
            return
    print("No task has that number.")


def main_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Quit")
    print("-----------------------")


load_todos()

while True:
    main_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        add_task(title, description)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        task_num = input("Enter task number to mark done: ")
        mark_completed(task_num)
    elif choice == '4':
        save_todos()
    elif choice == '5':
        load_todos()
    elif choice == '6':
        save_todos()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
```

### Expected Behavior or Output

Sample session (typed input shown after each prompt; the input sequence is 1, a task, 1, a second task, 2, 3, 2, 3, 7, 2, 6):
```
No existing tasks found.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6): 1
Enter task title: Study programming
Enter task description: Finish Unit 10
Task 'Study programming' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6): 1
Enter task title: Review scores
Enter task description: Check the four scores
Task 'Review scores' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6): 2
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
Enter your choice (1-6): 3
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------
Enter task number to mark done: 2
Task 'Review scores' marked as done.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6): 3
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------
Enter task number to mark done: 7
No task has that number.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6): 2
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
Enter your choice (1-6): 6
Tasks saved.
Goodbye!
```

### Common Mistakes

1. Saving the file but never loading it, so tasks disappear between runs.
2. Reusing a deleted task's id, which can confuse saved references.
3. Letting a damaged `todos.json` crash the program instead of printing a message.

### Activities

1. Run the sample session, then run the program again typing `2` and `6` to see the saved tasks.
2. Add a command to delete a task by number.
3. Open `todos.json` and read the saved text. Edit it to remove a bracket and run the program again.
4. Show each task's description in the view command.

### Accessibility Practice

Every menu is printed as numbered lines and every prompt is on its own line. The status words are `done` and `not done`, not symbols, so the list reads clearly in speech and braille.
>>>>>>> 2067a20 (curriculum clearning and updates)

### Skills Checklist

- [ ] I can design an interactive menu system for a tool.
- [ ] I can use a `while` loop to maintain continuous user interaction.
- [ ] I can break down the tool's functionality into separate functions.
- [ ] I can implement file I/O to save and load data.

---

## Lesson 10.5: Refinement and User Experience

### Reading References
- Matthes: Chapter 10 (Files and Exceptions), the sections on exceptions
- Zelle: Chapter 8 (Loop Structures and Booleans)

### Learning Objectives
- Write clear, descriptive prompts for user input.
- Handle invalid input gracefully using `try-except`.
- Provide helpful error messages.

### Concept Explanation

#### Principles for Accessible Text Programs

1. **Clear prompts** — Tell the user exactly what to enter and in what format.
2. **Consistent output** — Use the same format for similar information.
3. **Graceful error handling** — Never let the program crash on bad input.
4. **Helpful error messages** — Tell the user what went wrong and how to fix it.
5. **"Help" commands** — Provide a way to list available commands.
6. **Confirmation messages** — Confirm every action taken.

#### Robust Input Validation

### Worked Example

```python
def get_positive_number(prompt):
    """Prompts user until a positive integer is entered."""
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


age = get_positive_number("Enter your age: ")
print(f"You entered age: {age}")
```

### Expected Behavior or Output

Sample run typing `abc`, `-4`, `0`, `16` (typed input shown after each prompt):
```
Enter your age: abc
Invalid input. Please enter a whole number.
Enter your age: -4
Please enter a positive number.
Enter your age: 0
Please enter a positive number.
Enter your age: 16
You entered age: 16
```

### Common Mistakes

1. Writing the message "Invalid" without saying what is valid.
2. Accepting a decimal such as 88.5 for a field that requires a whole number.
3. Looping forever on bad input instead of limiting attempts or providing a way to quit.

### Activities

1. Run the example typing `abc`, `-4`, `0`, and `16`, and read each message aloud.
2. Add an upper limit of 120 and a message that names it.
3. Write `get_yes_no(prompt)` that accepts only yes or no in any letter case.
4. Rewrite two messages from earlier lessons so they say what to do next.

### Accessibility Practice

Check that every error message ends with an action the user can take, and that the same situation always produces the same words. Test with your screen reader that a message is announced before the next prompt appears.

### Skills Checklist

- [ ] I can write clear, descriptive prompts for user input.
- [ ] I can handle invalid input gracefully using `try-except`.
- [ ] I can provide helpful error messages.

---
