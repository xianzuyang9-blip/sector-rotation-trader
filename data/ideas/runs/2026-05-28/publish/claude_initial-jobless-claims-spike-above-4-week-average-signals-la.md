# Initial Jobless Claims Spike Above 4-week Average Signals Labor Weakness Rotation

**Idea ID:** `initial-jobless-claims-spike-above-4-week-average-signals-la`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly jobless claims that spike 15%+ above the 4-week moving average signal deteriorating labor market health and rising unemployment risk, triggering defensive sector rotation. Rising unemployment expectations reduce discretionary spending power; cyclical consumer sectors underperform in favor of defensive staples and utilities.

## Universe
- XLY

## Data Sources
- FRED series A4001 (Initial Claims) weekly via fred_series adapter

## Signal Logic
When weekly initial claims exceed 4-week MA by 15% and are above 52-week median

## Entry / Exit
Entry: When weekly initial claims exceed 4-week MA by 15% and are above 52-week median Exit: After 2 weeks or when claims drop below 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series A4001 (Initial Claims) weekly via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Jobless claims swing 10–20% weekly due to seasonal adjustments and economic shocks; significant spikes occur 3–5 times per year, often clustering around recessions or policy changes.

## Required Keys
- None
