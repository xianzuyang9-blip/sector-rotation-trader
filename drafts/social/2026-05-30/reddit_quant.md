# StockArithm Lab Report: 374 Algos, 1 Beating SPY (Full Window)

We're publishing today's live paper-trading results across 374 algorithmic signals. The headline is uncomfortable: only **Quantified Simple Monthly Rotation** is beating SPY on a force-ranked (full-window) basis. On the rolling 30-day leaderboard, 4 algos clear the benchmark. This is the point of public transparency—to show what actually works and what doesn't.

## The Setup

StockArithm runs two ranking systems simultaneously:

1. **Force rank**: cumulative return since seed date (117 days for most algos). This is the "did you make money?" test. Sample size is small—117 days is ~23 weeks, statistically insufficient to claim edge. We report it anyway because it's honest.

2. **Rolling 30D momentum**: last 30 calendar days of returns, Sharpe ratio, max drawdown. This window is even noisier but captures recent regime fit. Four algos beat SPY here.

Both rankings matter. An algo crushing the last month but underwater YTD (like Baileymol, ranked #2 force but #15 rolling 30D) signals regime sensitivity, not alpha.

## What's Actually Winning

**Quantified Simple Monthly Rotation** (simple_monthly): +12.42% YTD vs. SPY +11.03%. Alpha: +1.39%. Equity: $112,418. Rolling 30D return: +12.42%, Sharpe 4.10, max drawdown -4.03%. This is a standard rotation algo, not a "crazy" signal. It's also the only one beating the benchmark on force rank.

The rolling 30D top 4 include two VIX-based strategies (VIX Fear Rotation, VIX Term Structure) and Retail Sales Momentum. All three are classified "crazy"—meaning they use alternative data (FRED retail sales, VIX term structure). All three underperform on full-window basis but have outperformed SPY in the last month.

## The Failures

**Liquor Store Leading Indicator**, **Consumer Sentiment**, **FINRA Dark Pool Signal**: -2.14%, -1.53%, -1.80% YTD respectively. These are ranked 372–374 on force. They're also ranked 373–371 on rolling 30D. No recent bounce. These signals are not working.

**Baileymol (Chaos Monger)** is the "failure of day"—ranked #374 force with -6.59% YTD, yet #15 rolling 30D with +0.23% last month. This divergence is real and worth studying: the algo fit a recent regime but has been underwater for months.

## Critical Limitations

- **N = 117 days**. Not statistically significant. One algo beating SPY over 4 months could be luck.
- **No transaction costs modeled**. Paper trading ignores slippage, commissions, market impact.
- **Sector consensus is bearish across the board**: Industrials 27% bullish, Consumer Cyclical 15%. The algos are not contrarian here; they're following the same regime.
- **Alternative data quality unknown**. Job posting acceleration, retail sales momentum—these rely on FRED and job board scrapes. Lag, survivorship bias, and structural breaks are not quantified.

## Why Publish Losses?

Because the lab's differentiator is not claiming 20% returns. It's showing the methodology, the data sources, the full leaderboard, and the failures. Quants and academics can audit this. You can see which signals are overfitted, which are regime-dependent, and which are just noise.

Methodology and full leaderboard at **stockarithm.com**.