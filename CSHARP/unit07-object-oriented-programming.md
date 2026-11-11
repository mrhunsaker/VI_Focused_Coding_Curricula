# Unit 7: Object-Oriented Programming

## Overview

This unit covers types/classes, instances, fields, methods, inheritance or interfaces, composition. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 7.1: Types and object models

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# supports classes, records, structs, properties, methods, interfaces, inheritance, and composition. Choose value or reference semantics intentionally and protect invariants through the public API.
### Worked Example
```cs
var student = new Student("Avery", 16, "Computer Science");
Console.WriteLine($"{student.Name}, {student.Age}, {student.FavoriteSubject}");
record Student(string Name, int Age, string FavoriteSubject);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Avery, 16, Computer Science
```

### Common Mistakes
- Exposing mutable state that bypasses the type's invariants.
- Confusing reference identity with value equality.
- Using inheritance where an interface or composition better represents the relationship.
### Activities
1. Create a second object using the same type and compare its state or behavior.
2. Change one property or method input and verify the model invariant remains true.
3. Test equality, interface dispatch, inheritance, or nested composition as appropriate.
4. Explain why the selected C# type relationship is appropriate for the domain.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define and instantiate the required C# type.
- [ ] I can expose behavior through an appropriate public API.
- [ ] I can preserve model invariants.
- [ ] I can explain value/reference, interface, or composition semantics.
- [ ] I can test more than one instance or implementation.

## Lesson 7.2: Creating instances

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# supports classes, records, structs, properties, methods, interfaces, inheritance, and composition. Choose value or reference semantics intentionally and protect invariants through the public API.
### Worked Example
```cs
var avery = new Student("Avery", 16, "Computer Science"); var jordan = new Student("Jordan", 17, "Mathematics");
Console.WriteLine(avery); Console.WriteLine(jordan);
record Student(string Name, int Age, string FavoriteSubject);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Student { Name = Avery, Age = 16, FavoriteSubject = Computer Science }
Student { Name = Jordan, Age = 17, FavoriteSubject = Mathematics }
```

### Common Mistakes
- Exposing mutable state that bypasses the type's invariants.
- Confusing reference identity with value equality.
- Using inheritance where an interface or composition better represents the relationship.
### Activities
1. Create a second object using the same type and compare its state or behavior.
2. Change one property or method input and verify the model invariant remains true.
3. Test equality, interface dispatch, inheritance, or nested composition as appropriate.
4. Explain why the selected C# type relationship is appropriate for the domain.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define and instantiate the required C# type.
- [ ] I can expose behavior through an appropriate public API.
- [ ] I can preserve model invariants.
- [ ] I can explain value/reference, interface, or composition semantics.
- [ ] I can test more than one instance or implementation.

## Lesson 7.3: Fields and methods

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# supports classes, records, structs, properties, methods, interfaces, inheritance, and composition. Choose value or reference semantics intentionally and protect invariants through the public API.
### Worked Example
```cs
var stock = new InventoryItem("Notebook", 3); stock.Add(2);
Console.WriteLine($"{stock.Name}: {stock.Quantity}");
class InventoryItem(string name, int quantity) { public string Name { get; } = name; public int Quantity { get; private set; } = quantity; public void Add(int amount) { if (amount > 0) Quantity += amount; } }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Notebook: 5
```

### Common Mistakes
- Exposing mutable state that bypasses the type's invariants.
- Confusing reference identity with value equality.
- Using inheritance where an interface or composition better represents the relationship.
### Activities
1. Create a second object using the same type and compare its state or behavior.
2. Change one property or method input and verify the model invariant remains true.
3. Test equality, interface dispatch, inheritance, or nested composition as appropriate.
4. Explain why the selected C# type relationship is appropriate for the domain.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define and instantiate the required C# type.
- [ ] I can expose behavior through an appropriate public API.
- [ ] I can preserve model invariants.
- [ ] I can explain value/reference, interface, or composition semantics.
- [ ] I can test more than one instance or implementation.

## Lesson 7.4: Inheritance and interfaces

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# supports classes, records, structs, properties, methods, interfaces, inheritance, and composition. Choose value or reference semantics intentionally and protect invariants through the public API.
### Worked Example
```cs
IRecord record = new StudentRecord("Avery"); Console.WriteLine(record.Describe());
interface IRecord { string Describe(); }
class StudentRecord(string name) : IRecord { public string Describe() => $"Student: {name}"; }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Student: Avery
```

### Common Mistakes
- Exposing mutable state that bypasses the type's invariants.
- Confusing reference identity with value equality.
- Using inheritance where an interface or composition better represents the relationship.
### Activities
1. Create a second object using the same type and compare its state or behavior.
2. Change one property or method input and verify the model invariant remains true.
3. Test equality, interface dispatch, inheritance, or nested composition as appropriate.
4. Explain why the selected C# type relationship is appropriate for the domain.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define and instantiate the required C# type.
- [ ] I can expose behavior through an appropriate public API.
- [ ] I can preserve model invariants.
- [ ] I can explain value/reference, interface, or composition semantics.
- [ ] I can test more than one instance or implementation.

## Lesson 7.5: Composition

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# supports classes, records, structs, properties, methods, interfaces, inheritance, and composition. Choose value or reference semantics intentionally and protect invariants through the public API.
### Worked Example
```cs
var student = new Student("Avery", new Address("Farmington", "Utah"));
Console.WriteLine($"{student.Name} lives in {student.Address.City}, {student.Address.Region}");
record Address(string City, string Region); record Student(string Name, Address Address);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Expected Behavior or Output

Output observed when the worked example was run (.NET 8; the text of the output does not depend on the operating system):

```text
Avery lives in Farmington, Utah
```

### Common Mistakes
- Exposing mutable state that bypasses the type's invariants.
- Confusing reference identity with value equality.
- Using inheritance where an interface or composition better represents the relationship.
### Activities
1. Create a second object using the same type and compare its state or behavior.
2. Change one property or method input and verify the model invariant remains true.
3. Test equality, interface dispatch, inheritance, or nested composition as appropriate.
4. Explain why the selected C# type relationship is appropriate for the domain.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define and instantiate the required C# type.
- [ ] I can expose behavior through an appropriate public API.
- [ ] I can preserve model invariants.
- [ ] I can explain value/reference, interface, or composition semantics.
- [ ] I can test more than one instance or implementation.
