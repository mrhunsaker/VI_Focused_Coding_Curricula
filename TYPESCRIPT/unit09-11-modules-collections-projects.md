# Unit 9: Modules, Collections, and Testing

---

## Typed modules, collections, and data boundaries

Use interfaces and type aliases to describe records, and use generic collection types such as Map<string, number> and Set<string>. When data comes from JSON or a file, treat it as untrusted until it has been validated; a TypeScript annotation does not validate the runtime value.

## Lesson 9.1: TypeScript Modules

### CommonJS (Node.js default)

```typescript
// math.ts — exporting
const add = (a: number, b: number): number => a + b;
const multiply = (a: number, b: number): number => a * b;
const PI = Math.PI;

module.exports = { add, multiply, PI };

// Or export individually:
// module.exports.add = add;
```

```typescript
// main.ts — importing
const { add, multiply, PI } = require('./math');

console.log(add(5, 3));         // 8
console.log(multiply(4, 6));    // 24
console.log(PI.toFixed(5));     // 3.14159
```

### ES Modules (Modern — requires `"type": "module"` in package.json)

```typescript
// math.mjs
export const add = (a: number, b: number): number => a + b;
export const multiply = (a: number, b: number): number => a * b;
export const PI = Math.PI;
export default function greet(name: string): string {
    return `Hello, ${name}!`;
}
```

```typescript
// main.mjs
import greet, { add, multiply, PI } from './math.mjs';

console.log(greet("Alice"));
console.log(add(5, 3));
```

---

## Lesson 9.2: Maps and Sets

### `Map` — Key-Value (Better than plain objects for maps)

```typescript
const inventory = new Map();

// Adding
inventory.set("apples", 50);
inventory.set("bananas", 30);
inventory.set("oranges", 40);

// Access
console.log(inventory.get("apples"));    // 50
console.log(inventory.has("bananas"));   // true
console.log(inventory.size);             // 3

// Delete
inventory.delete("bananas");

// Iterate
for (const [key, value] of inventory) {
    console.log(`${key}: ${value}`);
}

inventory.forEach((value, key) => {
    console.log(`${key} = ${value}`);
});

console.log([...inventory.keys()]);
console.log([...inventory.values()]);
console.log([...inventory.entries()]);
```

### `Set` — Unique Values

```typescript
const uniqueWords = new Set();
uniqueWords.add("apple");
uniqueWords.add("banana");
uniqueWords.add("apple");   // Duplicate — ignored

console.log(uniqueWords.size);           // 2
console.log(uniqueWords.has("banana"));  // true
uniqueWords.delete("banana");

// Convert array to set (remove duplicates)
const nums = [1, 2, 2, 3, 3, 3, 4];
const unique = [...new Set(nums)];
console.log(unique);   // [1, 2, 3, 4]

// Iterate
for (const item of uniqueWords) {
    console.log(item);
}
```

---

## Lesson 9.3: Word Frequency Analysis

```typescript
const fs = require('node:fs');

function countWords(text: string): Map<string, number> {
    const words = text
        .toLowerCase()
        .replace(/[^a-z\s]/g, '')
        .trim()
        .split(/\s+/)
        .filter(word => word.length > 0);

    const frequency = new Map();
    for (const word of words) {
        frequency.set(word, (frequency.get(word) || 0) + 1);
    }

    return frequency;
}

const text = "the quick brown fox jumps over the lazy dog the quick brown fox";
const freq = countWords(text);

// Sort by frequency (most common first)
const sorted = [...freq.entries()].sort((a, b) => b[1] - a[1]);

console.log("Word Frequencies:");
for (const [word, count] of sorted) {
    console.log(`'${word}': ${count}`);
}

// Top 5 words
console.log("\nTop 5 words:");
sorted.slice(0, 5).forEach(([word, count]) => {
    console.log(`  ${word}: ${count}`);
});
```

---

## Lesson 9.4: Working with CSV Files

```typescript
const fs = require('node:fs');

type CsvRecord = Record<string, string>;

function parseCSV(content: string): CsvRecord[] {
    const lines = content.trim().split('\n');
    const headers = lines[0].split(',').map(h => h.trim());

    return lines.slice(1).map(line => {
        const values = line.split(',').map(v => v.trim());
        const record: CsvRecord = {};
        headers.forEach((header, index) => {
            record[header] = values[index];
        });
        return record;
    });
}

function generateCSV(records: CsvRecord[]): string {
    if (records.length === 0) return '';
    const headers = Object.keys(records[0]);
    const headerLine = headers.join(',');
    const dataLines = records.map(record =>
        headers.map(h => record[h]).join(',')
    );
    return [headerLine, ...dataLines].join('\n');
}

// Read and parse CSV
try {
    const content = fs.readFileSync('students.csv', 'utf8');
    const students = parseCSV(content);

    console.log(`Loaded ${students.length} students:`);
    students.forEach(student => {
        console.log(`  Name: ${student.name}, Age: ${student.age}, Grade: ${student.grade}`);
    });

} catch (err: unknown) {
    if (typeof err === 'object' && err !== null && 'code' in err && err.code === 'ENOENT') {
        // Create a sample CSV for demonstration
        const sampleData = `name,age,grade
Alice,15,A
Bob,14,B
Charlie,16,A`;
        fs.writeFileSync('students.csv', sampleData);
        console.log("Created sample students.csv");
    }
}
```

---

## Lesson 9.5: Testing with Jest

### Setting Up Jest

```bash
npm init -y
npm install --save-dev jest
```

Add to `package.json`:
```json
{
  "scripts": {
    "test": "jest"
  }
}
```

### Writing Tests

```typescript
// math.ts
const add = (a: number, b: number): number => a + b;
const getGrade = (score: number): string => {
    if (score >= 90) return "A";
    if (score >= 80) return "B";
    if (score >= 70) return "C";
    return "F";
};
const circleArea = (radius: number): number => Math.PI * radius ** 2;

module.exports = { add, getGrade, circleArea };
```

```typescript
// math.test.ts
const { add, getGrade, circleArea } = require('./math');

describe("add function", () => {
    test("adds two positive numbers", () => {
        expect(add(5, 3)).toBe(8);
    });

    test("adds negative numbers", () => {
        expect(add(-5, -3)).toBe(-8);
    });

    test("adds zero", () => {
        expect(add(0, 7)).toBe(7);
    });
});

describe("getGrade function", () => {
    test("returns A for score >= 90", () => {
        expect(getGrade(95)).toBe("A");
        expect(getGrade(90)).toBe("A");
    });

    test("returns B for score 80-89", () => {
        expect(getGrade(85)).toBe("B");
    });

    test("returns F for score < 60", () => {
        expect(getGrade(55)).toBe("F");
    });
});

describe("circleArea function", () => {
    test("calculates area of circle", () => {
        expect(circleArea(5)).toBeCloseTo(78.54, 1);
    });
});
```

Run tests:
```bash
npm test
```

### Common Jest Matchers

| Matcher | Description |
|---------|-------------|
| `toBe(value)` | Strict equality (`===`) |
| `toEqual(value)` | Deep equality (for objects/arrays) |
| `toBeCloseTo(num, decimals)` | Floating-point comparison |
| `toBeTruthy()` | Check if truthy |
| `toBeFalsy()` | Check if falsy |
| `toBeNull()` | Check if null |
| `toBeUndefined()` | Check if undefined |
| `toContain(item)` | Array/string contains item |
| `toHaveLength(n)` | Check length |
| `toThrow(error)` | Check if function throws |

### Skills Checklist
- [ ] I can create and import modules using CommonJS.
- [ ] I can use `Map` and `Set` for collections.
- [ ] I can write and run Jest tests.
- [ ] I can use common Jest matchers.

---

# Unit 10: Project-Based Learning

---

## Lesson 10.1: Text-Based Adventure Game

```typescript
class Room {
    name: string;
    description: string;
    exits: Record<string, Room>;
    items: string[];
    constructor(name: string, description: string) {
        this.name = name;
        this.description = description;
        this.exits = {};
        this.items = [];
    }

    addExit(direction: string, room: Room): void {
        this.exits[direction.toLowerCase()] = room;
    }

    addItem(item: string): void {
        this.items.push(item);
    }

    describe(): string {
        let desc = `--- ${this.name} ---\n${this.description}\n`;
        if (this.items.length > 0) {
            desc += `You see: ${this.items.join(', ')}\n`;
        }
        const exitList = Object.keys(this.exits).join(', ');
        desc += `Exits: ${exitList}`;
        return desc;
    }
}

class Player {
    name: string;
    currentRoom: Room;
    inventory: string[];
    health: number;
    constructor(name: string, startRoom: Room) {
        this.name = name;
        this.currentRoom = startRoom;
        this.inventory = [];
        this.health = 100;
    }

    move(direction: string): boolean {
        const nextRoom = this.currentRoom.exits[direction.toLowerCase()];
        if (nextRoom) {
            this.currentRoom = nextRoom;
            return true;
        }
        return false;
    }

    takeItem(itemName: string): boolean {
        const index = this.currentRoom.items.findIndex(
            item => item.toLowerCase() === itemName.toLowerCase()
        );
        if (index !== -1) {
            const item = this.currentRoom.items.splice(index, 1)[0];
            this.inventory.push(item);
            return true;
        }
        return false;
    }

    getStatus(): string {
        const inv = this.inventory.length > 0
            ? this.inventory.join(', ')
            : 'empty';
        return `${this.name} | Health: ${this.health} | Inventory: ${inv}`;
    }
}

async function playGame(): Promise<void> {
    const { askQuestion, close } = require('./input');

    // Build world
    const cave = new Room("Dark Cave", "You are in a dimly lit cave.");
    const tunnel = new Room("Stone Tunnel", "A narrow tunnel runs north and south.");
    const clearing = new Room("Sunny Clearing", "A bright clearing with tall trees.");

    cave.addExit("north", tunnel);
    cave.addItem("torch");
    tunnel.addExit("south", cave);
    tunnel.addExit("north", clearing);
    clearing.addExit("south", tunnel);
    clearing.addItem("magic key");

    const player = new Player("Hero", cave);

    console.log("=== Text Adventure ===");
    console.log("Commands: go [direction], take [item], inventory, look, quit\n");

    while (true) {
        console.log(player.currentRoom.describe());
        console.log(player.getStatus());

        const input = (await askQuestion("\n> ")).trim().toLowerCase();
        const [command, ...argParts] = input.split(/\s+/);
        const argument = argParts.join(' ');

        console.log('');

        switch (command) {
            case 'go':
                if (!argument) {
                    console.log("Go where?");
                } else if (!player.move(argument)) {
                    console.log("You can't go that way.");
                }
                break;
            case 'take':
                if (player.takeItem(argument)) {
                    console.log(`You picked up the ${argument}.`);
                } else {
                    console.log(`There's no ${argument} here.`);
                }
                break;
            case 'inventory':
                console.log(`Inventory: ${player.inventory.join(', ') || 'empty'}`);
                break;
            case 'look':
                // Description already shown at top
                break;
            case 'quit':
                console.log("Thanks for playing!");
                close();
                return;
            default:
                console.log(`Unknown command: '${command}'`);
        }
    }
}

playGame();
```

---

## Lesson 10.2: Command-Line To-Do Manager

```typescript
const fs = require('fs');
const { askQuestion, close } = require('./input');

const FILE_PATH = 'todos.json';

interface Todo {
    description: string;
    completed: boolean;
    createdAt: string;
}

function loadTodos(): Todo[] {
    try {
        const data = fs.readFileSync(FILE_PATH, 'utf8');
        return JSON.parse(data);
    } catch (err) {
        if (typeof err === 'object' && err !== null && 'code' in err && err.code === 'ENOENT') {
            return [];   // File doesn't exist yet
        }
        if (err instanceof SyntaxError) {
            console.log("Warning: Corrupted todos file. Starting fresh.");
            return [];
        }
        throw err;
    }
}

function saveTodos(todos: Todo[]): void {
    fs.writeFileSync(FILE_PATH, JSON.stringify(todos, null, 2));
}

function addTask(todos: Todo[], description: string): void {
    todos.push({ description, completed: false, createdAt: new Date().toISOString() });
    console.log(`Task added: "${description}"`);
}

function viewTasks(todos: Todo[]): void {
    if (todos.length === 0) {
        console.log("No tasks in your list.");
        return;
    }
    console.log("--- Your To-Do List ---");
    todos.forEach((task, index) => {
        const status = task.completed ? "[X]" : "[ ]";
        console.log(`${index + 1}. ${status} ${task.description}`);
    });
    console.log("-----------------------");
}

function markComplete(todos: Todo[], taskNumber: string): void {
    const index = parseInt(taskNumber) - 1;
    if (index >= 0 && index < todos.length) {
        todos[index].completed = true;
        console.log(`Completed: "${todos[index].description}"`);
    } else {
        console.log("Invalid task number.");
    }
}

function deleteTask(todos: Todo[], taskNumber: string): void {
    const index = parseInt(taskNumber) - 1;
    if (index >= 0 && index < todos.length) {
        const removed = todos.splice(index, 1)[0];
        console.log(`Deleted: "${removed.description}"`);
    } else {
        console.log("Invalid task number.");
    }
}

async function main(): Promise<void> {
    let todos = loadTodos();
    console.log("=== To-Do Manager ===");

    while (true) {
        console.log("\n1. Add Task  2. View Tasks  3. Mark Complete  4. Delete  5. Quit");
        const choice = (await askQuestion("Choice: ")).trim();

        switch (choice) {
            case '1':
                const desc = await askQuestion("Task description: ");
                addTask(todos, desc);
                saveTodos(todos);
                break;
            case '2':
                viewTasks(todos);
                break;
            case '3':
                viewTasks(todos);
                const completeNum = await askQuestion("Task number: ");
                markComplete(todos, completeNum);
                saveTodos(todos);
                break;
            case '4':
                viewTasks(todos);
                const deleteNum = await askQuestion("Task number to delete: ");
                deleteTask(todos, deleteNum);
                saveTodos(todos);
                break;
            case '5':
                console.log("Goodbye!");
                close();
                return;
            default:
                console.log("Invalid choice.");
        }
    }
}

main();
```

---

# Unit 11: Capstone Project — Personal Data Manager in TypeScript

## Overview

Build a fully functional, accessible command-line personal data manager using Node.js.

## Project Options

- **Contact Manager:** name, phone, email, notes
- **Book Tracker:** title, author, genre, read status
- **Recipe Collection:** name, ingredients, instructions, cuisine type
- **Budget Tracker:** category, amount, date, description

## Required Features

1. **Add item** — prompt for all attributes and save.
2. **View all items** — display clearly with numbers.
3. **Search/filter** — find items by keyword.
4. **Edit item** — select and modify specific fields.
5. **Delete item** — remove by number.
6. **Persistence** — save/load to JSON file.

## Project Structure

```
my-data-manager/
├── src/
│   ├── models/
│   │   └── contact.ts      (data model/class)
│   ├── storage/
│   │   └── dataManager.ts  (JSON file I/O)
│   ├── ui/
│   │   └── consoleUI.ts    (menu and display)
│   └── utils/
│       └── input.ts        (reusable input helper)
├── data/
│   └── contacts.json       (data storage)
├── tests/
│   └── contact.test.ts     (Jest tests)
├── package.json
├── README.md
└── index.ts                (entry point)
```

## Accessibility Guidelines

1. Every prompt must clearly describe what input is expected.
2. Print a confirmation message after every action.
3. Number all listed items for easy selection.
4. Provide clear, specific error messages.
5. Include a `help` command listing all available options.
6. Use consistent separators (`---`) to group output.

## Assessment Criteria

### Functionality (60%)
- [ ] All CRUD operations (Create, Read, Update, Delete) work correctly.
- [ ] Data persists to JSON between program runs.
- [ ] Search works by at least one field.
- [ ] Program handles invalid input without crashing.

### Code Quality (20%)
- [ ] Functions are small with single responsibilities.
- [ ] Consistent use of `const`/`let`, arrow functions, template literals.
- [ ] Meaningful names for all variables and functions.
- [ ] Code is organized into modules.
- [ ] Includes JSDoc comments for key functions.

### Accessibility & UX (15%)
- [ ] All prompts are descriptive and clear.
- [ ] Confirmation messages after every action.
- [ ] Consistent, predictable output format.
- [ ] Help system available.

### Documentation & Tests (5%)
- [ ] `README.md` with setup and usage instructions.
- [ ] At least 5 Jest unit tests for key functions.

## Deliverables

1. All source code files.
2. `data/` folder with example JSON data.
3. `README.md` including:
   - Installation steps: `npm install`
   - Run instructions: `npx tsc && node dist/index.js`
   - Available commands list.
   - Screen reader usage tips.
   - Reflection on challenges faced.
