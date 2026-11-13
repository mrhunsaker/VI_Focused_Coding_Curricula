# Unit 1: Foundations of Computing

## Overview

Introduce computer science, first programs, variables, and primitive types. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 1.1: Welcome to computer science


### Concept Explanation
Computer science studies computation and information. An algorithm is a finite, ordered set of steps for solving a problem; TypeScript is one language used to express algorithms.

### Worked Example
```typescript
const steps = ["understand the problem", "design steps", "implement", "test"];
for (const [index, step] of steps.entries()) {
  console.log(`${index + 1}. ${step}`);
}
```

### Expected Behavior or Output
Four ordered steps are printed, from understanding the problem through testing.

### Common Mistakes
- Equating computer science with learning syntax only.
- Beginning implementation before defining the problem.
- Treating one programming language as the only way to express an algorithm.

### Activities
1. Describe an everyday algorithm in plain language.
2. Identify input, processing, and output for a tip calculator.
3. Explain how testing provides evidence about a solution.

### Accessibility Practice
Present algorithms as numbered text steps. Do not rely on flowchart colors or spatial layout alone. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define computer science and an algorithm.
- [ ] I can identify input, processing, and output.
- [ ] I can describe a testable solution plan.

---

---

## Lesson 1.2: Your first TypeScript program: Hello World

### Reading References
- Python source counterpart: Unit 1 lesson 1.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create a source file, compile it, and explain sequential execution and output.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Statements execute in sequence unless control flow changes that order. `console.log` writes a line of text to standard output.

### Worked Example
```typescript
console.log("Hello, World!");
console.log("Welcome to TypeScript.");
```

### Expected Behavior or Output
The terminal prints the two messages in source order, one per line.

### Common Mistakes
- Forgetting to save the source file before compiling.
- Expecting TypeScript annotations to appear in runtime output.
- Changing capitalization or punctuation in an exact-output exercise.

### Activities
1. Change the second message and compile again.
2. Add a third line and predict its position.
3. Explain the difference between source code and terminal output.

### Accessibility Practice
Read one statement at a time and compare source order with output order. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can create and run a first program.
- [ ] I can predict sequential output.
- [ ] I can distinguish source text from program output.

---

---

## Lesson 1.3: Variables and simple data types

### Reading References
- Python source counterpart: Unit 1 lesson 1.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Declare typed variables and represent the canonical student profile.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
TypeScript can infer many local types, but annotations make contracts explicit. `const` prevents reassignment of a binding; it does not deeply freeze an object.

### Worked Example
```typescript
const student: { name: string; age: number; heightM: number; favoriteSubject: string } = {
  name: "Avery", age: 16, heightM: 1.72, favoriteSubject: "Computer Science"
};
console.log(`${student.name}, age ${student.age}`);
console.log(`Height: ${student.heightM} m`);
console.log(student.favoriteSubject);
```

### Expected Behavior or Output
The output identifies Avery, age 16, height 1.72 m, and Computer Science.

### Common Mistakes
- Using a string where a number is required.
- Assuming const makes object properties immutable.
- Using any to bypass a type error rather than correcting the type.

### Activities
1. Declare string, number, and boolean values.
2. Add a field to the student profile and update its type.
3. Explain type inference versus an explicit annotation.

### Accessibility Practice
Read property names and types aloud. Use one property per line for structured output. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can declare typed variables.
- [ ] I can explain const and type inference.
- [ ] I can model the canonical student profile.

---
