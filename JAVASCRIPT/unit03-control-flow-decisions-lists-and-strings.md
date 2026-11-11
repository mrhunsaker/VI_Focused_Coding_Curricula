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
### Reading References

- Python source counterpart: Unit 3, Lesson 3.2.
- MDN: Conditional statements.

### Learning Objectives

- Use ordered conditional branches.
- Apply the shared A–F grade thresholds.
- Test branch boundaries.

### Concept Explanation

A chained conditional evaluates branches in order and runs the first matching branch. JavaScript uses `else if` for intermediate alternatives. The shared thresholds are A at 90, B at 80, C at 70, D at 60, and F below 60.

### Worked Example

### Reading References
- Python source counterpart: Unit 3, Lesson 3.2.
- MDN: Conditional statements.

### Learning Objectives
- Use ordered conditional branches.
- Apply the shared A–F grade thresholds.
- Test branch boundaries.

### Worked Example
```javascript
function getGrade(score) {
  if (score >= 90) {
    return "A";
  } else if (score >= 80) {
    return "B";
  } else if (score >= 70) {
    return "C";
  } else if (score >= 60) {
    return "D";
  } else {
    return "F";
  }
}

for (const score of [82, 91, 76, 88]) {
  console.log(`Score ${score}: ${getGrade(score)}`);
}
```

Expected output:
```text
Score 82: B
Score 91: A
Score 76: C
Score 88: B
```

### Expected Behavior or Output
The canonical scores are classified as 82:B, 91:A, 76:C, and 88:B.

### Common Mistakes

- Testing lower thresholds before higher ones.
- Omitting the final fallback branch.
- Failing to reject scores outside the valid range.

### Activities
1. Classify scores 82, 91, 76, and 88.
2. Test 90, 89, 80, 79, 70, 69, 60, and 59.
3. Add validation for scores below 0 or above 100.
4. Explain why branch order matters.

### Accessibility Practice
Print the numeric score and grade together, one record per line.

### Skills Checklist

- [ ] I can write chained conditionals.
- [ ] I can implement the shared grade thresholds.
- [ ] I can test boundary values.
- [ ] I can validate a score range.

## Lesson 3.3: Introduction to Arrays

### Reading References
- Python source counterpart: Unit 3, Lesson 3.3.
- MDN: Indexed collections — Arrays.

### Learning Objectives
- Create, access, and modify arrays.
- Explain zero-based indexing and `length`.
- Use the canonical scores [82, 91, 76, 88].

### Concept Explanation
JavaScript arrays are ordered and zero-indexed. The first element is at index 0; the last is at `array.length - 1`. A `const` array can still have its elements changed because `const` prevents reassignment of the binding, not mutation of the array.

### Worked Example
```javascript
const scores = [82, 91, 76, 88];
console.log(`First score: ${scores[0]}`);
console.log(`Number of scores: ${scores.length}`);
scores[2] = 80;
console.log(`Updated third score: ${scores[2]}`);
```

Expected output:
```text
First score: 82
Number of scores: 4
Updated third score: 80
```

### Expected Behavior or Output
The initial array has four values. The first score is 82; after assigning index 2 to 80, the third score is 80.

### Common Mistakes
- Using index 1 for the first element.
- Assuming `const` freezes array contents.
- Reading beyond the array and receiving `undefined`.

### Activities
1. Read all four canonical scores by index.
2. Change the third score from 76 to 80.
3. Add a fifth score of 95 and report the new length.
4. Explain the difference between an index and a one-based display number.

### Accessibility Practice
Identify values by both position and meaning. Print one score per line.

### Skills Checklist
- [ ] I can create and access an array.
- [ ] I can explain zero-based indexing.
- [ ] I can update an array element.
- [ ] I can use the length property.

## Lesson 3.4: Iterating with `for` Loops
### Concept Explanation
A `for...of` loop visits each value in an iterable collection. The loop variable holds the current score, not its array index.


### Reading References
- Python source counterpart: Unit 3, Lesson 3.4.
- MDN: Loops and iteration.

### Learning Objectives
- Iterate over arrays with `for...of`.
- Calculate a total and average.
- Compare indexed loops with value-based iteration.

### Concept Explanation

A `for...of` loop visits each value in an iterable collection. The loop variable holds the current score, not its array index.

### Worked Example

### Worked Example
```javascript
const scores = [82, 91, 76, 88];
let total = 0;

for (const score of scores) {
  total += score;
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
The canonical score list totals 337 and has an average of 84.25.

### Common Mistakes

- Confusing an array index with an array value.
- Modifying the collection while iterating without understanding the effect.
- Using `forEach()` when early termination with `break` is required.

### Activities

1. Print each canonical score using `for...of`.
2. Calculate the total and average.
3. Print each score with a one-based display number.
4. Compare `for...of`, indexed `for`, and `forEach()`.

### Accessibility Practice

Use one output line per score and include a meaningful label. Do not rely on visual alignment.

### Skills Checklist

- [ ] I can iterate over an array.
- [ ] I can calculate a total and average.
- [ ] I can use an indexed loop.
- [ ] I can choose an appropriate loop form.

## Lesson 3.5: Basic String Operations

### Reading References

- Python source counterpart: Unit 3, Lesson 3.5.
- MDN: String.

### Learning Objectives

- Concatenate strings and use template literals.
- Normalize text and search within it.
- Count string length and replace text.

### Concept Explanation

JavaScript strings are immutable. Methods such as `trim()`, `toUpperCase()`, and `toLowerCase()` return new strings. Template literals use backticks and `${expression}` interpolation.

### Worked Example

### Worked Example
```javascript
const firstName = " Avery ";
const lastName = "Student";
const fullName = `${firstName.trim()} ${lastName}`;
const sample = "A student studies programming. Programming develops problem-solving skills.";

console.log(`Name: ${fullName}`);
console.log(`Uppercase: ${fullName.toUpperCase()}`);
console.log(`Contains programming: ${sample.toLowerCase().includes("programming")}`);
console.log(`Characters in name: ${fullName.length}`);
```

Expected output:
```text
Name: Avery Student
Uppercase: AVERY STUDENT
Contains programming: true
Characters in name: 13
```

### Expected Behavior or Output
The example prints `Avery Student`, its uppercase form, true for the programming search, and a character count of 13.

### Common Mistakes

- Assuming string methods mutate the original string.
- Forgetting to save the result of `trim()` or case conversion.
- Treating UTF-16 code-unit length as the count of user-perceived characters in all Unicode text.

### Activities
1. Trim extra spaces from a name.
2. Convert the canonical text sample to lowercase.
3. Count the occurrences of the word "programming".
4. Replace "skills" with "abilities".

### Accessibility Practice
Use complete labels for string length and search results. Explain punctuation and whitespace explicitly.

### Skills Checklist

- [ ] I can concatenate strings and use template literals.
- [ ] I can trim and change case.
- [ ] I can search and replace text.
- [ ] I can describe the Unicode caveat for string length.
