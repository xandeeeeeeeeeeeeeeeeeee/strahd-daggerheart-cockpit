# -*- coding: utf-8 -*-
"""
Inspect DragnaCarta source for Arc A scenes
"""
import re

content = open('reloaded-source/Act I - Into the Mists/Arc A - Escape From Death House.md', 'r', encoding='utf-8').read()

def parse_md_sections(text):
    pattern = r'^(#{1,3}\s+([A-Z0-9]+[a-z]?)\.?\s+([^\n]+))'
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    res = {}
    for i, m in enumerate(matches):
        code = m.group(2)
        title = m.group(3).strip()
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        res[code] = (title, text[start:end].strip())
    return res

sections = parse_md_sections(content)
print(f"Total sections parsed in Arc A: {len(sections)}")
for code, (title, body) in sorted(sections.items()):
    descs = re.findall(r'<div class=["\']?description["\']?[^>]*>([\s\S]*?)</div>', body)
    print(f"Code: {code} | Title: {title} | Len: {len(body)} | Descriptions: {len(descs)}")
