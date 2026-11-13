[Header 2 ("unit-9-testing-and-data-analysis", [], []) [Str "Unit 9: Testing and Data Analysis"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Write tests with expected results, test random code by its properties, analyze the shared text sample, and read the shared CSV file."], HorizontalRule, Header 3 ("lesson-91-testing-functions", ["unnumbered", "unlisted"], []) [Str "Lesson 9.1: Testing Functions"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Functions"] ("https://kotlinlang.org/docs/functions.html", "")]], [Plain [Link ("", [], []) [Str "Functions"] ("https://kotlinlang.org/docs/functions.html", "")]], [Plain [Str "Matching Python lesson: Lesson 9.1: Testing Your Code"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write checks with chosen inputs and expected results."]], [Plain [Str "Compare decimals with a tolerance."]], [Plain [Str "Test boundary values and report failure with an exit status."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "test"], Str " runs code with chosen inputs and compares the result with a value decided in advance. Real Kotlin projects use the ", Code ("", [], []) "kotlin.test", Str " library with JUnit, added through Gradle. To keep this course free of build tooling, the example uses a tiny ", Code ("", [], []) "check", Str " function; the habits (inputs, expected values, boundaries) are the same."], Para [Str "Decimal results are compared with a ", Emph [Str "tolerance"], Str ", not ", Code ("", [], []) "==", Str ", because of floating-point approximation: the tip for 24.50 at 0.15 is stored as 3.6749999999999998, so the test checks that it is within a tiny distance of 3.675."], Para [Str "The same tests appear in every language track: ", Code ("", [], []) "add(5, 3)", Str " is 8, ", Code ("", [], []) "add(-5, -3)", Str " is -8, ", Code ("", [], []) "add(10, -4)", Str " is 6, the tip is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F."], Para [Code ("", [], []) "exitProcess(1)", Str " ends the program with a failure status when any check fails, so other tools can notice."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "import kotlin.math.abs
import kotlin.system.exitProcess

fun add(a: Int, b: Int) = a + b

fun calculateTip(bill: Double, rate: Double) = bill * rate

fun classify(score: Int): String = when {
    score >= 90 -> \"A\"
    score >= 80 -> \"B\"
    score >= 70 -> \"C\"
    score >= 60 -> \"D\"
    else -> \"F\"
}

var passed = 0
var failed = 0

fun <T> check(name: String, actual: T, expected: T) {
    if (actual == expected) {
        passed++
        println(\"PASS $name\")
    } else {
        failed++
        println(\"FAIL $name: expected $expected but got $actual\")
    }
}

fun checkClose(name: String, actual: Double, expected: Double, tolerance: Double = 1e-9) {
    check(name, abs(actual - expected) <= tolerance, true)
}

fun main() {
    check(\"add 5 and 3\", add(5, 3), 8)
    check(\"add -5 and -3\", add(-5, -3), -8)
    check(\"add 10 and -4\", add(10, -4), 6)
    checkClose(\"tip on 24.50 at 0.15\", calculateTip(24.5, 0.15), 3.675)
    check(\"tip on a zero bill\", calculateTip(0.0, 0.15), 0.0)
    check(\"classify 90\", classify(90), \"A\")
    check(\"classify 89\", classify(89), \"B\")
    check(\"classify 60\", classify(60), \"D\")
    check(\"classify 59\", classify(59), \"F\")

    println(\"$passed passed, $failed failed\")
    if (failed > 0) exitProcess(1)
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
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Comparing decimal results with ", Code ("", [], []) "==", Str "."]], [Plain [Str "Testing only typical values and skipping the boundaries 90, 89, 60, and 59."]], [Plain [Str "Writing the expected value after seeing the output, which turns the test into a copy of the bug."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Change one expected value so a check fails, read the message, and restore it."]], [Plain [Str "Add checks for the grades at 80, 79, 70, and 69."]], [Plain [Str "Write checks for ", Code ("", [], []) "isPassing(score)", Str " before writing the function."]], [Plain [Str "Explain why the tip check uses a tolerance."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each check prints one complete line that starts with PASS or FAIL, and the last line gives the counts, so the result can be understood from the first word of each line and the final summary."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a check with an expected value."]], [Plain [Str "\9744", Space, Str "I can compare decimals with a tolerance."]], [Plain [Str "\9744", Space, Str "I can choose boundary tests."]], [Plain [Str "\9744", Space, Str "I can read PASS and FAIL lines."]], [Plain [Str "\9744", Space, Str "I know how to signal failure with an exit status."]]], HorizontalRule, Header 3 ("lesson-92-testing-classes", ["unnumbered", "unlisted"], []) [Str "Lesson 9.2: Testing Classes"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Classes"] ("https://kotlinlang.org/docs/classes.html", "")]], [Plain [Link ("", [], []) [Str "Exceptions"] ("https://kotlinlang.org/docs/exceptions.html", "")]], [Plain [Str "Matching Python lesson: Lesson 9.2: Testing a Class"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create a fresh object for every test."]], [Plain [Str "Test a value, a change of state, and an error."]], [Plain [Str "Use ", Code ("", [], []) "runCatching", Str " to test that an error occurs."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Each test should start from a known state, so create a new object for every test with a ", Emph [Str "setup"], Str " function. Tests that share an object can affect each other and fail in confusing ways."], Para [Str "Test three kinds of behavior: that a function returns the right value (", Code ("", [], []) "totalValue", Str " for 3 at 2.50 is 7.5), that a function changes the object correctly (restocking 2 makes the quantity 5), and that invalid use is rejected (restocking a negative amount throws)."], Para [Code ("", [], []) "runCatching { ... }.isFailure", Str " is true when the block throws, so a test can assert that an error ", Emph [Str "does"], Str " happen."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "import kotlin.math.abs

class Item(val name: String, var quantity: Int, val unitPrice: Double) {
    fun totalValue(): Double = quantity * unitPrice

    fun restock(amount: Int) {
        require(amount >= 0) { \"amount must not be negative\" }
        quantity += amount
    }
}

fun setup() = Item(\"Notebook\", 3, 2.50)

var failures = 0

fun test(name: String, body: () -> Unit) {
    val result = runCatching(body)
    if (result.isSuccess) {
        println(\"PASS $name\")
    } else {
        failures++
        println(\"FAIL $name: ${result.exceptionOrNull()?.message}\")
    }
}

fun assertThat(condition: Boolean, message: String) {
    if (!condition) throw AssertionError(message)
}

fun main() {
    test(\"total value is 7.5\") {
        assertThat(abs(setup().totalValue() - 7.5) < 1e-9, \"wrong total\")
    }

    test(\"restock adds to the quantity\") {
        val item = setup()
        item.restock(2)
        assertThat(item.quantity == 5, \"quantity should be 5\")
    }

    test(\"restock rejects a negative amount\") {
        val failed = runCatching { setup().restock(-1) }.isFailure
        assertThat(failed, \"an error should have been thrown\")
    }

    println(if (failures == 0) \"All tests passed.\" else \"$failures test(s) failed.\")
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "PASS total value is 7.5
PASS restock adds to the quantity
PASS restock rejects a negative amount
All tests passed.
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Sharing one object between tests, so an earlier test changes the later ones."]], [Plain [Str "Testing only the successful path and never the error path."]], [Plain [Str "Writing an ", Code ("", [], []) "assertThat", Str " with no message, so a failure says nothing about what went wrong."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Add a test that ", Code ("", [], []) "restock(0)", Str " leaves the quantity unchanged."]], [Plain [Str "Add a test for an ", Code ("", [], []) "isValid", Str " function."]], [Plain [Str "Break ", Code ("", [], []) "restock", Str " on purpose and read the failure line."]], [Plain [Str "Explain why ", Code ("", [], []) "setup", Str " creates a new item each time."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Name each test as a short sentence that says what it checks, so the PASS and FAIL lines read as clear statements. Read the final summary line first."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can create a fresh object per test."]], [Plain [Str "\9744", Space, Str "I can test a return value."]], [Plain [Str "\9744", Space, Str "I can test a change of state."]], [Plain [Str "\9744", Space, Str "I can test that an error is thrown."]], [Plain [Str "\9744", Space, Str "I can write a clear test name."]]], HorizontalRule, Header 3 ("lesson-93-random-numbers", ["unnumbered", "unlisted"], []) [Str "Lesson 9.3: Random Numbers"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Kotlin standard library: kotlin.random"] ("https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.random/", "")]], [Plain [Str "Matching Python lesson: Lesson 9.3: Random Numbers and Simulation"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Generate random integers and decimals."]], [Plain [Str "Use a seed to make results repeatable."]], [Plain [Str "Test random code by its properties."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "kotlin.random.Random", Str " produces random numbers. ", Code ("", [], []) "Random.nextInt(from, until)", Str " returns an integer from ", Code ("", [], []) "from", Str " up to but ", Strong [Str "not including"], Str " ", Code ("", [], []) "until", Str ", so a die roll is ", Code ("", [], []) "nextInt(1, 7)", Str ". ", Code ("", [], []) "Random.nextDouble()", Str " returns a decimal from 0.0 up to but not including 1.0, and ", Code ("", [], []) "list.random(random)", Str " picks a list element."], Para [Code ("", [], []) "Random(42)", Str " creates a generator with a fixed ", Emph [Str "seed"], Str ": two generators with the same seed produce the same sequence. Without a seed the results change on every run. Because the exact sequence may differ between Kotlin versions, tests should check ", Emph [Str "properties"], Str " (every roll is between 1 and 6) and repeatability, not particular values."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "import kotlin.random.Random

fun main() {
    val first = Random(42)
    val second = Random(42)
    val firstRolls = List(5) { first.nextInt(1, 7) }
    val secondRolls = List(5) { second.nextInt(1, 7) }
    println(\"Same seed gives the same rolls: ${firstRolls == secondRolls}\")

    val random = Random(7)
    val inRange = List(1000) { random.nextInt(1, 7) }.all { it in 1..6 }
    println(\"All rolls between 1 and 6: $inRange\")

    val decimal = random.nextDouble()
    println(\"Decimal in [0, 1): ${decimal >= 0.0 && decimal < 1.0}\")

    val scores = listOf(82, 91, 76, 88)
    val chosen = scores.random(random)
    println(\"Chosen score is from the list: ${chosen in scores}\")
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Same seed gives the same rolls: true
All rolls between 1 and 6: true
Decimal in [0, 1): true
Chosen score is from the list: true
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) "nextInt(1, 6)", Str " for a die and never rolling a 6. The upper limit is excluded."]], [Plain [Str "Testing for specific random values that may change between versions."]], [Plain [Str "Creating a new unseeded generator for every roll, which wastes work and can repeat values."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program three times and compare."]], [Plain [Str "Change the seeds and check that the property lines still print ", Code ("", [], []) "true", Str "."]], [Plain [Str "Simulate 600 rolls and count how many of each face appeared (the counts will differ with the seed)."]], [Plain [Str "Explain why a test should check a property rather than a specific random number."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print yes or no style results for random behavior, so the announced output is the same on every run and the screen reader does not read unpredictable values."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "nextInt", Str " with an excluded upper limit."]], [Plain [Str "\9744", Space, Str "I can set a seed."]], [Plain [Str "\9744", Space, Str "I can test properties of random code."]], [Plain [Str "\9744", Space, Str "I know sequences can differ between versions."]], [Plain [Str "\9744", Space, Str "I can pick a random list item."]]], HorizontalRule, Header 3 ("lesson-94-text-analysis", ["unnumbered", "unlisted"], []) [Str "Lesson 9.4: Text Analysis"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Strings"] ("https://kotlinlang.org/docs/strings.html", "")]], [Plain [Link ("", [], []) [Str "Grouping"] ("https://kotlinlang.org/docs/collection-grouping.html", "")]], [Plain [Str "Matching Python lesson: Lesson 9.4: Data Analysis - Text Analysis"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Split text into words and count them."]], [Plain [Str "Count word and letter frequencies with ", Code ("", [], []) "groupingBy", Str "."]], [Plain [Str "Produce stable, sorted output."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Splitting uses ", Code ("", [], []) "split", Str ": ", Code ("", [], []) "cleaned.split(\" \")", Str " or a regular expression such as ", Code ("", [], []) "Regex(\"\\\\s+\")", Str " for any run of spaces. Counting is a one-liner with ", Code ("", [], []) "groupingBy { it }.eachCount()", Str ", which returns a map from each item to its count."], Para [Str "Map order is only stable if you make it so. ", Code ("", [], []) "eachCount()", Str " keeps the order in which items first appeared, and sorting with ", Code ("", [], []) "sortedWith(compareBy({ -it.value }, { it.key }))", Str " orders by count (highest first) and then alphabetically, so ties print in a fixed order."], Para [Str "The shared text sample is \"A student studies programming. Programming develops problem-solving skills.\" After lower-casing and removing the periods it has 8 words, and ", Code ("", [], []) "programming", Str " appears twice."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun main() {
    val text = \"A student studies programming. Programming develops problem-solving skills.\"
    val words = text.lowercase().replace(\".\", \"\").split(\" \")

    println(\"Word count: ${words.size}\")
    println(\"Word frequencies:\")
    for ((word, count) in words.groupingBy { it }.eachCount()) {
        println(\"'$word': $count\")
    }

    val letters = text.lowercase().filter { it.isLetter() }.groupingBy { it }.eachCount()
    val topThree = letters.entries.sortedWith(compareBy({ -it.value }, { it.key })).take(3)
    println(\"Most common letters:\")
    for ((letter, count) in topThree) {
        println(\"$letter: $count\")
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
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Counting punctuation as part of a word, so ", Code ("", [], []) "programming.", Str " and ", Code ("", [], []) "programming", Str " are different words."]], [Plain [Str "Forgetting to lower-case first, so ", Code ("", [], []) "Programming", Str " and ", Code ("", [], []) "programming", Str " are counted separately."]], [Plain [Str "Relying on map order for tied counts without a tie-break."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the word count and the count for ", Code ("", [], []) "programming", Str " before running."]], [Plain [Str "Count the words longer than 8 letters."]], [Plain [Str "Print the longest word."]], [Plain [Str "Change the sort so ties are listed in reverse alphabetical order."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the frequency list in its fixed order. Because the order is stable, you can learn it and compare runs by ear. Print each pair as a short sentence with the same wording every time."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can split text into words."]], [Plain [Str "\9744", Space, Str "I can count frequencies with ", Code ("", [], []) "groupingBy", Str "."]], [Plain [Str "\9744", Space, Str "I can sort with a tie-break."]], [Plain [Str "\9744", Space, Str "I can remove punctuation first."]], [Plain [Str "\9744", Space, Str "I can read a stable report."]]], HorizontalRule, Header 3 ("lesson-95-working-with-csv-files", ["unnumbered", "unlisted"], []) [Str "Lesson 9.5: Working with CSV Files"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Kotlin standard library: kotlin.io"] ("https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.io/", "")]], [Plain [Link ("", [], []) [Str "Strings"] ("https://kotlinlang.org/docs/strings.html", "")]], [Plain [Str "Matching Python lesson: Lesson 9.5: Data Analysis - CSV Files"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create and read a CSV file."]], [Plain [Str "Split lines into fields and convert numbers."]], [Plain [Str "Compute an average and a count."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A CSV (comma-separated values) file stores a table as text. The first line names the columns and each later line is a record. The shared student file has the columns ", Code ("", [], []) "student_id", Str ", ", Code ("", [], []) "first_name", Str ", ", Code ("", [], []) "last_name", Str ", ", Code ("", [], []) "score", Str ", and ", Code ("", [], []) "active", Str ", and three records."], Para [Str "The standard library has no CSV reader. ", Code ("", [], []) "line.split(\",\")", Str " works only for ", Strong [Str "simple"], Str " files: a value that contains a comma inside quotation marks, such as ", Code ("", [], []) "\"Smith, Jr.\"", Str ", would be split wrongly. For such files use a maintained library or write a real parser."], Para [Str "Every field is text. Convert the score with ", Code ("", [], []) "toInt()", Str " and compare ", Code ("", [], []) "active", Str " with the text ", Code ("", [], []) "\"true\"", Str ". With scores 91, 82, and 76 the average is 83.00, and two students are active."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "import java.io.File

fun main() {
    val file = File(\"students.csv\")
    file.writeText(
        \"student_id,first_name,last_name,score,active\\n\" +
            \"1,Avery,Student,91,true\\n\" +
            \"2,Jordan,Lee,82,true\\n\" +
            \"3,Casey,Smith,76,false\\n\"
    )

    if (!file.exists()) {
        println(\"Error: students.csv was not found.\")
        return
    }
    val lines = file.readLines()
    println(\"Columns: \" + lines.first().split(\",\").joinToString(\", \"))

    var total = 0
    var active = 0
    val students = lines.drop(1)
    for (line in students) {
        val row = line.split(\",\")
        val score = row[3].toInt()
        total += score
        if (row[4] == \"true\") active++
        println(\"${row[0]}: ${row[1]} ${row[2]} scored $score\")
    }

    println(\"Students: ${students.size}\")
    println(\"Average score: \" + \"%.2f\".format(total.toDouble() / students.size))
    println(\"Active students: $active\")
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Columns: student_id, first_name, last_name, score, active
1: Avery Student scored 91
2: Jordan Lee scored 82
3: Casey Smith scored 76
Students: 3
Average score: 83.00
Active students: 2
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Splitting a CSV line at every comma when a value contains a quoted comma."]], [Plain [Str "Forgetting to convert the text in the score column to a number."]], [Plain [Str "Not skipping the header line, so ", Code ("", [], []) "toInt()", Str " fails on the text ", Code ("", [], []) "score", Str "."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed lines before running."]], [Plain [Str "Add a fourth student and check the new average."]], [Plain [Str "Print only the active students."]], [Plain [Str "Explain, with an example, why ", Code ("", [], []) "\"Smith, Jr.\"", Str " breaks ", Code ("", [], []) "split(\",\")", Str "."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print one student per line with the same wording each time, so the screen reader announces a repeating pattern that is easy to compare. Read the column names aloud once at the start."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write and read a CSV file."]], [Plain [Str "\9744", Space, Str "I can split a line into fields."]], [Plain [Str "\9744", Space, Str "I convert text fields to numbers."]], [Plain [Str "\9744", Space, Str "I can compute an average and a count."]], [Plain [Str "\9744", Space, Str "I know when ", Code ("", [], []) "split", Str " is not enough."]]], HorizontalRule]