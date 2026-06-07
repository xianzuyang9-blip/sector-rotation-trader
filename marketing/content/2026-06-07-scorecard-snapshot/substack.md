# The current scorecard in one glance

## What StockArithm Is

StockArithm is a live ranking system that tests algorithmic trading strategies against real market data. Every day, 419 different algorithms—ranging from classical momentum rotations to experimental volatility-based systems—generate signals and compete on a single leaderboard. The system tracks which strategies beat the S&P 500, which ones fail, and which ones are gaining or losing ground week to week. It's not a fund. It's not a recommendation service. It's a transparent scoreboard that answers one question: *which trading rules actually work right now?*

The reason this matters is simple. Most trading advice is backward-looking, anecdotal, or dressed up in marketing language. StockArithm publishes live results. You can see the equity curve, the drawdown, the Sharpe ratio, and the exact date each algorithm started running. No cherry-picked backtests. No survivorship bias. Just the current state of the game.

## The Snapshot: June 5, 2026

As of Friday, June 5, 2026, here's what the data shows:

**The big picture:**
- 419 algorithms ranked by force (full-window performance)
- 420 algorithms running in the rolling 30-day window
- 7 of those 30-day algorithms are beating SPY
- 105 stocks covered across all signals
- SPY returned 8.25% year-to-date; 0.51% in the last 30 days

**The leaders (force rank):**
1. **Algo Baileymol (Chaos Monger)** — up 8.16% YTD, -0.09% alpha vs. SPY, $108,161 equity
2. **Quantified Simple Monthly Rotation** — up 6.11% YTD, -2.15% alpha, $106,110 equity
3. **Antonacci Dual Momentum Sector Rotation** — up 4.80% YTD, -3.46% alpha, $104,796 equity

**The laggards (force rank):**
- **VIX Term Structure** — down 1.83% YTD, -10.08% alpha, $98,173 equity
- **Liquor Store Leading Indicator** — down 1.89% YTD, -10.15% alpha, $98,110 equity
- **VIX Fear Rotation** — down 3.56% YTD, -11.82% alpha, $96,438 equity

**The 30-day winners:**
1. **Algo Biscotti (Unconditional Loyalty) (alt)** — +1.73% in 30 days, +1.23% vs. SPY, Sharpe 0.73
2. **Algo Biscotti (Unconditional Loyalty)** — +1.73% in 30 days, +1.23% vs. SPY, Sharpe 0.73
3. **VIX Fear Rotation** — +1.04% in 30 days, +0.54% vs. SPY, Sharpe 0.35

**The 30-day losers:**
- **Faber Momentum Rotation** — -2.08% in 30 days, -2.58% vs. SPY, Sharpe -1.60
- **Copper Momentum** — -2.11% in 30 days, -2.62% vs. SPY, Sharpe -1.97
- **FINRA Dark Pool Signal** — -2.34% in 30 days, -2.85% vs. SPY, Sharpe -3.08

## The Divergences: When Rankings Flip

One of the most useful signals in StockArithm is the *rank gap*—the difference between an algorithm's full-window force rank and its rolling 30-day rank. When these diverge sharply, it tells you something important: the market regime has shifted, or the strategy is in transition.

**VIX Fear Rotation** is the clearest example. Over the full window, it ranks 417th (near the bottom). But in the last 30 days, it ranks 3rd. That's a gap of 414 positions. Why? Because volatility-based strategies that struggled in a calm, trending market have suddenly found traction in recent chop. The algorithm returned 1.04% in 30 days while the market returned 0.51%. But year-to-date, it's still down 3.56%. This is a strategy that's working *now* but hasn't worked for most of the year.

**Faber Momentum Rotation** shows the opposite pattern. Over the full window, it ranks 5th—a solid performer. But in the last 30 days, it ranks 416th, near the bottom. It's down 2.08% while SPY is up 0.51%. The gap is -411 positions. Faber is a classical momentum rotation system that has worked well for months, but it's broken down in the last month. The strategy is still up 2.40% year-to-date, but recent performance suggests the trend it relies on has stalled.

**VIX Term Structure** mirrors the VIX Fear Rotation story: force rank 415, rolling 30-day rank 4, gap of 411. It's a volatility play that's suddenly working, but the full-window record is poor.

These divergences matter because they show you which strategies are *regime-dependent*. A strategy that works in calm markets may fail in volatile ones, and vice versa. StockArithm's dual ranking system makes that visible.

## The Sector Consensus: Mostly Bearish

Across the 48 algorithms that generate sector signals, the consensus is uniformly bearish. Here's the breakdown:

- **Utilities (XLU)**: 25% bullish (12 of 48 algos) — **BEARISH**
- **Industrials (XLI)**: 22% bullish (14 of 65 algos) — **BEARISH**
- **Technology (XLK)**: 19% bullish (9 of 48 algos) — **BEARISH**
- **Basic Materials (XLB)**: 19% bullish (8 of 42 algos) — **BEARISH**
- **Consumer Defensive (XLP)**: 17% bullish (8 of 48 algos) — **BEARISH**

Not a single sector has a bullish consensus. The highest conviction is in Utilities at 25% bullish—still a clear bearish lean. This suggests that across the algorithmic universe, there's broad skepticism about sector rotation opportunities right now. Whether that skepticism is warranted will only be clear in hindsight.

## The Signal and the Failure

**Signal of the day:** Algo Biscotti (Unconditional Loyalty) (alt), ranked #1 on the rolling 30-day leaderboard with +1.73% return and a 0.73 Sharpe ratio. The caveat: it ranks 406th on the full-window force leaderboard. This is a recent winner, not a proven long-term performer.

**Failure of the day:** Chaos Rotation Lab (baileymol-crazy), ranked 419th (dead last) on the force leaderboard. It's down 8.96% year-to-date and has generated -17.21% alpha vs. SPY. This is a strategy that has failed consistently across the entire measurement window.

## What This Means

The scorecard tells you three things:

1. **Most algorithms are underwater on alpha.** Only 7 of 420 rolling 30-day algorithms beat SPY. The median strategy is losing to the index. This is not surprising—it's the baseline expectation. But it's worth stating plainly: algorithmic trading is hard, and most attempts fail.

2. **Regime matters more than you think.** The gap between Faber's full-window rank (5th) and its 30-day rank (416th) shows that a strategy can be "good" in one market and "bad" in another. There is no permanent leaderboard. The rules that worked in a trending market may not work in a choppy one.

3. **Volatility strategies are having a moment.** VIX Fear Rotation and VIX Term Structure both rank in the top 4 on the 30-day leaderboard despite ranking near the bottom over the full window. This suggests the market has shifted from calm and directional to choppy and mean-reverting. Whether that persists is an open question.

## What You Should Do

If you're building or testing trading strategies, use this as a benchmark. If your algorithm can't beat the median performer in this cohort, it's not ready. If it beats the top performers, be skeptical—ask whether you've overfitted to recent data or whether you've genuinely found an edge.

If you're evaluating trading advice from anyone else, ask them the same questions StockArithm asks: What's the full-window return? What's the 30-day return? What's the Sharpe ratio? What's the maximum drawdown? And most importantly: is the strategy beating SPY, or just beating other strategies that are also losing to SPY?

The market doesn't care about your ranking relative to other algorithms. It only cares about your ranking relative to the index.

---

**Want to see the full leaderboard, track individual algorithms, or test your own strategy?** Visit [stockarithm.com](https://www.stockarithm.com) to explore the live rankings, dive into the data, and see which rules are working right now.
