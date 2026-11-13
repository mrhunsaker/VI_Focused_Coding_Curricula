# Unit 7: Classes and Object-Oriented Programming

## Overview
This unit uses the same student and inventory domains as the Python course. JavaScript classes use prototypes under the hood; private fields begin with `#`. Composition is often preferable to inheritance when one object contains another.

## Lesson 7.1: Why Learn About Classes?

### Reading References
- Python source counterpart: Unit 7, Lesson 7.1.
- MDN: Classes.

### Learning Objectives
- Explain classes, objects, attributes, and methods.
- Describe encapsulation and abstraction.
- Identify an appropriate domain object.

### Concept Explanation
A class defines the structure and behavior shared by its instances. An inventory item can store a name, quantity, and unit price and provide a method that calculates its line value.

### Worked Example
```javascript
class InventoryItem {
  constructor(name, quantity, unitPrice) {
    this.name = name;
    this.quantity = quantity;
    this.unitPrice = unitPrice;
  }

  lineValue() {
    return this.quantity * this.unitPrice;
  }
}

const notebook = new InventoryItem("Notebook", 3, 2.50);
console.log(`${notebook.name}: $${notebook.lineValue().toFixed(2)}`);
```

Expected output:
```text
Notebook: $7.50
```

### Expected Behavior or Output
An InventoryItem for three Notebooks at $2.50 each prints `Notebook: $7.50`.

### Common Mistakes
- Confusing the class with an instance.
- Omitting `this` when accessing instance properties.
- Defining behavior that belongs to an object as unrelated global variables.

### Activities
1. Create an InventoryItem for each canonical inventory record.
2. Print each item's line value.
3. Create a Student class using Avery's profile fields.
4. Explain which data belongs in an instance and which behavior belongs in a method.

### Accessibility Practice
Use descriptive property and method names. Announce object values by property name rather than relying on visual object inspection.

### Skills Checklist
- [ ] I can explain a class and an instance.
- [ ] I can define a constructor and method.
- [ ] I can use `this` to access instance properties.
- [ ] I can identify encapsulation in a small class.

## Lesson 7.2: Creating and Using a Class

### Reading References
- Python source counterpart: Unit 7, Lesson 7.2.
- MDN: constructor.

### Learning Objectives
- Define a class with a constructor.
- Instantiate multiple objects.
- Validate constructor arguments.

### Concept Explanation
A class constructor initializes each new instance. The `new` operator creates an object and calls the class constructor with the supplied arguments.

### Worked Example
```javascript
class Student {
  constructor(name, age, heightM, favoriteSubject) {
    if (typeof name !== "string" || name.trim() === "") {
      throw new TypeError("Student name is required.");
    }
    this.name = name;
    this.age = age;
    this.heightM = heightM;
    this.favoriteSubject = favoriteSubject;
  }
}

const student = new Student("Avery", 16, 1.72, "Computer Science");
console.log(`${student.name}, age ${student.age}`);
```

Expected output:
```text
Avery, age 16
```

### Expected Behavior or Output
The canonical Student instance prints `Avery, age 16`.

### Common Mistakes
- Forgetting the `new` keyword.
- Using constructor parameters without assigning them to the instance.
- Failing to validate required data.

### Activities
1. Create two Student instances with different values.
2. Print each student's name and favorite subject.
3. Add validation that age is a nonnegative integer.
4. Deliberately pass an invalid name and read the error.

### Accessibility Practice
Make validation errors specific and textual. Keep constructor parameters in a consistent, documented order.

### Skills Checklist
- [ ] I can define a constructor.
- [ ] I can instantiate multiple objects.
- [ ] I can validate constructor inputs.
- [ ] I can explain the role of `new`.

## Lesson 7.3: Working with Attributes and Methods

### Reading References
- Python source counterpart: Unit 7, Lesson 7.3.
- MDN: Private class elements.

### Learning Objectives
- Read and update object properties.
- Define methods that validate or transform state.
- Use a private field for encapsulated state.

### Concept Explanation
Methods define behavior associated with an instance. Private fields beginning with `#` can be accessed only from within the declaring class.

### Worked Example
```javascript
class InventoryItem {
  #quantity;

  constructor(name, quantity, unitPrice) {
    this.name = name;
    this.#quantity = quantity;
    this.unitPrice = unitPrice;
  }

  updateQuantity(newQuantity) {
    if (!Number.isInteger(newQuantity) || newQuantity < 0) {
      throw new RangeError("Quantity must be a nonnegative integer.");
    }
    this.#quantity = newQuantity;
  }

  describe() {
    return `${this.name}: quantity ${this.#quantity}`;
  }
}

const pencil = new InventoryItem("Pencil", 10, 0.50);
pencil.updateQuantity(12);
console.log(pencil.describe());
```

Expected output:
```text
Pencil: quantity 12
```

### Expected Behavior or Output
After updating the Pencil quantity to 12, the method prints `Pencil: quantity 12`.

### Common Mistakes
- Accessing a private field from outside its class.
- Updating state without validating it.
- Confusing a method call with a property read.

### Activities
1. Add a method that returns the item's line value.
2. Reject a negative quantity.
3. Update the Notebook quantity from 3 to 5.
4. Explain why a private field can protect an object's invariants.

### Accessibility Practice
Use methods that return clear text or values. State the validation rule before asking learners to test it.

### Skills Checklist
- [ ] I can read and update public properties.
- [ ] I can define and call methods.
- [ ] I can use a private class field.
- [ ] I can validate state changes.

## Lesson 7.4: Inheritance

### Reading References
- Python source counterpart: Unit 7, Lesson 7.4.
- MDN: Inheritance and the prototype chain.

### Learning Objectives
- Define a subclass with `extends`.
- Call a parent constructor with `super()`.
- Override a method when specialized behavior is required.

### Concept Explanation
Inheritance models an is-a relationship. A subclass uses `extends` and calls its parent constructor with `super()` before accessing `this`.

### Worked Example
```javascript
class InventoryItem {
  constructor(name, quantity) {
    this.name = name;
    this.quantity = quantity;
  }

  describe() {
    return `${this.name}: ${this.quantity} in stock`;
  }
}

class PerishableItem extends InventoryItem {
  constructor(name, quantity, expirationDate) {
    super(name, quantity);
    this.expirationDate = expirationDate;
  }

  describe() {
    return `${super.describe()}, expires ${this.expirationDate}`;
  }
}

const milk = new PerishableItem("Milk", 2, "2026-11-10");
console.log(milk.describe());
```

Expected output:
```text
Milk: 2 in stock, expires 2026-11-10
```

### Expected Behavior or Output
The PerishableItem example prints `Milk: 2 in stock, expires 2026-11-10`.

### Common Mistakes
- Calling `this` before `super()` in a derived constructor.
- Forgetting to pass required parent arguments.
- Using inheritance when composition would be simpler.

### Activities
1. Create a PerishableItem subclass with an expiration date.
2. Override the description method.
3. Test an instance with the canonical inventory quantity.
4. Identify one situation where composition is preferable.

### Accessibility Practice
Describe the parent/child relationship explicitly. Keep overridden method behavior predictable and document what changes.

### Skills Checklist
- [ ] I can extend a class.
- [ ] I can call a parent constructor with `super()`.
- [ ] I can override a method.
- [ ] I can explain when inheritance is appropriate.

## Lesson 7.5: Instances as Attributes (Composition)

### Reading References
- Python source counterpart: Unit 7, Lesson 7.5.
- MDN: Working with objects.

### Learning Objectives
- Model a has-a relationship.
- Store one object inside another object.
- Explain composition as an alternative to inheritance.

### Concept Explanation
Composition models a has-a relationship by storing one object as a property of another. It often provides a simpler alternative to inheritance.

### Worked Example
```javascript
class Student {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

class StudentRecord {
  constructor(student, favoriteSubject) {
    this.student = student;
    this.favoriteSubject = favoriteSubject;
  }

  describe() {
    return `${this.student.name} studies ${this.favoriteSubject}.`;
  }
}

const record = new StudentRecord(
  new Student("Avery", 16),
  "Computer Science"
);
console.log(record.describe());
```

Expected output:
```text
Avery studies Computer Science.
```

### Expected Behavior or Output
The StudentRecord example prints `Avery studies Computer Science.`.

### Common Mistakes
- Copying an object's fields when a related object should be retained.
- Confusing has-a composition with is-a inheritance.
- Creating circular object references without a clear reason.

### Activities
1. Create a Student object for Avery.
2. Place the Student object inside a StudentRecord.
3. Add a second related object, such as a contact record.
4. Explain why StudentRecord is not a subclass of Student.

### Accessibility Practice
Use explicit relationship names such as `student` and `contact`. Print nested values with labels.

### Skills Checklist
- [ ] I can model a has-a relationship.
- [ ] I can store an object as another object's property.
- [ ] I can explain composition versus inheritance.
- [ ] I can access nested object properties.
