# Adapter Incubator Architecture

## Purpose

The adapter incubator exists to keep new adapter work separate from the main StockArithm signal board.

New adapters are infrastructure risk. A bad adapter can create:

- fetch instability
- schema drift
- fake historical depth
- weak or duplicated algos
- nightly pipeline noise

The incubator solves that by creating a parallel path where new adapters and the first algos built on them can be tested before they are allowed onto the main crazy board.

The main board should only contain signals built on proven adapter families.

## Core Rule

```text
No algo that depends on a newly introduced adapter should enter the main crazy board until the adapter and the first algos built on it pass a separate incubator review.
```

## Pipeline Stages

### 1. Proposed Adapter

Source:

- `data/adapters/proposed/YYYY-MM-DD/*.json`

These files are written when the final publish gate decides:

- the idea is interesting enough to keep
- the current adapter set is not sufficient
- the spec should not be built directly into the main factory

Proposal files should answer:

- what the idea is
- what source it needs
- why the current adapters are not enough
- what data contract is probably required

This is a queue, not a build surface.

### 2. Adapter Review

This is a human/operator review stage.

Decision options:

- `approved_for_build`
- `defer`
- `reject`

A reviewed proposal should move into something like:

- `data/adapters/reviewed/YYYY-MM-DD/*.json`

Optional fields to add during review:

- `review_status`
- `review_notes`
- `priority`
- `candidate_adapter_name`
- `why_this_source_is_different`

The point of this stage is to stop every interesting idea from immediately becoming infrastructure work.

### 3. Adapter Build

Once approved, the adapter is implemented in:

- `crazy/adapters/<adapter_name>.py`

Use:

- `crazy/adapters/_template.py`
- `crazy/adapters/ADAPTER_RULES.md`

Minimum adapter acceptance before any algo is built:

- function returns the standard adapter envelope
- missing credentials return empty safely
- bad HTTP returns empty safely
- schema is stable enough to inspect
- sample output is understandable
- date field is normalized
- the adapter does not break the pipeline on import

At this point, the adapter exists but is still considered incubating.

## Incubator Surface

### 4. Incubator Algo Build

The first algos that use a newly built adapter should go into a separate location.

Recommended path:

- `crazy/incubator/algos/`

Alternative if you want stricter separation:

- `incubator/algos/`

Recommended companion state/output paths:

- `data/crazy_incubator/state/`
- `reports/crazy_incubator/`
- `docs/incubator/` only if you later want public visibility

These algos should not:

- enter `data/algos_registry_crazy.txt`
- enter the main force-rank board
- enter the public leaderboard
- affect the main signal count

The incubator track is a proving ground, not a production surface.

### 5. Incubator Run

Create a dedicated workflow for incubator algos.

Recommended workflow name:

- `adapter_incubator_daily.yml`

Recommended job stages:

1. discover incubator algos
2. run adapter smoke checks
3. run seed viability checks
4. run narrow validation / first backtest
5. write incubator reports
6. do not publish to the main public board

Recommended outputs:

- `reports/crazy_incubator/YYYY-MM-DD/*.json`
- `reports/crazy_incubator/YYYY-MM-DD/*.md`
- optional summary index:
  - `reports/crazy_incubator/latest.json`
  - `reports/crazy_incubator/latest.md`

## Validation Rules

The incubator must test two different things separately:

1. adapter quality
2. algo quality

### Adapter Quality Checks

Required checks:

- data fetch succeeds consistently
- schema is stable
- historical depth is honest
- cadence matches the spec
- missing / stale data is handled safely
- no repeated runtime failures across several runs

Suggested adapter result states:

- `stable`
- `unstable`
- `insufficient_history`
- `schema_unstable`
- `credential_blocked`

### Algo Quality Checks

Required checks:

- algo seeds successfully
- algo runs without structural errors
- signal behavior is not obviously nonsensical
- basic backtest or seed path is coherent
- result does not look like a thin restatement of an existing algo family

Suggested algo result states:

- `incubating`
- `candidate_for_promotion`
- `redundant`
- `failed_validation`
- `needs_more_history`

## Promotion Gate

### 6. Graduation Review

An adapter and at least one incubator algo can only graduate if all of the following are true:

- adapter fetch is reliable
- schema has been stable across repeated runs
- historical depth is sufficient for honest validation
- the incubator algo seeds and runs cleanly
- the algo is not obviously duplicative or fake
- the workflow does not introduce nightly fragility

When promoted:

- the algo moves into the main crazy path
- the algo is registered in the main crazy registry
- the next normal crazy run can include it
- the public board can absorb it on the next daily cycle

When rejected:

- keep the adapter proposal history
- optionally keep the adapter if it may support future ideas
- mark the algo or adapter as rejected/deferred in the incubator report

## File Layout Proposal

### Proposed Queue

- `data/adapters/proposed/YYYY-MM-DD/*.json`
- `data/adapters/reviewed/YYYY-MM-DD/*.json`

### Adapter Code

- `crazy/adapters/_template.py`
- `crazy/adapters/<adapter_name>.py`

### Incubator Algo Layer

- `crazy/incubator/algos/*.py`
- `data/crazy_incubator/state/*.json`
- `reports/crazy_incubator/YYYY-MM-DD/*.json`
- `reports/crazy_incubator/YYYY-MM-DD/*.md`

### Optional Public Layer Later

- `docs/incubator/index.html`
- `docs/incubator/*.html`

Do not build the public layer first. Keep the incubator private until the workflow is operationally boring.

## Workflow Proposal

### Workflow A: Adapter Proposal Review

Purpose:

- review new adapter requests
- decide whether they deserve infrastructure work

Suggested outputs:

- reviewed proposal JSON
- operator notes

### Workflow B: Adapter Build Verification

Purpose:

- validate a newly coded adapter before any algo generation depends on it

Checks:

- import safety
- sample fetch
- schema check
- historical depth check

### Workflow C: Adapter Incubator Daily

Purpose:

- run incubator algos only
- keep them out of the main board

Suggested cadence:

- daily after market close
- or manual until stable

### Workflow D: Promotion Review

Purpose:

- evaluate whether an incubator adapter/algo pair can move into production

Suggested outputs:

- `promote`
- `hold`
- `reject`

## Separation Rules

These rules are important:

- incubator algos must not change the main signal count
- incubator algos must not appear on the public leaderboard
- incubator failures must not degrade trust in the main board
- adapter experiments must not silently enter the main crazy registry

The main board is the production lab.
The incubator is the infrastructure proving ground.

## Why This Is Worth Doing

Without this separation, adapter work and signal work get mixed together.
That makes it hard to answer:

- is this a bad signal?
- or is this a bad adapter?
- or is this only a noisy first implementation?

The incubator gives you a clean place to answer that before the main board absorbs the risk.

## Recommended Starting Scope

Start with the smallest version:

1. proposed adapter queue
2. reviewed adapter queue
3. incubator algo directory
4. incubator state directory
5. one private incubator report
6. explicit promotion step

Do not build a public incubator site first.
Do not merge incubator results into the main board automatically.
