[Header 2 ("unit-4-data-structures--lists-and-dictionaries", [], []) [Str "Unit 4: Data Structures — Lists and Dictionaries"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Work with lists, sorting, fixed records, dictionaries, and stable traversal of the shared inventory."], HorizontalRule, Header 3 ("lesson-41-more-on-mutable-lists", ["unnumbered", "unlisted"], []) [Str "Lesson 4.1: More on Mutable Lists"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Collections overview"] ("https://kotlinlang.org/docs/collections-overview.html", "")]], [Plain [Link ("", [], []) [Str "Adding and removing elements"] ("https://kotlinlang.org/docs/collection-write.html", "")]], [Plain [Str "Matching Python lesson: Lesson 4.1: More on Lists"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Add, insert, replace, and remove list items."]], [Plain [Str "Remove by value and by position without confusing them."]], [Plain [Str "Search a list with ", Code ("", [], []) "in", Str " and ", Code ("", [], []) "indexOf", Str "."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Code ("", [], []) "MutableList", Str " changes with ", Code ("", [], []) "add(value)", Str " (append), ", Code ("", [], []) "add(index, value)", Str " (insert and shift), ", Code ("", [], []) "set", Str " or ", Code ("", [], []) "list[i] = value", Str " (replace), ", Code ("", [], []) "remove(value)", Str " (remove the first matching ", Strong [Str "value"], Str "), and ", Code ("", [], []) "removeAt(index)", Str " (remove by ", Strong [Str "position"], Str "). For a list of ", Code ("", [], []) "Int", Str ", ", Code ("", [], []) "remove(76)", Str " removes the number 76, while ", Code ("", [], []) "removeAt(76)", Str " would try to remove position 76. ", Code ("", [], []) "removeAt", Str " returns the removed item."], Para [Code ("", [], []) "value in list", Str " tests membership, and ", Code ("", [], []) "indexOf(value)", Str " returns the position or ", Code ("", [], []) "-1", Str ". These searches look at each item in turn, so they take longer for longer lists."], Para [Str "Avoid ", Code ("", [], []) "removeLast()", Str " in code that must run on several JDK versions: newer JDKs add a method with the same name to ", Code ("", [], []) "List", Str ", and the behavior depends on the JDK. ", Code ("", [], []) "removeAt(lastIndex)", Str " is portable."], Para [Str "The example applies the same operations as the Python course to the shared scores, from [82, 91, 76, 88] to [82, 85, 93, 88]."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun main() {
    val scores = mutableListOf(82, 91, 76, 88)

    scores.add(95)
    scores.add(1, 85)
    scores[2] = 93
    scores.remove(76)
    val last = scores.removeAt(scores.lastIndex)

    println(scores)
    println(\"${scores.size} items; removed $last\")
    println(88 in scores)
    println(scores.indexOf(88))
    println(scores.indexOf(100))
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "[82, 85, 93, 88]
4 items; removed 95
true
3
-1
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Confusing ", Code ("", [], []) "remove(76)", Str " (by value) with ", Code ("", [], []) "removeAt(76)", Str " (by position)."]], [Plain [Str "Removing items inside a ", Code ("", [], []) "for", Str " loop over the same list, which throws ", Code ("", [], []) "ConcurrentModificationException", Str "."]], [Plain [Str "Calling ", Code ("", [], []) "removeLast()", Str " and getting different behavior on different JDKs."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace the list after every operation and write each version as a sentence."]], [Plain [Str "Remove the first score with ", Code ("", [], []) "removeAt(0)", Str " and describe what happens to the others."]], [Plain [Str "Remove every score below 80 safely, using ", Code ("", [], []) "removeAll { ... }", Str "."]], [Plain [Str "Print the position of the first score above 90 with ", Code ("", [], []) "indexOfFirst", Str "."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "After every change, print the whole list on one line so the screen reader reads a complete state in one pass. Say the method names aloud, and notice how ", Code ("", [], []) "remove", Str " and ", Code ("", [], []) "removeAt", Str " sound different."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can add, insert, replace, and remove items."]], [Plain [Str "\9744", Space, Str "I can tell ", Code ("", [], []) "remove", Str " from ", Code ("", [], []) "removeAt", Str "."]], [Plain [Str "\9744", Space, Str "I can search with ", Code ("", [], []) "in", Str " and ", Code ("", [], []) "indexOf", Str "."]], [Plain [Str "\9744", Space, Str "I know why ", Code ("", [], []) "removeLast()", Str " is avoided."]], [Plain [Str "\9744", Space, Str "I can show a list in one line."]]], HorizontalRule, Header 3 ("lesson-42-sorting-and-organizing-lists", ["unnumbered", "unlisted"], []) [Str "Lesson 4.2: Sorting and Organizing Lists"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Ordering"] ("https://kotlinlang.org/docs/collection-ordering.html", "")]], [Plain [Link ("", [], []) [Str "Collections overview"] ("https://kotlinlang.org/docs/collections-overview.html", "")]], [Plain [Str "Matching Python lesson: Lesson 4.2: Organizing Lists"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Sort a list ascending and descending."]], [Plain [Str "Tell ", Code ("", [], []) "sorted()", Str " (a new list) from ", Code ("", [], []) "sort()", Str " (in place)."]], [Plain [Str "Sort by a computed key."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Kotlin offers two families. ", Strong [Str "Returning"], Str " functions leave the original alone and give a new list: ", Code ("", [], []) "sorted()", Str ", ", Code ("", [], []) "sortedDescending()", Str ", ", Code ("", [], []) "sortedBy { ... }", Str ", and ", Code ("", [], []) "reversed()", Str ". ", Strong [Str "In-place"], Str " functions change a ", Code ("", [], []) "MutableList", Str ": ", Code ("", [], []) "sort()", Str ", ", Code ("", [], []) "sortDescending()", Str ", and ", Code ("", [], []) "reverse()", Str ". A read-only ", Code ("", [], []) "List", Str " has only the returning kind."], Para [Code ("", [], []) "sortedBy { it.length }", Str " sorts by a computed key, here the length of each word, and keeps the original order of items with equal keys because the sort is ", Emph [Str "stable"], Str "."], Para [Str "The shared scores sort to 76, 82, 88, 91 in ascending order and 91, 88, 82, 76 in descending order."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "fun main() {
    val scores = mutableListOf(82, 91, 76, 88)

    println(\"Original: $scores\")
    println(\"Ascending: ${scores.sorted()}\")
    println(\"Descending: ${scores.sortedDescending()}\")
    println(\"Still original: $scores\")

    scores.sort()
    println(\"Sorted in place: $scores\")
    scores.reverse()
    println(\"Reversed in place: $scores\")

    val words = listOf(\"pencil\", \"folder\", \"notebook\")
    println(words.sorted())
    println(words.sortedBy { it.length })
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Original: [82, 91, 76, 88]
Ascending: [76, 82, 88, 91]
Descending: [91, 88, 82, 76]
Still original: [82, 91, 76, 88]
Sorted in place: [76, 82, 88, 91]
Reversed in place: [91, 88, 82, 76]
[folder, notebook, pencil]
[pencil, folder, notebook]
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Expecting ", Code ("", [], []) "sorted()", Str " to change the list. It returns a new list."]], [Plain [Str "Calling ", Code ("", [], []) "sort()", Str " on a read-only ", Code ("", [], []) "List", Str ", which does not compile."]], [Plain [Str "Expecting ", Code ("", [], []) "reverse()", Str " to sort. It only flips the current order."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict each printed line before running."]], [Plain [Str "Print the scores in descending order without changing the original."]], [Plain [Str "Sort the words by their last letter with ", Code ("", [], []) "sortedBy", Str "."]], [Plain [Str "Explain the difference between ", Code ("", [], []) "sorted()", Str " and ", Code ("", [], []) "sort()", Str " in two sentences."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print each result on its own labelled line (", Code ("", [], []) "Ascending:", Str ", ", Code ("", [], []) "Descending:", Str "). The first and last numbers are the quickest to check by ear."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can sort ascending and descending."]], [Plain [Str "\9744", Space, Str "I know which functions change the list."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "sortedBy", Str "."]], [Plain [Str "\9744", Space, Str "I can reverse a list."]], [Plain [Str "\9744", Space, Str "I can keep the original order."]]], HorizontalRule, Header 3 ("lesson-43-pairs-triples-and-data-classes", ["unnumbered", "unlisted"], []) [Str "Lesson 4.3: Pairs, Triples, and Data Classes"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Data classes"] ("https://kotlinlang.org/docs/data-classes.html", "")]], [Plain [Link ("", [], []) [Str "Destructuring declarations"] ("https://kotlinlang.org/docs/destructuring-declarations.html", "")]], [Plain [Str "Matching Python lesson: Lesson 4.3: Tuples - Immutable Lists"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Use ", Code ("", [], []) "Pair", Str " and ", Code ("", [], []) "Triple", Str " for small fixed groups."]], [Plain [Str "Declare a data class with ", Code ("", [], []) "val", Str " properties."]], [Plain [Str "Unpack values with destructuring."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Kotlin has no general tuple type. For two or three values, use ", Code ("", [], []) "Pair(a, b)", Str " and ", Code ("", [], []) "Triple(a, b, c)", Str ", whose parts are ", Code ("", [], []) "first", Str ", ", Code ("", [], []) "second", Str ", and ", Code ("", [], []) "third", Str ". For anything you will use more than briefly, a ", Strong [Str "data class"], Str " with named properties is clearer: ", Code ("", [], []) "data class Point(val x: Int, val y: Int)", Str "."], Para [Str "A data class automatically provides ", Code ("", [], []) "toString()", Str ", ", Code ("", [], []) "equals()", Str " (so two points with the same values are equal), ", Code ("", [], []) "copy()", Str " (a new object with some values changed), and ", Emph [Str "destructuring"], Str ": ", Code ("", [], []) "val (x, y) = point", Str ". With ", Code ("", [], []) "val", Str " properties, the object cannot change after it is created, so use ", Code ("", [], []) "copy(y = 10)", Str " to get a changed version."], Para [Str "The shared coordinates are x = 3 and y = 4."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "data class Point(val x: Int, val y: Int)

fun minMax(values: List<Int>): Pair<Int, Int> = Pair(values.min(), values.max())

fun main() {
    val (x, y) = Pair(3, 4)
    println(\"x=$x y=$y\")

    val point = Point(3, 4)
    println(point)
    val moved = point.copy(y = 10)
    println(\"$point -> $moved\")
    println(point == Point(3, 4))

    val (low, high) = minMax(listOf(82, 91, 76, 88))
    println(\"low=$low high=$high\")

    val profile = Triple(\"Avery\", 16, 1.72)
    println(\"${profile.first} ${profile.second} ${profile.third}\")
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "x=3 y=4
Point(x=3, y=4)
Point(x=3, y=4) -> Point(x=3, y=10)
true
low=76 high=91
Avery 16 1.72
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) "var", Str " properties in a data class and then being surprised when values change."]], [Plain [Str "Expecting ", Code ("", [], []) "copy()", Str " to change the original. It returns a new object."]], [Plain [Str "Using ", Code ("", [], []) "Pair", Str " with unclear meanings (", Code ("", [], []) "first", Str ", ", Code ("", [], []) "second", Str ") in code that others must read."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output, then run."]], [Plain [Str "Create a ", Code ("", [], []) "Student", Str " data class for the shared profile and print it."]], [Plain [Str "Use ", Code ("", [], []) "copy", Str " to make a student one year older and print both."]], [Plain [Str "Explain when a data class is a better choice than a ", Code ("", [], []) "Pair", Str "."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Named properties read better aloud than ", Code ("", [], []) "first", Str " and ", Code ("", [], []) "second", Str ". Printing a data class shows its name and every property, so the screen reader announces ", Code ("", [], []) "Point(x=3, y=4)", Str " as a complete sentence."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "Pair", Str " and ", Code ("", [], []) "Triple", Str "."]], [Plain [Str "\9744", Space, Str "I can declare a data class."]], [Plain [Str "\9744", Space, Str "I can destructure values."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "copy()", Str "."]], [Plain [Str "\9744", Space, Str "I can choose between a pair and a data class."]]], HorizontalRule, Header 3 ("lesson-44-maps", ["unnumbered", "unlisted"], []) [Str "Lesson 4.4: Maps"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Map-specific operations"] ("https://kotlinlang.org/docs/map-operations.html", "")]], [Plain [Link ("", [], []) [Str "Collections overview"] ("https://kotlinlang.org/docs/collections-overview.html", "")]], [Plain [Str "Matching Python lesson: Lesson 4.4: Introducing Dictionaries"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create a map and read, add, change, and remove entries."]], [Plain [Str "Handle a missing key with ", Code ("", [], []) "?:", Str "."]], [Plain [Str "Model the shared inventory item with a data class."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Code ("", [], []) "Map", Str " pairs keys with values. ", Code ("", [], []) "mapOf(...)", Str " is read-only and ", Code ("", [], []) "mutableMapOf(...)", Str " can change. Read with ", Code ("", [], []) "map[key]", Str ", which returns a ", Strong [Str "nullable"], Str " value: it is ", Code ("", [], []) "null", Str " when the key is missing. Combine it with the Elvis operator to supply a default: ", Code ("", [], []) "map[key] ?: \"unknown\"", Str "."], Para [Code ("", [], []) "map[key] = value", Str " adds or replaces an entry, ", Code ("", [], []) "remove(key)", Str " deletes one, ", Code ("", [], []) "containsKey(key)", Str " tests for a key, and ", Code ("", [], []) "size", Str " counts the entries. ", Code ("", [], []) "mutableMapOf", Str " keeps insertion order."], Para [Str "A map with values of different types, such as ", Code ("", [], []) "MutableMap<String, Any>", Str ", is flexible but loses type checking. When the fields are known, a data class is safer, so the shared Notebook item is a data class."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "data class Item(val name: String, var quantity: Int, val unitPrice: Double)

fun main() {
    val profile = mutableMapOf<String, Any>(
        \"name\" to \"Avery\",
        \"age\" to 16,
        \"heightM\" to 1.72,
        \"favoriteSubject\" to \"Computer Science\",
    )
    println(profile[\"name\"])
    profile[\"age\"] = 17
    profile[\"gradeLevel\"] = 11
    profile.remove(\"heightM\")
    println(profile)
    println(profile[\"heightM\"])
    println(profile[\"heightM\"] ?: \"unknown\")
    println(profile.containsKey(\"gradeLevel\"))

    val item = Item(\"Notebook\", 3, 2.50)
    item.quantity += 2
    println(item)
    println(\"Stock value: ${item.quantity * item.unitPrice}\")
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Avery
{name=Avery, age=17, favoriteSubject=Computer Science, gradeLevel=11}
null
unknown
true
Item(name=Notebook, quantity=5, unitPrice=2.5)
Stock value: 12.5
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using a missing key and expecting an error. The result is ", Code ("", [], []) "null", Str "."]], [Plain [Str "Using ", Code ("", [], []) "!!", Str " on a map lookup, which crashes when the key is missing."]], [Plain [Str "Storing mixed types in ", Code ("", [], []) "Map<String, Any>", Str " and then needing casts everywhere."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed lines before running."]], [Plain [Str "Add a ", Code ("", [], []) "discount", Str " key to the item as a data class property and print the discounted value."]], [Plain [Str "Remove ", Code ("", [], []) "favoriteSubject", Str " and show what the lookup returns."]], [Plain [Str "Explain why a data class is safer than ", Code ("", [], []) "Map<String, Any>", Str " for a record."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print one entry per line when you need to read a map, because a one-line ", Code ("", [], []) "{a=1, b=2}", Str " is hard to navigate. Choose key names that read well aloud, such as ", Code ("", [], []) "unitPrice", Str "."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can create and change a map."]], [Plain [Str "\9744", Space, Str "I know a lookup returns a nullable value."]], [Plain [Str "\9744", Space, Str "I can supply a default with ", Code ("", [], []) "?:", Str "."]], [Plain [Str "\9744", Space, Str "I can model an item with a data class."]], [Plain [Str "\9744", Space, Str "I can test for a key."]]], HorizontalRule, Header 3 ("lesson-45-traversing-maps", ["unnumbered", "unlisted"], []) [Str "Lesson 4.5: Traversing Maps"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Map-specific operations"] ("https://kotlinlang.org/docs/map-operations.html", "")]], [Plain [Link ("", [], []) [Str "Collections overview"] ("https://kotlinlang.org/docs/collections-overview.html", "")]], [Plain [Str "Matching Python lesson: Lesson 4.5: Looping Through Dictionaries"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Visit keys, values, and key-value pairs."]], [Plain [Str "Explain which maps keep insertion order."]], [Plain [Str "Produce sorted output and total the shared inventory."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "for (key in map.keys)", Str " visits keys, ", Code ("", [], []) "for (value in map.values)", Str " visits values, and ", Code ("", [], []) "for ((key, value) in map)", Str " visits pairs with destructuring."], Para [Str "Order matters for readable output. ", Code ("", [], []) "mutableMapOf", Str ", ", Code ("", [], []) "linkedMapOf", Str ", and ", Code ("", [], []) "mapOf", Str " keep ", Strong [Str "insertion order"], Str ", so output is stable. ", Code ("", [], []) "hashMapOf", Str " makes no promise about order. To list keys alphabetically, use ", Code ("", [], []) "toSortedMap()", Str "."], Para [Code ("", [], []) "sumOf { ... }", Str " adds a computed number for every element, which is the compact way to total the shared inventory: Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25) are worth 7.50 + 5.00 + 5.00 = 17.50."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "data class Stock(val quantity: Int, val unitPrice: Double)

fun main() {
    val inventory = linkedMapOf(
        \"Notebook\" to Stock(3, 2.50),
        \"Pencil\" to Stock(10, 0.50),
        \"Folder\" to Stock(4, 1.25),
    )

    println(\"Keys:\")
    for (name in inventory.keys) println(name)

    println(\"Quantities:\")
    for (stock in inventory.values) println(stock.quantity)

    var totalValue = 0.0
    for ((name, stock) in inventory) {
        val lineValue = stock.quantity * stock.unitPrice
        println(\"$name: ${stock.quantity} in stock, value ${\"%.2f\".format(lineValue)}\")
        totalValue += lineValue
    }
    println(\"Total inventory value: ${\"%.2f\".format(totalValue)}\")

    println(inventory.toSortedMap().keys)
    println(inventory.values.sumOf { it.quantity * it.unitPrice })
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
[Folder, Notebook, Pencil]
17.5
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using a ", Code ("", [], []) "HashMap", Str " and expecting the same order every run."]], [Plain [Str "Adding or removing entries while looping over the map, which throws ", Code ("", [], []) "ConcurrentModificationException", Str "."]], [Plain [Str "Forgetting the parentheses in ", Code ("", [], []) "for ((name, stock) in inventory)", Str " and iterating over entries without unpacking them."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the example and write the three key-value lines in order."]], [Plain [Str "Print only the items with a quantity below 5."]], [Plain [Str "Print the items from the highest line value to the lowest."]], [Plain [Str "Explain how ", Code ("", [], []) "toSortedMap()", Str " differs from the default order."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Printing each inventory line as one sentence lets the screen reader announce the name, quantity, and value together. Because the order is stable, you can learn it and compare runs by ear."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can visit keys, values, and pairs."]], [Plain [Str "\9744", Space, Str "I know which maps keep insertion order."]], [Plain [Str "\9744", Space, Str "I can sort keys."]], [Plain [Str "\9744", Space, Str "I can total with ", Code ("", [], []) "sumOf", Str "."]], [Plain [Str "\9744", Space, Str "I can total the shared inventory."]]], HorizontalRule]