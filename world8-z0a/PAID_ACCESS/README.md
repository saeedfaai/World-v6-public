# World 8 / Z0-A — Paid Access System v1

**Status:** launch configuration / controlled access infrastructure  
**Architecture status:** FINAL DESIGN BASELINE / NOT PRODUCTION  
**Public publication DOI:** https://doi.org/10.5281/zenodo.22085394

This directory defines the public, non-secret policy and configuration layer for monetizing controlled access to non-public World 8 technical/evaluation materials.

## What is public here

- price book;
- access terms;
- Bitcoin payment policy;
- public receiving address;
- checkout boundary and security rules.

## What must never be public here

- private/paid technical content;
- wallet private keys or seed phrases;
- xpub unless intentionally approved for watch-only use;
- customer records;
- invoice/payment data;
- signed download URLs;
- trade secrets;
- commercial contract drafts containing private deal terms.

## Launch model

`Public architecture → account → plan → terms acceptance → invoice → BTC payment → on-chain verification → entitlement → private vault`

Automated Bitcoin checkout is deliberately limited to the USD 390 Technical Access and USD 990 Professional Access plans. Higher-value access and all commercial rights remain manual/contract-controlled.

## Backend

The World 8 Supabase project contains a dedicated `access` schema with plans, versioned terms, invoices, payments, entitlements, acceptance records, and audit events. Paid files use a non-public storage bucket named `world8-paid-vault`.

## Security principle

The application is watch-only. It never needs the wallet private key or recovery phrase. The launch address is a Bitcoin mainnet native-SegWit address. Before meaningful checkout volume, upgrade to unique per-invoice receive addresses using a watch-only xpub or an equivalent professional processor.

See `PRICING.md`, `TERMS_OF_ACCESS.md`, `PAYMENT_POLICY.md`, and `payment-config.json`.
