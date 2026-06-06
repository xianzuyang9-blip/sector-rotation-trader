# Corporate Bond Issuance Surge Signals Credit Confidence Reversal

**Idea ID:** `corporate-bond-issuance-surge-signals-credit-confidence-reve`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly corporate bond issuance volume doubles from prior month average. Indicates credit market confidence surge and refinancing window opening. Bond issuance surge signals credit market strength; financial and banking sectors benefit from underwriting fees and credit expansion.

## Universe
- XLF

## Data Sources
- FRED series CORPORATEINVGRADESA (weekly corporate bond issuance)

## Signal Logic
If weekly issuance > (4-week MA * 2.0), long XLF and short XLV (risk-on rotation)

## Entry / Exit
Entry: If weekly issuance > (4-week MA * 2.0), long XLF and short XLV (risk-on rotation) Exit: After 13 trading days or when issuance drops below 3-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series CORPORATEINVGRADESA (weekly corporate bond issuance) via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Corporate issuance is lumpy but structural; 2x MA surges occur 2-4 times quarterly in normal credit cycles.

## Required Keys
- None
