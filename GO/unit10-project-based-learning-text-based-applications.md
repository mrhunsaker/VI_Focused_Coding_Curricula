# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

Plan a text project, build the shared text adventure in two parts, build the command-line to-do manager, and refine input validation.

---

>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates requirements and top-down design with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
1. list tasks
2. add task
3. mark task complete
4. save tasks
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: rooms and movement using Go terminology and type conventions.
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
 rooms := map[string]string{"hall": "library", "library": "garden", "garden": "hall"}
 current := "hall"
 next, ok := rooms[current]
 if !ok { fmt.Println("Unknown room") } else { current = next; fmt.Println("Moved to:", current) }
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates text adventure: rooms and movement with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Moved to: library
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Mixing domain logic with terminal input/output in one function.
2. Assuming map iteration order is stable when displaying choices.
3. Making interaction depend on color, animation, or cursor positioning.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (text adventure: rooms and movement); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain text adventure: rooms and movement using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: inventory and puzzles using Go terminology and type conventions.
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
<<<<<<< HEAD
 inventory := map[string]bool{"shiny key": true}
 unlocked := inventory["shiny key"]
=======
 inventory := map[string]bool{"key": true}
 unlocked := inventory["key"]
>>>>>>> 2067a20 (curriculum clearning and updates)
 if unlocked { inventory["map"] = true }
 fmt.Println("puzzle unlocked:", unlocked, "inventory:", inventory)
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates text adventure: inventory and puzzles with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
puzzle unlocked: true inventory: map[key:true map:true]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Mixing domain logic with terminal input/output in one function.
2. Assuming map iteration order is stable when displaying choices.
3. Making interaction depend on color, animation, or cursor positioning.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (text adventure: inventory and puzzles); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain text adventure: inventory and puzzles using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates command-line to-do manager with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
1: Read lesson [true]
2: Run example [false]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates accessible interaction and validation with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Task title: A title is required.
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
=======
