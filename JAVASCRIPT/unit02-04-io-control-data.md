# Unit 2: Numbers, Input, and the Math Object

**Runtime baseline:** Examples target the current Node.js 26 LTS line (26.13.0 or a newer 26.x security/maintenance patch) and standard ECMAScript features supported by that runtime. Use explicit module mode in package.json and do not mix CommonJS and ES module syntax in one file.


---

## Lesson 2.1: The Math Object

JavaScript's built-in `Math` object provides mathematical functions and constants:

```javascript
// Constants
console.log(Math.PI);          // 3.14159265358979...
console.log(Math.E);           // 2.71828...

// Functions
console.log(Math.sqrt(25));    // 5
console.log(Math.pow(2, 10));  // 1024
console.log(Math.abs(-7.5));   // 7.5
console.log(Math.ceil(4.2));   // 5
console.log(Math.floor(4.8));  // 4
console.log(Math.round(4.5));  // 5
console.log(Math.round(4.4));  // 4
console.log(Math.max(3, 7, 1, 9, 5));  // 9
console.log(Math.min(3, 7, 1, 9, 5));  // 1

// Random number between 0 (inclusive) and 1 (exclusive)
console.log(Math.random());

// Random integer between min and max (inclusive)
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
console.log(randomInt(1, 6));  // Simulates a dice roll
```

---

## Lesson 2.2: Getting User Input in Node.js

Getting user input in Node.js requires the built-in `readline` module.

### Using `readline` (Standard Library)

```javascript
const readline = require('node:readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("What is your name? ", (name) => {
    console.log(`Hello, ${name}!`);
    rl.close();
});
```

### Promisified Input (Modern Approach)

```javascript
const readline = require('node:readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function askQuestion(prompt) {
    return new Promise((resolve) => {
        rl.question(prompt, (answer) => {
            resolve(answer);
        });
    });
}

async function main() {
    const name = await askQuestion("What is your name? ");
    const ageStr = await askQuestion("How old are you? ");
    const age = parseInt(ageStr);

    console.log(`Hello, ${name}!`);
    console.log(`Next year you will be ${age + 1} years old.`);

    rl.close();
}

main();
```

### Helper Module for Input (Reusable)

Create `input.js` once and reuse across projects:

```javascript
// input.js — save this file in your project
const readline = require('node:readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function askQuestion(prompt) {
    return new Promise((resolve) => {
        rl.question(prompt, resolve);
    });
}

function close() {
    rl.close();
}

module.exports = { askQuestion, close };
```

Usage in your main file:
```javascript
// main.js
const { askQuestion, close } = require('./input');

async function main() {
    const name = await askQuestion("Enter your name: ");
    const numStr = await askQuestion("Enter a number: ");
    const num = parseFloat(numStr);

    console.log(`Hello, ${name}!`);
    console.log(`Your number squared is: ${num ** 2}`);

    close();
}

main();
```

### Examples

**Example 2.2.1: Temperature Converter**
```javascript
const { askQuestion, close } = require('./input');

async function main() {
    const fahrenheitStr = await askQuestion("Enter temperature in Fahrenheit: ");
    const fahrenheit = parseFloat(fahrenheitStr);

    const celsius = (fahrenheit - 32) * 5 / 9;

    console.log(`${fahrenheit}°F is ${celsius.toFixed(1)}°C`);
    close();
}

main();
```

**Example 2.2.2: Circle Calculator**
```javascript
const { askQuestion, close } = require('./input');

async function main() {
    const radiusStr = await askQuestion("Enter the radius: ");
    const radius = parseFloat(radiusStr);

    const area = Math.PI * radius ** 2;
    const circumference = 2 * Math.PI * radius;

    console.log(`Area: ${area.toFixed(2)}`);
    console.log(`Circumference: ${circumference.toFixed(2)}`);
    close();
}

main();
```

### Skills Checklist
- [ ] I can use `Math` object methods and constants.
- [ ] I can get user input using the `readline` module.
- [ ] I understand `async`/`await` for asynchronous input.
- [ ] I can convert string input to numbers using `parseInt()` and `parseFloat()`.

---

# Unit 3: Control Flow — Decisions and Loops

---

## Lesson 3.1: Boolean Expressions and `if` Statements

### Comparison Operators

| Operator | Meaning | Note |
|----------|---------|------|
| `===` | Strict equal | Checks value AND type (preferred) |
| `!==` | Strict not equal | Checks value AND type (preferred) |
| `==` | Loose equal | Type coercion (avoid) |
| `!=` | Loose not equal | Type coercion (avoid) |
| `<` | Less than | |
| `>` | Greater than | |
| `<=` | Less than or equal | |
| `>=` | Greater than or equal | |

**Always use `===` and `!==`** — `==` does unexpected type conversions.

### Logical Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `&&` | AND | `age >= 18 && hasId` |
| `\|\|` | OR | `day === 'Sat' \|\| day === 'Sun'` |
| `!` | NOT | `!isRaining` |

### `if-else if-else`

```javascript
const score = 85;

if (score >= 90) {
    console.log("Grade: A");
} else if (score >= 80) {
    console.log("Grade: B");
} else if (score >= 70) {
    console.log("Grade: C");
} else {
    console.log("Grade: F");
}
```

### Ternary Operator

```javascript
const age = 20;
const status = age >= 18 ? "adult" : "minor";
console.log(status);  // "adult"
```

### `switch` Statement

```javascript
const day = "Wednesday";
switch (day) {
    case "Monday":
    case "Tuesday":
    case "Wednesday":
    case "Thursday":
    case "Friday":
        console.log("Weekday");
        break;
    case "Saturday":
    case "Sunday":
        console.log("Weekend");
        break;
    default:
        console.log("Unknown day");
}
```

### Truthy and Falsy Values

In JavaScript, the following values are **falsy** (evaluate to `false` in conditions):
- `false`, `0`, `""` (empty string), `null`, `undefined`, `NaN`

Everything else is **truthy**.

```javascript
const name = "";
if (name) {
    console.log("Name is set");
} else {
    console.log("Name is empty");  // This runs
}
```

### Examples

**Example 3.1.1: Grade Calculator**
```javascript
const { askQuestion, close } = require('./input');

async function main() {
    const scoreStr = await askQuestion("Enter your score (0-100): ");
    const score = parseInt(scoreStr);

    let grade;
    if (score >= 90) grade = "A";
    else if (score >= 80) grade = "B";
    else if (score >= 70) grade = "C";
    else if (score >= 60) grade = "D";
    else grade = "F";

    console.log(`Your grade: ${grade}`);
    close();
}

main();
```

### Skills Checklist
- [ ] I use `===` and `!==` for comparisons in JavaScript.
- [ ] I can write `if`, `else if`, and `else` statements.
- [ ] I understand truthy and falsy values.
- [ ] I can write a `switch` statement.

---

## Lesson 3.2: `for` Loops

```javascript
// Basic for loop
for (let i = 0; i < 5; i++) {
    console.log(`i = ${i}`);
}

// Counting down
for (let i = 10; i > 0; i--) {
    console.log(i);
}
console.log("Blast off!");

// for...of — iterate over array elements (like Python's for-in)
const fruits = ["apple", "banana", "cherry"];
for (const fruit of fruits) {
    console.log(`I like ${fruit}.`);
}

// for...in — iterate over object keys
const person = { name: "Alice", age: 15, city: "Portland" };
for (const key in person) {
    console.log(`${key}: ${person[key]}`);
}
```

### `Array.forEach()`

```javascript
const numbers = [1, 2, 3, 4, 5];

numbers.forEach((num) => {
    console.log(num * 2);
});

// With index
numbers.forEach((num, index) => {
    console.log(`Index ${index}: ${num}`);
});
```

### Examples

**Example 3.2.1: Multiplication Table**
```javascript
const n = 5;
console.log(`Multiplication table for ${n}:`);
for (let i = 1; i <= 10; i++) {
    console.log(`${n} x ${i} = ${n * i}`);
}
```

### Skills Checklist
- [ ] I can write a `for` loop with initialization, condition, and update.
- [ ] I can use `for...of` to iterate over arrays.
- [ ] I can use `for...in` to iterate over object keys.
- [ ] I can use `Array.forEach()`.

---

## Lesson 3.3: `while` Loops

```javascript
let count = 1;
while (count <= 5) {
    console.log(`Count: ${count}`);
    count++;
}

// do-while — runs at least once
let num;
do {
    num = Math.floor(Math.random() * 10);
    console.log(`Rolled: ${num}`);
} while (num < 5);
```

### `break` and `continue`

```javascript
// break — exit entirely
for (let i = 0; i < 10; i++) {
    if (i === 5) break;
    console.log(i);   // Prints 0-4
}

// continue — skip iteration
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) continue;
    console.log(i);   // Prints 1, 3, 5, 7, 9
}
```

### Skills Checklist
- [ ] I can write `while` and `do-while` loops.
- [ ] I can use `break` and `continue` appropriately.

---

# Unit 4: Data Structures — Arrays and Objects

---

## Lesson 4.1: Arrays

### Creating and Accessing Arrays

```javascript
const colors = ["red", "blue", "green", "yellow"];

// Access
console.log(colors[0]);           // "red"
console.log(colors[colors.length - 1]);  // "yellow"

// Modify
colors[1] = "purple";

// Check
console.log(colors.length);       // 4
console.log(colors.includes("red")); // true
console.log(colors.indexOf("green")); // 2
```

### Array Methods

```javascript
const fruits = ["apple", "banana"];

// Adding
fruits.push("cherry");          // Add to end → ["apple", "banana", "cherry"]
fruits.unshift("avocado");      // Add to start → ["avocado", "apple", "banana", "cherry"]

// Removing
const last = fruits.pop();      // Remove and return last
const first = fruits.shift();   // Remove and return first

// Slicing (non-destructive)
const sub = fruits.slice(1, 3); // Returns new array, original unchanged

// Splicing (destructive — modifies original)
fruits.splice(1, 1);            // Remove 1 element at index 1
fruits.splice(1, 0, "mango");   // Insert "mango" at index 1

// Joining
const str = fruits.join(", ");  // "apple, mango, cherry"

// Sorting
const nums = [3, 1, 4, 1, 5, 9, 2, 6];
nums.sort((a, b) => a - b);     // Ascending: [1, 1, 2, 3, 4, 5, 6, 9]
nums.sort((a, b) => b - a);     // Descending

// Reversing
const reversed = [...fruits].reverse(); // Use spread to avoid mutating original

// Concatenating
const combined = fruits.concat(nums);
```

### Functional Array Methods

These are powerful for data transformation:

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// map — transform each element, returns new array
const doubled = numbers.map(n => n * 2);
console.log(doubled);   // [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

// filter — keep elements matching condition
const evens = numbers.filter(n => n % 2 === 0);
console.log(evens);     // [2, 4, 6, 8, 10]

// reduce — combine elements into single value
const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
console.log(sum);       // 55

// find — return first matching element
const firstOver5 = numbers.find(n => n > 5);
console.log(firstOver5); // 6

// some — true if any element matches
const hasEven = numbers.some(n => n % 2 === 0);
console.log(hasEven);    // true

// every — true if all elements match
const allPositive = numbers.every(n => n > 0);
console.log(allPositive); // true

// Chaining
const result = numbers
    .filter(n => n % 2 === 0)
    .map(n => n ** 2)
    .reduce((sum, n) => sum + n, 0);
console.log(result);    // 220  (4+16+36+64+100)
```

### Examples

**Example 4.1.1: Array Analysis**
```javascript
const scores = [85, 92, 78, 95, 88, 72, 90, 83];

const average = scores.reduce((sum, s) => sum + s, 0) / scores.length;
const max = Math.max(...scores);
const min = Math.min(...scores);
const passing = scores.filter(s => s >= 80);

console.log(`Scores: ${scores.join(', ')}`);
console.log(`Average: ${average.toFixed(1)}`);
console.log(`Highest: ${max}`);
console.log(`Lowest: ${min}`);
console.log(`Passing (>=80): ${passing.length} students`);
```

### Skills Checklist
- [ ] I can create, access, and modify arrays.
- [ ] I can use `push`, `pop`, `shift`, `unshift`, `splice`, and `slice`.
- [ ] I can use `map`, `filter`, and `reduce`.
- [ ] I can sort arrays using a comparator function.

---

## Lesson 4.2: Objects

### Creating and Using Objects

Objects in JavaScript are like Python dictionaries and Java Maps combined with class instances.

```javascript
// Object literal
const studentProfile = {
    name: "Emily",
    age: 13,
    grade: "7th",
    favoriteSubject: "Science"
};

// Access properties
console.log(studentProfile.name);          // "Emily" (dot notation)
console.log(studentProfile["age"]);         // 13 (bracket notation)

// Add/modify
studentProfile.city = "Springfield";
studentProfile.age = 14;

// Delete
delete studentProfile.grade;

// Check if property exists
console.log("name" in studentProfile);      // true
console.log(studentProfile.hasOwnProperty("city")); // true

// Get keys, values, entries
console.log(Object.keys(studentProfile));
console.log(Object.values(studentProfile));
console.log(Object.entries(studentProfile));
```

### Iterating Over Objects

```javascript
const inventory = { apples: 50, bananas: 30, oranges: 40 };

// for...in
for (const key in inventory) {
    console.log(`${key}: ${inventory[key]}`);
}

// Object.entries() with destructuring
for (const [key, value] of Object.entries(inventory)) {
    console.log(`${key}: ${value} in stock`);
}
```

### Nested Objects and Arrays

```javascript
const library = {
    name: "City Library",
    location: "Downtown",
    books: [
        { title: "Dune", author: "Frank Herbert", available: true },
        { title: "1984", author: "George Orwell", available: false }
    ]
};

// Access nested data
console.log(library.books[0].title);        // "Dune"
console.log(library.books[1].author);       // "George Orwell"

// Filter available books
const available = library.books.filter(book => book.available);
console.log(`Available: ${available.map(b => b.title).join(', ')}`);
```

### Destructuring

```javascript
// Object destructuring
const { name, age } = studentProfile;
console.log(name, age);   // "Emily" 13

// With renaming
const { name: studentName, favoriteSubject: subject } = studentProfile;

// Array destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
console.log(first);  // 1
console.log(rest);   // [3, 4, 5]

// In function parameters
function printStudent({ name, age, grade }) {
    console.log(`${name} | Age: ${age} | Grade: ${grade}`);
}
printStudent(studentProfile);
```

### Spread and Rest Operators

```javascript
// Spread — expand array or object
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];   // [1, 2, 3, 4, 5, 6]

const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const merged = { ...obj1, ...obj2 };   // { a: 1, b: 2, c: 3, d: 4 }

// Copy without mutating
const originalArr = [1, 2, 3];
const copyArr = [...originalArr];

const originalObj = { name: "Alice" };
const copyObj = { ...originalObj };
```

### Skills Checklist
- [ ] I can create, access, modify, and delete object properties.
- [ ] I can iterate over objects using `for...in` and `Object.entries()`.
- [ ] I can work with nested objects and arrays.
- [ ] I can use destructuring assignment.
- [ ] I can use spread and rest operators.
