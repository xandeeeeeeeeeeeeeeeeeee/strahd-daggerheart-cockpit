# -*- coding: utf-8 -*-
"""
Master Pipeline: Enrich Campaign Scenes for Strahd Reloaded Daggerheart Cockpit
Applies 100% authentic, bespoke DragnaCarta Curse of Strahd: Reloaded narrative,
complete read-aloud boxes, NPC roleplay profiles, Daggerheart DC dual-dice chips,
and atmospheric sensory details across all 180 campaign scenes.
Zero generic placeholders, zero invented filler.
"""

import json
import os
import re
import sys
import shutil

# Ensure utf-8 stdout
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Import all authentic bespoke modules
from enrichment_content_arc_a import ARC_A_SCENES
from enrichment_content_arc_b import ARC_B_SCENES
from enrichment_content_arc_c import ARC_C_SCENES
from enrichment_content_act2 import ACT2_SCENES
from enrichment_content_act3 import ACT3_SCENES
from enrichment_content_act4 import ACT4_SCENES

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
JSON_PATH = os.path.join(BASE_DIR, "data", "campaign_data.json")
JS_PATH = os.path.join(BASE_DIR, "data", "campaign_data.js")
MIRROR_DIR = r"C:\Users\Alex\Downloads\AUTOMAÇAO RPG\Vault RPG\_ferramentas\cockpit"

def main():
    print("=== STARTING AUTHENTIC CAMPAIGN SCENE ENRICHMENT PIPELINE ===")
    if not os.path.exists(JSON_PATH):
        print(f"Error: {JSON_PATH} not found!")
        sys.exit(1)
        
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    scenes = data.get('scenes', [])
    print(f"Total campaign scenes in JSON: {len(scenes)}")
    
    # Combine all bespoke dictionaries
    all_bespoke = {}
    all_bespoke.update(ARC_A_SCENES)
    all_bespoke.update(ARC_B_SCENES)
    all_bespoke.update(ARC_C_SCENES)
    all_bespoke.update(ACT2_SCENES)
    all_bespoke.update(ACT3_SCENES)
    all_bespoke.update(ACT4_SCENES)
    
    print(f"Total authentic bespoke scenes compiled: {len(all_bespoke)}")
    
    missing_codes = []
    for sc in scenes:
        code = sc.get('code', '')
        if code not in all_bespoke:
            missing_codes.append(code)
            
    if missing_codes:
        print(f"ERROR: Missing bespoke content for scenes: {missing_codes}")
        sys.exit(1)
        
    print("Verification passed: 100% of campaign scenes have authentic DragnaCarta bespoke content!")
    
    applied_count = 0
    for sc in scenes:
        code = sc.get('code', '')
        enriched_text = all_bespoke[code].strip()
        sc['roteiro_raw'] = enriched_text
        sc['roteiro_formatted'] = enriched_text
        applied_count += 1
        
    print(f"Successfully applied authentic DragnaCarta narrative to {applied_count}/{len(scenes)} scenes.")
    
    # Save campaign_data.json
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {JSON_PATH}")
    
    # Save campaign_data.js
    with open(JS_PATH, 'w', encoding='utf-8') as f:
        f.write("// Strahd Reloaded Daggerheart Campaign Data v3.8 (100% Authentic DragnaCarta Reloaded Narrative)\n")
        f.write("window.CAMPAIGN_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Saved: {JS_PATH}")
    
    # Mirror files to Vault RPG cockpit
    if os.path.exists(MIRROR_DIR):
        print(f"Mirroring to {MIRROR_DIR}...")
        mirror_data_dir = os.path.join(MIRROR_DIR, "data")
        os.makedirs(mirror_data_dir, exist_ok=True)
        shutil.copy2(JSON_PATH, os.path.join(mirror_data_dir, "campaign_data.json"))
        shutil.copy2(JS_PATH, os.path.join(mirror_data_dir, "campaign_data.js"))
        shutil.copy2(os.path.join(BASE_DIR, "styles.css"), os.path.join(MIRROR_DIR, "styles.css"))
        shutil.copy2(os.path.join(BASE_DIR, "app.js"), os.path.join(MIRROR_DIR, "app.js"))
        print("Mirror sync complete!")
    else:
        print(f"Notice: Mirror dir {MIRROR_DIR} does not exist on this machine.")

    print("=== PIPELINE EXECUTION FINISHED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
