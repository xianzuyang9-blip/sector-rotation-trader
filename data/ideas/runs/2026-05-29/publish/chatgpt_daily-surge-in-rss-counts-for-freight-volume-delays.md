# Daily Surge In Rss Counts For Freight Volume Delays

**Idea ID:** `daily-surge-in-rss-counts-for-freight-volume-delays`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spike in news mentions of freight delays signals supply chain disruptions increasing input costs and inventory pressure. Industrial sector is directly impacted by logistic delays increasing operational costs and slowing production.

## Universe
- XLI

## Data Sources
- RSS news feed counts mentioning 'freight delay' or 'shipping backlog'

## Signal Logic
Enter short XLI on a daily RSS count increase of more than 30% compared to 5-day average

## Entry / Exit
Entry: Enter short XLI on a daily RSS count increase of more than 30% compared to 5-day average Exit: Exit after 7 trading days or when RSS counts fall below 10% above 5-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts mentioning 'freight delay' or 'shipping backlog' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily news cycles often report freight disruptions multiple times per month.

## Required Keys
- None
