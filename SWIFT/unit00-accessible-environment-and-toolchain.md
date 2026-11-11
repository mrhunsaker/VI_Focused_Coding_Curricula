# Unit 0: Accessible Environment and Toolchain

## Course overview

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

## Course Overview

Swift is used for iOS, macOS, watchOS, tvOS, server applications, and systems components. Its static type system, optionals, value semantics, protocols, structured error handling, Codable, and concurrency support robust application development. This course follows the Python curriculum's unit sequence and shared problem contexts while teaching Swift-native design.

**Version baseline:** Swift 6 language mode and a current Swift 6 toolchain. Verify with `swift --version`. Run a single file with `swift main.swift`; use Swift Package Manager for multi-file projects and dependencies.

## Unit 0: Accessible Environment and Toolchain

### Overview

Install and verify the Swift toolchain, create a predictable workspace, configure an accessible editor, and understand Swift Package Manager. On macOS, Xcode provides the integrated toolchain and simulator; supported Linux and Windows distributions can use the Swift toolchain for command-line development. iOS application development requires macOS and Xcode.

### Lesson 0.1: Install and Verify Swift

#### Reading References
- [Swift.org downloads](https://www.swift.org/install/)
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/)

#### Learning Objectives
- Install Swift 6 or Xcode with the Swift 6 toolchain.
- Verify compiler and interpreter availability.
- Distinguish the Swift REPL, script execution, and compilation.

#### Concept Explanation
On macOS, install Xcode or the official Swift toolchain. On supported Linux or Windows systems, follow the official Swift installation instructions for the platform. Open a new terminal and run `swift --version` and `swiftc --version`. Run a source file with `swift main.swift`; compile an executable with `swiftc main.swift -o main` and run it with `./main`. Xcode is required for Apple-platform SDKs and iOS simulators.

#### Worked Example
```swift
print("Swift toolchain is available.")
print("Run swift --version to inspect the installed version.")
```

#### Expected Behavior or Output
The program prints two lines confirming that the source file executes. The terminal version command reports the installed compiler version.

#### Common Mistakes
- Using a terminal session whose PATH has not refreshed after installation.
- Assuming the Swift REPL, script interpreter, compiler, and Xcode are interchangeable tools.
- Expecting iOS simulator tooling on a non-macOS host.

#### Activities
1. Install Swift or Xcode using the official platform instructions.
2. Record the output of `swift --version` and `swiftc --version`.
3. Run the worked example as a script and compile it as an executable.
4. Deliberately use an incorrect filename and read the compiler or runtime diagnostic.

#### Accessibility Practice
Navigate the installer and terminal by keyboard. Confirm that prompts, compiler messages, punctuation, and build output are announced by the learner's screen reader or braille display.

#### Skills Checklist
- [ ] I can install and identify a supported Swift toolchain.
- [ ] I can report the installed Swift version.
- [ ] I can run a Swift script from the terminal.
- [ ] I can compile and execute a standalone Swift program.
- [ ] I can read terminal output and diagnostics using my access technology.

### Lesson 0.2: Workspace and First Run

#### Reading References
- [Swift command-line usage](https://www.swift.org/documentation/)
- [Swift Package Manager](https://www.swift.org/documentation/package-manager/)

#### Learning Objectives
- Create and identify a project root and Swift source file.
- Distinguish source files from generated build artifacts.
- Explain how the process working directory affects relative file paths.

#### Concept Explanation
Create a course directory and save `main.swift` in its root. Use `pwd` in the terminal to confirm the current directory. Swift resolves relative file paths from the process working directory, not automatically from the source file's directory. Keep source, test, data, and generated files in predictable locations. Package builds create a `.build` directory.

#### Worked Example
```swift
import Foundation
print("Project: Swift course workspace")
print("Working directory: \(FileManager.default.currentDirectoryPath)")
```

#### Expected Behavior or Output
The program prints a project label and the absolute path of the directory from which it is running.

#### Common Mistakes
- Opening a parent directory instead of the intended project root.
- Assuming relative file paths are based on the source file's location.
- Editing or deleting generated files under `.build` instead of source files.

#### Activities
1. Create the project directory and verify it with `pwd`.
2. Save and run `main.swift` from the project root.
3. Change to a different working directory and observe how a relative path resolves.
4. Create a Swift package and identify its source and build directories.

#### Accessibility Practice
Use terminal history and directory commands without drag-and-drop. Verify that editor file navigation, indentation, build output, and diagnostics are exposed in a linear reading order.

#### Skills Checklist
- [ ] I can identify the project root and current working directory.
- [ ] I can create and run `main.swift`.
- [ ] I can explain how relative paths are resolved.
- [ ] I can distinguish source files from generated build artifacts.
- [ ] I can navigate the workspace without mouse-only actions.

### Lesson 0.3: Editor and Accessibility Workflow

#### Reading References
- [Swift tools and editors](https://www.swift.org/documentation/)
- [Shared IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md)

#### Learning Objectives
- Configure VS Code, VSCodium, Theia, or Xcode for Swift development.
- Navigate source, diagnostics, terminal, and project files by keyboard.
- Verify that editor language tooling uses the intended Swift toolchain.

#### Concept Explanation
Open the project root in the chosen editor and install compatible Swift language support. On macOS, Xcode provides integrated Swift editing and debugging. In VS Code or VSCodium, configure the Swift extension and sourcekit-lsp using the selected toolchain; extension availability differs across marketplaces. Theia may require a compatible extension distribution. Verify diagnostics and symbol navigation rather than relying on syntax coloring alone.

#### Worked Example
```swift
func greet(_ name: String) -> String {
    return "Hello, \(name)!"
}
print(greet("Avery"))
```

#### Expected Behavior or Output
The program prints `Hello, Avery!`. The editor should identify the function and its parameter type.

#### Common Mistakes
- Selecting a different Swift toolchain in the editor than in the terminal.
- Treating syntax coloring as proof that SourceKit-LSP diagnostics work.
- Depending on mouse-only navigation or inaccessible inline diagnostic panels.

#### Activities
1. Open the course project root in the selected editor.
2. Navigate the worked example by line, word, and character.
3. Introduce a type error, locate the diagnostic, and correct it.
4. Run the file from the integrated terminal and system terminal.

#### Accessibility Practice
Test punctuation verbosity, indentation announcements, completion popups, diagnostic navigation, terminal focus, and editor panels with the learner's access technology. Keep a terminal-first workflow available.

#### Skills Checklist
- [ ] I can open the project root and select the intended Swift toolchain.
- [ ] I can navigate and edit Swift source by keyboard.
- [ ] I can locate and correct a compiler or language-server diagnostic.
- [ ] I can run source code without mouse-dependent actions.
- [ ] I can describe editor accessibility limitations and use a workable alternative.

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

#### Reading References
- [Swift Package Manager](https://www.swift.org/documentation/package-manager/)
- [PackageDescription API](https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html)

#### Learning Objectives
- Create and inspect a Swift package.
- Explain the roles of `Package.swift`, source targets, and test targets.
- Add and resolve dependencies with Swift Package Manager.
- Build, test, and run a package from the terminal.

#### Concept Explanation
Use Swift Package Manager for multi-file applications and dependencies. Run `swift package init --type executable` from the project root. The package manifest `Package.swift` declares products, targets, and dependencies. Run `swift package resolve`, `swift build`, `swift test`, and `swift run`. Package artifacts are generated under `.build`; do not edit them directly. For Apple platform applications, Xcode projects and platform SDK configuration may also be required.

#### Worked Example
```swift
let manifestResponsibilities = ["package name", "products", "targets", "dependencies"]
print("Package.swift declares: \(manifestResponsibilities.joined(separator: ", "))")
```

#### Expected Behavior or Output
This manifest declares an executable package target named `CourseDemo`. Swift Package Manager uses it to determine how to build the package.

#### Common Mistakes
- Running package commands from a directory that does not contain `Package.swift`.
- Editing generated files in `.build` instead of the package sources or manifest.
- Adding a dependency without declaring the product in the appropriate target.

#### Activities
1. Initialize an executable package and inspect its directory structure.
2. Run `swift build` and `swift run`.
3. Add a test target and run `swift test`.
4. Add a small external dependency in a practice package and inspect the manifest and resolved package graph.

#### Accessibility Practice
Read `Package.swift` as source text and inspect build/test output sequentially. Document commands and error messages; do not rely on transient editor notifications or mouse-only build controls.

#### Skills Checklist
- [ ] I can initialize a Swift package.
- [ ] I can explain the purpose of `Package.swift` and its targets.
- [ ] I can resolve declared package dependencies.
- [ ] I can build, run, and test from the terminal.
- [ ] I can inspect package output using keyboard-accessible tools.
