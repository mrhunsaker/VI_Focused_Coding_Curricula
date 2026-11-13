[Header 2 ("unit-2-numeric-computations", [], []) [Str "Unit 2: Numeric Computations"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops numeric computations using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction."], Header 3 ("lesson-21-software-design-and-tracing", ["unnumbered", "unlisted"], []) [Str "Lesson 2.1: Software design and tracing"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain software design and tracing using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "bill := 24.50", SoftBreak, Str "rate := 0.15", SoftBreak, Str "tip := bill * rate", SoftBreak, Str "fmt.Printf(\"Tip: %.2f; total: %.2f\\n\", tip, bill+tip)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "subtotal := 24.50", SoftBreak, Str "taxRate := 0.075", SoftBreak, Str "tax := subtotal * taxRate", SoftBreak, Str "fmt.Printf(\"Subtotal %.2f, tax %.2f, total %.2f\\n\", subtotal, tax, subtotal+tax)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"bufio\"", SoftBreak, Str "\"fmt\"", SoftBreak, Str "\"os\"", SoftBreak, Str "\"strconv\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "reader := bufio.NewReader(os.Stdin)", SoftBreak, Str "fmt.Print(\"Enter a score: \")", SoftBreak, Str "text, _ := reader.ReadString('\\n')", SoftBreak, Str "score, err := strconv.Atoi(text)", SoftBreak, Str "if err != nil { fmt.Println(\"Enter a whole number.\") } else { fmt.Println(\"Score:\", score) }", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str "\"math\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "radius := 3.0", SoftBreak, Str "area := math.Pi * math.Pow(radius, 2)", SoftBreak, Str "circumference := 2 * math.Pi * radius", SoftBreak, Str "fmt.Printf(\"area=%.2f circumference=%.2f\\n\", area, circumference)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str "\"math\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "distance := math.Hypot(3, 4)", SoftBreak, Str "fmt.Println(\"Distance from origin:\", distance)", SoftBreak, Str "} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf(\"Tip: %.2f; total: %.2f\\n\", tip, bill+tip)
}
", Para [Strong [Str "Example 2.1.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf(\"Subtotal %.2f, tax %.2f, total %.2f\\n\", subtotal, tax, subtotal+tax)
}
", Para [Strong [Str "Example 2.1.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"bufio\"
	\"fmt\"
	\"os\"
	\"strconv\"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(\"Enter a score: \")
	text, _ := reader.ReadString('\\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println(\"Enter a whole number.\") } else { fmt.Println(\"Score:\", score) }
}
", Para [Strong [Str "Example 2.1.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf(\"area=%.2f circumference=%.2f\\n\", area, circumference)
}
", Para [Strong [Str "Example 2.1.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println(\"Distance from origin:\", distance)
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Tip: 3.67; total: 28.18
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Subtotal 24.50, tax 1.84, total 26.34
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "Enter a score: Enter a whole number.
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "area=28.27 circumference=18.85
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "Distance from origin: 5
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Confusing := declaration with = assignment."]], [Plain [Str "Ignoring errors returned by fmt.Fscan or strconv parsing."]], [Plain [Str "Mixing int and float64 without explicit conversion."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (software design and tracing); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain software design and tracing using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-22-expressions-operators-and-assignment", ["unnumbered", "unlisted"], []) [Str "Lesson 2.2: Expressions, operators, and assignment"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain expressions, operators, and assignment using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "An expression produces a value. Go's arithmetic operators are ", Code ("", [], []) "+", Str ", ", Code ("", [], []) "-", Str ", ", Code ("", [], []) "*", Str ", ", Code ("", [], []) "/", Str ", and ", Code ("", [], []) "%", Str "; dividing two integers truncates toward zero, so ", Code ("", [], []) "7 / 2", Str " is ", Code ("", [], []) "3", Str ". Go has no implicit numeric conversion, so an ", Code ("", [], []) "int", Str " and a ", Code ("", [], []) "float64", Str " cannot be mixed until one is converted. Assignment stores a result, and ", Code ("", [], []) "+=", Str " updates a variable in place."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 2.2.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf(\"Tip: %.2f; total: %.2f\\n\", tip, bill+tip)
},package main
import (
	\"fmt\"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf(\"Subtotal %.2f, tax %.2f, total %.2f\\n\", subtotal, tax, subtotal+tax)
},package main
import (
	\"bufio\"
	\"fmt\"
	\"os\"
	\"strconv\"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(\"Enter a score: \")
	text, _ := reader.ReadString('\\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println(\"Enter a whole number.\") } else { fmt.Println(\"Score:\", score) }
},package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf(\"area=%.2f circumference=%.2f\\n\", area, circumference)
},package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println(\"Distance from origin:\", distance)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf(\"Subtotal %.2f, tax %.2f, total %.2f\\n\", subtotal, tax, subtotal+tax)
}
", Para [Strong [Str "Example 2.2.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"bufio\"
	\"fmt\"
	\"os\"
	\"strconv\"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(\"Enter a score: \")
	text, _ := reader.ReadString('\\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println(\"Enter a whole number.\") } else { fmt.Println(\"Score:\", score) }
}
", Para [Strong [Str "Example 2.2.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf(\"area=%.2f circumference=%.2f\\n\", area, circumference)
}
", Para [Strong [Str "Example 2.2.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println(\"Distance from origin:\", distance)
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Tip: 3.67; total: 28.18
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Subtotal 24.50, tax 1.84, total 26.34
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "Enter a score: Enter a whole number.
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "area=28.27 circumference=18.85
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "Distance from origin: 5
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Confusing := declaration with = assignment."]], [Plain [Str "Ignoring errors returned by fmt.Fscan or strconv parsing."]], [Plain [Str "Mixing int and float64 without explicit conversion."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (expressions, operators, and assignment); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain expressions, operators, and assignment using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-23-input-and-output-with-fmt", ["unnumbered", "unlisted"], []) [Str "Lesson 2.3: Input and output with fmt"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain input and output with fmt using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The ", Code ("", [], []) "fmt", Str " package writes with ", Code ("", [], []) "Println", Str " and ", Code ("", [], []) "Printf", Str " and reads with ", Code ("", [], []) "Scanln", Str " or a ", Code ("", [], []) "bufio.Scanner", Str ". Reading returns an error value as well as data, and Go programs check it: at the end of input the error is ", Code ("", [], []) "io.EOF", Str ". Typed text is a string, so a number needs ", Code ("", [], []) "strconv.Atoi", Str " or ", Code ("", [], []) "strconv.ParseFloat", Str ", which also return an error for invalid text."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 2.3.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf(\"Tip: %.2f; total: %.2f\\n\", tip, bill+tip)
}
", Para [Strong [Str "Example 2.3.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf(\"Subtotal %.2f, tax %.2f, total %.2f\\n\", subtotal, tax, subtotal+tax)
},package main
import (
	\"bufio\"
	\"fmt\"
	\"os\"
	\"strconv\"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(\"Enter a score: \")
	text, _ := reader.ReadString('\\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println(\"Enter a whole number.\") } else { fmt.Println(\"Score:\", score) }
},package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf(\"area=%.2f circumference=%.2f\\n\", area, circumference)
},package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println(\"Distance from origin:\", distance)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"bufio\"
	\"fmt\"
	\"os\"
	\"strconv\"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(\"Enter a score: \")
	text, _ := reader.ReadString('\\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println(\"Enter a whole number.\") } else { fmt.Println(\"Score:\", score) }
}
", Para [Strong [Str "Example 2.3.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf(\"area=%.2f circumference=%.2f\\n\", area, circumference)
}
", Para [Strong [Str "Example 2.3.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println(\"Distance from origin:\", distance)
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Tip: 3.67; total: 28.18
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Subtotal 24.50, tax 1.84, total 26.34
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "Enter a score: Enter a whole number.
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "area=28.27 circumference=18.85
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "Distance from origin: 5
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Confusing := declaration with = assignment."]], [Plain [Str "Ignoring errors returned by fmt.Fscan or strconv parsing."]], [Plain [Str "Mixing int and float64 without explicit conversion."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (input and output with fmt); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain input and output with fmt using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-24-numeric-conversions-and-math", ["unnumbered", "unlisted"], []) [Str "Lesson 2.4: Numeric conversions and math"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain numeric conversions and math using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Go converts types explicitly: ", Code ("", [], []) "float64(count)", Str " and ", Code ("", [], []) "int(price)", Str ". Converting a float to an integer discards the fraction and does not round. ", Code ("", [], []) "strconv", Str " converts between text and numbers and reports invalid text through an error. Floating-point values are approximations, which is why ", Code ("", [], []) "0.1 + 0.2", Str " is not exactly ", Code ("", [], []) "0.3", Str "."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 2.4.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf(\"Tip: %.2f; total: %.2f\\n\", tip, bill+tip)
}
", Para [Strong [Str "Example 2.4.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf(\"Subtotal %.2f, tax %.2f, total %.2f\\n\", subtotal, tax, subtotal+tax)
}
", Para [Strong [Str "Example 2.4.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"bufio\"
	\"fmt\"
	\"os\"
	\"strconv\"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(\"Enter a score: \")
	text, _ := reader.ReadString('\\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println(\"Enter a whole number.\") } else { fmt.Println(\"Score:\", score) }
},package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf(\"area=%.2f circumference=%.2f\\n\", area, circumference)
},package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println(\"Distance from origin:\", distance)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf(\"area=%.2f circumference=%.2f\\n\", area, circumference)
}
", Para [Strong [Str "Example 2.4.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println(\"Distance from origin:\", distance)
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Tip: 3.67; total: 28.18
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Subtotal 24.50, tax 1.84, total 26.34
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "Enter a score: Enter a whole number.
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "area=28.27 circumference=18.85
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "Distance from origin: 5
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Confusing := declaration with = assignment."]], [Plain [Str "Ignoring errors returned by fmt.Fscan or strconv parsing."]], [Plain [Str "Mixing int and float64 without explicit conversion."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (numeric conversions and math); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain numeric conversions and math using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-25-mathematical-functions-circle-geometry-and-distance", ["unnumbered", "unlisted"], []) [Str "Lesson 2.5: Mathematical functions, circle geometry, and distance"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain mathematical functions, circle geometry, and distance using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The ", Code ("", [], []) "math", Str " package provides ", Code ("", [], []) "Pi", Str ", ", Code ("", [], []) "Sqrt", Str ", ", Code ("", [], []) "Pow", Str ", ", Code ("", [], []) "Floor", Str ", and ", Code ("", [], []) "Hypot", Str ". Go has a built-in hypotenuse function, so the distance from the origin to (3, 4) is ", Code ("", [], []) "math.Hypot(3, 4)", Str ", which is exactly 5. Every ", Code ("", [], []) "math", Str " function takes and returns ", Code ("", [], []) "float64", Str ", so integers must be converted first."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 2.5.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf(\"Tip: %.2f; total: %.2f\\n\", tip, bill+tip)
}
", Para [Strong [Str "Example 2.5.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf(\"Subtotal %.2f, tax %.2f, total %.2f\\n\", subtotal, tax, subtotal+tax)
}
", Para [Strong [Str "Example 2.5.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"bufio\"
	\"fmt\"
	\"os\"
	\"strconv\"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(\"Enter a score: \")
	text, _ := reader.ReadString('\\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println(\"Enter a whole number.\") } else { fmt.Println(\"Score:\", score) }
}
", Para [Strong [Str "Example 2.5.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf(\"area=%.2f circumference=%.2f\\n\", area, circumference)
},package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println(\"Distance from origin:\", distance)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
	\"math\"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println(\"Distance from origin:\", distance)
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Tip: 3.67; total: 28.18
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Subtotal 24.50, tax 1.84, total 26.34
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "Enter a score: Enter a whole number.
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "area=28.27 circumference=18.85
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "Distance from origin: 5
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Confusing := declaration with = assignment."]], [Plain [Str "Ignoring errors returned by fmt.Fscan or strconv parsing."]], [Plain [Str "Mixing int and float64 without explicit conversion."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (mathematical functions, circle geometry, and distance); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain mathematical functions, circle geometry, and distance using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]]]