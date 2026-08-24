
# Beyond Model-Centric Agents: A Five-Plane Runtime Architecture for Persistent, Provider-Independent, Governed AI Entities

**World 8 / Z0-A - Long-form technical article**  
**Author:** Saeed Farokhi  
**Date:** 24 August 2026  
**Status:** DRAFT FOR REVIEW / NOT A PRODUCTION CLAIM

## Abstract

Contemporary AI-agent systems often bind identity, memory, objectives, authority, and operational continuity to model-provider sessions or orchestration frameworks. That coupling is convenient for short-lived assistants but becomes dangerous when an AI-operated entity is expected to survive provider replacement, concurrent writers, process failure, long-running tasks, external side effects, and controlled self-development. World 8 / Z0-A is a five-plane runtime architecture that separates persistent accountable identity and accepted history from replaceable cognition. Its planes are Canonical Spine, Operational, Observation, Development/Mason, and Evidence/Governance. The governing development rule is: Observation measures, Mason proposes, an independent Evaluator judges, Promotion Authority decides, and the Canonical Spine records.

The architecture composes established systems mechanisms rather than claiming invention of them: commit-time compare-and-swap, intent-bound idempotency, append-oriented event history, transactional outbox with effect receipts, sequencer leases with fencing tokens, database-enforced append-only privileges, deterministic replay, checkpoints, and clean-host restoration. It introduces versioned Objective Contracts and Phenotype Revisions so optimization cannot silently rewrite goals or authority. It also requires attributed Evaluation Receipts because database capability constraints alone do not prove which evaluator produced a result.

The contribution is framed as a falsifiable runtime and governance composition for persistent AI entities, not a claim of biological life, consciousness, AGI, autonomous evolution, or production readiness. Evidence levels E0-E5 and claim-specific gates define the boundary between architecture, local evidence, integration evidence, production-like evidence, and longitudinal evidence.

**Keywords:** persistent AI agents; provider-independent identity; event sourcing; CAS; transactional outbox; AI governance; evidence registry; clean-host restore; multi-brain systems.

## 1. Introduction

A model call is cognition, not identity. A provider thread is a conversation container, not a constitutional ledger. A prompt is not a durable objective contract. A vector index is not authoritative history. A human approval button is not a complete security boundary. These distinctions are easy to ignore in a demo because all components live inside one short-lived process. They become architectural requirements when the system must continue for months or years.

The central World 8 question is therefore not "which model is the agent?" but "what must remain stable when the model is replaced?" Z0-A answers: accountable identity, canonical accepted state, authority, objectives, revision lineage, and evidence. Cognition attaches to this boundary but does not own it.

Earlier World iterations explored multi-brain routing, persistent entities, genomic metaphors, event-sourced state, development stages, and proof obligations. Review exposed a more fundamental problem: self-development can become self-referential when the optimizer chooses the telemetry, defines the metric, proposes the change, evaluates itself, and promotes itself. Z0-A converts that concern into enforceable separation of duties.

## 2. Research question

The research question is whether an AI-operated digital entity can preserve identity, authority, accepted history, and governed change across replacement of its cognition provider while remaining auditable and falsifiable. This requires more than memory persistence. It requires a stable identity namespace, serialized canonical mutation, objective versioning, explicit authorization, independently attributable observation and evaluation, and recovery that survives process and host loss.

The architecture deliberately refuses to make stronger claims before their evidence exists. In particular, it does not equate persistence with biological life, model switching with immortality, self-modification with evolution, or a passing local test suite with production readiness.

## 3. Five planes

The Canonical Spine owns accepted identity and history. Operational services run tasks, roles, cognition, context, connectors, and effects. Observation measures runtime behavior and emits attributed gaps. Development/Mason creates candidate revisions from those gaps. Evidence/Governance judges claims and controls promotion.

This five-way split is important because each plane solves a different trust problem. The Spine must serialize truth. Operational services must remain replaceable. Observation must not be owned by the optimizer. Development must be productive without becoming sovereign. Governance must decide from independently attributed evidence.

Cognition and ingress are intentionally inside Operational rather than separate top-level planes. This keeps the normative topology stable while allowing internal service decomposition.

## 4. Entity, Role, and RoleBinding

Agent frameworks use the word agent for a prompt, persona, process, graph node, or model session. World 8 introduces a stricter object distinction. An Entity carries canonical identity, lifecycle, state head, authority ceiling, and event lineage. A Role is a responsibility slot. A RoleBinding activates a Role for a holder/executor under scope, validity, and bounded grants.

This makes provider replacement ordinary. `company-001` remains the same operational society while `secretary-role` may be fulfilled by different brains or holders. Provider identity is provenance. Role names do not mint authority. Effective authority is derived by intersecting ceilings and explicit grants.

## 5. Objectives outside cognition

Self-improvement becomes incoherent if the improving component may silently rewrite the goal used to judge improvement. Z0-A therefore makes the Objective Contract canonical, immutable per version, and explicit about objective, metrics/SLOs, hard constraints, authority ceiling, risk class, observation contract, adaptation surface, and promotion policy.

A normal Mason candidate may not alter those constitutional fields. If a human or governance process wants to change the objective itself, that is a separately authorized version change with a separate evidence and audit path.

## 6. Phenotype Revisions

A Phenotype Revision represents a proposed executable/configuration change under a fixed Objective version. The revision references a parent revision, specifies the change, migration and rollback, expected metrics, risk, and evidence requirements, and remains a Candidate until promoted.

The term phenotype is operational rather than biological: it means the expressed runtime configuration. Promotion is a separate canonical action using CAS against the current active revision/head. Rollback creates a new event rather than erasing failed history.

## 7. Canonical concurrency

Compare-and-swap is checked at commit time. A pre-read outside the transaction cannot prevent a lost update because another writer may commit between read and write. Two writers targeting one expected head must race such that exactly one succeeds.

Idempotency is equally strict. A stable key is bound to semantic intent. Retrying identical intent can replay the prior result; reusing the same key for changed semantics is a collision error. This prevents "deduplication" from becoming silent semantic corruption.

## 8. Atomicity and external effects

When a canonical transition plans an external effect, the event append, head advancement, required authoritative projections, and outbox obligation are committed atomically. The external provider call occurs later.

Effect execution records attempts and receipts. Network ambiguity is explicit because a provider may have performed an action even when the caller observes a timeout. World 8 therefore claims only scoped effectively-once behavior where connector idempotency and reconciliation support it. Universal exactly-once is a non-claim.

## 9. Leases, fencing, and append-only history

A sequencer lease alone is insufficient because an expired process can continue running. Every sequencer epoch receives a monotonic fencing token and stale tokens are rejected at the storage/commit boundary.

Committed history is protected through database privileges. Runtime roles cannot UPDATE, DELETE, or TRUNCATE committed events. Hash chains provide tamper evidence, not secure privileged storage. These distinctions matter because architectural claims often confuse integrity signals with access control.

## 10. Replay and clean-host restoration

Replay validates the chain before materializing state: hashes, previous heads, versions, duplicate IDs, ordering, reducer compatibility, and final head. A replay implementation that ignores hashes is incomplete even if happy-path state reconstruction works.

Recovery is not proven by restarting the same service. A clean-host restore must reconstruct schema and data in a new environment, verify current head/objective/revision, recreate separated credentials, acquire a fresh higher fencing token, and execute a fresh governed write. That final write proves the recovered system can continue rather than merely display an old snapshot.

## 11. Independent observation

The Observation pipeline is raw telemetry -> normalization -> aggregation/windowing -> SLO/invariant evaluation -> gap signal. Each gap binds the objective version, metric/invariant, observation window, detector version, source telemetry, and rule.

Mason may consume a gap but cannot choose the evidence window or redefine the metric for the change it proposes. This separation prevents the development component from optimizing against a success criterion it controls.

## 12. Mason as an engineering proposer

Mason is intentionally limited. It references a valid gap and objective version, proposes the smallest reversible intervention, provides tests and rollback, and remains inside the allowed adaptation surface. It cannot change identity, authority, hard constraints, objectives, or the Canonical Spine. It cannot directly commit or promote.

This does not prevent advanced automation. It defines the trust boundary within which advanced automation can safely grow.

## 13. Attributed evaluation

Independent evaluation requires attribution. A database role proves that a credential possessed a database capability; it does not prove which model build, program binary, service principal, or human produced the judgment.

An Evaluation Receipt therefore binds evaluator principal, role/credential reference, build digest, candidate revision, Objective version, test-suite/environment digest, metrics, result, evidence references, and optional attestation. Promotion references that receipt.

## 14. Separation of duties

The normative chain is: Observation measures; Mason proposes; Evaluator judges; Promotion Authority promotes; Canonical Spine records; Effect Executor settles authorized obligations.

At low evidence levels multiple modules may share a host, but the semantic boundaries remain. At higher assurance levels credentials and principals are separated. If one actor controls telemetry, candidate creation, evaluation, and promotion, the Z0-A development-governance claim fails.

## 15. Evidence as architecture

World 8 classifies evidence from E0 to E5. E0 is defined but untested. E1 is static contract or privilege evidence. E2 is local/disposable executable evidence. E3 is persistent integration. E4 includes clean-host restore, independent credentials, security/load/chaos, and production-like failure behavior. E5 is longitudinal operation under predefined SLOs.

This ladder is not a score. It prevents an E2 test for concurrency from being used to imply an E4 disaster-recovery claim. Every Proof Registry entry has its own predicate, falsifier, required evidence level, status, and references.

## 16. Failure-oriented testing

The test program attacks the architecture. It races two writers against one head; reuses idempotency keys with changed intent; kills transactions between event/head/outbox writes; submits stale fencing tokens; attempts forbidden database writes; corrupts replay events; removes hash verification through mutation; lets Mason attempt constitutional changes; promotes without a receipt; promotes against stale revisions; restores onto a clean host; and exercises ambiguous external-effect timeouts.

A large happy-path test count is not a substitute for such adversarial tests. Mutation testing is particularly important because it can reveal vacuous tests that remain green after a critical safety check is deleted.

## 17. Provider-independent continuity

A provider handoff should preserve World, Entity/Society, Role, Task, Objective, active Revision, and canonical lineage. The new provider can receive a newly compiled K0-K4 context without owning the identity it continues.

K0 is the World kernel; K1 is Entity/Society context; K2 is Role contract; K3 is current Task; K4 is the minimum retrieved evidence/memory with provenance. This approach treats provider context windows as disposable projections rather than the authoritative memory of the entity.

## 18. Multi-brain operation

World 8 can route cognition across ChatGPT, Grok, DeepSeek, Gemini, Claude, local models, deterministic algorithms, or future providers. Routing may consider capability, cost, latency, availability, privacy, jurisdiction, context size, or policy.

Fallback is an operational availability feature, not an identity operation. Ensemble voting may influence a proposal, but it does not grant authority to commit.

## 19. Relationship to prior World versions

World v6.2 contributed Entity stability, replaceable Brain, scoped context, authority outside cognition, effect controls, evidence gates, and recovery discipline. World 7 strengthened persistent identity, Spine semantics, expected-head conflicts, idempotency, hash chaining, reconstruction, development stages, and proof obligations.

Review of World 7 also exposed overclaim risk: genomic/evolution metaphors, self-referential proof generation, vacuous assertions, insufficient mutation coverage, and evidence-registry attribution problems. Z0-A retains the durable systems insights while moving autonomous evolution out of the normative core.

World 8 v0.1/v0.1.1 provides operational lineage for `world-001`, `company-001`, RoleBindings, Task Bus, and persistent canonical history. Those artifacts do not automatically satisfy new Z0-A gates for Observation independence, Mason confinement, evaluator identity, or clean-host recovery.

## 20. Novelty boundary

World 8 does not claim invention of event sourcing, CAS, transaction isolation, transactional outbox, fencing tokens, hash chains, role-based access control, SLO monitoring, provenance, or model routing.

The potentially novel research contribution is the composition of these mechanisms around a persistent AI identity and a governed development loop, especially the fixed separation:

**Observation measures -> Mason proposes -> Evaluator judges -> Promotion Authority promotes -> Canonical Spine records.**

Novelty should be tested against prior art and empirical comparisons rather than asserted from terminology.

## 21. Limitations and non-claims

The frozen design is not a production certificate. It does not prove security against a fully compromised operating system, database administrator, secret manager, or supply chain. It does not solve semantic alignment by itself; objectives and SLOs can still be incomplete or wrong. Independent evaluators can still err.

The architecture makes no claim of consciousness, biological life, AGI, legal personhood, universal exactly-once effects, or proven autonomous evolution. Stronger claims require stronger evidence.

## 22. Evaluation roadmap

The implementation sequence is contract freeze, Spine hardening, Entity/Role separation, Objective/Revision versioning, independent Observation, constrained Mason, attributed evaluation, governed promotion, clean-host recovery, and end-to-end operational proof.

A strong initial demonstration should cross every plane: one persistent task, one provider handoff without identity fork, one real low-risk external effect with authorization/outbox/receipt, one predefined SLO breach, one Mason proposal, one independent evaluation, and one separate promotion decision.

## 23. Conclusion

World 8 / Z0-A reframes a persistent AI agent as a governed digital Entity whose cognition is replaceable but whose identity, authority, objective, accepted state, and evidence are not owned by cognition. The architecture does not seek autonomy by collapsing control boundaries. It seeks reliable automation by making those boundaries explicit.

The enduring proposition is simple: **replace the brain without replacing the accountable entity; improve the implementation without allowing the improver to silently rewrite the rules.**

## References

1. S. Farokhi, *World v6.2: Fractal Multi-Brain Architecture*, Zenodo, 2026, DOI: 10.5281/zenodo.22040348.
2. World 7 project artifacts, *Living Genome / Genomic Runtime Architecture*, 2026.
3. World 8 / Z0-A, *Final Architecture Baseline*, 24 August 2026.
4. NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, 2023.
5. W3C, *PROV-O: The PROV Ontology*.
6. Cloud Native Computing Foundation, *CloudEvents Specification*.
7. OpenTelemetry Authors, *OpenTelemetry Specification*.
8. PostgreSQL Global Development Group, *PostgreSQL Documentation: Transactions and Privileges*.
9. RFC 8785, *JSON Canonicalization Scheme (JCS)*.
10. Martin Kleppmann, *Designing Data-Intensive Applications*, O'Reilly, 2017.
11. Pat Helland, "Life Beyond Distributed Transactions: An Apostate's Opinion," CIDR, 2007.
12. Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System," CACM, 1978.

## AI-assisted technology disclosure

AI-assisted tools were used for organization, language editing, formatting, and preparation from the author's World architecture materials. No empirical measurement should be inferred from drafting prose. The human author remains responsible for architecture decisions, claims, citations, evidence, and final verification.


# Technical Appendix - Architecture checklist

### A.1 Architectural status and claim boundary
Z0-A is a frozen design baseline, not a production-readiness certificate. Implementation claims are promoted only by claim-specific evidence. Key verification points: design freeze is separate from deployment; no autonomous-evolution claim; no biological or consciousness claim; evidence status remains independently versioned.

### A.2 Final architectural ruling
The source of truth must remain outside replaceable cognition, provider sessions, interfaces, telemetry implementations, and development agents. Key verification points: accepted change moves known canonical state to new canonical state; explicit authority; commit-time CAS; intent-bound idempotency; append-oriented accepted history.

### A.3 Five-plane topology
The normative topology contains exactly Canonical Spine, Operational, Observation, Development/Mason, and Evidence/Governance. Key verification points: Cognition is an Operational service; Ingress is an Operational service; Observation is not canonical truth; Mason is not a promotion authority.

### A.4 Canonical Spine ownership
The Spine owns accountable identity, accepted event history, canonical heads and revisions, checkpoint references, authorizations, and activation history. Key verification points: models cannot write directly; telemetry cannot rewrite state; commits require governed interface; history corrections are new events.

### A.5 Operational Plane
Operational services perform work: tasks, roles, role bindings, cognition routing, context loading, connectors, outbox dispatch, and effect settlement. Key verification points: provider identifiers are provenance; workflow engines are not source of truth; task state must survive process loss; effects remain explicit obligations.

### A.6 Observation Plane
Observation receives raw telemetry and independently produces attributed aggregate measurements, SLO results, invariant results, and gap signals. Key verification points: loss of telemetry must not break replay; detector version recorded; windowing recorded; Mason cannot choose its own evidence window.

### A.7 Development / Mason Plane
Mason is a proposal-only development capability that consumes valid gaps and produces reversible candidate phenotype revisions. Key verification points: cannot alter objectives; cannot alter hard constraints; cannot alter authority or identity; cannot self-evaluate; cannot self-promote.

### A.8 Evidence / Governance Plane
Evidence and Governance own claim predicates, falsifiers, evidence references, evaluator receipts, approval policy, promotion gates, and audit. Key verification points: PASS does not propagate to unrelated claims; OPEN means required evidence is absent; human approval is not the only security boundary; promotion is separately authorized.

### A.9 World object
World is the top-level governance and namespace boundary, not a model session or a single prompt-defined agent. Key verification points: contains constitutional invariants; contains canonical identifier namespace; can contain multiple entities and societies; tracks architecture/runtime lineage.

### A.10 Entity model
An Entity is a persistent accountable object with stable canonical identity, lifecycle, state head, authority ceiling, and event lineage. Key verification points: entity survives provider replacement; entity is not a role name; entity can be individual or organizational; retirement does not silently recycle identity.

### A.11 Society / company-001
company-001 is modeled as an operational Entity/Society with independent history, objectives, roles, tasks, policies, and resources. Key verification points: society can host multiple roles; society identity persists across executors; role changes do not fork society identity; organizational state is canonical where required.

### A.12 Role model
A Role is a responsibility slot with a versioned contract; it is not automatically an independent identity-bearing entity. Key verification points: examples: secretary, sales, accountant; role name does not mint authority; role can require skills; role output contract is versioned.

### A.13 RoleBinding
RoleBinding is the governed relationship that activates a Role for a holder or executor within scope and bounded grants. Key verification points: provider-neutral binding; scope and validity explicit; authority grant bounded by ceilings; binding changes are auditable.

### A.14 Holder and executor
The current holder/executor may be a human proxy, LLM-backed runtime, deterministic service, shared runtime, or dedicated entity. Key verification points: holder is operational provenance; holder replacement need not replace entity; holder capabilities remain bounded; credentials are scoped.

### A.15 Task object and Task Bus
A Task is a stable governed work unit with identity, state, role/scope, artifacts, approvals, outputs, and provenance; a durable bus coordinates handoff. Key verification points: task may cross providers; workflow engine state is not authoritative; retries preserve task identity; terminal/waiting states are explicit.

### A.16 Skill model
A Skill is a reusable capability contract and remains a library/runtime capability unless independent identity, authority, state, or lifecycle is justified. Key verification points: skills do not mint authority; repeated behavior may become deterministic skill; role may bind skills; entity birth is a separate governance decision.

### A.17 Provider-independent identity
Provider, model, session, thread, and channel identifiers are provenance only; canonical identity must not be derived from them. Key verification points: provider handoff preserves World/Entity/Role/Task IDs; provider switch may be recorded as provenance; identity change requires canonical event; session closure is not identity death.

### A.18 Objective Contract
Goals and hard boundaries are externalized into immutable, versioned canonical Objective Contracts rather than buried in prompts. Key verification points: objective; success metrics and SLOs; hard constraints; authority ceiling; risk class; observation contract; allowed adaptation surface; promotion policy.

### A.19 Constitutional change path
Changing Objective, Hard Constraints, Authority ceilings, identity rules, or constitutional invariants is not an ordinary Mason optimization. Key verification points: separate governance authorization; stronger evidence/approval; versioned change; rollback/transition plan; audit trail.

### A.20 Phenotype Revision
A Phenotype Revision is a versioned candidate execution/configuration change linked to a parent revision and a specific Objective version. Key verification points: change set; migration plan; rollback plan; expected metrics; risk; evidence requirements; candidate status before activation.

### A.21 Authority algebra
Effective authority is the intersection of the Entity ceiling, active RoleBinding grant, optional Task grant, policy allowances, and temporal/scope validity. Key verification points: edges are conditions not grants; role names do not grant; authority expansion is privileged; fail closed on ambiguity.

### A.22 Authorization record
Every privileged canonical change or external effect should point to an authorization record or derivable authority context. Key verification points: principal identity; scope; required capability; grant source; expiry; risk class; policy decision.

### A.23 Canonical event schema
Canonical events bind semantic content, lineage, authority, objective/revision context, concurrency preconditions, and provenance. Key verification points: event_id unique; event_version explicit; expected/previous head; intent hash; payload hash; fencing token; evidence refs.

### A.24 Commit-time CAS
The expected head must be checked inside the same transaction that advances the canonical head; application pre-read is insufficient. Key verification points: two writers one head: only one commits; stale writer fails closed; no silent overwrite; retry requires new proposal or rebase.

### A.25 Intent-bound idempotency
Idempotency keys are bound to semantic intent; identical retries may deduplicate, while key reuse with changed semantics is a collision error. Key verification points: durable idempotency record; semantic hash; target/type included; collision is explicit.

### A.26 Atomic canonical transition
Event append, head advance, required authoritative projections, and outbox obligation creation are atomically coupled for a governed transition. Key verification points: fault injection must not create half-state; transaction rollback on partial failure; analytical projections may be asynchronous; authoritative minimum remains atomic.

### A.27 Transactional Outbox
External side effects are represented as obligations committed with the canonical intent and later claimed by an effect executor. Key verification points: obligation has stable id; attempts audited; provider id captured; ambiguous outcome reconciled.

### A.28 Effect Receipt
Effect success or externally visible settlement is recorded by a receipt that links the obligation, attempt, connector, provider result, and reconciliation state. Key verification points: scoped effectively-once only; no universal exactly-once claim; duplicate protection connector-specific; irreversible ambiguity is first-class.

### A.29 Sequencer lease
A sequencer lease identifies the current serialization authority for a governed scope and has explicit expiry and renewal rules. Key verification points: lease state durable for claim scope; single active authority or equivalent serialization; expired holder cannot be trusted by itself; monitor lease health.

### A.30 Fencing token
Each sequencer epoch receives a monotonically increasing fencing token so stale processes are rejected even if they remain alive. Key verification points: storage-side validation; stale token rejection; fresh token after failover; fresh higher token after restore.

### A.31 DB-enforced append-only
Committed history is protected by database privileges and controls, not only by application convention. Key verification points: runtime roles denied UPDATE; denied DELETE; denied TRUNCATE; correction is a new event; break-glass admin is audited.

### A.32 Canonicalization and hashes
Semantic hashes use deterministic serialization and versioned hash formulas to make content and chain verification reproducible. Key verification points: RFC 8785/JCS is a suitable reference; hash binds previous head and semantic content; hash is tamper-evidence; hash is not confidentiality or authorization.

### A.33 Checkpoint model
A checkpoint is a materialized state bound to a known canonical head and reducer/schema version; it accelerates recovery but does not replace accepted history. Key verification points: checkpoint hash/reference; version compatibility; periodic verification; stale checkpoints detected.

### A.34 Verified replay
Replay verifies chain continuity, hashes, event versions, duplicate identifiers, ordering, reducer compatibility, and final head before materialization. Key verification points: corruption fails closed; mutation removing hash check must be caught; duplicate event id rejected; unsupported version requires migration path.

### A.35 Clean-host restore
Continuity is not proven by restarting the same process. Recovery must reconstruct on a clean environment and then accept a fresh governed write. Key verification points: different system identity; restore schema/data; verify chain/head/objective/revision; recreate separated credentials; fresh lease/fencing; record RTO/RPO and restore receipt.

### A.36 Ingress and routing
External input is normalized, authenticated where needed, resolved to entity/task/role scope, and routed through Operational services without direct truth mutation. Key verification points: channel-specific data stays provenance; routing decision auditable; unknown identity handled explicitly; input cannot bypass policy.

### A.37 Brain Gateway
A provider-neutral Brain Gateway invokes replaceable cognition using scoped context, role contracts, tool descriptions, authority limits, and output schemas. Key verification points: ChatGPT/Grok/DeepSeek/Gemini/Claude/local/deterministic possible; provider selection by policy; brain output is proposal/result; brain cannot directly commit.

### A.38 Context Compiler K0-K4
Context is compiled by scope: World kernel, Entity/Society context, Role contract, current Task, and minimum provenance-bearing retrieved evidence. Key verification points: minimize context without losing invariants; source remains outside generated summary; staleness tracked; provider context window is not canonical memory.

### A.39 Memory architecture
Retrieval memory is separated from authoritative state and may include working, episodic, semantic, document/evidence, cold archive, and protected vault layers. Key verification points: summary does not replace source; vector index is rebuildable projection; provenance and timestamps retained; retention/privacy policy explicit.

### A.40 Observation pipeline
The normative pipeline is raw telemetry -> normalization -> aggregation/windowing -> SLO/invariant evaluation -> gap signal -> evidence registry. Key verification points: detector outside Mason; source refs retained; window and method recorded; coverage gaps explicit.

### A.41 SLO and invariant contracts
Success metrics and invariants are versioned as part of Objective/Observation contracts so optimization is judged against a stable target. Key verification points: threshold changes are versioned; identity continuity can be invariant; authorization-before-effect can be invariant; restore success can be SLO/gate.

### A.42 Gap Signal
A gap is an attributed discrepancy with objective version, metric/invariant, window, detector version, observed value, expected condition, and evidence refs. Key verification points: status OPEN/CLOSED/INVALIDATED/SUPERSEDED/EXPIRED; Mason does not own gap definition; confidence/severity optional but explicit; gap provenance immutable.

### A.43 Mason proposal contract
Mason references a valid gap and current objective, proposes the smallest reversible intervention, supplies tests and rollback, and stays in the adaptation surface. Key verification points: proposal has parent revision; proposal has risk; proposal has expected metrics; forbidden fields rejected before evaluation.

### A.44 Evaluator identity
Evaluator identity must be attributable to an authenticated principal and exact evaluator build/profile; database constraints alone are insufficient proof. Key verification points: principal id; credential/role ref; build digest; candidate/objective refs; environment/test digests; metrics/evidence; optional attestation/signature.

### A.45 Evaluation Receipt
An Evaluation Receipt is the durable record that binds the evaluator, candidate, objective, test environment, result, metrics, and evidence. Key verification points: PASS/FAIL/INCONCLUSIVE explicit; receipt immutable once committed; promotion references receipt; receipt does not store secrets.

### A.46 Separation of duties
Observation measures, Mason proposes, Evaluator judges, Promotion Authority promotes, Canonical Spine records, and Effect Executor settles obligations. Key verification points: separate credentials for high assurance; single host may contain logical modules only at low evidence levels; self-approval forbidden; one actor controlling all stages violates Z0-A.

### A.47 Promotion gate
A candidate can become active only after evidence and policy checks and a separately authorized promotion decision committed with CAS. Key verification points: receipt required; hard constraints unchanged; authority unchanged unless constitutional path; stale active revision rejected; activation itself is canonical event.

### A.48 Rollback
Rollback creates a new canonical event activating a known-good or repair revision; it never erases the failed history. Key verification points: trigger recorded; incident/evidence refs; authority recorded; post-rollback verification; external effect compensation handled separately.

### A.49 Evidence levels E0-E5
Evidence levels separate definition, static artifacts, local executable evidence, persistent integration, production-like testing, and longitudinal operation. Key verification points: E0 defined; E1 static; E2 local/disposable; E3 persistent/integration; E4 restore/security/load/chaos/independent credentials; E5 longitudinal SLO/failure envelope.

### A.50 Proof Registry
Every major claim has its own predicate, falsifier, required evidence level, status, environment/build information, and evidence references. Key verification points: OPEN is not failure but absence of required proof; runner output should drive status; manual status cannot override evidence; claims do not inherit neighbor PASS.

### A.51 Threat model
The architecture assumes failures and adversaries across providers, credentials, concurrency, operators, telemetry, storage, and external effects. Key verification points: stale writer; compromised model; prompt injection; compromised Mason; evaluator substitution; credential theft; partial DB failure; corrupt backup; operator error.

### A.52 Secrets and credentials
Secret material is kept outside canonical event payloads and evaluation receipts; only references and principals belong in durable audit records. Key verification points: rotation does not change identity; logs scanned for leaks; least privilege; high-risk credentials separated.

### A.53 Database role matrix
Reference PostgreSQL roles separate sequencer, observer, Mason, evaluator, effect executor, promotion authority, audit, and migration capabilities. Key verification points: GRANT/REVOKE versioned; negative privilege tests; runtime cannot rewrite events; evaluator cannot promote; effect executor cannot self-authorize.

### A.54 Service/API boundaries
Logical service boundaries include commit, query/projection, task, brain gateway, context compiler, observation, gap detection, Mason, evaluation, promotion, effects, and recovery. Key verification points: not required to be microservices; contracts matter more than process count; capability boundaries explicit; API versions governed.

### A.55 Lifecycle states
Entity lifecycle is an explicit operational state machine rather than an implicit property of whether a model session is open. Key verification points: PROVISIONED; ACTIVE; DEGRADED; FROZEN/QUARANTINED; HIBERNATED; RESTORED; RETIRED/TOMBSTONED.

### A.56 Health, repair, sleep and wake
Earlier World concepts of health, sleep/wake, repair, freeze, and reconstruction are retained only when mapped to explicit transitions and evidence. Key verification points: sleep can reduce active cognition; wake reloads current canonical state; repair is governed revision/recovery; no biological claim.

### A.57 Multi-brain routing
Multiple cognition providers may sit behind Brain Gateway and be selected by capability, cost, latency, privacy, jurisdiction, availability, or policy. Key verification points: fallback preserves identity; ensemble vote is not authority; provider metadata retained as provenance; hard constraints cannot weaken on fallback.

### A.58 Skill to Role to Entity growth
Repeated successful behavior may become a deterministic skill, persistent specialization may justify a role, and independent isolation/state may justify an entity. Key verification points: growth is evidence-driven; Mason cannot autonomously birth entities in Z0-A; authority ceilings inherited/bounded; genome/evolution language remains exploratory.

### A.59 Effect risk classes
External actions are classified by reversibility and impact so authorization and evidence requirements scale with risk. Key verification points: read-only; reversible low-risk write; externally visible communication; financial/legal/contractual; destructive/high-impact.

### A.60 Audit model
Audit must reconstruct who or what requested which action, under which objective and authority, against which head, with which provider/build, and with what result. Key verification points: link events/tasks/principals; link objective/revision; link effects/receipts; link gaps/evaluations/promotions; survives workflow engine loss.

### A.61 Failure-response matrix
Failure handling is explicit and fail-closed where ambiguity could corrupt identity, authority, history, or irreversible effects. Key verification points: stale writer -> reject; collision -> reject; partial transaction -> rollback; telemetry outage -> coverage degraded; hash mismatch -> stop replay; ambiguous effect -> reconcile.

### A.62 Adversarial testing
Tests intentionally attack boundaries through races, stale tokens, duplicate identifiers, privilege violations, corrupted replay, forbidden Mason changes, and stale promotion. Key verification points: negative tests mandatory; fault injection; cross-provider continuity test; restore on clean host; effect ambiguity test.

### A.63 Mutation testing
Mutation gates verify that removing a critical check such as replay hash verification or idempotency collision handling causes tests to fail. Key verification points: avoid vacuous test counts; report mutation score by family; critical mutants cannot survive; runner/evidence registry linked.

### A.64 Deployment profiles
Evidence levels map to deployment profiles ranging from local development to persistent integration, production-like separated credentials, and longitudinal operation. Key verification points: E2 local; E3 persistent integration; E4 restore/security/load/chaos; E5 longitudinal.

### A.65 Backup architecture
Backups cover canonical database, event history, schemas/migrations, objective/revision artifacts, evidence registry, manifests, and protected recovery procedures. Key verification points: backup is not proof until restore tested; checksums and manifests; restore order documented; source code alone is insufficient.

### A.66 Repository and release discipline
Normative artifacts are versioned and stable releases are immutable; fixes create new versions, manifests, and hashes. Key verification points: no secrets/private payloads in release; schema migrations versioned; rollback plan for destructive change; machine-readable contracts accompany prose.

### A.67 Lineage from World v6.2
World v6.2 contributed entity stability, replaceable brains, scoped context, authority outside cognition, effect handling, evidence gates, and recovery discipline. Key verification points: retained where compatible; older topology not automatically current; fractal/multi-brain ideas remain operational patterns; Z0-A is stricter about five planes.

### A.68 Lineage from World 7
World 7 contributed persistent identity, Spine semantics, proposal-only cognition, expected-head conflicts, idempotency, hash chains, reconstruction, and explicit proof obligations. Key verification points: genomic metaphor moved out of normative core; autonomous evolution claim rejected without evidence; review exposed vacuous/self-referential tests; mutation and registry discipline strengthened.

### A.69 Lineage from World 8 v0.1/v0.1.1
World 8 v0.1/v0.1.1 provides operational lineage for world-001, company-001, RoleBindings, Task Bus, and persistent canonical history. Key verification points: prior evidence remains valuable; new Z0-A gates require new evidence; Observation/Mason split is new fixed boundary; evaluator attribution is strengthened.

### A.70 Superseded interpretations
Earlier interpretations that conflict with Z0-A are preserved only for history and must not silently return as current architecture. Key verification points: more than five normative planes; Role treated as Entity by name; Mason-controlled telemetry/gaps; direct self-promotion; objective only in prompt; hash chain called secure storage.

### A.71 Explicit non-claims
The architecture does not claim consciousness, biological life, AGI, legal personhood, proven autonomous evolution, universal exactly-once effects, or production readiness by design freeze alone. Key verification points: claim modesty is normative; metaphors are operational only; production requires E3/E4/E5 as applicable; security claims remain scoped.

### A.72 Formal safety properties
Core claims are expressed as falsifiable safety properties so architecture can be tested rather than defended by metaphor. Key verification points: provider replacement preserves identity; stale head cannot commit; stale fencing cannot commit; Mason cannot mutate hard boundaries; promotion requires attributed receipt; restore requires fresh write.

### A.73 Liveness goals
The system should eventually resolve valid tasks, replace expired leases, settle or reconcile effects, decide candidates, recover entities, and close or invalidate gaps. Key verification points: liveness never bypasses safety; timeouts become explicit states; stuck work is observable; manual escalation is allowed but audited.

### A.74 Reference end-to-end scenario
A representative proof crosses all five planes: persistent task, provider handoff, governed commit, real low-risk effect receipt, SLO breach, Mason proposal, independent evaluation, and separate promotion. Key verification points: same entity/task identity across provider change; effect authorization/outbox/receipt; gap from predefined SLO; revision activated with CAS.

### A.75 Z0-A execution roadmap
Implementation proceeds from contract freeze through Spine hardening, Entity/Role separation, Objective/Revision versioning, Observation, Mason, evaluation, promotion, recovery, and operational proof. Key verification points: Z0A-0 contracts; Z0A-1 spine; Z0A-2 identity/role; Z0A-3 objective/revision; Z0A-4 observation; Z0A-5 mason; Z0A-6 evaluator; Z0A-7 promotion; Z0A-8 restore; Z0A-9 operational proof.

### A.76 Z0-A exit gates
Architecture and executable boundary must agree before a gate is called closed; document-only compliance is insufficient. Key verification points: G1 plane isolation; G2 entity/role split; G3 objective/revision versioning; G4 observation independence; G5 Mason confinement; G6 evaluator identity; G7 spine atomicity; G8 recovery; G9 effects.

### A.77 Future-maintainer reconstruction runbook
A future maintainer starts from the frozen architecture version, verifies manifests and schemas, locates proof and role matrices, replays state, checks adversarial gates, and only then resumes development. Key verification points: do not trust old diagrams over current manifest; verify active objective/revision; verify evaluator attribution; verify latest restore; verify provider handoff and effect reconciliation.

### A.78 Minimum machine-readable artifact set
The prose must be accompanied by schemas, role matrices, forbidden-transition policy, promotion policy, proof registry, runtime modules, observation modules, evidence, and release manifests. Key verification points: Objective schema; Revision schema; Event schema; Gap schema; Evaluation receipt schema; RoleBinding schema; Outbox/effect schema; DB role matrix; proof registry.

### A.79 Final continuity contract
Cognition and interfaces are replaceable; accountable identity, canonical state, authority, objectives, accepted history, and evidence remain governed and persistent. Key verification points: prose and runtime must agree; no bypass path; all stronger claims remain evidence-gated; future revisions require explicit governance.