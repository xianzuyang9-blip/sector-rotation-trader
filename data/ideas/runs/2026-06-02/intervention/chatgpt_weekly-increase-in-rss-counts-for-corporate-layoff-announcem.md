# Weekly Increase In Rss Counts For Corporate Layoff Announcements Signals Labor Market Stress

**Idea ID:** `weekly-increase-in-rss-counts-for-corporate-layoff-announcem`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A weekly surge in layoff news signals deteriorating labor conditions and potential economic slowdown. Financials tend to weaken as economic and labor headwinds build.

## Universe
- XLF

## Data Sources
- RSS news count for 'corporate layoff announcements'

## Signal Logic
Enter short XLF if weekly layoff announcements double versus prior week

## Entry / Exit
Entry: Enter short XLF if weekly layoff announcements double versus prior week Exit: Exit after 4 weeks or if news counts revert to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news count for 'corporate layoff announcements' via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Layoff news surges cluster with economic cycles and are visible in weekly news flows.

## Required Keys
- None
