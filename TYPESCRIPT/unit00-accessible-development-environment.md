# Unit 0: Accessible Development Environment

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

## Overview

Set up Node.js, TypeScript, an editor, workspace, and terminal workflow. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 0.1: Installing Node.js, npm, and TypeScript

### Reading References
- Python source counterpart: Unit 0 lesson 0.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Install and verify the Node.js runtime, npm, and a project-local TypeScript compiler.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Node.js executes JavaScript. TypeScript is checked and compiled before execution in this course. npm installs project-local tools so learners use a reproducible compiler version.

### Worked Example
```typescript
const runtime = "Node.js 26 LTS";
const compiler = "TypeScript 7.x";
console.log(`Runtime: ${runtime}`);
console.log(`Compiler: ${compiler}`);
```

### Expected Behavior or Output
The two lines identify the runtime and compiler separately. `node --version`, `npm --version`, and `npx tsc --version` verify the actual installations.

### Common Mistakes
- Confusing the TypeScript compiler with the Node.js runtime.
- Installing tools globally and losing project reproducibility.
- Assuming a Node.js REPL type-checks TypeScript annotations.

### Activities
1. Verify Node.js and npm versions in a terminal.
2. Create a project folder and initialize npm.
3. Install TypeScript as a development dependency and verify it with npx.

### Accessibility Practice
Read each command and its purpose before running it. Keep terminal output in a sequential log. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can distinguish Node.js from TypeScript.
- [ ] I can verify the runtime, npm, and compiler.
- [ ] I can install a project-local compiler.

---

---

## Lesson 0.2: Configuring VS Code or Theia for accessible TypeScript work

### Reading References
- Python source counterpart: Unit 0 lesson 0.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Configure an editor, TypeScript language service, terminal, and keyboard-first navigation.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The editor provides navigation, diagnostics, and refactoring support; the compiler remains the authoritative type checker. VS Code and Theia may differ in shortcuts and extension availability.

### Worked Example
```typescript
const editor = "VS Code or Theia";
const languageService = "TypeScript";
console.log(`${editor}: ${languageService} support enabled`);
```

### Expected Behavior or Output
The message confirms the intended editor and language support; verify actual navigation and diagnostic announcements with the learner's access technology.

### Common Mistakes
- Assuming the editor's visual layout is required for completing tasks.
- Using mouse-only instructions or undocumented shortcuts.
- Treating a language-service suggestion as proof that a program is correct.

### Activities
1. Open a workspace using the keyboard.
2. Navigate to a diagnostic by keyboard and read its full message.
3. Run a TypeScript build from the integrated terminal.

### Accessibility Practice
Test line, word, character, symbol, and diagnostic navigation with the learner's screen reader or braille display. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can navigate the editor by keyboard.
- [ ] I can locate and understand a TypeScript diagnostic.
- [ ] I can run a build without relying on mouse-only controls.

---

---

## Lesson 0.3: Creating the course workspace and editor extensions

### Reading References
- Python source counterpart: Unit 0 lesson 0.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create a consistent workspace and configure TypeScript formatting and project navigation.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A workspace groups source files and configuration. TypeScript projects use `package.json` for scripts and dependencies and `tsconfig.json` for compiler behavior.

### Worked Example
```typescript
const project = { name: "typescript-course", source: "src", output: "dist" };
console.log(`${project.name}: ${project.source} -> ${project.output}`);
```

### Expected Behavior or Output
The project name and source/output folders are announced as text. A standard project keeps editable TypeScript in src and emitted JavaScript in dist.

### Common Mistakes
- Editing generated JavaScript instead of TypeScript source.
- Placing course files in an unknown working directory.
- Installing editor extensions without checking publisher and availability.

### Activities
1. Create src and dist folders.
2. Open the project folder rather than an individual file.
3. Enable TypeScript language support and verify its version.

### Accessibility Practice
Use descriptive folder and file names. Announce the current working directory before running project commands. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can create and open a project workspace.
- [ ] I can identify source and generated-output folders.
- [ ] I can verify TypeScript editor support.

---

---
### Project configuration and module mode

Use a project-local TypeScript compiler and strict checking. A representative `tsconfig.json` is:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "noEmitOnError": true,
    "outDir": "dist",
    "rootDir": "src"
  },
  "include": ["src/**/*.ts"]
}
```

For the compiled Node.js workflow, set `"type": "module"` in package.json and use ES module imports consistently. If a project uses CommonJS instead, set `"type": "commonjs"` and use matching compiler settings. Do not mix `require()` and `import` in one module.

A typical script is `"build": "tsc"` and `"start": "node dist/hello.js"`. Run `npm run build` before `npm start`.


## Lesson 0.4: Your first TypeScript file and terminal workflow

### Reading References
- Python source counterpart: Unit 0 lesson 0.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Write, compile, and execute a small TypeScript program from the terminal.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
The compiler checks `.ts` source and emits `.js`. Node.js runs the emitted JavaScript. A package script makes the workflow repeatable.

### Worked Example
```typescript
const greeting: string = "Hello, World!";
console.log(greeting);
console.log("Welcome to TypeScript.");
```

### Expected Behavior or Output
Compilation succeeds and Node.js prints `Hello, World!` and `Welcome to TypeScript.` on separate lines.

### Common Mistakes
- Trying to run a TypeScript file as though it were ordinary JavaScript.
- Running Node.js from the wrong working directory.
- Ignoring compiler errors and executing stale output.

### Activities
1. Save the example as src/hello.ts.
2. Compile with the project tsconfig.
3. Run the emitted JavaScript with Node.js.

### Accessibility Practice
Read compiler diagnostics before running the program. Keep source and output paths explicit. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can write a .ts file.
- [ ] I can compile it with tsc.
- [ ] I can run emitted JavaScript with Node.js.

---
