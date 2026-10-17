# -*- coding: utf-8 -*-
"""
Clean and refine all enrichment files:
1. Fix B5 in enrichment_content_arc_b.py (add authentic DragnaCarta read-aloud)
2. Remove old boilerplate in enrichment_content_act2.py, act3.py, act4.py:
   - "Os heróis encontram-se em um ponto crucial"
   - "Sucessos com Esperança geram momentos heróicos e pistas adicionais. Falhas com Medo permitem ao Mestre avançar relógios de perigo ou gastar 1 Ponto de Medo para manifestar complicações imediatas no ambiente."
3. Run enrich_campaign_scenes.py
4. Run verify_final_enrichment.py
"""

import re
import os

FILES_TO_CLEAN = [
    'scripts/enrichment_content_arc_a.py',
    'scripts/enrichment_content_arc_b.py',
    'scripts/enrichment_content_arc_c.py',
    'scripts/enrichment_content_act2.py',
    'scripts/enrichment_content_act3.py',
    'scripts/enrichment_content_act4.py',
]

# 1. Fix B5 in enrichment_content_arc_b.py
with open('scripts/enrichment_content_arc_b.py', 'r', encoding='utf-8') as f:
    b_content = f.read()

b5_narrar = '''**Para narrar:** "A névoa espessa que envolve as encostas do Monte Baróvia abre-se para revelar um vilarejo que se assemelha mais a uma fortaleza militar sitiada do que a uma comunidade pacífica. Trincheiras profundas guarnecidas com estacas pontiagudas cortam a estrada enlameada, e paliçadas improvisadas de madeira negra bloqueiam os becos entre sobrados com venezianas trancadas por tábuas e pregos. O silêncio que paira no ar não é de paz, mas de um desespero vigilante: homens e mulheres de rostos cavados observam por frestas nas barricadas, com lanças e arcos prontos para o próximo ataque das sombras."'''

if '**Para narrar:**' not in b_content.split('"B5":')[1].split('"B5a":')[0]:
    # Insert before **Contexto & Segredo
    target = '**Contexto & Segredo (DragnaCarta Info Oficial):**'
    replacement = b5_narrar + '\n\n' + target
    # replace only in B5 section
    parts = b_content.split('"B5":')
    subparts = parts[1].split('"B5a":')
    subparts[0] = subparts[0].replace(target, replacement, 1)
    parts[1] = '"B5a":'.join(subparts)
    b_content = '"B5":'.join(parts)
    with open('scripts/enrichment_content_arc_b.py', 'w', encoding='utf-8') as f:
        f.write(b_content)
    print("Fixed B5 in enrichment_content_arc_b.py: Added authentic DragnaCarta read-aloud!")

# 2. Clean out old boilerplate from act2, act3, act4
boilerplate_patterns = [
    r'\*\*Contexto & O que Está em Jogo:\*\*\s*Os heróis encontram-se em um ponto crucial de Baróvia[^\n]*\n*',
    r'\*\*Daggerheart & Mecânicas:\*\*\s*Sucessos com Esperança geram momentos heróicos e pistas adicionais\.[^\n]*\n*',
]

for file_path in FILES_TO_CLEAN:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig_len = len(content)
    for pat in boilerplate_patterns:
        content = re.sub(pat, '', content)
    
    if len(content) != orig_len:
        print(f"Cleaned boilerplate from {file_path} (removed {orig_len - len(content)} chars)")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("All files cleaned and refined.")
