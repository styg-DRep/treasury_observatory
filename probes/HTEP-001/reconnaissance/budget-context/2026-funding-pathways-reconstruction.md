# HTEP-001 — 2026 Treasury Funding Pathways: Outside the Verified Intersect Hydra Cohort

**Status:** Reconnaissance / working classification v0.1 · 2026-11-03  
**Parent:** Budget Process Context Register — priorities 3 and 4  
**Source snapshot:** Koios `/proposal_list`, retrieved `2026-11-03T20:42:44.166123+00:00`, tip epoch 665.  
**Population boundary:** 61 TWD actions submitted in epochs 613–665, minus 11 verified members of the Intersect 2026 Hydra budget cohort = **50 actions**.  
**Companion evidence index:** `2026-outside-hydra-actions.csv` (50 action IDs); `summary.json`.

## Driver and question

The 2026 Intersect Hydra cohort explains only eleven of the sixty-one TWD submissions in the second NCL period. What institutional and operational pathways brought the other fifty requests before DReps, and how do those pathways share fiscal capacity without implying that any administrator controls the treasury?

## Central methodological correction

**Outside the verified Intersect 2026 Hydra cohort ≠ outside Intersect, outside institutional sponsorship, or necessarily independent of Intersect's budget work.** The cohort boundary is supported by eleven direct Hydra proposal references; it is not a proof that all fifty others have no informal, administrative, personnel, or budget-process connection.

Do not use one column labelled `independent`. Record the following separate dimensions when directly supported:

1. **Selection route:** Intersect Hydra 2026, another formal budget process, direct TWD without an evidenced prior selection, or unknown.
2. **Institutional driver / sponsorship:** initiating entity or strategic sponsor, which need not be the author or recipient.
3. **On-chain submitter:** transaction signers or other defensible submission evidence, not mere metadata authorship.
4. **Named administrator / custody:** contractual administrator and on-chain recipient account; separate legal role from treasury withdrawal destination.
5. **Delivery or implementing organization:** who does the funded work, possibly multiple parties.
6. **Institutional relationships:** e.g., PRAGMA member, Intersect member, oversight committee, subcontractor; these can be overlapping and temporal.
7. **Funding history:** resubmission, revision, renewal, successor, tranche, or genuinely new work—each relationship requires its own evidence.

Use evidence levels: `explicit public documentation`, `on-chain metadata`, `strong cross-source match`, `candidate / needs confirmation`, `unresolved`.

## Quantitative boundary (Koios snapshot)

| Population | Count | Enacted | Expired | Active / unresolved |
|---|---:|---:|---:|---:|
| Verified 2026 Intersect Hydra cohort | 11 | 10 | 1 | 0 |
| Other actions in epochs 613–665 | **50** | **20** | **27** | **3** |
| Total in epochs 613–665 | **61** | **30** | **28** | **3** |

The 50 non-Hydra actions requested **₳679,475,172**, but only **₳420,671,450** belongs to the 20 eventually enacted actions. These figures are *gross TWD action amounts*, not NCL utilization at every point in time, net spending, vendor disbursements, or delivered work. They should not be added uncritically to commitments that have different NCL treatment.

There are **42 distinct submission transactions** among the 50 actions. Nine actions were submitted together in **epoch 626** in one transaction; the other 41 each have their own submission transaction.

## Preliminary signature clusters (mutually exclusive index labels, NOT institutional categories)

| Investigative signature | Count | On-chain or metadata observation | Boundary |
|---|---:|---|---|
| Other proposer-authored or unattributed | 25 | Other authors, or missing metadata signatures | Does not establish who signed submission transaction or which off-chain selection occurred |
| IOG–Intersect nine-action batch | 9 | Nine co-authored actions in one epoch-626 transaction | Does not establish who signed submission transaction or which off-chain selection occurred |
| Intersect named metadata author, outside Hydra | 7 | Intersect appears as a metadata author but no direct Hydra reference | Does not establish who signed submission transaction or which off-chain selection occurred |
| CF–EMURGO event initiative | 4 | CF or Intersect/EMURGO-authored Summit and TOKEN2049 actions | Does not establish who signed submission transaction or which off-chain selection occurred |
| IOG–Intersect co-authored, outside Hydra | 3 | Other IOG and Intersect-authored actions | Does not establish who signed submission transaction or which off-chain selection occurred |
| Alternative-node / PRAGMA-associated | 2 | Amaru and Dingo submitted before Hydra on-chain cohort | Does not establish who signed submission transaction or which off-chain selection occurred |

### Strongly documented cases

**Amaru 2026 (epoch 614; ₳10.142M; enacted).** Amaru's published governance action describes PRAGMA as the organizational home, a maintainer committee coordinating scope, and direct project budget administration backed by five script accounts and a refund mechanism. Intersect's March 2 committee minutes explicitly refer to Amaru as running its own budget process. This is a documented **project-led, PRAGMA-associated, internally administered** funding pathway; PRAGMA membership is an organizational relationship, not a declaration that PRAGMA signed the governance transaction. [P1] [P2]

**Dingo / Blink Labs (epoch 617; ₳6.9M; enacted).** The action identifies Blink Labs and Dingo, with Cardano Foundation public records confirming a positive DRep vote. Given the user's contemporaneous testimony about PRAGMA membership and alternative-node timing, mark **PRAGMA association—user-reported, independently unverified in this pass**, and **selection/administration route—open**. Avoid copying Amaru's governance model onto Dingo. [K] [P3]

**Cardano Foundation / EMURGO event proposals (epochs 623, 627–628).** The initially joint Cardano Summit/TOKEN2049 request was followed by a revised standalone Summit proposal and separate TOKEN2049 actions (baseline and conditional top-up). Cardano Foundation's public update describes this revision and splitting. These are clear examples of **institutional sponsorship, collaborative authorship, and proposal revision** occurring outside the verified Hydra cohort. Intersect appears as metadata author on the TOKEN2049 actions, without proving Hydra selection. [K] [P4]

**Input Output / Intersect epoch-626 batch (nine actions; one transaction).** All nine governance metadata author lists contain Input Output Global and Intersect. Their titles cover research, upgrades, consensus, maintenance, developer experience, scalability and more. Six were eventually enacted and three expired. On-chain submission coordination is established; **who selected the initiatives, who exercised budget authority, and what formal role Intersect played are NOT established by joint authorship**. This is the highest-priority independent-pathway documentary investigation. [K]

**Intersect-authored separate actions.** For example, the large AlphaGrowth Cardano PRIME withdrawal (epoch 642, ₳120M) names Intersect in action metadata and was enacted outside the documented Hydra cohort. This is evidence that **Intersect institutionally participated in a different funding route**. It is not evidence that the action was part of the 2026 Hydra selected set. [K]

### Candidate repeated/related initiative chains (not adjudicated)

- **Cardano Summit/TOKEN2049:** combined proposal → revised Summit proposal; TOKEN2049 baseline and title-upgrade are related but not necessarily resubmissions of the same request.
- **Tweag core infrastructure:** large epoch-628 action expired; smaller epoch-634 action enacted. Compare scope/budget and formal references before labelling revision.
- **HLabs / Pebble / Gerolamo:** epoch-621 and epoch-629 requests, some shared project components; relationship unresolved.
- **Scalus:** epoch-630 and epoch-640 requests, similar subject but not presumptively identical.
- **Eternl sustainability:** epoch-631 and epoch-637 requests, title explicitly identifies v2.
- **dOSPO / OMF:** epoch-630 and epoch-641 requests, title explicitly identifies revision.
- **Ikigai deposit reimbursement:** epochs 636 and 649, matching title and amount; compare metadata and submitter before confirming resubmission.
- **Critical Integrations:** 2026 V2 refers to an earlier initiative; requires historical cross-year mapping.

## NCL: shared capacity, not an Intersect account

Intersect's March 2 budget-committee minutes state directly that the Net Change Limit constrains all budget processes at Cardano level. Its 2026 FAQ confirms direct actions can be submitted at any time and Intersect's administrative role is distinct from funding approval. Therefore an investigative model of NCL competition should attach **time-specific NCL rules and effective enactments** to TWD lifecycles, including commitments and other budget contexts, rather than treating all proposed ADA as spent or inferring financial competition from temporal proximity. [P1] [P5]

The present package **does not calculate NCL headroom** or infer strategic motives from timing. Preserve user-supplied contemporaneous testimony about perceived competition as a *research lead*, attributed as such, not as on-chain evidence or universal intent.

## Research queue ordered by consequential uncertainty

1. **Epoch-626 nine-action IOG/Intersect submission:** retrieve original proposal PDFs, budget approval/selection explanation, named recipients, escrow and administration contracts. Determine whether this represents an autonomous coordinated pathway or another facilitation route. This tests whether the Intersect budget cohort is only one part of Intersect-associated funding.
2. **Role-level validation of the 50 actions:** extract explicit named sponsor, proposer, administrator, delivery provider and on-chain recipient from proposal source documents. Never fill empty cells with presumed institutional identities.
3. **PRAGMA / node-diversity comparison:** Amaru vs Dingo vs relevant IOG node initiatives; test whether institutionally related projects have different custody and accountability structures.
4. **Foundation / EMURGO event sequence:** verify the explicit revision lineage, different administrators and outcomes from the authoring documents.
5. **Repeated-proposal chains:** examine Tweag, HLabs, Scalus, Eternl, dOSPO, etc. before interpreting expired counts as distinct initiative failures.
6. **Time-sensitive NCL ledger:** identify enacted NCL actions, constraints, applicable epochs and per-event headroom. Do not use a single current limit retroactively.

### Completion criteria

This reconnaissance is sufficiently mature for first-case selection when it can (a) distinguish documented selection pathways from administrators; (b) account for the nine-action IOG batch as a known or explicitly unresolved pathway; (c) present at least three contrasting, source-verified roles/administration models; (d) explain how shared NCL applies without claiming motives; and (e) make a defensible recommendation for the first small HTEP sample. **It need not verify every attribution or settle every resubmission.**

## Sources and provenance

- **[K]** Raw Koios `/proposal_list` response in `koios-proposal-list-raw.json`, retrieved 2026-11-03T20:42:44Z, chain tip epoch 665. Direct links are in companion CSV; labels are derived from that source.
- **[P1]** Intersect Budget 2026 FAQ: https://committees.docs.intersectmbo.org/intersect-budget-committee/cardano-budget-process/cardano-2026-budget-process-faqs
- **[P2]** Intersect Budget Committee March 2 minutes: https://committees.docs.intersectmbo.org/intersect-budget-committee/committee-meeting-notes/2026-meeting-notes/budget-committee-weekly-meetings/march-2nd-2026-budget-comm-minutes
- **[P3]** Amaru 2026 governance action: https://app.cgov.io/governance/2f2fc2539dde550d3c83bea67c11b03861407976bbe8d07c5b0e124aa8a12baa%3A0 ; Amaru documentation: https://amaru.global/treasury/
- **[P4]** Cardano Foundation April 2026 activity update: https://cardanofoundation.org/blog/april-2026-activities ; May update: https://cardanofoundation.org/blog/may-2026-activities
- **[P5]** Intersect 2026 budget overview: https://committees.docs.intersectmbo.org/intersect-budget-committee/cardano-budget-process/cardano-budget-2026-overview
- **[P6]** Cardano Foundation voting and budget review: https://cardanofoundation.org/blog/voting-decisions-2026-intersect-budget-process

**Caveats:** Metadata `authors` are not on-chain transaction signers. A TWD withdrawal address is not automatically the implementing organization. Counts in this document concern TWD actions, not independently verified unique projects, vendor disbursements or expenditure.
