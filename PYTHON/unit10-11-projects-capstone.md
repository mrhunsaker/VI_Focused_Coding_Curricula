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

### Top-Down Design

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

### Benefits of Top-Down Design

- **Reduces Complexity** — Focus on one piece at a time.
- **Encourages Reusability** — Functions written for one part may be useful elsewhere.
- **Simplifies Debugging** — Test each component in isolation.
- **Improves Collaboration** — Clear plan for assigning work.

### Accessibility Considerations for I/O Design

- Provide **clear, descriptive prompts** for all input.
- Provide **explicit, labeled output** — avoid relying on visual formatting.
- Print **confirmation messages** after every action.
- Use consistent **output separators** like `---` to group information.

### Skills Checklist
- [ ] I can break down a larger problem into smaller, manageable parts.
- [ ] I can identify the key features required for a project.
- [ ] I can plan which data structures will be most suitable for my project's data.
- [ ] I can outline the main steps or flow of my program.

---

## Lesson 10.2: Building a Text-Based Adventure Game (Part 1)

### Reading References
- Matthes: Chapter 6, pages 105–111

### Room Definition and Movement

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

### Skills Checklist
- [ ] I can design a way to represent different locations in a text-based game.
- [ ] I can implement player movement based on user commands.
- [ ] I can update and track the player's current location.
- [ ] I can parse simple commands from user input.

---

## Lesson 10.3: Building a Text-Based Adventure Game (Part 2)

### Adding Items, Inventory, and Puzzles

```python
rooms = {
    "start": {
        "description": "A dark cave. There's a SHINY KEY on the ground.",
        "exits": {"north": "locked_door_room"},
        "items": ["shiny key"]
    },
    "locked_door_room": {
        "description": "A small chamber with a heavy locked door to the NORTH.",
        "exits": {"south": "start"},
        "items": []
    }
}

current_room = "start"
player_inventory = []
door_locked = True

while True:
    print("\n" + rooms[current_room]["description"])
    if rooms[current_room]["items"]:
        print(f"You see: {', '.join(rooms[current_room]['items'])}")
    print(f"Your inventory: {', '.join(player_inventory) if player_inventory else 'empty'}")

    command = input("What do you want to do? ").lower()

    if command == "take shiny key" and "shiny key" in rooms[current_room]["items"]:
        player_inventory.append("shiny key")
        rooms[current_room]["items"].remove("shiny key")
        print("You picked up the shiny key.")
    elif command == "use shiny key" and current_room == "locked_door_room" and "shiny key" in player_inventory and door_locked:
        door_locked = False
        print("You unlocked the door!")
        rooms["locked_door_room"]["exits"]["north"] = "treasure_room"
    elif command in rooms[current_room]["exits"]:
        if command == "north" and current_room == "locked_door_room" and door_locked:
            print("The door is locked! You need a key.")
        else:
            current_room = rooms[current_room]["exits"][command]
    elif command == "quit":
        break
    else:
        print("I don't understand that command.")
```

### Skills Checklist
- [ ] I can add items to locations and manage a player's inventory.
- [ ] I can implement commands for picking up and dropping items.
- [ ] I can design and implement a simple puzzle.
- [ ] I can define win/lose conditions for the game.

---

## Lesson 10.4: Developing a Command-Line Tool

### Simple To-Do List Tool

```python
import json

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


def save_todos():
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)
    print("Tasks saved.")


def add_task(task_description):
    todos.append({"description": task_description, "completed": False})
    print(f"Task '{task_description}' added.")


def view_tasks():
    if not todos:
        print("No tasks in your list.")
        return
    print("--- Your To-Do List ---")
    for i, task in enumerate(todos):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{i + 1}. {status} {task['description']}")
    print("-----------------------")


def mark_completed(task_number):
    try:
        index = int(task_number) - 1
        if 0 <= index < len(todos):
            todos[index]["completed"] = True
            print(f"Task '{todos[index]['description']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Quit")
    print("-----------------------")


load_todos()

while True:
    main_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        desc = input("Enter task description: ")
        add_task(desc)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        task_num = input("Enter task number to mark complete: ")
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

### Skills Checklist
- [ ] I can design an interactive menu system for a tool.
- [ ] I can use a `while` loop to maintain continuous user interaction.
- [ ] I can break down the tool's functionality into separate functions.
- [ ] I can implement file I/O to save and load data.

---

## Lesson 10.5: Refinement and User Experience

### Principles for Accessible Text Programs

1. **Clear prompts** — Tell the user exactly what to enter and in what format.
2. **Consistent output** — Use the same format for similar information.
3. **Graceful error handling** — Never let the program crash on bad input.
4. **Helpful error messages** — Tell the user what went wrong and how to fix it.
5. **"Help" commands** — Provide a way to list available commands.
6. **Confirmation messages** — Confirm every action taken.

### Robust Input Validation

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

### Skills Checklist
- [ ] I can write clear, descriptive prompts for user input.
- [ ] I can handle invalid input gracefully using `try-except`.
- [ ] I can provide helpful error messages.

---

# Unit 11: Capstone Project — Accessible Personal Data Manager

## Overview

Students will develop a fully functional, screen-reader-accessible graphical application using NiceGUI that allows users to manage a collection of structured personal data.

**Project Goal:** Build a simple application to manage a list of structured items.

**Project Options:**
- Contact Manager: name, phone, email, notes
- Book/Movie Tracker: title, author/director, genre, status
- Simple To-Do List: task description, due date, status
- Simple Inventory: item name, quantity, location, notes

---

## Core Functionality Requirements

1. **Add New Item** — A form to input details for a new item.
2. **View All Items** — Display items in a clear, accessible list format.
3. **Edit Item** — Select an existing item and modify its details.
4. **Delete Item** — Remove an item from the collection.
5. **Save/Load Data** — Persist the data to a JSON file.

---

## Setup

```bash
uv add nicegui
```

**Windows PowerShell (Windows 11):**

```powershell
uv add nicegui
```

---

## Guided Implementation

### Lesson 11.1: Introduction to NiceGUI

**Task 1:** Run the `app_skeleton.py` file and navigate using the keyboard and screen reader to understand the existing structure.

**Task 2:** Define your data model class:
```python
class Contact:
    def __init__(self, name, phone, email, notes):
        self.name = name
        self.phone = phone
        self.email = email
        self.notes = notes
```

**Task 3:** Implement data persistence using the `json` module within the `load_data()` and `save_data()` functions.

### Lesson 11.2: Data Model and Storage

**Task 1:** Complete the `add_item_logic()` function:
1. Get values from input fields using `.value` attribute.
2. Validate (e.g., name cannot be empty).
3. Provide accessible feedback: `ui.notify("Name is required!", type='negative')`.

**Task 2:** Create a new item object and add it to `all_items`.

**Task 3:** Clear input fields and provide success notification.

### Lesson 11.3–11.5: Displaying and Managing Items

**Implement `update_item_display()`:**
1. Clear the display: `items_display_column.clear()`.
2. Loop through `all_items` and create `ui.card` for each.
3. Update `item_selection_dropdown.options`.

**Implement `update_item_logic()`:**
1. Find the item in `all_items`.
2. Update attributes from edit form fields.
3. Call `update_item_display()` and `save_data()`.

**Implement `delete_selected_item_logic()`:**
1. Find and remove the item from `all_items`.
2. Call `update_item_display()`.
3. Provide accessible feedback.

---

## Assessment Criteria

### Functionality (60%)
- [ ] Ability to add new items with all specified attributes.
- [ ] Correct display of all current items.
- [ ] Correct editing of existing items.
- [ ] Correct deletion of items.
- [ ] Accurate saving and loading to/from `data.json`.
- [ ] No major bugs or crashes during typical usage.

### Code Quality & Structure (20%)
- [ ] Clear and concise Python code.
- [ ] Appropriate use of functions and/or classes.
- [ ] Meaningful variable and function names.
- [ ] Adequate comments where complex logic exists.
- [ ] Proper indentation.

### Accessibility & User Experience (15%)
- [ ] All interactive elements are correctly labeled for screen readers.
- [ ] Clear and consistent user feedback via `ui.notify()`.
- [ ] Logical flow and presentation of information.
- [ ] No visual-only cues for critical information.

### README and Reflection (5%)
- [ ] Complete and clear README.
- [ ] Thoughtful reflection on development and accessibility challenges.

---

## Deliverables

1. `app.py` — Complete NiceGUI application code.
2. `data.json` — Example JSON file demonstrating saved data.
3. `README.md` — Including:
   - Project title and student name.
   - Description of the application.
   - Instructions on how to run: `python app.py`.
   - Instructions for interacting with a screen reader.
   - Reflection on challenges faced.

---

## Supplemental: AI Tools and Version Control

### AI-Powered Coding Tools

**Benefits:**
- Increased productivity and speed.
- Syntax and idiom discovery.
- Rapid prototyping.

**Critical Warning:** AI tools can produce code that looks correct but contains subtle bugs. **Always:**
1. Read every line of AI-generated code.
2. Verify the logic and intent.
3. Look for familiar error types (indentation, name errors, type errors).
4. Run and test incrementally.
5. Add your own comments and docstrings.

**The Golden Rule:** You are responsible for your code. Treat AI suggestions as a first draft that needs meticulous editing.

### Git and Version Control

**Git** is the most widely used distributed version control system, invented in 2005 by Linus Torvalds for the Linux kernel project.

**Core workflow:**
1. **Working directory** — Make changes to files.
2. **Staging area** — `git add` — Stage changes.
3. **Repository** — `git commit` — Save a permanent snapshot.
4. **Remote** — `git push` / `git pull` — Sync with GitHub.

**Why Git is especially valuable with AI code:**
- **Rollback** — If AI-generated code breaks your app, revert instantly.
- **`git blame`** — See exactly which commit introduced a bug.
- **Branches** — Test AI experiments in isolation without affecting main code.
- **Pull requests** — Review AI-generated code before merging.

**Basic commands:**
```bash
git init                    # Initialize a repository
git add .                   # Stage all changes
git commit -m "Add feature" # Save a snapshot
git log                     # View history
git diff                    # See what changed
git checkout -- file.py     # Discard changes to a file
```

**Windows PowerShell (Windows 11):**

```powershell
git init                    # Initialize a repository
git add .                   # Stage all changes
git commit -m "Add feature" # Save a snapshot
git log                     # View history
git diff                    # See what changed
git restore -- file.py     # Discard changes to a file
```
