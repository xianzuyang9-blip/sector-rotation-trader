# Why Good Signals Fail in the Wrong Regime

You built a signal that worked beautifully for three years. It caught the 2023 rally, navigated 2024, and made money in sideways markets. Then 2025 arrived, and it stopped working. Not because the logic broke. Because the market regime changed.

This is the story of 374 signals tested against the same market, over the same period. One is beating SPY. The other 373 are not. And the gap between them isn't random—it's a lesson in regime mismatch.

## The Brutal Leaderboard

As of May 29, 2026, StockArithm's signal library spans 374 quantified strategies across 105 tickers. Over the past 117 days, exactly one has delivered alpha: **Quantified Simple Monthly Rotation**, up 12.42% year-to-date versus SPY's 11.03%. That's 1.39% of outperformance. Not spectacular. But in a field of 374, it's the only one in the green.

The second-place finisher, Algo Baileymol, is down 2.87% relative to SPY. The third, Retail Sales Momentum, is down 3.06%. By the time you reach the bottom quartile, you're looking at strategies like the Liquor Store Leading Indicator (down 13.17% relative to SPY) and the FINRA Dark Pool Signal (down 12.83%).

The median strategy is underwater. The distribution is not a bell curve—it's a graveyard with one survivor.

But here's where regime mismatch enters the picture.

## The 30-Day Flip

Look at the rolling 30-day leaderboard, and the story inverts.

Over the last month, four strategies beat SPY. The top performer is still Quantified Simple Monthly Rotation, but now it's joined by VIX Fear Rotation, VIX Term Structure, and Retail Sales Momentum. These aren't new strategies. They're the same ones that were underwater over the full window.

Retail Sales Momentum, for example, ranks 3rd over 30 days (up 7.69% vs. SPY's 6.31%) but 3rd from the bottom over the full period (down 3.06% relative to SPY). That's not a typo. The same signal is both a top performer and a laggard, depending on which regime you're measuring.

Even more striking: Chaos Rotation Lab (Baileymol-crazy) ranks dead last on the full-window leaderboard but 15th over the past month. A 359-position gap between two measurements of the same strategy.

This is regime mismatch in action. The strategies that worked in the 2024–early 2025 environment—simple rotation, momentum, volatility-based rules—stopped working when the market shifted. Then, when conditions changed again in May 2026, they came roaring back.

## Why This Matters More Than You Think

The conventional narrative in quant trading is: *Find a good signal, backtest it, deploy it, collect alpha.* The data here suggests a darker truth: *Find a good signal, and wait for the regime to change.*

Consider the Retail Sales Momentum strategy. Its logic is sound: track retail sales acceleration, rotate into stocks that benefit. In a consumer-driven rally, it works. In a period where macro headwinds dominate, it fails. The signal didn't break. The market did.

This is why so many smart traders blow up. They optimize for the last regime. They build conviction on a strategy that worked for 18 months. Then they deploy it into a market that no longer rewards that behavior, and they hold on too long because the logic still feels right.

The data shows this happening across the board. Consumer Sentiment, Job Posting Acceleration, and other "crazy" category strategies (experimental, alternative data-driven) are clustered at the bottom of the full-window rankings. But several of them rank in the top 20 over 30 days. They're not broken. They're regime-dependent.

## The One That Survived

Quantified Simple Monthly Rotation is the only strategy beating SPY across both windows. It ranks #1 on the full-window leaderboard and #1 on the rolling 30-day leaderboard. Its alpha is modest—1.39% over the full period, 6.11% over the last month—but it's consistent.

Why? Because simple monthly rotation is regime-agnostic. It doesn't bet on consumer sentiment or dark pool flows or job posting acceleration. It rotates based on relative strength across a basket of assets. When momentum works, it wins. When mean reversion works, it still wins because it's rebalancing monthly. It's not trying to predict the regime; it's adapting to it.

This doesn't mean simple rotation is the answer. It means that in a world of 374 signals, the ones that survive regime shifts are the ones that don't require the regime to stay the same.

## What This Tells You

If you're building or evaluating trading signals, the leaderboard is not your friend. The leaderboard is a snapshot of the current regime. A strategy that ranks 370th today might rank 10th in six months. A strategy that's beating SPY now might be underwater by year-end.

The real question isn't: *Which signal is winning?* It's: *Which signal will keep winning when the regime changes?*

That requires stress-testing across multiple market environments, not just backtesting on historical data. It requires understanding what your signal is actually betting on—momentum? mean reversion? volatility? macro flows?—and asking whether that bet will hold when conditions shift.

One signal is beating SPY. The other 373 are waiting for their regime to come back. Some will. Most won't. The difference isn't luck. It's whether the signal was built to survive a regime change or just to exploit the last one.

---

*For a deeper dive into how these 374 strategies performed and what the data reveals about regime-dependent trading, read the full analysis on Substack.*
