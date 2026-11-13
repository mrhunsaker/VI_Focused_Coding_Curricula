[Header 2 ("unit-7-classes-and-object-oriented-programming", [], []) [Str "Unit 7: Classes and Object-Oriented Programming"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops classes and object-oriented programming through the same shared problem contexts and assessment expectations used across the general-purpose language tracks, expressed with Java 25 syntax, APIs, and static typing."], Para [Strong [Str "Unit objectives:"], Str " explain the core concepts, write and test complete Java programs, diagnose errors, and apply the ideas to accessible projects."], Header 3 ("lesson-71-why-learn-about-classes", ["unnumbered", "unlisted"], []) [Str "Lesson 7.1: Why Learn About Classes?"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 7.1: Why Learn About Classes?"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain a class as data plus behavior."]], [Plain [Str "Hide fields with ", Code ("", [], []) "private", Str " and change them only through methods."]], [Plain [Str "Describe encapsulation."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "class"], Str " describes what a kind of thing knows (its ", Emph [Str "fields"], Str ") and what it can do (its ", Emph [Str "methods"], Str "). An ", Emph [Str "object"], Str " is one actual thing made from a class with ", Code ("", [], []) "new", Str ". Bundling data with the methods that work on it is called ", Strong [Str "encapsulation"], Str ". The shared example is an inventory ", Emph [Str "item"], Str " with a name, a quantity, and a unit price."], Para [Str "Marking a field ", Code ("", [], []) "private", Str " means only code inside the class can read or change it. Other code uses methods such as ", Code ("", [], []) "getQuantity()", Str " and ", Code ("", [], []) "restock(amount)", Str ", and ", Code ("", [], []) "restock", Str " can refuse invalid changes. ", Code ("", [], []) "final", Str " on a field means it is assigned once, in the constructor."], Para [Str "A source file may contain several classes, but only one may be ", Code ("", [], []) "public", Str " and it must match the file name. The helper class ", Code ("", [], []) "Item", Str " below is a normal, package-private class in the same file."], Para [Str "A Notebook with quantity 3 and unit price 2.50 is worth 7.50. Restocking 2 raises that to 12.50, and a negative restock is refused."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.Locale;

class Item {
    private final String name;
    private int quantity;
    private final double unitPrice;

    Item(String name, int quantity, double unitPrice) {
        this.name = name;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    boolean restock(int amount) {
        if (amount < 0) {
            return false;
        }
        quantity += amount;
        return true;
    }

    int getQuantity() {
        return quantity;
    }

    double totalValue() {
        return quantity * unitPrice;
    }

    void describe() {
        System.out.println(name + \": \" + quantity + \" at \" + String.format(Locale.US, \"%.2f\", unitPrice)
            + \" each, value \" + String.format(Locale.US, \"%.2f\", totalValue()));
    }
}

public class Lesson_7_1 {
    public static void main(String[] args) {
        Item notebook = new Item(\"Notebook\", 3, 2.50);
        notebook.describe();
        System.out.println(notebook.restock(2));
        notebook.describe();
        System.out.println(notebook.restock(-1));
        System.out.println(notebook.getQuantity());
        // notebook.quantity = 99;   // would not compile: the field is private
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating why learn about classes?. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Exposing mutable fields and allowing callers to bypass class invariants."]], [Plain [Str "Using inheritance for a has-a relationship or failing to call the appropriate superclass constructor."]], [Plain [Str "Confusing an overridden method with an overloaded method, or omitting @Override when overriding."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Model one shared course entity with fields, constructor validation, and behavior methods."]], [Plain [Str "Attempt an invalid state transition and verify encapsulation prevents it."]], [Plain [Str "Demonstrate a true is-a relationship with overriding and runtime dispatch."]], [Plain [Str "Replace an artificial inheritance relationship with composition and compare coupling."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]], Header 3 ("lesson-72-creating-and-using-a-class", ["unnumbered", "unlisted"], []) [Str "Lesson 7.2: Creating and Using a Class"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 documentation"] ("https://docs.oracle.com/en/java/", ""), Str "."]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", ""), Str "."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the purpose and vocabulary of creating and using a class."]], [Plain [Str "Apply the relevant Java syntax and APIs in a small, complete program."]], [Plain [Str "Compile, run, inspect, and adapt the example using keyboard-accessible tools."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "This lesson develops creating and using a class through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Objects combine state and behavior. Encapsulation protects invariants, constructors establish valid initial state, inheritance models a genuine is-a relationship, and composition models has-a collaboration. Prefer interfaces and composition when they reduce coupling."], Para [Str "Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "public class Lesson_7_2 {
    public static void main(String[] args) {
        Student student = new Student(\"Avery\");
        student.enroll();
        System.out.println(student.name + \": \" + student.active);
        }
        static class Student {
            String name;
            boolean active;
            Student(String name) { this.name = name; }
            void enroll() { active = true; }
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating creating and using a class. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Exposing mutable fields and allowing callers to bypass class invariants."]], [Plain [Str "Using inheritance for a has-a relationship or failing to call the appropriate superclass constructor."]], [Plain [Str "Confusing an overridden method with an overloaded method, or omitting @Override when overriding."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Model one shared course entity with fields, constructor validation, and behavior methods."]], [Plain [Str "Attempt an invalid state transition and verify encapsulation prevents it."]], [Plain [Str "Demonstrate a true is-a relationship with overriding and runtime dispatch."]], [Plain [Str "Replace an artificial inheritance relationship with composition and compare coupling."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]], Header 3 ("lesson-73-working-with-attributes-and-methods", ["unnumbered", "unlisted"], []) [Str "Lesson 7.3: Working with Attributes and Methods"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 documentation"] ("https://docs.oracle.com/en/java/", ""), Str "."]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", ""), Str "."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the purpose and vocabulary of working with attributes and methods."]], [Plain [Str "Apply the relevant Java syntax and APIs in a small, complete program."]], [Plain [Str "Compile, run, inspect, and adapt the example using keyboard-accessible tools."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "This lesson develops working with attributes and methods through Java's class-based structure and standard library. Identify the input, output, state changes, and relevant type constraints before coding. Keep declarations local where possible, separate computation from presentation, and state preconditions and postconditions. Objects combine state and behavior. Encapsulation protects invariants, constructors establish valid initial state, inheritance models a genuine is-a relationship, and composition models has-a collaboration. Prefer interfaces and composition when they reduce coupling."], Para [Str "Java is statically typed and class-based. Local variables have declared or inferred compile-time types, reference values may be null, and methods and fields are governed by access and scope rules. The compiler checks syntax and type compatibility before execution; runtime behavior still requires testing. Follow Java naming conventions, use explicit imports in beginner work, and prefer small methods with clear contracts."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "public class Lesson_7_3 {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(100.0);
        account.deposit(25.0);
        System.out.printf(\"balance=%.2f%n\", account.balance());
        }
        static class BankAccount {
            private double balance;
            BankAccount(double opening) { if (opening < 0) throw new IllegalArgumentException(); balance = opening; }
            void deposit(double amount) { if (amount <= 0) throw new IllegalArgumentException(); balance += amount; }
            double balance() { return balance; }
    }
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Notebook: 3 at 2.50 each, value 7.50
Notebook: 5 at 2.50 each, value 12.50
Notebook: 4 at 2.50 each, value 10.00
Cannot restock a negative amount.
true
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting ", Code ("", [], []) "@Override", Str ", so a misspelled ", Code ("", [], []) "tostring()", Str " silently becomes a new method."]], [Plain [Str "Giving a field a public setter that skips the validation the object needs."]], [Plain [Str "Storing a value that can be computed, so it goes out of date when the inputs change."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output of all six lines before running."]], [Plain [Str "Add a method ", Code ("", [], []) "discounted(double rate)", Str " that returns the value after a discount without changing the item."]], [Plain [Str "Remove the ", Code ("", [], []) "setQuantity", Str " method and see which lines stop compiling."]], [Plain [Str "Explain why ", Code ("", [], []) "toString", Str " is better than printing fields one by one."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Name methods after actions (", Code ("", [], []) "restock", Str ") so a call reads as a sentence. Printing an object with a good ", Code ("", [], []) "toString", Str " gives the screen reader one complete line per object."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write getters and a computed method."]], [Plain [Str "\9744", Space, Str "I can validate in a method."]], [Plain [Str "\9744", Space, Str "I can override ", Code ("", [], []) "toString", Str "."]], [Plain [Str "\9744", Space, Str "I know why ", Code ("", [], []) "@Override", Str " helps."]], [Plain [Str "\9744", Space, Str "I can tell a stored from a computed value."]]], HorizontalRule, Header 3 ("lesson-74-inheritance", ["unnumbered", "unlisted"], []) [Str "Lesson 7.4: Inheritance"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 7.4: Inheritance"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Declare a subclass with ", Code ("", [], []) "extends", Str "."]], [Plain [Str "Override a method and call the parent's version with ", Code ("", [], []) "super", Str "."]], [Plain [Str "Explain polymorphism."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A subclass is declared with ", Code ("", [], []) "extends", Str ": ", Code ("", [], []) "class DiscountedItem extends Item", Str ". Its constructor must call the parent's constructor first with ", Code ("", [], []) "super(...)", Str ", which sets up the inherited fields. A method that replaces the parent's method is marked ", Code ("", [], []) "@Override", Str ", and ", Code ("", [], []) "super.totalValue()", Str " calls the parent's version. A class marked ", Code ("", [], []) "final", Str " cannot be extended, and a ", Code ("", [], []) "private", Str " field of the parent is not directly visible to the subclass."], Para [Emph [Str "Polymorphism"], Str " means the same method call behaves differently for different classes. A variable of type ", Code ("", [], []) "Item", Str " can refer to a ", Code ("", [], []) "DiscountedItem", Str ", and calling ", Code ("", [], []) "totalValue()", Str " runs the discounted version. ", Code ("", [], []) "describe", Str " is written once in ", Code ("", [], []) "Item", Str " and calls ", Code ("", [], []) "totalValue()", Str ", so it prints the discounted value automatically."], Para [Str "The example discounts the shared Folder (4 at 1.25) by 20 percent, so its value is 4.00 instead of 5.00."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.List;
import java.util.Locale;

class Item {
    protected final String name;
    protected final int quantity;
    protected final double unitPrice;

    Item(String name, int quantity, double unitPrice) {
        this.name = name;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    double totalValue() {
        return quantity * unitPrice;
    }

    void describe() {
        System.out.println(name + \": \" + quantity + \" at \" + String.format(Locale.US, \"%.2f\", unitPrice)
            + \" each, value \" + String.format(Locale.US, \"%.2f\", totalValue()));
    }
}

class DiscountedItem extends Item {
    private final double discountRate;

    DiscountedItem(String name, int quantity, double unitPrice, double discountRate) {
        super(name, quantity, unitPrice);
        this.discountRate = discountRate;
    }

    @Override
    double totalValue() {
        return super.totalValue() * (1 - discountRate);
    }
}

public class Lesson_7_4 {
    public static void main(String[] args) {
        DiscountedItem folder = new DiscountedItem(\"Folder\", 4, 1.25, 0.20);
        folder.describe();
        System.out.println(folder instanceof Item);

        List<Item> items = List.of(new Item(\"Notebook\", 3, 2.50), folder);
        for (Item item : items) {
            System.out.println(item.name + \": \" + String.format(Locale.US, \"%.2f\", item.totalValue()));
        }
    }
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Folder: 4 at 1.25 each, value 4.00
true
Notebook: 7.50
Folder: 4.00
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to call ", Code ("", [], []) "super(...)", Str " first in the constructor, which is a compile error when the parent has no no-argument constructor."]], [Plain [Str "Forgetting ", Code ("", [], []) "@Override", Str " and accidentally creating a new method instead of replacing the parent's."]], [Plain [Str "Using inheritance for a \"has a\" relationship; use composition instead (Lesson 7.5)."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output before running."]], [Plain [Str "Add a subclass ", Code ("", [], []) "PerishableItem", Str " with an ", Code ("", [], []) "expires", Str " field and override ", Code ("", [], []) "describe", Str "."]], [Plain [Str "Explain why ", Code ("", [], []) "describe", Str " prints the discounted value without being redefined."]], [Plain [Str "List the order in which Java looks for ", Code ("", [], []) "totalValue", Str " on a ", Code ("", [], []) "DiscountedItem", Str "."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Describe inheritance as an ordered list: the subclass first, then its parent. Speaking the chain aloud ('DiscountedItem, then Item') is clearer than a diagram."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can declare a subclass."]], [Plain [Str "\9744", Space, Str "I can override a method."]], [Plain [Str "\9744", Space, Str "I can call ", Code ("", [], []) "super", Str "."]], [Plain [Str "\9744", Space, Str "I can explain polymorphism."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "final", Str " stops inheritance."]]], HorizontalRule, Header 3 ("lesson-75-composition", ["unnumbered", "unlisted"], []) [Str "Lesson 7.5: Composition"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "Java SE 25 API documentation"] ("https://docs.oracle.com/en/java/javase/25/docs/api/", "")]], [Plain [Link ("", [], []) [Str "Java Language Specification, Java SE 25"] ("https://docs.oracle.com/javase/specs/jls/se25/html/index.html", "")]], [Plain [Link ("", [], []) [Str "Dev.java learning paths"] ("https://dev.java/learn/", "")]], [Plain [Str "Matching Python lesson: Lesson 7.5: Instances as Attributes (Composition)"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain composition (\"has a\")."]], [Plain [Str "Hold a list of objects inside another object."]], [Plain [Str "Build an inventory from the shared items."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Emph [Str "Composition"], Str " means that one object contains other objects. An inventory ", Emph [Str "has"], Str " items; it is not a kind of item. Composition is usually simpler and safer than inheritance when objects are related by containment."], Para [Str "The container keeps a ", Code ("", [], []) "private", Str " list of its parts and exposes methods that loop over the parts and call each part's own methods, so the container does not need to know how a part works. Keeping the list private forces other code to use ", Code ("", [], []) "add", Str " and ", Code ("", [], []) "report", Str ". The method ", Code ("", [], []) "find", Str " returns an ", Code ("", [], []) "Optional<Item>", Str " because the item may not exist."], Para [Str "The example builds an ", Code ("", [], []) "Inventory", Str " with the three shared items and reports each quantity and the total value, 17.50."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["java"], []) "import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Optional;

class Item {
    final String name;
    final int quantity;
    final double unitPrice;

    Item(String name, int quantity, double unitPrice) {
        this.name = name;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    double totalValue() {
        return quantity * unitPrice;
    }
}

class Inventory {
    private final List<Item> items = new ArrayList<>();

    void add(Item item) {
        items.add(item);
    }

    Optional<Item> find(String name) {
        for (Item item : items) {
            if (item.name.equals(name)) {
                return Optional.of(item);
            }
        }
        return Optional.empty();
    }

    double totalValue() {
        double total = 0;
        for (Item item : items) {
            total += item.totalValue();
        }
        return total;
    }

    void report() {
        for (Item item : items) {
            System.out.println(item.name + \": \" + item.quantity);
        }
        System.out.println(\"Total value: \" + String.format(Locale.US, \"%.2f\", totalValue()));
    }
}

public class Lesson_7_5 {
    public static void main(String[] args) {
        Inventory inventory = new Inventory();
        inventory.add(new Item(\"Notebook\", 3, 2.50));
        inventory.add(new Item(\"Pencil\", 10, 0.50));
        inventory.add(new Item(\"Folder\", 4, 1.25));
        inventory.report();
        System.out.println(inventory.find(\"Pencil\").map(item -> item.quantity).orElse(-1));
        System.out.println(inventory.find(\"Eraser\").isPresent());
    }
}
", Para [Strong [Str "Expected behavior:"], Str " The program compiles on JDK 25 and prints a deterministic result illustrating instances as attributes: composition. Run it from a terminal, compare actual output with your prediction, and change one input to test the effect."], Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], BulletList [[Plain [Str "Exposing mutable fields and allowing callers to bypass class invariants."]], [Plain [Str "Using inheritance for a has-a relationship or failing to call the appropriate superclass constructor."]], [Plain [Str "Confusing an overridden method with an overloaded method, or omitting @Override when overriding."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Model one shared course entity with fields, constructor validation, and behavior methods."]], [Plain [Str "Attempt an invalid state transition and verify encapsulation prevents it."]], [Plain [Str "Demonstrate a true is-a relationship with overriding and runtime dispatch."]], [Plain [Str "Replace an artificial inheritance relationship with composition and compare coupling."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Navigate by class, method, and line; inspect braces, parentheses, brackets, semicolons, generic delimiters, and compiler diagnostics with the preferred screen reader or braille display. Compile and run from the terminal so the workflow does not depend on color or a visual project explorer."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the key concept in Java terms."]], [Plain [Str "\9744", Space, Str "I can trace and predict the worked example."]], [Plain [Str "\9744", Space, Str "I can compile and run the example from the terminal."]], [Plain [Str "\9744", Space, Str "I can identify and correct a Java-specific mistake."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and navigate the workflow accessibly."]]]]