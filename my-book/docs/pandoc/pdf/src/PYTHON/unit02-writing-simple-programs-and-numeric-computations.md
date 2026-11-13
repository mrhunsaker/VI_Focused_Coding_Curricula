[Header 2 ("unit-2-writing-simple-programs-and-numeric-computations", [], []) [Str "Unit 2: Writing Simple Programs and Numeric Computations"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Strong [Str "Compatibility:"], Str " All code examples in this curriculum target Python 3.12 and newer. The course avoids syntax and APIs introduced after Python 3.12."], Para [Str "This unit explores the software development process, more complex numeric operations, and how to obtain and use input from users."], Para [Strong [Str "Objectives:"]], BulletList [[Plain [Str "Understand the phases of software development."]], [Plain [Str "Work with different numeric data types (integers, floats)."]], [Plain [Str "Perform type conversions."]], [Plain [Str "Use mathematical operators and the math library."]], [Plain [Str "Get user input with ", Code ("", [], []) "input()", Str "."]]], HorizontalRule, Header 3 ("lesson-21-the-software-development-process", ["unnumbered", "unlisted"], []) [Str "Lesson 2.1: The Software Development Process"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 2, pages 21–22 and pages 35–36"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Describe the purpose of the software development process."]], [Plain [Str "List and briefly explain the main phases of software development."]], [Plain [Str "Understand that problem-solving and design happen before writing code."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("the-three-phase-development-process", ["unnumbered", "unlisted"], []) [Str "The Three-Phase Development Process"], Para [Strong [Str "1. Design (Plan first)"], SoftBreak, Str "Before writing any code, fully understand the problem:"], BulletList [[Plain [Str "Identify ", Strong [Str "inputs"], Str " (information the program needs) and ", Strong [Str "outputs"], Str " (results it must produce)."]], [Plain [Str "Write an ", Strong [Str "algorithm"], Str " — a step-by-step plan in plain English (", Strong [Str "pseudocode"], Str ")."]], [Plain [Str "Consider ", Strong [Str "edge cases"], Str " — unusual inputs that might break your program."]]], Para [Strong [Str "2. Implement (Write the code)"]], BulletList [[Plain [Str "Translate your design into Python syntax."]], [Plain [Str "Code ", Strong [Str "incrementally"], Str " — build in small pieces and test as you go."]], [Plain [Str "Follow coding standards and use descriptive variable names."]]], Para [Strong [Str "3. Test and Debug (Verify it works)"]], BulletList [[Plain [Str "Run with a variety of inputs, including normal values and edge cases."]], [Plain [Str "Read error messages carefully — they tell you the type of error and the line number."]], [Plain [Str "Use ", Code ("", [], []) "print()", Str " statements to check variable values during debugging."]]], Header 5 ("why-this-process-matters", ["unnumbered", "unlisted"], []) [Str "Why This Process Matters"], BulletList [[Plain [Strong [Str "Reduces frustration"], Str " — Having a plan prevents getting stuck."]], [Plain [Strong [Str "Improves code quality"], Str " — A thoughtful design leads to cleaner code."]], [Plain [Strong [Str "Simplifies debugging"], Str " — Test each component in isolation."]], [Plain [Strong [Str "Saves time"], Str " — Good design prevents time-consuming rewrites."]]], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Str "Implement the pseudocode from the activity below with the shared values (bill 24.50, tip rate 0.15):"], CodeBlock ("", ["python"], []) "bill = 24.5
tip_rate = 0.15

tip = bill * tip_rate
total = bill + tip

print(f\"Bill: {bill:.2f}\")
print(f\"Tip: {tip:.2f}\")
print(f\"Total: {total:.2f}\")
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output of example 1:"], CodeBlock ("", [""], []) "Bill: 24.50
Tip: 3.67
Total: 28.18
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing the rate as 15 instead of 0.15, which makes the tip fifteen times too large."]], [Plain [Str "Rounding the tip before adding it to the bill, which can change the total by a cent."]], [Plain [Str "Skipping tests for a zero bill or a negative bill."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], Para [Strong [Str "Activity 2.1.1: Planning a Tip Calculator"], SoftBreak, Str "Write pseudocode before coding:"], CodeBlock ("", [""], []) "1. GET bill amount from user
2. CALCULATE tip as 15% of bill amount
3. CALCULATE total amount (bill + tip)
4. PRINT tip amount
5. PRINT total amount
", Para [Str "Trace this plan with the shared calculator values: the bill is 24.50 and the tip rate is 0.15. The tip is 24.50 × 0.15 = 3.675 and the total is 24.50 + 3.675 = 28.175. Shown with two decimal places, Python displays the tip as 3.67 and the total as 28.18, because 3.675 cannot be stored exactly in binary floating point. You will implement this plan in Lesson 2.4."], Para [Strong [Str "Activity 2.1.2: Tracing a Simple Program"], SoftBreak, Str "Without running the code, trace the execution and predict output:"], CodeBlock ("", ["python"], []) "a = 10
b = 5
c = a * b
a = a + 2
print(c)
print(a)
", Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Write the design steps as a numbered list and print every result on its own labelled line (", Code ("", [], []) "Tip: 3.67", Str "), so a screen reader reads each result as one clear unit. Do not use alignment or spacing to convey meaning."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can describe the purpose of the software development process."]], [Plain [Str "\9744", Space, Str "I can list and briefly explain the main phases of software development."]], [Plain [Str "\9744", Space, Str "I understand that problem-solving and design happen before writing code."]]], HorizontalRule, Header 3 ("lesson-22-elements-of-programs--expressions-and-assignment", ["unnumbered", "unlisted"], []) [Str "Lesson 2.2: Elements of Programs — Expressions and Assignment"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 2, pages 24–26"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Identify an expression in Python code."]], [Plain [Str "Predict the result of simple Python expressions."]], [Plain [Str "Explain how the assignment operator ", Code ("", [], []) "=", Str " works."]], [Plain [Str "Demonstrate how to update a variable's value."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("expressions-and-assignment", ["unnumbered", "unlisted"], []) [Str "Expressions and Assignment"], Para [Str "An ", Strong [Str "expression"], Str " is any combination of values, variables, and operators that evaluates to a single result. Python follows the standard mathematical order of operations (PEMDAS)."], CodeBlock ("", ["python"], []) "result1 = 10 / 2 + 3  # 10/2 is 5, then 5+3 = 8.0
message = \"Python\" + \" \" + \"is fun!\"
", Para [Strong [Str "Assignment:"]], CodeBlock ("", ["python"], []) "score = 82
score = score + 9  # score is now 91
", Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 2.2.1: Expression Evaluation"]], CodeBlock ("", ["python"], []) "result1 = 10 / 2 + 3
print(\"Result 1:\", result1)   # Output: Result 1: 8.0
print(\"Precedence:\", 8 + 4 * 2)   # Output: Precedence: 16
print(\"Grouped:\", (8 + 4) * 2)    # Output: Grouped: 24

message = \"Python\" + \" \" + \"is fun!\"
print(\"Message:\", message)    # Output: Message: Python is fun!
", Para [Strong [Str "Example 2.2.2: Reassigning Variables"]], CodeBlock ("", ["python"], []) "score = 82
print(\"Initial score:\", score)
score = score + 9
print(\"New score:\", score)     # Output: New score: 91
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output of example 1:"], CodeBlock ("", [""], []) "Result 1: 8.0
Precedence: 16
Grouped: 24
Message: Python is fun!
", Para [Str "Output of example 2:"], CodeBlock ("", [""], []) "Initial score: 82
New score: 91
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Reading ", Code ("", [], []) "=", Str " as \"equals\". In an assignment it means \"store the value on the right in the name on the left.\""]], [Plain [Str "Forgetting that ", Code ("", [], []) "/", Str " always gives a float, so ", Code ("", [], []) "10 / 2", Str " is ", Code ("", [], []) "5.0", Str ", not ", Code ("", [], []) "5", Str "."]], [Plain [Str "Expecting ", Code ("", [], []) "8 + 4 * 2", Str " to be 24. Multiplication happens first, so it is 16; use parentheses to change the order."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the value of ", Code ("", [], []) "8 + 4 * 2", Str ", ", Code ("", [], []) "(8 + 4) * 2", Str ", ", Code ("", [], []) "7 // 2", Str ", ", Code ("", [], []) "7 % 2", Str ", and ", Code ("", [], []) "2 ** 3", Str ", then check each in Python."]], [Plain [Str "Start with ", Code ("", [], []) "score = 82", Str " and write two statements that raise it by 9 and then double it. Predict the result."]], [Plain [Str "Join the strings ", Code ("", [], []) "\"Avery\"", Str " and ", Code ("", [], []) "\"Student\"", Str " with a space between them using ", Code ("", [], []) "+", Str "."]], [Plain [Str "Explain, in two sentences, why ", Code ("", [], []) "score = score + 9", Str " is valid even though it looks like an impossible equation."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Say operators by name when reading code aloud: 'double star' for ", Code ("", [], []) "**", Str ", 'double slash' for ", Code ("", [], []) "//", Str ", 'percent' for ", Code ("", [], []) "%", Str ". Raise your screen reader's punctuation level while reading expressions so that parentheses and operators are all announced."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can identify an expression in Python code."]], [Plain [Str "\9744", Space, Str "I can predict the result of simple Python expressions."]], [Plain [Str "\9744", Space, Str "I can explain how the assignment operator ", Code ("", [], []) "=", Str " works."]], [Plain [Str "\9744", Space, Str "I can demonstrate how to update a variable's value."]]], HorizontalRule, Header 3 ("lesson-23-input-and-output-revisited", ["unnumbered", "unlisted"], []) [Str "Lesson 2.3: Input and Output Revisited"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 2, pages 27–33"]], [Plain [Str "Matthes: Chapter 7, pages 114–116"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Use the ", Code ("", [], []) "input()", Str " function to ask the user for information."]], [Plain [Str "Provide a clear prompt message when using ", Code ("", [], []) "input()", Str "."]], [Plain [Str "Remember that ", Code ("", [], []) "input()", Str " returns a string, even for numbers."]], [Plain [Str "Combine text and variable values in a ", Code ("", [], []) "print()", Str " statement using f-strings."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("the-input-function", ["unnumbered", "unlisted"], []) [Str "The ", Code ("", [], []) "input()", Str " Function"], Para [Str "The ", Code ("", [], []) "input()", Str " function pauses program execution and waits for the user to type something and press Enter. ", Strong [Str "It always returns a string."]], CodeBlock ("", ["python"], []) "user_name = input(\"What is your name? \")
print(f\"Hello, {user_name}! Nice to meet you.\")
", Header 5 ("f-strings-formatted-string-literals", ["unnumbered", "unlisted"], []) [Str "F-Strings (Formatted String Literals)"], Para [Str "F-strings provide a clean way to embed variable values directly into a string:"], CodeBlock ("", ["python"], []) "name = \"Avery\"
age = 16
print(f\"Hello, {name}! You are {age} years old.\")
", Header 5 ("converting-input-for-calculations", ["unnumbered", "unlisted"], []) [Str "Converting Input for Calculations"], Para [Str "Since ", Code ("", [], []) "input()", Str " always returns a string, you must convert it for math:"], CodeBlock ("", ["python"], []) "age_str = input(\"How old are you? \")
age_int = int(age_str)
print(f\"Next year you will be {age_int + 1} years old.\")
", Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 2.3.1: Basic Input"]], CodeBlock ("", ["python"], []) "user_name = input(\"What is your name? \")
print(f\"Hello, {user_name}! Nice to meet you.\")
", Para [Strong [Str "Example 2.3.2: Numeric Input and Calculation"]], CodeBlock ("", ["python"], []) "user_name = input(\"Enter your name: \")

num1_str = input(\"Enter the first number: \")
num1 = int(num1_str)

num2_str = input(\"Enter the second number: \")
num2 = int(num2_str)

sum_result = num1 + num2
print(f\"Hello, {user_name}!\")
print(f\"The sum of {num1} and {num2} is {sum_result}.\")
", Para [Str "If the user types text that is not a whole number, ", Code ("", [], []) "int()", Str " raises a ", Code ("", [], []) "ValueError", Str ". Lesson 8.3 shows how to handle that."], Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Sample run (typed input shown after each prompt):"], CodeBlock ("", [""], []) "What is your name? Avery
Hello, Avery! Nice to meet you.
", Para [Str "Sample run (typed input shown after each prompt):"], CodeBlock ("", [""], []) "Enter your name: Avery
Enter the first number: 12
Enter the second number: 8
Hello, Avery!
The sum of 12 and 8 is 20.
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting that ", Code ("", [], []) "input()", Str " always returns text. ", Code ("", [], []) "\"12\" + \"8\"", Str " joins the text to make ", Code ("", [], []) "\"128\"", Str ", and does not add."]], [Plain [Str "Calling ", Code ("", [], []) "int()", Str " on text that is not a whole number, which raises a ", Code ("", [], []) "ValueError", Str "."]], [Plain [Str "Writing a prompt that does not say what to type, such as ", Code ("", [], []) "input(\"> \")", Str "."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], Para [Strong [Str "Activity 2.3.1: Temperature Converter"]], CodeBlock ("", ["python"], []) "fahrenheit_str = input(\"Enter temperature in Fahrenheit: \")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit - 32) * 5 / 9
print(f\"{fahrenheit}°F is {celsius:.2f}°C\")
", Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Write each prompt as a complete sentence that says what to enter, such as ", Code ("", [], []) "Enter the first number: ", Str ", and end it with a space so the answer starts after it. Test the program with your screen reader to confirm the prompt is read before you start typing."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use the ", Code ("", [], []) "input()", Str " function to ask the user for information."]], [Plain [Str "\9744", Space, Str "I can provide a clear prompt message when using ", Code ("", [], []) "input()", Str "."]], [Plain [Str "\9744", Space, Str "I remember that ", Code ("", [], []) "input()", Str " returns a string, even for numbers."]], [Plain [Str "\9744", Space, Str "I can combine text and variable values in a ", Code ("", [], []) "print()", Str " statement using f-strings."]]], HorizontalRule, Header 3 ("lesson-24-computing-with-numbers-and-type-conversions", ["unnumbered", "unlisted"], []) [Str "Lesson 2.4: Computing with Numbers and Type Conversions"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 3, pages 41–48"]], [Plain [Str "Matthes: Chapter 2, pages 26–28"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Identify when to use an integer versus a float."]], [Plain [Str "Convert a string to an integer using ", Code ("", [], []) "int()", Str "."]], [Plain [Str "Convert a string to a float using ", Code ("", [], []) "float()", Str "."]], [Plain [Str "Convert a number to a string using ", Code ("", [], []) "str()", Str "."]], [Plain [Str "Apply type conversions to perform calculations on user input."]], [Plain [Str "Understand and can apply the order of operations."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("integers-and-floats", ["unnumbered", "unlisted"], []) [Str "Integers and Floats"], Table ("", [], []) (Caption Nothing []) [(AlignDefault, ColWidthDefault), (AlignDefault, ColWidthDefault), (AlignDefault, ColWidthDefault)] (TableHead ("", [], []) [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Type"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Description"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Example"]]]]) [(TableBody ("", [], []) (RowHeadColumns 0) [] [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "int"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Whole numbers (exact)"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "5", Str ", ", Code ("", [], []) "-20", Str ", ", Code ("", [], []) "1000000"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "float"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Numbers with decimals"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "3.14", Str ", ", Code ("", [], []) "-2.5", Str ", ", Code ("", [], []) "6.0"]]]])] (TableFoot ("", [], []) []), Para [Strong [Str "Key behaviors:"]], BulletList [[Plain [Str "Division ", Code ("", [], []) "/", Str " always returns a float: ", Code ("", [], []) "10 / 2", Str " → ", Code ("", [], []) "5.0"]], [Plain [Str "Floor division ", Code ("", [], []) "//", Str " returns the integer part: ", Code ("", [], []) "10 // 3", Str " → ", Code ("", [], []) "3"]], [Plain [Str "Mixed operations promote to float: ", Code ("", [], []) "10 + 3.5", Str " → ", Code ("", [], []) "13.5"]]], Header 5 ("type-conversion-functions", ["unnumbered", "unlisted"], []) [Str "Type Conversion Functions"], CodeBlock ("", ["python"], []) "int(\"123\")      # → 123  (truncates: int(3.9) → 3)
float(\"3.14\")   # → 3.14
str(42)         # → \"42\"
", Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 2.4.1: Type Conversion"]], CodeBlock ("", ["python"], []) "num_str = \"123\"
num_int = int(num_str)
print(f\"String '{num_str}' as integer: {num_int}, type: {type(num_int)}\")

num_float = float(num_str)
print(f\"String '{num_str}' as float: {num_float}, type: {type(num_float)}\")

my_number = 42
my_text = str(my_number)
print(f\"Integer {my_number} as string: '{my_text}', type: {type(my_text)}\")
", Para [Strong [Str "Common Type Error:"]], CodeBlock ("", ["python"], []) "# This will cause a TypeError:
# print(\"My age is \" + 14)
# Fix: print(\"My age is \" + str(14))
# Or: print(f\"My age is {14}\")
", Para [Strong [Str "Example 2.4.2: Tip Calculator (shared calculator values)"]], CodeBlock ("", ["python"], []) "bill = 24.5
tip_rate = 0.15

tip = bill * tip_rate
total = bill + tip

print(f\"Bill: {bill:.2f}\")
print(f\"Tip: {tip:.2f}\")
print(f\"Total: {total:.2f}\")
", Para [Str "The unrounded values are 3.675 and 28.175. Python's ", Code ("", [], []) ":.2f", Str " formatting displays 3.67 and 28.18. This is binary floating-point behavior, not a mistake in the program; other languages may round the tip to 3.68."], Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Bill: 24.50
Tip: 3.67
Total: 28.18
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Converting with ", Code ("", [], []) "int()", Str " and expecting rounding. ", Code ("", [], []) "int(3.9)", Str " is ", Code ("", [], []) "3", Str " because it removes the fraction."]], [Plain [Str "Expecting ", Code ("", [], []) "0.1 + 0.2", Str " to equal exactly ", Code ("", [], []) "0.3", Str ". Floating-point numbers are approximations."]], [Plain [Str "Forgetting to convert typed text before arithmetic, then seeing ", Code ("", [], []) "TypeError", Str " or joined text instead of a sum."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], Para [Strong [Str "Activity 2.4.1: Mixed Bag Calculator"]], CodeBlock ("", ["python"], []) "age_str = input(\"Enter your age: \")
age = int(age_str)

height_str = input(\"Enter your height in meters: \")
height = float(height_str)

phrase = input(\"Enter a short phrase: \")

print(f\"Age doubled: {age * 2}\")
print(f\"Height in centimeters: {height * 100:.1f}\")
print(f\"Phrase length: {len(phrase)} characters\")
", Para [Str "Sample run (typed input shown after each prompt):"], CodeBlock ("", [""], []) "Enter your age: 16
Enter your height in meters: 1.72
Enter a short phrase: Computer Science
Age doubled: 32
Height in centimeters: 172.0
Phrase length: 16 characters
", Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "When printing floating-point results, format them (", Code ("", [], []) ":.2f", Str ") so the screen reader reads a short number instead of a long unrounded one. Read the type names printed by ", Code ("", [], []) "type()", Str " aloud, and note that ", Code ("", [], []) "<class 'int'>", Str " is announced with its angle brackets."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can identify when to use an integer versus a float."]], [Plain [Str "\9744", Space, Str "I can convert a string to an integer using ", Code ("", [], []) "int()", Str "."]], [Plain [Str "\9744", Space, Str "I can convert a string to a float using ", Code ("", [], []) "float()", Str "."]], [Plain [Str "\9744", Space, Str "I can convert a number to a string using ", Code ("", [], []) "str()", Str "."]], [Plain [Str "\9744", Space, Str "I can apply type conversions to perform calculations on user input."]], [Plain [Str "\9744", Space, Str "I understand and can apply the order of operations."]]], HorizontalRule, Header 3 ("lesson-25-using-the-math-library", ["unnumbered", "unlisted"], []) [Str "Lesson 2.5: Using the Math Library"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 3, pages 49–51"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain what a Python module is."]], [Plain [Str "Import the ", Code ("", [], []) "math", Str " module into my program."]], [Plain [Str "Use ", Code ("", [], []) "math.pi", Str " and ", Code ("", [], []) "math.sqrt()", Str "."]], [Plain [Str "Use ", Code ("", [], []) "math.ceil()", Str " to round up and ", Code ("", [], []) "math.floor()", Str " to round down."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("importing-the-math-module", ["unnumbered", "unlisted"], []) [Str "Importing the Math Module"], CodeBlock ("", ["python"], []) "import math
", Header 5 ("key-math-functions-and-constants", ["unnumbered", "unlisted"], []) [Str "Key Math Functions and Constants"], Table ("", [], []) (Caption Nothing []) [(AlignDefault, (ColWidth 0.4634146341463415)), (AlignDefault, (ColWidth 0.3170731707317073)), (AlignDefault, (ColWidth 0.21951219512195122))] (TableHead ("", [], []) [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Function/Constant"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Description"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Example"]]]]) [(TableBody ("", [], []) (RowHeadColumns 0) [] [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.pi"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "π ≈ 3.14159"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.pi"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.e"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "e ≈ 2.71828"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.e"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.sqrt(x)"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Square root of x"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.sqrt(25)", Str " → ", Code ("", [], []) "5.0"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.pow(x, y)"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "x raised to power y"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.pow(2, 4)", Str " → ", Code ("", [], []) "16.0"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.ceil(x)"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Round up"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.ceil(4.2)", Str " → ", Code ("", [], []) "5"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.floor(x)"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Round down"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.floor(4.8)", Str " → ", Code ("", [], []) "4"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.log(x, base)"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Logarithm"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.log(100, 10)", Str " → ", Code ("", [], []) "2.0"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.sin(x)"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Sine (in radians)"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.sin(math.pi/2)", Str " → ", Code ("", [], []) "1.0"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.radians(deg)"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Convert degrees to radians"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "math.radians(90)"]]]])] (TableFoot ("", [], []) []), Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 2.5.1: Circle Calculations"]], CodeBlock ("", ["python"], []) "import math

radius = 5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f\"Area of circle with radius {radius}: {area:.2f}\")
print(f\"Circumference: {circumference:.2f}\")

number = 81
square_root = math.sqrt(number)
print(f\"Square root of {number}: {square_root}\")
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output of example 1:"], CodeBlock ("", [""], []) "Area of circle with radius 5: 78.54
Circumference: 31.42
Square root of 81: 9.0
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting ", Code ("", [], []) "import math", Str ", so ", Code ("", [], []) "math.sqrt", Str " raises a ", Code ("", [], []) "NameError", Str "."]], [Plain [Str "Writing ", Code ("", [], []) "math.pi * radius * 2", Str " for the area. The radius must be squared: ", Code ("", [], []) "math.pi * radius ** 2", Str "."]], [Plain [Str "Expecting ", Code ("", [], []) "math.sqrt(81)", Str " to print ", Code ("", [], []) "9", Str ". It prints ", Code ("", [], []) "9.0", Str " because square roots are floats."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], Para [Strong [Str "Activity 2.5.1: Circle Calculator"]], CodeBlock ("", ["python"], []) "import math

radius_str = input(\"Enter the radius: \")
radius = float(radius_str)

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f\"Area: {area:.2f}\")
print(f\"Circumference: {circumference:.2f}\")
", Para [Strong [Str "Activity 2.5.2: Distance Finder"]], CodeBlock ("", ["python"], []) "import math

x = float(input(\"Enter x coordinate: \"))
y = float(input(\"Enter y coordinate: \"))
distance = math.sqrt(x**2 + y**2)
print(f\"Distance from origin: {distance:.2f}\")
", Para [Str "Sample run with the shared coordinates x = 3 and y = 4 (typed input shown after each prompt):"], CodeBlock ("", [""], []) "Enter x coordinate: 3
Enter y coordinate: 4
Distance from origin: 5.00
", Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Round results with ", Code ("", [], []) ":.2f", Str " so the screen reader announces ", Code ("", [], []) "78.54", Str " rather than fifteen digits. Say the dotted names aloud ('math dot sqrt') and listen for the dot, since a missing dot is a common transcription mistake when reading code by ear."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain what a Python module is."]], [Plain [Str "\9744", Space, Str "I can import the ", Code ("", [], []) "math", Str " module into my program."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "math.pi", Str " and ", Code ("", [], []) "math.sqrt()", Str "."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "math.ceil()", Str " to round up and ", Code ("", [], []) "math.floor()", Str " to round down."]]], Header 3 ("canonical-shared-dataset--calculator-and-coordinates", ["unnumbered", "unlisted"], []) [Str "Canonical Shared Dataset — Calculator and Coordinates"], Para [Str "Use the canonical bill and tip rate in every parallel-language implementation."], CodeBlock ("", ["python"], []) "from decimal import Decimal, ROUND_HALF_UP

bill = Decimal(\"24.50\")
tip_rate = Decimal(\"0.15\")
tip = (bill * tip_rate).quantize(Decimal(\"0.01\"), rounding=ROUND_HALF_UP)
total = bill + tip
print(f\"Tip: ${tip:.2f}\")
print(f\"Total: ${total:.2f}\")
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "Tip: $3.68
Total: $28.18
", Para [Str "Use the same coordinate values for the math-library example:"], CodeBlock ("", ["python"], []) "import math
x, y = 3, 4
distance = math.sqrt(x**2 + y**2)
print(distance)
", Para [Str "Expected output: ", Code ("", [], []) "5.0", Str ". The shared monetary contract rounds the tip to cents using decimal half-up rounding before adding it to the bill. Use decimal arithmetic rather than binary floating-point formatting for currency."]]