# Kotlin Teacher Guide

## Course alignment

Teach Units 0–11 in the shared sequence. The four unit files contain 57 lesson sections and use the common nine-part lesson structure. The standalone reference in `lessons.md` is supplementary, not a replacement for the mapped sequence.

## Language-specific instructional priorities

- Teach `val` and `var` early. Explain that inference is compile-time type inference, not dynamic typing.
- Explicitly teach numeric conversions; Kotlin does not silently widen numeric types.
- Introduce nullable types (`String?`), safe calls (`?.`), Elvis fallback (`?:`), and the risk of `!!`. Require runtime validation at file, network, user-input, and Java-interoperability boundaries.
- Explain that Kotlin does not have general-purpose tuple syntax. Prefer named data classes for domain records; introduce Pair/Triple only when suitable.
- Distinguish `List` from `MutableList`, and `Map` from `MutableMap`. A read-only interface does not imply deep immutability.
- Explain that classes are final by default. Use `open` deliberately; compare inheritance, interfaces, and composition.
- Use `use` for resource cleanup. Use maintained JSON and CSV libraries rather than ad hoc parsers.
- Treat Kotlin/JVM and Java interoperability as an advantage, but explicitly discuss platform types and Java API nullability.

## Accessible instruction

Use keyboard-first workflows and verify the chosen editor/language server with the student's actual screen reader. Do not assume that a VS Code extension, Theia extension, Gradle task view, or debugger is accessible because the editor itself is accessible. Teach terminal compile/run/test commands and how to read compiler diagnostics. Configure punctuation and indentation announcements; explain Kotlin operators verbally. Use short functions, descriptive identifiers, and named intermediate values. The capstone may use a text-first terminal interface; students are not required to inspect a GUI visually.

## Shared data and assessment

Preserve the canonical Avery profile, $24.50 bill with 15% tip, grade thresholds, scores 82/91/76/88, inventory records, coordinates (3,4), text sample, CSV columns, task fields, and capstone fields. Keep the text adventure, torch/magic-key puzzle, and CLI to-do requirements aligned with the other language tracks.

Assess independent explanation, tracing, boundary testing, validation, persistence, and accessible operation. A passing compiler build is not sufficient evidence of correctness.

## AI-use policy

AI tools may be used for conceptual understanding and reinforcement only. They must not generate, complete, repair, refactor, or write course code or assessment solutions for students or instructors. Instructors should use AI only to clarify concepts and reinforce understanding, not to create solutions or code artifacts for course work.
