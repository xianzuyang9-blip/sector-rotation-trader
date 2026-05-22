#!/usr/bin/env python3
"""
stockarithm_content_generator.py

Generate dispatcher-ready StockArithm marketing bundles from:
- marketing_schedule.csv
- reports/deep_validation/latest.json (or a dated report)

Output shape:
  marketing/content/YYYY-MM-DD-slug/
    meta.json
    x.md
    medium.md
    substack.md
    substack_note.md
    reddit_algotrading.md
    reddit_investing.md
    reddit_stocks.md
    reddit_quant.md
    reddit_security_analysis.md

Usage:
    python scripts/stockarithm_content_generator.py
    python scripts/stockarithm_content_generator.py --date 2026-05-23
    python scripts/stockarithm_content_generator.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

try:
    import anthropic
except ModuleNotFoundError:  # pragma: no cover - handled at runtime
    anthropic = None

MODEL = os.getenv("ANTHROPIC_MODEL") or "claude-haiku-4-5-20251001"
REPORTS_DIR = Path("reports/deep_validation")
SCHEDULE_FILE = Path("marketing_schedule.csv")
OUTPUT_ROOT = Path("marketing/content")
BRAND = "StockArithm"
DEFAULT_TIME = "09:30"
DEFAULT_TZ = "America/New_York"


def _slugify(value):
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def _load_report(run_date):
    dated = REPORTS_DIR / f"{run_date}.json"
    latest = REPORTS_DIR / "latest.json"
    for path in (dated, latest):
        if path.exists():
            try:
                return json.loads(path.read_text())
            except Exception:
                continue
    return {}


def _build_facts_block(report):
    cf = report.get("content_facts", {})
    ss = report.get("system_state", {})
    fr = report.get("force_rank", {})
    r30 = report.get("rolling_30d", {})
    sc = report.get("sector_consensus", {})

    facts = {
        "report_date": report.get("report_date"),
        "generated_at": report.get("generated_at"),
        "system_state": {
            "total_force_ranked": ss.get("total_force_ranked"),
            "beating_spy_force_rank": ss.get("beating_spy_force_rank"),
            "rolling_30d_algos": ss.get("rolling_30d_algos"),
            "rolling_30d_beating_spy": ss.get("rolling_30d_beating_spy"),
            "signals_generated": ss.get("signals_generated"),
            "tickers_covered": ss.get("tickers_covered"),
        },
        "top_force_ranked": (fr.get("top_10") or [])[:5],
        "bottom_force_ranked": (fr.get("bottom_5") or [])[:3],
        "top_rolling_30d": (r30.get("top_10") or [])[:5],
        "bottom_rolling_30d": (r30.get("bottom_5") or [])[:3],
        "spy_ret_30d": r30.get("spy_ret_30d"),
        "signal_of_day": cf.get("signal_of_day"),
        "failure_of_day": cf.get("failure_of_day"),
        "call_of_day": cf.get("call_of_day"),
        "notable_divergences": (cf.get("notable_divergences") or [])[:3],
        "sector_consensus": (sc.get("sectors_ranked") or [])[:5],
    }
    return json.dumps(facts, indent=2)


def _load_schedule_row(run_date):
    if not SCHEDULE_FILE.exists():
        return None

    with SCHEDULE_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        matches = []
        for row in reader:
            if row.get("date") != run_date:
                continue
            status = (row.get("status") or "").strip().lower()
            if status not in {"scheduled", "ready"}:
                continue
            matches.append(row)

    if not matches:
        return None
    if len(matches) > 1:
        raise RuntimeError(f"multiple schedule rows found for {run_date}")
    return matches[0]


def _split_list(value):
    if not value:
        return []
    parts = re.split(r"[;,]", value)
    return [part.strip() for part in parts if part.strip()]


def _channel_prompt(channel_key, schedule_row):
    title = schedule_row["title"]
    theme = schedule_row["theme"]
    notes = schedule_row.get("notes") or ""

    shared = """\
Hard rules:
- Use ONLY facts present in the JSON data block and schedule row. Do not invent metrics, returns, or causes.
- StockArithm is the brand. Never write "Stockarithm".
- stockarithm.com is the URL. Use it only if it fits the channel.
- Show wins and failures honestly. No hype. No investment advice.
- Keep the tone human, specific, and evidence-based.
"""

    if channel_key == "x":
        return f"""\
You are writing a single X post for StockArithm.

{shared}

Context:
- title: {title}
- theme: {theme}
- notes: {notes}

Write one tweet only, under 280 characters, with one sharp observation and a light CTA.
Return plain text only.
"""

    if channel_key == "medium":
        return f"""\
You are writing a Medium article for StockArithm.

{shared}

Context:
- title: {title}
- theme: {theme}
- notes: {notes}

Write a polished, readable Medium article with a clear title on the first line, 3-5 short sections, and a practical closing. Keep it honest and useful, not marketing copy.
Length: 700-1100 words.
Return markdown only.
"""

    if channel_key == "substack":
        return f"""\
You are writing a Substack post for StockArithm.

{shared}

Context:
- title: {title}
- theme: {theme}
- notes: {notes}

Write the canonical long-form post. Put the title on the first line, then the body. Make it feel like a real analyst's field note with a clear point of view.
Length: 900-1300 words.
Return markdown only.
"""

    if channel_key == "substack_note":
        return f"""\
You are writing a Substack Note for StockArithm.

{shared}

Context:
- title: {title}
- theme: {theme}
- notes: {notes}

Write a short note: 2-4 sentences, sharp and readable, ending with a real question when possible. Keep it discovery-oriented, not salesy.
Return plain text only.
"""

    reddit_prompts = {
        "reddit_algotrading": (
            "r/algotrading",
            "engineers, quant hobbyists, algo traders. Highly skeptical. Lead with methodology and failure rate.",
            400,
        ),
        "reddit_investing": (
            "r/investing",
            "general retail investors. More accessible than r/algotrading. Lead with what the signals measure and how they performed.",
            300,
        ),
        "reddit_stocks": (
            "r/stocks",
            "casual retail stock traders. Numbers first, short, direct, zero jargon.",
            200,
        ),
        "reddit_quant": (
            "r/quant",
            "quants, statisticians, finance academics. Be explicit about sample size limits and methodology.",
            450,
        ),
        "reddit_security_analysis": (
            "r/SecurityAnalysis",
            "fundamental analysts and macro-focused readers. Frame the post around sector-rotation rationale and economic logic.",
            350,
        ),
    }
    if channel_key in reddit_prompts:
        subreddit, audience, length = reddit_prompts[channel_key]
        return f"""\
You are writing a Reddit post for {subreddit} for StockArithm.

{shared}

Audience: {audience}

Context:
- title: {title}
- theme: {theme}
- notes: {notes}

Write a post tailored to the subreddit. Include a title line first, blank line, then body. Mention stockarithm.com unless the channel would obviously reject it.
Length: {length} to 550 words depending on the subreddit.
Return markdown/plain text only.
"""

    raise KeyError(channel_key)


CHANNEL_ORDER = [
    "x",
    "medium",
    "substack",
    "substack_note",
    "reddit_algotrading",
    "reddit_investing",
    "reddit_stocks",
    "reddit_quant",
    "reddit_security_analysis",
]


def _build_meta(run_date, row, bundle_dir, report):
    reddit_targets = _split_list(row.get("reddit_targets"))
    channels = _split_list(row.get("channels"))

    channel_meta = {}
    if "x" in channels:
        channel_meta["x"] = {"status": "ready", "file": "x.md"}
    if "medium" in channels:
        channel_meta["medium"] = {"status": "ready", "file": "medium.md"}
    if "substack" in channels:
        channel_meta["substack"] = {"status": "ready", "file": "substack.md"}
    if "substack_note" in channels:
        channel_meta["substack_note"] = {"status": "ready", "file": "substack_note.md"}
    if "reddit" in channels and reddit_targets:
        channel_meta["reddit"] = {
            "status": "ready",
            "subreddits": [
                {"name": target, "status": "ready", "file": f"reddit_{target}.md"}
                for target in reddit_targets
            ],
        }

    meta = {
        "post_id": f"{run_date}-{row['slug']}",
        "product": "stockarithm",
        "scheduled_date": run_date,
        "scheduled_time": row.get("scheduled_time") or DEFAULT_TIME,
        "timezone": row.get("timezone") or DEFAULT_TZ,
        "status": "ready",
        "title": row.get("title"),
        "slug": row.get("slug"),
        "theme": row.get("theme"),
        "source_report": str((REPORTS_DIR / f"{run_date}.json") if (REPORTS_DIR / f"{run_date}.json").exists() else REPORTS_DIR / "latest.json"),
        "bundle_path": str(bundle_dir),
        "channels": channel_meta,
    }
    return meta


def _lint_draft(text, channel_key):
    if re.search(r"\{[^}]+\}", text):
        raise ValueError(f"{channel_key}: unresolved placeholder found")
    if "Stockarithm" in text:
        raise ValueError(f"{channel_key}: stale brand casing Stockarithm found")
    if channel_key == "x" and len(text) > 280:
        raise ValueError(f"{channel_key}: X draft exceeds 280 characters")
    if channel_key != "substack_note" and "stockarithm.com" not in text.lower():
        raise ValueError(f"{channel_key}: missing stockarithm.com URL")


def _write_channel(client, channel_key, run_date, facts_block, row, bundle_dir):
    prompt = _channel_prompt(channel_key, row)
    user_message = (
        f"Schedule row for {run_date}:\n"
        f"{json.dumps(row, indent=2, sort_keys=True)}\n\n"
        f"Locked facts:\n```json\n{facts_block}\n```\n\n"
        f"Write the draft for {channel_key} now."
    )

    max_tokens = {
        "x": 256,
        "medium": 1400,
        "substack": 1800,
        "substack_note": 512,
        "reddit_algotrading": 1100,
        "reddit_investing": 900,
        "reddit_stocks": 700,
        "reddit_quant": 1300,
        "reddit_security_analysis": 1100,
    }[channel_key]

    message = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        temperature=0,
        system=prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    draft = message.content[0].text.strip()
    _lint_draft(draft, channel_key)

    filename = {
        "x": "x.md",
        "medium": "medium.md",
        "substack": "substack.md",
        "substack_note": "substack_note.md",
        "reddit_algotrading": "reddit_algotrading.md",
        "reddit_investing": "reddit_investing.md",
        "reddit_stocks": "reddit_stocks.md",
        "reddit_quant": "reddit_quant.md",
        "reddit_security_analysis": "reddit_security_analysis.md",
    }[channel_key]
    out_path = bundle_dir / filename
    out_path.write_text(draft + "\n", encoding="utf-8")
    print(f"[stockarithm-content] wrote {out_path}")


def generate(run_date, dry_run=False):
    row = _load_schedule_row(run_date)
    if not row:
        print(f"[stockarithm-content] no scheduled bundle for {run_date}")
        return

    report = _load_report(run_date)
    if not report:
        print(f"[stockarithm-content] no deep validation report found for {run_date}", file=sys.stderr)
        sys.exit(1)

    facts_block = _build_facts_block(report)
    bundle_dir = OUTPUT_ROOT / f"{run_date}-{row['slug']}"
    bundle_dir.mkdir(parents=True, exist_ok=True)
    meta = _build_meta(run_date, row, bundle_dir, report)

    if dry_run:
        print(f"[stockarithm-content] dry-run for {run_date}")
        print(json.dumps(meta, indent=2, sort_keys=True))
        channels = _split_list(row.get("channels"))
        if "reddit" in channels:
            for target in _split_list(row.get("reddit_targets")):
                print(f"  would write: {bundle_dir / f'reddit_{target}.md'}")
        for key in ("x", "medium", "substack", "substack_note"):
            if key in channels:
                print(f"  would write: {bundle_dir / f'{key}.md'}")
        return

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("[stockarithm-content] ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    if anthropic is None:
        print("[stockarithm-content] anthropic module not installed", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    channels = _split_list(row.get("channels"))

    for channel_key in CHANNEL_ORDER:
        if channel_key.startswith("reddit_"):
            if "reddit" not in channels:
                continue
            target = channel_key.replace("reddit_", "")
            if target not in _split_list(row.get("reddit_targets")):
                continue
        else:
            if channel_key not in channels:
                continue
        _write_channel(client, channel_key, run_date, facts_block, row, bundle_dir)

    (bundle_dir / "meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"[stockarithm-content] wrote {bundle_dir / 'meta.json'}")


def main():
    parser = argparse.ArgumentParser(description="Generate dispatcher-ready StockArithm marketing bundles")
    parser.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_date = args.date or date.today().isoformat()
    generate(run_date, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
