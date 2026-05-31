We've been running 374 sector-rotation signals in public since early 2026. One is beating SPY. The other 373 are not. This post is about why that matters less than you'd think, and what the failures actually teach us.

**The Setup**

Each signal is a rule: rotate into sectors when condition X fires. Some are standard (Faber momentum, simple monthly rebalance). Most are experimental—job posting acceleration, retail sales momentum, dark pool flow, consumer sentiment, liquor store foot traffic. We backtest nothing. We paper-trade everything. We publish wins and losses equally.

As of May 29, 2026:
- 374 signals ranked by full-window alpha
- 1 beating SPY: "Quantified Simple Monthly Rotation" (+12.42% YTD vs SPY +11.03%)
- 373 underperforming
- Sample: 117 days live for most signals

**The Regime Mismatch Problem**

Here's where it gets interesting. Over the last 30 days, 4 signals beat SPY. Over the full window, only 1 does. The gap reveals regime mismatch.

Take "Chaos Rotation Lab" (Baileymol): ranked 374th overall (−6.59% YTD), but ranked 15th in the last 30 days (+0.23% vs SPY +6.31%). A 359-rank gap. Same signal. Different regime.

Or "Algo Biscotti": ranked 366th full-window (−1.13% YTD), but 11th in rolling 30D (+1.40% vs SPY). A 355-rank gap.

These aren't glitches. They're evidence that a signal's edge is regime-dependent. A rule that works in low-volatility consolidation may fail in trending markets. A contrarian signal may shine when mean reversion dominates, then crater when momentum takes over.

**What This Means for Sample Size**

117 days is not enough to separate signal from noise. We know this. But the regime-mismatch pattern is *visible* in the data right now. The signals that ranked worst full-window are often the ones performing best in the current 30-day window. That's not recovery—that's regime rotation.

If we'd stopped this experiment at day 60, we'd have crowned different winners. At day 90, different again. At day 117, we have one clear leader. But that leader (simple monthly rotation) is also the most regime-agnostic: it just rebalances on a calendar. It doesn't bet on sentiment, job postings, or dark pool flow.

**The Honest Part**

373 signals are failing. Most of them have real logic behind them. Retail sales should correlate with consumer discretionary. Job postings should lead hiring. Dark pool volume should signal institutional intent. On paper, these make sense.

But the market doesn't care about paper logic. It cares about regime. And we don't have enough data to know which regime we're in, or when it will flip.

The one signal beating SPY isn't beating it because it's smarter. It's beating it because it's simple enough to work across multiple regimes. That's not a feature. That's survivorship bias in a 117-day window.

**What We're Actually Testing**

This isn't a strategy showcase. It's a regime-detection lab. The failures are the data. The fact that 359 ranks can separate a signal's full-window performance from its 30-day performance tells us that regime mismatch is real, measurable, and large enough to dominate alpha.

If you're building signals, this should matter to you: your edge might be real. It might just be regime-specific. And you won't know which until you've lived through multiple regimes—which takes longer than 117 days.
