C++ capstone reference core

Install nlohmann-json3-dev, then compile and run from the repository root:

    g++ -std=c++20 -Wall -Wextra -Werror -ICPP/capstone CPP/capstone/test_records.cpp -o /tmp/cpp-capstone-tests
    /tmp/cpp-capstone-tests

The tested domain layer implements the shared six-field schema, optional done state, CRUD, search, JSON persistence, validation, and missing/malformed-file handling. An accessible user interface remains a separate requirement.
