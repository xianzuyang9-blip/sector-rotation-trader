# StockArithm Lab Report: 2026-05-26 — One Winner in 374

We're running 374 algorithmic signals across 105 tickers in live paper trading. Today's snapshot: **1 algo is beating SPY on force rank. 5 are beating it on rolling 30-day momentum.** The rest are underwater. This is the lab working as designed.

## The Numbers

**Force Rank (full-window since seed, 114 days):**
- Quantified Simple Monthly Rotation: +5.89% alpha, +16.06% YTD, $116,063.69 equity
- Faber Momentum Rotation: -1.82% alpha, +8.35% YTD
- Algo Baileymol (Chaos Monger): -2.01% alpha, +8.16% YTD
- 371 others: negative alpha, trailing SPY's +10.17%

**Rolling 30-Day Momentum (last 30 calendar days):**
- Simple Monthly Rotation leads again: +16.06% return, 6.53 Sharpe, +111 bps vs. SPY
- VIX Term Structure: +6.60% return, 4.62 Sharpe
- VIX Fear Rotation: +6.08% return, 4.20 Sharpe
- 372 others: SPY returned +4.95% in the same window

**The spread matters.** Of 375 rolling-30D algos, only 5 beat SPY. That's 1.3%. On force rank, it's 1 of 374 (0.27%). These are not edge numbers—they're noise floors. We report them anyway.

## Why Two Leaderboards?

Force rank captures consistency over the full sample. Rolling 30D captures recent momentum. They diverge sharply: VIX Fear Rotation ranks 372nd all-time but 3rd in the last month (+369 rank gap). Algo Biscotti (Unconditional Loyalty) ranks 369th all-time but 15th recently (+354 gap). This tells you something about regime change and signal decay. It also tells you the sample is too short to draw conclusions.

## The Honest Critique

114 days of live paper trading is **not statistically significant.** With 374 independent signals, you expect ~3–4 to beat a benchmark by chance alone. Simple Monthly Rotation's +5.89% alpha could be luck. The Sharpe ratios look clean, but the max drawdowns are shallow (all under 3.5% in the last 30 days)—we haven't stress-tested these in a real drawdown. The sector consensus is uniformly bearish (Technology at 33% bullish, Utilities at 12%), which is a data point, not a forecast.

## What We're Actually Testing

The signals feed on alternative data: FRED macroeconomic releases, TSA passenger volumes, Reddit sentiment, job openings, port container throughput, liquor store foot traffic, VIX term structure. Some work. Most don't. Port Container Volume and Liquor Store Leading Indicator are down 11%+ YTD. That's the lab's value: **public failure is as important as public success.** You see which data sources are noise.

The methodology is transparent. The leaderboard is live. The losses are real.

**Methodology and full leaderboard at stockarithm.com.**