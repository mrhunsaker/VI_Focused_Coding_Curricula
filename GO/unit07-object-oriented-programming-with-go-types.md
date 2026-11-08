# Unit 7: Object-Oriented Programming with Go Types

## Overview
This unit develops object-oriented programming with go types using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction.

## Lesson 7.1: Structs and data modeling

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain structs and data modeling using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
<<<<<<< HEAD
package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Score int }
	type Status int
	const ( Active Status = iota; Inactive )
	s := Student{Name: "Avery", Score: 82}
	state := Active
	fmt.Printf("%s: %d; active=%t; inactive=%t\n", s.Name, s.Score, state == Active, Inactive == Inactive)
},package main
import (
	"fmt"
)
type Student struct { Name string; Score int }
func (s *Student) AddPoints(points int) { s.Score += points }
func main() {
	s := Student{Name: "Avery", Score: 82}
	s.AddPoints(3)
	fmt.Println(s.Name, "score:", s.Score)
},package main
import (
	"fmt"
)
type Summarizer interface { Summary() string }
type Task struct { Title string; Done bool }
func (t Task) Summary() string { return fmt.Sprintf("%s: %t", t.Title, t.Done) }
func main() {
	var item Summarizer = Task{Title: "Study Go", Done: false}
	fmt.Println(item.Summary())
},package main
import (
	"fmt"
)
func main() {
	type Contact struct { Email string }
	type Contact struct { Email string }
type Student struct { Name string; Contact }
	s := Student{Name: "Avery", Contact: Contact{Email: "avery@example.test"}}
	fmt.Println(s.Name, s.Email)
},package main
import (
	"fmt"
)
type Reader interface { Read() string }
type Note struct { Text string }
func (n Note) Read() string { return n.Text }
func display(r Reader) { fmt.Println(r.Read()) }
func main() {
	display(Note{Text: "Composition and interfaces"})
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
=======
A struct groups named fields into a new type. `type Item struct { Name string; Quantity int; UnitPrice float64 }` models the shared inventory item, and a struct literal creates values. Fields are read and written with a dot. A struct is copied when assigned or passed, so use a pointer when a function must change the original.
### Worked Example

**Example 7.1.1**
>>>>>>> 2067a20 (curriculum clearning and updates)
```go
package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Score int }
	type Status int
	const ( Active Status = iota; Inactive )
	s := Student{Name: "Avery", Score: 82}
	state := Active
	fmt.Printf("%s: %d; active=%t; inactive=%t\n", s.Name, s.Score, state == Active, Inactive == Inactive)
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates structs and data modeling with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 7.1.2**
```go
package main
import (
	"fmt"
)
type Student struct { Name string; Score int }
func (s *Student) AddPoints(points int) { s.Score += points }
func main() {
	s := Student{Name: "Avery", Score: 82}
	s.AddPoints(3)
	fmt.Println(s.Name, "score:", s.Score)
}
```

**Example 7.1.3**
```go
package main
import (
	"fmt"
)
type Summarizer interface { Summary() string }
type Task struct { Title string; Done bool }
func (t Task) Summary() string { return fmt.Sprintf("%s: %t", t.Title, t.Done) }
func main() {
	var item Summarizer = Task{Title: "Study Go", Done: false}
	fmt.Println(item.Summary())
}
```

**Example 7.1.4**
```go
package main
import (
	"fmt"
)
type Reader interface { Read() string }
type Note struct { Text string }
func (n Note) Read() string { return n.Text }
func display(r Reader) { fmt.Println(r.Read()) }
func main() {
	display(Note{Text: "Composition and interfaces"})
}
```


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Avery: 82; active=true; inactive=true
```

Example 2:
```text
Avery score: 85
```

Example 3:
```text
Study Go: false
```

Example 4:
```text
Composition and interfaces
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Using a value receiver when mutation of the original struct is required.
2. Assuming Go interfaces must be declared as implemented explicitly.
3. Mistaking embedding for class inheritance or assuming promoted fields are always unambiguous.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (structs and data modeling); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain structs and data modeling using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 7.2: Creating values and pointer receivers

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain creating values and pointer receivers using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go models data with structs and behavior with methods and interfaces. Pointer receivers can mutate a value; interfaces are satisfied implicitly. Embedding promotes fields and methods but is composition, not inheritance. Keep domain types small and make dependencies explicit. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
	type Student struct { Name string; Score int }
	func (s *Student) AddPoints(points int) { s.Score += points }
	func main() {
	 s := Student{Name: "Avery", Score: 82}
	 s.AddPoints(3)
	 fmt.Println(s.Name, "score:", s.Score)
	}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates creating values and pointer receivers with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Avery score: 85
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Using a value receiver when mutation of the original struct is required.
2. Assuming interfaces must be declared as implemented explicitly.
3. Mistaking embedding for class inheritance or overlooking promoted-field ambiguity.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (creating values and pointer receivers); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain creating values and pointer receivers using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 7.3: Methods and interfaces

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain methods and interfaces using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go models data with structs and behavior with methods and interfaces. Pointer receivers can mutate a value; interfaces are satisfied implicitly. Embedding promotes fields and methods but is composition, not inheritance. Keep domain types small and make dependencies explicit. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
	type Summarizer interface { Summary() string }
	type Task struct { Title string; Done bool }
	func (t Task) Summary() string { return fmt.Sprintf("%s: %t", t.Title, t.Done) }
	func main() {
	 var item Summarizer = Task{Title: "Study Go", Done: false}
	 fmt.Println(item.Summary())
	}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates methods and interfaces with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Study Go: false
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Using a value receiver when mutation of the original struct is required.
2. Assuming interfaces must be declared as implemented explicitly.
3. Mistaking embedding for class inheritance or overlooking promoted-field ambiguity.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (methods and interfaces); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain methods and interfaces using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 7.4: Embedding and polymorphism

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain embedding and polymorphism using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go models data with structs and behavior with methods and interfaces. Pointer receivers can mutate a value; interfaces are satisfied implicitly. Embedding promotes fields and methods but is composition, not inheritance. Keep domain types small and make dependencies explicit. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
	func main() {
	 type Contact struct { Email string }
	 type Student struct { Name string; Contact }
	 s := Student{Name: "Avery", Contact: Contact{Email: "avery@example.test"}}
	 fmt.Println(s.Name, s.Email)
	}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates embedding and polymorphism with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Avery avery@example.test
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Using a value receiver when mutation of the original struct is required.
2. Assuming interfaces must be declared as implemented explicitly.
3. Mistaking embedding for class inheritance or overlooking promoted-field ambiguity.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (embedding and polymorphism); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain embedding and polymorphism using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 7.5: Composition and collaboration

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain composition and collaboration using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go models data with structs and behavior with methods and interfaces. Pointer receivers can mutate a value; interfaces are satisfied implicitly. Embedding promotes fields and methods but is composition, not inheritance. Keep domain types small and make dependencies explicit. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
	type Reader interface { Read() string }
	type Note struct { Text string }
	func (n Note) Read() string { return n.Text }
	func display(r Reader) { fmt.Println(r.Read()) }
	func main() { display(Note{Text: "Composition and interfaces"}) }
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates composition and collaboration with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Composition and interfaces
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Using a value receiver when mutation of the original struct is required.
2. Assuming interfaces must be declared as implemented explicitly.
3. Mistaking embedding for class inheritance or overlooking promoted-field ambiguity.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (composition and collaboration); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain composition and collaboration using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

<<<<<<< HEAD
=======
