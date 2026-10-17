# -*- coding: utf-8 -*-
"""
DragnaCarta Curse of Strahd: Reloaded Parser
Parses top-level scenes (# Code. and ## Code.) with all their internal subsections.
"""
import os
import re
import html

def clean_html(raw_html):
    text = re.sub(r'</p>\s*<p>', '\n\n', raw_html)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    return html.unescape(text).strip()

def parse_reloaded_file(file_path):
    content = open(file_path, 'r', encoding='utf-8').read()
    # Match # Code. or ## Code. (where Code is A1, A2a, B5c, etc.)
    pattern = r'^(#{1,2}\s+([A-Z0-9]+[a-z]?)\.\s+([^\n]+))'
    matches = list(re.finditer(pattern, content, re.MULTILINE))
    
    scenes = {}
    for i, m in enumerate(matches):
        code = m.group(2)
        title = m.group(3).strip()
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(content)
        sec_text = content[start:end].strip()
        
        raw_descs = re.findall(r'<div class=["\']?description["\']?[^>]*>([\s\S]*?)</div>', sec_text)
        descs = [clean_html(d) for d in raw_descs]
        
        scenes[code] = {
            'title': title,
            'full_text': sec_text,
            'descriptions': descs,
            'file_path': file_path
        }
    return scenes

if __name__ == '__main__':
    arc_a = parse_reloaded_file('reloaded-source/Act I - Into the Mists/Arc A - Escape From Death House.md')
    print("Arc A parsed scenes:")
    for c, data in arc_a.items():
        print(f"  {c}: {data['title']} (len {len(data['full_text'])}, descriptions: {len(data['descriptions'])})")

    arc_b = parse_reloaded_file('reloaded-source/Act I - Into the Mists/Arc B - Welcome to Barovia.md')
    print("\nArc B parsed scenes:")
    for c, data in arc_b.items():
        print(f"  {c}: {data['title']} (len {len(data['full_text'])}, descriptions: {len(data['descriptions'])})")
