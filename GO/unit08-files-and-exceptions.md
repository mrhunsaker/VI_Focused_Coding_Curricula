# Unit 8: Files and Exceptions

## Overview

Read and write files, handle errors, release resources reliably, and store records as JSON.

---

>>>>>>> 2067a20 (curriculum clearning and updates)
## Lesson 8.1: Reading text files

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain reading text files using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The os and io packages provide file operations. Functions return errors that callers must check. defer schedules cleanup at function return; check Close errors when writes matter. encoding/json handles JSON serialization with struct tags. Production code should avoid panic for expected failures. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"os"
)
func main() {
 path := "go_read_demo.txt"
 if err := os.WriteFile(path, []byte("Avery,82\n"), 0600); err != nil { panic(err) }
 data, err := os.ReadFile(path)
 if err != nil { panic(err) }
 fmt.Print(string(data))
 if err := os.Remove(path); err != nil { panic(err) }
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates reading text files with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Avery,82
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Ignoring errors from file operations and Close.
2. Calling defer inside a long-running loop and retaining resources too long.
3. Using hand-built JSON instead of encoding/json.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (reading text files); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain reading text files using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 8.2: Writing and appending files

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain writing and appending files using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The os and io packages provide file operations. Functions return errors that callers must check. defer schedules cleanup at function return; check Close errors when writes matter. encoding/json handles JSON serialization with struct tags. Production code should avoid panic for expected failures. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"os"
)
func main() {
 path := "go_append_demo.txt"
 file, err := os.OpenFile(path, os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0600)
 if err != nil { panic(err) }
 if _, err := fmt.Fprintln(file, "Notebook,3"); err != nil { panic(err) }
 if err := file.Close(); err != nil { panic(err) }
 fmt.Println("appended inventory record")
 if err := os.Remove(path); err != nil { panic(err) }
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates writing and appending files with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
appended inventory record
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Ignoring errors from file operations and Close.
2. Calling defer inside a long-running loop and retaining resources too long.
3. Using hand-built JSON instead of encoding/json.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (writing and appending files); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain writing and appending files using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 8.3: Explicit error handling

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain explicit error handling using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The os and io packages provide file operations. Functions return errors that callers must check. defer schedules cleanup at function return; check Close errors when writes matter. encoding/json handles JSON serialization with struct tags. Production code should avoid panic for expected failures. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"errors"
	"fmt"
)
func main() {
 load := func(path string) (string, error) { return "", errors.New("file not found: " + path) }
 text, err := load("missing_course_file.txt")
 if err != nil { fmt.Println("Could not read file:", err) } else { fmt.Println(text) }
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates explicit error handling with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Could not read file: file not found: missing_course_file.txt
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Ignoring errors from file operations and Close.
2. Calling defer inside a long-running loop and retaining resources too long.
3. Using hand-built JSON instead of encoding/json.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (explicit error handling); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain explicit error handling using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 8.4: Deferred cleanup and resource lifetime

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain deferred cleanup and resource lifetime using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The os and io packages provide file operations. Functions return errors that callers must check. defer schedules cleanup at function return; check Close errors when writes matter. encoding/json handles JSON serialization with struct tags. Production code should avoid panic for expected failures. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"os"
)
func main() {
 path := "go_cleanup_demo.txt"
 file, err := os.Create(path)
 if err != nil { panic(err) }
 defer func() { if err := file.Close(); err != nil { fmt.Println("close error:", err) }; _ = os.Remove(path) }()
 if _, err := fmt.Fprintln(file, "closed when function returns"); err != nil { panic(err) }
 fmt.Println("deferred cleanup is scheduled")
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates deferred cleanup and resource lifetime with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
deferred cleanup is scheduled
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Ignoring errors from file operations and Close.
2. Calling defer inside a long-running loop and retaining resources too long.
3. Using hand-built JSON instead of encoding/json.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (deferred cleanup and resource lifetime); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain deferred cleanup and resource lifetime using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 8.5: JSON encoding and persistence

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain json encoding and persistence using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The os and io packages provide file operations. Functions return errors that callers must check. defer schedules cleanup at function return; check Close errors when writes matter. encoding/json handles JSON serialization with struct tags. Production code should avoid panic for expected failures. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"encoding/json"
	"fmt"
)
func main() {
 record := struct { Name string `json:"name"`; Score int `json:"score"` }{Name: "Avery", Score: 82}
 data, err := json.Marshal(record)
 if err != nil { panic(err) }
 fmt.Println(string(data))
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates json encoding and persistence with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
{"name":"Avery","score":82}
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Ignoring errors from file operations and Close.
2. Calling defer inside a long-running loop and retaining resources too long.
3. Using hand-built JSON instead of encoding/json.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (json encoding and persistence); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain json encoding and persistence using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

<<<<<<< HEAD
=======
