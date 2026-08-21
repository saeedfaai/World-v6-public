-- Secretary-specific durable conversation continuity.
-- Provider sessions (ChatGPT/Google/etc.) and Telegram chats are transports only, never the source of conversation truth.
CREATE TABLE IF NOT EXISTS secretary_conversations (
  world_id TEXT NOT NULL,
  entity_id TEXT NOT NULL,
  principal_id TEXT NOT NULL,
  conversation_id TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (world_id, entity_id, principal_id, conversation_id)
);

CREATE TABLE IF NOT EXISTS secretary_conversation_messages (
  world_id TEXT NOT NULL,
  entity_id TEXT NOT NULL,
  principal_id TEXT NOT NULL,
  conversation_id TEXT NOT NULL,
  message_id TEXT NOT NULL,
  direction TEXT NOT NULL CHECK (direction IN ('INBOUND','OUTBOUND')),
  source_channel TEXT NOT NULL,
  channel_actor_id TEXT NULL,
  brain_provider TEXT NULL,
  body_text TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (world_id, entity_id, message_id),
  FOREIGN KEY (world_id, entity_id, principal_id, conversation_id)
    REFERENCES secretary_conversations(world_id, entity_id, principal_id, conversation_id)
);
CREATE INDEX IF NOT EXISTS idx_secretary_conversation_context
  ON secretary_conversation_messages(world_id, entity_id, principal_id, conversation_id, created_at);
