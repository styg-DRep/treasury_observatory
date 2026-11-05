# HTEP-001 · S2 — Eternl bounded evidence intake (v0.1)

**Disposition:** Bounded Phase 1 intake complete for action history, explicit relationships, proposal-budget comparison, and public vote tallies; not an expenditure or delivery audit.  
**Source snapshot:** Koios `/proposal_list` retrieved `2026-11-03T20:42:44.166123+00:00`, chain tip `665`. SHA-256 of saved raw file `8836d85e6530613d9042cc1f1d7e11e9e6e5a8e9391cda32be527f5a63e7fcd8`.  
**Additional context:** Public Cardanoscan governance-action records consulted November 4, 2026. The raw Koios snapshot is the reusable source; case CSVs are exploratory derivatives.

## Driver and boundary

**Question:** Can an earlier budget-cohort allocation, a later failed maintenance/sustainability request, and an enacted revised request be represented as a coherent funding history without counting the failed proposal as expenditure, attributing all changes to constitutional review, or treating a change in ADA requested as a change in work cost?

Included: three on-chain TWD actions; direct metadata links; status and amounts; a line-level comparison of the 2026 requests; proposer descriptions of previous financing and CC feedback; independent public vote tallies; possible cross-mechanism leads. Excluded: individual CC rationale retrieval and judgment, auditing prior project delivery, stablecoin conversions, realized labor payments, project income, repayment verification, and full Catalyst history.

## 1. Observed events

| Event | Governance action | Submitted → outcome | ADA requested | On-chain outcome |
|---|---|---|---:|---|
| E1 · 2025 Eternl Maintenance | `gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlpqx4t762` | 570 → enacted 576 | ₳583,000 | Withdrawn under 2025 Intersect selected budget cohort; submitted by Intersect and administered through its contractual framework |
| E2 · Path to Sustainability | `gov_action1ngpqafax5rvp8lcgey4asvqtycrh4e56fwp8cn2r9trx2ysryhtsqdm3w3z` | 631 → expired 638 | ₳1,680,000 | No treasury withdrawal |
| E3 · Path to Sustainability v2 | `gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse` | 637 → enacted 645 | ₳2,350,000 | Withdrawn; recipient reward account same as E2 |

**Total 2025 + 2026 enacted treasury withdrawal actions: ₳2,933,000.** Total nominal requested across all three actions: ₳4,613,000. The latter includes the failed E2 request; these are different economic measures. The ₳583,000 initial allocation belongs to a separate budget period and is not a direct USD-price comparator for E3.

### Outcome corroboration (not reasons)

Cardanoscan's expired E2 page reports DRep Yes 58.18% against 67% required, and 3/7 CC members voting constitutional. The E3 page reports DRep Yes 71.29% and 6/7 CC members voting constitutional. Both thresholds were unmet for E2 and met for E3. These *vote outcomes* corroborate a governance change, but **they do not establish which specific arguments caused any member to vote differently**.

- E2: https://cardanoscan.io/govAction/gov_action1ngpqafax5rvp8lcgey4asvqtycrh4e56fwp8cn2r9trx2ysryhtsqdm3w3z
- E3: https://cardanoscan.io/govAction/gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse

## 2. Relationship assertions

**S2-R1, E2 `continuation_of` E1:** supported by E2's FAQ statement about 2025 budget funding of ₳583,000 for Eternl. E2 calls that award approximately $408,000 at a proposal rate of $0.70/ADA, and claims a roughly $133,000 shortfall relative to the intended dollar value at the time of writing. E3's version of this statement reports a $153,000 shortfall. Both are **time-specific proposer claims**, not independently reconstructed cash-flow or exchange transactions. E1's original text identifies a €30,000/month maintenance need, while E2–E3 seek USD $420,000/year and a paid-Pro transition; continuity does not imply identical scopes.

**S2-R2, E3 `resubmission_of` + `revision_of` E2:** strongly supported. E3 names E2's exact action ID in its preamble. Its text characterizes the earlier committee objections as insufficient audit clarity. That attribution is *the proposer's description of CC feedback*; the public vote tally independently shows 4/7 CC non-constitutional votes, not their rationales. The actions overlap temporally: E3 was submitted in epoch 637 while E2 expired at epoch 638. A resubmission need not wait for formal ledger expiry.

The E2→E3 relationship is both a resubmission and a revision. Neither replaces or edits the earlier on-chain record.

## 3. A change in ADA amount is not necessarily a change in underlying work cost

| Parameter | E2 | E3 |
|---|---:|---:|
| Headline annual USD operating cost | $420,000 | $420,000 |
| ADA/USD *proposer planning rate* | $0.25 | ≈$0.1787 |
| Requested withdrawal | ₳1,680,000 | ₳2,350,000 |
| Nominal ADA increase | — | ₳670,000 (+39.88%) |
| Audit budget in ADA | ₳16,800 (1%) | ₳47,000 (2%) |
| Planned duration | 12 months | 12 months |
| Team assumption | 6 FTE among 10 people | 6 FTE among 10 people |
| Stated annual FTE cost | $70,000 | $70,000 |

E3's updated dollar conversion accounts for most of the ADA change; its audit category and proportions also change. **The 39.88% increase in requested ADA is not evidence of 39.88% higher planned USD delivery costs**. This is a particularly good HTEP P4 test because the cost object (USD $420,000 annual operations) remains stated as stable while its ADA representation changes.

The action metadata shows that E3 changed more than audit text. Its preamble summarizes three areas: audit clarity/oversight, exchange rates, and Eternl's own DRep abstention response. A direct comparison also finds altered reported shortfall ($133,000→$153,000), corporate Pro-plan price ($384→$360 per year), and expense-category amounts. We should not describe it simply as “same proposal plus audits.”

### Different administration topologies

E1: Intersect submitted the action on behalf of the vendor; the withdrawal is directed to the Intersect treasury administration script account, followed by separate contractual/milestone administration. E2/E3: both direct withdrawal proposals name Tastenkunst GmbH as administrator and share a destination reward address; E3 explicitly says funding is **not milestone-based**, instead ensuring a 12-month operating period. The private legal arrangements and eventual recipient account cash flows are outside this intake.

### Financial commitments are not observed payment events

E3 proposes conversion of up to $420,000 worth of ADA to stablecoins, return of excess ADA, financial audits in February and August 2027, six-monthly tests for returns funded by Pro subscriptions, and additional conditional donations. These are **forward-looking commitments**, not verified conversions, audit reports, or repayments. In November 2026, the scheduled audits are not yet due.

## 4. Cross-mechanism funding-history leads (not expanded)

E2 and E3 include an explicit previous-funding register listing Catalyst Fund 9 project numbers **900103, 900102, 900203**, Fund 10 numbers **1000157, 1000081, 1000197**, and an Intersect-funded CIP-95 project. These are self-reported history leads; no project-by-project matching or award reconciliation has been done. They demonstrate that a future longitudinal Eternl case could cross funding mechanisms, but this intake must not become a Catalyst survey.

## 5. Evidence and verification status

| Claim/record | Evidence level | Limitation |
|---|---|---|
| Three action IDs, epochs, requested withdrawal amounts, recipients | Koios structured records | Enactment/withdrawal ≠ downstream spending |
| E3→E2 link | Exact prior action ID in E3 metadata | Revision does not prove outcomes |
| E2/E3→2025 maintenance connection | Proposer FAQ reference with 2025 amount; E1 corroborates amount | Scope, realized dollar conversion, delivered outputs not audited |
| E2 CC outcome | Public Cardanoscan votes 3/7 constitutional | Individual CC rationale anchors not collected |
| E3 CC outcome | Public Cardanoscan votes 6/7 constitutional | Does not prove why votes changed |
| E2→E3 cost differences | Side-by-side proposal metadata / derived CSV | Proposer rates, not historical market FX evidence |
| Claimed shortfall and repayment arrangements | Proposer text | Not independently verified |
| Prior Catalyst/Intersect awards | Proposer historical list | External awards not independently reconstructed |

### Missingness and friction

- No independently verified realized USD proceeds from 2025's ₳583,000; no specific payment/expenditure/disbursement total for E1 or E3.
- No actual 2026 $420k stablecoin conversion, Pro revenue, refunds, or scheduled audits verified.
- No individual Constitutional Committee rationale anchors reviewed; rationale attribution remains proposer-reported despite verified voting results.
- Document structure locates cost categories in `meta_json.body.motivation` (not always the `rationale` field); an extractor treating the latter as the only rich text would lose key data.
- No measured human minutes for this intake. Source count and number of targeted checks are documented; precise burden cannot honestly be inferred from the session.

## 6. Provisional HTEP P1–P5 readout

| Hypothesis | S2 signal | Boundary |
|---|---|---|
| P1 reusable evidence | Positive: IDs, metadata, vote outcomes, and explicit lineage support a reproducible history | Payment and delivery remain separate sources |
| P2 minimal normalization | Positive but nuanced: action, relation, source and economic-event type suffice for this case | Same item can have multiple overlapping relation types; price basis needs provenance |
| P3 longitudinal learning | Positive: prior maintenance→follow-up request→revised governance bid is visible | Claims of earlier shortfall and later sustainability are not verified |
| P4 historical cost comparisons | Strong caution: +39.88% ADA requested with unchanged stated USD baseline | Proposed FX and budget allocations ≠ realized cost or exchange rate |
| P5 proportionate effort | Positive signal: the case is interpretable from snapshot plus two public voting records | No timed burden log; CC reasoning and delivery would increase burden materially |

## 7. Checkpoint and stopping decision

**Close S2 bounded intake at v0.1.** The relational hypothesis has been tested with an enacted–expired–enacted sequence, overlapping governance windows, an FX-adjusted request, changed institutional administration, and a proposal-reported response to CC feedback. It is not necessary to discover all rationales or verify every receipt to establish this evidence topology.

**Reopen narrowly if** we need to: (a) test whether constitutional-review rationales really caused a particular amendment; (b) compare realized 2025 vs 2026 costs; or (c) explicitly test cross-Catalyst longitudinal funding identity. Otherwise move to S3 (Fund 8 Universal Resolver for did:prism).

**Core insight:** Treating “funding request” as a single homogeneous object would hide at least four meaningful differences: earlier intermediary-administered funding, an expired request, an enacted repriced revision, and private commercial-income/repayment commitments. The same continuing work appears in those objects without becoming interchangeable with them.
