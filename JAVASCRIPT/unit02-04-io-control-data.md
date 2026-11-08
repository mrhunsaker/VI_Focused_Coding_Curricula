# Unit 2: Numeric Computations and Input/Output

**Runtime baseline:** Node.js 26.x. Examples use built-in ECMAScript and Node.js APIs; no third-party package is required for these lessons.

## Overview
This unit follows the same design, expression, input/output, numeric-conversion, and mathematics sequence as the Python course. Use the shared bill of $24.50 and tip rate of 0.15, the student profile Avery (age 16, height 1.72 m), and the coordinates (3, 4). JavaScript is dynamically typed; input from a terminal arrives as text and must be converted and validated before arithmetic.

## Lesson 2.1: The Software Development Process

### Reading References
- Python source counterpart: Unit 2, Lesson 2.1.
- MDN: JavaScript Guide, Grammar and Types.

### Learning Objectives
- Separate problem analysis, design, implementation, and testing.
- Identify inputs, outputs, assumptions, and boundary cases before coding.
- Write language-neutral pseudocode before JavaScript.

### Concept Explanation
Use the same three-phase cycle for every language: **design**, **implement**, and **test/debug**. For a tip calculator, inputs are bill amount and tip rate; outputs are tip amount and total. State assumptions explicitly: the bill is nonnegative, the rate is a decimal fraction, and money is displayed to two decimal places. Pseudocode should describe the calculation without depending on JavaScript syntax.

### Worked Example
Pseudocode:
```text
GET bill amount
GET tip rate
CALCULATE tip = bill amount * tip rate
CALCULATE total = bill amount + tip
DISPLAY tip and total to two decimal places
```

JavaScript implementation using the canonical values:
```javascript
const bill = 24.50;
const tipRate = 0.15;
const tip = bill * tipRate;
const total = bill + tip;

console.log(`Tip: $${tip.toFixed(2)}`);
console.log(`Total: $${total.toFixed(2)}`);
```

Expected output:
```text
Tip: $3.67
Total: $28.18
```

### Expected Behavior or Output
The canonical bill of $24.50 at a 0.15 rate produces a displayed tip of $3.67 and total of $28.18 with JavaScript's binary floating-point and `toFixed(2)` behavior.

### Common Mistakes
- Coding before deciding what the program should accept and display.
- Treating 15 as equivalent to 0.15 for a percentage rate.
- Forgetting to test zero, negative, and unusually large inputs.
- Rounding intermediate values when only the displayed result needs formatting.

### Activities
1. Write input/output tables for the tip calculator before coding.
2. Add a test case for a $0.00 bill and explain its expected result.
3. Change the tip rate to 0.20 and predict the output before running the program.
4. Describe one invalid input and the validation rule that should reject it.

### Accessibility Practice
Read the pseudocode and output in order. Use explicit labels for each displayed amount; do not rely on alignment, color, or visual placement to communicate which value is the tip and which is the total.

### Skills Checklist
- [ ] I can identify a program's inputs, outputs, assumptions, and edge cases.
- [ ] I can write pseudocode independently of JavaScript syntax.
- [ ] I can distinguish design, implementation, and testing.
- [ ] I can explain why expected results should be predicted before execution.

---

## Lesson 2.2: Expressions and Assignment

### Reading References
- Python source counterpart: Unit 2, Lesson 2.2.
- MDN: Expressions and operators.

### Learning Objectives
- Evaluate arithmetic expressions using precedence and parentheses.
- Assign and update variables with clear, predictable statements.
- Explain the difference between `=`, `===`, and arithmetic operators.

### Concept Explanation
An expression produces a value. An assignment stores a value in a variable. JavaScript evaluates multiplication and division before addition and subtraction; parentheses make intended grouping explicit. Use `===` for strict equality in beginner examples so that JavaScript does not silently coerce unlike types during comparison.

### Worked Example
```javascript
let score = 10;
score = score + 5;
const subtotal = 3 * 4 + 2;
const grouped = 3 * (4 + 2);

console.log(`Score: ${score}`);
console.log(`Subtotal: ${subtotal}`);
console.log(`Grouped: ${grouped}`);
console.log(`Is score 15? ${score === 15}`);
```

Expected output:
```text
Score: 15
Subtotal: 14
Grouped: 18
Is score 15? true
```

### Expected Behavior or Output
The program prints score 15, subtotal 14, grouped result 18, and strict comparison result true.

### Common Mistakes
- Using `=` when a comparison with `===` is intended.
- Forgetting that `const` prevents reassignment of the binding.
- Assuming arithmetic with a string will always behave like arithmetic with a number.
- Omitting parentheses when they would make a multi-step expression easier to audit.

### Activities
1. Predict and then verify `8 + 4 * 2` and `(8 + 4) * 2`.
2. Update a score from 82 by adding 9, then print the new value.
3. Create a bill expression with a 15% tip using the canonical $24.50 bill.
4. Explain why `"15" === 15` evaluates to false.

### Accessibility Practice
When reading code aloud, identify parentheses, operators, and assignment separately. Keep one calculation per line when that makes the sequence easier to navigate.

### Skills Checklist
- [ ] I can evaluate expressions using operator precedence.
- [ ] I can use parentheses to control grouping.
- [ ] I can update a variable with `let`.
- [ ] I can explain assignment versus strict equality.

---

## Lesson 2.3: Input and Output Revisited

### Reading References
- Python source counterpart: Unit 2, Lesson 2.3.
- Node.js documentation: readline.

### Learning Objectives
- Read terminal input with Node.js `readline/promises`.
- Explain that terminal input is returned as a string.
- Display a greeting and the sum of two validated numeric inputs.

### Concept Explanation
Unlike Python's built-in `input()`, Node.js uses an input API. The `readline/promises` module provides an asynchronous `question()` method. It returns text, so numeric input must be converted and checked. Always close the interface so the process can exit cleanly.

### Worked Example
Save as `sum-input.js` and run with `node sum-input.js`:

```javascript
const readline = require("node:readline/promises");
const { stdin, stdout } = require("node:process");

async function main() {
  const rl = readline.createInterface({ input: stdin, output: stdout });
  try {
    const name = await rl.question("What is your name? ");
    const firstText = await rl.question("Enter the first number: ");
    const secondText = await rl.question("Enter the second number: ");
    const first = Number(firstText);
    const second = Number(secondText);

    if (firstText.trim() === "" || secondText.trim() === ""
        || !Number.isFinite(first) || !Number.isFinite(second)) {
      console.log("Error: enter two valid numbers.");
      return;
    }

    console.log(`Hello, ${name}!`);
    console.log(`Sum: ${first + second}`);
  } finally {
    rl.close();
  }
}

main();
```

Example interaction:
```text
What is your name? Avery
Enter the first number: 12
Enter the second number: 8
Hello, Avery!
Sum: 20
```

### Expected Behavior or Output
For inputs Avery, 12, and 8, the program prints `Hello, Avery!` and `Sum: 20`. Blank or nonnumeric input produces the validation message.

### Common Mistakes
- Adding two input strings and getting concatenation instead of numeric addition.
- Treating `Number("")` as invalid even though it evaluates to zero; validate blank text explicitly.
- Forgetting to await `question()`.
- Leaving the readline interface open.

### Activities
1. Run the example with the name Avery and numbers 12 and 8.
2. Enter a blank value and confirm that the validation message appears.
3. Enter a decimal and a negative number; explain why both are valid numeric values.
4. Change the program to ask for the canonical age 16 and print the year of birth only after asking for a reference year.

### Accessibility Practice
Use prompts that state exactly what input is expected. Announce the full error message and re-prompt when extending this example. Keep the interaction linear and keyboard-only.

### Skills Checklist
- [ ] I can create a Node.js readline interface.
- [ ] I can read terminal input asynchronously.
- [ ] I can convert and validate numeric text.
- [ ] I can close the interface in a `finally` block.

---

## Lesson 2.4: Computing with Numbers and Type Conversions

### Reading References
- Python source counterpart: Unit 2, Lesson 2.4.
- MDN: Number, Number.isFinite, and Number.isInteger.

### Learning Objectives
- Distinguish JavaScript numbers from numeric strings.
- Convert text using `Number()` and parse integer text when appropriate.
- Detect invalid numeric values, including `NaN`.

### Concept Explanation
JavaScript has one ordinary `Number` type for integers and floating-point values. It uses IEEE 754 double-precision floating-point arithmetic. `Number("16")` returns 16; `Number("sixteen")` returns `NaN`. `parseInt()` parses an integer prefix, so it should not be used as a substitute for strict validation. Use `Number.isFinite()` to reject `NaN` and infinities.

### Worked Example
```javascript
const ageText = "16";
const heightText = "1.72";
const age = Number(ageText);
const height = Number(heightText);

console.log(`Age next year: ${age + 1}`);
console.log(`Height in centimeters: ${(height * 100).toFixed(0)}`);
console.log(`Is age valid? ${Number.isInteger(age) && age >= 0}`);
console.log(`Is 'sixteen' valid? ${Number.isFinite(Number("sixteen"))}`);
```

Expected output:
```text
Age next year: 17
Height in centimeters: 172
Is age valid? true
Is 'sixteen' valid? false
```

### Expected Behavior or Output
The program prints age next year 17, height 172 centimetres, a valid age result of true, and an invalid numeric-text result of false.

### Common Mistakes
- Assuming JavaScript separates integers and floats into different primitive types.
- Forgetting that `typeof NaN` is `"number"`.
- Using `parseInt("12abc")` and accepting the partial result 12 without checking the entire input.
- Comparing floating-point calculations for exact equality when a tolerance is needed.

### Activities
1. Convert the canonical age text `"16"` and height text `"1.72"` to numbers.
2. Convert `"abc"` and `""`; explain why blank input needs separate validation.
3. Calculate the bill total from $24.50 and a 0.15 tip rate.
4. Test whether 3.5 is an integer and whether `Infinity` is finite.

### Accessibility Practice
Use textual labels that name the value and its unit. State why a conversion failed rather than only printing `NaN`.

### Skills Checklist
- [ ] I can convert numeric strings with `Number()`.
- [ ] I can detect invalid numeric values with `Number.isFinite()`.
- [ ] I can distinguish integers from non-integer numbers.
- [ ] I can explain JavaScript's single ordinary Number type.

---

## Lesson 2.5: Using the Math Object

### Reading References
- Python source counterpart: Unit 2, Lesson 2.5.
- MDN: Math.

### Learning Objectives
- Use `Math.PI`, `Math.sqrt()`, `Math.ceil()`, and `Math.floor()`.
- Calculate circle area and circumference.
- Calculate distance from the origin using the canonical coordinates (3, 4).

### Concept Explanation
JavaScript's built-in `Math` object provides mathematical constants and functions. It is used directly; it is not imported. `Math.PI` is the value of pi, `Math.sqrt()` calculates a square root, `Math.ceil()` rounds upward, and `Math.floor()` rounds downward.

### Worked Example
```javascript
const radius = 5;
const area = Math.PI * radius ** 2;
const circumference = 2 * Math.PI * radius;

const x = 3;
const y = 4;
const distance = Math.sqrt(x ** 2 + y ** 2);

console.log(`Area: ${area.toFixed(2)}`);
console.log(`Circumference: ${circumference.toFixed(2)}`);
console.log(`Distance from origin: ${distance.toFixed(2)}`);
console.log(`Ceiling of 4.2: ${Math.ceil(4.2)}`);
console.log(`Floor of 4.8: ${Math.floor(4.8)}`);
```

Expected output:
```text
Area: 78.54
Circumference: 31.42
Distance from origin: 5.00
Ceiling of 4.2: 5
Floor of 4.8: 4
```

### Expected Behavior or Output
For radius 5 and coordinates (3, 4), the program prints area 78.54, circumference 31.42, distance 5.00, ceiling 5, and floor 4.

### Common Mistakes
- Writing `Math.pi` instead of the case-sensitive `Math.PI`.
- Calling `Math.sqrt` without parentheses.
- Confusing `Math.round()` with ceiling or floor.
- Forgetting that `toFixed()` returns a string for display.

### Activities
1. Calculate the area and circumference of a circle with radius 5.
2. Calculate the distance from (3, 4) to the origin.
3. Predict the results of `Math.ceil(2.01)` and `Math.floor(2.99)`.
4. Change the radius to 2.5 and report both results to two decimal places.

### Accessibility Practice
Read each result with its label. Preserve units in prompts and output. Ensure mathematical notation is also explained in words when students are using a screen reader or braille display.

### Skills Checklist
- [ ] I can use `Math.PI` and `Math.sqrt()`.
- [ ] I can calculate circle area and circumference.
- [ ] I can calculate distance from the origin.
- [ ] I can distinguish ceiling, floor, and rounding.

# Unit 3: Control Flow — Decisions, Lists, and Strings

## Overview
This unit follows the Python sequence of Boolean reasoning, chained conditionals, arrays, iteration, and string operations. Use the shared grade thresholds and score list throughout.

## Lesson 3.1: Boolean Expressions and `if` Statements

### Reading References
- Python source counterpart: Unit 3, Lesson 3.1.
- MDN: Expressions and operators.

### Learning Objectives
- Compare values with relational operators.
- Combine conditions with `&&`, `||`, and `!`.
- Use an `if` statement to make a decision.

### Concept Explanation
JavaScript Boolean values are `true` and `false`. Use strict equality (`===`) to avoid implicit type conversion during comparisons. Logical AND (`&&`) requires both conditions to be true; logical OR (`||`) requires at least one; logical NOT (`!`) reverses a Boolean value.

### Worked Example
```javascript
const score = 82;
const isPassing = score >= 60;
const isValid = score >= 0 && score <= 100;

if (isValid && isPassing) {
  console.log("Valid passing score.");
} else {
  console.log("Score is invalid or not passing.");
}
```

Expected output:
```text
Valid passing score.
```

### Expected Behavior or Output
With score 82, the program prints `Valid passing score.` because the score is between 0 and 100 and at least 60.

### Common Mistakes
- Using `=` instead of `===` in a comparison.
- Confusing `&&` with `||`.
- Forgetting that JavaScript conditions can use truthy/falsy values, not only Booleans.

### Activities
1. Test whether each canonical score is at least 60.
2. Write a condition that accepts scores from 0 through 100.
3. Compare `0`, `"0"`, `""`, and `null` using strict equality.
4. Explain the result of `true && false` and `true || false`.

### Accessibility Practice
Print the score and decision as a complete sentence. Do not use color alone to indicate pass/fail.

### Skills Checklist
- [ ] I can use relational operators.
- [ ] I can combine conditions with logical operators.
- [ ] I can write an if/else statement.
- [ ] I can explain strict equality.

## Lesson 3.2: Chained Conditionals (`else if`, `else`)

### Concept Explanation
A chained conditional evaluates branches in order and runs the first matching branch. JavaScript uses `else if` for intermediate alternatives. The shared thresholds are A at 90, B at 80, C at 70, D at 60, and F below 60.

