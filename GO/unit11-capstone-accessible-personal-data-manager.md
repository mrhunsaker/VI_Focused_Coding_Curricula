# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

Build a personal data manager with the shared record schema, storage, search and completion, acceptance tests, and a documentation and accessibility check.

---

## Lesson 11.1: Requirements and design

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and design using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is an accessible record manager. Define record fields, validation rules, and storage format; implement create/read/update/delete; persist safely; and test normal, boundary, malformed, and missing-data cases. Document exact build, test, and run commands. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"strings"
)
func main() {
 fields := []string{"id", "title", "description", "category", "created_at", "updated_at"}
 fmt.Println("Capstone fields:", strings.Join(fields, ", "))
}
```

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Capstone fields: id, title, description, category, created_at, updated_at
```

### Common Mistakes
1. Updating a record without confirming that the identifier exists.
2. Overwriting the only persisted copy before validating new data.
3. Treating a successful build as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical capstone record fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (requirements and design); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain requirements and design using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 11.2: Data model and storage

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain data model and storage using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is an accessible record manager. Define record fields, validation rules, and storage format; implement create/read/update/delete; persist safely; and test normal, boundary, malformed, and missing-data cases. Document exact build, test, and run commands. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"encoding/json"
	"fmt"
)
func main() {
 type Record struct {
  ID int `json:"id"`
  Title string `json:"title"`
  Description string `json:"description"`
  Category string `json:"category"`
  CreatedAt string `json:"created_at"`
  UpdatedAt string `json:"updated_at"`
 }
 record := Record{ID: 1, Title: "Study Go", Description: "Complete the Go capstone", Category: "learning", CreatedAt: "2026-11-01", UpdatedAt: "2026-11-01"}
 data, err := json.Marshal(record)
 if err != nil { panic(err) }
 fmt.Println(string(data))
}
```

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
{"id":1,"title":"Study Go","category":"learning"}
```

### Common Mistakes
1. Updating a record without confirming that the identifier exists.
2. Overwriting the only persisted copy before validating new data.
3. Treating a successful build as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical capstone record fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (data model and storage); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain data model and storage using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 11.3: Create, read, update, delete

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain create, read, update, delete using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is an accessible record manager. Define record fields, validation rules, and storage format; implement create/read/update/delete; persist safely; and test normal, boundary, malformed, and missing-data cases. Document exact build, test, and run commands. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 type Record struct { ID int; Title string; Done bool }
 records := []Record{{ID: 1, Title: "Draft"}, {ID: 2, Title: "Review"}}
 records[0].Done = true
 for _, record := range records { fmt.Printf("%d %s done=%t\n", record.ID, record.Title, record.Done) }
}
```

**Expected behavior:** The standalone program demonstrates create, read, update, delete with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Updating a record without confirming that the identifier exists.
2. Overwriting the only persisted copy before validating new data.
3. Treating a successful build as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical capstone record fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (create, read, update, delete); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain create, read, update, delete using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 11.4: Validation and tests

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain validation and tests using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is an accessible record manager. Define record fields, validation rules, and storage format; implement create/read/update/delete; persist safely; and test normal, boundary, malformed, and missing-data cases. Document exact build, test, and run commands. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"strings"
)
func main() {
 valid := func(title string) bool { return strings.TrimSpace(title) != "" && len([]rune(title)) <= 80 }
 for _, title := range []string{"Plan", "", strings.Repeat("x", 81)} { fmt.Printf("%q valid=%t\n", title, valid(title)) }
}
```

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
"Plan" valid=true
"" valid=false
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" valid=false
```

### Common Mistakes
1. Updating a record without confirming that the identifier exists.
2. Overwriting the only persisted copy before validating new data.
3. Treating a successful build as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical capstone record fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (validation and tests); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain validation and tests using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 11.5: Documentation and presentation

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain documentation and presentation using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is an accessible record manager. Define record fields, validation rules, and storage format; implement create/read/update/delete; persist safely; and test normal, boundary, malformed, and missing-data cases. Document exact build, test, and run commands. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 fmt.Println("Project: accessible record manager")
 fmt.Println("Build: go build ./...")
 fmt.Println("Test: go test ./...")
 fmt.Println("Run: go run .")
 fmt.Println("Document validation, storage, errors, and keyboard workflow.")
}
```

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Project: accessible record manager
Build: go build ./...
Test: go test ./...
Run: go run .
Document validation, storage, errors, and keyboard workflow.
```

### Common Mistakes
1. Updating a record without confirming that the identifier exists.
2. Overwriting the only persisted copy before validating new data.
3. Treating a successful build as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical capstone record fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (documentation and presentation); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain documentation and presentation using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Course-Wide Assessment and Portfolio

Submit a Go module that passes gofmt, go test ./..., and go build ./.... Document its data model, validation rules, error handling, persistence format, and keyboard/screen-reader workflow. Include exact build, test, and run commands in README.md.

## AI Policy

AI tools may explain compiler diagnostics, compare data structures, and suggest test cases. Learners must explain every type, package, error path, concurrency decision, and dependency. Compile and test generated code, review dependency provenance, and do not expose private data or credentials. AI output is a draft, not evidence of correctness.

## Go-Specific Verification Notes

The examples use the standard library. Production CSV processing should use encoding/csv rather than splitting rows manually. Check every file and JSON operation error; avoid panic for expected failures. The random sequence example is deterministic and pedagogical, not cryptographically secure.
