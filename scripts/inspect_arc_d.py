# -*- coding: utf-8 -*-
with open("reloaded-source/Act II - The Shadowed Town/Arc D - St. Andral's Feast.md", encoding='utf-8') as f:
    text = f.read()

import re
scenes_d = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']
for i, c in enumerate(scenes_d):
    pat = rf'^#\s+{c}\.\s+([^\n]+)'
    m = re.search(pat, text, re.MULTILINE)
    next_pat = rf'^#\s+{scenes_d[i+1]}\.\s+' if i+1 < len(scenes_d) else r'\Z'
    m_next = re.search(next_pat, text, re.MULTILINE)
    start = m.start() if m else 0
    end = m_next.start() if m_next else len(text)
    sec = text[start:end]
    title = m.group(1) if m else ""
    descs = re.findall(r'<div class="description">([\s\S]*?)</div>', sec)
    profiles = re.findall(r'> \[!profile\]\+?\s*\*\*Profile:\s*([^\*]+)\*\*', sec)
    print(f"=== {c}: {title} ({len(sec)} chars) ===")
    print(f"   Read-alouds: {len(descs)}, Profiles: {profiles}")
    for d in descs[:2]:
        clean_d = ' '.join(re.sub(r'<[^>]+>', '', d).split())[:120]
        print(f"     Read-aloud: \"{clean_d}...\"")
