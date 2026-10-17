# -*- coding: utf-8 -*-
"""
DragnaCarta Authentic Content Compiler for Strahd Reloaded Daggerheart Cockpit
Generates bespoke, authentic Portuguese roteiros for all remaining campaign scenes
directly from the cloned DragnaCarta/Curse-of-Strahd-Reloaded repository.
"""

import os
import re
import json
import html

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
JSON_PATH = os.path.join(BASE_DIR, "data", "campaign_data.json")

from verify_all_matches import arc_files, file_texts
from extract_all_slices import scene_slices

def clean_html(text):
    text = re.sub(r'</?(?:p|div|span|em|strong|hr|b|i)[^>]*>', ' ', text)
    text = html.unescape(text)
    return ' '.join(text.split())

# Translation dictionary for common D&D to Daggerheart mechanics
TRANSLATIONS = [
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
    (r'\bhit points\b', 'pontos de vida (PV)'),
    (r'\blong rest\b', 'Descanso Longo'),
    (r'\bshort rest\b', 'Descanso Curto'),
    (r'\bsaving throw\b', 'teste de resistência'),
]

def translate_mechanics(text):
    for pat, rep in TRANSLATIONS:
        text = re.sub(pat, rep, text, flags=re.IGNORECASE)
    # Ensure (CD X) format
    text = re.sub(r'\bCD\s*(\d{1,2})\b(?!\))', r'(CD \1)', text)
    return text

print("DragnaCarta Authentic Content Compiler ready.")
