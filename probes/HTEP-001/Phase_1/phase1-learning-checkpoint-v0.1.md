# HTEP-001 — Phase 1 learning checkpoint v0.1

**Date:** 2026-11-04  
**Cases:** S1 Amaru (TWD funding continuation); S2 Eternl (TWD revision); S3 Universal Resolver for did:prism (Catalyst Fund 8); S4 Hydra-Point-of-Sale (Catalyst Fund 14).

**Scope:** This is an interpretive checkpoint drawn from four bounded case memos and their public anchors. No full audit, cross-system database, or representative sample claim. Treat earlier case-specific findings as provisional where independent verification was not performed.

## Comparison matrix

| Case | Historical unit | Strongest recoverable relation | Amount object | Primary evidence | Critical unresolved distinction |
|---|---|---|---|---|---|
| S1 Amaru | Two enacted TWDs | Continuation and proposer-reported prior returns | Enacted withdrawals, planned allocations, contingency, reported returns | Governance metadata, public proposal | Return claims vs independently reconciled on-chain returns; reserves vs expenditure |
| S2 Eternl | Three TWD actions; one expired | Revision after unsuccessful proposal; earlier maintenance funding | Requested ADA, enacted ADA, USD operating estimate, conversion rate | On-chain action status, proposal revisions, voting/CC results | Exchange-rate change vs underlying costs; proposer account vs individual constitutional rationales |
| S3 Fund 8 Universal Resolver | Grant and 2022 reporting sequence | Monthly progress over time; expressly disclaims continuation | USD proposed budget, labor hours, administered grant distribution | Catalyst project record, three dated reports | Plan vs actual hours/expenses; reported completion vs verified technical delivery |
| S4 Fund 14 Hydra-PoS | Grant with four milestones | Milestone evidence and approval event sequence | ADA grant, allocated milestone budgets, staged schedules, reported distribution | Catalyst proposal, milestone recap, Fund 14 rules | Administrative sign-off vs demonstrated outcomes; apparent Statement of Milestones UI allocation inconsistency |

## What changed in our understanding

1. **No single flat funding-action unit works for all four histories.** There are actions, revisions, ongoing initiatives, grants, milestones, scheduled payments, refunds and administrative judgments. Keep distinct entities where evidence makes them distinct; do not require a complete ontology.
2. **Every amount needs an economic meaning.** A withdrawal, funding request, planned cost, contingency, returned amount, installment schedule, and reported distribution must remain distinct, even when denominated in ADA.
3. **Relationships are evidence claims.** Explicit links (e.g., revision or continuity) are useful, but they do not certify execution claims. Shared contributors and sector labels do not establish continuation.
4. **Evidence density and verification strength are orthogonal.** S4 produces more structured approvals; S3 has better planned labor-hour granularity. Neither yields audited realized cost. Mature compliance can increase formal traceability without resolving public data comparability.
5. **Administrative status is an observed institutional decision.** Treat 'completed' and 'approved' as status assertions with issuer and timestamp, not as substitutes for independently measured outcome or impact.
6. **Missingness is itself historically patterned.** Earlier monthly reports, inaccessible linked documents, late-stage data-integrity warnings, and missing disbursement reconciliation should be preserved, not filled by inference.

## Hypothesis checkpoint

| HTEP hypothesis | Initial judgment | Limits |
|---|---|---|
| P1: reusable evidence | **Promising in all four**, especially when provenance and claim-status survive | Partial secondary artifacts; public pages mutable |
| P2: minimum viable normalization | **Feasible as a light event/claim vocabulary** | Single homogeneous proposal/cost table loses meaning |
| P3: longitudinal learning | **Clear benefit from funding histories and milestone sequences** | Long-term ecosystem impacts not established |
| P4: useful cost comparisons | **Promising for selected planned-cost components, not verified realized costs** | Different currencies, times, units and economic-event types; no representative cost benchmark |
| P5: proportionate burden | **Intake-level success, measurement gap** | Staff/time/steps were not logged consistently; no robust cost-of-verification estimate |

## Minimal portable representation to test next

Rather than a universal relational schema, test five optional record classes with stable source references and assertion qualifiers:

- **Source**: original link/identifier, publisher, observed date, retrieval state, preservation/reproducibility.
- **Funding event**: authority and mechanism, requested/approved/withdrawn/allocated/distributed/returned, currency, date, evidence status.
- **Relationship assertion**: subject, predicate, object, asserting party, source, verification state.
- **Delivery/assessment event**: planned output, submitted proof, reviewer determination, date, issuer; do not collapse assessment into outcome.
- **Cost observation**: amount, unit, proposed vs realized basis, time/reference currency, attribution, independent verification status.

These are observational distinctions, not required tables. A case may have zero or many of each.

## Next-step decision and stopping rule

**Decision: finish Phase 1 and permit a small Phase 2 designed for contrast, not coverage quotas.** Keep the ~30-history long-run horizon as provisional. Select at most three targeted new histories when a specific discriminating question justifies each:

1. **Early Catalyst F2–F4 recovery boundary** — does any individual proposal have enough surviving primary evidence? Stop if search becomes archive reconstruction; log failure if appropriate.
2. **Cross-mechanism or delegated funding** — choose a case with a reasonably traceable Treasury-to-allocator-to-project chain (e.g. one downstream grant/investment associated with PRIME or Draper), but do not require an entire allocator portfolio.
3. **Repeatable infrastructure maintenance OR revised/split funding** — e.g. Pallas or the 2026 Summit/TOKEN2049 restructure, selected for a precise unresolved distinction, not for balance alone.

**First Phase 2 checkpoint:** after 2–3 contrasting histories, ask whether new cases reveal new evidence types or merely repeat the same limitations. Pause if additional intakes add no consequential learning, or if verification burden is unbounded. Do not set a target completion date or promise 30 cases. Keep a short time/effort log in the next cases to test P5.

## Reopening conditions from Phase 1

- S1: only if independently verifying returns or expenditure becomes necessary to test a precise financial proposition.
- S2: only if individual CC rationales or cross-Catalyst award references become dispositive.
- S3: only if final technical artifacts/actual costs materially affect the comparator.
- S4: only if proof-content, distribution reconciliation, or actual reviewer-compliance effects become decision-critical.

## Institutional legitimacy implication

Treat stopping as an affirmative research decision with stated sufficiency and uncertainty, not as omission or a performance shortfall. The Observatory earns legitimacy by preserving what is knowable, documenting what is not, and declining to transform administrative data into stronger claims than it can bear.
