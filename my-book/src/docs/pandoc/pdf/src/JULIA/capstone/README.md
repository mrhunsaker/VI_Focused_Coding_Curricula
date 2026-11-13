Julia capstone reference core

Install JSON3 once with Julia's package manager, then run the tests:

    julia -e 'using Pkg; Pkg.add("JSON3")'
    julia JULIA/capstone/test_records.jl

The tested core implements the shared six-field schema, optional done state, CRUD, search, JSON persistence, validation, and malformed/missing-file handling. An accessible user interface remains a separate requirement.
