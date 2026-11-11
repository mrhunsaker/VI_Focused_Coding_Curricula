# Swift Curriculum

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

Swift is used for iOS, macOS, watchOS, tvOS, server applications, and systems components. Its static type system, optionals, value semantics, protocols, structured error handling, Codable, and concurrency support robust application development.

## Course structure

A complete course aligned to the Python curriculum's Units 0–11, including four environment/toolchain lessons and 53 numbered lessons. The worked examples reuse shared course contexts: Avery's profile, calculator and tip values, grades, scores, inventory, coordinates, text samples, CSV fields, task records, text-adventure requirements, and personal-record management.

## Environment

- Baseline: Swift 6 language mode and a current Swift 6 toolchain.
- Verify with `swift --version` and `swiftc --version`.
- Run a single source file with `swift main.swift`.
- Initialize a package with `swift package init --type executable`; build, run, and test with `swift build`, `swift run`, and `swift test`.
- Xcode and Apple platform SDKs are required for iOS simulator and Apple-platform application development.
- Use Foundation for file operations and Codable JSON encoding. Use a standards-aware CSV library for quoted fields and embedded newlines.

Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md) and [terminal prerequisite](../TERMINAL/TERMINAL_README.md). The course supports keyboard-first work with screen readers, braille displays, magnification, and other access technology.

- [Complete lessons](lessons.md)
- [Topic index](INDEX.md)
- [Example validation instructions](VALIDATION.md)

## GUI, visualization, and workbench accessibility

See the shared [GUI, visualization, and workbench accessibility reference](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) for screen-reader support by toolkit, platform-specific activation settings, recommended alternatives, and interfaces that must not be required without an equivalent accessible route.
## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.

## Recommended introductory books

- Mathias, Matthew, John Gallagher, and Mikey Ward. *Swift Programming: The Big Nerd Ranch Guide*, 3rd edition. Big Nerd Ranch Guides, 2020 (updated e-text edition, 2022). A structured introduction to Swift fundamentals, collections, functions, protocols, error handling, memory management, and application development. [Publisher page](https://www.pearson.com/en-us/subject-catalog/p/swift-programming-the-big-nerd-ranch-guide/P200000000450).
- Apple. *Develop in Swift* learning materials. Apple's free curriculum materials introduce Swift and app development through guided projects. [Apple Education](https://developer.apple.com/education/).

**Suggested use:** use the Big Nerd Ranch guide for language concepts and Apple's materials for platform-specific context. The book predates Swift 6 language mode; follow the curriculum's Swift 6 baseline and current Swift documentation where concurrency or compiler diagnostics differ.
