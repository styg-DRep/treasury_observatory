# HTEP-001 — Burden Record v0.1

**Status:** Probe check/learn — retrospective record, not a prospective labor study  
**Record date:** 2026-11-04  
**Scope:** Historical Treasury Evidence Probe (HTEP-001), from reconnaissance through six bounded intakes and the first Corpus handoffs  
**Purpose:** Fulfill Section 11 of the activated probe as faithfully as available evidence permits; inform H11 (proportionate burden), H12 (independent commons capacity), and closure review.

## 1. Measurement basis and candor

This record separates **reported measurements**, **observable outputs**, **qualitative process observations**, **interpretations**, and **unmeasured costs**. It does not backfill task times from conversation length, number of files, or commit counts. In particular, an AI-assisted research session is not a measured end-to-end cost of independent future maintenance or replication.

### Reported by the project steward

| Measure | Value | Meaning / limitation |
|---|---:|---|
| Personal time invested | **16 hours** | Reported total of steward's direct effort across investigation, commits, PR work, and local file management. No per-task contemporaneous timesheet. |
| Git commits | **41** | Reported repository activity; **not** a unit of labor or evidence quality. |
| Pull requests | **6** | Reported PR activity; does not by itself establish number of review iterations, review minutes, or merged artifacts. |
| External review | **Occurred** | Independent feedback and corrections demonstrably affected handoffs; reviewer time not measured. |
| AI assistance | **Substantial** | Used for source discovery, analysis, coding, artifact drafting, and review response. Model execution time, compute, subscription/API cost, and independent reproduction time not measured. |

**Counterfactual:** The steward judges that comparable gathering, source validation, and scripting **without AI tooling would likely have taken weeks**. This is a credible experiential estimate to preserve, **not an experimentally measured productivity ratio**. Do not use it to infer hours saved or cost per case.

**Repository state as reported at record date:** Amaru and Eternl Corpus PRs were independently reviewed and merged; the Catalyst evidence contribution was reviewed and merged with an accepted milestone-capture limitation. No assertion is made here that every one of the six sampled histories now has an equally complete Corpus source record; in particular, the Orion/Xverse multi-source handoff should be tracked separately if still outstanding.

## 2. Work performed: activity and burden types

| Stage | Work undertaken | Effort characteristics | Observed return |
|---|---|---|---|
| Governance and TWD reconnaissance | Koios population capture and reproducible extraction; budget-selection and NCL context; TWD relationship discovery | High initial interpretation and verification burden; some batch extraction automatable | Stable 107-action population and better understanding of institutional variation |
| Catalyst landscape | Fund-level inventory, source atlas, four-era recoverability survey | Variable identifiers and source affordances; inconsistent web representations; manual interpretation | Deliberate sampling rather than indiscriminate ingestion |
| Phase 1 (S1–S4) | Amaru, Eternl, Fund 8 Universal Resolver, Fund 14 Hydra-POS | Source retrieval; distinguishing requested, withdrawn, distributed, estimated, reviewed and realized amounts; relationship interpretation | Four contrasting funding histories and first checkpoint |
| Phase 2 (S5–S6) | Fund 2 Liqwid and Orion/Xverse | Historical incompleteness; delegated-investment confidentiality and ambiguous financial boundaries | Early-history boundary and one additional financial topology; sampling stopped before S7 |
| Corpus transfer | Amaru/Eternl reproducible records; Catalyst observation/preservation packages; scripts, indexes, hash checks | Initial structural conventions and repository integration cost; corrections prompted by independent review | Inspectable, versioned evidence rather than only Observatory analysis |
| Independent review and revision | Corrected locators, source transformations, nonapplicable values, vocabulary, portability, and application-shell classification | Human reviewer effort external to steward's 16 hours; review turnaround not logged | Stronger fidelity, reuse and preservation discipline |

These rows are **qualitative attribution**, not allocations of the 16 hours. No per-stage time is known.

## 3. Section 11 evidence matrix

The activated probe requires recording source location, extraction, normalization, recurrent ambiguity, specialist judgment, automation potential, and automation-resistant tasks.

| Section 11 requirement | Evidence we have | Missing / qualification | Provisional burden signal |
|---|---|---|---|
| **Time locating sources** | Total steward time (16 h); source atlases, links and failed retrieval documented | No source-search minutes per case or per platform | Historical discovery can be quick once a canonical index is known; early Catalyst and dynamic systems are harder |
| **Time extracting evidence** | Retrieval scripts, manifests, checksums; Koios deterministic rebuild; Catalyst source captures | No extraction minutes; no controlled cold-start rerun | Repeatable Koios extraction appears amenable to automation; heterogeneous web capture less so |
| **Time normalizing records** | TWD inventory script; Amaru and Eternl action/relationship tables; Catalyst observation tables | No normalization minutes or maintenance effort | Deterministic fields can be shared; interpreted relationships demand source-level attention |
| **Recurrent ambiguity** | Numerous explicit cases listed below | No systematic frequency or severity coding | Persistent, consequential feature—not an exceptional data-cleaning defect |
| **Specialist interpretation** | Constitution and governance lifecycle, proposal budget assumptions, currency conversion, financial structures, evidence status | Amount of subject expertise and learning time unmeasured | High consequence when economic objects are conflated; judgment cannot simply be automated away |
| **Appears automatable** | Fetching stable APIs; checksums; extracting exact identifiers/amounts; CSV reproduction; consistent indexes | Automation robustness across source changes not benchmarked | Favor narrow, auditable transforms over comprehensive inferred ontologies |
| **Resists automation** | Interpreting funding relationships, distinctions among allocation/disbursement/spend, legal or institutional nuances, retrospective missingness, source completeness, materiality of further inquiry | Human review costs not logged | Review and stopping decisions remain substantial stewardship responsibilities |

### Recurrent friction observed

1. **Economic meaning mismatch.** Authorization, requested amount, award, treasury withdrawal, intermediary commitment, disbursement, reported distribution, expenditure, refund, and contingent reserve are not interchangeable.
2. **Relational ambiguity.** Similar organizations, shared contributors, explicit revisions, continuity of work, funding successor, and institutional selection pathway require different evidence.
3. **Governance semantics.** Ledger lifecycle, constitutional or voting acceptance, and proposer characterization can refer to different facts; absence of voting evidence is not evidence of a contrary vote.
4. **Historical source loss or opacity.** Fund 2 closeout and Fund 8 external support were not fully recovered; later investment transactions are not publicly reconciled.
5. **Dynamic web capture.** Three Catalyst project response bodies were substantive; the Fund 14 milestone response was a JavaScript shell, although it had HTTP 200 and a valid hash. Integrity checks do not imply content completeness.
6. **Reproducibility portability.** UTF-8 declaration, required output directory, stable line endings, explicit identifiers and transformations, and cross-platform verification commands mattered in peer review.
7. **Schema and discovery costs.** Case bundles need canonical-identifier indexes; even a tiny relationship vocabulary benefits from a shared definition and version.
8. **Public reuse constraints.** Source-redistribution rights and sensitive or confidential materials require deliberate treatment; not every public page can be assumed freely republishable.

These are observed *types* of burden, not measured incidence or cost distributions.

## 4. What the 16 hours does and does not establish

**Supports:** Under the observed AI-assisted, steward-led workflow, six deliberately contrasting bounded intake cases, substantial reconnaissance, and several reviewable Corpus contributions were generated within a reported 16 hours of the steward's own effort. Checkpoints permitted early stopping below the original approximately 30-case target.

**Does not support:** A reliable per-case production cost; total social cost including reviewers; total technical cost including AI compute and service subscriptions; future operational cost; a quantified AI productivity multiple; or a claim that source preservation and external reuse are now fully solved.

**Do not divide 16 hours by 6 cases or 41 commits and present the quotient as a transferable unit cost.** The effort includes one-time discovery and formation work, repeated revisions, and shared infrastructure; the sample cases and PRs are not independent identical work units.

### Burden is distributed

The steward's human time is only one component. The investigation also drew on:

- independent reviewer attention, correction and legitimacy-building;
- model/tool processing and interaction;
- upstream maintenance of Koios, Catalyst archives, milestone services, governance explorers and Git repositories;
- preservation and software-maintenance obligations that may persist after HTEP closes;
- future users' time to inspect and reinterpret the records.

We should not erase these contributions or call the system costless simply because many are currently externalized or unmetered.

## 5. The stopping rule as an observed burden-control mechanism

**Design:** The original probe proposed ~30 purposive records but allowed a documented early stop when learning was sufficient.

**Observed:** After four cases, a checkpoint authorized only contrasting Phase 2 tests. S5 confirmed earlier recoverability; S6 discovered a qualitatively different delegated-investment seam. A further S7 intake was not activated because incremental learning did not justify it. Source capture limitations were documented rather than necessarily triggering an open-ended audit.

**Interpretation:** The stopping discipline avoided conflating *possible research* with *obligatory research* and protected attention for Corpus handoffs and learning synthesis. This is observable procedural proportionality, though **not a measured cost-benefit ratio**.

**Important correction:** Time not spent is not the only saving. Restraint also reduces the maintenance surface, schema commitments, review queue, and risk of creating unsupported authority from weak data.

## 6. Hypothesis implications

### P5 / H11 — Proportionate burden

**Provisional assessment: qualified encouragement, not quantitative confirmation.** Productive inquiry and bounded closure were achieved within the steward's reported 16 hours, using substantial AI assistance and independent review. We cannot extrapolate this to the cost of a stable, externally maintained Corpus or a fully verified cost-comparison service. Future evidence architecture should require a separate sustainability and operating-cost test before scaling.

### H12 — Capacity rather than dependency

**Early positive institutional signal.** Independent reviewer corrections and the movement of shared relationship definitions, identifiers and provenance into Corpus conventions show potential for others to work without adopting Observatory interpretation. An actual cold-start independent reuse test remains a better signal than author-side reproduction alone.

### P1–P4 interaction

Time spent on epistemic separation is not automatically “overhead.” The very ambiguities that made normalization slower were often the most decision-relevant discoveries (refunds, reserves, currency repricing, hidden financial seams). A burden minimization regime that removes those distinctions would sacrifice the probe's purpose. Proportionality is **useful understanding per unit of collective effort**, not minimum labor or maximum row count.

## 7. Open obligations and future measurement (not new HTEP intake requirements)

For the remaining HTEP closure review:

- State whether the Orion/Xverse Corpus handoff is committed, pending, or deliberately excepted. Do not infer its state from the Catalyst merge.
- Keep the milestone-module raw-capture gap explicitly open for a later issue/PR; do not treat it as a blocker if independent review accepted it as a bounded limitation.
- Confirm that the committed Corpus artifacts and schema declarations, not only author-local bundles, are referenced in the final learning record.

For **any subsequent probe**, a minimal prospective burden log should record: activity/case; start or rounded minutes by *locate / extract / interpret-normalize / verify-review / package-publish*; source failures; manual specialist decision; automatable step; outcome of stopping decision. Reviewer time should be logged by reviewers if feasible and voluntary. A weekly total plus rough category fractions is acceptable; do not impose timesheet bureaucracy beyond the informational value gained.

Consider one later cold-start replication or source-refresh exercise to estimate actual maintenance cost—**only if** a real scaling decision requires it.

## 8. Conclusion and closure-facing statement

The record satisfies Section 11 as an **earnest retrospective qualitative burden assessment with one steward-reported total**, and candidly records the measurement limitations. It does **not** establish a comprehensive cost accounting of HTEP or demonstrate that a permanent Observatory is economically sustainable.

The most defensible learning is:

> A bounded, AI-assisted, independently reviewed evidence inquiry can generate reusable historical observations with surprisingly modest steward time; but the burden is not eliminated. It moves among retrieval, interpretation, review, preservation, upstream infrastructure, and future stewardship. A legitimate stopping rule governs which of those costs the commons has sufficient reason to incur.

**Recommended disposition:** Include this burden record in HTEP's check/learn closure materials, with P5/H11 marked *encouraging but incompletely measured*. Do not prolong the probe solely to fabricate a per-task timesheet or a productivity ratio.
