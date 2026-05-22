# Weekly Spike In Google Trends For Warehouse Labor Shortage Signals Industrial Labor Stress

**Idea ID:** `weekly-spike-in-google-trends-for-warehouse-labor-shortage-s`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A 25%+ increase in weekly search interest for warehouse labor shortage reflects tight labor supply in industrial logistics. Labor shortages constrain industrial output and slow supply chains, pressuring industrial stocks.

## Universe
- XLI

## Data Sources
- Google Trends weekly search data via google_trends adapter

## Signal Logic
Enter short XLI if weekly warehouse labor shortage interest > 125% of prior week

## Entry / Exit
Entry: Enter short XLI if weekly warehouse labor shortage interest > 125% of prior week Exit: Exit after 3 weeks or if interest drops below 110%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search data via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor shortage concerns often arise quickly with changing labor market conditions.

## Required Keys
- None
