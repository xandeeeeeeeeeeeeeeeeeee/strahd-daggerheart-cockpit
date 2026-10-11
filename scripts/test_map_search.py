# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import re
import pymupdf

# 1. Test DuckDuckGo Image Search (with vqd token)
def search_ddg_images(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    url1 = "https://duckduckgo.com/?q=" + urllib.parse.quote(query) + "&iax=images&ia=images"
    req1 = urllib.request.Request(url1, headers=headers)
    html1 = urllib.request.urlopen(req1, timeout=12).read().decode("utf-8", "ignore")
    m = re.search(r'vqd=([\d-]+)', html1) or re.search(r'"vqd":"([\d-]+)"', html1) or re.search(r"vqd='([\d-]+)'", html1)
    if not m:
        print("No vqd for", query)
        return []
    vqd = m.group(1)
    url2 = f"https://duckduckgo.com/i.js?l=us-en&o=json&q={urllib.parse.quote(query)}&vqd={vqd}&f=,,,&p=1"
    headers["Referer"] = "https://duckduckgo.com/"
    req2 = urllib.request.Request(url2, headers=headers)
    data = json.loads(urllib.request.urlopen(req2, timeout=12).read().decode("utf-8", "ignore"))
    return [
        {"title": r.get("title"), "image": r.get("image"), "width": r.get("width"), "height": r.get("height")}
        for r in data.get("results", [])
    ]

for q in [
    "Curse of Strahd Barovia map high resolution",
    "Curse of Strahd Tser Pool Encampment battlemap",
    "Curse of Strahd Town of Vallaki map",
    "Curse of Strahd St Andral Church battlemap",
]:
    try:
        res = search_ddg_images(q)
        print(f"=== DDG: {q} ({len(res)} results) ===")
        for r in res[:5]:
            print(f"  [{r['width']}x{r['height']}] {r['title']} -> {r['image']}")
    except Exception as e:
        print("DDG error:", e)
