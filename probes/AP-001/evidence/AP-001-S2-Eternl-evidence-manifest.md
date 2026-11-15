# AP-001 — S2 Eternl evidence manifest

**Status:** Experimental evidence inventory · 2026-11-14  
**Owner of manifest:** Treasury Observatory / AP-001  
**Evidence owner:** [Treasury Evidence Corpus](https://github.com/styg-DRep/treasury_evidence_corpus)  
**Corpus revision:** [`e34d1c9beddddbb6cb8ae3fb8c5135af1525ce89`](https://github.com/styg-DRep/treasury_evidence_corpus/commit/e34d1c9beddddbb6cb8ae3fb8c5135af1525ce89) (main at inspection)  
**Case path:** [`records/htep-001/s2-eternl/`](https://github.com/styg-DRep/treasury_evidence_corpus/tree/e34d1c9beddddbb6cb8ae3fb8c5135af1525ce89/records/htep-001/s2-eternl)

## 1. Purpose and experimental boundary

This manifest identifies the **existing, source-backed Corpus materials** admitted as AP-001's S2 substrate. The aim is to evaluate representations of a funding revision history, not to determine whether Eternl's funding, expenditure, delivery, or value were appropriate. HTEP interpretation is not independently added to the substrate.

All AP-001 representations of S2 must draw from the **same pinned evidence set**, although they may structure and explain it differently. New research requires an explicitly recorded deviation before reader exposure.

## 2. Pinned primary capture

- Raw capture: `sources/cardano-governance/koios/2026-11-03/koios-proposal-list-raw.json`
- Corpus-reported raw-file SHA-256: `8836d85e6530613d9042cc1f1d7e11e9e6e5a8e9391cda32be527f5a63e7fcd8`
- Retrieval timestamp: `2026-11-03T20:42:44.166123+00:00`
- Source: Koios `proposal_list` indexed metadata; independent IPFS re-fetch and hash verification were **not performed**.
- Stable keys: complete governance action IDs. Folder grouping does not establish one canonical Eternl project identity or complete financing history.

## 3. Admitted records

| Corpus file | Evidence available | Status / use boundary |
|---|---|---|
| [`README.md`](https://github.com/styg-DRep/treasury_evidence_corpus/blob/e34d1c9beddddbb6cb8ae3fb8c5135af1525ce89/records/htep-001/s2-eternl/README.md) | Source scope, caveats and reproduction instructions | Corpus documentation, not an Observatory analysis |
| `actions.csv` | Three action identities, epochs, funding requests and lifecycle data | Requested on-chain action fields, not actual project spending |
| `withdrawals.csv` | Recipient stake addresses and requested lovelace amounts | Expired action E2's amount is **requested**, not an executed withdrawal |
| `sources.csv` | Source URLs, metadata hash, row locators and capture timestamp | Koios-indexed source, not reverified original metadata |
| `relationships.csv` | Three manually reviewed source-backed links | Does not verify shared scope, actual delivery, or CC reasoning |
| `budget-claims.csv` | Proposal totals, approximate planning exchange rates, audit allocations | Proposer-attested budgeting, not paid exchange rates or audit costs |
| `action-index.csv` | Stable action-ID lookup | Case directory is not a canonical project graph |
| `build_case.py` | Reproduces deterministic registers | Does not automatically generate manually reviewed relationship/budget claims |
| `schemas/relations-v0.3.md` | Shared vocabulary for relation assertions | Provisional curator categories |

All relative file paths are inside `records/htep-001/s2-eternl/` except the common schema. The raw capture is stored in `sources/`. The repository also includes `records/action-index.csv`.

## 4. Identified action records

| Key | Funding request | Governance lifecycle | Requested amount |
|---|---|---|---:|
| E1 | Intersect-administered 2025 Eternl Maintenance | Submitted epoch 570; ratified 575; enacted 576 | ₳583,000 |
| E2 | Path to Sustainability (2026–2027) | Submitted 631; expired 638; dropped 639 | ₳1,680,000 |
| E3 | Path to Sustainability — v2 | Submitted 637; ratified 644; enacted 645 | ₳2,350,000 |

Full IDs:

- E1: `gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlpqx4t762`
- E2: `gov_action1ngpqafax5rvp8lcgey4asvqtycrh4e56fwp8cn2r9trx2ysryhtsqdm3w3z`
- E3: `gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse`

The E1 and E3 enacted requests total **₳2,933,000 in authorized withdrawals**, as characterized by the case README, *not verified operational spending*. The nominal sum of all three **requests** is ₳4,613,000 and **must not** be described as funded expenditure, because E2 expired.

## 5. Admitted relationship assertions

| Later action → earlier action | Corpus classification | Evidence boundary |
|---|---|---|
| E2 → E1 | `references_prior_funding` | E2 cites E1's earlier grant via a linked transaction matched against E1's proposal transaction hash; no scope equivalence or spend established |
| E3 → E2 | `revision_of` | E3 expressly identifies and revises E2; a different on-chain action, not an in-place edit |
| E3 → E1 | `references_prior_funding` | E3 cites E1 as past funding; does not imply that the 2025 award was a 2026 cost |

These are manual source-backed classifications; consult `relationships.csv` for exact metadata locators and hash matching methods.

## 6. Additional economic observations

`budget-claims.csv` records the following proposer-attested planning assertions:

| Observation | E2 | E3 | Boundary |
|---|---:|---:|---|
| Proposal amount | ₳1,680,000 | ₳2,350,000 | Corresponds to recorded withdrawal request, not expenditure |
| Approximate ADA/USD planning rate | $0.25 / ADA | $0.1787 / ADA | Not realized exchange rates |
| Allocated audit budget | ₳16,800 | ₳47,000 | Budget, not evidence of completed/paid audits |

The distinct exchange assumptions make a simple ADA-only comparison potentially misleading. This is a **reason to preserve the denominators and status labels**, not permission to infer actual USD spending or motives for revision.

## 7. Non-established or unavailable propositions

- Verified execution of downstream payments to the working entity or vendors and actual operational expenses.
- Completion or economic value of the proposed work; verified audit delivery.
- Independent retrieval of CC member rationales; E3's explanation of feedback is the proponent's account.
- Independently verified IPFS originals.
- Verification of other earlier Catalyst or related engagements mentioned in narrative.
- A complete cross-mechanism funding graph for Eternl.

Absence here means **not established by the admitted Corpus bundle**, not that the event did not occur.

## 8. Reproduction and treatment integrity

1. Check out the pinned Corpus revision and inspect case tables/source locators.
2. Use `build_case.py` per case README for deterministic fields; manually reviewed `relationships.csv` and `budget-claims.csv` require source inspection.
3. Preserve the distinctions: request vs enactment vs execution vs expenditure; planning conversion vs paid conversion; an author-described revision vs independently validated rationale.
4. Do not silently conflate E2's expired request with enacted awards or treat E3 as simply an increased payout on E2.
5. Make all analyst-added calculations, exclusions and interpretive claims explicit in each AP-001 treatment.

**Baseline status:** Manifest created from reading the committed Corpus registers; the source snapshot's SHA-256 and derivation scripts have **not been independently rerun or checked** during manifest preparation.
