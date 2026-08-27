# World 8 v0.1.0 — Public Research Release

Status: **DEVELOPMENT PRE-RELEASE / NON-PRODUCTION**
Date: 2026-08-27
Author: Saeed Farrokhi
Affiliation: Mechanical Engineering, University of Tehran

## Public entry points

- Live research demo: https://huggingface.co/spaces/Saeedfa/world8-demo
- Zenodo immutable software snapshot: https://zenodo.org/records/22127650
- DOI: https://doi.org/10.5281/zenodo.22127650
- GitHub release anchor: https://github.com/saeedfaai/world-8/releases/tag/V0.1.0
- SSRN submission (under staff review): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7359740
- Hugging Face World 8 collection: https://huggingface.co/collections/Saeedfa/world-8-6a902b1a3a05b0ab39990265

## Research question

World 8 tests an architecture in which **Forecast != Decision != Order**.

The goal is to make multi-agent market reasoning more auditable by separating predictive objects, downstream decisions, and execution artifacts, each with explicit evidence and lifecycle boundaries.

## Frozen evidence

- exact World 8 release commit: `b14f2feea0fa233851a774d6ebd295b63cde75c0`
- empirical evidence commit: `917dd82ed87a3470acfdb9175905ec7c8727c096`
- deterministic evidence archive SHA256: `100484ffba683111622377703e836728817fd6cbb45f53d62e45a5a3766ece70`
- Forecast Contract lifecycle records: `52,920 RESOLVED / 0 integrity failures`

## Main measured result

In the frozen BTC/ETH/SOL historical replay, calibrated weighted aggregation reduced Brier loss relative to the equal-weight raw baseline:

| Market | Brier delta | 95% bootstrap CI |
|---|---:|---:|
| BTC | -0.016393 | [-0.021891, -0.011495] |
| ETH | -0.013569 | [-0.020824, -0.005867] |
| SOL | -0.012082 | [-0.016465, -0.007784] |

The independent SPY/QQQ/GLD replication produced directionally lower calibrated Brier point estimates, but all corresponding bootstrap confidence intervals crossed zero.

## Negative and limiting findings retained

World 8 publication records deliberately retain results that did **not** support a broad performance claim:

- correlation-control penalty: no useful general improvement;
- disagreement shrink: supported small improvement only for SOL;
- regime weighting: small supported improvement for ETH, supported worsening for BTC, SOL inconclusive;
- shadow cold-start: neutral;
- volatility risk veto: no Decision/UOP benefit in the frozen replay.

## What this release does NOT claim

This release does not claim:

- trading profitability;
- production readiness;
- universal superiority across markets;
- causal superiority of the architecture;
- autonomous economic agency, AGI, or consciousness;
- authorization for live trading or capital deployment.

## Feedback requested

Technical critique is especially welcome on:

1. Forecast / Decision / Order separation;
2. evidence and lifecycle contracts;
3. no-lookahead / replay methodology;
4. calibration and ensemble evaluation;
5. negative-result interpretation;
6. reproducibility and failure modes;
7. how the public demo should evolve into a more useful research tool.

## Publication principle

**Parallelize distribution; serialize truth.**

GitHub is the living engineering source of truth. Zenodo preserves immutable release history. Public demo/distribution surfaces point back to the frozen evidence and release receipts rather than becoming competing canonical sources.
