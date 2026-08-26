# World 8 — Mason Rulebase (Public Pointer)

> This repository is an ancestor/public reference, **not** the canonical World 8 repository.

World 8 development follows a provider-independent Mason Rulebase. A ChatGPT, Claude, Grok, Codex, Cursor, human developer, or other engineering agent must not rely on conversation history as project state.

## Required engineering sequence

`Bootstrap -> Architecture -> Search -> Code Shadow -> Diagnostics -> Preflight -> Work Claim -> Lease/Fencing/CAS -> Test/Evidence -> Change Packet/Handoff -> Documentation -> Release/Sync`

## Core rules

- Search existing capabilities before building new shared infrastructure.
- Every governed code artifact must have a versioned machine-readable Code Shadow describing purpose, input, output, protocol, config, dependencies, side effects, failures, tests, and replacement requirements.
- Existing governed code cannot be modified without a complete Code Shadow and a valid Mason preflight.
- Every material engineering error must become a diagnostic incident so recovery knowledge accumulates over time.
- Interface/config/protocol changes require compatibility analysis and migration/versioning when breaking.
- Lease does not replace fencing + CAS.
- `IMPLEMENTED != VALIDATED != PROMOTED != ACTIVE`.
- Runtime reality should be generated from deployed systems, not declared manually in documentation.
- Secrets and private recovery details are intentionally not published in this public pointer.

The private/canonical World 8 control surfaces maintain exact recovery links, ownership, active work, leases, diagnostics, and continuity references.
