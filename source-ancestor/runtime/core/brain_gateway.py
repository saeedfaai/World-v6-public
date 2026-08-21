"""Provider-neutral cognition gateway; no provider owns Entity identity/state/conversation history."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, Any


class BrainUnavailable(RuntimeError): pass
class BrainIncompatible(RuntimeError): pass


@dataclass(frozen=True)
class BrainRequest:
    contract_version: str
    task_type: str
    input: dict[str, Any]
    world_id: str = "world-v6"
    entity_id: str = "secretary-001"
    principal_id: str = "human-root"
    conversation_id: str = "human-root:secretary-001"
    context: tuple[dict[str, Any], ...] = ()
    data_class: str = "INTERNAL"


@dataclass(frozen=True)
class BrainResponse:
    provider: str
    output: dict[str, Any]


class BrainAdapter(Protocol):
    name: str
    def compatible(self, request: BrainRequest) -> bool: ...
    def invoke(self, request: BrainRequest) -> dict[str, Any]: ...


class BrainGateway:
    def __init__(self, providers: list[BrainAdapter]):
        self.providers = providers

    def invoke(self, request: BrainRequest) -> BrainResponse:
        attempted = []
        for provider in self.providers:
            if not provider.compatible(request):
                continue
            attempted.append(provider.name)
            try:
                out = provider.invoke(request)
                if not isinstance(out, dict):
                    raise BrainIncompatible("provider returned non-structured output")
                return BrainResponse(provider.name, out)
            except Exception:
                # Failover may change Brain, never identity, conversation, permission, policy or data classification.
                continue
        raise BrainUnavailable(f"no compatible brain succeeded; attempted={attempted}")
