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
        "description": "You are in a dimly lit cave. There's a narrow passage to the NORTH.",
        "exits": {"north": "tunnel"}
    },
    "tunnel": {
        "description": "The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.",
        "exits": {"south": "start_room", "east": "clearing"}
    },
    "clearing": {
        "description": "You've reached a small, sunny clearing. A faint path leads WEST.",
        "exits": {"west": "tunnel"}
    }
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
}

current_room = "start"
player_inventory = []
door_locked = True

while True:
    print("\n" + rooms[current_room]["description"])
    if current_room == "treasure_room":
        break
    if rooms[current_room]["items"]:
        print(f"You see: {', '.join(rooms[current_room]['items'])}")
    print(f"Your inventory: {', '.join(player_inventory) if player_inventory else 'empty'}")

    command = input("What do you want to do? ").lower()

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
        print("Exiting game. Goodbye!")
        break
    else:
        print("I don't understand that command.")
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

# Unit 11: Capstone Project — Accessible Personal Data Manager

## Overview

Students develop a fully functional personal data manager that is built to work with a screen reader and keyboard. The program keeps a list of structured records, lets the user add, view, search, change, complete, and delete them, and saves them to a JSON file. The Python track builds it as a small local web application with NiceGUI. The other language tracks build a text-based version with the same records, rules, and tests.

**Project goal.** Build a simple application that manages a list of structured items.

**Shared record schema (all general-purpose language tracks).** Every record has these fields: `id` (unique whole number), `title`, `description`, `category`, `created_at`, and `updated_at` (ISO 8601 text). A project may add fields but must not remove these. This course adds the optional field `done` (true or false).

**Project options (each builds on the shared schema):**
- Contact Manager: add phone and email fields
- Book/Movie Tracker: add author/director and status fields
- Simple To-Do List: add a done field and due date
- Simple Inventory: add quantity and location fields

**Shared sample data.** Use these three records for demonstrations and tests:
```json
[
  {"id": 1, "title": "Notebook", "description": "Course notes", "category": "supplies", "created_at": "2026-01-15T09:00:00", "updated_at": "2026-01-15T09:00:00"},
  {"id": 2, "title": "Pencil", "description": "Box of 10", "category": "supplies", "created_at": "2026-01-15T09:05:00", "updated_at": "2026-01-15T09:05:00"},
  {"id": 3, "title": "Study plan", "description": "Weekly schedule", "category": "planning", "created_at": "2026-01-15T09:10:00", "updated_at": "2026-01-15T09:10:00"}
]
```

**Shared acceptance tests.**
1. Adding a record with an empty title is rejected with a clear message.
2. A new record receives an unused `id`.
3. Updating a record changes `updated_at` but not `created_at`.
4. Deleting a record removes only that record.
5. Saving and reloading preserves all fields and values.
6. Every message and control can be used without color or a mouse (checked by hand, Lesson 11.5).

**Core functionality requirements.**
1. **Add New Item** — a form to enter the details of a new item.
2. **View All Items** — display items in a clear, accessible list.
3. **Edit Item** — select an existing item and change its details.
4. **Delete Item** — remove an item from the collection.
5. **Save/Load Data** — keep the data in a JSON file.
6. **Search Items** — find items whose title or description contains the entered text.
7. **Mark an Item Complete** — set the optional `done` field; this updates `updated_at`.

**Verified code.** The code in this unit is available as files in the `PYTHON/capstone/` folder of this repository. It was run with Python 3.12 and NiceGUI 3.19.0. The NiceGUI tests simulate the page in Python; they do not replace testing with a real browser and your own screen reader.

**Lessons in this unit.** 11.1 Introduction to NiceGUI; 11.2 Data Model and Storage; 11.3 Displaying and Searching Items; 11.4 Changing, Completing, and Deleting Items; 11.5 Testing, Documentation, and Final Submission.

---

## Lesson 11.1: Introduction to NiceGUI

### Reading References
- NiceGUI documentation (official site, nicegui.io); check the documentation for the version you installed
- Matthes: Chapter 8 (Functions) and Chapter 9 (Classes) for the Python used in this capstone

### Learning Objectives
- Install NiceGUI with `uv` and start a page from the terminal.
- Explain that each `ui.` call creates an element and that an event handler runs when the user acts.
- Give every input a label and report results in a plain text status line.

### Concept Explanation

NiceGUI lets you build a web page in Python. When the program runs it starts a small web server on your own computer and prints an address, normally `http://localhost:8080`. You open that address in a browser. Nothing is sent to other people; the page is served only from your computer unless you choose otherwise.

**Setup.** Install the package into the project environment:
```bash
uv add nicegui
```
Windows PowerShell uses the same command:
```powershell
uv add nicegui
```

**Elements and handlers.** Each call such as `ui.label(...)`, `ui.input(...)`, or `ui.button(...)` creates an element on the page. A button takes an `on_click` function, called a *handler*, that runs when the user presses it. The code inside `@ui.page("/")` builds the page each time someone opens it.

**Starting the server.** `ui.run(...)` starts the server. Guard it with `if __name__ in {"__main__", "__mp_main__"}:` as NiceGUI requires. Pass `show=False` so that no browser is opened automatically, and `reload=False` while learning.

**Accessibility.** NiceGUI pages are ordinary web pages, so a screen reader reads them as any other page. Three habits make them usable: give every input a clear `label`, because the label text is what a screen reader announces for the field; report every result in a plain text label as well as in a pop-up, because a pop-up message disappears; and never use color as the only signal. The status label below uses the standard attributes `role="status"` and `aria-live="polite"`, which ask assistive technology to announce changes. Whether your screen reader announces them as intended must be tested with your own setup.

### Worked Example

Save this as `hello_app.py`:
```python
from nicegui import ui


@ui.page("/")
def main_page():
    ui.page_title("Personal Data Manager")
    ui.label("Personal Data Manager")
    name = ui.input(label="Your name")
    greeting = ui.label("Type a name and press the button.").props('role="status" aria-live="polite"')

    def greet():
        if name.value.strip():
            greeting.set_text(f"Hello, {name.value.strip()}!")
        else:
            greeting.set_text("Please enter a name.")

    ui.button("Greet", on_click=greet)


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Personal Data Manager", reload=False, show=False)
```

Start it from the terminal and open the address that it prints:
```bash
uv run python hello_app.py
```

The repository also includes a user-level test, `test_hello_ui.py`, which needs `uv add --dev pytest pytest-asyncio`:
```python
from nicegui.testing import User

pytest_plugins = ["nicegui.testing.user_plugin"]


async def test_greeting(user: User) -> None:
    await user.open("/")
    await user.should_see("Personal Data Manager")
    user.find("Greet").click()
    await user.should_see("Please enter a name.")
    user.find("Your name").type("Avery")
    user.find("Greet").click()
    await user.should_see("Hello, Avery!")
```
```ini
# pytest.ini
[pytest]
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
main_file = hello_app.py
```

### Expected Behavior or Output

When the program starts, the terminal prints a line like this one (the address and port depend on your computer; the default port is 8080):
```text
NiceGUI ready to go on http://localhost:8080, and http://192.0.2.2:8080
```
The page title is Personal Data Manager. Pressing **Greet** with an empty field sets the status line to `Please enter a name.`; after typing `Avery` it says `Hello, Avery!`. Running the test with `python -m pytest -q test_hello_ui.py` prints:
```text
1 passed
```

### Common Mistakes

1. Calling `ui.run()` without the `__name__` guard, which can start the server twice.
2. Relying only on `ui.notify`, whose message disappears, instead of also updating a text status line.
3. Leaving an input without a label, so the screen reader announces only "edit text".
4. Starting a second copy of the program while the first still holds the port.

### Activities

1. Start `hello_app.py` and read the page title and the status line with your screen reader.
2. Change the greeting to include the time of day using a second input.
3. Run the test file and then break the greeting text on purpose to watch the test fail.
4. Add a second button that clears the name and sets the status line to `Name cleared.`

### Accessibility Practice

Open the page with the keyboard only: press Tab to move between the input and the button and read each stop. Check that the input's label is announced and that the status line is read after you press the button. Record the browser, screen reader, and version you tested, and do not claim the page is accessible to other setups.

### Skills Checklist

- [ ] I can install NiceGUI and start a page from the terminal.
- [ ] I can explain elements and event handlers.
- [ ] I can give every input a label.
- [ ] I can report results in a plain text status line.
- [ ] I can run a user-level test.

---

## Lesson 11.2: Data Model and Storage

### Reading References
- Matthes: Chapter 6 (Dictionaries) and Chapter 10 (Files and Exceptions)
- Python documentation: the `json` and `datetime` modules

### Learning Objectives
- Represent each record as a dictionary with the shared fields.
- Validate input and return a clear message when it is invalid.
- Save to and load from a JSON file, and handle a missing or damaged file.

### Concept Explanation

The data and the rules live in one module, `records.py`, that contains no user-interface code. Keeping logic separate from the page has two benefits: the rules can be tested without a browser, and the same logic can serve a different front end later.

Each record is a dictionary with the shared fields (`id`, `title`, `description`, `category`, `created_at`, `updated_at`) and the optional `done` field. Dictionaries convert directly to JSON.

**Rules.** A title and a category are required. A new record gets an `id` one higher than the highest in use. `created_at` is set once and never changes. `updated_at` changes whenever a record is updated, completed, or edited. Every function that can fail returns a clear message instead of raising an error that the user must interpret; functions return a pair `(result, message)`.

**Storage.** `save_records` writes the list as JSON. `load_records` treats a missing file as an empty list (this is normal on first use), and returns a message when the file is damaged or does not contain valid records, so the program never overwrites good data with an empty list without telling the user.

**Testable time.** Functions that stamp a record take a `clock` argument that defaults to the real time. Tests pass a fake clock so that timestamps are predictable.

### Worked Example

Save this as `records.py`:
```python
"""Logic for the Personal Data Manager. No user-interface code lives here."""
import json
from datetime import datetime

REQUIRED_FIELDS = ("id", "title", "description", "category", "created_at", "updated_at")


def now():
    """Return the current time as ISO 8601 text, for example 2026-01-15T09:00:00."""
    return datetime.now().isoformat(timespec="seconds")


def validate(title, category):
    """Return an error message for invalid input, or None when it is valid."""
    if not title or not title.strip():
        return "A title is required."
    if not category or not category.strip():
        return "A category is required."
    return None


def next_id(records):
    """Return one more than the highest id in use (1 for an empty list)."""
    return max((record["id"] for record in records), default=0) + 1


def find(records, record_id):
    """Return the record with this id, or None."""
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def add_record(records, title, description, category, clock=now):
    """Add a record. Return (record, None) on success or (None, message) on failure."""
    problem = validate(title, category)
    if problem:
        return None, problem
    stamp = clock()
    record = {
        "id": next_id(records),
        "title": title.strip(),
        "description": (description or "").strip(),
        "category": category.strip(),
        "created_at": stamp,
        "updated_at": stamp,
        "done": False,
    }
    records.append(record)
    return record, None


def update_record(records, record_id, changes, clock=now):
    """Change fields of a record. created_at and id never change."""
    record = find(records, record_id)
    if record is None:
        return None, "No record has that id."
    problem = validate(changes.get("title", record["title"]), changes.get("category", record["category"]))
    if problem:
        return None, problem
    for key, value in changes.items():
        if key not in ("id", "created_at"):
            record[key] = value.strip() if isinstance(value, str) else value
    record["updated_at"] = clock()
    return record, None


def complete_record(records, record_id, clock=now):
    """Mark a record done; this counts as an update."""
    return update_record(records, record_id, {"done": True}, clock)


def delete_record(records, record_id):
    """Remove one record. Return (True, None) or (False, message)."""
    record = find(records, record_id)
    if record is None:
        return False, "No record has that id."
    records.remove(record)
    return True, None


def search(records, text):
    """Return records whose title or description contains the text (ignoring case)."""
    needle = text.strip().lower()
    return [r for r in records if needle in r["title"].lower() or needle in r["description"].lower()]


def describe(record):
    """One line of plain text for a record; status is shown in words, never by color."""
    status = "done" if record.get("done") else "not done"
    return f"{record['id']}. {record['title']} [{record['category']}] ({status})"


def save_records(path, records):
    """Write records to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


def load_records(path):
    """Return (records, None) or ([], message). A missing file is not an error."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return [], None
    except json.JSONDecodeError:
        return [], f"{path} is not valid JSON, so the list starts empty."
    if not isinstance(data, list) or not all(isinstance(r, dict) and all(f in r for f in REQUIRED_FIELDS) for r in data):
        return [], f"{path} does not contain valid records, so the list starts empty."
    return data, None
```

Try it with this short script, `demo.py`, in the same folder:
```python
import records

ticks = iter(range(1, 100))


def clock():
    return f"2026-01-15T10:00:{next(ticks):02d}"


items = []
records.add_record(items, "Notebook", "Course notes", "supplies", clock)
records.add_record(items, "Pencil", "Box of 10", "supplies", clock)
print(records.add_record(items, "  ", "x", "supplies", clock))
for item in items:
    print(records.describe(item))

records.save_records("data.json", items)
loaded, problem = records.load_records("data.json")
print(loaded == items, problem)
print(records.load_records("missing.json"))
```

### Expected Behavior or Output

Running `python demo.py` prints:
```text
(None, 'A title is required.')
1. Notebook [supplies] (not done)
2. Pencil [supplies] (not done)
True None
([], None)
```
The invalid record is rejected with `(None, 'A title is required.')`. The saved and reloaded list equals the original (`True None`), and a missing file gives an empty list with no message.

### Common Mistakes

1. Letting the user interface and the rules share the same code, so neither can be tested alone.
2. Overwriting `data.json` with an empty list after a failed load.
3. Changing `created_at` when a record is edited.
4. Reusing an old `id` by counting the list length instead of using the highest `id`.

### Activities

1. Run `demo.py` and open the saved `data.json`. Read the text aloud.
2. Add a rule that a title may not be longer than 60 characters, with a clear message.
3. Add an `is_done` filter function that returns only completed records.
4. Damage `data.json` by deleting a bracket and run `load_records` again; read the message it returns.

### Accessibility Practice

Messages are complete sentences that say what is wrong (`A title is required.`) so they read clearly in speech and braille. After saving, read `data.json` in the terminal; `indent=4` puts one field per line, which reads well line by line.

### Skills Checklist

- [ ] I can represent records as dictionaries.
- [ ] I can validate input and return clear messages.
- [ ] I can save and load JSON.
- [ ] I can handle a missing or damaged file.
- [ ] I can keep logic separate from the user interface.

---

## Lesson 11.3: Displaying and Searching Items

### Reading References
- NiceGUI documentation (official site, nicegui.io); check the documentation for the version you installed

### Learning Objectives
- Build a page that adds a record and lists all records.
- Filter the list as the user types in a search box.
- Show errors in a status line that is also announced.

### Concept Explanation

The page uses the functions from `records.py`. It builds a form for a new record, a search box, and a list. The list is rebuilt by one function, `refresh()`, that clears the list column and then creates one label per record. Calling `refresh()` after every change keeps the page and the data in step.

Each record is shown as one plain sentence produced by `describe()`, for example `1. Notebook [supplies] (not done)`. The status is the words *done* and *not done*, never a color or an icon alone. The description appears on its own line prefixed `Details:`.

The search box filters as the user types: `search_text.on_value_change(...)` calls `refresh()`, which uses `search()` when the box is not empty.

Every input has a unique label (`Record title`, `Record description`, `Record category`, `Search title or description`). Unique labels let a screen reader user tell the fields apart and let the tests find them.

### Worked Example

Save this as `app_v1.py` (it uses `records.py` from Lesson 11.2):
```python
"""Personal Data Manager, version for Lesson 11.3: add, list, and search."""
import os
from pathlib import Path

from nicegui import ui

import records as store

DATA_FILE = Path(os.environ.get("PDM_DATA_FILE", "data.json"))
items, load_problem = store.load_records(DATA_FILE)


@ui.page("/")
def main_page():
    ui.page_title("Personal Data Manager")
    ui.label("Personal Data Manager").classes("text-2xl")

    # A plain-text status line. aria-live asks assistive technology to announce changes.
    status = ui.label(load_problem or "Ready.").props('role="status" aria-live="polite"')

    def say(message, ok=True):
        status.set_text(message)
        ui.notify(message, type="positive" if ok else "negative")

    ui.label("Add a record")
    title = ui.input(label="Record title")
    description = ui.input(label="Record description")
    category = ui.input(label="Record category")

    ui.label("Find records")
    search_text = ui.input(label="Search title or description")

    ui.label("Records")
    list_column = ui.column()

    def refresh():
        shown = store.search(items, search_text.value) if search_text.value else items
        list_column.clear()
        with list_column:
            if not shown:
                ui.label("No records to show.")
            for record in shown:
                ui.label(store.describe(record))
                if record["description"]:
                    ui.label("Details: " + record["description"])

    def add_clicked():
        record, problem = store.add_record(items, title.value, description.value, category.value)
        if problem:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        title.set_value("")
        description.set_value("")
        category.set_value("")
        refresh()
        say(f"Added record {record['id']}: {record['title']}.")

    ui.button("Add record", on_click=add_clicked)
    search_text.on_value_change(lambda _: refresh())
    refresh()


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Personal Data Manager", reload=False, show=False)
```

The user-level test `test_app_v1_ui.py`:
```python
import os
import tempfile

from nicegui.testing import User

pytest_plugins = ["nicegui.testing.user_plugin"]
os.environ["PDM_DATA_FILE"] = os.path.join(tempfile.mkdtemp(), "data.json")


async def test_add_and_search(user: User) -> None:
    await user.open("/")
    await user.should_see("No records to show.")
    for title, description, category in [("Notebook", "Course notes", "supplies"), ("Pencil", "Box of 10", "supplies")]:
        user.find("Record title").type(title)
        user.find("Record description").type(description)
        user.find("Record category").type(category)
        user.find("Add record").click()
    await user.should_see("2. Pencil [supplies] (not done)")
    user.find("Search title or description").type("note")
    await user.should_see("1. Notebook [supplies] (not done)")
    await user.should_not_see("2. Pencil [supplies] (not done)")
    user.find("Add record").click()
    await user.should_see("A title is required.")
```
```ini
# pytest.ini
[pytest]
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
main_file = app_v1.py
```

### Expected Behavior or Output

Start the app with `uv run python app_v1.py` and open the printed address. With no records the list says `No records to show.` After adding Notebook and Pencil, the list shows `1. Notebook [supplies] (not done)` and `2. Pencil [supplies] (not done)`. Typing `note` in the search box leaves only the Notebook line. Pressing **Add record** with an empty title sets the status line to `A title is required.` Running the test prints:
```text
1 passed
```

### Common Mistakes

1. Building the list outside `refresh()`, so it is not updated when the data changes.
2. Using the same label text for two inputs, so the screen reader cannot tell them apart.
3. Showing a record's status only by color.
4. Forgetting to clear the form after a successful add, so the next record starts with old text.

### Activities

1. Add the three shared sample records through the page and compare the list with the sample data.
2. Add a category filter next to the search box.
3. Show the number of records after the list, for example `3 records.`
4. Break the `describe()` text on purpose and see which test fails.

### Accessibility Practice

Tab through the form and confirm that each field is announced with its label. After pressing **Add record**, listen for the status line. If your screen reader does not announce it, note the browser and screen reader you used, then add a visible sentence under the button as a fallback.

### Skills Checklist

- [ ] I can build a form and a list in NiceGUI.
- [ ] I can refresh the list after every change.
- [ ] I can filter the list with a search box.
- [ ] I can show status in words.
- [ ] I can give each input a unique label.

---

## Lesson 11.4: Changing, Completing, and Deleting Items

### Reading References
- NiceGUI documentation (official site, nicegui.io); check the documentation for the version you installed

### Learning Objectives
- Select a record from a list and change its title or category.
- Mark a record done and delete a record.
- Save after every successful change and report each result.

### Concept Explanation

The finished page adds a *chooser* (`ui.select`) that lists every record by its descriptive sentence, plus buttons to change, complete, or delete the chosen record. All three handlers follow the same pattern: check that a record is chosen, call the matching function in `records.py`, show the message if it failed, and otherwise save the file, refresh the list, and report what happened.

`update_record` changes only the fields that are supplied and always updates `updated_at`. `complete_record` is an update that sets `done` to `True`. `delete_record` removes exactly one record. After a delete the chooser is cleared so a stale choice cannot be used.

Notice that the handlers contain no rules. A rule such as "a title is required" exists once, in `records.py`, and applies the same way no matter which control triggers it.

### Worked Example

The finished `app.py` (it uses `records.py` from Lesson 11.2):
```python
"""Personal Data Manager: a NiceGUI front end for records.py."""
import os
from pathlib import Path

from nicegui import ui

import records as store

DATA_FILE = Path(os.environ.get("PDM_DATA_FILE", "data.json"))
items, load_problem = store.load_records(DATA_FILE)


@ui.page("/")
def main_page():
    ui.page_title("Personal Data Manager")
    ui.label("Personal Data Manager").classes("text-2xl")

    # A plain-text status line. aria-live asks assistive technology to announce changes.
    status = ui.label(load_problem or "Ready.").props('role="status" aria-live="polite"')

    def say(message, ok=True):
        status.set_text(message)
        ui.notify(message, type="positive" if ok else "negative")

    ui.label("Add a record")
    title = ui.input(label="Record title")
    description = ui.input(label="Record description")
    category = ui.input(label="Record category")

    ui.label("Find records")
    search_text = ui.input(label="Search title or description")

    ui.label("Records")
    list_column = ui.column()

    ui.label("Change one record")
    chooser = ui.select(options={}, label="Choose a record")
    new_title = ui.input(label="New title (leave blank to keep)")
    new_category = ui.input(label="New category (leave blank to keep)")

    def refresh():
        shown = store.search(items, search_text.value) if search_text.value else items
        list_column.clear()
        with list_column:
            if not shown:
                ui.label("No records to show.")
            for record in shown:
                ui.label(store.describe(record))
                if record["description"]:
                    ui.label("Details: " + record["description"])
        chooser.set_options({r["id"]: store.describe(r) for r in items})

    def add_clicked():
        record, problem = store.add_record(items, title.value, description.value, category.value)
        if problem:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        title.set_value("")
        description.set_value("")
        category.set_value("")
        refresh()
        say(f"Added record {record['id']}: {record['title']}.")

    def change_clicked():
        if chooser.value is None:
            say("Choose a record first.", ok=False)
            return
        changes = {}
        if new_title.value.strip():
            changes["title"] = new_title.value
        if new_category.value.strip():
            changes["category"] = new_category.value
        if not changes:
            say("Enter a new title or a new category.", ok=False)
            return
        record, problem = store.update_record(items, chooser.value, changes)
        if problem:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        new_title.set_value("")
        new_category.set_value("")
        refresh()
        say(f"Updated record {record['id']}.")

    def complete_clicked():
        if chooser.value is None:
            say("Choose a record first.", ok=False)
            return
        record, problem = store.complete_record(items, chooser.value)
        if problem:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        refresh()
        say(f"Marked record {record['id']} as done.")

    def delete_clicked():
        if chooser.value is None:
            say("Choose a record first.", ok=False)
            return
        record_id = chooser.value
        ok, problem = store.delete_record(items, record_id)
        if not ok:
            say(problem, ok=False)
            return
        store.save_records(DATA_FILE, items)
        chooser.set_value(None)
        refresh()
        say(f"Deleted record {record_id}.")

    ui.button("Add record", on_click=add_clicked)
    search_text.on_value_change(lambda _: refresh())
    ui.button("Change selected record", on_click=change_clicked)
    ui.button("Mark selected record done", on_click=complete_clicked)
    ui.button("Delete selected record", on_click=delete_clicked)
    refresh()


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Personal Data Manager", reload=False, show=False)
```

The user-level test `test_app_ui.py`:
```python
"""User-level tests for app.py. They need: pip install nicegui pytest pytest-asyncio"""
import os
import tempfile

from nicegui.testing import User

pytest_plugins = ["nicegui.testing.user_plugin"]
os.environ["PDM_DATA_FILE"] = os.path.join(tempfile.mkdtemp(), "data.json")


async def test_add_search_complete_delete(user: User) -> None:
    await user.open("/")
    await user.should_see("Personal Data Manager")
    await user.should_see("No records to show.")

    user.find("Record title").type("Notebook")
    user.find("Record description").type("Course notes")
    user.find("Record category").type("supplies")
    user.find("Add record").click()
    await user.should_see("1. Notebook [supplies] (not done)")
    await user.should_see("Added record 1: Notebook.")

    user.find("Add record").click()
    await user.should_see("A title is required.")

    user.find("Choose a record").click()
    user.find("1. Notebook [supplies] (not done)").click()
    user.find("Mark selected record done").click()
    await user.should_see("1. Notebook [supplies] (done)")

    user.find("Delete selected record").click()
    await user.should_see("Deleted record 1.")
    await user.should_see("No records to show.")
```
```ini
# pytest.ini
[pytest]
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
main_file = app.py
```

### Expected Behavior or Output

In the page: choose `1. Notebook [supplies] (not done)` and press **Mark selected record done**; the list shows `1. Notebook [supplies] (done)` and the status line says `Marked record 1 as done.` Pressing **Delete selected record** says `Deleted record 1.` Pressing a change button with nothing chosen says `Choose a record first.` The test prints:
```text
1 passed
```

### Common Mistakes

1. Using a stale choice after deleting, so a later action targets a record that no longer exists.
2. Putting rules in the handlers, so two buttons enforce the same rule differently.
3. Forgetting to save after a change, so the change is lost when the program stops.
4. Deleting without telling the user, which gives no way to confirm that the action happened.

### Activities

1. Change the title and category of record 2 through the page and read `data.json` to confirm.
2. Add a confirmation step before a delete (for example a second button that must be pressed).
3. Add a button that deletes all completed records and reports how many were removed.
4. Write a user-level test for the change handler.

### Accessibility Practice

Use the keyboard to choose a record in the chooser and press each button. Confirm that the result of every action is spoken or readable in the status line without using a mouse. Check that buttons have text labels that say what they do; avoid icon-only buttons.

### Skills Checklist

- [ ] I can select a record and change its fields.
- [ ] I can mark a record done.
- [ ] I can delete one record.
- [ ] I save and refresh after each change.
- [ ] I keep rules in one place.

---

## Lesson 11.5: Testing, Documentation, and Final Submission

### Reading References
- Matthes: Chapter 11 (Testing Your Code)
- Python documentation: the `unittest` module
- NiceGUI documentation (official site, nicegui.io); check the documentation for the version you installed

### Learning Objectives
- Run the shared acceptance tests for the logic module.
- Check the page by hand with the keyboard and your own screen reader.
- Write the README and submit the deliverables.

### Concept Explanation

The shared acceptance tests (listed in the unit overview) are written once for the logic in `records.py`. Tests 1 to 5 are automated below; test 6, using every control without color or a mouse, must be checked by hand. The user-level page test from Lesson 11.4 adds a simulated walk through the page, but it runs in Python, so it cannot tell you how a real browser and screen reader behave.

A **README** tells the next reader what the program does and how to run it. Write it in plain text or Markdown with short headings and complete sentences. Include the project title and your name, a description, the run command (`uv run python app.py`), the keyboard and screen reader instructions that you actually tested, the shared record fields, and a reflection on what was hard.

**Version control.** Keep your project in Git and commit after each working step so you can return to a working version (see the supplemental section at the end of this unit).

### Worked Example

The test file `test_records.py` (put it next to `records.py`):
```python
import json
import tempfile
import unittest
from pathlib import Path

import records


def make_clock():
    state = {"n": 0}

    def clock():
        state["n"] += 1
        return f"2026-01-15T10:00:{state['n']:02d}"
    return clock


class TestRecords(unittest.TestCase):
    def setUp(self):
        self.clock = make_clock()
        self.items = []
        records.add_record(self.items, "Notebook", "Course notes", "supplies", self.clock)
        records.add_record(self.items, "Pencil", "Box of 10", "supplies", self.clock)
        records.add_record(self.items, "Study plan", "Weekly schedule", "planning", self.clock)

    def test_1_empty_title_is_rejected(self):
        record, message = records.add_record(self.items, "   ", "x", "supplies", self.clock)
        self.assertIsNone(record)
        self.assertEqual(message, "A title is required.")
        self.assertEqual(len(self.items), 3)

    def test_2_new_record_gets_an_unused_id(self):
        records.delete_record(self.items, 2)
        record, _ = records.add_record(self.items, "Ruler", "30 cm", "supplies", self.clock)
        self.assertEqual(record["id"], 4)

    def test_3_update_changes_updated_at_but_not_created_at(self):
        before = dict(records.find(self.items, 1))
        records.update_record(self.items, 1, {"description": "Lecture notes"}, self.clock)
        after = records.find(self.items, 1)
        self.assertEqual(after["created_at"], before["created_at"])
        self.assertNotEqual(after["updated_at"], before["updated_at"])

    def test_4_delete_removes_only_that_record(self):
        ok, _ = records.delete_record(self.items, 2)
        self.assertTrue(ok)
        self.assertEqual([r["id"] for r in self.items], [1, 3])

    def test_5_save_and_reload_preserves_all_fields(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            records.save_records(path, self.items)
            loaded, message = records.load_records(path)
        self.assertIsNone(message)
        self.assertEqual(loaded, self.items)

    def test_damaged_file_gives_an_empty_list_and_a_message(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            path.write_text('[{"id": 1,', encoding="utf-8")
            loaded, message = records.load_records(path)
        self.assertEqual(loaded, [])
        self.assertIn("not valid JSON", message)

    def test_complete_marks_done_and_updates(self):
        record, _ = records.complete_record(self.items, 3, self.clock)
        self.assertTrue(record["done"])
        self.assertNotEqual(record["updated_at"], record["created_at"])

    def test_search_ignores_case_and_checks_description(self):
        self.assertEqual([r["title"] for r in records.search(self.items, "NOTE")], ["Notebook"])
        self.assertEqual([r["title"] for r in records.search(self.items, "box")], ["Pencil"])

    def test_blank_title_cannot_be_saved_by_update(self):
        record, message = records.update_record(self.items, 1, {"title": ""}, self.clock)
        self.assertIsNone(record)
        self.assertEqual(message, "A title is required.")


if __name__ == "__main__":
    unittest.main()
```

Run it from the terminal:
```bash
uv run python -m unittest -v test_records
```

A starting point for `README.md`:
```markdown
# Personal Data Manager

By: (your name)

## What it does
A small web application that keeps a list of records and saves them to data.json.

## How to run
    uv run python app.py
Then open the address that the terminal prints.

## Keyboard and screen reader notes
(Describe what you tested: operating system, browser, screen reader, and versions.)

## Record fields
id, title, description, category, created_at, updated_at, done

## Reflection
(What was hard, and what would you improve?)
```

### Expected Behavior or Output

The command prints one line per test and a summary (the timing differs from run to run):
```text
test_1_empty_title_is_rejected (test_records.TestRecords.test_1_empty_title_is_rejected) ... ok
test_2_new_record_gets_an_unused_id (test_records.TestRecords.test_2_new_record_gets_an_unused_id) ... ok
test_3_update_changes_updated_at_but_not_created_at (test_records.TestRecords.test_3_update_changes_updated_at_but_not_created_at) ... ok
test_4_delete_removes_only_that_record (test_records.TestRecords.test_4_delete_removes_only_that_record) ... ok
test_5_save_and_reload_preserves_all_fields (test_records.TestRecords.test_5_save_and_reload_preserves_all_fields) ... ok
test_blank_title_cannot_be_saved_by_update (test_records.TestRecords.test_blank_title_cannot_be_saved_by_update) ... ok
test_complete_marks_done_and_updates (test_records.TestRecords.test_complete_marks_done_and_updates) ... ok
test_damaged_file_gives_an_empty_list_and_a_message (test_records.TestRecords.test_damaged_file_gives_an_empty_list_and_a_message) ... ok
test_search_ignores_case_and_checks_description (test_records.TestRecords.test_search_ignores_case_and_checks_description) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

### Common Mistakes

1. Testing only that nothing crashed, and not checking the values returned.
2. Sharing one list of records between tests, so one test's changes affect the next.
3. Writing a README that only the author can follow, or claiming accessibility that was never tested.
4. Skipping test 6 because it cannot be automated.

### Activities

1. Run the tests, then break `update_record` so it also changes `created_at` and watch test 3 fail. Restore it.
2. Add a test that deleting an unknown id returns `False` and a message.
3. Ask a classmate to follow your README from an empty folder and note where they get stuck.
4. Complete test 6 by hand: use every control with the keyboard only and record what you found.

### Accessibility Practice

Run the tests from the terminal and read the summary line first. For the hand check, use the keyboard only, then repeat with your screen reader or braille display. Record the operating system, browser, screen reader, and versions that you tested, and describe only what you actually tried.

### Skills Checklist

- [ ] I can run the acceptance tests and read the results.
- [ ] I can complete a hand check of keyboard and screen reader use.
- [ ] I can write a README another person can follow.
- [ ] I know what the page test does and does not show.
- [ ] I can submit the listed deliverables.

---

## Assessment Criteria

### Functionality (60%)
- [ ] Ability to add new items with all specified attributes.
- [ ] Correct display of all current items.
- [ ] Correct editing of existing items.
- [ ] Correct deletion of items.
- [ ] Accurate saving and loading to and from `data.json`.
- [ ] Search and completion work as described.
- [ ] No major bugs or crashes during typical usage.

### Code Quality and Structure (20%)
- [ ] Clear and concise Python code.
- [ ] Appropriate use of functions, with rules kept in `records.py`.
- [ ] Meaningful variable and function names.
- [ ] Adequate comments where logic is complex.
- [ ] Proper indentation.

### Accessibility and User Experience (15%)
- [ ] All interactive elements are correctly labeled for screen readers.
- [ ] Clear and consistent feedback in a text status line.
- [ ] Logical flow and presentation of information.
- [ ] No visual-only cues for critical information.

### README and Reflection (5%)
- [ ] Complete and clear README.
- [ ] Thoughtful reflection on development and accessibility challenges.

---

## Deliverables

1. `app.py` and `records.py`: the complete application code.
2. `test_records.py`: the acceptance tests.
3. `data.json`: an example file that shows saved data.
4. `README.md`, including: the project title and student name; a description of the application; instructions on how to run it (`uv run python app.py`); instructions for interacting with a screen reader; and a reflection on challenges faced.

---

## Supplemental: Version Control

### Git and Version Control

**Git** is the most widely used distributed version control system, invented in 2005 by Linus Torvalds for the Linux kernel project.

**Core workflow:**
1. **Working directory** — Make changes to files.
2. **Staging area** — `git add` — Stage changes.
3. **Repository** — `git commit` — Save a permanent snapshot.
4. **Remote** — `git push` / `git pull` — Sync with GitHub.

**Why Git is valuable:**
- **Rollback** — If a change breaks your app, revert instantly.
- **`git blame`** — See exactly which commit introduced a bug.
- **Branches** — Try experiments in isolation without affecting main code.
- **Pull requests** — Review changes with others before merging.

**Basic commands:**
```bash
git init                    # Initialize a repository
git add .                   # Stage all changes
git commit -m "Add feature" # Save a snapshot
git log                     # View history
git diff                    # See what changed
git checkout -- file.py     # Discard changes to a file
```

Windows Powershell

```powershell
git init                    # Initialize a repository
git add .                   # Stage all changes
git commit -m "Add feature" # Save a snapshot
git log                     # View history
git diff                    # See what changed
git restore -- file.py     # Discard changes to a file
```

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
