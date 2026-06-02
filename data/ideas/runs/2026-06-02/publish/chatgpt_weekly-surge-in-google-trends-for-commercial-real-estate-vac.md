# Weekly Surge In Google Trends For Commercial Real Estate Vacancy Signals Xlre Weakness

**Idea ID:** `weekly-surge-in-google-trends-for-commercial-real-estate-vac`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising weekly interest in commercial vacancy indicates growing concern over CRE fundamentals and tenant risk. Real estate sector ETFs suffer from increased vacancy and rental income pressure.

## Universe
- XLRE

## Data Sources
- Google Trends weekly search interest for 'commercial real estate vacancy'

## Signal Logic
Enter short XLRE if weekly search interest rises 25%+ vs prior week

## Entry / Exit
Entry: Enter short XLRE if weekly search interest rises 25%+ vs prior week Exit: Exit after 4 weeks or if interest declines below baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'commercial real estate vacancy' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: CRE vacancy concerns tend to rise in waves, frequently captured in weekly trend data.

## Required Keys
- None
