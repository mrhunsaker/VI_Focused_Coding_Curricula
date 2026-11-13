# Swift Curriculum Validation

## Validation purpose

This page records the checks that should be performed before describing the Swift examples as validated. Compilation, execution, expected-output comparison, application behavior, and accessibility testing are separate evidence categories.

## Automated checks

The repository should use a Swift example checker and a GitHub Actions workflow to compile and execute the fenced Swift examples. Before recording a new pass, inspect the current checker and workflow to confirm which files, code fences, and lesson examples they cover.

A validation report should record:

- Swift compiler version and Swift language mode.
- Operating system and architecture.
- Exact validation command and repository commit.
- Number of examples parsed, compiled, and executed.
- Whether expected output was compared automatically.
- Any examples excluded from automated validation and the reason.

## Verification boundaries

A successful compiler run establishes that the checked source is accepted by that compiler under the stated language mode. A successful process exit does not establish correct output or complete application behavior. Expected-output comparisons do not establish accessibility.

The following require separate evidence:

- Exact-output or assertion-based behavioral tests.
- File persistence and round-trip tests.
- Invalid-input and error-path tests.
- Package and dependency reproducibility.
- Cross-platform behavior.
- Keyboard, screen-reader, and braille workflows.

## Accessibility validation

Record the operating system, Swift toolchain, editor or IDE, screen reader, braille display if applicable, and the workflows actually exercised. Test navigation, source editing, punctuation, diagnostics, build output, test results, and debugging. Do not infer accessibility from the use of a particular IDE or from vendor documentation.

## Current record

This page is a validation template and scope statement. It does not assert a new Swift compile, runtime, expected-output, or assistive-technology test. Update it with reproducible evidence when those checks have been run.
