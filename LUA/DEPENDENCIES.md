# Lua runtime and dependency decisions

The curriculum targets Lua 5.4. Pin the following pure-Lua libraries for examples and project validation:

| Package | Exact LuaRocks version | Purpose | License |
|---|---:|---|---|
| `dkjson` | `2.11-1` | JSON encoding/decoding for the task manager and capstone | MIT/X11 |
| `ftcsv` | `1.5.0-1` | CSV parsing/encoding, including quoted fields and multiline fields | MIT |

Install into the Lua 5.4 tree:

```sh
luarocks --lua-version=5.4 install dkjson 2.11
luarocks --lua-version=5.4 install ftcsv 1.5.0-1
```

The CI workflow installs these exact versions and runs `scripts/check_lua_dependencies.lua`. The checks cover JSON round-trip and malformed JSON, plus CSV quoted commas, doubled quotes, embedded newlines, CRLF records, and the canonical five-column header.

**Parser limitation:** `ftcsv` is documented by its maintainer as handling most real-world CSV variants; it is not represented here as a strict RFC 4180 conformance validator. Validate column count and the canonical header in curriculum code, and reject malformed records rather than assuming parsing alone validates the data contract.

Dependency metadata:
- `dkjson` supports Lua 5.1 through 5.5 and is implemented in Lua without mandatory dependencies.
- `ftcsv` is pure Lua and its upstream project reports testing with Lua 5.4; it supports multiline fields and UTF-8 BOM handling.

Review package versions before upgrading. Any version change must update this document and the dependency-validation workflow together.
