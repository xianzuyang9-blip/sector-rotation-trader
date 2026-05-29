# Daily Jump In Google Trends For Solar Panel Installation Delay

**Idea ID:** `daily-jump-in-google-trends-for-solar-panel-installation-del`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising searches for delays in solar panel installation reflect supply chain or labor issues affecting renewable energy adoption. Energy sector ETFs with renewable exposure may face short-term headwinds from project delays.

## Universe
- XLE

## Data Sources
- Google Trends daily search interest for 'solar panel installation delay'

## Signal Logic
Enter short XLE when daily search interest spikes by more than 30% versus 7-day average

## Entry / Exit
Entry: Enter short XLE when daily search interest spikes by more than 30% versus 7-day average Exit: Exit after 5 trading days or when spike subsides below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'solar panel installation delay' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Solar project delays are frequent and receive periodic media/search attention.

## Required Keys
- None
