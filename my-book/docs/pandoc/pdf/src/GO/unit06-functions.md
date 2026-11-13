[Header 2 ("unit-6-functions", [], []) [Str "Unit 6: Functions"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops functions using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction."], Header 3 ("lesson-61-defining-and-calling-functions", ["unnumbered", "unlisted"], []) [Str "Lesson 6.1: Defining and calling functions"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain defining and calling functions using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "greet := func(name string) { fmt.Println(\"Hello,\", name) }", SoftBreak, Str "greet(\"Avery\")", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "describe := func(name string, score int) { fmt.Printf(\"%s scored %d.\\n\", name, score) }", SoftBreak, Str "name := \"Avery\"", SoftBreak, Str "describe(name, 82)", SoftBreak, Str "fmt.Println(\"still available:\", name)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "grade := func(score int) string { if score >= 60 { return \"pass\" }; return \"retry\" }", SoftBreak, Str "fmt.Println(grade(82))", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }", SoftBreak, Str "scores := []int{82, 91, 76, 88}", SoftBreak, Str "fmt.Printf(\"average=%.1f\\n\", average(scores))", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }", SoftBreak, Str "fmt.Println(\"sum:\", sum(82, 91, 76, 88))", SoftBreak, Str "} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	greet := func(name string) { fmt.Println(\"Hello,\", name) }
	greet(\"Avery\")
}
", Para [Strong [Str "Example 6.1.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	describe := func(name string, score int) { fmt.Printf(\"%s scored %d.\\n\", name, score) }
	name := \"Avery\"
	describe(name, 82)
	fmt.Println(\"still available:\", name)
}
", Para [Strong [Str "Example 6.1.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	grade := func(score int) string { if score >= 60 { return \"pass\" }; return \"retry\" }
	fmt.Println(grade(82))
}
", Para [Strong [Str "Example 6.1.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"average=%.1f\\n\", average(scores))
}
", Para [Strong [Str "Example 6.1.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println(\"sum:\", sum(82, 91, 76, 88))
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Hello, Avery
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Avery scored 82.
still available: Avery
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "pass
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "average=84.2
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "sum: 337
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Expecting a function to return a value when its signature does not."]], [Plain [Str "Ignoring an error return value."]], [Plain [Str "Confusing variadic arguments with a slice argument; use ... to expand a slice."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (defining and calling functions); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain defining and calling functions using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-62-parameters-and-multiple-return-values", ["unnumbered", "unlisted"], []) [Str "Lesson 6.2: Parameters and multiple return values"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain parameters and multiple return values using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Go has no default arguments or keyword arguments. Pass every argument in order, or use a struct as an options value when a call needs many named settings. A function can return several results, written ", Code ("", [], []) "func f() (int, error)", Str ", and the caller receives them with ", Code ("", [], []) "a, b := f()", Str "."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 6.2.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	greet := func(name string) { fmt.Println(\"Hello,\", name) }
	greet(\"Avery\")
},package main
import (
	\"fmt\"
)
func main() {
	describe := func(name string, score int) { fmt.Printf(\"%s scored %d.\\n\", name, score) }
	name := \"Avery\"
	describe(name, 82)
	fmt.Println(\"still available:\", name)
},package main
import (
	\"fmt\"
)
func main() {
	grade := func(score int) string { if score >= 60 { return \"pass\" }; return \"retry\" }
	fmt.Println(grade(82))
},package main
import (
	\"fmt\"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"average=%.1f\\n\", average(scores))
},package main
import (
	\"fmt\"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println(\"sum:\", sum(82, 91, 76, 88))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	describe := func(name string, score int) { fmt.Printf(\"%s scored %d.\\n\", name, score) }
	name := \"Avery\"
	describe(name, 82)
	fmt.Println(\"still available:\", name)
}
", Para [Strong [Str "Example 6.2.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	grade := func(score int) string { if score >= 60 { return \"pass\" }; return \"retry\" }
	fmt.Println(grade(82))
}
", Para [Strong [Str "Example 6.2.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"average=%.1f\\n\", average(scores))
}
", Para [Strong [Str "Example 6.2.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println(\"sum:\", sum(82, 91, 76, 88))
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Hello, Avery
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Avery scored 82.
still available: Avery
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "pass
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "average=84.2
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "sum: 337
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Expecting a function to return a value when its signature does not."]], [Plain [Str "Ignoring an error return value."]], [Plain [Str "Confusing variadic arguments with a slice argument; use ... to expand a slice."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (parameters and multiple return values); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain parameters and multiple return values using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-63-return-values-and-errors", ["unnumbered", "unlisted"], []) [Str "Lesson 6.3: Return values and errors"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain return values and errors using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A function sends a result back with ", Code ("", [], []) "return", Str ". By convention, a function that can fail returns its result and an ", Code ("", [], []) "error", Str " as the last value, and the caller checks ", Code ("", [], []) "if err != nil", Str ". Create errors with ", Code ("", [], []) "errors.New", Str " or ", Code ("", [], []) "fmt.Errorf", Str ", and never ignore a returned error silently."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 6.3.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	greet := func(name string) { fmt.Println(\"Hello,\", name) }
	greet(\"Avery\")
}
", Para [Strong [Str "Example 6.3.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	describe := func(name string, score int) { fmt.Printf(\"%s scored %d.\\n\", name, score) }
	name := \"Avery\"
	describe(name, 82)
	fmt.Println(\"still available:\", name)
},package main
import (
	\"fmt\"
)
func main() {
	grade := func(score int) string { if score >= 60 { return \"pass\" }; return \"retry\" }
	fmt.Println(grade(82))
},package main
import (
	\"fmt\"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"average=%.1f\\n\", average(scores))
},package main
import (
	\"fmt\"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println(\"sum:\", sum(82, 91, 76, 88))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	grade := func(score int) string { if score >= 60 { return \"pass\" }; return \"retry\" }
	fmt.Println(grade(82))
}
", Para [Strong [Str "Example 6.3.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"average=%.1f\\n\", average(scores))
}
", Para [Strong [Str "Example 6.3.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println(\"sum:\", sum(82, 91, 76, 88))
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Hello, Avery
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Avery scored 82.
still available: Avery
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "pass
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "average=84.2
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "sum: 337
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Expecting a function to return a value when its signature does not."]], [Plain [Str "Ignoring an error return value."]], [Plain [Str "Confusing variadic arguments with a slice argument; use ... to expand a slice."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (return values and errors); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain return values and errors using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-64-functions-over-slices-and-maps", ["unnumbered", "unlisted"], []) [Str "Lesson 6.4: Functions over slices and maps"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain functions over slices and maps using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A slice passed to a function shares its elements with the caller, so changing an element inside the function changes the caller's slice; appending may not be visible to the caller unless the slice is returned. A map is passed by reference and can be changed in place. To protect the caller's data, copy a slice before changing it."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 6.4.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	greet := func(name string) { fmt.Println(\"Hello,\", name) }
	greet(\"Avery\")
}
", Para [Strong [Str "Example 6.4.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	describe := func(name string, score int) { fmt.Printf(\"%s scored %d.\\n\", name, score) }
	name := \"Avery\"
	describe(name, 82)
	fmt.Println(\"still available:\", name)
}
", Para [Strong [Str "Example 6.4.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	grade := func(score int) string { if score >= 60 { return \"pass\" }; return \"retry\" }
	fmt.Println(grade(82))
},package main
import (
	\"fmt\"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"average=%.1f\\n\", average(scores))
},package main
import (
	\"fmt\"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println(\"sum:\", sum(82, 91, 76, 88))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"average=%.1f\\n\", average(scores))
}
", Para [Strong [Str "Example 6.4.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println(\"sum:\", sum(82, 91, 76, 88))
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Hello, Avery
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Avery scored 82.
still available: Avery
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "pass
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "average=84.2
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "sum: 337
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Expecting a function to return a value when its signature does not."]], [Plain [Str "Ignoring an error return value."]], [Plain [Str "Confusing variadic arguments with a slice argument; use ... to expand a slice."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (functions over slices and maps); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain functions over slices and maps using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-65-variadic-parameters-and-scope", ["unnumbered", "unlisted"], []) [Str "Lesson 6.5: Variadic parameters and scope"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain variadic parameters and scope using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A final parameter written ", Code ("", [], []) "...int", Str " accepts any number of arguments and arrives in the function as a slice. Pass an existing slice with ", Code ("", [], []) "values...", Str ". Variables declared inside a function or block are local to it, and an inner variable with the same name shadows an outer one, which hides the outer value inside that block."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 6.5.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	greet := func(name string) { fmt.Println(\"Hello,\", name) }
	greet(\"Avery\")
}
", Para [Strong [Str "Example 6.5.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	describe := func(name string, score int) { fmt.Printf(\"%s scored %d.\\n\", name, score) }
	name := \"Avery\"
	describe(name, 82)
	fmt.Println(\"still available:\", name)
}
", Para [Strong [Str "Example 6.5.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	grade := func(score int) string { if score >= 60 { return \"pass\" }; return \"retry\" }
	fmt.Println(grade(82))
}
", Para [Strong [Str "Example 6.5.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"average=%.1f\\n\", average(scores))
},package main
import (
	\"fmt\"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println(\"sum:\", sum(82, 91, 76, 88))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println(\"sum:\", sum(82, 91, 76, 88))
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Hello, Avery
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Avery scored 82.
still available: Avery
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "pass
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "average=84.2
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "sum: 337
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Expecting a function to return a value when its signature does not."]], [Plain [Str "Ignoring an error return value."]], [Plain [Str "Confusing variadic arguments with a slice argument; use ... to expand a slice."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (variadic parameters and scope); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain variadic parameters and scope using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]]]