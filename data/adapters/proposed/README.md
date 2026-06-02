# Proposed Adapters

This directory is the queue for ideas that appear useful but need a new adapter
or a material adapter extension before they can be built safely.

Contract:

- one JSON file per proposal;
- grouped by run date under `data/adapters/proposed/YYYY-MM-DD/`;
- written by `scripts/final_publish_llm_gate.py` when a spec is marked
  `needs_new_adapter`;
- not a public artifact by default.

Each proposal should capture:

- `proposal_id`
- `run_date`
- `source_spec`
- `idea_id`
- `title`
- `family`
- `frequency`
- `selected_adapter`
- `routed_adapters`
- `route_confidence`
- `reason`
- `risk_flags`
- `data_sources`
- `implementation_notes`

Purpose:

- keep adapter-needing ideas out of the generic intervention pile;
- create a reviewable queue of data-access expansion opportunities;
- make it easier to distinguish "bad idea" from "good idea that needs a new adapter".
