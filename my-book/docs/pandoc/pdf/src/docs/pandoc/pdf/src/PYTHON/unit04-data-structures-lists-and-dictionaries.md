[Header 2 ("unit-4-data-structures--lists-and-dictionaries", [], []) [Str "Unit 4: Data Structures — Lists and Dictionaries"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Strong [Str "Compatibility:"], Str " All examples target Python 3.12 and newer; they avoid syntax and standard-library APIs introduced after Python 3.12."], Para [Str "This unit deepens understanding of lists and introduces dictionaries as powerful mechanisms for organizing data."], Para [Strong [Str "Objectives:"]], BulletList [[Plain [Str "Add, remove, and organize list elements."]], [Plain [Str "Work with tuples (immutable lists)."]], [Plain [Str "Use dictionaries for key-value pair storage."]], [Plain [Str "Loop through dictionaries."]]], HorizontalRule, Header 3 ("lesson-41-more-on-lists", ["unnumbered", "unlisted"], []) [Str "Lesson 4.1: More on Lists"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 3 (Introducing Lists) and Chapter 4 (Working with Lists)"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Add an item to the end of a list using ", Code ("", [], []) ".append()", Str "."]], [Plain [Str "Insert an item at a specific position using ", Code ("", [], []) ".insert()", Str "."]], [Plain [Str "Remove an item by index using ", Code ("", [], []) "del", Str "."]], [Plain [Str "Remove an item and retrieve its value using ", Code ("", [], []) ".pop()", Str "."]], [Plain [Str "Remove the first occurrence of a value using ", Code ("", [], []) ".remove()", Str "."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("adding-and-removing-elements", ["unnumbered", "unlisted"], []) [Str "Adding and Removing Elements"], CodeBlock ("", ["python"], []) "my_list = [10, 20, 30]

my_list.append(40)          # Add to end → [10, 20, 30, 40]
my_list.insert(1, 15)       # Insert at index 1 → [10, 15, 20, 30, 40]
del my_list[0]              # Delete by index → [15, 20, 30, 40]
removed = my_list.pop()     # Remove and return last → removed=40, list=[15, 20, 30]
my_list.remove(20)          # Remove by value → [15, 30]
", Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "scores = [82, 91, 76, 88]

scores.append(95)        # [82, 91, 76, 88, 95]
scores.insert(1, 85)     # [82, 85, 91, 76, 88, 95]
scores[2] = 93           # [82, 85, 93, 76, 88, 95]
scores.remove(76)        # [82, 85, 93, 88, 95]
last_score = scores.pop()  # last_score is 95

print(scores)
print(len(scores))
print(88 in scores)
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "[82, 85, 93, 88]
4
True
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) "list.insert(value, position)", Str ". The position comes first: ", Code ("", [], []) "scores.insert(1, 85)", Str "."]], [Plain [Str "Calling ", Code ("", [], []) "remove()", Str " with a value that is not in the list, which raises a ", Code ("", [], []) "ValueError", Str "; check with ", Code ("", [], []) "in", Str " first."]], [Plain [Str "Removing items from a list while looping over it, which skips the item after each removal."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace the list after each operation in the example and write each version as one sentence."]], [Plain [Str "Remove the first score with ", Code ("", [], []) "pop(0)", Str " and explain what happens to the other scores."]], [Plain [Str "Write code that removes every score below 80 safely."]], [Plain [Str "Print the position of the first score above 90 with ", Code ("", [], []) "index()", Str ", and explain what happens if none exists."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "After every change, print the whole list on one line so a screen reader reads a complete state in one pass. Say the comments aloud as part of each line, since they hold the expected value after the change."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can add an item to the end of a list using ", Code ("", [], []) ".append()", Str "."]], [Plain [Str "\9744", Space, Str "I can insert an item at a specific position using ", Code ("", [], []) ".insert()", Str "."]], [Plain [Str "\9744", Space, Str "I can remove an item by index using ", Code ("", [], []) "del", Str "."]], [Plain [Str "\9744", Space, Str "I can remove an item and retrieve its value using ", Code ("", [], []) ".pop()", Str "."]], [Plain [Str "\9744", Space, Str "I can remove the first occurrence of a value using ", Code ("", [], []) ".remove()", Str "."]]], HorizontalRule, Header 3 ("lesson-42-organizing-lists", ["unnumbered", "unlisted"], []) [Str "Lesson 4.2: Organizing Lists"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 3 (Introducing Lists) and Chapter 4 (Working with Lists)"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Sort a list permanently using ", Code ("", [], []) ".sort()", Str "."]], [Plain [Str "Get a temporarily sorted version using ", Code ("", [], []) "sorted()", Str "."]], [Plain [Str "Reverse a list using ", Code ("", [], []) ".reverse()", Str "."]], [Plain [Str "Find how many items are in a list using ", Code ("", [], []) "len()", Str "."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Lists can be reordered in two ways. ", Code ("", [], []) "sort()", Str " changes the list ", Emph [Str "in place"], Str " and returns nothing. ", Code ("", [], []) "sorted()", Str " returns a ", Emph [Str "new"], Str " sorted list and leaves the original unchanged. Both accept ", Code ("", [], []) "reverse=True", Str " for descending order."], Header 5 ("sorting-and-reversing", ["unnumbered", "unlisted"], []) [Str "Sorting and Reversing"], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "scores = [82, 91, 76, 88]
scores.sort()                           # Permanent sort in-place
print(scores)                           # [76, 82, 88, 91]

fruits = [\"orange\", \"apple\", \"banana\"]
sorted_fruits = sorted(fruits)          # Temporary sort — original unchanged
print(fruits)                           # ['orange', 'apple', 'banana']
print(sorted_fruits)                    # ['apple', 'banana', 'orange']

scores.reverse()                        # Reverse in-place -> [91, 88, 82, 76]
scores.sort(reverse=True)               # Sort descending -> [91, 88, 82, 76]
print(scores)                           # [91, 88, 82, 76]
print(len(scores))                      # Length: 4
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output of example 1:"], CodeBlock ("", [""], []) "[76, 82, 88, 91]
['orange', 'apple', 'banana']
['apple', 'banana', 'orange']
[91, 88, 82, 76]
4
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing ", Code ("", [], []) "scores = scores.sort()", Str ". ", Code ("", [], []) "sort()", Str " returns ", Code ("", [], []) "None", Str ", so the list is lost."]], [Plain [Str "Sorting a list that mixes numbers and text, which raises a ", Code ("", [], []) "TypeError", Str "."]], [Plain [Str "Expecting ", Code ("", [], []) "reverse()", Str " to sort. It only flips the current order."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the result of ", Code ("", [], []) "scores.sort()", Str " and ", Code ("", [], []) "scores.sort(reverse=True)", Str " on the shared scores, then check."]], [Plain [Str "Use ", Code ("", [], []) "sorted(scores)", Str " and show that the original list is unchanged."]], [Plain [Str "Sort the words ", Code ("", [], []) "[\"pencil\", \"folder\", \"notebook\"]", Str " and print them."]], [Plain [Str "Explain the difference between ", Code ("", [], []) "sort()", Str " and ", Code ("", [], []) "sorted()", Str " in two sentences."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print each sorted version on its own labelled line (", Code ("", [], []) "Ascending:", Str ", ", Code ("", [], []) "Descending:", Str "). The first and last numbers are the quickest to check by ear."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can sort a list permanently using ", Code ("", [], []) ".sort()", Str "."]], [Plain [Str "\9744", Space, Str "I can get a temporarily sorted version using ", Code ("", [], []) "sorted()", Str "."]], [Plain [Str "\9744", Space, Str "I can reverse a list using ", Code ("", [], []) ".reverse()", Str "."]], [Plain [Str "\9744", Space, Str "I can find how many items are in a list using ", Code ("", [], []) "len()", Str "."]]], HorizontalRule, Header 3 ("lesson-43-tuples--immutable-lists", ["unnumbered", "unlisted"], []) [Str "Lesson 4.3: Tuples — Immutable Lists"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 4 (Working with Lists), the section on tuples"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create a tuple in Python."]], [Plain [Str "Explain the main difference between a list and a tuple (mutability)."]], [Plain [Str "Access items in a tuple by their index."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "tuple"], Str " is an ordered collection like a list, written with parentheses, but it cannot be changed after it is created. Use a tuple for a fixed group of values such as the shared coordinates (3, 4). Because it cannot change, a tuple can also be used where Python needs a value that never changes, such as a dictionary key."], Header 5 ("tuples", ["unnumbered", "unlisted"], []) [Str "Tuples"], Para [Str "Tuples are defined with parentheses and ", Strong [Str "cannot be changed"], Str " after creation."], Para [Strong [Str "When to use tuples:"], Str " For data that should remain constant (coordinates, RGB values, fixed settings)."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "coordinates = (3, 4)
x, y = coordinates        # tuple unpacking
print(coordinates[0])     # 3
print(coordinates[-1])    # 4
print(x, y)               # 3 4

# This would cause a TypeError:
# coordinates[1] = 5
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output of example 1:"], CodeBlock ("", [""], []) "3
4
3 4
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing ", Code ("", [], []) "(5)", Str " for a one-item tuple. A one-item tuple needs a comma: ", Code ("", [], []) "(5,)", Str "."]], [Plain [Str "Trying to assign to an item (", Code ("", [], []) "coordinates[1] = 5", Str "), which raises a ", Code ("", [], []) "TypeError", Str "."]], [Plain [Str "Using a list when the data should never change, so an accidental change goes unnoticed."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Create the tuple ", Code ("", [], []) "(3, 4)", Str ", unpack it into ", Code ("", [], []) "x", Str " and ", Code ("", [], []) "y", Str ", and print both."]], [Plain [Str "Write a function that returns a name, an age, and a height as a tuple and unpack all three."]], [Plain [Str "Try to change one item of a tuple and read the error message aloud."]], [Plain [Str "Explain, in two sentences, when a tuple is a better choice than a list."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Say the parentheses and the commas aloud when reading a tuple, because a one-item tuple differs from a plain value only by its trailing comma. Read error messages from the last line upward to find the problem quickly."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can create a tuple in Python."]], [Plain [Str "\9744", Space, Str "I can explain the main difference between a list and a tuple (mutability)."]], [Plain [Str "\9744", Space, Str "I can access items in a tuple by their index."]]], HorizontalRule, Header 3 ("lesson-44-introducing-dictionaries", ["unnumbered", "unlisted"], []) [Str "Lesson 4.4: Introducing Dictionaries"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 11, pages 307–309"]], [Plain [Str "Matthes: Chapter 6, pages 91–98"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create a dictionary in Python."]], [Plain [Str "Explain what a key-value pair is."]], [Plain [Str "Access a value in a dictionary using its key."]], [Plain [Str "Add, modify, and remove key-value pairs."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("dictionary-basics", ["unnumbered", "unlisted"], []) [Str "Dictionary Basics"], Para [Str "A dictionary stores ", Strong [Str "key-value pairs"], Str ". Keys must be unique and immutable (strings, numbers, tuples). Values can be anything."], CodeBlock ("", ["python"], []) "student_profile = {
    \"name\": \"Avery\",
    \"age\": 16,
    \"height_m\": 1.72,
    \"favorite_subject\": \"Computer Science\",
}

print(student_profile[\"name\"])
print(student_profile[\"favorite_subject\"])

# Demonstrate adding and removing a temporary key without changing
# the four-field canonical student record.
student_profile[\"temporary_note\"] = \"Dictionary example\"
del student_profile[\"temporary_note\"]
print(sorted(student_profile))
", Para [Str "Expected output:"], CodeBlock ("", [""], []) "Avery
Computer Science
['age', 'favorite_subject', 'height_m', 'name']
", Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 4.4.1: Inventory Item Dictionary"]], CodeBlock ("", ["python"], []) "item = {
    \"name\": \"Notebook\",
    \"quantity\": 3,
    \"unit_price\": 2.50
}

print(f\"Item: {item['name']}\")
print(f\"Quantity: {item['quantity']}\")

item[\"quantity\"] = item[\"quantity\"] + 2    # restock two more
item[\"location\"] = \"Shelf A\"               # add a new key
print(item)
print(\"Stock value:\", item[\"quantity\"] * item[\"unit_price\"])
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Item: Notebook
Quantity: 3
{'name': 'Notebook', 'quantity': 5, 'unit_price': 2.5, 'location': 'Shelf A'}
Stock value: 12.5
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using a key that does not exist (", Code ("", [], []) "profile[\"grade\"]", Str "), which raises a ", Code ("", [], []) "KeyError", Str "; use ", Code ("", [], []) "profile.get(\"grade\")", Str " to receive ", Code ("", [], []) "None", Str " instead."]], [Plain [Str "Forgetting the quotation marks around a text key, so Python looks for a variable."]], [Plain [Str "Expecting dictionary order to be sorted. Dictionaries keep insertion order, not alphabetical order."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed values before running the example, then run it."]], [Plain [Str "Add a ", Code ("", [], []) "\"discount\"", Str " key to the item and print the discounted line value."]], [Plain [Str "Remove ", Code ("", [], []) "\"favorite_subject\"", Str " from the profile with ", Code ("", [], []) "del", Str " and show what ", Code ("", [], []) "get", Str " returns afterward."]], [Plain [Str "Write a check that tells whether an item has all of the keys ", Code ("", [], []) "name", Str ", ", Code ("", [], []) "quantity", Str ", and ", Code ("", [], []) "unit_price", Str "."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Choose key names that read well aloud, such as ", Code ("", [], []) "unit_price", Str ". Print one key and value per line, so the screen reader announces each pair separately, and avoid relying on curly braces alone to see where a dictionary ends."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can create a dictionary in Python."]], [Plain [Str "\9744", Space, Str "I can explain what a key-value pair is."]], [Plain [Str "\9744", Space, Str "I can access a value in a dictionary using its key."]], [Plain [Str "\9744", Space, Str "I can add, modify, and remove key-value pairs."]]], HorizontalRule, Header 3 ("lesson-45-looping-through-dictionaries", ["unnumbered", "unlisted"], []) [Str "Lesson 4.5: Looping Through Dictionaries"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 6 (Dictionaries), the sections on looping through a dictionary"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Loop through all the keys in a dictionary."]], [Plain [Str "Loop through all the values in a dictionary."]], [Plain [Str "Loop through both keys and values at the same time."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("dictionary-iteration-methods", ["unnumbered", "unlisted"], []) [Str "Dictionary Iteration Methods"], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "inventory = {
    \"Notebook\": {\"quantity\": 3, \"unit_price\": 2.50},
    \"Pencil\": {\"quantity\": 10, \"unit_price\": 0.50},
    \"Folder\": {\"quantity\": 4, \"unit_price\": 1.25},
}

# Loop through keys (default)
for item_name in inventory:
    print(item_name)

# Loop through values only
for details in inventory.values():
    print(details[\"quantity\"])

# Loop through key-value pairs
total_value = 0
for item_name, details in inventory.items():
    line_value = details[\"quantity\"] * details[\"unit_price\"]
    print(f\"{item_name}: {details['quantity']} in stock, value {line_value:.2f}\")
    total_value += line_value
print(f\"Total inventory value: {total_value:.2f}\")
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Notebook
Pencil
Folder
3
10
4
Notebook: 3 in stock, value 7.50
Pencil: 10 in stock, value 5.00
Folder: 4 in stock, value 5.00
Total inventory value: 17.50
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Looping with ", Code ("", [], []) "for item in inventory", Str " and expecting the values. The default loop gives the keys."]], [Plain [Str "Changing the dictionary's size while looping over it, which raises a ", Code ("", [], []) "RuntimeError", Str "."]], [Plain [Str "Forgetting ", Code ("", [], []) ".items()", Str " when both the key and the value are needed."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the example and write the three key-value lines in order."]], [Plain [Str "Print only the items with a quantity below 5."]], [Plain [Str "Print the inventory sorted by the line value, highest first."]], [Plain [Str "Explain why ", Code ("", [], []) ".items()", Str " returns pairs and how the loop unpacks them."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print each inventory item as one complete sentence so the screen reader reads the name, quantity, and value together. Python dictionaries keep insertion order, so the order is stable and can be learned by ear."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can loop through all the keys in a dictionary."]], [Plain [Str "\9744", Space, Str "I can loop through all the values in a dictionary."]], [Plain [Str "\9744", Space, Str "I can loop through both keys and values at the same time."]]], HorizontalRule]