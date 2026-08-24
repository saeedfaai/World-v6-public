# World 8 / Z0-A — Patent Candidate Inventory

**Classification:** PUBLIC-SAFE TRIAGE ONLY  
**Important:** Do not place undisclosed invention details or claim language in this public file.

## Purpose

This inventory is a triage framework for deciding which technical mechanisms may deserve confidential patentability review. It is **not** a patent application, patentability opinion, freedom-to-operate opinion, or representation that any item is novel, non-obvious, enabled, or patent-eligible.

Because World 8 / Z0-A has already been publicly disclosed, filing strategy is time-sensitive and jurisdiction-dependent. Any undisclosed improvement should be kept private until qualified patent counsel has reviewed disclosure timing and filing options.

## Publicly disclosed technical families to review

The following high-level families are already part of the public architecture and may be screened for claimable combinations or implementations, while avoiding any assumption that the individual underlying mechanisms are novel:

| Candidate family | Public-safe description | Public disclosure status | Triage status |
|---|---|---|---|
| Provider-independent accountable identity | Identity continuity remains distinct from provider/model/session/thread/channel/device provenance | Public | Counsel review needed |
| Governed five-plane architecture | Separation among Canonical Spine, Operational, Observation, Development/Mason, and Evidence/Governance | Public | Counsel review needed |
| Observation-to-gap attribution pipeline | Independent observation converts telemetry into attributable gaps before proposal generation | Public | Counsel review needed |
| Proposal-only development with independent evaluation | Mason proposes but cannot directly promote protected state; independent evidence/evaluation gates promotion | Public | Counsel review needed |
| Versioned objective/phenotype governance | Versioned Objective Contracts and Phenotype Revisions with controlled promotion | Public | Counsel review needed |
| Recoverable continuity / clean-host identity test | Identity and accountable state are tested through clean-host restore/reconstruction | Public | Counsel review needed |
| Effect-obligation governance | External effects are represented as governed obligations with receipts/reconciliation rather than relying on universal exactly-once claims | Public | Counsel review needed |
| Integrated continuity/governance contract | Specific combination of identity, authority, evidence, promotion, recovery, and effect accountability | Public | Highest-value combination to examine |

## Explicitly not asserted as individually novel

The public release does not claim individual novelty for standard mechanisms such as compare-and-swap, event sourcing, transactional outbox, fencing, hash chains, ordinary idempotency, or generic append-only logs. Any patent strategy should focus on a technically specific, supported combination or implementation rather than relabeling established mechanisms.

## Confidential patent review worksheet

For each candidate, the **private** patent file should answer:

1. What is the exact technical problem?
2. What conventional systems fail to do?
3. What is the precise technical mechanism?
4. What steps/components are mandatory vs. optional?
5. What measurable technical effect results?
6. What prior art is closest?
7. What was the earliest conception date and evidence?
8. What was the first public disclosure date?
9. Which jurisdictions matter commercially?
10. Who are the inventors under applicable patent law?
11. Is there enabling technical detail sufficient for filing?
12. What improvements remain undisclosed and should stay confidential until filing?

## Evidence packet for counsel

Prepare privately:

- Zenodo DOI and timestamp;
- Software Heritage SWHIDs;
- frozen Git commit and directory hashes;
- earlier World 6 / World 7 lineage where relevant;
- architecture change log;
- inventor/contributor records;
- dated design notes and experiment evidence;
- disclosure timeline: GitHub, Zenodo, Reddit, LinkedIn, ResearchGate/other public venues;
- known prior-art references;
- confidential implementation details not present in the public baseline.

## Filing rule

Do not publicly add new enabling details for an unpublished invention merely to strengthen this inventory. Record them in an access-controlled private patent dossier and obtain jurisdiction-specific advice before further disclosure.
