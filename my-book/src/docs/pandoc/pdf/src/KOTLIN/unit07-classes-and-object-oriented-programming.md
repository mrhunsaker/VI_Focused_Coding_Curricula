[Header 2 ("unit-7-classes-and-object-oriented-programming", [], []) [Str "Unit 7: Classes and Object-Oriented Programming"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Model the shared inventory item as an object: constructors, methods, inheritance, and composition."], HorizontalRule, Header 3 ("lesson-71-why-learn-about-classes", ["unnumbered", "unlisted"], []) [Str "Lesson 7.1: Why Learn About Classes?"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Classes"] ("https://kotlinlang.org/docs/classes.html", "")]], [Plain [Link ("", [], []) [Str "Visibility modifiers"] ("https://kotlinlang.org/docs/visibility-modifiers.html", "")]], [Plain [Str "Matching Python lesson: Lesson 7.1: Why Learn About Classes?"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain a class as data plus behavior."]], [Plain [Str "Hide a property's setter to protect it."]], [Plain [Str "Describe encapsulation."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "class"], Str " describes what a kind of thing knows (its ", Emph [Str "properties"], Str ") and what it can do (its ", Emph [Str "functions"], Str "). An ", Emph [Str "object"], Str " is one actual thing made from a class. Bundling data with the functions that work on it is called ", Strong [Str "encapsulation"], Str ". The shared example is an inventory ", Emph [Str "item"], Str " with a name, a quantity, and a unit price."], Para [Str "Kotlin lets you protect a property with a ", Emph [Str "private setter"], Str ": ", Code ("", [], []) "var quantity: Int = quantity", Str " followed by ", Code ("", [], []) "private set", Str " on the next line means code outside the class can read ", Code ("", [], []) "quantity", Str " but cannot assign to it. Changes must go through a function such as ", Code ("", [], []) "restock", Str ", which can check them."], Para [Str "Kotlin does not have a ", Code ("", [], []) "new", Str " keyword: you create an object by calling the class like a function, ", Code ("", [], []) "Item(\"Notebook\", 3, 2.50)", Str "."], Para [Str "A Notebook with quantity 3 and unit price 2.50 is worth 7.50. Restocking 2 raises that to 12.50, and a negative restock is refused."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "class Item(val name: String, quantity: Int, val unitPrice: Double) {
    var quantity: Int = quantity
        private set

    fun restock(amount: Int): Boolean {
        if (amount < 0) return false
        quantity += amount
        return true
    }

    fun totalValue(): Double = quantity * unitPrice

    fun describe() {
        println(\"$name: $quantity at ${\"%.2f\".format(unitPrice)} each, value ${\"%.2f\".format(totalValue())}\")
    }
}

fun main() {
    val notebook = Item(\"Notebook\", 3, 2.50)
    notebook.describe()
    println(notebook.restock(2))
    notebook.describe()
    println(notebook.restock(-1))
    println(notebook.quantity)
    // notebook.quantity = 99   // would not compile: the setter is private
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Notebook: 3 at 2.50 each, value 7.50
true
Notebook: 5 at 2.50 each, value 12.50
false
5
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Treating a class as one single thing. A class is a blueprint; each call such as ", Code ("", [], []) "Item(...)", Str " makes a separate object."]], [Plain [Str "Making every property public and changeable, so outside code can put the object into an invalid state."]], [Plain [Str "Looking for a ", Code ("", [], []) "new", Str " keyword, which Kotlin does not have."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the five printed lines before running."]], [Plain [Str "Add a function ", Code ("", [], []) "isLowStock()", Str " that returns true when the quantity is below 5."]], [Plain [Str "Uncomment the assignment, read the compiler message, and restore the comment."]], [Plain [Str "Explain what encapsulation means and why a private setter helps."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Describe a class as a list read in order: the name, then each property, then each function. Reading a class aloud works best by saying 'class Item, open parenthesis, val name colon String...' and listening for the braces that show structure."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain data plus behavior."]], [Plain [Str "\9744", Space, Str "I can use a private setter."]], [Plain [Str "\9744", Space, Str "I can create an object without ", Code ("", [], []) "new", Str "."]], [Plain [Str "\9744", Space, Str "I can describe encapsulation."]], [Plain [Str "\9744", Space, Str "I can read a class definition aloud."]]], HorizontalRule, Header 3 ("lesson-72-creating-classes-and-objects", ["unnumbered", "unlisted"], []) [Str "Lesson 7.2: Creating Classes and Objects"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Classes"] ("https://kotlinlang.org/docs/classes.html", "")]], [Plain [Link ("", [], []) [Str "Exceptions: require"] ("https://kotlinlang.org/docs/exceptions.html", "")]], [Plain [Str "Matching Python lesson: Lesson 7.2: Creating and Using a Class"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Declare a class with a primary constructor."]], [Plain [Str "Validate in an ", Code ("", [], []) "init", Str " block with ", Code ("", [], []) "require", Str "."]], [Plain [Str "Create several objects with the same properties."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A class declares its constructor right after its name: ", Code ("", [], []) "class Item(val name: String, val quantity: Int, val unitPrice: Double)", Str ". Writing ", Code ("", [], []) "val", Str " or ", Code ("", [], []) "var", Str " in front of a constructor parameter makes it a property in one step."], Para [Str "An ", Code ("", [], []) "init", Str " block runs whenever an object is created, so it is the place to check the values. ", Code ("", [], []) "require(condition) { message }", Str " throws an ", Code ("", [], []) "IllegalArgumentException", Str " with the message when the condition is false. An object that cannot be created invalid never needs to be checked again."], Para [Str "The example creates the three shared inventory items. Each has the same properties with different values. A class is a blueprint and each object is one ", Emph [Str "instance"], Str "."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "class Item(val name: String, val quantity: Int, val unitPrice: Double) {
    init {
        require(quantity >= 0) { \"quantity must not be negative\" }
        require(unitPrice >= 0.0) { \"unit price must not be negative\" }
    }
}

fun main() {
    val notebook = Item(\"Notebook\", 3, 2.50)
    val pencil = Item(\"Pencil\", 10, 0.50)
    val folder = Item(\"Folder\", 4, 1.25)

    for (item in listOf(notebook, pencil, folder)) {
        println(\"${item.name}: ${item.quantity} at ${\"%.2f\".format(item.unitPrice)}\")
    }

    val attempt = runCatching { Item(\"Broken\", -1, 1.0) }
    println(attempt.exceptionOrNull()?.message)
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Notebook: 3 at 2.50
Pencil: 10 at 0.50
Folder: 4 at 1.25
quantity must not be negative
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting ", Code ("", [], []) "val", Str " in the constructor, so the parameter is not a property and cannot be read later."]], [Plain [Str "Validating in each caller instead of once in ", Code ("", [], []) "init", Str "."]], [Plain [Str "Catching the ", Code ("", [], []) "IllegalArgumentException", Str " and ignoring it, so the program continues with no object."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create a fourth item with your own values and print it."]], [Plain [Str "Add a rule that the name must not be blank."]], [Plain [Str "Create two items with the same name and different quantities and show that they are separate objects."]], [Plain [Str "Explain what ", Code ("", [], []) "init", Str " does and when it runs."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Say the constructor aloud in order and check that the closing parenthesis and brace match. Print each object on its own line with its name so the output can be matched to the objects by ear."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a primary constructor."]], [Plain [Str "\9744", Space, Str "I can validate with ", Code ("", [], []) "init", Str " and ", Code ("", [], []) "require", Str "."]], [Plain [Str "\9744", Space, Str "I can create several objects."]], [Plain [Str "\9744", Space, Str "I know what an instance is."]], [Plain [Str "\9744", Space, Str "I can read a class header aloud."]]], HorizontalRule, Header 3 ("lesson-73-properties-and-functions", ["unnumbered", "unlisted"], []) [Str "Lesson 7.3: Properties and Functions"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Properties"] ("https://kotlinlang.org/docs/properties.html", "")]], [Plain [Link ("", [], []) [Str "Classes"] ("https://kotlinlang.org/docs/classes.html", "")]], [Plain [Str "Matching Python lesson: Lesson 7.3: Working with Attributes and Methods"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Define a computed property and member functions."]], [Plain [Str "Change properties directly and through functions."]], [Plain [Str "Validate in a function."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "property"], Str " can be stored (", Code ("", [], []) "var quantity", Str ") or ", Emph [Str "computed"], Str ": ", Code ("", [], []) "val totalValue: Double get() = quantity * unitPrice", Str " has no stored value and is calculated each time it is read. Callers use it like any property, without parentheses."], Para [Str "A ", Emph [Str "member function"], Str " works on the object: ", Code ("", [], []) "item.restock(2)", Str ". A function that validates its input protects the object from invalid data. Directly changing a public ", Code ("", [], []) "var", Str " skips that protection, so make a property ", Code ("", [], []) "var", Str " only when any value is acceptable."], Para [Str "The example adds a computed value, a validity check, a restock function, and a describe function to the shared Notebook."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "class Item(val name: String, var quantity: Int, val unitPrice: Double) {
    val totalValue: Double
        get() = quantity * unitPrice

    fun isValid(): Boolean = name.isNotBlank() && quantity >= 0 && unitPrice >= 0.0

    fun restock(amount: Int) {
        if (amount < 0) {
            println(\"Cannot restock a negative amount.\")
            return
        }
        quantity += amount
    }

    fun describe() {
        println(\"$name: $quantity at ${\"%.2f\".format(unitPrice)} each, value ${\"%.2f\".format(totalValue)}\")
    }
}

fun main() {
    val notebook = Item(\"Notebook\", 3, 2.50)
    notebook.describe()
    notebook.restock(2)
    notebook.describe()
    notebook.quantity = 4
    notebook.describe()
    notebook.restock(-1)
    println(notebook.isValid())
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Notebook: 3 at 2.50 each, value 7.50
Notebook: 5 at 2.50 each, value 12.50
Notebook: 4 at 2.50 each, value 10.00
Cannot restock a negative amount.
true
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing ", Code ("", [], []) "totalValue()", Str " with parentheses for a property, or ", Code ("", [], []) "isValid", Str " without them for a function."]], [Plain [Str "Changing a public ", Code ("", [], []) "var", Str " directly and skipping the validation that a function would perform."]], [Plain [Str "Storing a value that can be computed, so it goes out of date when the inputs change."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output of all six calls before running."]], [Plain [Str "Add a function ", Code ("", [], []) "discounted(rate: Double): Double", Str " that returns the value after a discount without changing the item."]], [Plain [Str "Make ", Code ("", [], []) "quantity", Str " have a private setter and see which lines stop compiling."]], [Plain [Str "Explain the difference between a stored and a computed property."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Name functions after actions (", Code ("", [], []) "restock", Str ", ", Code ("", [], []) "describe", Str ") so a call reads as a sentence. Print one line per call, so the screen reader announces the effect of each step in order."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a computed property."]], [Plain [Str "\9744", Space, Str "I can write member functions."]], [Plain [Str "\9744", Space, Str "I can validate in a function."]], [Plain [Str "\9744", Space, Str "I know when to use a private setter."]], [Plain [Str "\9744", Space, Str "I can tell a property from a function when reading."]]], HorizontalRule, Header 3 ("lesson-74-inheritance", ["unnumbered", "unlisted"], []) [Str "Lesson 7.4: Inheritance"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Inheritance"] ("https://kotlinlang.org/docs/inheritance.html", "")]], [Plain [Str "Matching Python lesson: Lesson 7.4: Inheritance"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Declare an ", Code ("", [], []) "open", Str " class and a subclass."]], [Plain [Str "Override a function and call the parent's version."]], [Plain [Str "Explain polymorphism."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Kotlin classes are ", Strong [Str "final by default"], Str ": nothing can inherit from them. Mark a class ", Code ("", [], []) "open", Str " to allow subclasses, and mark each function that may be replaced ", Code ("", [], []) "open", Str " as well. A subclass names its parent after a colon and passes constructor values up: ", Code ("", [], []) "class DiscountedItem(...) : Item(name, quantity, unitPrice)", Str ". A function that replaces a parent's function is marked ", Code ("", [], []) "override", Str ", and ", Code ("", [], []) "super.totalValue()", Str " calls the parent's version."], Para [Emph [Str "Polymorphism"], Str " means that the same function name behaves differently for different classes. Here ", Code ("", [], []) "describe", Str ", written once in ", Code ("", [], []) "Item", Str ", calls ", Code ("", [], []) "totalValue()", Str ", so a ", Code ("", [], []) "DiscountedItem", Str " prints its discounted value automatically."], Para [Str "The example discounts the shared Folder (4 at 1.25) by 20 percent, so its value is 4.00 instead of 5.00."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "open class Item(val name: String, val quantity: Int, val unitPrice: Double) {
    open fun totalValue(): Double = quantity * unitPrice

    fun describe() {
        println(\"$name: $quantity at ${\"%.2f\".format(unitPrice)} each, value ${\"%.2f\".format(totalValue())}\")
    }
}

class DiscountedItem(name: String, quantity: Int, unitPrice: Double, val discountRate: Double) :
    Item(name, quantity, unitPrice) {
    override fun totalValue(): Double = super.totalValue() * (1 - discountRate)
}

fun main() {
    val folder = DiscountedItem(\"Folder\", 4, 1.25, 0.20)
    folder.describe()
    println(folder is Item)

    val items: List<Item> = listOf(Item(\"Notebook\", 3, 2.50), folder)
    for (item in items) println(\"${item.name}: ${\"%.2f\".format(item.totalValue())}\")
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Folder: 4 at 1.25 each, value 4.00
true
Notebook: 7.50
Folder: 4.00
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting ", Code ("", [], []) "open", Str ", so the compiler refuses to let another class inherit or override."]], [Plain [Str "Forgetting ", Code ("", [], []) "override", Str " on a function that replaces a parent's function, which is a compile error."]], [Plain [Str "Using inheritance for a \"has a\" relationship; use composition instead (Lesson 7.5)."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output before running."]], [Plain [Str "Add a subclass ", Code ("", [], []) "PerishableItem", Str " with an ", Code ("", [], []) "expires", Str " property and override ", Code ("", [], []) "describe", Str " by making it ", Code ("", [], []) "open", Str "."]], [Plain [Str "Explain why ", Code ("", [], []) "describe", Str " prints the discounted value without being redefined."]], [Plain [Str "List the order in which Kotlin looks for ", Code ("", [], []) "totalValue", Str " on a ", Code ("", [], []) "DiscountedItem", Str "."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Describe inheritance as an ordered list: the subclass first, then its parent. Speaking the chain aloud ('DiscountedItem, then Item') is clearer than a diagram."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can declare an open class and a subclass."]], [Plain [Str "\9744", Space, Str "I can override a function."]], [Plain [Str "\9744", Space, Str "I can call ", Code ("", [], []) "super", Str "."]], [Plain [Str "\9744", Space, Str "I can explain polymorphism."]], [Plain [Str "\9744", Space, Str "I know classes are final by default."]]], HorizontalRule, Header 3 ("lesson-75-composition", ["unnumbered", "unlisted"], []) [Str "Lesson 7.5: Composition"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Classes"] ("https://kotlinlang.org/docs/classes.html", "")]], [Plain [Str "Matching Python lesson: Lesson 7.5: Instances as Attributes (Composition)"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain composition (\"has a\")."]], [Plain [Str "Hold a list of objects inside another object."]], [Plain [Str "Build an inventory from the shared items."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Emph [Str "Composition"], Str " means that one object contains other objects. An inventory ", Emph [Str "has"], Str " items; it is not a kind of item. Composition is usually simpler and safer than inheritance when objects are related by containment."], Para [Str "The container keeps a private list of its parts and exposes functions that loop over the parts and call each part's own functions, so the container does not need to know how a part works. Keeping the list ", Code ("", [], []) "private", Str " forces other code to use ", Code ("", [], []) "add", Str " and ", Code ("", [], []) "report", Str "."], Para [Str "The example builds an ", Code ("", [], []) "Inventory", Str " with the three shared items and reports each quantity and the total value, 17.50."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["kotlin"], []) "class Item(val name: String, val quantity: Int, val unitPrice: Double) {
    fun totalValue(): Double = quantity * unitPrice
}

class Inventory {
    private val items = mutableListOf<Item>()

    fun add(item: Item) {
        items.add(item)
    }

    fun find(name: String): Item? = items.firstOrNull { it.name == name }

    fun totalValue(): Double = items.sumOf { it.totalValue() }

    fun report() {
        for (item in items) {
            println(\"${item.name}: ${item.quantity}\")
        }
        println(\"Total value: \" + \"%.2f\".format(totalValue()))
    }
}

fun main() {
    val inventory = Inventory()
    inventory.add(Item(\"Notebook\", 3, 2.50))
    inventory.add(Item(\"Pencil\", 10, 0.50))
    inventory.add(Item(\"Folder\", 4, 1.25))
    inventory.report()
    println(inventory.find(\"Pencil\")?.quantity)
    println(inventory.find(\"Eraser\"))
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Notebook: 3
Pencil: 10
Folder: 4
Total value: 17.50
10
null
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using inheritance where a \"has a\" relationship is meant."]], [Plain [Str "Making the list public so other code changes it without going through ", Code ("", [], []) "add", Str "."]], [Plain [Str "Letting the container read each item's properties directly instead of calling the item's functions."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output."]], [Plain [Str "Add ", Code ("", [], []) "remove(name)", Str " to ", Code ("", [], []) "Inventory", Str " and test it."]], [Plain [Str "Add a function that returns the names of items with a quantity below 5."]], [Plain [Str "Explain \"is a\" versus \"has a\" with two examples."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Report the inventory as one labelled line per item and a final total line, so the screen reader reads a complete summary in order."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain composition."]], [Plain [Str "\9744", Space, Str "I can hold a list of objects in an object."]], [Plain [Str "\9744", Space, Str "I can keep a list private."]], [Plain [Str "\9744", Space, Str "I can say \"is a\" versus \"has a\"."]], [Plain [Str "\9744", Space, Str "I can build the shared inventory."]]], HorizontalRule]