#!/usr/bin/env python3
"""Fetch recent Apple App Store reviews via the public iTunes RSS JSON feed. Read-only research helper.

Usage:
  python3 scripts/app_reviews.py --find "quickbooks"            # look up app ids by name
  python3 scripts/app_reviews.py 1232780281 --max-stars 3 --pages 3
Output per review: date | stars | title | text (truncated) | app URL
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "idea-research/1.0 (read-only)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def find(term, country):
    q = urllib.parse.urlencode({"term": term, "entity": "software", "country": country, "limit": 10})
    d = get(f"https://itunes.apple.com/search?{q}")
    for r in d.get("results", []):
        print(f"{r.get('trackId')} | {r.get('trackName')} | {r.get('sellerName')} | rating {r.get('averageUserRating')} ({r.get('userRatingCount')}) | {r.get('trackViewUrl')}")


def reviews(app_id, country, pages, max_stars, max_chars):
    app_url = f"https://apps.apple.com/{country}/app/id{app_id}"
    for p in range(1, pages + 1):
        url = f"https://itunes.apple.com/{country}/rss/customerreviews/page={p}/id={app_id}/sortby=mostrecent/json"
        try:
            d = get(url)
        except Exception as e:  # noqa: BLE001
            print(f"# page {p} failed: {e}")
            break
        entries = d.get("feed", {}).get("entry", [])
        if isinstance(entries, dict):
            entries = [entries]
        for e in entries:
            if "im:rating" not in e:
                continue
            stars = int(e["im:rating"]["label"])
            if stars > max_stars:
                continue
            text = e.get("content", {}).get("label", "").replace("\n", " ")
            if max_chars and len(text) > max_chars:
                text = text[:max_chars] + " [...]"
            print(f"--- {e.get('updated', {}).get('label', '')[:10]} | {stars}* | {e.get('title', {}).get('label', '')} | {app_url}")
            print(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("app_id", nargs="?")
    ap.add_argument("--find", default="")
    ap.add_argument("--country", default="us")
    ap.add_argument("--pages", type=int, default=2)
    ap.add_argument("--max-stars", type=int, default=3)
    ap.add_argument("--max-chars", type=int, default=500)
    a = ap.parse_args()
    if a.find:
        find(a.find, a.country)
    elif a.app_id:
        reviews(a.app_id, a.country, a.pages, a.max_stars, a.max_chars)
    else:
        ap.print_help()


if __name__ == "__main__":
    sys.exit(main())
