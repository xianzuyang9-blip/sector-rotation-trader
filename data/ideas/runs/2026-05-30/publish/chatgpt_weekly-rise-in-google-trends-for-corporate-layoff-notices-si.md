# Weekly Rise In Google Trends For Corporate Layoff Notices Signals Labor Market Stress

**Idea ID:** `weekly-rise-in-google-trends-for-corporate-layoff-notices-si`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing search interest on layoffs signals rising labor market stress and potential earnings pressure on cyclical sectors. Consumer discretionary stocks are sensitive to job losses and lower consumer spending.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'corporate layoff notices'

## Signal Logic
If weekly search interest increases more than 25% compared to 4-week average

## Entry / Exit
Entry: If weekly search interest increases more than 25% compared to 4-week average Exit: Exit after 6 weeks or when interest drops below 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'corporate layoff notices' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Layoff discussions surge with economic cycles and corporate earnings reports.

## Required Keys
- None
