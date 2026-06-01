# Weekly Surge In Google Trends For Solar Panel Malfunction Signals Green Energy Sector Tech Stress

**Idea ID:** `weekly-surge-in-google-trends-for-solar-panel-malfunction-si`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased searches for solar panel malfunctions indicate technical or supply issues in renewable energy equipment. Solar panel tech issues can pressure renewable energy companies within energy sector ETFs.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest for 'solar panel malfunction'

## Signal Logic
Enter short XLE if weekly search interest rises 25% above 6-week average

## Entry / Exit
Entry: Enter short XLE if weekly search interest rises 25% above 6-week average Exit: Exit after 3 weeks or if interest falls below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'solar panel malfunction' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Equipment malfunctions in solar frequently spike due to weather or manufacturing recalls.

## Required Keys
- None
