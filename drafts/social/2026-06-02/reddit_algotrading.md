# StockArithm Lab Report: 2026-06-02 — 1 Winner, 373 Losers

## The Setup

We're running **374 signals** across **105 tickers**, all paper-traded from entry to today. Each algo gets ranked two ways:

1. **Force rank** — full-window performance since launch (118 days for most)
2. **Rolling 30D rank** — last 30 days only (SPY returned +5.64% in that window)

Why both? Force rank shows durability. Rolling 30D catches regime shifts. They often disagree, and that disagreement is where the lab gets interesting.

---

## The Failure Rate (Lead With This)

**373 of 374 algos are underperforming SPY on force rank.**

That's a 99.7% failure rate. One algo beats the benchmark. One.

On the rolling 30D leaderboard, it's slightly less grim: **3 of 375 algos** beat SPY in the last month. Still 99.2% underwater.

This is the differentiator. We publish the graveyard.

---

## The One Winner

**Quantified Simple Monthly Rotation** (`simple_monthly`):
- **Force rank alpha:** +3.87% (SPY: +11.34%, algo: +15.21% YTD)
- **30D return:** +13.53% vs SPY's +5.64% (+7.89% delta)
- **Sharpe (30D):** 4.24
- **Max drawdown (30D):** -4.03%
- **Equity:** $115,208 (started at $100k)

118 days running. Consistent. Not flashy, but it's holding rank.

---

## The Divergences Worth Watching

Two algos show interesting rank splits:

**Daily Rise In Freightlogistics Google Trends** (`daily-rise-in-freightlogistics-google-trends-for-truck-drive`):
- Force rank: 357 (bad)
- Rolling 30D rank: 15 (good)
- 30D return: +0.086% (barely positive, but trending right)
- Rank gap: 342 positions

This one woke up recently. Might be signal, might be noise.

**Price Momentum Reversion In Defensive Sectors** (`price-momentum-reversion-in-defensive-sectors-after-tech-cra`):
- Force rank: 28 (decent)
- Rolling 30D rank: 317 (collapsed)
- 30D return: -0.053%
- Rank gap: -289 positions

Worked for months, broke in the last 30 days. Classic regime failure.

---

## Sector Consensus (All Bearish)

Across 374 signals, the sector votes are:
- **Technology (XLK):** 28% bullish (13 of 46 signals)
- **Consumer Cyclical (XLY):** 23% bullish (16 of 69)
- **Utilities (XLU):** 21% bullish (11 of 52)

No sector has majority bullish signals. The lab is hedged or short-biased across the board.

---

## The Basement

**Electricity Consumption** (`electricity-consumption`):
- Force rank: 374 (dead last)
- YTD: -7.25%
- Alpha: -18.59%

**Liquor Store Leading Indicator** (`liquor`):
- Force rank: 370
- YTD: -3.56%
- 30D: -3.54% (max DD: -3.54%)

Some of these are labeled "crazy" — experimental alt-data plays. Some are just broken.

---

## Questions for You

- Why does Simple Monthly Rotation work when 373 others don't? (Survivorship bias? Regime fit? Luck?)
- Are the 30D divergences early warnings or false positives?
- What would make you trust a signal that's 99% underwater?

Full leaderboard at stockarithm.com — all signals public, failures included.