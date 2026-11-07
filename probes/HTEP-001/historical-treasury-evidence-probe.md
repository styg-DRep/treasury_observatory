# Historical Treasury Evidence Probe

## Status

**Closed — qualified findings (effective upon accepted merge of HTEP closure PR #6)**

Closure decision: [HTEP-001 Closure Learning Record](HTEP-001-Closure-Learning-Record.md). The original mandate below is preserved as activated; its separate check/learn record documents the accepted early stop and the requested variance for prospective burden logging.

This probe is a bounded experiment within the Treasury Observatory Formation Inquiry.

Its purpose is to test whether a small body of historical treasury activity can be transformed into reusable, provenance-preserving evidence that supports longitudinal sensemaking and cost inquiry.

The probe is exploratory.

It does not establish a canonical treasury dataset, final evidence schema, cost standard, or permanent ingestion process.

---

# 1. Probe Driver

Historical treasury activity contains information that may be useful for understanding costs, estimation practices, funding trajectories, delivery patterns, and other characteristics of the funding commons.

That information is distributed across proposals, governance records, supporting documents, milestone records, transactions, and other sources, and may differ substantially in availability and structure.

Before designing a larger evidence system, the Formation Inquiry needs to determine whether a bounded sample can be collected and represented in a way that produces reusable evidence and meaningful longitudinal insight.

---

# 2. Probe Domain

This probe concerns:

> **the collection, preservation, normalization, and exploratory analysis of a bounded sample of historical treasury evidence.**

The probe is responsible for:

- selecting a defensible sample;
- preserving source provenance;
- distinguishing source evidence from interpretation;
- testing a minimal evidence representation;
- documenting ambiguity and missing data;
- attempting limited longitudinal and cost analysis;
- recording the effort required to produce the evidence;
- leaving reusable corpus records behind.

The probe is not responsible for:

- constructing a complete treasury database;
- establishing final cost categories;
- determining whether past proposals were correctly priced;
- assigning proposer quality or value scores;
- producing binding benchmarks;
- defining the final Observatory architecture.

---

# 3. Parent Formation Hypotheses

The probe primarily informs:

### H01 — Durable Shared Memory
A durable shared record of treasury evidence can improve the commons' ability to carry learning across funding decisions and governance cycles.

### H02 — Longitudinal Integration Improves Sensemaking
Connecting evidence across time can help participants reason about trajectories, persistence, structural change, and prior interventions more effectively than isolated snapshots.

### H06 — Historical Reference Classes Can Improve Cost Reasoning Without Becoming Price Rules
Historical treasury and external evidence may support useful comparison without automatically becoming normative benchmarks.

### H11 — Observatory Burden Can Remain Proportionate
Useful evidence and assurance may be produced without imposing costs that outweigh their informational value.

The probe also produces early evidence relevant to:

### H12 — Commons Capacity Rather Than Institutional Dependency
Reusable corpus records may increase the ability of other researchers to work independently of the Observatory.

---

# 4. Local Probe Hypotheses

## P1 — Reusable Evidence

A bounded sample of historical treasury proposals can be collected into provenance-preserving records that can be reused for questions beyond the immediate probe.

## P2 — Minimal Normalization

A relatively small shared schema can represent enough common information across proposals to support comparison without erasing important contextual differences.

## P3 — Longitudinal Value

Connecting proposal and funding records across time will reveal at least some decision-relevant patterns that are difficult to see from individual proposals.

## P4 — Cost Comparability

Some subset of the sample will support useful cost comparison or reference-class reasoning.

## P5 — Proportionate Intake

The effort required to collect and normalize the sample will be low enough to suggest that further corpus development could be justified.

These hypotheses may be supported, weakened, reframed, or left unresolved.

---

# 5. Sample

The initial target is approximately **30 historical treasury-funded proposals or governance actions**.

The sample should be large enough to reveal recurring data structures and comparability problems, but small enough that the probe remains reversible.

Selection should intentionally include variation where possible, such as:

- funding size;
- project type;
- funding period;
- recurring versus one-time requests;
- maintenance versus development;
- incumbent versus first-time recipients;
- technical versus non-technical work.

The sample does not need to be statistically representative.

Its purpose is methodological discovery.

Selection criteria and exclusions should be recorded.

---

# 6. Evidence Handling

Every proposal included in the probe should leave behind a durable evidence record in the Treasury Evidence Corpus.

The evidence model should distinguish at least three layers.

## Source Record

A faithful preservation or structured capture of the retrieved source material.

Where full preservation is not appropriate or possible, the record should retain sufficient source identifiers and metadata to support later retrieval.

## Provenance Record

The record of where the evidence came from.

This should include, where available:

- source URL or canonical identifier;
- governance action or proposal ID;
- retrieval date;
- source type;
- source version or revision where identifiable;
- retrieval method;
- relationship to other records.

## Normalized Record

A structured interpretation of selected evidence according to the experimental schema.

Normalized fields should remain traceable to their underlying source wherever practical.

A normalized record should never silently replace the source record.

---

# 7. Initial Evidence Profile

The probe should attempt to identify whether the following information is available and useful:

### Identity
- proposal or governance identifier;
- proposer or recipient;
- date or epoch;
- funding mechanism.

### Funding
- requested amount;
- denomination;
- payment structure;
- prior related funding where identifiable.

### Scope
- stated purpose;
- project type;
- duration;
- major deliverables.

### Cost
- major cost categories;
- labor quantities or rates where supplied;
- infrastructure costs;
- external services;
- contingency;
- other material assumptions.

### Execution
- milestones;
- later scope changes;
- later funding;
- known completion or delivery evidence.

### Context
- relevant market conditions;
- governance process;
- important dependencies;
- comparability limitations.

Not every field is expected to be available.

Missingness is itself evidence.

---

# 8. Minimal Experimental Schema

The first schema should prioritize descriptive usefulness over completeness.

Every proposed field should answer:

> **What inquiry becomes possible because this field exists?**

Fields that cannot answer that question should not automatically be included.

The schema should remain versioned.

Changes discovered during the probe should be recorded rather than silently normalized away.

---

# 9. Analysis

The probe should attempt only enough analysis to determine whether the evidence generates useful learning.

Possible exploratory analyses include:

- funding amount distribution;
- proposal categories;
- repeated recipients;
- funding over time;
- recurring project classes;
- estimate structure;
- cost-category availability;
- estimate-to-later-funding relationships;
- possible reference classes;
- missing-data patterns.

Where the data permits, at least one longitudinal representation should be attempted.

The purpose is not to produce definitive treasury conclusions.

It is to determine what kinds of conclusions the evidence can responsibly support.

---

# 10. Epistemic Handling

The probe should preserve distinctions among:

### Observation
What the source states or records.

### Transformation
How source material was normalized or categorized.

### Interpretation
What an analyst believes the transformed evidence may indicate.

### Judgment
Any conclusion about desirability, pricing, governance action, or public value.

These layers should remain visible in both the Corpus and the probe results.

Disagreement or ambiguity should be recorded rather than resolved merely for schema cleanliness.

---

# 11. Burden Record

The probe should record the effort required to produce the evidence.

At minimum:

- time spent locating sources;
- time spent extracting evidence;
- time spent normalizing records;
- recurrent ambiguity;
- specialist interpretation required;
- steps that appear automatable;
- steps that appear resistant to automation.

This record is a probe output, not administrative overhead.

It directly informs whether future corpus development is proportionate.

---

# 12. Probe Outputs

The probe should leave behind:

## In the Treasury Evidence Corpus

- source/provenance records for the sample;
- normalized proposal records;
- the experimental schema and version history;
- documentation of known limitations.

## In the Treasury Observatory

- sample-selection rationale;
- probe method;
- exploratory analyses;
- longitudinal views;
- findings;
- unresolved questions;
- burden assessment;
- implications for parent hypotheses;
- recommended next step or branch.

---

# 13. Interpretation Criteria

The probe should not be judged simply as a success or failure.

Instead, interpretation should ask:

### Evidence usefulness
Did the sample support meaningful comparison or trajectory analysis?

### Reusability
Did the corpus records remain useful outside the immediate analysis?

### Comparability
Which categories of proposal could or could not be meaningfully compared?

### Burden
Was the evidence sufficiently useful relative to the effort required?

### Epistemic integrity
Could source, transformation, interpretation, and judgment remain distinguishable?

### Unexpected learning
What did the probe reveal that its designers did not anticipate?

---

# 14. Possible Outcomes

## Continue

Evidence is sufficiently useful and reusable to justify additional corpus development or another analytical probe.

## Refine

The concept appears useful, but the schema, sample, intake process, or methods require modification.

## Redirect

Historical evidence is too incomplete or heterogeneous for the intended purpose, but the probe identifies another promising direction such as prospective evidence capture or external market comparison.

## Stop

The evidence generated does not justify the cost or complexity of continued work in this direction.

None of these outcomes should be treated as institutional failure.

---

# 15. Review and Closure

The probe is complete when:

- the agreed sample has been processed or a documented reason exists for stopping earlier;
- corpus records have been committed;
- analytical outputs are available;
- limitations and ambiguity are documented;
- burden has been recorded;
- parent hypotheses have received a learning update;
- the next recommended path is explicit.

The probe should close with a short learning record:

> What did we expect?  
> What did we observe?  
> What changed in our understanding?  
> What remains unresolved?  
> What should happen next?

---

# Working Principle

> **Collect once where practical, preserve provenance, interpret cautiously, and leave the evidence more reusable than you found it.**
