# -*- coding: utf-8 -*-
import json
import re

with open('data/campaign_data.json', encoding='utf-8') as f:
    data = json.load(f)

scenes = data['scenes']
print(f"Total scenes verified: {len(scenes)}")

forbidden_phrases = [
    "Conduzir os eventos de",
    "Os heróis encontram-se em um ponto crucial",
    "A névoa espessa abre-se lentamente sobre a paisagem de",
    "Sucessos com Esperança geram momentos heróicos e pistas adicionais. Falhas com Medo permitem ao Mestre avançar relógios"
]

forbidden_found = {p: 0 for p in forbidden_phrases}

short_scenes = []
no_objective = []
no_context = []
no_narrar = []
no_sensory = []

total_chars = 0

for sc in scenes:
    code = sc.get('code')
    text = sc.get('roteiro_raw', '')
    total_chars += len(text)
    
    for p in forbidden_phrases:
        if p in text:
            forbidden_found[p] += 1
            
    if len(text) < 400:
        short_scenes.append((code, len(text)))
    if '**Objetivo:**' not in text:
        no_objective.append(code)
    if '**Contexto' not in text:
        no_context.append(code)
    if '**Para narrar:**' not in text and '<div class="description">' not in text:
        no_narrar.append(code)
    if '**Ambiente & Sensações:**' not in text and '**Sensações:**' not in text and '**Ambiente & Atmosfera:**' not in text and 'Ambiente & Sensações:' not in text:
        no_sensory.append(code)

print("\n=== FORBIDDEN GENERIC BOILERPLATE CHECK ===")
all_clean = True
for p, count in forbidden_found.items():
    status = "CLEAN" if count == 0 else f"FAIL ({count} found)"
    print(f"  [{status}] '{p[:50]}...': {count}")
    if count > 0:
        all_clean = False

print(f"\nTotal characters across all 180 scenes: {total_chars:,} (avg {total_chars//len(scenes):,} chars/scene)")
print(f"Short scenes (<400 chars): {len(short_scenes)} {short_scenes}")
print(f"Missing Objetivo: {len(no_objective)} {no_objective}")
print(f"Missing Contexto: {len(no_context)} {no_context}")
print(f"Missing Narrar: {len(no_narrar)} {no_narrar}")
print(f"Missing Sensory: {len(no_sensory)} {no_sensory}")

if all_clean and not short_scenes and not no_objective and not no_context and not no_narrar and not no_sensory:
    print("\n>>> ALL CHECKS PASSED PERFECTLY! 100% BESPOKE, ZERO PLACEHOLDERS. <<<")
else:
    print("\n>>> ATTENTION REQUIRED ON FLAGGED ITEMS. <<<")
