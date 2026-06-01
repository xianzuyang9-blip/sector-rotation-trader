# Ev Charger Installation Surge Signals Green Capex Acceleration

**Idea ID:** `ev-charger-installation-surge-signals-green-capex-accelerati`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
EV charger networks expand 5-10% quarterly as infrastructure spending accelerates. Week-over-week jumps 2%+ are rare but signal policy tailwinds or corporate expansion announcements. Tech and infrastructure plays benefit from capex acceleration in EV charging networks.

## Universe
- XLK

## Data Sources
- Open Charge Map EV charger count changes (weekly snapshots) via openchargemap adapter

## Signal Logic
If total charger count increases 2% or more week-over-week AND closes above its 8-week MA

## Entry / Exit
Entry: If total charger count increases 2% or more week-over-week AND closes above its 8-week MA Exit: After 4 weeks or once growth rate normalizes below 0.5% weekly for 2 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open Charge Map EV charger count changes (weekly snapshots) via openchargemap adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Regional rollouts and permit batches create clustering; 2%+ weeks fire 6-8 times per year.

## Required Keys
- None
