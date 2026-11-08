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

<<<<<<< HEAD
=======
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

>>>>>>> 2067a20 (curriculum clearning and updates)
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

## Lesson 10.2: Text adventure: rooms and movement

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
<<<<<<< HEAD
var exits = new Dictionary<string, string> { ["start_room:north"] = "tunnel" }; string room = "start_room", direction = "north";
string transition = $"{room}:{direction}";
if (exits.TryGetValue(transition, out string? destination)) room = destination;
=======
var exits = new Dictionary<string, string> { ["north"] = "Library", ["east"] = "Garden" }; string room = "Atrium", direction = "north";
if (exits.TryGetValue(direction, out string? destination)) room = destination;
>>>>>>> 2067a20 (curriculum clearning and updates)
Console.WriteLine($"Current room: {room}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Current room: Library
```

>>>>>>> 2067a20 (curriculum clearning and updates)
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

## Lesson 10.3: Text adventure: inventory and puzzles

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
<<<<<<< HEAD
var inventory = new HashSet<string> { "shiny key", "map" }; bool canOpenChest = inventory.Contains("shiny key");
=======
var inventory = new HashSet<string> { "key", "map" }; bool canOpenChest = inventory.Contains("key");
>>>>>>> 2067a20 (curriculum clearning and updates)
if (canOpenChest) inventory.Add("chest reward");
Console.WriteLine($"Chest opened: {canOpenChest}; items: {string.Join(", ", inventory)}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Chest opened: True; items: key, map, chest reward
```

>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
1: [X] Read lesson
2: [ ] Run tests
```

>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
=======
### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
16: True (parsed value: 16)
abc: False (parsed value: 0)
131: False (parsed value: 131)
```

>>>>>>> 2067a20 (curriculum clearning and updates)
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
