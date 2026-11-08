# Unit 6: Functions

## Overview
Functions support decomposition, reuse, and testing. JavaScript supports declarations, expressions, arrow functions, default parameters, rest parameters, and closures. Unlike Python, JavaScript does not support Python-style keyword arguments; use an options object when named configuration is useful.

## Lesson 6.1: Defining Functions

### Reading References
- Python source counterpart: Unit 6, Lesson 6.1.
- MDN: Functions.

### Learning Objectives
- Define and call a function.
- Explain parameters and function bodies.
- Choose a function declaration or expression.

### Concept Explanation
A function is a reusable block of code. Parameters receive input values, and `return` sends a result back to the caller.

### Worked Example
```javascript
function calculateTip(bill, rate) {
  return bill * rate;
}

const tip = calculateTip(24.50, 0.15);
console.log(`Tip: $${tip.toFixed(2)}`);
```

Expected output:
```text
<<<<<<< HEAD
Tip: $3.68
=======
Tip: $3.67
>>>>>>> 2067a20 (curriculum clearning and updates)
```

### Expected Behavior or Output
The canonical bill and tip rate produce a displayed tip of $3.67.

### Common Mistakes
- Calling a function before understanding its parameter order.
- Omitting `return` when the caller needs a result.
- Confusing a function definition with a function call.

### Activities
1. Define `calculateTip` using the canonical bill and tip rate.
2. Define a function that returns the average of the canonical scores.
3. Call each function with at least two different inputs.
4. Explain why returning a value is more reusable than printing inside the function.

### Accessibility Practice
Use descriptive function and parameter names. Read the function declaration, call, and returned result as separate steps.

### Skills Checklist
- [ ] I can define and call a function.
- [ ] I can identify parameters and arguments.
- [ ] I can return a computed value.
- [ ] I can use a function to reduce repeated code.

## Lesson 6.2: Passing Arguments

### Reading References
- Python source counterpart: Unit 6, Lesson 6.2.
- MDN: Function parameters.

### Learning Objectives
- Pass positional arguments in the correct order.
- Use default parameters.
- Use an options object to model named configuration.

### Concept Explanation
JavaScript arguments are positional. It does not have Python's `name=value` call syntax. For functions with several optional settings, pass one object whose properties describe each setting.

### Worked Example
```javascript
function calculateTotal(bill, tipRate = 0.15) {
  return bill + bill * tipRate;
}

function describeStudent({ name, age, favoriteSubject }) {
  return `${name}, age ${age}, studies ${favoriteSubject}.`;
}

console.log(calculateTotal(24.50).toFixed(2));
console.log(calculateTotal(24.50, 0.20).toFixed(2));
console.log(describeStudent({
  name: "Avery",
  age: 16,
  favoriteSubject: "Computer Science"
}));
```

Expected output:
```text
28.18
29.40
Avery, age 16, studies Computer Science.
```

### Expected Behavior or Output
The default tip rate produces 28.18; the 0.20 rate produces 29.40; the student description names Avery and Computer Science.

### Common Mistakes
- Swapping positional arguments that have the same primitive type.
- Assuming JavaScript supports Python keyword arguments.
- Forgetting that a default parameter is used for an omitted or `undefined` argument, not for `null`.

### Activities
1. Call `calculateTotal` with the default rate and with a 0.20 rate.
2. Create an options object for the canonical student profile.
3. Omit one required property and decide how the function should validate it.
4. Explain the difference between omitted, `undefined`, and `null`.

### Accessibility Practice
Prefer clear property names over unexplained positional values when a function accepts several related settings.

### Skills Checklist
- [ ] I can pass positional arguments.
- [ ] I can define default parameters.
- [ ] I can use an options object.
- [ ] I can explain JavaScript's argument semantics.

## Lesson 6.3: Return Values

### Reading References
- Python source counterpart: Unit 6, Lesson 6.3.
- MDN: return.

### Learning Objectives
- Return values from functions.
- Distinguish returning from printing.
- Handle early returns for invalid inputs.

### Concept Explanation
A return value is data supplied to the caller. Printing is a side effect and does not substitute for returning a value.

### Worked Example
```javascript
function average(scores) {
  if (!Array.isArray(scores) || scores.length === 0) {
    return null;
  }
  const total = scores.reduce((sum, score) => sum + score, 0);
  return total / scores.length;
}

const result = average([82, 91, 76, 88]);
console.log(`Average: ${result.toFixed(2)}`);
console.log(`Empty input: ${average([])}`);
```

Expected output:
```text
Average: 84.25
Empty input: null
```

### Expected Behavior or Output
The canonical score average is 84.25 and an empty array returns null.

### Common Mistakes
- Expecting a function that only calls `console.log()` to return a useful value.
- Forgetting that a function without an explicit return produces `undefined`.
- Returning a formatted string when later calculations require a number.

### Activities
1. Write a function that returns the total of the canonical scores.
2. Write a function that returns `null` for an empty list.
3. Use the returned average in a second calculation.
4. Compare a function that prints a result with one that returns it.

### Accessibility Practice
Keep calculation results and explanatory output distinct. Use explicit labels when displaying a returned value.

### Skills Checklist
- [ ] I can return a value from a function.
- [ ] I can use early returns for invalid cases.
- [ ] I can distinguish `undefined`, `null`, and a computed value.
- [ ] I can reuse returned values in later calculations.

## Lesson 6.4: Functions with Arrays and Objects

### Reading References
- Python source counterpart: Unit 6, Lesson 6.4.
- MDN: Working with objects and arrays.

### Learning Objectives
- Pass arrays and objects to functions.
- Process the canonical score and inventory data.
- Explain that object and array values are passed by sharing their references.

### Concept Explanation
Arrays and objects are passed as values that refer to the same underlying object. A function can therefore mutate caller-visible state unless it works on a copy.

### Worked Example
```javascript
function inventoryValue(items) {
  return items.reduce(
    (total, item) => total + item.quantity * item.unitPrice,
    0
  );
}

const inventory = [
  { name: "Notebook", quantity: 3, unitPrice: 2.50 },
  { name: "Pencil", quantity: 10, unitPrice: 0.50 },
  { name: "Folder", quantity: 4, unitPrice: 1.25 }
];

console.log(`Inventory value: $${inventoryValue(inventory).toFixed(2)}`);
```

Expected output:
```text
Inventory value: $17.50
```

### Expected Behavior or Output
The canonical inventory value is $17.50.

### Common Mistakes
- Mutating an array or object inside a function without documenting the side effect.
- Assuming a new variable created with `const` makes the referenced object immutable.
- Returning the wrong data shape for the caller.

### Activities
1. Write a function that returns the average of the canonical scores.
2. Write a function that returns the total value of the canonical inventory.
3. Add a new inventory item and verify the total changes by its line value.
4. Write a non-mutating function that returns a filtered list of scores at least 80.

### Accessibility Practice
Use named object properties and label each returned total. Explain whether a function changes the original collection.

### Skills Checklist
- [ ] I can pass arrays and objects to functions.
- [ ] I can process a collection with `reduce()` or a loop.
- [ ] I can explain reference sharing and mutation.
- [ ] I can return a predictable result shape.

## Lesson 6.5: Arbitrary Numbers of Arguments

### Reading References
- Python source counterpart: Unit 6, Lesson 6.5.
- MDN: Rest parameters.

### Learning Objectives
- Use rest parameters to collect arbitrary positional arguments.
- Use spread syntax to pass array elements as arguments.
- Explain the difference between rest and spread syntax.

### Concept Explanation
A rest parameter gathers remaining positional arguments into an array. Spread syntax expands an iterable into individual arguments at a call site.

### Worked Example
```javascript
function sumScores(...scores) {
  return scores.reduce((total, score) => total + score, 0);
}

const values = [82, 91, 76, 88];
console.log(sumScores(...values));
console.log(sumScores(10, 20, 30));
```

Expected output:
```text
337
60
```

### Expected Behavior or Output
The four canonical scores sum to 337; the values 10, 20, and 30 sum to 60.

### Common Mistakes
- Confusing rest parameters in a function definition with spread syntax in a call.
- Placing a rest parameter anywhere other than the final parameter position.
- Passing a whole array when the function expects individual numeric arguments.

### Activities
1. Call `sumScores` with the four canonical scores.
2. Call it with three different values.
3. Pass an array using spread syntax.
4. Explain why JavaScript rest parameters do not provide a direct equivalent to Python's `**kwargs`.

### Accessibility Practice
Use parameter names that communicate the expected value type. Keep the function's input contract explicit.

### Skills Checklist
- [ ] I can define a rest parameter.
- [ ] I can use spread syntax in a function call.
- [ ] I can distinguish rest from spread.
- [ ] I can explain the lack of Python-style keyword-argument collection.
