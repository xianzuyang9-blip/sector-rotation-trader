# StockArithm Lab Report: 323 Algos, 1 Winner vs. SPY (109 Days In)

We're running 323 signals across 105 tickers in live paper trading. After 109 days, exactly **one algo is beating SPY**. That's the honest headline. The other 322 are underwater or treading water. This is what happens when you publish everything.

## The Numbers

SPY returned 9.01% YTD. **Quantified Simple Monthly Rotation** (force rank #1) returned 11.96%, delivering +2.95% alpha on $100k starting capital. Current equity: $111,963.78. That's it for the winners.

Baileymol sits at rank #2 with 8.06% YTD (−0.96% alpha). Faber Momentum Rotation is #3 at 7.67% (−1.34% alpha). By rank #5, we're at Uber Mobility Index: 4.53% YTD (−4.48% alpha). The bottom dwellers—Copper Momentum, Port Container Volume, VIX Fear Rotation—are down 2–3% YTD, lagging SPY by 11–12 percentage points.

**This is the distribution we publish.** Not curated. Not filtered. All 323.

## Why Two Leaderboards?

We report both **force rank** (full-window cumulative return since seed) and **rolling 30D momentum** because they answer different questions.

Force rank shows durability. Rolling 30D shows what's working *right now*—and it's volatile. VIX Fear Rotation ranks #321 all-time but #2 in the last 30 days (5.49% return, 3.45 Sharpe). That's a 319-rank gap. It's real. It's also a red flag for overfitting to recent regime.

Over the past 30 days, SPY returned 5.49%. Simple Monthly Rotation returned 11.96%, beating SPY by 6.48 percentage points. VIX Fear Rotation and VIX Term Structure both outperformed SPY in the rolling window despite being underwater YTD. This divergence matters—and we flag it.

## The Caveats (Say Them First)

**Sample size:** 109 days is not statistically significant. One algo beating 322 others could be luck. The Sharpe ratios look clean (Simple Monthly: 4.29 over 30D), but that's a short window. Maximum drawdown on the winner is −3.49% over 30D; we're not claiming immunity to volatility.

**Data sources:** These algos consume FRED macroeconomic data, TSA passenger flows, Reddit sentiment, job openings, freight tonnage, VIX term structure, and sector rotation signals. Each introduces its own lag, survivorship bias, and regime dependency. Copper Momentum and Port Container Volume are "crazy" type algos—experimental signals with no track record. They're failing. That's the point of publishing them.

**Methodology:** We rank by total return (force rank) and by 30D Sharpe-adjusted momentum. Both are mechanical. No discretion. No rebalancing based on hindsight. The sector consensus at the bottom shows 28% bullish on Technology (XLK), 24% on Industrials (XLI)—both marked BEARISH by composite vote. That's the algos' collective read, not ours.

## What This Isn't

This is not a pitch. We're not claiming an edge. We're showing you the lab. One winner in 323 trials, after 109 days, in a rising market. That's a baseline. The methodology is transparent. The failures are public. The data sources are named.

**Methodology and full leaderboard at stockarithm.com.**