# Google Trends Surge In Job Search Keywords Signals Labor Anxiety

**Idea ID:** `google-trends-surge-in-job-search-keywords-signals-labor-anx`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in job-search-related Google searches above 8-week rolling average indicate rising worker anxiety and voluntary separation risk, signaling wage pressure and consumer stress ahead. Rising job search activity precedes income disruption and consumer discretionary pullback.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'job search', 'resume writing', 'interview tips' via google_trends adapter

## Signal Logic
When job search query volume > 8-week MA × 1.15, short XLY and long XLP

## Entry / Exit
Entry: When job search query volume > 8-week MA × 1.15, short XLY and long XLP Exit: Exit after 10 trading days or when search volume returns below 8-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'job search', 'resume writing', 'interview tips' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Job search trends spike seasonally and during recession cycles; 15%+ moves occur monthly.

## Required Keys
- None
