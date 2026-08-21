# Third-Party Notices and Publication Controls

This file distinguishes original World v6 publication material from assets whose redistribution rights require separate verification.

## Publication rule

A file is **not cleared for public redistribution** merely because it was present in the private development repository. Before public release, every third-party or uncertain-origin binary/reference must have one of the following recorded:

1. an applicable license permitting redistribution;
2. explicit written permission from the rights holder;
3. a documented public-domain status; or
4. exclusion from the public repository/release payload, with only a citation or external reference retained where lawful.

## Known private-development references excluded from the public RC3 payload

The following files are excluded from the current publication payload and must not be restored from legacy Git history into the public release unless redistribution rights are separately established:

- `research/SHARD_ssrn-6898739.pdf`
- `legacy-reference/V_06_v6.1.1_CANONICAL_ALIGNED.zip`
- `candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/assets/proforma_reference.pdf`
- `source-ancestor/secretary-v0.1.3/assets/proforma_reference.pdf`
- `candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/assets/letterhead_template.pptx`
- `source-ancestor/secretary-v0.1.3/assets/letterhead_template.pptx`

No binary letterhead template is shipped in the public RC3 payload. Candidate and preserved-ancestor letter rendering now create a project-owned publication-safe template from source code into a temporary PPTX at runtime. No legacy template bytes are reused.

Source paths:

- `candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/src/letters.py`
- `source-ancestor/secretary-v0.1.3/src/letters.py`

## Remaining review

The exclusions above are the minimum known set, not a declaration that every other binary is cleared. Remaining PDF/DOCX/PPTX/ZIP files are subject to the publication binary/privacy scan and must still be attributable to World v6 or separately licensed before release.

Historical copies of excluded files are a separate risk: deleting them from the current tree does not remove them from old Git commits. A public release must therefore use either a clean repository/snapshot with no legacy history or a separately verified history rewrite that makes excluded objects unreachable.

## External standards and names

References to JSON Schema, CloudEvents, PostgreSQL, W3C PROV-O, OpenTelemetry, NIST AI RMF, SLSA, CycloneDX, GitHub, Zenodo, ChatGPT, Gemini, Grok, Claude, Copilot, n8n, MCP, Telegram, Bale, or other standards/products are descriptive references only. Their names, specifications, software, and trademarks remain subject to their respective owners' rights and licenses.

## Release gate

The repository must remain private until `PUBLICATION_GATES.md` records that the third-party/uncertain-origin material and history gates have passed, or the release is published from a clean public repository containing only the approved payload.
