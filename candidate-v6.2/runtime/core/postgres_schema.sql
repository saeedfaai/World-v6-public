-- World v6 Phase-1 canonical PostgreSQL authority schema.
-- State + Event metadata + optional Outbox intent share one transaction boundary.
CREATE TABLE IF NOT EXISTS worlds (
  world_id text PRIMARY KEY,
  constitution_version text NOT NULL,
  status text NOT NULL,
  control_epoch bigint NOT NULL DEFAULT 1,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS entities (
  world_id text NOT NULL REFERENCES worlds(world_id),
  entity_id text NOT NULL,
  entity_version text NOT NULL,
  dna_version text NOT NULL,
  dna_hash text NOT NULL,
  root_owner_ref text NOT NULL,
  parent_relation text NOT NULL CHECK (parent_relation IN ('ROOT_DIRECT','ENTITY_PARENT')),
  parent_entity_id text,
  lifecycle_stage text NOT NULL,
  operational_status text NOT NULL,
  lock_version bigint NOT NULL DEFAULT 1,
  control_epoch bigint NOT NULL DEFAULT 1,
  last_event_sequence bigint NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL,
  updated_at timestamptz NOT NULL DEFAULT now(),
  archived boolean NOT NULL DEFAULT false,
  PRIMARY KEY (world_id, entity_id),
  CHECK ((parent_relation='ROOT_DIRECT' AND parent_entity_id IS NULL) OR
         (parent_relation='ENTITY_PARENT' AND parent_entity_id IS NOT NULL))
);

CREATE TABLE IF NOT EXISTS events (
  world_id text NOT NULL,
  entity_id text NOT NULL,
  event_id text PRIMARY KEY,
  entity_sequence bigint NOT NULL,
  event_type text NOT NULL,
  occurred_at timestamptz NOT NULL,
  causation_id text,
  correlation_id text,
  actor_json jsonb NOT NULL,
  payload_json jsonb,
  payload_hash text NOT NULL,
  schema_version text NOT NULL,
  policy_decision_ref text,
  approval_ref text,
  authorized_control_epoch bigint,
  outcome text,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (world_id, entity_id, entity_sequence),
  FOREIGN KEY (world_id, entity_id) REFERENCES entities(world_id, entity_id)
);

CREATE TABLE IF NOT EXISTS commands (
  world_id text NOT NULL,
  entity_id text NOT NULL,
  command_id text PRIMARY KEY,
  command_type text NOT NULL,
  actor_json jsonb NOT NULL,
  payload_json jsonb NOT NULL,
  payload_hash text NOT NULL,
  status text NOT NULL,
  expected_version bigint,
  idempotency_scope text,
  idempotency_key text,
  effect_hash text,
  authorized_control_epoch bigint,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  FOREIGN KEY (world_id, entity_id) REFERENCES entities(world_id, entity_id),
  UNIQUE (idempotency_scope, idempotency_key, effect_hash)
);

CREATE TABLE IF NOT EXISTS approvals (
  approval_id text PRIMARY KEY,
  world_id text NOT NULL,
  entity_id text NOT NULL,
  command_id text NOT NULL REFERENCES commands(command_id),
  approver_ref text NOT NULL,
  decision text NOT NULL,
  action text NOT NULL,
  resource_ref text,
  recipient_ref text,
  payload_hash text NOT NULL,
  policy_version text NOT NULL,
  expected_version bigint,
  issued_at timestamptz NOT NULL,
  expires_at timestamptz,
  FOREIGN KEY (world_id, entity_id) REFERENCES entities(world_id, entity_id)
);

CREATE TABLE IF NOT EXISTS outbox (
  outbox_id text PRIMARY KEY,
  world_id text NOT NULL,
  entity_id text NOT NULL,
  command_id text NOT NULL REFERENCES commands(command_id),
  destination text NOT NULL,
  action text NOT NULL,
  resource_ref text,
  recipient_ref text,
  payload_json jsonb,
  payload_ref text,
  payload_hash text NOT NULL,
  effect_hash text NOT NULL,
  idempotency_scope text NOT NULL,
  idempotency_key text NOT NULL,
  approval_ref text,
  policy_decision_ref text NOT NULL,
  authorized_control_epoch bigint NOT NULL,
  effect_semantics text NOT NULL CHECK (effect_semantics IN ('NATIVE_IDEMPOTENT','RECONCILABLE','NON_IDEMPOTENT')),
  status text NOT NULL DEFAULT 'QUEUED',
  attempts integer NOT NULL DEFAULT 0,
  provider_receipt text,
  last_error text,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  FOREIGN KEY (world_id, entity_id) REFERENCES entities(world_id, entity_id),
  UNIQUE (idempotency_scope, idempotency_key, effect_hash)
);

CREATE INDEX IF NOT EXISTS idx_events_stream ON events(world_id, entity_id, entity_sequence);
CREATE INDEX IF NOT EXISTS idx_outbox_status ON outbox(status, created_at);
