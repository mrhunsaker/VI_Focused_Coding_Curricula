# Unit 0: Accessible Environment and Toolchain

## Course overview

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

## Course Overview

Go is a compiled, statically typed language used for cloud services, network servers, command-line tools, infrastructure, and concurrent systems. This course follows the Python curriculum's shared examples and datasets while teaching Go idioms: packages and modules, explicit types, slices, maps, structs, interfaces, error values, goroutines, channels, and the standard library.

**Toolchain baseline:** current stable Go release. Use the official Go distribution, gofmt, modules, and the go command. The examples are self-contained standard-library programs unless a lesson explicitly names a package.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install Go, create a module, configure editor support, and verify keyboard and screen-reader access.

### Lesson 0.1: Install and Verify Go

### Reading References
- [Go installation](https://go.dev/dl/)
- [A Tour of Go](https://go.dev/tour/)
- [Go command documentation](https://go.dev/doc/cmd)

### Learning Objectives
- Install the official Go toolchain and verify go and gofmt are available.
- Verify the workflow with terminal commands and interpret their output.
- Complete the task using keyboard navigation and accessible diagnostics.

### Concept Explanation
The Go distribution includes the compiler, standard library, go command, and formatter. Confirm that the intended installation appears first on PATH. Avoid mixing system and manually installed copies.

### Worked Example
```sh
go version\ngofmt -h
```

### Expected Behavior or Output

The terminal prints the installed Go version and gofmt usage information.

### Common Mistakes
- Installing Go from an unofficial source or mixing multiple PATH installations.
- Confusing the editor language server with the Go compiler and toolchain.
- Running commands outside the intended module root.

### Activities
1. Follow the commands from a new project directory and record each result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional source error and locate the diagnostic text.
4. Explain which files are source, module metadata, and generated build artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostic navigation, and sequential output reading. Document a keyboard-only route for build, run, and test.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the module root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.
### Lesson 0.2: Modules, Workspace, and First Run

### Reading References
- [Go installation](https://go.dev/dl/)
- [A Tour of Go](https://go.dev/tour/)
- [Go command documentation](https://go.dev/doc/cmd)

### Learning Objectives
- Create a module and run a minimal Go executable.
- Verify the workflow with terminal commands and interpret their output.
- Complete the task using keyboard navigation and accessible diagnostics.

### Concept Explanation
A module is described by go.mod. An executable starts in package main and defines func main(). The command go run . builds and runs the package from its module root.

### Worked Example
```sh
mkdir courseapp\ncd courseapp\ngo mod init example.com/courseapp\nprintf 'package main\\nimport "fmt"\\nfunc main() { fmt.Println("Hello, Go!") }\\n' > main.go\ngo run .
```

### Expected Behavior or Output

Go creates go.mod and runs main.go, printing Hello, Go!.

### Common Mistakes
- Installing Go from an unofficial source or mixing multiple PATH installations.
- Confusing the editor language server with the Go compiler and toolchain.
- Running commands outside the intended module root.

### Activities
1. Follow the commands from a new project directory and record each result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional source error and locate the diagnostic text.
4. Explain which files are source, module metadata, and generated build artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostic navigation, and sequential output reading. Document a keyboard-only route for build, run, and test.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the module root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.
### Lesson 0.3: Editor and Accessibility Workflow

### Reading References
- [Go installation](https://go.dev/dl/)
- [A Tour of Go](https://go.dev/tour/)
- [Go command documentation](https://go.dev/doc/cmd)

### Learning Objectives
- Configure Go editor support and verify accessible source navigation and diagnostics.
- Verify the workflow with terminal commands and interpret their output.
- Complete the task using keyboard navigation and accessible diagnostics.

### Concept Explanation
The Go extension and gopls provide language-aware navigation and diagnostics; they are not substitutes for go, gofmt, or go test. Test the actual screen-reader/editor combination. Keep terminal output and compiler messages available as text.

### Worked Example
```sh
gofmt -w main.go\ngo test ./...\ngo build ./...
```

### Expected Behavior or Output

The source is formatted, tests run (or report that none exist), and the module builds.

### Common Mistakes
- Installing Go from an unofficial source or mixing multiple PATH installations.
- Confusing the editor language server with the Go compiler and toolchain.
- Running commands outside the intended module root.

### Activities
1. Follow the commands from a new project directory and record each result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional source error and locate the diagnostic text.
4. Explain which files are source, module metadata, and generated build artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostic navigation, and sequential output reading. Document a keyboard-only route for build, run, and test.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the module root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.
### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

### Reading References
- [Go installation](https://go.dev/dl/)
- [A Tour of Go](https://go.dev/tour/)
- [Go command documentation](https://go.dev/doc/cmd)

### Learning Objectives
- Manage module dependencies and run build, test, and execution commands from the module root.
- Verify the workflow with terminal commands and interpret their output.
- Complete the task using keyboard navigation and accessible diagnostics.

### Concept Explanation
Go modules record direct requirements in go.mod and checksums in go.sum. Use go get to add a dependency, go mod tidy to reconcile imports and metadata, go test ./... for tests, go build ./... to compile, and go run . to launch the current package. Review third-party dependencies before adding them.

### Worked Example
```sh
go env GOMOD\ngo list ./...\ngo test ./...\ngo build ./...
```

### Expected Behavior or Output

The commands identify the active module, list packages, run tests, and build packages.

### Common Mistakes
- Installing Go from an unofficial source or mixing multiple PATH installations.
- Confusing the editor language server with the Go compiler and toolchain.
- Running commands outside the intended module root.

### Activities
1. Follow the commands from a new project directory and record each result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional source error and locate the diagnostic text.
4. Explain which files are source, module metadata, and generated build artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostic navigation, and sequential output reading. Document a keyboard-only route for build, run, and test.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the module root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.
