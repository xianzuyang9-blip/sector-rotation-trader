# Healthcare Cost Search Spike Signals Staples Defensive Rotation

**Idea ID:** `healthcare-cost-search-spike-signals-staples-defensive-rotat`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in healthcare cost searches correlate with consumer anxiety about out-of-pocket expenses and signal rotation from discretionary to defensive sectors. Rising healthcare cost concerns drive flight-to-safety; staples sectors benefit as consumers prioritize essential spending and healthcare-linked defensive plays.

## Universe
- XLP

## Data Sources
- Google Trends weekly search volume for 'health insurance deductible' and 'prescription drug costs' through google_trends adapter

## Signal Logic
If weekly Google Trends index for 'health insurance deductible' exceeds prior 8-week median by 45%, enter long position in XLP

## Entry / Exit
Entry: If weekly Google Trends index for 'health insurance deductible' exceeds prior 8-week median by 45%, enter long position in XLP Exit: Exit after 9 trading days or if search index falls below 8-week median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'health insurance deductible' and 'prescription drug costs' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare cost anxiety spikes around open enrollment periods and pharmaceutical price announcements; fires 2-3 times per quarter.

## Required Keys
- None
