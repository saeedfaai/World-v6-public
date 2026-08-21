# World v6.2 RC3 — Public Release Gates

Target release: `v6.2.0-rc.3`  
Target title: **World v6.2 Fractal Multi-Brain Architecture — RC3**  
Private development repository: `saeedfaai/world-v6`  
Preparation branch: `release/v6.2.0-rc.3-publication-prep`

## Publication model

The approved publication model is **PUBLIC / SOURCE-AVAILABLE / NON-COMMERCIAL**. It is not represented as OSI Open Source.

- Original software materials: PolyForm Noncommercial License 1.0.0.
- Original documentation and architecture materials: CC BY-NC-SA 4.0.
- Commercial use requires a separate written commercial license from Saeed Farokhi.
- Public release must be created from a **clean snapshot with no legacy Git history**. The historical development repository is not approved for conversion to Public.

## G0 — Identity and status

- [x] Version fixed as `6.2.0-rc.3`.
- [x] Author/release owner recorded as Saeed Farokhi.
- [x] Status remains Ratification Candidate / Non-Canonical / Not Deployed.
- [x] Secretary-001 remains GESTATING / PRE-BIRTH / NOT DEPLOYED.
- [x] Evidence claims remain bounded to repository evidence.

**Status: PASS**

## G1 — Rights, licensing, citation, and public-disclosure decision

- [x] Non-commercial source-available license map adopted.
- [x] Commercial use explicitly requires a separate written license.
- [x] NOTICE, AUTHORS, CITATION.cff and Zenodo metadata prepared.
- [x] Release owner explicitly authorized public non-commercial publication on 2026-08-21.
- [x] Publication authorization is recorded as a release decision only; it is not a legal opinion or representation that public disclosure preserves patentability in any jurisdiction.

**Status: PASS FOR PUBLICATION**

## G2 — Secrets, privacy, and operational data

For the clean publication snapshot:

- [x] Repository verification scans common OpenAI, GitHub, Google and Telegram credential forms.
- [x] Publication binary scan checks credential patterns, email addresses, Office review payloads and document metadata.
- [x] Path-hygiene scan fails closed on quote/backslash/control-character publication paths so malformed names cannot bypass binary discovery.
- [x] Current publication payload review found no real customer, contract, bank/card/IBAN, national-ID, pricing or private operational records intended for exclusion. Dummy test data remains test-only.
- [x] Legacy repository history is outside the public snapshot and therefore is not exposed by this publication route.

**Status: PASS FOR CLEAN SNAPSHOT**

## G3 — Third-party and uncertain-origin material

The following private-development/reference assets are excluded from the clean publication payload:

- [x] `research/SHARD_ssrn-6898739.pdf`
- [x] `legacy-reference/V_06_v6.1.1_CANONICAL_ALIGNED.zip`
- [x] both secretary `proforma_reference.pdf` assets
- [x] both secretary `letterhead_template.pptx` assets
- [x] letter rendering now creates a project-owned temporary template from source at runtime; excluded template bytes are not reused
- [x] 14 malformed quote/backslash-literal filename artifacts discovered during release QA were removed
- [x] remaining real publication binaries are subject to the CI binary/privacy scan
- [x] legacy Git history containing excluded material will not be published; the release route is a clean no-history snapshot

**Status: PASS FOR CLEAN SNAPSHOT**

## G4 — Reproducibility and exact payload

The release workflow is fail-closed and must succeed on the exact publication commit. It performs:

- [x] binary/privacy/path-hygiene scan
- [x] deterministic release ZIP build
- [x] generated `FILE_INVENTORY.txt` and `SHA256SUMS.txt`
- [x] exact publication artifact upload
- [x] repository contract/hash/JSON/claim-boundary verification
- [x] Python compilation
- [x] Mother Core test suite
- [x] Secretary-001 test suite
- [x] preserved ancestor regression suite
- [x] offline provider portability demos

`FILE_INVENTORY.txt` and `SHA256SUMS.txt` are generated release artifacts rather than tracked source files. They are generated for the exact snapshot and included in the release ZIP/artifact, preventing stale checksum indexes after source changes.

**Status: FINAL CI REQUIRED ON EXACT PUBLICATION COMMIT**

A successful final workflow run on the exact approved commit closes G4 without requiring another source commit. The run ID, commit SHA and artifact hashes are recorded in the GitHub publication issue/release record.

## G5 — English publication surface

- [x] English root README.
- [x] Persian README retained.
- [x] Complete English architecture specification included.
- [x] English RC3 release notes included.
- [x] English architecture PDF generated and visually QA'd; build hash record retained.
- [x] Publication language states non-commercial licensing and evidence boundaries.

**Status: PASS**

## G6 — Public GitHub publication

After G4 has a successful final run:

- [ ] Create a new clean public repository/snapshot with no legacy development history.
- [ ] Import only the exact approved publication payload.
- [ ] Tag `v6.2.0-rc.3` on the exact imported snapshot.
- [ ] Create a GitHub **Pre-release** titled `World v6.2 Fractal Multi-Brain Architecture — RC3`.
- [ ] Attach the deterministic source ZIP, generated hashes/inventory, manifest, SBOM and cleared architecture PDFs.
- [ ] State prominently: `NON-COMMERCIAL`, `NOT CANONICAL`, `NOT DEPLOYED`, `E2`.
- [ ] Keep `saeedfaai/world-v6` private unless its full legacy history is separately cleared and intentionally published.

**Status: READY AFTER FINAL G4 CI; PUBLIC-REPOSITORY CREATION STILL REQUIRED**

## G7 — DOI archival

- [ ] Enable/confirm Zenodo integration for the clean public repository.
- [ ] Archive the public pre-release.
- [ ] Record the version DOI.
- [ ] Add the DOI to citation metadata and future release records.

**Status: PENDING PUBLIC RELEASE**

## Controlling decision

**DO NOT CHANGE THE EXISTING HISTORICAL `saeedfaai/world-v6` REPOSITORY TO PUBLIC.**

The authorized release route is a **clean public snapshot with no old Git history**, under the non-commercial license map above. Once the exact-commit CI is green, the payload is technically ready for creation of that clean public repository and pre-release.
