# 2026 Intersect Budget Process — Hydra-to-TWD Crosswalk

**Status:** Verified direct-reference crosswalk v0.1 · 2026-11-03  
**Parent:** HTEP-001 / Budget Process Context Register, priority 2  
**Snapshot:** Koios `/proposal_list`, retrieved `2026-11-03T20:42:44.166123+00:00`, tip epoch 665.  
**Working data:** `2026-hydra-to-twd-crosswalk.csv` (11 actions); `twd-process-annotations-2026.csv` (107 actions; classifications not inferred from timing alone).

## Core finding

The 11 Treasury Withdrawal actions submitted on **2026-06-23 (epoch 638)** in a **single transaction** are directly mapped to the 11 proposals that passed Intersect's 2026 Hydra Voting stage. Each action's proposal metadata directly references one **distinct Hydra proposal URL**, the audited-results document, and the audit report. Intersect independently says it submitted eleven individual TWDs on June 23. The audited results list 11 qualifying proposals, with support ranging from 68.45% to 85.67%. These three independent evidence surfaces triangulate the cohort. This is not just a temporal or title match. [K] [S2] [S3]

## Process reconstruction — intended vs observed

1. **Framework:** An on-chain Info Action described the 2026 Intersect-facilitated process; the framework is not itself a funding decision. [S1]
2. **Applications:** 69 proposals sought 331,569,537 ADA according to the Cardano Foundation's published 2026 budget-process review. This number counts *applications*, not TWDs. [S4]
3. **Advisory voting:** Hydra stage ran May 26–June 12. Audit reports 113 DReps participating, 112 valid voters, and 5,070,798,414.70 ADA valid participating voting power (84.39% of 6,008,653,786.69 ADA total DRep power). Eleven met ≥67% support. [S3]
4. **On-chain submission:** Eleven distinct governance actions were packaged in one *submission transaction*, rather than becoming two consolidated governance actions, as outlined in an earlier FAQ/proposal description. Documented plans should not be retroactively treated as implemented. [K] [S1] [S2]
5. **Outcome:** In the November 3 Koios snapshot, **10 enacted** and **1 expired**; statuses are eventual outcomes, not statuses at submission. [K]

## Exact on-chain crosswalk

| # | Proposal (short title) | ADA | Hydra support | Nov 3 status |
|---:|---|---:|---:|---|
| 0 | 3,961,538 — Bringing Real-World Payments to Cardano with Wirex | 3,961,538 | 78.93% | expired |
| 1 | 540,750 — by TxPipe Dolos: Maintaining Cardano's Lightweight D... | 540,750 | 85.28% | enacted |
| 2 | 1,310,960 — Hardware Wallet Maintenance 2026 | 1,310,960 | 71.33% | enacted |
| 3 | 1,193,000 — Intersect Technical Steering Committee Support | 1,193,000 | 68.45% | enacted |
| 4 | 25,400,000 — Intersect: Governance coordination and technical ... | 25,400,000 | 80.91% | enacted |
| 5 | 3,810,423 — Mithril Protocol | 3,810,423 | 81.33% | enacted |
| 6 | 1,162,746 — MLabs Core Tool Maintenance & Enhancement: Plutarc... | 1,162,746 | 72.62% | enacted |
| 7 | 540,750 — Oura by TxPipe: Maintaining Cardano’s Event Pipeline | 540,750 | 73.57% | enacted |
| 8 | 540,750 — Pallas by TxPipe: Maintaining Cardano's Core Rust Li... | 540,750 | 85.67% | enacted |
| 9 | 1,684,050 — Tx3 by TxPipe: Open API Layer for Cardano's dApp P... | 1,684,050 | 75.63% | enacted |
| 10 | 540,750 — UTxO RPC by TxPipe: Maintaining Cardano’s Integratio... | 540,750 | 85.08% | enacted |

**Totals:** 11 submitted actions requested **₳40,685,717**; 10 enacted actions withdrew **₳36,724,179**; one expired (Wirex) requested **₳3,961,538**. These are amounts in the on-chain actions, not proof of downstream project spending. [K]

### Evidence levels and open boundaries

- **Verified:** 11 action IDs ↔ 11 distinct Hydra reference URLs, published audited successful-proposal names/support percentages ↔ 11 corresponding on-chain titles, same June 23 transaction, and cohort count/timing corroborated by Intersect's June 26 update.
- **Not yet independently re-audited:** We read the public final audited-results page, but did not reproduce the Hydra cryptographic vote verification or examine the full signed audit PDF. We transcribed percentages from its published table.
- **Not established:** whether each accepted proposal had revisions between the Hydra lock and on-chain metadata, whether a revised spend amount was inserted, and which NCL headroom rule/capacity applied at each funding commitment.
- **Not inferred:** membership in the process from on-chain *batching alone*. The nine-action **epoch 626** transaction is separate, predates June 23, and does not belong to this 11-action crosswalk. Process identity remains unverified in this pass.
- **Do not conflate:** participation in the 2026 Intersect budget process with later appointment of Intersect as an *administrator* on a separately initiated TWD.

## Comparison with 2025

| Dimension | 2025 | 2026 |
|---|---|---|
| Off-chain entry population | 194 proposals reported in Intersect's retrospective | 69 proposals reported in 2026 budget-process review |
| Intermediate selection | 39 represented by aggregate Budget Info Action | 11 reached Hydra advisory threshold |
| On-chain action count | 39 individual TWDs | 11 individual TWDs |
| Submission transactions | 3 | 1 |
| Funding outcomes, snapshot | 37 enacted / 2 expired | 10 enacted / 1 expired |
| Relationship evidence | Direct Ekklesia proposal references | Direct Hydra proposal references + published per-proposal audited percentages |

This establishes a concrete **process discontinuity**: information-action anchoring, deliberation design, selection platform, minimum participation conditions and final packaging changed. It does *not* establish that process changes caused differences in applicant counts, success rates, vote rationales, or initiative quality.

## Consequences for sampling and the register

**Priority 2 may move to `core crosswalk verified; process-versus-implementation divergence documented`.** Preserve the original operational framework, Hydra audited-results page, 11 on-chain action IDs, and the funding timeline as separate evidence objects. Leave the finer NCL reconstruction for Priority 4. Retain Amaru, Dingo, the epoch-626 batch, and other direct submissions as contrasting pathways, not as failed applications or implicit members of this cohort.

**Suggested next consequential question:** How did the *other* 50 2026 TWD submissions relate to the Intersect process? Establish pathway labels only where supported by documents (e.g., explicit independent budget process, direct submitter references, prior funding relationships). Then reconstruct NCL as a shared constraint across paths, rather than a fictional Intersect-only fund.

## Sources

- **[K]** Koios full raw snapshot, local `koios-proposal-list-raw.json`, timestamp `2026-11-03T20:42:44.166123+00:00`; every action exposes stable action ID, `proposal_tx_hash`, `proposal_index`, epoch, withdrawal, and direct Hydra proposal URL.
- **[S1]** 2026 Intersect Budget Process Framework FAQs: https://committees.docs.intersectmbo.org/intersect-budget-committee/cardano-budget-process/cardano-2026-budget-process-faqs
- **[S2]** Intersect June 26 weekly update: https://www.intersectmbo.org/news/intersect-weekly-update-117-june-26-2026
- **[S3]** 2026 Hydra Final Audited Results: https://docs.intersectmbo.org/intersect-knowledge-base/cardano-facilitation-services/cardano-budget-2026/2026-budget-process-final-audited-results; Intersect June 19 audit update: https://www.intersectmbo.org/news/intersect-weekly-update-116-june-19-2026
- **[S4]** Cardano Foundation June 9 review of 69 proposals: https://cardanofoundation.org/blog/voting-decisions-2026-intersect-budget-process

## Source caveat

The underlying raw Koios snapshot is the faithful observation; this crosswalk and the 107-row annotation file are **derived investigative indexes**. Preserve source URLs, metadata anchors, and retrieval dates. Publish analysis in the Observatory and source/normalization with provenance in the Evidence Corpus. No inference about proposer motives is implied by the classifications.
