# Daily Spike In Rss Counts For New Labor Union Formations Signals Labor Market Shift

**Idea ID:** `daily-spike-in-rss-counts-for-new-labor-union-formations-sig`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased news flow about new labor unions correlates with rising labor activism and potential wage pressure. Financials and industrials face margin pressure and uncertainty with rising union activity increasing labor costs.

## Universe
- XLF

## Data Sources
- RSS/news feed counts

## Signal Logic
If daily RSS counts for 'new labor union' news rise 40% above 30-day average

## Entry / Exit
Entry: If daily RSS counts for 'new labor union' news rise 40% above 30-day average Exit: After 14 days or when news counts normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS/news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor organizing surges happen with regular news cycles and union drives.

## Required Keys
- None
