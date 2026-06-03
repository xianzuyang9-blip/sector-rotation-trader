# Restaurant Job Postings Surge Signals Consumer Services Demand Recovery

**Idea ID:** `restaurant-job-postings-surge-signals-consumer-services-dema`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly restaurant/hospitality job postings jump >20% sequentially, it signals rising consumer dining/travel demand and labor market tightness in services. Hospitality job growth foreshadows consumer discretionary spending strength and pricing power for service businesses.

## Universe
- XLY

## Data Sources
- HTML table scrape from Indeed job postings (restaurant/hospitality category) weekly snapshot through html_table adapter

## Signal Logic
If weekly restaurant/hospitality job posting count rises >18% week-over-week AND is above the 12-week moving average

## Entry / Exit
Entry: If weekly restaurant/hospitality job posting count rises >18% week-over-week AND is above the 12-week moving average Exit: After 3 weeks or if weekly postings drop >10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use HTML table scrape from Indeed job postings (restaurant/hospitality category) weekly snapshot through html_table adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal hiring cycles, holiday/summer demand swings, and staffing shortages trigger job posting spikes multiple times per year.

## Required Keys
- None
