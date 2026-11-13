[Header 2 ("unit-10-project-based-learning--text-based-applications", [], []) [Str "Unit 10: Project-Based Learning — Text-Based Applications"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Plan a text project, build the shared text adventure in two parts, build the command-line to-do manager, and refine input validation."], HorizontalRule, Header 3 ("lesson-101-requirements-and-top-down-design", ["unnumbered", "unlisted"], []) [Str "Lesson 10.1: Requirements and top-down design"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain requirements and top-down design using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Separate requirements, application state, domain operations, validation, and terminal interaction. Small functions and explicit types make behavior testable. Terminal prompts should be linear, textual, keyboard-operable, and independent of color or cursor positioning. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
 requirements := []string{\"list tasks\", \"add task\", \"mark task complete\", \"save tasks\"}
 for i, requirement := range requirements { fmt.Printf(\"%d. %s\\n\", i+1, requirement) }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], CodeBlock ("", ["text"], []) "1. list tasks
2. add task
3. mark task complete
4. save tasks
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Mixing domain logic with terminal input/output in one function."]], [Plain [Str "Assuming map iteration order is stable when displaying choices."]], [Plain [Str "Making interaction depend on color, animation, or cursor positioning."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical text-adventure state and to-do fields and predict the output before running it."]], [Plain [Str "Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program."]], [Plain [Str "Refactor one part using the Go feature in this lesson (requirements and top-down design); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain requirements and top-down design using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-102-text-adventure-five-rooms-and-movement", ["unnumbered", "unlisted"], []) [Str "Lesson 10.2: Text adventure: five rooms and movement"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Go maps"] ("https://go.dev/blog/maps", "")]], [Plain [Link ("", [], []) [Str "Go standard library: bufio"] ("https://pkg.go.dev/bufio", "")]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Represent all five canonical rooms with Go structs and maps."]], [Plain [Str "Validate movement before changing the current room."]], [Plain [Str "Explain why treasure_room is not reachable until the key puzzle is implemented."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The shared graph has five rooms: start_room, tunnel, clearing, locked_door_room, and treasure_room. A Room stores its description and valid exits. The player starts in start_room. Part 1 does not provide the north exit from locked_door_room. Map lookup uses the two-result form so a missing direction cannot change state."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main

import (
    \"bufio\"
    \"fmt\"
    \"os\"
    \"strings\"
)

type Room struct {
    description string
    exits       map[string]string
}

func main() {
    rooms := map[string]Room{
        \"start_room\":       {\"A dimly lit cave. A narrow passage leads north.\", map[string]string{\"north\": \"tunnel\"}},
        \"tunnel\":           {\"A damp tunnel. Passages lead south and east.\", map[string]string{\"south\": \"start_room\", \"east\": \"clearing\"}},
        \"clearing\":         {\"A quiet clearing. An antechamber lies to the north.\", map[string]string{\"west\": \"tunnel\", \"north\": \"locked_door_room\"}},
        \"locked_door_room\": {\"A chamber with a heavy door to the north.\", map[string]string{\"south\": \"clearing\"}},
        \"treasure_room\":    {\"You found the treasure. You win!\", map[string]string{}},
    }
    scanner := bufio.NewScanner(os.Stdin)
    current := \"start_room\"

    for {
        fmt.Println(\"---\")
        fmt.Println(rooms[current].description)
        fmt.Println(\"What do you want to do?\")
        command := \"quit\"
        if scanner.Scan() {
            command = strings.ToLower(strings.TrimSpace(scanner.Text()))
        }
        if command == \"quit\" {
            fmt.Println(\"Exiting game. Goodbye!\")
            break
        }
        if destination, ok := rooms[current].exits[command]; ok {
            current = destination
        } else {
            fmt.Println(\"You cannot go that way. Enter a listed direction or quit.\")
        }
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Enter north, east, north, north, quit. The player reaches tunnel, clearing, and locked_door_room. The second north is rejected and the current room does not change. The treasure room exists but has no incoming exit in Part 1."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Using a map result without checking the boolean."]], [Plain [Str "Updating current before validating the destination."]], [Plain [Str "Defining a destination that is not one of the five room identifiers."]], [Plain [Str "Adding the treasure exit before implementing the key puzzle."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace north, east, north, north and record the current room."]], [Plain [Str "Try west from start_room and verify that the room does not change."]], [Plain [Str "Check every exit destination against the room map."]], [Plain [Str "Explain why treasure_room cannot yet be reached."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Announce the room description and prompt in a consistent order. The invalid-movement response explains what happened and how to continue. Run from the terminal and inspect output sequentially with the learner's access technology."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model all five canonical rooms."]], [Plain [Str "\9744", Space, Str "I can represent exits with maps."]], [Plain [Str "\9744", Space, Str "I can reject invalid movement without changing state."]], [Plain [Str "\9744", Space, Str "I can explain why the treasure room is not yet reachable."]]], HorizontalRule, Header 3 ("lesson-103-text-adventure-shiny-key-and-locked-door", ["unnumbered", "unlisted"], []) [Str "Lesson 10.3: Text adventure: shiny key and locked door"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Go slices"] ("https://go.dev/blog/slices-intro", "")]], [Plain [Link ("", [], []) [Str "Go standard library: strings"] ("https://pkg.go.dev/strings", "")]], [Plain [Str "Canonical shared project specification: Python Unit 10, Lesson 10.3."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Place the shiny key in start_room and transfer it to inventory exactly once."]], [Plain [Str "Require key use in locked_door_room."]], [Plain [Str "Unlock the north exit only after the puzzle succeeds."]], [Plain [Str "End the game when the player reaches treasure_room."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Keep the five-room graph from Lesson 10.2. Room values contain slices of items. Picking up the shiny key removes it from start_room and appends it to inventory. Using the key succeeds only in locked_door_room when inventory contains it. The north exit remains blocked until the key is used."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main

import (
    \"bufio\"
    \"fmt\"
    \"os\"
    \"strings\"
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
        \"start_room\":       {\"A dimly lit cave.\", map[string]string{\"north\": \"tunnel\"}, []string{\"shiny key\"}},
        \"tunnel\":           {\"A damp tunnel. Passages lead south and east.\", map[string]string{\"south\": \"start_room\", \"east\": \"clearing\"}, nil},
        \"clearing\":         {\"A quiet clearing. An antechamber lies to the north.\", map[string]string{\"west\": \"tunnel\", \"north\": \"locked_door_room\"}, nil},
        \"locked_door_room\": {\"A chamber with a heavy door to the north.\", map[string]string{\"south\": \"clearing\", \"north\": \"treasure_room\"}, nil},
        \"treasure_room\":    {\"You found the treasure. You win!\", map[string]string{}, nil},
    }
    current := \"start_room\"
    inventory := []string{}
    doorLocked := true
    scanner := bufio.NewScanner(os.Stdin)

    for {
        room := rooms[current]
        fmt.Println()
        fmt.Println(room.description)
        if current == \"treasure_room\" {
            break
        }
        if len(room.items) > 0 {
            fmt.Println(\"You see:\", strings.Join(room.items, \", \"))
        }
        inventoryText := \"empty\"
        if len(inventory) > 0 {
            inventoryText = strings.Join(inventory, \", \")
        }
        fmt.Println(\"Your inventory:\", inventoryText)
        fmt.Println(\"What do you want to do?\")
        command := \"quit\"
        if scanner.Scan() {
            command = strings.ToLower(strings.TrimSpace(scanner.Text()))
        }

        switch command {
        case \"quit\":
            fmt.Println(\"You quit the adventure.\")
            return
        case \"take shiny key\":
            room = rooms[current]
            if contains(room.items, \"shiny key\") {
                for i, item := range room.items {
                    if item == \"shiny key\" {
                        room.items = append(room.items[:i], room.items[i+1:]...)
                        break
                    }
                }
                rooms[current] = room
                inventory = append(inventory, \"shiny key\")
                fmt.Println(\"You picked up the shiny key.\")
            } else {
                fmt.Println(\"There is no shiny key here to take.\")
            }
        case \"use shiny key\":
            if current != \"locked_door_room\" {
                fmt.Println(\"You must be at the locked door to use the key.\")
            } else if !contains(inventory, \"shiny key\") {
                fmt.Println(\"You do not have the shiny key.\")
            } else {
                doorLocked = false
                fmt.Println(\"You unlocked the door!\")
            }
        case \"north\":
            if current == \"locked_door_room\" && doorLocked {
                fmt.Println(\"The door is locked! You need to use the shiny key here.\")
            } else if destination, ok := rooms[current].exits[command]; ok {
                current = destination
            } else {
                fmt.Println(\"You cannot go that way.\")
            }
        case \"south\", \"east\", \"west\":
            if destination, ok := rooms[current].exits[command]; ok {
                current = destination
            } else {
                fmt.Println(\"You cannot go that way.\")
            }
        default:
            fmt.Println(\"Invalid command. Enter north, south, east, west, take shiny key, use shiny key, or quit.\")
        }
    }
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Enter north, east, north, north, south, west, south, take shiny key, north, east, north, use shiny key, north. The first north from locked_door_room is rejected. Taking the key removes it from the room and adds it to inventory. Using it outside locked_door_room is rejected. Using it there unlocks the door; the final north reaches treasure_room and prints the win description."], Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Updating a local copy of a Room without writing it back into the map."]], [Plain [Str "Removing the key without adding it to inventory, or adding it without removing it."]], [Plain [Str "Unlocking the door outside locked_door_room."]], [Plain [Str "Allowing north movement before doorLocked becomes false."]], [Plain [Str "Treating a missing map key as a valid destination."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the complete puzzle sequence and record room, items, inventory, and door state."]], [Plain [Str "Attempt to take the key twice; the second attempt must be rejected."]], [Plain [Str "Try to use the key outside locked_door_room."]], [Plain [Str "Try north before and after unlocking."]], [Plain [Str "Add a help command listing every supported command."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Announce the room, visible items, inventory, and prompt as separate text lines. Error messages explain the failed action. Test the complete interaction with keyboard-only input and sequential screen-reader output."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model the five canonical rooms."]], [Plain [Str "\9744", Space, Str "I can transfer the key from a room to inventory."]], [Plain [Str "\9744", Space, Str "I can prevent duplicate pickup."]], [Plain [Str "\9744", Space, Str "I can require key use in locked_door_room."]], [Plain [Str "\9744", Space, Str "I can block and unlock the north exit."]], [Plain [Str "\9744", Space, Str "I can end the game in treasure_room."]]], HorizontalRule, Header 3 ("lesson-104-command-line-to-do-manager", ["unnumbered", "unlisted"], []) [Str "Lesson 10.4: Command-line to-do manager"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain command-line to-do manager using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Separate requirements, application state, domain operations, validation, and terminal interaction. Small functions and explicit types make behavior testable. Terminal prompts should be linear, textual, keyboard-operable, and independent of color or cursor positioning. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
 type Task struct { ID int; Title string; Done bool }
 tasks := []Task{{ID: 1, Title: \"Read lesson\"}, {ID: 2, Title: \"Run example\"}}
 tasks[0].Done = true
 for _, task := range tasks { fmt.Printf(\"%d: %s [%t]\\n\", task.ID, task.Title, task.Done) }
}
", Para [Strong [Str "Expected behavior:"], Str " The standalone program demonstrates command-line to-do manager with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output."], Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Mixing domain logic with terminal input/output in one function."]], [Plain [Str "Assuming map iteration order is stable when displaying choices."]], [Plain [Str "Making interaction depend on color, animation, or cursor positioning."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical text-adventure state and to-do fields and predict the output before running it."]], [Plain [Str "Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program."]], [Plain [Str "Refactor one part using the Go feature in this lesson (command-line to-do manager); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain command-line to-do manager using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-105-accessible-interaction-and-validation", ["unnumbered", "unlisted"], []) [Str "Lesson 10.5: Accessible interaction and validation"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain accessible interaction and validation using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Separate requirements, application state, domain operations, validation, and terminal interaction. Small functions and explicit types make behavior testable. Terminal prompts should be linear, textual, keyboard-operable, and independent of color or cursor positioning. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main
import (
	\"bufio\"
	\"fmt\"
	\"os\"
	\"strings\"
)
func main() {
 reader := bufio.NewReader(os.Stdin)
 fmt.Print(\"Task title: \")
 title, _ := reader.ReadString('\\n')
 title = strings.TrimSpace(title)
 if title == \"\" { fmt.Println(\"A title is required.\") } else { fmt.Println(\"Accepted task:\", title) }
}
", Para [Strong [Str "Expected behavior:"], Str " The standalone program demonstrates accessible interaction and validation with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output."], Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Mixing domain logic with terminal input/output in one function."]], [Plain [Str "Assuming map iteration order is stable when displaying choices."]], [Plain [Str "Making interaction depend on color, animation, or cursor positioning."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical text-adventure state and to-do fields and predict the output before running it."]], [Plain [Str "Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program."]], [Plain [Str "Refactor one part using the Go feature in this lesson (accessible interaction and validation); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain accessible interaction and validation using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]]]