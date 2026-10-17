# -*- coding: utf-8 -*-
"""
Map all 180 scenes in campaign_data.json to their exact source in reloaded-source.
"""
import json
import glob
import re

data = json.load(open('data/campaign_data.json', encoding='utf-8'))
scenes = data['scenes']

files = sorted(glob.glob('reloaded-source/**/*.md', recursive=True))

file_sections = {}
for f in files:
    content = open(f, 'r', encoding='utf-8').read()
    pattern = r'^(#{1,3}\s+([A-Za-z0-9]+[a-z]?)\.?\s+([^\n]+))'
    matches = list(re.finditer(pattern, content, re.MULTILINE))
    for i, m in enumerate(matches):
        code = m.group(2)
        title = m.group(3).strip()
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(content)
        sec_text = content[start:end].strip()
        file_sections[code] = (f, title, sec_text)

mapped = {}
unmapped = []
for s in scenes:
    code = s['code']
    if code in file_sections:
        mapped[code] = file_sections[code]
    else:
        unmapped.append(s)

print(f"Total scenes: {len(scenes)}")
print(f"Successfully mapped: {len(mapped)}")
print(f"Unmapped: {len(unmapped)}")
for s in unmapped:
    print(f"  Unmapped: {s['code']} - {s['title']}")
