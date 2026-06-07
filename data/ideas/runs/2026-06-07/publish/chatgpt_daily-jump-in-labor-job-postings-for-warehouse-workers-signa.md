# Daily Jump In Labor Job Postings For Warehouse Workers Signals Industrial Sector Hiring Surge

**Idea ID:** `daily-jump-in-labor-job-postings-for-warehouse-workers-signa`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A rapid increase in warehouse job postings indicates rising industrial logistics demand. Growing warehouse employment reflects industrial sector expansion and supply chain activity.

## Universe
- XLI

## Data Sources
- Public job posting API scrape for warehouse sector

## Signal Logic
If daily warehouse job postings increase by 15% compared to 5-day moving average

## Entry / Exit
Entry: If daily warehouse job postings increase by 15% compared to 5-day moving average Exit: When postings revert below 5% increase compared to 5-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Public job posting API scrape for warehouse sector via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Warehouse labor demand fluctuates with supply chain bottlenecks and seasonal needs.

## Required Keys
- None
