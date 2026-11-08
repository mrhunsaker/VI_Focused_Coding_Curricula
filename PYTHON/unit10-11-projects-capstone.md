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
