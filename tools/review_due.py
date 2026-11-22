"""
Which pages are due a content review. Funding, policy and price pages go out of
date fastest, so they're reviewed every six months; method and how-to pages
every year. After reviewing a page (checking every figure against its source),
set its last_reviewed date in tools/review.json.

    python3 tools/review_due.py          # list pages due now or within 30 days
"""
import datetime as dt
import json
from pathlib import Path

REVIEW = Path(__file__).resolve().parent / 'review.json'


def add_months(d, n):
    y, m = divmod(d.month - 1 + n, 12)
    return d.replace(year=d.year + y, month=m + 1, day=min(d.day, 28))


def due(within_days=30, today=None):
    today = today or dt.date.today()
    out = []
    for file, r in json.loads(REVIEW.read_text()).items():
        when = add_months(dt.date.fromisoformat(r['last_reviewed']), r['every_months'])
        if when <= today + dt.timedelta(days=within_days):
            out.append((when, file))
    return sorted(out)


if __name__ == '__main__':
    rows = due()
    print('\n'.join(f'{w.isoformat()}  {f}' for w, f in rows) if rows else 'No pages due a review in the next 30 days.')
