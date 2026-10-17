# -*- coding: utf-8 -*-
"""
Analyze elements in DragnaCarta's source across all 180 scenes.
"""
import re
from map_scenes_to_source import mapped, scenes

total_descriptions = 0
total_profiles = 0
total_lore = 0

for code, (file_path, title, text) in mapped.items():
    descs = re.findall(r'<div class=["\']?description["\']?[^>]*>([\s\S]*?)</div>', text)
    profiles = re.findall(r'>\s*\[!profile\]', text)
    lore = re.findall(r'>\s*\[!lore\]', text)
    total_descriptions += len(descs)
    total_profiles += len(profiles)
    total_lore += len(lore)

print(f"Across the 174 mapped DragnaCarta scenes:")
print(f"  Total official read-aloud boxes: {total_descriptions}")
print(f"  Total NPC character profiles: {total_profiles}")
print(f"  Total lore background callouts: {total_lore}")
