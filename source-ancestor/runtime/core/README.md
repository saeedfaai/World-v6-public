# Minimal World Core for Secretary vertical slice

Only world-level contracts needed by the first entity belong here. Secretary-specific business logic must not move here.

Phase-1 canonical runtime target remains: PostgreSQL atomic Registry/State + Event + optional Outbox transaction, L0 Policy Gate, control_epoch fencing, provider-neutral Brain Gateway, and Executor for external I/O.
