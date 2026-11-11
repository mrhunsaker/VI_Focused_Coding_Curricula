# C Teacher's Guide

## Purpose and course context

This guide supports instructors teaching the C curriculum to beginning programmers, including blind and visually impaired learners using screen readers, braille displays, magnification, keyboard navigation, or combinations of access technology. It supplements the [C curriculum overview](c_README.md), [complete lessons](lessons.md), and [topic index](INDEX.md).

The course targets **C17** and a GCC or Clang workflow. C is a compiled procedural language in which learners work directly with explicit types, arrays, structs, pointers, memory lifetimes, and return-code-based error handling. Do not treat C as merely Python with different punctuation: its model of memory and program execution is a central learning objective.

## Outcomes and sequence

Follow Units 0–11 in order, after the shared [Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md) and [Terminal Skills prerequisite](../TERMINAL/TERMINAL_README.md). Learners should be able to create and compile a project, interpret compiler diagnostics, use scalar types and expressions, implement decisions and loops, work with arrays and strings, define functions and structs, reason about pointers and object lifetimes, process files, check return values, test behavior, and complete the capstone.

Use the same lesson rhythm throughout: state the objective; define vocabulary; explain the code's structure and punctuation; ask for a prediction; compile and run; inspect output and diagnostics; modify one feature; and ask the learner to explain the result.

## Toolchain and compilation

Use a C17-capable GCC or Clang compiler. The curriculum's representative command is:

```sh
cc -std=c17 -Wall -Wextra -Wpedantic -g main.c -o main
./main
```

Explain each compiler option: language standard, warnings, debug information, source input, and output executable. Compile after small changes rather than accumulating many errors. Teach the learner to read the first diagnostic, identify its file and line, navigate directly to that location, and distinguish a warning from an error. Warnings are instructional feedback; do not normalize ignoring them.

## Teaching C's distinctive concepts

### Types, expressions, and input

C does not provide Python-style automatic conversion for every operation. Teach integer division, signed and unsigned values, floating-point representation, integer promotions, and explicit conversions with small examples. Use format specifiers carefully and explain that a mismatch between a format string and the corresponding argument can cause undefined behavior. Validate input results; never assume a conversion succeeded merely because a prompt was displayed.

### Arrays, strings, and bounds

An array is a fixed-size contiguous sequence; it does not carry a runtime length that can safely be recovered from an arbitrary pointer. A C string is a character sequence terminated by a null character. Teach the distinction between array capacity, current string length, and the terminating null byte. Make bounds checks explicit and use size-aware library operations. Do not teach unsafe input functions or imply that a buffer automatically expands.

### Pointers, structs, and lifetime

Introduce addresses and indirection with a stable verbal model: a pointer stores an address, and dereferencing accesses the object at that address. Distinguish a pointer from the object it points to. Teach null pointers, initialization, pointer arithmetic limits, and the lifetime of automatic, static, and dynamically allocated objects. Every allocation needs a clear ownership and release plan; pair allocation and deallocation in the same documented responsibility. Do not present a pointer as an integer or suggest that every pointer is safe to dereference.

Use structs to model named records. Prefer named fields over parallel arrays when they improve the learner's ability to inspect and explain a record. Explain that passing a struct by value copies it, while passing a pointer permits access to the original object.

### Errors and files

C has no built-in exception mechanism. Teach functions' return values, status codes, output parameters, and relevant library error indicators. Check the result of file opening, reading, writing, and closing operations. Make failure paths explicit and ensure resources are released on every path. JSON persistence in the course uses a documented external library; distinguish library functionality from the C standard library and explain its build/link requirements.

## Accessibility and classroom delivery

- Keep demonstrations and assessments text-first; make terminal output and compiler diagnostics available as selectable text.
- Describe braces, parentheses, brackets, pointer operators, ampersands, semicolons, and nesting explicitly when first introduced.
- Teach editor navigation by line, symbol, diagnostic, and file; provide keyboard equivalents for every essential action.
- Let learners configure punctuation verbosity and braille output to match their needs.
- Avoid visual memory diagrams as the only explanation. Describe memory regions, addresses, array positions, and ownership verbally or with structured text.
- Do not require a visual debugger, graphical IDE feature, or GUI-only workflow without an equivalent accessible route.
- Allow time for navigating compiler output and reviewing punctuation; assess conceptual understanding separately from navigation speed.

A text interface is not automatically accessible. Test the actual compiler, terminal, editor, and assistive-technology combination used in class.

## Assessment and common misconceptions

Assess compilation, runtime behavior, reasoning, and safety separately. Ask learners to explain array bounds, string termination, pointer validity, object lifetime, and the consequences of unchecked input. Include normal, boundary, and invalid-input tests. Useful debugging tasks include a format-specifier mismatch, an off-by-one loop, a failed file open, and a pointer that is not initialized.

Do not equate a successful compile with correctness or memory safety. The repository's example checks, where available, establish only their documented scope; they do not replace behavioral tests or hands-on accessibility validation.

## Differentiation and pacing

Some learners will need additional practice with punctuation, nested blocks, compiler invocation, or terminal navigation. Others may be ready for deeper work on const-correctness, allocation strategies, or API contracts. Keep the learning objective constant while varying the amount of scaffolding, number of examples, and time allowed. Offer a short trace table in text for loops and pointer changes; never require a visual memory diagram.

## AI-use policy

Follow the repository's course policy: AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, refactor, or generate course code or assessment solutions. Apply the same rule to instructor demonstrations and student submissions.

## Instructor preparation and maintenance

Before teaching, verify the installed compiler and its C17 support, run the repository's current example-validation procedure if provided, and confirm the terminal/editor workflow with the learner's assistive technology. Record compiler version, platform, command, and validation scope. When changing examples, update related expected output and validation materials together. Consult the [shared accessibility guidance](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) before selecting any graphical tool.
