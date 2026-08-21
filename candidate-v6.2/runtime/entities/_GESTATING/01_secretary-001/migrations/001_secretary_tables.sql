-- PostgreSQL target. Secretary-specific domain tables only; world Kernel/Event/Outbox tables belong to Core migrations.
CREATE TABLE IF NOT EXISTS secretary_tasks (
  task_id TEXT PRIMARY KEY,
  world_id TEXT NOT NULL,
  entity_id TEXT NOT NULL,
  title TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('OPEN','DONE','CANCELLED')),
  priority TEXT NOT NULL,
  domain TEXT NOT NULL,
  due_at TIMESTAMPTZ NULL,
  goal_id TEXT NULL,
  next_action TEXT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_secretary_tasks_due ON secretary_tasks(entity_id,status,due_at);

CREATE TABLE IF NOT EXISTS secretary_customer_prices (
  price_id TEXT PRIMARY KEY,
  world_id TEXT NOT NULL,
  entity_id TEXT NOT NULL,
  customer_id TEXT NOT NULL,
  product_key TEXT NOT NULL,
  unit TEXT NOT NULL,
  unit_price_irr NUMERIC(24,4) NOT NULL,
  valid_until TIMESTAMPTZ NULL,
  approved_by TEXT NOT NULL,
  approved_at TIMESTAMPTZ NOT NULL,
  active BOOLEAN NOT NULL DEFAULT true,
  UNIQUE(world_id, entity_id, customer_id, product_key, unit, approved_at)
);
CREATE INDEX IF NOT EXISTS idx_secretary_prices_lookup ON secretary_customer_prices(entity_id,customer_id,product_key,unit,active,valid_until);

CREATE TABLE IF NOT EXISTS secretary_price_inquiries (
  inquiry_id TEXT PRIMARY KEY,
  world_id TEXT NOT NULL,
  entity_id TEXT NOT NULL,
  customer_id TEXT NOT NULL,
  product_key TEXT NOT NULL,
  unit TEXT NOT NULL,
  requested_quantity NUMERIC(24,4) NOT NULL,
  status TEXT NOT NULL DEFAULT 'PENDING_ROOT',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  resolved_at TIMESTAMPTZ NULL
);
