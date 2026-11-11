# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

Plan a text project, build the shared text adventure in two parts, build the command-line to-do manager, and refine input validation.

---

## Lesson 10.1: Requirements and top-down design

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and top-down design using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Separate requirements, application state, domain operations, validation, and terminal interaction. Small functions and explicit types make behavior testable. Terminal prompts should be linear, textual, keyboard-operable, and independent of color or cursor positioning. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 requirements := []string{"list tasks", "add task", "mark task complete", "save tasks"}
 for i, requirement := range requirements { fmt.Printf("%d. %s\n", i+1, requirement) }
}
```

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
1. list tasks
2. add task
3. mark task complete
4. save tasks
```

### Common Mistakes
1. Mixing domain logic with terminal input/output in one function.
2. Assuming map iteration order is stable when displaying choices.
3. Making interaction depend on color, animation, or cursor positioning.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (requirements and top-down design); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain requirements and top-down design using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 10.2: Text adventure: five rooms and movement

### Reading References
- [Go maps](https://go.dev/blog/maps)
- [Go standard library: bufio](https://pkg.go.dev/bufio)
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Represent all five canonical rooms with Go structs and maps.
- Validate movement before changing the current room.
- Explain why treasure_room is not reachable until the key puzzle is implemented.

### Concept Explanation

The shared graph has five rooms: start_room, tunnel, clearing, locked_door_room, and treasure_room. A Room stores its description and valid exits. The player starts in start_room. Part 1 does not provide the north exit from locked_door_room. Map lookup uses the two-result form so a missing direction cannot change state.

### Worked Example

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

type Room struct {
    description string
    exits       map[string]string
}

func main() {
    rooms := map[string]Room{
        "start_room":       {"A dimly lit cave. A narrow passage leads north.", map[string]string{"north": "tunnel"}},
        "tunnel":           {"A damp tunnel. Passages lead south and east.", map[string]string{"south": "start_room", "east": "clearing"}},
        "clearing":         {"A quiet clearing. An antechamber lies to the north.", map[string]string{"west": "tunnel", "north": "locked_door_room"}},
        "locked_door_room": {"A chamber with a heavy door to the north.", map[string]string{"south": "clearing"}},
        "treasure_room":    {"You found the treasure. You win!", map[string]string{}},
    }
    scanner := bufio.NewScanner(os.Stdin)
    current := "start_room"

    for {
        fmt.Println("---")
        fmt.Println(rooms[current].description)
        fmt.Println("What do you want to do?")
        command := "quit"
        if scanner.Scan() {
            command = strings.ToLower(strings.TrimSpace(scanner.Text()))
        }
        if command == "quit" {
            fmt.Println("Exiting game. Goodbye!")
            break
        }
        if destination, ok := rooms[current].exits[command]; ok {
            current = destination
        } else {
            fmt.Println("You cannot go that way. Enter a listed direction or quit.")
        }
    }
}
```

### Expected Behavior or Output

Enter north, east, north, north, quit. The player reaches tunnel, clearing, and locked_door_room. The second north is rejected and the current room does not change. The treasure room exists but has no incoming exit in Part 1.

### Common Mistakes
- Using a map result without checking the boolean.
- Updating current before validating the destination.
- Defining a destination that is not one of the five room identifiers.
- Adding the treasure exit before implementing the key puzzle.

### Activities
1. Trace north, east, north, north and record the current room.
2. Try west from start_room and verify that the room does not change.
3. Check every exit destination against the room map.
4. Explain why treasure_room cannot yet be reached.

### Accessibility Practice

Announce the room description and prompt in a consistent order. The invalid-movement response explains what happened and how to continue. Run from the terminal and inspect output sequentially with the learner's access technology.

### Skills Checklist
- [ ] I can model all five canonical rooms.
- [ ] I can represent exits with maps.
- [ ] I can reject invalid movement without changing state.
- [ ] I can explain why the treasure room is not yet reachable.

---

## Lesson 10.3: Text adventure: shiny key and locked door

### Reading References
- [Go slices](https://go.dev/blog/slices-intro)
- [Go standard library: strings](https://pkg.go.dev/strings)
- Canonical shared project specification: Python Unit 10, Lesson 10.3.

### Learning Objectives
- Place the shiny key in start_room and transfer it to inventory exactly once.
- Require key use in locked_door_room.
- Unlock the north exit only after the puzzle succeeds.
- End the game when the player reaches treasure_room.

### Concept Explanation

Keep the five-room graph from Lesson 10.2. Room values contain slices of items. Picking up the shiny key removes it from start_room and appends it to inventory. Using the key succeeds only in locked_door_room when inventory contains it. The north exit remains blocked until the key is used.

### Worked Example

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

type Room struct {
    description string
    exits       map[string]string
    items       []string
}

func contains(items []string, target string) bool {
    for _, item := range items {
        if item == target {
            return true
        }
    }
    return false
}

func main() {
    rooms := map[string]Room{
        "start_room":       {"A dimly lit cave.", map[string]string{"north": "tunnel"}, []string{"shiny key"}},
        "tunnel":           {"A damp tunnel. Passages lead south and east.", map[string]string{"south": "start_room", "east": "clearing"}, nil},
        "clearing":         {"A quiet clearing. An antechamber lies to the north.", map[string]string{"west": "tunnel", "north": "locked_door_room"}, nil},
        "locked_door_room": {"A chamber with a heavy door to the north.", map[string]string{"south": "clearing", "north": "treasure_room"}, nil},
        "treasure_room":    {"You found the treasure. You win!", map[string]string{}, nil},
    }
    current := "start_room"
    inventory := []string{}
    doorLocked := true
    scanner := bufio.NewScanner(os.Stdin)

    for {
        room := rooms[current]
        fmt.Println()
        fmt.Println(room.description)
        if current == "treasure_room" {
            break
        }
        if len(room.items) > 0 {
            fmt.Println("You see:", strings.Join(room.items, ", "))
        }
        inventoryText := "empty"
        if len(inventory) > 0 {
            inventoryText = strings.Join(inventory, ", ")
        }
        fmt.Println("Your inventory:", inventoryText)
        fmt.Println("What do you want to do?")
        command := "quit"
        if scanner.Scan() {
            command = strings.ToLower(strings.TrimSpace(scanner.Text()))
        }

        switch command {
        case "quit":
            fmt.Println("You quit the adventure.")
            return
        case "take shiny key":
            room = rooms[current]
            if contains(room.items, "shiny key") {
                for i, item := range room.items {
                    if item == "shiny key" {
                        room.items = append(room.items[:i], room.items[i+1:]...)
                        break
                    }
                }
                rooms[current] = room
                inventory = append(inventory, "shiny key")
                fmt.Println("You picked up the shiny key.")
            } else {
                fmt.Println("There is no shiny key here to take.")
            }
        case "use shiny key":
            if current != "locked_door_room" {
                fmt.Println("You must be at the locked door to use the key.")
            } else if !contains(inventory, "shiny key") {
                fmt.Println("You do not have the shiny key.")
            } else {
                doorLocked = false
                fmt.Println("You unlocked the door!")
            }
        case "north":
            if current == "locked_door_room" && doorLocked {
                fmt.Println("The door is locked! You need to use the shiny key here.")
            } else if destination, ok := rooms[current].exits[command]; ok {
                current = destination
            } else {
                fmt.Println("You cannot go that way.")
            }
        case "south", "east", "west":
            if destination, ok := rooms[current].exits[command]; ok {
                current = destination
            } else {
                fmt.Println("You cannot go that way.")
            }
        default:
            fmt.Println("Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.")
        }
    }
}
```

### Expected Behavior or Output

Enter north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north. The first north from locked_door_room is rejected. Taking the key removes it from the room and adds it to inventory. Using it outside locked_door_room is rejected. Using it there unlocks the door; the final north reaches treasure_room and prints the win description.

### Common Mistakes
- Updating a local copy of a Room without writing it back into the map.
- Removing the key without adding it to inventory, or adding it without removing it.
- Unlocking the door outside locked_door_room.
- Allowing north movement before doorLocked becomes false.
- Treating a missing map key as a valid destination.

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
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain command-line to-do manager using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Separate requirements, application state, domain operations, validation, and terminal interaction. Small functions and explicit types make behavior testable. Terminal prompts should be linear, textual, keyboard-operable, and independent of color or cursor positioning. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 type Task struct { ID int; Title string; Done bool }
 tasks := []Task{{ID: 1, Title: "Read lesson"}, {ID: 2, Title: "Run example"}}
 tasks[0].Done = true
 for _, task := range tasks { fmt.Printf("%d: %s [%t]\n", task.ID, task.Title, task.Done) }
}
```

**Expected behavior:** The standalone program demonstrates command-line to-do manager with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Mixing domain logic with terminal input/output in one function.
2. Assuming map iteration order is stable when displaying choices.
3. Making interaction depend on color, animation, or cursor positioning.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (command-line to-do manager); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain command-line to-do manager using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 10.5: Accessible interaction and validation

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain accessible interaction and validation using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Separate requirements, application state, domain operations, validation, and terminal interaction. Small functions and explicit types make behavior testable. Terminal prompts should be linear, textual, keyboard-operable, and independent of color or cursor positioning. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"bufio"
	"fmt"
	"os"
	"strings"
)
func main() {
 reader := bufio.NewReader(os.Stdin)
 fmt.Print("Task title: ")
 title, _ := reader.ReadString('\n')
 title = strings.TrimSpace(title)
 if title == "" { fmt.Println("A title is required.") } else { fmt.Println("Accepted task:", title) }
}
```

**Expected behavior:** The standalone program demonstrates accessible interaction and validation with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Mixing domain logic with terminal input/output in one function.
2. Assuming map iteration order is stable when displaying choices.
3. Making interaction depend on color, animation, or cursor positioning.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (accessible interaction and validation); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain accessible interaction and validation using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

