# Weekly Surge In Google Trends For Tech Stock Selloff Signals Rotation To Defensive Sectors

**Idea ID:** `weekly-surge-in-google-trends-for-tech-stock-selloff-signals`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A 30%+ weekly increase in search interest for tech stock selloff indicates growing market risk aversion. Rotation from tech to consumer staples is common during risk-off market environments.

## Universe
- XLP

## Data Sources
- Google Trends weekly data via google_trends adapter

## Signal Logic
Enter long XLP if weekly search interest for 'tech stock selloff' > 130% of prior week

## Entry / Exit
Entry: Enter long XLP if weekly search interest for 'tech stock selloff' > 130% of prior week Exit: Exit after 6 weeks or if interest falls below 110%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Market sentiment searches fluctuate with volatility and sector rotations.

## Required Keys
- None
