# W8-P01 Public Reviewer Package v0.1

Status: **BUILDING / NOT YET ARCHIVED / NO LIVE EFFECTS**

Paper:
**A Governed Shared-Kernel Architecture for Persistent, Auditable Multi-Agent Societies Beyond the LLM Session**

Purpose: provide reviewers with a public, narrow, reproducible package for the manuscript-relevant synthetic/reference experiments without exposing the private World 8 development repository, credentials, operational business state, or live effect infrastructure.

## Frozen evidence relation

Private canonical evidence commit:
`34ed68b6e04c548e7ee14aa16e0e3eecdb1b31f0`

Frozen ref in canonical development repository:
`freeze/w8-p01-evidence-v0.1`

This public package is a reviewer-facing mirror of selected manuscript-relevant experimental source/receipts. The private repository remains the engineering source of record; the paper must cite exact public-package commit/hash after this package is finalized and archived.

## Scope included

Planned/selected public material:
- deterministic reference governance model;
- hardened baseline and mechanism ablations;
- Company/Trading shared-kernel conformance experiment;
- mutation gate;
- compound-fault gate;
- selected tests;
- AutoGen Core external-baseline fixture/requirements/receipt;
- evidence freeze summary and claim ceiling;
- reproducibility instructions.

## Scope excluded

This reviewer package intentionally excludes:
- credentials, API keys, tokens or secrets;
- private Supabase/project identifiers and operational database data;
- business/customer/supplier data;
- live provider credentials or credential-broker implementation details;
- live trading or external business effects;
- private engineering-control-plane state that is not required to reproduce manuscript Results.

## Claim ceiling

This package supports only the frozen W8-P01 manuscript claims. It does **not** establish:
- production readiness;
- trading profitability;
- universal security;
- general superiority over AutoGen, LangGraph, OpenAI Agents SDK, or other frameworks;
- standalone novelty for persistent/provider-independent agent identity, governance/norms, authorization, leases/fencing, checkpoints/recovery, hash chains/provenance, or agent runtimes.

The evaluated contribution is the bounded **effect-governance composition + contract boundary + falsification evidence**.

## Safety

All reference scenarios are synthetic. No code in this package should require a real trading account, real business provider, or production database.

## Build status

- [x] public package branch created
- [x] scope/claim boundary frozen
- [ ] canonical selected files mirrored and SHA mapped
- [ ] tests/workflow added
- [ ] public CI PASS
- [ ] package manifest frozen
- [ ] public review commit frozen
- [ ] archival DOI created

Do not cite this branch as final until the checklist is complete.
