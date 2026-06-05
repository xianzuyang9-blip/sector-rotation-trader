# Used Car Price Rally Google Trends Signals Discretionary Demand Rebound

**Idea ID:** `used-car-price-rally-google-trends-signals-discretionary-dem`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sustained increases in used car searches correlate with consumers shifting away from new vehicle purchases but maintaining mobility demand, indicating stabilizing affordability perception. Used car demand strength signals consumer willingness to spend on discretionary purchases and vehicle maintenance; supports consumer cyclical rotation.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'used car prices' and 'cheap used cars near me' through google_trends adapter

## Signal Logic
If 3-week rolling average of 'used car prices' Google Trends index exceeds prior 8-week median by 25%, enter long position

## Entry / Exit
Entry: If 3-week rolling average of 'used car prices' Google Trends index exceeds prior 8-week median by 25%, enter long position Exit: Exit after 12 trading days or if index falls below 8-week median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'used car prices' and 'cheap used cars near me' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Used car search interest fluctuates weekly with inventory and price changes; high volatility ensures multiple fire events per quarter.

## Required Keys
- None
