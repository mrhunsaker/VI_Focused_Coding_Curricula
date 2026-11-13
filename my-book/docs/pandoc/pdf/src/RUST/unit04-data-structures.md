[Header 2 ("unit-4-data-structures", [], []) [Str "Unit 4: Data Structures"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops data structures through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly."], Header 3 ("lesson-41-vectors-and-collection-mutation", ["unnumbered", "unlisted"], []) [Str "Lesson 4.1: Vectors and collection mutation"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Vectors"] ("https://doc.rust-lang.org/book/ch08-01-vectors.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 4.1: More on Lists"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Push, insert, replace, and remove vector items."]], [Plain [Str "Remove by value using ", Code ("", [], []) "position", Str " and by condition using ", Code ("", [], []) "retain", Str "."]], [Plain [Str "Handle an empty ", Code ("", [], []) "pop", Str " with ", Code ("", [], []) "Option", Str "."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Code ("", [], []) "Vec", Str " changes with ", Code ("", [], []) "push(value)", Str " (append), ", Code ("", [], []) "insert(index, value)", Str " (insert and shift), ", Code ("", [], []) "scores[i] = value", Str " (replace), ", Code ("", [], []) "remove(index)", Str " (remove by ", Strong [Str "position"], Str " and return the item), ", Code ("", [], []) "pop()", Str " (remove and return the last item as an ", Code ("", [], []) "Option", Str ", because the vector might be empty), and ", Code ("", [], []) "retain(|item| condition)", Str " (keep only matching items). Rust has no \"remove by value\"; find the position first with ", Code ("", [], []) "iter().position(|&s| s == value)", Str ", which returns an ", Code ("", [], []) "Option<usize>", Str "."], Para [Code ("", [], []) "contains(&value)", Str " tests membership. All of these methods need the vector to be declared ", Code ("", [], []) "mut", Str ", and Rust checks at compile time that nothing else holds a borrow of the vector while it changes."], Para [Str "The example applies the same operations as the Python course to the shared scores, from [82, 91, 76, 88] to [82, 85, 93, 88]."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "fn main() {
    let mut scores = vec![82, 91, 76, 88];

    scores.push(95);
    scores.insert(1, 85);
    scores[2] = 93;
    if let Some(position) = scores.iter().position(|&s| s == 76) {
        scores.remove(position);
    }
    let last = scores.pop();

    println!(\"{:?}\", scores);
    println!(\"{} items; removed {:?}\", scores.len(), last);
    println!(\"{}\", scores.contains(&88));
    println!(\"{:?}\", scores.iter().position(|&s| s == 88));
    println!(\"{:?}\", scores.iter().position(|&s| s == 100));

    scores.retain(|&s| s >= 90);
    println!(\"{:?}\", scores);
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "[82, 85, 93, 88]
4 items; removed Some(95)
true
Some(3)
None
[93]
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Looking for a ", Code ("", [], []) "remove_value", Str " method. Find the position first, then remove by index."]], [Plain [Str "Calling ", Code ("", [], []) "remove(index)", Str " with an index that is too large, which panics."]], [Plain [Str "Holding a reference into the vector (", Code ("", [], []) "let first = &scores[0];", Str ") and then calling ", Code ("", [], []) "push", Str ", which the borrow checker rejects."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace the vector after every operation and write each version as a sentence."]], [Plain [Str "Remove the first score with ", Code ("", [], []) "remove(0)", Str " and describe what happens to the others."]], [Plain [Str "Remove every score below 80 with ", Code ("", [], []) "retain", Str "."]], [Plain [Str "Print the position of the first score above 90."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "After every change, print the whole vector on one line so the screen reader reads a complete state in one pass. Say the method names aloud and notice how ", Code ("", [], []) "remove", Str " and ", Code ("", [], []) "retain", Str " differ in what they take."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can push, insert, replace, and remove items."]], [Plain [Str "\9744", Space, Str "I can find a position with ", Code ("", [], []) "position", Str "."]], [Plain [Str "\9744", Space, Str "I can filter with ", Code ("", [], []) "retain", Str "."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "pop", Str " returns an ", Code ("", [], []) "Option", Str "."]], [Plain [Str "\9744", Space, Str "I can show a vector in one line."]]], HorizontalRule, Header 3 ("lesson-42-sorting-and-organizing-data", ["unnumbered", "unlisted"], []) [Str "Lesson 4.2: Sorting and organizing data"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Vectors"] ("https://doc.rust-lang.org/book/ch08-01-vectors.html", "")]], [Plain [Link ("", [], []) [Str "Vec sorting methods"] ("https://doc.rust-lang.org/std/vec/struct.Vec.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 4.2: Organizing Lists"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Sort a vector ascending and descending."]], [Plain [Str "Sort a clone so the original is unchanged."]], [Plain [Str "Sort by a computed key and sort decimals."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "sort()", Str " sorts a ", Code ("", [], []) "mut", Str " vector ", Strong [Str "in place"], Str ", smallest first. ", Code ("", [], []) "sort_by(|a, b| b.cmp(a))", Str " takes a comparison closure, here reversing the order to get descending. ", Code ("", [], []) "sort_by_key(|w| w.len())", Str " sorts by a computed key and keeps equal keys in their original order (the sort is ", Emph [Str "stable"], Str "). ", Code ("", [], []) "reverse()", Str " flips the current order. To keep the original, sort a ", Code ("", [], []) "clone()", Str "."], Para [Str "Decimals (", Code ("", [], []) "f64", Str ") cannot use ", Code ("", [], []) "sort()", Str " because ", Code ("", [], []) "NaN", Str " has no order. Use ", Code ("", [], []) "sort_by(|a, b| a.partial_cmp(b).unwrap())", Str ", which is safe when the data contains no ", Code ("", [], []) "NaN", Str "."], Para [Str "The shared scores sort to 76, 82, 88, 91 in ascending order and 91, 88, 82, 76 in descending order."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "fn main() {
    let scores = vec![82, 91, 76, 88];

    let mut ascending = scores.clone();
    ascending.sort();
    let mut descending = scores.clone();
    descending.sort_by(|a, b| b.cmp(a));
    println!(\"Original: {:?}\", scores);
    println!(\"Ascending: {:?}\", ascending);
    println!(\"Descending: {:?}\", descending);

    let mut in_place = scores.clone();
    in_place.sort();
    in_place.reverse();
    println!(\"Sorted then reversed in place: {:?}\", in_place);

    let mut words = vec![\"pencil\", \"folder\", \"notebook\"];
    words.sort();
    println!(\"{:?}\", words);
    words.sort_by_key(|w| w.len());
    println!(\"{:?}\", words);

    let mut prices = vec![2.5, 0.5, 1.25];
    prices.sort_by(|a, b| a.partial_cmp(b).unwrap());
    println!(\"{:?}\", prices);
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Original: [82, 91, 76, 88]
Ascending: [76, 82, 88, 91]
Descending: [91, 88, 82, 76]
Sorted then reversed in place: [91, 88, 82, 76]
[\"folder\", \"notebook\", \"pencil\"]
[\"folder\", \"pencil\", \"notebook\"]
[0.5, 1.25, 2.5]
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Calling ", Code ("", [], []) "sort()", Str " on a vector of ", Code ("", [], []) "f64", Str ", which does not compile because decimals are only partially ordered."]], [Plain [Str "Forgetting ", Code ("", [], []) "mut", Str " on the vector, so ", Code ("", [], []) "sort", Str " is rejected."]], [Plain [Str "Expecting ", Code ("", [], []) "sort", Str " to return the sorted vector. It sorts in place and returns nothing."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict each printed line before running."]], [Plain [Str "Print the scores in descending order without changing the original."]], [Plain [Str "Sort the words by their last letter with ", Code ("", [], []) "sort_by_key", Str "."]], [Plain [Str "Explain why decimals need ", Code ("", [], []) "partial_cmp", Str "."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print each result on its own labelled line (", Code ("", [], []) "Ascending:", Str ", ", Code ("", [], []) "Descending:", Str "). The first and last numbers are the quickest to check by ear."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can sort ascending and descending."]], [Plain [Str "\9744", Space, Str "I can sort a clone."]], [Plain [Str "\9744", Space, Str "I can sort by a key."]], [Plain [Str "\9744", Space, Str "I can sort decimals."]], [Plain [Str "\9744", Space, Str "I can reverse a vector."]]], HorizontalRule, Header 3 ("lesson-43-tuples-and-immutable-values", ["unnumbered", "unlisted"], []) [Str "Lesson 4.3: Tuples and immutable values"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: The Tuple Type"] ("https://doc.rust-lang.org/book/ch03-02-data-types.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Using Tuple Structs"] ("https://doc.rust-lang.org/book/ch05-01-defining-structs.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 4.3: Tuples - Immutable Lists"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create tuples and unpack them by destructuring."]], [Plain [Str "Declare a tuple struct for a named fixed group."]], [Plain [Str "Return several values from a function."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "tuple"], Str " groups a fixed number of values that may have different types: ", Code ("", [], []) "(3, 4)", Str " or ", Code ("", [], []) "(\"Avery\", 16, 1.72)", Str ". Read a part with ", Code ("", [], []) "point.0", Str ", or ", Strong [Str "destructure"], Str " the whole tuple: ", Code ("", [], []) "let (x, y) = point;", Str ". A tuple is immutable unless its binding is ", Code ("", [], []) "mut", Str ", and its length and types cannot change."], Para [Str "A ", Emph [Str "tuple struct"], Str " gives a tuple a name: ", Code ("", [], []) "struct Point(i32, i32);", Str " so that two values of different meaning cannot be mixed up. For anything with more than two or three parts, a struct with named fields (Unit 7) reads better."], Para [Str "Functions return several values as a tuple: ", Code ("", [], []) "fn min_max(values: &[i32]) -> (i32, i32)", Str ". The shared coordinates are x = 3 and y = 4."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "struct Point(i32, i32);

fn min_max(values: &[i32]) -> (i32, i32) {
    let mut low = values[0];
    let mut high = values[0];
    for &value in values {
        if value < low {
            low = value;
        }
        if value > high {
            high = value;
        }
    }
    (low, high)
}

fn main() {
    let (x, y) = (3, 4);
    println!(\"x={x} y={y}\");

    let point = (3, 4);
    println!(\"{:?} {} {}\", point, point.0, point.1);

    let named = Point(3, 4);
    println!(\"{} {}\", named.0, named.1);

    let moved = (point.0, 10);
    println!(\"{:?} -> {:?}\", point, moved);
    println!(\"{}\", point == (3, 4));

    let (low, high) = min_max(&[82, 91, 76, 88]);
    println!(\"low={low} high={high}\");

    let profile = (\"Avery\", 16, 1.72);
    println!(\"{} {} {}\", profile.0, profile.1, profile.2);
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "x=3 y=4
(3, 4) 3 4
3 4
(3, 4) -> (3, 10)
true
low=76 high=91
Avery 16 1.72
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trying to assign ", Code ("", [], []) "point.0 = 5", Str " on a binding that is not ", Code ("", [], []) "mut", Str ", which is a compile error."]], [Plain [Str "Forgetting that ", Code ("", [], []) "min_max", Str " panics on an empty slice because it reads ", Code ("", [], []) "values[0]", Str "."]], [Plain [Str "Using a tuple where named fields would make the code readable."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output, then run."]], [Plain [Str "Create a tuple for the shared profile and destructure it into three bindings."]], [Plain [Str "Write a function that returns the lowest and highest scores as a tuple and test it with one score."]], [Plain [Str "Explain when a tuple is a better choice than a struct."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Printing a tuple with ", Code ("", [], []) "{:?}", Str " shows the parentheses and commas, so the screen reader announces ", Code ("", [], []) "(3, 4)", Str " as a complete phrase. Named fields read better aloud than ", Code ("", [], []) ".0", Str " and ", Code ("", [], []) ".1", Str "."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can create and destructure tuples."]], [Plain [Str "\9744", Space, Str "I can use a tuple struct."]], [Plain [Str "\9744", Space, Str "I can return several values."]], [Plain [Str "\9744", Space, Str "I know tuples cannot change length."]], [Plain [Str "\9744", Space, Str "I can choose between a tuple and a struct."]]], HorizontalRule, Header 3 ("lesson-44-hash-maps-and-key-value-data", ["unnumbered", "unlisted"], []) [Str "Lesson 4.4: Hash maps and key-value data"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Storing Keys with Associated Values in Hash Maps"] ("https://doc.rust-lang.org/book/ch08-03-hash-maps.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 4.4: Introducing Dictionaries"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create a ", Code ("", [], []) "HashMap", Str " and insert, read, and remove entries."]], [Plain [Str "Handle a missing key with ", Code ("", [], []) "Option", Str "."]], [Plain [Str "Model the shared inventory item with a struct."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Code ("", [], []) "HashMap<K, V>", Str " from ", Code ("", [], []) "std::collections", Str " pairs keys with values. ", Code ("", [], []) "insert(key, value)", Str " adds or replaces an entry, ", Code ("", [], []) "get(&key)", Str " returns an ", Code ("", [], []) "Option<&V>", Str " (", Code ("", [], []) "None", Str " when the key is missing, never a crash), ", Code ("", [], []) "remove(&key)", Str " deletes one, ", Code ("", [], []) "contains_key(&key)", Str " tests for a key, and ", Code ("", [], []) "len()", Str " counts the entries. ", Code ("", [], []) "entry(key).or_insert(0)", Str " gives a mutable reference to a value, inserting a starting value if the key is new: ", Code ("", [], []) "*counts.entry(\"pencil\").or_insert(0) += 1;", Str "."], Para [Str "Every value in a map has the ", Strong [Str "same type"], Str ". For a record whose fields have different types, use a struct, as with the shared Notebook item. A ", Code ("", [], []) "HashMap", Str " has no useful order, so the example prints only counts and single lookups."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::collections::HashMap;

struct Item {
    name: String,
    quantity: u32,
    unit_price: f64,
}

fn main() {
    let mut profile: HashMap<String, String> = HashMap::new();
    profile.insert(\"name\".to_string(), \"Avery\".to_string());
    profile.insert(\"age\".to_string(), \"16\".to_string());
    profile.insert(\"height_m\".to_string(), \"1.72\".to_string());
    profile.insert(\"favorite_subject\".to_string(), \"Computer Science\".to_string());

    println!(\"{:?}\", profile.get(\"name\"));
    profile.insert(\"age\".to_string(), \"17\".to_string());
    profile.insert(\"grade_level\".to_string(), \"11\".to_string());
    profile.remove(\"height_m\");
    println!(\"{}\", profile.len());
    println!(\"{:?}\", profile.get(\"height_m\"));
    println!(\"{}\", profile.get(\"height_m\").map(String::as_str).unwrap_or(\"unknown\"));
    println!(\"{}\", profile.contains_key(\"grade_level\"));

    let mut counts: HashMap<&str, u32> = HashMap::new();
    *counts.entry(\"pencil\").or_insert(0) += 1;
    *counts.entry(\"pencil\").or_insert(0) += 1;
    println!(\"{:?}\", counts.get(\"pencil\"));

    let mut item = Item { name: \"Notebook\".to_string(), quantity: 3, unit_price: 2.50 };
    item.quantity += 2;
    println!(\"{}: {} at {} = {}\", item.name, item.quantity, item.unit_price, item.quantity as f64 * item.unit_price);
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Some(\"Avery\")
4
None
unknown
true
Some(2)
Notebook: 5 at 2.5 = 12.5
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) "profile[\"height_m\"]", Str " on a missing key, which panics. Use ", Code ("", [], []) "get", Str "."]], [Plain [Str "Printing a whole ", Code ("", [], []) "HashMap", Str " and expecting the same order every run."]], [Plain [Str "Trying to store values of different types in one ", Code ("", [], []) "HashMap", Str "."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed lines before running."]], [Plain [Str "Add a ", Code ("", [], []) "discount", Str " field to ", Code ("", [], []) "Item", Str " and print the discounted value."]], [Plain [Str "Remove ", Code ("", [], []) "favorite_subject", Str " and show what ", Code ("", [], []) "get", Str " returns."]], [Plain [Str "Explain why a struct is safer than a map of text for a known set of fields."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print one lookup per line, because a one-line ", Code ("", [], []) "{key: value, ...}", Str " form is hard to navigate and has no stable order. Choose key names that read well aloud, such as ", Code ("", [], []) "favorite_subject", Str "."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can create and change a ", Code ("", [], []) "HashMap", Str "."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "get", Str " returns an ", Code ("", [], []) "Option", Str "."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "entry", Str " to count."]], [Plain [Str "\9744", Space, Str "I know map values share one type."]], [Plain [Str "\9744", Space, Str "I can model an item with a struct."]]], HorizontalRule, Header 3 ("lesson-45-collection-traversal-and-iterators", ["unnumbered", "unlisted"], []) [Str "Lesson 4.5: Collection traversal and iterators"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Iterators"] ("https://doc.rust-lang.org/book/ch13-02-iterators.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Hash Maps"] ("https://doc.rust-lang.org/book/ch08-03-hash-maps.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 4.5: Looping Through Dictionaries"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Visit pairs in a stable order."]], [Plain [Str "Explain why ", Code ("", [], []) "HashMap", Str " order is unspecified."]], [Plain [Str "Sort keys with ", Code ("", [], []) "BTreeMap", Str " and total the shared inventory."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Iterating a ", Code ("", [], []) "HashMap", Str " visits entries in an ", Strong [Str "unspecified order that can change between runs"], Str "; Rust randomizes it on purpose. For readable, testable output choose a collection with a defined order: a ", Code ("", [], []) "Vec", Str " of pairs keeps insertion order, and a ", Code ("", [], []) "BTreeMap", Str " keeps its keys sorted."], Para [Code ("", [], []) "for (name, stock) in &inventory", Str " visits a ", Code ("", [], []) "Vec", Str " of pairs and borrows it. Iterator methods can summarize: ", Code ("", [], []) ".iter().map(|(_, s)| ...).sum::<f64>()", Str " totals a computed value, and ", Code ("", [], []) ".collect()", Str " can build a ", Code ("", [], []) "BTreeMap", Str " from pairs."], Para [Str "The shared inventory is Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25), worth 7.50 + 5.00 + 5.00 = 17.50."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::collections::BTreeMap;

struct Stock {
    quantity: u32,
    unit_price: f64,
}

fn main() {
    let inventory = vec![
        (\"Notebook\", Stock { quantity: 3, unit_price: 2.50 }),
        (\"Pencil\", Stock { quantity: 10, unit_price: 0.50 }),
        (\"Folder\", Stock { quantity: 4, unit_price: 1.25 }),
    ];

    println!(\"Keys:\");
    for (name, _) in &inventory {
        println!(\"{name}\");
    }

    println!(\"Quantities:\");
    for (_, stock) in &inventory {
        println!(\"{}\", stock.quantity);
    }

    let mut total_value = 0.0;
    for (name, stock) in &inventory {
        let line_value = stock.quantity as f64 * stock.unit_price;
        println!(\"{name}: {} in stock, value {line_value:.2}\", stock.quantity);
        total_value += line_value;
    }
    println!(\"Total inventory value: {total_value:.2}\");

    let sorted: BTreeMap<&str, u32> = inventory.iter().map(|(name, stock)| (*name, stock.quantity)).collect();
    println!(\"{:?}\", sorted);
    println!(\"{}\", inventory.iter().map(|(_, s)| s.quantity as f64 * s.unit_price).sum::<f64>());
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Keys:
Notebook
Pencil
Folder
Quantities:
3
10
4
Notebook: 3 in stock, value 7.50
Pencil: 10 in stock, value 5.00
Folder: 4 in stock, value 5.00
Total inventory value: 17.50
{\"Folder\": 4, \"Notebook\": 3, \"Pencil\": 10}
17.5
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using a ", Code ("", [], []) "HashMap", Str " and expecting the same order every run."]], [Plain [Str "Looping over ", Code ("", [], []) "inventory", Str " instead of ", Code ("", [], []) "&inventory", Str ", which moves the vector so that it cannot be used again."]], [Plain [Str "Forgetting ", Code ("", [], []) "*name", Str " when building a map from borrowed pairs, which gives a type error."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the example and write the three key-value lines in order."]], [Plain [Str "Print only the items with a quantity below 5."]], [Plain [Str "Print the items from the highest line value to the lowest."]], [Plain [Str "Explain how ", Code ("", [], []) "BTreeMap", Str " differs from ", Code ("", [], []) "HashMap", Str "."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Printing each inventory line as one sentence lets the screen reader announce the name, quantity, and value together. Because the order is stable, you can learn it and compare runs by ear."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can visit pairs in a stable order."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "HashMap", Str " order is unspecified."]], [Plain [Str "\9744", Space, Str "I can sort keys with ", Code ("", [], []) "BTreeMap", Str "."]], [Plain [Str "\9744", Space, Str "I can total with an iterator."]], [Plain [Str "\9744", Space, Str "I can total the shared inventory."]]], HorizontalRule]