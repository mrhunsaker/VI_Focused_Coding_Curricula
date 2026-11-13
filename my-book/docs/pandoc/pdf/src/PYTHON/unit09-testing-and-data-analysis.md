[Header 2 ("unit-9-testing-and-data-analysis", [], []) [Str "Unit 9: Testing and Data Analysis"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit introduces testing code for correctness and explores basic text-based data analysis."], HorizontalRule, Header 3 ("lesson-91-testing-a-function", ["unnumbered", "unlisted"], []) [Str "Lesson 9.1: Testing a Function"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 11, pages 209–217"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create a basic test class using ", Code ("", [], []) "unittest.TestCase", Str "."]], [Plain [Str "Define test methods within a test class."]], [Plain [Str "Use ", Code ("", [], []) "assertEqual()", Str " to check for expected results."]], [Plain [Str "Run unit tests from the terminal."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("unit-testing-with-unittest", ["unnumbered", "unlisted"], []) [Str "Unit Testing with ", Code ("", [], []) "unittest"], CodeBlock ("", ["python"], []) "# my_functions.py
def add(a, b):
    return a + b


def calculate_tip(bill, rate):
    return bill * rate


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
", CodeBlock ("", ["python"], []) "# test_my_functions.py
import unittest
from my_functions import add, calculate_tip, classify


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(10, -4), 6)

    def test_tip(self):
        # Decimal results are compared with a tolerance, not exact equality.
        self.assertAlmostEqual(calculate_tip(24.5, 0.15), 3.675)
        self.assertEqual(calculate_tip(0, 0.15), 0)

    def test_classify_boundaries(self):
        self.assertEqual(classify(90), \"A\")
        self.assertEqual(classify(89), \"B\")
        self.assertEqual(classify(60), \"D\")
        self.assertEqual(classify(59), \"F\")


if __name__ == '__main__':
    unittest.main()
", Para [Str "Run the tests from the terminal with ", Code ("", [], []) "python test_my_functions.py", Str " or ", Code ("", [], []) "python -m unittest", Str ". Expected output (the timing line will differ):"], CodeBlock ("", [""], []) "...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
", Para [Str "The three tests check the same inputs and expected results in every language track: ", Code ("", [], []) "add(5, 3)", Str " is 8, the tip for a bill of 24.50 at 0.15 is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "# my_functions.py
def add(a, b):
    return a + b


def calculate_tip(bill, rate):
    return bill * rate


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
", CodeBlock ("", ["python"], []) "# test_my_functions.py
import unittest
from my_functions import add, calculate_tip, classify


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(10, -4), 6)

    def test_tip(self):
        # Decimal results are compared with a tolerance, not exact equality.
        self.assertAlmostEqual(calculate_tip(24.5, 0.15), 3.675)
        self.assertEqual(calculate_tip(0, 0.15), 0)

    def test_classify_boundaries(self):
        self.assertEqual(classify(90), \"A\")
        self.assertEqual(classify(89), \"B\")
        self.assertEqual(classify(60), \"D\")
        self.assertEqual(classify(59), \"F\")


if __name__ == '__main__':
    unittest.main()
", Para [Str "Run the tests from the terminal with ", Code ("", [], []) "python test_my_functions.py", Str " or ", Code ("", [], []) "python -m unittest", Str "."], Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output (the timing line differs from run to run):"], CodeBlock ("", [""], []) "...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
", Para [Str "The three tests check the same inputs and expected results in every language track: ", Code ("", [], []) "add(5, 3)", Str " is 8, the tip for a bill of 24.50 at 0.15 is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F."], Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Comparing decimal results with ", Code ("", [], []) "assertEqual", Str ". Use ", Code ("", [], []) "assertAlmostEqual", Str ", because floating-point results are approximations."]], [Plain [Str "Naming a test method without the ", Code ("", [], []) "test_", Str " prefix, so ", Code ("", [], []) "unittest", Str " never runs it."]], [Plain [Str "Testing only typical values and skipping the boundaries 90, 89, 60, and 59."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Change one expected value so a test fails, read the failure message, and then restore it."]], [Plain [Str "Add tests for the grades at 80, 79, 70, and 69."]], [Plain [Str "Write the tests for ", Code ("", [], []) "is_passing(score)", Str " before you write the function."]], [Plain [Str "Explain why the tip test uses a tolerance."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "A passing run prints a short summary (", Code ("", [], []) "Ran 3 tests ... OK", Str ") that is quick to read. A failing run prints the test name and the expected and actual values on separate lines; jump to those lines first. Name each test as a sentence that completes 'This test checks that...'."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can create a basic test class using ", Code ("", [], []) "unittest.TestCase", Str "."]], [Plain [Str "\9744", Space, Str "I can define test methods within a test class."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "assertEqual()", Str " to check for expected results."]], [Plain [Str "\9744", Space, Str "I can run unit tests from the terminal."]]], HorizontalRule, Header 3 ("lesson-92-testing-a-class", ["unnumbered", "unlisted"], []) [Str "Lesson 9.2: Testing a Class"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 11 (Testing Your Code), the sections on testing a class"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write tests for a Python class."]], [Plain [Str "Use ", Code ("", [], []) "setUp()", Str " to prepare my tests."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("the-setup-method", ["unnumbered", "unlisted"], []) [Str "The ", Code ("", [], []) "setUp()", Str " Method"], Para [Code ("", [], []) "setUp()", Str " runs ", Strong [Str "before every test method"], Str ", providing a fresh instance each time:"], CodeBlock ("", ["python"], []) "# item.py  (the Item class from Unit 7, with a restock method)
class Item:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        return self.quantity * self.unit_price

    def restock(self, amount):
        if amount < 0:
            raise ValueError(\"amount must not be negative\")
        self.quantity += amount
", CodeBlock ("", ["python"], []) "# test_item.py
import unittest
from item import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        \"\"\"Create a fresh Notebook for every test method.\"\"\"
        self.item = Item(\"Notebook\", 3, 2.50)

    def test_total_value(self):
        self.assertAlmostEqual(self.item.total_value(), 7.5)

    def test_restock(self):
        self.item.restock(2)
        self.assertEqual(self.item.quantity, 5)

    def test_restock_rejects_negative_amount(self):
        with self.assertRaises(ValueError):
            self.item.restock(-1)


if __name__ == '__main__':
    unittest.main()
", Para [Str "Expected output (the timing line will differ):"], CodeBlock ("", [""], []) "...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
", Para [Str "Because ", Code ("", [], []) "setUp()", Str " runs before each test, ", Code ("", [], []) "test_restock", Str " changing the quantity to 5 does not affect ", Code ("", [], []) "test_total_value", Str ", which still sees 3 notebooks."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "# item.py  (the Item class from Unit 7, with a restock method)
class Item:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        return self.quantity * self.unit_price

    def restock(self, amount):
        if amount < 0:
            raise ValueError(\"amount must not be negative\")
        self.quantity += amount
", CodeBlock ("", ["python"], []) "# test_item.py
import unittest
from item import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        \"\"\"Create a fresh Notebook for every test method.\"\"\"
        self.item = Item(\"Notebook\", 3, 2.50)

    def test_total_value(self):
        self.assertAlmostEqual(self.item.total_value(), 7.5)

    def test_restock(self):
        self.item.restock(2)
        self.assertEqual(self.item.quantity, 5)

    def test_restock_rejects_negative_amount(self):
        with self.assertRaises(ValueError):
            self.item.restock(-1)


if __name__ == '__main__':
    unittest.main()
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output (the timing line differs):"], CodeBlock ("", [""], []) "...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
", Para [Str "Because ", Code ("", [], []) "setUp()", Str " runs before each test, ", Code ("", [], []) "test_restock", Str " changing the quantity to 5 does not affect ", Code ("", [], []) "test_total_value", Str ", which still sees 3 notebooks."], Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Sharing one object between tests so that an earlier test changes the later ones; use ", Code ("", [], []) "setUp", Str "."]], [Plain [Str "Testing only the successful path and never the error path."]], [Plain [Str "Forgetting ", Code ("", [], []) "self.", Str " inside a test method, so the fixture object is not found."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Add a test that ", Code ("", [], []) "restock(0)", Str " leaves the quantity unchanged."]], [Plain [Str "Add a test for the ", Code ("", [], []) "is_valid", Str " method from Unit 7."]], [Plain [Str "Break ", Code ("", [], []) "restock", Str " on purpose and read the failure report."]], [Plain [Str "Explain why ", Code ("", [], []) "setUp", Str " creates a new item for each test."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Name each test as a short sentence that says what behavior it checks, so the PASS or FAIL report reads as a clear statement. Read the summary line first, and open the failure details only when it says FAILED."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write tests for a Python class."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "setUp()", Str " to prepare my tests."]]], HorizontalRule, Header 3 ("lesson-93-introduction-to-random-numbers", ["unnumbered", "unlisted"], []) [Str "Lesson 9.3: Introduction to Random Numbers"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 9 (Classes), the section on the ", Code ("", [], []) "random", Str " module"]], [Plain [Str "Zelle: Chapter 9 (Simulation and Design)"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Import the ", Code ("", [], []) "random", Str " module."]], [Plain [Str "Generate a random integer within a range."]], [Plain [Str "Select a random item from a list."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Without the ", Code ("", [], []) "random.seed(...)", Str " line the values change on every run. Use a seed when you need to test or reproduce a result."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "import random

random.seed(42)   # a fixed seed makes the \"random\" results repeatable

die_roll = random.randint(1, 6)          # random integer (inclusive)
print(f\"You rolled: {die_roll}\")

rand_float = random.random()             # random float from 0.0 up to 1.0
print(f\"Random decimal: {rand_float:.4f}\")

scores = [82, 91, 76, 88]
chosen = random.choice(scores)           # random choice from a list
print(f\"Chosen score: {chosen}\")
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output with ", Code ("", [], []) "random.seed(42)", Str " on Python 3.12:"], CodeBlock ("", [""], []) "You rolled: 6
Random decimal: 0.1113
Chosen score: 76
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Testing for specific random values that change between Python versions; test properties such as the range instead."]], [Plain [Str "Calling ", Code ("", [], []) "random.seed()", Str " in every loop pass, which repeats the same value."]], [Plain [Str "Forgetting that ", Code ("", [], []) "randint(1, 6)", Str " includes both ends, while ", Code ("", [], []) "randrange(1, 6)", Str " does not include 6."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the example three times with the seed line and then three times without it; compare."]], [Plain [Str "Change the seed and check that the ranges still hold."]], [Plain [Str "Simulate 600 rolls and count how many of each face appeared (the counts will differ)."]], [Plain [Str "Explain why a test should check a property rather than a specific random number."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "When output is random, print yes or no results about properties (", Code ("", [], []) "All rolls between 1 and 6: True", Str ") so the screen reader announces the same result on every run and does not read unpredictable values."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can import the ", Code ("", [], []) "random", Str " module."]], [Plain [Str "\9744", Space, Str "I can generate a random integer within a range."]], [Plain [Str "\9744", Space, Str "I can select a random item from a list."]]], HorizontalRule, Header 3 ("lesson-94-analyzing-text-data", ["unnumbered", "unlisted"], []) [Str "Lesson 9.4: Analyzing Text Data"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 6 (Dictionaries), the section on counting with dictionaries"]], [Plain [Str "Zelle: Chapter 5 (Sequences: Strings, Lists, and Files)"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Read text content from a file."]], [Plain [Str "Split a string of text into individual words."]], [Plain [Str "Use a dictionary to count the frequency of words."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "sentence = \"A student studies programming. Programming develops problem-solving skills.\"
words = sentence.lower().replace(\".\", \"\").split()

word_frequencies = {}
for word in words:
    word_frequencies[word] = word_frequencies.get(word, 0) + 1

print(\"Word count:\", len(words))
print(\"Word Frequencies:\")
for word, count in word_frequencies.items():
    print(f\"'{word}': {count}\")

letter_counts = {}
for ch in text.lower():
    if ch.isalpha():
        letter_counts[ch] = letter_counts.get(ch, 0) + 1

top_three = sorted(letter_counts.items(), key=lambda pair: (-pair[1], pair[0]))[:3]
print(\"Most common letters:\", top_three)
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Word count: 8
Word Frequencies:
'a': 1
'student': 1
'studies': 1
'programming': 2
'develops': 1
'problem-solving': 1
'skills': 1
Most common letters: [('s', 7), ('e', 5), ('g', 5)]
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Counting punctuation as part of a word, so ", Code ("", [], []) "programming.", Str " and ", Code ("", [], []) "programming", Str " become different words."]], [Plain [Str "Forgetting to convert text to lower case before counting, so ", Code ("", [], []) "Programming", Str " and ", Code ("", [], []) "programming", Str " are counted separately."]], [Plain [Str "Sorting a dictionary by key when the count was intended."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the word count and the count for ", Code ("", [], []) "programming", Str " before running."]], [Plain [Str "Count the words longer than 8 letters."]], [Plain [Str "Print the longest word."]], [Plain [Str "Change the sort so ties are listed in reverse alphabetical order."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the frequency list in its fixed order. Because the order is stable, you can learn it and compare runs by ear. Print each pair as a short sentence (", Code ("", [], []) "'programming': 2", Str ") with the same wording every time."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can read text content from a file."]], [Plain [Str "\9744", Space, Str "I can split a string of text into individual words."]], [Plain [Str "\9744", Space, Str "I can use a dictionary to count the frequency of words."]]], HorizontalRule, Header 3 ("lesson-95-working-with-csv-data", ["unnumbered", "unlisted"], []) [Str "Lesson 9.5: Working with CSV Data"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 10 (Files and Exceptions), the section on CSV files"]], [Plain [Str "Zelle: Chapter 5 (Sequences: Strings, Lists, and Files)"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain what CSV data is."]], [Plain [Str "Read a CSV file line by line."]], [Plain [Str "Split a line of CSV data into individual values."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Save this as ", Code ("", [], []) "students.csv", Str " (the same file is used in every language track):"], CodeBlock ("", ["csv"], []) "student_id,first_name,last_name,score,active
1,Avery,Student,91,true
2,Jordan,Lee,82,true
3,Casey,Smith,76,false
", Para [Str "The ", Code ("", [], []) "csv", Str " module handles quoted fields and embedded commas correctly. Splitting each line on commas with ", Code ("", [], []) "line.split(',')", Str " works only for simple files where no value contains a comma."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "import csv

filename = 'students.csv'
try:
    with open(filename, 'r', newline='') as file_object:
        reader = csv.DictReader(file_object)
        print(f\"Columns: {reader.fieldnames}\")
        scores = []
        active_count = 0
        for row in reader:
            scores.append(int(row[\"score\"]))
            if row[\"active\"] == \"true\":
                active_count += 1
            print(f\"{row['student_id']}: {row['first_name']} {row['last_name']} scored {row['score']}\")
    print(f\"Students: {len(scores)}\")
    print(f\"Average score: {sum(scores) / len(scores):.2f}\")
    print(f\"Active students: {active_count}\")
except FileNotFoundError:
    print(f\"Error: The file {filename} was not found.\")
", Header 4 ("reading-the-canonical-csv-schema", ["unnumbered", "unlisted"], []) [Str "Reading the Canonical CSV Schema"], Para [Str "Use the standard ", Code ("", [], []) "csv", Str " module rather than splitting rows on commas. A quoted field may itself contain a comma."], CodeBlock ("", ["python"], []) "import csv
from io import StringIO

csv_text = \"\"\"student_id,first_name,last_name,score,active
1001,Avery,Jordan,82,true
1002,Riley,Chen,91,true
1003,Sam,Patel,76,false
1004,Morgan,Diaz,88,true
\"\"\"

reader = csv.DictReader(StringIO(csv_text))
for row in reader:
    print(row[\"student_id\"], row[\"first_name\"], row[\"last_name\"],
          row[\"score\"], row[\"active\"])
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "1001 Avery Jordan 82 true
1002 Riley Chen 91 true
1003 Sam Patel 76 false
1004 Morgan Diaz 88 true
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Splitting a CSV line at every comma when a value itself contains a quoted comma; use the ", Code ("", [], []) "csv", Str " module."]], [Plain [Str "Forgetting to convert the text in the score column to a number."]], [Plain [Str "Opening a CSV file without ", Code ("", [], []) "newline=''", Str ", which can produce blank rows on some systems."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed lines before running."]], [Plain [Str "Add a fourth student and check the new average."]], [Plain [Str "Print only the active students."]], [Plain [Str "Explain, with an example, why ", Code ("", [], []) "\"Smith, Jr.\"", Str " breaks ", Code ("", [], []) "line.split(',')", Str "."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print one student per line with the same wording each time, so the screen reader announces a repeating pattern that is easy to compare line by line. Read the column names aloud once at the start so the values that follow have meaning."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain what CSV data is."]], [Plain [Str "\9744", Space, Str "I can read a CSV file line by line."]], [Plain [Str "\9744", Space, Str "I can split a line of CSV data into individual values."]]], Header 3 ("canonical-shared-dataset--text-csv-tasks-and-tests", ["unnumbered", "unlisted"], []) [Str "Canonical Shared Dataset — Text, CSV, Tasks, and Tests"], Header 4 ("text-analysis", ["unnumbered", "unlisted"], []) [Str "Text analysis"], Para [Str "Use this exact sentence for word-count and character-processing exercises:"], CodeBlock ("", ["python"], []) "text_sample = \"A student studies programming. Programming develops problem-solving skills.\"
words = text_sample.lower().replace(\".\", \"\").split()
print(\"Words:\", len(words))
print(\"Programming:\", words.count(\"programming\"))
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "Words: 8
Programming: 2
", Header 4 ("csv-schema", ["unnumbered", "unlisted"], []) [Str "CSV schema"], Para [Str "The shared CSV header is exactly ", Code ("", [], []) "student_id,first_name,last_name,score,active", Str ". Example rows:"], CodeBlock ("", ["csv"], []) "student_id,first_name,last_name,score,active
1001,Avery,Jordan,82,true
1002,Riley,Chen,91,true
1003,Sam,Patel,76,false
1004,Morgan,Diaz,88,true
", Para [Str "Use the ", Code ("", [], []) "csv", Str " module and named column positions; do not substitute a different three-column name/age/grade schema."], CodeBlock ("", ["python"], []) "import csv
from io import StringIO

csv_text = \"\"\"student_id,first_name,last_name,score,active
1001,Avery,Jordan,82,true
1002,Riley,Chen,91,true
1003,Sam,Patel,76,false
1004,Morgan,Diaz,88,true
\"\"\"
for row in csv.DictReader(StringIO(csv_text)):
    print(row[\"student_id\"], row[\"first_name\"], row[\"last_name\"],
          row[\"score\"], row[\"active\"])
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "1001 Avery Jordan 82 true
1002 Riley Chen 91 true
1003 Sam Patel 76 false
1004 Morgan Diaz 88 true
", Header 4 ("to-do-record-schema", ["unnumbered", "unlisted"], []) [Str "To-do record schema"], Para [Str "Use all five fields in every serialized task record: ", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "done", Str ", and ", Code ("", [], []) "created_at", Str "."], CodeBlock ("", ["python"], []) "task = {
    \"id\": 1,
    \"title\": \"Practice Python\",
    \"description\": \"Complete the shared dataset exercises\",
    \"done\": False,
    \"created_at\": \"2025-01-15T09:00:00Z\",
}
", CodeBlock ("", ["python"], []) "import json

task = {
    \"id\": 1,
    \"title\": \"Practice Python\",
    \"description\": \"Complete the shared dataset exercises\",
    \"done\": False,
    \"created_at\": \"2025-01-15T09:00:00Z\",
}
serialized = json.dumps([task])
loaded_tasks = json.loads(serialized)
loaded_task = loaded_tasks[0]
required_fields = {\"id\", \"title\", \"description\", \"done\", \"created_at\"}
assert set(loaded_task) == required_fields
print(loaded_task[\"id\"], loaded_task[\"title\"], loaded_task[\"done\"])
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "1 Practice Python False
", Para [Str "Tests should assert deterministic results for the shared tip calculator, grade classifier, inventory total, and text sample. Random-number lessons must seed the generator when an exact result is asserted."]]