# Weekly Surge In Google Trends For Diy Home Repair Kit Searches

**Idea ID:** `weekly-surge-in-google-trends-for-diy-home-repair-kit-search`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in DIY kits reflects consumer cost-cutting and home maintenance stress. Consumer discretionary benefits from increased sales of home repair and improvement products.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'DIY home repair kit'

## Signal Logic
If weekly searches rise 20% above 8-week average

## Entry / Exit
Entry: If weekly searches rise 20% above 8-week average Exit: When searches fall below 10% increase for 2 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'DIY home repair kit' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: DIY interest fluctuates seasonally and with economic stress, generating repeatable spikes.

## Required Keys
- None
