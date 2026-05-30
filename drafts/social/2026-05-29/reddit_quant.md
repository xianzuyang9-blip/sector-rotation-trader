# StockArithm Lab Report: 374 Algos, 1 Winner, 371 Lessons (2026-05-29)

We're running 374 signals across 105 tickers in live paper trading. Today's snapshot: **1 algo is beating SPY on force rank. 4 are beating it on rolling 30-day momentum.** The rest are underwater. This is the point.

## The Numbers

**Force Rank (full-window since seed, ~117 days):**
- Quantified Simple Monthly Rotation: +12.42% YTD, +1.39% alpha vs. SPY's +11.03%
- Baileymol (Chaos Monger): +8.16% YTD, -2.87% alpha
- Retail Sales Momentum (FRED data): +7.97% YTD, -3.06% alpha
- Job Posting Acceleration (job openings data): +6.18% YTD, -4.86% alpha

The tail is brutal. Consumer Sentiment, FINRA Dark Pool Signal, and Liquor Store Leading Indicator are all down 1–2% YTD, trailing SPY by 12–13 percentage points.

**Rolling 30-Day Momentum (last month only):**
- Simple Monthly Rotation: +12.42%, Sharpe 4.10
- VIX Fear Rotation: +9.23%, Sharpe 5.45
- VIX Term Structure: +9.21%, Sharpe 5.45
- Retail Sales Momentum: +7.69%, Sharpe 5.83
- Job Posting Acceleration: +6.18%, Sharpe 5.03

SPY returned +6.31% in the last 30 days. Four algos beat that threshold. 371 did not.

## Why We Report Both Rankings

Force rank rewards consistency over 117 days. Rolling 30D captures recent regime shifts. They diverge sharply: Baileymol ranks 374th all-time but 15th in the last month (+0.23% in 30D). Biscotti variants rank 364–366 force but 10–11 rolling. This isn't noise—it's signal about mean reversion, regime change, or luck. We publish both so you can decide which matters to your thesis.

## The Honest Critique

**Sample size:** 117 days is not statistically significant. One algo beating SPY over four months could be luck. Sharpe ratios above 5 on 30-day windows are suspicious—likely overfitting or survivorship bias in the signal construction. We're not claiming edge; we're publishing methodology so you can audit it.

**Data sources:** Retail Sales Momentum uses FRED retail sales data. Job Posting Acceleration uses job openings counts. VIX signals use term structure. Consumer Sentiment uses survey data. None of these are proprietary. The edge (if it exists) is in the *combination and timing*, not the raw inputs.

**Sector consensus:** Across 374 algos, only 27% are bullish on Industrials (XLI), 21% on Consumer Defensive (XLP). The composite reads BEARISH across all major sectors. This is the aggregate signal—not a prediction, just what the lab is seeing.

## The Failure

Chaos Rotation Lab is down 6.59% YTD, ranked 374th. It's public. We don't hide it. That's the differentiator from closed-door quant shops.

The lab exists to test alternative data signals at scale and show you what works and what doesn't. Most don't. That's the real finding.

**Methodology and full leaderboard at stockarithm.com.**