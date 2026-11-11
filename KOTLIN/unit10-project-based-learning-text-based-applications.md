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

## Lesson 10.2: Text Adventure, Part 1: Five Rooms and Movement

### Reading References
- [Data classes](https://kotlinlang.org/docs/data-classes.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Canonical shared project specification: Python Unit 10, Lesson 10.3

### Learning Objectives
- Represent the five canonical rooms and their exits with Kotlin data.
- Move through valid exits without changing location after an invalid command.
- Explain why the north exit from the locked-door room is not available yet.

### Concept Explanation

The shared adventure has five rooms: start_room, tunnel, clearing, locked_door_room, and treasure_room. The unconditional connections are start north to tunnel; tunnel south to start and east to clearing; clearing west to tunnel and north to the locked-door room; and locked-door room south to clearing. The north exit to the treasure room is conditional and is added in Part 2 only after the shiny-key puzzle is solved.

A Room data class stores a description and a map of exits. Looking up a missing direction with square brackets returns null; it does not change the current room.

### Worked Example

```kotlin
data class Room(val description: String, val exits: Map<String, String>)

fun main() {
    val rooms = mapOf(
        "start_room" to Room("A dimly lit cave. A narrow passage leads north.", mapOf("north" to "tunnel")),
        "tunnel" to Room("A damp tunnel. Passages lead south and east.", mapOf("south" to "start_room", "east" to "clearing")),
        "clearing" to Room("A quiet clearing. An antechamber lies to the north.", mapOf("west" to "tunnel", "north" to "locked_door_room")),
        "locked_door_room" to Room("A chamber with a heavy door to the north.", mapOf("south" to "clearing")),
        "treasure_room" to Room("You found the treasure. You win!", emptyMap()),
    )

    var currentRoom = "start_room"
    while (true) {
        println("---")
        println(rooms.getValue(currentRoom).description)
        println("What do you want to do?")
        val command = (readlnOrNull() ?: "quit").trim().lowercase()
        val destination = rooms.getValue(currentRoom).exits[command]
        when {
            command == "quit" -> {
                println("Exiting game. Goodbye!")
                break
            }
            destination != null -> currentRoom = destination
            else -> println("You cannot go that way. Enter a listed direction or quit.")
        }
    }
}
```

### Expected Behavior or Output

With north, east, north, north, quit entered as separate input lines, the player visits tunnel, clearing, and locked_door_room. The second north from locked_door_room is rejected and the current room does not change. The treasure room exists in the model but cannot be reached in Part 1.

### Common Mistakes
1. Adding the treasure-room north exit before implementing the key puzzle.
2. Updating currentRoom before confirming that the requested exit exists.
3. Using getValue on an exit map when the direction may be absent.
4. Defining an exit whose destination is not one of the five room identifiers.

### Activities
1. Trace north, east, north, north and record the room after each command.
2. Try west from start_room; confirm that the location does not change.
3. Check that every destination in every unconditional exit exists in rooms.
4. Explain why treasure_room has no incoming exit in Part 1.

### Accessibility Practice

Read the separator, room description, and prompt in order. The invalid-movement response explains what happened and how to continue. Test the sequence by listening to terminal output; do not rely on a visual map.

### Skills Checklist
- [ ] I can model all five canonical rooms.
- [ ] I can represent exits with a map.
- [ ] I can move only when an exit exists.
- [ ] I can reject an invalid direction without changing state.
- [ ] I can explain why the treasure room is not yet reachable.

---

## Lesson 10.3: Text Adventure, Part 2: Shiny Key and Locked Door

### Reading References
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- [Control flow: when](https://kotlinlang.org/docs/control-flow.html#when-expression)
- Canonical shared project specification: Python Unit 10, Lesson 10.3

### Learning Objectives
- Place the shiny key in start_room and transfer it to inventory exactly once.
- Require the player to use the key while in locked_door_room.
- Unlock the north exit to treasure_room only after the puzzle succeeds.
- End the game when the player reaches the treasure room.

### Concept Explanation

Part 2 keeps the same five-room graph. The shiny key begins in start_room. The take shiny key command removes it from that room and adds it to inventory. The use shiny key command works only in locked_door_room and only when the key is in inventory. Attempting north from the locked-door room before that action prints a locked-door message and leaves the player in place. After the key is used, north leads to treasure_room.

Room descriptions do not claim that an item is still present. Room items and inventory are announced on separate lines.

### Worked Example

```kotlin
class Room(
    val description: String,
    val exits: Map<String, String>,
    val items: MutableList<String> = mutableListOf(),
)

fun main() {
    val rooms = mapOf(
        "start_room" to Room("A dimly lit cave.", mapOf("north" to "tunnel"), mutableListOf("shiny key")),
        "tunnel" to Room("A damp tunnel. Passages lead south and east.", mapOf("south" to "start_room", "east" to "clearing")),
        "clearing" to Room("A quiet clearing. An antechamber lies to the north.", mapOf("west" to "tunnel", "north" to "locked_door_room")),
        "locked_door_room" to Room("A chamber with a heavy door to the north.", mapOf("south" to "clearing", "north" to "treasure_room")),
        "treasure_room" to Room("You found the treasure. You win!", emptyMap()),
    )
    var currentRoom = "start_room"
    val inventory = mutableListOf<String>()
    var doorLocked = true

    while (true) {
        val room = rooms.getValue(currentRoom)
        println()
        println(room.description)
        if (currentRoom == "treasure_room") break
        if (room.items.isNotEmpty()) println("You see: " + room.items.joinToString(", "))
        println("Your inventory: " + if (inventory.isEmpty()) "empty" else inventory.joinToString(", "))
        println("What do you want to do?")
        val command = (readlnOrNull() ?: "quit").trim().lowercase()

        when {
            command == "quit" -> {
                println("You quit the adventure.")
                break
            }
            command == "take shiny key" -> {
                if (room.items.remove("shiny key")) {
                    inventory.add("shiny key")
                    println("You picked up the shiny key.")
                } else println("There is no shiny key here to take.")
            }
            command == "use shiny key" -> when {
                currentRoom != "locked_door_room" -> println("You must be at the locked door to use the key.")
                "shiny key" !in inventory -> println("You do not have the shiny key.")
                else -> {
                    doorLocked = false
                    println("You unlocked the door!")
                }
            }
            currentRoom == "locked_door_room" && command == "north" && doorLocked ->
                println("The door is locked! You need to use the shiny key here.")
            command in room.exits -> currentRoom = room.exits.getValue(command)
            else -> println("Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.")
        }
    }
}
```

### Expected Behavior or Output

Use this sequence to verify the puzzle: north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north.

The first north attempt from locked_door_room must be rejected. Taking the key removes it from start_room and adds it to inventory. Using it outside locked_door_room must be rejected. Using it there prints You unlocked the door!; the next north reaches treasure_room and prints You found the treasure. You win!. End-of-file is treated as quit.

### Common Mistakes
1. Leaving the shiny key in the room after adding it to inventory.
2. Unlocking the door outside locked_door_room.
3. Unlocking the door without checking inventory.
4. Allowing north movement before doorLocked becomes false.
5. Describing the key as still on the floor after it has been collected.

### Activities
1. Run the full sequence and record room, room items, inventory, and door state after every command.
2. Try take shiny key twice; the second attempt must not duplicate the item.
3. Try use shiny key in start_room and clearing; both attempts must be rejected.
4. Try north from locked_door_room before and after unlocking.
5. Add a look command that announces room, visible items, inventory, and exits in a consistent order.

### Accessibility Practice

Announce room description, visible items, inventory, and prompt as separate text lines. Every failed action explains why it failed. Listen to the full puzzle sequence and verify that key location and door state are unambiguous.

### Skills Checklist
- [ ] I can model the five canonical rooms.
- [ ] I can transfer the shiny key from a room to inventory.
- [ ] I can prevent duplicate pickup.
- [ ] I can require key use in the locked-door room.
- [ ] I can block and unlock the north exit.
- [ ] I can end the game when the treasure room is reached.

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
