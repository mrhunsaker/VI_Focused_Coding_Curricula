# Unit 10: Project-Based Learning

## Overview

This unit covers requirements, top-down design, text adventure, command-line to-do manager, accessible validation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 10.1: Requirements and design

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Project work starts with observable requirements and acceptance criteria. Separate domain state, command parsing, validation, persistence, and output so each behavior can be tested and navigated accessibly.
### Worked Example
```cs
string[] requirements = { "create records", "list records", "search by ID", "update records", "delete records", "validate input", "save and load JSON" };
foreach (string requirement in requirements) Console.WriteLine($"Requirement: {requirement}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Requirement: create records
Requirement: list records
Requirement: search by ID
Requirement: update records
Requirement: delete records
Requirement: validate input
Requirement: save and load JSON
```

### Common Mistakes
- Implementing before defining observable requirements and acceptance tests.
- Combining parsing, domain logic, persistence, and output into one untestable block.
- Providing errors or status that depend on color or visual layout alone.
### Activities
1. Write an acceptance criterion for the behavior demonstrated by the example.
2. Add one valid command and one invalid command or state transition.
3. Separate one responsibility into a method or model and test it independently.
4. Review prompts and output using keyboard navigation and assistive technology.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define observable project requirements.
- [ ] I can implement and test a valid state transition or command.
- [ ] I can handle invalid input with actionable feedback.
- [ ] I can separate domain logic from interaction.
- [ ] I can assess keyboard and screen-reader usability.

## Lesson 10.2: Text adventure: five rooms and movement

### Reading References
- [C# collections](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/collections)
- [.NET Dictionary documentation](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2)
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Represent all five canonical rooms with C# objects and dictionaries.
- Validate movement before changing the current room.
- Explain why the treasure room is not reachable until the key puzzle is implemented.

### Concept Explanation

The shared graph has five rooms: start_room, tunnel, clearing, locked_door_room, and treasure_room. A Room object stores a description and a dictionary of exits. The player begins in start_room. The north exit from locked_door_room is not available in Part 1. Use TryGetValue to handle missing directions without changing state.

### Worked Example

```csharp
using System;
using System.Collections.Generic;

var rooms = new Dictionary<string, Room>
{
    ["start_room"] = new("A dimly lit cave. A narrow passage leads north.", new() { ["north"] = "tunnel" }),
    ["tunnel"] = new("A damp tunnel. Passages lead south and east.", new() { ["south"] = "start_room", ["east"] = "clearing" }),
    ["clearing"] = new("A quiet clearing. An antechamber lies to the north.", new() { ["west"] = "tunnel", ["north"] = "locked_door_room" }),
    ["locked_door_room"] = new("A chamber with a heavy door to the north.", new() { ["south"] = "clearing" }),
    ["treasure_room"] = new("You found the treasure. You win!", new())
};

var current = "start_room";
while (true)
{
    Console.WriteLine("---");
    Console.WriteLine(rooms[current].Description);
    Console.WriteLine("What do you want to do?");
    var command = (Console.ReadLine() ?? "quit").Trim().ToLowerInvariant();
    if (command == "quit")
    {
        Console.WriteLine("Exiting game. Goodbye!");
        break;
    }
    if (rooms[current].Exits.TryGetValue(command, out var destination))
        current = destination;
    else
        Console.WriteLine("You cannot go that way. Enter a listed direction or quit.");
}

record Room(string Description, Dictionary<string, string> Exits);
```

### Expected Behavior or Output

Enter north, east, north, north, quit. The player reaches tunnel, clearing, and locked_door_room. The second north is rejected and the current room does not change. The treasure room exists but has no incoming exit in Part 1.

### Common Mistakes
- Using the dictionary indexer for a direction that may not exist.
- Updating current before validating the requested exit.
- Defining a destination that is not one of the five room identifiers.
- Adding the treasure exit before implementing the key puzzle.

### Activities
1. Trace north, east, north, north and record the current room.
2. Try west from start_room and verify that the room does not change.
3. Check every exit destination against the room dictionary.
4. Explain why treasure_room cannot yet be reached.

### Accessibility Practice

Announce the room description and prompt in a consistent order. The invalid-movement response explains what happened and how to continue. Run from the terminal and inspect output sequentially with the learner's access technology.

### Skills Checklist
- [ ] I can model all five canonical rooms.
- [ ] I can represent exits with a dictionary.
- [ ] I can reject invalid movement without changing state.
- [ ] I can explain why the treasure room is not yet reachable.

---

## Lesson 10.3: Text adventure: shiny key and locked door

### Reading References
- [C# collections](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/collections)
- [.NET List documentation](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1)
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Place the shiny key in start_room and transfer it to inventory exactly once.
- Require key use in locked_door_room.
- Unlock the north exit only after the puzzle succeeds.
- End the game when the player reaches treasure_room.

### Concept Explanation

Keep the five-room graph from Lesson 10.2. Room objects also contain item lists. Picking up the shiny key removes it from start_room and adds it to inventory. Using the key succeeds only in locked_door_room when the key is in inventory. The north exit remains blocked until the key is used.

### Worked Example

```csharp
using System;
using System.Collections.Generic;

var rooms = new Dictionary<string, Room>
{
    ["start_room"] = new("A dimly lit cave.", new() { ["north"] = "tunnel" }, new() { "shiny key" }),
    ["tunnel"] = new("A damp tunnel. Passages lead south and east.", new() { ["south"] = "start_room", ["east"] = "clearing" }),
    ["clearing"] = new("A quiet clearing. An antechamber lies to the north.", new() { ["west"] = "tunnel", ["north"] = "locked_door_room" }),
    ["locked_door_room"] = new("A chamber with a heavy door to the north.", new() { ["south"] = "clearing", ["north"] = "treasure_room" }),
    ["treasure_room"] = new("You found the treasure. You win!", new())
};

var current = "start_room";
var inventory = new List<string>();
var doorLocked = true;
while (true)
{
    var room = rooms[current];
    Console.WriteLine();
    Console.WriteLine(room.Description);
    if (current == "treasure_room") break;
    if (room.Items.Count > 0) Console.WriteLine("You see: " + string.Join(", ", room.Items));
    Console.WriteLine("Your inventory: " + (inventory.Count == 0 ? "empty" : string.Join(", ", inventory)));
    Console.WriteLine("What do you want to do?");
    var command = (Console.ReadLine() ?? "quit").Trim().ToLowerInvariant();

    if (command == "quit")
    {
        Console.WriteLine("You quit the adventure.");
        break;
    }
    if (command == "take shiny key")
    {
        if (room.Items.Remove("shiny key"))
        {
            inventory.Add("shiny key");
            Console.WriteLine("You picked up the shiny key.");
        }
        else Console.WriteLine("There is no shiny key here to take.");
    }
    else if (command == "use shiny key")
    {
        if (current != "locked_door_room") Console.WriteLine("You must be at the locked door to use the key.");
        else if (!inventory.Contains("shiny key")) Console.WriteLine("You do not have the shiny key.");
        else
        {
            doorLocked = false;
            Console.WriteLine("You unlocked the door!");
        }
    }
    else if (current == "locked_door_room" && command == "north" && doorLocked)
        Console.WriteLine("The door is locked! You need to use the shiny key here.");
    else if (room.Exits.TryGetValue(command, out var destination))
        current = destination;
    else
        Console.WriteLine("Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.");
}

record Room(string Description, Dictionary<string, string> Exits, List<string> Items)
{
    public Room(string description, Dictionary<string, string> exits) : this(description, exits, new()) { }
}
```

### Expected Behavior or Output

Enter north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north. The first north from locked_door_room is rejected. Taking the key removes it from the room and adds it to inventory. Using it outside locked_door_room is rejected. Using it there unlocks the door; the final north reaches treasure_room and prints the win description.

### Common Mistakes
- Leaving the key in the room after adding it to inventory.
- Unlocking the door outside locked_door_room.
- Unlocking the door without checking inventory.
- Allowing north movement before doorLocked becomes false.
- Treating a failed action as a state change.

### Activities
1. Run the complete puzzle sequence and record room, items, inventory, and door state.
2. Attempt to take the key twice; the second attempt must be rejected.
3. Try to use the key outside locked_door_room.
4. Try north before and after unlocking.
5. Add a help command listing every supported command.

### Accessibility Practice

Announce the room, visible items, inventory, and prompt as separate text lines. Error messages explain the failed action. Test the complete interaction with keyboard-only input and sequential screen-reader output.

### Skills Checklist
- [ ] I can model the five canonical rooms.
- [ ] I can transfer the key from a room to inventory.
- [ ] I can prevent duplicate pickup.
- [ ] I can require key use in locked_door_room.
- [ ] I can block and unlock the north exit.
- [ ] I can end the game in treasure_room.

---

## Lesson 10.4: Command-line to-do manager

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Project work starts with observable requirements and acceptance criteria. Separate domain state, command parsing, validation, persistence, and output so each behavior can be tested and navigated accessibly.
### Worked Example
```cs
var tasks = new List<TodoTask> { new(1, "Read lesson", "Review the C# lesson", false, "2026-11-01") };
tasks.Add(new TodoTask(2, "Run tests", "Check the console application", false, "2026-11-01"));
tasks[0] = tasks[0] with { Done = true };
foreach (var task in tasks) Console.WriteLine($"{task.Id}: [{(task.Done ? "X" : " ")}] {task.Title}");
record TodoTask(int Id, string Title, string Description, bool Done, string CreatedAt);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
1: [X] Read lesson
2: [ ] Run tests
```

### Common Mistakes
- Implementing before defining observable requirements and acceptance tests.
- Combining parsing, domain logic, persistence, and output into one untestable block.
- Providing errors or status that depend on color or visual layout alone.
### Activities
1. Write an acceptance criterion for the behavior demonstrated by the example.
2. Add one valid command and one invalid command or state transition.
3. Separate one responsibility into a method or model and test it independently.
4. Review prompts and output using keyboard navigation and assistive technology.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define observable project requirements.
- [ ] I can implement and test a valid state transition or command.
- [ ] I can handle invalid input with actionable feedback.
- [ ] I can separate domain logic from interaction.
- [ ] I can assess keyboard and screen-reader usability.

## Lesson 10.5: Accessible UX and validation

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Project work starts with observable requirements and acceptance criteria. Separate domain state, command parsing, validation, persistence, and output so each behavior can be tested and navigated accessibly.
### Worked Example
```cs
static bool IsValidAge(string input, out int age) => int.TryParse(input, out age) && age >= 0 && age <= 130;
foreach (string candidate in new[] { "16", "abc", "131" }) Console.WriteLine($"{candidate}: {IsValidAge(candidate, out int age)} (parsed value: {age})");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
16: True (parsed value: 16)
abc: False (parsed value: 0)
131: False (parsed value: 131)
```

### Common Mistakes
- Implementing before defining observable requirements and acceptance tests.
- Combining parsing, domain logic, persistence, and output into one untestable block.
- Providing errors or status that depend on color or visual layout alone.
### Activities
1. Write an acceptance criterion for the behavior demonstrated by the example.
2. Add one valid command and one invalid command or state transition.
3. Separate one responsibility into a method or model and test it independently.
4. Review prompts and output using keyboard navigation and assistive technology.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define observable project requirements.
- [ ] I can implement and test a valid state transition or command.
- [ ] I can handle invalid input with actionable feedback.
- [ ] I can separate domain logic from interaction.
- [ ] I can assess keyboard and screen-reader usability.
