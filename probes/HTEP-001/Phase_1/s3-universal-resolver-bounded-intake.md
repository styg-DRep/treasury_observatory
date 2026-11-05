# HTEP-001 / S3 — Universal Resolver for did:prism

**Bounded intake v0.1 · 2026-11-04 · Catalyst Fund 8 · Catalyst project ID #800352**

## Purpose and boundary

Determine whether an older Catalyst grant record supplies reusable evidence for planned costs, administrative grant status, and reported delivery. This is **not** a code audit, independent assessment of project outcomes, or an audit of spending.

Primary source: https://projectcatalyst.io/funds/8/accelerate-decentralized-identity/universal-resolver-for-didprism (consulted 2026-11-04). The current project page is a mutable public rendering of the historical proposal and reports; historical version integrity was not demonstrated.

## Identified funding object

- Catalyst Fund 8; Accelerate Decentralized Identity challenge; proposal/project ID **800352**.
- Title: *Universal Resolver for did:prism*. Listed team/proposer: Rodolfo Miranda, RootsId-associated.
- Allocated/requested **USD 6,425**; public page reports **Distributed: USD 6,425; Remaining: USD 0** and **Status: Complete**. These are administrative representations, not independent bank/ledger verification or actual project expenditure.
- Voting display: 496 votes cast; about 149 million Yes and 563,000 No voting power; the rendered aggregation should not be interpreted as 496 ADA or as the headcount of beneficiaries.

## Proposed work and budget

The proposal envisioned a PRISM DID-method driver usable with the Decentralized Identity Foundation's Universal Resolver, associated containers, a fork, and a publicly accessible hosted AWS instance. Five proposed deliverables: driver code, driver Docker image, resolver fork integrating driver, fork Docker image, and deployed AWS instance. Planned duration: four weeks; task time boxes were 10 + 5 + 5 *days*, while monetary work estimate used hourly quantities; do not assume these are interchangeable units.

| Budget line | Quantity / basis | Proposed USD |
|---|---|---:|
| Driver development | 40 hours × $100/hour | 4,000 |
| Fork, Docker Hub, hosting activities | 20 hours × $100/hour | 2,000 |
| AWS instance | Annual estimate | 400 |
| Domain + SSL | Combined estimate | 25 |
| **Total** | **60 planned billed hours + operating estimates** | **6,425** |

Labor-like portion $6,000 (93.39% of request); non-labor $425 (6.61%). $100/hour is a **proposal assumption**, not an observed market price, validated timesheet rate, or realized expenditure. None of these line items is evidenced as actually spent through the available administrative display.

## Dated evidence / administrative sequence

| Date | Record | What is established | What is not established |
|---|---|---|---|
| 2022-05-17 | Monthly report, 'In progress' | Reports funding received, work planned to begin in two weeks, estimated completion June 30 | Payment transaction/date or actual work commenced |
| 2022-06-20 | Monthly report, 'In progress', on track | Proposer reports defining PRISM DIDDocument → W3C DID Document transformation and agreement with Atala Prism team; Google Drive supporting file linked | Contents of file could not be retrieved; independent confirmation of agreement absent |
| 2022-07-19 | Monthly report, 'Completed' | Proposer reports project completed and refers to attached final report | Linked final report contents not retrieved; tests, code and actual deployed instance not independently verified |
| Current administrative page | 'Complete'; distributed $6,425; remaining $0 | Current program administration's recorded status and distribution total | Direct payment proof; actual invoice, labor timesheets or operating expenses |

Supporting external documents linked but not substantively read:
- Final/completed outcome report: https://drive.google.com/file/d/1tuGBkU3eWGyWqOr4N-CYxGQjfqEu3F8Y/view?usp=sharing
- July completion evidence: https://drive.google.com/open?id=1j060tTwT-Sg781bstXgK9Xi8MQpn1q9v
- June progress evidence: https://drive.google.com/open?id=1BuvpWNg_Rs_gKXtI6DKoQJ5JOQDdOT1E

Direct link retrieval via public web tool produced inaccessible/cache-miss results. These URLs remain evidence pointers, not verified evidence contents.

## Relationships and topology

- The proposal names earlier Fund 6 and Fund 7 related open-source SSI initiatives and contributions to RootsId. It also **explicitly says this proposal is not a continuation of a previously funded project**; do not assert `continuation_of` based on the team or domain being the same.
- Candidate `related_technical_work` or `shared_contributor` connections may be noted, but they are **not** funding continuations without further evidence.
- The currently maintained Universal Resolver GitHub repository lists a `did-prism` driver from `fabiopinheiro`, which is not sufficient evidence of this 2022 grant's original deliverables, authorship, or continued operation. https://github.com/decentralized-identity/universal-resolver

## Reusability and limitations

**Recoverable:** stable-enough public project identifier and URL; original grant budget arithmetic, proposed output types, three report dates and summary statuses, a completion assertion, named evidence links and recorded award/distribution totals.

**Not verified:** signed source version, actual payments, invoices/timesheets, final report substance, code provenance, live operation, ongoing use, independent economic impact, whether hosting ran for the proposed year.

**Cost comparison candidate:** proposed 60 hours at $100/hour for defined integration and deployment tasks. It is a **planned input-unit reference**, not an observed unit cost or realized deliverable cost. The public page's 'Distributed' is a *program disbursement figure*, not proven project expenditure.

## P1–P5 observations

- **P1 Reusable evidence:** encouraging; the original description, budgets, dated reporting trail, and evidence pointers survive.
- **P2 Minimal normalization:** feasible if record kind, amount semantics, currencies, units, period and attestation are all retained; do not coerce 'reported complete' into 'independently completed'.
- **P3 Longitudinal learning:** limited but present in three dated progress summaries; links to earlier projects are domain/team relationships, not confirmed direct continuations.
- **P4 Cost reference:** narrowly promising for the *estimated* labor-hours and proposed rate, not as realized price/performance evidence.
- **P5 Proportionate burden:** one official project page yields substantial data. Attempted Google Drive source recovery did not yield contents. No precise researcher time instrumentation, so burden is reported qualitatively.

## Stopping rule and reopening

**Close S3 v0.1 for the Phase 1 comparison.** The intake establishes what the older reporting regime can and cannot presently support. Do not pursue a codebase archaeology or full financial verification without a subsequent question that makes it consequential. Reopen only if (a) S4 comparison requires verification of a final report, (b) a historical planned-rate benchmark is proposed for real use, or (c) cross-fund SSI trajectories become a selected sample dimension.

**Methodological lesson:** preservation of a budget arithmetic and an administrative completion flag is materially stronger than total source loss, but materially weaker than a verifiable account of work performed and costs incurred.
