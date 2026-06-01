# Mortgage Rate Spike Collapses Housing Demand Sentiment

**Idea ID:** `mortgage-rate-spike-collapses-housing-demand-sentiment`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Mortgage rates move 20-40bps weekly on Fed expectations and bond yields. A 3-day spike of 30bps+ collapses homebuilder and real estate confidence almost immediately. Real estate equities tank when financing costs jump; homebuilders face demand collapse within days.

## Universe
- XLRE

## Data Sources
- FRED series MORTGAGE30US (30-Year Fixed Mortgage Rate) via fred_series adapter

## Signal Logic
If 30Y mortgage rate rises 30bps or more over 3 consecutive trading days and closes above its 20-day MA

## Entry / Exit
Entry: If 30Y mortgage rate rises 30bps or more over 3 consecutive trading days and closes above its 20-day MA Exit: After 5 trading days or once rates fall 20bps from entry peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MORTGAGE30US (30-Year Fixed Mortgage Rate) via fred_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 60
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Bond market volatility ensures 30bps+ 3-day moves occur 4-6 times per quarter.

## Required Keys
- None
