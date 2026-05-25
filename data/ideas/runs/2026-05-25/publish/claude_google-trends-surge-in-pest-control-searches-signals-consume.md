# Google Trends Surge In Pest Control Searches Signals Consumer Home Stress

**Idea ID:** `google-trends-surge-in-pest-control-searches-signals-consume`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Surges in pest control search interest often spike in spring and fall, signaling homeowner stress and reactive spending on home maintenance. Consumer discretionary home services and maintenance spending correlates with confidence; pest control searches precede broader home improvement cycles.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'pest control near me' and 'termite treatment'

## Signal Logic
When weekly Google Trends index for pest control searches exceeds 70 (on 0–100 scale) and increases >20 points week-over-week

## Entry / Exit
Entry: When weekly Google Trends index for pest control searches exceeds 70 (on 0–100 scale) and increases >20 points week-over-week Exit: After 14 trading days or when index falls below 55

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'pest control near me' and 'termite treatment' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal pest activity spikes occur reliably in spring (March–May) and fall (August–October), generating predictable signals multiple times per year.

## Required Keys
- None
