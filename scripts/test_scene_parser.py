# -*- coding: utf-8 -*-
import json
import re

from verify_all_matches import arc_files, file_texts

data = json.load(open('data/campaign_data.json', encoding='utf-8'))
scenes = data['scenes']

# Test on D1, D2, D4, E1, F2
test_codes = ['D1', 'D2', 'D4', 'E1', 'F2']

for sc in scenes:
    code = sc['code']
    if code not in test_codes:
        continue
    arc = sc['arc_code']
    text = file_texts[arc]
    
    # Find slice
    escaped_code = re.escape(code)
    m = re.search(rf'^#{{1,3}}\s+{escaped_code}\.\s+([^\n]+)', text, re.MULTILINE)
    if not m:
        continue
    start = m.start()
    
    # Find next top-level scene
    m_next = re.search(r'\n(?=#{1,2}\s+[A-Z0-9]+[a-z]?\.|\Z)', text[start+1:])
    end = start + 1 + m_next.start() if m_next else len(text)
    slice_text = text[start:end]
    
    descs = re.findall(r'<div class="description">([\s\S]*?)</div>', slice_text)
    profiles = re.findall(r'> \[!profile\]\+?\s*\*\*Profile:\s*([^\*]+)\*\*([\s\S]*?)(?=\n[^\n> ]|\Z)', slice_text)
    dcs = re.findall(r'DC\s+(\d+)\s+([A-Za-z]+(?:\s*\([A-Za-z]+\))?)', slice_text)
    
    print(f"=== {code}: {m.group(1)} ({len(slice_text)} chars) ===")
    print(f"   Read-alouds: {len(descs)}")
    print(f"   Profiles: {[p[0].strip() for p in profiles]}")
    print(f"   DCs: {dcs[:5]}")
