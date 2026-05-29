# Flat-Fee Signal Clone Permission
Status: Draft
Generated: 2026-05-29 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** Receipts Guy and Signal Hunter find algos they want to run themselves but fear they'll diverge from the lab record, creating confusion. There is no mechanism to let a user fork a signal, keep score against the original, and see if their execution differs.
- **Goal:** Enable users to spawn a paper-trading copy of any public algo, run it in parallel, and compare their results head-to-head against the lab's version to isolate implementation or timing variance.
- **Metric:** Number of clones created per week; % of clones that run for >30 days; paid subscriber retention lift for users who clone vs. don't.

## 2. User Stories

- As a Signal Hunter, I want to clone Baileymol and run it on my own account to see if my execution gets the same results, so I can trust the signal or spot where I'm messing up.
- As a Receipts Guy, I want to see my clone's PnL plotted against the lab's original Baileymol, so I know if the lab is fudging the numbers or if I'm just slower to trade.

## 3. Functional Requirements (The "What")

- **Requirement 1:** Paid subscriber clicks 'Clone' on any public algo; system creates a new algo in their private account with identical parameters, named '[Original]-Clone-[Date]', and starts fresh paper trading.
- **Requirement 2:** Clone runs in parallel: user's portfolio, user's cash, user's trade timing, but identical entry/exit rules. Clone equity curve appears on user's dashboard and can be overlaid against original algo's curve.
- **Requirement 3:** Clones are private by default; user may optionally publish clone results back to leaderboard as a 'comparison run' (shows original algo name + clone name + divergence % side-by-side).

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Clone button lives on the algo detail page, right next to the name. No wizard. No config flow. One click, one new entry in your signals list. The value is transparency: if your clone underperforms the original, you know your broker/timing is the issue, not the signal. If it matches, the signal is repeatable.

## 5. Acceptance Criteria (AC)

- Clone spawns with identical parameters (entry threshold, position size %, exit rule) as original within 5 minutes of user click.
- Clone's first trade executes within 2 market hours of next eligible signal trigger (matches the original algo's timing logic).
- User can view side-by-side equity curves (original vs clone) on a single dashboard tile; divergence % is calculated and displayed (e.g., 'Your clone is -3.2% vs. original').

## 6. Out of Scope

- Automated parameter optimization for clones. User edits parameters manually if they want to test variations.
- Syncing live market data to user clones from a live-trading account. Paper trading only.
