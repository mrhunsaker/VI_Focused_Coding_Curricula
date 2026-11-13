# Lesson Structure Audit and Editorial Standard

## Purpose

This document defines a repeatable review standard for curriculum lessons. It is intended for authors, reviewers, and instructors who need to determine whether a lesson is instructionally complete, technically responsible, accessible, and consistent with the repository's course design.

An audit records evidence and limitations. The presence of a heading or checklist does not prove that a program compiles, behaves correctly, or works with assistive technology.

## Required lesson components

A complete instructional lesson should include the following components where appropriate:

1. **Title and placement:** a descriptive title and a clear relationship to the unit's learning progression.
2. **Prerequisite knowledge:** concepts or tools the learner is expected to know.
3. **Learning objectives:** observable outcomes using measurable verbs.
4. **Concept explanation:** accurate definitions, rationale, and language-specific behavior.
5. **Worked example:** a complete, appropriately scoped example with imports or dependencies identified.
6. **Expected behavior or output:** a text-based result that lets a learner verify the example.
7. **Common mistakes:** realistic errors, why they occur, and how to recognize or correct them.
8. **Practice activities:** activities that require prediction, modification, debugging, or independent application.
9. **Accessibility practice:** explicit keyboard-first and assistive-technology considerations relevant to the task.
10. **Skills checklist:** observable criteria that align with the objectives.

Not every page needs all ten sections. Reference pages, indexes, and short conceptual notes should use a structure appropriate to their purpose rather than adding empty headings.

## Technical review

Reviewers should assess:

- Language and runtime versions are stated when behavior depends on them.
- Examples use the language's conventional idioms and avoid unexplained dependencies.
- Code fences specify the correct language identifier.
- Shell commands are safe, scoped to a project, and paired across Bash and PowerShell in cross-platform instructional pages.
- Shell-specific prerequisite pages may use only their designated shell, as documented in CODE_STYLE.md.
- Expected output matches the actual example and input.
- File paths, case sensitivity, and platform-specific behavior are explained.
- Error handling and invalid input are addressed when relevant.
- Dependencies are declared at project scope and not installed globally without justification.
- No credentials, private data, or unsafe commands are included.
- Automated validation claims identify exactly what was tested and what remains unverified.

## Accessibility review

The reviewer should be able to complete the core learning activity without depending on visual-only information.

Check for:

- Logical heading hierarchy and descriptive headings.
- Descriptive links and meaningful alternative text for informative images.
- Instructions that do not depend only on color, location, shape, or visual appearance.
- Explicit names for keyboard keys and shortcuts.
- Clear explanation of punctuation, indentation, nested structure, and relevant editor feedback.
- Text equivalents for essential output and diagrams.
- Keyboard access to editing, running, debugging, testing, and inspecting errors.
- Screen-reader behavior tested with a named platform and assistive technology when a claim of compatibility is made.
- An accessible alternative when a specialized graphical tool is unavoidable.

Do not label a tool or lesson accessible solely because it is keyboard-operable or because a vendor publishes an accessibility statement. Record the actual test scope.

## Instructional quality review

Evaluate whether objectives describe skills the lesson actually teaches and assesses; explanations distinguish concepts beginners may confuse; examples are small enough to reason about and complete enough to run; activities progress from guided practice to independent application; common mistakes are specific to the language or tool; assessments test understanding rather than transcription; terminology is consistent with the shared glossary; and the lesson contributes to the course sequence without unnecessary repetition.

## Cross-language alignment

When a topic is taught in multiple language tracks, the underlying learning outcome and problem context should be comparable. The implementation should remain idiomatic to each language. Alignment does not require identical syntax, data structures, or examples where language semantics differ.

For shell instructions in shared lessons, follow CODE_STYLE.md: Bash-family commands for macOS/Linux are followed immediately by equivalent Windows 11 PowerShell commands. The dedicated Bash and PowerShell terminal tracks are intentionally separate.

## Validation evidence levels

Use precise language when recording status:

- **Editorial review:** content and structure have been read for clarity and consistency.
- **Link check:** internal and external links have been checked for reachability at a stated time.
- **Static inspection:** code or configuration has been inspected without execution.
- **Syntax/compile check:** examples passed a named parser or compiler under a stated version.
- **Smoke execution:** examples ran and exited under stated conditions.
- **Behavioral test:** assertions or expected-output checks validated specified behavior.
- **Accessibility test:** a named workflow was exercised with specified assistive technology, operating system, and application version.

Passing one level does not imply passing the next. Successful compilation does not establish correct behavior, and successful execution does not establish accessibility.

## Audit record template

For a formal review, record the file and revision, reviewer and review date, lesson components present or not applicable, technical validation command and tool version, expected-output or behavioral test evidence, accessibility test environment and observed issues, broken links or editorial defects, required changes and owner, remaining limitations, and next review date.

## Completion criteria

A lesson is ready for instruction when its objectives, explanation, example, activities, and assessment align; its code and links have been checked to the level claimed; and no known accessibility barrier prevents the core learning outcome without an alternative. A course-wide audit must also verify book navigation, internal links, and the build independently of lesson-level review.
