import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { execFileSync } from "node:child_process";

const files = [
  "TYPESCRIPT/unit00-01-setup-foundations.md",
  "TYPESCRIPT/unit02-04-io-control-data.md",
  "TYPESCRIPT/unit05-08-strings-functions-oop-files.md",
  "TYPESCRIPT/unit09-11-modules-collections-projects.md"
];
const required = [
  "Reading References", "Learning Objectives", "Concept Explanation",
  "Worked Example", "Expected Behavior or Output", "Common Mistakes",
  "Activities", "Accessibility Practice", "Skills Checklist"
];
const errors = [];
let lessonCount = 0;
let exampleCount = 0;
const temp = fs.mkdtempSync(path.join(process.cwd(), ".ts-curriculum-"));
fs.writeFileSync(path.join(temp, "package.json"), JSON.stringify({ type: "module" }));

try {
  for (const file of files) {
    const markdown = fs.readFileSync(file, "utf8");
    const headings = [...markdown.matchAll(/^## Lesson ([^\n]+)/gm)];
    for (let i = 0; i < headings.length; i += 1) {
      lessonCount += 1;
      const start = headings[i].index;
      const next = headings[i + 1]?.index ?? markdown.length;
      const unit = markdown.indexOf("\n# Unit ", start + 1);
      const end = unit >= 0 && unit < next ? unit : next;
      const section = markdown.slice(start, end);
      for (const name of required) {
        if (!section.includes(`### ${name}`)) {
          errors.push(`${file}: ${headings[i][1]} missing ${name}`);
        }
      }
    }
    const blocks = [...markdown.matchAll(/```typescript[^\n]*\n([\s\S]*?)```/g)];
    for (let i = 0; i < blocks.length; i += 1) {
      exampleCount += 1;
      const name = `example-${String(exampleCount).padStart(3, "0")}.ts`;
      fs.writeFileSync(path.join(temp, name), `${blocks[i][1]}\nexport {};\n`);
    }
  }
  if (lessonCount !== 57) errors.push(`Expected 57 lesson sections; found ${lessonCount}`);
  const sourceFiles = fs.readdirSync(temp).filter(name => name.endsWith(".ts")).map(name => path.join(temp, name));
  const compiler = path.join(process.cwd(), "node_modules", ".bin", "tsc");
  const args = [
    "--noEmit", "--strict", "--target", "ES2022",
    "--module", "NodeNext", "--moduleResolution", "NodeNext",
    "--types", "node", "--esModuleInterop", "--skipLibCheck",
    ...sourceFiles
  ];
  try {
    execFileSync(compiler, args, { cwd: temp, stdio: "pipe", encoding: "utf8" });
  } catch (error) {
    const output = error.stdout || error.stderr || error.message;
    errors.push(String(output));
  }
  if (errors.length) {
    console.error(errors.join("\n"));
    process.exitCode = 1;
  } else {
    console.log(`Validated ${lessonCount} lesson sections and type-checked ${exampleCount} TypeScript examples with strict mode.`);
    console.log("This checker type-checks isolated examples; it does not execute them or assert their output.");
  }
} finally {
  fs.rmSync(temp, { recursive: true, force: true });
}
