# Unit 9: Collections, Data Analysis, and Testing

## Overview

This unit introduces Java's Collections Framework, basic data analysis, and unit testing with JUnit.

---

## Lesson 9.1: Java Collections Framework

### Key Interfaces and Classes

```
Collection
|--- List
|   |--- ArrayList
|   +--- LinkedList
+--- Set
    |--- HashSet
    +--- TreeSet

Map
|--- HashMap
+--- TreeMap
```

### `HashMap` --- Key-Value Storage

```java
import java.util.HashMap;
import java.util.Map;

HashMap<String, Integer> inventory = new HashMap<>();

// Add entries
inventory.put("apples", 50);
inventory.put("bananas", 30);
inventory.put("oranges", 40);

// Access
System.out.println(inventory.get("apples"));           // 50
System.out.println(inventory.getOrDefault("grapes", 0)); // 0

// Check
System.out.println(inventory.containsKey("bananas"));   // true
System.out.println(inventory.containsValue(30));         // true

// Update
inventory.put("apples", 55);

// Remove
inventory.remove("bananas");

// Iterate
for (Map.Entry<String, Integer> entry : inventory.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}

// Keys only
for (String key : inventory.keySet()) {
    System.out.println(key);
}

// Values only
for (int value : inventory.values()) {
    System.out.println(value);
}

System.out.println("Size: " + inventory.size());
```

### `HashSet` --- Unique Elements

```java
import java.util.HashSet;

HashSet<String> uniqueWords = new HashSet<>();
uniqueWords.add("apple");
uniqueWords.add("banana");
uniqueWords.add("apple");   // Duplicate --- ignored

System.out.println(uniqueWords.size());          // 2
System.out.println(uniqueWords.contains("banana")); // true
```

### `TreeMap` --- Sorted Keys

```java
import java.util.TreeMap;

TreeMap<String, Integer> sorted = new TreeMap<>();
sorted.put("banana", 2);
sorted.put("apple", 1);
sorted.put("cherry", 3);

// Iterates in alphabetical key order
for (Map.Entry<String, Integer> e : sorted.entrySet()) {
    System.out.println(e.getKey() + ": " + e.getValue());
}
```

### Sorting with Collections

```java
import java.util.*;

List<Integer> numbers = new ArrayList<>(Arrays.asList(5, 2, 9, 1, 7));
Collections.sort(numbers);
System.out.println(numbers);   // [1, 2, 5, 7, 9]

Collections.sort(numbers, Collections.reverseOrder());
System.out.println(numbers);   // [9, 7, 5, 2, 1]

int max = Collections.max(numbers);
int min = Collections.min(numbers);
```

---

## Lesson 9.2: Word Frequency Analysis

```java
import java.util.*;

public class WordFrequency {
    public static Map<String, Integer> countWords(String text) {
        Map<String, Integer> frequency = new HashMap<>();
        String[] words = text.toLowerCase()
                             .replaceAll("[^a-z\\s]", "")
                             .trim()
                             .split("\\s+");

        for (String word : words) {
            frequency.put(word, frequency.getOrDefault(word, 0) + 1);
        }
        return frequency;
    }

    public static void main(String[] args) {
        String text = "the quick brown fox jumps over the lazy dog the quick brown fox";
        Map<String, Integer> freq = countWords(text);

        // Sort by frequency (most common first)
        List<Map.Entry<String, Integer>> entries = new ArrayList<>(freq.entrySet());
        entries.sort((a, b) -> b.getValue() - a.getValue());

        System.out.println("Word Frequencies:");
        for (Map.Entry<String, Integer> entry : entries) {
            System.out.printf("'%s': %d%n", entry.getKey(), entry.getValue());
        }
    }
}
```

---

## Lesson 9.3: Working with CSV Files

```java
import java.io.*;
import java.util.*;

public class CSVReader {
    public static void main(String[] args) {
        String filename = "students.csv";

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String headerLine = reader.readLine();
            String[] headers = headerLine.split(",");
            System.out.println("Columns: " + Arrays.toString(headers));
            System.out.println("---");

            String line;
            while ((line = reader.readLine()) != null) {
                String[] data = line.split(",");
                if (data.length == headers.length) {
                    String name = data[0].trim();
                    int age = Integer.parseInt(data[1].trim());
                    String grade = data[2].trim();
                    System.out.printf("Name: %-15s Age: %3d  Grade: %s%n",
                                      name, age, grade);
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found - " + filename);
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid number format in CSV.");
        }
    }
}
```

---

## Lesson 9.4: Unit Testing with JUnit

### Adding JUnit to Your Project

If using VS Code with Maven, add to `pom.xml`:

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.0</version>
    <scope>test</scope>
</dependency>
```

### Writing Tests

```java
// MyMath.java
public class MyMath {
    public static int add(int a, int b) { return a + b; }
    public static double circleArea(double radius) { return Math.PI * radius * radius; }
    public static String getGrade(int score) {
        if (score >= 90) return "A";
        if (score >= 80) return "B";
        if (score >= 70) return "C";
        return "F";
    }
}
```

```java
// TestMyMath.java
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

public class TestMyMath {

    @Test
    public void testAddPositiveNumbers() {
        assertEquals(8, MyMath.add(5, 3));
    }

    @Test
    public void testAddNegativeNumbers() {
        assertEquals(-8, MyMath.add(-5, -3));
    }

    @Test
    public void testCircleArea() {
        double expected = Math.PI * 25;
        assertEquals(expected, MyMath.circleArea(5.0), 0.0001);
    }

    @Test
    public void testGradeA() {
        assertEquals("A", MyMath.getGrade(95));
    }

    @Test
    public void testGradeF() {
        assertEquals("F", MyMath.getGrade(55));
    }
}
```

### Common JUnit Assertions

| Method                                     | Description               |
| ------------------------------------------ | ------------------------- |
| `assertEquals(expected, actual)`           | Check equality            |
| `assertTrue(condition)`                    | Check condition is true   |
| `assertFalse(condition)`                   | Check condition is false  |
| `assertNull(object)`                       | Check object is null      |
| `assertNotNull(object)`                    | Check object is not null  |
| `assertThrows(ExceptionClass, executable)` | Check exception is thrown |

### Skills Checklist

- [ ] I can use `HashMap` for key-value storage in Java.
- [ ] I can iterate through a map's entries, keys, and values.
- [ ] I can write unit tests using JUnit 5.
- [ ] I can use common assertion methods.

---

# Unit 10: Project-Based Learning

## Overview

This unit guides students through building text-based Java applications.

---

## Lesson 10.1: Designing a Text-Based Adventure Game

### Room and Player Structure

```java
import java.util.*;

public class Room {
    private String name;
    private String description;
    private Map<String, Room> exits;
    private List<String> items;

    public Room(String name, String description) {
        this.name = name;
        this.description = description;
        this.exits = new HashMap<>();
        this.items = new ArrayList<>();
    }

    public void addExit(String direction, Room room) {
        exits.put(direction.toLowerCase(), room);
    }

    public void addItem(String item) {
        items.add(item);
    }

    public Room getExit(String direction) {
        return exits.get(direction.toLowerCase());
    }

    public String getDescription() {
        StringBuilder sb = new StringBuilder();
        sb.append("--- ").append(name).append(" ---\n");
        sb.append(description).append("\n");
        if (!items.isEmpty()) {
            sb.append("You see: ").append(String.join(", ", items)).append("\n");
        }
        sb.append("Exits: ").append(String.join(", ", exits.keySet()));
        return sb.toString();
    }

    public String getName() { return name; }
    public List<String> getItems() { return items; }
}
```

```java
import java.util.*;

public class Player {
    private String name;
    private Room currentRoom;
    private List<String> inventory;
    private int health;

    public Player(String name, Room startRoom) {
        this.name = name;
        this.currentRoom = startRoom;
        this.inventory = new ArrayList<>();
        this.health = 100;
    }

    public boolean move(String direction) {
        Room nextRoom = currentRoom.getExit(direction);
        if (nextRoom != null) {
            currentRoom = nextRoom;
            return true;
        }
        return false;
    }

    public boolean takeItem(String itemName) {
        List<String> roomItems = currentRoom.getItems();
        for (String item : roomItems) {
            if (item.equalsIgnoreCase(itemName)) {
                inventory.add(item);
                roomItems.remove(item);
                return true;
            }
        }
        return false;
    }

    public String getStatus() {
        return "Player: " + name + " | Health: " + health +
               " | Inventory: " + (inventory.isEmpty() ? "empty" : String.join(", ", inventory));
    }

    public Room getCurrentRoom() { return currentRoom; }
    public List<String> getInventory() { return inventory; }
}
```

```java
import java.util.Scanner;

public class AdventureGame {
    public static void main(String[] args) {
        // Build the world
        Room cave = new Room("Dark Cave", "You are in a dimly lit cave.");
        Room tunnel = new Room("Stone Tunnel", "A narrow tunnel leads north and south.");
        Room clearing = new Room("Sunny Clearing", "A bright clearing with tall trees.");

        cave.addExit("north", tunnel);
        cave.addItem("torch");
        tunnel.addExit("south", cave);
        tunnel.addExit("north", clearing);
        clearing.addExit("south", tunnel);

        Player player = new Player("Hero", cave);
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Text Adventure ===");
        System.out.println("Commands: go [direction], take [item], inventory, look, quit");
        System.out.println();

        while (true) {
            System.out.println(player.getCurrentRoom().getDescription());
            System.out.println(player.getStatus());
            System.out.print("\n> ");

            String input = scanner.nextLine().trim().toLowerCase();
            String[] parts = input.split("\\s+", 2);
            String command = parts[0];
            String argument = parts.length > 1 ? parts[1] : "";

            switch (command) {
                case "go":
                    if (argument.isEmpty()) {
                        System.out.println("Go where?");
                    } else if (!player.move(argument)) {
                        System.out.println("You can't go that way.");
                    }
                    break;
                case "take":
                    if (player.takeItem(argument)) {
                        System.out.println("You picked up the " + argument + ".");
                    } else {
                        System.out.println("There's no " + argument + " here.");
                    }
                    break;
                case "inventory":
                    System.out.println("Inventory: " + player.getInventory());
                    break;
                case "look":
                    // Room description already shown at top of loop
                    break;
                case "quit":
                    System.out.println("Thanks for playing!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Unknown command: " + command);
            }
            System.out.println();
        }
    }
}
```

---

## Lesson 10.2: Command-Line To-Do Manager

```java
import java.util.*;
import java.io.*;
import com.google.gson.*;   // Add Gson library for JSON support

public class TodoManager {
    private List<Map<String, Object>> todos = new ArrayList<>();
    private final String FILE_PATH = "todos.json";

    public void addTask(String description) {
        Map<String, Object> task = new HashMap<>();
        task.put("description", description);
        task.put("completed", false);
        todos.add(task);
        System.out.println("Task added: " + description);
    }

    public void viewTasks() {
        if (todos.isEmpty()) {
            System.out.println("No tasks in your list.");
            return;
        }
        System.out.println("--- Your To-Do List ---");
        for (int i = 0; i < todos.size(); i++) {
            Map<String, Object> task = todos.get(i);
            String status = (Boolean) task.get("completed") ? "[X]" : "[ ]";
            System.out.printf("%d. %s %s%n", i + 1, status, task.get("description"));
        }
        System.out.println("-----------------------");
    }

    public void markComplete(int taskNumber) {
        int index = taskNumber - 1;
        if (index >= 0 && index < todos.size()) {
            todos.get(index).put("completed", true);
            System.out.println("Task marked complete: " + todos.get(index).get("description"));
        } else {
            System.out.println("Invalid task number.");
        }
    }

    public static void main(String[] args) {
        TodoManager manager = new TodoManager();
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== To-Do Manager ===");

        while (true) {
            System.out.println("\n1. Add Task  2. View Tasks  3. Mark Complete  4. Quit");
            System.out.print("Choice: ");
            String choice = scanner.nextLine().trim();

            switch (choice) {
                case "1":
                    System.out.print("Task description: ");
                    manager.addTask(scanner.nextLine());
                    break;
                case "2":
                    manager.viewTasks();
                    break;
                case "3":
                    manager.viewTasks();
                    System.out.print("Task number: ");
                    try {
                        manager.markComplete(Integer.parseInt(scanner.nextLine()));
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid input.");
                    }
                    break;
                case "4":
                    System.out.println("Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}
```

---

# Unit 11: Capstone Project --- Personal Data Manager in Java

## Overview

Students build a fully functional command-line personal data manager in Java.

## Project Options

- **Contact Manager:** name, phone, email, notes
- **Book Tracker:** title, author, genre, read status
- **Inventory System:** item name, quantity, location, notes
- **To-Do App:** description, due date, priority, status

## Required Features

1. **Add item** --- prompt for all attributes and save to list.
2. **View all items** --- display all stored items clearly.
3. **Edit item** --- select by number/name and modify.
4. **Delete item** --- remove selected item.
5. **Search/filter** --- find items by keyword.
6. **Persistence** --- save/load to a JSON or CSV file.

## Architecture Recommendations

```
src/
|--- model/
|   +--- Contact.java        (data model class)
|--- storage/
|   +--- DataManager.java    (file I/O)
|--- ui/
|   +--- ConsoleUI.java      (user interface)
+--- Main.java               (entry point)
```

## Assessment Criteria

### Functionality (60%)

- [ ] Add, view, edit, and delete items work correctly.
- [ ] Data persists between program runs.
- [ ] Program handles invalid input without crashing.

### Code Quality (20%)

- [ ] Methods are small and have a single responsibility.
- [ ] Classes follow OOP principles (encapsulation).
- [ ] Meaningful names for all variables, methods, and classes.
- [ ] Appropriate comments and Javadoc.

### Accessibility & UX (15%)

- [ ] Clear, descriptive prompts for all input.
- [ ] Explicit confirmation messages after every action.
- [ ] Consistent output format.
- [ ] Informative error messages.

### Documentation (5%)

- [ ] `README.md` with setup and usage instructions.
- [ ] Reflection on challenges and solutions.
