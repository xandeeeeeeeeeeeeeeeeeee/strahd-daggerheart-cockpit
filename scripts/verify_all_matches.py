# -*- coding: utf-8 -*-
import json
import re

data = json.load(open('data/campaign_data.json', encoding='utf-8'))
scenes = data['scenes']

arc_files = {
    'A': 'reloaded-source/Act I - Into the Mists/Arc A - Escape From Death House.md',
    'B': 'reloaded-source/Act I - Into the Mists/Arc B - Welcome to Barovia.md',
    'C': 'reloaded-source/Act I - Into the Mists/Arc C - Into the Valley.md',
    'D': "reloaded-source/Act II - The Shadowed Town/Arc D - St. Andral's Feast.md",
    'E': 'reloaded-source/Act II - The Shadowed Town/Arc E - The Missing Vistana.md',
    'F': "reloaded-source/Act II - The Shadowed Town/Arc F - Lady Wachter's Wish.md",
    'G': 'reloaded-source/Act II - The Shadowed Town/Arc G - The Strazni Siblings.md',
    'H': 'reloaded-source/Act II - The Shadowed Town/Arc H - The Lost Soul.md',
    'I': 'reloaded-source/Act II - The Shadowed Town/Arc I - The Walls of Krezk.md',
    'J': 'reloaded-source/Act III - The Broken Land/Arc J - The Stolen Gem.md',
    'K': 'reloaded-source/Act III - The Broken Land/Arc K - The Fallen Abbey.md',
    'L': 'reloaded-source/Act III - The Broken Land/Arc L - The Den of Wolves.md',
    'M': "reloaded-source/Act III - The Broken Land/Arc M - The Dragon's Manor.md",
    'O': 'reloaded-source/Act III - The Broken Land/Arc O - Dinner with the Devil.md',
    'P': 'reloaded-source/Act III - The Broken Land/Arc P - Ravenloft Heist.md',
    'Q': 'reloaded-source/Act III - The Broken Land/Arc Q - A Shining Beacon.md',
    'R': 'reloaded-source/Act IV - Secrets of the Ancient/Arc R - Trials of the Mountain.md',
    'S': 'reloaded-source/Act IV - Secrets of the Ancient/Arc S - A Sword of Sunlight.md',
    'T': 'reloaded-source/Act IV - Secrets of the Ancient/Arc T - The Three Fanes.md',
    'U': 'reloaded-source/Act IV - Secrets of the Ancient/Arc U - Dreams of Dawn.md',
    'EP': 'reloaded-source/Act IV - Secrets of the Ancient/Epilogue.md'
}

file_texts = {a: open(p, encoding='utf-8').read() for a, p in arc_files.items()}

matched = []
missing = []

for s in scenes:
    code = s['code']
    arc = s['arc_code']
    text = file_texts[arc]
    
    # In f-string, {{1,3}} gives regex quantifier {1,3}
    escaped_code = re.escape(code)
    patterns = [
        rf'^#{{1,3}}\s+{escaped_code}\.\s+([^\n]+)',
        rf'^#{{1,3}}\s+{escaped_code}:\s+([^\n]+)',
        rf'^#{{1,3}}\s+{escaped_code}\s+([^\n]+)',
    ]
    if arc == 'EP':
        num = code.replace('EP', '')
        patterns.append(rf'^#{{1,3}}\s+{num}\.\s+([^\n]+)')
    
    found_title = None
    for p in patterns:
        m = re.search(p, text, re.MULTILINE)
        if m:
            found_title = m.group(1).strip()
            break
            
    if found_title:
        matched.append((code, arc, found_title, s['title']))
    else:
        missing.append((code, arc, s['title']))

with open('scripts/matching_report.txt', 'w', encoding='utf-8') as out:
    out.write(f"Total scenes: {len(scenes)}\n")
    out.write(f"Matched: {len(matched)}\n")
    out.write(f"Missing: {len(missing)}\n\n")
    if missing:
        out.write("MISSING SCENES:\n")
        for m in missing:
            out.write(f"  Code: {m[0]} (Arc {m[1]}): {m[2]}\n")
    out.write("\nMATCHED SCENES:\n")
    for m in matched:
        out.write(f"  {m[0]} -> {m[2]} (Campaign: {m[3]})\n")

print(f"DONE. Matched: {len(matched)} / {len(scenes)}, Missing: {len(missing)}")
