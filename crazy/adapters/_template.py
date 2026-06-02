"""
Minimum viable adapter template.

Copy this file to `crazy/adapters/<adapter_name>.py` and replace the marked
placeholders. Keep the contract narrow:

- one public fetch function per file
- return a DataFrame with `date` plus one or more value columns
- return an empty DataFrame on any failure
- keep optional imports inside the function body
"""

import os
from datetime import datetime, timedelta

import pandas as pd


def fetch_template_series(query: str, days_back: int = 30) -> pd.DataFrame:
    """
    Fetch data for one external source and return a standard adapter envelope.

    Required output:
    - `date`: pd.Timestamp
    - one or more lowercase snake_case value columns

    Rules:
    - never raise to the caller
    - return empty DataFrame on missing credentials or any failure
    - sort by date ascending
    """
    api_key = os.getenv("TEMPLATE_API_KEY")
    if not api_key:
        return pd.DataFrame(columns=["date", "value"])

    try:
        import requests

        cutoff = datetime.utcnow().date() - timedelta(days=days_back)
        resp = requests.get(
            "https://api.example.com/data",
            params={"api_key": api_key, "q": query},
            timeout=20,
        )
        resp.raise_for_status()
        payload = resp.json()

        rows = []
        for item in payload:
            raw_date = item.get("date")
            raw_value = item.get("value")
            if raw_date is None or raw_value is None:
                continue
            day = pd.to_datetime(raw_date, errors="coerce")
            if pd.isna(day):
                continue
            if day.date() < cutoff:
                continue
            rows.append(
                {
                    "date": day,
                    "value": raw_value,
                }
            )

        df = pd.DataFrame(rows)
        if df.empty:
            return pd.DataFrame(columns=["date", "value"])

        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])
        if df.empty:
            return pd.DataFrame(columns=["date", "value"])

        return df.sort_values("date").reset_index(drop=True)
    except Exception:
        return pd.DataFrame(columns=["date", "value"])
