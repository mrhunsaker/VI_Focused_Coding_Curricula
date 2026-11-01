import { readFileSync } from "node:fs";
import { existsSync } from "node:fs";
import { dirname, resolve } from "node:path";

const files = [
  "KOTLIN/unit00-01-setup-foundations.md",
  "KOTLIN/unit02-04-io-control-data.md",
  "KOTLIN/unit05-08-strings-functions-oop-files.md",
  "KOTLIN/unit09-11-collections-projects.md",
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
let lessons = 0;
let failures = 0;
for (const file of files) {
  const content = readFileSync(file, "utf8");
  const headings = [...content.matchAll(/^### Lesson (\d+)\.(\d+): .+$/gm)];
  lessons += headings.length;
  for (let i = 0; i < headings.length; i++) {
    const start = headings[i].index;
    const end = headings[i + 1]?.index ?? content.length;
    const section = content.slice(start, end);
    for (const heading of required) {
      if (!section.includes(`#### ${heading}`)) {
        console.error(`${file}: lesson ${headings[i][1]}.${headings[i][2]} missing ${heading}`);
        failures++;
      }
    }
    if (!section.includes("```kotlin")) {
      console.error(`${file}: lesson ${headings[i][1]}.${headings[i][2]} missing Kotlin example`);
      failures++;
    }
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
console.log(`Kotlin curriculum structure passed: ${lessons} lessons; all nine sections and Kotlin example blocks present.`);
