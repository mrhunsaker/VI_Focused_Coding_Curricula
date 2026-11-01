# Kotlin Standardization Audit

## Structural result

- Units covered: 0–11.
- Mapped lesson sections: 57.
- Standard lesson sections: Reading References; Learning Objectives; Concept Explanation; Worked Example; Expected Behavior or Output; Common Mistakes; Activities; Accessibility Practice; Skills Checklist.
- Core unit files: four.
- Kotlin-specific topics: JVM toolchain, static typing and inference, null safety, numeric conversions, data classes, read-only/mutable collections, functions, inheritance defaults, resource cleanup, Java interoperability, and terminal-first accessibility.

## Alignment

The course preserves the shared unit order and lesson topic map. The capstone retains the shared record fields and operations. Kotlin-specific substitutions are documented where Python concepts have no direct Kotlin equivalent: named data classes replace general-purpose tuple usage; Kotlin/JVM terminal interaction is the default alternative to the Python NiceGUI presentation layer; maintained libraries are required for general JSON and CSV parsing.

## Verification status

**Status: Structural draft**

The lesson structure and links are prepared, but this is not a claim of full instructional or runtime verification.

Pending before marking the track fully complete:

1. Replace the repeated unit-level worked-example scaffold with a distinct, lesson-specific Kotlin example and exact expected output for every mapped lesson.
2. Compile and execute every Kotlin example with the pinned Kotlin compiler and supported JDK; add expected-output assertions.
3. Verify Gradle/JUnit or kotlin.test setup and representative invalid-input, null, boundary, file, JSON, and CSV cases.
4. Run the text adventure and CLI to-do applications end to end.
5. Run capstone CRUD and JSON persistence tests, including at least five automated tests.
6. Run a fresh mdBook build and complete repository Markdown/local-link crawl.
7. Perform hands-on keyboard-only, screen-reader, and braille verification with named operating systems, editors, and access technologies.

## Important limitations

The worked-example blocks are currently repeated by unit as structural exemplars. They must be specialized before teaching each lesson. This audit intentionally records that limitation rather than treating section counts as proof of pedagogical completeness.
