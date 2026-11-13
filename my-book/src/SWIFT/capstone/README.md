Swift capstone reference core

Compile and run the acceptance suite with Swift 6:

    swiftc SWIFT/capstone/Records.swift SWIFT/capstone/Acceptance.swift -o /tmp/swift-capstone-tests
    /tmp/swift-capstone-tests

The tested core implements the shared six-field schema, optional done state, CRUD, search, JSON Codable persistence, validation, and missing/malformed-file handling. An accessible user interface remains a separate requirement.
