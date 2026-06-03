# Daily Jump In Google Trends For Holiday Travel Cancellations Signals Consumer Travel Stress

**Idea ID:** `daily-jump-in-google-trends-for-holiday-travel-cancellations`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sharp increases in cancellation-related travel searches indicate rising consumer travel anxiety and potential demand shock. Consumer discretionary travel and leisure stocks are sensitive to sudden travel disruption signals.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily Google Trends for 'holiday travel cancellations' rises by 20%+ compared to 7-day average

## Entry / Exit
Entry: If daily Google Trends for 'holiday travel cancellations' rises by 20%+ compared to 7-day average Exit: Exit after 7 calendar days or when searches decline below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Holiday travel windows often produce measurable cancellation search spikes as plans change.

## Required Keys
- None
