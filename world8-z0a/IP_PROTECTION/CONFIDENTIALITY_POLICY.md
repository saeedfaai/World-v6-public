# World 8 / Z0-A — Confidentiality Policy

**Classification:** PUBLIC POLICY / NON-CONFIDENTIAL  
**Applies to:** future development, contributors, contractors, reviewers, partners, vendors, and commercial pilots.

## 1. Objective

World 8 distinguishes public architecture/evidence from private implementation and commercial know-how. Public disclosure should be intentional, reviewed, and traceable. Confidential information should be disclosed only on a need-to-know basis under an appropriate agreement.

## 2. Public material

The following may be public when intentionally released and approved:

- published architecture and manuscripts;
- DOI/SWHID/citation metadata;
- public evidence receipts and non-sensitive manifests;
- deliberately published interface descriptions and high-level contracts;
- public claim boundaries, falsifiers, and non-sensitive evaluation results.

## 3. Confidential material

Unless specifically approved for publication, treat the following as confidential:

- unpublished source code and implementation details;
- deployment architecture not already disclosed;
- agent orchestration recipes, routing logic, scoring systems, prompts where commercially sensitive, and operational tuning;
- unreleased algorithms, mechanisms, experiments, and patent candidates;
- private datasets, customer data, CRM information, partner information, pricing logic, unit economics, sales strategy, negotiation playbooks, and vendor terms;
- security architecture, threat-response procedures, credentials, keys, tokens, secrets, internal endpoints, access-control data, and vulnerability information;
- proprietary benchmarks, production telemetry, incident reports, failure datasets, and recovery procedures not approved for public release;
- confidential business plans, fundraising materials, cap-table information, and transaction terms.

## 4. Never commit to a public repository

Never commit passwords, API keys, private keys, access tokens, customer personal data, authentication cookies, confidential contracts, unreleased patent claim language, or trade-secret implementation details to a public repository.

If accidental disclosure occurs, immediately revoke/rotate affected credentials where applicable, preserve the incident evidence privately, remove the material from active public surfaces where possible, and obtain legal/security advice regarding downstream copies and notification duties.

## 5. Access control

Confidential material should use least-privilege access. Each person should receive only the data and systems needed for their role. Access should be revocable and periodically reviewed. Shared credentials should be avoided where individual accounts are available.

## 6. Agreement requirement

Before giving a person or organization access to material classified as confidential, use an appropriate written agreement. Depending on the relationship, this may include an NDA, employee IP/confidentiality agreement, contractor IP-assignment agreement, research collaboration agreement, evaluation agreement, or commercial license.

An NDA alone does not automatically establish ownership of newly created IP; ownership and assignment/licensing terms should be addressed expressly.

## 7. Publication gate

Before publishing a new technical detail, ask:

1. Is it already public?
2. Could it contain a patentable invention that should be reviewed before disclosure?
3. Is its economic value partly dependent on secrecy?
4. Does it contain third-party confidential material or personal data?
5. Does publication conflict with a contract, license, customer obligation, or security duty?
6. Has the publication been recorded with version/hash/provenance evidence?

If any answer is uncertain, hold publication and obtain appropriate review.

## 8. Retention and offboarding

When a contributor or contractor leaves, revoke access promptly, rotate shared credentials where appropriate, inventory devices/accounts/materials, confirm return or permitted destruction of confidential copies, and preserve the signed agreements and contribution history.

## 9. No change to public license

This policy does not retroactively convert public material into confidential information and does not modify any existing file-specific license. It governs handling of confidential and future materials.
