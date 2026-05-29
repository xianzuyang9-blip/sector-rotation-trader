# StockArithm Lab Report: 2026-05-29 — 1 Winner, 373 Losers

## The Setup

We're running **374 signals** across **105 tickers**, all paper-traded from entry to today. Each algo gets ranked two ways:

1. **Force rank** — full-window performance (how long it's been running)
2. **Rolling 30D rank** — last 30 days only (what's working *now*)

Both matter. Force rank shows durability. Rolling 30D shows momentum. When they diverge, something interesting is happening.

SPY returned **+10.76%** over the force-rank window and **+6.03%** in the last 30 days.

## The Failure Rate (Lead With This)

**373 of 374 algos are underperforming SPY on force rank.**

That's a **99.7% failure rate** by the primary metric. One algo beat the benchmark. One.

- **Quantified Simple Monthly Rotation** (simple_monthly): +6.38% alpha, +$17,135 equity
- Everything else: negative alpha, lagging SPY

On rolling 30D, it's slightly less grim: **4 of 375 algos** beat SPY in the last month. But that's a different cohort — some algos are too new for force rank.

## The Winner (And Why It Matters Less Than You'd Think)

**Quantified Simple Monthly Rotation** is ranked #1 on both metrics:

- Force rank alpha: **+6.38%** (117 days running)
- Rolling 30D return: **+17.14%** vs SPY's +6.03%
- Sharpe (30D): **6.73**
- Max drawdown (30D): **-3.49%**

It's a monthly rotation strategy. Simple. Boring. It works in this window. Will it work next month? Unknown. The lab publishes it anyway.

## The Divergences (Where It Gets Weird)

Two algos show massive rank gaps between force and rolling 30D:

**Chaos Rotation Lab (baileymol-crazy)**
- Force rank: **374** (dead last)
- Rolling 30D rank: **16** (top 5%)
- YTD: **-6.26%**
- Last 30D return: **+0.80%**

This thing is tanking overall but just caught fire. Is it a dead cat bounce or a regime shift? The data doesn't say. We publish both rankings so you can decide.

**Insider Trading Signals**
- Force rank: **12** (solid)
- Rolling 30D rank: **365** (bottom 3%)
- YTD: **+0.35%**
- Last 30D return: **-0.26%**

Built a lead early. Lost it recently. Happens.

## Sector Consensus (All Bearish)

Across 46 signals covering Technology (XLK), only **24% are bullish**. Consumer Defensive, Utilities, Materials, Industrials: all showing 12–19% bullish conviction. The lab's sector consensus is uniformly red.

This is not a prediction. It's a snapshot of what 374 different signals are saying *right now*.

## What We're Not Claiming

- These algos will beat SPY tomorrow
- The one winner is "better" (it just won this window)
- Alternative data is magic (see: Liquor Store Leading Indicator, down 11.86%)
- You should trade any of this

## What We're Actually Doing

Publishing failures alongside wins. Showing the math. Running the same algos everyone can see. If you spot a bug in the methodology, the leaderboard, or the data — call it out.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**