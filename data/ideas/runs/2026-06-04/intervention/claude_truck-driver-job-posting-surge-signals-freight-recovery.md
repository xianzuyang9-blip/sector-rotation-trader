# Truck Driver Job Posting Surge Signals Freight Recovery

**Idea ID:** `truck-driver-job-posting-surge-signals-freight-recovery`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sudden increases in truck driver job postings often coincide with seasonal shipping surges and freight demand acceleration, preceding freight index improvements. Freight sector hiring signals near-term shipping volume pickup and industrial transportation demand; benefits logistics and industrial equipment manufacturers.

## Universe
- XLI

## Data Sources
- RSS feed count spike for 'truck driver jobs hiring' from job boards and news aggregators through rss_count adapter

## Signal Logic
If weekly RSS count for 'truck driver jobs' increases by 50% or more versus prior week, enter long position

## Entry / Exit
Entry: If weekly RSS count for 'truck driver jobs' increases by 50% or more versus prior week, enter long position Exit: Exit after 8 trading days or if RSS count returns to prior 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count spike for 'truck driver jobs hiring' from job boards and news aggregators through rss_count adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Job posting volume is highly sensitive to seasonal shipping patterns and unexpected demand surges; fires 1-2 times per week on average.

## Required Keys
- None
