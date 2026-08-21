"""Minimal deterministic World-v6 Phase-1 Kernel primitives.

This module deliberately contains no secretary business logic and no model/provider calls.
A real deployment passes a PostgreSQL DB-API compatible connection factory.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
import uuid
from .resolution import (
    ProjectionProfile,
    ResolutionPatch,
    apply_patch,
    canonical_hash,
    canonical_json,
)


def utcnow():
    return datetime.now(timezone.utc)


def canonical_json_hash(value) -> str:
    """Compatibility alias for the single World Canonical JSON hash contract."""
    return canonical_hash(value)


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex}"


@dataclass(frozen=True)
class BirthResult:
    entity_id: str
    event_id: str
    created_at: str
    dna_hash: str
    lifecycle_stage: str = "NEWBORN"
    operational_status: str = "READY"
    control_epoch: int = 1


class KernelConflict(RuntimeError): pass
class KernelPolicyError(RuntimeError): pass


class Kernel:
    """Deterministic transaction coordinator. Brain text never calls SQL directly."""
    def __init__(self, connection_factory):
        self.connection_factory = connection_factory

    def validate_resolution_patch(
        self,
        *,
        canonical_state: dict,
        profile: ProjectionProfile,
        patch: ResolutionPatch,
        current_version: int,
        source_ref: str,
    ) -> dict:
        """Validate/merge a projected leaf patch before any authoritative transaction.

        This helper grants no authority. Callers must still perform the canonical
        Policy/Approval/expected_version/transaction/Event path before persistence.
        """
        return apply_patch(
            canonical_state,
            profile=profile,
            patch=patch,
            current_version=current_version,
            source_ref=source_ref,
        )

    def birth_entity(self, *, world_id: str, manifest: dict, actor: dict, policy_ref: str) -> BirthResult:
        if manifest.get("root_owner") != "human-root":
            raise KernelPolicyError("birth requires stable human-root owner role")
        if manifest.get("parent_relation") not in {"ROOT_DIRECT", "ENTITY_PARENT"}:
            raise KernelPolicyError("invalid parent_relation")
        if manifest.get("parent_relation") == "ROOT_DIRECT" and manifest.get("parent_entity_id"):
            raise KernelPolicyError("ROOT_DIRECT cannot carry parent_entity_id")
        created_at = utcnow()
        event_id = new_id("evt")
        born_dna = dict(manifest)
        born_dna["lifecycle_stage"] = "NEWBORN"
        born_dna["operational_status"] = "READY"
        born_dna["created_at"] = created_at.isoformat()
        born_dna["creation_event_ref"] = event_id
        dna_hash = canonical_json_hash(born_dna)
        payload = {"entity_id": manifest["entity_id"], "dna_hash": dna_hash, "state": "NEWBORN/READY"}
        payload_hash = canonical_json_hash(payload)

        conn = self.connection_factory()
        try:
            cur = conn.cursor()
            # Entity-id reservation + initial state + creation Event are one transaction.
            cur.execute(
                """INSERT INTO entities
                (world_id,entity_id,entity_version,dna_version,dna_hash,root_owner_ref,parent_relation,parent_entity_id,
                 lifecycle_stage,operational_status,lock_version,control_epoch,last_event_sequence,created_at)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'NEWBORN','READY',1,1,1,%s)""",
                (world_id, manifest["entity_id"], manifest["entity_version"], manifest["dna_version"], dna_hash,
                 manifest["root_owner"], manifest["parent_relation"], manifest.get("parent_entity_id"), created_at),
            )
            cur.execute(
                """INSERT INTO events
                (world_id,entity_id,event_id,entity_sequence,event_type,occurred_at,actor_json,payload_json,payload_hash,
                 schema_version,policy_decision_ref,authorized_control_epoch,outcome)
                VALUES (%s,%s,%s,1,'ENTITY.CREATED',%s,%s::jsonb,%s::jsonb,%s,'1.1.0',%s,1,'success')""",
                (world_id, manifest["entity_id"], event_id, created_at,
                 canonical_json(actor), canonical_json(payload), payload_hash, policy_ref),
            )
            conn.commit()
            return BirthResult(manifest["entity_id"], event_id, created_at.isoformat(), dna_hash)
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def wake_entity(self, *, world_id: str, entity_id: str, expected_version: int, actor: dict, policy_ref: str) -> dict:
        conn = self.connection_factory()
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT lock_version,control_epoch,last_event_sequence,lifecycle_stage,operational_status FROM entities WHERE world_id=%s AND entity_id=%s FOR UPDATE",
                (world_id, entity_id),
            )
            row = cur.fetchone()
            if not row: raise KernelConflict("entity not found")
            lock_version, epoch, seq, stage, status = row
            if lock_version != expected_version: raise KernelConflict("expected_version mismatch")
            if stage != "NEWBORN" or status != "READY": raise KernelConflict("WAKE requires NEWBORN/READY")
            event_id = new_id("evt")
            now = utcnow()
            payload = {"from": "NEWBORN/READY", "to": "NEWBORN/AWAKE"}
            cur.execute(
                "UPDATE entities SET operational_status='AWAKE',lock_version=lock_version+1,last_event_sequence=last_event_sequence+1,updated_at=%s WHERE world_id=%s AND entity_id=%s",
                (now, world_id, entity_id),
            )
            cur.execute(
                """INSERT INTO events
                (world_id,entity_id,event_id,entity_sequence,event_type,occurred_at,actor_json,payload_json,payload_hash,
                 schema_version,policy_decision_ref,authorized_control_epoch,outcome)
                VALUES (%s,%s,%s,%s,'LIFECYCLE.WAKE',%s,%s::jsonb,%s::jsonb,%s,'1.1.0',%s,%s,'success')""",
                (world_id, entity_id, event_id, seq+1, now, canonical_json(actor),
                 canonical_json(payload), canonical_json_hash(payload), policy_ref, epoch),
            )
            conn.commit()
            return {"event_id": event_id, "status": "AWAKE", "lock_version": lock_version+1, "control_epoch": epoch}
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
