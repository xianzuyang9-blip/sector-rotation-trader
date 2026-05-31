# Daily Spread Widening Of Airline Sector Etf Vs Consumer Discretionary Etf

**Idea ID:** `daily-spread-widening-of-airline-sector-etf-vs-consumer-disc`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rapid underperformance of airlines relative to broad consumer discretionary signals travel sector stress or sentiment shifts. Travel mobility weakness drags on consumer discretionary demand.

## Universe
- XLY

## Data Sources
- Yahoo Finance daily prices for JETS and XLY ETFs

## Signal Logic
If JETS underperforms XLY by more than 3% intraday

## Entry / Exit
Entry: If JETS underperforms XLY by more than 3% intraday Exit: When JETS recovers to within 1% relative performance

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for JETS and XLY ETFs via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Airline stocks frequently diverge intra-month due to travel shocks and news flow.

## Required Keys
- None
