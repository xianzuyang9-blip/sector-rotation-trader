# Lab Report: 323 Signals, 1 Winner. Here's What We're Learning.

**TL;DR:** We're running 323 algos across 105 tickers. SPY returned 5.49% over the last 30 days. Only **1 algo is beating it** on force rank. Only **1 is beating it** on rolling 30D. The gap between those two rankings tells us something useful about regime change.

---

## The Setup

Each signal runs live paper trading from a fixed $100k starting equity. We measure two things:

1. **Force rank** — full-window performance since launch (109 days for most algos)
2. **Rolling 30D rank** — last 30 days only

Why both? Force rank shows consistency. Rolling 30D catches regime shifts. When they diverge wildly, something changed.

---

## The Failure Rate (Lead With This)

**322 of 323 algos are underperforming SPY on force rank.**

That's 99.7% failure. The one winner:

- **Quantified Simple Monthly Rotation** (`simple_monthly`)
  - Force rank: #1
  - YTD: +11.96% vs SPY +9.01%
  - Alpha: +2.95%
  - 109 days running

Everyone else is negative alpha. Baileymol (Chaos Monger) is at -0.96%. Faber Momentum Rotation at -1.34%. By rank 320, you're down -11.69% (Port Container Volume).

---

## The Divergence Problem

Here's where it gets interesting. **VIX Fear Rotation** ranks #321 on force rank but #2 on rolling 30D.

| Algo | Force Rank | 30D Rank | 30D Return | Rank Gap |
|------|-----------|----------|-----------|----------|
| VIX Fear Rotation | 321 | 2 | +5.49% | 319 |
| VIX Term Structure | 315 | 3 | +5.33% | 312 |
| Algo Biscotti (alt) | 313 | 7 | +3.45% | 306 |

These algos are **recently hot but historically cold**. That's not edge—that's regime capture. The market shifted, they caught it, but they've been wrong for 100+ days before that.

This is why we show both metrics. Force rank alone hides recency bias. Rolling 30D alone hides the fact that you're riding a wave that may reverse.

---

## What's Actually Working (Barely)

`simple_monthly` is the only signal with positive alpha. It's a monthly rotation strategy. No alternative data. No chaos. Just rebalance once a month.

- Sharpe (30D): 4.29
- Max drawdown (30D): -3.49%
- SPY delta (30D): +6.48%

It's boring. It's working.

---

## The Sector Consensus

Across 50 tech signals, 28% are bullish on XLK. That's **BEARISH** by our threshold. Industrials, materials, consumer cyclical—all red. The lab is not constructive right now.

---

## What We're Not Claiming

- No prediction of future returns
- No stock picks
- No claim that `simple_monthly` will keep winning
- No explanation for *why* it's winning (that's your job to figure out)

We're publishing the data. The failures are public. The one winner is public. You can fork the methodology, test it yourself, or tell us why we're measuring the wrong thing.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What's your read on the force rank / rolling 30D split? Are we measuring regime capture correctly, or missing something?