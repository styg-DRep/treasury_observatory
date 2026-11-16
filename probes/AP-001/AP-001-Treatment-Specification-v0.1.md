# AP-001 — Treatment Specification v0.1

**Status:** Proposed implementation protocol for AP-001; subject to review before reader exposure  
**Parent agreement:** [`probes/AP-001/probe.md`](./probe.md)  
**Formation issue:** [#7](https://github.com/styg-DRep/treasury_observatory/issues/7)  
**Location:** `probes/AP-001/treatment-specification-v0.1.md`  
**Evidence baseline:** [S1 Amaru](./evidence/AP-001-S1-Amaru-evidence-manifest.md) and [S2 Eternl](./evidence/AP-001-S2-Eternl-evidence-manifest.md)  
**Pinned Evidence Corpus commit:** [`e34d1c9beddddbb6cb8ae3fb8c5135af1525ce89`](https://github.com/styg-DRep/treasury_evidence_corpus/commit/e34d1c9beddddbb6cb8ae3fb8c5135af1525ce89)

> **Governing principle:** Make evidence easier to encounter, relationships easier to understand, and interpretations easier to contest—without making conclusions easier to inherit unexamined.

## 1. Purpose and authority

This document specifies the *differences* among AP-001's three authorized representation treatments, the controls necessary to compare them, and the observations that might support or challenge the method. It operationalizes the merged AP-001 agreement; it does not broaden that agreement, replace the evidence manifests, alter the Corpus, or authorize an assessment service.

**Experimental question:** Can transparent, uncertainty-aware representations of the *same independently preserved historical evidence* improve participant understanding and traceability without producing false comparability, anchoring, or de facto Observatory assessment authority?

AP-001 is a bounded exploration of evidence representation, **not** an audit, an evaluation of historical funding merit, a cost reference-class study, a randomized causal trial, or a prospective proposer-intake test. No ratings, rankings, funding recommendations, binding cost rules, composite confidence indicators, production tooling, or unverified matched-cost comparisons are permitted.

The intended progression is **A → B: introduce structure** and **B → C: introduce offered interpretations**. It is *not* an expected hierarchy of quality. The differences between C and A combine multiple interventions and cannot isolate one mechanism.

## 2. Common evidence substrate

Exactly two HTEP-001 histories are admitted: **S1 Amaru** and **S2 Eternl**. They are contrasting histories, **not a project-efficiency or realized-cost reference class**. Each has its own pinned manifest, source register, and verification boundaries.

All three treatments of a given case must draw on that case's *same admitted Corpus evidence*. The source universe is available to readers in each condition, even when the visible foreground differs. No later treatment may silently receive facts unavailable in A. No HTEP analytical memo or new public-source retrieval may be treated as additional evidence by default. Any exception requires documented justification and review before exposure.

All material is anchored to the Corpus commit above. The manifests' source snapshot is Koios `proposal_list`, with indexed proposer-authored metadata; independent IPFS-original validation and independent rerunning of raw hash/extraction checks were **not** performed during manifest preparation. The treatments must not imply otherwise.

The invariant epistemic distinctions are:

- **Observation:** a recorded field or source text, including the source's stated provenance.
- **Transformation:** a documented extraction, aggregation, mapping, categorization, or formatting operation.
- **Source assertion:** a statement made by a proposer or other source party, not automatically an independently verified fact.
- **Interpretation:** a possible account of meaning, significance, or relationships, with assumptions and uncertainty visible.
- **Judgment:** a reader's contingent decision about relevance, reliance, merit, or action; not an Observatory output.

These distinctions are analytical aids, not claims that every record can be cleanly placed in only one category. In particular, the Corpus's `relationships.csv` combines source-backed assertions with **curator classifications**, which must not appear as ledger-native or causal facts.

## 3. Treatment definitions

| Dimension | A — Source-first | B — Structured | C — Plural |
|---|---|---|---|
| Intervention | Minimal source navigation | Source-traceable analytical organization | Exactly B's structured core plus explicit alternative readings |
| Primary reader work | Reconstruct events and relationships | Inspect organized economic distinctions and trace claims | Inspect B's structure and test offered readings against evidence |
| Organization | Corpus index and neutral file descriptions | Chronology, event/status distinctions, relationship layout, uncertainty | Same chronology, distinctions, layout and uncertainty as B |
| Interpretation supplied | No Observatory case-memo conclusions | No funding-merit conclusion; analytical choices disclosed | At least two clearly attributed or explicitly hypothetical, non-authoritative readings |
| Source access | Pinned Corpus records | Same records and locators | Same records and locators |
| Principal risk | Cognitive load or misclassification | Reification of layout into authority | Anchoring, false dichotomy or deference to supplied narratives |

### A — Source-first: evidence access without new synthesis

**Construct:** a fair and usable entry into the Corpus evidence. Include the case title as a navigational label, pinned manifest, file index, neutral descriptions of record types, stable governance action IDs, provenance links, and the common non-assessment disclaimer. Preserve source caveats. Do **not** supply an Observatory-authored chronology, derived comparison table, thematic emphasis, analytical relationship diagram, or proposed reading of historical significance. Existing Corpus README commentary is part of the admitted source materials; distinguish it from newly authored Observatory synthesis.

**Expected benefit:** readers retain freedom to choose which connections matter. **Risk to observe:** readers may confuse actions, infer spend from withdrawals, miss important relationships, or incur disproportionate source-navigation burden. A must not be artificially degraded to make B appear useful.

### B — Structured: traceable analytical legibility without conclusion

**Construct:** organize A's exact source universe into a concise chronology/event table, explicit economic-status vocabulary, relationship presentation, source-claim attribution, and visible missingness/verification boundaries. Cite actionable source locations for consequential statements; document any calculations or transformations. Make authorial selection and emphasis inspectable. Do **not** supply an interpretation of whether funding was deserved, efficient, appropriate, successful, or fiscally prudent. Avoid evaluative titles such as “overspending” or “good stewardship.”

**Expected benefit:** improved comprehension and traceability with less reconstruction effort. **Risk to observe:** a clean diagram or chronology may be accepted as a complete, authoritative funding history or as validated cost assurance.

B is **conclusion-restrained**, not interpretation-free: selecting and organizing evidence necessarily affects salience. That intervention is part of what AP-001 must examine.

### C — Plural: structured evidence with contestable readings

**Construct:** reproduce B's structured core **without changing its facts, ordering, source links, emphasis or uncertainty markers**, and append a clearly separated section containing **at least two** non-authoritative alternative readings. Attribute an interpretation to its actual source when demonstrably sourced; otherwise label it *hypothetical Observatory-authored reading*. Each reading should state (i) its focal question, (ii) what admissible evidence lends it plausibility, (iii) which assumptions remain unverified, and (iv) at least one way the reader could contest or extend it. Invite readers to reject both or offer an additional reading.

The readings need not be mutually exclusive or polarized; different plausible questions may constitute plurality. Do not create fictional stakeholder quotes, assign positions to actual participants without evidence, or imply that two readings exhaust the possibilities.

**Expected benefit:** readers articulate assumptions and alternative explanations without inheriting an Observatory conclusion. **Risk to observe:** readers repeat prewritten frames, treat the pair as exhaustive, or interpret polished narrative as recommendation. The additional text/reading burden belongs in the observation record.

## 4. Case-specific application constraints

### S1 — Amaru: continuation and claimed returns

The substrate contains **A0**, a 2025 budget Info Action with an expired/dropped protocol record; **A1**, an enacted 2025 withdrawal action with ₳1,500,000 in withdrawal fields; and **A2**, an enacted 2026 withdrawal action with ₳10,142,000 in withdrawal fields. The Corpus has three manually reviewed relation assertions (`follows_budget_statement`, `references_prior_budget`, `continuation_of`), and five **proposer-reported, not independently ledger-verified** return amounts/transaction references. The Info Action's expiration does not resolve claims about a favorable vote; vote tally/threshold verification is out of the admitted record.

- **A:** index and offer the case's pinned records, including `actions.csv`, `withdrawals.csv`, `sources.csv`, `relationships.csv`, and `reported-returns.csv`.
- **B:** make A0/A1/A2's different action types and lifecycle statuses legible; represent relationship *assertions* without upgrading them to causal proof; separate reported returns from verified transfers; do not compute “net spent.”
- **C, candidate reading 1 — continuity lens:** linked actions may support investigating the initiative as a longitudinal funding history, while actual scope/delivery continuity remains unverified.
- **C, candidate reading 2 — verification lens:** linked withdrawals and reported returns do not establish downstream expenses, reconciled refunds or realized costs.

The two candidate readings are **hypothetical analytical lenses**, not findings about Amaru's merit. Their final wording must be checked against the pinned source locators before reader exposure.

### S2 — Eternl: revision and planning assumptions

The substrate contains **E1**, an enacted 2025 maintenance withdrawal request for ₳583,000; **E2**, an expired 2026 request for ₳1,680,000; and **E3**, an enacted revised request for ₳2,350,000. The Corpus classifies E3 → E2 as `revision_of`, and E2/E3 → E1 as `references_prior_funding`. Proposer-attested planning exchange rates are **$0.25/ADA** (E2) and **$0.1787/ADA** (E3); allocated audit budgets are **₳16,800** and **₳47,000**, respectively. They are not evidence of realized currency conversion or completed audits.

- **A:** index and offer the pinned action, withdrawal, source, relationship, and budget-claim records.
- **B:** distinguish E2's **expired request** from E1/E3's enacted actions; depict E3 as a **new action revising E2**, not an in-place modification; preserve nominal ADA amounts and the separate approximate planning rates; do not present a nominal sum of all requests as funding disbursed.
- **C, candidate reading 1 — planning-context lens:** the change in nominal ADA requested should be read alongside disclosed changes in planning assumptions, without claiming that exchange-rate changes explain all of the revision.
- **C, candidate reading 2 — governance-process lens:** the revision and the proposer's account of feedback may illuminate the request's evolution, without independent validation of CC-member rationales or the cause of every changed term.

These are **hypothetical analytical lenses**, not explanations established by independent investigation. Do not infer spending, outcomes, project merits, or equivalent scope across the actions.

## 5. Treatment integrity and production rules

Before creating reader-ready variants, retain the following controls:

1. **Fixed substrate:** all source-derived claims must have a corresponding admitted record and locator; record any exception before exposure. Version the exact files shown to readers.
2. **Matched core:** B and C must use the same structured core verbatim where practical; C's distinct intervention is the appended readings. Changes to tone, graphic prominence, colors or navigational affordances must not silently favor C.
3. **Fair baseline:** A offers functional, readable Corpus navigation. All treatments carry the same disclosed preparer, provenance availability, scope limitations, and non-recommendation statement.
4. **Economic meanings:** request ≠ enacted authorization ≠ downstream execution ≠ expenditure; proposed budget ≠ actual cost; reported return ≠ verified refund; planning exchange rate ≠ actual conversion rate; source-backed relationship ≠ verified continuity or causation.
5. **No hidden normalization:** any aggregation, unit conversion, omission, sorting or transformation is labeled with method and input records. Prefer no derived totals unless directly necessary to the reader task.
6. **Case portability:** define the representational pattern using S1 first, then apply it to S2 without redesigning treatment boundaries to exploit case-specific features. Document unavoidable differences rather than forcing unlike claims into identical tables.
7. **Negative-case audit:** before exposure, ask whether a reasonable reader could interpret headings, page layout, selective emphasis or Observatory branding as a merit, verification or approval signal. Revise and record the concern.

A simple pre-exposure integrity check should answer: Can a reader reach the same source material from A/B/C? Does B visibly distinguish claims from verified observations? Does C add readings rather than new evidence? Is any financial comparison implying verified costs? Could presentation conventions confer unwarranted authority?

## 6. Exploratory expectations and adverse observations

These are **local AP-001 expectations**, not additions to the Formation Hypothesis Registry or proof obligations requiring quantitative scoring.

| ID | Expectation | Observation that could support it | Observation that could complicate or count against it | Related AP-001 questions |
|---|---|---|---|---|
| **E1 — Structural assistance** | B supports better economic distinctions and source-traceable comprehension than A | Reader distinguishes action lifecycle, requested amounts and missing realized spending; locates a consequential source | New misclassifications; reliance on unsourced inferences; no useful gain relative to burden | P1, P2, P4 |
| **E2 — Interpretive plurality** | C helps readers identify assumptions and generate or contest defensible readings relative to B | Reader questions a proposed lens, identifies its assumptions or offers a new plausible question | Reader merely repeats prepared readings or treats them as an exhaustive choice | P2, P3 |
| **E3 — Authority risk** | B or C may increase unwarranted certainty or deference | Reader explicitly notices a misleading signal, or reported confidence exceeds the evidence | If no such effect is observed, the concern remains unconfirmed—not disproven by a tiny sample | P1, P3 |
| **E4 — Proportionate complexity** | Added structure/interpretation must justify their preparation and reading costs in participant-relevant usefulness | Reader identifies concrete assistance worth the added effort; independent investigation becomes easier | Cost or confusion exceeds perceived benefit; investigator support is necessary | P4 |

**Two kinds of possible benefit:** AP-001 may directly observe *informational usefulness* (comprehension, source tracing, recognition of uncertainty). It may collect only early indications of *developmental usefulness* (capacity for independent future inquiry). A short exercise cannot establish durable improvement in governance judgment or long-term autonomy.

**No scoring or winner selection:** preserve examples, disagreements, error types, pauses, voluntary usefulness judgments, and contrary observations as qualitative evidence. Reader preference is not equivalent to improved comprehension or better governance outcomes.

## 7. Reader encounter and prompt protocol

AP-001 requires **at least one voluntary cold-start reader** exposed to Corpus evidence before Observatory-authored interpretation; seek a second independent reader only if feasible within the ceiling. The recommended sequence gives each reader a short **A/Corpus-first encounter**, captures their initial response, and then shows B and C in **counterbalanced order across readers when feasible**. This respects cold-start source access while making clear that the later presentations are affected by learning and carryover. If a reader sees only one subsequent treatment, record that limitation. Do not characterize later responses as independent first-exposure comparisons or as causally attributable treatment effects.

Use the *same core open-ended prompts*, adapted only for case identifiers, following each encounter:

1. **Reconstruction:** What actions or events can you establish from what you saw? Which economic distinctions matter?
2. **Unknowns:** What cannot be established from the available material?
3. **Traceability:** Select one consequential claim; where would you go to verify its source and verification boundary?
4. **Interpretive independence:** What different reasonable questions or readings occur to you? What assumptions would each require?
5. **Reliance and authority:** What would you, or would you not, rely on in a contemporary deliberation? *What, if anything, does this representation seem to be telling you to conclude?*
6. **Benefit and burden:** What helped or hindered your inquiry? Was the added effort worthwhile to you?

Collect answers before revealing any later representation or offered interpretations. Do not coach the participant toward the prepared C lenses before they independently respond. Questions may be shortened if needed to respect time limits, with deviations logged. Record exposure order, prior familiarity, approximate time, source checks actually attempted, and any investigator assistance. Preserve unexpected, mixed and negative reactions.

Before participation, disclose experiment purpose, who prepared the treatments, absence of funding-merit assessment, expected use of notes, attribution/publication choices, and the right to decline or withdraw unpublished responses. Obtain explicit consent. Private responses are **not published by default** and do not belong in the Corpus. Invite independent review of findings before closure.

## 8. Burden, stopping and governance

**Authorized ceilings:** 12 cumulative investigator hours; 4 cumulative invited-reader hours. Record preparation/retrieval, variant assembly, recruitment, reading/response, interpretation, review, deviations and unmeasured effort prospectively. The separately documented closure review is excluded from these initial ceilings per the parent agreement; do not silently exempt ordinary analysis or preparation.

Stop further experimental work and seek re-review upon either ceiling being reached, substantive evidence/provenance failure preventing faithful representation, or serious consent/authority concern. Stop earlier if additional work ceases to reduce consequential uncertainty. Additional cases, variants, participant demands or prospective proposer intake require separate authorization or an amended probe agreement.

**Outputs in the Observatory:** this versioned specification; six case-treatment artifacts (S1-A/B/C and S2-A/B/C) or a documented justified stop; shared reader prompts; a lightweight version/exposure and burden record; consent-appropriate observations; adverse and alternative readings; independent challenge; and a closure learning record evaluating P1–P4 and relevant parent hypotheses with a decision to **continue / refine / redirect / stop**.

**Outputs in the Corpus:** none required. Any correction or schema proposal proceeds through independent Corpus governance. The Observatory cannot overwrite source records by presenting them differently.

## 9. Pre-exposure decision record

- **Treatment definitions:** A source-first; B conclusion-restrained structure; C B plus at least two explicitly hypothetical/attributed readings.
- **Substrate:** S1 and S2 pinned at the commit above; no additional evidence admitted by default.
- **Primary comparisons:** B versus A for structure; C versus B for supplied interpretive plurality. Neither yields a controlled causal estimate under the planned reader encounter.
- **Reader design:** Corpus-first cold-start, qualitative tasks, exposure/carryover recorded; second reader and counterbalancing contingent on capacity.
- **First build:** produce S1-A/B/C, inspect treatment integrity, then reproduce the method for S2-A/B/C.
- **Open risks to track:** A's usability; B's apparent completeness; C's anchoring; economic conflation; visually induced authority; source verification gaps; additional reading burden.
- **Change rule:** any substantive adjustment to intervention boundaries or admission of new evidence requires a versioned amendment and documented review before exposure. Minor typo fixes may be documented without altering treatment meaning.

**Interpretive posture:** Increased legibility is not itself increased truth. Explicit plurality is not itself reader independence. Better understanding is not a funding recommendation. AP-001 learns from each distinction without trying to settle it in advance.
