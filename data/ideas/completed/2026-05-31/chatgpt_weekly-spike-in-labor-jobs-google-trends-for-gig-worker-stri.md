# Weekly Spike In Labor Jobs Google Trends For Gig Worker Strike

**Idea ID:** `weekly-spike-in-labor-jobs-google-trends-for-gig-worker-stri`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising strike interest among gig economy workers signals potential labor disruptions impacting service sectors. Labor supply shocks in gig economy can reduce service availability and increase costs.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'gig worker strike'

## Signal Logic
If weekly search interest increases by 25% week-over-week

## Entry / Exit
Entry: If weekly search interest increases by 25% week-over-week Exit: When search interest falls below 10% increase for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'gig worker strike' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Gig worker labor tensions are recurring and often appear in media, driving search spikes.

## Required Keys
- None
