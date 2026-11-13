import { readFileSync, existsSync } from "node:fs";
import { dirname, resolve } from "node:path";

const files = [
  "KOTLIN/unit00-accessible-development-environment.md",
  "KOTLIN/unit01-foundations-of-computing.md",
  "KOTLIN/unit02-numeric-computations.md",
  "KOTLIN/unit03-control-flow-decisions-and-loops.md",
  "KOTLIN/unit04-data-structures-lists-and-dictionaries.md",
  "KOTLIN/unit05-user-input-and-while-loops.md",
  "KOTLIN/unit06-functions.md",
  "KOTLIN/unit07-classes-and-object-oriented-programming.md",
  "KOTLIN/unit08-files-and-exceptions.md",
  "KOTLIN/unit09-testing-and-data-analysis.md",
  "KOTLIN/unit10-project-based-learning-text-based-applications.md",
  "KOTLIN/unit11-capstone-accessible-personal-data-manager.md",
];
const required = [
  "Reading References",
  "Learning Objectives",
  "Concept Explanation",
  "Worked Example",
  "Expected Behavior or Output",
  "Common Mistakes",
  "Activities",
  "Accessibility Practice",
  "Skills Checklist",
];
const seen = new Set();
let lessons = 0;
let failures = 0;

for (const file of files) {
  if (!existsSync(file)) {
    console.error(`Missing current Kotlin unit file: ${file}`);
    failures++;
    continue;
  }
  const content = readFileSync(file, "utf8");
  const headings = [...content.matchAll(/^## Lesson (\d+\.\d+): .+$/gm)];
  lessons += headings.length;
  for (let i = 0; i < headings.length; i++) {
    const lessonId = headings[i][1];
    if (seen.has(lessonId)) {
      console.error(`${file}: duplicate lesson ${lessonId}`);
      failures++;
    }
    seen.add(lessonId);
    const start = headings[i].index;
    const end = headings[i + 1]?.index ?? content.length;
    const section = content.slice(start, end);
    for (const heading of required) {
      if (!section.includes(`### ${heading}`)) {
        console.error(`${file}: lesson ${lessonId} missing ${heading}`);
        failures++;
      }
    }
    if (!section.includes("```kotlin")) {
      console.error(`${file}: lesson ${lessonId} missing Kotlin example`);
      failures++;
    }
  }
  const fences = [...content.matchAll(/^```/gm)].length;
  if (fences % 2 !== 0) {
    console.error(`${file}: unbalanced Markdown code fences (${fences})`);
    failures++;
  }
  for (const match of content.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)) {
    const target = match[1];
    if (/^(https?:|mailto:|#)/i.test(target)) continue;
    const local = resolve(dirname(file), target.split("#")[0]);
    if (!existsSync(local)) {
      console.error(`${file}: broken local link ${target}`);
      failures++;
    }
  }
}
if (lessons !== 57) {
  console.error(`Expected 57 mapped lesson sections; found ${lessons}`);
  failures++;
}
if (failures) process.exit(1);
console.log(`Kotlin curriculum structure passed: ${lessons} unique lessons; all nine sections, Kotlin examples, code fences, and checked local links are present.`);
