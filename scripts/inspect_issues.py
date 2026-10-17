# -*- coding: utf-8 -*-
with open('scripts/enrichment_content_act3.py', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'("O10":\s*r?"""[\s\S]*?""")', text)
if m:
    print("Found O10:")
    print(m.group(1)[:500])
    print("--- contains ponto crucial? ---")
    print('ponto crucial' in m.group(1))

# Check B5 in scripts/enrichment_content_arc_b.py
with open('scripts/enrichment_content_arc_b.py', encoding='utf-8') as f:
    b_text = f.read()

m_b5 = re.search(r'("B5":\s*r?"""[\s\S]*?""")', b_text)
if m_b5:
    print("\nFound B5:")
    print(m_b5.group(1)[:500])
    print("--- has Para narrar? ---")
    print('**Para narrar:**' in m_b5.group(1))

# Check the 68 DH generic lines
with open('data/campaign_data.json', encoding='utf-8') as f:
    import json
    data = json.load(f)

dh_gen = "Sucessos com Esperança geram momentos heróicos e pistas adicionais. Falhas com Medo permitem ao Mestre avançar relógios"
found_dh = [sc['code'] for sc in data['scenes'] if dh_gen in sc.get('roteiro_raw', '')]
print(f"\nScenes with generic DH line: {len(found_dh)}")
print(found_dh[:15])
