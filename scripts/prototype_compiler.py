# -*- coding: utf-8 -*-
import re
import html

# Test translation dictionary of key RPG terms
TERM_MAP = [
    (r'\bDC\s+(\d+)\s+Wisdom\s*\((?:Perception|Insight|Survival|Animal Handling|Medicine)\)', r'Instinto (CD \1)'),
    (r'\bDC\s+(\d+)\s+Charisma\s*\((?:Persuasion|Deception|Intimidation|Performance)\)', r'Presença (CD \1)'),
    (r'\bDC\s+(\d+)\s+Intelligence\s*\((?:Investigation|History|Arcana|Religion|Nature)\)', r'Conhecimento (CD \1)'),
    (r'\bDC\s+(\d+)\s+Dexterity\s*\((?:Stealth|Sleight of Hand)\)', r'Finesse (CD \1)'),
    (r'\bDC\s+(\d+)\s+Dexterity\s*\((?:Acrobatics)\)', r'Agilidade (CD \1)'),
    (r'\bDC\s+(\d+)\s+Strength\s*\((?:Athletics)\)', r'Força (CD \1)'),
    (r'\bDC\s+(\d+)\s+Constitution\s*(?:saving throw|check)?', r'Força (CD \1)'),
    (r'\bWisdom\s*\((?:Perception|Insight|Survival)\)\s*check', r'teste de Instinto'),
    (r'\bCharisma\s*\((?:Persuasion|Deception|Intimidation)\)\s*check', r'teste de Presença'),
    (r'\bIntelligence\s*\((?:Investigation|History|Arcana|Religion)\)\s*check', r'teste de Conhecimento'),
    (r'\bDexterity\s*\((?:Stealth|Sleight of Hand)\)\s*check', r'teste de Finesse'),
    (r'\bStrength\s*\((?:Athletics)\)\s*check', r'teste de Força'),
]

def clean_html_tags(text):
    text = re.sub(r'</?(?:p|div|span|em|strong|hr)[^>]*>', ' ', text)
    text = html.unescape(text)
    return ' '.join(text.split())

def test_scene():
    from extract_all_slices import scene_slices
    from verify_all_matches import arc_files
    import json
    data = json.load(open('data/campaign_data.json', encoding='utf-8'))
    s = [x for x in data['scenes'] if x['code'] == 'D2'][0]
    slice_text = scene_slices['D2']
    print("D2 slice preview:")
    print(slice_text[:500])
    print("---")
    descs = re.findall(r'<div class="description">([\s\S]*?)</div>', slice_text)
    for i, d in enumerate(descs):
        print(f"Desc {i+1}: {clean_html_tags(d)[:200]}")

if __name__ == '__main__':
    test_scene()
