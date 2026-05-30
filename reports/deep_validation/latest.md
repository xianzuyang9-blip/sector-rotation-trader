# Deep Validation Report - 2026-05-29

## Definitions
- force_rank: Full-window/since-seed rank from data/rank_history.csv. Use for long-term trust, promotion, demotion, and kill review.
- rolling_30d: Recent trailing 30-day return rank from docs/leaderboards/rolling_30d.json. Use for tactical spotlight and recent momentum.
- sector_consensus: Precomputed sector verdicts from docs/signals/index.json. Use for current directional sector context.

## System State
- Force-ranked algos: 374 rows (374 unique algo_ids)
- Force-ranked beating SPY: 1 of 374 rows
- Rolling 30D algos: 375 rows (375 unique algo_ids)
- Rolling 30D beating SPY: 4 of 375 rows
- Signals generated: 374
- Tickers covered: 105
- Sectors computed: 11

## Data Hygiene
- Force-rank duplicate rows: 0
- Rolling 30D duplicate rows: 0
- Rolling-only algo_ids with no force-rank row: 1

## Force Rank
Full-window/since-seed rank; not the same as recent 30D performance.

### Top 10
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 1 | Quantified Simple Monthly Rotation | normal | +12.42% | +1.39% | +0 |
| 2 | Algo Baileymol (Chaos Monger) | normal | +8.16% | -2.87% | +0 |
| 3 | Retail Sales Momentum | crazy | +7.97% | -3.06% | +2 |
| 4 | Job Posting Acceleration | crazy | +6.18% | -4.86% | +2 |
| 5 | Faber Momentum Rotation | normal | +6.15% | -4.89% | -2 |
| 6 | Antonacci Dual Momentum Sector Rotation | normal | +5.47% | -5.56% | -2 |
| 7 | Uber Mobility Index | crazy | +3.22% | -7.81% | +0 |
| 8 | VIX Term Structure | crazy | +2.38% | -8.65% | +1 |
| 9 | Housing Permit Velocity | crazy | +1.22% | -9.81% | -1 |
| 10 | VIX Fear Rotation | crazy | +0.58% | -10.46% | +360 |

### Bottom 5
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 370 | Consumer Sentiment | crazy | -1.53% | -12.56% | -33 |
| 371 | FINRA Dark Pool Signal | crazy | -1.80% | -12.83% | -10 |
| 372 | Liquor Store Leading Indicator | crazy | -2.14% | -13.17% | -4 |
| 373 | Electricity Consumption | crazy | -5.84% | -16.87% | +0 |
| 374 | Chaos Rotation Lab | crazy | -6.59% | -17.62% | +0 |

## Rolling 30D
Trailing 30-day return rank; useful for recent momentum and tactical spotlight.
SPY 30D: +6.31%

| Rank | Algo | Category | 30D Return | 30D vs SPY |
| --- | --- | --- | --- | --- |
| 1 | Quantified Simple Monthly Rotation | standard | +12.42% | +6.11% |
| 2 | VIX Fear Rotation | crazy | +9.23% | +2.92% |
| 3 | VIX Term Structure | crazy | +9.21% | +2.90% |
| 4 | Retail Sales Momentum | crazy | +7.69% | +1.38% |
| 5 | Job Posting Acceleration | crazy | +6.18% | -0.13% |
| 6 | NRWise Acceleration | standard | +3.87% | -2.44% |
| 7 | Uber Mobility Index | crazy | +2.69% | -3.62% |
| 8 | Algo Baileymol (Chaos Monger) | standard | +2.31% | -4.00% |
| 9 | Faber Momentum Rotation | standard | +2.22% | -4.09% |
| 10 | Algo Biscotti (Unconditional Loyalty) (alt) | crazy | +2.11% | -4.20% |

## Sector Consensus
- Top Bullish: XLI, XLP, XLK
- Top Bearish: XLC, XLRE, XLV

| ETF | Sector | Composite | Label | Bullish % |
| --- | --- | --- | --- | --- |
| XLI | Industrials | 18 of 66 | BEARISH | 27% |
| XLP | Consumer Defensive | 11 of 53 | BEARISH | 21% |
| XLU | Utilities | 12 of 59 | BEARISH | 20% |
| XLK | Technology | 11 of 56 | BEARISH | 20% |
| XLY | Consumer Cyclical | 12 of 81 | BEARISH | 15% |
| XLB | Basic Materials | 8 of 53 | BEARISH | 15% |
| XLF | Financial Services | 4 of 53 | BEARISH | 8% |
| XLE | Energy | 4 of 54 | BEARISH | 7% |
| XLC | Communication Services | 2 of 49 | BEARISH | 4% |
| XLRE | Real Estate | 1 of 50 | BEARISH | 2% |
| XLV | Healthcare | 0 of 55 | BEARISH | 0% |

## Content Facts
- Signal of day: Quantified Simple Monthly Rotation (Ranked #1 on rolling 30D leaderboard)
- Call of day: XLI BEARISH (Highest bullish percentage in precomputed sector consensus)
- Failure of day: Chaos Rotation Lab (Lowest full-window force rank)

## Notable Divergences
- Chaos Rotation Lab: force rank #374, rolling 30D rank #15. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty): force rank #366, rolling 30D rank #11. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty) (alt): force rank #364, rolling 30D rank #10. Strong recent 30D rank despite weaker full-window force rank.
- Lumber Momentum: force rank #365, rolling 30D rank #14. Strong recent 30D rank despite weaker full-window force rank.
- Copper Momentum: force rank #362, rolling 30D rank #13. Strong recent 30D rank despite weaker full-window force rank.

