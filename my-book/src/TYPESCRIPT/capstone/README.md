TypeScript capstone reference core

Build and test with TypeScript 5.8 and Node.js 22:

    tsc -p tsconfig.json
    node --test records.test.js

The reference core implements the shared six-field record schema, optional done state, CRUD, search, JSON persistence, validation, and malformed/missing-file handling. It is a tested data/domain layer; a complete accessible user interface remains a separate requirement.
