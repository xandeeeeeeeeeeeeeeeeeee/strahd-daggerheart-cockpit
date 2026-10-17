# -*- coding: utf-8 -*-
import json
import re

from verify_all_matches import arc_files, file_texts

data = json.load(open('data/campaign_data.json', encoding='utf-8'))
scenes = data['scenes']

by_arc = {}
for s in scenes:
    by_arc.setdefault(s['arc_code'], []).append(s)

scene_slices = {}

for arc, scs in by_arc.items():
    text = file_texts[arc]
    # Find position of each scene in text
    positions = []
    for s in scs:
        code = s['code']
        escaped_code = re.escape(code)
        patterns = [
            rf'^#{{1,3}}\s+{escaped_code}\.\s+([^\n]+)',
            rf'^#{{1,3}}\s+{escaped_code}:\s+([^\n]+)',
            rf'^#{{1,3}}\s+{escaped_code}\s+([^\n]+)',
        ]
        if arc == 'EP':
            num = code.replace('EP', '')
            patterns.append(rf'^#{{1,3}}\s+{num}\.\s+([^\n]+)')
            
        pos = None
        for p in patterns:
            m = re.search(p, text, re.MULTILINE)
            if m:
                pos = m.start()
                break
        positions.append((code, pos))
    
    for i, (code, pos) in enumerate(positions):
        next_pos = positions[i+1][1] if i+1 < len(positions) else len(text)
        slice_text = text[pos:next_pos].strip()
        scene_slices[code] = slice_text

print(f"Total slices extracted: {len(scene_slices)}")
# Print length of each arc's slices
for arc, scs in sorted(by_arc.items()):
    total_len = sum(len(scene_slices[s['code']]) for s in scs)
    print(f"  Arc {arc}: {len(scs)} scenes, {total_len} chars total")
