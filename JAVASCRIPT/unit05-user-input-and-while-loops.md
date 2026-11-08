# Unit 5: User Input and `while` Loops

## Overview
This unit builds on terminal input and introduces sentinel-controlled repetition, loop flags, `break`, and `continue`. The goal is to create predictable interactive programs with explicit stopping conditions.

## Lesson 5.1: How Terminal Input Works

### Reading References
- Python source counterpart: Unit 5, Lesson 5.1.
- Node.js documentation: `node:readline/promises`.

### Learning Objectives
- Explain why Node.js terminal input is asynchronous.
- Read, trim, and validate a text response.
- Close a readline interface reliably.

### Concept Explanation
Node.js does not provide a built-in synchronous `input()` function. Use `readline/promises` and `await question()` to obtain a response. The result is a string; conversion and validation are separate steps.

### Worked Example
```javascript
const readline = require("node:readline/promises");
const { stdin, stdout } = require("node:process");

async function main() {
  const rl = readline.createInterface({ input: stdin, output: stdout });
  try {
    const response = (await rl.question("Enter your favorite subject: ")).trim();
    if (response === "") {
      console.log("Error: a subject is required.");
    } else {
      console.log(`Favorite subject: ${response}`);
    }
  } finally {
    rl.close();
  }
}
main();
```

Example interaction:
```text
Enter your favorite subject: Computer Science
Favorite subject: Computer Science
```

### Expected Behavior or Output
For the input Computer Science, the program prints `Favorite subject: Computer Science`. Blank input prints the required-field error.

### Common Mistakes
- Forgetting `await` before `question()`.
- Treating the response as a number without converting it.
- Failing to close the interface.
- Accepting an empty string when a nonempty response is required.

### Activities
1. Ask for the canonical student name Avery and print a greeting.
2. Ask for age, convert it with `Number()`, and reject blank or non-finite input.
3. Ask for a menu choice and normalize it with `trim()`.
4. Explain the purpose of `try/finally` around the readline interface.

### Accessibility Practice
Use descriptive prompts, announce validation errors in text, and keep the prompt sequence linear. All steps must work from the terminal without mouse interaction.

### Skills Checklist
- [ ] I can create a readline interface.
- [ ] I can await terminal input.
- [ ] I can validate and normalize text input.
- [ ] I can close the interface reliably.

## Lesson 5.2: The `while` Loop in Action

### Reading References
- Python source counterpart: Unit 5, Lesson 5.2.
- MDN: `while` statement.

### Learning Objectives
- Write a condition-controlled loop.
- Use a sentinel value to terminate repetition.
- Explain the difference between a `for` loop and a `while` loop.

### Concept Explanation
A `while` loop repeats as long as its condition is true. A sentinel is a special input value that signals completion. The loop must update state so its condition can eventually become false.

### Worked Example
```javascript
const scores = [82, 91, 76, 88];
let index = 0;
let total = 0;

while (index < scores.length) {
  total += scores[index];
  index += 1;
}

console.log(`Total: ${total}`);
console.log(`Average: ${(total / scores.length).toFixed(2)}`);
```

Expected output:
```text
Total: 337
Average: 84.25
```

### Expected Behavior or Output
The canonical score list produces total 337 and average 84.25.

### Common Mistakes
- Forgetting to increment the index.
- Using a condition that is already false before the first iteration.
- Updating the index after a branch that can skip the update.

### Activities
1. Count from 1 through 5 with a `while` loop.
2. Sum the canonical scores and calculate their average.
3. Design a sentinel-controlled menu that stops when the user enters "quit".
4. Trace the value of the loop index before and after each iteration.

### Accessibility Practice
State the loop condition and termination rule before running the program. Provide a textual completion message.

### Skills Checklist
- [ ] I can write a condition-controlled loop.
- [ ] I can use a sentinel to stop repetition.
- [ ] I can update loop state correctly.
- [ ] I can choose between `for` and `while`.

## Lesson 5.3: Using Flags and `break` to Exit Loops

### Reading References
- Python source counterpart: Unit 5, Lesson 5.3.
- MDN: `break` statement.

### Learning Objectives
- Use a Boolean flag to record a condition.
- Stop a loop early with `break`.
- Distinguish normal loop completion from early termination.

### Concept Explanation
A flag stores whether a condition has been found or satisfied. `break` exits the nearest loop immediately; code after the loop can then report the final result.

### Worked Example
```javascript
const scores = [82, 91, 76, 88];
let found = false;

for (const score of scores) {
  if (score > 90) {
    found = true;
    console.log(`First score above 90: ${score}`);
    break;
  }
}

if (!found) {
  console.log("No score above 90 was found.");
}
```

Expected output:
```text
First score above 90: 91
```

### Expected Behavior or Output
The canonical scores produce `First score above 90: 91`; if no value matches, the fallback message is printed.

### Common Mistakes
- Using a string such as "false" instead of the Boolean value `false`.
- Forgetting to set the flag when the condition is met.
- Placing `break` outside a loop or switch statement.

### Activities
1. Search the canonical scores for the first score greater than 90.
2. Repeat the search for a score greater than 95 and report that none exists.
3. Use a flag to validate that a required inventory item exists.
4. Explain when `break` is clearer than changing the loop condition.

### Accessibility Practice
Report both the search result and whether a match was found. Do not rely on color or a visual marker.

### Skills Checklist
- [ ] I can initialize and update a Boolean flag.
- [ ] I can use `break` to stop a loop.
- [ ] I can report successful and unsuccessful searches.
- [ ] I can explain early termination.

## Lesson 5.4: Using `continue` in Loops

### Reading References
- Python source counterpart: Unit 5, Lesson 5.4.
- MDN: `continue` statement.

### Learning Objectives
- Skip the current iteration with `continue`.
- Validate data before processing it.
- Explain the difference between `continue` and `break`.

### Concept Explanation
The `continue` statement skips the remainder of the current iteration and starts the next one. It does not end the loop.

### Worked Example
```javascript
const entries = ["82", "", "91", "invalid", "76", "88"];
let total = 0;
let validCount = 0;

for (const entry of entries) {
  const score = Number(entry);
  if (entry.trim() === "" || !Number.isFinite(score)) {
    console.log("Skipping invalid score.");
    continue;
  }
  total += score;
  validCount += 1;
}

console.log(`Valid scores: ${validCount}`);
console.log(`Total: ${total}`);
```

Expected output:
```text
Skipping invalid score.
Skipping invalid score.
Valid scores: 4
Total: 337
```

### Expected Behavior or Output
The invalid blank and nonnumeric entries are skipped; four valid scores remain and their total is 337.

### Common Mistakes
- Using `continue` when the entire loop should end.
- Skipping a loop-control update in a `while` loop.
- Failing to explain why an entry was skipped.

### Activities
1. Process the canonical scores while skipping negative values.
2. Add blank and nonnumeric entries and confirm they are rejected.
3. Count accepted and rejected entries separately.
4. Rewrite a short loop using `if/else` instead of `continue`; compare readability.

### Accessibility Practice
Print a concise reason for each rejected entry. Keep accepted and rejected counts explicit.

### Skills Checklist
- [ ] I can use `continue` to skip an iteration.
- [ ] I can validate data before processing.
- [ ] I can distinguish `continue` from `break`.
- [ ] I can report rejected input clearly.

## Lesson 5.5: Avoiding Infinite Loops

### Reading References
- Python source counterpart: Unit 5, Lesson 5.5.
- MDN: Loops and iteration.

### Learning Objectives
- Identify loop conditions that never become false.
- Trace and repair loop-control logic.
- Test both normal and boundary termination.

### Concept Explanation
An infinite loop occurs when the loop condition remains true indefinitely. Before execution, identify the variable that changes, the condition that ends the loop, and every path through the body. For interactive programs, include an explicit quit command.

### Worked Example
```javascript
let count = 1;
while (count <= 3) {
  console.log(`Count: ${count}`);
  count += 1;
}
console.log("Loop finished.");
```

Expected output:
```text
Count: 1
Count: 2
Count: 3
Loop finished.
```

### Expected Behavior or Output
The loop prints Count 1, Count 2, Count 3, then Loop finished. It terminates after exactly three iterations.

### Common Mistakes
- Never changing a variable used in the condition.
- Incrementing in the wrong direction.
- Creating a path through the loop that bypasses the update.
- Testing only the normal path and not the stopping boundary.

### Activities
1. Trace the worked example by hand before running it.
2. Diagnose a loop that decrements a counter while testing whether it is less than 10.
3. Add a quit command to a menu loop.
4. Test the loop with its initial value already at the boundary.

### Accessibility Practice
Announce the expected maximum number of iterations for bounded examples. Stop runaway processes with the terminal interrupt command and describe the recovery procedure.

### Skills Checklist
- [ ] I can identify the termination condition.
- [ ] I can trace loop state changes.
- [ ] I can diagnose common infinite-loop causes.
- [ ] I can test loop boundary cases.
