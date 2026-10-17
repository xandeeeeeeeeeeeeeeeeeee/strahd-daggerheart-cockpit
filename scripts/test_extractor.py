# -*- coding: utf-8 -*-
import re
import sys

content = open('reloaded-source/Act I - Into the Mists/Arc B - Welcome to Barovia.md', 'r', encoding='utf-8').read()

def extract_sections(content):
    pattern = r'^(#+\s+([A-Z0-9]+[a-z]?)\.?\s+([^\n]+))'
    matches = list(re.finditer(pattern, content, re.MULTILINE))
    sections = {}
    for i, m in enumerate(matches):
        code = m.group(2)
        title = m.group(3).strip()
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(content)
        sec_text = content[start:end].strip()
        sections[code] = (title, sec_text)
    return sections

secs = extract_sections(content)
print('Extracted sections from Arc B:')
for code, (title, text) in sorted(secs.items()):
    descs = re.findall(r'<div class=["\']?description["\']?[^>]*>([\s\S]*?)</div>', text)
    print(f'  {code}: {title} (len {len(text)}, descriptions: {len(descs)})')
