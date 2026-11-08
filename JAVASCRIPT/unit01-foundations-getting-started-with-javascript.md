# Unit 1: Foundations — Getting Started with JavaScript

## Overview

This unit covers JavaScript fundamentals: variables, data types, and basic output.

---

## Lesson 1.1: Welcome to Computer Science

*(See Python Unit 1.1 for conceptual content — hardware, software, algorithms, and problem-solving are language-agnostic.)*

### Reading References
<<<<<<< HEAD
- Python source counterpart: Unit 1, Lesson 1.1.
- MDN: Introduction to JavaScript.

### Concept Explanation
Computer science studies computational problem-solving: representing information, designing algorithms, and evaluating solutions. JavaScript is a programming language; Node.js and web browsers are different runtime environments that host JavaScript code.

### JavaScript's Role
=======

- Python source counterpart: Unit 1, Lesson 1.1.
- MDN: Introduction to JavaScript.

### Learning Objectives

- Define computer science as the study of computational problem-solving.
- Distinguish hardware from software.
- Describe JavaScript's role in browser and server-side programming.

### Concept Explanation

Computer science studies computational problem-solving: representing information, designing algorithms, and evaluating solutions. JavaScript is a programming language; Node.js and web browsers are different runtime environments that host JavaScript code.

#### JavaScript's Role
>>>>>>> 2067a20 (curriculum clearning and updates)

JavaScript was created by Brendan Eich at Netscape in 1995. Originally just for web browsers, it now runs everywhere thanks to Node.js (2009).

---

<<<<<<< HEAD
### Learning Objectives
- Define computer science as the study of computational problem-solving.
- Distinguish hardware from software.
- Describe JavaScript's role in browser and server-side programming.

### Worked Example
A simple algorithm for preparing a school day can be written as ordered steps: check the schedule, pack required materials, travel to school, and attend the first class. A computer program expresses a precise algorithm so that a machine can execute it consistently.

### Expected Behavior or Output
Students can explain the difference between a physical computer component and a program, and identify that JavaScript code can run in a browser or in Node.js.

### Common Mistakes
- Defining computer science as only learning a programming language.
- Confusing a browser with JavaScript itself.
- Assuming JavaScript running in Node.js has browser APIs such as document and window.

### Activities
1. Identify three hardware components and three software examples.
2. Describe an everyday task as an ordered algorithm.
3. Compare JavaScript in a browser with JavaScript in Node.js.
4. Explain why this course starts with terminal programs.

### Accessibility Practice
Describe hardware and software with textual examples. Do not require interpreting a diagram as the only way to understand system components.

### Skills Checklist
- [ ] I can define computer science.
- [ ] I can distinguish hardware and software.
- [ ] I can describe JavaScript's browser and Node.js environments.
- [ ] I can express a simple task as an algorithm.


## Lesson 1.2: Your First JavaScript Program — Hello World

### Reading References
- Python source counterpart: Unit 1, Lesson 1.2.
- MDN: JavaScript first steps.

### Learning Objectives
- Write and run a minimal JavaScript program.
- Explain sequential execution and console output.
- Run the same file from the terminal.

### Concept Explanation
A JavaScript program is a sequence of instructions. Node.js executes statements in order. The `console.log()` function writes text to standard output. JavaScript statements are commonly separated by line breaks and may optionally end with semicolons; this course uses semicolons consistently.

### Worked Example
Save as `hello.js`:
```javascript
console.log("Hello, World!");
console.log("Welcome to JavaScript.");
```

Run with `node hello.js`.

Expected output:
```text
Hello, World!
Welcome to JavaScript.
```

### Expected Behavior or Output
Running `node hello.js` prints `Hello, World!` followed by `Welcome to JavaScript.` on the next line.

### Common Mistakes
- Saving the file with the wrong extension.
- Running Node.js from a directory that does not contain the file.
- Misspelling the case-sensitive function name `console.log`.

### Activities
1. Type and run the two-line program.
2. Add a third line that prints your name.
3. Change the greeting and predict the output before running.
4. Run the program from a different directory and diagnose the error.

### Accessibility Practice
Use the terminal and keyboard to create, save, and run the file. Read the output sequentially and confirm the file name and extension.

### Skills Checklist
- [ ] I can create a JavaScript source file.
- [ ] I can print text with `console.log()`.
- [ ] I can run a file with `node`.
- [ ] I can explain sequential execution.

## Lesson 1.3: Variables and Simple Data Types
=======
### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)

A simple algorithm for preparing a school day can be written as ordered steps: check the schedule, pack required materials, travel to school, and attend the first class. A computer program expresses a precise algorithm so that a machine can execute it consistently.

### Expected Behavior or Output

Students can explain the difference between a physical computer component and a program, and identify that JavaScript code can run in a browser or in Node.js.

### Common Mistakes

- Defining computer science as only learning a programming language.
- Confusing a browser with JavaScript itself.
- Assuming JavaScript running in Node.js has browser APIs such as document and window.

### Activities

1. Identify three hardware components and three software examples.
2. Describe an everyday task as an ordered algorithm.
3. Compare JavaScript in a browser with JavaScript in Node.js.
4. Explain why this course starts with terminal programs.

### Accessibility Practice

Describe hardware and software with textual examples. Do not require interpreting a diagram as the only way to understand system components.

### Skills Checklist

- [ ] I can define computer science.
- [ ] I can distinguish hardware and software.
- [ ] I can describe JavaScript's browser and Node.js environments.
- [ ] I can express a simple task as an algorithm.

## Lesson 1.2: Your First JavaScript Program — Hello World

### Reading References
- Python source counterpart: Unit 1, Lesson 1.2.
- MDN: JavaScript first steps.

### Learning Objectives
- Write and run a minimal JavaScript program.
- Explain sequential execution and console output.
- Run the same file from the terminal.

### Concept Explanation
A JavaScript program is a sequence of instructions. Node.js executes statements in order. The `console.log()` function writes text to standard output. JavaScript statements are commonly separated by line breaks and may optionally end with semicolons; this course uses semicolons consistently.

### Worked Example
Save as `hello.js`:
```javascript
console.log("Hello, World!");
console.log("Welcome to JavaScript.");
```

Run with `node hello.js`.

Expected output:
```text
Hello, World!
Welcome to JavaScript.
```

### Expected Behavior or Output
Running `node hello.js` prints `Hello, World!` followed by `Welcome to JavaScript.` on the next line.

### Common Mistakes
- Saving the file with the wrong extension.
- Running Node.js from a directory that does not contain the file.
- Misspelling the case-sensitive function name `console.log`.

### Activities
1. Type and run the two-line program.
2. Add a third line that prints your name.
3. Change the greeting and predict the output before running.
4. Run the program from a different directory and diagnose the error.

### Accessibility Practice
Use the terminal and keyboard to create, save, and run the file. Read the output sequentially and confirm the file name and extension.

### Skills Checklist
- [ ] I can create a JavaScript source file.
- [ ] I can print text with `console.log()`.
- [ ] I can run a file with `node`.
- [ ] I can explain sequential execution.

## Lesson 1.3: Variables and Simple Data Types

### Reading References

- Python source counterpart: Unit 1, Lesson 1.3.
- MDN: JavaScript data types and structures.

### Learning Objectives

- Declare variables with `const` and `let`.
- Store strings, numbers, and Booleans.
- Explain JavaScript's dynamic typing and primitive values.

### Concept Explanation

A variable name refers to a value. Use `const` when the binding will not be reassigned and `let` when reassignment is required. JavaScript is dynamically typed: a variable can refer to values of different types over time.

#### `console.log()`

```javascript
console.log("Hello, World!");
console.log(42);
console.log(true);
console.log("Value:", 42, "and", "text");
```

#### Declaring Variables

JavaScript has three ways to declare variables:

| Keyword | Scope | Reassignable | Use When |
|---------|-------|-------------|----------|
| `const` | Block | No | Value won't change (default choice) |
| `let` | Block | Yes | Value will change |
| `var` | Function | Yes | Legacy — avoid in modern code |

```javascript
const PI = 3.14159;               // Cannot be reassigned
let score = 100;                  // Can change
score = 150;                      // OK

// var is function-scoped (legacy)
var oldWay = "avoid this";
```

**Best practice:** Use `const` by default; use `let` only when you need to reassign.

#### Template Literals

```javascript
const name = "Alice";
const age = 15;

// Template literal (backticks — preferred)
console.log(`Hello, ${name}! You are ${age} years old.`);

// Concatenation (older style)
console.log("Hello, " + name + "! You are " + age + " years old.");
```

#### Additional Primitive Types and Type Conversion


<<<<<<< HEAD
### Additional Primitive Types and Type Conversion

### Reading References
- Python source counterpart: Unit 1, Lesson 1.3.
- MDN: JavaScript data types and structures.

### Learning Objectives
- Declare variables with `const` and `let`.
- Store strings, numbers, and Booleans.
- Explain JavaScript's dynamic typing and primitive values.

### Concept Explanation
A variable name refers to a value. Use `const` when the binding will not be reassigned and `let` when reassignment is required. JavaScript is dynamically typed: a variable can refer to values of different types over time.
=======
>>>>>>> 2067a20 (curriculum clearning and updates)

#### Primitive Types

```javascript
// Number (integers and floats use the same type)
let integer = 42;
let decimal = 3.14;
let negative = -10;

// String
let name = "Alice";
let greeting = 'Hello';
let multiLine = `Line 1
Line 2`;

// Boolean
let isRaining = false;
let isLoggedIn = true;

// null (intentional absence of value)
let emptyValue = null;

// undefined (value not assigned)
let notAssigned;
console.log(notAssigned);  // undefined

// Check type
console.log(typeof 42);           // "number"
console.log(typeof "hello");      // "string"
console.log(typeof true);         // "boolean"
console.log(typeof null);         // "object" (known quirk!)
console.log(typeof undefined);    // "undefined"
```

#### Arithmetic Operators

```javascript
console.log(5 + 3);   // 8
console.log(10 - 4);  // 6
console.log(7 * 6);   // 42
console.log(15 / 4);  // 3.75  (always decimal, unlike Python 2 or Java)
console.log(10 % 3);  // 1  (remainder)
console.log(2 ** 10); // 1024  (exponentiation)

// Math.floor for integer division equivalent
console.log(Math.floor(15 / 4));  // 3
```

#### Type Conversion

```javascript
// String to Number
let str = "123";
let num = Number(str);          // 123
let numParsed = parseInt(str);  // 123
let floatParsed = parseFloat("3.14"); // 3.14

// Number to String
let n = 42;
let s = String(n);              // "42"
let s2 = n.toString();          // "42"
let s3 = `${n}`;               // "42" (template literal)

// Checking
console.log(isNaN("abc"));     // true — "not a number"
console.log(isNaN(42));        // false
console.log(Number("abc"));    // NaN
```

#### Constants

```javascript
const MAX_SIZE = 100;
const APP_NAME = "My App";
const PI = Math.PI;  // Use Math.PI — already defined
```

#### Examples

**Example 1.3.1: Personal Information**
```javascript
const myName = "Jamie";
const favoriteNumber = 7;
const heightInMeters = 1.75;
const likesPizza = true;

console.log(`Name: ${myName}`);
console.log(`Favorite number: ${favoriteNumber}`);
console.log(`Height: ${heightInMeters} meters`);
console.log(`Likes pizza: ${likesPizza}`);
```

**Example 1.3.2: Simple Math**
```javascript
const num1 = 15;
const num2 = 7;

console.log(`Sum: ${num1 + num2}`);
console.log(`Difference: ${num1 - num2}`);
console.log(`Product: ${num1 * num2}`);
console.log(`Quotient: ${(num1 / num2).toFixed(2)}`);
console.log(`Remainder: ${num1 % num2}`);
```

### Worked Example

```javascript
const student = { name: "Avery", age: 16, heightM: 1.72, favoriteSubject: "Computer Science" };
console.log(`${student.name}, age ${student.age}`);
console.log(`Height: ${student.heightM} m`);
```

### Expected Behavior or Output

The program prints Avery's name and age, then the height with the unit metres. The profile uses the shared canonical values.

### Common Mistakes

- Using `var` when `const` or `let` expresses the intended behavior more clearly.
- Assuming JavaScript has separate integer and floating-point primitive types.
- Confusing `null` with `undefined`.
- Assuming a conversion such as `Number("hello")` throws instead of returning `NaN`.

### Activities

**Activity 1.3.1: Area Calculator**
```javascript
const length = 12;
const width = 5;
const height = 8;

const rectangleArea = length * width;
const boxVolume = length * width * height;
const circleArea = Math.PI * (length / 2) ** 2;

console.log(`Rectangle area: ${rectangleArea}`);
console.log(`Box volume: ${boxVolume}`);
console.log(`Circle area: ${circleArea.toFixed(2)}`);
```

1. Create an Avery profile with name, age 16, height 1.72, and favorite subject Computer Science.
2. Print each property with a descriptive label.
3. Compare `typeof 16`, `typeof 1.72`, `typeof "Avery"`, and `typeof true`.
4. Convert the text `"16"` to a number and test the invalid text `"sixteen"`.

### Accessibility Practice

Use meaningful variable names and explicit output labels. Explain punctuation such as braces, commas, quotation marks, and semicolons when reading code aloud.

### Skills Checklist

- [ ] I can use `console.log()` to display output.
- [ ] I can declare variables using `const` and `let`.
- [ ] I can use template literals with `${}`.

---

- [ ] I can identify JavaScript's primitive data types.
- [ ] I can perform arithmetic operations in JavaScript.
- [ ] I understand that JavaScript's `/` always gives a decimal result.
- [ ] I can convert between types using `Number()`, `String()`, `parseInt()`.
- [ ] I understand `const` vs. `let`.

<<<<<<< HEAD
### Worked Example
```javascript
const student = { name: "Avery", age: 16, heightM: 1.72, favoriteSubject: "Computer Science" };
console.log(`${student.name}, age ${student.age}`);
console.log(`Height: ${student.heightM} m`);
```

### Common Mistakes
- Using `var` when `const` or `let` expresses the intended behavior more clearly.
- Assuming JavaScript has separate integer and floating-point primitive types.
- Confusing `null` with `undefined`.
- Assuming a conversion such as `Number("hello")` throws instead of returning `NaN`.

### Activities
1. Create an Avery profile with name, age 16, height 1.72, and favorite subject Computer Science.
2. Print each property with a descriptive label.
3. Compare `typeof 16`, `typeof 1.72`, `typeof "Avery"`, and `typeof true`.
4. Convert the text `"16"` to a number and test the invalid text `"sixteen"`.

### Accessibility Practice
Use meaningful variable names and explicit output labels. Explain punctuation such as braces, commas, quotation marks, and semicolons when reading code aloud.

### Expected Behavior or Output
The program prints Avery's name and age, then the height with the unit metres. The profile uses the shared canonical values.
=======
>>>>>>> 2067a20 (curriculum clearning and updates)
