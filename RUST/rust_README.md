# Introduction to Rust

## Standalone beginner curriculum

Rust is a statically typed, compiled language built around ownership, borrowing, and traits. It is used for systems programming, command-line tools, network services, WebAssembly, embedded development, and performance-sensitive software where memory safety is a priority.

## What information is a good fit?

Rust suits owned values, borrowed views, structured records, byte buffers, collections, and concurrent data with explicit lifetime and mutation rules. Ownership and borrowing help prevent many memory-safety errors, but they do not replace validation of external input or logical correctness.

## Lessons

1. rustup, Cargo, and project structure.
2. Bindings, scalar types, and expressions.
3. Ownership, moves, and borrowing.
4. Control flow, functions, and modules.
5. Structs, enums, and pattern matching.
6. Collections, strings, and error handling.
7. Traits, generics, and lifetimes.
8. Files, iterators, and testing.
9. Threads and safe concurrency.
10. Systems-oriented capstone.

## First program

~~~rust
fn main() {
    let name = "Avery";
    let count: i32 = 3;
    println!("{name}: {count}");
}
~~~

Toolchain: rustup, rustc, and Cargo. Use stable Rust and Cargo-managed projects. See [Rust lessons](lessons.md).
