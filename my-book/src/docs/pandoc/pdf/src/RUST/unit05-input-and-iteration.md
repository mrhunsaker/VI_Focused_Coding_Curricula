[Header 2 ("unit-5-input-and-iteration", [], []) [Str "Unit 5: Input and Iteration"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops input and iteration through Rust's type system and standard library. Prerequisites: prior units, a working Cargo project, and the ability to read compiler diagnostics. Preserve shared course datasets and test boundary conditions explicitly."], Header 3 ("lesson-51-input-and-validation", ["unnumbered", "unlisted"], []) [Str "Lesson 5.1: Input and validation"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Programming a Guessing Game"] ("https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 5.1: How the input() Function Works"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Read a line and recognize it as text."]], [Plain [Str "Convert it safely and handle failure."]], [Plain [Str "Handle the end of input."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "read_line", Str " appends the next line to a ", Code ("", [], []) "String", Str " and returns a ", Code ("", [], []) "Result", Str "; ", Code ("", [], []) "Ok(0)", Str " means the input has ended. The text keeps its line ending, so ", Code ("", [], []) "trim()", Str " it. Typed digits are text until you convert them: ", Code ("", [], []) "text.parse::<i32>()", Str " returns ", Code ("", [], []) "Ok(number)", Str " or ", Code ("", [], []) "Err(error)", Str "."], Para [Code ("", [], []) ".ok()", Str " turns a ", Code ("", [], []) "Result", Str " into an ", Code ("", [], []) "Option", Str " and ", Code ("", [], []) "and_then", Str " chains steps that may each fail: ", Code ("", [], []) "text.as_deref().and_then(|t| t.parse::<i32>().ok())", Str " means \"if there is text, and it parses, give the number\". A program that reads input must plan for three cases: a valid value, an invalid value, and no value at all. With the typed value 16 the age five years later is 21; the second value, ", Code ("", [], []) "abc", Str ", is rejected."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    println!(\"How old are you?\");
    let text = next_line();
    match &text {
        Some(t) => println!(\"Read: {} characters of text\", t.len()),
        None => println!(\"Read: nothing\"),
    }

    let age = text.as_deref().and_then(|t| t.parse::<i32>().ok());
    match age {
        Some(age) => println!(\"In 5 years: {}\", age + 5),
        None => println!(\"That was not a whole number.\"),
    }

    println!(\"Enter another value:\");
    let second = next_line().and_then(|t| t.parse::<i32>().ok());
    match second {
        Some(number) => println!(\"Number: {number}\"),
        None => println!(\"Not a number; the parse returned None.\"),
    }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "16
abc
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "How old are you?
Read: 2 characters of text
In 5 years: 21
Enter another value:
Not a number; the parse returned None.
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "How old are you?
Read: nothing
That was not a whole number.
Enter another value:
Not a number; the parse returned None.
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Adding to the text without converting it, which does not compile."]], [Plain [Str "Forgetting ", Code ("", [], []) "trim()", Str ", so the line ending makes ", Code ("", [], []) "parse", Str " fail."]], [Plain [Str "Using ", Code ("", [], []) "unwrap()", Str " on user input and crashing on ", Code ("", [], []) "abc", Str "."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run with 16 and then ", Code ("", [], []) "abc", Str " and compare with the shown output."]], [Plain [Str "Run with no input and explain every line printed."]], [Plain [Str "Accept an age only from 0 to 120."]], [Plain [Str "Rewrite the second input with a ", Code ("", [], []) "match", Str " on the ", Code ("", [], []) "Result", Str " and print the parse error."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each prompt is a complete sentence on its own line. Run the program twice, once typing and once with piped input, and compare what your screen reader announces."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can read a line of input."]], [Plain [Str "\9744", Space, Str "I can convert and validate it."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]], [Plain [Str "\9744", Space, Str "I know typed input is text."]], [Plain [Str "\9744", Space, Str "I can chain ", Code ("", [], []) "Option", Str " steps."]]], HorizontalRule, Header 3 ("lesson-52-while-loops-and-sentinel-repetition", ["unnumbered", "unlisted"], []) [Str "Lesson 5.2: While loops and sentinel repetition"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Repetition with Loops"] ("https://doc.rust-lang.org/book/ch03-05-control-flow.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 5.2: The while Loop in Action"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write a counting ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "Write a sentinel loop that ends on a command."]], [Plain [Str "Stop at the end of input."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "while condition { ... }", Str " repeats while the condition is true, testing ", Strong [Str "before"], Str " each pass. A loop needs a way to make its condition false, normally by changing a variable inside the body: ", Code ("", [], []) "count += 1", Str " adds one. ", Code ("", [], []) "while let Some(x) = value { ... }", Str " repeats while a pattern matches."], Para [Str "A ", Emph [Str "sentinel"], Str " is a special input that tells the loop to stop, here the word ", Code ("", [], []) "quit", Str ". The standard pattern reads once before the loop and again at the end of each pass, and ends when there is no more input (", Code ("", [], []) "None", Str ") as well as on ", Code ("", [], []) "quit", Str ", so the loop stops when input runs out even without ", Code ("", [], []) "quit", Str "."], Para [Str "The example counts from 1 to 5, then repeats a message prompt until the user types ", Code ("", [], []) "quit", Str "."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    let mut count = 1;
    while count <= 5 {
        println!(\"{count}\");
        count += 1;
    }
    println!(\"Counting finished!\");

    println!(\"Enter a message, or type quit to exit:\");
    let mut message = next_line();
    while let Some(text) = &message {
        if text == \"quit\" {
            break;
        }
        println!(\"You said: {text}\");
        println!(\"Enter a message, or type quit to exit:\");
        message = next_line();
    }
    println!(\"Goodbye!\");
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "hello
scores
quit
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit:
You said: hello
Enter a message, or type quit to exit:
You said: scores
Enter a message, or type quit to exit:
Goodbye!
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit:
Goodbye!
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to change the loop variable, which creates an endless loop."]], [Plain [Str "Testing for ", Code ("", [], []) "quit", Str " but not for ", Code ("", [], []) "None", Str ", so the loop reads forever after input ends."]], [Plain [Str "Comparing a ", Code ("", [], []) "String", Str " with ", Code ("", [], []) "\"quit\"", Str " after forgetting that the text still contains its line ending."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output for the typed lines hello, scores, and quit."]], [Plain [Str "Change the sentinel to ", Code ("", [], []) "exit", Str " and update the prompt."]], [Plain [Str "Count the messages entered and print the count at the end."]], [Plain [Str "Rewrite the counting loop as ", Code ("", [], []) "for count in 1..=5", Str " and compare."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each prompt is on its own line and each response begins with ", Code ("", [], []) "You said:", Str ", so the conversation can be followed in order by ear. If a loop floods the screen reader, stop it with Ctrl+C."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a counting ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "\9744", Space, Str "I can write a sentinel loop."]], [Plain [Str "\9744", Space, Str "I test for ", Code ("", [], []) "None", Str " as well as the sentinel."]], [Plain [Str "\9744", Space, Str "I update the loop variable."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "while let", Str "."]]], HorizontalRule, Header 3 ("lesson-53-flags-and-loop-exits", ["unnumbered", "unlisted"], []) [Str "Lesson 5.3: Flags and loop exits"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Loop Labels to Disambiguate Between Multiple Loops"] ("https://doc.rust-lang.org/book/ch03-05-control-flow.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 5.3: Using Flags and break to Exit Loops"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Control a loop with a Boolean flag."]], [Plain [Str "Leave a loop with ", Code ("", [], []) "break", Str " and an outer loop with a label."]], [Plain [Str "Search a collection and remember the position."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "flag"], Str " is a ", Code ("", [], []) "bool", Str " variable that controls a loop: the loop runs while ", Code ("", [], []) "running", Str " is true, and the body sets it to ", Code ("", [], []) "false", Str " to stop. ", Code ("", [], []) "break", Str " leaves the nearest enclosing loop at once."], Para [Str "A search keeps its answer in an ", Code ("", [], []) "Option<usize>", Str " (", Code ("", [], []) "None", Str " means \"not found\"), sets it when the item is found, and uses ", Code ("", [], []) "break", Str ". After the loop, the ", Code ("", [], []) "Option", Str " says whether a match was found. Positions start at 0. The iterator method ", Code ("", [], []) "position", Str " does the same search in one line."], Para [Str "A ", Emph [Str "label"], Str " lets ", Code ("", [], []) "break", Str " leave an outer loop from inside an inner one: write ", Code ("", [], []) "'outer:", Str " before the outer loop and ", Code ("", [], []) "break 'outer;", Str " inside."], Para [Str "The shared scores 82, 91, 76, 88 have their first score of 90 or higher at index 1, with the value 91."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    let mut running = true;
    let mut handled = 0;
    while running {
        println!(\"Say something, or type quit to stop:\");
        match next_line() {
            Some(message) if message != \"quit\" => {
                handled += 1;
                println!(\"You said: {message}\");
            }
            _ => running = false,
        }
    }
    println!(\"Messages handled: {handled}\");

    let scores = [82, 91, 76, 88];
    let mut found_index = None;
    for (index, &score) in scores.iter().enumerate() {
        if score >= 90 {
            found_index = Some(index);
            break;
        }
    }
    match found_index {
        Some(index) => println!(\"First score of 90 or higher: {} at index {}\", scores[index], index),
        None => println!(\"No score of 90 or higher.\"),
    }
    println!(\"{:?}\", scores.iter().position(|&s| s >= 90));

    'outer: for row in 1..=3 {
        for col in 1..=3 {
            if row * col == 4 {
                println!(\"Stopped at row {row}, column {col}\");
                break 'outer;
            }
        }
    }
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "hello
quit
ignored
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "Say something, or type quit to stop:
You said: hello
Say something, or type quit to stop:
Messages handled: 1
First score of 90 or higher: 91 at index 1
Some(1)
Stopped at row 2, column 2
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "Say something, or type quit to stop:
Messages handled: 0
First score of 90 or higher: 91 at index 1
Some(1)
Stopped at row 2, column 2
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Setting the flag but running more code in the same pass that should be skipped."]], [Plain [Str "Forgetting to give the result variable a starting value (", Code ("", [], []) "None", Str "), then misreading it after the loop."]], [Plain [Str "Using ", Code ("", [], []) "break", Str " in an inner loop and expecting it to leave the outer loop."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run with hello and quit and confirm the count is 1."]], [Plain [Str "Change the search to the first score below 80 and predict the index."]], [Plain [Str "Rewrite the first loop without a flag, using ", Code ("", [], []) "break", Str "."]], [Plain [Str "Explain in two sentences when a flag is clearer than ", Code ("", [], []) "break", Str "."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Report search results as complete sentences that include both the value and its position. Remember that Rust indexes start at 0, and say 'index 1' aloud to avoid confusing it with 'the first'."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can control a loop with a flag."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "break", Str "."]], [Plain [Str "\9744", Space, Str "I can use a label to leave an outer loop."]], [Plain [Str "\9744", Space, Str "I can search with an ", Code ("", [], []) "Option", Str "."]], [Plain [Str "\9744", Space, Str "I can explain flag versus ", Code ("", [], []) "break", Str "."]]], HorizontalRule, Header 3 ("lesson-54-continue-and-filtering", ["unnumbered", "unlisted"], []) [Str "Lesson 5.4: Continue and filtering"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language"] ("https://doc.rust-lang.org/book/", "")]], [Plain [Link ("", [], []) [Str "Rust standard library"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Link ("", [], []) [Str "Cargo Book"] ("https://doc.rust-lang.org/cargo/", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain Continue and filtering using Rust's types, ownership model, and standard-library conventions."]], [Plain [Str "Select an idiomatic Rust construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the example's behavior."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Read input into String, trim it, then parse. loop, while, and iterator loops express different repetition patterns. Every loop needs a clear termination condition; break and continue should make control flow easier to reason about. This lesson retains the canonical course data so learners practice Rust rather than a new domain problem. Use cargo fmt, cargo check, and cargo test as routine development tools."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "fn main() { let values=[-2,3,0,7,-1,9]; let mut positives=Vec::new(); for v in values {if v<=0 {continue;} positives.push(v);} println!(\"{positives:?}\"); }
", Para [Strong [Str "Expected behavior:"], Str " Runs independently with the standard library and prints the result of this lesson's focused operation. Predict the output, then compare it with the terminal output."], Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Failing to trim the newline before parsing input."]], [Plain [Str "Choosing a sentinel that is also valid data without documenting it."]], [Plain [Str "Creating a loop whose state is not updated on every path."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each binding, expression, ownership transfer, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and predict the result before running it."]], [Plain [Str "Add one boundary case and one invalid or missing-data case; state expected behavior before implementing the change."]], [Plain [Str "Refactor one part using the Rust feature named in this lesson (continue and filtering); run cargo check and explain the diagnostic output."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in ownership and borrowing expressions (&, &mut, ::, ->, ?). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order and verify that output is announced without unexpected focus movement."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain continue and filtering using Rust terminology."]], [Plain [Str "\9744", Space, Str "I can compile and run the example with cargo run."]], [Plain [Str "\9744", Space, Str "I can explain the ownership, borrowing, and type decisions used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-55-preventing-infinite-loops", ["unnumbered", "unlisted"], []) [Str "Lesson 5.5: Preventing infinite loops"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Rust Programming Language: Repetition with Loops"] ("https://doc.rust-lang.org/book/ch03-05-control-flow.html", "")]], [Plain [Link ("", [], []) [Str "Rust standard library documentation"] ("https://doc.rust-lang.org/std/", "")]], [Plain [Str "Matching Python lesson: Lesson 5.5: Avoiding Infinite Loops"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Identify what makes a loop stop."]], [Plain [Str "Add an attempt limit and handle the end of input."]], [Plain [Str "Write a loop that runs at least once."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "An ", Emph [Str "infinite loop"], Str " never ends because its condition never becomes false. Common causes are forgetting to change the loop variable, testing the wrong variable, and waiting for input that never arrives. In a terminal, stop a running program with Ctrl+C. Rust's ", Code ("", [], []) "loop { ... }", Str " is an ", Emph [Str "intentional"], Str " endless loop and must contain a ", Code ("", [], []) "break", Str " or ", Code ("", [], []) "return", Str "."], Para [Str "Protect every loop with a ", Emph [Str "progress rule"], Str " and a ", Emph [Str "limit"], Str ": count attempts, and stop when the limit is reached or the input ends. Rust has no ", Code ("", [], []) "do ... while", Str "; to run a body at least once, use ", Code ("", [], []) "loop", Str " and put the exit test at the end."], Para [Str "The example allows three attempts to enter a score from 0 to 100. With the typed lines abc, 105, and 88, the first two are rejected and the third is accepted."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["rust"], []) "use std::io;

fn next_line() -> Option<String> {
    let mut line = String::new();
    match io::stdin().read_line(&mut line) {
        Ok(0) | Err(_) => None,
        Ok(_) => Some(line.trim().to_string()),
    }
}

fn main() {
    let max_attempts = 3;
    let mut attempts = 0;
    let mut score: Option<i32> = None;

    while attempts < max_attempts && score.is_none() {
        attempts += 1;
        println!(\"Enter a score from 0 to 100 (attempt {attempts} of {max_attempts}):\");
        let Some(text) = next_line() else {
            println!(\"No more input.\");
            break;
        };
        match text.parse::<i32>() {
            Ok(number) if (0..=100).contains(&number) => score = Some(number),
            _ => println!(\"Invalid score: {text}\"),
        }
    }

    match score {
        Some(score) => println!(\"Accepted score: {score}\"),
        None => println!(\"No valid score was entered.\"),
    }

    let mut count = 1;
    loop {
        println!(\"{count}\");
        count += 1;
        if count > 3 {
            break;
        }
    }
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "abc
105
88
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "Enter a score from 0 to 100 (attempt 1 of 3):
Invalid score: abc
Enter a score from 0 to 100 (attempt 2 of 3):
Invalid score: 105
Enter a score from 0 to 100 (attempt 3 of 3):
Accepted score: 88
1
2
3
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "Enter a score from 0 to 100 (attempt 1 of 3):
No more input.
No valid score was entered.
1
2
3
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to increase ", Code ("", [], []) "attempts", Str ", so the limit is never reached."]], [Plain [Str "Writing ", Code ("", [], []) "loop { ... }", Str " with no ", Code ("", [], []) "break", Str " or ", Code ("", [], []) "return", Str ", which never ends."]], [Plain [Str "Looking for a ", Code ("", [], []) "do ... while", Str " loop. Use ", Code ("", [], []) "loop", Str " with the test at the end."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run with abc, 105, and 88 and confirm the accepted score."]], [Plain [Str "Run with three invalid lines and read the final message."]], [Plain [Str "Change the limit to 5 and test it."]], [Plain [Str "For each loop in the example, write down what makes it stop."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "A loop that cannot be stopped is an accessibility problem, because it can flood a screen reader with output. Learn Ctrl+C before running loops, give every input loop a limit, and write error messages that say what is valid."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can name what ends each loop."]], [Plain [Str "\9744", Space, Str "I can add an attempt limit."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]], [Plain [Str "\9744", Space, Str "I can write a loop that runs at least once."]], [Plain [Str "\9744", Space, Str "I know how to interrupt a program."]]], HorizontalRule]