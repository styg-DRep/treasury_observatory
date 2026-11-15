# AP-001 — S1 Amaru evidence manifest

**Status:** Experimental evidence inventory · 2026-11-14  
**Owner of manifest:** Treasury Observatory / AP-001  
**Evidence owner:** [Treasury Evidence Corpus](https://github.com/styg-DRep/treasury_evidence_corpus)  
**Corpus revision:** [`e34d1c9beddddbb6cb8ae3fb8c5135af1525ce89`](https://github.com/styg-DRep/treasury_evidence_corpus/commit/e34d1c9beddddbb6cb8ae3fb8c5135af1525ce89) (main at inspection)  
**Case path:** [`records/htep-001/s1-amaru/`](https://github.com/styg-DRep/treasury_evidence_corpus/tree/e34d1c9beddddbb6cb8ae3fb8c5135af1525ce89/records/htep-001/s1-amaru)

## 1. Purpose and experimental boundary

This manifest identifies the **existing, source-backed Corpus materials** admitted as AP-001's S1 substrate. It is not an analysis of whether Amaru should have received funding, whether costs were appropriate, or whether funds were spent as proposed. No HTEP interpretive memo or new external retrieval is admitted as evidence by default.

The manifest records the **same evidentiary substrate** to be available for each AP-001 representation. Treatments may select, sequence and explain material differently, but must not gain extra facts from outside this pinned substrate. If an exception is necessary, document and review it before reader exposure.

## 2. Pinned primary capture

- Raw capture: `sources/cardano-governance/koios/2026-11-03/koios-proposal-list-raw.json`
- Corpus-reported raw-file SHA-256: `8836d85e6530613d9042cc1f1d7e11e9e6e5a8e9391cda32be527f5a63e7fcd8`
- Retrieval timestamp: `2026-11-03T20:42:44.166123+00:00`
- Source: Koios `proposal_list` snapshot, including indexed proposer-authored `meta_json`; original IPFS documents were **not independently re-fetched or content-hash verified**.
- Stable lookup keys: full governance action IDs (not “Amaru” as a claimed universal project identity).

## 3. Admitted records

| Corpus file | Evidence available | Status / use boundary |
|---|---|---|
| [`README.md`](https://github.com/styg-DRep/treasury_evidence_corpus/blob/e34d1c9beddddbb6cb8ae3fb8c5135af1525ce89/records/htep-001/s1-amaru/README.md) | Case-specific derivation, caveats, reproduction instructions | Descriptive corpus documentation, not an Observatory judgment |
| `actions.csv` | Three action IDs, types, epochs, recorded withdrawal amounts, metadata titles | Indexed governance record; not downstream spending |
| `withdrawals.csv` | Ordered stake recipients and amounts for A1/A2 | Recorded treasury-withdrawal fields, not recipient onward payments |
| `sources.csv` | Per-action source URLs, locator strings, hashes, capture time | Indexed metadata, not revalidated IPFS originals |
| `relationships.csv` | Three manually reviewed, source-backed relationship assertions | Proposer assertions + curator relationship classification, not causal proof |
| `reported-returns.csv` | Five amounts and transaction references claimed in A2 | **Proposer-reported only**, not independently ledger-verified refunds |
| `build_case.py` | Reproduction logic for extracted registers | Relationships require separate manual review |
| `schemas/relations-v0.3.md` | Shared relationship vocabulary and verification conventions | Provisional curator classification, not a ledger-native schema |

All relative file paths are inside `records/htep-001/s1-amaru/` except `schemas/relations-v0.3.md`. Source snapshot is retained in the separate `sources/` tree. The case's action-ID lookup also appears in `records/action-index.csv` at repository level.

## 4. Identified action records

| Key | Action type | Recorded governance lifecycle | Amount recorded in withdrawal field |
|---|---|---|---:|
| A0 | 2025 ecosystem-budget Info Action | Submitted epoch 556; expired 563; dropped 564 | Not applicable (blank, not zero) |
| A1 | 2025 Treasury Withdrawal | Submitted 566; ratified 570; enacted 571 | ₳1,500,000 |
| A2 | 2026 Treasury Withdrawal | Submitted 614; ratified 620; enacted 621 | ₳10,142,000 |

Full IDs (lookup identities):

- A0: `gov_action1h4ygjv0hjfj3lmafcm76rpdzcm8vsvj9k5wejn3npyxwxm3fesnqqw9kxxz`
- A1: `gov_action1vrkk4dpuss8l3z9g4uc2rmf8ks0f7j534zvz9v4k85dlc54wa3zsqq68rx0`
- A2: `gov_action19uhuy5uame2s60yrh6n8cyds8ps5q7tkh05dqlzmpcfy429p9w4qq5ll3g0`

The two withdrawal-field amounts must not be relabeled as verified project expenditure. No inference of net spending is authorized.

## 5. Admitted relationship assertions

| Later action → earlier action | Corpus classification | Evidence boundary |
|---|---|---|
| A2 → A1 | `continuation_of` | A2's proposer explicitly identifies the earlier action; not verified continuity of delivered work or cost |
| A2 → A0 | `references_prior_budget` | A2 references A0; does not prove A0's governance-vote approval |
| A1 → A0 | `follows_budget_statement` | Proposer-linked budget transaction hash matched to A0's `proposal_tx_hash` in snapshot; Info Action expiration does not resolve the separate favorable-vote claim |

These relationship labels are **curator classifications** of source-backed assertions. Their direct locators, assertion types, and matching transformations are preserved in `relationships.csv`.

## 6. Additional distinct economic observations

`reported-returns.csv` contains five A2-proposer-reported amounts: Consensus ₳11,900; Ledger ₳168,750; Marketing ₳39,750; Mercenaries ₳400,000; Contingency ₳300,000. Each includes a referenced transaction hash, but the Corpus **does not establish independent refund validation**. Treat these as reported claims; do not subtract them to infer actual net treasury expenditure.

## 7. Non-established or unavailable propositions

- Independently verified returns and ledger reconciliation of the referenced transfers.
- Expenditure downstream of the recorded treasury withdrawals.
- Independent evidence of technical completion or outcomes.
- Independently checked voting tallies / applicable approval thresholds for A0.
- Separate verification that source metadata matches original IPFS objects.
- A canonical identity or full historical funding graph for the broader Amaru initiative.

Absence here means **not established by this admitted bundle**, not necessarily false or nonexistent.

## 8. Reproduction and treatment integrity

1. Check out the pinned Corpus commit and inspect the source snapshot and case registers.
2. Follow the reproducibility procedure in the case README for machine-generated tables. `relationships.csv` must be reviewed against its source locators; `reported-returns.csv` is a source-derived claim register, not ledger verification.
3. Use the same admitted records for all AP-001 S1 treatments.
4. In every treatment, identify any analyst-derived calculations, simplifications, omissions, or relationship assertions as transformations/interpretations rather than raw observations.
5. Record deliberate exclusions, confusions, or apparent new facts in the AP-001 investigator log instead of silently updating this baseline.

**Baseline status:** Corpus record inventory verified by reading the cited committed registers; raw snapshot's byte-level SHA-256 and the extracted data were **not independently recomputed** during manifest preparation. AP-001 should not claim such verification without running the provided reproduction steps.
