# StockArithm Lab Report: June 2, 2026 — Sector Rotation Signals Remain Broadly Bearish

The StockArithm paper-trading lab is running 374 sector rotation signals across 105 tickers. As of today, only 1 algorithm is beating SPY on a force-ranked basis—a stark reminder that macro-driven sector rotation is difficult to time, and that publishing failures alongside wins is how systematic testing actually works.

## The Winner: Simple Monthly Rotation

**Quantified Simple Monthly Rotation** leads the lab with +15.21% YTD and +3.87% alpha versus SPY's +11.34%. Over the past 30 days, it returned +13.53%, outpacing the broad market by 7.9 percentage points. The signal is straightforward: rotate monthly into the sector with the highest trailing momentum. No economic leading indicator. No macro thesis. Just disciplined rebalancing. It ranks #1 on both force and rolling 30-day leaderboards, with a 30-day Sharpe of 4.24.

The lesson here is uncomfortable: the simplest approach is winning. That should humble any algo designer claiming economic rationale alone drives outperformance.

## The Consensus: Bearish Across All Sectors

The sector consensus from the lab's 46 precomputed rotation signals is uniformly cautious:

- **Technology (XLK)**: 28% bullish — the "least bearish" sector, but still red
- **Consumer Cyclical (XLY)**: 23% bullish
- **Utilities (XLU)**: 21% bullish
- **Consumer Defensive (XLP)**: 19% bullish
- **Basic Materials (XLB)**: 15% bullish

This is not a market calling for sector rotation into growth or cyclicals. The signals are positioning defensively or staying in cash. Whether that thesis proves correct is an open question—the lab will publish the result either way.

## Notable Failures

**Electricity Consumption** ranks dead last (374th) with -7.25% YTD and -18.59% alpha. The economic rationale was sound: utility demand should lead recession signals. It didn't. **Liquor Store Leading Indicator** sits near the bottom at -3.56% YTD, also failing to predict sector rotation. These aren't hidden; they're published.

## Divergences Worth Watching

Two signals show interesting rank gaps between full-window and recent 30-day performance:

- **Freight/Logistics Google Trends** ranks 357th overall but 15th in the past month, suggesting a recent labor-supply signal in industrials that hasn't yet translated to sustained outperformance.
- **Defensive Sector Price Momentum** ranks 28th overall but 317th in the past 30 days, indicating that the post-tech-crash reversion thesis has stalled.

These divergences hint at regime shifts—the kind that sector rotation strategies must detect in real time or miss entirely.

## The Macro Frame

The lab's thesis is that economic leading indicators (TSA checkpoints, jobless claims, consumer sentiment, freight trends) should predict sector rotation before price momentum does. The data so far suggests: sometimes yes, often no. Simple monthly momentum is winning. Sophisticated macro signals are losing. That's the kind of honest result that matters.

**Full signal methodology and sector consensus at stockarithm.com.**