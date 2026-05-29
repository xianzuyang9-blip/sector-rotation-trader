1 of 374 signals is beating SPY. Here is the full public board.

We've been running 374 sector-rotation signals in paper trading for 116 days. One is ahead of SPY. The rest are behind. I'm posting this because the failure case is the actual finding.

**The numbers:**

- Quantified Simple Monthly Rotation: +17.14% YTD, +6.38% alpha vs SPY's +10.76%
- Faber Momentum Rotation: +8.2% YTD, -2.56% alpha
- Algo Baileymol (Chaos Monger): +8.16% YTD, -2.6% alpha
- 371 others: all negative alpha

Over 30 days, SPY returned 6.03%. The top signal returned 17.14%. But that's one winner across 374 attempts. The median is underwater.

**Why this matters for the methodology:**

The sample is small. 116 days of paper trading is not a track record. One signal beating SPY over four months could be luck, regime fit, or signal quality—we can't separate those yet. The rolling 30-day leaderboard shows different winners (VIX Fear Rotation, VIX Term Structure both outperformed in the last month), which suggests time-dependent performance, not stable alpha.

**The visible failures:**

- FINRA Dark Pool Signal: -0.92% YTD, -11.67% alpha
- Port Container Volume: -0.94% YTD, -11.7% alpha
- Liquor Store Leading Indicator: -1.1% YTD, -11.86% alpha

These are labeled "crazy" signals—experimental, untested, built on thin premises. They're losing. I'm keeping them visible because deleting them would hide the base rate of failure. If you're building a signal lab, expect most signals to fail. The question isn't whether you'll have failures; it's whether you'll admit them.

**Notable divergence:**

Chaos Rotation Lab ranks 374th overall (force rank) but 16th over the last 30 days. That's a 358-rank gap. It's been up +0.8% in the last month while down -6.26% YTD. This is a red flag for overfitting to recent regime or luck. The signal that looks worst on the full window looks decent on the rolling window. That's the kind of pattern that kills live trading.

**What we can't claim:**

- That the one winner will keep winning
- That the methodology is sound (116 days is too short)
- That any signal has genuine edge (no out-of-sample validation yet)
- That sector rotation is the right framework (it's just one approach)

**What we can claim:**

- 374 signals, 1 beating SPY, 373 behind
- The failures are real and documented
- Time-dependent performance is visible in the rolling ranks
- Most experimental signals lose money

The board is public. Every signal, every return, every rank. If you want to audit the math or challenge the signal logic, the data is there.

---
