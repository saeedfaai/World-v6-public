# Brain Gateway Contract — World v6.2 RC1

1. Brain/Provider is replaceable cognition, never Entity identity, authority,
   canonical state or conversation truth.
2. A request contains one or more profile-scoped canonical input segments.
3. Provider compatibility receives value-free descriptors only.
4. Provider capability must match exact `profile_id + version + hash`; a global
   scalar maximum is insufficient.
5. Gateway verifies every profile/hash, negotiates each segment without lowering
   minimum, projects the actual canonical value, and passes only consumer-safe
   derived envelopes.
6. The effective result is a Resolution vector when more than one domain exists.
7. Failover may change Provider but cannot change world/entity/principal/
   conversation identity, purpose, classification, freshness, profile, minimum
   Resolution, Policy or approval requirements.
8. Up-resolution reloads canonical input and recompiles; no lower envelope is
   inverted or semantically guessed.
