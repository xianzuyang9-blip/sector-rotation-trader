# StockArithm Lab Report: 419 Algos, Zero Beating SPY on Force Rank (June 5, 2026)

We're publishing today's full leaderboard snapshot because the honest answer is: nothing is working right now.

## The State of the Lab

**Force rank (full-window since seed):** 419 algos tracked across 105 tickers. **0 are beating SPY.** SPY is up 8.25% YTD. The best performer, Algo Baileymol (Chaos Monger), is at +8.16% with -0.09% alpha—essentially flat relative to the benchmark after 122 days of live paper trading.

The next two—Quantified Simple Monthly Rotation (+6.11%) and Antonacci Dual Momentum Sector Rotation (+4.80%)—are both underwater on alpha. The spread is wide: bottom performers like VIX Fear Rotation (-3.56%) and Liquor Store Leading Indicator (-1.89%) are lagging by 11–12 percentage points.

**Rolling 30-day leaderboard:** 420 algos. 7 are beating SPY over the last month. SPY returned 0.51% in the past 30 days. Algo Biscotti (Unconditional Loyalty) leads at +1.73% with a 0.73 Sharpe ratio and -4.7% max drawdown. The two VIX-based strategies (Fear Rotation, Term Structure) rank #3 and #4 on the 30D window despite ranking #417 and #415 on force rank—a 411–414 point divergence.

## Why We Report Both Rankings

**Force rank** answers: "What's the best long-term signal?" It's the full-window cumulative return since each algo went live (typically 112–122 days). It's noisy at this sample size and heavily weighted to early performance.

**Rolling 30D** answers: "What's working *right now*?" It's more responsive to regime change but suffers from look-ahead bias and short-window overfitting. A 30-day window is not statistically significant.

Neither ranking is predictive. Both are published because the methodology demands transparency about what we don't know.

## The Divergences

**VIX Fear Rotation** is the clearest case: force rank #417 (YTD -3.56%), rolling 30D rank #3 (last 30 days +1.04%). This is a regime flip. Either the algo is capturing a temporary edge in volatility structure, or it's noise. We can't tell yet.

**Faber Momentum Rotation** shows the inverse: force rank #5 (YTD +2.40%), rolling 30D rank #416 (last 30 days -2.08%). The momentum framework worked earlier; it's broken now.

## Sector Consensus

Across 48 sector-level signals, only 12 are bullish on Utilities (XLU). Technology (XLK) is 19% bullish (9 of 48 signals). All five major sectors are flagged BEARISH. This is not a market-timing call—it's the aggregate output of 419 independent signal streams. It reflects what the algos are seeing in FRED data, TSA mobility, Reddit sentiment, job openings, and alternative datasets.

## The Honest Framing

- **Sample size:** 122 days is not enough to distinguish signal from noise. Confidence intervals are wide.
- **Survivorship:** We're not filtering. Failed algos stay on the board.
- **Benchmark:** SPY is the only fair comparison for a diversified equity lab.
- **Edge:** We don't have one yet. The point is the methodology and the public record.

Methodology and full leaderboard at stockarithm.com.