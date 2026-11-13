[Header 2 ("unit-6-functions", [], []) [Str "Unit 6: Functions"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit introduces functions, enabling organization of code into reusable blocks, passing arguments, and returning values."], Para [Strong [Str "Objectives:"]], BulletList [[Plain [Str "Define and call functions."]], [Plain [Str "Pass arguments to functions."]], [Plain [Str "Return values from functions."]], [Plain [Str "Understand the concept of scope."]]], HorizontalRule, Header 3 ("lesson-61-defining-functions", ["unnumbered", "unlisted"], []) [Str "Lesson 6.1: Defining Functions"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 6, pages 137–142"]], [Plain [Str "Matthes: Chapter 8, pages 129–130"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain why functions are useful."]], [Plain [Str "Define a simple function in Python."]], [Plain [Str "Use parameters to specify function inputs."]], [Plain [Str "Call a function by its name."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("function-syntax", ["unnumbered", "unlisted"], []) [Str "Function Syntax"], CodeBlock ("", ["python"], []) "def function_name(parameter1, parameter2):
    \"\"\"Docstring describing what the function does.\"\"\"
    # Function body
    print(f\"Hello, {parameter1}!\")
", Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 6.1.1: Simple Greeting Function"]], CodeBlock ("", ["python"], []) "def greet_user():
    \"\"\"Prints a simple greeting message.\"\"\"
    print(\"Hello, Python programmer!\")

greet_user()   # Call the function
greet_user()   # Call it again
", Para [Strong [Str "Example 6.1.2: Function with a Parameter"]], CodeBlock ("", ["python"], []) "def greet_name(name):
    \"\"\"Prints a personalized greeting.\"\"\"
    print(f\"Hello, {name}!\")

greet_name(\"Avery\")
greet_name(\"Riley\")
", Para [Strong [Str "Example 6.1.3: A Reusable Tip Calculator (shared calculator values)"]], CodeBlock ("", ["python"], []) "def show_tip(bill, tip_rate):
    \"\"\"Print the tip and the total for a bill.\"\"\"
    tip = bill * tip_rate
    print(f\"Tip: {tip:.2f}\")
    print(f\"Total: {bill + tip:.2f}\")

show_tip(24.5, 0.15)
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Tip: 3.67
Total: 28.18
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing ", Code ("", [], []) "greet_user", Str " without parentheses and expecting the function to run."]], [Plain [Str "Forgetting the colon after the ", Code ("", [], []) "def", Str " line, or the indentation of the body."]], [Plain [Str "Passing arguments in the wrong order, such as ", Code ("", [], []) "show_tip(0.15, 24.5)", Str "."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Call ", Code ("", [], []) "show_tip(100, 0.2)", Str " and predict both printed lines."]], [Plain [Str "Write a function ", Code ("", [], []) "describe_student(name, age)", Str " that prints one sentence."]], [Plain [Str "Call ", Code ("", [], []) "greet_name()", Str " with no argument and read the error message."]], [Plain [Str "Explain the difference between a parameter and an argument using the example."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Choose function names that read as actions when spoken, such as ", Code ("", [], []) "show_tip", Str ". Print complete sentences from a function so the screen reader announces the result of each call separately, and say 'open parenthesis, close parenthesis' for an empty parameter list."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain why functions are useful."]], [Plain [Str "\9744", Space, Str "I can define a simple function in Python."]], [Plain [Str "\9744", Space, Str "I can use parameters to specify function inputs."]], [Plain [Str "\9744", Space, Str "I can call a function by its name."]]], HorizontalRule, Header 3 ("lesson-62-passing-arguments", ["unnumbered", "unlisted"], []) [Str "Lesson 6.2: Passing Arguments"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 8 (Functions), the sections on passing arguments"]], [Plain [Str "Zelle: Chapter 6 (Defining Functions)"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Differentiate between a parameter and an argument."]], [Plain [Str "Pass arguments using positional order."]], [Plain [Str "Pass arguments using keyword arguments."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("positional-vs-keyword-arguments", ["unnumbered", "unlisted"], []) [Str "Positional vs. Keyword Arguments"], CodeBlock ("", ["python"], []) "def describe_animal(animal_type, animal_name):
    print(f\"I have a {animal_type} named {animal_name}.\")

# Positional arguments (order matters)
describe_animal(\"dog\", \"Buddy\")

# Keyword arguments (order doesn't matter)
describe_animal(animal_name=\"Max\", animal_type=\"cat\")
", Header 5 ("default-values", ["unnumbered", "unlisted"], []) [Str "Default Values"], CodeBlock ("", ["python"], []) "def make_shirt(size, message=\"I love Python\"):
    print(f\"Making a {size}-sized shirt: '{message}'\")

make_shirt(\"large\")                       # Uses default message
make_shirt(\"medium\", \"Hello World\")       # Custom message
", Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example: Default, Positional, and Keyword Arguments (shared calculator values)"]], CodeBlock ("", ["python"], []) "def calculate_total(bill, tip_rate=0.15):
    return bill + bill * tip_rate

print(f\"{calculate_total(24.5):.2f}\")                       # default rate
print(f\"{calculate_total(24.5, 0.20):.2f}\")                 # positional
print(f\"{calculate_total(tip_rate=0.10, bill=24.5):.2f}\")   # keyword
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "28.18
29.40
26.95
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Putting a parameter with a default before a parameter without one in the definition, which is a syntax error."]], [Plain [Str "Mixing positional and keyword arguments in an order Python does not allow (positional first)."]], [Plain [Str "Using a mutable default such as ", Code ("", [], []) "[]", Str ", which is shared between calls."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the three totals in the example before running it."]], [Plain [Str "Add a third parameter ", Code ("", [], []) "round_total", Str " with the default ", Code ("", [], []) "False", Str " and use it."]], [Plain [Str "Call the function with the arguments in a different order using keywords."]], [Plain [Str "Explain why ", Code ("", [], []) "tip_rate=0.15", Str " is called a default value."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Keyword arguments make a call read as a sentence: 'calculate total, bill equals 24.5, tip rate equals 0.10'. Say the equals signs aloud and check that your screen reader announces them."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can differentiate between a parameter and an argument."]], [Plain [Str "\9744", Space, Str "I can pass arguments using positional order."]], [Plain [Str "\9744", Space, Str "I can pass arguments using keyword arguments."]]], HorizontalRule, Header 3 ("lesson-63-return-values", ["unnumbered", "unlisted"], []) [Str "Lesson 6.3: Return Values"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 8 (Functions), the section on return values"]], [Plain [Str "Zelle: Chapter 6 (Defining Functions)"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Use ", Code ("", [], []) "return", Str " to send a value back from a function."]], [Plain [Str "Explain the difference between ", Code ("", [], []) "print()", Str " and ", Code ("", [], []) "return", Str "."]], [Plain [Str "Store the returned value of a function in a variable."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("the-return-statement", ["unnumbered", "unlisted"], []) [Str "The ", Code ("", [], []) "return", Str " Statement"], CodeBlock ("", ["python"], []) "def add_numbers(num1, num2):
    \"\"\"Adds two numbers and returns the result.\"\"\"
    total = num1 + num2
    return total

result = add_numbers(5, 3)
print(f\"The sum is: {result}\")   # 8
", Para [Strong [Str "Key difference:"], Str " ", Code ("", [], []) "print()", Str " displays a value; ", Code ("", [], []) "return", Str " sends a value back to the caller for further use."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example: Returning Computed Results (shared scores)"]], CodeBlock ("", ["python"], []) "def average(scores):
    \"\"\"Return the average of a list of scores.\"\"\"
    return sum(scores) / len(scores)

def classify(score):
    if score >= 90:
        return \"A\"
    elif score >= 80:
        return \"B\"
    elif score >= 70:
        return \"C\"
    elif score >= 60:
        return \"D\"
    return \"F\"

avg = average([82, 91, 76, 88])   # returned, not just printed
print(f\"Average: {avg}\")
print(f\"Grade for the average: {classify(avg)}\")
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Average: 84.25
Grade for the average: B
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Printing inside a function and then trying to use the result in a calculation. The function returned ", Code ("", [], []) "None", Str "."]], [Plain [Str "Writing statements after ", Code ("", [], []) "return", Str " in the same block. They never run."]], [Plain [Str "Ignoring a returned value, so the work of the function is lost."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the two printed results of the example before running."]], [Plain [Str "Write ", Code ("", [], []) "total(list)", Str " that returns the sum of a list of numbers."]], [Plain [Str "Write ", Code ("", [], []) "is_passing(score)", Str " that returns ", Code ("", [], []) "True", Str " or ", Code ("", [], []) "False", Str " using the shared thresholds."]], [Plain [Str "Explain the difference between ", Code ("", [], []) "print", Str " and ", Code ("", [], []) "return", Str " in two sentences."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Return values from functions and print them in one place. A function that prints and returns at the same time can announce a result twice. Read the single printed line aloud and check it matches the returned value."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "return", Str " to send a value back from a function."]], [Plain [Str "\9744", Space, Str "I can explain the difference between ", Code ("", [], []) "print()", Str " and ", Code ("", [], []) "return", Str "."]], [Plain [Str "\9744", Space, Str "I can store the returned value of a function in a variable."]]], HorizontalRule, Header 3 ("lesson-64-functions-with-lists-and-dictionaries", ["unnumbered", "unlisted"], []) [Str "Lesson 6.4: Functions with Lists and Dictionaries"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 8 (Functions), the section on passing a list to a function"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Pass a list or dictionary as an argument to a function."]], [Plain [Str "Understand that modifying a list inside a function affects the original."]], [Plain [Str "Create a copy of a list to avoid unintended modifications."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Since lists are ", Strong [Str "mutable"], Str ", modifying them inside a function changes the original:"], CodeBlock ("", ["python"], []) "def add_score(score_list, new_score):
    score_list.append(new_score)

scores = [82, 91, 76, 88]
add_score(scores, 95)
print(scores)   # [82, 91, 76, 88, 95]  - the original list changed
", Para [Str "Expected output:"], CodeBlock ("", [""], []) "[82, 91, 76, 88, 95]
", Para [Str "To prevent modification, pass a copy:"], CodeBlock ("", ["python"], []) "add_score(scores[:], 100)   # Original unchanged
", Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example: Processing the Shared Inventory with a Function"]], CodeBlock ("", ["python"], []) "def inventory_value(inventory):
    total = 0
    for details in inventory.values():
        total += details[\"quantity\"] * details[\"unit_price\"]
    return total

inventory = {
    \"Notebook\": {\"quantity\": 3, \"unit_price\": 2.50},
    \"Pencil\": {\"quantity\": 10, \"unit_price\": 0.50},
    \"Folder\": {\"quantity\": 4, \"unit_price\": 1.25},
}
print(f\"Total inventory value: {inventory_value(inventory):.2f}\")
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Total inventory value: 17.50
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Expecting a function to receive its own copy of a list. It receives the same list and can change it."]], [Plain [Str "Changing a list inside a function that is meant only to read it."]], [Plain [Str "Making a copy with ", Code ("", [], []) "copy = original", Str " instead of ", Code ("", [], []) "original[:]", Str " or ", Code ("", [], []) "list(original)", Str "."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed lists in the example before running it."]], [Plain [Str "Write ", Code ("", [], []) "scale_prices(inventory, factor)", Str " that changes the prices in place and show the effect."]], [Plain [Str "Rewrite it so it returns a new inventory and leaves the original unchanged."]], [Plain [Str "Explain the difference between passing a number and passing a list to a function."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "State aloud before each call whether the function changes its argument. Print the list before and after the call so a screen reader user hears the effect, and use names such as ", Code ("", [], []) "add_score", Str " that say a change will happen."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can pass a list or dictionary as an argument to a function."]], [Plain [Str "\9744", Space, Str "I understand that modifying a list inside a function affects the original."]], [Plain [Str "\9744", Space, Str "I can create a copy of a list to avoid unintended modifications."]]], HorizontalRule, Header 3 ("lesson-65-arbitrary-number-of-arguments", ["unnumbered", "unlisted"], []) [Str "Lesson 6.5: Arbitrary Number of Arguments"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 8 (Functions), the section on passing an arbitrary number of arguments"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Define a function using ", Code ("", [], []) "*args", Str " for arbitrary positional arguments."]], [Plain [Str "Define a function using ", Code ("", [], []) "**kwargs", Str " for arbitrary keyword arguments."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("args--arbitrary-positional-arguments", ["unnumbered", "unlisted"], []) [Code ("", [], []) "*args", Str " — Arbitrary Positional Arguments"], CodeBlock ("", ["python"], []) "def make_pizza(size, *toppings):
    print(f\"Making a {size}-inch pizza with:\")
    for topping in toppings:
        print(f\"  - {topping}\")

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
", Para [Strong [Str "Example: Variable Number of Scores"]], CodeBlock ("", ["python"], []) "def average(*scores):
    return sum(scores) / len(scores)

print(average(82, 91, 76, 88))   # any number of arguments
print(average(90, 80))
", Para [Str "Expected output:"], CodeBlock ("", [""], []) "84.25
85.0
", Header 5 ("kwargs--arbitrary-keyword-arguments", ["unnumbered", "unlisted"], []) [Code ("", [], []) "**kwargs", Str " — Arbitrary Keyword Arguments"], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

profile = build_profile('albert', 'einstein',
                        location='princeton',
                        field='physics')
print(profile)
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output of example 1:"], CodeBlock ("", [""], []) "{'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Calling ", Code ("", [], []) "average()", Str " with no arguments, which divides by zero. Check the count first."]], [Plain [Str "Putting ", Code ("", [], []) "*args", Str " before a normal parameter and being unable to pass the normal one by position."]], [Plain [Str "Forgetting that ", Code ("", [], []) "*args", Str " is a tuple, not a list, so it cannot be changed."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the result of ", Code ("", [], []) "average(82, 91, 76, 88)", Str " and ", Code ("", [], []) "average(90, 80)", Str "."]], [Plain [Str "Write ", Code ("", [], []) "maximum(*numbers)", Str " that returns the largest argument."]], [Plain [Str "Write ", Code ("", [], []) "join_words(separator, *words)", Str " that joins any number of words."]], [Plain [Str "Explain what the ", Code ("", [], []) "*", Str " does in a call such as ", Code ("", [], []) "average(*scores)", Str "."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read variadic signatures aloud: 'define average, open parenthesis, star scores, close parenthesis'. Make sure your screen reader announces the star, since it changes the meaning of the parameter."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can define a function using ", Code ("", [], []) "*args", Str " for arbitrary positional arguments."]], [Plain [Str "\9744", Space, Str "I can define a function using ", Code ("", [], []) "**kwargs", Str " for arbitrary keyword arguments."]]], Header 3 ("canonical-shared-dataset--inventory-collections-and-functions", ["unnumbered", "unlisted"], []) [Str "Canonical Shared Dataset — Inventory, Collections, and Functions"], Para [Str "Use the same inventory records for list, dictionary, iteration, and function examples."], CodeBlock ("", ["python"], []) "inventory = [
    {\"name\": \"Notebook\", \"quantity\": 3, \"unit_price\": 2.50},
    {\"name\": \"Pencil\", \"quantity\": 10, \"unit_price\": 0.50},
    {\"name\": \"Folder\", \"quantity\": 4, \"unit_price\": 1.25},
]

def item_value(item):
    return item[\"quantity\"] * item[\"unit_price\"]

for item in inventory:
    print(item[\"name\"], item[\"quantity\"], f\"${item['unit_price']:.2f}\",
          f\"${item_value(item):.2f}\")

grand_total = sum(item_value(item) for item in inventory)
print(f\"Inventory total: ${grand_total:.2f}\")
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "Notebook 3 $2.50 $7.50
Pencil 10 $0.50 $5.00
Folder 4 $1.25 $5.00
Inventory total: $17.50
", Para [Str "For sequence exercises, use the canonical scores ", Code ("", [], []) "[82, 91, 76, 88]", Str ". For immutable-sequence exercises, use coordinates ", Code ("", [], []) "(3, 4)", Str ". Keep language-specific collection types idiomatic while preserving record values and calculation results."]]