# Probes

This folder contains bounded formation experiments used to reduce consequential uncertainty about the Treasury Observatory.

A **probe** is not a project plan or permanent program.

It is a deliberately scoped piece of work designed to generate evidence about an important hypothesis, design choice, or institutional uncertainty.

## When to Propose a Probe

A probe is appropriate when:

- the Formation Pathmap identifies a consequential uncertainty;
- meaningful evidence can be generated through a bounded activity;
- the result could change what the Observatory does next;
- the work can remain reasonably reversible;
- the expected learning is proportionate to the effort required.

A probe should not be created merely because a topic is interesting.

A useful test is:

> **What consequential uncertainty will this work reduce, and what might we do differently depending on what we learn?**

## Minimum Probe Structure

A proposed probe should normally include:

### Status
Usually `Proposed` when submitted.

### Probe Driver
What condition gives the Formation Inquiry reason to undertake this work?

### Probe Domain
What field of activity is the probe responsible for, and what lies outside its scope?

### Parent Hypotheses
Which Hypothesis Registry entries does the probe inform?

### Local Hypothesis or Learning Questions
What does this particular probe expect to learn?

### Method or Intervention
What will actually be done?

### Evidence Handling
What evidence will be collected, preserved, or generated?

### Interpretation Criteria
How will the results be examined without reducing the probe to a simple pass/fail test?

### Outputs
What artifacts should remain when the probe concludes?

### Closure Conditions
What needs to be complete for the probe to close?

The structure should remain proportional to the probe.

Small probes should stay small.

## Probe Lifecycle

The working lifecycle is:

```text
Establish
   ↓
Activate
   ↓
Conduct
   ↓
Check
   ↓
Learn
   ↓
Close
```

### Establish

A probe is drafted and proposed through a pull request.

The PR should reference the relevant formation issue or Pathmap territory.

### Activate

Review asks whether the probe:

- responds to a consequential uncertainty;
- has a bounded domain;
- makes relevant hypotheses explicit;
- aligns with current Design Principles;
- appears proportionate to the learning sought.

Merging the probe agreement changes its status from:

`Proposed → Active`

The merge establishes the working agreement for the probe.

### Conduct

Work proceeds within the active probe domain.

Small operational choices do not require governance.

Material changes to the probe's scope, method, or agreement should be visible through commits or pull requests.

Where the probe produces reusable evidence, that evidence should be contributed to the appropriate evidence repository rather than embedded only in analysis.

### Check

Before closure, results should be reviewed for:

- evidence support;
- provenance;
- visible uncertainty;
- alignment between method and conclusions;
- treatment of competing explanations;
- documented burden;
- adherence to the probe's agreed boundaries.

Checking does not require agreement with the interpretation.

### Learn

The probe should record:

> What did we expect?  
> What did we observe?  
> What changed in our understanding?  
> What remains unresolved?  
> What should happen next?

Relevant parent hypotheses should receive learning updates.

### Close

A probe closes when its agreed work is complete, its evidence and limitations are available, and its learning has been integrated into the Formation Inquiry.

A probe may conclude with:

- **Continue**
- **Refine**
- **Redirect**
- **Stop**

None of these outcomes should be treated as failure by default.

## Suggested Folder Pattern

A probe may use:

```text
/probes/<probe-id>/
  probe.md
  analysis/
  findings.md
  learning.md
```

Use only the structure the work actually needs.

Do not create empty folders or documents merely to match a template.

## Relationship to Inquiries

A probe is primarily a **learning intervention**.

An inquiry is primarily a **bounded investigation of a tension, pattern, or question**.

A probe may contain an inquiry, and an inquiry may use probes to test competing hypotheses.

The distinction should remain useful rather than rigid.

## Relationship to Evidence

Evidence should outlive the probe where practical.

Source records, provenance, schemas, and reusable normalized evidence should live in the appropriate evidence commons rather than becoming inseparable from one interpretation.

The probe should link to that evidence and document how it was used.

## Working Principles

> **Inherit the topology, not the bureaucracy.**

> **Use the smallest structure that makes the work legible, checkable, and learnable.**

> **A probe exists to change understanding, not merely to produce activity.**

> **The result of a probe is learning, including learning that redirects or stops the work.**
