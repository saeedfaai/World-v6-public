# Kernel API v1.3 Candidate Overlay
Kernel may accept a Resolution Envelope/Patch and validate exact profile
id/version/hash, source ref, expected state version, canonical/projection hashes,
existing scalar path, declared type and write policy. It then continues through
the existing deterministic Policy/Approval/atomic transaction path. Resolution
Compiler has no adapter or state-mutation authority.
