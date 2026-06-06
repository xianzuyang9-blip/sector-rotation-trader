#!/usr/bin/env python3
"""
Generate LinkedIn-ready event posts from overnight StockArithm artifacts.

This is intentionally deterministic: it turns locked repo facts into founder-style
drafts without requiring an LLM or inventing performance claims.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
IDEA_RUNS = ROOT / "data" / "ideas" / "runs"
DAILY_SUMMARY = ROOT / "data" / "product" / "daily_summary.json"
OUT_ROOT = ROOT / "drafts" / "linkedin_events"
SITE = "stockarithm.com"


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text())
    except Exception:
        return {}


def _humanize_slug(value: str) -> str:
    value = re.sub(r"[-_]+", " ", value).strip()
    value = re.sub(r"\s+", " ", value)
    words = []
    for word in value.split():
        upper = word.upper()
        if upper in {"rss", "fred", "ev", "cpi", "spy", "xlf", "xlk", "xly", "xlc", "xlu", "xlv", "xle", "xlb"}:
            words.append(upper)
        else:
            words.append(word)
    return " ".join(words)


def _display_adapter(value: str) -> str:
    labels = {
        "google_trends": "Google Trends",
        "rss": "RSS",
        "fred": "FRED",
        "openchargemap": "OpenChargeMap",
    }
    return labels.get(value, _humanize_slug(value))


def _first_heading(path: Path) -> str:
    if not path.exists():
        return ""
    for line in path.read_text(errors="ignore").splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return ""


def _spec_heading(run_date: str, payload: dict[str, Any], idea_id: str) -> str:
    candidates = []
    if payload.get("spec_file"):
        candidates.append(ROOT / str(payload["spec_file"]))
    candidates.extend(
        [
            IDEA_RUNS / run_date / "publish" / f"chatgpt_{idea_id}.md",
            IDEA_RUNS / run_date / "publish" / f"claude_{idea_id}.md",
            IDEA_RUNS / run_date / "completed" / f"chatgpt_{idea_id}.md",
            IDEA_RUNS / run_date / "completed" / f"claude_{idea_id}.md",
        ]
    )
    for path in candidates:
        heading = _first_heading(path)
        if heading:
            return heading
    return ""


def _factory_events(run_date: str) -> list[dict[str, Any]]:
    root = IDEA_RUNS / run_date / "factory_results"
    if not root.exists():
        return []

    events = []
    for path in sorted(root.glob("*.json")):
        if path.name == "summary.json" or path.name.endswith("_template_build.json"):
            continue
        payload = _load_json(path)
        if not payload.get("built") and not payload.get("seeded"):
            continue

        idea_id = str(payload.get("idea_id") or path.stem)
        title = _spec_heading(run_date, payload, idea_id) or _humanize_slug(idea_id)
        events.append(
            {
                "kind": "new_algo",
                "idea_id": idea_id,
                "title": title,
                "adapter": _display_adapter(str(payload.get("adapter") or "unknown")),
                "algo_file": payload.get("algo_file"),
                "backtest_status": payload.get("backtest_status") or "unknown",
                "backtest_reason": payload.get("backtest_reason") or "",
                "report_dir": payload.get("backtest_report_dir") or "",
            }
        )
    return events


def _daily_summary_events(run_date: str) -> list[dict[str, Any]]:
    payload = _load_json(DAILY_SUMMARY)
    if not payload:
        return []

    events: list[dict[str, Any]] = []
    counts = payload.get("counts") or {}
    by_status = payload.get("by_status") or {}
    top_live = payload.get("top_live_ytd") or []
    new_algos = payload.get("new_algos_today") or []

    if counts:
        events.append(
            {
                "kind": "scoreboard",
                "total": counts.get("total"),
                "normal": counts.get("normal"),
                "crazy": counts.get("crazy"),
                "promoted": counts.get("promoted"),
                "watchlist": counts.get("watchlist"),
                "graveyard": counts.get("graveyard"),
                "by_status": by_status,
            }
        )

    if top_live:
        events.append({"kind": "leaderboard", "leaders": top_live[:3]})

    for item in new_algos[:5]:
        events.append({"kind": "new_algo_index", "algo": item})

    return events


def _pick_adapter_events(factory_events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    counts = Counter(str(event.get("adapter") or "unknown") for event in factory_events)
    return [
        {"kind": "adapter_activity", "adapter": adapter, "count": count}
        for adapter, count in sorted(counts.items())
        if adapter != "unknown"
    ]


def _render_new_algo(event: dict[str, Any]) -> str:
    title = event["title"]
    adapter = event["adapter"]
    status = event["backtest_status"]
    reason = event["backtest_reason"]
    public_path = f"https://{SITE}/signals/{event['idea_id']}.html"
    lines = [
        f"Shipped a new StockArithm signal into the lab: {title}.",
        "",
        f"It came through the {adapter} adapter, got seeded into the paper-trading system, and is now tracked with the rest of the public signal board.",
        "",
        f"Backtest gate: {status}.",
    ]
    if reason:
        lines.append(f"Reason: {reason}.")
    lines.extend(
        [
            "",
            "That is the part I want public: not every signal gets a clean historical grade. Some are live-only because the source is non-price data. Those still matter if the question is whether a strange external signal can survive live tracking.",
            "",
            f"Public page: {public_path}",
            "",
            "Not investment advice. This is a public paper-trading lab.",
        ]
    )
    return "\n".join(lines) + "\n"


def _render_adapter(event: dict[str, Any]) -> str:
    adapter = event["adapter"]
    count = int(event["count"])
    noun = "signal" if count == 1 else "signals"
    return (
        f"The {adapter} adapter produced {count} new StockArithm {noun} overnight.\n\n"
        "That is the product motion I want: every adapter is a distribution surface.\n\n"
        "A new data source becomes a new class of signals. A new class of signals becomes a public artifact. "
        "A public artifact becomes something to inspect, criticize, share, or ignore.\n\n"
        f"Everything rolls into the public board at {SITE}. Failures included.\n\n"
        "Not investment advice. Paper-trading lab notes.\n"
    )


def _render_scoreboard(event: dict[str, Any]) -> str:
    by_status = event.get("by_status") or {}
    status_bits = ", ".join(f"{key}: {value}" for key, value in sorted(by_status.items()))
    return (
        f"StockArithm is up to {event.get('total')} tracked algos: {event.get('normal')} normal, {event.get('crazy')} weird.\n\n"
        f"Current status mix: {status_bits}.\n\n"
        "This is the part I think most trading products hide: the messy middle. "
        "Promoted ideas, live-only ideas, weak backtests, parked ideas, failures. All of it stays visible.\n\n"
        "The goal is not to make every signal look smart. The goal is to create enough public evidence that the useful ones become obvious over time.\n\n"
        f"{SITE}\n"
    )


def _render_leaderboard(event: dict[str, Any]) -> str:
    leaders = event.get("leaders") or []
    lines = ["Current top live StockArithm signals:"]
    lines.append("")
    for idx, row in enumerate(leaders, 1):
        name = row.get("name") or row.get("algo_id") or "unknown"
        ytd = row.get("ytd_pct")
        status = row.get("status") or "unknown"
        ytd_text = f"{float(ytd):+.2f}%" if isinstance(ytd, (int, float)) else "n/a"
        lines.append(f"{idx}. {name} - {ytd_text} YTD - {status}")
    lines.extend(
        [
            "",
            "This is not a recommendation list. It is a public scoreboard.",
            "",
            "The interesting question is not which signal looks good today. It is which signals keep surviving after enough days, trades, and ugly marks.",
            "",
            f"Leaderboard: https://{SITE}/leaderboard.html",
        ]
    )
    return "\n".join(lines) + "\n"


def _render_event(event: dict[str, Any]) -> str:
    kind = event.get("kind")
    if kind == "new_algo":
        return _render_new_algo(event)
    if kind == "adapter_activity":
        return _render_adapter(event)
    if kind == "scoreboard":
        return _render_scoreboard(event)
    if kind == "leaderboard":
        return _render_leaderboard(event)
    if kind == "new_algo_index":
        algo = event.get("algo") or {}
        return _render_new_algo(
            {
                "title": algo.get("name") or _humanize_slug(str(algo.get("algo_id") or "new signal")),
                "adapter": algo.get("family") or "unknown",
                "backtest_status": algo.get("backtest_status") or "unknown",
                "backtest_reason": algo.get("backtest_reason") or "",
                "idea_id": algo.get("algo_id") or "signals",
            }
        )
    return ""


def _filename_for(event: dict[str, Any], index: int) -> str:
    kind = str(event.get("kind") or "event")
    seed = str(event.get("idea_id") or event.get("adapter") or kind)
    seed = re.sub(r"[^a-zA-Z0-9]+", "-", seed).strip("-").lower()
    return f"{index:02d}-{kind}-{seed}.md"


def generate(run_date: str, out_root: Path) -> list[Path]:
    factory_events = _factory_events(run_date)
    events = factory_events + _pick_adapter_events(factory_events) + _daily_summary_events(run_date)
    out_dir = out_root / run_date
    out_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    for idx, event in enumerate(events, 1):
        text = _render_event(event).strip() + "\n"
        if not text.strip():
            continue
        path = out_dir / _filename_for(event, idx)
        path.write_text(text)
        written.append(path)

    index = {
        "run_date": run_date,
        "count": len(written),
        "drafts": [str(path.relative_to(ROOT)) for path in written],
    }
    (out_dir / "index.json").write_text(json.dumps(index, indent=2) + "\n")
    return written


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat(), help="Event date YYYY-MM-DD")
    parser.add_argument("--out-dir", default=str(OUT_ROOT))
    args = parser.parse_args()

    written = generate(args.date, Path(args.out_dir))
    print(f"[linkedin-events] wrote {len(written)} drafts for {args.date}")
    for path in written:
        print(f"[linkedin-events] {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
