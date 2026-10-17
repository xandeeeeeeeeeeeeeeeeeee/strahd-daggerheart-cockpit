# -*- coding: utf-8 -*-
with open('reloaded-source/Act I - Into the Mists/Arc C - Into the Valley.md', encoding='utf-8') as f:
    text = f.read()

import re

for i in range(1, 13):
    code = f"C{i}"
    next_code = f"C{i+1}" if i < 12 else "Design Notes"
    start_m = re.search(rf'^#\s+{code}\.\s+([^\n]+)', text, re.MULTILINE)
    end_m = re.search(rf'^#\s+{next_code}\b', text, re.MULTILINE)
    if start_m and end_m:
        sec = text[start_m.start():end_m.start()]
        title = start_m.group(1)
        descs = re.findall(r'<div class="description">([\s\S]*?)</div>', sec)
        h2s = re.findall(r'^##\s+([^\n]+)', sec, re.MULTILINE)
        print(f"[{code}] {title} ({len(sec)} chars, {len(descs)} descs)")
        print(f"   Sub: {h2s}")
        if descs:
            d_clean = ' '.join(re.sub(r'<[^>]+>', '', descs[0]).split())[:140]
            print(f"   Desc 1: \"{d_clean}...\"")
