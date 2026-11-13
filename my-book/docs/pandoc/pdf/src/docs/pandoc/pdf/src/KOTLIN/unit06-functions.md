[Header 2 ("unit-6-functions", [], []) [Str "Unit 6: Functions"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Define functions, pass arguments, return results, process collections in functions, and accept a variable number of arguments."], HorizontalRule, Header 3 ("lesson-61-defining-functions", ["unnumbered", "unlisted"], []) [Str "Lesson 6.1: Defining Functions"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Functions"] ("https://kotlinlang.org/docs/functions.html", "")]], [Plain [Str "Matching Python lesson: Lesson 6.1: Defining Functions"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Define and call functions."]], [Plain [Str "Pass parameters and return nothing or a value."]], [Plain [Str "Treat a function as a value."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A function is declared with ", Code ("", [], []) "fun name(parameters): ReturnType { ... }", Str ". Each parameter names its type: ", Code ("", [], []) "fun showTip(bill: Double, tipRate: Double)", Str ". A function with no result returns ", Code ("", [], []) "Unit", Str ", which you usually leave out. A function whose body is one expression can use ", Code ("", [], []) "=", Str ": ", Code ("", [], []) "fun greetName(name: String) = println(\"Hello, $name!\")", Str "."], Para [Str "The ", Emph [Str "parameters"], Str " are the names in the definition and the ", Emph [Str "arguments"], Str " are the values you pass. Arguments are matched to parameters by position."], Para [Str "Functions are values. ", Code ("", [], []) "::showTip", Str " is a reference to the function, which can be stored in a variable and called like the function itself. Top-level functions are declared outside any class and can be called from anywhere in the same package."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun greetUser() {
    println(\"Hello, Kotlin programmer!\")
}

fun greetName(name: String) = println(\"Hello, $name!\")

fun showTip(bill: Double, tipRate: Double) {
    val tip = bill * tipRate
    println(\"Tip: \" + \"%.2f\".format(tip))
    println(\"Total: \" + \"%.2f\".format(bill + tip))
}

fun main() {
    greetUser()
    greetUser()
    greetName(\"Avery\")
    greetName(\"Riley\")
    showTip(24.5, 0.15)

    val reference = ::showTip
    reference(100.0, 0.2)
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Hello, Kotlin programmer!
Hello, Kotlin programmer!
Hello, Avery!
Hello, Riley!
Tip: 3.68
Total: 28.18
Tip: 20.00
Total: 120.00
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing ", Code ("", [], []) "greetUser", Str " without parentheses and expecting the function to run."]], [Plain [Str "Passing arguments in the wrong order, such as ", Code ("", [], []) "showTip(0.15, 24.5)", Str "."]], [Plain [Str "Omitting a parameter's type, which is a compile error."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Call ", Code ("", [], []) "showTip(100.0, 0.2)", Str " yourself and predict both lines."]], [Plain [Str "Write ", Code ("", [], []) "describeStudent(name: String, age: Int)", Str " that prints one sentence."]], [Plain [Str "Call ", Code ("", [], []) "greetName()", Str " with no argument and read the compiler message."]], [Plain [Str "Explain the difference between a parameter and an argument."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Choose function names that read as actions when spoken, such as ", Code ("", [], []) "showTip", Str ". Print complete sentences from a function so the screen reader announces each call's result separately."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can define and call a function."]], [Plain [Str "\9744", Space, Str "I can distinguish parameters from arguments."]], [Plain [Str "\9744", Space, Str "I can write an expression-bodied function."]], [Plain [Str "\9744", Space, Str "I can store a function in a variable."]], [Plain [Str "\9744", Space, Str "I can read a function signature aloud."]]], HorizontalRule, Header 3 ("lesson-62-default-and-named-arguments", ["unnumbered", "unlisted"], []) [Str "Lesson 6.2: Default and Named Arguments"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Functions: default and named arguments"] ("https://kotlinlang.org/docs/functions.html#default-arguments", "")]], [Plain [Str "Matching Python lesson: Lesson 6.2: Passing Arguments"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Give a parameter a default value."]], [Plain [Str "Call a function with named arguments."]], [Plain [Str "Mix positional and named arguments correctly."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Kotlin supports ", Emph [Str "default values"], Str ", written in the parameter list: ", Code ("", [], []) "fun calculateTotal(bill: Double, tipRate: Double = 0.15)", Str ". A caller may leave out an argument that has a default. It also supports ", Emph [Str "named arguments"], Str ": ", Code ("", [], []) "calculateTotal(tipRate = 0.10, bill = 24.5)", Str ". Named arguments make a call read like a sentence and let you give them in any order."], Para [Str "You may mix the two: positional arguments first, then named ones. With the shared bill of 24.50, the total at the default rate 0.15 is 28.18, at 0.20 it is 29.40, and at 0.10 it is 26.95."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun calculateTotal(bill: Double, tipRate: Double = 0.15): Double = bill + bill * tipRate

fun main() {
    println(\"%.2f\".format(calculateTotal(24.5)))
    println(\"%.2f\".format(calculateTotal(24.5, 0.20)))
    println(\"%.2f\".format(calculateTotal(tipRate = 0.10, bill = 24.5)))
    println(\"%.2f\".format(calculateTotal(24.5, tipRate = 0.0)))
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "28.18
29.40
26.95
24.50
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Putting a positional argument after a named one in a way the compiler cannot match."]], [Plain [Str "Changing a default value and forgetting that every caller that omitted it now gets the new value."]], [Plain [Str "Using a very long list of positional parameters instead of named arguments."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the four totals before running."]], [Plain [Str "Add a ", Code ("", [], []) "roundTotal: Boolean = false", Str " parameter and use it."]], [Plain [Str "Call the function with the arguments in a different order using names."]], [Plain [Str "Explain why named arguments help a screen reader user."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Named arguments make a call read as a sentence: 'calculate total, bill equals 24.5, tip rate equals 0.10'. Say the equals signs aloud and check that your screen reader announces them."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write default values."]], [Plain [Str "\9744", Space, Str "I can call with named arguments."]], [Plain [Str "\9744", Space, Str "I can mix positional and named arguments."]], [Plain [Str "\9744", Space, Str "I know defaults apply to omitted arguments."]], [Plain [Str "\9744", Space, Str "I can read a named call aloud."]]], HorizontalRule, Header 3 ("lesson-63-return-values", ["unnumbered", "unlisted"], []) [Str "Lesson 6.3: Return Values"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Functions"] ("https://kotlinlang.org/docs/functions.html", "")]], [Plain [Link ("", [], []) [Str "Null safety"] ("https://kotlinlang.org/docs/null-safety.html", "")]], [Plain [Str "Matching Python lesson: Lesson 6.3: Return Values"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Return a computed value."]], [Plain [Str "Return a nullable result when a value may be missing."]], [Plain [Str "Return several values with a data class."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A function sends a value back with ", Code ("", [], []) "return", Str ", or with ", Code ("", [], []) "=", Str " for a single expression. The return type follows the parameters: ", Code ("", [], []) "fun average(scores: List<Int>): Double?", Str ". A ", Code ("", [], []) "?", Str " after the type means the function may return ", Code ("", [], []) "null", Str "; that is the Kotlin way to say \"no result\", for example the average of an empty list."], Para [Str "The caller must deal with ", Code ("", [], []) "null", Str " before using the value, usually with a check or with ", Code ("", [], []) "?:", Str ". To return several values, return a ", Code ("", [], []) "Pair", Str " or a small data class and destructure it."], Para [Str "The example returns the average of the shared scores, classifies that average, returns a minimum and maximum together, and shows the empty-list case."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "data class ScoreRange(val low: Int, val high: Int)

fun average(scores: List<Int>): Double? {
    if (scores.isEmpty()) return null
    return scores.sum().toDouble() / scores.size
}

fun classify(score: Double): String = when {
    score >= 90 -> \"A\"
    score >= 80 -> \"B\"
    score >= 70 -> \"C\"
    score >= 60 -> \"D\"
    else -> \"F\"
}

fun minMax(scores: List<Int>) = ScoreRange(scores.min(), scores.max())

fun main() {
    val scores = listOf(82, 91, 76, 88)
    val avg = average(scores)
    println(\"Average: $avg\")
    if (avg != null) {
        println(\"Grade for the average: ${classify(avg)}\")
    }
    val (low, high) = minMax(scores)
    println(\"Lowest and highest: $low and $high\")
    println(average(emptyList()))
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Average: 84.25
Grade for the average: B
Lowest and highest: 76 and 91
null
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Printing inside the function and then trying to use the result in a calculation."]], [Plain [Str "Ignoring the ", Code ("", [], []) "null", Str " case and crashing with ", Code ("", [], []) "!!", Str "."]], [Plain [Str "Writing code after a ", Code ("", [], []) "return", Str " in the same block. It never runs."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the four printed lines before running."]], [Plain [Str "Write ", Code ("", [], []) "total(list: List<Int>)", Str " that returns the sum."]], [Plain [Str "Write ", Code ("", [], []) "isPassing(score: Int)", Str " that returns a ", Code ("", [], []) "Boolean", Str "."]], [Plain [Str "Explain how a caller should use a function that returns ", Code ("", [], []) "Double?", Str "."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Return values instead of printing inside logic functions, so the caller prints once and the screen reader announces each result a single time."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can return a value."]], [Plain [Str "\9744", Space, Str "I can return a nullable result."]], [Plain [Str "\9744", Space, Str "I can return several values with a data class."]], [Plain [Str "\9744", Space, Str "I can use a returned value in a calculation."]], [Plain [Str "\9744", Space, Str "I can classify an average with the shared thresholds."]]], HorizontalRule, Header 3 ("lesson-64-functions-with-collections", ["unnumbered", "unlisted"], []) [Str "Lesson 6.4: Functions with Collections"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Collections overview"] ("https://kotlinlang.org/docs/collections-overview.html", "")]], [Plain [Link ("", [], []) [Str "Functions"] ("https://kotlinlang.org/docs/functions.html", "")]], [Plain [Str "Matching Python lesson: Lesson 6.4: Functions with Lists and Dictionaries"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain that a collection argument refers to the same object."]], [Plain [Str "Change a list in a function and protect the original with a copy or a new list."]], [Plain [Str "Process the shared inventory with a function."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Code ("", [], []) "List", Str " or ", Code ("", [], []) "MutableList", Str " passed to a function is a ", Emph [Str "reference"], Str " to the same object. A function that takes a ", Code ("", [], []) "MutableList", Str " can change the caller's list; a function that takes a read-only ", Code ("", [], []) "List", Str " cannot change it through that parameter. Numbers and strings are copied or immutable, so they cannot be changed this way."], Para [Str "To produce a changed list without touching the original, return a ", Emph [Str "new"], Str " list: ", Code ("", [], []) "scoreList + newScore", Str " builds one. Choose the parameter type to say what the function does: ", Code ("", [], []) "MutableList<Int>", Str " means \"I will change this\", ", Code ("", [], []) "List<Int>", Str " means \"I will only read this\"."], Para [Str "The shared inventory is Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25), worth 17.50 in total."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "data class Item(val name: String, val quantity: Int, val unitPrice: Double)

fun addScore(scoreList: MutableList<Int>, newScore: Int) {
    scoreList.add(newScore)
}

fun withScore(scoreList: List<Int>, newScore: Int): List<Int> = scoreList + newScore

fun inventoryValue(inventory: List<Item>): Double =
    inventory.sumOf { it.quantity * it.unitPrice }

fun main() {
    val scores = mutableListOf(82, 91, 76, 88)
    addScore(scores, 95)
    println(scores)

    val longer = withScore(scores, 100)
    println(\"${scores.size} ${longer.size}\")

    val inventory = listOf(
        Item(\"Notebook\", 3, 2.50),
        Item(\"Pencil\", 10, 0.50),
        Item(\"Folder\", 4, 1.25),
    )
    println(\"Total inventory value: \" + \"%.2f\".format(inventoryValue(inventory)))
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "[82, 91, 76, 88, 95]
5 6
Total inventory value: 17.50
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Expecting a function to receive its own copy of a list."]], [Plain [Str "Changing a list inside a function that was meant only to read it."]], [Plain [Str "Declaring a parameter ", Code ("", [], []) "MutableList", Str " when ", Code ("", [], []) "List", Str " is enough, which allows accidental changes."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the three printed lines before running."]], [Plain [Str "Write ", Code ("", [], []) "scalePrices(inventory, factor)", Str " that returns a new list with changed prices and leaves the original unchanged."]], [Plain [Str "Write a version that changes a ", Code ("", [], []) "MutableList<Item>", Str " in place and compare the two designs."]], [Plain [Str "Explain the difference between passing a number and passing a list."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "State aloud before each call whether the function changes its argument, and name it accordingly (", Code ("", [], []) "addScore", Str " changes, ", Code ("", [], []) "withScore", Str " returns a new list). Print the list before and after so that the effect is heard."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I know collections are passed by reference."]], [Plain [Str "\9744", Space, Str "I can change a list in a function."]], [Plain [Str "\9744", Space, Str "I can return a new list instead."]], [Plain [Str "\9744", Space, Str "I can choose ", Code ("", [], []) "List", Str " or ", Code ("", [], []) "MutableList", Str " for a parameter."]], [Plain [Str "\9744", Space, Str "I can total the shared inventory in a function."]]], HorizontalRule, Header 3 ("lesson-65-variable-numbers-of-arguments", ["unnumbered", "unlisted"], []) [Str "Lesson 6.5: Variable Numbers of Arguments"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Functions: variable number of arguments"] ("https://kotlinlang.org/docs/functions.html#variable-number-of-arguments-varargs", "")]], [Plain [Str "Matching Python lesson: Lesson 6.5: Arbitrary Number of Arguments"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write a function with ", Code ("", [], []) "vararg", Str "."]], [Plain [Str "Pass an existing array with the spread operator ", Code ("", [], []) "*", Str "."]], [Plain [Str "Handle the case of no arguments."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A parameter marked ", Code ("", [], []) "vararg", Str " accepts any number of arguments, and inside the function it is an array: ", Code ("", [], []) "vararg scores: Int", Str " is an ", Code ("", [], []) "IntArray", Str ". Pass an existing array with the ", Emph [Str "spread operator"], Str ": ", Code ("", [], []) "average(*list.toIntArray())", Str ". A list must be converted to an array first."], Para [Str "Handle the case of zero arguments explicitly. Dividing a sum by a size of 0 would give a meaningless result, so the example returns ", Code ("", [], []) "null", Str "."], Para [Str "The shared scores 82, 91, 76, 88 average 84.25, and the average of 90 and 80 is 85.0."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun average(vararg scores: Int): Double? =
    if (scores.isEmpty()) null else scores.sum().toDouble() / scores.size

fun describe(label: String, vararg values: Int): String =
    \"$label: ${values.joinToString(\", \")}\"

fun main() {
    println(average(82, 91, 76, 88))
    println(average(90, 80))
    println(average())

    val list = listOf(82, 91, 76, 88)
    println(average(*list.toIntArray()))

    println(describe(\"scores\", 82, 91, 76, 88))
    println(describe(\"nothing\"))
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "84.25
85.0
null
84.25
scores: 82, 91, 76, 88
nothing: 
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Calling ", Code ("", [], []) "average()", Str " with no arguments and dividing by zero."]], [Plain [Str "Passing a list directly to a ", Code ("", [], []) "vararg", Str " parameter instead of spreading an array."]], [Plain [Str "Placing ", Code ("", [], []) "vararg", Str " before other parameters and then needing named arguments for the rest."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict each printed line."]], [Plain [Str "Write ", Code ("", [], []) "maximum(vararg numbers: Int)", Str " that returns the largest or ", Code ("", [], []) "null", Str "."]], [Plain [Str "Write ", Code ("", [], []) "joinWords(separator: String, vararg words: String)", Str "."]], [Plain [Str "Explain what the ", Code ("", [], []) "*", Str " does in a call."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read variadic signatures aloud: 'fun average, open parenthesis, vararg scores colon Int, close parenthesis'. Check that your screen reader announces ", Code ("", [], []) "vararg", Str " and the star."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a ", Code ("", [], []) "vararg", Str " function."]], [Plain [Str "\9744", Space, Str "I can use the spread operator."]], [Plain [Str "\9744", Space, Str "I handle the no-argument case."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "vararg", Str " is an array inside the function."]], [Plain [Str "\9744", Space, Str "I can convert a list with ", Code ("", [], []) "toIntArray()", Str "."]]], HorizontalRule]