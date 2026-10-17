# -*- coding: utf-8 -*-
"""
Compiler: Generate 100% Authentic DragnaCarta Enrichments for All 180 Scenes.
Combines:
- Bespoke Arc A (A1..A3a)
- Bespoke Arc B (B1..B8)
- Bespoke Arc C (C1..C12)
- Authentic DragnaCarta extraction for Arcs D through EP (D1..U6, EP1..EP6)
Ensures:
- NO GENERIC PLACEHOLDERS ("Conduzir os eventos de...", "Os heróis encontram-se em um ponto crucial...", "A névoa espessa...")
- Real DragnaCarta read-alouds translated from <div class="description">
- Real DragnaCarta objectives & context
- Location-specific sensory details
- Clickable Daggerheart (CD X) chips
"""

import json
import os
import re
import html
import sys

# Set stdout to utf-8
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from verify_all_matches import arc_files, file_texts
from extract_all_slices import scene_slices
from enrichment_content_arc_a import ARC_A_SCENES
from enrichment_content_arc_b import ARC_B_SCENES
from enrichment_content_arc_c import ARC_C_SCENES

print(f"Arc A: {len(ARC_A_SCENES)} scenes")
print(f"Arc B: {len(ARC_B_SCENES)} scenes")
print(f"Arc C: {len(ARC_C_SCENES)} scenes")
