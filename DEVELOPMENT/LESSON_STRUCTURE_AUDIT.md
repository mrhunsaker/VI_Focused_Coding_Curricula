# Lesson Structure Audit

## Purpose

This audit compares the curriculum lesson files with the instructional pattern established by the original Python course. It checks organization and teaching components, not whether every lesson teaches the same subject matter or has the same length.

## Python course reference pattern

The Python units establish a recognizable sequence:

1. Unit title and **Overview** with scope, compatibility notes where relevant, and learning objectives.
2. Individual numbered lessons with a clear lesson title.
3. **Reading References** where appropriate.
4. Concept explanations, definitions, and structured examples.
5. Examples with expected output or an explanation of the result.
6. **Common Mistakes/Common Errors** where relevant.
7. **Activities** or guided practice.
8. **Skills Checklist** describing observable learning outcomes.
9. Accessibility guidance where it materially affects the workflow.

The Python source is not mechanically identical in every lesson: some later Python lessons omit one or more subsections such as Reading References or Activities. The useful standard is therefore a consistent instructional sequence and predictable signposts, not identical word counts or forcing irrelevant sections into every topic.

## Audit result

<blockquote>
**Result: the repository does not yet have one consistent lesson structure across every language and prerequisite.** The original Python course is the strongest existing model, but several other tracks use shorter outlines or different heading patterns. This audit does not certify all lessons as structurally identical.
</blockquote>

### File groups reviewed

| Curriculum group | Files reviewed | Finding |
|---|---:|---|
| Python | 7 unit files | Reference model. Most lessons use explicit references, explanations, examples, activities, and checklists, but some later lessons omit individual components. |
| JavaScript | 4 unit files | Detailed lesson content exists, but several lessons omit Overview, Reading References, Activities, or consistent lesson-level checklists. |
| TypeScript | 4 unit files | Closely follows the JavaScript grouping and inherits its inconsistent lesson-level signposts; some units add TypeScript-specific notes. |
| Java | 4 unit files | Detailed content exists and often includes Overview, examples, and checklists, but Reading References and Activities are not consistently present. |
| Kotlin | 1 standalone lessons file | Uses numbered topic sections and a learning sequence rather than the Python unit/lesson structure. It is standalone and has substantial instructional content, but its headings are not normalized to the Python pattern. |
| C, C++, C#, Julia, Swift, Rust | 6 lessons files | Each contains a ten-lesson sequence, but the files are compact guided outlines. Lesson entries generally have a short topic description and exercise rather than the full Python-style set of instructional subsections. |
| Bash and PowerShell | 2 terminal lesson files | Organized as command-skill lessons and practice, not as language-course units with the complete Python lesson architecture. |
| IDE setup | 1 standalone lesson | Uses Overview, objectives, prerequisites, sequenced lessons, explanations, activities, and a skills checklist. It is aligned to the Python teaching approach, while retaining tool-specific sections. |

### Specific structural differences

- The newer C-family, Julia, Swift, and Rust lesson files are lesson maps, not full lesson manuscripts. They need expanded explanations, examples with expected output, common errors, activities, and skills checklists for each lesson.
- Kotlin is a substantial standalone course, but its numbered sections do not consistently use the same repeated lesson-level headings as Python.
- JavaScript and TypeScript have grouped unit files with uneven use of the Python signposts. Some lessons have examples and checklists but no explicit reading references or activities.
- Java is closer to the Python format than the shorter tracks, but its lesson-level sections are not fully uniform.
- Bash and PowerShell are prerequisite skill modules. Their command-oriented organization is appropriate to the subject, but they should use a documented adapted template rather than be described as identical to a programming-language lesson.
- The Python reference itself is not perfectly uniform; its later units sometimes omit Reading References or Activities. A course-wide standard should preserve useful variation while making the key teaching sequence predictable.

## Recommended standard for future and revised lessons

Each unit file should begin with:

- Unit title.
- Overview explaining scope and prerequisites.
- Compatibility/toolchain note where applicable.
- Unit learning objectives.
- A numbered lesson sequence.

Each substantive lesson should normally include:

1. **Reading References** — official documentation and/or course text, when a useful source exists.
2. **Learning Objectives** — observable outcomes for that lesson.
3. **Concept Explanation** — definitions, syntax, semantics, and a worked explanation.
4. **Examples** — complete, runnable examples with expected text output or an explicit description of behavior.
5. **Common Mistakes** — likely errors, their symptoms, and a correction or diagnostic approach.
6. **Activities** — independent practice that changes or extends the example; include expected behavior, not a copied solution.
7. **Accessibility Practice** — keyboard/screen-reader/braille workflow when relevant to the task.
8. **Skills Checklist** — first-person statements that a learner can verify.

A section may be omitted when it genuinely does not apply, but the reason should be clear. Project and capstone lessons may use requirements, milestones, test criteria, and deliverables in place of a conventional worked example.

## Validation status

- Heading-level review completed for the Python, JavaScript, TypeScript, Java, Kotlin, C, C++, C#, Julia, Swift, Rust, Bash, and PowerShell lesson files.
- The new standalone IDE lesson follows the recommended sequence and includes learning objectives, explanations, platform-specific steps, activities, and a checklist.
- This is a structural audit, not a complete content rewrite of all lesson files.
- A full normalization pass remains necessary before the repository can accurately claim that every lesson follows one common template.
- No claim is made here that every code example, external link, screen-reader workflow, or lesson objective has been independently tested.

---

The goal of standardization is predictable navigation and teaching structure, not identical prose. Keep each language's compiler, runtime, syntax, and accessibility requirements specific to that language.
