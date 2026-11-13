# Programming Code Glossary

A detailed student reference for Python, JavaScript, TypeScript, Java, and the optional post-capstone Kotlin supplement. Find the term in the language section, then use that language's INDEX.md to locate the teaching lesson. Definitions distinguish concepts that are easy to confuse.

## Shared computer science vocabulary

### Algorithm

A finite, ordered method for solving a problem. It defines steps, decisions, inputs, and expected outputs; a program implements an algorithm.

### Argument

The actual value supplied to a function call. The parameter is the receiving name in the function definition.

### Assignment

Storing a value in a variable or assignable location. Assignment is not equality comparison.

### Boolean

A logical value that is true or false. Python spells literals True and False; the other languages use lowercase.

### Bug

A defect causing a crash, incorrect result, or unmet requirement.

### Class

A definition describing data and behavior for a kind of object.

### Compiler

A program translating source code and reporting compile-time problems. Java compiles to JVM bytecode; TypeScript emits JavaScript.

### Condition

An expression deciding which branch runs or whether a loop continues. Java requires Boolean conditions; Python and JavaScript also allow truth-value testing.

### Constant

A binding that cannot be reassigned. This does not necessarily make the referenced object immutable.

### Data type

A classification defining possible values and valid operations, such as integer, string, Boolean, array, or object.

### Debugging

Systematically reproducing a problem, narrowing its cause, inspecting state, testing a hypothesis, correcting the defect, and retesting.

### Declaration

An instruction introducing a name such as a variable, function, class, or type. Initialization gives a variable its first value.

### Expression

A combination of values, names, operators, and calls evaluated to produce a value.

### Function

A callable unit of code performing a task. It may accept parameters and return a result.

### Input

Data received from a person, file, command line, network, or another system. Validate external input.

### Instance

One particular object created from a class.

### Iteration

One repetition of a loop body, or traversal of a sequence or collection.

### Library

Reusable code packaged for use by programs. A standard library ships with a language or runtime.

### Literal

A value written directly in source code, such as 42, 3.5, a quoted string, or true.

### Loop

A control-flow structure repeating instructions. for commonly traverses items; while repeats while a condition is true.

### Method

A function associated with an object or class.

### Module

A file or unit grouping code and exposing selected names for reuse.

### Object

A value grouping data and often behavior. Java objects are class instances; JavaScript and TypeScript also have flexible property objects.

### Operator

A symbol or keyword performing an operation, such as arithmetic, comparison, or logic.

### Parameter

A named variable in a function definition that receives an argument from the caller.

### Return value

The value a function or method gives back to its caller.

### Scope

The region of code where a name can be accessed. Local, block, function, and module scope rules differ by language.

### Statement

A complete instruction such as a declaration, assignment, conditional, loop, or return.

### String

A sequence of text characters. Strings are immutable in all languages covered.

### Syntax

Formal rules defining valid source-code structure. Valid syntax does not guarantee correct logic.

### Testing

Checking program behavior against expected outcomes. Unit tests focus on a small function or method.

### Variable

A named binding used to refer to a value. Declaration, assignment, mutability, and type rules vary by language.

## Python glossary

### __init__

Initialization method called when an instance is initialized. Commonly assigns self attributes; allocation itself involves __new__.

### __name__ and main guard

Module attribute equal to __main__ when run as entry point. The if __name__ == __main__ guard protects entry-point code from running on import.

### append()

List method adding one item to the same list. It mutates the list and returns None.

### break and continue

break exits the nearest loop. continue skips the rest of the current iteration and proceeds to the next.

### dict

Mutable mapping of keys to values. Keys must be hashable; values can be any objects.

### elif

Additional conditional branch evaluated only if earlier conditions are false. Python uses elif, not else if.

### except and finally

except handles a matching exception. finally is used for cleanup and runs whether or not an exception occurred, subject to process termination.

### float and int

float is binary floating point; many decimal fractions are approximate. int is arbitrary precision in ordinary Python implementations.

### for and while

for iterates over an iterable. while repeats while its condition is true.

### F-string

String prefixed with f that evaluates expressions in braces, for example f-string interpolation of a name.

### import

Loads a module and binds names for use, such as importing math.

### input()

Reads one line from standard input and returns a string. Convert it before numeric operations.

### is and is not

Identity comparisons testing whether references are the same object. Use == for value equality; is None is conventional.

### Iterable

Object supplying members one at a time, such as list, tuple, string, dictionary, set, or range.

### len()

Returns number of items in a collection or code points in a string, not necessarily user-perceived Unicode characters.

### list and tuple

list is mutable and ordered. tuple is ordered and immutable; a one-item tuple needs a trailing comma.

### None

Singleton meaning absence of a value. Compare using is None.

### open() and file modes

Opens a file. r reads, w writes and truncates, a appends. Prefer a with statement and specify UTF-8 encoding.

### range()

Arithmetic sequence used in loops. Stop is excluded: range(3) yields 0, 1, 2.

### return

Ends a function and optionally sends a value to caller. Falling off the end returns None.

### set

Mutable collection of unique hashable elements; no positional indexing.

### Slicing

Selects a sequence portion with start, stop, and optional step; start is included and stop excluded.

### with and context manager

Managed context with reliable cleanup. File contexts close files automatically through the context-manager protocol.

### Comprehension

Concise collection construction from an iterable, optionally filtered. Use a loop when clearer.

### Docstring

String literal first in a module, class, or function, stored in __doc__ and used to document behavior.

### Exception

Object representing an error. Common types include ValueError, TypeError, KeyError, IndexError, and FileNotFoundError.

### Generator

Iterator-producing function or expression yielding values lazily. Generator functions use yield.

### Lambda

Small anonymous function expression containing one expression. Use def for multi-statement or documented functions.

### MRO

Method Resolution Order: order Python searches base classes for attributes, especially with multiple inheritance.

### Mutable and immutable

Lists and dictionaries can change in place; strings, integers, and tuples cannot. A variable can be rebound either way.

### PEP 8

Python style guide recommending four-space indentation and snake_case names for functions and variables.

### Property

Managed attribute commonly created with property decorator, allowing attribute-style access with getter/setter logic.

### Type hint

Optional syntax describing expected types. Not generally enforced by Python at runtime; static tools can analyze hints.

### Virtual environment

Isolated Python interpreter/package context. The course uses uv to create and manage the project's `.venv`, install dependencies, and run commands without global pip installation.

### uv

A Python version, project, and package manager. `uv init` creates project configuration, `uv add package` installs and records a project dependency, `uv run command` executes inside the managed environment, `uv sync` installs the dependencies recorded in the project files, and `uv tree` displays the dependency tree. uv manages the project-local `.venv` and can install Python interpreters.

## JavaScript glossary

### Array

Indexed ordered collection that can change length. Methods include push, pop, map, filter, find, reduce, and forEach.

### async and await

An async function always returns a Promise. await waits for a Promise inside an async function without blocking the whole event loop.

### BigInt

Primitive for integers beyond Number's safe range. BigInt and Number arithmetic cannot be mixed directly.

### const, let, and var

const is block-scoped and cannot be reassigned; let is block-scoped and reassignable; var is function-scoped legacy syntax.

### console.log()

Writes values to the console; common terminal output in Node.js, not a file-writing API.

### Destructuring

Extracts array elements or object properties into variables.

### Event loop

Coordinates synchronous call-stack execution, queued callbacks, and asynchronous completions. Long synchronous work delays other tasks.

### export and import

ES module declarations exposing and bringing in bindings. Dynamic import returns a Promise.

### filter, map, and forEach

filter creates an array of passing elements; map creates a transformed array; forEach calls a callback and returns undefined.

### for...of and for...in

for...of iterates values from an iterable; for...in iterates enumerable property keys.

### Map and Set

Map stores key-value pairs with arbitrary key types. Set stores unique values.

### NaN

Special Number value for invalid numeric results. It is not equal to itself; use Number.isNaN().

### null and undefined

null represents intentional absence of an object value. undefined commonly means missing, uninitialized, or no returned value.

### Number

IEEE 754 binary64 numeric primitive. Use Number.isFinite() and Number.isSafeInteger() where appropriate.

### Object

Property collection. Ordinary keys are strings or symbols; use Map for arbitrary key types.

### package.json

Node project metadata. Its type field selects ES module or CommonJS interpretation for .js files in that package scope.

### Promise

Represents an asynchronous result that is pending, fulfilled, or rejected. Handle with then/catch or async/await.

### readline

Node built-in module for line-by-line input from a stream such as standard input.

### require() and CommonJS

require loads modules using Node's CommonJS system; module.exports exposes values. ES modules use import.

### Spread syntax

Expands iterables or object properties. Array/object spreads make shallow copies, not deep clones.

### Strict equality ===

Compares without loose equality coercion. Preferred for most comparisons; objects compare by identity.

### Template literal

Backtick-delimited string supporting multiline text and expression interpolation.

### Arrow function

Function expression using arrow syntax. It has no own this or arguments; not interchangeable with every traditional function.

### Callback and closure

Callback is a function passed to be called later. Closure is a function plus access to surrounding lexical variables.

### ECMAScript

Standard defining JavaScript syntax and semantics. Node and browsers add different host APIs.

### Hoisting

Processing declarations before scope execution. Function declarations and var differ from let/const temporal-dead-zone behavior.

### JSON

Text format for objects, arrays, strings, numbers, booleans, and null. Use JSON.parse() and JSON.stringify().

### Node.js and npm

Node.js runs JavaScript outside browsers. npm manages dependencies, scripts, and lockfiles. Use `npm install` or `npm install --save-dev` in the project directory to keep dependencies local.

### npx

npm's package-execution command. It runs a package binary from the current project's dependencies when available, or can fetch a package into npm's cache for one-off execution. Prefer project-local development dependencies and `npx` or npm scripts over global npm installs.

### Prototype

Object used in property lookup when a property is not found directly.

### Type coercion and truthiness

Coercion converts types automatically or explicitly. Falsy values include false, 0, empty string, null, undefined, and NaN; empty arrays/objects are truthy.

## TypeScript glossary

### any and unknown

any disables most type checking. unknown accepts any value but requires narrowing before use; prefer unknown for untrusted data.

### as assertion

Tells compiler to treat an expression as a type. It does not convert or validate runtime data.

### enum

Defines named constants. Numeric enums can create runtime objects; string unions or const objects may be simpler.

### interface and type alias

interface describes object shape; type names a type expression including unions, intersections, tuples, and function types.

### never

Type representing values that should not occur; used for non-returning functions and exhaustive checks.

### Null and undefined in strict mode

With strictNullChecks, they are distinct types and must be handled or narrowed before non-null use.

### Union and intersection

Union uses vertical-bar syntax for alternatives; intersection combines requirements.

### Type annotation and inference

Annotation explicitly states a type; inference derives a type from values and context. Neither adds runtime validation.

### Generic

Type or function parameterized by a type variable, preserving type information across reusable operations.

### keyof and readonly

keyof produces a union of keys of a type. readonly prevents assignment through a type but does not freeze runtime objects.

### strict and tsconfig.json

strict enables stronger checks. tsconfig.json controls source inclusion, target, module resolution, strictness, and output.

### tsc

TypeScript compiler. Checks types and can emit JavaScript; prefer the project-local compiler.

### Discriminated union and narrowing

A shared distinguishing property enables compiler narrowing based on control flow.

### Structural typing

Compatibility based on members a value provides, not its declared type name.

### Type guard

Condition or function giving evidence about a value's type so compiler can narrow it.

### Type erasure

TypeScript-only annotations, interfaces, and aliases are removed during compilation. Validate external data at runtime.

### Utility type

Built-in transformations such as Partial, Required, Readonly, Pick, Omit, and Record.

## Java glossary

### abstract class

Cannot be instantiated directly; can contain implemented and abstract methods.

### Array and ArrayList

Array has fixed length and one component type; use its length field. ArrayList is a resizable List; generic arguments use reference types such as Integer.

### boolean, char, int, and long

boolean is true/false. char is a UTF-16 code unit. int is 32-bit signed; long is 64-bit signed.

### break and enhanced for

break exits the nearest loop or switch. Enhanced for traverses array or Iterable elements.

### catch and finally

catch handles an exception. finally performs cleanup; prefer try-with-resources for AutoCloseable resources.

### class, constructor, and this

class declares a type. Constructor initializes an instance and has no return type. this refers to the current instance.

### final and static

final prevents reassignment, overriding, or subclassing depending on use. static associates a member with the class.

### HashMap, HashSet, and TreeMap

HashMap stores pairs without guaranteed order. HashSet stores unique values. TreeMap orders keys.

### implements and interface

A class uses implements to satisfy an interface contract. Interfaces define member contracts.

### JDK, JRE, and JVM

JDK provides development tools including javac. JRE describes runtime components. JVM executes bytecode.

### List and Map

List is an ordered collection allowing duplicates. Map stores key-value associations.

### main method

Traditional entry point: public static void main(String[] args).

### null

Absence of an object reference. Calling an instance method through null causes NullPointerException; primitives cannot hold null.

### package and import

Package organizes types and access. Import allows simple type names; importing a package does not import subpackages.

### private and public

private restricts member access; public exposes a member wherever its declaring type is accessible.

### return and void

return ends a method and may send a value. void means no return value.

### Scanner

java.util input parser. Mixing nextInt() and nextLine() can leave a newline for the next read.

### String and equals()

String is immutable. Compare contents with equals(), not ==, which compares reference identity.

### switch

Selects a branch; Java supports switch statements and newer switch expressions.

### throw and throws

throw raises an exception object. throws declares checked exceptions a method may propagate.

### Try-with-resources

Automatically closes resources implementing AutoCloseable.

### Wrapper and autoboxing

Wrapper classes such as Integer correspond to primitives. Unboxing null throws NullPointerException.

### Checked exception

Compiler requires code to catch or declare it with throws, unless it is unchecked.

### Encapsulation, inheritance, and polymorphism

Encapsulation hides internal state; inheritance extends a superclass; polymorphism lets a general reference invoke concrete overridden behavior.

### Garbage collection

Reclaims unreachable heap objects. It does not replace closing files or sockets.

### Generics

Type parameters provide compile-time type safety; Java implements generics with type erasure.

### Maven and Gradle wrappers

Project-local scripts that run a declared Maven or Gradle version for a project. Maven commonly uses `./mvnw` on macOS/Linux and `mvnw.cmd` on Windows; Gradle uses `./gradlew` and `gradlew.bat`. The wrapper avoids requiring each learner to install a global build tool.

### JUnit, overloading, and overriding

JUnit tests behavior with assertions. Overloading changes parameter lists. Overriding replaces inherited instance behavior; use @Override.

## Kotlin supplement glossary

### data class

Compiler generates equals, hashCode, toString, and copy based on primary-constructor properties.

### fun, val, and var

fun declares a function. val is a read-only binding. var is reassignable.

### Null safety and nullable type

Kotlin distinguishes non-null String from nullable String?. Java interoperability and external data may still require checks.

### Safe call and Elvis operator

Safe call ?. accesses only when receiver is non-null. Elvis ?: supplies a fallback when its left side is null.

### when and smart cast

when is a multi-branch expression or statement. Smart cast narrows a stable value after a type or null check.

### Extension function

Function with a receiver type, callable with member-like syntax; it does not add a real class member.

### object and companion object

object declares a singleton. Companion object provides class-associated members but is not identical to Java static.

### Coroutine

Concurrency abstraction for suspending/resuming work. kotlinx.coroutines supplies the framework; suspend alone is not the framework.

## Cross-language distinctions

| Concept | Python | JavaScript | TypeScript | Java | Kotlin |
|---|---|---|---|---|---|
| Variable | assignment; optional hints | let / const | let / const plus types | declared type; final | var / val |
| Boolean | True / False | true / false | true / false | true / false | true / false |
| Function | def | function / arrow | typed function / arrow | method in class | fun |
| Null-like | None | null / undefined | both; strict null checks | null reference | nullable types such as String? |
| Sequence | list / tuple | Array | Array<T> / T[] | array / List<E> | List<T> / MutableList<T> |
| Equality | == value; is identity | === strict equality | JavaScript runtime === | equals() for objects; == for primitives | == structural; === referential |

## Runtime and type-system distinctions

- Python type hints are optional metadata; ordinary execution does not enforce them.
- JavaScript is dynamically typed and its runtime does not enforce TypeScript annotations.
- TypeScript checks types before execution, then emits JavaScript. Type annotations are erased; validate external data at runtime.
- Java checks declared types at compile time. References can still be null, and generics use type erasure.
- Kotlin distinguishes nullable and non-nullable types, but Java interoperability and external data can still require runtime checks.
