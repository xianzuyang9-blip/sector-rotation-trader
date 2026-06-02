# TL;DR Adapter Incubator

## Purpose

New adapters should not go straight onto the main StockArithm board.

A new adapter can fail because of:

- bad data
- unstable schema
- weak historical depth
- duplicated signal logic
- runtime fragility

So new adapters need a separate proving ground first.

## Core Rule

```text
New-adapter algos stay off the main board until the adapter and the first algos built on it pass an incubator review.
```

## Pipeline

1. `proposed`
- `data/adapters/proposed/YYYY-MM-DD/*.json`
- idea looks useful but needs a new adapter

2. `reviewed`
- operator decides build / defer / reject

3. `adapter built`
- code lands in `crazy/adapters/<adapter>.py`
- scaffold starts from `crazy/adapters/_template.py`

4. `incubator algo`
- algo goes into a separate track such as:
  - `crazy/incubator/algos/`
- it does not enter the main crazy registry

5. `incubator run`
- separate daytime workflow
- separate state
- separate reports
- no effect on main leaderboard or signal count

6. `promote or reject`
- only promote if adapter and algo are both stable
- promotion is a separate pipeline from incubation

## Suggested Paths

- `data/adapters/proposed/`
- `data/adapters/reviewed/`
- `crazy/incubator/algos/`
- `data/crazy_incubator/state/`
- `reports/crazy_incubator/`

## Separation Rules

- no incubator algo on the main board
- no incubator algo in public leaderboard counts
- no automatic promotion
- no public incubator surface until the process is boring

## Practical Rule

Each new adapter should usually:

1. prove it is different from existing adapters
2. get 2-3 trial algo expressions
3. handle bad or missing data gracefully
4. send at least one trial algo through codegen / seed / backtest
5. stay in the daytime incubator until a separate promotion review decides it can move to production

## Practical Benefit

This separates two questions:

- is the adapter good?
- is the signal good?

That keeps the main board cleaner and gives you a safer path to expand into new data sources.
