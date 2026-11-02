#!/usr/bin/env python3
"""Monthly stats update for stats.ericcoulombe.com.

Reads registry.json, downloads each chart's CSV from GVR Stats Centre's public
share links, checks the numbers, and writes data/<area>.json for the pages.

Safety rules:
- A required chart that fails to download or fails a check blocks the whole
  area: its data file is left exactly as it was (the page keeps last good data).
- An optional chart that fails keeps its previous data (or stays hidden).
- Data may never move backwards (latest month earlier than what's published).
- From the 15th of the month on, benchmark prices must include last month;
  if they don't, the run fails so the owner is alerted.

Exit code 0 = all good; 1 = something needs attention (details printed and
written to status.md for the alert issue).

Usage: update.py [--local DIR]   (DIR holds <csv-id>.csv files, for testing)
"""
import csv, io, json, os, sys, time, datetime, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://statscentre.rebgv.org/infoserv/s-v1/"
MONTHS = {m: i + 1 for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"])}


def fetch(csv_id, local_dir=None):
    if local_dir:
        with open(os.path.join(local_dir, csv_id + ".csv"), encoding="utf-8-sig") as f:
            return f.read()
    last = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(BASE + csv_id, headers={"User-Agent": "Mozilla/5.0 (stats.ericcoulombe.com monthly update)"})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read().decode("utf-8-sig", errors="replace")
        except Exception as e:  # network hiccup: wait and retry
            last = e
            time.sleep(15 * (attempt + 1))
    raise RuntimeError(f"download failed after retries: {last}")


def parse(text):
    """Return (header, rows) where rows = [((year, month), [values...]), ...]."""
    if "Date," not in text:
        snippet = text.strip().splitlines()[0][:120] if text.strip() else "empty response"
        raise ValueError(f"not a data file (GVR said: {snippet})")
    lines = text.replace("\r", "").split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("Date,"))
    header = [h.strip().strip('"') for h in next(csv.reader([lines[start]]))]
    rows = []
    for line in lines[start + 1:]:
        if not line.strip():
            break
        cells = next(csv.reader([line]))
        name, year = cells[0].rsplit(" ", 1)
        vals = []
        for c in cells[1:len(header)]:
            c = c.strip().replace(",", "")
            vals.append(float(c) if c not in ("", "-", "N/A") else None)
        rows.append(((int(year), MONTHS[name.strip()]), vals))
    return header, rows


def build_chart(spec, text):
    header, rows = parse(text)
    idx = []
    for col in spec["cols"]:
        if col not in header:
            raise ValueError(f"column '{col}' missing (file has {header[1:]})")
        idx.append(header.index(col) - 1)
    if len(rows) < 12:
        raise ValueError(f"only {len(rows)} months of data")
    for (a, _), (b, _) in zip(rows, rows[1:]):
        if (b[0] * 12 + b[1]) - (a[0] * 12 + a[1]) != 1:
            raise ValueError(f"months not consecutive around {a}")
    series = [[r[1][i] if i < len(r[1]) else None for r in rows] for i in idx]
    if spec["kind"] == "pct":  # GVR may give 0.965 or 96.5; store as percent
        series = [[(v * 100 if v is not None and v <= 2 else v) for v in s] for s in series]
    for col, s in zip(spec["cols"], series):
        if s[-1] is None:
            raise ValueError(f"latest month is blank for {col}")
        bad = [v for v in s if v is not None and not (spec["min"] <= v <= spec["max"])]
        if bad:
            raise ValueError(f"{col} has out-of-range values, e.g. {bad[0]}")
    y, m = rows[0][0]
    ly, lm = rows[-1][0]
    nd = lambda v: int(v) if v is not None and float(v).is_integer() else (round(v, 4) if v is not None else None)
    return {"start": f"{y:04d}-{m:02d}", "through": f"{ly:04d}-{lm:02d}",
            "cols": spec["cols"], "series": [[nd(v) for v in s] for s in series]}


def main():
    local_dir = sys.argv[sys.argv.index("--local") + 1] if "--local" in sys.argv else None
    today = datetime.date.today()
    reg = json.load(open(os.path.join(ROOT, "registry.json")))
    problems, notes, changed = [], [], []
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)

    for key, area in reg["areas"].items():
        path = os.path.join(ROOT, "data", key + ".json")
        old = json.load(open(path)) if os.path.exists(path) else {"charts": {}}
        new = {"area": key, "name": area["name"], "full_name": area["full_name"], "charts": {}}
        blocked = False
        for ck, spec in area["charts"].items():
            prev = old.get("charts", {}).get(ck)
            try:
                chart = build_chart(spec, fetch(spec["csv"], local_dir))
                if prev and chart["through"] < prev["through"]:
                    raise ValueError(f"data went backwards ({chart['through']} < published {prev['through']})")
                new["charts"][ck] = chart
            except Exception as e:
                msg = f"{area['name']} / {ck} (share {spec['csv']}): {e}"
                if spec.get("required"):
                    problems.append(msg); blocked = True
                else:
                    notes.append(msg + " — optional chart, " + ("kept last good data" if prev else "hidden on page"))
                    if prev:
                        new["charts"][ck] = prev
        if blocked:
            notes.append(f"{area['name']}: page left unchanged (last good data kept)")
            continue
        hpi = new["charts"].get("hpi")
        if hpi and today.day >= 15:
            ly, lm = map(int, hpi["through"].split("-"))
            want = (today.year * 12 + today.month - 1) - 1  # last calendar month
            if ly * 12 + (lm - 1) < want:
                problems.append(f"{area['name']}: benchmark prices still end {hpi['through']} on {today} — GVR's monthly update hasn't come through")
        if new != old:
            with open(path, "w") as f:
                json.dump(new, f, separators=(",", ":"))
                f.write("\n")
            changed.append(area["name"])

    lines = [f"Stats update {today}", ""]
    lines.append("Updated: " + (", ".join(changed) if changed else "no new data"))
    for p in problems:
        lines.append("PROBLEM: " + p)
    for n in notes:
        lines.append("Note: " + n)
    report = "\n".join(lines)
    print(report)
    with open(os.path.join(ROOT, "status.md"), "w") as f:
        f.write(report.replace("\n", "\n\n") + "\n")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        open(summary, "a").write(report.replace("\n", "\n\n") + "\n")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
