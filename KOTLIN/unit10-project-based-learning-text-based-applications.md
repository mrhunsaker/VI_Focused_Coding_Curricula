# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

Plan a text project, build the shared text adventure in two parts, build the command-line to-do manager, and refine input validation.

---


## Lesson 10.1: Planning a Text-Based Project

### Reading References
- [Functions: function types](https://kotlinlang.org/docs/lambdas.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 10.1: Project Planning and Design

### Learning Objectives
- Write a short requirements list.
- Design a command loop with a map of handlers.
- Plan in small steps and test each one.

### Concept Explanation

A project is easier to finish when it is planned in small steps. Write down what the program must do (*requirements*), what information it keeps (*data*), and the commands a person can give (*interface*). Build one small piece, test it, then add the next.

Text-based projects share a *command loop*: show a prompt, read a line, find the matching action, and repeat until the user quits. In Kotlin, a `Map<String, () -> Unit>` holds actions: the keys are command names and the values are *lambdas*, small functions with no name. A new command is one new entry, and an unknown command is a failed lookup that prints a helpful message.

The loop stops on `quit` and also when input ends (`null`). The example is a skeleton with two commands; typing `help`, `look`, an unknown word, and `quit` shows each path.

### Worked Example

```kotlin
fun main() {
    val commands: Map<String, () -> Unit> = mapOf(
        "help" to { println("Commands: help, look, quit") },
        "look" to { println("You are in a dark cave.") },
    )

    println("Type a command:")
    var line = readlnOrNull()
    while (line != null && line != "quit") {
        val handler = commands[line]
        if (handler != null) {
            handler()
        } else {
            println("I don't understand that command. Type help for a list.")
        }
        println("Type a command:")
        line = readlnOrNull()
    }
    println("Goodbye!")
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
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

With no standard input at all, the program ends cleanly and prints:
```text
Type a command:
Goodbye!
```

### Common Mistakes
1. Starting to code before listing the requirements.
2. Using a long chain of `if` statements instead of a map of handlers.
3. Forgetting that an unknown command should say what to do next.

### Activities
1. Write five requirements for the text adventure and the to-do list.
2. Add a `score` command that prints the shared scores.
3. Add the aliases `h` and `l` without copying the lambdas.
4. Describe the data for the capstone in three sentences.

### Accessibility Practice

Prompts and responses are on separate lines and every response is a complete sentence. Test the prompts by listening to them before you add features.

### Skills Checklist
- [ ] I can list requirements.
- [ ] I can design a command loop.
- [ ] I can use a map of lambdas.
- [ ] I handle unknown commands.
- [ ] I handle the end of input.

---

## Lesson 10.2: Text Adventure, Part 1: Rooms and Movement

### Reading References
- [Data classes](https://kotlinlang.org/docs/data-classes.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 10.2: Building a Text-Based Adventure Game (Part 1)

### Learning Objectives
- Represent rooms and exits with a data class and a map.
- Move the player by command.
- Handle impossible moves and the end of input.

### Concept Explanation

A room is a data class with a `description` and an `exits` map from a direction to the *name* of another room. The program remembers the player's location in one variable. A move looks up the command in the current room's exits; if it is found, the location changes, otherwise the program explains that the move is impossible.

This is the same three-room layout as the Python course: a cave, a tunnel, and a clearing. Part 2 adds items and a locked door.

The example is played with north, east, west, up, south, and quit. The command `up` is not an exit anywhere, so it prints the help message.

### Worked Example

```kotlin
data class Room(val description: String, val exits: Map<String, String>)

fun main() {
    val rooms = mapOf(
        "start_room" to Room(
            "You are in a dimly lit cave. There's a narrow passage to the NORTH.",
            mapOf("north" to "tunnel"),
        ),
        "tunnel" to Room(
            "The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.",
            mapOf("south" to "start_room", "east" to "clearing"),
        ),
        "clearing" to Room(
            "You've reached a small, sunny clearing. A faint path leads WEST.",
            mapOf("west" to "tunnel"),
        ),
    )

    var current = "start_room"
    while (true) {
        println("---")
        println(rooms.getValue(current).description)
        println("What do you want to do?")
        val command = (readlnOrNull() ?: "quit").lowercase()
        val next = rooms.getValue(current).exits[command]
        if (next != null) {
            current = next
        } else if (command == "quit") {
            println("Exiting game. Goodbye!")
            break
        } else {
            println("I don't understand that command or you can't go that way.")
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
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

With no standard input at all, the program ends cleanly and prints:
```text
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Looking up a direction with `getValue`, which throws if the key is missing. Use `[]` for a nullable result.
2. Forgetting to treat the end of input as `quit`, so the program loops forever when input is piped in.
3. Misspelling a room name in `exits`, so a move leads to a room that does not exist.

### Activities
1. Trace the six commands by hand and write the room after each one.
2. Add a fourth room reached from the clearing and test it.
3. Add the aliases `n`, `s`, `e`, and `w`.
4. Write a loop that checks that every exit names a real room.

### Accessibility Practice

Each turn prints a separator line, the description, and the prompt, so a whole turn can be read in order. Listen to one turn from start to finish to confirm that a player could follow it without seeing the screen.

### Skills Checklist
- [ ] I can represent rooms with a data class.
- [ ] I can move the player by command.
- [ ] I can handle an impossible move.
- [ ] I treat end of input as quit.
- [ ] I can trace a game by hand.

---

## Lesson 10.3: Text Adventure, Part 2: Items and a Locked Door

### Reading References
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- [Control flow: when](https://kotlinlang.org/docs/control-flow.html#when-expression)
- Matching Python lesson: Lesson 10.3: Building a Text-Based Adventure Game (Part 2)

### Learning Objectives
- Keep items in rooms and in an inventory.
- Implement take and use commands.
- Block and then allow a move through a locked door.

### Concept Explanation

Part 2 adds *state*: items in rooms, an inventory, and a door that is locked until the player uses the key. This is the shared specification used by every language track: three rooms (`start`, `locked_door_room`, `treasure_room`); the commands `north`, `south`, `east`, `west`, `take shiny key`, `use shiny key`, and `quit`; the door between the chamber and the treasure room stays locked until the key is used there; reaching the treasure room ends the game.

Items are a mutable list of names inside each room. Taking an item removes it from the room's list and adds it to the inventory. The locked door is a Boolean variable, `doorLocked`. A move through the door checks it first.

The example is played with: north (into the chamber), north (the locked door refuses), south, take shiny key, north, use shiny key, north (the treasure room).

### Worked Example

```kotlin
class Room(
    val description: String,
    val exits: Map<String, String>,
    val items: MutableList<String> = mutableListOf(),
)

fun main() {
    val rooms = mapOf(
        "start" to Room("A dark cave.", mapOf("north" to "locked_door_room"), mutableListOf("shiny key")),
        "locked_door_room" to Room(
            "A small chamber with a heavy door to the NORTH.",
            mapOf("south" to "start", "north" to "treasure_room"),
        ),
        "treasure_room" to Room("A glittering room full of treasure. You win!", mapOf("south" to "locked_door_room")),
    )

    var current = "start"
    val inventory = mutableListOf<String>()
    var doorLocked = true

    while (true) {
        val room = rooms.getValue(current)
        println()
        println(room.description)
        if (current == "treasure_room") break
        if (room.items.isNotEmpty()) println("You see: ${room.items.joinToString(", ")}")
        println("Your inventory: ${if (inventory.isEmpty()) "empty" else inventory.joinToString(", ")}")
        println("What do you want to do?")

        val command = (readlnOrNull() ?: "quit").lowercase()
        when {
            command == "take shiny key" && "shiny key" in room.items -> {
                room.items.remove("shiny key")
                inventory.add("shiny key")
                println("You picked up the shiny key.")
            }
            command == "use shiny key" && current == "locked_door_room" && "shiny key" in inventory -> {
                doorLocked = false
                println("You unlocked the door!")
            }
            command in room.exits -> {
                if (current == "locked_door_room" && command == "north" && doorLocked) {
                    println("The door is locked! You need a key.")
                } else {
                    current = room.exits.getValue(command)
                }
            }
            command == "quit" -> {
                println("Exiting game. Goodbye!")
                break
            }
            else -> println("I don't understand that command.")
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
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

With no standard input at all, the program ends cleanly and prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Making the door's locked state part of the exits so that the "locked" message can never be reached.
2. Defining an exit to a room that is missing from the `rooms` map, which crashes when the player arrives.
3. Printing a fixed room description that still mentions an item after the player has taken it.

### Activities
1. Play the program with the shown commands and follow each turn on paper.
2. Try `use shiny key` in the cave and describe what happens.
3. Add a second item and require both to open the door.
4. List the game's state (location, inventory, door) and say which command changes each part.

### Accessibility Practice

The room description never mentions the key. A separate 'You see:' line lists items, so the description stays true after the key is taken and the screen reader announces the current state.

### Skills Checklist
- [ ] I can store items in rooms and an inventory.
- [ ] I can implement take and use commands.
- [ ] I can block and allow a move.
- [ ] I can list the game's state.
- [ ] I can keep descriptions true after state changes.

---

## Lesson 10.4: Command-Line To-Do List

### Reading References
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 10.4: Building a Command-Line To-Do List

### Learning Objectives
- Keep records with the shared fields.
- Save and load them as JSON.
- Offer add, view, mark-done, save, load, and quit commands.

### Concept Explanation

A to-do list ties together records, loops, functions, and files. Each task has the shared fields `id`, `title`, `description`, `done`, and `created_at`. The program keeps a list of tasks in memory, shows a numbered menu, and saves the list to `todos.json` when asked and on exit.

Saving uses the teaching JSON helper from Lesson 8.5, included here so the example runs on its own. At start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program: it prints a message and starts with an empty list.

New ids are one more than the highest existing id. The status is shown as the words `done` and `not done`, never with a symbol or color alone.

In the sample session the user adds two tasks, views the list, marks task 2 done, views it again, tries an invalid menu choice, views the list, and quits.

### Worked Example

```kotlin
object Json {
    fun encode(value: Any?): String = when (value) {
        null -> "null"
        is String -> quote(value)
        is Boolean, is Int, is Long, is Double -> value.toString()
        is Map<*, *> -> value.entries.sortedBy { it.key.toString() }
            .joinToString(",", "{", "}") { quote(it.key.toString()) + ":" + encode(it.value) }
        is List<*> -> value.joinToString(",", "[", "]") { encode(it) }
        else -> throw IllegalArgumentException("cannot encode ${value::class.simpleName}")
    }

    private fun quote(text: String): String {
        val out = StringBuilder("\"")
        for (c in text) {
            when {
                c == '"' -> out.append("\\\"")
                c == '\\' -> out.append("\\\\")
                c == '\n' -> out.append("\\n")
                c == '\r' -> out.append("\\r")
                c == '\t' -> out.append("\\t")
                c < ' ' -> out.append("\\u%04x".format(c.code))
                else -> out.append(c)
            }
        }
        return out.append('"').toString()
    }

    fun decode(text: String): Any? = Parser(text).parse()

    private class Parser(private val text: String) {
        private var pos = 0

        private fun fail(message: String): Nothing =
            throw IllegalArgumentException("$message at position $pos")

        private fun skip() {
            while (pos < text.length && text[pos].isWhitespace()) pos++
        }

        fun parse(): Any? {
            val result = value()
            skip()
            if (pos < text.length) fail("unexpected extra text")
            return result
        }

        private fun value(): Any? {
            skip()
            if (pos >= text.length) fail("unexpected end of text")
            val c = text[pos]
            return when {
                c == '{' -> obj()
                c == '[' -> list()
                c == '"' -> str()
                text.startsWith("true", pos) -> { pos += 4; true }
                text.startsWith("false", pos) -> { pos += 5; false }
                text.startsWith("null", pos) -> { pos += 4; null }
                c == '-' || c.isDigit() -> number()
                else -> fail("unexpected character")
            }
        }

        private fun number(): Any {
            val start = pos
            if (text[pos] == '-') pos++
            while (pos < text.length && (text[pos].isDigit() || text[pos] in ".eE+-")) pos++
            val token = text.substring(start, pos)
            return token.toLongOrNull() ?: token.toDoubleOrNull() ?: fail("bad number")
        }

        private fun str(): String {
            pos++
            val out = StringBuilder()
            while (true) {
                if (pos >= text.length) fail("unterminated string")
                val c = text[pos++]
                if (c == '"') return out.toString()
                if (c != '\\') { out.append(c); continue }
                if (pos >= text.length) fail("bad escape")
                when (text[pos++]) {
                    'n' -> out.append('\n')
                    't' -> out.append('\t')
                    'r' -> out.append('\r')
                    '"' -> out.append('"')
                    '\\' -> out.append('\\')
                    '/' -> out.append('/')
                    'u' -> {
                        if (pos + 4 > text.length) fail("bad escape")
                        out.append(text.substring(pos, pos + 4).toInt(16).toChar())
                        pos += 4
                    }
                    else -> fail("bad escape")
                }
            }
        }

        private fun obj(): Map<String, Any?> {
            pos++
            val map = LinkedHashMap<String, Any?>()
            skip()
            if (pos < text.length && text[pos] == '}') { pos++; return map }
            while (true) {
                skip()
                if (pos >= text.length || text[pos] != '"') fail("expected a key")
                val key = str()
                skip()
                if (pos >= text.length || text[pos] != ':') fail("expected ':'")
                pos++
                map[key] = value()
                skip()
                if (pos >= text.length) fail("unterminated object")
                val d = text[pos++]
                if (d == '}') return map
                if (d != ',') { pos--; fail("expected ',' or '}'") }
            }
        }

        private fun list(): List<Any?> {
            pos++
            val items = ArrayList<Any?>()
            skip()
            if (pos < text.length && text[pos] == ']') { pos++; return items }
            while (true) {
                items.add(value())
                skip()
                if (pos >= text.length) fail("unterminated list")
                val d = text[pos++]
                if (d == ']') return items
                if (d != ',') { pos--; fail("expected ',' or ']'") }
            }
        }
    }
}

val todoFile = java.io.File("todos.json")
var todos = mutableListOf<MutableMap<String, Any?>>()

fun loadTodos() {
    if (!todoFile.exists()) {
        println("No existing tasks found.")
        todos = mutableListOf()
        return
    }
    try {
        val data = Json.decode(todoFile.readText()) as List<*>
        todos = data.map { (it as Map<*, *>).entries.associate { e -> e.key.toString() to e.value }.toMutableMap() }.toMutableList()
        println("Tasks loaded.")
    } catch (e: Exception) {
        println("Error: todos.json is not valid JSON. Starting with an empty list.")
        todos = mutableListOf()
    }
}

fun saveTodos() {
    todoFile.writeText(Json.encode(todos))
    println("Tasks saved.")
}

fun nextId(): Long = (todos.maxOfOrNull { it["id"] as Long } ?: 0L) + 1

fun addTask(title: String, description: String) {
    if (title.isBlank()) {
        println("A title is required.")
        return
    }
    val stamp = java.time.LocalDateTime.now().format(java.time.format.DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss"))
    todos.add(mutableMapOf("id" to nextId(), "title" to title.trim(), "description" to description.trim(), "done" to false, "created_at" to stamp))
    println("Task '${title.trim()}' added.")
}

fun viewTasks() {
    if (todos.isEmpty()) {
        println("No tasks in your list.")
        return
    }
    println("--- Your To-Do List ---")
    for (task in todos) {
        val status = if (task["done"] == true) "done" else "not done"
        println("${task["id"]}. ${task["title"]} ($status)")
    }
    println("-----------------------")
}

fun markDone(text: String?) {
    val id = text?.trim()?.toLongOrNull()
    if (id == null) {
        println("Please enter a whole number.")
        return
    }
    val task = todos.firstOrNull { it["id"] == id }
    if (task == null) {
        println("No task has that number.")
        return
    }
    task["done"] = true
    println("Task '${task["title"]}' marked as done.")
}

fun showMenu() {
    println()
    println("--- To-Do List Menu ---")
    println("1. Add Task")
    println("2. View Tasks")
    println("3. Mark Task Done")
    println("4. Save Tasks")
    println("5. Load Tasks")
    println("6. Quit")
    println("-----------------------")
}

fun main() {
    loadTodos()
    while (true) {
        showMenu()
        println("Enter your choice (1-6):")
        val choice = readlnOrNull() ?: "6"
        when (choice) {
            "1" -> {
                println("Enter task title:")
                val title = readlnOrNull() ?: ""
                println("Enter task description:")
                val description = readlnOrNull() ?: ""
                addTask(title, description)
            }
            "2" -> viewTasks()
            "3" -> {
                viewTasks()
                println("Enter task number to mark done:")
                markDone(readlnOrNull())
            }
            "4" -> saveTodos()
            "5" -> loadTodos()
            "6" -> {
                saveTodos()
                println("Goodbye!")
                return
            }
            else -> println("Invalid choice. Please try again.")
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
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

With no standard input at all, the program ends cleanly and prints:
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
- [ ] I can keep records with the shared fields.
- [ ] I can save and load JSON.
- [ ] I handle a missing or damaged file.
- [ ] I keep ids unique.
- [ ] I show status in words.

---

## Lesson 10.5: User Experience and Input Validation

### Reading References
- [Functions](https://kotlinlang.org/docs/functions.html)
- [Null safety](https://kotlinlang.org/docs/null-safety.html)
- Matching Python lesson: Lesson 10.5: Refining User Experience and Validation

### Learning Objectives
- Write reusable validation functions.
- Limit retries and handle the end of input.
- Write clear, accessible messages.

### Concept Explanation

Reusable validation functions make every menu and form consistent. `askNumber(prompt, low, high, attempts)` prints a prompt, reads a line, converts it, checks the range, and either returns the number or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns `null`. `askYesNo(prompt)` accepts `y`, `yes`, `n`, and `no` in any letter case.

Good messages say *what was wrong* and *what to do*: "Enter a whole number from 0 to 100," not "Invalid." They never depend on color, position, or symbols alone, and they use the same wording every time. The return type `Int?` makes the caller deal with the failure case.

The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y.

### Worked Example

```kotlin
fun askNumber(prompt: String, low: Int, high: Int, attempts: Int): Int? {
    for (attempt in 1..attempts) {
        println(prompt)
        val text = readlnOrNull() ?: return null
        val number = text.trim().toIntOrNull()
        if (number != null && number in low..high) return number
        println("Enter a whole number from $low to $high. You have ${attempts - attempt} attempt(s) left.")
    }
    return null
}

fun askYesNo(prompt: String): Boolean? {
    while (true) {
        println("$prompt (yes or no)")
        val text = readlnOrNull()?.trim()?.lowercase() ?: return null
        if (text == "y" || text == "yes") return true
        if (text == "n" || text == "no") return false
        println("Please answer yes or no.")
    }
}

fun main() {
    val score = askNumber("Enter a score from 0 to 100:", 0, 100, 3)
    if (score != null) {
        println("Accepted score: $score")
    } else {
        println("No valid score was entered.")
    }

    val keep = askYesNo("Save this score?")
    println("Save answer: $keep")
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
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
Save answer: true
```

With no standard input at all, the program ends cleanly and prints:
```text
Enter a score from 0 to 100:
No valid score was entered.
Save this score? (yes or no)
Save answer: null
```

### Common Mistakes
1. Writing the message "Invalid" without saying what is valid.
2. Accepting a decimal such as 88.5 for a field that requires a whole number.
3. Looping forever on bad input instead of limiting attempts.

### Activities
1. Run the sample input and read each message aloud.
2. Run with three invalid numbers and read the final message.
3. Add `askText(prompt)` that rejects empty answers.
4. Rewrite two messages from earlier lessons so they say what to do next.

### Accessibility Practice

Check that every error message ends with an action the user can take, and that the same situation always produces the same words.

### Skills Checklist
- [ ] I can write reusable validation functions.
- [ ] I limit retries.
- [ ] I handle the end of input.
- [ ] I write messages that say what to do.
- [ ] I keep wording consistent.

---
