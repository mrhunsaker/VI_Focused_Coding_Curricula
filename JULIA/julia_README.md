# Introduction to Julia

## Standalone beginner curriculum

Julia is a high-level, dynamic language with multiple dispatch and just-in-time compilation. It is designed for scientific computing, numerical analysis, optimization, simulation, statistics, machine learning, and research code.

## What information is a good fit?

Julia is especially useful for vectors, matrices, tensors, measurements, simulation outputs, statistical samples, and scientific datasets. Its array and numerical abstractions make mathematical transformations direct. Record units, missing-value conventions, precision, and reproducibility requirements explicitly.

## Lessons

1. Julia REPL, scripts, and package environments.
2. Bindings, types, and numeric expressions.
3. Functions and multiple dispatch.
4. Arrays, ranges, and broadcasting.
5. Control flow and comprehensions.
6. Tuples, named tuples, dictionaries, and structs.
7. Modules, packages, and data input.
8. Performance, allocation, and type stability.
9. Testing and reproducibility.
10. Scientific-computing capstone.

## First program

~~~julia
name = "Avery"
values = [1.0, 2.5, 4.0]
println("Hello, $name")
println(sum(values) / length(values))
~~~

Toolchain: Julia runtime and package manager. Use project environments to make dependencies reproducible. See [Julia lessons](lessons.md).
