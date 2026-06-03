# Weekly Google Trends Surge For Warehouse Automation Layoffs Signals Labor Market Disruption

**Idea ID:** `weekly-google-trends-surge-for-warehouse-automation-layoffs-`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A weekly surge suggests layoffs related to automation adoption, signaling labor displacement risks in industrials. Industrial sector may face temporary headwinds from labor unrest and adjustment costs.

## Universe
- XLI

## Data Sources
- Google Trends weekly searches for 'warehouse automation layoffs'

## Signal Logic
Enter short XLI when weekly search interest jumps 40%+ vs prior week

## Entry / Exit
Entry: Enter short XLI when weekly search interest jumps 40%+ vs prior week Exit: Exit after 3 weeks or if interest normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'warehouse automation layoffs' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Layoff-related searches spike episodically with automation announcements or news.

## Required Keys
- None
