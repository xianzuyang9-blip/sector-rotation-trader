# Lab Report: 344 Signals, 1 Winner (Force Rank), 4 Winners (Last 30 Days)

We're running 344 alternative-data signals across 105 tickers. Today's snapshot: **99.7% are underperforming SPY on a full-window force-rank basis.** One signal is beating the benchmark. Four are beating it over the rolling 30-day window. This is the lab working as designed — most ideas fail publicly.

## The Pipeline

Each signal generates a daily trade decision. We measure two things:

1. **Force Rank** — cumulative return vs. SPY since inception (112 days for most signals)
2. **Rolling 30D** — last 30 calendar days of returns + Sharpe ratio + max drawdown

Both matter. Force rank shows if an idea has *any* edge over a long window. Rolling 30D catches regime shifts and recent momentum. They often disagree, and that disagreement is where the interesting questions live.

## The Numbers

**Force Rank Leaderboard (Full Window):**

- **#1: Quantified Simple Monthly Rotation** — +13.09% YTD, +3.64% alpha vs. SPY (9.44%). Equity: $113,086. This is the only signal beating SPY on cumulative returns.
- **#2–#344:** Baileymol, Faber, Antonacci Dual Momentum, and 340 others are all underwater relative to the benchmark.

The bottom three: Copper Momentum (–1.8% YTD), Port Container Volume (–2.18%), VIX Fear Rotation (–2.35%). All "crazy" type signals (alternative data experiments).

**Rolling 30D Leaderboard (Last Month):**

SPY returned +4.84% in the last 30 days. Four signals beat that:

1. **Quantified Simple Monthly Rotation** — +13.09%, Sharpe 5.46, max DD –3.49%
2. **VIX Fear Rotation** — +6.14%, Sharpe 4.14, max DD –2.52%
3. **VIX Term Structure** — +5.99%, Sharpe 3.94, max DD –2.52%
4. **Retail Sales Momentum** — +5.26%, Sharpe 3.73, max DD –2.49%

Bottom three: Freight Rail Carloads (–1.05%), FINRA Dark Pool Signal (–1.38%), Copper Momentum (–1.83%).

## The Divergences

This is where the lab gets interesting. Three signals show rank gaps worth watching:

- **VIX Fear Rotation**: Force rank #342 (down 11.79% YTD), but rolling 30D rank #2 (+6.14% last month). Regime shift or noise? Running 102 days.
- **FINRA Dark Pool Signal**: Force rank #10 (+0.27% YTD), but rolling 30D rank #342 (–1.38% last month). Was working; stopped working.
- **VIX Term Structure**: Force rank #334 (–0.59% YTD), rolling 30D rank #3 (+5.99% last month). Recent strength, long-term weakness.

## Sector Consensus

All five major sectors are flagged BEARISH by our signal consensus. XLB (Basic Materials) is the "least bearish" at 26% bullish signals (9 of 34). XLE (Energy) is the most bearish at 15% (5 of 34). This is a data point, not a call.

## What We're Not Saying

We're not claiming any of these will beat SPY tomorrow. We're not ranking them by Sharpe ratio alone (that's how you overfit). We're not hiding the failures — they're all here, ranked, with equity curves public.

The lab publishes everything. Failures included.

---

**Full leaderboard at stockarithm.com — all signals public, failures included.**

What rank gaps or divergences are you seeing that we should dig into?