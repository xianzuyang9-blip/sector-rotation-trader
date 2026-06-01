# StockArithm May 29 Report: Simple Monthly Rotation Leads; Macro Signals Diverge Sharply

The StockArithm lab published 374 signals across 105 tickers on May 29, with a stark bifurcation emerging between systematic monthly rotation and economic leading indicator strategies. While the S&P 500 returned 6.3% over the trailing 30 days, only four of 375 rolling-window algos beat that benchmark—a signal that most macro-driven sector rotation theses are currently out of sync with market momentum.

## The Winner: Simplicity Over Complexity

**Quantified Simple Monthly Rotation** ranks #1 on both force rank and 30-day rolling performance, delivering 12.4% YTD with a 61-basis-point alpha advantage over SPY in the past month. Its 4.1 Sharpe ratio and minimal 4% maximum drawdown suggest the signal is capturing genuine mean reversion or seasonal patterns without excessive volatility. The economic rationale is straightforward: monthly rebalancing across sector baskets, independent of real-time macro data, has outperformed more elaborate leading-indicator frameworks.

This result invites a hard question: *Why are 370+ algos underperforming a simple calendar-based rotation?*

## The Failures: Macro Thesis Breakdown

The bottom performers reveal where economic leading indicators have misfired:

- **Consumer Sentiment** (-12.6% alpha, -1.53% YTD): The thesis that consumer confidence predicts cyclical rotation has collapsed. Sentiment remains elevated in headline data, yet the signal has lagged for months.
- **Liquor Store Leading Indicator** (-13.2% alpha, -2.14% YTD): A proxy for discretionary spending stress, this signal has been consistently wrong. Either the indicator is too noisy, or consumer behavior has decoupled from traditional stress metrics.
- **Misery Rotation** (-7.6% alpha, 30-day): The combination of inflation and unemployment—historically a defensive signal—has offered no protection in a rally-driven market.

The sector consensus reinforces this divergence. Industrials (XLI) shows only 27% bullish signals despite being the highest-conviction call—a BEARISH composite. Consumer Defensive (XLP), Utilities (XLU), and Technology (XLK) all register below 21% bullish, suggesting the lab's algos are collectively defensive while the market remains risk-on.

## Notable Divergence: Recent Strength Masking Longer Decay

Three algos—**Baileymol**, **Biscotti**, and **Biscotti (alt)**—rank in the top 15 over 30 days but bottom 15 on full-window force rank. Baileymol, for instance, sits at #374 overall yet #15 in the past month. This suggests recent mean reversion or tactical positioning that hasn't yet validated the underlying thesis. These are watch-list candidates: either they're catching a genuine inflection, or they're noise.

## The Macro Implication

The lab's public failure rate—with 371 of 375 algos trailing SPY—indicates that economic leading indicators are lagging signal confirmation. Job posting acceleration, retail sales momentum, and VIX-based rotation all underperformed, despite theoretical soundness. The market may be pricing in macro data faster than these signals can react, or the relationships themselves have shifted.

For fundamental analysts, this is a reminder: *leading indicators lead, but they don't always lead profitably.* The simple monthly rotation's dominance suggests that in a strong bull market, mean reversion and seasonal patterns may matter more than real-time economic data.

Full signal methodology and sector consensus at **stockarithm.com**.