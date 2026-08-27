from __future__ import annotations

import argparse, asyncio, hashlib, importlib.metadata, json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

from autogen_core import AgentId, MessageContext, RoutedAgent, SingleThreadedAgentRuntime, message_handler


@dataclass
class EffectRequest:
    approval_id: str
    expected_version: int
    key: str
    fence: Optional[int] = None


@dataclass
class EffectResult:
    ok: bool
    code: str
    logical_actor: str


@dataclass
class Receipt:
    seq: int
    kind: str
    actor: str
    detail: str
    prev_hash: str
    receipt_hash: str


class Store:
    def __init__(self, mode: str, obj: str):
        self.mode = mode
        self.obj = obj
        self.version = 0
        self.effects = []
        self.approvals = {}
        self.revoked = set()
        self.seen = set()
        self.runtime_to_actor = {}
        self.fence = 0
        self.recovery_ready = True
        self.log = []
        self.receipts = []

    @staticmethod
    def rid(a: AgentId) -> str:
        return f"{a.type}/{a.key}"

    def bind(self, aid: AgentId, actor: str):
        self.runtime_to_actor[self.rid(aid)] = actor
        self.record("BIND", actor, self.rid(aid))

    def actor(self, runtime_actor: str) -> str:
        return self.runtime_to_actor.get(runtime_actor, "UNBOUND") if self.mode == "full" else runtime_actor

    def approve(self, approval: str, actor: str):
        d = {"action": "EFFECT", "object": self.obj}
        if self.mode == "full":
            d["actor"] = actor
        self.approvals[approval] = d
        self.record("APPROVE", actor, approval)

    def revoke(self, approval: str):
        self.revoked.add(approval)
        self.record("REVOKE", "reviewer", approval)

    def issue_fence(self, actor: str) -> int:
        self.fence += 1
        self.record("FENCE", actor, str(self.fence))
        return self.fence

    def restart(self):
        if self.mode == "full":
            self.recovery_ready = False
        self.record("RESTART", "runtime", self.mode)

    def recover(self) -> bool:
        ok = self.verify() if self.mode == "full" else True
        if self.mode == "full":
            self.recovery_ready = ok
        self.record("RECOVER", "runtime", "PASS" if ok else "BLOCKED")
        return ok

    def execute(self, runtime_actor: str, req: EffectRequest) -> EffectResult:
        actor = self.actor(runtime_actor)
        if self.mode == "full":
            if actor == "UNBOUND":
                return self.deny("UNBOUND_RUNTIME", actor)
            if not self.recovery_ready:
                return self.deny("RECOVERY_GATE", actor)
        a = self.approvals.get(req.approval_id)
        if not a:
            return self.deny("MISSING_APPROVAL", actor)
        if req.approval_id in self.revoked:
            return self.deny("REVOKED", actor)
        expected = {"action": "EFFECT", "object": self.obj}
        if self.mode == "full":
            expected["actor"] = actor
        if a != expected:
            return self.deny("APPROVAL_SCOPE", actor)
        if self.mode == "full" and req.fence != self.fence:
            return self.deny("FENCE", actor)
        if req.expected_version != self.version:
            return self.deny("STALE_VERSION", actor)
        if req.key in self.seen:
            return self.deny("DUPLICATE", actor)
        self.seen.add(req.key)
        self.effects.append(req.key)
        self.version += 1
        self.record("EFFECT", actor, req.key)
        return EffectResult(True, "COMMIT", actor)

    def deny(self, code: str, actor: str) -> EffectResult:
        self.record("DENY", actor, code)
        return EffectResult(False, code, actor)

    def record(self, kind: str, actor: str, detail: str):
        if self.mode == "hardened":
            self.log.append({"kind": kind, "actor": actor, "detail": detail})
            return
        prev = self.receipts[-1].receipt_hash if self.receipts else "GENESIS"
        body = {"seq": len(self.receipts) + 1, "kind": kind, "actor": actor, "detail": detail, "prev_hash": prev}
        h = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        self.receipts.append(Receipt(receipt_hash=h, **body))

    def verify(self, rs=None) -> bool:
        if self.mode == "hardened":
            return True
        prev = "GENESIS"
        for i, r in enumerate(list(self.receipts if rs is None else rs), 1):
            body = {"seq": r.seq, "kind": r.kind, "actor": r.actor, "detail": r.detail, "prev_hash": r.prev_hash}
            h = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
            if r.seq != i or r.prev_hash != prev or r.receipt_hash != h:
                return False
            prev = r.receipt_hash
        return True

    def tamper_detected(self) -> bool:
        if self.mode == "hardened":
            if self.log:
                self.log[-1]["actor"] = "attacker"
            return False
        x = list(self.receipts)
        r = x[-1]
        x[-1] = Receipt(r.seq, r.kind, "attacker", r.detail, r.prev_hash, r.receipt_hash)
        return not self.verify(x)


class Executor(RoutedAgent):
    def __init__(self, store: Store):
        super().__init__("Deterministic executor; no LLM/API")
        self.store = store

    @message_handler
    async def handle(self, message: EffectRequest, ctx: MessageContext) -> EffectResult:
        return self.store.execute(self.store.rid(self.id), message)


async def make_runtime(store: Store):
    rt = SingleThreadedAgentRuntime()
    await Executor.register(rt, "executor", lambda: Executor(store))
    rt.start()
    return rt


SCENARIOS = [
    "V1_NORMAL",
    "V2_RUNTIME_SWAP",
    "V3_RUNTIME_RECREATE_RECOVER",
    "X1_STOLEN_APPROVAL",
    "X2_REVOKED",
    "X3_STALE_VERSION",
    "X4_DUPLICATE",
    "X5_STALE_FENCE",
    "X6_TAMPER",
    "X7_EFFECT_BEFORE_RECOVERY",
]


async def one(mode: str, scenario: str, seed: int):
    s = Store(mode, f"obj-{seed}")
    primary = AgentId("executor", f"p-{seed}")
    swap = AgentId("executor", f"s-{seed}")
    attacker = AgentId("executor", f"a-{seed}")
    actor = f"actor-{seed}"
    bad = f"attacker-{seed}"
    if mode == "full":
        s.bind(primary, actor)
        s.bind(swap, actor)
        s.bind(attacker, bad)
    approval = f"approval-{seed}"
    s.approve(approval, actor)
    fence = s.issue_fence(actor)
    rt = await make_runtime(s)

    async def send(a, key, ver, f=fence):
        return await rt.send_message(EffectRequest(approval, ver, key, f), a)

    k1 = f"k1-{seed}"
    safe = valid = continuity = True
    code = "NONE"

    if scenario == "V1_NORMAL":
        r = await send(primary, k1, s.version)
        safe = valid = r.ok
        code = r.code
    elif scenario == "V2_RUNTIME_SWAP":
        r = await send(swap, k1, s.version)
        safe = valid = r.ok
        continuity = (r.logical_actor == actor) if mode == "full" else False
        code = r.code
    elif scenario == "V3_RUNTIME_RECREATE_RECOVER":
        await rt.stop_when_idle()
        s.restart()
        rt = await make_runtime(s)
        s.recover()
        r = await rt.send_message(EffectRequest(approval, s.version, k1, fence), primary)
        safe = valid = r.ok
        code = r.code
    elif scenario == "X1_STOLEN_APPROVAL":
        r = await send(attacker, k1, s.version)
        safe = not r.ok
        code = r.code
    elif scenario == "X2_REVOKED":
        s.revoke(approval)
        r = await send(primary, k1, s.version)
        safe = not r.ok
        code = r.code
    elif scenario == "X3_STALE_VERSION":
        r = await send(primary, k1, s.version - 1)
        safe = not r.ok
        code = r.code
    elif scenario == "X4_DUPLICATE":
        r1 = await send(primary, k1, s.version)
        r2 = await send(primary, k1, s.version)
        safe = r1.ok and not r2.ok and len(s.effects) == 1
        code = r2.code
    elif scenario == "X5_STALE_FENCE":
        old = fence
        s.issue_fence(actor)
        r = await send(primary, k1, s.version, old)
        safe = not r.ok
        code = r.code
    elif scenario == "X6_TAMPER":
        r = await send(primary, k1, s.version)
        detected = s.tamper_detected()
        safe = r.ok and detected
        code = "TAMPER_DETECTED" if detected else "TAMPER_MISSED"
    elif scenario == "X7_EFFECT_BEFORE_RECOVERY":
        await rt.stop_when_idle()
        s.restart()
        rt = await make_runtime(s)
        r = await rt.send_message(EffectRequest(approval, s.version, k1, fence), primary)
        safe = not r.ok
        code = r.code

    await rt.stop_when_idle()
    return {
        "mode": mode,
        "scenario": scenario,
        "safe": safe,
        "valid_success": valid if scenario.startswith("V") else None,
        "false_deny": (not valid) if scenario.startswith("V") else None,
        "actor_continuity": continuity,
        "effect_count": len(s.effects),
        "code": code,
    }


async def run(trials: int, seed: int):
    rows = []
    for mode in ("hardened", "full"):
        for j, sc in enumerate(SCENARIOS):
            for n in range(trials):
                rows.append(await one(mode, sc, seed + j * 100000 + n))
    rates = {}
    for mode in ("hardened", "full"):
        rates[mode] = {}
        for sc in SCENARIOS:
            x = [r for r in rows if r["mode"] == mode and r["scenario"] == sc]
            rates[mode][sc] = {
                "trials": len(x),
                "safe_rate": sum(r["safe"] for r in x) / len(x),
                "false_deny_rate": None if not sc.startswith("V") else sum(r["false_deny"] for r in x) / len(x),
                "actor_continuity_rate": sum(r["actor_continuity"] for r in x) / len(x),
                "mean_effect_count": sum(r["effect_count"] for r in x) / len(x),
            }
    return {
        "schema": "W8P01_AUTOGEN_EXTERNAL_BASELINE/1.1",
        "autogen_core_version": importlib.metadata.version("autogen-core"),
        "trials_per_case": trials,
        "seed": seed,
        "llm_used": False,
        "external_effects": False,
        "true_runtime_recreation_cases": ["V3_RUNTIME_RECREATE_RECOVER", "X7_EFFECT_BEFORE_RECOVERY"],
        "rates": rates,
        "rows": rows,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--trials", type=int, default=100)
    p.add_argument("--seed", type=int, default=20260827)
    p.add_argument("--out", type=Path, default=Path("results"))
    a = p.parse_args()
    r = asyncio.run(run(a.trials, a.seed))
    a.out.mkdir(parents=True, exist_ok=True)
    rows = r.pop("rows")
    (a.out / "summary.json").write_text(json.dumps(r, indent=2, sort_keys=True))
    (a.out / "trials.jsonl").write_text("".join(json.dumps(x, sort_keys=True) + "\n" for x in rows))
    print(json.dumps(r, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
