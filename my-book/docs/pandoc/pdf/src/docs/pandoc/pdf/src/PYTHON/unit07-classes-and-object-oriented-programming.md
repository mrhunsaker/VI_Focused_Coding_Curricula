[Header 2 ("unit-7-classes-and-object-oriented-programming", [], []) [Str "Unit 7: Classes and Object-Oriented Programming"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Strong [Str "Compatibility:"], Str " All examples target Python 3.12 and newer; they avoid syntax and standard-library APIs introduced after Python 3.12."], Para [Str "This unit introduces the fundamental concepts of Object-Oriented Programming (OOP) in Python, focusing on defining and using classes, attributes, methods, and inheritance."], Para [Strong [Str "Objectives:"]], BulletList [[Plain [Str "Define and instantiate classes."]], [Plain [Str "Work with attributes and methods."]], [Plain [Str "Understand inheritance and composition."]]], HorizontalRule, Header 3 ("lesson-71-why-learn-about-classes", ["unnumbered", "unlisted"], []) [Str "Lesson 7.1: Why Learn About Classes?"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 4, pages 65–67; Chapter 10, pages 247–248"]], [Plain [Str "Matthes: Chapter 9, page 157"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the basic idea of Object-Oriented Programming."]], [Plain [Str "Describe a class as a blueprint and an object as an instance."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "class"], Str " describes what a kind of thing knows (its ", Emph [Str "attributes"], Str ") and what it can do (its ", Emph [Str "methods"], Str "). An ", Emph [Str "object"], Str " is one actual thing made from a class. Bundling data with the functions that work on it is called ", Strong [Str "encapsulation"], Str ", and it keeps related code together so a change in one place does not break unrelated code."], Header 5 ("classes-as-blueprints", ["unnumbered", "unlisted"], []) [Str "Classes as Blueprints"], Para [Str "A ", Strong [Str "class"], Str " is a blueprint or template for creating objects. An ", Strong [Str "object"], Str " is a concrete instance created from that blueprint."], Para [Strong [Str "Analogy:"], Str " An \"Item\" class defines that every inventory item has a ", Code ("", [], []) "name", Str ", a ", Code ("", [], []) "quantity", Str ", and a ", Code ("", [], []) "unit_price", Str " (attributes) and can report its ", Code ("", [], []) "total_value()", Str " (a method). A Notebook and a Pencil are two separate ", Strong [Str "objects"], Str " of the same \"Item\" class. This course models the same inventory item in every language."], Header 5 ("key-oop-concepts", ["unnumbered", "unlisted"], []) [Str "Key OOP Concepts"], BulletList [[Plain [Strong [Str "Encapsulation"], Str " — Bundling data and methods into a single unit."]], [Plain [Strong [Str "Abstraction"], Str " — Hiding complexity from the outside."]], [Plain [Strong [Str "Inheritance"], Str " — New class reuses functionality of existing class."]], [Plain [Strong [Str "Polymorphism"], Str " — Same method name behaves differently for different classes."]]], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "A student profile kept as loose variables is easy to mix up. As an object, the same data and the operations on it travel together:"], CodeBlock ("", ["python"], []) "class Item:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        return self.quantity * self.unit_price


notebook = Item(\"Notebook\", 3, 2.50)
print(notebook.name, notebook.total_value())
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output of example 1:"], CodeBlock ("", [""], []) "Notebook 7.5
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Treating a class as one single thing. A class is a blueprint, and each call such as ", Code ("", [], []) "Item(...)", Str " makes a separate object."]], [Plain [Str "Putting unrelated data into one class so that it has no clear purpose."]], [Plain [Str "Skipping the design step and creating classes before knowing what data and operations are needed."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "List the attributes and methods of a ", Code ("", [], []) "Student", Str " class for the shared profile (Avery, 16, 1.72, Computer Science)."]], [Plain [Str "Describe in two sentences how a class differs from an object, using ", Code ("", [], []) "Item", Str " and ", Code ("", [], []) "notebook", Str "."]], [Plain [Str "Name three real things and for each write one attribute and one method."]], [Plain [Str "Explain what encapsulation means and why it helps when a program grows."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Describe a class as a list read in order: its name, then its attributes, then its methods. Reading a class definition aloud works best by saying 'class Item, colon, define init, open parenthesis, self, comma, name...' and listening for the colons and indentation that show structure."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the basic idea of Object-Oriented Programming."]], [Plain [Str "\9744", Space, Str "I can describe a class as a blueprint and an object as an instance."]]], HorizontalRule, Header 3 ("lesson-72-creating-and-using-a-class", ["unnumbered", "unlisted"], []) [Str "Lesson 7.2: Creating and Using a Class"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 10, pages 248–254"]], [Plain [Str "Matthes: Chapter 9, pages 158–162"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Define a basic Python class."]], [Plain [Str "Define the ", Code ("", [], []) "__init__", Str " method within a class."]], [Plain [Str "Understand the purpose of the ", Code ("", [], []) "self", Str " parameter."]], [Plain [Str "Create an instance (object) of a class."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("class-syntax", ["unnumbered", "unlisted"], []) [Str "Class Syntax"], Para [Str "The ", Code ("", [], []) "__init__()", Str " method runs automatically when a new object is created. ", Code ("", [], []) "self", Str " refers to the specific instance being created. Each of the three objects above has the same fields (", Code ("", [], []) "name", Str ", ", Code ("", [], []) "quantity", Str ", ", Code ("", [], []) "unit_price", Str ") with different values. Keeping the attributes inside the object, and changing them only through methods, is called ", Strong [Str "encapsulation"], Str "."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "class Item:
    \"\"\"An inventory item with a name, a quantity, and a unit price.\"\"\"

    def __init__(self, name, quantity, unit_price):
        \"\"\"Initialize the item's attributes.\"\"\"
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price


notebook = Item(\"Notebook\", 3, 2.50)
pencil = Item(\"Pencil\", 10, 0.50)
folder = Item(\"Folder\", 4, 1.25)

print(f\"{notebook.name}: {notebook.quantity} at {notebook.unit_price}\")
print(f\"{pencil.name}: {pencil.quantity} at {pencil.unit_price}\")
print(f\"{folder.name}: {folder.quantity} at {folder.unit_price}\")
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Notebook: 3 at 2.5
Pencil: 10 at 0.5
Folder: 4 at 1.25
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting ", Code ("", [], []) "self", Str " as the first parameter of ", Code ("", [], []) "__init__", Str ", which raises a ", Code ("", [], []) "TypeError", Str " when an object is created."]], [Plain [Str "Writing ", Code ("", [], []) "name = name", Str " instead of ", Code ("", [], []) "self.name = name", Str ", so the value is lost when ", Code ("", [], []) "__init__", Str " ends."]], [Plain [Str "Writing ", Code ("", [], []) "__init__", Str " with one underscore on each side, so it is not recognized."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create a fourth item with your own values and print its fields."]], [Plain [Str "Add a check in ", Code ("", [], []) "__init__", Str " that rejects a negative quantity by printing a message."]], [Plain [Str "Create two items with the same name and different quantities and show that changing one does not change the other."]], [Plain [Str "Explain what ", Code ("", [], []) "self", Str " refers to in your own words."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Say the double underscores aloud ('dunder init') and confirm that your screen reader announces them, because ", Code ("", [], []) "_init_", Str " with a single underscore fails silently. Print each object on its own line with its name, so the output can be matched to the objects by ear."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can define a basic Python class."]], [Plain [Str "\9744", Space, Str "I can define the ", Code ("", [], []) "__init__", Str " method within a class."]], [Plain [Str "\9744", Space, Str "I understand the purpose of the ", Code ("", [], []) "self", Str " parameter."]], [Plain [Str "\9744", Space, Str "I can create an instance (object) of a class."]]], HorizontalRule, Header 3 ("lesson-73-working-with-attributes-and-methods", ["unnumbered", "unlisted"], []) [Str "Lesson 7.3: Working with Attributes and Methods"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 9, pages 162–166"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Access an object's attributes using dot notation."]], [Plain [Str "Define and call methods within a class."]], [Plain [Str "Use a method to change an object's attribute."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("calling-methods", ["unnumbered", "unlisted"], []) [Str "Calling Methods"], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "class Item:
    \"\"\"An inventory item with a name, a quantity, and a unit price.\"\"\"

    def __init__(self, name, quantity, unit_price):
        \"\"\"Initialize the item's attributes.\"\"\"
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        \"\"\"Return quantity multiplied by unit price.\"\"\"
        return self.quantity * self.unit_price

    def is_valid(self):
        \"\"\"An item is valid if it has a name and non-negative numbers.\"\"\"
        return bool(self.name) and self.quantity >= 0 and self.unit_price >= 0

    def restock(self, amount):
        \"\"\"Add stock; reject a negative amount.\"\"\"
        if amount < 0:
            print(\"Cannot restock a negative amount.\")
            return
        self.quantity += amount

    def describe(self):
        print(f\"{self.name}: {self.quantity} at {self.unit_price:.2f} each, \"
              f\"value {self.total_value():.2f}\")


notebook = Item(\"Notebook\", 3, 2.50)
notebook.describe()
notebook.restock(2)          # method-based modification
notebook.describe()
notebook.quantity = 4        # direct attribute modification
notebook.describe()
notebook.restock(-1)         # validation message
print(notebook.is_valid())
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Notebook: 3 at 2.50 each, value 7.50
Notebook: 5 at 2.50 each, value 12.50
Notebook: 4 at 2.50 each, value 10.00
Cannot restock a negative amount.
True
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Calling a method without parentheses (", Code ("", [], []) "notebook.describe", Str "), which refers to the method but does not run it."]], [Plain [Str "Changing an attribute directly and skipping the validation that a method would have performed."]], [Plain [Str "Forgetting ", Code ("", [], []) "self.", Str " when a method uses an attribute, which raises a ", Code ("", [], []) "NameError", Str "."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output of each call in the example before running it."]], [Plain [Str "Add a method ", Code ("", [], []) "discount(rate)", Str " that returns the value after a discount without changing the item."]], [Plain [Str "Call ", Code ("", [], []) "restock(-1)", Str " and read the message. Then change the method to reject zero as well."]], [Plain [Str "Explain the difference between changing ", Code ("", [], []) "quantity", Str " directly and calling ", Code ("", [], []) "restock", Str "."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Name methods after actions (", Code ("", [], []) "restock", Str ", ", Code ("", [], []) "describe", Str ") so the call reads as a sentence. Print one line per method call, so a screen reader announces the effect of every step in order."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can access an object's attributes using dot notation."]], [Plain [Str "\9744", Space, Str "I can define and call methods within a class."]], [Plain [Str "\9744", Space, Str "I can use a method to change an object's attribute."]]], HorizontalRule, Header 3 ("lesson-74-inheritance", ["unnumbered", "unlisted"], []) [Str "Lesson 7.4: Inheritance"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 12, pages 351–352"]], [Plain [Str "Matthes: Chapter 9, pages 167–170"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Define a child class that inherits from a parent class."]], [Plain [Str "Use ", Code ("", [], []) "super().__init__()", Str " to properly initialize inherited attributes."]], [Plain [Str "Add new attributes and methods to a child class."]], [Plain [Str "Override a parent method in a child class."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("creating-a-child-class", ["unnumbered", "unlisted"], []) [Str "Creating a Child Class"], Header 5 ("super-function", ["unnumbered", "unlisted"], []) [Code ("", [], []) "super()", Str " Function"], Para [Code ("", [], []) "super().__init__()", Str " calls the parent class's ", Code ("", [], []) "__init__()", Str " method, ensuring inherited attributes are properly initialized. In the example, ", Code ("", [], []) "DiscountedItem", Str " overrides ", Code ("", [], []) "total_value()", Str "; the inherited ", Code ("", [], []) "describe()", Str " automatically uses the new version. This is ", Strong [Str "polymorphism"], Str ": the same method name behaves differently for different classes."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "class Item:
    \"\"\"An inventory item with a name, a quantity, and a unit price.\"\"\"

    def __init__(self, name, quantity, unit_price):
        \"\"\"Initialize the item's attributes.\"\"\"
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        return self.quantity * self.unit_price

    def describe(self):
        print(f\"{self.name}: {self.quantity} at {self.unit_price:.2f} each, \"
              f\"value {self.total_value():.2f}\")


class DiscountedItem(Item):
    \"\"\"An item sold at a discount; inherits from Item.\"\"\"

    def __init__(self, name, quantity, unit_price, discount_rate):
        super().__init__(name, quantity, unit_price)   # Call parent's __init__
        self.discount_rate = discount_rate

    def total_value(self):                              # Override
        return super().total_value() * (1 - self.discount_rate)


folder = DiscountedItem(\"Folder\", 4, 1.25, 0.20)
folder.describe()        # inherited describe() calls the overridden total_value()
print(isinstance(folder, Item))
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Folder: 4 at 1.25 each, value 4.00
True
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to call ", Code ("", [], []) "super().__init__()", Str ", so the parent's attributes are never created."]], [Plain [Str "Overriding a method but changing what it returns, so code that uses the parent version breaks."]], [Plain [Str "Using inheritance for a \"has a\" relationship; use composition (Lesson 7.5) instead."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed value and the final ", Code ("", [], []) "True", Str " of the example before running it."]], [Plain [Str "Add a subclass ", Code ("", [], []) "PerishableItem", Str " with an ", Code ("", [], []) "expires", Str " attribute and override ", Code ("", [], []) "describe", Str "."]], [Plain [Str "Explain why ", Code ("", [], []) "describe", Str " prints the discounted value without being redefined."]], [Plain [Str "List the lookup order Python uses to find ", Code ("", [], []) "describe", Str " for a ", Code ("", [], []) "DiscountedItem", Str "."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Describe inheritance as an ordered list: the object's own class first, then its parent. Speaking the chain aloud ('DiscountedItem, then Item') is clearer than a diagram."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can define a child class that inherits from a parent class."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "super().__init__()", Str " to properly initialize inherited attributes."]], [Plain [Str "\9744", Space, Str "I can add new attributes and methods to a child class."]], [Plain [Str "\9744", Space, Str "I can override a parent method in a child class."]]], HorizontalRule, Header 3 ("lesson-75-instances-as-attributes-composition", ["unnumbered", "unlisted"], []) [Str "Lesson 7.5: Instances as Attributes (Composition)"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 9 (Classes), the section on instances as attributes"]], [Plain [Str "Zelle: Chapter 10 (Defining Classes)"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the concept of composition in OOP."]], [Plain [Str "Create an instance of one class and assign it as an attribute of another."]], [Plain [Str "Access attributes and methods of a nested object."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("composition--has-a-relationship", ["unnumbered", "unlisted"], []) [Str "Composition — \"Has-A\" Relationship"], Para [Str "Instead of inheriting, a class ", Strong [Str "contains an instance of another class"], Str " as an attribute."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "class Item:
    \"\"\"An inventory item with a name, a quantity, and a unit price.\"\"\"

    def __init__(self, name, quantity, unit_price):
        \"\"\"Initialize the item's attributes.\"\"\"
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        return self.quantity * self.unit_price


class Inventory:
    \"\"\"An Inventory HAS-A list of Item objects (composition).\"\"\"

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total_value(self):
        return sum(item.total_value() for item in self.items)

    def report(self):
        for item in self.items:
            print(f\"{item.name}: {item.quantity}\")
        print(f\"Total value: {self.total_value():.2f}\")


inventory = Inventory()
inventory.add(Item(\"Notebook\", 3, 2.50))
inventory.add(Item(\"Pencil\", 10, 0.50))
inventory.add(Item(\"Folder\", 4, 1.25))
inventory.report()
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Notebook: 3
Pencil: 10
Folder: 4
Total value: 17.50
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using inheritance where a \"has a\" relationship is meant."]], [Plain [Str "Letting the container reach into each item's attributes instead of calling the item's own methods."]], [Plain [Str "Creating the list in a default argument or at class level, so every ", Code ("", [], []) "Inventory", Str " shares one list."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output of the example."]], [Plain [Str "Add ", Code ("", [], []) "Inventory.find(name)", Str " that returns the item with that name or ", Code ("", [], []) "None", Str "."]], [Plain [Str "Add ", Code ("", [], []) "Inventory.remove(name)", Str " and test it."]], [Plain [Str "Explain the difference between \"is a\" and \"has a\" with two examples."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Report the inventory as one labelled line per item and a final total line, so a screen reader reads a complete summary in order."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the concept of composition in OOP."]], [Plain [Str "\9744", Space, Str "I can create an instance of one class and assign it as an attribute of another."]], [Plain [Str "\9744", Space, Str "I can access attributes and methods of a nested object."]]], HorizontalRule]