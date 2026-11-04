# HTEP-001 TWD Relationship Discovery v0.1

Bounded exploratory relationship study based on the **November 3, 2026 Koios proposal-list snapshot** already deposited in the Treasury Evidence Corpus.

## Contents

- `twd-relationship-discovery.md` — method, findings, evidence limits, stopping rule.
- `twd-relationship-candidates.csv` — 16 directional, individually sourced propositions, 11 supported by proposer metadata and 5 candidates.
- `twd-relationship-coverage.csv` — one row for each of 107 TWD actions; presence means included in *this curated set*, not relationship completeness.
- `discovery-summary.json` — machine-readable scope check.
- `build_relationship_discovery.py` — offline reproducible generation script with explicitly curated relationship pairs.

## Regeneration

Save `koios-proposal-list-raw.json` from the existing dated Koios Corpus package in the **same directory**, then run:

```bash
python build_relationship_discovery.py koios-proposal-list-raw.json
```

The raw Koios file is **not duplicated in this package**; it belongs to the dated Corpus snapshot. The script creates the two CSVs and summary alongside itself. It neither fetches new data nor changes the 107-action inventory.

This is research material for the Observatory. The word `supported` refers to text appearing in proposal metadata; it does not mean independently adjudicated or verified beyond the snapshot.
