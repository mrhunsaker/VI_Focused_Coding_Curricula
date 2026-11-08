# Unit 4: Data Structures

## Overview
This unit develops data structures using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction.

## Lesson 4.1: Slices and collection mutation

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain slices and collection mutation using Go terminology and type conventions.
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
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
},package main
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
},package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
},package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
=======
`append` adds to a slice and returns the (possibly new) slice, so the result must be assigned back: `scores = append(scores, 95)`. Removing an element is done by re-slicing and appending: `scores = append(scores[:i], scores[i+1:]...)`. Because slices share memory, a change through one slice variable can appear through another.
### Worked Example

**Example 4.1.1**
>>>>>>> 2067a20 (curriculum clearning and updates)
```go
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates slices and collection mutation with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 4.1.2**
```go
package main
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
}
```

**Example 4.1.3**
```go
package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
}
```

**Example 4.1.4**
```go
package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
}
```

**Example 4.1.5**
```go
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
}
```


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
[82 91 76 88]
```

Example 2:
```text
ascending: [76 82 88 91]
descending: [91 88 82 76]
```

Example 3:
```text
Avery age 16 score 82
```

Example 4:
```text
Notebook stock: 3
```

Example 5:
```text
Passing: [82 91 88]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Assuming append always mutates the original backing array in place.
2. Relying on map iteration order.
3. Mutating a map or slice while overlooking aliasing through shared references.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (slices and collection mutation); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain slices and collection mutation using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 4.2: Sorting and organizing data

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain sorting and organizing data using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
<<<<<<< HEAD
=======
The `sort` package sorts slices in place: `sort.Ints`, `sort.Strings`, and `sort.Slice` with a comparison function. `sort.Sort(sort.Reverse(sort.IntSlice(s)))` sorts in descending order. To keep the original order, copy the slice first with `copy` or `slices.Clone`.
### Worked Example

**Example 4.2.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
<<<<<<< HEAD
},package main
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
},package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
},package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
=======
}
```

**Example 4.2.2**
>>>>>>> 2067a20 (curriculum clearning and updates)
```go
package main
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates sorting and organizing data with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 4.2.3**
```go
package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
}
```

**Example 4.2.4**
```go
package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
}
```

**Example 4.2.5**
```go
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
}
```


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
[82 91 76 88]
```

Example 2:
```text
ascending: [76 82 88 91]
descending: [91 88 82 76]
```

Example 3:
```text
Avery age 16 score 82
```

Example 4:
```text
Notebook stock: 3
```

Example 5:
```text
Passing: [82 91 88]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Assuming append always mutates the original backing array in place.
2. Relying on map iteration order.
3. Mutating a map or slice while overlooking aliasing through shared references.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (sorting and organizing data); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain sorting and organizing data using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 4.3: Structs and tuple-like multiple returns

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain structs and tuple-like multiple returns using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
<<<<<<< HEAD
=======
Go has no tuples. A struct groups named fields into one value, and a function can return several values. Returning `(x, y)` and receiving `x, y := point()` covers the same need. Struct values are copied on assignment, which makes a struct a good fixed record.
### Worked Example

**Example 4.3.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.3.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
<<<<<<< HEAD
},package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
},package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
=======
}
```

**Example 4.3.3**
>>>>>>> 2067a20 (curriculum clearning and updates)
```go
package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates structs and tuple-like multiple returns with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 4.3.4**
```go
package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
}
```

**Example 4.3.5**
```go
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
}
```


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
[82 91 76 88]
```

Example 2:
```text
ascending: [76 82 88 91]
descending: [91 88 82 76]
```

Example 3:
```text
Avery age 16 score 82
```

Example 4:
```text
Notebook stock: 3
```

Example 5:
```text
Passing: [82 91 88]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Assuming append always mutates the original backing array in place.
2. Relying on map iteration order.
3. Mutating a map or slice while overlooking aliasing through shared references.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (structs and tuple-like multiple returns); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain structs and tuple-like multiple returns using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 4.4: Maps and key-value data

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain maps and key-value data using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
<<<<<<< HEAD
=======
A map holds key-value pairs: `map[string]int`. Reading a missing key returns the zero value, so the two-value form `value, ok := m[key]` tells you whether the key exists. `delete(m, key)` removes a key, and `len(m)` counts the keys. A nil map can be read but writing to it panics, so create maps with `make` or a literal.
### Worked Example

**Example 4.4.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.4.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.4.3**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
<<<<<<< HEAD
},package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
=======
}
```

**Example 4.4.4**
>>>>>>> 2067a20 (curriculum clearning and updates)
```go
package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates maps and key-value data with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 4.4.5**
```go
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
}
```


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
[82 91 76 88]
```

Example 2:
```text
ascending: [76 82 88 91]
descending: [91 88 82 76]
```

Example 3:
```text
Avery age 16 score 82
```

Example 4:
```text
Notebook stock: 3
```

Example 5:
```text
Passing: [82 91 88]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Assuming append always mutates the original backing array in place.
2. Relying on map iteration order.
3. Mutating a map or slice while overlooking aliasing through shared references.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (maps and key-value data); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain maps and key-value data using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 4.5: Collection traversal

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain collection traversal using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
<<<<<<< HEAD
=======
`for key, value := range m` visits a map, but **Go randomizes the iteration order on purpose**, so output printed straight from a map can differ between runs. For stable output, collect the keys into a slice, sort it, and then visit the keys in order. Printing a map with `fmt` is the exception: it prints keys in sorted order.
### Worked Example

**Example 4.5.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.5.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.5.3**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.5.4**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
<<<<<<< HEAD
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
=======
}
```

**Example 4.5.5**
>>>>>>> 2067a20 (curriculum clearning and updates)
```go
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates collection traversal with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======

### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
[82 91 76 88]
```

Example 2:
```text
ascending: [76 82 88 91]
descending: [91 88 82 76]
```

Example 3:
```text
Avery age 16 score 82
```

Example 4:
```text
Notebook stock: 3
```

Example 5:
```text
Passing: [82 91 88]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

### Common Mistakes
1. Assuming append always mutates the original backing array in place.
2. Relying on map iteration order.
3. Mutating a map or slice while overlooking aliasing through shared references.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (collection traversal); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain collection traversal using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
