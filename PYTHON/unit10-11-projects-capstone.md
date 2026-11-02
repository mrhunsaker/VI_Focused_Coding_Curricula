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
player_inventory = []
door_locked = True

while True:
    print("\n" + rooms[current_room]["description"])
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
        print("You quit the adventure.")
        break
    else:
        print("Invalid command. Use a direction, 'take shiny key', 'use shiny key', or 'quit'.")
```

### Skills Checklist
- [ ] I can add items to locations and manage a player's inventory.
- [ ] I can implement commands for picking up and dropping items.
- [ ] I can design and implement a simple puzzle.
- [ ] I can define win/lose conditions for the game.

---

## Lesson 10.4: Developing a Command-Line Tool

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
- Contact Manager
- Book/Movie Tracker
- Study Notes Manager
- Personal Inventory

Every option uses the same six-field record schema (`id`, `title`, `description`, `category`, `created_at`, `updated_at`). The selected project domain changes the meaning of the field values, not the record shape or required operations.

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

Windows Powershell

```powershell
uv add nicegui
```

---

## Guided Implementation

### Lesson 11.1: Introduction to NiceGUI

**Task 1:** Run the `app_skeleton.py` file and navigate using the keyboard and screen reader to understand the existing structure.

**Task 2:** Define a data model class with all six canonical record fields:
```python
class PersonalRecord:
    def __init__(self, record_id, title, description, category,
                 created_at, updated_at):
        self.id = record_id
        self.title = title
        self.description = description
        self.category = category
        self.created_at = created_at
        self.updated_at = updated_at
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

### Academic Integrity: AI and Assessment

AI tools must not write, complete, autocomplete, repair, or generate course code or assessment solutions. Students may use only instructor-authorized conceptual explanations that do not produce deliverable code. Git and version control are taught separately and are not a workaround for the assessment-integrity rule.

### Git and Version Control

**Git** is the most widely used distributed version control system, invented in 2005 by Linus Torvalds for the Linux kernel project.

**Core workflow:**
1. **Working directory** — Make changes to files.
2. **Staging area** — `git add` — Stage changes.
3. **Repository** — `git commit` — Save a permanent snapshot.
4. **Remote** — `git push` / `git pull` — Sync with GitHub.

**Why Git is useful in collaborative development:**
- **Rollback** — Revert a change when a regression is introduced.
- **`git blame`** — Identify the commit that introduced a change.
- **Branches** — Develop and test changes in isolation.
- **Pull requests** — Review changes before merging.

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

## Canonical Shared Project Contracts

### Unit 10: Adventure and command-line to-do projects

All parallel-language versions must use this exact adventure graph and command set.

| Room | Exits | Items / state |
|---|---|---|
| `start_room` | north → `tunnel` | shiny key |
| `tunnel` | south → `start_room`; east → `clearing` | none |
| `clearing` | west → `tunnel`; north → `locked_door_room` | north exit is blocked until unlocked |
| `locked_door_room` | south → `clearing`; north → `treasure_room` after unlocking | locked door |
| `treasure_room` | none | terminal winning room |

Commands are `north`, `south`, `east`, `west`, `take shiny key`, `use shiny key`, and `quit`. The key begins in `start_room`; the player must take it, travel to `locked_door_room`, use it there, and then enter `treasure_room` to win. Invalid movement must not change the current room.

The CLI to-do manager must store these five fields on every task: `id`, `title`, `description`, `done`, and `created_at`. It must support create, list, complete/update, delete, save, and load. Invalid identifiers, empty titles, and malformed persistence data require explicit textual errors.

### Unit 11: Accessible Personal Data Manager

The shared capstone record has exactly these fields:

```python
record = {
    "id": 1,
    "title": "Programming notes",
    "description": "Review lists and dictionaries",
    "category": "Study",
    "created_at": "2025-01-15T09:00:00Z",
    "updated_at": "2025-01-15T09:00:00Z",
}
```

Required operations are list/display, add, search, update, delete, and completion/status management where applicable to the shared specification. Persist the same records as JSON. A GUI framework is a Python-specific implementation choice; the data model, operations, textual status/error messages, keyboard access, and acceptance tests are not optional or language-specific.

### Academic integrity and AI policy

AI tools must not write, complete, autocomplete, repair, or generate course code or assessment solutions. Students may use only instructor-authorized conceptual explanations that do not produce deliverable code. Git and version control remain appropriate topics when taught independently of AI code generation.
