# Unit 7: Classes and Object-Oriented Programming

## Overview

Model state and behavior using classes, inheritance, and composition. The TypeScript adaptation preserves the shared Python curriculum's learning objectives, datasets, expected results, and assessment criteria while teaching TypeScript's compile-time type system and JavaScript runtime behavior.
## Lesson 7.1: Why learn about classes?

### Reading References
- Python source counterpart: Unit 7 lesson 7.1 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Explain classes, instances, encapsulation, and object state with an inventory example.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A class describes the state and behavior of objects. TypeScript classes add static type checking, access modifiers, and optional private fields; types are erased from emitted JavaScript.

### Worked Example
```typescript
class InventoryItem {
  constructor(public name: string, public quantity: number, public unitPrice: number) {}
  value(): number { return this.quantity * this.unitPrice; }
}
const notebook = new InventoryItem("Notebook", 3, 2.5);
console.log(`${notebook.name}: ${notebook.value().toFixed(2)}`);
```

### Expected Behavior or Output
The output is `Notebook: 7.50`.

### Common Mistakes
- Treating a class as only a data container without behavior.
- Confusing a class with an instance.
- Assuming TypeScript access modifiers create runtime security.

### Activities
1. Identify the fields and behavior of an inventory item.
2. Create two instances with different values.
3. Explain what the class and each instance represent.

### Accessibility Practice
Use meaningful instance names and print a labeled summary. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can explain class and instance.
- [ ] I can identify state and behavior.
- [ ] I can create a simple class.

---

---

## Lesson 7.2: Creating and using a class

### Reading References
- Python source counterpart: Unit 7 lesson 7.2 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create a Student class and instantiate the canonical learner profile.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
A constructor initializes an instance. Parameter properties can declare and initialize fields in one place. Explicit types make the class contract readable.

### Worked Example
```typescript
class Student {
  constructor(public name: string, public age: number, public favoriteSubject: string) {}
  describe(): string { return `${this.name}, age ${this.age}, studies ${this.favoriteSubject}`; }
}
const learner = new Student("Avery", 16, "Computer Science");
console.log(learner.describe());
```

### Expected Behavior or Output
The output is `Avery, age 16, studies Computer Science`.

### Common Mistakes
- Forgetting new when constructing an instance.
- Using a parameter type that conflicts with the property type.
- Writing a method that refers to a variable instead of this.

### Activities
1. Create Avery's Student instance.
2. Create a second student instance.
3. Call describe on both instances.

### Accessibility Practice
Read constructor parameters in order and label each property. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define a constructor.
- [ ] I can instantiate a class.
- [ ] I can call an instance method.

---

---

## Lesson 7.3: Working with attributes and methods

### Reading References
- Python source counterpart: Unit 7 lesson 7.3 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Add validation and update behavior to a class.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Methods define operations over an instance's state. Encapsulation keeps validation close to the state it protects. Private fields and access modifiers guide compile-time access.

### Worked Example
```typescript
class StockItem {
  #quantity: number;
  constructor(public name: string, quantity: number) { this.#quantity = quantity; }
  get quantity(): number { return this.#quantity; }
  setQuantity(value: number): void {
    if (!Number.isInteger(value) || value < 0) throw new RangeError("Quantity must be a nonnegative integer.");
    this.#quantity = value;
  }
}
const pencil = new StockItem("Pencil", 10);
pencil.setQuantity(12);
console.log(pencil.quantity);
```

### Expected Behavior or Output
The output is 12. A negative or fractional quantity throws RangeError.

### Common Mistakes
- Changing state without validation.
- Assuming a private field is accessible outside its class.
- Allowing negative quantities.

### Activities
1. Update Pencil quantity to 12.
2. Try a negative quantity and inspect the error.
3. Explain the difference between a property and a method.

### Accessibility Practice
Use explicit validation messages and one state change per operation. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can define methods and fields.
- [ ] I can protect state with private fields.
- [ ] I can validate state updates.

---

---

## Lesson 7.4: Inheritance

### Reading References
- Python source counterpart: Unit 7 lesson 7.4 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Create a specialized item class that extends a base class.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Inheritance models an is-a relationship. A subclass uses extends and calls super before accessing this. Use inheritance only when the subtype genuinely satisfies the base contract.

### Worked Example
```typescript
class Item {
  constructor(public name: string, public quantity: number) {}
}
class PerishableItem extends Item {
  constructor(name: string, quantity: number, public expiresOn: string) {
    super(name, quantity);
  }
  describe(): string { return `${this.name}: ${this.quantity} in stock, expires ${this.expiresOn}`; }
}
console.log(new PerishableItem("Milk", 2, "2026-11-10").describe());
```

### Expected Behavior or Output
The output is `Milk: 2 in stock, expires 2026-11-10`.

### Common Mistakes
- Forgetting to call super before using this.
- Extending a class only to reuse unrelated code.
- Changing a subclass method so it violates the base contract.

### Activities
1. Create a PerishableItem.
2. Override or add a method with a clear contract.
3. Compare inheritance with composition.

### Accessibility Practice
Use a descriptive sentence for the specialized instance. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can extend a base class.
- [ ] I can call super in a constructor.
- [ ] I can explain when inheritance is appropriate.

---

---

## Lesson 7.5: Composition: instances as attributes

### Reading References
- Python source counterpart: Unit 7 lesson 7.5 in the canonical Python curriculum.
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Node.js documentation where terminal, file, or runtime APIs are used.

### Learning Objectives
- Build a record from related objects using composition.
- Explain the TypeScript-specific language or runtime behavior used in the lesson.
- Predict the example's behavior and test a boundary or invalid case.

### Concept Explanation
Composition models a has-a relationship. A class stores another object as a property rather than inheriting its behavior. This often keeps responsibilities smaller.

### Worked Example
```typescript
class Student {
  constructor(public name: string, public age: number, public favoriteSubject: string) {}
}
class Course {
  constructor(public title: string) {}
}
class StudentRecord {
  constructor(public student: Student, public course: Course) {}
  describe(): string { return `${this.student.name} studies ${this.course.title}.`; }
}
const record = new StudentRecord(new Student("Avery", 16, "Computer Science"), new Course("Computer Science"));
console.log(record.describe());
```

### Expected Behavior or Output
The output is `Avery studies Computer Science.`

### Common Mistakes
- Using inheritance for a has-a relationship.
- Creating tightly coupled classes with unclear responsibilities.
- Duplicating data already stored in a related object.

### Activities
1. Create a StudentRecord containing a Student and Course.
2. Add a method that describes the relationship.
3. Draw a text outline of the object relationships.

### Accessibility Practice
Explain object relationships in words before reading nested property access. All prompts, errors, and status messages must have meaningful text equivalents; keyboard operation is required.

### Skills Checklist
- [ ] I can model a has-a relationship.
- [ ] I can compose objects from instances.
- [ ] I can distinguish composition from inheritance.

---
