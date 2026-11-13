C capstone reference core

Install json-c and pkg-config, then compile and run from the repository root:

    gcc -D_GNU_SOURCE -std=c17 -Wall -Wextra -Werror C/capstone/records.c C/capstone/test_records.c $(pkg-config --cflags --libs json-c) -o /tmp/c-capstone-tests
    /tmp/c-capstone-tests

The tested domain layer implements the shared six-field schema, optional done state, CRUD, search, JSON persistence, validation, and missing/malformed-file handling. An accessible user interface remains a separate requirement.
