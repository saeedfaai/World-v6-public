# World 8 / Z0-A — Bitcoin Payment Policy v1.0

## Purpose

Bitcoin is an optional payment rail for controlled World 8 paid access. It is not the only future payment method and does not alter the public licensing status of already published World 8 materials.

## Launch configuration

- Network: Bitcoin mainnet only.
- Asset: BTC only.
- Receiving address: `bc1qe4nydvpu79cu4ngtryp7yghksveqcya9drg0zc`.
- Prices: defined in USD; converted to an exact satoshi amount when an invoice is created.
- Invoice validity: 30 minutes.
- Automated checkout: Technical Access and Professional Access only.
- High-value/team/enterprise/pilot/commercial arrangements: manual review and, where applicable, signed agreement.

## Reconciliation controls

Each automated invoice receives a unique invoice ID and a small unique satoshi nonce so concurrent payments can be distinguished even while v1 uses one receiving address. The buyer must also submit the transaction hash. A transaction hash cannot satisfy more than one invoice.

## Confirmation policy

- Technical Access: at least 1 Bitcoin confirmation.
- Professional Access: at least 1 Bitcoin confirmation.
- Any manually approved higher-value BTC transaction: default 2 confirmations or a stricter threshold set in the agreement.

No access is granted merely because a user reports that payment was sent.

## Validation requirements

The verifier must validate all of the following before activation:

1. transaction exists on Bitcoin mainnet;
2. transaction contains an output to the configured receiving address;
3. value paid to that address is at least the invoice's required satoshi amount;
4. invoice has not expired unless manually approved;
5. required confirmation threshold has been met;
6. transaction hash has not already been consumed by another invoice;
7. terms acceptance exists for the exact invoice and terms version;
8. plan is eligible for automated activation.

## Security boundary

The application must never request, store, transmit, log, or expose a Bitcoin private key, wallet seed phrase, recovery phrase, or signing key. The payment service is watch-only. The public receiving address may be stored in public configuration.

## Storage and delivery

Paid materials must not be committed to the public repository. They are stored in private object storage. Access is delivered only through authenticated, short-lived signed URLs after entitlement checks.

## Professional upgrade path

The single-address v1 design is acceptable for low-volume launch but is not the preferred long-term architecture. Before material payment volume, migrate to unique per-invoice receive addresses derived from a watch-only xpub or use a compliant payment processor that provides equivalent invoice isolation. Private keys remain offline/outside the application.

## Legal/compliance boundary

Bitcoin payment does not waive applicable tax, sanctions, export-control, consumer, anti-fraud, accounting, identity-verification, or other legal requirements. High-value and commercial transactions remain subject to manual review.
