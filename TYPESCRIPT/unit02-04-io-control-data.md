# Unit 2: Numeric Computations

## Overview

Translate requirements into programs, expressions, input, conversions, and mathematical calculations. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.

## Lesson 2.1: The software development process

### Reading References
- Python source counterpart: Unit 2 lesson 2.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Apply the design, implementation, and testing cycle to the canonical tip calculator.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A problem statement becomes requirements, an algorithm, an implementation, and tests. The shared calculator uses a $24.50 bill and a 15% tip rate.

### Worked Example
```typescript
const bill = 24.50;
const tipRate = 0.15;
const tip = bill * tipRate;
const total = bill + tip;
console.log(`Tip: $${tip.toFixed(2)}`);
console.log(`Total: $${total.toFixed(2)}`);
```

### Expected Behavior or Output

The tip is $3.68 and the total is $28.18 when rounded using JavaScript number formatting.
