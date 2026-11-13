[Header 2 ("unit-9-testing-and-data-analysis", [], []) [Str "Unit 9: Testing and Data Analysis"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit follows the Python sequence: test a function, test a class, generate random values, analyze text, and process CSV data. Reuse the canonical score list, text sample, inventory, and CSV column names."], Header 3 ("lesson-91-testing-a-function", ["unnumbered", "unlisted"], []) [Str "Lesson 9.1: Testing a Function"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 9, Lesson 9.1."]], [Plain [Str "Node.js documentation: Test runner (", Code ("", [], []) "node:test", Str ")."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write unit tests for deterministic functions."]], [Plain [Str "Use assertions for expected and actual values."]], [Plain [Str "Run tests from the terminal."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A unit test calls a deterministic function with known inputs and compares the returned value with an expected result. Tests should include ordinary inputs and boundary conditions."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "Create ", Code ("", [], []) "math.js", Str ":"], CodeBlock ("", ["javascript"], []) "function add(a, b) {
  return a + b;
}

function getGrade(score) {
  if (score >= 90) return \"A\";
  if (score >= 80) return \"B\";
  if (score >= 70) return \"C\";
  if (score >= 60) return \"D\";
  return \"F\";
}

module.exports = { add, getGrade };
", Para [Str "Create ", Code ("", [], []) "math.test.js", Str ":"], CodeBlock ("", ["javascript"], []) "const test = require(\"node:test\");
const assert = require(\"node:assert/strict\");
const { add, getGrade } = require(\"./math\");

test(\"add returns the sum\", () => {
  assert.equal(add(5, 3), 8);
  assert.equal(add(-5, -3), -8);
  assert.equal(add(0, 7), 7);
});

test(\"getGrade follows shared thresholds\", () => {
  assert.equal(getGrade(90), \"A\");
  assert.equal(getGrade(82), \"B\");
  assert.equal(getGrade(76), \"C\");
  assert.equal(getGrade(60), \"D\");
  assert.equal(getGrade(59), \"F\");
});
", Para [Str "Run with ", Code ("", [], []) "node --test", Str "."], Para [Str "Expected result: two passing tests and zero failures."], Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The Node.js test runner reports two passing tests and no failures when add() and getGrade() satisfy the stated contracts."], Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Testing only one typical value and ignoring boundaries."]], [Plain [Str "Writing assertions that merely repeat the implementation."]], [Plain [Str "Forgetting to export the function being tested."]], [Plain [Str "Making tests depend on execution order or shared mutable state."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Add tests for the canonical scores 82, 91, 76, and 88."]], [Plain [Str "Add boundary tests for every grade threshold."]], [Plain [Str "Add a test for invalid scores and decide what the function contract should be."]], [Plain [Str "Run the test file from the terminal and interpret the pass/fail summary."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read each test name and assertion result. Ensure failures identify the expected and actual values in text."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a test with ", Code ("", [], []) "node:test", Str "."]], [Plain [Str "\9744", Space, Str "I can assert expected values."]], [Plain [Str "\9744", Space, Str "I can test normal and boundary cases."]], [Plain [Str "\9744", Space, Str "I can run tests from the terminal."]]], Header 3 ("lesson-92-testing-a-class", ["unnumbered", "unlisted"], []) [Str "Lesson 9.2: Testing a Class"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 9, Lesson 9.2."]], [Plain [Str "Node.js documentation: Test runner and assert."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Test object construction, state changes, and methods."]], [Plain [Str "Verify both valid and invalid operations."]], [Plain [Str "Keep test cases independent."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A class test verifies observable behavior of an instance: construction, method results, valid state changes, and rejected invalid changes."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "Assume ", Code ("", [], []) "InventoryItem", Str " exposes ", Code ("", [], []) "quantity", Str ", ", Code ("", [], []) "updateQuantity()", Str ", and ", Code ("", [], []) "lineValue()", Str ". A test file can verify its public behavior:"], CodeBlock ("", ["javascript"], []) "const test = require(\"node:test\");
const assert = require(\"node:assert/strict\");
const { InventoryItem } = require(\"./inventory-item\");

test(\"inventory item updates quantity and calculates value\", () => {
  const item = new InventoryItem(\"Notebook\", 3, 2.50);
  assert.equal(item.lineValue(), 7.50);
  item.updateQuantity(5);
  assert.equal(item.lineValue(), 12.50);
});

test(\"inventory item rejects a negative quantity\", () => {
  const item = new InventoryItem(\"Pencil\", 10, 0.50);
  assert.throws(() => item.updateQuantity(-1), RangeError);
});
", Para [Str "Expected result: both tests pass when the class enforces its stated contract."], Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Both tests pass when the item value updates from $7.50 to $12.50 and a negative quantity throws RangeError."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Testing private implementation details instead of public behavior."]], [Plain [Str "Reusing one mutated instance across unrelated tests."]], [Plain [Str "Forgetting to test invalid state transitions."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Test a Notebook item with quantity 3 and unit price 2.50."]], [Plain [Str "Verify its line value after changing quantity to 5."]], [Plain [Str "Verify that a negative quantity is rejected."]], [Plain [Str "Add a test for a zero quantity and explain whether it is valid."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Give each test a descriptive name that states the behavior being verified. Avoid ambiguous test labels such as \"test 1\"."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can instantiate an object in a test."]], [Plain [Str "\9744", Space, Str "I can test a method's return value."]], [Plain [Str "\9744", Space, Str "I can test a state change."]], [Plain [Str "\9744", Space, Str "I can assert that invalid operations throw."]]], Header 3 ("lesson-93-introduction-to-random-numbers", ["unnumbered", "unlisted"], []) [Str "Lesson 9.3: Introduction to Random Numbers"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 9, Lesson 9.3."]], [Plain [Str "MDN: Math.random."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Generate random floating-point values and bounded integers."]], [Plain [Str "Select a random element from an array."]], [Plain [Str "Explain why random tests should not depend on a specific result."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Math.random() returns a pseudorandom floating-point value greater than or equal to zero and less than one. Transform it to a bounded integer with multiplication and Math.floor()."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["javascript"], []) "const randomDecimal = Math.random();
const randomInteger = Math.floor(Math.random() * 10) + 1;

const colors = [\"red\", \"blue\", \"green\"];
const randomChoice = colors[Math.floor(Math.random() * colors.length)];

console.log(`Decimal in [0, 1): ${randomDecimal >= 0 && randomDecimal < 1}`);
console.log(`Integer in 1..10: ${randomInteger >= 1 && randomInteger <= 10}`);
console.log(`Selected item is valid: ${colors.includes(randomChoice)}`);
", Para [Str "Expected output: three lines containing ", Code ("", [], []) "true", Str "; the sampled values vary on each run."], Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Each run prints true for all three range and membership checks; the sampled values may differ."], Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Assuming ", Code ("", [], []) "Math.random()", Str " can return exactly 1."]], [Plain [Str "Forgetting that ", Code ("", [], []) "Math.floor()", Str " is needed for an integer index."]], [Plain [Str "Writing a test that expects one particular random result."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Generate a random integer from 1 through 10."]], [Plain [Str "Select one of the canonical inventory item names."]], [Plain [Str "Run the program several times and observe that values vary."]], [Plain [Str "Explain why randomness makes exact-output tests unreliable without a controllable source."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Label the range and meaning of each random value. Never require a visual animation to observe a random result."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "Math.random()", Str "."]], [Plain [Str "\9744", Space, Str "I can generate a bounded integer."]], [Plain [Str "\9744", Space, Str "I can select a random array element."]], [Plain [Str "\9744", Space, Str "I can test properties of random output rather than one exact sample."]]], Header 3 ("lesson-94-analyzing-text-data", ["unnumbered", "unlisted"], []) [Str "Lesson 9.4: Analyzing Text Data"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 9, Lesson 9.4."]], [Plain [Str "MDN: String and Map."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Normalize text before analysis."]], [Plain [Str "Count words and character frequencies."]], [Plain [Str "Use a Map to store frequency counts."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Text analysis requires explicit normalization and tokenization rules. A Map stores each token and its current frequency; the regular expression in this example treats hyphenated words as separate alphabetic tokens."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["javascript"], []) "const sample = \"A student studies programming. Programming develops problem-solving skills.\";

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
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "a: 1
student: 1
studies: 1
programming: 2
develops: 1
problem: 1
solving: 1
skills: 1
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The sample produces nine tokens and eight distinct token keys; programming has frequency 2 and every other displayed token has frequency 1."], Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Counting uppercase and lowercase forms as separate words."]], [Plain [Str "Splitting on a single space and retaining punctuation."]], [Plain [Str "Assuming a simple regular expression handles every language's word boundaries."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Count the words in the canonical text sample."]], [Plain [Str "Identify the most frequent word."]], [Plain [Str "Count characters after normalizing case."]], [Plain [Str "Explain how punctuation and hyphenation affect the result."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print each word and count as a labeled pair. State the normalization rules so learners can understand why the counts have those values."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can normalize text before counting."]], [Plain [Str "\9744", Space, Str "I can tokenize a simple English text sample."]], [Plain [Str "\9744", Space, Str "I can store frequencies in a Map."]], [Plain [Str "\9744", Space, Str "I can explain limitations of a simple tokenizer."]]], Header 3 ("lesson-95-working-with-csv-data", ["unnumbered", "unlisted"], []) [Str "Lesson 9.5: Working with CSV Data"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 9, Lesson 9.5."]], [Plain [Str "npm documentation: ", Code ("", [], []) "csv-parse", Str "."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain rows, columns, headers, and records."]], [Plain [Str "Read CSV data with a standards-aware parser."]], [Plain [Str "Compute a summary from the canonical column set."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "CSV is a text format with quoting and escaping rules. Splitting every line on commas is not a correct general CSV parser because a quoted field may itself contain a comma or newline. Use a maintained parser for real CSV data. The canonical headers are ", Code ("", [], []) "student_id", Str ", ", Code ("", [], []) "first_name", Str ", ", Code ("", [], []) "last_name", Str ", ", Code ("", [], []) "score", Str ", and ", Code ("", [], []) "active", Str "."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "Install the parser with ", Code ("", [], []) "npm install csv-parse", Str ". Save a small fixture as ", Code ("", [], []) "students.csv", Str ":"], CodeBlock ("", ["csv"], []) "student_id,first_name,last_name,score,active
1,Avery,Student,91,true
2,Jordan,Lee,82,true
3,Casey,Smith,76,false
", Para [Str "Read it with ", Code ("", [], []) "csv-parse", Str ":"], CodeBlock ("", ["javascript"], []) "const fs = require(\"node:fs\");
const { parse } = require(\"csv-parse/sync\");

const records = parse(fs.readFileSync(\"students.csv\", \"utf8\"), {
  columns: true,
  skip_empty_lines: true,
  trim: true
});

const average = records.reduce((sum, row) => sum + Number(row.score), 0)
  / records.length;

console.log(`Loaded students: ${records.length}`);
console.log(`Average score: ${average.toFixed(2)}`);
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "Loaded students: 3
Average score: 83.00
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The sample CSV contains three records with scores 91, 82, and 76. The average is 83.00."], Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Splitting CSV lines on commas without handling quoted fields."]], [Plain [Str "Forgetting that parsed field values are strings until converted."]], [Plain [Str "Assuming every row contains every required column."]], [Plain [Str "Failing to handle a missing or empty file."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create a CSV with the five canonical column names."]], [Plain [Str "Load the records and print each student's name and score."]], [Plain [Str "Calculate the average score."]], [Plain [Str "Add a quoted field containing a comma and verify that the parser reads it as one field."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print one record per line with column names. Provide a textual summary of any malformed rows rather than relying on a spreadsheet's visual highlighting."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain CSV headers and records."]], [Plain [Str "\9744", Space, Str "I can parse CSV with a standards-aware library."]], [Plain [Str "\9744", Space, Str "I can convert numeric fields before calculating."]], [Plain [Str "\9744", Space, Str "I can summarize a dataset with labeled output."]]]]