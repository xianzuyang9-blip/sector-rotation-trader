# Daily Spike In Google Trends For Warehouse Worker Strike Signals Labor Disruption In Industrials

**Idea ID:** `daily-spike-in-google-trends-for-warehouse-worker-strike-sig`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased search interest for warehouse strikes signals imminent labor disruptions impacting supply chains. Warehouse labor strikes slow industrial logistics and manufacturing output, pressuring industrial sector earnings.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest for 'warehouse worker strike'

## Signal Logic
If daily Google Trends interest spikes more than 40% compared to previous day

## Entry / Exit
Entry: If daily Google Trends interest spikes more than 40% compared to previous day Exit: After 7 trading days or when interest normalizes below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'warehouse worker strike' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor unrest and strike news often appear in bursts, causing daily spikes in related search terms.

## Required Keys
- None
