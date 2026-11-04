# HTEP-001 — Initial Sample Frame and Phase 1 Cohort v0.1

**Prepared:** 2026-11-03  
**Status:** Phase 1 sampling decision; cases nominated for evidence intake, not yet fully normalized.  
**Parent:** Historical Treasury Evidence Probe (HTEP-001).  
**Inputs:** Koios mainnet snapshot dated 2026-11-03; Budget Process Context Register v0.2; TWD Relationship Discovery v0.1; Catalyst C1/C3 landscape and C5 recovery v0.1.

## Sampling driver

Choose a *small, deliberately contrasting* starting cohort that tests whether treasury funding evidence across different institutions and periods can be captured with provenance, linked across time, interpreted for cost and delivery without conflating economic events, and recovered at proportionate effort. This is **purposive methodological sampling**, not a representative estimate of Cardano treasury funding. Cases are funding histories where appropriate; **a case is not necessarily one governance action**.

## Phase 1: four nominated histories

| Case | Funding mechanism / evidence era | Primary question | Selection rationale | First boundary |
|---|---|---|---|---|
| **S1 — Amaru funding continuation** | Conway TWDs, 2025 → 2026 | Can two enacted funding actions be connected into a traceable history without assuming delivery success? | Explicit continuation; distinct periods; project-led / PRAGMA-associated context | 2025 and 2026 actions, their proposal evidence and accessible outcome references |
| **S2 — Eternl funding revision** | Intersect 2025 cohort → non-Hydra 2026 | Can prior maintenance funding and a revised later request be represented without counting a revision as fresh independent demand? | Mix of enacted earlier action, expired 2026 request and enacted v2; governance feedback in later proposal's account | Three action records plus identified revision evidence; CC rationale only if necessary to determine relationship |
| **S3 — Universal Resolver for did:prism** | Catalyst Fund 8, expansion / monthly reporting | Can historical planned labor units be extracted alongside deliverables and monthly reports without mislabeling them as realized costs? | Detailed historical USD budget despite pre-milestone reporting regime | Official proposal record, source links, final/monthly reports as retrievable |
| **S4 — Hydra-Point-of-Sale** | Catalyst Fund 14, mature milestone / compliance era | Does a rich public milestone trail yield reusable evidence despite apparent budget-allocation display inconsistencies? | Later administrative regime; visible milestone approvals and PoA; informative inconsistencies | Project and milestone records, approval timeline and publicly available deliverable references; **not** private KYC records |

### Anchors and prior observations

**S1 — Amaru**
- 2025 action `gov_action1vrkk4dpuss8l3z9g4uc2rmf8ks0f7j534zvz9v4k85dlc54wa3zsqq68rx0`, epoch 566, enacted, ₳1,500,000.
- 2026 action `gov_action19uhuy5uame2s60yrh6n8cyds8ps5q7tkh05dqlzmpcfy429p9w4qq5ll3g0`, epoch 614, enacted, ₳10,142,000.
- Relationship discovery R001: later proposal *states* that this is a second funding request. Treat that as proposal-supported continuity, not independent proof of performance.

**S2 — Eternl**
- 2025 maintenance action `gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlpqx4t762`, epoch 570, enacted, ₳583,000.
- 2026 action `gov_action1ngpqafax5rvp8lcgey4asvqtycrh4e56fwp8cn2r9trx2ysryhtsqdm3w3z`, epoch 631, expired, ₳1,680,000.
- 2026 revision `gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse`, epoch 637, enacted, ₳2,350,000.
- Relationship discovery R002–R003. The later proposal describes governance feedback; do **not** treat that description as verified independent CC reasoning without consulting vote rationales.

**S3 — Catalyst F8**
- Project: *Universal Resolver for did:prism*, official page: https://projectcatalyst.io/funds/8/accelerate-decentralized-identity/universal-resolver-for-didprism ; project ID 800352.
- Prior survey: USD 6,425 requested/distributed displayed; budget includes 40h × USD 100/h + 20h × USD 100/h + USD 400 hosting + USD 25 domain; monthly reports and external deliverables referenced. Planned costs ≠ verified actual costs.

**S4 — Catalyst F14**
- Project: *Hydra-Point-of-Sale: Accept ADA, CNTs in Retail & Invoicing*; https://milestones.projectcatalyst.io/projects/1400065 ; project ID 1400065.
- Prior survey: ₳95,000 budget/reported distributed; completed status; milestones and approvals visible, alongside an apparent SoM allocation of zero. Treat as a record inconsistency to inspect, not evidence of no funding. Public procedural evidence must be distinguished from private compliance or KYC data.

## The bounded intake procedure (applies independently to each case)

1. **Source capture:** List every authoritative source actually accessed, stable ID, retrieval timestamp, artifact type, and link/hash where available. Preserve original content where appropriate in the Corpus; record unavailable or changed links.
2. **Minimal events:** Capture request/proposal, decision, authorized withdrawal or grant award, reported disbursement, milestone/report, and outcome separately **only where observed**; mark missing, not-applicable, and not-yet-checked distinctly.
3. **Relationship assertions:** Record relationship as its own source-backed assertion (which record claims it, what text or ID supports it, whether externally verified). Do not silently create a permanent initiative ID.
4. **Costs:** Separate requested amounts, award/withdrawal amounts, planned line items, reported distributions, actual expenditures and returned amounts. Preserve currency/units and pricing time; do not compute historical price judgments.
5. **Burden:** Briefly log discovery, source retrieval, extraction, reconciliation, interpretive ambiguity, and what could be automated. Approximate elapsed minutes are useful but not a target.
6. **Case memo:** One page on what is observed, what can be compared, what remains ambiguous, and whether its inclusion changed our sense of P1–P5.

## First checkpoint (after four histories, not after thirty records)

Evaluate:
- **P1:** Can another person reconstruct the case's key assertions from durable references?
- **P2:** Which minimal fields recur across TWD and Catalyst, and which are mechanism-specific?
- **P3:** Did the linked actions or reports make the history more informative than isolated records?
- **P4:** Which cost observations actually have sufficiently similar scopes, units and economic meaning to form a candidate reference class? No forced comparison.
- **P5:** What recovery burdens and missingness recur? Would another case of the same type add much learning?

A checkpoint may lead to **continue**, **refine**, **redirect**, or **stop**. Phase 1 does not establish a final schema, require all referenced reports to be retrieved, or make an unbounded compliance-process investigation obligatory.

## Forecast for the rest of the approximately 30-case probe — directional, not quotas

The full sample is likely to need **contrasts along several axes**, not a fixed split between governance mechanisms:

- **Instrument/authority:** direct Conway TWD; Catalyst downstream grant; intermediary allocation (e.g., Draper Dragon or PRIME) when evidence of downstream grants becomes accessible.
- **Governance pathway:** Intersect 2025 Ekklesia; 2026 Hydra; separately coordinated institutional batches; project-led submissions; ambiguous pathways.
- **Temporal relation:** new request; revision/resubmission; continuation/renewal; cross-fund or cross-mechanism trajectory.
- **Delivery-evidence maturity:** early Catalyst/monthly reports; mature Catalyst milestones/PoA; recent TWD with little elapsed delivery time.
- **Cost semantics and structure:** proposed labor units; milestone budgets; administration fees; pooled or program allocation; ADA and USD budgets; completed vs incomplete evidence.
- **Institutional context:** NCL regime and amendments, role overlap among sponsor/submitter/administrator/deliverer, policy/compliance shifts.

**Candidate Phase 2 branches, activated by learning:** Fund 11 Cardanoscan API Javascript SDK (project 1100083) to separate milestone *maturity* from late compliance; an actual Fund 2–4 project to test oldest recoverability; Pallas or another 2025→2026 infrastructure continuation; Summit/TOKEN2049 for splitting; one delegated-allocator TWD to test treasury-to-intermediary-to-project mapping. None is compulsory at this stage.

## Inclusion / exclusion and stopping discipline

- Select because a case offers a distinct test of uncertainty, **not** because it is easy, prestigious, controversial, or large.
- Record exclusions and substitutions with a short reason, so selection logic remains inspectable.
- Do not classify an expired TWD as a funded project; an expired predecessor may be evidence *within* a history anchored by an enacted action.
- Do not infer project delivery from funding approval or milestone status; do not infer expenditure from a distribution field.
- Prefer a new case only when it challenges an assumption not already examined or when an observed gap materially affects HTEP hypotheses.
- Retain an explicit right to close well below thirty if further cases have low expected learning relative to burden; likewise the target of ~30 is a planning boundary, not an obligation.

## Repository disposition

- **Observatory:** this sample frame, case-selection decisions, case memos, hypothesis checkpoint, and unresolved interpretation.
- **Evidence Corpus:** the already deposited raw Koios snapshot, faithful Catalyst source captures if obtainable, minimal independently reusable event or relationship records with provenance. Do not insert investigator confidence or normative conclusions into raw source data.
- **No amendment to the active HTEP agreement is proposed.** This operational cohort is a reversible conduct decision within its existing scope.
