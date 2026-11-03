# Budget Process Context Register — HTEP-001

**Version:** v0.2 — reconnaissance integration / complete enough (2026-11-03)  
**Parent:** Historical Treasury Evidence Probe (HTEP-001)  
**Evidence boundary:** Koios `/api/v1/proposal_list` snapshot retrieved **2026-11-03T20:42:44.166123Z**, tip epoch 665; independent reconstruction notes and public Intersect documentary sources from the four priorities.  
**Companion:** [`budget-process-action-register-v0.2.csv`](budget-process-action-register-v0.2.csv), **107** actions; joins by immutable `action_id`.  
**Status:** **Reconnaissance sufficiently complete for HTEP sampling**, not exhaustive historical or constitutional reconciliation.

## Driver

The timing and count of TWD actions do not reveal independent funding demand by themselves. Formal budget selection, coordination of submission transactions, individually initiated funding routes, administrative relationships, and a shared Net Change Limit (NCL) all shape the observed record. We need enough institutional context to interpret action cohorts and select historical evidence cases without mistaking procedural effects for independent funding initiatives.

## Boundary and units

The primary observation unit is the **governance action**; the snapshot identifies **107 unique TWD actions in 53 submission transactions** (70 enacted, 34 expired, 3 unresolved). Submissions occurred in **33 epochs**, epochs 566–662; epoch 570 has 39 actions, epoch 626 has nine, and epoch 638 has eleven. An action is not necessarily a unique proposal, funding initiative, recipient, transfer, or delivery history. Distinguish **selection process → selected proposal → submission transaction → TWD action → recipient / administrator → implementing work and subsequent outcomes**. Relations can be many-to-many.

**Important methodological choice:** “Independent” is always *relative to a specified selection mechanism*. **Outside the verified Intersect Hydra cohort** does not imply “no Intersect participation,” “no institutional sponsor,” “unmediated submission,” or “no upstream process.” Separate pathway selection, sponsorship, metadata authorship, transaction submission, custody/administration, delivery, and longitudinal initiative relationships. Unknown is an acceptable state.

## Investigational structure: four priorities, provisional answers, and stopping conditions

| Priority / question | Provisional answer supported by the investigations | Evidentiary boundary | Close status |
|---|---|---|---|
| **P1 · 2025:** How did off-chain budget selection become on-chain withdrawals? | **39 epoch-570 TWDs ↔ 39 distinct Ekklesia references**, each directly linked in TWD metadata; common 2025 Budget Info Action and successful-list reference. 37 eventually enacted, two expired. | Referenced successful-proposals CSV was **not independently reconciled**. Aggregate Budget Info Action ₳275,269,340 vs submitted TWDs ₳275,031,507 (**₳237,833 unexplained**). | **Sufficient for pathway/sampling; conditional reconciliation open** |
| **P2 · 2026:** Which budget-process output produced which TWDs, and did design match execution? | **11 epoch-638 TWDs ↔ 11 distinct Hydra references**, corroborated by published audited results and Intersect June 26 announcement; 10 enacted / one expired. Earlier design considered two consolidated withdrawals; execution was 11 separately votable actions in one transaction. | Audit figures sourced from published results, not independently cryptographically re-audited; proposal revisions/contract execution not exhaustively traced. | **Sufficient for pathway/sampling** |
| **P3 · Other pathways:** What explains actions outside 2026 Hydra, and which institutional roles overlap? | Of 61 TWDs submitted in epochs 613–665, **50 are outside the verified Hydra eleven**. They comprise 42 submission transactions, including the nine-action epoch-626 IOG/Intersect-authored batch. Amaru is project-led and PRAGMA-associated; Dingo is Blink Labs; CF/EMURGO event revisions and Intersect-associated non-Hydra actions show role overlap. | **Outside Hydra is not an independently documented alternative selection route for all 50.** On-chain transaction signer, contractual administrator, sponsor, and implementer were not verified systematically. User’s recollection that IOG submitted separately from the Intersect end-to-end process is useful context, not definitive upstream authorization evidence. | **Sufficient for contrasting pathways; item-level roles open** |
| **P4 · NCL:** How did a common limit apply across pathways, and what happened around PRIME? | 2026–27 NCL originally **₳350M** for epochs **613–713**; a later Info Action proposed **₳500M** over the same window. Before PRIME, enacted withdrawals totaled **₳337,395,629**. PRIME ₳120M enacted at epoch 650, bringing cumulative to **₳457,395,629**: **₳107,395,629 above the old cap**, **₳42,604,371 below the new**. | ₳500M Info Action **expired in ledger terms** while public vote records showed >50% DRep Yes. Its constitutional recognition, decisive tally, and individual CC rationales remain unresolved. PRIME **was enacted**, and an adverse CC ruling is **not established**. | **Sufficient arithmetic/context; bounded constitutional ambiguity open** |

**Closure judgment:** Each priority now supplies a defensible, falsifiable context for sample design. Reopening is justified by a *consequential* mismatch affecting a case, an institutionally important new source, or a hypothesis—not by the mere availability of more historical data.

## How the four answers connect

### The two Intersect-selected cohorts are not equivalent governance regimes

| Dimension | Intersect 2025 | Intersect 2026 |
|---|---|---|
| Application population | 194 reported applicants | 69 reported applicants |
| Selection/evidence surface | Ekklesia and aggregate Budget Info Action | Hydra advisory voting and published audit |
| Verified action links | 39 direct Ekklesia references | 11 direct Hydra references |
| Submitted on-chain | 39 TWDs in 3 transactions (epoch 570) | 11 TWDs in 1 transaction (epoch 638) |
| Snapshot outcomes | 37 enacted / 2 expired | 10 enacted / 1 expired |
| Interpretive hazard | Treating a coordinated budget cohort as independent demand | Mistaking proposed consolidation for actual governance-action consolidation |

Both are strong process-to-action crosswalks, but not evidence of equal project scopes, quality, amount semantics, selection denominator, or delivery. The process structure is part of the historical evidence, not a neutral backdrop.

### Other 2026 actions: separate process selection from institutional roles

The **50 non-Hydra 2026 TWDs** include **20 enacted / 27 expired / 3 unresolved**; the enacted twenty withdrew **₳420,671,450** versus **₳36,724,179** enacted through Hydra (as classified by **submission cohort**, not enactment date). The non-Hydra population requested ₳679,475,172. It is heterogeneous, not a single “independent” category.

- **IOG / Intersect epoch 626:** nine co-authored actions in one transaction; six enacted, three expired. The batch is *outside the directly proven Hydra cohort*. User's contemporaneous recollection is that these were independently submitted IOG proposals mentioned in Intersect bulletins, rather than entries in the end-to-end selection process. No evidence here establishes whether IOG had any internal approval mechanism; do **not** equate an unobserved mechanism with no approval.
- **Amaru epoch 614:** project-led process with PRAGMA-associated institutional home and described maintainer committee / project budget controls. The Intersect budget committee itself recognized Amaru's own funding process. Establishing sponsor and administration requires the specific proposal's language, not merely PRAGMA association.
- **Dingo epoch 617:** Blink Labs initiative; PRAGMA membership and NCL-related timing discussed by the user are contextual leads, not proven motivations or an assertion that its administration matches Amaru's.
- **Cardano Foundation / EMURGO event chain:** a combined proposal, later separated/revised actions, and multiple named institutional participants; sponsorship and metadata authorship do not identify transaction submitters or contractual administrators by themselves.
- **Intersect-associated, non-Hydra:** e.g. AlphaGrowth PRIME. Named Intersect metadata participation does not make a proposal Hydra-selected; a treasury withdrawal's receiving stake credential need not represent the eventual project implementer.
- **Resubmissions and continuations:** related titles in Tweag, Eternl, Scalus, dOSPO, Ikigai and event actions suggest candidate relationships. No exhaustive initiative-level deduplication has been performed; preserve them as leads.

### NCL as a shared, time-indexed decision condition

In the 2026 window the ₳350M limit and claimed ₳500M replacement cannot be treated as equivalent *enacted ledger parameters*: NCL agreement is expressed through Info Actions and interpreted under constitutional rules, whereas the withdrawal amounts are directly recorded in the ledger. The ₳500M action's expiry is not proof that it failed its constitutional voting test; neither does a public aggregate vote tally alone resolve the controlling interpretation. PRIME was ratified in epoch 649 and enacted in epoch 650 with affirmative CC support; individual CC rationales are necessary for a member-by-member account of the NCL reasoning.

**The NCL capacity arithmetic is not a motive model.** Cumulative *enacted* withdrawals must not be conflated with pending requests, Intersect-selected allocations, promised vendor disbursements, actual execution spending, or a legal finding of compliance. The NCL applied to all pathways, not to an Intersect-administered funding pool. A later change to the nominal limit can change the fiscal context between *proposal submission* and *enactment*.

## The 107-action annotation model (v0.2)

The companion CSV is an investigative **view**, not a new mandatory Corpus schema. Preserve the underlying Koios rows unmodified in the Evidence Corpus. Every derived field has a source/basis and action ID to permit correction, rebuilding, and independent reuse.

| Column group | Meaning and safeguards |
|---|---|
| **Identity & event** | `action_id`, epoch, submission transaction hash, transaction action count, snapshot outcome and gross requested ADA. Values from the prior working index/Koios snapshot. |
| **Documented selection** | `verified_process_cohort`, `process_link_evidence`, `documented_selection_route`, `offchain_proposal_reference`. Direct 2025 Ekklesia and 2026 Hydra links supersede v0.1 candidate labels. |
| **Institutional roles** | `pathway_signature_exploratory`, `metadata_authors`, `onchain_submitter`, `institutional_driver`, `fund_administrator`, `delivery_organization`, `institutional_role_note`. Missing roles are **not** filled from authorship. |
| **Time-dependent fiscal context** | `ncl_window`, `ncl_context`, and, for the 30 actions enacted in the 2026 period, actual enactment epoch, cumulative withdrawal amount and *counterfactual* headroom under each of ₳350M and ₳500M. Not an assertion of effective NCL at submission. |
| **Provenance & limits** | `source_level`, `ncl_arithmetic_note`, `snapshot_retrieved_utc`; consult the independent priority reports for exact source references. |

**Coverage / validation (disjoint by action ID):**

| Classification | Actions | Evidence |
|---|---:|---|
| `intersect_2025_budget` | 39 | Metadata links to 39 distinct Ekklesia proposal URLs |
| `intersect_2026_hydra` | 11 | Metadata links to 11 distinct Hydra proposal URLs, supported by published audit |
| `outside_verified_2026_hydra` | 50 | Other 2026-period submissions; **not** a uniform affirmative pathway identity |
| `other_2025_outside_verified_budget` | 7 | All other 2025-period submissions; no blanket classification |
| **Total** | **107** | Each action appears once; stable join by `action_id` |

**Do not confuse cohort grouping with institutional attribution.** The categories above are a mutually exclusive *coverage partition*, while sponsor/administrator/delivery/provider relationships are potentially multiple and overlapping.

## Unresolved questions and conditions for reopening

| Question | Current disposition | Reopen if… |
|---|---|---|
| Why is the 2025 Budget Info Action ₳237,833 above the 39 TWD sum? | Preserved as an unexplained discrepancy. | A selected seed case hinges on the exact budget-to-withdrawal reconciliation, or an authoritative itemized source becomes material. |
| Did 2026 Hydra-selected proposals materially change between advisory vote and TWD submission? | Not systematically investigated. | Sampling or cost-comparison requires proposal-version history. |
| Which entity signed each submission, administered custody, and delivered? | Role-level examination deferred for the broad population. | A selected case requires attribution, or an inferred institutional pathway changes. |
| Was epoch-626 IOG batch selected by another off-chain mechanism? | Not determined; documented as coordinated, non-Hydra. | Evidence suggests a specific consequential selection process. |
| Why did individual initiatives submit when they did? | No generalized motive conclusion. User testimony is a lead only. | Contemporaneous primary evidence and an HTEP question justify inquiry. |
| Did the ₳500M NCL amendment achieve constitutional effectiveness, and how did CC members interpret it for PRIME? | Public tally + expiry + later PRIME enactment retained as separate observations. | HTEP selects PRIME or constitutional process is a central question. |
| Are apparently repeated TWDs revisions, continuations, or resubmissions? | Not systematically adjudicated. | A seed case tests initiative-level longitudinal reconstruction. |

## HTEP learning and sampling implications

1. **P1 reusable evidence:** complete action population and explicit 2025/2026 off-chain reference keys provide strong evidence that a source-preserving crosswalk is feasible.
2. **P2 minimal normalization:** a stable action ID, separate transaction and process evidence, provisional institutional roles, and temporal context suffice for the first comparative inventory. This is not a final schema.
3. **P3 longitudinal value:** version changes, fiscal-period switches, process discontinuities, and potentially related actions expose a real need for temporal relationship records; no longitudinal project outcome is inferred.
4. **P4 cost comparison:** amount data is abundant, but requested vs enacted vs administered vs spent costs are not interchangeable. A sample needs explicit funding and delivery evidence before cost comparison.
5. **P5 proportional effort:** aggregate process attribution can be established for the major cohorts without reconstructing every proposal's approvals, contract or voting rationale. Investigate unfilled roles only when a case needs them.

**Practical sampling consequence:** choose first cases across different **funding pathways and documentary forms**, e.g. an Intersect-selected 2025 or 2026 TWD, a project-led 2026 case (Amaru), and a structurally unusual case (PRIME / NCL amendment or a repeat/revision sequence). Do not select three cases merely because three action rows look different.

## Evidence chain and preservation

**Canonical source for action facts:** timestamped Koios raw JSON `koios-proposal-list-raw.json` in the Treasury Evidence Corpus. The full set of source links, individual actions, and evidence boundaries is preserved in the four reports below. The Observatory should hold this integrative register and analytical conclusions; the Corpus should hold faithful captures and reproducible transformations. Until archived, external pages remain live sources and may change.

| Supporting investigation | Artifact | Most important external references |
|---|---|---|
| **P1** | `2025-budget-crosswalk.md` + `2025-budget-action-crosswalk.csv` | Intersect 2025 annual report: https://docs.intersectmbo.org/intersect-knowledge-base/intersect-membership/annual-member-meetings-amm/2025-annual-members-meeting/intersect-development-update-2025-report ; linked Ekklesia items; referenced IPFS successful-proposals list |
| **P2** | `2026-budget-crosswalk.md` + `2026-hydra-to-twd-crosswalk.csv` | Intersect June 26: https://www.intersectmbo.org/news/intersect-weekly-update-117-june-26-2026 ; Hydra final audited results: https://docs.intersectmbo.org/intersect-knowledge-base/cardano-facilitation-services/cardano-budget-2026/2026-budget-process-final-audited-results |
| **P3** | `2026-funding-pathways-reconstruction.md` + `2026-outside-hydra-actions.csv` | Intersect Budget Committee March 2 minutes: https://committees.docs.intersectmbo.org/intersect-budget-committee/committee-meeting-notes/2026-meeting-notes/budget-committee-weekly-meetings/march-2nd-2026-budget-comm-minutes ; project-specific proposal anchors |
| **P4** | `ncl-context-reconstruction.md` + `ncl-2026-withdrawal-ledger.csv` | NCL ₳500M action: https://app.cgov.io/governance/gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq ; PRIME: https://app.cgov.io/governance/gov_action122wue2k65qq8gmpz795z2axt8apka6ay6xt3pwg8jxj5yfkujmtsqvlfpu7 ; Constitution https://cardano.org/constitution/ |

## Decision

**Close Budget Process Context Register reconnaissance at v0.2 as complete enough for the HTEP sampling decision.** Keep the register available for correction if a particular historical case reveals materially different selection, administration, or NCL interpretation. Do **not** make open reconciliations automatic prerequisites for selecting cases. This closeout does not close the parent HTEP probe or its open issue.
