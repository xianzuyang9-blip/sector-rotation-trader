# Healthcare Staffing Shortage Rss Spike Signals Wage Inflation In Medical Sector

**Idea ID:** `healthcare-staffing-shortage-rss-spike-signals-wage-inflatio`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily spikes in healthcare staffing shortage mentions in news feeds signal labor cost inflation, pressuring hospital margins and medical device companies. Healthcare staffing shortages raise labor costs for hospitals and clinics, compressing margins and reducing valuations for XLV healthcare providers and services.

## Universe
- XLV

## Data Sources
- RSS news feed count for 'healthcare staffing shortage' and 'nurse shortage' via rss_count adapter

## Signal Logic
If daily RSS feed count for healthcare/nurse staffing shortage doubles from 5-day average, short XLV on next open

## Entry / Exit
Entry: If daily RSS feed count for healthcare/nurse staffing shortage doubles from 5-day average, short XLV on next open Exit: Exit after 8 trading days or if RSS count returns to baseline for 3 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed count for 'healthcare staffing shortage' and 'nurse shortage' via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare staffing shortages are chronic and persistently newsworthy; RSS feed spikes occur multiple times per month.

## Required Keys
- None
