# Unit 7: Data Modeling and Traits

## Overview
This unit develops data modeling and traits through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly.

## Lesson 7.1: Structs, enums, and data modeling

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Structs, enums, and data modeling using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Rust models data with structs and enums rather than class inheritance. impl blocks define methods and associated functions; traits define shared behavior. Composition and explicit ownership make relationships and lifetimes visible. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
#[derive(Debug)] struct Student{name:String,score:u8} enum Status{Active,Inactive} fn main(){let s=Student{name:"Avery".into(),score:82};let st=Status::Active;let archived=Status::Inactive;println!("{}: {}; active={}; archived={}",s.name,s.score,matches!(st,Status::Active),matches!(archived,Status::Inactive));}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Moving a non-Copy field out of a borrowed struct.
2. Confusing associated functions with methods that receive self.
3. Implementing a trait method with a mismatched signature.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical inventory and CSV records and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (structs, enums, and data modeling); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain structs, enums, and data modeling using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
- [The Rust Programming Language: Defining and Instantiating Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [The Rust Programming Language: Defining an Enum](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [The Rust Programming Language: Modules and Privacy](https://doc.rust-lang.org/book/ch07-02-defining-modules-to-control-scope-and-privacy.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 7.1: Why Learn About Classes?

### Learning Objectives
- Model data with a struct and with an enum.
- Hide a field with module privacy and change it only through methods.
- Explain that Rust has no classes and no inheritance.

### Concept Explanation

Rust has no classes. Data is modeled with a **struct** (named fields) or an **enum** (a value that is exactly one of several variants), and behavior is added in `impl` blocks (Lesson 7.3) and *traits* (Lesson 7.4). Bundling data with the functions that work on it, and hiding the details, is still called **encapsulation**.

Privacy in Rust is controlled by *modules*. Fields and functions are private to the module they are written in unless marked `pub`. In the example, `mod inventory` holds an `Item` whose `quantity` field is private: code outside the module can read it only through the `quantity()` method and change it only through `restock`.

`match` on an enum must cover every variant, so adding a new variant later makes the compiler point at every place that needs a decision. The shared Notebook has quantity 3; restocking 2 gives 5.

### Worked Example

```rust
mod inventory {
    pub struct Item {
        pub name: String,
        quantity: u32,
        pub unit_price: f64,
    }

    impl Item {
        pub fn new(name: &str, quantity: u32, unit_price: f64) -> Item {
            Item { name: name.to_string(), quantity, unit_price }
        }

        pub fn quantity(&self) -> u32 {
            self.quantity
        }

        pub fn restock(&mut self, amount: u32) {
            self.quantity += amount;
        }
    }
}

#[derive(Debug)]
enum Stock {
    Out,
    Low,
    Enough,
}

fn status(quantity: u32) -> Stock {
    match quantity {
        0 => Stock::Out,
        1..=4 => Stock::Low,
        _ => Stock::Enough,
    }
}

fn main() {
    let mut notebook = inventory::Item::new("Notebook", 3, 2.50);
    println!("{}: {} at {} is {:?}", notebook.name, notebook.quantity(), notebook.unit_price, status(notebook.quantity()));
    notebook.restock(2);
    println!("{}: {} is now {:?}", notebook.name, notebook.quantity(), status(notebook.quantity()));
    println!("{:?}", status(0));
    // notebook.quantity = 99;   // would not compile: the field is private
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.5 is Low
Notebook: 5 is now Enough
Out
```

### Common Mistakes
1. Looking for a `class` keyword. Rust uses structs, enums, impl blocks, and traits.
2. Making every field `pub`, so outside code can put the value into an invalid state.
3. Forgetting a variant in a `match` on an enum, which the compiler rejects.

### Activities
1. Predict the three printed lines before running.
2. Add a variant `Overstocked` for quantities above 100 and fix every `match` the compiler points to.
3. Uncomment the assignment, read the compiler message, and restore the comment.
4. Explain what encapsulation means and how modules provide it.

### Accessibility Practice

Describe a data type as a list read in order: the name, then each field, then each variant. Reading a struct aloud works best by saying 'pub struct Item, open brace, pub name colon String comma...' and listening for the braces that show structure.

### Skills Checklist
- [ ] I can model data with a struct and an enum.
- [ ] I can hide a field with a module.
- [ ] I know Rust has no classes.
- [ ] I can read a struct definition aloud.
- [ ] I can match every enum variant.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 7.2: Creating instances and methods

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Creating instances and methods using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Rust models data with structs and enums rather than class inheritance. impl blocks define methods and associated functions; traits define shared behavior. Composition and explicit ownership make relationships and lifetimes visible. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
struct Student{name:String,score:u8} impl Student{fn passed(&self)->bool{self.score>=60}} fn main(){let s=Student{name:"Avery".into(),score:82};println!("{} passed={}",s.name,s.passed());}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Moving a non-Copy field out of a borrowed struct.
2. Confusing associated functions with methods that receive self.
3. Implementing a trait method with a mismatched signature.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical inventory and CSV records and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (creating instances and methods); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain creating instances and methods using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
- [The Rust Programming Language: Method Syntax](https://doc.rust-lang.org/book/ch05-03-method-syntax.html)
- [The Rust Programming Language: Recoverable Errors with Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 7.2: Creating and Using a Class

### Learning Objectives
- Write a constructor function that validates and returns a `Result`.
- Create several instances with the same fields.
- Handle the error when a value is invalid.

### Concept Explanation

Rust has no constructors in the language; by convention an *associated function* named `new` builds a value: `Item::new("Notebook", 3, 2.50)`. Because Rust has no exceptions, a constructor that can fail returns a `Result<Item, String>`: `Ok(item)` for success or `Err(message)` for a clear failure. The caller must handle both cases, usually with `match` or `?`.

An `impl Item { ... }` block holds the functions. A method takes `&self` to read the value or `&mut self` to change it. The example creates the three shared inventory items and then tries to create an invalid one.

### Worked Example

```rust
struct Item {
    name: String,
    quantity: i32,
    unit_price: f64,
}

impl Item {
    fn new(name: &str, quantity: i32, unit_price: f64) -> Result<Item, String> {
        if quantity < 0 {
            return Err("quantity must not be negative".to_string());
        }
        if unit_price < 0.0 {
            return Err("unit price must not be negative".to_string());
        }
        Ok(Item { name: name.to_string(), quantity, unit_price })
    }

    fn total_value(&self) -> f64 {
        self.quantity as f64 * self.unit_price
    }
}

fn main() {
    let notebook = Item::new("Notebook", 3, 2.50).unwrap();
    let pencil = Item::new("Pencil", 10, 0.50).unwrap();
    let folder = Item::new("Folder", 4, 1.25).unwrap();

    for item in [&notebook, &pencil, &folder] {
        println!("{}: {} at {:.2}, value {:.2}", item.name, item.quantity, item.unit_price, item.total_value());
    }

    match Item::new("Broken", -1, 1.0) {
        Ok(item) => println!("Created {}", item.name),
        Err(message) => println!("Could not create the item: {message}"),
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50, value 7.50
Pencil: 10 at 0.50, value 5.00
Folder: 4 at 1.25, value 5.00
Could not create the item: quantity must not be negative
```

### Common Mistakes
1. Calling `unwrap()` on a `Result` from untrusted data, which panics on `Err`.
2. Forgetting `&self`, so the function is associated and cannot be called with the dot syntax.
3. Ignoring the `Err` case. The compiler warns about an unused `Result`.

### Activities
1. Create a fourth item with your own values and print it.
2. Add a rule that the name must not be blank.
3. Create two items with the same name and different quantities and show that they are separate values.
4. Explain the difference between `Item::new` and `item.total_value()`.

### Accessibility Practice

Say the signature aloud in order: 'fn new, open parenthesis, name colon ampersand str...' and check that your screen reader announces the arrow and the `Result` type. Print each item on its own line so output can be matched to values by ear.

### Skills Checklist
- [ ] I can write a `new` function.
- [ ] I can return a `Result` from a constructor.
- [ ] I can create several instances.
- [ ] I can handle the `Err` case.
- [ ] I can tell `&self` from `&mut self`.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 7.3: Associated functions and impl blocks

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Associated functions and impl blocks using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Rust models data with structs and enums rather than class inheritance. impl blocks define methods and associated functions; traits define shared behavior. Composition and explicit ownership make relationships and lifetimes visible. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
struct Point{x:f64,y:f64} impl Point{fn origin()->Self{Self{x:0.0,y:0.0}}} fn main(){let p=Point::origin();println!("({}, {})",p.x,p.y);}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Moving a non-Copy field out of a borrowed struct.
2. Confusing associated functions with methods that receive self.
3. Implementing a trait method with a mismatched signature.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical inventory and CSV records and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (associated functions and impl blocks); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain associated functions and impl blocks using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
- [The Rust Programming Language: Method Syntax](https://doc.rust-lang.org/book/ch05-03-method-syntax.html)
- [The Rust Programming Language: Implementing a Trait on a Type](https://doc.rust-lang.org/book/ch10-02-traits.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 7.3: Working with Attributes and Methods

### Learning Objectives
- Write methods that read, change, and consume a value.
- Define an associated constant.
- Implement `Display` so a value prints as a sentence.

### Concept Explanation

An `impl` block can hold three kinds of function. A method with **`&self`** reads the value, a method with **`&mut self`** changes it, and a method with **`self`** *consumes* it, so the value cannot be used afterward. A function without a `self` parameter, such as `new`, is an *associated function* called with `Item::new`. An *associated constant* such as `const LOW_STOCK: u32 = 5;` belongs to the type and is read as `Item::LOW_STOCK`.

`impl fmt::Display for Item` teaches `println!("{}", item)` how to print the value, so it prints as a useful sentence. The example adds a computed value, a low-stock check, a restock method with validation, a consuming summary, and `Display` to the shared Notebook.

### Worked Example

```rust
use std::fmt;

struct Item {
    name: String,
    quantity: u32,
    unit_price: f64,
}

impl Item {
    const LOW_STOCK: u32 = 5;

    fn new(name: &str, quantity: u32, unit_price: f64) -> Item {
        Item { name: name.to_string(), quantity, unit_price }
    }

    fn total_value(&self) -> f64 {
        self.quantity as f64 * self.unit_price
    }

    fn is_low_stock(&self) -> bool {
        self.quantity < Item::LOW_STOCK
    }

    fn restock(&mut self, amount: i32) {
        if amount < 0 {
            println!("Cannot restock a negative amount.");
            return;
        }
        self.quantity += amount as u32;
    }

    fn into_summary(self) -> String {
        format!("{} x{}", self.name, self.quantity)
    }
}

impl fmt::Display for Item {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}: {} at {:.2} each, value {:.2}", self.name, self.quantity, self.unit_price, self.total_value())
    }
}

fn main() {
    let mut notebook = Item::new("Notebook", 3, 2.50);
    println!("{notebook}");
    println!("Low stock: {}", notebook.is_low_stock());
    notebook.restock(2);
    println!("{notebook}");
    println!("Low stock: {}", notebook.is_low_stock());
    notebook.restock(-1);
    println!("{}", notebook.into_summary());
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
Low stock: true
Notebook: 5 at 2.50 each, value 12.50
Low stock: false
Cannot restock a negative amount.
Notebook x5
```

### Common Mistakes
1. Using a value after calling a method that takes `self`, which is a compile error because the value was consumed.
2. Calling a `&mut self` method on a binding that is not `mut`.
3. Forgetting `use std::fmt;` or the `fmt::Result` return type when implementing `Display`.

### Activities
1. Predict the six printed lines before running.
2. Add a method `discounted(&self, rate: f64) -> f64` that returns the value after a discount without changing the item.
3. Try to print `notebook` after `into_summary` and read the compiler message.
4. Explain the difference between `&self`, `&mut self`, and `self`.

### Accessibility Practice

Name methods after actions (`restock`) so a call reads as a sentence. A good `Display` gives the screen reader one complete line per value; say 'ampersand self' and 'self' aloud to hear the difference between a borrow and a move.

### Skills Checklist
- [ ] I can write read, change, and consume methods.
- [ ] I can define an associated constant.
- [ ] I can implement `Display`.
- [ ] I know a `self` method consumes the value.
- [ ] I can validate in a method.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 7.4: Traits and polymorphic behavior

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Traits and polymorphic behavior using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Rust models data with structs and enums rather than class inheritance. impl blocks define methods and associated functions; traits define shared behavior. Composition and explicit ownership make relationships and lifetimes visible. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
trait Summary{fn summary(&self)->String;} struct Task{title:String,done:bool} impl Summary for Task{fn summary(&self)->String{format!("{}: {}",self.title,if self.done {"done"}else{"open"})}} fn main(){let t=Task{title:"Study Rust".into(),done:false};println!("{}",t.summary());}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Moving a non-Copy field out of a borrowed struct.
2. Confusing associated functions with methods that receive self.
3. Implementing a trait method with a mismatched signature.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical inventory and CSV records and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (traits and polymorphic behavior); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain traits and polymorphic behavior using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
- [The Rust Programming Language: Traits: Defining Shared Behavior](https://doc.rust-lang.org/book/ch10-02-traits.html)
- [The Rust Programming Language: Using Trait Objects](https://doc.rust-lang.org/book/ch17-02-trait-objects.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 7.4: Inheritance

### Learning Objectives
- Define a trait with a default method.
- Implement the trait for two types.
- Explain polymorphism with generics and trait objects.

### Concept Explanation

Rust has no inheritance. Shared behavior is described by a **trait**: a set of methods that a type promises to provide. A trait may supply a *default method*, here `describe`, which calls the trait's other methods. Each type writes `impl Priced for Item { ... }` to implement the trait, and may override a default.

*Polymorphism* comes in two forms. A *generic* function, `fn print_total<T: Priced>(item: &T)`, is compiled for each type it is used with. A *trait object*, `Box<dyn Priced>`, lets one vector hold values of different types and picks the method at run time. A struct can hold another struct as a field (composition) instead of inheriting from it.

The example discounts the shared Folder (4 at 1.25) by 20 percent, so its value is 4.00 instead of 5.00.

### Worked Example

```rust
trait Priced {
    fn name(&self) -> &str;
    fn total_value(&self) -> f64;

    fn describe(&self) -> String {
        format!("{}: value {:.2}", self.name(), self.total_value())
    }
}

struct Item {
    name: String,
    quantity: u32,
    unit_price: f64,
}

struct DiscountedItem {
    item: Item,
    discount_rate: f64,
}

impl Priced for Item {
    fn name(&self) -> &str {
        &self.name
    }

    fn total_value(&self) -> f64 {
        self.quantity as f64 * self.unit_price
    }
}

impl Priced for DiscountedItem {
    fn name(&self) -> &str {
        self.item.name()
    }

    fn total_value(&self) -> f64 {
        self.item.total_value() * (1.0 - self.discount_rate)
    }
}

fn print_total<T: Priced>(item: &T) {
    println!("Generic: {}", item.describe());
}

fn main() {
    let notebook = Item { name: "Notebook".to_string(), quantity: 3, unit_price: 2.50 };
    let folder = DiscountedItem {
        item: Item { name: "Folder".to_string(), quantity: 4, unit_price: 1.25 },
        discount_rate: 0.20,
    };

    print_total(&folder);

    let items: Vec<Box<dyn Priced>> = vec![Box::new(notebook), Box::new(folder)];
    for item in &items {
        println!("{}", item.describe());
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Generic: Folder: value 4.00
Notebook: value 7.50
Folder: value 4.00
```

### Common Mistakes
1. Looking for `extends`. Rust has no inheritance; use a trait or a field.
2. Forgetting to implement a required method, which the compiler reports by name.
3. Putting values of different types in a plain `Vec<T>`, which allows only one type; use `Vec<Box<dyn Trait>>`.

### Activities
1. Predict the output before running.
2. Add a third type, `PerishableItem`, that implements `Priced` and override `describe`.
3. Explain why `describe` prints the discounted value without being rewritten.
4. Explain the difference between a generic function and a trait object.

### Accessibility Practice

Describe a trait as a list of promised methods. Speaking `impl Priced for DiscountedItem` aloud ('implement Priced for DiscountedItem') is clearer than a diagram. Print one line per value so the screen reader announces each result in order.

### Skills Checklist
- [ ] I can define a trait with a default method.
- [ ] I can implement a trait for two types.
- [ ] I can explain polymorphism.
- [ ] I know Rust has no inheritance.
- [ ] I can store trait objects in a vector.

---
>>>>>>> 2067a20 (curriculum clearning and updates)

## Lesson 7.5: Composition and ownership

### Reading References
<<<<<<< HEAD
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust standard library](https://doc.rust-lang.org/std/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain Composition and ownership using Rust's types, ownership model, and standard-library conventions.
- Select an idiomatic Rust construct rather than transliterating Python syntax.
- Predict, compile, and verify the example's behavior.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Rust models data with structs and enums rather than class inheritance. impl blocks define methods and associated functions; traits define shared behavior. Composition and explicit ownership make relationships and lifetimes visible. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools.

### Worked Example
```rust
struct Student{name:String} struct Enrollment{student:Student,course:String} fn main(){let e=Enrollment{student:Student{name:"Avery".into()},course:"Rust".into()};println!("{} is enrolled in {}",e.student.name,e.course);}
```

**Expected behavior:** Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output.

### Common Mistakes
1. Moving a non-Copy field out of a borrowed struct.
2. Confusing associated functions with methods that receive self.
3. Implementing a trait method with a mismatched signature.

### Activities
1. Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line.
2. Change the canonical inventory and CSV records and predict the result before running it.
3. Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change.
4. Refactor one part using the Rust feature named in this lesson (composition and ownership); run cargo check and explain the diagnostic output.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain composition and ownership using Rust terminology.
- [ ] I can compile and run the example with cargo run.
- [ ] I can explain the ownership, borrowing, and type decisions used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
=======
- [The Rust Programming Language: Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [The Rust Programming Language: Ownership](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)
- [Rust standard library documentation](https://doc.rust-lang.org/std/)
- Matching Python lesson: Lesson 7.5: Instances as Attributes (Composition)

### Learning Objectives
- Explain composition ("has a") and ownership of parts.
- Hold a vector of values inside a struct.
- Build an inventory from the shared items.

### Concept Explanation

*Composition* means one value contains other values. An inventory *has* items; it is not a kind of item. In Rust a struct **owns** its fields: `Inventory { items: Vec<Item> }` owns the vector and every item in it. `add(&mut self, item: Item)` takes the item by value, so ownership **moves** into the inventory and the caller can no longer use it.

Methods that look at the parts borrow: `find(&self, name)` returns `Option<&Item>`, a borrowed reference that lives no longer than the inventory. `remove` returns the owned item back as `Option<Item>`.

The example builds an `Inventory` with the three shared items and reports each quantity and the total value, 17.50.

### Worked Example

```rust
struct Item {
    name: String,
    quantity: u32,
    unit_price: f64,
}

impl Item {
    fn total_value(&self) -> f64 {
        self.quantity as f64 * self.unit_price
    }
}

struct Inventory {
    items: Vec<Item>,
}

impl Inventory {
    fn new() -> Inventory {
        Inventory { items: Vec::new() }
    }

    fn add(&mut self, item: Item) {
        self.items.push(item);
    }

    fn find(&self, name: &str) -> Option<&Item> {
        self.items.iter().find(|item| item.name == name)
    }

    fn remove(&mut self, name: &str) -> Option<Item> {
        let position = self.items.iter().position(|item| item.name == name)?;
        Some(self.items.remove(position))
    }

    fn total_value(&self) -> f64 {
        self.items.iter().map(|item| item.total_value()).sum()
    }

    fn report(&self) {
        for item in &self.items {
            println!("{}: {}", item.name, item.quantity);
        }
        println!("Total value: {:.2}", self.total_value());
    }
}

fn main() {
    let mut inventory = Inventory::new();
    inventory.add(Item { name: "Notebook".to_string(), quantity: 3, unit_price: 2.50 });
    inventory.add(Item { name: "Pencil".to_string(), quantity: 10, unit_price: 0.50 });
    inventory.add(Item { name: "Folder".to_string(), quantity: 4, unit_price: 1.25 });
    inventory.report();

    println!("{:?}", inventory.find("Pencil").map(|item| item.quantity));
    println!("{}", inventory.find("Eraser").is_none());
    let removed = inventory.remove("Pencil");
    println!("{}", removed.map(|item| item.name).unwrap_or_default());
    println!("{}", inventory.items.len());
}
```

### Expected Behavior or Output

The program prints:
```text
Notebook: 3
Pencil: 10
Folder: 4
Total value: 17.50
Some(10)
true
Pencil
2
```

### Common Mistakes
1. Using an item after passing it to `add`, which is a compile error because it was moved.
2. Returning a reference from `find` and then changing the inventory while still holding it.
3. Using inheritance thinking: an inventory is not a kind of item.

### Activities
1. Predict the output.
2. Add a method that returns the names of items with a quantity below 5.
3. Try to use `notebook` after `inventory.add(notebook)` and read the compiler message.
4. Explain "is a" versus "has a" with two examples.

### Accessibility Practice

Report the inventory as one labelled line per item and a final total line, so the screen reader reads a complete summary in order. Say 'ampersand' and 'ampersand mut' aloud so that borrows are heard.

### Skills Checklist
- [ ] I can explain composition.
- [ ] I can hold a vector in a struct.
- [ ] I understand ownership moving into a container.
- [ ] I can return a borrowed `Option<&Item>`.
- [ ] I can build the shared inventory.

---
>>>>>>> 2067a20 (curriculum clearning and updates)
