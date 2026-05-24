# Healthcare Cost Urgency Spike

**Idea ID:** `healthcare-cost-urgency-spike`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in cost-assistance searches signal consumer healthcare distress and predict outpatient utilization drops and insurance margin pressure. Rising cost-assistance searches indicate affordability stress; healthcare providers repricing margins and utilization.

## Universe
- XLV

## Data Sources
- Google Trends weekly search interest for 'prescription drug cost assistance' + 'medical debt relief'

## Signal Logic
If combined search index rises >20% WoW

## Entry / Exit
Entry: If combined search index rises >20% WoW Exit: After 11 trading days or when index falls >15% from spike peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'prescription drug cost assistance' + 'medical debt relief' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Drug pricing news and healthcare policy announcements fire weekly spikes; threshold is accessible 2–4 times per month.

## Required Keys
- None
