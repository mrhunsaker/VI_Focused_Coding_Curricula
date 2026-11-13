[Header 2 ("unit-7-classes-and-object-oriented-programming", [], []) [Str "Unit 7: Classes and Object-Oriented Programming"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit uses the same student and inventory domains as the Python course. JavaScript classes use prototypes under the hood; private fields begin with ", Code ("", [], []) "#", Str ". Composition is often preferable to inheritance when one object contains another."], Header 3 ("lesson-71-why-learn-about-classes", ["unnumbered", "unlisted"], []) [Str "Lesson 7.1: Why Learn About Classes?"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 7, Lesson 7.1."]], [Plain [Str "MDN: Classes."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain classes, objects, attributes, and methods."]], [Plain [Str "Describe encapsulation and abstraction."]], [Plain [Str "Identify an appropriate domain object."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A class defines the structure and behavior shared by its instances. An inventory item can store a name, quantity, and unit price and provide a method that calculates its line value."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["javascript"], []) "class InventoryItem {
  constructor(name, quantity, unitPrice) {
    this.name = name;
    this.quantity = quantity;
    this.unitPrice = unitPrice;
  }

  lineValue() {
    return this.quantity * this.unitPrice;
  }
}

const notebook = new InventoryItem(\"Notebook\", 3, 2.50);
console.log(`${notebook.name}: $${notebook.lineValue().toFixed(2)}`);
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "Notebook: $7.50
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "An InventoryItem for three Notebooks at $2.50 each prints ", Code ("", [], []) "Notebook: $7.50", Str "."], Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Confusing the class with an instance."]], [Plain [Str "Omitting ", Code ("", [], []) "this", Str " when accessing instance properties."]], [Plain [Str "Defining behavior that belongs to an object as unrelated global variables."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create an InventoryItem for each canonical inventory record."]], [Plain [Str "Print each item's line value."]], [Plain [Str "Create a Student class using Avery's profile fields."]], [Plain [Str "Explain which data belongs in an instance and which behavior belongs in a method."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use descriptive property and method names. Announce object values by property name rather than relying on visual object inspection."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain a class and an instance."]], [Plain [Str "\9744", Space, Str "I can define a constructor and method."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "this", Str " to access instance properties."]], [Plain [Str "\9744", Space, Str "I can identify encapsulation in a small class."]]], Header 3 ("lesson-72-creating-and-using-a-class", ["unnumbered", "unlisted"], []) [Str "Lesson 7.2: Creating and Using a Class"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 7, Lesson 7.2."]], [Plain [Str "MDN: constructor."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Define a class with a constructor."]], [Plain [Str "Instantiate multiple objects."]], [Plain [Str "Validate constructor arguments."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A class constructor initializes each new instance. The ", Code ("", [], []) "new", Str " operator creates an object and calls the class constructor with the supplied arguments."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["javascript"], []) "class Student {
  constructor(name, age, heightM, favoriteSubject) {
    if (typeof name !== \"string\" || name.trim() === \"\") {
      throw new TypeError(\"Student name is required.\");
    }
    this.name = name;
    this.age = age;
    this.heightM = heightM;
    this.favoriteSubject = favoriteSubject;
  }
}

const student = new Student(\"Avery\", 16, 1.72, \"Computer Science\");
console.log(`${student.name}, age ${student.age}`);
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "Avery, age 16
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The canonical Student instance prints ", Code ("", [], []) "Avery, age 16", Str "."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Forgetting the ", Code ("", [], []) "new", Str " keyword."]], [Plain [Str "Using constructor parameters without assigning them to the instance."]], [Plain [Str "Failing to validate required data."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create two Student instances with different values."]], [Plain [Str "Print each student's name and favorite subject."]], [Plain [Str "Add validation that age is a nonnegative integer."]], [Plain [Str "Deliberately pass an invalid name and read the error."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Make validation errors specific and textual. Keep constructor parameters in a consistent, documented order."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can define a constructor."]], [Plain [Str "\9744", Space, Str "I can instantiate multiple objects."]], [Plain [Str "\9744", Space, Str "I can validate constructor inputs."]], [Plain [Str "\9744", Space, Str "I can explain the role of ", Code ("", [], []) "new", Str "."]]], Header 3 ("lesson-73-working-with-attributes-and-methods", ["unnumbered", "unlisted"], []) [Str "Lesson 7.3: Working with Attributes and Methods"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 7, Lesson 7.3."]], [Plain [Str "MDN: Private class elements."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Read and update object properties."]], [Plain [Str "Define methods that validate or transform state."]], [Plain [Str "Use a private field for encapsulated state."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Methods define behavior associated with an instance. Private fields beginning with ", Code ("", [], []) "#", Str " can be accessed only from within the declaring class."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["javascript"], []) "class InventoryItem {
  #quantity;

  constructor(name, quantity, unitPrice) {
    this.name = name;
    this.#quantity = quantity;
    this.unitPrice = unitPrice;
  }

  updateQuantity(newQuantity) {
    if (!Number.isInteger(newQuantity) || newQuantity < 0) {
      throw new RangeError(\"Quantity must be a nonnegative integer.\");
    }
    this.#quantity = newQuantity;
  }

  describe() {
    return `${this.name}: quantity ${this.#quantity}`;
  }
}

const pencil = new InventoryItem(\"Pencil\", 10, 0.50);
pencil.updateQuantity(12);
console.log(pencil.describe());
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "Pencil: quantity 12
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "After updating the Pencil quantity to 12, the method prints ", Code ("", [], []) "Pencil: quantity 12", Str "."], Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Accessing a private field from outside its class."]], [Plain [Str "Updating state without validating it."]], [Plain [Str "Confusing a method call with a property read."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Add a method that returns the item's line value."]], [Plain [Str "Reject a negative quantity."]], [Plain [Str "Update the Notebook quantity from 3 to 5."]], [Plain [Str "Explain why a private field can protect an object's invariants."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use methods that return clear text or values. State the validation rule before asking learners to test it."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can read and update public properties."]], [Plain [Str "\9744", Space, Str "I can define and call methods."]], [Plain [Str "\9744", Space, Str "I can use a private class field."]], [Plain [Str "\9744", Space, Str "I can validate state changes."]]], Header 3 ("lesson-74-inheritance", ["unnumbered", "unlisted"], []) [Str "Lesson 7.4: Inheritance"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 7, Lesson 7.4."]], [Plain [Str "MDN: Inheritance and the prototype chain."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Define a subclass with ", Code ("", [], []) "extends", Str "."]], [Plain [Str "Call a parent constructor with ", Code ("", [], []) "super()", Str "."]], [Plain [Str "Override a method when specialized behavior is required."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Inheritance models an is-a relationship. A subclass uses ", Code ("", [], []) "extends", Str " and calls its parent constructor with ", Code ("", [], []) "super()", Str " before accessing ", Code ("", [], []) "this", Str "."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["javascript"], []) "class InventoryItem {
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

const milk = new PerishableItem(\"Milk\", 2, \"2026-11-10\");
console.log(milk.describe());
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "Milk: 2 in stock, expires 2026-11-10
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The PerishableItem example prints ", Code ("", [], []) "Milk: 2 in stock, expires 2026-11-10", Str "."], Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Calling ", Code ("", [], []) "this", Str " before ", Code ("", [], []) "super()", Str " in a derived constructor."]], [Plain [Str "Forgetting to pass required parent arguments."]], [Plain [Str "Using inheritance when composition would be simpler."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create a PerishableItem subclass with an expiration date."]], [Plain [Str "Override the description method."]], [Plain [Str "Test an instance with the canonical inventory quantity."]], [Plain [Str "Identify one situation where composition is preferable."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Describe the parent/child relationship explicitly. Keep overridden method behavior predictable and document what changes."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can extend a class."]], [Plain [Str "\9744", Space, Str "I can call a parent constructor with ", Code ("", [], []) "super()", Str "."]], [Plain [Str "\9744", Space, Str "I can override a method."]], [Plain [Str "\9744", Space, Str "I can explain when inheritance is appropriate."]]], Header 3 ("lesson-75-instances-as-attributes-composition", ["unnumbered", "unlisted"], []) [Str "Lesson 7.5: Instances as Attributes (Composition)"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Python source counterpart: Unit 7, Lesson 7.5."]], [Plain [Str "MDN: Working with objects."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Model a has-a relationship."]], [Plain [Str "Store one object inside another object."]], [Plain [Str "Explain composition as an alternative to inheritance."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Composition models a has-a relationship by storing one object as a property of another. It often provides a simpler alternative to inheritance."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["javascript"], []) "class Student {
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
  new Student(\"Avery\", 16),
  \"Computer Science\"
);
console.log(record.describe());
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "Avery studies Computer Science.
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The StudentRecord example prints ", Code ("", [], []) "Avery studies Computer Science.", Str "."], Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Copying an object's fields when a related object should be retained."]], [Plain [Str "Confusing has-a composition with is-a inheritance."]], [Plain [Str "Creating circular object references without a clear reason."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create a Student object for Avery."]], [Plain [Str "Place the Student object inside a StudentRecord."]], [Plain [Str "Add a second related object, such as a contact record."]], [Plain [Str "Explain why StudentRecord is not a subclass of Student."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use explicit relationship names such as ", Code ("", [], []) "student", Str " and ", Code ("", [], []) "contact", Str ". Print nested values with labels."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model a has-a relationship."]], [Plain [Str "\9744", Space, Str "I can store an object as another object's property."]], [Plain [Str "\9744", Space, Str "I can explain composition versus inheritance."]], [Plain [Str "\9744", Space, Str "I can access nested object properties."]]]]