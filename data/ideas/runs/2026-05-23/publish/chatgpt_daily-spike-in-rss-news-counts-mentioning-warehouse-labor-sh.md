# Daily Spike In Rss News Counts Mentioning Warehouse Labor Shortage Signals Xli Downside

**Idea ID:** `daily-spike-in-rss-news-counts-mentioning-warehouse-labor-sh`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising news counts on warehouse labor shortages indicate operational challenges in industrial sector supply chains. Labor shortages reduce throughput and increase costs in industrials.

## Universe
- XLI

## Data Sources
- RSS news feed daily counts for 'warehouse labor shortage'

## Signal Logic
Enter short XLI if daily RSS news counts for 'warehouse labor shortage' rise by 40% over 3-day average

## Entry / Exit
Entry: Enter short XLI if daily RSS news counts for 'warehouse labor shortage' rise by 40% over 3-day average Exit: Exit after 5 trading days or when counts fall below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed daily counts for 'warehouse labor shortage' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Warehouse labor shortage news often spikes due to demand surges and hiring challenges.

## Required Keys
- None
