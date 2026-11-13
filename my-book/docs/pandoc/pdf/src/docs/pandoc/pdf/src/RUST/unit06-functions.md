[Header 2 ("unit-6-functions", [], []) [Str "Unit 6: Functions"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops functions through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly."], Header 3 ("lesson-61-defining-and-calling-functions", ["unnumbered", "unlisted"], []) [Str "Lesson 6.1: Defining and calling functions"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language"] ("https://doc.rust-lang.org/book/", "")]], [Plain [Link ("", [], []) [Str "Rust standard library"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Link ("", [], []) [Str "Cargo Book"] ("https://doc.rust-lang.org/cargo/", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain Defining and calling functions using Rust's types, ownership model, and standard-library conventions."]], [Plain [Str "Select an idiomatic Rust construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the example's behavior."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Functions declare parameter and return types. Borrow &T for read-only access and &mut T for exclusive mutation; accept owned values when retaining or transforming ownership. Generics express behavior over multiple types while preserving static checking. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "fn greet(name:&str) {println!(\"Hello, {name}!\");} fn main() {greet(\"Avery\");}
", Para [Strong [Str "Expected behavior:"], Str " Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output."], Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Returning a reference that outlives its owner."]], [Plain [Str "Taking ownership when a shared borrow is sufficient."]], [Plain [Str "Adding a semicolon to the final expression that should be returned."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and predict the result before running it."]], [Plain [Str "Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change."]], [Plain [Str "Refactor one part using the Rust feature named in this lesson (defining and calling functions); run cargo check and explain the diagnostic output."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain defining and calling functions using Rust terminology."]], [Plain [Str "\9744", Space, Str "I can compile and run the example with cargo run."]], [Plain [Str "\9744", Space, Str "I can explain the ownership, borrowing, and type decisions used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-62-parameters-ownership-and-borrowing", ["unnumbered", "unlisted"], []) [Str "Lesson 6.2: Parameters, ownership, and borrowing"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: What Is Ownership?"] ("https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: References and Borrowing"] ("https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 6.2: Passing Arguments"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain moving versus borrowing a value."]], [Plain [Str "Use a struct with ", Code ("", [], []) "Default", Str " in place of default and named arguments."]], [Plain [Str "Pass a reference to read data without taking it."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Rust has no default arguments and no named arguments. A struct with ", Code ("", [], []) "Default", Str " gives both: ", Code ("", [], []) "TipOptions { bill: 24.5, ..Default::default() }", Str " names each field and fills the rest from the default, here a tip rate of 0.15."], Para [Str "Passing a value to a function normally ", Strong [Str "moves"], Str " it: the function owns it, and the caller can no longer use it. Passing a ", Strong [Str "reference"], Str ", ", Code ("", [], []) "&name", Str ", lets the function ", Emph [Str "borrow"], Str " the value to read it, and the caller keeps ownership. ", Code ("", [], []) "&mut", Str " borrows it for changing, and Rust allows either many readers or one writer at a time."], Para [Str "With the shared bill of 24.50, the total at the default rate 0.15 is 28.18, at 0.20 it is 29.40, and at 0.10 it is 26.95."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "struct TipOptions {
    bill: f64,
    tip_rate: f64,
}

impl Default for TipOptions {
    fn default() -> Self {
        TipOptions { bill: 0.0, tip_rate: 0.15 }
    }
}

fn calculate_total(options: &TipOptions) -> f64 {
    options.bill + options.bill * options.tip_rate
}

fn borrow_length(text: &String) -> usize {
    text.len()
}

fn take_ownership(text: String) {
    println!(\"The function now owns {text}\");
}

fn main() {
    let default_rate = TipOptions { bill: 24.5, ..Default::default() };
    let high = TipOptions { bill: 24.5, tip_rate: 0.20 };
    let low = TipOptions { tip_rate: 0.10, bill: 24.5 };
    println!(\"{:.2}\", calculate_total(&default_rate));
    println!(\"{:.2}\", calculate_total(&high));
    println!(\"{:.2}\", calculate_total(&low));

    let name = String::from(\"Avery\");
    let length = borrow_length(&name);
    println!(\"{name} has {length} letters\");
    take_ownership(name);
    // println!(\"{name}\");   // would not compile: name was moved
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "28.18
29.40
26.95
Avery has 5 letters
The function now owns Avery
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using a value after passing it by value to a function, which is a compile error (\"borrow of moved value\")."]], [Plain [Str "Taking ", Code ("", [], []) "&String", Str " when ", Code ("", [], []) "&str", Str " would accept more kinds of text."]], [Plain [Str "Expecting default or named arguments. Use a struct with ", Code ("", [], []) "Default", Str "."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output before running."]], [Plain [Str "Uncomment the last line, read the compiler message, and restore the comment."]], [Plain [Str "Change ", Code ("", [], []) "borrow_length", Str " to take ", Code ("", [], []) "&str", Str " and call it with a literal and with a ", Code ("", [], []) "String", Str "."]], [Plain [Str "Explain in two sentences the difference between moving and borrowing."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "The compiler message for a moved value names the line where the move happened and the line where the value was used again, so read both. Say 'ampersand' aloud for a borrow and check that your screen reader announces it."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain move versus borrow."]], [Plain [Str "\9744", Space, Str "I can pass a reference."]], [Plain [Str "\9744", Space, Str "I can use a struct with ", Code ("", [], []) "Default", Str "."]], [Plain [Str "\9744", Space, Str "I can read a borrow-checker message."]], [Plain [Str "\9744", Space, Str "I know Rust has no default arguments."]]], HorizontalRule, Header 3 ("lesson-63-return-values-and-expressions", ["unnumbered", "unlisted"], []) [Str "Lesson 6.3: Return values and expressions"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Functions with Return Values"] ("https://doc.rust-lang.org/book/ch03-03-how-functions-work.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 6.3: Return Values"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Return a computed value as the final expression."]], [Plain [Str "Return an ", Code ("", [], []) "Option", Str " when a value may be missing."]], [Plain [Str "Return several values with a tuple or a struct."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A function's body ends with an ", Emph [Str "expression"], Str " ", Strong [Str "without a semicolon"], Str ", and that is its return value: ", Code ("", [], []) "fn classify(score: f64) -> &'static str { if score >= 90.0 { \"A\" } else { \"F\" } }", Str ". ", Code ("", [], []) "return value;", Str " leaves early. Adding a semicolon to the last line turns it into a statement and the function returns ", Code ("", [], []) "()", Str ", which the compiler rejects when a value is expected."], Para [Str "When a result may not exist, such as the average of an empty slice, return an ", Code ("", [], []) "Option<f64>", Str ": ", Code ("", [], []) "Some(x)", Str " or ", Code ("", [], []) "None", Str ". Rust has no null, so the caller must handle both cases. To return several values, return a tuple or a small struct."], Para [Str "The example returns the average of the shared scores, classifies the average, returns a minimum and maximum together, and shows the empty case."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "struct ScoreRange {
    low: i32,
    high: i32,
}

fn average(scores: &[i32]) -> Option<f64> {
    if scores.is_empty() {
        return None;
    }
    let total: i32 = scores.iter().sum();
    Some(total as f64 / scores.len() as f64)
}

fn classify(score: f64) -> &'static str {
    if score >= 90.0 {
        \"A\"
    } else if score >= 80.0 {
        \"B\"
    } else if score >= 70.0 {
        \"C\"
    } else if score >= 60.0 {
        \"D\"
    } else {
        \"F\"
    }
}

fn min_max(scores: &[i32]) -> ScoreRange {
    let low = *scores.iter().min().unwrap_or(&0);
    let high = *scores.iter().max().unwrap_or(&0);
    ScoreRange { low, high }
}

fn main() {
    let scores = [82, 91, 76, 88];
    let avg = average(&scores);
    println!(\"Average: {:?}\", avg);
    if let Some(value) = avg {
        println!(\"Grade for the average: {}\", classify(value));
    }
    let range = min_max(&scores);
    println!(\"Lowest and highest: {} and {}\", range.low, range.high);
    println!(\"{:?}\", average(&[]));
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Average: Some(84.25)
Grade for the average: B
Lowest and highest: 76 and 91
None
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Adding a semicolon to the last expression, so the function returns ", Code ("", [], []) "()", Str " instead of the value."]], [Plain [Str "Calling ", Code ("", [], []) "unwrap()", Str " on an empty ", Code ("", [], []) "Option", Str " and crashing."]], [Plain [Str "Printing inside the function and then trying to use the result in a calculation."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the four printed lines before running."]], [Plain [Str "Write ", Code ("", [], []) "total(scores: &[i32]) -> i32", Str " that returns the sum."]], [Plain [Str "Write ", Code ("", [], []) "is_passing(score: i32) -> bool", Str "."]], [Plain [Str "Explain how a caller should use a function that returns ", Code ("", [], []) "Option<f64>", Str "."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Return values instead of printing inside logic functions, so the caller prints once and the screen reader announces each result a single time."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can return the final expression."]], [Plain [Str "\9744", Space, Str "I can return an ", Code ("", [], []) "Option", Str "."]], [Plain [Str "\9744", Space, Str "I can return several values."]], [Plain [Str "\9744", Space, Str "I know a trailing semicolon changes the meaning."]], [Plain [Str "\9744", Space, Str "I can classify an average with the shared thresholds."]]], HorizontalRule, Header 3 ("lesson-64-functions-over-collections", ["unnumbered", "unlisted"], []) [Str "Lesson 6.4: Functions over collections"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: References and Borrowing"] ("https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: The Slice Type"] ("https://doc.rust-lang.org/book/ch04-03-slices.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 6.4: Functions with Lists and Dictionaries"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Pass a slice to read and ", Code ("", [], []) "&mut Vec", Str " to change."]], [Plain [Str "Return a new vector and leave the original unchanged."]], [Plain [Str "Process the shared inventory with a function."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A function that only ", Strong [Str "reads"], Str " a list takes a ", Emph [Str "slice"], Str ", ", Code ("", [], []) "&[i32]", Str ", which accepts a vector, an array, or part of either without copying. A function that ", Strong [Str "changes"], Str " a vector takes ", Code ("", [], []) "&mut Vec<i32>", Str ", and the caller passes ", Code ("", [], []) "&mut scores", Str "; the call site shows that a change will happen. A function can also take ownership and return a new vector."], Para [Str "Rust enforces the rules at compile time: while a function holds a ", Code ("", [], []) "&mut", Str ", nothing else may read the vector. That removes a whole class of bugs that other languages find at run time."], Para [Str "The shared inventory is Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25), worth 17.50 in total."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "struct Item {
    name: String,
    quantity: u32,
    unit_price: f64,
}

fn add_score(score_list: &mut Vec<i32>, new_score: i32) {
    score_list.push(new_score);
}

fn with_score(score_list: &[i32], new_score: i32) -> Vec<i32> {
    let mut copy = score_list.to_vec();
    copy.push(new_score);
    copy
}

fn inventory_value(inventory: &[Item]) -> f64 {
    inventory.iter().map(|item| item.quantity as f64 * item.unit_price).sum()
}

fn main() {
    let mut scores = vec![82, 91, 76, 88];
    add_score(&mut scores, 95);
    println!(\"{:?}\", scores);

    let longer = with_score(&scores, 100);
    println!(\"{} {}\", scores.len(), longer.len());

    let inventory = vec![
        Item { name: \"Notebook\".to_string(), quantity: 3, unit_price: 2.50 },
        Item { name: \"Pencil\".to_string(), quantity: 10, unit_price: 0.50 },
        Item { name: \"Folder\".to_string(), quantity: 4, unit_price: 1.25 },
    ];
    println!(\"Total inventory value: {:.2}\", inventory_value(&inventory));
    println!(\"{}\", inventory.iter().map(|item| item.name.as_str()).collect::<Vec<_>>().join(\", \"));
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "[82, 91, 76, 88, 95]
5 6
Total inventory value: 17.50
Notebook, Pencil, Folder
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Passing ", Code ("", [], []) "&scores", Str " to a function that needs ", Code ("", [], []) "&mut Vec<i32>", Str ", which is a compile error."]], [Plain [Str "Taking ", Code ("", [], []) "&Vec<i32>", Str " in a function that only reads, instead of the more flexible ", Code ("", [], []) "&[i32]", Str "."]], [Plain [Str "Holding a reference to an element while calling a function that pushes to the vector."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the four printed lines before running."]], [Plain [Str "Write ", Code ("", [], []) "scale_prices(inventory: &mut [Item], factor: f64)", Str " that changes prices in place."]], [Plain [Str "Write a version that returns a new vector and leaves the original unchanged."]], [Plain [Str "Explain why ", Code ("", [], []) "&mut", Str " appears at the call site."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "State aloud before each call whether the function changes its argument: ", Code ("", [], []) "&mut", Str " at the call site and a name such as ", Code ("", [], []) "add_score", Str " both say so. Print the list before and after so the effect is heard."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can pass a slice to read."]], [Plain [Str "\9744", Space, Str "I can pass ", Code ("", [], []) "&mut Vec", Str " to change."]], [Plain [Str "\9744", Space, Str "I can return a new vector."]], [Plain [Str "\9744", Space, Str "I can explain why ", Code ("", [], []) "&mut", Str " is written at the call."]], [Plain [Str "\9744", Space, Str "I can total the shared inventory."]]], HorizontalRule, Header 3 ("lesson-65-scope-generics-and-variadic-alternatives", ["unnumbered", "unlisted"], []) [Str "Lesson 6.5: Scope, generics, and variadic alternatives"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Generic Data Types"] ("https://doc.rust-lang.org/book/ch10-01-syntax.html", "")]], [Plain [Link ("", [], []) [Str "Rust by Example: macro_rules!"] ("https://doc.rust-lang.org/rust-by-example/macros.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 6.5: Arbitrary Number of Arguments"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Take any number of values with a slice."]], [Plain [Str "Write a generic function over a type parameter."]], [Plain [Str "Explain scope and a variadic macro."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Rust functions have a fixed number of parameters; there are no variadic functions. The usual replacement is a ", Strong [Str "slice"], Str ": ", Code ("", [], []) "average_of(&[82, 91, 76, 88])", Str " takes any number of values. A ", Emph [Str "macro"], Str " defined with ", Code ("", [], []) "macro_rules!", Str " can accept a repeated pattern, which is how ", Code ("", [], []) "println!", Str " and ", Code ("", [], []) "vec!", Str " take any number of arguments."], Para [Str "A ", Emph [Str "generic"], Str " function works for many types: ", Code ("", [], []) "fn largest<T: PartialOrd + Copy>(items: &[T]) -> T", Str " accepts any type that can be compared and copied. ", Emph [Str "Scope"], Str " is the region where a name is visible: a ", Code ("", [], []) "{ ... }", Str " block creates a scope, and a name declared inside ends at the closing brace. An inner binding with the same name ", Emph [Str "shadows"], Str " the outer one."], Para [Str "The shared scores average 84.25, and the average of 90 and 80 is 85."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "macro_rules! average {
    ($($x:expr),+ $(,)?) => {{
        let values = [$($x as f64),+];
        values.iter().sum::<f64>() / values.len() as f64
    }};
}

fn average_of(scores: &[i32]) -> Option<f64> {
    if scores.is_empty() {
        None
    } else {
        Some(scores.iter().sum::<i32>() as f64 / scores.len() as f64)
    }
}

fn largest<T: PartialOrd + Copy>(items: &[T]) -> T {
    let mut best = items[0];
    for &item in items {
        if item > best {
            best = item;
        }
    }
    best
}

fn main() {
    println!(\"{}\", average!(82, 91, 76, 88));
    println!(\"{}\", average!(90, 80));
    println!(\"{:?}\", average_of(&[82, 91, 76, 88]));
    println!(\"{:?}\", average_of(&[]));

    println!(\"{} {} {}\", largest(&[82, 91, 76]), largest(&[2.5, 0.5]), largest(&['a', 'z', 'm']));

    let value = 1;
    {
        let value = value + 41;
        println!(\"inner {value}\");
    }
    println!(\"outer {value}\");
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "84.25
85
Some(84.25)
None
91 2.5 z
inner 42
outer 1
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Looking for a variadic function. Use a slice or a macro."]], [Plain [Str "Calling ", Code ("", [], []) "largest(&[])", Str " on an empty slice, which panics because it reads ", Code ("", [], []) "items[0]", Str "."]], [Plain [Str "Forgetting the trait bounds on ", Code ("", [], []) "T", Str ", so the comparison does not compile."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict each printed line."]], [Plain [Str "Write ", Code ("", [], []) "maximum_of(scores: &[i32]) -> Option<i32>", Str " that handles an empty slice."]], [Plain [Str "Call ", Code ("", [], []) "largest", Str " with a slice of words (", Code ("", [], []) "&str", Str ") and explain why it works."]], [Plain [Str "Explain scope and shadowing using the last lines of the example."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read macro and generic syntax aloud one piece at a time: 'fn largest, angle bracket T colon PartialOrd plus Copy, close angle bracket'. Check that your screen reader announces the angle brackets and the plus sign."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can take many values with a slice."]], [Plain [Str "\9744", Space, Str "I can write a generic function."]], [Plain [Str "\9744", Space, Str "I understand scope and shadowing."]], [Plain [Str "\9744", Space, Str "I can read a macro call."]], [Plain [Str "\9744", Space, Str "I handle the empty case."]]], HorizontalRule]