# HTEP-001 — Catalyst Evidence Landscape: C1 and C3 (v0.1)

**Research snapshot:** 2026-11-03. **Status:** bounded reconnaissance; no Catalyst project-level ingestion performed.  
**Purpose:** establish historical funding-round population (C1) and discover which classes of evidence can be retrieved (C3), before selecting HTEP cases.

## C1 — What rounds actually occurred?

The official Catalyst fund pages identify **13 grant-awarding rounds, Funds 2–14**, totaling **2,221 funded proposals**. The arithmetic of individual official page counts reconciles exactly to the official aggregate. **Fund 0** was an internal trial; **Fund 1** was a non-funding community test. Neither belongs in the population of grant awards. A separate **Pilot 2026** selected 12 projects through a different mechanism. Fund 15 is still displayed as active on one official page, but contemporary transition announcements establish the planned round did not proceed and no awards are recorded. Fund 16 did not proceed in its planned form.

| Round | Awarded | Completed | In progress | Did not finish |
|---|---:|---:|---:|---:|
| [Fund 2](https://projectcatalyst.io/funds/2) | 11 | 9 | 0 | 2 |
| [Fund 3](https://projectcatalyst.io/funds/3) | 21 | 16 | 0 | 5 |
| [Fund 4](https://projectcatalyst.io/funds/4) | 51 | 40 | 0 | 11 |
| [Fund 5](https://projectcatalyst.io/funds/5) | 69 | 59 | 0 | 10 |
| [Fund 6](https://projectcatalyst.io/funds/6) | 151 | 122 | 0 | 29 |
| [Fund 7](https://projectcatalyst.io/funds/7) | 264 | 217 | 0 | 47 |
| [Fund 8](https://projectcatalyst.io/funds/8) | 367 | 306 | 0 | 61 |
| [Fund 9](https://projectcatalyst.io/funds/9) | 207 | 178 | 0 | 29 |
| [Fund 10](https://projectcatalyst.io/funds/10) | 192 | 173 | 0 | 19 |
| [Fund 11](https://projectcatalyst.io/funds/11) | 300 | 246 | 32 | 22 |
| [Fund 12](https://projectcatalyst.io/funds/12) | 258 | 193 | 34 | 31 |
| [Fund 13](https://projectcatalyst.io/funds/13) | 199 | 143 | 32 | 24 |
| [Fund 14](https://projectcatalyst.io/funds/14) | 131 | 70 | 47 | 14 |
| **Funds 2–14, sum of displayed round pages** | **2,221** | **1,772** | **145** | **304** |

### Data quality and round-status caution

The **awarded counts reconcile exactly** to 2,221. However, the sum of the round-level published statuses **does not** reconcile with the aggregate dashboard: rounds display 1,772 completed vs 1,784 aggregate; 145 in progress vs 127 aggregate; and 304 did-not-finish vs 310 aggregate. Fund 14 also displays 70 complete + 47 in progress + 3 onboarding + 14 did-not-finish = 134 statuses despite only 131 awarded. These are discrepancies in publicly displayed data and/or update cadence, not grounds to silently alter round records. Project-level counts must be reverified at sampling time.

Another distinction: **fund-level requested or budgeted amounts** (sometimes USD converted at fund results, sometimes ADA) are not the same as the amount disbursed or actually spent by a project. Do not sum unlike monetary units or use historical conversion figures as normative cost rates.

### Boundaries

- Fund 0: internal trial with no comparable grant awards; original infrastructure claims (including Jörmungandr) are outside this round census and not independently verified here.
- Fund 1: non-funding community pilot with ballot proposals (not zero proposals).
- Funds 2–14: grant-awarding rounds; their awards are downstream institutional allocations, **not individually enacted CIP-1694 Treasury Withdrawals**.
- Fund 15 and proposed Fund 16: discontinued original plans, not an additional completed grant cohort.
- Pilot 2026: a separate curated selection mechanism with 12 selected projects. Do not add these 12 to the 2,221 historical fund awards without verifying official aggregate scope.

## C3 — Where does usable evidence survive?

| Evidence need | Best current entry point | Present assessment |
|---|---|---|
| Round-level award population | Official fund pages | **High discovery confidence**, subject to mutable status summaries |
| Original proposal and budget | Official project/search pages; CatalystExplorer API | **Likely recoverable** for many rounds; historical version preservation untested |
| Funding decision / vote | Official proposal result pages; third-party API | **Present in published results**; underlying ballots/independent reconstruction untested |
| Milestone, proof of achievement, payments | Milestone Module | **Directly observed** for Fund 9 and Fund 14 and Pilot; pre-F9 coverage unresolved |
| Administrative rules at decision time | Knowledge Base / contemporary fund rules | **Available**, but must match the specific round version |
| Cross-round project/organization histories | Proposal IDs, team metadata, references | **Feasible candidate**, not tested longitudinally yet |
| Original treasury transfers | Separate ledger/administration evidence | **Not established** in this survey; keep apart from awarded budgets |
| Actual project expenditure / verified public value | External delivery evidence, ledgers, audited reports | **Not implied** by grant approval, module distribution, or completion status |

A directly accessible Fund 14 Milestone Module page exposes milestone plan, project budget, funds distributed, and a module warning about its allocated milestone budget. This proves both the *value* of the module and the need to preserve source-specific incompleteness. See `c3-source-atlas.csv` for the exact public URLs, observations, and limits.

### Interpretive caution

- **Project 'Completed'** means an administrative status, not independently established impact or spending efficiency.
- **Funds distributed** means reported grant transfers, not verified grantee expenditure.
- **Funded proposal** means a downstream grant selection, not a separate protocol treasury withdrawal.
- **Availability** is not historical completeness. A current project page may have changed since the award decision.
- **No public voting** for Pilot 2026 does not mean no review or public application process.

## Stopping condition and immediate next step

**C1 is sufficiently established** for HTEP case selection: the distinct historical award rounds and the Pilot boundary are identified and the award counts reconcile. **C3 is sufficient for selecting targeted recovery tests**, not for claiming that milestones or original proposal versions are complete across eras.

Select **3–4 deliberately contrasting Catalyst records**: one early Fund 2–4 grant; one Fund 7–8 grant; one completed Fund 10–12 grant with visible milestone/PoA detail; and, only if useful, a repeated recipient or Pilot boundary case. Record source-link success, amount type, missingness, and retrieval burden. Stop when differences relevant to HTEP P1–P5 are visible.

Do not ingest 2,221 proposals or reconcile the entire treasury transfer history as a prerequisite.

## Public sources

- Official all-funds overview: https://projectcatalyst.io/funds
- Round pages: https://projectcatalyst.io/funds/{2..14}
- IOG earliest experimental rounds: https://www.iog.io/news/project-catalyst-introducing-our-first-public-fund-for-cardano-community-innovation
- Milestone Module: https://milestones.projectcatalyst.io/projects
- Example live milestones: https://milestones.projectcatalyst.io/projects/1400078/milestones/1
- CatalystExplorer API: https://www.catalystexplorer.com/docs/
- Transition summary: https://cardano.org/glossary/project-catalyst/
- Pilot selection report: https://projectcatalyst.io/blog/meet-the-12-teams-selected-for-the-catalyst-pilot-2026

**Corpus boundary:** these files are Observatory reconnaissance, not a raw snapshot of Project Catalyst's API. Preserve exact sources and provenance when a Catalyst case is selected for formal evidence ingestion.
