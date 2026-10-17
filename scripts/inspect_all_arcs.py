# -*- coding: utf-8 -*-
import glob
import re

files = sorted(glob.glob('reloaded-source/**/*.md', recursive=True))

for f in files:
    if 'Appendices' in f:
        continue
    content = open(f, encoding='utf-8').read()
    # Match headers
    h1 = re.findall(r'^#\s+([A-Z0-9]+[a-z]?)\.\s+([^\n]+)', content, re.MULTILINE)
    h2 = re.findall(r'^##\s+([A-Z0-9]+[a-z]?|[0-9]+)\.\s+([^\n]+)', content, re.MULTILINE)
    all_h = h1 if h1 else h2
    descs = re.findall(r'<div class="description">', content)
    print(f"{f.split('reloaded-source')[-1]}: {len(all_h)} top scenes, {len(descs)} read-aloud boxes")
    for code, title in all_h[:8]:
        print(f"   [{code}] {title}")
