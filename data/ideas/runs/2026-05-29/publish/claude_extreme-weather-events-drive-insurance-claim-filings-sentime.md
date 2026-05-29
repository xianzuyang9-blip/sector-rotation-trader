# Extreme Weather Events Drive Insurance Claim Filings Sentiment

**Idea ID:** `extreme-weather-events-drive-insurance-claim-filings-sentime`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Severe weather events trigger spikes in insurance claim-related news and search volume, creating short-term volatility in insurance and reinsurance equities. Extreme weather events create catastrophic loss exposure for insurers, suppressing stock prices ahead of earnings adjustments.

## Universe
- XLF

## Data Sources
- Open-Meteo weather API (daily severe weather alerts, hail, tornado, flood risk) + RSS news count for 'insurance claim surge'

## Signal Logic
When daily severe weather alerts (tornado, hail, flood) exceed 10 events nationally AND insurance claim news mentions spike 60%+

## Entry / Exit
Entry: When daily severe weather alerts (tornado, hail, flood) exceed 10 events nationally AND insurance claim news mentions spike 60%+ Exit: After 3 trading days or when weather alerts drop below 3 daily events

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo weather API (daily severe weather alerts, hail, tornado, flood risk) + RSS news count for 'insurance claim surge' via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Severe weather clusters occur 2–4 times per quarter during seasonal storm seasons, especially spring and fall.

## Required Keys
- None
