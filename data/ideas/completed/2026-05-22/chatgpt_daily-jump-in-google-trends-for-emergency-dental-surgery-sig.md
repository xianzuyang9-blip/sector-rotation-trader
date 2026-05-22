# Daily Jump In Google Trends For Emergency Dental Surgery Signals Healthcare Consumer Stress

**Idea ID:** `daily-jump-in-google-trends-for-emergency-dental-surgery-sig`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A 20%+ daily increase in searches for emergency dental surgery signals rising consumer health stress. Higher health emergency search volume often precedes increased healthcare service utilization.

## Universe
- XLV

## Data Sources
- Google Trends daily data via google_trends adapter

## Signal Logic
Enter long XLV if daily search interest for emergency dental surgery > 120% previous day

## Entry / Exit
Entry: Enter long XLV if daily search interest for emergency dental surgery > 120% previous day Exit: Exit after 7 trading days or if interest falls below 110%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily data via google_trends adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Health emergency-related searches spike often due to seasonal illness or accidents.

## Required Keys
- None
