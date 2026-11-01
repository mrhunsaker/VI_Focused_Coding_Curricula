# Swift Example Validation

Run the curriculum's standalone example checks from the repository root with Swift 6 available on `PATH`:

```sh
swift --version
python3 scripts/check_swift_examples.py
```

The checker extracts each fenced `swift` block from `SWIFT/lessons.md`, writes it to an isolated temporary directory, and executes it as an independent Swift script. It supplies standard input for the two introductory console-input examples and fails on a nonzero exit status or timeout.

A passing run verifies that all examples compile and execute under the configured toolchain. It does not assert exact output, cover every invalid-input path, test an Xcode/iOS target, or replace package-level XCTest and capstone persistence tests.
