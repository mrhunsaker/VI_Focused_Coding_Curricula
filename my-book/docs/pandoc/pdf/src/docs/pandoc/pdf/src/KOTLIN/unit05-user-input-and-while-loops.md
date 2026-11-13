[Header 2 ("unit-5-user-input-and-while-loops", [], []) [Str "Unit 5: User Input and while Loops"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Read and validate input, write sentinel and flag loops, skip entries, and prevent endless loops."], HorizontalRule, Header 3 ("lesson-51-how-console-input-works", ["unnumbered", "unlisted"], []) [Str "Lesson 5.1: How Console Input Works"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Basic syntax"] ("https://kotlinlang.org/docs/basic-syntax.html", "")]], [Plain [Link ("", [], []) [Str "Null safety"] ("https://kotlinlang.org/docs/null-safety.html", "")]], [Plain [Str "Matching Python lesson: Lesson 5.1: How the input() Function Works"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Read a line and recognize it as text."]], [Plain [Str "Convert it safely and handle failure."]], [Plain [Str "Handle the end of input."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "readlnOrNull()", Str " returns the next line as a ", Code ("", [], []) "String?", Str ", or ", Code ("", [], []) "null", Str " when the input has ended. It never returns a number: typed digits are text until you convert them. ", Code ("", [], []) "toIntOrNull()", Str " returns an ", Code ("", [], []) "Int?", Str ", and a ", Code ("", [], []) "null", Str " result means the text was not a whole number."], Para [Str "A program that reads input must plan for three cases: a valid value, an invalid value, and no value at all. The example reads an age and then a second value, so you can see the valid, invalid, and missing cases. With the typed value 16 the age five years later is 21; the second value, ", Code ("", [], []) "abc", Str ", is rejected."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun main() {
    println(\"How old are you?\")
    val text = readlnOrNull()
    println(\"Read: ${if (text == null) \"nothing\" else text::class.simpleName}\")

    val age = text?.trim()?.toIntOrNull()
    if (age != null) {
        println(\"In 5 years: ${age + 5}\")
    } else {
        println(\"That was not a whole number.\")
    }

    println(\"Enter another value:\")
    val second = readlnOrNull()?.trim()?.toIntOrNull()
    if (second != null) {
        println(\"Number: $second\")
    } else {
        println(\"Not a number; toIntOrNull returned null.\")
    }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "16
abc
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "How old are you?
Read: String
In 5 years: 21
Enter another value:
Not a number; toIntOrNull returned null.
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "How old are you?
Read: nothing
That was not a whole number.
Enter another value:
Not a number; toIntOrNull returned null.
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Adding to the text without converting it, which does not compile or gives joined text."]], [Plain [Str "Using ", Code ("", [], []) "toInt()", Str " on user input and crashing on ", Code ("", [], []) "abc", Str "."]], [Plain [Str "Forgetting that an empty answer is not a number, so ", Code ("", [], []) "toIntOrNull()", Str " is ", Code ("", [], []) "null", Str "."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run with 16 and then ", Code ("", [], []) "abc", Str " and compare with the shown output."]], [Plain [Str "Run with no input and explain every line printed."]], [Plain [Str "Accept an age only from 0 to 120."]], [Plain [Str "Rewrite the program using ", Code ("", [], []) "readln()", Str " and describe what happens at the end of input."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each prompt is a complete sentence on its own line. Run the program twice, once typing and once with piped input, and compare what your screen reader announces."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can read a line of input."]], [Plain [Str "\9744", Space, Str "I can convert and validate it."]], [Plain [Str "\9744", Space, Str "I handle ", Code ("", [], []) "null", Str " at the end of input."]], [Plain [Str "\9744", Space, Str "I know typed input is text."]], [Plain [Str "\9744", Space, Str "I can write a clear prompt."]]], HorizontalRule, Header 3 ("lesson-52-the-while-loop-in-action", ["unnumbered", "unlisted"], []) [Str "Lesson 5.2: The while Loop in Action"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Control flow: while loops"] ("https://kotlinlang.org/docs/control-flow.html#while-loops", "")]], [Plain [Str "Matching Python lesson: Lesson 5.2: The while Loop in Action"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write a counting ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "Write a sentinel loop that ends on a command."]], [Plain [Str "Stop at the end of input."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "while (condition) { ... }", Str " repeats while the condition is true, testing ", Strong [Str "before"], Str " each pass. A loop needs a way to make its condition false, normally by changing a variable inside the body: ", Code ("", [], []) "count++", Str " adds one."], Para [Str "A ", Emph [Str "sentinel"], Str " is a special input that tells the loop to stop. Here it is the word ", Code ("", [], []) "quit", Str ". The standard pattern reads once before the loop and again at the end of each pass, and tests for ", Code ("", [], []) "null", Str " as well, so the loop ends when input runs out even without ", Code ("", [], []) "quit", Str "."], Para [Str "The example counts from 1 to 5, then repeats a message prompt until the user types ", Code ("", [], []) "quit", Str "."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun main() {
    var count = 1
    while (count <= 5) {
        println(count)
        count++
    }
    println(\"Counting finished!\")

    println(\"Enter a message, or type quit to exit:\")
    var message = readlnOrNull()
    while (message != null && message != \"quit\") {
        println(\"You said: $message\")
        println(\"Enter a message, or type quit to exit:\")
        message = readlnOrNull()
    }
    println(\"Goodbye!\")
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
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to change the loop variable, which creates an endless loop."]], [Plain [Str "Testing for ", Code ("", [], []) "quit", Str " but not for ", Code ("", [], []) "null", Str ", so the loop reads forever after input ends."]], [Plain [Str "Reading input only before the loop and never again inside it."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output for the typed lines hello, scores, and quit."]], [Plain [Str "Change the sentinel to ", Code ("", [], []) "exit", Str " and update the prompt."]], [Plain [Str "Count the messages entered and print the count at the end."]], [Plain [Str "Rewrite the counting loop with ", Code ("", [], []) "for (count in 1..5)", Str " and compare."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each prompt is on its own line and each response begins with ", Code ("", [], []) "You said:", Str ", so the conversation can be followed in order by ear. If a loop floods the screen reader, stop it with Ctrl+C."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a counting ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "\9744", Space, Str "I can write a sentinel loop."]], [Plain [Str "\9744", Space, Str "I test for ", Code ("", [], []) "null", Str " as well as the sentinel."]], [Plain [Str "\9744", Space, Str "I update the loop variable."]], [Plain [Str "\9744", Space, Str "I can compare ", Code ("", [], []) "while", Str " with ", Code ("", [], []) "for", Str "."]]], HorizontalRule, Header 3 ("lesson-53-flags-break-and-labels", ["unnumbered", "unlisted"], []) [Str "Lesson 5.3: Flags, break, and Labels"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Returns and jumps"] ("https://kotlinlang.org/docs/returns.html", "")]], [Plain [Str "Matching Python lesson: Lesson 5.3: Using Flags and break to Exit Loops"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Control a loop with a Boolean flag."]], [Plain [Str "Leave a loop with ", Code ("", [], []) "break", Str " and an outer loop with a label."]], [Plain [Str "Search a list and remember the position."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "flag"], Str " is a Boolean variable that controls a loop: the loop runs while ", Code ("", [], []) "running", Str " is true, and the body sets it to ", Code ("", [], []) "false", Str " to stop. ", Code ("", [], []) "break", Str " leaves the nearest enclosing loop at once."], Para [Str "A search keeps its answer in a variable (here ", Code ("", [], []) "-1", Str " means \"not found\"), sets it when the item is found, and uses ", Code ("", [], []) "break", Str ". After the loop, the variable says whether a match was found. List positions start at 0."], Para [Str "A ", Emph [Str "label"], Str " lets ", Code ("", [], []) "break", Str " leave an outer loop from inside an inner one: write ", Code ("", [], []) "outer@ for (...)", Str " and ", Code ("", [], []) "break@outer", Str "."], Para [Str "The shared scores 82, 91, 76, 88 have their first score of 90 or higher at index 1, with the value 91."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun main() {
    var running = true
    var handled = 0
    while (running) {
        println(\"Say something, or type quit to stop:\")
        val message = readlnOrNull()
        if (message == null || message == \"quit\") {
            running = false
        } else {
            handled++
            println(\"You said: $message\")
        }
    }
    println(\"Messages handled: $handled\")

    val scores = listOf(82, 91, 76, 88)
    var foundIndex = -1
    for ((index, score) in scores.withIndex()) {
        if (score >= 90) {
            foundIndex = index
            break
        }
    }
    if (foundIndex >= 0) {
        println(\"First score of 90 or higher: ${scores[foundIndex]} at index $foundIndex\")
    } else {
        println(\"No score of 90 or higher.\")
    }

    outer@ for (row in 1..3) {
        for (col in 1..3) {
            if (row * col == 4) {
                println(\"Stopped at row $row, column $col\")
                break@outer
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
Stopped at row 2, column 2
", Para [Str "With no standard input at all, the program ends cleanly and prints:"], CodeBlock ("", ["text"], []) "Say something, or type quit to stop:
Messages handled: 0
First score of 90 or higher: 91 at index 1
Stopped at row 2, column 2
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Setting the flag but running more code in the same pass that should be skipped."]], [Plain [Str "Forgetting to give the result variable a starting value, then misreading it after the loop."]], [Plain [Str "Using ", Code ("", [], []) "break", Str " in an inner loop and expecting it to leave the outer loop."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run with hello and quit and confirm the count is 1."]], [Plain [Str "Change the search to the first score below 80 and predict the index."]], [Plain [Str "Rewrite the first loop without a flag, using ", Code ("", [], []) "break", Str "."]], [Plain [Str "Explain in two sentences when a flag is clearer than ", Code ("", [], []) "break", Str "."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Report search results as complete sentences that include both the value and its position. Remember that Kotlin indexes start at 0, and say 'index 1' aloud to avoid confusing it with 'the first'."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can control a loop with a flag."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "break", Str "."]], [Plain [Str "\9744", Space, Str "I can use a label to leave an outer loop."]], [Plain [Str "\9744", Space, Str "I can search a list and keep the position."]], [Plain [Str "\9744", Space, Str "I can explain flag versus ", Code ("", [], []) "break", Str "."]]], HorizontalRule, Header 3 ("lesson-54-skipping-entries-with-continue", ["unnumbered", "unlisted"], []) [Str "Lesson 5.4: Skipping Entries with continue"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Returns and jumps"] ("https://kotlinlang.org/docs/returns.html", "")]], [Plain [Str "Matching Python lesson: Lesson 5.4: Using continue in Loops"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Skip one pass of a loop with ", Code ("", [], []) "continue", Str "."]], [Plain [Str "Skip invalid scores in a list."]], [Plain [Str "Compare ", Code ("", [], []) "continue", Str " with ", Code ("", [], []) "filter", Str "."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "continue", Str " skips the rest of the current pass and goes straight to the next one. It is useful for ignoring invalid entries while still reporting them. In a ", Code ("", [], []) "while", Str " loop, make sure that the loop variable is updated ", Emph [Str "before"], Str " ", Code ("", [], []) "continue", Str ", or the loop never ends."], Para [Str "Kotlin also lets you filter first: ", Code ("", [], []) "rawScores.filter { it in 0..100 }", Str " builds a list of the valid scores, which is shorter when you do not need to report each skipped entry."], Para [Str "The example skips the invalid scores -5 and 105 in the list 82, -5, 91, 105, 76, 88. The four valid scores total 337."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun main() {
    val rawScores = listOf(82, -5, 91, 105, 76, 88)
    var validTotal = 0
    var validCount = 0

    for (raw in rawScores) {
        if (raw < 0 || raw > 100) {
            println(\"Skipping invalid score: $raw\")
            continue
        }
        validTotal += raw
        validCount++
    }
    println(\"Valid scores: $validCount, total: $validTotal\")

    for (number in 1..9) {
        if (number % 2 == 0) continue
        println(number)
    }

    println(rawScores.filter { it in 0..100 }.sum())
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Skipping invalid score: -5
Skipping invalid score: 105
Valid scores: 4, total: 337
1
3
5
7
9
337
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Putting statements that must always run after ", Code ("", [], []) "continue", Str ", so they are skipped."]], [Plain [Str "Using ", Code ("", [], []) "continue", Str " in a ", Code ("", [], []) "while", Str " loop before updating the counter, which creates an endless loop."]], [Plain [Str "Confusing ", Code ("", [], []) "continue", Str " (skip this pass) with ", Code ("", [], []) "break", Str " (leave the loop)."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed lines and the final total."]], [Plain [Str "Skip scores below 80 instead."]], [Plain [Str "Rewrite the first loop with an ", Code ("", [], []) "if", Str "/", Code ("", [], []) "else", Str " and no ", Code ("", [], []) "continue", Str "."]], [Plain [Str "Rewrite it with ", Code ("", [], []) "filter", Str " and explain what you no longer report."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print a line for each skipped entry, so the screen reader announces what was ignored. Never skip silently when a user needs to know what happened to their data."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "continue", Str "."]], [Plain [Str "\9744", Space, Str "I can skip invalid entries."]], [Plain [Str "\9744", Space, Str "I know where the counter must be updated."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "filter", Str " as an alternative."]], [Plain [Str "\9744", Space, Str "I can tell ", Code ("", [], []) "continue", Str " from ", Code ("", [], []) "break", Str "."]]], HorizontalRule, Header 3 ("lesson-55-avoiding-infinite-loops", ["unnumbered", "unlisted"], []) [Str "Lesson 5.5: Avoiding Infinite Loops"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Control flow: do-while"] ("https://kotlinlang.org/docs/control-flow.html#while-loops", "")]], [Plain [Str "Matching Python lesson: Lesson 5.5: Avoiding Infinite Loops"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Identify what makes a loop stop."]], [Plain [Str "Add an attempt limit and handle the end of input."]], [Plain [Str "Use ", Code ("", [], []) "do ... while", Str "."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "An ", Emph [Str "infinite loop"], Str " never ends because its condition never becomes false. Common causes are forgetting to change the loop variable, testing the wrong variable, and waiting for input that never arrives. In a terminal, stop a running program with Ctrl+C."], Para [Str "Protect every loop with a ", Emph [Str "progress rule"], Str " and a ", Emph [Str "limit"], Str ": count attempts, and stop when the limit is reached or the input ends."], Para [Code ("", [], []) "do { ... } while (condition)", Str " runs the body first and tests afterward, so it always runs at least once. A variable declared inside the body is visible in the ", Code ("", [], []) "while", Str " condition."], Para [Str "The example allows three attempts to enter a score from 0 to 100. With the typed lines abc, 105, and 88, the first two are rejected and the third is accepted."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun main() {
    val maxAttempts = 3
    var attempts = 0
    var score: Int? = null

    while (attempts < maxAttempts && score == null) {
        attempts++
        println(\"Enter a score from 0 to 100 (attempt $attempts of $maxAttempts):\")
        val text = readlnOrNull()
        if (text == null) {
            println(\"No more input.\")
            break
        }
        val number = text.trim().toIntOrNull()
        if (number != null && number in 0..100) {
            score = number
        } else {
            println(\"Invalid score: $text\")
        }
    }

    if (score != null) {
        println(\"Accepted score: $score\")
    } else {
        println(\"No valid score was entered.\")
    }

    var count = 1
    do {
        println(count)
        count++
    } while (count <= 3)
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):"], CodeBlock ("", ["text"], []) "abc
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
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to increase ", Code ("", [], []) "attempts", Str ", so the limit is never reached."]], [Plain [Str "Not handling ", Code ("", [], []) "null", Str " from ", Code ("", [], []) "readlnOrNull()", Str ", so the loop never ends or crashes when input closes."]], [Plain [Str "Writing ", Code ("", [], []) "while (count < 3)", Str " after a ", Code ("", [], []) "do", Str " body and stopping one pass early."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run with abc, 105, and 88 and confirm the accepted score."]], [Plain [Str "Run with three invalid lines and read the final message."]], [Plain [Str "Change the limit to 5 and test it."]], [Plain [Str "For each loop in the example, write down what makes it stop."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "A loop that cannot be stopped is an accessibility problem, because it can flood a screen reader with output. Learn Ctrl+C before running loops, give every input loop a limit, and write error messages that say what is valid."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can name what ends each loop."]], [Plain [Str "\9744", Space, Str "I can add an attempt limit."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "do ... while", Str "."]], [Plain [Str "\9744", Space, Str "I know how to interrupt a program."]]], HorizontalRule]