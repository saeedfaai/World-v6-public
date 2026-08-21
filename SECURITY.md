# Security Policy

## Supported publication state

World v6.2.0-rc.3 is a **Ratification Candidate / Non-Canonical / Not Deployed** research and engineering release candidate. It is not represented as production-ready software.

## Reporting security issues

Do not disclose credentials, private keys, access tokens, private customer data, personal data, or exploitable vulnerabilities in a public issue.

Until a dedicated security contact channel is published, report suspected security problems privately to the repository owner through GitHub's private contact mechanisms available to you. If no private channel is available, report only that a private security issue exists and do not include exploit details or secrets in a public thread.

## Repository rules

- Never commit API keys, tokens, passwords, private keys, session cookies, production connection strings, or secret-bearing fixtures.
- Never commit raw confidential customer, contract, financial, medical, or personal payloads.
- Treat model/provider output as untrusted input.
- External effects require policy evaluation, exact approval when applicable, and the defined outbox/executor boundary.
- Secrets must live outside the repository in an appropriate secret-management system.
- Publication requires a clean secret scan across tracked files and repository history, plus manual review of binary/document metadata.

## Current limitations

The current evidence level is E2. Security/load/chaos testing, live-provider conformance, production isolation, disaster restore, and other E3/E4 gates remain unproven unless a later evidence record explicitly states otherwise.
