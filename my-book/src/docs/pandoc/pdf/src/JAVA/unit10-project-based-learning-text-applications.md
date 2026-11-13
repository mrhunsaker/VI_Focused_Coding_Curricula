[Header 2 ("unit-10-project-based-learning--text-applications", [], []) [Str "Unit 10: Project-Based Learning — Text Applications"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops project-based learning — text applications through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing."], Para [Strong [Str "Unit objectives:"], Str " explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects."], Header 3 ("lesson-101-planning-a-text-based-project", ["unnumbered", "unlisted"], []) [Str "Lesson 10.1: Planning a Text-Based Project"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 10.1: Project Planning and Design"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write a short requirements list."]], [Plain [Str "Design a command loop with a map of handlers."]], [Plain [Str "Plan in small steps and test each one."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A project is easier to finish when it is planned in small steps. Write down what the program must do (", Emph [Str "requirements"], Str "), what information it keeps (", Emph [Str "data"], Str "), and the commands a person can give (", Emph [Str "interface"], Str "). Build one small piece, test it, then add the next."], Para [Str "Text-based projects share a ", Emph [Str "command loop"], Str ": show a prompt, read a line, find the matching action, and repeat until the user quits. In Java, a ", Code ("", [], []) "Map<String, Runnable>", Str " holds actions: the keys are command names and the values are ", Emph [Str "lambdas"], Str ", small unnamed methods. A new command is one new entry, and an unknown command is a failed lookup that prints a helpful message."], Para [Str "The loop stops on ", Code ("", [], []) "quit", Str " and also when input ends. The example is a skeleton with two commands; typing ", Code ("", [], []) "help", Str ", ", Code ("", [], []) "look", Str ", an unknown word, and ", Code ("", [], []) "quit", Str " shows each path."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.Map;
import java.util.Scanner;

public class Lesson_10_1 {
    public static void main(String[] args) {
        Map<String, Runnable> commands = Map.of(
            \"help\", () -> System.out.println(\"Commands: help, look, quit\"),
            \"look\", () -> System.out.println(\"You are in a dark cave.\"));

        Scanner in = new Scanner(System.in);
        System.out.println(\"Type a command:\");
        String line = in.hasNextLine() ? in.nextLine() : null;
        while (line != null && !line.equals(\"quit\")) {
            Runnable handler = commands.get(line);
            if (handler != null) {
                handler.run();
            } else {
                System.out.println(\"I don't understand that command. Type help for a list.\");
            }
            System.out.println(\"Type a command:\");
            line = in.hasNextLine() ? in.nextLine() : null;
        }
        System.out.println(\"Goodbye!\");
    }
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
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Starting to code before listing the requirements."]], [Plain [Str "Using a long chain of ", Code ("", [], []) "if", Str " statements instead of a map of handlers."]], [Plain [Str "Forgetting that an unknown command should say what to do next."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Write five requirements for the text adventure and the to-do list."]], [Plain [Str "Add a ", Code ("", [], []) "score", Str " command that prints the shared scores."]], [Plain [Str "Add the aliases ", Code ("", [], []) "h", Str " and ", Code ("", [], []) "l", Str " without copying the lambdas."]], [Plain [Str "Describe the data for the capstone in three sentences."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Prompts and responses are on separate lines and every response is a complete sentence. Test the prompts by listening to them before you add features."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can list requirements."]], [Plain [Str "\9744", Space, Str "I can design a command loop."]], [Plain [Str "\9744", Space, Str "I can use a map of lambdas."]], [Plain [Str "\9744", Space, Str "I handle unknown commands."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]]], HorizontalRule, Header 3 ("lesson-102-text-adventure-part-1-rooms-and-movement", ["unnumbered", "unlisted"], []) [Str "Lesson 10.2: Text Adventure, Part 1: Rooms and Movement"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 10.2: Building a Text-Based Adventure Game (Part 1)"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Represent rooms and exits with a record and a map."]], [Plain [Str "Move the player by command."]], [Plain [Str "Handle impossible moves and the end of input."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A room is a record with a description and an exits map from a direction to another room ID. The player’s current room is stored separately. The map contains five rooms: ", Code ("", [], []) "start_room", Str ", ", Code ("", [], []) "tunnel", Str ", ", Code ("", [], []) "clearing", Str ", ", Code ("", [], []) "locked_door_room", Str ", and ", Code ("", [], []) "treasure_room", Str ". In this first part, movement is unrestricted so you can verify that every exit points to a room that exists. Part 2 adds the key and locked-door rule."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.Map;
import java.util.Scanner;

public class Lesson_10_2 {
    record Room(String description, Map<String, String> exits) {}

    public static void main(String[] args) {
        Map<String, Room> rooms = Map.of(
            \"start_room\", new Room(
                \"A dark cave. A narrow passage leads NORTH.\",
                Map.of(\"north\", \"tunnel\")),
            \"tunnel\", new Room(
                \"A damp tunnel. Passages lead SOUTH and EAST.\",
                Map.of(\"south\", \"start_room\", \"east\", \"clearing\")),
            \"clearing\", new Room(
                \"A quiet clearing. A small antechamber lies to the NORTH.\",
                Map.of(\"west\", \"tunnel\", \"north\", \"locked_door_room\")),
            \"locked_door_room\", new Room(
                \"A small chamber with a heavy door to the NORTH.\",
                Map.of(\"south\", \"clearing\")),
            \"treasure_room\", new Room(
                \"A glittering room full of treasure. You win!\",
                Map.of(\"south\", \"locked_door_room\")));

        Scanner in = new Scanner(System.in);
        String current = \"start_room\";
        while (true) {
            System.out.println(\"---\");
            System.out.println(rooms.get(current).description());
            if (current.equals(\"treasure_room\")) {
                break;
            }
            System.out.println(\"What do you want to do?\");
            String command = (in.hasNextLine() ? in.nextLine() : \"quit\").strip().toLowerCase();
            String next = rooms.get(current).exits().get(command);
            if (next != null) {
                current = next;
            } else if (command.equals(\"quit\")) {
                System.out.println(\"Exiting game. Goodbye!\");
                break;
            } else {
                System.out.println(\"I don't understand that command or you can't go that way.\");
            }
        }
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines supplied as standard input (piped input is not echoed):"], CodeBlock ("", ["text"], []) "north
east
north
north
quit
", Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "---
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
", Para [Str "With no standard input, the program treats end of input as ", Code ("", [], []) "quit", Str " and exits cleanly."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using a ", Code ("", [], []) "Map", Str " lookup result without checking for ", Code ("", [], []) "null", Str ", which throws ", Code ("", [], []) "NullPointerException", Str " for an unknown direction."]], [Plain [Str "Forgetting to treat the end of input as ", Code ("", [], []) "quit", Str ", so the program loops forever when input is piped in."]], [Plain [Str "Misspelling a room name in ", Code ("", [], []) "exits", Str ", so a move leads to a room that does not exist."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace the six commands by hand and write the room after each one."]], [Plain [Str "Add a fourth room reached from the clearing and test it."]], [Plain [Str "Add the aliases ", Code ("", [], []) "n", Str ", ", Code ("", [], []) "s", Str ", ", Code ("", [], []) "e", Str ", and ", Code ("", [], []) "w", Str "."]], [Plain [Str "Write a loop that checks that every exit names a real room."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each turn prints a separator line, the description, and the prompt, so a whole turn can be read in order. Listen to one turn from start to finish to confirm that a player could follow it without seeing the screen."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can represent rooms with a record."]], [Plain [Str "\9744", Space, Str "I can move the player by command."]], [Plain [Str "\9744", Space, Str "I can handle an impossible move."]], [Plain [Str "\9744", Space, Str "I treat end of input as quit."]], [Plain [Str "\9744", Space, Str "I can trace a game by hand."]]], HorizontalRule, Header 3 ("lesson-103-text-adventure-part-2-items-and-a-locked-door", ["unnumbered", "unlisted"], []) [Str "Lesson 10.3: Text Adventure, Part 2: Items and a Locked Door"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 10.3: Building a Text-Based Adventure Game (Part 2)"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Keep items in rooms and in an inventory."]], [Plain [Str "Implement take and use commands."]], [Plain [Str "Block and then allow a move through a locked door."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The completed adventure uses the same five-room graph as the Python, JavaScript, and TypeScript tracks: ", Code ("", [], []) "start_room", Str " leads north to ", Code ("", [], []) "tunnel", Str "; ", Code ("", [], []) "tunnel", Str " leads south to ", Code ("", [], []) "start_room", Str " and east to ", Code ("", [], []) "clearing", Str "; ", Code ("", [], []) "clearing", Str " leads west to ", Code ("", [], []) "tunnel", Str " and north to ", Code ("", [], []) "locked_door_room", Str "; the locked room leads south to ", Code ("", [], []) "clearing", Str " and north to ", Code ("", [], []) "treasure_room", Str ". The shiny key starts in ", Code ("", [], []) "start_room", Str ". The player must take it, travel to ", Code ("", [], []) "locked_door_room", Str ", and use it there before the north exit is allowed. Reaching ", Code ("", [], []) "treasure_room", Str " ends the game."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Lesson_10_3 {
    record Room(String description, Map<String, String> exits, List<String> items) {}

    public static void main(String[] args) {
        Map<String, Room> rooms = Map.of(
            \"start_room\", new Room(\"A dark cave.\", Map.of(\"north\", \"tunnel\"),
                new ArrayList<>(List.of(\"shiny key\"))),
            \"tunnel\", new Room(\"A damp tunnel. Passages lead SOUTH and EAST.\",
                Map.of(\"south\", \"start_room\", \"east\", \"clearing\"), new ArrayList<>()),
            \"clearing\", new Room(\"A quiet clearing. A small antechamber lies to the NORTH.\",
                Map.of(\"west\", \"tunnel\", \"north\", \"locked_door_room\"), new ArrayList<>()),
            \"locked_door_room\", new Room(\"A small chamber with a heavy door to the NORTH.\",
                Map.of(\"south\", \"clearing\", \"north\", \"treasure_room\"), new ArrayList<>()),
            \"treasure_room\", new Room(\"A glittering room full of treasure. You win!\",
                Map.of(\"south\", \"locked_door_room\"), new ArrayList<>()));

        Scanner in = new Scanner(System.in);
        String current = \"start_room\";
        List<String> inventory = new ArrayList<>();
        boolean doorLocked = true;

        while (true) {
            Room room = rooms.get(current);
            System.out.println();
            System.out.println(room.description());
            if (current.equals(\"treasure_room\")) {
                break;
            }
            if (!room.items().isEmpty()) {
                System.out.println(\"You see: \" + String.join(\", \", room.items()));
            }
            System.out.println(\"Your inventory: \" +
                (inventory.isEmpty() ? \"empty\" : String.join(\", \", inventory)));
            System.out.println(\"What do you want to do?\");

            String command = (in.hasNextLine() ? in.nextLine() : \"quit\").strip().toLowerCase();
            if (command.equals(\"take shiny key\") && room.items().contains(\"shiny key\")) {
                room.items().remove(\"shiny key\");
                inventory.add(\"shiny key\");
                System.out.println(\"You picked up the shiny key.\");
            } else if (command.equals(\"use shiny key\") && current.equals(\"locked_door_room\")
                    && inventory.contains(\"shiny key\")) {
                doorLocked = false;
                System.out.println(\"You unlocked the door!\");
            } else if (room.exits().containsKey(command)) {
                if (current.equals(\"locked_door_room\") && command.equals(\"north\") && doorLocked) {
                    System.out.println(\"The door is locked! You need a key.\");
                } else {
                    current = room.exits().get(command);
                }
            } else if (command.equals(\"quit\")) {
                System.out.println(\"You quit the adventure.\");
                break;
            } else {
                System.out.println(\"Invalid command. Use a direction, 'take shiny key', \" +
                    \"'use shiny key', or 'quit'.\");
            }
        }
    }
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines supplied as standard input (piped input is not echoed):"], CodeBlock ("", ["text"], []) "north
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
", Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "
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
", Para [Str "With no standard input, the program treats end of input as ", Code ("", [], []) "quit", Str " and exits cleanly."], Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Making the door's locked state part of the exits so that the \"locked\" message can never be reached."]], [Plain [Str "Defining an exit to a room that is missing from the ", Code ("", [], []) "rooms", Str " map, which crashes when the player arrives."]], [Plain [Str "Printing a fixed room description that still mentions an item after the player has taken it."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Play the program with the shown commands and follow each turn on paper."]], [Plain [Str "Try ", Code ("", [], []) "use shiny key", Str " in the cave and describe what happens."]], [Plain [Str "Add a second item and require both to open the door."]], [Plain [Str "List the game's state (location, inventory, door) and say which command changes each part."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "The room description never mentions the key. A separate 'You see:' line lists items, so the description stays true after the key is taken and the screen reader announces the current state."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can store items in rooms and an inventory."]], [Plain [Str "\9744", Space, Str "I can implement take and use commands."]], [Plain [Str "\9744", Space, Str "I can block and allow a move."]], [Plain [Str "\9744", Space, Str "I can list the game's state."]], [Plain [Str "\9744", Space, Str "I can keep descriptions true after state changes."]]], HorizontalRule, Header 3 ("lesson-104-command-line-to-do-list", ["unnumbered", "unlisted"], []) [Str "Lesson 10.4: Command-Line To-Do List"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 10.4: Building a Command-Line To-Do List"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Keep records with the shared fields."]], [Plain [Str "Save and load them as JSON."]], [Plain [Str "Offer add, view, mark-done, save, load, and quit commands."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A to-do list ties together records, loops, methods, and files. Each task has the shared fields ", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "done", Str ", and ", Code ("", [], []) "created_at", Str ". The program keeps a list of tasks in memory, shows a numbered menu, and saves the list to ", Code ("", [], []) "todos.json", Str " when asked and on exit."], Para [Str "Saving uses the teaching JSON helper from Lesson 8.5, included here so the example runs on its own. At start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program: it prints a message and starts with an empty list."], Para [Str "New ids are one more than the highest existing id. The status is shown as the words ", Code ("", [], []) "done", Str " and ", Code ("", [], []) "not done", Str ", never with a symbol or color alone."], Para [Str "In the sample session the user adds two tasks, views the list, marks task 2 done, views it again, tries an invalid menu choice, views the list, and quits."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.io.IOException;
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
                return \"null\";
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
                StringBuilder out = new StringBuilder(\"{\");
                for (int i = 0; i < keys.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(quote(keys.get(i))).append(':').append(encode(map.get(keys.get(i))));
                }
                return out.append('}').toString();
            }
            if (value instanceof List<?> list) {
                StringBuilder out = new StringBuilder(\"[\");
                for (int i = 0; i < list.size(); i++) {
                    if (i > 0) {
                        out.append(',');
                    }
                    out.append(encode(list.get(i)));
                }
                return out.append(']').toString();
            }
            throw new IllegalArgumentException(\"cannot encode \" + value.getClass().getSimpleName());
        }

        private static String quote(String text) {
            StringBuilder out = new StringBuilder(\"\\\"\");
            for (char c : text.toCharArray()) {
                switch (c) {
                    case '\"' -> out.append(\"\\\\\\\"\");
                    case '\\\\' -> out.append(\"\\\\\\\\\");
                    case '\\n' -> out.append(\"\\\\n\");
                    case '\\r' -> out.append(\"\\\\r\");
                    case '\\t' -> out.append(\"\\\\t\");
                    default -> {
                        if (c < ' ') {
                            out.append(String.format(\"\\\\u%04x\", (int) c));
                        } else {
                            out.append(c);
                        }
                    }
                }
            }
            return out.append('\"').toString();
        }

        static Object decode(String text) {
            Parser parser = new Parser(text);
            Object result = parser.value();
            parser.skip();
            if (parser.pos < text.length()) {
                throw parser.fail(\"unexpected extra text\");
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
                return new IllegalArgumentException(message + \" at position \" + pos);
            }

            void skip() {
                while (pos < text.length() && Character.isWhitespace(text.charAt(pos))) {
                    pos++;
                }
            }

            Object value() {
                skip();
                if (pos >= text.length()) {
                    throw fail(\"unexpected end of text\");
                }
                char c = text.charAt(pos);
                if (c == '{') return object();
                if (c == '[') return list();
                if (c == '\"') return string();
                if (text.startsWith(\"true\", pos)) { pos += 4; return Boolean.TRUE; }
                if (text.startsWith(\"false\", pos)) { pos += 5; return Boolean.FALSE; }
                if (text.startsWith(\"null\", pos)) { pos += 4; return null; }
                if (c == '-' || Character.isDigit(c)) return number();
                throw fail(\"unexpected character\");
            }

            Object number() {
                int start = pos;
                if (text.charAt(pos) == '-') {
                    pos++;
                }
                while (pos < text.length() && (Character.isDigit(text.charAt(pos)) || \".eE+-\".indexOf(text.charAt(pos)) >= 0)) {
                    pos++;
                }
                String token = text.substring(start, pos);
                try {
                    return Long.parseLong(token);
                } catch (NumberFormatException notWhole) {
                    try {
                        return Double.parseDouble(token);
                    } catch (NumberFormatException notNumber) {
                        throw fail(\"bad number\");
                    }
                }
            }

            String string() {
                pos++;
                StringBuilder out = new StringBuilder();
                while (true) {
                    if (pos >= text.length()) {
                        throw fail(\"unterminated string\");
                    }
                    char c = text.charAt(pos++);
                    if (c == '\"') {
                        return out.toString();
                    }
                    if (c != '\\\\') {
                        out.append(c);
                        continue;
                    }
                    if (pos >= text.length()) {
                        throw fail(\"bad escape\");
                    }
                    char e = text.charAt(pos++);
                    switch (e) {
                        case 'n' -> out.append('\\n');
                        case 't' -> out.append('\\t');
                        case 'r' -> out.append('\\r');
                        case '\"' -> out.append('\"');
                        case '\\\\' -> out.append('\\\\');
                        case '/' -> out.append('/');
                        case 'u' -> {
                            if (pos + 4 > text.length()) {
                                throw fail(\"bad escape\");
                            }
                            out.append((char) Integer.parseInt(text.substring(pos, pos + 4), 16));
                            pos += 4;
                        }
                        default -> throw fail(\"bad escape\");
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
                    if (pos >= text.length() || text.charAt(pos) != '\"') {
                        throw fail(\"expected a key\");
                    }
                    String key = string();
                    skip();
                    if (pos >= text.length() || text.charAt(pos) != ':') {
                        throw fail(\"expected ':'\");
                    }
                    pos++;
                    map.put(key, value());
                    skip();
                    if (pos >= text.length()) {
                        throw fail(\"unterminated object\");
                    }
                    char d = text.charAt(pos++);
                    if (d == '}') {
                        return map;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail(\"expected ',' or '}'\");
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
                        throw fail(\"unterminated list\");
                    }
                    char d = text.charAt(pos++);
                    if (d == ']') {
                        return items;
                    }
                    if (d != ',') {
                        pos--;
                        throw fail(\"expected ',' or ']'\");
                    }
                }
            }
        }
    }

    static final Path TODO_FILE = Path.of(\"todos.json\");
    static List<Map<String, Object>> todos = new ArrayList<>();

    static void loadTodos() throws IOException {
        if (!Files.exists(TODO_FILE)) {
            System.out.println(\"No existing tasks found.\");
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
            System.out.println(\"Tasks loaded.\");
        } catch (IllegalArgumentException | ClassCastException e) {
            System.out.println(\"Error: todos.json is not valid JSON. Starting with an empty list.\");
            todos = new ArrayList<>();
        }
    }

    static void saveTodos() throws IOException {
        Files.writeString(TODO_FILE, Json.encode(todos));
        System.out.println(\"Tasks saved.\");
    }

    static long nextId() {
        long highest = 0;
        for (Map<String, Object> task : todos) {
            highest = Math.max(highest, (Long) task.get(\"id\"));
        }
        return highest + 1;
    }

    static void addTask(String title, String description) {
        if (title.isBlank()) {
            System.out.println(\"A title is required.\");
            return;
        }
        Map<String, Object> task = new LinkedHashMap<>();
        task.put(\"id\", nextId());
        task.put(\"title\", title.strip());
        task.put(\"description\", description.strip());
        task.put(\"done\", false);
        task.put(\"created_at\", LocalDateTime.now().format(DateTimeFormatter.ofPattern(\"yyyy-MM-dd'T'HH:mm:ss\")));
        todos.add(task);
        System.out.println(\"Task '\" + title.strip() + \"' added.\");
    }

    static void viewTasks() {
        if (todos.isEmpty()) {
            System.out.println(\"No tasks in your list.\");
            return;
        }
        System.out.println(\"--- Your To-Do List ---\");
        for (Map<String, Object> task : todos) {
            String status = Boolean.TRUE.equals(task.get(\"done\")) ? \"done\" : \"not done\";
            System.out.println(task.get(\"id\") + \". \" + task.get(\"title\") + \" (\" + status + \")\");
        }
        System.out.println(\"-----------------------\");
    }

    static void markDone(String text) {
        long id;
        try {
            id = Long.parseLong(text.trim());
        } catch (NumberFormatException e) {
            System.out.println(\"Please enter a whole number.\");
            return;
        }
        for (Map<String, Object> task : todos) {
            if (task.get(\"id\").equals(id)) {
                task.put(\"done\", true);
                System.out.println(\"Task '\" + task.get(\"title\") + \"' marked as done.\");
                return;
            }
        }
        System.out.println(\"No task has that number.\");
    }

    static void showMenu() {
        System.out.println();
        System.out.println(\"--- To-Do List Menu ---\");
        System.out.println(\"1. Add Task\");
        System.out.println(\"2. View Tasks\");
        System.out.println(\"3. Mark Task Done\");
        System.out.println(\"4. Save Tasks\");
        System.out.println(\"5. Load Tasks\");
        System.out.println(\"6. Quit\");
        System.out.println(\"-----------------------\");
    }

    static String next(Scanner in, String fallback) {
        return in.hasNextLine() ? in.nextLine() : fallback;
    }

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        loadTodos();
        while (true) {
            showMenu();
            System.out.println(\"Enter your choice (1-6):\");
            String choice = next(in, \"6\");
            switch (choice) {
                case \"1\" -> {
                    System.out.println(\"Enter task title:\");
                    String title = next(in, \"\");
                    System.out.println(\"Enter task description:\");
                    String description = next(in, \"\");
                    addTask(title, description);
                }
                case \"2\" -> viewTasks();
                case \"3\" -> {
                    viewTasks();
                    System.out.println(\"Enter task number to mark done:\");
                    markDone(next(in, \"\"));
                }
                case \"4\" -> saveTodos();
                case \"5\" -> loadTodos();
                case \"6\" -> {
                    saveTodos();
                    System.out.println(\"Goodbye!\");
                    return;
                }
                default -> System.out.println(\"Invalid choice. Please try again.\");
            }
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
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Saving the file but never loading it, so tasks disappear between runs."]], [Plain [Str "Reusing a deleted task's id, which can confuse saved references."]], [Plain [Str "Letting a damaged ", Code ("", [], []) "todos.json", Str " crash the program instead of printing a message."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the sample session, then run the program again typing ", Code ("", [], []) "2", Str " and ", Code ("", [], []) "6", Str " to see the saved tasks."]], [Plain [Str "Add a command to delete a task by number."]], [Plain [Str "Open ", Code ("", [], []) "todos.json", Str " and read the saved text. Edit it to remove a bracket and run the program again."]], [Plain [Str "Show each task's description in the view command."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Every menu is printed as numbered lines and every prompt is on its own line. The status words are ", Code ("", [], []) "done", Str " and ", Code ("", [], []) "not done", Str ", not symbols, so the list reads clearly in speech and braille."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can keep records with the shared fields."]], [Plain [Str "\9744", Space, Str "I can save and load JSON."]], [Plain [Str "\9744", Space, Str "I handle a missing or damaged file."]], [Plain [Str "\9744", Space, Str "I keep ids unique."]], [Plain [Str "\9744", Space, Str "I show status in words."]]], HorizontalRule, Header 3 ("lesson-105-user-experience-and-input-validation", ["unnumbered", "unlisted"], []) [Str "Lesson 10.5: User Experience and Input Validation"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 10.5: Refining User Experience and Validation"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write reusable validation methods."]], [Plain [Str "Limit retries and handle the end of input."]], [Plain [Str "Write clear, accessible messages."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Reusable validation methods make every menu and form consistent. ", Code ("", [], []) "askNumber(in, prompt, low, high, attempts)", Str " prints a prompt, reads a line, converts it, checks the range, and either returns the number or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns ", Code ("", [], []) "null", Str ". ", Code ("", [], []) "askYesNo(in, prompt)", Str " accepts ", Code ("", [], []) "y", Str ", ", Code ("", [], []) "yes", Str ", ", Code ("", [], []) "n", Str ", and ", Code ("", [], []) "no", Str " in any letter case. Returning the wrapper types ", Code ("", [], []) "Integer", Str " and ", Code ("", [], []) "Boolean", Str " lets ", Code ("", [], []) "null", Str " mean \"no answer\"."], Para [Str "Good messages say ", Emph [Str "what was wrong"], Str " and ", Emph [Str "what to do"], Str ": \"Enter a whole number from 0 to 100,\" not \"Invalid.\" They never depend on color, position, or symbols alone, and they use the same wording every time."], Para [Str "The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.Scanner;

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
            System.out.println(\"Enter a whole number from \" + low + \" to \" + high + \". You have \"
                + (attempts - attempt) + \" attempt(s) left.\");
        }
        return null;
    }

    static Boolean askYesNo(Scanner in, String prompt) {
        while (true) {
            System.out.println(prompt + \" (yes or no)\");
            if (!in.hasNextLine()) {
                return null;
            }
            String text = in.nextLine().trim().toLowerCase();
            if (text.equals(\"y\") || text.equals(\"yes\")) {
                return true;
            }
            if (text.equals(\"n\") || text.equals(\"no\")) {
                return false;
            }
            System.out.println(\"Please answer yes or no.\");
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Integer score = askNumber(in, \"Enter a score from 0 to 100:\", 0, 100, 3);
        if (score != null) {
            System.out.println(\"Accepted score: \" + score);
        } else {
            System.out.println(\"No valid score was entered.\");
        }

        Boolean keep = askYesNo(in, \"Save this score?\");
        System.out.println(\"Save answer: \" + keep);
    }
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
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing the message \"Invalid\" without saying what is valid."]], [Plain [Str "Accepting a decimal such as 88.5 for a field that requires a whole number."]], [Plain [Str "Looping forever on bad input instead of limiting attempts."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the sample input and read each message aloud."]], [Plain [Str "Run with three invalid numbers and read the final message."]], [Plain [Str "Add ", Code ("", [], []) "askText(in, prompt)", Str " that rejects empty answers."]], [Plain [Str "Rewrite two messages from earlier lessons so they say what to do next."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Check that every error message ends with an action the user can take, and that the same situation always produces the same words."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write reusable validation methods."]], [Plain [Str "\9744", Space, Str "I limit retries."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]], [Plain [Str "\9744", Space, Str "I write messages that say what to do."]], [Plain [Str "\9744", Space, Str "I keep wording consistent."]]], HorizontalRule]