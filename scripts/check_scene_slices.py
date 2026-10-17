# -*- coding: utf-8 -*-
import json
import re

data = json.load(open('data/campaign_data.json', encoding='utf-8'))
scenes = data['scenes']

try:
    from verify_all_matches import arc_files, file_texts
except ImportError:
    from scripts.verify_all_matches import arc_files, file_texts

# Check each arc's scenes and their slice boundaries
by_arc = {}
for s in scenes:
    by_arc.setdefault(s['arc_code'], []).append(s)

for arc, scs in sorted(by_arc.items()):
    text = file_texts[arc]
    print(f"=== Arc {arc}: {len(scs)} scenes ===")
    
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
    
    # Sort by position to verify ordering
    for i, (code, pos) in enumerate(positions):
        next_pos = positions[i+1][1] if i+1 < len(positions) else len(text)
        length = next_pos - pos if pos is not None else -1
        print(f"  {code}: start={pos}, length={length}")
