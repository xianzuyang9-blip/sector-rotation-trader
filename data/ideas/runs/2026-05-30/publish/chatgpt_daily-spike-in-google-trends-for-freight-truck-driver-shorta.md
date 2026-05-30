# Daily Spike In Google Trends For Freight Truck Driver Shortage Signals Industrial Sector Bottleneck

**Idea ID:** `daily-spike-in-google-trends-for-freight-truck-driver-shorta`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising search interest on driver shortage reflects labor constraints in freight logistics, often leading to shipping delays. Labor shortages in logistics can reduce industrial throughput and pressure industrial sector earnings.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest for 'freight truck driver shortage'

## Signal Logic
If daily Google Trends for 'freight truck driver shortage' increases by more than 20% compared to prior 5-day average

## Entry / Exit
Entry: If daily Google Trends for 'freight truck driver shortage' increases by more than 20% compared to prior 5-day average Exit: Exit after 7 trading days or when the search interest falls below the 5-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'freight truck driver shortage' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor shortage concerns in freight logistics are a frequent news and search topic.

## Required Keys
- None
