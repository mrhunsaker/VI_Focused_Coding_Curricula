[Header 2 ("unit-1-foundations-of-computing", [], []) [Str "Unit 1: Foundations of Computing"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops foundations of computing using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction."], Header 3 ("lesson-11-computer-science-and-problem-solving", ["unnumbered", "unlisted"], []) [Str "Lesson 1.1: Computer science and problem solving"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain computer science and problem solving using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "fmt.Println(\"A program is a precise set of instructions.\")", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "name := \"Avery\"", SoftBreak, Str "fmt.Println(\"Hello,\", name)", SoftBreak, Str "fmt.Println(\"This line runs second.\")", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "var age int = 16", SoftBreak, Str "height := 1.72", SoftBreak, Str "active := true", SoftBreak, Str "fmt.Printf(\"age=%d height=%.2f active=%t\\n\", age, height, active)", SoftBreak, Str "} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	fmt.Println(\"A program is a precise set of instructions.\")
}
", Para [Strong [Str "Example 1.1.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	name := \"Avery\"
	fmt.Println(\"Hello,\", name)
	fmt.Println(\"This line runs second.\")
}
", Para [Strong [Str "Example 1.1.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf(\"age=%d height=%.2f active=%t\\n\", age, height, active)
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "A program is a precise set of instructions.
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Hello, Avery
This line runs second.
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "age=16 height=1.72 active=true
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Treating a computer as if it inferred unstated requirements."]], [Plain [Str "Omitting package main or the required main entry point in an executable."]], [Plain [Str "Using a variable without declaring it or misunderstanding inferred types."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (computer science and problem solving); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain computer science and problem solving using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-12-your-first-go-program-and-packages", ["unnumbered", "unlisted"], []) [Str "Lesson 1.2: Your first Go program and packages"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain your first go program and packages using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Every Go executable lives in ", Code ("", [], []) "package main", Str " and starts at ", Code ("", [], []) "func main()", Str ". The ", Code ("", [], []) "import", Str " block names the packages the file uses, and an unused import is a compile error. ", Code ("", [], []) "fmt.Println", Str " writes its arguments separated by spaces and ends with a new line; ", Code ("", [], []) "gofmt", Str " formats the file so every Go program looks the same."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 1.2.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	fmt.Println(\"A program is a precise set of instructions.\")
},package main
import (
	\"fmt\"
)
func main() {
	name := \"Avery\"
	fmt.Println(\"Hello,\", name)
	fmt.Println(\"This line runs second.\")
},package main
import (
	\"fmt\"
)
func main() {
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf(\"age=%d height=%.2f active=%t\\n\", age, height, active)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	name := \"Avery\"
	fmt.Println(\"Hello,\", name)
	fmt.Println(\"This line runs second.\")
}
", Para [Strong [Str "Example 1.2.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf(\"age=%d height=%.2f active=%t\\n\", age, height, active)
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "A program is a precise set of instructions.
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Hello, Avery
This line runs second.
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "age=16 height=1.72 active=true
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Treating a computer as if it inferred unstated requirements."]], [Plain [Str "Omitting package main or the required main entry point in an executable."]], [Plain [Str "Using a variable without declaring it or misunderstanding inferred types."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (your first go program and packages); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain your first go program and packages using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-13-variables-constants-and-primitive-types", ["unnumbered", "unlisted"], []) [Str "Lesson 1.3: Variables, constants, and primitive types"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain variables, constants, and primitive types using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Go is statically typed: every variable has a type fixed at compile time. ", Code ("", [], []) "var age int = 16", Str " declares the type explicitly, while ", Code ("", [], []) "height := 1.72", Str " declares and infers ", Code ("", [], []) "float64", Str " inside a function. Constants use ", Code ("", [], []) "const", Str ", and an unassigned variable holds its type's zero value (0, \"\", false) rather than an undefined value."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 1.3.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	fmt.Println(\"A program is a precise set of instructions.\")
}
", Para [Strong [Str "Example 1.3.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	name := \"Avery\"
	fmt.Println(\"Hello,\", name)
	fmt.Println(\"This line runs second.\")
},package main
import (
	\"fmt\"
)
func main() {
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf(\"age=%d height=%.2f active=%t\\n\", age, height, active)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf(\"age=%d height=%.2f active=%t\\n\", age, height, active)
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "A program is a precise set of instructions.
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Hello, Avery
This line runs second.
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "age=16 height=1.72 active=true
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Treating a computer as if it inferred unstated requirements."]], [Plain [Str "Omitting package main or the required main entry point in an executable."]], [Plain [Str "Using a variable without declaring it or misunderstanding inferred types."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (variables, constants, and primitive types); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain variables, constants, and primitive types using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]]]