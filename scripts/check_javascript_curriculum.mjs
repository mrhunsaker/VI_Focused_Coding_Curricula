import fs from "node:fs";

const files = [
  "JAVASCRIPT/unit00-01-setup-foundations.md",
  "JAVASCRIPT/unit02-04-io-control-data.md",
  "JAVASCRIPT/unit05-08-strings-functions-oop-files.md",
  "JAVASCRIPT/unit09-11-modules-collections-projects.md"
];

const requiredSections = [
  "Reading References",
  "Learning Objectives",
  "Concept Explanation",
  "Worked Example",
  "Expected Behavior or Output",
  "Common Mistakes",
  "Activities",
  "Accessibility Practice",
  "Skills Checklist"
];

let lessonCount = 0;
let exampleCount = 0;
const errors = [];

for (const path of files) {
  const markdown = fs.readFileSync(path, "utf8");
  const headings = [...markdown.matchAll(/^## Lesson [^\n]+/gm)];
  for (let index = 0; index < headings.length; index += 1) {
    const start = headings[index].index;
    const nextLesson = headings[index + 1]?.index ?? markdown.length;
    const nextUnit = markdown.indexOf("\n# Unit ", start + 1);
    const end = nextUnit >= 0 && nextUnit < nextLesson ? nextUnit : nextLesson;
    const section = markdown.slice(start, end);
    lessonCount += 1;

    for (const required of requiredSections) {
      if (!section.includes(`### ${required}`)) {
        errors.push(`${path}: ${headings[index][0]} is missing "${required}"`);
      }
    }
  }

  const examples = [...markdown.matchAll(/```javascript[^\n]*\n([\s\S]*?)```/g)];
  for (let index = 0; index < examples.length; index += 1) {
    exampleCount += 1;
    try {
      // Syntax validation only. Examples are not executed by this checker.
      new Function(examples[index][1]);
    } catch (error) {
      errors.push(`${path}: JavaScript example ${index + 1}: ${error.message}`);
    }
  }
}

if (lessonCount !== 57) {
  errors.push(`Expected 57 mapped lesson sections; found ${lessonCount}.`);
}

if (errors.length > 0) {
  console.error(errors.join("\n"));
  process.exitCode = 1;
} else {
  console.log(`Validated ${lessonCount} lesson sections and syntax-parsed ${exampleCount} JavaScript examples.`);
  console.log("This check does not execute examples or test expected output.");
}
