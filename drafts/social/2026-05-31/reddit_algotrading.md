# Lab Report: 374 Signals, 1 Beating SPY on Force Rank — Here's What's Failing

We're running 374 alternative-data signals across 105 tickers. Today's snapshot: **1 algo is beating SPY on full-window force rank. 373 are not.**

That's the headline. The rest is the work.

## The Setup

Each signal runs on a 117-day window (roughly 6 months live). We measure two things:

1. **Force rank** — cumulative alpha vs SPY over the full run. This is what matters for "does this edge exist?"
2. **Rolling 30D rank** — last month's performance. This catches regime shifts and recent momentum.

Why both? Force rank tells you if you found signal. Rolling 30D tells you if it's *still working*. They diverge constantly, and that's where the lab gets interesting.

## The Failure Rate (Lead With It)

- **373 of 374 algos are underwater vs SPY on force rank.**
- Only **Quantified Simple Monthly Rotation** (simple_monthly) is positive: +1.39% alpha, $112.4K equity.
- Baileymol (Chaos Monger) is at -2.87% alpha. Faber Momentum Rotation dropped from rank 3 to rank 5 in one day, now -4.89% alpha.
- Bottom tier: Liquor Store Leading Indicator at -13.17% alpha. FINRA Dark Pool Signal at -12.83%. Consumer Sentiment at -12.56%.

These aren't edge cases. They're the majority.

## The Divergence Problem

Here's where it gets weird. **Baileymol ranks 374th on force rank but 15th on rolling 30D.** That's a 359-rank gap. Same with Biscotti variants — force rank 364–366, rolling 30D rank 10–11.

What does this mean? Either:
- These algos found something real in the last 30 days after months of failure (possible).
- They're fitting noise in a narrow window (more likely).
- The regime shifted hard and old signals broke (also possible).

We don't know yet. That's why we publish both.

## What's Actually Working (This Month)

Rolling 30D leaderboard shows 4 algos beating SPY:

1. **Quantified Simple Monthly Rotation** — +12.42% YTD, +6.1% vs SPY in 30D, Sharpe 4.1
2. **VIX Fear Rotation** — +9.23% in 30D, Sharpe 5.45
3. **VIX Term Structure** — +9.21% in 30D, Sharpe 5.45
4. **Retail Sales Momentum** — +7.69% in 30D, Sharpe 5.83

SPY returned +6.31% in the last 30 days. These four beat it. The other 371 did not.

## The Sector Call

Consensus across all 374 signals: **bearish across all major sectors.** Industrials (XLI) has the highest bullish vote at 27% (still bearish composite). Consumer Cyclical (XLY) at 15% bullish. This is not a bullish lab right now.

## Why This Matters

We're not hiding the 373 failures. We're publishing them. If you're building algos, you need to see what *doesn't* work at scale. The Liquor Store Leading Indicator sounds clever. It's down 13%. The dark pool signal sounded clever. Down 12.8%. Consumer sentiment? Down 12.5%.

The one thing working is a simple monthly rotation. No alternative data. No chaos. Just rebalance monthly.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the force rank vs 30D split? Are we watching regime change or just overfitting the last month?