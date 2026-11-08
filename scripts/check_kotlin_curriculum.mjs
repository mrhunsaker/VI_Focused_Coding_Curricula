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
