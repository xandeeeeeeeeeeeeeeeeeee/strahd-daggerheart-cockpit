# -*- coding: utf-8 -*-
"""
Generate comprehensive, authentic DragnaCarta content for Act II (Arcs D, E, F, G, H, I).
38 scenes: D1-D6, E1-E8, F1-F5, G1-G4, H1-H9, I1-I6.
"""

import json
import re
import html

# Load campaign data
data = json.load(open('data/campaign_data.json', encoding='utf-8'))
scenes_by_code = {s['code']: s for s in data['scenes']}

# Clean existing body
def get_clean_body(code):
    sc = scenes_by_code.get(code)
    if not sc:
        return ""
    raw = sc.get('roteiro_raw', '')
    # Remove old generic headers if present
    lines = raw.splitlines()
    body_lines = []
    skip = True
    for line in lines:
        if line.startswith('### ') or line.startswith('**Local') or line.startswith('**Mapa') or line.startswith('**Consulta') or line.startswith('**Casa:') or line.startswith('**Entrada:'):
            skip = False
        if not skip:
            body_lines.append(line)
    
    clean_body = '\n'.join(body_lines).strip()
    # Format DCs
    clean_body = re.sub(r'\b(Instinto|Presença|Conhecimento|Agilidade|Força|Finesse)\s+(\d{1,2})\b', r'\1 (CD \2)', clean_body)
    clean_body = re.sub(r'\bCD\s*(\d{1,2})\b(?!\))', r'(CD \1)', clean_body)
    return clean_body

print("Helper ready.")
