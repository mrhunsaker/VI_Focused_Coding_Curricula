# Unit 10: Project-Based Learning — Text Applications

## Overview

This unit develops project-based learning — text applications through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing.

**Unit objectives:** explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects.

## Lesson 10.1: Planning a Text-Based Project

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 10.1: Project Planning and Design

### Learning Objectives
- Write a short requirements list.
- Design a command loop with a map of handlers.
- Plan in small steps and test each one.

### Concept Explanation

A project is easier to finish when it is planned in small steps. Write down what the program must do (*requirements*), what information it keeps (*data*), and the commands a person can give (*interface*). Build one small piece, test it, then add the next.

Text-based projects share a *command loop*: show a prompt, read a line, find the matching action, and repeat until the user quits. In Java, a `Map<String, Runnable>` holds actions: the keys are command names and the values are *lambdas*, small unnamed methods. A new command is one new entry, and an unknown command is a failed lookup that prints a helpful message.

The loop stops on `quit` and also when input ends. The example is a skeleton with two commands; typing `help`, `look`, an unknown word, and `quit` shows each path.

### Worked Example

```java
import java.util.Map;
import java.util.Scanner;

public class Lesson_10_1 {
    public static void main(String[] args) {
        Map<String, Runnable> commands = Map.of(
            "help", () -> System.out.println("Commands: help, look, quit"),
            "look", () -> System.out.println("You are in a dark cave."));

        Scanner in = new Scanner(System.in);
        System.out.println("Type a command:");
        String line = in.hasNextLine() ? in.nextLine() : null;
        while (line != null && !line.equals("quit")) {
            Runnable handler = commands.get(line);
            if (handler != null) {
                handler.run();
            } else {
                System.out.println("I don't understand that command. Type help for a list.");
            }
            System.out.println("Type a command:");
            line = in.hasNextLine() ? in.nextLine() : null;
        }
        System.out.println("Goodbye!");
    }
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
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 10.2: Building a Text-Based Adventure Game (Part 1)

### Learning Objectives
- Represent rooms and exits with a record and a map.
- Move the player by command.
- Handle impossible moves and the end of input.

### Concept Explanation

A room is a record with a description and an exits map from a direction to another room ID. The player’s current room is stored separately. The map contains five rooms: `start_room`, `tunnel`, `clearing`, `locked_door_room`, and `treasure_room`. In this first part, movement is unrestricted so you can verify that every exit points to a room that exists. Part 2 adds the key and locked-door rule.

### Worked Example

```java
import java.util.Map;
import java.util.Scanner;

public class Lesson_10_2 {
    record Room(String description, Map<String, String> exits) {}

    public static void main(String[] args) {
        Map<String, Room> rooms = Map.of(
            "start_room", new Room(
                "A dark cave. A narrow passage leads NORTH.",
                Map.of("north", "tunnel")),
            "tunnel", new Room(
                "A damp tunnel. Passages lead SOUTH and EAST.",
                Map.of("south", "start_room", "east", "clearing")),
            "clearing", new Room(
                "A quiet clearing. A small antechamber lies to the NORTH.",
                Map.of("west", "tunnel", "north", "locked_door_room")),
            "locked_door_room", new Room(
                "A small chamber with a heavy door to the NORTH.",
                Map.of("south", "clearing", "north", "treasure_room")),
            "treasure_room", new Room(
                "A glittering room full of treasure. You win!",
                Map.of("south", "locked_door_room")));

        Scanner in = new Scanner(System.in);
        String current = "start_room";
        while (true) {
            System.out.println("---");
            System.out.println(rooms.get(current).description());
            if (current.equals("treasure_room")) {
                break;
            }
            System.out.println("What do you want to do?");
            String command = (in.hasNextLine() ? in.nextLine() : "quit").strip().toLowerCase();
            String next = rooms.get(current).exits().get(command);
            if (next != null) {
                current = next;
            } else if (command.equals("quit")) {
                System.out.println("Exiting game. Goodbye!");
                break;
            } else {
                System.out.println("I don't understand that command or you can't go that way.");
            }
        }
    }
}
```

### Expected Behavior or Output

With the following lines supplied as standard input (piped input is not echoed):
```text
north
east
north
up
quit
```

The program prints:
```text
---
A dark cave. A narrow passage leads NORTH.
What do you want to do?
---
A damp tunnel. Passages lead SOUTH and EAST.
What do you want to do?
---
A quiet clearing. A small antechamber lies to the NORTH.
What do you want to do?
---
A small chamber with a heavy door to the NORTH.
What do you want to do?
I don't understand that command or you can't go that way.
---
A small chamber with a heavy door to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

With no standard input, the program treats end of input as `quit` and exits cleanly.

### Common Mistakes
1. Using a `Map` lookup result without checking for `null`, which throws `NullPointerException` for an unknown direction.
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
- [ ] I can represent rooms with a record.
- [ ] I can move the player by command.
- [ ] I can handle an impossible move.
- [ ] I treat end of input as quit.
- [ ] I can trace a game by hand.

---

## Lesson 10.3: Text Adventure, Part 2: Items and a Locked Door

### Reading References
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 10.3: Building a Text-Based Adventure Game (Part 2)

### Learning Objectives
- Keep items in rooms and in an inventory.
- Implement take and use commands.
- Block and then allow a move through a locked door.

### Concept Explanation

The completed adventure uses the same five-room graph as the Python, JavaScript, and TypeScript tracks: `start_room` leads north to `tunnel`; `tunnel` leads south to `start_room` and east to `clearing`; `clearing` leads west to `tunnel` and north to `locked_door_room`; the locked room leads south to `clearing` and north to `treasure_room`. The shiny key starts in `start_room`. The player must take it, travel to `locked_door_room`, and use it there before the north exit is allowed. Reaching `treasure_room` ends the game.

### Worked Example

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Lesson_10_3 {
    record Room(String description, Map<String, String> exits, List<String> items) {}

    public static void main(String[] args) {
        Map<String, Room> rooms = Map.of(
            "start_room", new Room("A dark cave.", Map.of("north", "tunnel"),
                new ArrayList<>(List.of("shiny key"))),
            "tunnel", new Room("A damp tunnel. Passages lead SOUTH and EAST.",
                Map.of("south", "start_room", "east", "clearing"), new ArrayList<>()),
            "clearing", new Room("A quiet clearing. A small antechamber lies to the NORTH.",
                Map.of("west", "tunnel", "north", "locked_door_room"), new ArrayList<>()),
            "locked_door_room", new Room("A small chamber with a heavy door to the NORTH.",
                Map.of("south", "clearing", "north", "treasure_room"), new ArrayList<>()),
            "treasure_room", new Room("A glittering room full of treasure. You win!",
                Map.of("south", "locked_door_room"), new ArrayList<>()));

        Scanner in = new Scanner(System.in);
        String current = "start_room";
        List<String> inventory = new ArrayList<>();
        boolean doorLocked = true;

        while (true) {
            Room room = rooms.get(current);
            System.out.println();
            System.out.println(room.description());
            if (current.equals("treasure_room")) {
                break;
            }
            if (!room.items().isEmpty()) {
                System.out.println("You see: " + String.join(", ", room.items()));
            }
            System.out.println("Your inventory: " +
                (inventory.isEmpty() ? "empty" : String.join(", ", inventory)));
            System.out.println("What do you want to do?");

            String command = (in.hasNextLine() ? in.nextLine() : "quit").strip().toLowerCase();
            if (command.equals("take shiny key") && room.items().contains("shiny key")) {
                room.items().remove("shiny key");
                inventory.add("shiny key");
                System.out.println("You picked up the shiny key.");
            } else if (command.equals("use shiny key") && current.equals("locked_door_room")
                    && inventory.contains("shiny key")) {
                doorLocked = false;
                System.out.println("You unlocked the door!");
            } else if (room.exits().containsKey(command)) {
                if (current.equals("locked_door_room") && command.equals("north") && doorLocked) {
                    System.out.println("The door is locked! You need a key.");
                } else {
                    current = room.exits().get(command);
                }
            } else if (command.equals("quit")) {
                System.out.println("You quit the adventure.");
                break;
            } else {
                System.out.println("Invalid command. Use a direction, 'take shiny key', " +
                    "'use shiny key', or 'quit'.");
            }
        }
    }
}
```

### Expected Behavior or Output

With the following lines supplied as standard input (piped input is not echoed):
```text
north
east
north
north
south
west
south
take shiny key
north
east
north
use shiny key
north
```

The program prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?

A damp tunnel. Passages lead SOUTH and EAST.
Your inventory: empty
What do you want to do?

A quiet clearing. A small antechamber lies to the NORTH.
Your inventory: empty
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?
The door is locked! You need a key.

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?

A quiet clearing. A small antechamber lies to the NORTH.
Your inventory: empty
What do you want to do?

A damp tunnel. Passages lead SOUTH and EAST.
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

A damp tunnel. Passages lead SOUTH and EAST.
Your inventory: shiny key
What do you want to do?

A quiet clearing. A small antechamber lies to the NORTH.
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

With no standard input, the program treats end of input as `quit` and exits cleanly.

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
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 10.4: Building a Command-Line To-Do List

### Learning Objectives
- Keep records with the shared fields.
- Save and load them as JSON.
- Offer add, view, mark-done, save, load, and quit commands.

### Concept Explanation

A to-do list ties together records, loops, methods, and files. Each task has the shared fields `id`, `title`, `description`, `done`, and `created_at`. The program keeps a list of tasks in memory, shows a numbered menu, and saves the list to `todos.json` when asked and on exit.

Saving uses the teaching JSON helper from Lesson 8.5, included here so the example runs on its own. At start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program: it prints a message and starts with an empty list.

New ids are one more than the highest existing id. The status is shown as the words `done` and `not done`, never with a symbol or color alone.

In the sample session the user adds two tasks, views the list, marks task 2 done, views it again, tries an invalid menu choice, views the list, and quits.

### Worked Example

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class Lesson_10_4 {
    static final class Json {
        private Json() {}

        static String encode(Object value) {
            if (value == null) {
                return "null";
            }
            if (value instanceof String text) {
                return quote(text);
            }
            if (value instanceof Boolean || value instanceof Integer || value instanceof Long || value instanceof Double) {
                return value.toString();
            }
            if (value instanceof Map<?, ?> map) {
                List<String> keys = new ArrayList<>();
                for (Object key : map.keySet()) {
                    keys.add(key.toString());
                }
                Collections.sort(keys);
                StringBuilder out = new StringBuilder("{");
                for (int i = 0; i < keys.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(quote(keys.get(i))).append(':').append(encode(map.get(keys.get(i))));
                }
                return out.append('}').toString();
            }
            if (value instanceof List<?> list) {
                StringBuilder out = new StringBuilder("[");
                for (int i = 0; i < list.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(encode(list.get(i)));
                }
                return out.append(']').toString();
            }
            throw new IllegalArgumentException("cannot encode " + value.getClass().getSimpleName());
        }

        private static String quote(String text) {
            StringBuilder out = new StringBuilder("\"");
            for (char c : text.toCharArray()) {
                switch (c) {
                    case '"' -> out.append("\\\"");
                    case '\\' -> out.append("\\\\");
                    case '\n' -> out.append("\\n");
                    case '\r' -> out.append("\\r");
                    case '\t' -> out.append("\\t");
                    default -> {
                        if (c < ' ') {
                            out.append(String.format("\\u%04x", (int) c));
                        } else {
                            out.append(c);
                        }
                    }
                }
            }
            return out.append('"').toString();
        }

        static Object decode(String text) {
            Parser parser = new Parser(text);
            Object result = parser.value();
            parser.skip();
            if (parser.pos < text.length()) {
                throw parser.fail("unexpected extra text");
            }
            return result;
        }

        private static final class Parser {
            private final String text;
            private int pos = 0;

            Parser(String text) {
                this.text = text;
            }

            IllegalArgumentException fail(String message) {
                return new IllegalArgumentException(message + " at position " + pos);
            }

            void skip() {
                while (pos < text.length() && Character.isWhitespace(text.charAt(pos))) {
                    pos++;
                }
            }

            Object value() {
                skip();
                if (pos >= text.length()) {
                    throw fail("unexpected end of text");
                }
                char c = text.charAt(pos);
                if (c == '{') return object();
                if (c == '[') return list();
                if (c == '"') return string();
                if (text.startsWith("true", pos)) { pos += 4; return Boolean.TRUE; }
                if (text.startsWith("false", pos)) { pos += 5; return Boolean.FALSE; }
                if (text.startsWith("null", pos)) { pos += 4; return null; }
                if (c == '-' || Character.isDigit(c)) return number();
                throw fail("unexpected character");
            }

            Object number() {
                int start = pos;
                if (text.charAt(pos) == '-') {
                    pos++;
                }
                while (pos < text.length() && (Character.isDigit(text.charAt(pos)) || ".eE+-".indexOf(text.charAt(pos)) >= 0)) {
                    pos++;
                }
                String token = text.substring(start, pos);
                try {
                    return Long.parseLong(token);
                } catch (NumberFormatException notWhole) {
                    try {
                        return Double.parseDouble(token);
                    } catch (NumberFormatException notNumber) {
                        throw fail("bad number");
                    }
                }
            }

            String string() {
                pos++;
                StringBuilder out = new StringBuilder();
                while (true) {
                    if (pos >= text.length()) {
                        throw fail("unterminated string");
                    }
                    char c = text.charAt(pos++);
                    if (c == '"') {
                        return out.toString();
                    }
                    if (c != '\\') {
                        out.append(c);
                        continue;
                    }
                    if (pos >= text.length()) {
                        throw fail("bad escape");
                    }
                    char e = text.charAt(pos++);
                    switch (e) {
                        case 'n' -> out.append('\n');
                        case 't' -> out.append('\t');
                        case 'r' -> out.append('\r');
                        case '"' -> out.append('"');
                        case '\\' -> out.append('\\');
                        case '/' -> out.append('/');
                        case 'u' -> {
                            if (pos + 4 > text.length()) {
                                throw fail("bad escape");
                            }
                            out.append((char) Integer.parseInt(text.substring(pos, pos + 4), 16));
                            pos += 4;
                        }
                        default -> throw fail("bad escape");
                    }
                }
            }

            Map<String, Object> object() {
                pos++;
                Map<String, Object> map = new LinkedHashMap<>();
                skip();
                if (pos < text.length() && text.charAt(pos) == '}') {
                    pos++;
                    return map;
                }
                while (true) {
                    skip();
                    if (pos >= text.length() || text.charAt(pos) != '"') {
                        throw fail("expected a key");
                    }
                    String key = string();
                    skip();
                    if (pos >= text.length() || text.charAt(pos) != ':') {
                        throw fail("expected ':'");
                    }
                    pos++;
                    map.put(key, value());
                    skip();
                    if (pos >= text.length()) {
                        throw fail("unterminated object");
                    }
                    char d = text.charAt(pos++);
                    if (d == '}') {
                        return map;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail("expected ',' or '}'");
                    }
                }
            }

            List<Object> list() {
                pos++;
                List<Object> items = new ArrayList<>();
                skip();
                if (pos < text.length() && text.charAt(pos) == ']') {
                    pos++;
                    return items;
                }
                while (true) {
                    items.add(value());
                    skip();
                    if (pos >= text.length()) {
                        throw fail("unterminated list");
                    }
                    char d = text.charAt(pos++);
                    if (d == ']') {
                        return items;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail("expected ',' or ']'");
                    }
                }
            }
        }
    }

    static final Path TODO_FILE = Path.of("todos.json");
    static List<Map<String, Object>> todos = new ArrayList<>();

    static void loadTodos() throws IOException {
        if (!Files.exists(TODO_FILE)) {
            System.out.println("No existing tasks found.");
            todos = new ArrayList<>();
            return;
        }
        try {
            List<Map<String, Object>> loaded = new ArrayList<>();
            for (Object entry : (List<?>) Json.decode(Files.readString(TODO_FILE))) {
                Map<String, Object> task = new LinkedHashMap<>();
                for (Map.Entry<?, ?> field : ((Map<?, ?>) entry).entrySet()) {
                    task.put(field.getKey().toString(), field.getValue());
                }
                loaded.add(task);
            }
            todos = loaded;
            System.out.println("Tasks loaded.");
        } catch (IllegalArgumentException | ClassCastException e) {
            System.out.println("Error: todos.json is not valid JSON. Starting with an empty list.");
            todos = new ArrayList<>();
        }
    }

    static void saveTodos() throws IOException {
        Files.writeString(TODO_FILE, Json.encode(todos));
        System.out.println("Tasks saved.");
    }

    static long nextId() {
        long highest = 0;
        for (Map<String, Object> task : todos) {
            highest = Math.max(highest, (Long) task.get("id"));
        }
        return highest + 1;
    }

    static void addTask(String title, String description) {
        if (title.isBlank()) {
            System.out.println("A title is required.");
            return;
        }
        Map<String, Object> task = new LinkedHashMap<>();
        task.put("id", nextId());
        task.put("title", title.strip());
        task.put("description", description.strip());
        task.put("done", false);
        task.put("created_at", LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss")));
        todos.add(task);
        System.out.println("Task '" + title.strip() + "' added.");
    }

    static void viewTasks() {
        if (todos.isEmpty()) {
            System.out.println("No tasks in your list.");
            return;
        }
        System.out.println("--- Your To-Do List ---");
        for (Map<String, Object> task : todos) {
            String status = Boolean.TRUE.equals(task.get("done")) ? "done" : "not done";
            System.out.println(task.get("id") + ". " + task.get("title") + " (" + status + ")");
        }
        System.out.println("-----------------------");
    }

    static void markDone(String text) {
        long id;
        try {
            id = Long.parseLong(text.trim());
        } catch (NumberFormatException e) {
            System.out.println("Please enter a whole number.");
            return;
        }
        for (Map<String, Object> task : todos) {
            if (task.get("id").equals(id)) {
                task.put("done", true);
                System.out.println("Task '" + task.get("title") + "' marked as done.");
                return;
            }
        }
        System.out.println("No task has that number.");
    }

    static void showMenu() {
        System.out.println();
        System.out.println("--- To-Do List Menu ---");
        System.out.println("1. Add Task");
        System.out.println("2. View Tasks");
        System.out.println("3. Mark Task Done");
        System.out.println("4. Save Tasks");
        System.out.println("5. Load Tasks");
        System.out.println("6. Quit");
        System.out.println("-----------------------");
    }

    static String next(Scanner in, String fallback) {
        return in.hasNextLine() ? in.nextLine() : fallback;
    }

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        loadTodos();
        while (true) {
            showMenu();
            System.out.println("Enter your choice (1-6):");
            String choice = next(in, "6");
            switch (choice) {
                case "1" -> {
                    System.out.println("Enter task title:");
                    String title = next(in, "");
                    System.out.println("Enter task description:");
                    String description = next(in, "");
                    addTask(title, description);
                }
                case "2" -> viewTasks();
                case "3" -> {
                    viewTasks();
                    System.out.println("Enter task number to mark done:");
                    markDone(next(in, ""));
                }
                case "4" -> saveTodos();
                case "5" -> loadTodos();
                case "6" -> {
                    saveTodos();
                    System.out.println("Goodbye!");
                    return;
                }
                default -> System.out.println("Invalid choice. Please try again.");
            }
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
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Dev.java learning paths](https://dev.java/learn/)
- Matching Python lesson: Lesson 10.5: Refining User Experience and Validation

### Learning Objectives
- Write reusable validation methods.
- Limit retries and handle the end of input.
- Write clear, accessible messages.

### Concept Explanation

Reusable validation methods make every menu and form consistent. `askNumber(in, prompt, low, high, attempts)` prints a prompt, reads a line, converts it, checks the range, and either returns the number or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns `null`. `askYesNo(in, prompt)` accepts `y`, `yes`, `n`, and `no` in any letter case. Returning the wrapper types `Integer` and `Boolean` lets `null` mean "no answer".

Good messages say *what was wrong* and *what to do*: "Enter a whole number from 0 to 100," not "Invalid." They never depend on color, position, or symbols alone, and they use the same wording every time.

The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y.

### Worked Example

```java
import java.util.Scanner;

public class Lesson_10_5 {
    static Integer askNumber(Scanner in, String prompt, int low, int high, int attempts) {
        for (int attempt = 1; attempt <= attempts; attempt++) {
            System.out.println(prompt);
            if (!in.hasNextLine()) {
                return null;
            }
            String text = in.nextLine().trim();
            try {
                int number = Integer.parseInt(text);
                if (number >= low && number <= high) {
                    return number;
                }
            } catch (NumberFormatException e) {
                // fall through to the message below
            }
            System.out.println("Enter a whole number from " + low + " to " + high + ". You have "
                + (attempts - attempt) + " attempt(s) left.");
        }
        return null;
    }

    static Boolean askYesNo(Scanner in, String prompt) {
        while (true) {
            System.out.println(prompt + " (yes or no)");
            if (!in.hasNextLine()) {
                return null;
            }
            String text = in.nextLine().trim().toLowerCase();
            if (text.equals("y") || text.equals("yes")) {
                return true;
            }
            if (text.equals("n") || text.equals("no")) {
                return false;
            }
            System.out.println("Please answer yes or no.");
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Integer score = askNumber(in, "Enter a score from 0 to 100:", 0, 100, 3);
        if (score != null) {
            System.out.println("Accepted score: " + score);
        } else {
            System.out.println("No valid score was entered.");
        }

        Boolean keep = askYesNo(in, "Save this score?");
        System.out.println("Save answer: " + keep);
    }
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
3. Add `askText(in, prompt)` that rejects empty answers.
4. Rewrite two messages from earlier lessons so they say what to do next.

### Accessibility Practice

Check that every error message ends with an action the user can take, and that the same situation always produces the same words.

### Skills Checklist
- [ ] I can write reusable validation methods.
- [ ] I limit retries.
- [ ] I handle the end of input.
- [ ] I write messages that say what to do.
- [ ] I keep wording consistent.

---
