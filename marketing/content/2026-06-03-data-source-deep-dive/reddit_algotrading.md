I run 385 signals across 105 tickers. One is beating SPY. The other 384 are not.

That's the honest starting point. And it's why I keep a public leaderboard—because when you're testing alternative data sources, the failure rate is the real story.

**The Winner: Quantified Simple Monthly Rotation**

It's up 16.65% YTD versus SPY's 11.49%. Over the last 30 days, it returned 14.83% while SPY returned 5.79%. Sharpe of 4.62 on the rolling window. It's a sector rotation model—nothing exotic. It ranks sectors by momentum and rebalances monthly. The methodology is transparent. The results are real.

**The Losers: Alternative Data That Doesn't Work**

Here's where it gets interesting. I tested signals built on:

- **Retail Sales Momentum**: -5.92% alpha. Ranked 5th overall but still underwater.
- **FINRA Dark Pool Signal**: -14.19% alpha. The theory was sound—dark pool volume should predict institutional moves. It doesn't, at least not in this regime.
- **Liquor Store Leading Indicator**: -14.63% alpha. Consumer discretionary spending as a recession proxy. Failed hard.
- **Electricity Consumption**: -18.23% alpha. Lowest rank of all 385. Economic activity proxy that lagged.
- **Consumer Sentiment**: -13.9% alpha. You'd think survey data would correlate with market direction. It doesn't.

**Why Keep Them Public?**

Because the alternative is survivorship bias. If I only published the one winner, you'd think alternative data sources work. They mostly don't. The signal-to-noise ratio is brutal.

The divergences are worth noting too. Algo Biscotti ranks 16th over the last 30 days but 380th overall. That's a 364-rank gap. It means recent performance is decoupled from long-term performance. That's a red flag for curve-fitting or regime-dependent edge.

**What This Tells You**

1. **Most alternative data is noise.** Retail sales, dark pools, electricity usage, consumer sentiment—they sound logical. They fail in live trading.

2. **Simple beats complex.** Monthly sector rotation outperforms everything. No alternative data required. No machine learning. No exotic sources.

3. **Failure visibility matters.** If you're building a trading system, you need to see what doesn't work. The 384 losers teach you more than the 1 winner.

4. **Regime matters.** A signal that works for 30 days might not work for 119 days. The Biscotti divergence shows that recent strength doesn't predict forward returns.

The full board is live. Every signal. Every failure. Every rank. No cherry-picking. That's the only way to know if your edge is real or if you're just looking at noise.

---
