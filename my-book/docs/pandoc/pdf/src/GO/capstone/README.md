Go capstone reference core

Run the standard-library acceptance tests from this directory:

    go test -v ./...

The tested domain layer implements the shared six-field record schema, optional done state, CRUD, search, JSON persistence, validation, and malformed/missing-file handling. An accessible user interface remains a separate requirement.
