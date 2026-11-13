Lua capstone reference core

Install dkjson with LuaRocks, then run the tests from the repository root:

    luarocks install dkjson
    lua LUA/capstone/test_records.lua

The tested core implements the shared six-field schema, optional done state, CRUD, search, JSON persistence, validation, and malformed/missing-file handling. An accessible user interface remains a separate requirement.
