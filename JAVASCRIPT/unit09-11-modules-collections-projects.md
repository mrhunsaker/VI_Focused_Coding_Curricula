# Units 9–11: Testing, Data Analysis, Projects, and Capstone

**Runtime baseline:** Node.js 26.x. Unit 9 uses Node's built-in test runner for a dependency-free baseline. A Jest alternative may be introduced as an extension.

# Unit 9: Testing and Data Analysis

## Overview
This unit follows the Python sequence: test a function, test a class, generate random values, analyze text, and process CSV data. Reuse the canonical score list, text sample, inventory, and CSV column names.

## Lesson 9.1: Testing a Function

### Reading References
- Python source counterpart: Unit 9, Lesson 9.1.
- Node.js documentation: Test runner (`node:test`).

### Learning Objectives
- Write unit tests for deterministic functions.
- Use assertions for expected and actual values.
- Run tests from the terminal.

### Concept Explanation
A unit test calls a deterministic function with known inputs and compares the returned value with an expected result. Tests should include ordinary inputs and boundary conditions.

### Worked Example
Create `math.js`:
```javascript
function add(a, b) {
  return a + b;
}

function getGrade(score) {
  if (score >= 90) return "A";
  if (score >= 80) return "B";
  if (score >= 70) return "C";
  if (score >= 60) return "D";
  return "F";
}

module.exports = { add, getGrade };
```

Create `math.test.js`:
```javascript
const test = require("node:test");
const assert = require("node:assert/strict");
const { add, getGrade } = require("./math");

test("add returns the sum", () => {
  assert.equal(add(5, 3), 8);
  assert.equal(add(-5, -3), -8);
  assert.equal(add(0, 7), 7);
});

test("getGrade follows shared thresholds", () => {
  assert.equal(getGrade(90), "A");
  assert.equal(getGrade(82), "B");
  assert.equal(getGrade(76), "C");
  assert.equal(getGrade(60), "D");
  assert.equal(getGrade(59), "F");
});
```

Run with `node --test`.

Expected result: two passing tests and zero failures.

### Expected Behavior or Output
The Node.js test runner reports two passing tests and no failures when add() and getGrade() satisfy the stated contracts.

### Common Mistakes
- Testing only one typical value and ignoring boundaries.
- Writing assertions that merely repeat the implementation.
- Forgetting to export the function being tested.
- Making tests depend on execution order or shared mutable state.

### Activities
1. Add tests for the canonical scores 82, 91, 76, and 88.
2. Add boundary tests for every grade threshold.
3. Add a test for invalid scores and decide what the function contract should be.
4. Run the test file from the terminal and interpret the pass/fail summary.

### Accessibility Practice
Read each test name and assertion result. Ensure failures identify the expected and actual values in text.

### Skills Checklist
- [ ] I can write a test with `node:test`.
- [ ] I can assert expected values.
- [ ] I can test normal and boundary cases.
- [ ] I can run tests from the terminal.

## Lesson 9.2: Testing a Class

### Reading References
- Python source counterpart: Unit 9, Lesson 9.2.
- Node.js documentation: Test runner and assert.

### Learning Objectives
- Test object construction, state changes, and methods.
- Verify both valid and invalid operations.
- Keep test cases independent.

### Concept Explanation
A class test verifies observable behavior of an instance: construction, method results, valid state changes, and rejected invalid changes.

### Worked Example
Assume `InventoryItem` exposes `quantity`, `updateQuantity()`, and `lineValue()`. A test file can verify its public behavior:

```javascript
const test = require("node:test");
const assert = require("node:assert/strict");
const { InventoryItem } = require("./inventory-item");

test("inventory item updates quantity and calculates value", () => {
  const item = new InventoryItem("Notebook", 3, 2.50);
  assert.equal(item.lineValue(), 7.50);
  item.updateQuantity(5);
  assert.equal(item.lineValue(), 12.50);
});

test("inventory item rejects a negative quantity", () => {
  const item = new InventoryItem("Pencil", 10, 0.50);
  assert.throws(() => item.updateQuantity(-1), RangeError);
});
```

Expected result: both tests pass when the class enforces its stated contract.

### Expected Behavior or Output
Both tests pass when the item value updates from $7.50 to $12.50 and a negative quantity throws RangeError.

### Common Mistakes
- Testing private implementation details instead of public behavior.
- Reusing one mutated instance across unrelated tests.
- Forgetting to test invalid state transitions.

### Activities
1. Test a Notebook item with quantity 3 and unit price 2.50.
2. Verify its line value after changing quantity to 5.
3. Verify that a negative quantity is rejected.
4. Add a test for a zero quantity and explain whether it is valid.

### Accessibility Practice
Give each test a descriptive name that states the behavior being verified. Avoid ambiguous test labels such as "test 1".

### Skills Checklist
- [ ] I can instantiate an object in a test.
- [ ] I can test a method's return value.
- [ ] I can test a state change.
- [ ] I can assert that invalid operations throw.

## Lesson 9.3: Introduction to Random Numbers

### Reading References
- Python source counterpart: Unit 9, Lesson 9.3.
- MDN: Math.random.

### Learning Objectives
- Generate random floating-point values and bounded integers.
- Select a random element from an array.
- Explain why random tests should not depend on a specific result.

### Concept Explanation
Math.random() returns a pseudorandom floating-point value greater than or equal to zero and less than one. Transform it to a bounded integer with multiplication and Math.floor().

### Worked Example
```javascript
const randomDecimal = Math.random();
const randomInteger = Math.floor(Math.random() * 10) + 1;

const colors = ["red", "blue", "green"];
const randomChoice = colors[Math.floor(Math.random() * colors.length)];

console.log(`Decimal in [0, 1): ${randomDecimal >= 0 && randomDecimal < 1}`);
console.log(`Integer in 1..10: ${randomInteger >= 1 && randomInteger <= 10}`);
console.log(`Selected item is valid: ${colors.includes(randomChoice)}`);
```

Expected output: three lines containing `true`; the sampled values vary on each run.

### Expected Behavior or Output
Each run prints true for all three range and membership checks; the sampled values may differ.

### Common Mistakes
- Assuming `Math.random()` can return exactly 1.
- Forgetting that `Math.floor()` is needed for an integer index.
- Writing a test that expects one particular random result.

### Activities
1. Generate a random integer from 1 through 10.
2. Select one of the canonical inventory item names.
3. Run the program several times and observe that values vary.
4. Explain why randomness makes exact-output tests unreliable without a controllable source.

### Accessibility Practice
Label the range and meaning of each random value. Never require a visual animation to observe a random result.

### Skills Checklist
- [ ] I can use `Math.random()`.
- [ ] I can generate a bounded integer.
- [ ] I can select a random array element.
- [ ] I can test properties of random output rather than one exact sample.

## Lesson 9.4: Analyzing Text Data

### Reading References
- Python source counterpart: Unit 9, Lesson 9.4.
- MDN: String and Map.

### Learning Objectives
- Normalize text before analysis.
- Count words and character frequencies.
- Use a Map to store frequency counts.

### Concept Explanation
Text analysis requires explicit normalization and tokenization rules. A Map stores each token and its current frequency; the regular expression in this example treats hyphenated words as separate alphabetic tokens.

### Worked Example
```javascript
const sample = "A student studies programming. Programming develops problem-solving skills.";

function countWords(text) {
  const words = text.toLowerCase().match(/[a-z]+/g) ?? [];
  const counts = new Map();

  for (const word of words) {
    counts.set(word, (counts.get(word) ?? 0) + 1);
  }
  return counts;
}

const frequencies = countWords(sample);
for (const [word, count] of frequencies) {
  console.log(`${word}: ${count}`);
}
```

Expected output:
```text
a: 1
student: 1
studies: 1
programming: 2
develops: 1
problem: 1
solving: 1
skills: 1
```

### Expected Behavior or Output
The sample produces nine tokens and eight distinct token keys; programming has frequency 2 and every other displayed token has frequency 1.

### Common Mistakes
- Counting uppercase and lowercase forms as separate words.
- Splitting on a single space and retaining punctuation.
- Assuming a simple regular expression handles every language's word boundaries.

### Activities
1. Count the words in the canonical text sample.
2. Identify the most frequent word.
3. Count characters after normalizing case.
4. Explain how punctuation and hyphenation affect the result.

### Accessibility Practice
Print each word and count as a labeled pair. State the normalization rules so learners can understand why the counts have those values.

### Skills Checklist
- [ ] I can normalize text before counting.
- [ ] I can tokenize a simple English text sample.
- [ ] I can store frequencies in a Map.
- [ ] I can explain limitations of a simple tokenizer.

## Lesson 9.5: Working with CSV Data

### Reading References
- Python source counterpart: Unit 9, Lesson 9.5.
- npm documentation: `csv-parse`.

### Learning Objectives
- Explain rows, columns, headers, and records.
- Read CSV data with a standards-aware parser.
- Compute a summary from the canonical column set.

### Concept Explanation
CSV is a text format with quoting and escaping rules. Splitting every line on commas is not a correct general CSV parser because a quoted field may itself contain a comma or newline. Use a maintained parser for real CSV data. The canonical headers are `student_id`, `first_name`, `last_name`, `score`, and `active`.

### Worked Example
Install the parser with `npm install csv-parse`. Save a small fixture as `students.csv`:
```csv
student_id,first_name,last_name,score,active
1,Avery,Student,91,true
2,Jordan,Lee,82,true
3,Casey,Smith,76,false
```

Read it with `csv-parse`:
```javascript
const fs = require("node:fs");
const { parse } = require("csv-parse/sync");

const records = parse(fs.readFileSync("students.csv", "utf8"), {
  columns: true,
  skip_empty_lines: true,
  trim: true
});

const average = records.reduce((sum, row) => sum + Number(row.score), 0)
  / records.length;

console.log(`Loaded students: ${records.length}`);
console.log(`Average score: ${average.toFixed(2)}`);
```

Expected output:
```text
Loaded students: 3
Average score: 83.00
```

### Expected Behavior or Output
The sample CSV contains three records with scores 91, 82, and 76. The average is 83.00.

### Common Mistakes
- Splitting CSV lines on commas without handling quoted fields.
- Forgetting that parsed field values are strings until converted.
- Assuming every row contains every required column.
- Failing to handle a missing or empty file.

### Activities
1. Create a CSV with the five canonical column names.
2. Load the records and print each student's name and score.
3. Calculate the average score.
4. Add a quoted field containing a comma and verify that the parser reads it as one field.

### Accessibility Practice
Print one record per line with column names. Provide a textual summary of any malformed rows rather than relying on a spreadsheet's visual highlighting.

### Skills Checklist
- [ ] I can explain CSV headers and records.
- [ ] I can parse CSV with a standards-aware library.
- [ ] I can convert numeric fields before calculating.
- [ ] I can summarize a dataset with labeled output.

# Unit 10: Project-Based Learning — Text-Based Applications

## Overview
The projects preserve the Python track's requirements and user interaction. The text adventure uses the same three rooms, exits, torch, magic key, and movement commands. The command-line to-do manager supports add, view, complete, delete, and JSON persistence.

## Lesson 10.1: Designing Your Project

### Reading References
- Python source counterpart: Unit 10, Lesson 10.1.
- MDN: JavaScript modules and functions.

### Learning Objectives
- Apply top-down design to a multi-part program.
- Identify inputs, outputs, data, and edge cases.
- Write pseudocode and acceptance tests before implementation.

### Concept Explanation
Top-down design breaks a large task into smaller responsibilities. The project should have separate functions for input, state changes, display, and persistence. Define command names and error behavior before writing code.

### Worked Example
Text-adventure pseudocode:
```text
CREATE rooms and exits
PLACE items in selected rooms
CREATE player at starting room
REPEAT
  DISPLAY current room and player status
  READ command
  VALIDATE command
  APPLY movement or inventory action
UNTIL player enters quit
```

### Expected Behavior or Output
The learner produces pseudocode, a room/command specification, and acceptance tests before implementation.

### Common Mistakes
- Starting implementation before defining the project requirements.
- Combining input, state changes, and display in one large function.
- Omitting invalid-command and boundary cases.

### Activities
1. Draw or describe the three-room map in text.
2. List every valid movement command and its destination.
3. Define the to-do manager's five menu operations.
4. Write at least five acceptance tests before implementation.

### Accessibility Practice
Use keyboard-operable commands, descriptive prompts, and predictable text output. Do not require maps, color, drag-and-drop, or mouse-only interaction.

### Skills Checklist
- [ ] I can decompose a project into functions or modules.
- [ ] I can define inputs and outputs.
- [ ] I can write pseudocode.
- [ ] I can define acceptance tests and error cases.

## Lesson 10.2: Building a Text-Based Adventure Game (Part 1)

### Reading References

