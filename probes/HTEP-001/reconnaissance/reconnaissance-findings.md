# HTEP-001 — TWD Population and Epoch Distribution: First Findings

**Snapshot:** Koios `/api/v1/proposal_list`, retrieved 2026-11-03T20:42:44.166123+00:00, chain tip epoch 665.  
**Unit:** one distinct TreasuryWithdrawals governance action ID, not one recipient, project, or funding initiative.  
**Inputs:** `koios-proposal-list-raw.json` (separately preserved), `build_twd_inventory.py`.  
**Output regeneration:** `python build_twd_inventory.py --from-raw /path/to/koios-proposal-list-raw.json`.

## Reconciliation

The 162 governance actions contain 107 unique TreasuryWithdrawals: 70 enacted, 34 expired, 3 active/unresolved. The enacted withdrawal amounts sum to **804,427,136 ADA**. CSV action IDs are unique; action withdrawal amounts reconcile to Koios `withdrawal` entries. Two actions include five recipients each; the other 105 include one recipient each. 106 TWD records have a title; one does not.

The originally uploaded `twd-summary.json` was generated from an offline bare-array export and reports an unknown retrieval timestamp, null chain tip and endpoint epoch 662; the accompanying epoch CSV contains rows through epoch 665. Regeneration from the preserved timestamped Koios wrapper yields **identical action and epoch CSVs** and fixes this metadata discrepancy. Use the regenerated `twd-summary.json` alongside them.

## Submission distribution

- Earliest submitted TWD: epoch 566; latest: epoch 662.
- Observation interval: epochs 537–665 inclusive (129 epochs); 33 contain one or more TWD submissions and 96 have none.
- Within the actual submission span (epochs 566–662 inclusive, 97 epochs), 33 epochs have submissions and 64 have none.
- Epoch 570 has **39 submissions** (36.45% of the entire population), with 37 eventually enacted and two expired.
- Next busiest: epoch 638 (11 submissions) and epoch 626 (9). The three busiest epochs contain 59 actions (55.14% of the total).
- The mean over the 97-epoch submission span is 1.103 actions/epoch, but this is misleading as a description of typical activity. Excluding epoch 570, the other 68 submissions average 0.708 per epoch over the remaining 96 epochs.
- For epochs 566–612 inclusive, 46 actions were submitted, 39 in epoch 570. For epochs 613–665, 61 actions were submitted, 47 in epochs 626–640. These ranges are useful exploratory contrasts, not homogeneous causal regimes.

## Enactment distribution

- Earliest enacted TWD: epoch 571; latest enacted epoch present in the snapshot: epoch 650.
- All 70 enacted actions have an `enacted_epoch`. Enactment epochs must not be mixed with submission epochs.
- Largest enactment-action count is epoch 576: 27 enacted actions; the largest recorded enactment-ADA epoch is epoch 575: 168,438,176 ADA from three actions.
- Snapshot outcomes are not historical status-at-submission, and the 3 currently unresolved records are right-censored. Do not interpret a cohort's current enactment fraction as a fully matured approval probability.

## Evidentiary limitations and next steps

1. Audit the complete action-ID roster, metadata completeness and per-recipient withdrawal semantics independently if publication demands it; this snapshot reconciles internally but is not an independent second-node verification.
2. Map the pronounced submission clusters (particularly epochs 570, 626 and 638) to budget cohorts and process context, **without inferring causation from timing alone**.
3. Start resubmission/initiative linkage as a separate layer; same recipient or similar title does not prove identity.
4. Inventory rationale/vote availability separately. The `meta_json.body.rationale` field in this dataset is a **proposer's action rationale**, not a DRep vote rationale.
5. Preserve raw source, retrieval timestamp, chain-tip epoch, script version and transformations in the Evidence Corpus. The epoch CSV is a derived dataset, not a source-of-truth record.
