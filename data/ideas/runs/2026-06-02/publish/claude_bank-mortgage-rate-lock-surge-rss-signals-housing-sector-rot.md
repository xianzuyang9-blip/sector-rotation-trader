# Bank Mortgage Rate Lock Surge Rss Signals Housing Sector Rotation

**Idea ID:** `bank-mortgage-rate-lock-surge-rss-signals-housing-sector-rot`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When news about mortgage financing incentives and rate locks spike, it signals builder/lender desperation to move inventory; precedes housing demand weakness. Aggressive financing promotion by builders signals slowing demand and potential price correction in residential real estate sector.

## Universe
- XLRE

## Data Sources
- RSS news feed count for 'mortgage rate lock', 'rate buydown', and 'financing incentive' announcements

## Signal Logic
When daily RSS article count for 'mortgage rate lock' or 'rate buydown' exceeds 3 articles and is above 80th percentile of 30-day rolling history, enter short XLRE

## Entry / Exit
Entry: When daily RSS article count for 'mortgage rate lock' or 'rate buydown' exceeds 3 articles and is above 80th percentile of 30-day rolling history, enter short XLRE Exit: Exit after 7 trading days or when article count falls below 1 for 3 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed count for 'mortgage rate lock', 'rate buydown', and 'financing incentive' announcements via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Builder financing promotions are announced weekly during seasonal demand windows; RSS spike frequency is 1–3 times per week.

## Required Keys
- None
