# HTEP-001 · S1 — Amaru bounded evidence intake (v0.1)

**Status:** Phase 1 first case; bounded intake complete for source/relationship/budget structure; transactions, delivered work and expenditure not independently audited.  
**As-of:** Koios snapshot retrieved `2026-11-03T20:42:44Z`, tip epoch 665; public materials consulted November 4, 2026.  
**Primary input:** `sources/cardano-governance/koios/2026-11-03/koios-proposal-list-raw.json` in Evidence Corpus, SHA-256 `8836d85e6530613d9042cc1f1d7e11e9e6e5a8e9391cda32be527f5a63e7fcd8`. The present CSVs are extracted case working records, not new canonical funding facts.

## Driver and intake boundary

**Question:** Can two enacted TWDs for a continuing project be connected into a usable historical funding trajectory, while preserving the difference between authorization, withdrawal, managed funds, reported refunds, actual expenditure and delivery? This tests HTEP P1/P2/P3/P4/P5 without requiring a full project audit.

**Included:** 2025 budget Info Action as a documentary antecedent; the two TWDs; original proposal metadata/links; per-scope amounts; 2026's claims and transaction pointers to 2025 returns; administration mechanism; source availability and costs caveats. **Excluded:** exhaustive chain transaction tracing, private contracts, verification of every development milestone, independent price benchmarking, causal claims about funding efficacy, DRep rationale collection.

## 1. Observed governance events

| Event | Action and epoch(s) | Economic object | Outcome at snapshot |
|---|---|---|---|
| 2025 budget Info Action | `gov_action1h4ygjv0hjfj3lmafcm76rpdzcm8vsvj9k5wejn3npyxwxm3fesnqqw9kxxz` — submitted 556, expired 563 | Statement of intended budget; **not withdrawal** | Ledger `expired`; proposal text elsewhere describes it as community-approved; distinguish ledger status from off-chain/support interpretation |
| 2025 TWD | `gov_action1vrkk4dpuss8l3z9g4uc2rmf8ks0f7j534zvz9v4k85dlc54wa3zsqq68rx0` — submitted 566, ratified 570, enacted 571 | ₳1,500,000 authorized/withdrawn to five script reward accounts | Enacted |
| 2026 TWD | `gov_action19uhuy5uame2s60yrh6n8cyds8ps5q7tkh05dqlzmpcfy429p9w4qq5ll3g0` — submitted 614, ratified 620, enacted 621 | ₳10,142,000 authorized/withdrawn to five script reward accounts | Enacted |

The two on-chain withdrawal action amounts sum to **₳11,642,000 gross**. This is *not* a statement that ₳11,642,000 was spent. The 2025 and 2026 actions address partly different calendar periods and funding structures. Submission date 2025-06-25 and 2026-02-23 UTC from Koios block_time.

## 2. Relationship assertion: R001

**2026 TWD `continuation_of` 2025 TWD** — **explicit proposer-attested, on-chain-action anchored**. The 2026 abstract calls itself the second TWD and links both the preceding budget Info Action and 2025 withdrawal. Thus the relation and intended project continuity are documented. The relationship does **not** prove fulfillment of the 2025 plan, nor identical work scopes or prices. Its evidence path is `2026 action → meta_json.body.abstract → 2025 action ID`; the latter is independently present in the Koios snapshot. No invented permanent initiative ID needed.

**2025 TWD `follows_budget_statement` 2025 Info Action** — explicit in the 2025 abstract and supporting references. The Info Action's ledger outcome is `expired`, despite the proposer's description of a successful/approved budget. This distinction is preserved as an institutional-record tension rather than silently resolved.

## 3. Funding composition, not interchangeable amounts

**2025 planned funding:** six unfunded FTEs for the second half of 2025, with proposal model of USD $600,000 base + 25% contingency ($150,000), totaling **$750,000** at proposal's $0.50/ADA reference rate, or **₳1.5M**. Five on-chain script account allocations: ₳100,000 marketing/management, ₳500,000 ad-hoc work, ₳300,000 consensus, ₳300,000 ledger, ₳300,000 contingency. Proposal FTE assumptions are historical *proposer estimates* rather than observed market rates.

**2026 planned funding:** **$3,042,500** scope budget, represented as **₳6,085,000** at proposal's $0.50/ADA planning rate, plus **₳4,057,000** *conditional volatility contingency* for an aggregate **₳10,142,000** TWD. The proposal discusses a $225,000 annual billable FTE assumption (approx. $108/hour) and an ADA downside scenario near $0.30. These are the **proposer's planning assumptions**, not independent currency observations or verified costs. The contingency is subject to additional authorization and not described as a budget for unplanned activities. Do not compare gross 2025 and 2026 withdrawals as like-for-like costs or annual growth without separating scopes, durations, co-funding, and contingency.

**2025 reported returned funds:** the 2026 proposal states that five 2025 scope accounts sent back ₳11,900 (consensus), ₳168,750 (ledger), ₳39,750 (marketing), ₳400,000 (ad-hoc/mercenaries), and ₳300,000 (contingency). **Reported total ₳920,400**, or 61.36% of the original 2025 withdrawal; **₳579,600** is the arithmetic remainder, **not independently verified 2025 actual spending**. The same proposal notes late invoices and some remaining account balances at proposal-writing time; reported returns and the remainder must not be interpreted as a closed comprehensive expense reconciliation. Five transaction hashes are preserved in `amaru-reported-returns.csv`. Chain transaction contents/destinations are not independently verified in this intake.

## 4. Institutional and evidence roles

2025 and 2026 proposal materials identify Amaru as a PRAGMA-supported multi-entity open-source node initiative. The **Amaru maintainer committee** describes itself as the direct budget administrator, with scope owners controlling dedicated script treasuries and an off-chain contributor-contract process. PRAGMA supplies institutional governance/framework support; **do not equate PRAGMA's role with direct custody of all withdrawals**. The public [Amaru treasury repository](https://github.com/pragma-org/amaru-treasury) describes `sweep`, `disburse`, `reorganize`, and permission controls, as well as a transaction journal. Its existence and documented mechanism were checked, not the entirety of its transaction accounting. [PRAGMA's project page](https://pragma.builders/projects/amaru/) explicitly says PRAGMA is not the project treasury fund custodian.

## 5. Source register (access/claim boundary)

| ID | Source | Used for | Verification boundary |
|---|---|---|---|
| K0 | Saved Koios `/proposal_list` snapshot | IDs, submission/lifecycle epochs, metadata anchors, withdrawal entries | Reproducible source capture; Koios is an indexed view of the chain |
| K1 | K0 `2025 budget Info Action` metadata | Original work/assumptions; budget relationship | Proposer text; ledger `expired` |
| K2 | K0 `2025 TWD` metadata and withdrawal entries | Five addresses, budget allocations, enacted action | Withdrawal ≠ downstream disbursement |
| K3 | K0 `2026 TWD` metadata and withdrawal entries | Continuation, new budget assumptions, refund statements and refs | Claimed returns are not independently validated |
| W1 | https://github.com/pragma-org/amaru-treasury | Public administration design, journal presence | Software documentation ≠ audit of use |
| W2 | https://amaru.global/treasury/ | 2025 scopes and scope-owner administration | Project-authored description |
| W3 | https://pragma.builders/projects/amaru/ | PRAGMA's support vs custodian distinction | Institutional self-description |
| W4 | https://github.com/pragma-org/amaru/discussions/91 | 2025 maintainer committee discussion / budget context | Meeting record, not independent completion proof |
| U1 | `ipfs://bafkreihjsdpolefycwjt75nnslqdbweu5pcyffzv6pjuknpc7bldmp2ch4` | 2025 retrospective annex | Referenced, **not fetched and evaluated** |
| U2 | `ipfs://bafybeidrfx7yxy54xg7crp2n4s2uxflmxaafebf5py4xi2ze75nya3sp5a` | 2026 detailed scope/budget annex | Referenced, **not fetched and evaluated** |
| U3 | Five explorer transaction links in K3 | Reported returns | Identifiers captured; **not transaction-verified** |

## 6. Missingness and evidence friction

- **Observed:** 2025 and 2026 proposal metadata; two enacted gross withdrawals; exact withdrawal entries; explicit continuation links; detailed proposer cost assumptions; five referenced 2025 refund transactions; identifiable administrative mechanism.
- **Claimed but not checked:** refund destinations and amounts on ledger; audit results; 2025 retrospective delivery comparison; actual contributor remuneration; 2026 scope deliveries; contractual obligations; remaining funds; any late 2025 invoices; comparable market labor rates.
- **Not established:** full period expenditure; realized cost per deliverable; whether 2025 output met independently verified acceptance tests; all non-treasury co-funding; net public-benefit assessment.
- **Process friction:** IPFS annexes, journal and chain activity each require different retrieval and verification methods; varying 2025/2026 work scope and reserve treatment can induce misleading comparisons. The Koios source contains large text bodies but preserves actionable references.
- **Burden evidence:** one bounded local source scan plus a small public corroboration search; exact retrieval minutes not instrumented, so **time burden is unmeasured**, not estimated. Further work would require transaction-level verification and separate outcomes source review.

## 7. HTEP local hypothesis readout (provisional)

| Hypothesis | Signal from S1 | Limit |
|---|---|---|
| P1 — reusable evidence | **Positive:** stable IDs and explicit metadata references support a reproducible multi-action history | No downstream spend accounting validated |
| P2 — minimal normalization | **Positive:** only action, event, relation, claim-status and source are needed for this initial representation | Scope/cost transformations need separate decisions |
| P3 — longitudinal learning | **Positive:** later proposal directly references earlier funding and retrospective; partial refund trail promises richer continuity | Retrospective and technical outcomes not independently evaluated |
| P4 — historical cost comparison | **Qualified:** year-specific FTE, exchange-rate and contingencies are disclosed; must distinguish planned, withdrawn, returned, spent | No realized cost-per-output established |
| P5 — proportional effort | **Promising:** material insights from one saved snapshot and small number of checks | Time burden not recorded; transaction tracing would increase cost |

## 8. Checkpoint: where to stop and why

**Stop S1 intake at v0.1.** We have established the continuity link, distinct economic events, a multi-scope administration topology, conditional volatility buffer, and potentially reusable refund pointers. Do **not** extend into full chain forensic accounting merely because the transaction hashes are available.

**Reopen narrowly only if** (a) a reference-class comparison depends on net 2025 realized spending; (b) HTEP needs to verify refund evidence as part of a cross-case standard; or (c) independent delivery corroboration becomes essential to an explicit hypothesis test. In that case, first examine the five referenced transactions and published retrospective/audit, not every project transaction.

**Next case:** S2 Eternl, focusing on revision/expiry/CC feedback relationships. At the four-case Phase 1 checkpoint, revisit whether the relation and economic-event distinctions improved comparison enough to justify expansion.
