"""Secretary-001 bridge to the provider-neutral RC2 Portable Brain runtime.

This bridge reads canonical entity state, creates a profile-bound BrainRequest,
and returns a proposal.  It never persists a model answer and never executes an
external effect on its own.
"""
from __future__ import annotations

from core.brain_gateway import BrainInputSegment, BrainRequest
from core.portable_brain import PortableSecretaryResult, PortableSecretaryRunner

from .resolution_profile import (
    CONVERSATION_PROFILE,
    TASK_PROFILE,
    conversation_dict,
    task_dict,
)


class PortableSecretaryService:
    def __init__(self, secretary, runner: PortableSecretaryRunner) -> None:
        if runner.pack.entity_id != "secretary-001":
            raise ValueError("Portable Brain Pack is not bound to secretary-001")
        self.secretary = secretary
        self.runner = runner

    def decide_task(self, task_id: str) -> PortableSecretaryResult:
        """Ask any compatible Brain to propose a response for one canonical task."""
        task = self.secretary.store.tasks[task_id]
        profile = TASK_PROFILE
        segment = BrainInputSegment(
            segment_id="task",
            canonical=task_dict(task),
            profile_id=profile.profile_id,
            profile_version=profile.version,
            profile_hash=profile.profile_hash,
            source_ref=f"task:{task.task_id}",
            source_version=0,
            desired_resolution=self.secretary.execution_resolution,
            minimum_resolution="R0",
            purpose="TASK_PROPOSAL",
            data_class="INTERNAL",
            freshness="CURRENT",
        )
        return self.runner.run(
            BrainRequest(
                "world-v6.brain-request.v2",
                "secretary.task",
                (segment,),
                world_id="world-v6",
                entity_id="secretary-001",
                principal_id="human-root",
                conversation_id=self.secretary.DEFAULT_CONVERSATION_ID,
            )
        )

    def decide_latest_message(
        self,
        *,
        principal_id: str = "human-root",
        conversation_id: str | None = None,
    ) -> PortableSecretaryResult:
        """Propose a reply from the latest canonical conversation message."""
        conversation_id = conversation_id or self.secretary.DEFAULT_CONVERSATION_ID
        messages = self.secretary.store.conversation_context(principal_id, conversation_id, 1)
        if not messages:
            raise LookupError("no canonical conversation message is available")
        message = messages[-1]
        profile = CONVERSATION_PROFILE
        segment = BrainInputSegment(
            segment_id="conversation",
            canonical=conversation_dict(message),
            profile_id=profile.profile_id,
            profile_version=profile.version,
            profile_hash=profile.profile_hash,
            source_ref=f"conversation-message:{message.message_id}",
            source_version=0,
            desired_resolution=self.secretary.execution_resolution,
            minimum_resolution="R0",
            purpose="DRAFT_REPLY",
            data_class="INTERNAL",
            freshness="APPEND_ONLY",
        )
        return self.runner.run(
            BrainRequest(
                "world-v6.brain-request.v2",
                "secretary.reply",
                (segment,),
                world_id="world-v6",
                entity_id="secretary-001",
                principal_id=principal_id,
                conversation_id=conversation_id,
            )
        )
