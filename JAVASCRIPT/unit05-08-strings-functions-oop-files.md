# Unit 5: Strings and String Methods

**Runtime baseline:** Examples target the current Node.js 26 LTS line (26.13.0 or a newer 26.x security/maintenance patch) and standard ECMAScript features supported by that runtime. Use explicit module mode in package.json and do not mix CommonJS and ES module syntax in one file.


---

## Lesson 5.1: Working with Strings

```javascript
const name = "Alice Smith";

// Properties
console.log(name.length);              // 11

// Accessing characters
console.log(name[0]);                  // "A"
console.log(name.charAt(0));           // "A"
console.log(name[name.length - 1]);    // "h"

// Substrings
console.log(name.slice(6));            // "Smith"
console.log(name.slice(0, 5));         // "Alice"
console.log(name.substring(6, 11));    // "Smith"

// Case
console.log(name.toUpperCase());       // "ALICE SMITH"
console.log(name.toLowerCase());       // "alice smith"

// Trimming
const padded = "  hello  ";
console.log(padded.trim());            // "hello"
console.log(padded.trimStart());       // "hello  "
console.log(padded.trimEnd());         // "  hello"

// Searching
console.log(name.indexOf("Smith"));    // 6
console.log(name.lastIndexOf("l"));    // 3
console.log(name.includes("Alice"));   // true
console.log(name.startsWith("Ali"));   // true
console.log(name.endsWith("ith"));     // true

// Replacing
const result = name.replace("Alice", "Bob");  // "Bob Smith"
const allReplaced = "a,b,a,c,a".replaceAll("a", "x");  // "x,b,x,c,x"

// Splitting
const sentence = "the quick brown fox";
const words = sentence.split(" ");
console.log(words);   // ["the", "quick", "brown", "fox"]

const csv = "Alice,15,Portland";
const parts = csv.split(",");
console.log(parts);   // ["Alice", "15", "Portland"]

// Repeating and Padding
console.log("ha".repeat(3));           // "hahaha"
console.log("5".padStart(3, "0"));     // "005"
console.log("5".padEnd(3, "0"));       // "500"

// Template literals (multi-line)
const multiLine = `
Name: ${name}
Length: ${name.length}
Uppercase: ${name.toUpperCase()}
`;
console.log(multiLine);
```

### Regular Expressions (Basics)

```javascript
const text = "Hello World! Hello JavaScript!";

// Test if pattern exists
console.log(/hello/i.test(text));    // true (i = case-insensitive)

// Find matches
const matches = text.match(/Hello/g); // g = global (find all)
console.log(matches);                  // ["Hello", "Hello"]

// Replace with regex
const cleaned = text.replace(/[!]/g, ".");  // "Hello World. Hello JavaScript."

// Split with regex
const words2 = "one  two   three".split(/\s+/);
console.log(words2);   // ["one", "two", "three"]
```

### Skills Checklist
- [ ] I can use common `String` methods in JavaScript.
- [ ] I can use template literals for multi-line strings and interpolation.
- [ ] I can split strings into arrays and join arrays into strings.
- [ ] I understand basic regular expressions.

---

# Unit 6: Functions

---

## Lesson 6.1: Defining Functions

JavaScript has multiple ways to define functions:

### Function Declaration

```javascript
function greetUser() {
    console.log("Hello, JavaScript programmer!");
}

greetUser();
greetUser();
```

### Function Expression

```javascript
const greetByName = function(name) {
    console.log(`Hello, ${name}!`);
};

greetByName("Alice");
```

### Arrow Functions (ES6) — Modern Preferred Style

```javascript
// Full arrow function
const add = (a, b) => {
    return a + b;
};

// Concise body (implicit return for single expressions)
const addShort = (a, b) => a + b;

// Single parameter (no parentheses needed)
const double = n => n * 2;

// No parameters
const sayHello = () => console.log("Hello!");

console.log(add(5, 3));     // 8
console.log(addShort(5, 3)); // 8
console.log(double(7));      // 14
sayHello();
```

### Default Parameters

```javascript
function makeShirt(size, message = "I love JavaScript") {
    console.log(`Making a ${size}-sized shirt: '${message}'`);
}

makeShirt("large");                   // Uses default
makeShirt("medium", "Hello World");   // Custom message
```

### Rest Parameters

```javascript
function sum(...numbers) {
    return numbers.reduce((total, n) => total + n, 0);
}

console.log(sum(1, 2, 3));           // 6
console.log(sum(10, 20, 30, 40));    // 100
```

### Examples

**Example 6.1.1: Calculator Functions**
```javascript
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;
const multiply = (a, b) => a * b;
const divide = (a, b) => {
    if (b === 0) throw new Error("Cannot divide by zero");
    return a / b;
};

const circleArea = (radius) => Math.PI * radius ** 2;
const getGrade = (score) => {
    if (score >= 90) return "A";
    if (score >= 80) return "B";
    if (score >= 70) return "C";
    if (score >= 60) return "D";
    return "F";
};

console.log(add(5, 3));
console.log(circleArea(5).toFixed(2));
console.log(getGrade(85));
```

**Example 6.1.2: Higher-Order Functions**
```javascript
// Functions that take or return other functions

// Map using our own function
function doubleAll(numbers) {
    return numbers.map(n => n * 2);
}

// Function that returns a function (closure)
function makeAdder(x) {
    return (y) => x + y;
}

const addFive = makeAdder(5);
const addTen = makeAdder(10);

console.log(addFive(3));   // 8
console.log(addTen(3));    // 13
console.log(doubleAll([1, 2, 3, 4, 5]));
```

### Closures

```javascript
function makeCounter() {
    let count = 0;    // Private variable

    return {
        increment: () => ++count,
        decrement: () => --count,
        getCount: () => count
    };
}

const counter = makeCounter();
counter.increment();
counter.increment();
counter.increment();
counter.decrement();
console.log(counter.getCount());  // 2
```

### Skills Checklist
- [ ] I can define functions using declarations, expressions, and arrow syntax.
- [ ] I can use default and rest parameters.
- [ ] I understand closures and how they capture variables.
- [ ] I can pass functions as arguments and return them.

---

# Unit 7: Classes and Object-Oriented Programming

---

## Lesson 7.1: Classes in JavaScript

JavaScript uses prototype-based inheritance, but ES6 `class` syntax provides a familiar OOP style.

### Class Syntax

```javascript
class Dog {
    // Instance variables declared in constructor
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    // Methods
    sit() {
        console.log(`${this.name} is now sitting.`);
    }

    rollOver() {
        console.log(`${this.name} rolled over!`);
    }

    getOlder(years) {
        this.age += years;
        console.log(`${this.name} is now ${this.age} years old.`);
    }

    // Getter
    get info() {
        return `${this.name} (${this.age} years old)`;
    }

    // toString equivalent
    toString() {
        return `Dog { name: '${this.name}', age: ${this.age} }`;
    }
}

// Create instances
const myDog = new Dog("Buddy", 3);
const yourDog = new Dog("Lucy", 1);

myDog.sit();
myDog.getOlder(2);
console.log(myDog.info);        // Uses getter
console.log(myDog.toString());
```

### Private Fields (ES2022)

```javascript
class BankAccount {
    #balance;   // Private field — only accessible within the class

    constructor(initialBalance) {
        this.#balance = initialBalance;
    }

    deposit(amount) {
        if (amount > 0) {
            this.#balance += amount;
            console.log(`Deposited $${amount}. New balance: $${this.#balance}`);
        }
    }

    withdraw(amount) {
        if (amount > this.#balance) {
            console.log("Insufficient funds!");
        } else {
            this.#balance -= amount;
            console.log(`Withdrew $${amount}. New balance: $${this.#balance}`);
        }
    }

    get balance() {
        return this.#balance;
    }
}

const account = new BankAccount(1000);
account.deposit(500);
account.withdraw(200);
console.log(`Balance: $${account.balance}`);
```

### Static Methods

```javascript
class MathHelper {
    static add(a, b) { return a + b; }
    static multiply(a, b) { return a * b; }
    static PI = 3.14159265358979;
}

// Call without creating an instance
console.log(MathHelper.add(5, 3));
console.log(MathHelper.PI);
```

---

## Lesson 7.2: Inheritance

```javascript
class Vehicle {
    constructor(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.odometer = 0;
    }

    getDescriptiveName() {
        return `${this.year} ${this.make} ${this.model}`;
    }

    readOdometer() {
        console.log(`This vehicle has ${this.odometer} miles on it.`);
    }
}

class Car extends Vehicle {
    constructor(make, model, year) {
        super(make, model, year);   // Call parent constructor
        this.numDoors = 4;
    }

    readOdometer() {                // Override parent method
        console.log(`This car has ${this.odometer} miles on it.`);
    }
}

class ElectricCar extends Car {
    #batterySize;

    constructor(make, model, year) {
        super(make, model, year);
        this.#batterySize = 75;
    }

    describeBattery() {
        console.log(`This car has a ${this.#batterySize}-kWh battery.`);
    }
}

const myEV = new ElectricCar("Ford", "Mustang Mach-E", 2023);
console.log(myEV.getDescriptiveName());   // Inherited from Vehicle
myEV.readOdometer();                       // Overridden in Car
myEV.describeBattery();                    // Defined in ElectricCar
```

### Skills Checklist
- [ ] I can define a JavaScript class with a constructor and methods.
- [ ] I can use `extends` to create a subclass.
- [ ] I can use `super()` to call the parent constructor.
- [ ] I can use `#` for private fields.
- [ ] I can define static methods and properties.

---

# Unit 8: Files, Modules, and Error Handling

---

## Lesson 8.1: Reading and Writing Files

```javascript
const fs = require('node:fs');
const path = require('node:path');

// Synchronous reading (simple but blocks execution)
try {
    const content = fs.readFileSync('my_notes.txt', 'utf8');
    console.log(content);
} catch (err) {
    console.log(`Error: ${err.message}`);
}

// Reading line by line
const lines = content.split('\n');
lines.forEach((line, index) => {
    console.log(`Line ${index + 1}: ${line}`);
});

// Writing (overwrites existing content)
try {
    fs.writeFileSync('output.txt', 'Hello, Node.js file I/O!\n');
    console.log("File written successfully.");
} catch (err) {
    console.log(`Error writing file: ${err.message}`);
}

// Appending
try {
    fs.appendFileSync('output.txt', 'This line is appended.\n');
    console.log("Line appended.");
} catch (err) {
    console.log(`Error appending: ${err.message}`);
}

// Check if file exists
if (fs.existsSync('my_notes.txt')) {
    console.log("File exists.");
}
```

### Asynchronous File I/O (Modern Approach)

```javascript
const fs = require('node:fs/promises');  // Promise-based fs

async function readFile() {
    try {
        const content = await fs.readFile('my_notes.txt', 'utf8');
        console.log(content);
    } catch (err) {
        console.log(`Error reading file: ${err.message}`);
    }
}

async function writeFile() {
    try {
        await fs.writeFile('output.txt', 'Async write!\n');
        await fs.appendFile('output.txt', 'Appended!\n');
        console.log("Files written.");
    } catch (err) {
        console.log(`Error: ${err.message}`);
    }
}

readFile();
writeFile();
```

---

## Lesson 8.2: Error Handling

```javascript
// try-catch-finally
try {
    const result = 10 / 0;   // Doesn't throw in JS (gives Infinity)
    const parsed = JSON.parse("invalid json");  // This throws
} catch (err) {
    console.log(`Error type: ${err.constructor.name}`);
    console.log(`Error message: ${err.message}`);
} finally {
    console.log("This always runs.");
}

// Throwing custom errors
function divide(a, b) {
    if (b === 0) {
        throw new Error("Division by zero is not allowed.");
    }
    return a / b;
}

try {
    console.log(divide(10, 2));  // 5
    console.log(divide(10, 0));  // Throws
} catch (err) {
    console.log(`Caught: ${err.message}`);
}
```

### Custom Error Classes

```javascript
class ValidationError extends Error {
    constructor(field, message) {
        super(message);
        this.name = "ValidationError";
        this.field = field;
    }
}

class InsufficientFundsError extends Error {
    constructor(needed) {
        super(`Insufficient funds. Need $${needed} more.`);
        this.name = "InsufficientFundsError";
        this.needed = needed;
    }
}

try {
    throw new ValidationError("email", "Invalid email format.");
} catch (err) {
    if (err instanceof ValidationError) {
        console.log(`Validation failed on '${err.field}': ${err.message}`);
    } else {
        throw err;  // Re-throw if not our custom error
    }
}
```

---

## Lesson 8.3: JSON in Node.js

```javascript
const fs = require('node:fs');

// JavaScript object to JSON string
const settings = {
    username: "coder_kid",
    theme: "dark",
    notificationsOn: true,
    favoriteNumbers: [7, 13, 42]
};

const jsonString = JSON.stringify(settings, null, 2);  // Pretty-printed
console.log(jsonString);

// Save to file
fs.writeFileSync('settings.json', jsonString);

// Load from file
try {
    const loaded = JSON.parse(fs.readFileSync('settings.json', 'utf8'));
    console.log(`Username: ${loaded.username}`);
    console.log(`Theme: ${loaded.theme}`);
    console.log(`Numbers: ${loaded.favoriteNumbers}`);
} catch (err) {
    if (err instanceof SyntaxError) {
        console.log("Error: JSON file is corrupted.");
    } else if (err.code === 'ENOENT') {
        console.log("Error: File not found.");
    } else {
        console.log(`Error: ${err.message}`);
    }
}
```

### Skills Checklist
- [ ] I can read and write files using the `fs` module.
- [ ] I can use `try-catch-finally` to handle errors.
- [ ] I can throw custom errors using `Error` or custom classes.
- [ ] I can serialize/deserialize data using `JSON.stringify` and `JSON.parse`.
