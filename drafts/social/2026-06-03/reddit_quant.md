# StockArithm Lab Report: 2026-06-03 — One Winner in 385 Algos

We're running 385 signals across 105 tickers in live paper trading. Today's snapshot: **1 algo is beating SPY on force rank. 3 are beating it on rolling 30D momentum.** The rest are underwater. This is the point.

## The Numbers

**Force Rank (full-window since seed, 119 days):**
- Quantified Simple Monthly Rotation: +16.65% YTD, +5.16% alpha vs. SPY's +11.49%
- Algo Baileymol (Chaos Monger): +8.16% YTD, -3.33% alpha
- Antonacci Dual Momentum Sector Rotation: +7.41% YTD, -4.08% alpha
- 382 others: negative alpha

**Rolling 30D (last 30 calendar days):**
- Simple Monthly Rotation: +14.83% vs. SPY's +5.79%, Sharpe 4.62
- VIX Fear Rotation: +8.72%, Sharpe 5.56
- VIX Term Structure: +8.70%, Sharpe 5.56
- 383 others: trailing or negative

SPY returned +11.49% YTD. The median algo in this cohort is losing to it. That's not a bug—it's the lab's design. We publish failures as loudly as wins.

## What We're Testing

The signals ingest FRED macroeconomic data (retail sales, job postings, electricity consumption, mortgage rates), TSA passenger flows, Reddit sentiment, FINRA dark pool activity, VIX term structure, and sector rotation mechanics. Some algos are "normal" (momentum, dual-momentum, rebalancing rules). Others are "crazy"—alternative-data experiments that often fail spectacularly.

**Electricity Consumption** is today's failure: -6.74% YTD, ranked 385th. **Consumer Sentiment** and **Liquor Store Leading Indicator** are also deeply negative. These aren't edge cases; they're the majority of the lab.

## The Divergence Signal

Three algos show a notable pattern: **Algo Biscotti** (both variants) and **Lumber Momentum** rank poorly on force (375–380) but rank 15–17 on rolling 30D. A 362–364 rank gap suggests recent regime shift or mean reversion. This is worth watching, but 30 days is not statistically significant. We're flagging it, not endorsing it.

## Sector Consensus

Across 64 Industrials signals, 25% are bullish (16 of 64). Technology: 23% bullish. Utilities, Consumer Defensive, Basic Materials all sub-25%. The composite label is **BEARISH** across all major sectors. This reflects the algos' collective positioning, not a forecast.

## Caveats

- **Sample size:** 119 days of live paper trading is not enough to distinguish skill from luck. A single algo beating 384 others could be noise.
- **Survivorship:** We're showing all 385 signals, including the ones that should probably be retired. That's intentional.
- **Data lag:** FRED releases are monthly; TSA data is 1–2 days behind. Sentiment is real-time but noisy.
- **Two leaderboards:** Force rank rewards consistency over the full window. Rolling 30D captures recent momentum. They often disagree. Both are reported because both matter for different questions.

## The Differentiator

Most quant shops hide their failures. We publish them. You can see which alternative-data sources are actually predictive and which are noise. That's the methodology.

Methodology and full leaderboard at stockarithm.com.