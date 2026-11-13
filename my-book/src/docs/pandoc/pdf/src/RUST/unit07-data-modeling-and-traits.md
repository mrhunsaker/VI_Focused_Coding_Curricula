[Header 2 ("unit-7-data-modeling-and-traits", [], []) [Str "Unit 7: Data Modeling and Traits"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops data modeling and traits through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly."], Header 3 ("lesson-71-structs-enums-and-data-modeling", ["unnumbered", "unlisted"], []) [Str "Lesson 7.1: Structs, enums, and data modeling"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Defining and Instantiating Structs"] ("https://doc.rust-lang.org/book/ch05-01-defining-structs.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Defining an Enum"] ("https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Modules and Privacy"] ("https://doc.rust-lang.org/book/ch07-02-defining-modules-to-control-scope-and-privacy.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 7.1: Why Learn About Classes?"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Model data with a struct and with an enum."]], [Plain [Str "Hide a field with module privacy and change it only through methods."]], [Plain [Str "Explain that Rust has no classes and no inheritance."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Rust has no classes. Data is modeled with a ", Strong [Str "struct"], Str " (named fields) or an ", Strong [Str "enum"], Str " (a value that is exactly one of several variants), and behavior is added in ", Code ("", [], []) "impl", Str " blocks (Lesson 7.3) and ", Emph [Str "traits"], Str " (Lesson 7.4). Bundling data with the functions that work on it, and hiding the details, is still called ", Strong [Str "encapsulation"], Str "."], Para [Str "Privacy in Rust is controlled by ", Emph [Str "modules"], Str ". Fields and functions are private to the module they are written in unless marked ", Code ("", [], []) "pub", Str ". In the example, ", Code ("", [], []) "mod inventory", Str " holds an ", Code ("", [], []) "Item", Str " whose ", Code ("", [], []) "quantity", Str " field is private: code outside the module can read it only through the ", Code ("", [], []) "quantity()", Str " method and change it only through ", Code ("", [], []) "restock", Str "."], Para [Code ("", [], []) "match", Str " on an enum must cover every variant, so adding a new variant later makes the compiler point at every place that needs a decision. The shared Notebook has quantity 3; restocking 2 gives 5."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "mod inventory {
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
    let mut notebook = inventory::Item::new(\"Notebook\", 3, 2.50);
    println!(\"{}: {} at {} is {:?}\", notebook.name, notebook.quantity(), notebook.unit_price, status(notebook.quantity()));
    notebook.restock(2);
    println!(\"{}: {} is now {:?}\", notebook.name, notebook.quantity(), status(notebook.quantity()));
    println!(\"{:?}\", status(0));
    // notebook.quantity = 99;   // would not compile: the field is private
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Notebook: 3 at 2.5 is Low
Notebook: 5 is now Enough
Out
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Looking for a ", Code ("", [], []) "class", Str " keyword. Rust uses structs, enums, impl blocks, and traits."]], [Plain [Str "Making every field ", Code ("", [], []) "pub", Str ", so outside code can put the value into an invalid state."]], [Plain [Str "Forgetting a variant in a ", Code ("", [], []) "match", Str " on an enum, which the compiler rejects."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the three printed lines before running."]], [Plain [Str "Add a variant ", Code ("", [], []) "Overstocked", Str " for quantities above 100 and fix every ", Code ("", [], []) "match", Str " the compiler points to."]], [Plain [Str "Uncomment the assignment, read the compiler message, and restore the comment."]], [Plain [Str "Explain what encapsulation means and how modules provide it."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Describe a data type as a list read in order: the name, then each field, then each variant. Reading a struct aloud works best by saying 'pub struct Item, open brace, pub name colon String comma...' and listening for the braces that show structure."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can model data with a struct and an enum."]], [Plain [Str "\9744", Space, Str "I can hide a field with a module."]], [Plain [Str "\9744", Space, Str "I know Rust has no classes."]], [Plain [Str "\9744", Space, Str "I can read a struct definition aloud."]], [Plain [Str "\9744", Space, Str "I can match every enum variant."]]], HorizontalRule, Header 3 ("lesson-72-creating-instances-and-methods", ["unnumbered", "unlisted"], []) [Str "Lesson 7.2: Creating instances and methods"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Method Syntax"] ("https://doc.rust-lang.org/book/ch05-03-method-syntax.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Recoverable Errors with Result"] ("https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 7.2: Creating and Using a Class"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write a constructor function that validates and returns a ", Code ("", [], []) "Result", Str "."]], [Plain [Str "Create several instances with the same fields."]], [Plain [Str "Handle the error when a value is invalid."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Rust has no constructors in the language; by convention an ", Emph [Str "associated function"], Str " named ", Code ("", [], []) "new", Str " builds a value: ", Code ("", [], []) "Item::new(\"Notebook\", 3, 2.50)", Str ". Because Rust has no exceptions, a constructor that can fail returns a ", Code ("", [], []) "Result<Item, String>", Str ": ", Code ("", [], []) "Ok(item)", Str " for success or ", Code ("", [], []) "Err(message)", Str " for a clear failure. The caller must handle both cases, usually with ", Code ("", [], []) "match", Str " or ", Code ("", [], []) "?", Str "."], Para [Str "An ", Code ("", [], []) "impl Item { ... }", Str " block holds the functions. A method takes ", Code ("", [], []) "&self", Str " to read the value or ", Code ("", [], []) "&mut self", Str " to change it. The example creates the three shared inventory items and then tries to create an invalid one."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "struct Item {
    name: String,
    quantity: i32,
    unit_price: f64,
}

impl Item {
    fn new(name: &str, quantity: i32, unit_price: f64) -> Result<Item, String> {
        if quantity < 0 {
            return Err(\"quantity must not be negative\".to_string());
        }
        if unit_price < 0.0 {
            return Err(\"unit price must not be negative\".to_string());
        }
        Ok(Item { name: name.to_string(), quantity, unit_price })
    }

    fn total_value(&self) -> f64 {
        self.quantity as f64 * self.unit_price
    }
}

fn main() {
    let notebook = Item::new(\"Notebook\", 3, 2.50).unwrap();
    let pencil = Item::new(\"Pencil\", 10, 0.50).unwrap();
    let folder = Item::new(\"Folder\", 4, 1.25).unwrap();

    for item in [&notebook, &pencil, &folder] {
        println!(\"{}: {} at {:.2}, value {:.2}\", item.name, item.quantity, item.unit_price, item.total_value());
    }

    match Item::new(\"Broken\", -1, 1.0) {
        Ok(item) => println!(\"Created {}\", item.name),
        Err(message) => println!(\"Could not create the item: {message}\"),
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Notebook: 3 at 2.50, value 7.50
Pencil: 10 at 0.50, value 5.00
Folder: 4 at 1.25, value 5.00
Could not create the item: quantity must not be negative
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Calling ", Code ("", [], []) "unwrap()", Str " on a ", Code ("", [], []) "Result", Str " from untrusted data, which panics on ", Code ("", [], []) "Err", Str "."]], [Plain [Str "Forgetting ", Code ("", [], []) "&self", Str ", so the function is associated and cannot be called with the dot syntax."]], [Plain [Str "Ignoring the ", Code ("", [], []) "Err", Str " case. The compiler warns about an unused ", Code ("", [], []) "Result", Str "."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create a fourth item with your own values and print it."]], [Plain [Str "Add a rule that the name must not be blank."]], [Plain [Str "Create two items with the same name and different quantities and show that they are separate values."]], [Plain [Str "Explain the difference between ", Code ("", [], []) "Item::new", Str " and ", Code ("", [], []) "item.total_value()", Str "."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Say the signature aloud in order: 'fn new, open parenthesis, name colon ampersand str...' and check that your screen reader announces the arrow and the ", Code ("", [], []) "Result", Str " type. Print each item on its own line so output can be matched to values by ear."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a ", Code ("", [], []) "new", Str " function."]], [Plain [Str "\9744", Space, Str "I can return a ", Code ("", [], []) "Result", Str " from a constructor."]], [Plain [Str "\9744", Space, Str "I can create several instances."]], [Plain [Str "\9744", Space, Str "I can handle the ", Code ("", [], []) "Err", Str " case."]], [Plain [Str "\9744", Space, Str "I can tell ", Code ("", [], []) "&self", Str " from ", Code ("", [], []) "&mut self", Str "."]]], HorizontalRule, Header 3 ("lesson-73-associated-functions-and-impl-blocks", ["unnumbered", "unlisted"], []) [Str "Lesson 7.3: Associated functions and impl blocks"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Method Syntax"] ("https://doc.rust-lang.org/book/ch05-03-method-syntax.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Implementing a Trait on a Type"] ("https://doc.rust-lang.org/book/ch10-02-traits.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 7.3: Working with Attributes and Methods"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write methods that read, change, and consume a value."]], [Plain [Str "Define an associated constant."]], [Plain [Str "Implement ", Code ("", [], []) "Display", Str " so a value prints as a sentence."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "An ", Code ("", [], []) "impl", Str " block can hold three kinds of function. A method with ", Strong [Code ("", [], []) "&self"], Str " reads the value, a method with ", Strong [Code ("", [], []) "&mut self"], Str " changes it, and a method with ", Strong [Code ("", [], []) "self"], Str " ", Emph [Str "consumes"], Str " it, so the value cannot be used afterward. A function without a ", Code ("", [], []) "self", Str " parameter, such as ", Code ("", [], []) "new", Str ", is an ", Emph [Str "associated function"], Str " called with ", Code ("", [], []) "Item::new", Str ". An ", Emph [Str "associated constant"], Str " such as ", Code ("", [], []) "const LOW_STOCK: u32 = 5;", Str " belongs to the type and is read as ", Code ("", [], []) "Item::LOW_STOCK", Str "."], Para [Code ("", [], []) "impl fmt::Display for Item", Str " teaches ", Code ("", [], []) "println!(\"{}\", item)", Str " how to print the value, so it prints as a useful sentence. The example adds a computed value, a low-stock check, a restock method with validation, a consuming summary, and ", Code ("", [], []) "Display", Str " to the shared Notebook."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::fmt;

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
            println!(\"Cannot restock a negative amount.\");
            return;
        }
        self.quantity += amount as u32;
    }

    fn into_summary(self) -> String {
        format!(\"{} x{}\", self.name, self.quantity)
    }
}

impl fmt::Display for Item {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, \"{}: {} at {:.2} each, value {:.2}\", self.name, self.quantity, self.unit_price, self.total_value())
    }
}

fn main() {
    let mut notebook = Item::new(\"Notebook\", 3, 2.50);
    println!(\"{notebook}\");
    println!(\"Low stock: {}\", notebook.is_low_stock());
    notebook.restock(2);
    println!(\"{notebook}\");
    println!(\"Low stock: {}\", notebook.is_low_stock());
    notebook.restock(-1);
    println!(\"{}\", notebook.into_summary());
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Notebook: 3 at 2.50 each, value 7.50
Low stock: true
Notebook: 5 at 2.50 each, value 12.50
Low stock: false
Cannot restock a negative amount.
Notebook x5
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using a value after calling a method that takes ", Code ("", [], []) "self", Str ", which is a compile error because the value was consumed."]], [Plain [Str "Calling a ", Code ("", [], []) "&mut self", Str " method on a binding that is not ", Code ("", [], []) "mut", Str "."]], [Plain [Str "Forgetting ", Code ("", [], []) "use std::fmt;", Str " or the ", Code ("", [], []) "fmt::Result", Str " return type when implementing ", Code ("", [], []) "Display", Str "."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the six printed lines before running."]], [Plain [Str "Add a method ", Code ("", [], []) "discounted(&self, rate: f64) -> f64", Str " that returns the value after a discount without changing the item."]], [Plain [Str "Try to print ", Code ("", [], []) "notebook", Str " after ", Code ("", [], []) "into_summary", Str " and read the compiler message."]], [Plain [Str "Explain the difference between ", Code ("", [], []) "&self", Str ", ", Code ("", [], []) "&mut self", Str ", and ", Code ("", [], []) "self", Str "."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Name methods after actions (", Code ("", [], []) "restock", Str ") so a call reads as a sentence. A good ", Code ("", [], []) "Display", Str " gives the screen reader one complete line per value; say 'ampersand self' and 'self' aloud to hear the difference between a borrow and a move."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write read, change, and consume methods."]], [Plain [Str "\9744", Space, Str "I can define an associated constant."]], [Plain [Str "\9744", Space, Str "I can implement ", Code ("", [], []) "Display", Str "."]], [Plain [Str "\9744", Space, Str "I know a ", Code ("", [], []) "self", Str " method consumes the value."]], [Plain [Str "\9744", Space, Str "I can validate in a method."]]], HorizontalRule, Header 3 ("lesson-74-traits-and-polymorphic-behavior", ["unnumbered", "unlisted"], []) [Str "Lesson 7.4: Traits and polymorphic behavior"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Traits: Defining Shared Behavior"] ("https://doc.rust-lang.org/book/ch10-02-traits.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Using Trait Objects"] ("https://doc.rust-lang.org/book/ch17-02-trait-objects.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 7.4: Inheritance"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Define a trait with a default method."]], [Plain [Str "Implement the trait for two types."]], [Plain [Str "Explain polymorphism with generics and trait objects."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Rust has no inheritance. Shared behavior is described by a ", Strong [Str "trait"], Str ": a set of methods that a type promises to provide. A trait may supply a ", Emph [Str "default method"], Str ", here ", Code ("", [], []) "describe", Str ", which calls the trait's other methods. Each type writes ", Code ("", [], []) "impl Priced for Item { ... }", Str " to implement the trait, and may override a default."], Para [Emph [Str "Polymorphism"], Str " comes in two forms. A ", Emph [Str "generic"], Str " function, ", Code ("", [], []) "fn print_total<T: Priced>(item: &T)", Str ", is compiled for each type it is used with. A ", Emph [Str "trait object"], Str ", ", Code ("", [], []) "Box<dyn Priced>", Str ", lets one vector hold values of different types and picks the method at run time. A struct can hold another struct as a field (composition) instead of inheriting from it."], Para [Str "The example discounts the shared Folder (4 at 1.25) by 20 percent, so its value is 4.00 instead of 5.00."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "trait Priced {
    fn name(&self) -> &str;
    fn total_value(&self) -> f64;

    fn describe(&self) -> String {
        format!(\"{}: value {:.2}\", self.name(), self.total_value())
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
    println!(\"Generic: {}\", item.describe());
}

fn main() {
    let notebook = Item { name: \"Notebook\".to_string(), quantity: 3, unit_price: 2.50 };
    let folder = DiscountedItem {
        item: Item { name: \"Folder\".to_string(), quantity: 4, unit_price: 1.25 },
        discount_rate: 0.20,
    };

    print_total(&folder);

    let items: Vec<Box<dyn Priced>> = vec![Box::new(notebook), Box::new(folder)];
    for item in &items {
        println!(\"{}\", item.describe());
    }
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Generic: Folder: value 4.00
Notebook: value 7.50
Folder: value 4.00
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Looking for ", Code ("", [], []) "extends", Str ". Rust has no inheritance; use a trait or a field."]], [Plain [Str "Forgetting to implement a required method, which the compiler reports by name."]], [Plain [Str "Putting values of different types in a plain ", Code ("", [], []) "Vec<T>", Str ", which allows only one type; use ", Code ("", [], []) "Vec<Box<dyn Trait>>", Str "."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output before running."]], [Plain [Str "Add a third type, ", Code ("", [], []) "PerishableItem", Str ", that implements ", Code ("", [], []) "Priced", Str " and override ", Code ("", [], []) "describe", Str "."]], [Plain [Str "Explain why ", Code ("", [], []) "describe", Str " prints the discounted value without being rewritten."]], [Plain [Str "Explain the difference between a generic function and a trait object."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Describe a trait as a list of promised methods. Speaking ", Code ("", [], []) "impl Priced for DiscountedItem", Str " aloud ('implement Priced for DiscountedItem') is clearer than a diagram. Print one line per value so the screen reader announces each result in order."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can define a trait with a default method."]], [Plain [Str "\9744", Space, Str "I can implement a trait for two types."]], [Plain [Str "\9744", Space, Str "I can explain polymorphism."]], [Plain [Str "\9744", Space, Str "I know Rust has no inheritance."]], [Plain [Str "\9744", Space, Str "I can store trait objects in a vector."]]], HorizontalRule, Header 3 ("lesson-75-composition-and-ownership", ["unnumbered", "unlisted"], []) [Str "Lesson 7.5: Composition and ownership"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Structs"] ("https://doc.rust-lang.org/book/ch05-01-defining-structs.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Ownership"] ("https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 7.5: Instances as Attributes (Composition)"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain composition (\"has a\") and ownership of parts."]], [Plain [Str "Hold a vector of values inside a struct."]], [Plain [Str "Build an inventory from the shared items."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Emph [Str "Composition"], Str " means one value contains other values. An inventory ", Emph [Str "has"], Str " items; it is not a kind of item. In Rust a struct ", Strong [Str "owns"], Str " its fields: ", Code ("", [], []) "Inventory { items: Vec<Item> }", Str " owns the vector and every item in it. ", Code ("", [], []) "add(&mut self, item: Item)", Str " takes the item by value, so ownership ", Strong [Str "moves"], Str " into the inventory and the caller can no longer use it."], Para [Str "Methods that look at the parts borrow: ", Code ("", [], []) "find(&self, name)", Str " returns ", Code ("", [], []) "Option<&Item>", Str ", a borrowed reference that lives no longer than the inventory. ", Code ("", [], []) "remove", Str " returns the owned item back as ", Code ("", [], []) "Option<Item>", Str "."], Para [Str "The example builds an ", Code ("", [], []) "Inventory", Str " with the three shared items and reports each quantity and the total value, 17.50."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "struct Item {
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
            println!(\"{}: {}\", item.name, item.quantity);
        }
        println!(\"Total value: {:.2}\", self.total_value());
    }
}

fn main() {
    let mut inventory = Inventory::new();
    inventory.add(Item { name: \"Notebook\".to_string(), quantity: 3, unit_price: 2.50 });
    inventory.add(Item { name: \"Pencil\".to_string(), quantity: 10, unit_price: 0.50 });
    inventory.add(Item { name: \"Folder\".to_string(), quantity: 4, unit_price: 1.25 });
    inventory.report();

    println!(\"{:?}\", inventory.find(\"Pencil\").map(|item| item.quantity));
    println!(\"{}\", inventory.find(\"Eraser\").is_none());
    let removed = inventory.remove(\"Pencil\");
    println!(\"{}\", removed.map(|item| item.name).unwrap_or_default());
    println!(\"{}\", inventory.items.len());
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Notebook: 3
Pencil: 10
Folder: 4
Total value: 17.50
Some(10)
true
Pencil
2
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using an item after passing it to ", Code ("", [], []) "add", Str ", which is a compile error because it was moved."]], [Plain [Str "Returning a reference from ", Code ("", [], []) "find", Str " and then changing the inventory while still holding it."]], [Plain [Str "Using inheritance thinking: an inventory is not a kind of item."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output."]], [Plain [Str "Add a method that returns the names of items with a quantity below 5."]], [Plain [Str "Try to use ", Code ("", [], []) "notebook", Str " after ", Code ("", [], []) "inventory.add(notebook)", Str " and read the compiler message."]], [Plain [Str "Explain \"is a\" versus \"has a\" with two examples."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Report the inventory as one labelled line per item and a final total line, so the screen reader reads a complete summary in order. Say 'ampersand' and 'ampersand mut' aloud so that borrows are heard."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain composition."]], [Plain [Str "\9744", Space, Str "I can hold a vector in a struct."]], [Plain [Str "\9744", Space, Str "I understand ownership moving into a container."]], [Plain [Str "\9744", Space, Str "I can return a borrowed ", Code ("", [], []) "Option<&Item>", Str "."]], [Plain [Str "\9744", Space, Str "I can build the shared inventory."]]], HorizontalRule]