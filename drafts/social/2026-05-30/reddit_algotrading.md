# Lab Report: 374 Signals, 1 Beating SPY on Force Rank — Here's What's Failing

We're running 374 alternative-data signals across 105 tickers. Today's snapshot: **1 algo is beating SPY on full-window force rank. 373 are not.**

That's the headline. The rest is the work.

## The Setup

Each signal runs on a 117-day window (roughly 6 months live). We measure two things:

1. **Force rank** — cumulative alpha vs SPY over the full run. This is your "does this actually work?" test.
2. **Rolling 30D rank** — last month's performance. This catches regime shifts and recent edge.

Why both? Force rank tells you if the signal has *any* edge. Rolling 30D tells you if that edge is *still there*. They diverge constantly, and that divergence is where the interesting failures live.

## The Failure Rate (Lead with This)

- **373 of 374 algos are underwater vs SPY on force rank.**
- **371 of 375 algos are underwater vs SPY on rolling 30D.**

The two that beat SPY in the last 30 days:
- **Quantified Simple Monthly Rotation** (+12.42% YTD, +6.1% vs SPY in 30D)
- **VIX Fear Rotation** (+9.23% in 30D, +2.9% vs SPY)

Everything else is chasing. Most are losing.

## Notable Divergences: When Recent ≠ Historical

Three algos show a massive rank gap between force rank and rolling 30D:

| Algo | Force Rank | 30D Rank | Gap | 30D Return | YTD |
|------|-----------|----------|-----|-----------|-----|
| Chaos Rotation Lab (Baileymol) | 374 | 15 | 359 | +0.23% | -6.59% |
| Algo Biscotti (alt) | 364 | 10 | 354 | +2.11% | -0.82% |
| Algo Biscotti | 366 | 11 | 355 | +1.40% | -1.13% |

These three are *recently* working but have been *historically* terrible. Classic regime-flip candidates — or noise. The lab publishes both interpretations. You pick.

## The Worst Performers (Force Rank)

Bottom 3 by cumulative alpha:

- **Liquor Store Leading Indicator**: -13.17% alpha, -2.14% YTD
- **FINRA Dark Pool Signal**: -12.83% alpha, -1.80% YTD
- **Consumer Sentiment**: -12.56% alpha, -1.53% YTD

All three are "crazy" type signals (alternative data experiments). All three are still running. We don't delete failures — we publish them.

## Sector Consensus (All Bearish)

66 signals covering Industrials (XLI): 27% bullish → **BEARISH**  
53 signals covering Consumer Defensive (XLP): 21% bullish → **BEARISH**  
59 signals covering Tech (XLK): 20% bullish → **BEARISH**

The lab is not constructive right now. That's data, not opinion.

## What We're Asking

- Why is force rank so brutal? Is the market regime fundamentally hostile to these signals, or are we measuring the wrong window?
- The Biscotti divergence is real — is that a leading indicator or a dead cat bounce?
- Should we weight rolling 30D more heavily in live trading, or does that just chase noise?

Full leaderboard at stockarithm.com — all signals public, failures included.