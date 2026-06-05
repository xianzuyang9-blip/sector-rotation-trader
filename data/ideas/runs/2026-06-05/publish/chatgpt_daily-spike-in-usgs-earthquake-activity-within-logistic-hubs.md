# Daily Spike In Usgs Earthquake Activity Within Logistic Hubs Signals Short-term Freight Disruptions

**Idea ID:** `daily-spike-in-usgs-earthquake-activity-within-logistic-hubs`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Earthquake activity near major freight hubs often causes short-term disruptions in supply chains and logistics flows. Industrial sector freight and logistics companies face operational slowdowns reducing earnings expectations.

## Universe
- XLI

## Data Sources
- USGS earthquake daily activity counts near major US freight hubs

## Signal Logic
Enter short XLI when daily earthquake events within 50km of top 5 US ports or rail hubs spike 50% above 30-day average

## Entry / Exit
Entry: Enter short XLI when daily earthquake events within 50km of top 5 US ports or rail hubs spike 50% above 30-day average Exit: Exit after 7 trading days or once event frequency normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake daily activity counts near major US freight hubs via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic events near freight hubs occur intermittently but frequently enough to trigger signals multiple times per year.

## Required Keys
- None
