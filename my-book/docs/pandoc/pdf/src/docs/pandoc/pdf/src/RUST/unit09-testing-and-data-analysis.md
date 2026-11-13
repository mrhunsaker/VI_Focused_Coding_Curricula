[Header 2 ("unit-9-testing-and-data-analysis", [], []) [Str "Unit 9: Testing and Data Analysis"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops testing and data analysis through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly."], Header 3 ("lesson-91-unit-tests", ["unnumbered", "unlisted"], []) [Str "Lesson 9.1: Unit tests"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: How to Write Tests"] ("https://doc.rust-lang.org/book/ch11-01-writing-tests.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Test Organization"] ("https://doc.rust-lang.org/book/ch11-03-test-organization.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 9.1: Testing Your Code"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write checks with chosen inputs and expected results."]], [Plain [Str "Write a ", Code ("", [], []) "#[cfg(test)]", Str " module with ", Code ("", [], []) "#[test]", Str " functions."]], [Plain [Str "Compare decimals with a tolerance and test boundary values."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Rust has testing built in. A function marked ", Code ("", [], []) "#[test]", Str " inside a module marked ", Code ("", [], []) "#[cfg(test)]", Str " is compiled and run only by the test harness (", Code ("", [], []) "cargo test", Str ", or ", Code ("", [], []) "rustc --test", Str "), and ", Code ("", [], []) "assert_eq!(actual, expected)", Str " stops that test with a clear message when the values differ. A normal build ignores the module, so tests cost nothing at run time."], Para [Str "The example shows both styles: a small hand-written ", Code ("", [], []) "Tally", Str " that prints PASS and FAIL lines when the program runs, and the idiomatic ", Code ("", [], []) "#[test]", Str " module, which is verified separately in the Expected section. Decimal results are compared with a ", Emph [Str "tolerance"], Str ", not ", Code ("", [], []) "==", Str ", because the tip for 24.50 at 0.15 is stored as 3.6749999999999998."], Para [Str "The same tests appear in every language track: ", Code ("", [], []) "add(5, 3)", Str " is 8, ", Code ("", [], []) "add(-5, -3)", Str " is -8, ", Code ("", [], []) "add(10, -4)", Str " is 6, the tip is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F. ", Code ("", [], []) "std::process::exit(1)", Str " ends the program with a failure status."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn calculate_tip(bill: f64, rate: f64) -> f64 {
    bill * rate
}

fn classify(score: i32) -> &'static str {
    if score >= 90 {
        \"A\"
    } else if score >= 80 {
        \"B\"
    } else if score >= 70 {
        \"C\"
    } else if score >= 60 {
        \"D\"
    } else {
        \"F\"
    }
}

struct Tally {
    passed: u32,
    failed: u32,
}

impl Tally {
    fn check<T: PartialEq + std::fmt::Debug>(&mut self, name: &str, actual: T, expected: T) {
        if actual == expected {
            self.passed += 1;
            println!(\"PASS {name}\");
        } else {
            self.failed += 1;
            println!(\"FAIL {name}: expected {:?} but got {:?}\", expected, actual);
        }
    }

    fn check_close(&mut self, name: &str, actual: f64, expected: f64, tolerance: f64) {
        self.check(name, (actual - expected).abs() <= tolerance, true);
    }
}

fn main() {
    let mut tally = Tally { passed: 0, failed: 0 };
    tally.check(\"add 5 and 3\", add(5, 3), 8);
    tally.check(\"add -5 and -3\", add(-5, -3), -8);
    tally.check(\"add 10 and -4\", add(10, -4), 6);
    tally.check_close(\"tip on 24.50 at 0.15\", calculate_tip(24.5, 0.15), 3.675, 1e-9);
    tally.check(\"tip on a zero bill\", calculate_tip(0.0, 0.15), 0.0);
    tally.check(\"classify 90\", classify(90), \"A\");
    tally.check(\"classify 89\", classify(89), \"B\");
    tally.check(\"classify 60\", classify(60), \"D\");
    tally.check(\"classify 59\", classify(59), \"F\");

    println!(\"{} passed, {} failed\", tally.passed, tally.failed);
    if tally.failed > 0 {
        std::process::exit(1);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn adds_numbers() {
        assert_eq!(add(5, 3), 8);
        assert_eq!(add(-5, -3), -8);
        assert_eq!(add(10, -4), 6);
    }

    #[test]
    fn tip_is_close_to_expected() {
        assert!((calculate_tip(24.5, 0.15) - 3.675).abs() < 1e-9);
    }

    #[test]
    fn grade_boundaries() {
        assert_eq!(classify(90), \"A\");
        assert_eq!(classify(89), \"B\");
        assert_eq!(classify(60), \"D\");
        assert_eq!(classify(59), \"F\");
    }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "PASS add 5 and 3
PASS add -5 and -3
PASS add 10 and -4
PASS tip on 24.50 at 0.15
PASS tip on a zero bill
PASS classify 90
PASS classify 89
PASS classify 60
PASS classify 59
9 passed, 0 failed
", Para [Str "The ", Code ("", [], []) "#[cfg(test)]", Str " module is not compiled in a normal build. Running it with the test harness (", Code ("", [], []) "rustc --test main.rs -o tests", Str " then ", Code ("", [], []) "./tests --test-threads=1", Str ", or ", Code ("", [], []) "cargo test", Str ") prints:"], CodeBlock ("", ["text"], []) "running 3 tests
test tests::adds_numbers ... ok
test tests::grade_boundaries ... ok
test tests::tip_is_close_to_expected ... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Comparing decimal results with ", Code ("", [], []) "assert_eq!", Str " and ", Code ("", [], []) "==", Str "."]], [Plain [Str "Testing only typical values and skipping the boundaries 90, 89, 60, and 59."]], [Plain [Str "Putting ", Code ("", [], []) "#[test]", Str " functions outside a ", Code ("", [], []) "#[cfg(test)]", Str " module, which compiles them into the normal build."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Change one expected value so a check fails, read the message, and restore it."]], [Plain [Str "Add checks for the grades at 80, 79, 70, and 69."]], [Plain [Str "Write the tests for ", Code ("", [], []) "is_passing(score)", Str " before writing the function."]], [Plain [Str "Explain why the tip test uses a tolerance."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each check prints one complete line that starts with PASS or FAIL, and the last line gives the counts, so the result can be understood from the first word of each line and the final summary. The test harness prints one line per test and a final result line in the same style."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a check with an expected value."]], [Plain [Str "\9744", Space, Str "I can write a ", Code ("", [], []) "#[test]", Str " module."]], [Plain [Str "\9744", Space, Str "I can compare decimals with a tolerance."]], [Plain [Str "\9744", Space, Str "I can choose boundary tests."]], [Plain [Str "\9744", Space, Str "I know how to signal failure with an exit status."]]], HorizontalRule, Header 3 ("lesson-92-testing-stateful-types", ["unnumbered", "unlisted"], []) [Str "Lesson 9.2: Testing stateful types"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: How to Write Tests"] ("https://doc.rust-lang.org/book/ch11-01-writing-tests.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Checking for Panics with should_panic"] ("https://doc.rust-lang.org/book/ch11-01-writing-tests.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 9.2: Testing a Class"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create a fresh value for every test."]], [Plain [Str "Test a return value, a change of state, and an error result."]], [Plain [Str "Write the same tests in a ", Code ("", [], []) "#[cfg(test)]", Str " module."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Each test should start from a known state, so build a new value for every test with a ", Emph [Str "setup"], Str " function. Tests that share a value can affect each other and fail in confusing ways."], Para [Str "Test three kinds of behavior: that a method returns the right value (", Code ("", [], []) "total_value", Str " for 3 at 2.50 is 7.5), that a method changes the value correctly (restocking 2 makes the quantity 5), and that invalid use is reported (restocking a negative amount returns an ", Code ("", [], []) "Err", Str "). Because Rust reports expected failures with ", Code ("", [], []) "Result", Str ", a test can simply check ", Code ("", [], []) "is_err()", Str ". A function that is expected to panic can be tested with ", Code ("", [], []) "#[should_panic]", Str "."], Para [Str "The example runs each test as a function returning ", Code ("", [], []) "Result<(), String>", Str ", so a failed check carries a message, and the same tests also appear in a ", Code ("", [], []) "#[cfg(test)]", Str " module."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "struct Item {
    name: String,
    quantity: i32,
    unit_price: f64,
}

impl Item {
    fn total_value(&self) -> f64 {
        self.quantity as f64 * self.unit_price
    }

    fn restock(&mut self, amount: i32) -> Result<(), String> {
        if amount < 0 {
            return Err(\"amount must not be negative\".to_string());
        }
        self.quantity += amount;
        Ok(())
    }
}

fn setup() -> Item {
    Item { name: \"Notebook\".to_string(), quantity: 3, unit_price: 2.50 }
}

fn expect(condition: bool, message: &str) -> Result<(), String> {
    if condition {
        Ok(())
    } else {
        Err(message.to_string())
    }
}

fn total_value_is_7_5() -> Result<(), String> {
    expect((setup().total_value() - 7.5).abs() < 1e-9, \"wrong total\")
}

fn restock_adds_to_the_quantity() -> Result<(), String> {
    let mut item = setup();
    item.restock(2)?;
    expect(item.quantity == 5, \"quantity should be 5\")
}

fn restock_rejects_a_negative_amount() -> Result<(), String> {
    let mut item = setup();
    expect(item.restock(-1).is_err(), \"an error should have been returned\")?;
    expect(item.quantity == 3, \"the quantity should be unchanged\")?;
    expect(!item.name.is_empty(), \"the name should be kept\")
}

fn main() {
    let tests: [(&str, fn() -> Result<(), String>); 3] = [
        (\"total value is 7.5\", total_value_is_7_5),
        (\"restock adds to the quantity\", restock_adds_to_the_quantity),
        (\"restock rejects a negative amount\", restock_rejects_a_negative_amount),
    ];

    let mut failures = 0;
    for (name, test) in tests {
        match test() {
            Ok(()) => println!(\"PASS {name}\"),
            Err(message) => {
                failures += 1;
                println!(\"FAIL {name}: {message}\");
            }
        }
    }
    println!(\"{}\", if failures == 0 { \"All tests passed.\".to_string() } else { format!(\"{failures} test(s) failed.\") });
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn total_value() {
        assert!(total_value_is_7_5().is_ok());
    }

    #[test]
    fn restock_adds() {
        assert_eq!(restock_adds_to_the_quantity(), Ok(()));
    }

    #[test]
    fn restock_rejects_negative() {
        assert_eq!(restock_rejects_a_negative_amount(), Ok(()));
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "PASS total value is 7.5
PASS restock adds to the quantity
PASS restock rejects a negative amount
All tests passed.
", Para [Str "The ", Code ("", [], []) "#[cfg(test)]", Str " module is not compiled in a normal build. Running it with the test harness (", Code ("", [], []) "rustc --test main.rs -o tests", Str " then ", Code ("", [], []) "./tests --test-threads=1", Str ", or ", Code ("", [], []) "cargo test", Str ") prints:"], CodeBlock ("", ["text"], []) "running 3 tests
test tests::restock_adds ... ok
test tests::restock_rejects_negative ... ok
test tests::total_value ... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Sharing one value between tests, so an earlier test changes the later ones."]], [Plain [Str "Testing only the successful path and never the error path."]], [Plain [Str "Using ", Code ("", [], []) "unwrap()", Str " inside a test helper so that a failure panics with no message about which check failed."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Add a test that ", Code ("", [], []) "restock(0)", Str " leaves the quantity unchanged."]], [Plain [Str "Add a test for an ", Code ("", [], []) "is_valid", Str " method."]], [Plain [Str "Break ", Code ("", [], []) "restock", Str " on purpose and read the failure line."]], [Plain [Str "Explain why ", Code ("", [], []) "setup", Str " creates a new item each time."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Name each test as a short sentence that says what it checks, so the PASS and FAIL lines read as clear statements. Read the final summary line first."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can create a fresh value per test."]], [Plain [Str "\9744", Space, Str "I can test a return value."]], [Plain [Str "\9744", Space, Str "I can test a change of state."]], [Plain [Str "\9744", Space, Str "I can test an error result."]], [Plain [Str "\9744", Space, Str "I can write a clear test name."]]], HorizontalRule, Header 3 ("lesson-93-random-values", ["unnumbered", "unlisted"], []) [Str "Lesson 9.3: Random values"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The rand crate"] ("https://docs.rs/rand/", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Method Syntax"] ("https://doc.rust-lang.org/book/ch05-03-method-syntax.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 9.3: Random Numbers and Simulation"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain why the standard library has no random numbers."]], [Plain [Str "Use a small seeded generator and test it by its properties."]], [Plain [Str "Pick a random list item."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The Rust standard library has ", Strong [Str "no random-number generator"], Str ". Real programs add the ", Code ("", [], []) "rand", Str " crate through Cargo. To keep this course free of dependencies, the example uses a tiny ", Emph [Str "xorshift"], Str " generator written in a few lines. It is predictable and ", Strong [Str "not secure"], Str ", so it must never be used for passwords or tokens, but it is enough to learn the ideas."], Para [Str "A generator started from the same ", Emph [Str "seed"], Str " produces the same sequence, so a test can check ", Emph [Str "repeatability"], Str ". A seed must not be zero for this algorithm. Because the exact numbers depend on the algorithm, tests should check ", Emph [Str "properties"], Str " (every roll is between 1 and 6, a decimal is in 0 up to but not including 1) and not particular values."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "struct Rng {
    state: u64,
}

impl Rng {
    fn new(seed: u64) -> Rng {
        Rng { state: if seed == 0 { 1 } else { seed } }
    }

    fn next_u64(&mut self) -> u64 {
        let mut x = self.state;
        x ^= x << 13;
        x ^= x >> 7;
        x ^= x << 17;
        self.state = x;
        x
    }

    fn range(&mut self, low: u64, high: u64) -> u64 {
        low + self.next_u64() % (high - low)
    }

    fn next_f64(&mut self) -> f64 {
        (self.next_u64() >> 11) as f64 / (1u64 << 53) as f64
    }
}

fn main() {
    let mut first = Rng::new(42);
    let mut second = Rng::new(42);
    let first_rolls: Vec<u64> = (0..5).map(|_| first.range(1, 7)).collect();
    let second_rolls: Vec<u64> = (0..5).map(|_| second.range(1, 7)).collect();
    println!(\"Same seed gives the same rolls: {}\", first_rolls == second_rolls);

    let mut random = Rng::new(7);
    let in_range = (0..1000).all(|_| (1..=6).contains(&random.range(1, 7)));
    println!(\"All rolls between 1 and 6: {in_range}\");

    let decimal = random.next_f64();
    println!(\"Decimal in [0, 1): {}\", (0.0..1.0).contains(&decimal));

    let scores = [82, 91, 76, 88];
    let chosen = scores[random.range(0, scores.len() as u64) as usize];
    println!(\"Chosen score is from the list: {}\", scores.contains(&chosen));
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Same seed gives the same rolls: true
All rolls between 1 and 6: true
Decimal in [0, 1): true
Chosen score is from the list: true
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Looking for ", Code ("", [], []) "std::random", Str ". It does not exist; use the ", Code ("", [], []) "rand", Str " crate in real programs."]], [Plain [Str "Using a simple generator for passwords or tokens, which it is not designed for."]], [Plain [Str "Seeding with zero, which makes this algorithm produce only zeros."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program three times and compare."]], [Plain [Str "Change the seeds and check that the property lines still print ", Code ("", [], []) "true", Str "."]], [Plain [Str "Simulate 600 rolls and count how many of each face appeared (the counts depend on the seed)."]], [Plain [Str "Explain why a test should check a property rather than a specific random number."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print yes or no style results for random behavior, so the announced output is the same on every run and the screen reader does not read unpredictable values."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I know the standard library has no random numbers."]], [Plain [Str "\9744", Space, Str "I can use a seeded generator."]], [Plain [Str "\9744", Space, Str "I can test properties of random code."]], [Plain [Str "\9744", Space, Str "I know this generator is not secure."]], [Plain [Str "\9744", Space, Str "I can pick a random list item."]]], HorizontalRule, Header 3 ("lesson-94-text-analysis", ["unnumbered", "unlisted"], []) [Str "Lesson 9.4: Text analysis"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Hash Maps"] ("https://doc.rust-lang.org/book/ch08-03-hash-maps.html", "")]], [Plain [Link ("", [], []) [Str "The Rust Programming Language: Strings"] ("https://doc.rust-lang.org/book/ch08-02-strings.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 9.4: Data Analysis - Text Analysis"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Split text into words and count them."]], [Plain [Str "Count word and letter frequencies in a stable order."]], [Plain [Str "Sort with a tie-break."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "text.split_whitespace()", Str " iterates over the words of a string. Counting uses a map; because a ", Code ("", [], []) "HashMap", Str " has no stable order, the example keeps first-seen order in a ", Code ("", [], []) "Vec<(String, u32)>", Str " for words and uses a ", Code ("", [], []) "BTreeMap", Str " for letters, then sorts the letter pairs with ", Code ("", [], []) "sort_by", Str ": count descending first, then letter ascending, so ties print in a fixed order."], Para [Code ("", [], []) "to_lowercase()", Str " and ", Code ("", [], []) "replace(\".\", \"\")", Str " normalize the text first. The shared text sample is \"A student studies programming. Programming develops problem-solving skills.\" After lower-casing and removing the periods it has 8 words, and ", Code ("", [], []) "programming", Str " appears twice."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::collections::BTreeMap;

fn main() {
    let text = \"A student studies programming. Programming develops problem-solving skills.\";
    let cleaned = text.to_lowercase().replace('.', \"\");
    let words: Vec<&str> = cleaned.split_whitespace().collect();

    let mut frequencies: Vec<(String, u32)> = Vec::new();
    for word in &words {
        match frequencies.iter_mut().find(|(known, _)| known == word) {
            Some((_, count)) => *count += 1,
            None => frequencies.push((word.to_string(), 1)),
        }
    }

    println!(\"Word count: {}\", words.len());
    println!(\"Word frequencies:\");
    for (word, count) in &frequencies {
        println!(\"'{word}': {count}\");
    }

    let mut letters: BTreeMap<char, u32> = BTreeMap::new();
    for c in text.to_lowercase().chars().filter(|c| c.is_alphabetic()) {
        *letters.entry(c).or_insert(0) += 1;
    }
    let mut pairs: Vec<(char, u32)> = letters.into_iter().collect();
    pairs.sort_by(|a, b| b.1.cmp(&a.1).then(a.0.cmp(&b.0)));
    println!(\"Most common letters:\");
    for (letter, count) in pairs.iter().take(3) {
        println!(\"{letter}: {count}\");
    }
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Word count: 8
Word frequencies:
'a': 1
'student': 1
'studies': 1
'programming': 2
'develops': 1
'problem-solving': 1
'skills': 1
Most common letters:
s: 7
e: 5
g: 5
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Counting punctuation as part of a word, so ", Code ("", [], []) "programming.", Str " and ", Code ("", [], []) "programming", Str " are different words."]], [Plain [Str "Forgetting to lower-case first, so ", Code ("", [], []) "Programming", Str " and ", Code ("", [], []) "programming", Str " are counted separately."]], [Plain [Str "Printing a ", Code ("", [], []) "HashMap", Str " and expecting a stable order."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the word count and the count for ", Code ("", [], []) "programming", Str " before running."]], [Plain [Str "Count the words longer than 8 letters."]], [Plain [Str "Print the longest word."]], [Plain [Str "Change the sort so ties are listed in reverse alphabetical order."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the frequency list in its fixed order. Because the order is stable, you can learn it and compare runs by ear. Print each pair as a short sentence with the same wording every time."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can split text into words."]], [Plain [Str "\9744", Space, Str "I can count frequencies in a stable order."]], [Plain [Str "\9744", Space, Str "I can sort with a tie-break."]], [Plain [Str "\9744", Space, Str "I can remove punctuation first."]], [Plain [Str "\9744", Space, Str "I can read a stable report."]]], HorizontalRule, Header 3 ("lesson-95-csv-records", ["unnumbered", "unlisted"], []) [Str "Lesson 9.5: CSV records"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Reading a File"] ("https://doc.rust-lang.org/book/ch12-02-reading-a-file.html", "")]], [Plain [Link ("", [], []) [Str "The csv crate"] ("https://docs.rs/csv/", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 9.5: Data Analysis - CSV Files"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create and read a CSV file."]], [Plain [Str "Split lines into fields and convert numbers."]], [Plain [Str "Compute an average and a count."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A CSV (comma-separated values) file stores a table as text. The first line names the columns and each later line is a record. The shared student file has the columns ", Code ("", [], []) "student_id", Str ", ", Code ("", [], []) "first_name", Str ", ", Code ("", [], []) "last_name", Str ", ", Code ("", [], []) "score", Str ", and ", Code ("", [], []) "active", Str ", and three records."], Para [Str "The standard library has no CSV reader. ", Code ("", [], []) "line.split(',')", Str " works only for ", Strong [Str "simple"], Str " files: a value that contains a comma inside quotation marks, such as ", Code ("", [], []) "\"Smith, Jr.\"", Str ", would be split wrongly. For such files use the ", Code ("", [], []) "csv", Str " crate or write a real parser."], Para [Str "Every field is text. Convert the score with ", Code ("", [], []) "parse::<i32>()", Str " and compare ", Code ("", [], []) "active", Str " with the text ", Code ("", [], []) "\"true\"", Str ". With scores 91, 82, and 76 the average is 83.00, and two students are active."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::fs;
use std::io;

fn main() -> io::Result<()> {
    let content = [
        \"student_id,first_name,last_name,score,active\",
        \"1,Avery,Student,91,true\",
        \"2,Jordan,Lee,82,true\",
        \"3,Casey,Smith,76,false\",
    ]
    .join(\"\\n\")
        + \"\\n\";
    fs::write(\"students.csv\", content)?;

    let text = match fs::read_to_string(\"students.csv\") {
        Ok(text) => text,
        Err(_) => {
            println!(\"Error: students.csv was not found.\");
            return Ok(());
        }
    };
    let mut lines = text.lines();
    let header = lines.next().unwrap_or(\"\");
    println!(\"Columns: {}\", header.split(',').collect::<Vec<_>>().join(\", \"));

    let mut total = 0;
    let mut active = 0;
    let mut count = 0;
    for line in lines {
        let row: Vec<&str> = line.split(',').collect();
        let score: i32 = row[3].parse().unwrap_or(0);
        total += score;
        count += 1;
        if row[4] == \"true\" {
            active += 1;
        }
        println!(\"{}: {} {} scored {}\", row[0], row[1], row[2], score);
    }

    println!(\"Students: {count}\");
    println!(\"Average score: {:.2}\", total as f64 / count as f64);
    println!(\"Active students: {active}\");
    Ok(())
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Columns: student_id, first_name, last_name, score, active
1: Avery Student scored 91
2: Jordan Lee scored 82
3: Casey Smith scored 76
Students: 3
Average score: 83.00
Active students: 2
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Splitting a CSV line at every comma when a value contains a quoted comma."]], [Plain [Str "Forgetting to convert the text in the score column to a number."]], [Plain [Str "Not skipping the header line, so ", Code ("", [], []) "parse", Str " fails on the text ", Code ("", [], []) "score", Str "."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed lines before running."]], [Plain [Str "Add a fourth student and check the new average."]], [Plain [Str "Print only the active students."]], [Plain [Str "Explain, with an example, why ", Code ("", [], []) "\"Smith, Jr.\"", Str " breaks ", Code ("", [], []) "split(',')", Str "."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print one student per line with the same wording each time, so the screen reader announces a repeating pattern that is easy to compare. Read the column names aloud once at the start."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write and read a CSV file."]], [Plain [Str "\9744", Space, Str "I can split a line into fields."]], [Plain [Str "\9744", Space, Str "I convert text fields to numbers."]], [Plain [Str "\9744", Space, Str "I can compute an average and a count."]], [Plain [Str "\9744", Space, Str "I know when ", Code ("", [], []) "split", Str " is not enough."]]], HorizontalRule]