# StockArithm Lab Report: 385 Signals Running, Only 1 Beating SPY

We're running 385 algorithmic signals across 105 tickers, and the results are... humbling.

**The Setup**

StockArithm is a public paper-trading lab that tests alternative-data signals as sector rotation triggers. We publish everything—wins and losses—because that's the only way to know if a signal actually works or just got lucky.

Our signals measure things like:
- Economic data (retail sales, job postings, electricity consumption)
- Market structure (VIX term structure, dark pool activity)
- Behavioral proxies (consumer sentiment, liquor store traffic)

Each signal generates a daily trade recommendation. We track them all in real time.

**Today's Snapshot (June 3, 2026)**

SPY is up **11.49%** YTD.

Of 385 signals:
- **1 is beating SPY** (Quantified Simple Monthly Rotation, +16.65% YTD, +5.16% alpha)
- **3 are beating SPY over the last 30 days**
- **382 are underperforming**

The winner? A dead-simple monthly sector rotation model. No exotic data. No complexity. It's been running 119 days and has $116,650 in paper equity (started at $100k).

The losers are brutal. Electricity Consumption is down **-6.74%** YTD (ranked 385th). Consumer Sentiment, FINRA Dark Pool Signal, and Liquor Store Leading Indicator are all down 2–3% while SPY climbs.

**The Interesting Part: Recent vs. Full-Window**

Some signals are tanking long-term but crushing the last 30 days. Algo Biscotti (Unconditional Loyalty) ranks 380th overall but 16th in the last month—a 364-rank gap. Same with Lumber Momentum. This suggests either mean reversion or that recent market conditions favor certain approaches.

VIX-based signals (VIX Fear Rotation, VIX Term Structure) are in the top 3 for the last 30 days, both with Sharpe ratios above 5.5.

**Sector Consensus**

Across all 385 signals, the consensus is **bearish across the board**. Industrials (XLI) has the highest bullish percentage at just 25%. Technology, Utilities, and Consumer Defensive are all below 23%. This is a crowded bearish call—worth noting.

**The Real Takeaway**

Most alternative-data signals are not working right now. The lab publishes this because it matters. One simple model is winning. Everything else is noise or lag.

Everything is public at stockarithm.com.