# Julia example validation

Run `python3 scripts/check_julia_examples.py` from the repository root with Julia 1.12 available on `PATH`. The checker executes each fenced `jl` example in an isolated temporary working directory, disables user startup/history files, and supplies deterministic stdin for the interactive input example. A successful run verifies process exit status; it does not assert exact output, cover every invalid-input path, validate the external JSON3.jl or CSV.jl application workflows, or replace a full capstone test.
