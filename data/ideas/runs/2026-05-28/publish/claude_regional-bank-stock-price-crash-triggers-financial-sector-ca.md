# Regional Bank Stock Price Crash Triggers Financial Sector Capitulation Buy Signal

**Idea ID:** `regional-bank-stock-price-crash-triggers-financial-sector-ca`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When KRE (regional banks) drops 8%+ in 2 trading days relative to XLF, it signals capitulation selling often followed by mean-reversion bounce as oversold conditions trigger value buying. Regional bank crashes create extreme valuation dislocation; buying pressure from index funds and value investors reverses declines within 5–10 trading days.

## Universe
- XLF

## Data Sources
- Yahoo Finance daily prices for regional bank ETF KRE and broad bank ETF XLF via price_only adapter

## Signal Logic
When KRE underperforms XLF by 8%+ over 2 trading days and RSI(14) on KRE closes below 30

## Entry / Exit
Entry: When KRE underperforms XLF by 8%+ over 2 trading days and RSI(14) on KRE closes below 30 Exit: After 5 trading days or when KRE outperforms XLF by 2% cumulatively

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for regional bank ETF KRE and broad bank ETF XLF via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Regional banking sector experiences 6–10% crashes 2–4 times per year during credit stress events, earnings misses, and rate shock cycles; 2-day 8%+ swings trigger monthly.

## Required Keys
- None
