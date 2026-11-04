# HTEP-001 — TWD Relationship Discovery, v0.1

**Research state:** bounded discovery completed; selective verification begun; schema and exhaustive normalization intentionally deferred.  
**Source:** Koios `/proposal_list` snapshot retrieved 2026-11-03T20:42:44.166123Z; 107 TWD governance actions, mainnet.  
**Relationship unit:** a directed, evidenced assertion between **two distinct on-chain governance-action IDs**. This is not a project identity assignment.

## Driver

The action inventory is a reproducible population of 107 TWD submissions. It does not, by itself, preserve whether a submission is a repeat request, materially revised request, later funding installment, or part of a related workstream. Discover just enough such relationships to test whether a relational evidence layer improves historical sampling and longitudinal interpretation in HTEP.

## Method and boundary

1. Read the saved snapshot offline and preserve action IDs and proposal metadata as observed.
2. Inspect titles, amounts, proposal body text, and references for explicit descriptions of earlier requests and likely related pairs.
3. Curate a deliberately **non-exhaustive** set of contrasting relationships. Each candidate records a source action, a target action, a relation label, an evidence excerpt with a metadata-field locator, a support tier, and both requested amounts.
4. Mark `supported` only where the **later proposal's metadata describes the relationship**. This establishes a proposer's expressed account of history, **not independent confirmation** of prior delivery, voting rationales, motivations, or outcomes. Mark `candidate` where relationship rests mainly on names, amounts, and sequence.
5. Stop once sufficient diversity exists to test utility. Avoid building permanent initiative IDs or enforcing a complete type ontology from a single exploratory pass.

## Observed results

- **107** distinct TWD actions available in the dated Koios snapshot.
- **16** curated directed relationship hypotheses touch **28** distinct actions. **11** have explicit support in the later proposal metadata; **5** remain candidates.
- Titles and proposal metadata are rich enough to distinguish several relationships without re-ingesting governance records.
- Automated screening also found **19 unique action-to-action ID mentions** inside proposal prose or reference URLs in the snapshot. These are *mention candidates*, not automatically funding-history relationships, and are not appended wholesale to the curated set; some may be budget governance references rather than predecessor TWDs. Their existence indicates an additional, more rigorous ID-based discovery method if needed.

### Selective comparisons

| Relationship | Earlier → later requests | Evidentiary observation | Status |
|---|---:|---|---|
| Amaru continuation | ₳1.5M → ₳10.142M | Later proposal explicitly calls itself the second withdrawal and cites earlier funding | Supported by metadata |
| Eternl revision | ₳1.68M → ₳2.35M | Later proposal explicitly describes the prior proposal and a missing-audit-clarity objection; *the objection is the proposer's account, not independently checked CC votes* | Supported by metadata |
| Scalus revised request | ₳8.503M → ₳2.465M | Later proposal calls itself a focused resubmission with reduced scope and duration | Supported by metadata |
| Cardano Summit event restructure | ₳14.077M combined → ₳7.8M Summit / ₳3.304M TOKEN2049 baseline | Later metadata explicitly describes revision and decoupling; the separate top-up proposal is a further candidate relation | Supported / candidate |
| Pallas / Dolos / UTxO RPC | 2025 and 2026 requests | 2026 metadata describes 2025 budget maintenance funding, explicitly naming all three | Supported by metadata |
| Tweag 2026–2028 → 2026–2027 | ₳39.787M → ₳18.263M | Nearly identical work identity with changed amount and horizon; later text not yet confirmed as directly referencing former action | Candidate |
| Ikigai deposit reimbursement | ₳103K → ₳103K | Repeated request title and amount in two expired actions | Candidate |

Amounts are **on-chain amounts requested**, not costs actually incurred. The status of each TWD can be obtained from the underlying `twd-actions.csv` and Koios records; relationship discovery does not modify those statuses.

## Relationship vocabulary (provisional)

- `resubmission_of`: a later governance request is made again; requires evidence that the subject is substantially the same, not merely a similar title.
- `revision_of`: a later governance request materially changes an earlier proposal. This does **not** edit the earlier on-chain action.
- `continuation_of`: an additional request concerns a later phase or period of continuing work; not evidence of successful previous delivery.
- `split_from`: a previously combined request is reconstituted into separately submitted scopes.

These are **not mutually exclusive**: a revision can also be a resubmission; a split can also involve revisions. Do not infer causation or institutional motives from a relation label.

## What this does and does not validate

The discovery supports a limited version of **P1 (reusable evidence)** and **P3 (longitudinal value)**: relationships can be anchored in stable action IDs and source-specific metadata, and they expose multi-step histories absent from the flat inventory. Whether a relational layer materially improves **cost reference classes (P4)** or remains **proportionate (P5)** requires applying it to actual evidence cases, not adding more candidate edges.

Unresolved: whether title-based links are correct; whether more complicated many-to-many histories need stable initiative IDs; whether external / Catalyst proposal IDs are required; and whether the relationships expose realized expenditure or outcomes. These are questions to be activated only if selected historical cases require them.

## Stopping rule and next use

**Stop broad TWD relationship discovery at v0.1.** For the initial HTEP sample, test a few contrasting histories: (a) Amaru as continuation; (b) Scalus or Eternl as revised request; (c) the event-program split, or a recurring infrastructure project across budget cycles. Verify each chosen pair's source links and available downstream evidence *when selected*. Then undertake a **bounded Catalyst Evidence Survey** to decide whether the first HTEP sample benefits from cross-mechanism histories.

No new mandatory Corpus schema, permanent initiative catalog, complete duplicate classification, or claim that the other 79 actions are unrelated is warranted.

## Evidence boundary / repository role

The source Koios wrapper and its action inventory remain in the **Treasury Evidence Corpus**. The curated `twd-relationship-candidates.csv` and this exploratory interpretation belong in the **Treasury Observatory**, under `probes/HTEP-001/reconnaissance/`, until verified relation assertions have a reusable shape fit for promotion. `twd-relationship-coverage.csv` simply records discovery coverage; `false` **does not mean unrelated**.

The Python script reproduces the two CSVs from the original Koios snapshot. It uses explicitly curated pair selectors: it is reproducible *curation*, not automatic detection of every relation, and assumes the snapshot still contains exactly 107 TWDs.
