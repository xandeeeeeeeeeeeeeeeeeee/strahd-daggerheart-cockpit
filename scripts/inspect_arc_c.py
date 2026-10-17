# -*- coding: utf-8 -*-
with open('reloaded-source/Act I - Into the Mists/Arc C - Into the Valley.md', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'^# (C\d+)\.\s+([^\n]+)', text, re.MULTILINE))
for i, m in enumerate(matches):
    code = m.group(1)
    title = m.group(2)
    start = m.start()
    end = matches[i+1].start() if i+1 < len(matches) else len(text)
    sub = text[start:end]
    descs = re.findall(r'<div class="description">([\s\S]*?)</div>', sub)
    h2s = re.findall(r'^##\s+([^\n]+)', sub, re.MULTILINE)
    print(f'=== {code}: {title} ===')
    print(f'  Length: {len(sub)} chars, Subheadings: {h2s}')
    print(f'  Read-alouds ({len(descs)}):')
    for d in descs[:3]:
        clean_d = ' '.join(d.strip().split())[:120]
        print(f'    - "{clean_d}..."')
