# HTEP-001 — TWD population reconnaissance

**State:** source-confirmed population summary; full action-level extraction **not yet run or verified**.

**Observation date:** 2026-11-03. Available third-party Koios-derived indexes report 107 Treasury Withdrawal governance actions: 70 enacted, 34 not approved, 3 live; enacted withdrawals total approximately 804,427,136 ADA. Public indexes are snapshots and should be reconciled with the direct chain-indexed export.

**Sources**
- https://realtap.app/governance/treasury
- https://supercardano.com/governance?view=treasury
- https://www.koios.rest/api.html
- https://cardano.org/insights/supply/summary/

## Extraction

Run `python build_twd_inventory.py` in a Python 3 environment with public Internet access. The script queries Koios `/proposal_list`, saves the raw response alongside `twd-actions.csv` (one row per governance action) and `twd-by-epoch.csv` (one row per epoch, including zero-action epochs), and a count audit.

**Important:** This script has been syntax-checked but **not live-tested** against Koios in the creation environment because outbound access to Koios was unavailable. Validate its output and schema mapping before accepting a Corpus contribution. The third-party totals are checks, not values to force into the results. In particular, the source indexes may classify dropped actions differently.

The raw response is preserved so action statuses and submission-epoch mappings can be independently checked. The epoch distribution must be built from `proposed_epoch`, **not** `enacted_epoch`. Both appear in the output, separately.

## Questions left open

- First observed TWD **submission** epoch (distinct from earliest enactment epoch 566).
- Counts per submitted epoch, zero-activity epochs and burstiness metrics.
- Verification of unique action IDs and any excluded or discrepant actions.
- Resubmission and initiative-level relationships (deliberately out of scope for this first extraction).
