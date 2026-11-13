[Header 2 ("unit-10-project-based-learning--text-based-applications", [], []) [Str "Unit 10: Project-Based Learning — Text-Based Applications"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Plan a text project, build the shared text adventure in two parts, build the command-line to-do manager, and refine input validation."], HorizontalRule, Header 3 ("lesson-101-planning-a-text-based-project", ["unnumbered", "unlisted"], []) [Str "Lesson 10.1: Planning a Text-Based Project"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Functions: function types"] ("https://kotlinlang.org/docs/lambdas.html", "")]], [Plain [Link ("", [], []) [Str "Collections overview"] ("https://kotlinlang.org/docs/collections-overview.html", "")]], [Plain [Str "Matching Python lesson: Lesson 10.1: Project Planning and Design"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write a short requirements list."]], [Plain [Str "Design a command loop with a map of handlers."]], [Plain [Str "Plan in small steps and test each one."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A project is easier to finish when it is planned in small steps. Write down what the program must do (", Emph [Str "requirements"], Str "), what information it keeps (", Emph [Str "data"], Str "), and the commands a person can give (", Emph [Str "interface"], Str "). Build one small piece, test it, then add the next."], Para [Str "Text-based projects share a ", Emph [Str "command loop"], Str ": show a prompt, read a line, find the matching action, and repeat until the user quits. In Kotlin, a ", Code ("", [], []) "Map<String, () -> Unit>", Str " holds actions: the keys are command names and the values are ", Emph [Str "lambdas"], Str ", small functions with no name. A new command is one new entry, and an unknown command is a failed lookup that prints a helpful message."], Para [Str "The loop stops on ", Code ("", [], []) "quit", Str " and also when input ends (", Code ("", [], []) "null", Str "). The example is a skeleton with two commands; typing ", Code ("", [], []) "help", Str ", ", Code ("", [], []) "look", Str ", an unknown word, and ", Code ("", [], []) "quit", Str " shows each path."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun main() {
    val commands: Map<String, () -> Unit> = mapOf(
        \"help\" to { println(\"Commands: help, look, quit\") },
        \"look\" to { println(\"You are in a dark cave.\") },
    )

    println(\"Type a command:\")
    var line = readlnOrNull()
    while (line != null && line != \"quit\") {
        val handler = commands[line]
        if (handler != null) {
            handler()
        } else {
            println(\"I don't understand that command. Type help for a list.\")
        }
        println(\"Type a command:\")
        line = readlnOrNull()
    }
    println(\"Goodbye!\")
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "help
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
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "Type a command:
Goodbye!
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Starting to code before listing the requirements."]], [Plain [Str "Using a long chain of ", Code ("", [], []) "if", Str " statements instead of a map of handlers."]], [Plain [Str "Forgetting that an unknown command should say what to do next."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write five requirements for the text adventure and the to-do list."]], [Plain [Str "Add a ", Code ("", [], []) "score", Str " command that prints the shared scores."]], [Plain [Str "Add the aliases ", Code ("", [], []) "h", Str " and ", Code ("", [], []) "l", Str " without copying the lambdas."]], [Plain [Str "Describe the data for the capstone in three sentences."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Prompts and responses are on separate lines and every response is a complete sentence. Test the prompts by listening to them before you add features."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can list requirements."]], [Plain [Str "\9744", Space, Str "I can design a command loop."]], [Plain [Str "\9744", Space, Str "I can use a map of lambdas."]], [Plain [Str "\9744", Space, Str "I handle unknown commands."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]]], HorizontalRule, Header 3 ("lesson-102-text-adventure-part-1-five-rooms-and-movement", ["unnumbered", "unlisted"], []) [Str "Lesson 10.2: Text Adventure, Part 1: Five Rooms and Movement"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Data classes"] ("https://kotlinlang.org/docs/data-classes.html", "")]], [Plain [Link ("", [], []) [Str "Collections overview"] ("https://kotlinlang.org/docs/collections-overview.html", "")]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Represent the five canonical rooms and their exits with Kotlin data."]], [Plain [Str "Move through valid exits without changing location after an invalid command."]], [Plain [Str "Explain why the north exit from the locked-door room is not available yet."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The shared adventure has five rooms: start_room, tunnel, clearing, locked_door_room, and treasure_room. The unconditional connections are start north to tunnel; tunnel south to start and east to clearing; clearing west to tunnel and north to the locked-door room; and locked-door room south to clearing. The north exit to the treasure room is conditional and is added in Part 2 only after the shiny-key puzzle is solved."], Para [Str "A Room data class stores a description and a map of exits. Looking up a missing direction with square brackets returns null; it does not change the current room."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "data class Room(val description: String, val exits: Map<String, String>)

fun main() {
    val rooms = mapOf(
        \"start_room\" to Room(\"A dimly lit cave. A narrow passage leads north.\", mapOf(\"north\" to \"tunnel\")),
        \"tunnel\" to Room(\"A damp tunnel. Passages lead south and east.\", mapOf(\"south\" to \"start_room\", \"east\" to \"clearing\")),
        \"clearing\" to Room(\"A quiet clearing. An antechamber lies to the north.\", mapOf(\"west\" to \"tunnel\", \"north\" to \"locked_door_room\")),
        \"locked_door_room\" to Room(\"A chamber with a heavy door to the north.\", mapOf(\"south\" to \"clearing\")),
        \"treasure_room\" to Room(\"You found the treasure. You win!\", emptyMap()),
    )

    var currentRoom = \"start_room\"
    while (true) {
        println(\"---\")
        println(rooms.getValue(currentRoom).description)
        println(\"What do you want to do?\")
        val command = (readlnOrNull() ?: \"quit\").trim().lowercase()
        val destination = rooms.getValue(currentRoom).exits[command]
        when {
            command == \"quit\" -> {
                println(\"Exiting game. Goodbye!\")
                break
            }
            destination != null -> currentRoom = destination
            else -> println(\"You cannot go that way. Enter a listed direction or quit.\")
        }
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With north, east, north, north, quit entered as separate input lines, the player visits tunnel, clearing, and locked_door_room. The second north from locked_door_room is rejected and the current room does not change. The treasure room exists in the model but cannot be reached in Part 1."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Adding the treasure-room north exit before implementing the key puzzle."]], [Plain [Str "Updating currentRoom before confirming that the requested exit exists."]], [Plain [Str "Using getValue on an exit map when the direction may be absent."]], [Plain [Str "Defining an exit whose destination is not one of the five room identifiers."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace north, east, north, north and record the room after each command."]], [Plain [Str "Try west from start_room; confirm that the location does not change."]], [Plain [Str "Check that every destination in every unconditional exit exists in rooms."]], [Plain [Str "Explain why treasure_room has no incoming exit in Part 1."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the separator, room description, and prompt in order. The invalid-movement response explains what happened and how to continue. Test the sequence by listening to terminal output; do not rely on a visual map."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model all five canonical rooms."]], [Plain [Str "\9744", Space, Str "I can represent exits with a map."]], [Plain [Str "\9744", Space, Str "I can move only when an exit exists."]], [Plain [Str "\9744", Space, Str "I can reject an invalid direction without changing state."]], [Plain [Str "\9744", Space, Str "I can explain why the treasure room is not yet reachable."]]], HorizontalRule, Header 3 ("lesson-103-text-adventure-part-2-shiny-key-and-locked-door", ["unnumbered", "unlisted"], []) [Str "Lesson 10.3: Text Adventure, Part 2: Shiny Key and Locked Door"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Collections overview"] ("https://kotlinlang.org/docs/collections-overview.html", "")]], [Plain [Link ("", [], []) [Str "Control flow: when"] ("https://kotlinlang.org/docs/control-flow.html#when-expression", "")]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Place the shiny key in start_room and transfer it to inventory exactly once."]], [Plain [Str "Require the player to use the key while in locked_door_room."]], [Plain [Str "Unlock the north exit to treasure_room only after the puzzle succeeds."]], [Plain [Str "End the game when the player reaches the treasure room."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Part 2 keeps the same five-room graph. The shiny key begins in start_room. The take shiny key command removes it from that room and adds it to inventory. The use shiny key command works only in locked_door_room and only when the key is in inventory. Attempting north from the locked-door room before that action prints a locked-door message and leaves the player in place. After the key is used, north leads to treasure_room."], Para [Str "Room descriptions do not claim that an item is still present. Room items and inventory are announced on separate lines."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "class Room(
    val description: String,
    val exits: Map<String, String>,
    val items: MutableList<String> = mutableListOf(),
)

fun main() {
    val rooms = mapOf(
        \"start_room\" to Room(\"A dimly lit cave.\", mapOf(\"north\" to \"tunnel\"), mutableListOf(\"shiny key\")),
        \"tunnel\" to Room(\"A damp tunnel. Passages lead south and east.\", mapOf(\"south\" to \"start_room\", \"east\" to \"clearing\")),
        \"clearing\" to Room(\"A quiet clearing. An antechamber lies to the north.\", mapOf(\"west\" to \"tunnel\", \"north\" to \"locked_door_room\")),
        \"locked_door_room\" to Room(\"A chamber with a heavy door to the north.\", mapOf(\"south\" to \"clearing\", \"north\" to \"treasure_room\")),
        \"treasure_room\" to Room(\"You found the treasure. You win!\", emptyMap()),
    )
    var currentRoom = \"start_room\"
    val inventory = mutableListOf<String>()
    var doorLocked = true

    while (true) {
        val room = rooms.getValue(currentRoom)
        println()
        println(room.description)
        if (currentRoom == \"treasure_room\") break
        if (room.items.isNotEmpty()) println(\"You see: \" + room.items.joinToString(\", \"))
        println(\"Your inventory: \" + if (inventory.isEmpty()) \"empty\" else inventory.joinToString(\", \"))
        println(\"What do you want to do?\")
        val command = (readlnOrNull() ?: \"quit\").trim().lowercase()

        when {
            command == \"quit\" -> {
                println(\"You quit the adventure.\")
                break
            }
            command == \"take shiny key\" -> {
                if (room.items.remove(\"shiny key\")) {
                    inventory.add(\"shiny key\")
                    println(\"You picked up the shiny key.\")
                } else println(\"There is no shiny key here to take.\")
            }
            command == \"use shiny key\" -> when {
                currentRoom != \"locked_door_room\" -> println(\"You must be at the locked door to use the key.\")
                \"shiny key\" !in inventory -> println(\"You do not have the shiny key.\")
                else -> {
                    doorLocked = false
                    println(\"You unlocked the door!\")
                }
            }
            currentRoom == \"locked_door_room\" && command == \"north\" && doorLocked ->
                println(\"The door is locked! You need to use the shiny key here.\")
            command in room.exits -> currentRoom = room.exits.getValue(command)
            else -> println(\"Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.\")
        }
    }
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Use this sequence to verify the puzzle: north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north."], Para [Str "The first north attempt from locked_door_room must be rejected. Taking the key removes it from start_room and adds it to inventory. Using it outside locked_door_room must be rejected. Using it there prints You unlocked the door!; the next north reaches treasure_room and prints You found the treasure. You win!. End-of-file is treated as quit."], Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Leaving the shiny key in the room after adding it to inventory."]], [Plain [Str "Unlocking the door outside locked_door_room."]], [Plain [Str "Unlocking the door without checking inventory."]], [Plain [Str "Allowing north movement before doorLocked becomes false."]], [Plain [Str "Describing the key as still on the floor after it has been collected."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the full sequence and record room, room items, inventory, and door state after every command."]], [Plain [Str "Try take shiny key twice; the second attempt must not duplicate the item."]], [Plain [Str "Try use shiny key in start_room and clearing; both attempts must be rejected."]], [Plain [Str "Try north from locked_door_room before and after unlocking."]], [Plain [Str "Add a look command that announces room, visible items, inventory, and exits in a consistent order."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Announce room description, visible items, inventory, and prompt as separate text lines. Every failed action explains why it failed. Listen to the full puzzle sequence and verify that key location and door state are unambiguous."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model the five canonical rooms."]], [Plain [Str "\9744", Space, Str "I can transfer the shiny key from a room to inventory."]], [Plain [Str "\9744", Space, Str "I can prevent duplicate pickup."]], [Plain [Str "\9744", Space, Str "I can require key use in the locked-door room."]], [Plain [Str "\9744", Space, Str "I can block and unlock the north exit."]], [Plain [Str "\9744", Space, Str "I can end the game when the treasure room is reached."]]], HorizontalRule, Header 3 ("lesson-104-command-line-to-do-list", ["unnumbered", "unlisted"], []) [Str "Lesson 10.4: Command-Line To-Do List"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Collections overview"] ("https://kotlinlang.org/docs/collections-overview.html", "")]], [Plain [Link ("", [], []) [Str "Exceptions"] ("https://kotlinlang.org/docs/exceptions.html", "")]], [Plain [Str "Matching Python lesson: Lesson 10.4: Building a Command-Line To-Do List"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Keep records with the shared fields."]], [Plain [Str "Save and load them as JSON."]], [Plain [Str "Offer add, view, mark-done, save, load, and quit commands."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A to-do list ties together records, loops, functions, and files. Each task has the shared fields ", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "done", Str ", and ", Code ("", [], []) "created_at", Str ". The program keeps a list of tasks in memory, shows a numbered menu, and saves the list to ", Code ("", [], []) "todos.json", Str " when asked and on exit."], Para [Str "Saving uses the teaching JSON helper from Lesson 8.5, included here so the example runs on its own. At start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program: it prints a message and starts with an empty list."], Para [Str "New ids are one more than the highest existing id. The status is shown as the words ", Code ("", [], []) "done", Str " and ", Code ("", [], []) "not done", Str ", never with a symbol or color alone."], Para [Str "In the sample session the user adds two tasks, views the list, marks task 2 done, views it again, tries an invalid menu choice, views the list, and quits."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "object Json {
    fun encode(value: Any?): String = when (value) {
        null -> \"null\"
        is String -> quote(value)
        is Boolean, is Int, is Long, is Double -> value.toString()
        is Map<*, *> -> value.entries.sortedBy { it.key.toString() }
            .joinToString(\",\", \"{\", \"}\") { quote(it.key.toString()) + \":\" + encode(it.value) }
        is List<*> -> value.joinToString(\",\", \"[\", \"]\") { encode(it) }
        else -> throw IllegalArgumentException(\"cannot encode ${value::class.simpleName}\")
    }

    private fun quote(text: String): String {
        val out = StringBuilder(\"\\\"\")
        for (c in text) {
            when {
                c == '\"' -> out.append(\"\\\\\\\"\")
                c == '\\\\' -> out.append(\"\\\\\\\\\")
                c == '\\n' -> out.append(\"\\\\n\")
                c == '\\r' -> out.append(\"\\\\r\")
                c == '\\t' -> out.append(\"\\\\t\")
                c < ' ' -> out.append(\"\\\\u%04x\".format(c.code))
                else -> out.append(c)
            }
        }
        return out.append('\"').toString()
    }

    fun decode(text: String): Any? = Parser(text).parse()

    private class Parser(private val text: String) {
        private var pos = 0

        private fun fail(message: String): Nothing =
            throw IllegalArgumentException(\"$message at position $pos\")

        private fun skip() {
            while (pos < text.length && text[pos].isWhitespace()) pos++
        }

        fun parse(): Any? {
            val result = value()
            skip()
            if (pos < text.length) fail(\"unexpected extra text\")
            return result
        }

        private fun value(): Any? {
            skip()
            if (pos >= text.length) fail(\"unexpected end of text\")
            val c = text[pos]
            return when {
                c == '{' -> obj()
                c == '[' -> list()
                c == '\"' -> str()
                text.startsWith(\"true\", pos) -> { pos += 4; true }
                text.startsWith(\"false\", pos) -> { pos += 5; false }
                text.startsWith(\"null\", pos) -> { pos += 4; null }
                c == '-' || c.isDigit() -> number()
                else -> fail(\"unexpected character\")
            }
        }

        private fun number(): Any {
            val start = pos
            if (text[pos] == '-') pos++
            while (pos < text.length && (text[pos].isDigit() || text[pos] in \".eE+-\")) pos++
            val token = text.substring(start, pos)
            return token.toLongOrNull() ?: token.toDoubleOrNull() ?: fail(\"bad number\")
        }

        private fun str(): String {
            pos++
            val out = StringBuilder()
            while (true) {
                if (pos >= text.length) fail(\"unterminated string\")
                val c = text[pos++]
                if (c == '\"') return out.toString()
                if (c != '\\\\') { out.append(c); continue }
                if (pos >= text.length) fail(\"bad escape\")
                when (text[pos++]) {
                    'n' -> out.append('\\n')
                    't' -> out.append('\\t')
                    'r' -> out.append('\\r')
                    '\"' -> out.append('\"')
                    '\\\\' -> out.append('\\\\')
                    '/' -> out.append('/')
                    'u' -> {
                        if (pos + 4 > text.length) fail(\"bad escape\")
                        out.append(text.substring(pos, pos + 4).toInt(16).toChar())
                        pos += 4
                    }
                    else -> fail(\"bad escape\")
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
                if (pos >= text.length || text[pos] != '\"') fail(\"expected a key\")
                val key = str()
                skip()
                if (pos >= text.length || text[pos] != ':') fail(\"expected ':'\")
                pos++
                map[key] = value()
                skip()
                if (pos >= text.length) fail(\"unterminated object\")
                val d = text[pos++]
                if (d == '}') return map
                if (d != ',') { pos--; fail(\"expected ',' or '}'\") }
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
                if (pos >= text.length) fail(\"unterminated list\")
                val d = text[pos++]
                if (d == ']') return items
                if (d != ',') { pos--; fail(\"expected ',' or ']'\") }
            }
        }
    }
}

val todoFile = java.io.File(\"todos.json\")
var todos = mutableListOf<MutableMap<String, Any?>>()

fun loadTodos() {
    if (!todoFile.exists()) {
        println(\"No existing tasks found.\")
        todos = mutableListOf()
        return
    }
    try {
        val data = Json.decode(todoFile.readText()) as List<*>
        todos = data.map { (it as Map<*, *>).entries.associate { e -> e.key.toString() to e.value }.toMutableMap() }.toMutableList()
        println(\"Tasks loaded.\")
    } catch (e: Exception) {
        println(\"Error: todos.json is not valid JSON. Starting with an empty list.\")
        todos = mutableListOf()
    }
}

fun saveTodos() {
    todoFile.writeText(Json.encode(todos))
    println(\"Tasks saved.\")
}

fun nextId(): Long = (todos.maxOfOrNull { it[\"id\"] as Long } ?: 0L) + 1

fun addTask(title: String, description: String) {
    if (title.isBlank()) {
        println(\"A title is required.\")
        return
    }
    val stamp = java.time.LocalDateTime.now().format(java.time.format.DateTimeFormatter.ofPattern(\"yyyy-MM-dd'T'HH:mm:ss\"))
    todos.add(mutableMapOf(\"id\" to nextId(), \"title\" to title.trim(), \"description\" to description.trim(), \"done\" to false, \"created_at\" to stamp))
    println(\"Task '${title.trim()}' added.\")
}

fun viewTasks() {
    if (todos.isEmpty()) {
        println(\"No tasks in your list.\")
        return
    }
    println(\"--- Your To-Do List ---\")
    for (task in todos) {
        val status = if (task[\"done\"] == true) \"done\" else \"not done\"
        println(\"${task[\"id\"]}. ${task[\"title\"]} ($status)\")
    }
    println(\"-----------------------\")
}

fun markDone(text: String?) {
    val id = text?.trim()?.toLongOrNull()
    if (id == null) {
        println(\"Please enter a whole number.\")
        return
    }
    val task = todos.firstOrNull { it[\"id\"] == id }
    if (task == null) {
        println(\"No task has that number.\")
        return
    }
    task[\"done\"] = true
    println(\"Task '${task[\"title\"]}' marked as done.\")
}

fun showMenu() {
    println()
    println(\"--- To-Do List Menu ---\")
    println(\"1. Add Task\")
    println(\"2. View Tasks\")
    println(\"3. Mark Task Done\")
    println(\"4. Save Tasks\")
    println(\"5. Load Tasks\")
    println(\"6. Quit\")
    println(\"-----------------------\")
}

fun main() {
    loadTodos()
    while (true) {
        showMenu()
        println(\"Enter your choice (1-6):\")
        val choice = readlnOrNull() ?: \"6\"
        when (choice) {
            \"1\" -> {
                println(\"Enter task title:\")
                val title = readlnOrNull() ?: \"\"
                println(\"Enter task description:\")
                val description = readlnOrNull() ?: \"\"
                addTask(title, description)
            }
            \"2\" -> viewTasks()
            \"3\" -> {
                viewTasks()
                println(\"Enter task number to mark done:\")
                markDone(readlnOrNull())
            }
            \"4\" -> saveTodos()
            \"5\" -> loadTodos()
            \"6\" -> {
                saveTodos()
                println(\"Goodbye!\")
                return
            }
            else -> println(\"Invalid choice. Please try again.\")
        }
    }
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "1
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
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "No existing tasks found.

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
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Saving the file but never loading it, so tasks disappear between runs."]], [Plain [Str "Reusing a deleted task's id, which can confuse saved references."]], [Plain [Str "Letting a damaged ", Code ("", [], []) "todos.json", Str " crash the program instead of printing a message."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the sample session, then run the program again typing ", Code ("", [], []) "2", Str " and ", Code ("", [], []) "6", Str " to see the saved tasks."]], [Plain [Str "Add a command to delete a task by number."]], [Plain [Str "Open ", Code ("", [], []) "todos.json", Str " and read the saved text. Edit it to remove a bracket and run the program again."]], [Plain [Str "Show each task's description in the view command."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Every menu is printed as numbered lines and every prompt is on its own line. The status words are ", Code ("", [], []) "done", Str " and ", Code ("", [], []) "not done", Str ", not symbols, so the list reads clearly in speech and braille."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can keep records with the shared fields."]], [Plain [Str "\9744", Space, Str "I can save and load JSON."]], [Plain [Str "\9744", Space, Str "I handle a missing or damaged file."]], [Plain [Str "\9744", Space, Str "I keep ids unique."]], [Plain [Str "\9744", Space, Str "I show status in words."]]], HorizontalRule, Header 3 ("lesson-105-user-experience-and-input-validation", ["unnumbered", "unlisted"], []) [Str "Lesson 10.5: User Experience and Input Validation"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Functions"] ("https://kotlinlang.org/docs/functions.html", "")]], [Plain [Link ("", [], []) [Str "Null safety"] ("https://kotlinlang.org/docs/null-safety.html", "")]], [Plain [Str "Matching Python lesson: Lesson 10.5: Refining User Experience and Validation"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write reusable validation functions."]], [Plain [Str "Limit retries and handle the end of input."]], [Plain [Str "Write clear, accessible messages."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Reusable validation functions make every menu and form consistent. ", Code ("", [], []) "askNumber(prompt, low, high, attempts)", Str " prints a prompt, reads a line, converts it, checks the range, and either returns the number or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns ", Code ("", [], []) "null", Str ". ", Code ("", [], []) "askYesNo(prompt)", Str " accepts ", Code ("", [], []) "y", Str ", ", Code ("", [], []) "yes", Str ", ", Code ("", [], []) "n", Str ", and ", Code ("", [], []) "no", Str " in any letter case."], Para [Str "Good messages say ", Emph [Str "what was wrong"], Str " and ", Emph [Str "what to do"], Str ": \"Enter a whole number from 0 to 100,\" not \"Invalid.\" They never depend on color, position, or symbols alone, and they use the same wording every time. The return type ", Code ("", [], []) "Int?", Str " makes the caller deal with the failure case."], Para [Str "The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun askNumber(prompt: String, low: Int, high: Int, attempts: Int): Int? {
    for (attempt in 1..attempts) {
        println(prompt)
        val text = readlnOrNull() ?: return null
        val number = text.trim().toIntOrNull()
        if (number != null && number in low..high) return number
        println(\"Enter a whole number from $low to $high. You have ${attempts - attempt} attempt(s) left.\")
    }
    return null
}

fun askYesNo(prompt: String): Boolean? {
    while (true) {
        println(\"$prompt (yes or no)\")
        val text = readlnOrNull()?.trim()?.lowercase() ?: return null
        if (text == \"y\" || text == \"yes\") return true
        if (text == \"n\" || text == \"no\") return false
        println(\"Please answer yes or no.\")
    }
}

fun main() {
    val score = askNumber(\"Enter a score from 0 to 100:\", 0, 100, 3)
    if (score != null) {
        println(\"Accepted score: $score\")
    } else {
        println(\"No valid score was entered.\")
    }

    val keep = askYesNo(\"Save this score?\")
    println(\"Save answer: $keep\")
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "abc
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
Save answer: true
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "Enter a score from 0 to 100:
No valid score was entered.
Save this score? (yes or no)
Save answer: null
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing the message \"Invalid\" without saying what is valid."]], [Plain [Str "Accepting a decimal such as 88.5 for a field that requires a whole number."]], [Plain [Str "Looping forever on bad input instead of limiting attempts."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the sample input and read each message aloud."]], [Plain [Str "Run with three invalid numbers and read the final message."]], [Plain [Str "Add ", Code ("", [], []) "askText(prompt)", Str " that rejects empty answers."]], [Plain [Str "Rewrite two messages from earlier lessons so they say what to do next."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Check that every error message ends with an action the user can take, and that the same situation always produces the same words."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write reusable validation functions."]], [Plain [Str "\9744", Space, Str "I limit retries."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]], [Plain [Str "\9744", Space, Str "I write messages that say what to do."]], [Plain [Str "\9744", Space, Str "I keep wording consistent."]]], HorizontalRule]