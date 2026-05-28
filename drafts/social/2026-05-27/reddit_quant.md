# StockArithm Lab Report: 374 Algos, 1 Winner, 373 Lessons (2026-05-27)

We're running 374 alternative-data signals in live paper trading across 105 tickers. Today's snapshot: SPY returned 10.15% YTD. One algo beat it. The other 373 didn't. That's the honest baseline.

## The Numbers

**Force rank (full-window since seed, ~115 days):**
- Total algos: 374
- Beating SPY: 1
- That one: *Quantified Simple Monthly Rotation* (+5.47% alpha, +15.62% YTD vs. SPY's 10.15%)

The rest range from Baileymol (-1.99% alpha) down to Port Container Volume (-11.08% alpha). The spread is real. Most alternative signals underperform a passive index over this window.

**Rolling 30-day momentum (last month only):**
- Algos beating SPY in the last 30 days: 5 of 375
- Top performer: Simple Monthly Rotation again (15.62% return, 6.19 Sharpe, +10.68% vs. SPY delta)
- Bottom: Chaos Rotation Lab (-0.43% return, -1.49 Sharpe, -5.37% vs. SPY delta)

This is the critical divergence. VIX Fear Rotation ranks 370th all-time but 3rd in the last month (+6.53% rolling return). Biscotti and Lumber Momentum show similar gaps. **This matters:** a signal dead in full-window analysis can spike on recent data. We report both rankings because neither tells the complete story alone.

## Data Sources & Methodology

The lab ingests FRED macroeconomic releases, TSA travel data, Reddit sentiment, job posting acceleration (alternative labor market proxy), retail sales momentum, port container volume, VIX term structure, and Google Trends searches. Each signal is backtested, then run live in paper trading with equal-weight position sizing across the 105-ticker universe.

We separate "normal" algos (momentum rotations, dual-momentum frameworks) from "crazy" algos (alternative data experiments). Both are ranked transparently. The crazy category includes the outliers—some outperform, most crater.

## The Honest Critique

**Sample size:** 115 days is not statistically significant. One algo beating SPY over four months could be luck. We need 2–3 years minimum to distinguish signal from noise. We know this. We're publishing anyway because the methodology—not the returns—is the point.

**Survivorship bias:** We're not hiding dead signals. Failures appear on the leaderboard. Chaos Rotation Lab is down 6.66% YTD and ranked 374th. It stays live.

**Sector consensus:** Today's call is bearish across all major sectors (Industrials 21% bullish, Tech 17%, Utilities 14%). The algos agree the market is overextended. SPY disagrees.

## Why This Matters

The lab's differentiator is **public failure**. We don't cherry-pick winners or rebrand losers. You see the full distribution: one winner, 373 experiments in progress. That's the edge—transparency, not returns.

Methodology and full leaderboard at stockarithm.com.