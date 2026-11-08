<<<<<<< HEAD
# Kotlin: Testing, analysis, and projects

This course sequence aligns Kotlin with the shared 12-unit curriculum map. Each mapped lesson includes all nine standard instructional sections. Examples target Kotlin/JVM. The terminal-first workflow is the default for accessible, reproducible work.

### Lesson 9.1: Testing a Function

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 9; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun grade(s:Int)=if(s>=60)"Pass" else "Retry"
fun main(){ check(grade(60)=="Pass"); check(grade(59)=="Retry"); println("Grade boundary checks passed") }
```

#### Expected Behavior or Output
Both assertions pass and print Grade boundary checks passed.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 9.2: Testing a Class

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 9; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ class InventoryItem(var quantity:Int){ fun removeOne(){require(quantity>0);quantity--} }; val item=InventoryItem(2); item.removeOne(); check(item.quantity==1); println("Inventory state test passed") }
```

#### Expected Behavior or Output
The assertion confirms quantity becomes 1 and prints Inventory state test passed.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 9.3: Introduction to Random Numbers

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 9; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ val roll=kotlin.random.Random(42).nextInt(1,7); check(roll in 1..6); println("Roll is within 1..6: "+(roll in 1..6)) }
```

#### Expected Behavior or Output
The seeded value is checked to be within 1 through 6; prints Roll is within 1..6: true.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 9.4: Analyzing Text Data

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 9; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ val text="A student studies programming. Programming develops skills."; val counts=text.lowercase().split(Regex("[^a-z]+")).filter(String::isNotBlank).groupingBy{it}.eachCount(); println("programming="+counts["programming"]+"; student="+counts["student"]) }
```

#### Expected Behavior or Output
Prints programming=2; student=1; tokens are lowercase alphabetic sequences.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 9.5: Working with CSV Data

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 9; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ val header="id,title,done"; val row="1,Read chapter,false"; val names=header.split(','); val fields=row.split(','); check(names.size==fields.size); println(names.zip(fields).toMap()) }
```

#### Expected Behavior or Output
Prints {id=1, title=Read chapter, done=false}. This simple row has no quoted commas; use a CSV library for general files.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 10.1: Designing Your Project

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 10; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ data class Requirement(val id:String,val acceptance:String); val plan=listOf(Requirement("R1","List records"),Requirement("R2","Add a record"),Requirement("R3","Persist changes")); plan.forEach{println(it.id+": "+it.acceptance)} }
```

#### Expected Behavior or Output
Prints three ordered requirements: list records, add a record, and persist changes.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 10.2: Building a Text-Based Adventure Game — Movement

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 10; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ val exits=mapOf("start_room" to mapOf("north" to "tunnel"),"tunnel" to mapOf("south" to "start_room","east" to "clearing"),"clearing" to mapOf("west" to "tunnel","north" to "locked_door_room"),"locked_door_room" to mapOf("south" to "clearing"),"treasure_room" to emptyMap<String,String>()); val room="start_room"; val direction="north"; println(exits[room]?.get(direction)?:"You cannot go that way.") }
```

#### Expected Behavior or Output
Prints tunnel; an absent exit produces the blocked-movement message. The locked_door_room north exit is conditional on using shiny key.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 10.3: Building a Text-Based Adventure Game — Inventory and Puzzle

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 10; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ val room="locked_door_room"; val inventory=setOf("shiny key"); val canUnlock=room=="locked_door_room" && "shiny key" in inventory; println(if(canUnlock)"The door unlocks." else "The door remains locked.") }
```

#### Expected Behavior or Output
Prints The door unlocks. because the shiny key is used while the player is in locked_door_room; using it elsewhere or without it leaves the door locked.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 10.4: Developing a Command-Line To-Do Tool

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 10; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ data class Task(val id:Int,val title:String,val description:String,val done:Boolean,val createdAt:String); val tasks=mutableListOf(Task(1,"Study","Review Kotlin",false,"2026-11-01")); tasks+=Task(2,"Practice","Trace a loop",false,"2026-11-01"); println(tasks.joinToString{it.id.toString()+":"+it.title}) }
```

#### Expected Behavior or Output
Prints 1:Study, 2:Practice; each task preserves id, title, description, completion state, and creation date.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 10.5: Refinement and User Experience

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 10; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun response(command:String)=when(command.lowercase()){ "list"->"Showing tasks"; "add"->"Enter a task title"; "quit"->"Goodbye"; else->"Unknown command; enter list, add, or quit" }
fun main(){ println(response("ADD")); println(response("remove")) }
```

#### Expected Behavior or Output
Prints Enter a task title and then Unknown command; enter list, add, or quit.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 11.1: Introduction to the Accessible Personal Data Manager

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 11; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ data class Record(val id:Int,val title:String,val description:String,val category:String,val createdAt:String,val updatedAt:String); val r=Record(1,"Plan","Course work","School","2026-11-01","2026-11-01"); println("Record "+r.id+": "+r.title+" ("+r.category+")") }
```

#### Expected Behavior or Output
Prints Record 1: Plan (School); the model contains all six shared capstone fields.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 11.2: Data Model, Validation, and Storage

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 11; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun validTitle(s:String)=s.isNotBlank()
fun validCategory(s:String,allowed:Set<String>)=s in allowed
fun main(){ println(validTitle("Plan")); println(validTitle("   ")); println(validCategory("School",setOf("School","Personal"))) }
```

#### Expected Behavior or Output
Prints true, false, true; whitespace-only titles and unknown categories are rejected.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 11.3: Displaying and Managing Items

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 11; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ data class Record(val id:Int,val title:String,val category:String); val records=listOf(Record(1,"Plan","School"),Record(2,"Call","Personal")); records.sortedBy{it.id}.forEach{println(it.id.toString()+": "+it.title+" ["+it.category+"]")} }
```

#### Expected Behavior or Output
Prints records in identifier order with title and category; production interface should also define empty-state behavior.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---

### Lesson 11.4: Searching, Updating, and Deleting Records

#### Reading References
- [Kotlin documentation](https://kotlinlang.org/docs/home.html)
- Shared capstone acceptance criteria and accessible interface requirements.

#### Learning Objectives
- Implement search, update, and delete operations using stable record identifiers and clearly defined matching rules.
- Preserve the shared record schema and user-facing behavior.
- Verify the operation with deterministic tests.

#### Concept Explanation
Treat each operation as a defined state transition. Validate input before changing stored data, preserve identifiers, update timestamps consistently, and report success or failure in text. A terminal menu is an appropriate Kotlin/JVM implementation; a visual interface is not required.

#### Worked Example

```kotlin
fun main(){ data class Record(val id:Int,val title:String); val records=listOf(Record(1,"Plan"),Record(2,"Read"),Record(3,"Plan review")); val matches=records.filter{it.title.contains("plan",ignoreCase=true)}; println(matches.map{it.id}); val updated=records.map{if(it.id==2)it.copy(title="Read chapter") else it}; val remaining=updated.filterNot{it.id==1}; println(remaining) }
```

#### Expected Behavior or Output
Search returns identifiers [1, 3]. Update changes record 2; delete removes record 1 and leaves records 2 and 3.

#### Common Mistakes
- Updating the wrong record when identifiers are duplicated or missing.
- Mutating stored data before validation succeeds.
- Reporting success when persistence fails.
- Omitting a regression test for the state transition.

#### Activities
1. Specify preconditions and postconditions for the operation.
2. Test an existing identifier, an unknown identifier, and an empty collection.
3. Verify that unrelated records remain unchanged.
4. Add a persistence round-trip test.

#### Accessibility Practice
Use explicit menu labels, predictable result messages, and keyboard-operable commands. Announce validation failures and successful state changes in text; never communicate state only through color or position.

#### Skills Checklist
- [ ] I can explain the operation's preconditions and postconditions.
- [ ] I can preserve the shared record schema.
- [ ] I can test success, missing-record, and invalid-input cases.
- [ ] I can verify the operation using keyboard and screen-reader output.

---

### Lesson 11.5: Completion State, Persistence, and Acceptance Tests

#### Reading References
- [Kotlin documentation](https://kotlinlang.org/docs/home.html)
- Shared capstone acceptance criteria and accessible interface requirements.

#### Learning Objectives
- Implement completion-state changes and verify the complete CRUD workflow, JSON persistence, and accessible text feedback.
- Preserve the shared record schema and user-facing behavior.
- Verify the operation with deterministic tests.

#### Concept Explanation
Treat each operation as a defined state transition. Validate input before changing stored data, preserve identifiers, update timestamps consistently, and report success or failure in text. A terminal menu is an appropriate Kotlin/JVM implementation; a visual interface is not required.

#### Worked Example

```kotlin
fun main(){ data class Record(val id:Int,val title:String,val done:Boolean); val original=listOf(Record(1,"Plan",false),Record(2,"Read",true)); val completed=original.map{if(it.id==1)it.copy(done=true) else it}; check(completed.count{it.done}==2); check(completed.first{it.id==1}.title=="Plan"); println("Completion and preservation checks passed") }
```

#### Expected Behavior or Output
Both assertions pass; record 1 becomes complete, its title is unchanged, and record 2 is preserved.

#### Common Mistakes
- Updating the wrong record when identifiers are duplicated or missing.
- Mutating stored data before validation succeeds.
- Reporting success when persistence fails.
- Omitting a regression test for the state transition.

#### Activities
1. Specify preconditions and postconditions for the operation.
2. Test an existing identifier, an unknown identifier, and an empty collection.
3. Verify that unrelated records remain unchanged.
4. Add a persistence round-trip test.

#### Accessibility Practice
Use explicit menu labels, predictable result messages, and keyboard-operable commands. Announce validation failures and successful state changes in text; never communicate state only through color or position.

#### Skills Checklist
- [ ] I can explain the operation's preconditions and postconditions.
- [ ] I can preserve the shared record schema.
- [ ] I can test success, missing-record, and invalid-input cases.
- [ ] I can verify the operation using keyboard and screen-reader output.

---

=======
# Unit 9: Testing and Data Analysis

## Overview

Write tests with expected results, test random code by its properties, analyze the shared text sample, and read the shared CSV file.

---


## Lesson 9.1: Testing Functions

### Reading References
- [Functions](https://kotlinlang.org/docs/functions.html)
- [Functions](https://kotlinlang.org/docs/functions.html)
- Matching Python lesson: Lesson 9.1: Testing Your Code

### Learning Objectives
- Write checks with chosen inputs and expected results.
- Compare decimals with a tolerance.
- Test boundary values and report failure with an exit status.

### Concept Explanation

A *test* runs code with chosen inputs and compares the result with a value decided in advance. Real Kotlin projects use the `kotlin.test` library with JUnit, added through Gradle. To keep this course free of build tooling, the example uses a tiny `check` function; the habits (inputs, expected values, boundaries) are the same.

Decimal results are compared with a *tolerance*, not `==`, because of floating-point approximation: the tip for 24.50 at 0.15 is stored as 3.6749999999999998, so the test checks that it is within a tiny distance of 3.675.

The same tests appear in every language track: `add(5, 3)` is 8, `add(-5, -3)` is -8, `add(10, -4)` is 6, the tip is 3.675, and the grade boundaries 90, 89, 60, and 59 give A, B, D, and F.

`exitProcess(1)` ends the program with a failure status when any check fails, so other tools can notice.

### Worked Example

```kotlin
import kotlin.math.abs
import kotlin.system.exitProcess

fun add(a: Int, b: Int) = a + b

fun calculateTip(bill: Double, rate: Double) = bill * rate

fun classify(score: Int): String = when {
    score >= 90 -> "A"
    score >= 80 -> "B"
    score >= 70 -> "C"
    score >= 60 -> "D"
    else -> "F"
}

var passed = 0
var failed = 0

fun <T> check(name: String, actual: T, expected: T) {
    if (actual == expected) {
        passed++
        println("PASS $name")
    } else {
        failed++
        println("FAIL $name: expected $expected but got $actual")
    }
}

fun checkClose(name: String, actual: Double, expected: Double, tolerance: Double = 1e-9) {
    check(name, abs(actual - expected) <= tolerance, true)
}

fun main() {
    check("add 5 and 3", add(5, 3), 8)
    check("add -5 and -3", add(-5, -3), -8)
    check("add 10 and -4", add(10, -4), 6)
    checkClose("tip on 24.50 at 0.15", calculateTip(24.5, 0.15), 3.675)
    check("tip on a zero bill", calculateTip(0.0, 0.15), 0.0)
    check("classify 90", classify(90), "A")
    check("classify 89", classify(89), "B")
    check("classify 60", classify(60), "D")
    check("classify 59", classify(59), "F")

    println("$passed passed, $failed failed")
    if (failed > 0) exitProcess(1)
}
```

### Expected Behavior or Output

The program prints:
```text
PASS add 5 and 3
PASS add -5 and -3
PASS add 10 and -4
PASS tip on 24.50 at 0.15
PASS tip on a zero bill
PASS classify 90
PASS classify 89
PASS classify 60
PASS classify 59
9 passed, 0 failed
```

### Common Mistakes
1. Comparing decimal results with `==`.
2. Testing only typical values and skipping the boundaries 90, 89, 60, and 59.
3. Writing the expected value after seeing the output, which turns the test into a copy of the bug.

### Activities
1. Change one expected value so a check fails, read the message, and restore it.
2. Add checks for the grades at 80, 79, 70, and 69.
3. Write checks for `isPassing(score)` before writing the function.
4. Explain why the tip check uses a tolerance.

### Accessibility Practice

Each check prints one complete line that starts with PASS or FAIL, and the last line gives the counts, so the result can be understood from the first word of each line and the final summary.

### Skills Checklist
- [ ] I can write a check with an expected value.
- [ ] I can compare decimals with a tolerance.
- [ ] I can choose boundary tests.
- [ ] I can read PASS and FAIL lines.
- [ ] I know how to signal failure with an exit status.

---

## Lesson 9.2: Testing Classes

### Reading References
- [Classes](https://kotlinlang.org/docs/classes.html)
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 9.2: Testing a Class

### Learning Objectives
- Create a fresh object for every test.
- Test a value, a change of state, and an error.
- Use `runCatching` to test that an error occurs.

### Concept Explanation

Each test should start from a known state, so create a new object for every test with a *setup* function. Tests that share an object can affect each other and fail in confusing ways.

Test three kinds of behavior: that a function returns the right value (`totalValue` for 3 at 2.50 is 7.5), that a function changes the object correctly (restocking 2 makes the quantity 5), and that invalid use is rejected (restocking a negative amount throws).

`runCatching { ... }.isFailure` is true when the block throws, so a test can assert that an error *does* happen.

### Worked Example

```kotlin
import kotlin.math.abs

class Item(val name: String, var quantity: Int, val unitPrice: Double) {
    fun totalValue(): Double = quantity * unitPrice

    fun restock(amount: Int) {
        require(amount >= 0) { "amount must not be negative" }
        quantity += amount
    }
}

fun setup() = Item("Notebook", 3, 2.50)

var failures = 0

fun test(name: String, body: () -> Unit) {
    val result = runCatching(body)
    if (result.isSuccess) {
        println("PASS $name")
    } else {
        failures++
        println("FAIL $name: ${result.exceptionOrNull()?.message}")
    }
}

fun assertThat(condition: Boolean, message: String) {
    if (!condition) throw AssertionError(message)
}

fun main() {
    test("total value is 7.5") {
        assertThat(abs(setup().totalValue() - 7.5) < 1e-9, "wrong total")
    }

    test("restock adds to the quantity") {
        val item = setup()
        item.restock(2)
        assertThat(item.quantity == 5, "quantity should be 5")
    }

    test("restock rejects a negative amount") {
        val failed = runCatching { setup().restock(-1) }.isFailure
        assertThat(failed, "an error should have been thrown")
    }

    println(if (failures == 0) "All tests passed." else "$failures test(s) failed.")
}
```

### Expected Behavior or Output

The program prints:
```text
PASS total value is 7.5
PASS restock adds to the quantity
PASS restock rejects a negative amount
All tests passed.
```

### Common Mistakes
1. Sharing one object between tests, so an earlier test changes the later ones.
2. Testing only the successful path and never the error path.
3. Writing an `assertThat` with no message, so a failure says nothing about what went wrong.

### Activities
1. Add a test that `restock(0)` leaves the quantity unchanged.
2. Add a test for an `isValid` function.
3. Break `restock` on purpose and read the failure line.
4. Explain why `setup` creates a new item each time.

### Accessibility Practice

Name each test as a short sentence that says what it checks, so the PASS and FAIL lines read as clear statements. Read the final summary line first.

### Skills Checklist
- [ ] I can create a fresh object per test.
- [ ] I can test a return value.
- [ ] I can test a change of state.
- [ ] I can test that an error is thrown.
- [ ] I can write a clear test name.

---

## Lesson 9.3: Random Numbers

### Reading References
- [Kotlin standard library: kotlin.random](https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.random/)
- Matching Python lesson: Lesson 9.3: Random Numbers and Simulation

### Learning Objectives
- Generate random integers and decimals.
- Use a seed to make results repeatable.
- Test random code by its properties.

### Concept Explanation

`kotlin.random.Random` produces random numbers. `Random.nextInt(from, until)` returns an integer from `from` up to but **not including** `until`, so a die roll is `nextInt(1, 7)`. `Random.nextDouble()` returns a decimal from 0.0 up to but not including 1.0, and `list.random(random)` picks a list element.

`Random(42)` creates a generator with a fixed *seed*: two generators with the same seed produce the same sequence. Without a seed the results change on every run. Because the exact sequence may differ between Kotlin versions, tests should check *properties* (every roll is between 1 and 6) and repeatability, not particular values.

### Worked Example

```kotlin
import kotlin.random.Random

fun main() {
    val first = Random(42)
    val second = Random(42)
    val firstRolls = List(5) { first.nextInt(1, 7) }
    val secondRolls = List(5) { second.nextInt(1, 7) }
    println("Same seed gives the same rolls: ${firstRolls == secondRolls}")

    val random = Random(7)
    val inRange = List(1000) { random.nextInt(1, 7) }.all { it in 1..6 }
    println("All rolls between 1 and 6: $inRange")

    val decimal = random.nextDouble()
    println("Decimal in [0, 1): ${decimal >= 0.0 && decimal < 1.0}")

    val scores = listOf(82, 91, 76, 88)
    val chosen = scores.random(random)
    println("Chosen score is from the list: ${chosen in scores}")
}
```

### Expected Behavior or Output

The program prints:
```text
Same seed gives the same rolls: true
All rolls between 1 and 6: true
Decimal in [0, 1): true
Chosen score is from the list: true
```

### Common Mistakes
1. Using `nextInt(1, 6)` for a die and never rolling a 6. The upper limit is excluded.
2. Testing for specific random values that may change between versions.
3. Creating a new unseeded generator for every roll, which wastes work and can repeat values.

### Activities
1. Run the program three times and compare.
2. Change the seeds and check that the property lines still print `true`.
3. Simulate 600 rolls and count how many of each face appeared (the counts will differ with the seed).
4. Explain why a test should check a property rather than a specific random number.

### Accessibility Practice

Print yes or no style results for random behavior, so the announced output is the same on every run and the screen reader does not read unpredictable values.

### Skills Checklist
- [ ] I can use `nextInt` with an excluded upper limit.
- [ ] I can set a seed.
- [ ] I can test properties of random code.
- [ ] I know sequences can differ between versions.
- [ ] I can pick a random list item.

---

## Lesson 9.4: Text Analysis

### Reading References
- [Strings](https://kotlinlang.org/docs/strings.html)
- [Grouping](https://kotlinlang.org/docs/collection-grouping.html)
- Matching Python lesson: Lesson 9.4: Data Analysis - Text Analysis

### Learning Objectives
- Split text into words and count them.
- Count word and letter frequencies with `groupingBy`.
- Produce stable, sorted output.

### Concept Explanation

Splitting uses `split`: `cleaned.split(" ")` or a regular expression such as `Regex("\\s+")` for any run of spaces. Counting is a one-liner with `groupingBy { it }.eachCount()`, which returns a map from each item to its count.

Map order is only stable if you make it so. `eachCount()` keeps the order in which items first appeared, and sorting with `sortedWith(compareBy({ -it.value }, { it.key }))` orders by count (highest first) and then alphabetically, so ties print in a fixed order.

The shared text sample is "A student studies programming. Programming develops problem-solving skills." After lower-casing and removing the periods it has 8 words, and `programming` appears twice.

### Worked Example

```kotlin
fun main() {
    val text = "A student studies programming. Programming develops problem-solving skills."
    val words = text.lowercase().replace(".", "").split(" ")

    println("Word count: ${words.size}")
    println("Word frequencies:")
    for ((word, count) in words.groupingBy { it }.eachCount()) {
        println("'$word': $count")
    }

    val letters = text.lowercase().filter { it.isLetter() }.groupingBy { it }.eachCount()
    val topThree = letters.entries.sortedWith(compareBy({ -it.value }, { it.key })).take(3)
    println("Most common letters:")
    for ((letter, count) in topThree) {
        println("$letter: $count")
    }
}
```

### Expected Behavior or Output

The program prints:
```text
Word count: 8
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
```

### Common Mistakes
1. Counting punctuation as part of a word, so `programming.` and `programming` are different words.
2. Forgetting to lower-case first, so `Programming` and `programming` are counted separately.
3. Relying on map order for tied counts without a tie-break.

### Activities
1. Predict the word count and the count for `programming` before running.
2. Count the words longer than 8 letters.
3. Print the longest word.
4. Change the sort so ties are listed in reverse alphabetical order.

### Accessibility Practice

Read the frequency list in its fixed order. Because the order is stable, you can learn it and compare runs by ear. Print each pair as a short sentence with the same wording every time.

### Skills Checklist
- [ ] I can split text into words.
- [ ] I can count frequencies with `groupingBy`.
- [ ] I can sort with a tie-break.
- [ ] I can remove punctuation first.
- [ ] I can read a stable report.

---

## Lesson 9.5: Working with CSV Files

### Reading References
- [Kotlin standard library: kotlin.io](https://kotlinlang.org/docs/../api/latest/jvm/stdlib/kotlin.io/)
- [Strings](https://kotlinlang.org/docs/strings.html)
- Matching Python lesson: Lesson 9.5: Data Analysis - CSV Files

### Learning Objectives
- Create and read a CSV file.
- Split lines into fields and convert numbers.
- Compute an average and a count.

### Concept Explanation

A CSV (comma-separated values) file stores a table as text. The first line names the columns and each later line is a record. The shared student file has the columns `student_id`, `first_name`, `last_name`, `score`, and `active`, and three records.

The standard library has no CSV reader. `line.split(",")` works only for **simple** files: a value that contains a comma inside quotation marks, such as `"Smith, Jr."`, would be split wrongly. For such files use a maintained library or write a real parser.

Every field is text. Convert the score with `toInt()` and compare `active` with the text `"true"`. With scores 91, 82, and 76 the average is 83.00, and two students are active.

### Worked Example

```kotlin
import java.io.File

fun main() {
    val file = File("students.csv")
    file.writeText(
        "student_id,first_name,last_name,score,active\n" +
            "1,Avery,Student,91,true\n" +
            "2,Jordan,Lee,82,true\n" +
            "3,Casey,Smith,76,false\n"
    )

    if (!file.exists()) {
        println("Error: students.csv was not found.")
        return
    }
    val lines = file.readLines()
    println("Columns: " + lines.first().split(",").joinToString(", "))

    var total = 0
    var active = 0
    val students = lines.drop(1)
    for (line in students) {
        val row = line.split(",")
        val score = row[3].toInt()
        total += score
        if (row[4] == "true") active++
        println("${row[0]}: ${row[1]} ${row[2]} scored $score")
    }

    println("Students: ${students.size}")
    println("Average score: " + "%.2f".format(total.toDouble() / students.size))
    println("Active students: $active")
}
```

### Expected Behavior or Output

The program prints:
```text
Columns: student_id, first_name, last_name, score, active
1: Avery Student scored 91
2: Jordan Lee scored 82
3: Casey Smith scored 76
Students: 3
Average score: 83.00
Active students: 2
```

### Common Mistakes
1. Splitting a CSV line at every comma when a value contains a quoted comma.
2. Forgetting to convert the text in the score column to a number.
3. Not skipping the header line, so `toInt()` fails on the text `score`.

### Activities
1. Predict the printed lines before running.
2. Add a fourth student and check the new average.
3. Print only the active students.
4. Explain, with an example, why `"Smith, Jr."` breaks `split(",")`.

### Accessibility Practice

Print one student per line with the same wording each time, so the screen reader announces a repeating pattern that is easy to compare. Read the column names aloud once at the start.

### Skills Checklist
- [ ] I can write and read a CSV file.
- [ ] I can split a line into fields.
- [ ] I convert text fields to numbers.
- [ ] I can compute an average and a count.
- [ ] I know when `split` is not enough.

---

# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

Plan a text project, build the shared text adventure in two parts, build the command-line to-do manager, and refine input validation.

---


## Lesson 10.1: Planning a Text-Based Project

### Reading References
- [Functions: function types](https://kotlinlang.org/docs/lambdas.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 10.1: Project Planning and Design

### Learning Objectives
- Write a short requirements list.
- Design a command loop with a map of handlers.
- Plan in small steps and test each one.

### Concept Explanation

A project is easier to finish when it is planned in small steps. Write down what the program must do (*requirements*), what information it keeps (*data*), and the commands a person can give (*interface*). Build one small piece, test it, then add the next.

Text-based projects share a *command loop*: show a prompt, read a line, find the matching action, and repeat until the user quits. In Kotlin, a `Map<String, () -> Unit>` holds actions: the keys are command names and the values are *lambdas*, small functions with no name. A new command is one new entry, and an unknown command is a failed lookup that prints a helpful message.

The loop stops on `quit` and also when input ends (`null`). The example is a skeleton with two commands; typing `help`, `look`, an unknown word, and `quit` shows each path.

### Worked Example

```kotlin
fun main() {
    val commands: Map<String, () -> Unit> = mapOf(
        "help" to { println("Commands: help, look, quit") },
        "look" to { println("You are in a dark cave.") },
    )

    println("Type a command:")
    var line = readlnOrNull()
    while (line != null && line != "quit") {
        val handler = commands[line]
        if (handler != null) {
            handler()
        } else {
            println("I don't understand that command. Type help for a list.")
        }
        println("Type a command:")
        line = readlnOrNull()
    }
    println("Goodbye!")
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
help
look
dance
quit
```

the program prints:
```text
Type a command:
Commands: help, look, quit
Type a command:
You are in a dark cave.
Type a command:
I don't understand that command. Type help for a list.
Type a command:
Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
Type a command:
Goodbye!
```

### Common Mistakes
1. Starting to code before listing the requirements.
2. Using a long chain of `if` statements instead of a map of handlers.
3. Forgetting that an unknown command should say what to do next.

### Activities
1. Write five requirements for the text adventure and the to-do list.
2. Add a `score` command that prints the shared scores.
3. Add the aliases `h` and `l` without copying the lambdas.
4. Describe the data for the capstone in three sentences.

### Accessibility Practice

Prompts and responses are on separate lines and every response is a complete sentence. Test the prompts by listening to them before you add features.

### Skills Checklist
- [ ] I can list requirements.
- [ ] I can design a command loop.
- [ ] I can use a map of lambdas.
- [ ] I handle unknown commands.
- [ ] I handle the end of input.

---

## Lesson 10.2: Text Adventure, Part 1: Rooms and Movement

### Reading References
- [Data classes](https://kotlinlang.org/docs/data-classes.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 10.2: Building a Text-Based Adventure Game (Part 1)

### Learning Objectives
- Represent rooms and exits with a data class and a map.
- Move the player by command.
- Handle impossible moves and the end of input.

### Concept Explanation

A room is a data class with a `description` and an `exits` map from a direction to the *name* of another room. The program remembers the player's location in one variable. A move looks up the command in the current room's exits; if it is found, the location changes, otherwise the program explains that the move is impossible.

This is the same three-room layout as the Python course: a cave, a tunnel, and a clearing. Part 2 adds items and a locked door.

The example is played with north, east, west, up, south, and quit. The command `up` is not an exit anywhere, so it prints the help message.

### Worked Example

```kotlin
data class Room(val description: String, val exits: Map<String, String>)

fun main() {
    val rooms = mapOf(
        "start_room" to Room(
            "You are in a dimly lit cave. There's a narrow passage to the NORTH.",
            mapOf("north" to "tunnel"),
        ),
        "tunnel" to Room(
            "The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.",
            mapOf("south" to "start_room", "east" to "clearing"),
        ),
        "clearing" to Room(
            "You've reached a small, sunny clearing. A faint path leads WEST.",
            mapOf("west" to "tunnel"),
        ),
    )

    var current = "start_room"
    while (true) {
        println("---")
        println(rooms.getValue(current).description)
        println("What do you want to do?")
        val command = (readlnOrNull() ?: "quit").lowercase()
        val next = rooms.getValue(current).exits[command]
        if (next != null) {
            current = next
        } else if (command == "quit") {
            println("Exiting game. Goodbye!")
            break
        } else {
            println("I don't understand that command or you can't go that way.")
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
north
east
west
up
south
quit
```

the program prints:
```text
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You've reached a small, sunny clearing. A faint path leads WEST.
What do you want to do?
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
I don't understand that command or you can't go that way.
---
The tunnel is damp and cold. You can go SOUTH back to the cave or EAST to a clearing.
What do you want to do?
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
---
You are in a dimly lit cave. There's a narrow passage to the NORTH.
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Looking up a direction with `getValue`, which throws if the key is missing. Use `[]` for a nullable result.
2. Forgetting to treat the end of input as `quit`, so the program loops forever when input is piped in.
3. Misspelling a room name in `exits`, so a move leads to a room that does not exist.

### Activities
1. Trace the six commands by hand and write the room after each one.
2. Add a fourth room reached from the clearing and test it.
3. Add the aliases `n`, `s`, `e`, and `w`.
4. Write a loop that checks that every exit names a real room.

### Accessibility Practice

Each turn prints a separator line, the description, and the prompt, so a whole turn can be read in order. Listen to one turn from start to finish to confirm that a player could follow it without seeing the screen.

### Skills Checklist
- [ ] I can represent rooms with a data class.
- [ ] I can move the player by command.
- [ ] I can handle an impossible move.
- [ ] I treat end of input as quit.
- [ ] I can trace a game by hand.

---

## Lesson 10.3: Text Adventure, Part 2: Items and a Locked Door

### Reading References
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- [Control flow: when](https://kotlinlang.org/docs/control-flow.html#when-expression)
- Matching Python lesson: Lesson 10.3: Building a Text-Based Adventure Game (Part 2)

### Learning Objectives
- Keep items in rooms and in an inventory.
- Implement take and use commands.
- Block and then allow a move through a locked door.

### Concept Explanation

Part 2 adds *state*: items in rooms, an inventory, and a door that is locked until the player uses the key. This is the shared specification used by every language track: three rooms (`start`, `locked_door_room`, `treasure_room`); the commands `north`, `south`, `east`, `west`, `take shiny key`, `use shiny key`, and `quit`; the door between the chamber and the treasure room stays locked until the key is used there; reaching the treasure room ends the game.

Items are a mutable list of names inside each room. Taking an item removes it from the room's list and adds it to the inventory. The locked door is a Boolean variable, `doorLocked`. A move through the door checks it first.

The example is played with: north (into the chamber), north (the locked door refuses), south, take shiny key, north, use shiny key, north (the treasure room).

### Worked Example

```kotlin
class Room(
    val description: String,
    val exits: Map<String, String>,
    val items: MutableList<String> = mutableListOf(),
)

fun main() {
    val rooms = mapOf(
        "start" to Room("A dark cave.", mapOf("north" to "locked_door_room"), mutableListOf("shiny key")),
        "locked_door_room" to Room(
            "A small chamber with a heavy door to the NORTH.",
            mapOf("south" to "start", "north" to "treasure_room"),
        ),
        "treasure_room" to Room("A glittering room full of treasure. You win!", mapOf("south" to "locked_door_room")),
    )

    var current = "start"
    val inventory = mutableListOf<String>()
    var doorLocked = true

    while (true) {
        val room = rooms.getValue(current)
        println()
        println(room.description)
        if (current == "treasure_room") break
        if (room.items.isNotEmpty()) println("You see: ${room.items.joinToString(", ")}")
        println("Your inventory: ${if (inventory.isEmpty()) "empty" else inventory.joinToString(", ")}")
        println("What do you want to do?")

        val command = (readlnOrNull() ?: "quit").lowercase()
        when {
            command == "take shiny key" && "shiny key" in room.items -> {
                room.items.remove("shiny key")
                inventory.add("shiny key")
                println("You picked up the shiny key.")
            }
            command == "use shiny key" && current == "locked_door_room" && "shiny key" in inventory -> {
                doorLocked = false
                println("You unlocked the door!")
            }
            command in room.exits -> {
                if (current == "locked_door_room" && command == "north" && doorLocked) {
                    println("The door is locked! You need a key.")
                } else {
                    current = room.exits.getValue(command)
                }
            }
            command == "quit" -> {
                println("Exiting game. Goodbye!")
                break
            }
            else -> println("I don't understand that command.")
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
north
north
south
take shiny key
north
use shiny key
north
```

the program prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?
The door is locked! You need a key.

A small chamber with a heavy door to the NORTH.
Your inventory: empty
What do you want to do?

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?
You picked up the shiny key.

A dark cave.
Your inventory: shiny key
What do you want to do?

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?
You unlocked the door!

A small chamber with a heavy door to the NORTH.
Your inventory: shiny key
What do you want to do?

A glittering room full of treasure. You win!
```

With no standard input at all, the program ends cleanly and prints:
```text

A dark cave.
You see: shiny key
Your inventory: empty
What do you want to do?
Exiting game. Goodbye!
```

### Common Mistakes
1. Making the door's locked state part of the exits so that the "locked" message can never be reached.
2. Defining an exit to a room that is missing from the `rooms` map, which crashes when the player arrives.
3. Printing a fixed room description that still mentions an item after the player has taken it.

### Activities
1. Play the program with the shown commands and follow each turn on paper.
2. Try `use shiny key` in the cave and describe what happens.
3. Add a second item and require both to open the door.
4. List the game's state (location, inventory, door) and say which command changes each part.

### Accessibility Practice

The room description never mentions the key. A separate 'You see:' line lists items, so the description stays true after the key is taken and the screen reader announces the current state.

### Skills Checklist
- [ ] I can store items in rooms and an inventory.
- [ ] I can implement take and use commands.
- [ ] I can block and allow a move.
- [ ] I can list the game's state.
- [ ] I can keep descriptions true after state changes.

---

## Lesson 10.4: Command-Line To-Do List

### Reading References
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 10.4: Building a Command-Line To-Do List

### Learning Objectives
- Keep records with the shared fields.
- Save and load them as JSON.
- Offer add, view, mark-done, save, load, and quit commands.

### Concept Explanation

A to-do list ties together records, loops, functions, and files. Each task has the shared fields `id`, `title`, `description`, `done`, and `created_at`. The program keeps a list of tasks in memory, shows a numbered menu, and saves the list to `todos.json` when asked and on exit.

Saving uses the teaching JSON helper from Lesson 8.5, included here so the example runs on its own. At start-up the program loads the file if it exists. A missing file is normal on first use, and a damaged file must not crash the program: it prints a message and starts with an empty list.

New ids are one more than the highest existing id. The status is shown as the words `done` and `not done`, never with a symbol or color alone.

In the sample session the user adds two tasks, views the list, marks task 2 done, views it again, tries an invalid menu choice, views the list, and quits.

### Worked Example

```kotlin
object Json {
    fun encode(value: Any?): String = when (value) {
        null -> "null"
        is String -> quote(value)
        is Boolean, is Int, is Long, is Double -> value.toString()
        is Map<*, *> -> value.entries.sortedBy { it.key.toString() }
            .joinToString(",", "{", "}") { quote(it.key.toString()) + ":" + encode(it.value) }
        is List<*> -> value.joinToString(",", "[", "]") { encode(it) }
        else -> throw IllegalArgumentException("cannot encode ${value::class.simpleName}")
    }

    private fun quote(text: String): String {
        val out = StringBuilder("\"")
        for (c in text) {
            when {
                c == '"' -> out.append("\\\"")
                c == '\\' -> out.append("\\\\")
                c == '\n' -> out.append("\\n")
                c == '\r' -> out.append("\\r")
                c == '\t' -> out.append("\\t")
                c < ' ' -> out.append("\\u%04x".format(c.code))
                else -> out.append(c)
            }
        }
        return out.append('"').toString()
    }

    fun decode(text: String): Any? = Parser(text).parse()

    private class Parser(private val text: String) {
        private var pos = 0

        private fun fail(message: String): Nothing =
            throw IllegalArgumentException("$message at position $pos")

        private fun skip() {
            while (pos < text.length && text[pos].isWhitespace()) pos++
        }

        fun parse(): Any? {
            val result = value()
            skip()
            if (pos < text.length) fail("unexpected extra text")
            return result
        }

        private fun value(): Any? {
            skip()
            if (pos >= text.length) fail("unexpected end of text")
            val c = text[pos]
            return when {
                c == '{' -> obj()
                c == '[' -> list()
                c == '"' -> str()
                text.startsWith("true", pos) -> { pos += 4; true }
                text.startsWith("false", pos) -> { pos += 5; false }
                text.startsWith("null", pos) -> { pos += 4; null }
                c == '-' || c.isDigit() -> number()
                else -> fail("unexpected character")
            }
        }

        private fun number(): Any {
            val start = pos
            if (text[pos] == '-') pos++
            while (pos < text.length && (text[pos].isDigit() || text[pos] in ".eE+-")) pos++
            val token = text.substring(start, pos)
            return token.toLongOrNull() ?: token.toDoubleOrNull() ?: fail("bad number")
        }

        private fun str(): String {
            pos++
            val out = StringBuilder()
            while (true) {
                if (pos >= text.length) fail("unterminated string")
                val c = text[pos++]
                if (c == '"') return out.toString()
                if (c != '\\') { out.append(c); continue }
                if (pos >= text.length) fail("bad escape")
                when (text[pos++]) {
                    'n' -> out.append('\n')
                    't' -> out.append('\t')
                    'r' -> out.append('\r')
                    '"' -> out.append('"')
                    '\\' -> out.append('\\')
                    '/' -> out.append('/')
                    'u' -> {
                        if (pos + 4 > text.length) fail("bad escape")
                        out.append(text.substring(pos, pos + 4).toInt(16).toChar())
                        pos += 4
                    }
                    else -> fail("bad escape")
                }
            }
        }

        private fun obj(): Map<String, Any?> {
            pos++
            val map = LinkedHashMap<String, Any?>()
            skip()
            if (pos < text.length && text[pos] == '}') { pos++; return map }
            while (true) {
                skip()
                if (pos >= text.length || text[pos] != '"') fail("expected a key")
                val key = str()
                skip()
                if (pos >= text.length || text[pos] != ':') fail("expected ':'")
                pos++
                map[key] = value()
                skip()
                if (pos >= text.length) fail("unterminated object")
                val d = text[pos++]
                if (d == '}') return map
                if (d != ',') { pos--; fail("expected ',' or '}'") }
            }
        }

        private fun list(): List<Any?> {
            pos++
            val items = ArrayList<Any?>()
            skip()
            if (pos < text.length && text[pos] == ']') { pos++; return items }
            while (true) {
                items.add(value())
                skip()
                if (pos >= text.length) fail("unterminated list")
                val d = text[pos++]
                if (d == ']') return items
                if (d != ',') { pos--; fail("expected ',' or ']'") }
            }
        }
    }
}

val todoFile = java.io.File("todos.json")
var todos = mutableListOf<MutableMap<String, Any?>>()

fun loadTodos() {
    if (!todoFile.exists()) {
        println("No existing tasks found.")
        todos = mutableListOf()
        return
    }
    try {
        val data = Json.decode(todoFile.readText()) as List<*>
        todos = data.map { (it as Map<*, *>).entries.associate { e -> e.key.toString() to e.value }.toMutableMap() }.toMutableList()
        println("Tasks loaded.")
    } catch (e: Exception) {
        println("Error: todos.json is not valid JSON. Starting with an empty list.")
        todos = mutableListOf()
    }
}

fun saveTodos() {
    todoFile.writeText(Json.encode(todos))
    println("Tasks saved.")
}

fun nextId(): Long = (todos.maxOfOrNull { it["id"] as Long } ?: 0L) + 1

fun addTask(title: String, description: String) {
    if (title.isBlank()) {
        println("A title is required.")
        return
    }
    val stamp = java.time.LocalDateTime.now().format(java.time.format.DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss"))
    todos.add(mutableMapOf("id" to nextId(), "title" to title.trim(), "description" to description.trim(), "done" to false, "created_at" to stamp))
    println("Task '${title.trim()}' added.")
}

fun viewTasks() {
    if (todos.isEmpty()) {
        println("No tasks in your list.")
        return
    }
    println("--- Your To-Do List ---")
    for (task in todos) {
        val status = if (task["done"] == true) "done" else "not done"
        println("${task["id"]}. ${task["title"]} ($status)")
    }
    println("-----------------------")
}

fun markDone(text: String?) {
    val id = text?.trim()?.toLongOrNull()
    if (id == null) {
        println("Please enter a whole number.")
        return
    }
    val task = todos.firstOrNull { it["id"] == id }
    if (task == null) {
        println("No task has that number.")
        return
    }
    task["done"] = true
    println("Task '${task["title"]}' marked as done.")
}

fun showMenu() {
    println()
    println("--- To-Do List Menu ---")
    println("1. Add Task")
    println("2. View Tasks")
    println("3. Mark Task Done")
    println("4. Save Tasks")
    println("5. Load Tasks")
    println("6. Quit")
    println("-----------------------")
}

fun main() {
    loadTodos()
    while (true) {
        showMenu()
        println("Enter your choice (1-6):")
        val choice = readlnOrNull() ?: "6"
        when (choice) {
            "1" -> {
                println("Enter task title:")
                val title = readlnOrNull() ?: ""
                println("Enter task description:")
                val description = readlnOrNull() ?: ""
                addTask(title, description)
            }
            "2" -> viewTasks()
            "3" -> {
                viewTasks()
                println("Enter task number to mark done:")
                markDone(readlnOrNull())
            }
            "4" -> saveTodos()
            "5" -> loadTodos()
            "6" -> {
                saveTodos()
                println("Goodbye!")
                return
            }
            else -> println("Invalid choice. Please try again.")
        }
    }
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
1
Study programming
Finish Unit 10
1
Review scores
Check the four scores
2
3
2
3
7
2
6
```

the program prints:
```text
No existing tasks found.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Study programming' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Enter task title:
Enter task description:
Task 'Review scores' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (not done)
-----------------------
Enter task number to mark done:
Task 'Review scores' marked as done.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------
Enter task number to mark done:
No task has that number.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
--- Your To-Do List ---
1. Study programming (not done)
2. Review scores (done)
-----------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Tasks saved.
Goodbye!
```

With no standard input at all, the program ends cleanly and prints:
```text
No existing tasks found.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Mark Task Done
4. Save Tasks
5. Load Tasks
6. Quit
-----------------------
Enter your choice (1-6):
Tasks saved.
Goodbye!
```

### Common Mistakes
1. Saving the file but never loading it, so tasks disappear between runs.
2. Reusing a deleted task's id, which can confuse saved references.
3. Letting a damaged `todos.json` crash the program instead of printing a message.

### Activities
1. Run the sample session, then run the program again typing `2` and `6` to see the saved tasks.
2. Add a command to delete a task by number.
3. Open `todos.json` and read the saved text. Edit it to remove a bracket and run the program again.
4. Show each task's description in the view command.

### Accessibility Practice

Every menu is printed as numbered lines and every prompt is on its own line. The status words are `done` and `not done`, not symbols, so the list reads clearly in speech and braille.

### Skills Checklist
- [ ] I can keep records with the shared fields.
- [ ] I can save and load JSON.
- [ ] I handle a missing or damaged file.
- [ ] I keep ids unique.
- [ ] I show status in words.

---

## Lesson 10.5: User Experience and Input Validation

### Reading References
- [Functions](https://kotlinlang.org/docs/functions.html)
- [Null safety](https://kotlinlang.org/docs/null-safety.html)
- Matching Python lesson: Lesson 10.5: Refining User Experience and Validation

### Learning Objectives
- Write reusable validation functions.
- Limit retries and handle the end of input.
- Write clear, accessible messages.

### Concept Explanation

Reusable validation functions make every menu and form consistent. `askNumber(prompt, low, high, attempts)` prints a prompt, reads a line, converts it, checks the range, and either returns the number or explains the problem and asks again. After the allowed attempts, or at the end of input, it returns `null`. `askYesNo(prompt)` accepts `y`, `yes`, `n`, and `no` in any letter case.

Good messages say *what was wrong* and *what to do*: "Enter a whole number from 0 to 100," not "Invalid." They never depend on color, position, or symbols alone, and they use the same wording every time. The return type `Int?` makes the caller deal with the failure case.

The example reads a score with the typed lines abc, 105, and 88, then asks a yes or no question with the lines maybe and y.

### Worked Example

```kotlin
fun askNumber(prompt: String, low: Int, high: Int, attempts: Int): Int? {
    for (attempt in 1..attempts) {
        println(prompt)
        val text = readlnOrNull() ?: return null
        val number = text.trim().toIntOrNull()
        if (number != null && number in low..high) return number
        println("Enter a whole number from $low to $high. You have ${attempts - attempt} attempt(s) left.")
    }
    return null
}

fun askYesNo(prompt: String): Boolean? {
    while (true) {
        println("$prompt (yes or no)")
        val text = readlnOrNull()?.trim()?.lowercase() ?: return null
        if (text == "y" || text == "yes") return true
        if (text == "n" || text == "no") return false
        println("Please answer yes or no.")
    }
}

fun main() {
    val score = askNumber("Enter a score from 0 to 100:", 0, 100, 3)
    if (score != null) {
        println("Accepted score: $score")
    } else {
        println("No valid score was entered.")
    }

    val keep = askYesNo("Save this score?")
    println("Save answer: $keep")
}
```

### Expected Behavior or Output

With the following lines typed as standard input (piped input is not echoed, so it does not appear in the output):
```text
abc
105
88
maybe
y
```

the program prints:
```text
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 2 attempt(s) left.
Enter a score from 0 to 100:
Enter a whole number from 0 to 100. You have 1 attempt(s) left.
Enter a score from 0 to 100:
Accepted score: 88
Save this score? (yes or no)
Please answer yes or no.
Save this score? (yes or no)
Save answer: true
```

With no standard input at all, the program ends cleanly and prints:
```text
Enter a score from 0 to 100:
No valid score was entered.
Save this score? (yes or no)
Save answer: null
```

### Common Mistakes
1. Writing the message "Invalid" without saying what is valid.
2. Accepting a decimal such as 88.5 for a field that requires a whole number.
3. Looping forever on bad input instead of limiting attempts.

### Activities
1. Run the sample input and read each message aloud.
2. Run with three invalid numbers and read the final message.
3. Add `askText(prompt)` that rejects empty answers.
4. Rewrite two messages from earlier lessons so they say what to do next.

### Accessibility Practice

Check that every error message ends with an action the user can take, and that the same situation always produces the same words.

### Skills Checklist
- [ ] I can write reusable validation functions.
- [ ] I limit retries.
- [ ] I handle the end of input.
- [ ] I write messages that say what to do.
- [ ] I keep wording consistent.

---

# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

Build a personal data manager with the shared record schema, storage, search and completion, acceptance tests, and a documentation and accessibility check.

---


## Lesson 11.1: Capstone: Requirements and Design

### Reading References
- [Data classes](https://kotlinlang.org/docs/data-classes.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 11.1: Introduction to NiceGUI (capstone planning)

### Learning Objectives
- Write requirements for a personal data manager.
- Define the shared record schema as a data class.
- Check records against the validation rules before building features.

### Concept Explanation

The capstone is a *personal data manager*: a program that keeps a list of records, lets the user add, view, search, change, complete, and delete them, and saves them to a file. In the Kotlin track it is a text program, so it runs from the terminal and is fully usable with a screen reader or braille display.

**Shared record schema (all general-purpose language tracks).** Every record has `id` (unique whole number), `title`, `description`, `category`, `created_at`, and `updated_at` (ISO 8601 text). A project may add fields, such as an optional `done` flag, but must not remove these. Kotlin property names use camel case (`createdAt`), and the stored JSON uses the shared names.

**Validation rules.** A record must have a non-empty title and a non-empty category. Timestamps are ISO 8601 text such as `2026-01-15T09:00:00`.

Design before coding: list the operations, then the data, then the messages. The example checks the three shared sample records against the rules and prints them as a plain-text list.

### Worked Example

```kotlin
data class Record(
    val id: Int,
    val title: String,
    val description: String,
    val category: String,
    val createdAt: String,
    val updatedAt: String,
)

fun validate(title: String?, category: String?): String? = when {
    title == null || title.isBlank() -> "A title is required."
    category == null || category.isBlank() -> "A category is required."
    else -> null
}

fun main() {
    val sample = listOf(
        Record(1, "Notebook", "Course notes", "supplies", "2026-01-15T09:00:00", "2026-01-15T09:00:00"),
        Record(2, "Pencil", "Box of 10", "supplies", "2026-01-15T09:05:00", "2026-01-15T09:05:00"),
        Record(3, "Study plan", "Weekly schedule", "planning", "2026-01-15T09:10:00", "2026-01-15T09:10:00"),
    )

    for (record in sample) {
        val problem = validate(record.title, record.category)
        println("${record.id}. ${record.title} [${record.category}] - ${problem ?: "valid"}")
    }

    println(validate("  ", "supplies"))
    println(validate("Ruler", ""))
}
```

### Expected Behavior or Output

The program prints:
```text
1. Notebook [supplies] - valid
2. Pencil [supplies] - valid
3. Study plan [planning] - valid
A title is required.
A category is required.
```

### Common Mistakes
1. Starting to build features before agreeing on the record fields.
2. Allowing a record with an empty title because the check was left for later.
3. Storing timestamps in different formats in different places.

### Activities
1. Write the seven operations as a numbered list of requirements.
2. Add one project-specific property and say how it is validated.
3. Write three sample records for your own project.
4. Describe in plain sentences what each shared field means.

### Accessibility Practice

Design the screen output as lines of plain text: one record per line, with the same field order each time. Decide the wording of every message now so that it can be tested.

### Skills Checklist
- [ ] I can write requirements.
- [ ] I know the shared record fields.
- [ ] I can write validation rules.
- [ ] I can describe sample data.
- [ ] I can plan messages before coding.

---

## Lesson 11.2: Capstone: Data Model and Storage

### Reading References
- [Data classes](https://kotlinlang.org/docs/data-classes.html)
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- Matching Python lesson: Lesson 11.2: Data Model and Storage

### Learning Objectives
- Store records as data class objects.
- Save and load them as JSON.
- Confirm that every field survives a round trip.

### Concept Explanation

Records are stored as a list of data class objects in memory and as a JSON array on disk. The storage layer has two functions: `saveRecords(path, records)` and `loadRecords(path)`. Loading returns a pair of the records and a message, so the caller decides what to do when the file is missing or damaged.

A `Record` is converted to a map for saving (`toMap`) and rebuilt from a decoded map when loading (`toRecord`), which checks that each field is present and has the right type. The optional `done` field defaults to `false`.

The example uses the teaching JSON helper from Lesson 8.5 (included so the program runs on its own). After saving and reloading it compares the lists; data classes compare by value, so this *round-trip test* checks every field of every record. It is the first acceptance test for storage.

### Worked Example

```kotlin
object Json {
    fun encode(value: Any?): String = when (value) {
        null -> "null"
        is String -> quote(value)
        is Boolean, is Int, is Long, is Double -> value.toString()
        is Map<*, *> -> value.entries.sortedBy { it.key.toString() }
            .joinToString(",", "{", "}") { quote(it.key.toString()) + ":" + encode(it.value) }
        is List<*> -> value.joinToString(",", "[", "]") { encode(it) }
        else -> throw IllegalArgumentException("cannot encode ${value::class.simpleName}")
    }

    private fun quote(text: String): String {
        val out = StringBuilder("\"")
        for (c in text) {
            when {
                c == '"' -> out.append("\\\"")
                c == '\\' -> out.append("\\\\")
                c == '\n' -> out.append("\\n")
                c == '\r' -> out.append("\\r")
                c == '\t' -> out.append("\\t")
                c < ' ' -> out.append("\\u%04x".format(c.code))
                else -> out.append(c)
            }
        }
        return out.append('"').toString()
    }

    fun decode(text: String): Any? = Parser(text).parse()

    private class Parser(private val text: String) {
        private var pos = 0

        private fun fail(message: String): Nothing =
            throw IllegalArgumentException("$message at position $pos")

        private fun skip() {
            while (pos < text.length && text[pos].isWhitespace()) pos++
        }

        fun parse(): Any? {
            val result = value()
            skip()
            if (pos < text.length) fail("unexpected extra text")
            return result
        }

        private fun value(): Any? {
            skip()
            if (pos >= text.length) fail("unexpected end of text")
            val c = text[pos]
            return when {
                c == '{' -> obj()
                c == '[' -> list()
                c == '"' -> str()
                text.startsWith("true", pos) -> { pos += 4; true }
                text.startsWith("false", pos) -> { pos += 5; false }
                text.startsWith("null", pos) -> { pos += 4; null }
                c == '-' || c.isDigit() -> number()
                else -> fail("unexpected character")
            }
        }

        private fun number(): Any {
            val start = pos
            if (text[pos] == '-') pos++
            while (pos < text.length && (text[pos].isDigit() || text[pos] in ".eE+-")) pos++
            val token = text.substring(start, pos)
            return token.toLongOrNull() ?: token.toDoubleOrNull() ?: fail("bad number")
        }

        private fun str(): String {
            pos++
            val out = StringBuilder()
            while (true) {
                if (pos >= text.length) fail("unterminated string")
                val c = text[pos++]
                if (c == '"') return out.toString()
                if (c != '\\') { out.append(c); continue }
                if (pos >= text.length) fail("bad escape")
                when (text[pos++]) {
                    'n' -> out.append('\n')
                    't' -> out.append('\t')
                    'r' -> out.append('\r')
                    '"' -> out.append('"')
                    '\\' -> out.append('\\')
                    '/' -> out.append('/')
                    'u' -> {
                        if (pos + 4 > text.length) fail("bad escape")
                        out.append(text.substring(pos, pos + 4).toInt(16).toChar())
                        pos += 4
                    }
                    else -> fail("bad escape")
                }
            }
        }

        private fun obj(): Map<String, Any?> {
            pos++
            val map = LinkedHashMap<String, Any?>()
            skip()
            if (pos < text.length && text[pos] == '}') { pos++; return map }
            while (true) {
                skip()
                if (pos >= text.length || text[pos] != '"') fail("expected a key")
                val key = str()
                skip()
                if (pos >= text.length || text[pos] != ':') fail("expected ':'")
                pos++
                map[key] = value()
                skip()
                if (pos >= text.length) fail("unterminated object")
                val d = text[pos++]
                if (d == '}') return map
                if (d != ',') { pos--; fail("expected ',' or '}'") }
            }
        }

        private fun list(): List<Any?> {
            pos++
            val items = ArrayList<Any?>()
            skip()
            if (pos < text.length && text[pos] == ']') { pos++; return items }
            while (true) {
                items.add(value())
                skip()
                if (pos >= text.length) fail("unterminated list")
                val d = text[pos++]
                if (d == ']') return items
                if (d != ',') { pos--; fail("expected ',' or ']'") }
            }
        }
    }
}

data class Record(
    val id: Int,
    val title: String,
    val description: String,
    val category: String,
    val createdAt: String,
    val updatedAt: String,
    val done: Boolean = false,
)

fun Record.toMap(): Map<String, Any?> = mapOf(
    "id" to id, "title" to title, "description" to description, "category" to category,
    "created_at" to createdAt, "updated_at" to updatedAt, "done" to done,
)

fun toRecord(entry: Any?): Record {
    val map = entry as? Map<*, *> ?: throw IllegalArgumentException("a record must be an object")
    fun text(key: String) = map[key] as? String ?: throw IllegalArgumentException("missing field $key")
    val id = (map["id"] as? Long)?.toInt() ?: throw IllegalArgumentException("missing field id")
    return Record(id, text("title"), text("description"), text("category"),
        text("created_at"), text("updated_at"), map["done"] as? Boolean ?: false)
}

fun saveRecords(path: String, records: List<Record>) {
    java.io.File(path).writeText(Json.encode(records.map { it.toMap() }))
}

fun loadRecords(path: String): Pair<List<Record>, String?> {
    val file = java.io.File(path)
    if (!file.exists()) return Pair(emptyList(), "Could not open $path: file not found.")
    return try {
        Pair((Json.decode(file.readText()) as List<*>).map { toRecord(it) }, null)
    } catch (e: Exception) {
        Pair(emptyList(), "The data file is not valid: ${e.message}")
    }
}

fun main() {
    val sample = listOf(
        Record(1, "Notebook", "Course notes", "supplies", "2026-01-15T09:00:00", "2026-01-15T09:00:00"),
        Record(2, "Pencil", "Box of 10", "supplies", "2026-01-15T09:05:00", "2026-01-15T09:05:00"),
        Record(3, "Study plan", "Weekly schedule", "planning", "2026-01-15T09:10:00", "2026-01-15T09:10:00"),
    )

    saveRecords("records.json", sample)
    val (loaded, problem) = loadRecords("records.json")
    println("Round trip preserved all fields: ${loaded == sample}")
    println("Records loaded: ${loaded.size}")
    println(problem)

    println(loadRecords("missing.json").second)

    java.io.File("broken.json").writeText("[{\"id\": 1,")
    println(loadRecords("broken.json").second)
}
```

### Expected Behavior or Output

The program prints:
```text
Round trip preserved all fields: true
Records loaded: 3
null
Could not open missing.json: file not found.
The data file is not valid: expected a key at position 10
```

### Common Mistakes
1. Overwriting the data file with an empty list after a failed load.
2. Saving only some of the fields.
3. Assuming a loaded record has every field without checking.

### Activities
1. Run the program and open `records.json` to read the saved text.
2. Add a field to `Record`, save it, and confirm that it survives the round trip.
3. Make `toRecord` reject a record whose title is blank.
4. Explain why `loadRecords` returns a message and does not throw.

### Accessibility Practice

Messages that name the file and the problem read clearly in speech. After saving, read the file in the terminal to confirm it contains what you expect.

### Skills Checklist
- [ ] I can store records in data class objects.
- [ ] I can save and load JSON.
- [ ] I can run a round-trip test.
- [ ] I handle missing and damaged files.
- [ ] I do not overwrite good data after a failed load.

---

## Lesson 11.3: Capstone: Core Operations

### Reading References
- [Classes](https://kotlinlang.org/docs/classes.html)
- [Collections overview](https://kotlinlang.org/docs/collections-overview.html)
- Matching Python lesson: Lesson 11.3: Displaying and Managing Items

### Learning Objectives
- Add, list, search, change, complete, and delete records.
- Assign new ids and update timestamps correctly.
- Return a message when an operation cannot be done.

### Concept Explanation

A `Manager` class holds the records and offers one function per operation. Each function that can fail returns a pair of the result and a message, so the user interface can show the message and decide what to do. New ids are one more than the highest id, so ids are never reused while higher ids exist. Updating a record sets `updatedAt` but never changes `createdAt`, which is a `val`. Completing a record sets the optional `done` field to `true` and counts as an update.

For repeatable output the example passes in a *fake clock* that returns a new fixed time on each call. A real program passes a function that reads the real time.

The example adds the three shared sample records, lists them, searches for "note", changes one description, completes one record, deletes one, and tries to delete a record that does not exist.

### Worked Example

```kotlin
data class Record(
    val id: Int,
    var title: String,
    var description: String,
    var category: String,
    val createdAt: String,
    var updatedAt: String,
    var done: Boolean = false,
)

fun validate(title: String?, category: String?): String? = when {
    title == null || title.isBlank() -> "A title is required."
    category == null || category.isBlank() -> "A category is required."
    else -> null
}

class Manager(private val clock: () -> String) {
    val records = mutableListOf<Record>()

    private fun nextId(): Int = (records.maxOfOrNull { it.id } ?: 0) + 1

    fun find(id: Int): Record? = records.firstOrNull { it.id == id }

    fun add(title: String, description: String, category: String): Pair<Record?, String?> {
        val problem = validate(title, category)
        if (problem != null) return Pair(null, problem)
        val stamp = clock()
        val record = Record(nextId(), title.trim(), description.trim(), category.trim(), stamp, stamp)
        records.add(record)
        return Pair(record, null)
    }

    fun update(
        id: Int,
        title: String? = null,
        description: String? = null,
        category: String? = null,
        done: Boolean? = null,
    ): Pair<Record?, String?> {
        val record = find(id) ?: return Pair(null, "No record has that id.")
        val problem = validate(title ?: record.title, category ?: record.category)
        if (problem != null) return Pair(null, problem)
        if (title != null) record.title = title.trim()
        if (description != null) record.description = description.trim()
        if (category != null) record.category = category.trim()
        if (done != null) record.done = done
        record.updatedAt = clock()
        return Pair(record, null)
    }

    fun complete(id: Int) = update(id, done = true)

    fun delete(id: Int): Pair<Boolean, String?> {
        val record = find(id) ?: return Pair(false, "No record has that id.")
        records.remove(record)
        return Pair(true, null)
    }

    fun search(text: String): List<Record> {
        val needle = text.trim().lowercase()
        return records.filter { it.title.lowercase().contains(needle) || it.description.lowercase().contains(needle) }
    }
}

fun describe(record: Record): String =
    "${record.id}. ${record.title} [${record.category}] (${if (record.done) "done" else "not done"})"

fun makeClock(): () -> String {
    var ticks = 0
    return {
        ticks++
        "2026-01-15T10:00:%02d".format(ticks)
    }
}

fun show(manager: Manager) {
    for (record in manager.records) println(describe(record))
}

fun main() {
    val manager = Manager(makeClock())
    manager.add("Notebook", "Course notes", "supplies")
    manager.add("Pencil", "Box of 10", "supplies")
    manager.add("Study plan", "Weekly schedule", "planning")
    show(manager)

    println("Search for 'note':")
    for (record in manager.search("note")) println(record.title)

    manager.update(2, description = "Box of 12")
    manager.complete(3)
    println("${manager.find(2)?.description} ${manager.find(2)?.updatedAt}")
    println(manager.delete(1))
    println(manager.delete(99))
    show(manager)
}
```

### Expected Behavior or Output

The program prints:
```text
1. Notebook [supplies] (not done)
2. Pencil [supplies] (not done)
3. Study plan [planning] (not done)
Search for 'note':
Notebook
Box of 12 2026-01-15T10:00:04
(true, null)
(false, No record has that id.)
2. Pencil [supplies] (not done)
3. Study plan [planning] (done)
```

### Common Mistakes
1. Reusing a deleted record's id by counting the list size instead of using the highest id.
2. Changing `createdAt` when updating a record (the property is a `val` to prevent this).
3. Throwing an exception for a missing record where a message to display is more helpful.

### Activities
1. Predict the output before running.
2. Add `listByCategory(category)` to `Manager`.
3. Add a rule that blocks completing a record that is already complete, with a message.
4. Explain how the fake clock makes the output repeatable.

### Accessibility Practice

List output uses the same fixed format for every record and the words `done` and `not done`. Search results print only titles, so each line is short.

### Skills Checklist
- [ ] I can implement add, list, search, change, complete, and delete.
- [ ] I assign unique ids.
- [ ] I update timestamps correctly.
- [ ] I return clear messages for failures.
- [ ] I can make output repeatable with a fake clock.

---

## Lesson 11.4: Capstone: Validation and Acceptance Tests

### Reading References
- [Exceptions](https://kotlinlang.org/docs/exceptions.html)
- [Functions](https://kotlinlang.org/docs/functions.html)
- Matching Python lesson: Lesson 11.4: Testing and Refinement

### Learning Objectives
- Run the shared acceptance tests.
- Verify that validation rejects bad data.
- Read and interpret test results.

### Concept Explanation

The shared acceptance tests describe behavior that every language track's capstone must show:

1. Adding a record with an empty title is rejected with a clear message.
2. A new record receives an unused `id`.
3. Updating a record changes `updated_at` but not `created_at`.
4. Deleting a record removes only that record.
5. Saving and reloading preserves all fields and values (shown in Lesson 11.2).
6. Every message and control can be used without color or a mouse (checked by hand in Lesson 11.5).

This lesson automates tests 1 to 4 and also tests completion and the rejection of a blank title in an update. Each test builds a new `Manager`, so tests cannot affect each other. The fake clock keeps timestamps predictable so a test can check that `updatedAt` changed while `createdAt` did not.

### Worked Example

```kotlin
data class Record(
    val id: Int,
    var title: String,
    var description: String,
    var category: String,
    val createdAt: String,
    var updatedAt: String,
    var done: Boolean = false,
)

fun validate(title: String?, category: String?): String? = when {
    title == null || title.isBlank() -> "A title is required."
    category == null || category.isBlank() -> "A category is required."
    else -> null
}

class Manager(private val clock: () -> String) {
    val records = mutableListOf<Record>()

    private fun nextId(): Int = (records.maxOfOrNull { it.id } ?: 0) + 1

    fun find(id: Int): Record? = records.firstOrNull { it.id == id }

    fun add(title: String, description: String, category: String): Pair<Record?, String?> {
        val problem = validate(title, category)
        if (problem != null) return Pair(null, problem)
        val stamp = clock()
        val record = Record(nextId(), title.trim(), description.trim(), category.trim(), stamp, stamp)
        records.add(record)
        return Pair(record, null)
    }

    fun update(
        id: Int,
        title: String? = null,
        description: String? = null,
        category: String? = null,
        done: Boolean? = null,
    ): Pair<Record?, String?> {
        val record = find(id) ?: return Pair(null, "No record has that id.")
        val problem = validate(title ?: record.title, category ?: record.category)
        if (problem != null) return Pair(null, problem)
        if (title != null) record.title = title.trim()
        if (description != null) record.description = description.trim()
        if (category != null) record.category = category.trim()
        if (done != null) record.done = done
        record.updatedAt = clock()
        return Pair(record, null)
    }

    fun complete(id: Int) = update(id, done = true)

    fun delete(id: Int): Pair<Boolean, String?> {
        val record = find(id) ?: return Pair(false, "No record has that id.")
        records.remove(record)
        return Pair(true, null)
    }

    fun search(text: String): List<Record> {
        val needle = text.trim().lowercase()
        return records.filter { it.title.lowercase().contains(needle) || it.description.lowercase().contains(needle) }
    }
}

fun describe(record: Record): String =
    "${record.id}. ${record.title} [${record.category}] (${if (record.done) "done" else "not done"})"

fun makeClock(): () -> String {
    var ticks = 0
    return {
        ticks++
        "2026-01-15T10:00:%02d".format(ticks)
    }
}

var failures = 0

fun test(name: String, body: () -> Unit) {
    val result = runCatching(body)
    if (result.isSuccess) {
        println("PASS $name")
    } else {
        failures++
        println("FAIL $name: ${result.exceptionOrNull()?.message}")
    }
}

fun assertThat(condition: Boolean, message: String) {
    if (!condition) throw AssertionError(message)
}

fun fresh(): Manager {
    val manager = Manager(makeClock())
    manager.add("Notebook", "Course notes", "supplies")
    manager.add("Pencil", "Box of 10", "supplies")
    manager.add("Study plan", "Weekly schedule", "planning")
    return manager
}

fun main() {
    test("1. an empty title is rejected") {
        val manager = fresh()
        val (record, message) = manager.add("   ", "x", "supplies")
        assertThat(record == null && message == "A title is required.", "expected the title message")
        assertThat(manager.records.size == 3, "the list should be unchanged")
    }

    test("2. a new record gets an unused id") {
        val manager = fresh()
        manager.delete(2)
        val (record, _) = manager.add("Ruler", "30 cm", "supplies")
        assertThat(record?.id == 4, "expected id 4 but got ${record?.id}")
    }

    test("3. update changes updatedAt but not createdAt") {
        val manager = fresh()
        val before = manager.find(1)!!.copy()
        manager.update(1, description = "Lecture notes")
        val after = manager.find(1)!!
        assertThat(after.createdAt == before.createdAt, "createdAt changed")
        assertThat(after.updatedAt != before.updatedAt, "updatedAt did not change")
    }

    test("4. delete removes only that record") {
        val manager = fresh()
        manager.delete(2)
        val ids = manager.records.map { it.id }
        assertThat(ids == listOf(1, 3), "wrong records remain: $ids")
    }

    test("5. complete marks done and updates the record") {
        val manager = fresh()
        val (record, _) = manager.complete(3)
        assertThat(record?.done == true && record.updatedAt != record.createdAt, "completion not recorded")
    }

    test("6. a blank title cannot be saved by update") {
        val manager = fresh()
        val (record, message) = manager.update(1, title = "")
        assertThat(record == null && message == "A title is required.", "update accepted a blank title")
    }

    println(if (failures == 0) "All acceptance tests passed." else "$failures test(s) failed.")
}
```

### Expected Behavior or Output

The program prints:
```text
PASS 1. an empty title is rejected
PASS 2. a new record gets an unused id
PASS 3. update changes updatedAt but not createdAt
PASS 4. delete removes only that record
PASS 5. complete marks done and updates the record
PASS 6. a blank title cannot be saved by update
All acceptance tests passed.
```

### Common Mistakes
1. Sharing one manager between tests, so one test's deletions change the next test.
2. Checking only that no exception occurred, and not checking the result.
3. Writing the expected message differently from the program, so a correct program fails the test.

### Activities
1. Break `Manager.update` so it also changes `createdAt` (make the property a `var`) and watch test 3 fail. Restore it.
2. Add a test that searching ignores case.
3. Add a test that deleting an unknown id returns `false` and a message.
4. Explain why test 2 deletes record 2 before adding the new one.

### Accessibility Practice

The test names begin with the acceptance-test number, so PASS and FAIL lines can be matched to the specification. Read only the first word of each line to hear the overall result quickly.

### Skills Checklist
- [ ] I can run the shared acceptance tests.
- [ ] I can test validation failures.
- [ ] I can test timestamps with a fake clock.
- [ ] I can read PASS and FAIL lines.
- [ ] I use a fresh manager for every test.

---

## Lesson 11.5: Capstone: Documentation and Presentation

### Reading References
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- [Unit P, Lesson P.6](../FOUNDATIONS/unit-p-computing-foundations.md): files, data formats, and the shared accessible workflow
- Matching Python lesson: Lesson 11.5: Final Submission

### Learning Objectives
- Write a plain-text project summary.
- Report a count of records by category.
- Complete a manual accessibility check.

### Concept Explanation

Documentation tells a future reader what the program does and how to run it. Write it as plain text or Markdown with short headings, numbered steps, and complete sentences. Include: the purpose of the program, the compile and run commands, the shared record fields, the commands a user can give, the accessibility checks you carried out, and what you would improve next.

The example generates a summary from the shared sample data. It counts records by category and prints the categories in alphabetical order so the output is stable. It then prints the manual accessibility checklist. The unchecked boxes `[ ]` are for *you* to complete by hand with your own access technology; the program cannot verify them.

Acceptance test 6 is a manual check: every message and control can be used without color or a mouse. Test it with the keyboard only, and with the screen reader or braille display you actually use. Record what you tested and its version; do not claim compatibility with software you did not test.

### Worked Example

```kotlin
data class Record(val id: Int, val title: String, val category: String)

fun main() {
    val sample = listOf(
        Record(1, "Notebook", "supplies"),
        Record(2, "Pencil", "supplies"),
        Record(3, "Study plan", "planning"),
    )

    val counts = sample.groupingBy { it.category }.eachCount().toSortedMap()

    println("Personal Data Manager - Summary")
    println("Records: ${sample.size}")
    println("Categories:")
    for ((category, count) in counts) {
        println("- $category: $count")
    }

    println()
    println("Manual accessibility checklist (complete this by hand):")
    val checks = listOf(
        "[ ] Every command can be used with the keyboard only.",
        "[ ] Every message is a complete sentence that says what to do next.",
        "[ ] No meaning depends on color, position, or symbols alone.",
        "[ ] The output was read with my own screen reader or braille display.",
        "[ ] I recorded the operating system, program, and version I tested.",
    )
    for (check in checks) println(check)
}
```

### Expected Behavior or Output

The program prints:
```text
Personal Data Manager - Summary
Records: 3
Categories:
- planning: 1
- supplies: 2

Manual accessibility checklist (complete this by hand):
[ ] Every command can be used with the keyboard only.
[ ] Every message is a complete sentence that says what to do next.
[ ] No meaning depends on color, position, or symbols alone.
[ ] The output was read with my own screen reader or braille display.
[ ] I recorded the operating system, program, and version I tested.
```

### Common Mistakes
1. Writing documentation that only the author can follow.
2. Claiming that a program is accessible without recording what was tested and how.
3. Letting the documentation drift from the program after later changes.

### Activities
1. Write the project summary for your own capstone using the headings above.
2. Run the keyboard-only check and record each problem you find.
3. Ask a classmate to follow your run instructions from a fresh folder and note where they get stuck.
4. Write three improvements for the next version, ordered by user benefit.

### Accessibility Practice

This is the final accessibility lesson. Read your own documentation aloud from start to finish. Anything you have to look at the screen to understand needs rewriting.

### Skills Checklist
- [ ] I can write a plain-text project summary.
- [ ] I can report counts by category.
- [ ] I can run a manual accessibility check.
- [ ] I record what I tested.
- [ ] I do not claim untested compatibility.

---

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)
