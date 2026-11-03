# HTEP-001 — Net Change Limit Context Reconstruction v0.1

**Status:** evidence-backed reconnaissance; constitutional-interpretation question remains open.  
**Source snapshot:** Koios `/proposal_list`, retrieved 2026-11-03T20:42:44.166123+00:00; tip epoch 665.  
**Purpose:** Priority 4 of the Budget Process Context Register—establish applicable NCL proposals, effective conventions, cumulative on-chain withdrawals, and the exceptional AlphaGrowth PRIME sequence.

## Main observation

The 2026–27 period was initially assigned an NCL of **₳350,000,000** for epochs **613–713**. A later Info Action submitted in epoch **640** asserted a replacement cap of **₳500,000,000**, for *the same period*, counting earlier period withdrawals and explicitly excluding new treasury inflows from its arithmetic.

At the end of epoch 647, the chain recorded **₳337,395,629** of enacted treasury withdrawals since epoch 613. This leaves **₳12,604,371** under ₳350M. AlphaGrowth's **₳120,000,000** PRIME action was submitted in epoch **642**, ratified in **649**, and enacted in **650**. After that enactment, cumulative withdrawals were **₳457,395,629**—**₳107,395,629 above the initial ₳350M cap** but **₳42,604,371 below ₳500M**.

**The arithmetic is verified; the operative legal/constitutional status of the new NCL must not be inferred solely from an Info Action's ledger lifecycle fields.**

## Historical sequence and epistemic status

| Epoch | Event | Evidentiary characterization |
|---|---|---|
| 547 | 2025 NCL Info Action proposes ₳350M for epochs 532–604 | Proposal metadata (the Koios row subsequently expires in ledger terms, as Info Actions do) |
| 597 | 2025 NCL Extension requests the same ₳350M through epoch 612 | Proposal metadata; no reset of prior withdrawals |
| 605 | Intersect Budget Committee's NCL proposes ₳350M for epochs 613–713 | Proposal metadata; records use of 2025 inflows and anticipated stablecoin allocation |
| 611 | Competing NCL proposal suggests ₳300M for the same period | Proposal metadata; public vote tallies below its stated constitutional threshold |
| 613 | New NCL period begins | Period stated in relevant Info Action documents |
| 640 | New NCL Info Action proposes ₳500M, superseding ₳350M for the same period | Proposal metadata; declares tally >50% sufficient; no on-chain enforcement |
| 642 | PRIME TWD ₳120M submitted | Koios on-chain governance-action record |
| 647 | ₳500M NCL Info Action expires in Koios | **Not** evidence that the DRep agreement necessarily failed; Info Actions have no enactment transition |
| 649 | PRIME TWD ratified | Koios on-chain record |
| 650 | PRIME TWD enacted, pushing period total to ₳457.396M | Koios on-chain record |

## The 500M Info Action: essential ambiguity

- **Governance action:** `gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq`.
- **On-chain fields:** proposed epoch 640; no ratified/enacted epochs; expired epoch 647, dropped epoch 648.
- **Textual claim:** a new ₳500M NCL supersedes the old ₳350M for epochs 613–713; only enacted ledger withdrawals count; treasury inflows do not increase headroom.
- **Public governance explorer display:** DRep Yes ~62.3%, CC Yes ~83.3%; the explorer shows a generic 100% threshold for Info Actions and status 'Closed'. Those interface status labels are not direct statements about whether the constitutional special rule (>50% DRep support) was met at the relevant cutoff.
- **Remaining verification:** retrieve vote snapshot at the decisive cutoff and *individual CC rationales on PRIME*, particularly their reading of the ₳500M Info Action; determine whether any member explicitly found the prior cap controlling or held the amendment invalid. Do not translate the CC's aggregate constitutional votes into a single adjudicated judgment about NCL validity.

## Distinguish five different dimensions

1. **Normative text:** TREASURY-01a and TREASURY-02a in the enacted constitution require agreed NCL and compliance. Source: https://cardano.org/constitution/
2. **Governance signaling:** Info Actions contain the proposed cap and DRep votes but do not themselves enact ledger parameter updates.
3. **Constitutional interpretation:** CC votes on TWD constitutionality, considering the relevant cap and period; member rationales are needed to reconstruct the reasons.
4. **Ledger operation:** TWD can ratify/enact only under ledger-valid mechanisms, but the NCL itself was not directly ledger-enforced in 2026 (CIP-173 remains proposed).
5. **Observed treasury change:** sum enacted withdrawals in the relevant NCL period—not submitted requests, off-chain budget reservations, or downstream payouts.

## Reproducible aggregate, not a causal theory

The companion `ncl-2026-withdrawal-ledger.csv` enumerates all **30** TWD actions enacted during epochs 613–713 as of the snapshot, sorted by enactment epoch and stable action identifiers. The historical numerator includes all relevant mechanism types (Intersect Hydra, IOG coordinated, independent, etc.), with no artificial attribution to one budget process. Since the 2026 epoch records begin at 613, no retroactive reclassification of requests is needed.

The observed excess under the old cap is a *counterfactual arithmetic comparison*, not a finding that the PRIME TWD was unconstitutional. The public explorer reports strong CC approval of PRIME, not a CC rejection. Further constitutional analysis would require the individual contemporaneous rationales, including any dissent.

## Open questions with explicit closure threshold

| Question | Minimum evidence to resolve | Present state |
|---|---|---|
| Was ₳500M DRep agreement constitutionally achieved at the decisive point? | Timestamped final DRep stake tally and correct TREASURY-01a denominator | Explorer shows 62.3% Yes; independently reconstructable tally pending |
| How did CC members apply the NCL to PRIME? | Member-by-member votes and rationale anchors; credible same-period context | Aggregate CC support observed, individual rationale examination pending |
| Was there an affirmative CC ruling **against** PRIME because of NCL? | A recorded No vote with explicit rationale or formal published finding | Not established; on-chain outcome is **enacted** |
| Was the revision specifically *for* PRIME? | Contemporaneous proposer statements and documents establishing the connection | Temporal alignment + amount necessity observed; motive not established |
| How did contemporaneous actors calculate headroom? | Dated NCL dashboards, budget forecasts, DRep/CC rationales | Ledger-based historical baseline now available |
| Does a 2025 budget approval reserve 2026 NCL capacity? | Governing source/rationales on binding commitments versus enactments | 2026 limit rationale considered prior approved stablecoin budget, but 500M action explicitly counts only enacted withdrawals |

## Source links

- Koios raw snapshot: local `koios-proposal-list-raw.json` (exact source retained in Corpus).
- 2026 ₳350M Info Action: https://app.cgov.io/governance/gov_action1m3xx08yv788vfxqh6nfvrjtvmqpwezsy0ggaczctkyjmttc2wmxsq4jsr7q
- Competing ₳300M proposal: https://app.cgov.io/governance/gov_action1wwjwkg2g0qwr0mehey9r8gwn6qz3r28wl6wdl2s75kfmpy8j87tqqtft9tp
- 2026 ₳500M Info Action: https://app.cgov.io/governance/gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq
- PRIME: https://app.cgov.io/governance/gov_action122wue2k65qq8gmpz795z2axt8apka6ay6xt3pwg8jxj5yfkujmtsqvlfpu7
- Constitution: https://cardano.org/constitution/
- CIP-173 proposal (ledger NCL enforcement): https://cips.cardano.org/cip/CIP-0173

## Observations about scope and burden

This phase answers the *numeric* and *chronological* priority, and isolates a bounded interpretive question. It does not require reconstructing all DRep voting rationales or all transaction-level treasury inflows. The high-value next step is narrow: inspect the NCL change vote at expiry and individual CC PRIME rationales, then decide whether the constitutional-process anomaly warrants a separate case study.
