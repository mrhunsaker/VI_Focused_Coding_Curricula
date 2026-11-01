# Kotlin Standardization Audit

## Structural and example result

- Units covered: 0–11.
- Mapped lesson sections: 57 (4 setup lessons and 53 numbered lessons).
- All 57 worked examples are distinct and are stored as standalone Kotlin/JVM programs.
- Every lesson retains the nine required instructional sections.
- Exact expected standard output is stored in `examples_expected.json`.
- The Python checker compiles all 57 examples in one package-isolated Kotlin compiler invocation, executes each main function independently, and compares stdout exactly with its expected fixture.
- Toolchain for automated validation: Kotlin 1.9.24 and JDK 21.

## Language and course alignment

The course preserves the shared unit order and lesson topic map. The capstone retains the shared record schema and CRUD requirements. Kotlin-specific substitutions are documented: named data classes replace general-purpose tuple syntax; a Kotlin/JVM terminal interface is the default accessible alternative to the Python NiceGUI presentation layer; maintained libraries are required for general JSON and CSV parsing.

## Automated verification

The GitHub Actions workflow `.github/workflows/kotlin-curriculum.yml` performs:

1. Lesson structure and local-link checks.
2. Independent compilation of all 57 Kotlin examples.
3. Execution of all 57 examples.
4. Exact stdout comparison against the 57 expected-output fixtures.

Run results are recorded in `lesson_standardization.json` and the branch's Actions history.

## Remaining verification

The following work remains separate from the isolated lesson-example checks:

1. Verify Gradle/JUnit or kotlin.test setup in a complete project and exercise representative invalid-input, null, boundary, file, JSON, and CSV integration cases.
2. Run the text adventure and CLI to-do applications end to end.
3. Run capstone CRUD and JSON persistence integration tests, including at least five automated tests.
4. Run a fresh mdBook build and complete repository Markdown/local-link crawl.
5. Perform hands-on keyboard-only, screen-reader, and braille verification with named operating systems, editors, and access technologies.

## Important limitations

Passing isolated examples does not establish that a complete student project meets its requirements. The JSON lesson's short code sample illustrates a constrained JSON shape; production serialization must use a maintained serializer. The CSV example deliberately demonstrates only a simple unquoted row; general CSV input requires a standards-compliant parser. Hands-on accessibility claims are intentionally withheld until those tests are performed.
